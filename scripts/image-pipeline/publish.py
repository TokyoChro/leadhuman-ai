"""
Cloud Publisher — fetches a draft from Notion, generates an Ivy Boys illustration,
writes the markdown, and notifies via Telegram. Runs entirely in GitHub Actions.

Usage:
  python publish.py                          # Auto-find "Ready" draft in Notion
  python publish.py --slug "my-post" --prompt "scene description"  # Manual override

Required env vars: GOOGLE_API_KEY, NOTION_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
Optional env var: ANTHROPIC_API_KEY (for auto scene prompt generation)
"""

import argparse
import json
import os
import re
import sys
import urllib.parse
from datetime import datetime
from pathlib import Path

import requests

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
CONTENT_DIR = REPO_ROOT / "src" / "content"
IMAGES_DIR = REPO_ROOT / "src" / "assets" / "images" / "posts"

# Notion config
NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "")
NOTION_BASE_URL = "https://api.notion.com/v1"
NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}
LH_CONTENT_VAULT_DB_ID = "fdaa0716068f4318899bb188de1fe816"

# Telegram config
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")


# ─── Notion Helpers ──────────────────────────────────────────────────────────

def notion_query_database(database_id, filter_obj):
    resp = requests.post(
        f"{NOTION_BASE_URL}/databases/{database_id}/query",
        headers=NOTION_HEADERS,
        json={
            "filter": filter_obj,
            "page_size": 1,
            "sorts": [{"timestamp": "created_time", "direction": "descending"}],
        },
    )
    if resp.status_code != 200:
        print(f"Notion query failed: {resp.status_code} {resp.text[:300]}", file=sys.stderr)
        return None
    results = resp.json().get("results", [])
    return results[0] if results else None


def notion_get_page_blocks(page_id):
    blocks = []
    cursor = None
    while True:
        params = {"page_size": 100}
        if cursor:
            params["start_cursor"] = cursor
        resp = requests.get(
            f"{NOTION_BASE_URL}/blocks/{page_id}/children",
            headers=NOTION_HEADERS,
            params=params,
        )
        if resp.status_code != 200:
            print(f"Notion blocks fetch failed: {resp.status_code}", file=sys.stderr)
            return blocks
        data = resp.json()
        blocks.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return blocks


def notion_update_status(page_id, status_name):
    payload = {"properties": {"Status": {"select": {"name": status_name}}}}
    resp = requests.patch(
        f"{NOTION_BASE_URL}/pages/{page_id}",
        headers=NOTION_HEADERS,
        json=payload,
    )
    if resp.status_code != 200:
        print(f"Notion status update failed: {resp.status_code} {resp.text[:200]}", file=sys.stderr)
        return False
    return True


def extract_text(rich_text_array):
    return "".join(item.get("plain_text", "") for item in rich_text_array)


def blocks_to_text(blocks):
    lines = []
    for block in blocks:
        block_type = block.get("type", "")
        block_data = block.get(block_type, {})

        if block_type == "paragraph":
            lines.append(extract_text(block_data.get("rich_text", [])))
        elif block_type == "heading_1":
            lines.append(f"# {extract_text(block_data.get('rich_text', []))}")
        elif block_type == "heading_2":
            lines.append(f"## {extract_text(block_data.get('rich_text', []))}")
        elif block_type == "heading_3":
            lines.append(f"### {extract_text(block_data.get('rich_text', []))}")
        elif block_type == "bulleted_list_item":
            lines.append(f"- {extract_text(block_data.get('rich_text', []))}")
        elif block_type == "numbered_list_item":
            lines.append(f"1. {extract_text(block_data.get('rich_text', []))}")
        elif block_type == "quote":
            lines.append(f"> {extract_text(block_data.get('rich_text', []))}")
        elif block_type == "callout":
            text = extract_text(block_data.get("rich_text", []))
            if text and text[0].isdigit() and ". " in text[:5]:
                num_end = text.index(". ") + 2
                rest = text[num_end:]
                first_period = rest.find(". ")
                if first_period > 0:
                    title_part = rest[: first_period + 1]
                    desc_part = rest[first_period + 2 :]
                    lines.append(f"> **{text[:num_end]}{title_part}** {desc_part}")
                else:
                    lines.append(f"> **{text}**")
            else:
                lines.append(f"> {text}")
        elif block_type == "code":
            text = extract_text(block_data.get("rich_text", []))
            lang = block_data.get("language", "")
            # Skip code blocks that contain frontmatter YAML (injected by remote trigger)
            if text.strip().startswith("---") and "title:" in text:
                continue
            lines.append(f"```{lang}\n{text}\n```")
        elif block_type == "divider":
            lines.append("---")
        elif block_type == "image":
            caption = extract_text(block_data.get("caption", []))
            if caption:
                lines.append(f"![{caption}]")

    return "\n\n".join(lines)


