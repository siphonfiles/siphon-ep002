"""Ep. 002 thumbnail options (CPU, from the episode's own illustrations, no Bitget logo, no real brand).

Title on YouTube (owner, 25 Nov 2026): "Bitget's Alarm Rang. $388M in Crypto Kept Leaving."
The thumbnail completes the title and never repeats it (no "$388M", no "alarm" in the text):
  A  emptied deposit box under a red alarm        "NO KEY WAS STOLEN"
  B  the guard's desk, empty chair, 0 open alerts  "THE GUARD LET THEM IN"
  C  the alarm over the control-room wall          "NO KEY WAS STOLEN"
  D  crypto coins streaming out of the emptied box  "CRYPTO HEIST / NO KEY TAKEN"
  E  the signing machine, red HACKED stamp           "HACKED / WITHOUT A KEY"
  F  a silhouette at a laptop, coins on the screen   "HACKED THROUGH / SECURITY"
Crypto coins are generic (a hexagonal block glyph, no real coin's logo): 13 different assets were taken.
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


GOLD = (232, 184, 92)


def crypto_coin(r, tilt=0.0, tone=GOLD):
    """A generic crypto coin drawn at 4x: metal disc, rim, hexagonal block with network nodes (no real logo).
    tilt squashes it vertically (0 = face-on, 0.6 = strongly tilted)."""
    s = r * 8
    yy, xx = np.mgrid[0:s, 0:s] / s
    shade = 1.2 - 0.6 * np.hypot(xx - 0.32, yy - 0.28)
    body = np.dstack([np.full((s, s), c, np.float32) for c in tone]) * shade[..., None]
    c = Image.fromarray(np.dstack([body.clip(0, 255), np.full((s, s), 255)]).astype(np.uint8), "RGBA")
    m = Image.new("L", (s, s), 0)
    ImageDraw.Draw(m).ellipse((0, 0, s - 1, s - 1), fill=255)
    c.putalpha(m)
    d = ImageDraw.Draw(c)
    rim = s // 20
    d.ellipse((rim, rim, s - rim, s - rim), outline=(255, 226, 160, 255), width=s // 36)
    d.ellipse((rim * 3, rim * 3, s - rim * 3, s - rim * 3), outline=(150, 105, 40, 255), width=s // 60)
    import math
    cx = cy = s / 2
    R = s * 0.24
    pts = [(cx + R * math.cos(math.pi / 6 + k * math.pi / 3), cy + R * math.sin(math.pi / 6 + k * math.pi / 3)) for k in range(6)]
    ink = (120, 80, 25, 255)
    w = s // 34
    d.polygon(pts, outline=ink, width=w)
    for k in (1, 3, 5):
        d.line([(cx, cy), pts[k]], fill=ink, width=w)
    for x, y in pts + [(cx, cy)]:
        d.ellipse((x - w * 1.3, y - w * 1.3, x + w * 1.3, y + w * 1.3), fill=ink)
    c = c.resize((r * 2, max(2, int(r * 2 * (1 - tilt)))), Image.LANCZOS)
    return c


def paste_coin(im, cx, cy, r, tilt=0.0, rot=0.0, alpha=1.0, blur=0.0):
    c = crypto_coin(r, tilt).rotate(rot, expand=True, resample=Image.BICUBIC)
    if blur:
        c = c.filter(ImageFilter.GaussianBlur(blur))
    if alpha < 1:
        a = c.split()[3].point(lambda v: int(v * alpha))
        c.putalpha(a)
    g = Image.new("RGBA", im.size, (0, 0, 0, 0))
    glow = Image.new("L", im.size, 0)
    ImageDraw.Draw(glow).ellipse((cx - r * 1.6, cy - r * 1.6, cx + r * 1.6, cy + r * 1.6), fill=int(90 * alpha))
    glow = glow.filter(ImageFilter.GaussianBlur(r * 0.7))
    out = Image.composite(Image.new("RGBA", im.size, GOLD + (255,)), im.convert("RGBA"), glow.point(lambda v: v // 2))
    out.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))
    return out.convert("RGB")


def stamp(im, text, cx, cy, size, rot=-8, col=RED):
    f = ImageFont.truetype(ANTON, size)
    tw = int(ImageDraw.Draw(im).textlength(text, font=f))
    pad = size // 4
    lay = Image.new("RGBA", (tw + pad * 4, int(size * 1.5) + pad * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.rounded_rectangle((pad // 2, pad // 2, lay.width - pad // 2, lay.height - pad // 2), radius=size // 10,
                        outline=col + (255,), width=max(6, size // 12))
    d.text((lay.width / 2, lay.height / 2), text, font=f, fill=col + (255,), anchor="mm")
    rng = np.random.default_rng(3)          # worn ink, like a rubber stamp
    a = np.array(lay)
    a[..., 3] = (a[..., 3] * (0.78 + 0.22 * rng.random(a.shape[:2]))).astype(np.uint8)
    lay = Image.fromarray(a).rotate(rot, expand=True, resample=Image.BICUBIC)
    out = im.convert("RGBA")
    out.alpha_composite(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)))
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
    # D: coins streaming out of the emptied box, toward the bottom right
    d = base("b42_emptied_deposit_wall", crop=(300, 0, 2048, 983))
    d = vignette(shade(d, "right", 0.9, 0.46))
    path = [(330, 430, 34, 0.15, -10, 1.0), (430, 470, 40, 0.25, 15, 1.0), (545, 520, 48, 0.35, -20, 1.0),
            (690, 585, 58, 0.30, 25, 1.0), (860, 640, 70, 0.40, -15, 0.95), (300, 380, 26, 0.2, 5, 0.85)]
    for x, y, r, tl, rt, al in path:
        d = paste_coin(d, x, y, r, tl, rt, al)
    d = lines(d, [("CRYPTO HEIST", 128, WHITE), ("NO KEY TAKEN", 96, RED)], 1240, 70, align="right")
    d.save(os.path.join(OUT, "ep002_thumb_D_crypto_coins_heist.jpg"), quality=92)
    # E: the signing machine (it kept signing), a red HACKED stamp
    e = base("b41_signing_machine", crop=(0, 60, 1700, 1016))
    e = vignette(shade(e, "right", 0.9, 0.5))
    e = stamp(e, "HACKED", 520, 470, 150, rot=-9)
    e = lines(e, [("WITHOUT", 120, WHITE), ("A KEY", 150, RED)], 1235, 150, align="right")
    e.save(os.path.join(OUT, "ep002_thumb_E_hacked_without_key.jpg"), quality=92)
    # F: a silhouette at a laptop (from behind), coins rising from the screen
    f = base("b14_launderer_laptop", crop=(0, 0, 2048, 1152))
    f = vignette(shade(f, "right", 0.9, 0.45))
    for x, y, r, tl, rt, al in [(430, 300, 20, 0.2, 10, 0.8), (410, 232, 26, 0.25, -15, 0.9),
                                (385, 160, 32, 0.3, 20, 1.0), (355, 80, 38, 0.35, -10, 1.0)]:
        f = paste_coin(f, x, y, r, tl, rt, al)
    f = lines(f, [("HACKED", 170, RED), ("THROUGH", 112, WHITE), ("SECURITY", 112, CYAN)], 1240, 90, align="right")
    f.save(os.path.join(OUT, "ep002_thumb_F_hacked_through_security.jpg"), quality=92)
    print("thumbnails in", OUT)


if __name__ == "__main__":
    main()
