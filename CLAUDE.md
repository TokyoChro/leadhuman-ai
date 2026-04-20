# leadhuman.ai Project CLAUDE.md

## Who I Am
I'm Jay Vergara. Partner and Lead Learning Consultant at Peak Potential Consulting (co-founded with Matt Gates, ACC). Based in Tokyo, Japan. Originally from Vancouver, B.C., Canada. Filipino.
Background: L&D professional with experience at Indeed, Rakuten, TELUS, and Yellow Pages. Currently finishing my MBA at GLOBIS University. Languages: English (primary), Japanese (professional).
LinkedIn: linkedin.com/in/vergarajay/

I am NOT an engineer. I'm a content creator and consultant who vibe codes. Explain technical concepts clearly and don't assume I know jargon. When something could break the site, warn me before doing it.

## What This Project Is
leadhuman.ai is my personal thought leadership platform.
Mantra: "Lead humanly. Learn constantly. Build with AI."
Split: 50% AI tutorials (/build/), 50% leadership, cross-cultural, communications, and L&D content (/lead/).

## Tech Stack
This is an Astro (v6.0) site with:
- Tailwind CSS (v4.2) with Vite integration and the typography plugin
- Node.js v22.12.0 or higher
- Deployed to Vercel using the @astrojs/vercel adapter
- Content Collections (content.config.ts) for type safe markdown/MDX authoring
- Dynamic sitemap via @astrojs/sitemap
- RSS feed via @astrojs/rss (src/pages/rss.xml.ts)

## Project Structure
- src/pages/ is file based routing. Top level pages: index.astro, about.astro, connect.astro, videos.astro
- src/pages/build/ and src/pages/lead/ are the two content hubs
- src/layouts/BaseLayout.astro is the main reusable HTML skeleton
- src/components/ has reusable UI components
- src/content/ has the blog/article content (markdown/MDX)
- public/ has static assets (images, icons, fonts)

## Development Rules
- Always run the dev server with `npm run dev` before saying a change works. Verify it builds.
- If you're unsure whether a change will break something, tell me first. Don't just do it.
- Keep the file structure clean. Don't create files outside the existing patterns.
- When creating new pages or blog posts, follow the patterns already established in existing files.
- Commit messages should be clear and descriptive. No generic "update" or "fix" messages.

## Content Pipeline & Automation

This project has a fully automated content pipeline that researches, writes, and publishes blog posts.

### How It Works (Plain English)
The entire pipeline is fully autonomous. Jay's computer does NOT need to be on.

1. Monday and Thursday mornings, a cloud trigger automatically researches trending AI topics, searches for academic papers on Consensus, writes a "Lead Humanly" article, and saves it to the Content Vault in Notion with status "Ready."
2. Every 30 minutes, a GitHub Action (`auto-publish.yml`) checks Notion for "Ready" drafts.
3. When it finds one, it generates an Ivy Boys illustration via Gemini, writes the markdown with image, commits and pushes to GitHub (triggering Vercel deploy), updates Notion to "Live," and sends Jay a Telegram notification.

No manual steps. No Mac required. Jay gets a Telegram ping when the post is live.

### Key Components

