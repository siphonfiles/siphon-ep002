"""Ep. 002 thumbnail options (CPU, from the episode's own illustrations, no Bitget logo, no real brand).

Title on YouTube (owner, 25 Nov 2026): "Bitget's Alarm Rang. $388M in Crypto Kept Leaving."
The thumbnail completes the title and never repeats it (no "$388M", no "alarm" in the text):
  A  emptied deposit box under a red alarm        "NO KEY WAS STOLEN"
  B  the guard's desk, empty chair, 0 open alerts  "THE GUARD LET THEM IN"
  C  the alarm over the control-room wall          "NO KEY WAS STOLEN"
"No key was stolen" is Bitget's own finding [S2]; the video attributes it to Bitget.
Usage: python3 thumbnails/make_ep002_options.py   -> thumbnails/ep002/*.jpg (1280x720)
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "..", "illustrations", "ep002", "img")
OUT = os.path.join(HERE, "ep002")
ANTON = "/usr/share/fonts/truetype/google-fonts/ofl/anton/Anton-Regular.ttf"
W, H = 1280, 720
WHITE = (244, 246, 248)
CYAN = (62, 224, 208)
RED = (255, 77, 94)


def base(name, crop=None, dark=0.0, sat=1.0):
    im = Image.open(os.path.join(IMG, name + ".jpg")).convert("RGB")
    if crop:
        im = im.crop(crop)
    im = im.resize((W, H), Image.LANCZOS)
    if sat != 1.0:
        g = im.convert("L").convert("RGB")
        im = Image.blend(g, im, sat)
    if dark:
        im = Image.blend(im, Image.new("RGB", im.size, (0, 0, 0)), dark)
    return im


def shade(im, side="right", amount=0.85, width=0.6):
    x = np.linspace(0, 1, W)
    if side == "left":
        x = x[::-1]
    g = np.clip((x - (1 - width)) / width, 0, 1) ** 1.2 * amount
    a = np.array(im).astype(np.float32) * (1 - g[None, :, None])
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))


def vignette(im, amount=0.45):
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.hypot((xx - W / 2) / (W / 2), (yy - H / 2) / (H / 2))
    g = np.clip(r - 0.55, 0, 1) * amount
    a = np.array(im).astype(np.float32) * (1 - g[..., None])
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))


def lines(im, rows, x, y, align="left", gap=6):
    """rows: [(text, size, colour)]; drawn with a soft shadow so they read on any background."""
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ds, out = ImageDraw.Draw(sh), im.convert("RGBA")
    pos, yy = [], y
    for t, size, col in rows:
        f = ImageFont.truetype(ANTON, size)
        w = ds.textlength(t, font=f)
        xx = x if align == "left" else (x - w if align == "right" else x - w / 2)
        pos.append((t, f, col, xx, yy))
        ds.text((xx + 4, yy + 6), t, font=f, fill=(0, 0, 0, 200))
        yy += int(size * 1.08) + gap
    out.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
    d = ImageDraw.Draw(out)
    for t, f, col, xx, yy in pos:
        d.text((xx, yy), t, font=f, fill=col)
    return out.convert("RGB")


def main():
    os.makedirs(OUT, exist_ok=True)
    # A: the emptied box and the red alarm on the left, text on the dark right
    a = base("b42_emptied_deposit_wall", crop=(300, 0, 2048, 983))
    a = vignette(shade(a, "right", 0.9, 0.46))
    a = lines(a, [("NO KEY", 172, WHITE), ("WAS STOLEN", 107, RED)], 1240, 170, align="right")
    a.save(os.path.join(OUT, "ep002_thumb_A_vault_no_key.jpg"), quality=92)
    # B: the guard's empty chair and the calm monitor; text over the darkened left
    b = base("b28_guard_monitors", crop=(150, 120, 2048, 1187))
    b = vignette(shade(b, "left", 0.93, 0.62))
    b = lines(b, [("THE GUARD", 150, WHITE), ("LET THEM IN", 150, CYAN)], 55, 330)
    b.save(os.path.join(OUT, "ep002_thumb_B_guard_let_them_in.jpg"), quality=92)
    # C: the alarm and the alert screen, close; text on the dark left
    c = base("b12_alarm_control_room", crop=(380, 0, 1640, 709))
    c = vignette(shade(c, "left", 0.93, 0.62))
    c = lines(c, [("NO KEY", 190, WHITE), ("WAS STOLEN", 118, RED)], 55, 150)
    c.save(os.path.join(OUT, "ep002_thumb_C_alarm_no_key.jpg"), quality=92)
    print("thumbnails in", OUT)


if __name__ == "__main__":
    main()
