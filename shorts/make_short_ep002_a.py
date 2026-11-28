"""Short #1 for ep. 002 (vertical 1080x1920, ~31 s). Built from scratch for the vertical feed, not cut
from the 16:9 episode: a split screen (customers locked out / attacker still signing), one clock,
one counter. Clean voice takes + its own sound (alarm, vault_run, sub hits).
Usage: python3 shorts/make_short_ep002_a.py <voices_dir> <out.mp4>"""
import math, os, subprocess, sys
import numpy as np
from scipy.io import wavfile
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "sound"))
import heist_tracks as HT  # noqa: E402
import sting_design as SD  # noqa: E402

VOICES, OUT = sys.argv[1], sys.argv[2]
W, H, FPS, SR = 1080, 1920, 30, 44100
BG, PANEL, CYAN, RED, INK, DIM = (10, 20, 23), (16, 31, 35), (62, 224, 208), (255, 77, 94), (240, 244, 244), (132, 150, 152)
BOLD = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
SEMI = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
ANTON = "/usr/share/fonts/truetype/google-fonts/ofl/anton/Anton-Regular.ttf"
F = lambda p, s: ImageFont.truetype(p, s)

# ---------------- audio ----------------
def voice(k):
    sr, a = wavfile.read(os.path.join(VOICES, k + ".wav"))
    a = a.astype(np.float64) / 32768
    if a.ndim > 1: a = a.mean(1)
    env = np.abs(a) > 0.004
    i0, i1 = np.argmax(env), len(a) - np.argmax(env[::-1])
    a = a[max(0, i0 - int(0.02 * sr)): min(len(a), i1 + int(0.08 * sr))].copy()
    f = int(0.04 * sr); a[-f:] *= np.linspace(1, 0, f)
    return a

# (line, gap after it, chunks: (text, highlighted words))
SEQ = [
    ("t3", 0.30, [("AT 19:05, THE ALARM WENT OFF.", ["19:05,"]),
                  ("BITGET FROZE EVERY CUSTOMER WITHDRAWAL.", ["FROZE"]),
                  ("AND THE MONEY KEPT LEAVING", ["KEPT", "LEAVING"]),
                  ("FOR ANOTHER TWO HOURS.", ["TWO", "HOURS."])]),
    ("f6", 0.50, [("19:16.", ["19:16."])]),
    ("f7", 0.12, [("FIVE TRANSFERS.", []), ("FIVE CHAINS.", []), ("NINE SECONDS.", ["NINE", "SECONDS."])]),
    ("f8", 0.55, [("ABOUT $203 MILLION.", ["$203", "MILLION."])]),
    ("f9", 0.12, [("THE CUSTOMERS HAD BEEN LOCKED OUT", ["LOCKED", "OUT"]), ("11 MINUTES EARLIER.", ["11", "MINUTES"])]),
    ("f10", 0.65, [("THE ATTACKER HADN'T.", ["HADN'T."])]),
    ("g1", 0.45, [("BLOCKING CUSTOMER WITHDRAWALS", []), ("WAS THE WRONG SWITCH.", ["WRONG", "SWITCH."]),
                  ("THE FORGED REQUESTS", ["FORGED"]), ("WEREN'T CUSTOMER WITHDRAWALS.", ["WEREN'T"])]),
]
END_DUR = 3.6
T, CAPS, t = {}, [], 0.45
voice_buf = np.zeros(int(60 * SR))
for k, gap, chunks in SEQ:
    a = voice(k)
    voice_buf[int(t * SR): int(t * SR) + len(a)] += a
    d = len(a) / SR
    T[k] = (t, t + d)
    # caption chunk boundaries: proportional to characters, snapped to the nearest pause
    quiet = np.convolve((np.abs(a) < 0.006).astype(float), np.ones(int(0.12 * SR)) / int(0.12 * SR), "same") > 0.98
    pauses = [i / SR for i in range(0, len(a), 200) if quiet[i]]
    tot = sum(len(c[0]) for c in chunks); acc = 0; cuts = [0.0]
    for c in chunks[:-1]:
        acc += len(c[0]); g = d * acc / tot
        near = [p for p in pauses if abs(p - g) < 0.45]
        cuts.append(min(near, key=lambda p: abs(p - g)) if near else g)
    cuts.append(d + 0.08)
    for (txt, hi), c0, c1 in zip(chunks, cuts[:-1], cuts[1:]):
        CAPS.append((t + c0, t + c1, txt, hi))
    t += d + gap