def generate_slug(title):
    slug = title.lower()
    for c in ["'", "\u2019", '"', ":", ".", ",", "?", "!", "(", ")", "&", "\u2018"]:
        slug = slug.replace(c, "")
    slug = slug.replace(" ", "-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


# ─── Fetch Draft ─────────────────────────────────────────────────────────────

def fetch_draft():
    """Find the latest Ready or Drafting article in the LH Content Vault."""
    for status in ("Ready", "Drafting"):
        filter_obj = {
            "and": [
                {"property": "Status", "select": {"equals": status}},
                {"property": "Platform", "select": {"equals": "leadhuman.ai"}},
                {"property": "Content Type", "select": {"equals": "Article"}},
            ]
        }
        page = notion_query_database(LH_CONTENT_VAULT_DB_ID, filter_obj)
        if page:
            break
    else:
        return None

    page_id = page["id"]
    props = page.get("properties", {})

    title = extract_text(props.get("Title", {}).get("title", []))
    if not title:
        return None

    slug = extract_text(props.get("Slug", {}).get("rich_text", []))
    if not slug:
        slug = generate_slug(title)

    tags_prop = props.get("Tags", {}).get("multi_select", [])
    tags = [t.get("name", "") for t in tags_prop] if tags_prop else []

    hub = extract_text(props.get("Hub", {}).get("rich_text", [])) or "/lead/"

    blocks = notion_get_page_blocks(page_id)
    content = blocks_to_text(blocks)

    # Strip frontmatter if present (bare or wrapped in a code fence)
    fm_match = re.search(
        r"^(```\w*\n)?---\n.*?\n---(```)?(\s*\n)?",
        content, re.DOTALL,
    )
    if fm_match:
        article_content = content[fm_match.end() :].strip()
    else:
        article_content = content

    # Strip LinkedIn companion post
    lm = article_content.find("## LinkedIn Companion Post")
    if lm > 0:
        sep = article_content.rfind("---", 0, lm)
        if sep > 10:
            article_content = article_content[:sep].rstrip()
        else:
            article_content = article_content[:lm].rstrip()

    return {
        "page_id": page_id,
        "title": title,
        "slug": slug,
        "tags": tags,
        "hub": hub,
        "article_content": article_content,
    }


# ─── Scene Prompt ────────────────────────────────────────────────────────────

def generate_scene_prompt(title, article_content):
    """Use Claude to generate a scene description for the illustration."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return "A young Japanese-American professional man in a modern Tokyo office setting, looking thoughtful"

    try:
        import anthropic

        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Generate a short scene description (1-2 sentences) for an editorial "
                        f"illustration of a young Japanese-American professional man. The scene "
                        f"should visually represent the theme of this blog post:\n\n"
                        f"Title: {title}\n\n"
                        f"Article excerpt: {article_content[:500]}\n\n"
                        f"The scene should be a warm, everyday setting (office, cafe, park, "
                        f"train station, meeting room, etc.) that metaphorically connects to "
                        f"the article's theme.\n\n"
                        f"IMPORTANT: Do NOT include the article title or any words/text in the "
                        f"scene description. Describe ONLY the visual setting, character posture, "
                        f"and mood. The image generator will render text if you include any.\n\n"
                        f"Just output the scene description, nothing else."
                    ),
                }
            ],
        )
        return response.content[0].text.strip()
    except Exception as e:
        print(f"Claude scene prompt failed: {e}", file=sys.stderr)
        return "A young Japanese-American professional man in a modern Tokyo office setting, looking thoughtful"


# ─── Source Linking ─────────────────────────────────────────────────────────

def link_sources(article_content):
    """Wrap plain-text academic sources with Consensus search links."""
    sources_idx = article_content.find("## Sources")
    if sources_idx < 0:
        return article_content

    before = article_content[:sources_idx]
    sources_section = article_content[sources_idx:]

    lines = sources_section.split("\n")
    result = [lines[0]]  # Keep "## Sources" header

    for line in lines[1:]:
        stripped = line.strip().lstrip("- ")
        # Skip if already linked, empty, or is a divider/header
        if not stripped or "](http" in stripped or stripped.startswith("#") or stripped == "---":
            result.append(line)
            continue

        # Extract paper title (text before the parenthetical author/year info)
        title_match = re.match(r'^(.+?)\s*\(', stripped)
        if title_match:
            paper_title = title_match.group(1).strip().rstrip(',').rstrip('.')
            search_url = f"https://consensus.app/results/?q={urllib.parse.quote(paper_title)}"
            linked = f"- [{stripped}]({search_url})"
            result.append(linked)
        else:
            result.append(line)

    return before + "\n".join(result)


# ─── Japanese Translation ──────────────────────────────────────────────────

def translate_to_japanese(title, description, article_content):
    """Translate the blog post to Japanese using Claude."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("  ANTHROPIC_API_KEY not set, skipping Japanese translation", file=sys.stderr)
        return None

    try:
        import anthropic

        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Translate the following blog post into natural, professional Japanese. "
                        f"This is for a bilingual thought leadership site (leadhuman.ai) written "
                        f"by Jay Vergara, a Canadian living in Tokyo.\n\n"
                        f"RULES:\n"
                        f"- Write in a conversational yet professional Japanese tone\n"
                        f"- Keep the author's voice: reflective, human, slightly self-deprecating\n"
                        f"- Do NOT use hyphens or em dashes anywhere\n"
                        f"- Keep markdown formatting (>, **, ##, links, etc.) exactly as-is\n"
                        f"- Keep all URLs, citation links, and source references unchanged\n"
                        f"- Keep author name as 'Jay Vergara' (do not transliterate)\n"
                        f"- Keep English terms in quotes when they are used as named concepts\n"
                        f"- Statistics and numbers stay as-is\n"
                        f"- The Sources section should keep paper titles in English but add a brief "
                        f"Japanese note for the journal name if helpful\n\n"
                        f"Return your response in this exact format:\n"
                        f"TITLE: [translated title]\n"
                        f"DESCRIPTION: [translated description, max 150 chars]\n"
                        f"BODY:\n[translated article body]\n\n"
                        f"---\n\n"
                        f"TITLE TO TRANSLATE: {title}\n\n"
                        f"DESCRIPTION TO TRANSLATE: {description}\n\n"
                        f"ARTICLE BODY TO TRANSLATE:\n{article_content}"
                    ),
                }
            ],
        )
        result = response.content[0].text.strip()

        # Parse the response
        ja_title = ""
        ja_description = ""
        ja_body = ""

        lines = result.split("\n")
        mode = None
        body_lines = []

        for line in lines:
            if line.startswith("TITLE:"):
                ja_title = line[6:].strip().strip('"')
            elif line.startswith("DESCRIPTION:"):
                ja_description = line[12:].strip().strip('"')
            elif line.startswith("BODY:"):
                mode = "body"
            elif mode == "body":
                body_lines.append(line)

        ja_body = "\n".join(body_lines).strip()

        if not ja_title or not ja_body:
            print("  Translation parse failed: missing title or body", file=sys.stderr)
            return None

        return {
            "title": ja_title,
            "description": ja_description or ja_title,
            "body": ja_body,
        }

    except Exception as e:
        print(f"  Japanese translation failed: {e}", file=sys.stderr)
        return None


