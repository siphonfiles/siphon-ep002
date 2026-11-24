"""Put content on the blank screens of two ep. 002 illustrations (CPU only, no quota).

b12_alarm_control_room: the video wall shows monitoring dashboards; the wide panel flags the
                        reconciliation gap at 19:05 UTC (illustrative), the rest are charts and lists.
b28_guard_monitors:     the guard's desk monitor shows a calm alert console: 0 alerts, all checks OK
                        ("STILL NO ALARM", 18:58 UTC). Light UI, so the warm glow of the screen stays.

Content is drawn flat, warped onto each screen with a perspective transform, masked by the screen
quad, softened and lit to sit in the photo. Originals are kept as <name>_blank.jpg (first run).
"""
import os
import shutil

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(__file__), "..")
IMG = os.path.join(ROOT, "illustrations", "ep002", "img")
MONO = "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-%s.ttf"
SANS = "/usr/share/fonts/truetype/ibm-plex/IBMPlexSansCondensed-%s.ttf"


def F(path, style, size):
    for p in (path % style, path % "Regular", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


rng = np.random.default_rng(7)
BG = (14, 30, 36)
GRID = (28, 52, 60)
CYAN = (62, 224, 208)
DIM = (96, 140, 146)
RED = (255, 77, 94)


def panel(W, H, title):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 34), fill=(10, 22, 27))
    d.text((14, 17), title, font=F(MONO, "Bold", 20), fill=DIM, anchor="lm")
    return im, d


def chart(W, H, title, falling=False, seed=0):
    im, d = panel(W, H, title)
    r = np.random.default_rng(seed)
    for gx in range(0, W, 60):
        d.line((gx, 40, gx, H), fill=GRID)
    for gy in range(40, H, 40):
        d.line((0, gy, W, gy), fill=GRID)
    n = 80
    v = np.cumsum(r.normal(0, 1, n)) * 6 + H * 0.5
    if falling:
        v[n * 2 // 3:] += np.linspace(0, H * 0.32, n - n * 2 // 3)
    pts = [(int(i * W / (n - 1)), int(np.clip(y, 50, H - 10))) for i, y in enumerate(v)]
    d.line(pts, fill=RED if falling else CYAN, width=4)
    return im


def table(W, H, title, seed=0):
    im, d = panel(W, H, title)
    r = np.random.default_rng(seed)
    f = F(MONO, "Regular", 18)
    y = 48
    while y < H - 20:
        d.text((14, y), "%02d:%02d:%02d" % (18, r.integers(0, 59), r.integers(0, 59)), font=f, fill=DIM)
        w = int(r.integers(60, 200))
        d.rectangle((130, y + 4, 130 + w, y + 16), fill=(40, 80, 86))
        d.text((W - 14, y), "OK", font=f, fill=CYAN, anchor="ra")
        y += 30
    return im


def status_grid(W, H, title, seed=0):
    im, d = panel(W, H, title)
    r = np.random.default_rng(seed)
    for gy in range(50, H - 20, 34):
        for gx in range(14, W - 20, 34):
            c = CYAN if r.random() > 0.08 else (230, 180, 80)
            d.rectangle((gx, gy, gx + 24, gy + 24), fill=tuple(int(x * 0.55) for x in c))
    return im


def wide_alert(W, H):
    im, d = panel(W, H, "RECONCILIATION · HOT WALLETS vs LEDGER")
    for gx in range(0, W, 80):
        d.line((gx, 40, gx, H), fill=GRID)
    n = 120
    led = np.full(n, H * 0.38)
    chain = led.copy()
    chain[70:] += np.cumsum(np.full(n - 70, 2.2))
    d.line([(int(i * W / (n - 1)), int(y)) for i, y in enumerate(led)], fill=CYAN, width=4)
    d.line([(int(i * W / (n - 1)), int(y)) for i, y in enumerate(chain)], fill=RED, width=5)
    bx = int(W * 0.60)
    d.rectangle((bx, 60, W - 30, 160), fill=(80, 18, 26), outline=RED, width=4)
    d.text((bx + 24, 92), "ALERT  19:05 UTC", font=F(MONO, "Bold", 34), fill=RED, anchor="lm")
    d.text((bx + 24, 134), "balance gap detected", font=F(MONO, "Regular", 26), fill=(255, 190, 196), anchor="lm")
    d.text((W - 16, H - 18), "ILLUSTRATIVE", font=F(MONO, "Regular", 18), fill=(70, 100, 104), anchor="rs")
    return im


def calm_console(W=1000, H=780):
    """The guard's desk monitor: light UI, nothing flagged."""
    im = Image.new("RGB", (W, H), (246, 240, 226))
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 70), fill=(225, 216, 196))
    d.text((30, 35), "ALERT CONSOLE", font=F(SANS, "Bold", 34), fill=(60, 58, 52), anchor="lm")
    d.text((W - 30, 35), "18:58 UTC", font=F(MONO, "Regular", 30), fill=(90, 86, 78), anchor="rm")
    d.text((W / 2, 190), "0", font=F(SANS, "Bold", 190), fill=(70, 150, 120), anchor="mm")
    d.text((W / 2, 320), "open alerts", font=F(SANS, "Regular", 44), fill=(90, 86, 78), anchor="mm")
    rows = ["Withdrawal risk checks", "Hot wallet signing", "Reconciliation", "Login monitor"]
    for i, t in enumerate(rows):
        y = 420 + i * 72
        d.rectangle((60, y, W - 60, y + 56), fill=(236, 228, 210))
        d.text((90, y + 28), t, font=F(SANS, "Regular", 34), fill=(70, 66, 60), anchor="lm")
        d.ellipse((W - 120, y + 14, W - 92, y + 42), fill=(80, 170, 120))
    d.text((W - 20, H - 14), "ILLUSTRATIVE", font=F(MONO, "Regular", 20), fill=(170, 160, 140), anchor="rs")
    return im