END0 = t
TOTAL = END0 + END_DUR
N = int(TOTAL * SR)
voice_buf = voice_buf[:N]

music = HT.vault_run(TOTAL + 3)[:N]
duck = np.ones(N) * 0.16
duck[: int(0.45 * SR)] = 0.30; duck[int(END0 * SR):] = 0.42
k = int(0.25 * SR); duck = np.convolve(duck, np.ones(k) / k, "same")
mix = voice_buf * 1.0 + music * duck
def add(sig, at, g):
    i = int(at * SR); n = min(len(sig), N - i)
    if n > 0: mix[i:i + n] += sig[:n] * g
for at in (T["f6"][0] - 0.06, T["f8"][1] + 0.05, T["f10"][1] + 0.08, END0 + 0.05):
    add(SD.sub_hit(), at, 0.75)
for j in range(5):                                   # five transfers = five ticks
    add(SD.tick(), T["f7"][0] + j * 0.16, 0.5)
# alarm: decoded from the chosen SFX take, loud for the first beat then under the voice
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", os.path.join(ROOT, "sound/ep002/sfx/candidates/building_alarm_s22.mp3"),
                "-ac", "1", "-ar", str(SR), "/tmp/s2_alarm.wav"], check=True)
_, al = wavfile.read("/tmp/s2_alarm.wav"); al = al.astype(np.float64) / 32768
al = al[: int(4.2 * SR)] / (np.max(np.abs(al)) + 1e-9)
envl = np.interp(np.arange(len(al)) / SR, [0, 0.4, 0.8, 3.2, 4.2], [0.55, 0.55, 0.10, 0.07, 0.0])
add(al * envl, 0.0, 1.0)
mix[-int(0.5 * SR):] *= np.linspace(1, 0, int(0.5 * SR))
mix /= np.max(np.abs(mix)) + 1e-9
wavfile.write("/tmp/s2_mix.wav", SR, (mix * 0.9 * 32767).astype(np.int16))
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", "/tmp/s2_mix.wav", "-af",
                "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-ac", "2", "/tmp/s2_audio.wav"], check=True)

# ---------------- picture ----------------
ease = lambda x: 0.0 if x <= 0 else 1.0 if x >= 1 else 1 - (1 - x) ** 3
mixc = lambda a, b, k: tuple(int(a[i] + (b[i] - a[i]) * k) for i in range(3))
FROZE = T["t3"][0] + (T["t3"][1] - T["t3"][0]) * 0.36          # "Bitget froze..."
KEPT = T["t3"][0] + (T["t3"][1] - T["t3"][0]) * 0.66           # "And the money kept leaving"
G1a, G1b = T["g1"]

def clock_text(t):
    if t < KEPT: m = 5
    elif t < T["f6"][0]: m = 5 + int(10 * (t - KEPT) / (T["f6"][0] - KEPT))
    elif t < G1a + 1.2: m = 16
    else: m = 16 + int((21 * 60 + 44 - 19 * 60 - 16) * ease(min(1, (t - G1a - 1.2) / (G1b - G1a - 1.6))))
    return f"{19 + m // 60:02d}:{m % 60:02d}"

def counter(t):
    if t < T["f8"][0]: return 0.0
    if t < G1a + 1.2: return 203 * ease((t - T["f8"][0]) / 0.7)
    return 203 + 35 * ease((t - G1a - 1.2) / (G1b - G1a - 1.6))

def grid_bg(t):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, W, 60): d.line([(x, 0), (x, H)], fill=(14, 27, 31))
    for y in range(0, H, 60): d.line([(0, y), (W, y)], fill=(14, 27, 31))
    return im

