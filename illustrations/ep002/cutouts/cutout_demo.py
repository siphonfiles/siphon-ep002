import math, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = "/home/claude/siphon-ep002/"
W, H, FPS = 1920, 1080, 30
BG = (0x0E, 0x1A, 0x1D); CY = (0x3E, 0xE0, 0xD0); INK = (0xE4, 0xEF, 0xEE); GREY = (0x7C, 0x93, 0x96); RED = (0xFF, 0x4D, 0x5E)
HEAD = "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf"
MONO = R + "fonts/NotoSansMono-Regular.ttf"; MONOB = R + "fonts/NotoSansMono-Bold.ttf"
F = lambda p, s: ImageFont.truetype(p, s)
def clamp(x): return max(0.0, min(1.0, x))
def eo(x): x = clamp(x); return 1 - (1 - x) ** 3
def pr(t, a, d): return clamp((t - a) / d)

def backdrop(t):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im, "RGBA")
    for k, x in enumerate(range(0, W + 1, 60)): d.line([(x, 0), (x, H)], fill=CY + (15 if k % 5 == 0 else 6,))
    for k, y in enumerate(range(0, H + 1, 60)): d.line([(0, y), (W, y)], fill=CY + (15 if k % 5 == 0 else 6,))
    y = (t / 9 % 1) * (H + 300) - 150
    d.rectangle([0, y - 60, W, y + 60], fill=CY + (5,))
    for cx, cy, dx, dy in ((40, 40, 1, 1), (W - 40, 40, -1, 1), (40, H - 40, 1, -1), (W - 40, H - 40, -1, -1)):
        d.line([(cx, cy + dy * 36), (cx, cy), (cx + dx * 36, cy)], fill=CY + (90,), width=2)
    return im

def cut(name, box):
    c = Image.open(R + f"illustrations/ep002/cutouts/{name}_cut.png")
    return c.crop(c.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox())

def place(im, obj, cx, cy, scale, alpha=1.0, rot=0.0, shadow=True):
    o = obj.resize((int(obj.width * scale), int(obj.height * scale)), Image.LANCZOS)
    if rot: o = o.rotate(rot, Image.BICUBIC, expand=True)
    if alpha < 1: o.putalpha(o.getchannel("A").point(lambda v: int(v * alpha)))
    x, y = int(cx - o.width / 2), int(cy - o.height / 2)
    if shadow:
        sh = Image.new("RGBA", o.size, (0, 0, 0, 0)); sh.putalpha(o.getchannel("A").point(lambda v: int(v * 0.6)))
        sh = sh.filter(ImageFilter.GaussianBlur(28)); im.paste(sh, (x + 18, y + 30), sh)
    im.paste(o, (x, y), o)
    return x, y, o.width, o.height

def text(d, xy, s, font, col, a=1.0, anchor="la"):
    d.text(xy, s, font=font, fill=col + (int(255 * a),), anchor=anchor)

def line_draw(d, p0, p1, k, col, w=3):
    if k <= 0: return
    x = p0[0] + (p1[0] - p0[0]) * k; y = p0[1] + (p1[1] - p0[1]) * k
    d.line([p0, (x, y)], fill=col + (230,), width=w)
    d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=col + (255,))

def node(d, xy, label, k, col=CY, sub=None):
    if k <= 0: return
    x, y = xy; a = eo(k)
    d.rounded_rectangle([x, y - 46, x + 500, y + 46], 8, outline=col + (int(220 * a),), width=2, fill=(0x13, 0x26, 0x2A, int(230 * a)))
    text(d, (x + 24, y - 14 if sub else y), label, F(MONOB, 30), col if col != CY else INK, a, "lm")
    if sub: text(d, (x + 24, y + 20), sub, F(MONO, 22), GREY, a, "lm")

def source(d, s, a): text(d, (W - 80, H - 80), s, F(MONO, 22), GREY, a, "rs")

BADGE, APP, PHONE = cut("b07_badge_lanyard", 0), cut("b04_security_appliance", 0), cut("b11_phone_nightstand", 0)

