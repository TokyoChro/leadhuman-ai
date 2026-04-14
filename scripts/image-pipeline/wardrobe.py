"""
Jay's Wardrobe Database — Rugged Ivy Style
Used by the image pipeline to dress Jay in accurate, owned outfits.
"""

import random

WARDROBE = {
    "outerwear": {
        "blazers": [
            {"name": "Navy Blazer", "type": "Unstructured", "brand": "Burberry", "color": "Navy"},
            {"name": "Tweed Blazer", "type": "Unstructured", "brand": "Burberry", "color": "Tweed"},
            {"name": "Houndstooth Blazer", "type": "Unstructured", "brand": "Unspecified", "color": "Brown"},
        ],
        "jackets": [
            {"name": "Vintage Windbreaker", "brand": "Burberry", "color": "Unspecified"},
            {"name": "Bedale", "brand": "Barbour", "color": "Olive"},
            {"name": "G9 Harrington", "brand": "Baracuta", "color": "Khaki"},
        ],
        "coats": [
            {"name": "Dunkeld", "brand": "Mackintosh", "color": "Navy"},
            {"name": "Dunkeld", "brand": "Mackintosh", "color": "Khaki"},
        ],
    },
    "tops": {
        "linen_shirts": [
            {"name": "Linen Shirt", "color": "White"},
            {"name": "Linen Shirt", "color": "Light Green"},
            {"name": "Linen Shirt", "color": "University Stripe Blue"},
            {"name": "Linen Shirt", "color": "University Stripe Gray"},
            {"name": "Linen Shirt", "color": "Light Blue"},
            {"name": "Linen Shirt", "color": "Navy"},
            {"name": "Linen Shirt", "color": "Black"},
            {"name": "Linen Shirt", "color": "Khaki"},
        ],
        "oxford_button_downs": [
            {"name": "Denim Shirt", "brand": "Kamakura", "color": "Denim"},
            {"name": "Chambray Shirt", "brand": "Kamakura", "color": "Chambray"},
            {"name": "Stretch Shirt", "brand": "Kamakura", "color": "Unspecified"},
            {"name": "Royal Oxford Cotton Shirt", "brand": "Kamakura", "color": "Unspecified"},
            {"name": "OCBD", "brand": "Kamakura", "color": "White"},
            {"name": "OCBD", "brand": "Kamakura", "color": "Off White (ECRU)"},
            {"name": "OCBD", "brand": "Kamakura", "color": "University Stripe Blue"},
            {"name": "OCBD", "brand": "Kamakura", "color": "Light Blue"},
            {"name": "MTM OCBD", "brand": "Kamakura", "color": "Pink University Stripe", "ref": "M453S2294QB", "mtm": True},
            {"name": "MTM OCBD", "brand": "Kamakura", "color": "Blue Multi Stripe", "ref": "M311S0861QB", "mtm": True},
            {"name": "MTM OCBD", "brand": "Kamakura", "color": "Red Pencil Stripe", "ref": "M613S0800QB", "mtm": True},
        ],
        "polos": [
            {"name": "Polo", "color": "White"},
            {"name": "Polo", "color": "Black"},
            {"name": "Polo", "color": "Navy"},
            {"name": "Polo", "color": "Gray"},
        ],
        "tees": [
            {"name": "Heavyweight Tee", "color": "White"},
            {"name": "Heavyweight Tee", "color": "Black"},
            {"name": "Heavyweight Tee", "color": "Navy"},
            {"name": "Heavyweight Tee", "color": "Gray"},
            {"name": "Knit Tee", "brand": "Banana Republic", "color": "Gray"},
            {"name": "Knit Tee", "brand": "Banana Republic", "color": "Brown"},
        ],
        "sweaters_knitwear": [
            {"name": "Knit Sweater", "brand": "Ralph Lauren", "color": "Unspecified"},
            {"name": "Knit Sweater Vest", "brand": "Ralph Lauren", "color": "Unspecified", "qty": 2},
            {"name": "Knit Sweater Cardigan", "brand": "Ralph Lauren", "color": "Unspecified"},
            {"name": "Pullover Sweater", "color": "Gray"},
            {"name": "Pullover Sweater", "color": "Maroon"},
            {"name": "Henley", "brand": "Banana Republic", "color": "Gray"},
            {"name": "Henley", "brand": "Banana Republic", "color": "Brown"},
            {"name": "Overshirt", "brand": "Banana Republic", "color": "Unspecified"},
        ],
    },
    "bottoms": {
        "chinos": [
            {"name": "Chinos", "color": "Stone"},
            {"name": "Chinos", "color": "Tan"},
            {"name": "Chinos", "color": "Olive"},
            {"name": "Chinos", "color": "Navy"},
            {"name": "Chinos", "color": "Khaki"},
            {"name": "Chinos", "color": "Gray"},
        ],
        "corduroy": [
            {"name": "Corduroy Pants", "brand": "Banana Republic", "color": "Gray"},
            {"name": "Corduroy Pants", "brand": "Banana Republic", "color": "Brown"},
        ],
        "denim": [
            {"name": "Travellers Slim Denim", "brand": "Banana Republic", "color": "Black"},
            {"name": "Travellers Super Skinny Denim", "brand": "Banana Republic", "color": "Indigo", "qty": 2},
            {"name": "Selvedge Denim", "brand": "Uniqlo", "color": "Indigo"},
        ],
        "shorts": [
            {"name": "Linen Shorts", "color": "Khaki"},
            {"name": "Linen Shorts", "color": "Navy"},
        ],
    },
    "shoes": {
        "boots": [
            {"name": "Stow", "brand": "Trickers", "color": "Acorn"},
            {"name": "1000 Mile", "brand": "Wolverine", "color": "Brown"},
        ],
        "dress_shoes": [
            {"name": "Molton", "brand": "Crockett & Jones", "color": "Unspecified"},
            {"name": "Strands", "brand": "Allen Edmonds", "color": "Unspecified"},
        ],
        "casual": [
            {"name": "Boat Shoes", "brand": "LL Bean", "color": "Unspecified"},
            {"name": "Killshots 2", "brand": "Nike", "color": "White/Gum"},
        ],
    },
    "accessories": {
        "watches": [
            {"name": "Seamaster 300M Diver", "brand": "Omega", "ref": "210.30", "role": "The Anchor", "color": "Blue (Ceramic)", "movement": "Co-Axial Auto"},
            {"name": "Speedmaster '57", "brand": "Omega", "ref": "3594.50", "role": "The Ritual", "color": "Gray (Steel)", "movement": "Manual Wind (Lemania)"},
            {"name": "Alpinist GMT", "brand": "Seiko", "ref": "SBEJ005", "role": "The Traveler", "color": "Green (Forest)", "movement": "Automatic GMT"},
        ],
        "glasses": [
            {"name": "Rectangular Glasses", "type": "traditional"},
            {"name": "G2 Smart Glasses", "brand": "Even Realities", "color": "Gray", "type": "smart"},
        ],
        "caps": [
            {"name": "Cap", "brand": "Brooks Brothers", "color": "Forest Green", "logo": "tiny white embroidered Golden Fleece logo"},
            {"name": "Cap", "brand": "Brooks Brothers", "color": "Navy", "logo": "tiny white embroidered Golden Fleece logo"},
            {"name": "Cap", "brand": "Ralph Lauren", "color": "Navy", "logo": "tiny embroidered polo player logo"},
            {"name": "Cap", "brand": "Ralph Lauren", "color": "Olive", "logo": "tiny embroidered polo player logo"},
        ],
    },
}