def toggle(d, x, y, on, k):
    w, h = 150, 74
    col = mixc((60, 70, 72), CYAN if on else RED, k)
    d.rounded_rectangle([x, y, x + w, y + h], radius=37, fill=mixc(PANEL, col, 0.35), outline=col, width=4)
    kx = x + 37 + (w - 74) * (k if on else 1 - k) if on else x + w - 37 - (w - 74) * k
    d.ellipse([kx - 27, y + 10, kx + 27, y + h - 10], fill=col)

def lock(d, cx, cy, s, col):
    d.arc([cx - s * 0.42, cy - s * 0.95, cx + s * 0.42, cy - s * 0.05], 180, 360, fill=col, width=int(s * 0.16))
    d.rounded_rectangle([cx - s * 0.62, cy - s * 0.5, cx + s * 0.62, cy + s * 0.5], radius=int(s * 0.14), fill=col)
    d.ellipse([cx - s * 0.11, cy - s * 0.16, cx + s * 0.11, cy + s * 0.06], fill=PANEL)
    d.rectangle([cx - s * 0.045, cy, cx + s * 0.045, cy + s * 0.25], fill=PANEL)

def caption(im, text, hi, age):
    d = ImageDraw.Draw(im); f = F(BOLD, 66)
    words = text.split(); lines, cur = [], []
    for w in words:
        if cur and d.textlength(" ".join(cur + [w]), font=f) > 900: lines.append(cur); cur = [w]
        else: cur.append(w)
    lines.append(cur)
    lh, pop = 84, min(1.0, age / 0.1)
    y0 = 1075 - len(lines) * lh // 2
    for i, ln in enumerate(lines):
        ws = [d.textlength(w, font=f) for w in ln]; sp = d.textlength(" ", font=f)
        x = W / 2 - (sum(ws) + sp * (len(ln) - 1)) / 2; y = y0 + i * lh + (1 - pop) * 12
        for w, wd in zip(ln, ws):
            d.text((x, y), w, font=f, fill=CYAN if w in hi else INK, stroke_width=7, stroke_fill=(0, 0, 0))
            x += wd + sp

