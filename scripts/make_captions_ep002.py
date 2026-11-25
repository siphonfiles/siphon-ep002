"""English captions (SRT) for ep. 002, from the exact voice timeline + the final takes' texts.

Text: sound/ep002/ep002_lines.json, with the re-voiced takes used in the mix (build_final_voices.py:
t3/c3/x6 "Bit-get", g5, x4 rephrased). The spoken forms are turned back into written form (digits, times,
tickers, names). Timing: graphics/motion/ep002_full.timeline.json (voice start + duration). Long lines are split
at sentence/clause breaks into cues of at most ~84 characters, timed in proportion to their length.
Usage: python3 scripts/make_captions_ep002.py  ->  episodes/publish/002-captions-en.srt
"""
import json
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SND = os.path.join(ROOT, "sound/ep002")
TEXT = {d["id"]: d["text"] for d in json.load(open(os.path.join(SND, "ep002_lines.json")))}


def _take(f, k, v):
    return next(x["text"] for x in json.load(open(os.path.join(SND, f))) if x["id"] == f"{k}_{v}")


for k, v in {"t3": "h6", "c3": "h7", "x6": "h7", "g5": "s9"}.items():
    TEXT[k] = _take("ep002_fix2_lines.json", k, v)
TEXT["x4"] = _take("ep002_fix3_lines.json", "x4", "s2")
TL = json.load(open(os.path.join(ROOT, "graphics/motion/ep002_full.timeline.json")))
OUT = os.path.join(ROOT, "episodes/publish/002-captions-en.srt")
MAX = 84

R = [  # spoken form -> written form (longest first where they overlap)
    ("three hundred and eighty-eight million dollars", "$388 million"),
    ("two hundred and thirty-eight million dollars", "$238 million"),
    ("about two hundred and three million dollars", "about $203 million"),
    ("About two hundred and three million dollars", "About $203 million"),
    ("one hundred and sixty-one million dollars", "$161 million"),
    ("just over three hundred million dollars", "just over $300 million"),
    ("one and a half billion dollars", "$1.5 billion"),
    ("more than six billion dollars", "more than $6 billion"),
    ("Thirty-four point seven five million U S D T", "34.75 million USDT"),
    ("zero point eight four ether", "0.84 ether"), ("zero point three percent", "0.3%"),
    ("forty thousand ether", "40,000 ether"), ("about sixty-three thousand", "about 63,000"),
    ("exactly one hundred thousand, or two hundred thousand", "exactly 100,000, or 200,000"),
    ("thirty-five thousand, six hundred and seventy-eight transactions", "35,678 transactions"),
    ("about a thousand pieces", "about 1,000 pieces"), ("had used fifty-four", "had used 54"),
    ("Ninety-three T R X", "93 TRX"), ("ninety-three T R X", "93 TRX"),
    ("U S D T", "USDT"), ("X R P", "XRP"), ("Zach X B T", "ZachXBT"), ("Thor Chain", "THORChain"),
    ("Coin Join", "CoinJoin"), ("Bit-get", "Bitget"), ("Chain-alysis", "Chainalysis"),
    ("February twenty twenty-five", "February 2025"), ("twenty twenty-six", "2026"),
    ("the thirty-first of August", "31 August"), ("The thirty-first of August", "31 August"),
    ("the twenty-third of September", "23 September"), ("the twenty-fourth of September", "24 September"),
    ("the 2nd of October", "2 October"),
    ("nineteen oh five", "19:05"), ("Nineteen oh five", "19:05"), ("Nineteen oh one", "19:01"),
    ("Nineteen oh three", "19:03"), ("Nineteen fourteen", "19:14"), ("Nineteen sixteen", "19:16"), ("sixteen oh seven", "16:07"), ("seventeen forty-nine", "17:49"),
    ("Eighteen thirty-one", "18:31"), ("Eighteen fifty-eight", "18:58"), ("twenty forty", "20:40"),
    ("twenty-one twenty-three", "21:23"), ("twenty-one forty-four", "21:44"),
    ("two hours and thirty-nine minutes", "2 hours and 39 minutes"),
    ("twenty-four days", "24 days"), ("eleven days", "11 days"), ("eleven minutes", "11 minutes"),
    ("twenty minutes", "20 minutes"), ("eight days", "8 days"), ("five weeks", "5 weeks"),
]


def written(t):
    for a, b in R:
        t = t.replace(a, b)
    return t


def chunks(text):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    out = []
    for p in parts:
        while len(p) > MAX:
            cut = max(p.rfind(", ", 0, MAX), p.rfind(": ", 0, MAX), p.rfind("; ", 0, MAX), p.rfind(" — ", 0, MAX))
            if cut < 20:
                cut = p.rfind(" ", 0, MAX)
            out.append(p[:cut + 1].strip())
            p = p[cut + 1:].strip()
        if out and len(out[-1]) + len(p) + 1 <= MAX and not out[-1].endswith((".", "?", "!")):
            out[-1] += " " + p
        else:
            out.append(p)
    return [c for c in out if c]


def ts(x):
    ms = int(round(x * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def main():
    cues = []
    for e in TL["events"]:
        if e.get("kind") != "voice":
            continue
        parts = chunks(written(TEXT[e["id"]]))
        total = sum(len(p) for p in parts)
        t = e["t"]
        for p in parts:
            d = e["dur"] * len(p) / total
            cues.append((t, t + d, p))
            t += d
    with open(OUT, "w") as f:
        for i, (a, b, p) in enumerate(cues, 1):
            f.write(f"{i}\n{ts(a)} --> {ts(min(b, a + 7.0))}\n{p}\n\n")
    left = sorted(set(re.findall(r"\b(?:[A-Z] ){1,}[A-Z]\b|\b(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)-\w+",
                                 " ".join(c[2] for c in cues))))
    print(len(cues), "cues ->", OUT, "| still spelled out:", left)


if __name__ == "__main__":
    main()
