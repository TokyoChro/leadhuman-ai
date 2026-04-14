"""
Cloud Image Pipeline — generates a single Ivy Boys blog illustration.
Designed to run in GitHub Actions. Outputs to src/assets/images/posts/{slug}.png.

Usage:
  python generate.py --slug "my-post-slug" --prompt "scene description" [--vibe "smart ivy"] [--season "summer"]
"""

import argparse
import os
import sys
from pathlib import Path

from google import genai
from google.genai import types
from PIL import Image
from wardrobe import pick_outfit


# ─── Config ──────────────────────────────────────────────────────────────────

API_KEY = os.environ.get("GOOGLE_API_KEY")
if not API_KEY:
    print("ERROR: GOOGLE_API_KEY not set.", file=sys.stderr)
    sys.exit(1)

SCRIPT_DIR = Path(__file__).parent
FACE_REFERENCE = SCRIPT_DIR / "reference" / "face-reference.png"
REPO_ROOT = SCRIPT_DIR.parent.parent
OUTPUT_DIR = REPO_ROOT / "src" / "assets" / "images" / "posts"

CREAM_BG = (245, 240, 230)

STYLE_BASE = (
    "Warm editorial illustration in the style of a Japanese lifestyle magazine, "
    "combining vintage menswear editorial art with manga-influenced character design "
    "and watercolor textures. Clean sepia/brown line work, warm earth tone palette "
    "(tan, olive, cream, forest green, navy), soft watercolor washes, hand-drawn feel "
    "on cream paper. No text, no annotations, no Japanese characters, no words, no letters."
)

COMPOSITION_SQUARE = (
    "IMPORTANT COMPOSITION: Center the subject in the frame. Show the FULL body "
    "from head to feet — do NOT crop at the legs or waist. The character should "
    "be fully visible and well-proportioned within the square frame. "
    "Leave breathing room around the subject. No parts of the body should extend "
    "outside the image boundaries."
)


# ─── Image Processing ────────────────────────────────────────────────────────

def adjust_to_square(filepath: Path) -> None:
    """Post-process an image to 1:1 ratio. Gemini ignores ratio requests."""
    img = Image.open(filepath)
    w, h = img.size

    if abs(w / h - 1.0) < 0.02:
        return  # close enough

    if w < h:
        new_w = h
        canvas = Image.new("RGB", (new_w, h), CREAM_BG)
        canvas.paste(img, ((new_w - w) // 2, 0))
    else:
        new_h = w
        canvas = Image.new("RGB", (w, new_h), CREAM_BG)
        canvas.paste(img, (0, (new_h - h) // 2))

    canvas.save(filepath)
    print(f"  Adjusted to 1:1: {canvas.size[0]}x{canvas.size[1]}")


# ─── Generation ──────────────────────────────────────────────────────────────

def generate(prompt_text: str, slug: str, vibe: str = None, season: str = None) -> Path:
    """Generate a single blog illustration and save it to the posts image directory."""
    client = genai.Client(api_key=API_KEY)
    output_path = OUTPUT_DIR / f"{slug}.png"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load face reference
    if not FACE_REFERENCE.exists():
        print(f"ERROR: Face reference not found at {FACE_REFERENCE}", file=sys.stderr)
        sys.exit(1)

    with open(FACE_REFERENCE, "rb") as f:
        image_bytes = f.read()
    ref_image = types.Part.from_bytes(data=image_bytes, mime_type="image/png")

    # Pick outfit
    outfit_info = pick_outfit(vibe=vibe, season=season)
    outfit_desc = outfit_info["description"]

    # Determine glasses instruction
    glasses = outfit_info.get("glasses")
    if glasses and glasses.get("type") == "smart":
        glasses_line = (
            f"He is wearing {glasses['brand']} {glasses['name']} in {glasses['color']} — "
            f"sleek, minimal smart glasses with a modern frameless look."
        )
    elif glasses:
        glasses_line = "He is wearing rectangular glasses."
    else:
        glasses_line = "He is NOT wearing glasses."

    full_prompt = (
        f"CRITICAL: This image must contain EXACTLY ONE person — a single male character. "
        f"Do NOT draw two people. Do NOT split into multiple figures. ONE man only.\n\n"
        f"FACE REFERENCE: Study the reference illustration carefully. This is the SAME person. "
        f"Replicate his EXACT facial structure: broad jaw, wide face shape, specific nose shape, "
        f"and eye shape. He has a tightly shaved/buzzcut head (almost bald, NO styled hair, "
        f"NO full head of hair), a goatee/facial hair, and East Asian features. "
        f"His skin tone must match the reference exactly. The face must be RECOGNIZABLY "
        f"the same person as the reference — not a generic character.\n\n"
        f"APPEARANCE: Make him look slightly YOUNGER than the reference — smoother skin, "
        f"youthful energy, fewer lines, but keep the SAME facial structure and features. "
        f"Late 20s/early 30s. His build should be SLIM and "
        f"proportions slightly TALL and lean. Think sharp, fit, confident young professional.\n\n"
        f"GLASSES: {glasses_line}\n\n"
        f"CLOTHING (on the SAME single character): {outfit_desc} Draw each clothing item "
        f"accurately — correct colors, textures, and layering. These are real garments, "
        f"render them faithfully.\n\n"
        f"Scene: {prompt_text}\n\n"
        f"{COMPOSITION_SQUARE}\n\n"
        f"Style: {STYLE_BASE}\n"
        f"Do NOT reproduce the reference. Create a NEW warm watercolor editorial illustration "
        f"with this ONE person in a new scene. Again — ONLY ONE CHARACTER in the image."
    )

    print(f"Generating blog image for: {slug}")
    print(f"Outfit vibe: {outfit_info.get('vibe', 'random')}")
    print(f"Outfit: {outfit_desc}")
    print(f"Output: {output_path}\n")

    # Try up to 3 times (Gemini can occasionally fail)
    model = "gemini-3.1-flash-image-preview"
    for attempt in range(3):
        try:
            print(f"  Attempt {attempt + 1}/3 (model: {model})...")
            response = client.models.generate_content(
                model=model,
                contents=[ref_image, full_prompt],
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE", "TEXT"],
                ),
            )
            for part in response.candidates[0].content.parts:
                if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                    with open(output_path, "wb") as f:
                        f.write(part.inline_data.data)
                    adjust_to_square(output_path)
                    print(f"  Saved: {output_path}")
                    return output_path
            print(f"  No image in response, retrying...")
        except Exception as e:
            print(f"  Error: {e}")
            if attempt == 0 and "gemini-3.1" in model:
                model = "gemini-3-pro-image-preview"
                print(f"  Falling back to {model}")

    print("ERROR: Failed to generate image after 3 attempts.", file=sys.stderr)
    sys.exit(1)


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Cloud Image Pipeline — generate a blog illustration")
    parser.add_argument("--slug", required=True, help="Post slug (used as filename)")
    parser.add_argument("--prompt", required=True, help="Scene description for the illustration")
    parser.add_argument("--vibe", help="Outfit vibe: smart ivy, rugged casual, summer ivy, etc.")
    parser.add_argument("--season", help="Season: summer, winter, spring, fall")
    args = parser.parse_args()

    output = generate(args.prompt, args.slug, vibe=args.vibe, season=args.season)
    print(f"\nDone! Image saved to: {output}")


if __name__ == "__main__":
    main()