def frame(t):
    im = grid_bg(t); d = ImageDraw.Draw(im)
    alarm = t >= 0
    # red alarm wash, pulsing (strong in the first second, then a slow beat)
    pulse = 0.5 + 0.5 * math.sin(2 * math.pi * (t * 1.6))
    amt = (0.34 if t < 1.0 else 0.13) * pulse + 0.05
    wash = Image.new("RGB", (W, H), RED)
    mask = Image.new("L", (W, H), 0); md = ImageDraw.Draw(mask)
    md.rectangle([0, 0, W, H], fill=int(255 * amt)); md.ellipse([-200, 300, W + 200, 1700], fill=int(255 * amt * 0.25))
    im = Image.composite(wash, im, mask.filter(ImageFilter.GaussianBlur(160))); d = ImageDraw.Draw(im)

    # top pill
    s = "THE BITGET HACK  ·  24 SEP 2026"; f = F(SEMI, 32); tw = d.textlength(s, font=f)
    d.rounded_rectangle([W / 2 - tw / 2 - 26, 232, W / 2 + tw / 2 + 26, 292], radius=30, fill=(6, 12, 14), outline=(30, 60, 64), width=2)
    d.text((W / 2, 262), s, font=f, fill=CYAN, anchor="mm")

    # ---------- panel A: customers ----------
    A = (60, 330, 1020, 780)
    kf = ease((t - FROZE) / 0.35)
    d.rounded_rectangle(A, radius=36, fill=PANEL, outline=mixc((38, 70, 74), RED, kf), width=4)
    d.text((100, 372), "CUSTOMERS", font=F(SEMI, 34), fill=DIM, anchor="lm")
    d.text((980, 372), "ILLUSTRATIVE", font=F(SEMI, 22), fill=(80, 98, 100), anchor="rm")
    if t < G1a:
        if kf < 0.5:
            tap = 0.5 + 0.5 * math.sin(t * 9)
            d.rounded_rectangle([180, 470, 900, 620], radius=75, fill=mixc(CYAN, (40, 170, 160), tap))
            d.text((540, 545), "WITHDRAW", font=F(ANTON, 84), fill=(6, 20, 22), anchor="mm")
            d.text((540, 690), "your funds · any time", font=F(SEMI, 34), fill=DIM, anchor="mm")
        else:
            lock(d, 200, 545, 105, RED)
            d.text((300, 505), "WITHDRAWALS", font=F(ANTON, 88), fill=INK, anchor="lm")
            d.text((300, 603), "SUSPENDED", font=F(ANTON, 88), fill=RED, anchor="lm")
            if T["f9"][0] <= t:
                k9 = ease((t - T["f9"][0]) / 0.3)
                d.rounded_rectangle([240, 678, 840, 748], radius=35, fill=mixc(PANEL, RED, 0.9 * k9))
                d.text((540, 713), "LOCKED OUT AT 19:05", font=F(BOLD, 38), fill=mixc(PANEL, (255, 255, 255), k9), anchor="mm")
            else:
                d.text((540, 713), "for every customer on the platform", font=F(SEMI, 34), fill=DIM, anchor="mm")
    else:
        kg = ease((t - G1a) / 0.5)
        d.text((100, 500), "CUSTOMER", font=F(ANTON, 84), fill=INK, anchor="lm")
        d.text((100, 596), "WITHDRAWALS", font=F(ANTON, 84), fill=INK, anchor="lm")
        toggle(d, 770, 510, False, kg)
        d.text((845, 625), "OFF", font=F(ANTON, 60), fill=mixc(PANEL, RED, kg), anchor="mm")
        d.text((100, 713), "the switch Bitget pulled", font=F(SEMI, 36), fill=DIM, anchor="lm")

    # ---------- clock ----------
    ct = clock_text(t)
    hot = (T["f6"][0] <= t < T["f6"][0] + 0.5) or t < 0.8
    d.text((W / 2 - 40, 880), ct, font=F(MONO, 128), fill=RED if hot else INK, anchor="mm", stroke_width=6, stroke_fill=(0, 0, 0))
    d.text((W / 2 + 205, 908), "UTC", font=F(SEMI, 36), fill=DIM, anchor="lm")

    # ---------- panel B: attacker ----------
    B = (60, 1190, 1020, 1560)
    d.rounded_rectangle(B, radius=36, fill=PANEL, outline=(38, 70, 74), width=4)
    d.text((100, 1232), "THE ATTACKER", font=F(SEMI, 34), fill=DIM, anchor="lm")
    if t < G1a:
        v = counter(t)
        if t < T["f7"][0]:
            # forged requests streaming out, no amounts yet
            if t >= KEPT - 0.2:
                for j in range(7):
                    ph = ((t - KEPT) * 0.9 + j / 7) % 1
                    x = 110 + ph * 760; a = math.sin(ph * math.pi)
                    d.rounded_rectangle([x, 1330, x + 70, 1350], radius=10, fill=mixc(PANEL, CYAN, a))
                d.text((100, 1420), "signed transfers still going out", font=F(SEMI, 38), fill=INK, anchor="lm")
            else:
                d.text((100, 1340), "…", font=F(ANTON, 90), fill=(60, 86, 90), anchor="lm")
        else:
            for j in range(5):
                on = t >= T["f7"][0] + j * 0.16
                d.rounded_rectangle([100 + j * 82, 1290, 100 + j * 82 + 62, 1314], radius=12, fill=CYAN if on else (34, 60, 64))
            d.text((530, 1302), "5 TRANSFERS · 5 CHAINS · 9 s", font=F(SEMI, 28), fill=DIM, anchor="lm")
            if t >= T["f8"][0]:
                d.text((100, 1400), f"~${v:,.0f}M", font=F(ANTON, 150), fill=CYAN, anchor="lm")
            if t >= T["f10"][0]:
                k10 = ease((t - T["f10"][0]) / 0.3)
                d.rounded_rectangle([100, 1486, 520, 1540], radius=27, fill=mixc(PANEL, CYAN, k10))
                d.text((310, 1513), "NOT LOCKED OUT", font=F(BOLD, 32), fill=mixc(PANEL, (4, 20, 22), k10), anchor="mm")
            elif t >= T["f8"][0]:
                d.text((100, 1513), "gone in one burst", font=F(SEMI, 34), fill=DIM, anchor="lm")
    else:
        kg = ease((t - G1a - 0.6) / 0.5)
        d.text((100, 1330), "SIGNING SERVICE", font=F(ANTON, 76), fill=INK, anchor="lm")
        toggle(d, 640, 1293, True, kg)
        d.text((845, 1330), "ON", font=F(ANTON, 60), fill=mixc(PANEL, CYAN, kg), anchor="mm")
        d.text((100, 1440), f"~${counter(t):,.0f}M", font=F(ANTON, 104), fill=CYAN, anchor="lm")
        d.text((455, 1428), "left after the alarm", font=F(SEMI, 32), fill=INK, anchor="lm")
        d.text((455, 1468), "two independent estimates", font=F(SEMI, 26), fill=DIM, anchor="lm")
        d.text((100, 1523), "SOURCES: BITGET · BITQUERY · HALBORN · CERTORA", font=F(SEMI, 22), fill=(86, 106, 108), anchor="lm")
    if t < G1a and t >= T["f7"][0]:
        d.text((980, 1232), "SOURCE: BITQUERY", font=F(SEMI, 22), fill=(86, 106, 108), anchor="rm")

    for a, b, txt, hi in CAPS:
        if a <= t < b: caption(im, txt, hi, t - a)
    return im