_OUTFIT_COMBOS = [
    {"top_cat": "oxford_button_downs", "outer_cat": "blazers", "bottom_cat": "chinos", "shoe_cat": "dress_shoes", "vibe": "smart ivy"},
    {"top_cat": "sweaters_knitwear", "outer_cat": "jackets", "bottom_cat": "corduroy", "shoe_cat": "boots", "vibe": "rugged casual"},
    {"top_cat": "linen_shirts", "outer_cat": None, "bottom_cat": "chinos", "shoe_cat": "casual", "vibe": "summer ivy"},
    {"top_cat": "polos", "outer_cat": None, "bottom_cat": "denim", "shoe_cat": "casual", "vibe": "weekend casual"},
    {"top_cat": "oxford_button_downs", "outer_cat": None, "bottom_cat": "chinos", "shoe_cat": "boots", "vibe": "heritage prep", "layer": "sweaters_knitwear"},
    {"top_cat": "sweaters_knitwear", "outer_cat": "coats", "bottom_cat": "denim", "shoe_cat": "boots", "vibe": "rainy day"},
    {"top_cat": "tees", "outer_cat": None, "bottom_cat": "shorts", "shoe_cat": "casual", "vibe": "summer casual"},
    {"top_cat": "linen_shirts", "outer_cat": "blazers", "bottom_cat": "corduroy", "shoe_cat": "dress_shoes", "vibe": "smart casual"},
]


