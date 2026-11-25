"""Print a generic staff-badge design onto the blank badge cutout of ep. 002 (owner, 25 Nov 2026:
"the badge needs a drawing so it looks like a badge").
- flat design: dark top band "STAFF ACCESS", an anonymous silhouette instead of a photo (never a face),
  the name hidden under a black bar (we never invent or show a real employee), an ID barcode, ILLUSTRATIVE tag
- warped in perspective onto the card face (corners measured on the 758x1004 cutout), then multiplied by the
  card's own shading so the lamp light and the edges stay as in the image
- the original stays as c_b07_badge_lanyard_blank.png
Usage: python3 scripts/badge_content_ep002.py
"""
import os, shutil
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CUT = os.path.join(ROOT, "illustrations/ep002/cutouts/c_b07_badge_lanyard.png")
BLANK = CUT.replace(".png", "_blank.png")
FONT_B = os.path.join(ROOT, "fonts/NotoSansMono-Bold.ttf")
FONT_R = os.path.join(ROOT, "fonts/NotoSansMono-Regular.ttf")
# inner face of the card (inside the metal rim): TL, TR, BR, BL
QUAD = np.float32([(40, 364), (484, 345), (736, 903), (271, 968)])
W, H = 600, 870   # flat design, about the face's aspect


def font(path, size):
    return ImageFont.truetype(path, size)


def design():
    im = Image.new("RGB", (W, H), (238, 234, 226))
    d = ImageDraw.Draw(im)
    # top band, below the clip slot (the slot covers the top ~9 % at the centre)
    d.rectangle([0, 105, W, 215], fill=(22, 52, 58))
    d.rectangle([0, 215, W, 223], fill=(62, 224, 208))
    d.text((40, 128), "STAFF ACCESS", font=font(FONT_B, 46), fill=(235, 245, 244))
    d.text((40, 182), "AUTHORISED PERSONNEL", font=font(FONT_R, 20), fill=(150, 200, 196))
    # photo box with an anonymous silhouette
    px, py, pw, ph = 40, 270, 210, 260
    d.rectangle([px, py, px + pw, py + ph], fill=(196, 202, 206))
    cx = px + pw // 2
    d.ellipse([cx - 52, py + 45, cx + 52, py + 150], fill=(120, 128, 134))
    d.pieslice([cx - 100, py + 160, cx + 100, py + 360], 180, 360, fill=(120, 128, 134))
    d.rectangle([px, py, px + pw, py + ph], outline=(150, 156, 160), width=3)
    # name and role, hidden
    tx = 285
    d.text((tx, 278), "NAME", font=font(FONT_R, 22), fill=(110, 112, 114))
    d.rectangle([tx, 312, W - 40, 352], fill=(18, 18, 20))
    d.text((tx, 380), "DEPARTMENT", font=font(FONT_R, 22), fill=(110, 112, 114))
    d.rectangle([tx, 414, W - 110, 446], fill=(18, 18, 20))
    d.text((tx, 474), "ACCESS LEVEL", font=font(FONT_R, 22), fill=(110, 112, 114))
    d.text((tx, 500), "INTERNAL", font=font(FONT_B, 30), fill=(22, 52, 58))
    # barcode
    rng = np.random.default_rng(7)
    x, by0, by1 = 40, 600, 720
    while x < W - 40:
        w = int(rng.choice([3, 3, 5, 7]))
        d.rectangle([x, by0, x + w - 1, by1], fill=(24, 24, 26))
        x += w + int(rng.choice([3, 4, 6]))
    d.text((40, 732), "ID  ▮▮▮▮ ▮▮▮▮ ▮▮", font=font(FONT_R, 24), fill=(70, 72, 74))
    d.text((40, 800), "ILLUSTRATIVE", font=font(FONT_R, 18), fill=(150, 150, 150))
    return im


def main():
    if not os.path.exists(BLANK):
        shutil.copy(CUT, BLANK)
    src = Image.open(BLANK).convert("RGBA")
    base = np.asarray(src).astype(np.float32) / 255.0
    flat = np.asarray(design()).astype(np.float32) / 255.0
    M = cv2.getPerspectiveTransform(np.float32([(0, 0), (W, 0), (W, H), (0, H)]), QUAD)
    Hh, Ww = base.shape[:2]
    warped = cv2.warpPerspective(flat, M, (Ww, Hh), flags=cv2.INTER_AREA)
    mask = cv2.warpPerspective(np.ones((H, W), np.float32), M, (Ww, Hh), flags=cv2.INTER_LINEAR)
    mask = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))) / 255.0
    # shading of the blank card face: luminance relative to its median, keeps the lamp gradient
    lum = base[..., :3].mean(2)
    face = mask > 0.99
    shade = np.clip(lum / np.median(lum[face]), 0.55, 1.25)[..., None]
    paint = np.clip(warped * shade, 0, 1)
    out = base.copy()
    m = mask[..., None]
    out[..., :3] = base[..., :3] * (1 - m) + paint * m
    # the clip and slot sit on top of the card: put them back from the original
    clip = np.zeros((Hh, Ww), np.float32)
    clip[300:400, 220:330] = 1.0
    clip = np.asarray(Image.fromarray((clip * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))) / 255.0
    dark = (lum < np.median(lum[face]) * 0.8).astype(np.float32)
    keep = (clip * np.maximum(dark, (base[..., :3].std(2) > 0.04).astype(np.float32)))[..., None]
    out[..., :3] = out[..., :3] * (1 - keep) + base[..., :3] * keep
    Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8), "RGBA").save(CUT)
    print("badge printed ->", CUT)


if __name__ == "__main__":
    main()