def end_card(t):
    im = grid_bg(t); d = ImageDraw.Draw(im); a = ease((t - END0) / 0.35)
    c = lambda col: mixc(BG, col, a)
    d.text((W / 2, 560), "THE SIGNING MACHINE", font=F(ANTON, 104), fill=c(INK), anchor="mm")
    d.text((W / 2, 690), "STAYED ON FOR", font=F(ANTON, 104), fill=c(INK), anchor="mm")
    d.text((W / 2, 880), "2 H 39 MIN", font=F(ANTON, 190), fill=c(RED), anchor="mm")
    d.text((W / 2, 1010), "after the first alert  ·  source: Bitget timeline", font=F(SEMI, 30), fill=c(DIM), anchor="mm")
    b = ease((t - END0 - 0.9) / 0.4); cb = lambda col: mixc(BG, col, b)
    d.text((W / 2, 1200), "And not one key was stolen,", font=F(SEMI, 48), fill=cb(INK), anchor="mm")
    d.text((W / 2, 1268), "Bitget says.", font=F(SEMI, 48), fill=cb(INK), anchor="mm")
    d.text((W / 2, 1390), "HOW THEY GOT IN  ↓", font=F(ANTON, 76), fill=cb(CYAN), anchor="mm")
    d.text((W / 2, 1470), "full investigation linked below", font=F(SEMI, 34), fill=cb(DIM), anchor="mm")
    return im

if len(sys.argv) > 3:                                  # stills only: times as extra args
    for s in sys.argv[3:]:
        tt = float(s); (end_card(tt) if tt >= END0 else frame(tt)).save(f"/tmp/short2/still_{tt:05.2f}.png")
    print({k: (round(a, 2), round(b, 2)) for k, (a, b) in T.items()}, "END0", round(END0, 2), "TOTAL", round(TOTAL, 2)); sys.exit()

enc = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                        "-r", str(FPS), "-i", "-", "-i", "/tmp/s2_audio.wav", "-c:v", "libx264", "-preset", "medium",
                        "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest",
                        "-movflags", "+faststart", OUT], stdin=subprocess.PIPE)
for i in range(int(TOTAL * FPS)):
    tt = i / FPS
    enc.stdin.write((end_card(tt) if tt >= END0 else frame(tt)).tobytes())
enc.stdin.close(); enc.wait()
print("ok", OUT, round(TOTAL, 2))