def pick_outfit(vibe: str = None, season: str = None) -> dict:
    combos = _OUTFIT_COMBOS.copy()

    if vibe:
        combos = [c for c in combos if vibe.lower() in c["vibe"].lower()]

    if season:
        s = season.lower()
        if s == "summer":
            combos = [c for c in combos if c["outer_cat"] not in ("coats",)]
        elif s in ("winter", "fall"):
            combos = [c for c in combos if c.get("bottom_cat") != "shorts"]

    if not combos:
        combos = _OUTFIT_COMBOS

    combo = random.choice(combos)

    top = random.choice(WARDROBE["tops"][combo["top_cat"]])
    bottom = random.choice(WARDROBE["bottoms"][combo["bottom_cat"]])
    shoes = random.choice(WARDROBE["shoes"][combo["shoe_cat"]])

    outerwear = None
    if combo["outer_cat"]:
        outerwear = random.choice(WARDROBE["outerwear"][combo["outer_cat"]])

    layer = None
    if combo.get("layer"):
        layer = random.choice(WARDROBE["tops"][combo["layer"]])

    watch = random.choice(WARDROBE["accessories"]["watches"])
    cap = random.choice(WARDROBE["accessories"]["caps"]) if random.random() > 0.5 else None
    glasses = random.choice(WARDROBE["accessories"]["glasses"]) if random.random() > 0.3 else None

    outfit = {
        "top": top,
        "layer": layer,
        "outerwear": outerwear,
        "bottom": bottom,
        "shoes": shoes,
        "watch": watch,
        "cap": cap,
        "glasses": glasses,
        "vibe": combo["vibe"],
    }
    outfit["description"] = _describe_outfit(outfit)
    return outfit


def _describe_outfit(outfit: dict) -> str:
    parts = []

    top = outfit["top"]
    color = top.get("color", "")
    if color and color != "Unspecified" and color.lower() not in top["name"].lower():
        top_desc = f"{color} {top['name']}"
    elif color and color != "Unspecified":
        top_desc = top["name"]
    else:
        top_desc = top["name"]
    parts.append(top_desc)

    if outfit.get("layer"):
        layer = outfit["layer"]
        layer_desc = f"{layer['color']} {layer['name']}" if layer.get("color") and layer["color"] != "Unspecified" else layer["name"]
        parts.append(f"layered with a {layer_desc}")

    if outfit.get("outerwear"):
        outer = outfit["outerwear"]
        o_color = outer.get("color", "")
        if o_color and o_color != "Unspecified" and o_color.lower() not in outer["name"].lower():
            outer_desc = f"{o_color} {outer['name']}"
        else:
            outer_desc = outer["name"]
        brand = f" ({outer['brand']})" if outer.get("brand") and outer["brand"] != "Unspecified" else ""
        parts.append(f"wearing a {outer_desc}{brand} over it")

    bottom = outfit["bottom"]
    bottom_desc = f"{bottom['color']} {bottom['name']}" if bottom.get("color") and bottom["color"] != "Unspecified" else bottom["name"]
    parts.append(bottom_desc)

    shoes = outfit["shoes"]
    shoe_desc = f"{shoes['brand']} {shoes['name']}" if shoes.get("brand") and shoes["brand"] != "Unspecified" else shoes["name"]
    parts.append(shoe_desc)

    watch = outfit["watch"]
    parts.append(f"{watch['brand']} {watch['name']} ({watch['role']}) on his wrist")

    if outfit.get("glasses"):
        g = outfit["glasses"]
        if g["type"] == "smart":
            parts.append(f"{g['brand']} {g['name']} in {g['color']}")
        else:
            parts.append(g["name"])

    if outfit.get("cap"):
        cap = outfit["cap"]
        parts.append(f"a {cap['color']} {cap['brand']} baseball cap with only a {cap['logo']} — logo must be VERY SMALL, under 1cm")

    desc = f"He is wearing a {parts[0]}"
    for i, p in enumerate(parts[1:], 1):
        if i == len(parts) - 1:
            desc += f", and {p}"
        else:
            desc += f", {p}"
    desc += "."

    return desc