# ─── Telegram ────────────────────────────────────────────────────────────────

def send_telegram(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram not configured, skipping notification")
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "Markdown",
            },
        )
    except Exception as e:
        print(f"Telegram send failed: {e}", file=sys.stderr)


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Cloud Publisher for leadhuman.ai")
    parser.add_argument("--slug", help="Post slug (overrides Notion)")
    parser.add_argument("--prompt", help="Scene prompt (overrides auto-generation)")
    parser.add_argument("--vibe", help="Outfit vibe")
    parser.add_argument("--season", help="Season filter")
    parser.add_argument("--skip-image", action="store_true", help="Publish without generating an image")
    args = parser.parse_args()

    # Step 1: Get the draft
    print("=" * 50)
    print("  CLOUD PUBLISHER — leadhuman.ai")
    print("=" * 50)

    print("\n[1/7] Fetching draft from Notion...")
    draft = fetch_draft()
    if not draft:
        print("No drafts found in Notion Content Vault. Nothing to publish.")
        sys.exit(0)

    title = draft["title"]
    slug = args.slug or draft["slug"]
    tags = draft["tags"]
    hub = draft["hub"]
    article_content = draft["article_content"]
    page_id = draft["page_id"]
    hub_path = "build" if hub == "/build/" else "lead"

    print(f"  Title: {title}")
    print(f"  Slug: {slug}")
    print(f"  Hub: /{hub_path}/")
    print(f"  Tags: {tags}")

    # Step 2: Generate image
    has_image = False
    if not args.skip_image:
        print("\n[2/7] Generating scene prompt...")
        scene_prompt = args.prompt or generate_scene_prompt(title, article_content)
        print(f"  Scene: {scene_prompt}")

        print("\n[3/7] Generating Ivy Boys illustration...")
        try:
            from generate import generate

            output_path = generate(scene_prompt, slug, vibe=args.vibe, season=args.season)
            if output_path and Path(output_path).exists():
                has_image = True
                print(f"  Image saved: {output_path}")
            else:
                print("  Image generation returned no file — publishing without image")
        except Exception as e:
            print(f"  Image generation failed: {e} — publishing without image", file=sys.stderr)
    else:
        print("\n[2/7] Skipping image generation (--skip-image)")
        print("[3/7] Skipped")

    # Step 3: Write English markdown
    print("\n[4/7] Writing English markdown...")
    content_path = CONTENT_DIR / hub_path / f"{slug}.md"
    content_path.parent.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    tags_str = json.dumps(tags)
    # Build description from clean article text (strip any leftover code fences/frontmatter)
    desc_text = re.sub(r'^```\w*\n', '', article_content.lstrip())
    desc_text = re.sub(r'^---\n.*?\n---\s*\n?', '', desc_text, flags=re.DOTALL).lstrip()
    desc_text = desc_text.replace("\n", " ").replace('"', "'").strip()
    if len(desc_text) > 150:
        cutoff = desc_text[:150].rfind(". ")
        if cutoff > 80:
            desc_text = desc_text[:cutoff + 1]
        else:
            cutoff = desc_text[:150].rfind(" ")
            desc_text = desc_text[:cutoff] if cutoff > 80 else desc_text[:150]
    description = desc_text.strip()

    image_line = f'\nimage: "../../assets/images/posts/{slug}.png"' if has_image else ""
    frontmatter = (
        f'---\n'
        f'title: "{title}"\n'
        f'description: "{description}"\n'
        f'pubDate: {today}\n'
        f'tags: {tags_str}\n'
        f'author: "Jay Vergara"'
        f'{image_line}\n'
        f'draft: false\n'
        f'---\n\n'
    )
    article_content = link_sources(article_content)
    content_path.write_text(frontmatter + article_content + "\n", encoding="utf-8")
    print(f"  Wrote: {content_path}")

    # Step 4: Translate and write Japanese version
    print("\n[5/7] Translating to Japanese...")
    ja = translate_to_japanese(title, description, article_content)
    if ja:
        ja_hub = f"{hub_path}-ja"
        ja_path = CONTENT_DIR / ja_hub / f"{slug}.md"
        ja_path.parent.mkdir(parents=True, exist_ok=True)

        ja_desc = ja["description"].replace('"', "'").replace("\n", " ").strip()
        ja_frontmatter = (
            f'---\n'
            f'title: "{ja["title"]}"\n'
            f'description: "{ja_desc}"\n'
            f'pubDate: {today}\n'
            f'tags: {tags_str}\n'
            f'author: "Jay Vergara"'
            f'{image_line}\n'
            f'draft: false\n'
            f'---\n\n'
        )
        ja_path.write_text(ja_frontmatter + ja["body"] + "\n", encoding="utf-8")
        print(f"  Wrote JA: {ja_path}")
    else:
        print("  Japanese translation skipped (no API key or translation failed)")

    # Step 5: Update Notion
    print("\n[6/7] Updating Notion status to 'Live'...")
    notion_update_status(page_id, "Live")

    # Step 6: Notify
    url = f"https://leadhuman.ai/{hub_path}/{slug}"
    print(f"\n[7/7] Sending Telegram notification...")
    img_status = "with custom illustration" if has_image else "without image"
    ja_status = " + Japanese" if ja else ""
    send_telegram(
        f"\U0001f4dd *leadhuman.ai Auto-Published*\n\n"
        f"*{title}*\n"
        f"Published {img_status}{ja_status}\n\n"
        f"EN: {url}\n"
        f"JA: https://leadhuman.ai/ja/{hub_path}/{slug}"
    )

    print(f"\n{'=' * 50}")
    print(f"  PUBLISHED: {url}")
    print(f"  JA: https://leadhuman.ai/ja/{hub_path}/{slug}")
    print(f"  Image: {'Yes' if has_image else 'No'}")
    print(f"  Japanese: {'Yes' if ja else 'No'}")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