def put(img, content, quad, gain, blur=0.8, keep=0.0, light=None):
    """Warp content onto quad (TL, TR, BR, BL in source px), blend into img (float BGR)."""
    H, W = img.shape[:2]
    c = cv2.cvtColor(np.array(content), cv2.COLOR_RGB2BGR).astype(np.float32)
    h, w = c.shape[:2]
    q = np.float32(quad)
    M = cv2.getPerspectiveTransform(np.float32([[0, 0], [w, 0], [w, h], [0, h]]), q)
    warp = cv2.warpPerspective(c, M, (W, H), flags=cv2.INTER_AREA)
    warp = cv2.GaussianBlur(warp, (0, 0), blur) * gain
    m = np.zeros((H, W), np.uint8)
    cv2.fillConvexPoly(m, q.astype(np.int32), 255)
    m = cv2.erode(m, np.ones((3, 3), np.uint8))
    a = cv2.GaussianBlur(m.astype(np.float32) / 255, (0, 0), 1.2)[..., None]
    if light is not None:      # keep light falling on the screen (the alarm beam) on top of the content
        warp = warp + light
    return img * (1 - a) + (warp + img * keep) * a


def do_b12():
    name = "b12_alarm_control_room"
    path = os.path.join(IMG, name + ".jpg")
    blank = os.path.join(IMG, name + "_blank.jpg")
    if not os.path.exists(blank):
        shutil.copy(path, blank)
    img = cv2.imread(blank).astype(np.float32)
    s = 1.28
    P = lambda pts: [(x * s, y * s + 150) for x, y in pts]
    # light from the alarm beam that falls across the wall: what is brighter than the plain panel tone
    base = cv2.GaussianBlur(img, (0, 0), 25)
    gray = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
    warmth = np.clip(base[..., 2] - base[..., 0], 0, None)       # red minus blue: the orange beam
    beam = (np.clip(warmth - 12, 0, None) / 60.0)[..., None] * np.array([40, 90, 150], np.float32)
    panels = [
        (P([(114, 90), (358, 114), (354, 246), (110, 241)]), chart(900, 480, "HOT WALLET OUTFLOW", True, 1)),
        (P([(368, 113), (603, 126), (602, 252), (366, 248)]), table(900, 480, "WITHDRAWAL QUEUE", 2)),
        (P([(612, 128), (838, 133), (838, 258), (612, 256)]), status_grid(900, 480, "SIGNING NODES", 3)),
        (P([(848, 135), (1422, 122), (1424, 262), (848, 262)]), wide_alert(1900, 470)),
        (P([(0, 240), (96, 243), (96, 388), (0, 386)]), table(400, 600, "LOGINS", 4)),
        (P([(107, 247), (354, 252), (352, 390), (106, 388)]), chart(900, 500, "API LATENCY", False, 5)),
        (P([(363, 256), (600, 262), (600, 392), (362, 390)]), status_grid(900, 500, "RISK CHECKS", 6)),
        (P([(609, 262), (838, 265), (840, 393), (609, 392)]), chart(900, 500, "COLD WALLET", False, 7)),
        (P([(848, 266), (1424, 262), (1426, 394), (848, 394)]), table(1900, 450, "CHAIN EVENTS", 8)),
    ]
    for quad, content in panels:
        img = put(img, content, quad, gain=0.78, keep=0.18, light=beam)
    img += np.random.default_rng(3).normal(0, 2.0, img.shape)
    cv2.imwrite(path, img.clip(0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 95])


def do_b28():
    name = "b28_guard_monitors"
    path = os.path.join(IMG, name + ".jpg")
    blank = os.path.join(IMG, name + "_blank.jpg")
    if not os.path.exists(blank):
        shutil.copy(path, blank)
    img = cv2.imread(blank).astype(np.float32)
    quad = [(862, 484), (1115, 486), (1128, 683), (878, 687)]
    # the screen glow falls off towards its edges: keep that shading on the new content
    H, W = img.shape[:2]
    shade = cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (0, 0), 6) / 235.0
    img2 = put(img.copy(), calm_console(), quad, gain=1.0, blur=0.7)
    m = np.zeros((H, W), np.uint8)
    cv2.fillConvexPoly(m, np.int32(quad), 255)
    a = cv2.GaussianBlur(m.astype(np.float32) / 255, (0, 0), 1.2)[..., None]
    sh = np.clip(shade, 0.55, 1.05)[..., None]
    img = img2 * (1 - a) + img2 * sh * a
    img += np.random.default_rng(4).normal(0, 2.0, img.shape)
    cv2.imwrite(path, img.clip(0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 95])


if __name__ == "__main__":
    do_b12()
    do_b28()