**Cloud (runs without Jay's computer — this is the primary path):**
- Remote trigger `trig_01G4wG4UhoH1kjybdoZkuUCp` (Monday 8:03 AM JST)
- Remote trigger `trig_01FmF5MK27E6mCHCGVZKFbTT` (Thursday 8:03 AM JST)
- These do research + writing + Notion. They run on Claude's servers.
- GitHub Action `auto-publish.yml` — checks Notion every 30 min, publishes with image
- GitHub Action `generate-blog-image.yml` — manual trigger for on-demand publish

**Cloud Image Pipeline (in this repo):**
- `scripts/image-pipeline/publish.py` — Full cloud publisher (Notion → image → markdown → commit → notify)
- `scripts/image-pipeline/generate.py` — Gemini-based Ivy Boys illustration generator
- `scripts/image-pipeline/wardrobe.py` — Jay's wardrobe database for outfit variation
- `scripts/image-pipeline/reference/face-reference.png` — Locked face reference for character consistency
- GitHub Secrets required: `GOOGLE_API_KEY`, `NOTION_API_KEY`, `ANTHROPIC_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`

**Local (backup path — only needed if cloud pipeline has issues):**
- Unified Telegram Bridge: `/Users/vergara/Desktop/Antigravity Projects/unified_bridge.py`
  - Runs as a macOS LaunchAgent (auto starts on boot, restarts on crash)
  - Plist: `~/Library/LaunchAgents/com.antigravity.unified-bridge.plist`
  - Logs: `~/Library/Logs/unified-bridge.error.log`
  - Also handles publishing for Peak Potential Consulting
- Local Image Pipeline: `/Users/vergara/Desktop/Antigravity Projects/Image Pipeline/pipeline.py`
  - Generates 4 images locally (higher quality, Jay picks one)
  - `python3 pipeline.py blog --prompt "..." --name "[slug]" --num 4`

**Claude Code Skills:**
- `/leadhuman-pipeline` — Full pipeline: research, write, images, Telegram preview (uses local image gen)
- `/leadhuman-publish` — Publish after Jay approves (backup path)

**Notion:**
- Content Vault database: `collection://f05c6994-f0c4-469b-8787-81ddb22e3952`
- Under Mission Control > Jay Vergara Main Hub
- Status flow: Idea → Drafting → Ready → Live
- Every article gets logged here with research notes, sources, and the full draft

**Telegram:**
- Bot: Master Librarian (`@PeakPotentialPublisher_Bot`)
- Jay's personal chat ID: 8313708098
- Bot token: stored in GitHub Secrets as `TELEGRAM_BOT_TOKEN` (never commit to this file)

### Manual Triggers
```bash
# Trigger cloud publish manually (from GitHub UI):
# GitHub → leadhuman-ai → Actions → "Publish Blog Post" → Run workflow → mode: auto

# Or via API:
curl -X POST "https://api.github.com/repos/TokyoChro/leadhuman-ai/actions/workflows/generate-blog-image.yml/dispatches" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -d '{"ref": "main", "inputs": {"mode": "auto"}}'
```

### Stopping and Starting the Bridge (backup path)
```bash
# Stop
launchctl unload ~/Library/LaunchAgents/com.antigravity.unified-bridge.plist

# Start
launchctl load ~/Library/LaunchAgents/com.antigravity.unified-bridge.plist

# Check if running
launchctl list | grep antigravity.unified

# View logs
tail -f ~/Library/Logs/unified-bridge.error.log
```

## Content Pillars
My content organizes around five pillars. Intersection posts (blending 2+ pillars) outperform single-pillar posts every time.

Japan / Cross-Cultural Business (32%)
HR / L&D / Learning & Development (29%)
AI / Technology / Automation (29%)
Leadership & Management (11%)
Career & Entrepreneurship (7%)

## Voice Rules (Apply to ALL Content I Produce)
These rules are non-negotiable. Every output, every platform, every piece of content on this site.

### NO HYPHENS OR EM DASHES. EVER.
Do not use "-", "--", or "---" anywhere in any output. Not between clauses, not in compound words, not anywhere. Use commas, periods, ellipses, or restructure the sentence. Scan every output character by character before finalizing. This is my #1 pet peeve and an absolute dealbreaker.

### Anti-Staccato Rule
My sentences connect and build. They do not stop and restart in punchy fragments. I stitch ideas together with "and" and "but" the way someone does when thinking out loud. Sentence fragments are fine occasionally for emphasis but should never be the dominant pattern.

The test:

AI rhythm: "Not theory. Things I've actually built and used."
My rhythm: "Not theory but things I've actually built and used."
AI rhythm: "I'm Jay Vergara. Originally from Vancouver, B.C."
My rhythm: "I'm Jay Vergara. I grew up in Vancouver, B.C. and I've been living in Tokyo for over a decade now."

BUT: Short conversational sentences at the end of a post are fine. "It sounds simpler than it is. But it works." is not staccato. It's a natural close. The distinction: staccato chops one connected thought into fragments for artificial impact. A natural close just finishes the thought.

### Anti-AI Rules
I absolutely refuse to sound like an AI. If it could have been written by ChatGPT, it has failed.

NO formulaic structures. "Not only X, but also Y" / "While X, it's important to Y" / "It's worth noting that" are AI tells.
NO perfect parallelism. Break symmetry. Let sentences be uneven.
NO hedging stacks. One hedge is fine. Two is suspicious. Three means rewrite.
NO transition word overuse. "Furthermore," "Moreover," "Additionally," "However" are AI signatures. Use "And" or "But" like a normal person.
NO overly polished prose. Leave some roughness. A "lol" in parentheses, an imperfect sentence, a trailing thought... these are human.
NO summarizing at the end. No "In summary" or restating what was just said.
NO "I hope this helps" / "Feel free to" / "Don't hesitate to." AI tells.
NO "delve" / "landscape" / "navigate" / "comprehensive" / "robust." AI red flags.
NO emoji overload. I use emoji rarely and selectively.
NO colon setups. "The part that stuck with me:" or "Here's the thing:" followed by a payoff line are AI templates.
NO rhetorical question + punchy answer combos. I don't ask a question and then answer my own question. I just make the statement.
NO corporate filler. Never write "In conclusion," "It is worth noting," "Best practices," "Leverage."
NO performative positivity. I don't do "What an incredible journey!" or "So blessed to announce..."

The ultimate test: read it out loud. If it sounds like a press release, a chatbot, or a LinkedIn influencer template, rewrite it.

### Punctuation and Formatting

Single quotes ' for concepts, reframed terms, and emphasis. Double quotes only for actual verbatim dialogue.
Minimize commas. Heavy comma use feels machine-generated. When in doubt, replace a comma with a period or "and."
Ellipses (...) sparingly. Long posts: max 2. Short posts: max 1. Never cluster them.
Exclamation points: sparingly, for genuine enthusiasm only.
Generous line breaks between thoughts.
Parenthetical asides: frequent. They add personality.
NO HASHTAGS. Zero. On any platform.
Contractions always: I'm, I've, don't, can't, it's, you're.

### Sentence Rhythm
Conversational flow, not staccato punch. Read it out loud. If it sounds like someone pausing for dramatic effect between every thought, smooth it out. If it sounds like someone actually talking, it's right.

### Word Count Rules (Hard Ceilings, Not Targets)

leadhuman.ai blog posts (/build/ and /lead/): 600 to 900 words
Tutorials (leadhuman.ai /build/): 600 to 800 words
About pages and static site pages: 400 to 600 words

The scroll test: if someone has to scroll more than twice on mobile, it's too long.
The tangent test: if a section could be its own post, pull it out. That's free content for next week.

### My Voice DNA
Vulnerability + authority. Conversational but intellectually dense. Bridge builder (synthesizes perspectives rather than picking sides). Storytelling through personal anecdote or professional observation. Human centered. Self deprecating humor. Earnest questions, not pronouncements. Action oriented optimism.
I frame myself as a learner sharing what I'm figuring out, not a guru dispensing wisdom. First person always. Connected to lived experience. Questions over mic drops.

### Signature Phrases

"I have a theory..."
"I've been reflecting on..."
"To be frank..." / "To be honest..."
"I don't know, but..."
"The thing about [X] is..."
"Curious if anyone has..."
"I would love to [verb]" (enthusiasm without demand)
"Let me know if [condition]" (respects autonomy)

### Two Patterns That Make My Posts Land

Concept Anchor: Build the post around a named concept ('nemawashi', 'tree ring management', 'psychological safety'). Name it, define it briefly, give it a memorable metaphor.
Diagnosis Before Prescription: Explain WHY the problem happens before offering the solution. Most posts skip this. I don't.