def scene_badge(t):
    im = backdrop(t + 0); d = ImageDraw.Draw(im, "RGBA")
    k = eo(pr(t, 0, 0.9))
    place(im, BADGE, 540 - 220 * (1 - k), 470 + 6 * math.sin(t * 1.3), 0.95, alpha=k, rot=4 * (1 - k) + 1.5 * math.sin(t * 0.9))
    d = ImageDraw.Draw(im, "RGBA")
    text(d, (960, 330), "16:07 UTC · PRODUCT B", F(MONOB, 30), CY, pr(t, 0.6, 0.4))
    text(d, (960, 380), "A borrowed name", F(HEAD, 76), INK, pr(t, 0.9, 0.5))
    text(d, (960, 480), "logged in to the management platform", F(MONO, 28), GREY, pr(t, 1.3, 0.5))
    line_draw(d, (800, 640), (1020, 640), eo(pr(t, 2.0, 0.8)), CY)
    node(d, (1030, 640), "WALLET JOB SERVER", pr(t, 2.7, 0.5), sub="builds withdrawal transactions")
    source(d, "[S3][S4][S7]", pr(t, 1.0, 0.5))
    return im

def scene_app(t):
    im = backdrop(t + 5); k = eo(pr(t, 0, 0.8))
    x, y, w, h = place(im, APP, 520, 560 + 30 * (1 - k), 1.15, alpha=k)
    d = ImageDraw.Draw(im, "RGBA")
    # LED on the cutout (~88% across, ~58% down): pulses red once the web shell lands
    lx, ly = x + w * 0.828, y + h * 0.565
    p = pr(t, 1.2, 0.3) * (0.7 + 0.3 * math.sin(t * 7))
    for r, a in ((70, 50), (34, 120), (12, 255)):
        d.ellipse([lx - r, ly - r, lx + r, ly + r], fill=RED + (int(a * p),))
    text(d, (x, y - 70), "APPLIANCE B", F(MONOB, 30), CY, pr(t, 0.5, 0.4))
    line_draw(d, (x + w + 20, ly), (1010, 430), eo(pr(t, 1.2, 0.5)), RED)
    node(d, (1020, 430), "WEB SHELL", pr(t, 1.5, 0.4), RED, "channel back to the attacker")
    line_draw(d, (1270, 480), (1270, 640), eo(pr(t, 2.4, 0.6)), CY)
    node(d, (1020, 690), "WALLET JOB SERVER", pr(t, 2.9, 0.4), sub="malicious packages installed")
    source(d, "Mandiant [S3]", pr(t, 0.8, 0.5))
    return im

def scene_phone(t):
    im = backdrop(t + 10); k = eo(pr(t, 0, 0.8))
    place(im, PHONE, W / 2, 760 + 40 * (1 - k), 1.25, alpha=k)
    d = ImageDraw.Draw(im, "RGBA")
    text(d, (W / 2, 210), "IF YOU HAD MONEY ON BITGET", F(MONOB, 30), CY, pr(t, 0.4, 0.4), "ma")
    b = eo(pr(t, 1.3, 0.45)); bx0, by = W / 2 - 400, 340 + 40 * (1 - b)
    if b > 0:
        d.rounded_rectangle([bx0, by, bx0 + 800, by + 170], 22, fill=(0x1B, 0x2B, 0x2F, int(240 * b)), outline=GREY + (int(120 * b),), width=1)
        d.rounded_rectangle([bx0 + 28, by + 34, bx0 + 88, by + 94], 12, fill=GREY + (int(160 * b),))
        text(d, (bx0 + 112, by + 46), "EXCHANGE · 19:05 UTC", F(MONO, 24), GREY, b)
        text(d, (bx0 + 112, by + 82), "Withdrawals suspended", F(HEAD, 46), INK, b)
        text(d, (bx0 + 112, by + 136), "for every customer on the platform", F(MONO, 22), GREY, b)
        d.line([(W / 2, by + 170), (W / 2, 620)], fill=GREY + (int(90 * b),), width=2)
    text(d, (W / 2, 1000 - 30), "…and the money kept leaving for two more hours", F(MONO, 28), RED, pr(t, 2.8, 0.6), "ms")
    source(d, "Bitget [S2]", pr(t, 1.0, 0.5))
    return im

ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                       "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "/tmp/demo/birefnet_demo.mp4"], stdin=subprocess.PIPE)
for sc in (scene_badge, scene_app, scene_phone):
    for i in range(5 * FPS):
        t = i / FPS; im = sc(t)
        fade = min(pr(t, 0, 0.25), 1 - pr(t, 4.7, 0.3))
        if fade < 1: im = Image.blend(Image.new("RGB", (W, H), BG), im, fade)
        ff.stdin.write(im.tobytes())
        if i == 105: im.save(f"/tmp/demo/{sc.__name__}.jpg", quality=90)
ff.stdin.close(); ff.wait(); print("ok")
