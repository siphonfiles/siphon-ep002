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
    ("Trader Traitor", "TraderTraitor"), ("go back nineteen months", "go back 19 months"), ("by the second of October", "by 2 October"), ("Coin Join", "CoinJoin"), ("Bit-get", "Bitget"), ("Chain-alysis", "Chainalysis"),
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
    return t.replace("24 September, 2026,", "24 September 2026,")


SOFT = (", ", "; ", ": ", " — ")
LINE = 42
KEEP = {"withdrawal services", "security products", "way in", "database password", "malicious activity", "crypto exchange", "cold wallets", "risk threshold", "wallet host", "test transfers", "binance money", "private pool", "wallet job", "job server", "web shell",
        "risk control", "signing service", "protection fund", "customer support", "security product", "security office"}
WEAK = {"a", "an", "the", "of", "to", "that", "and", "at", "for", "by", "in", "on", "into", "from", "with",
        "its", "their", "his", "her", "every", "no", "some", "one", "two", "five", "about", "than", "was", "were"}


def break_cost(left, right):
    """Penalty for ending a line/cue on `left` and starting the next on `right`."""
    lw, rw = left.split()[-1].lower().strip(",.;:"), right.split()[0]
    c = 0
    if lw in WEAK:
        c += 25
    if re.match(r"^[$\d]", lw) and rw.lower().strip(",.") in ("million", "billion", "thousand", "trx", "ether", "usdt", "days", "minutes", "hours", "weeks"):
        c += 60
    if (len(rw.strip(",.")) == 1 and rw not in ("a", "I")) or (len(lw) == 1 and lw not in ("a",)):
        c += 60
    if f"{lw} {rw.lower().strip(',.')}" in KEEP:
        c += 60
    if rw.lower() in ("and", "but", "which", "where", "so", "because", "when", "or"):
        c -= 10
    return c


def split_long(p):
    """A sentence longer than MAX is cut once, at the clause break nearest its middle (a plain space only if
    there is no comma/semicolon/dash), so no cue is left with a one-word tail like "million."."""
    if len(p) <= MAX:
        return [p]
    best = None
    for i in range(len(p)):
        for sep in SOFT + (" ",):
            if p.startswith(sep, i):
                left, right = p[:i + len(sep.rstrip())].strip(), p[i + len(sep):].strip()
                if min(len(left), len(right)) < 15:
                    continue
                cost = abs(len(left) - len(right)) + (0 if sep != " " else 60) + break_cost(left, right)
                if best is None or cost < best[0]:
                    best = (cost, left, right)
    return split_long(best[1]) + split_long(best[2])


def chunks(text):
    """Sentences, cut where needed, then regrouped so nothing flashes alone: runs of short sentences share a
    cue ("No interest. No collateral."), and a lone short one joins its neighbour ("31 August. That's ...")."""
    sents = [p for sent in re.split(r"(?<=[.!?])\s+", text.strip()) if sent for p in split_long(sent)]
    runs = []
    for p in sents:
        if runs and len(runs[-1]) < 25 and len(p) < 25 and len(runs[-1]) + 1 + len(p) <= 48:
            runs[-1] += " " + p
        else:
            runs.append(p)
    out = []
    i = 0
    while i < len(runs):
        p = runs[i]
        if len(p) < 17 and out and len(out[-1]) + 1 + len(p) <= MAX and not (i == 0):
            out[-1] += " " + p
        elif len(p) < 17 and i + 1 < len(runs) and len(p) + 1 + len(runs[i + 1]) <= MAX + 6:
            out.append(p + " " + runs[i + 1])
            i += 1
        else:
            out.append(p)
        i += 1
    return out


def wrap(p):
    """Two balanced lines when a cue is longer than one line."""
    if len(p) <= LINE:
        return p
    sp = [i for i, ch in enumerate(p) if ch == " "]
    i = min(sp, key=lambda k: max(k, len(p) - k - 1) + (0 if p[k - 1] in ",.;:?" else 3) + break_cost(p[:k], p[k + 1:])
            + (100 if max(k, len(p) - k - 1) > LINE + 2 else 0))
    return p[:i] + "\n" + p[i + 1:]


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
            cues.append([t, t + d, p])
            t += d
    # a cue may stay up into the silence after it (up to 1 s, never into the next cue), for reading time
    for c, n in zip(cues, cues[1:] + [[1e9]]):
        c[1] = min(c[1] + 1.0, n[0] - 0.05, c[0] + 7.0) if n[0] - c[1] > 0.1 else min(c[1], c[0] + 7.0)
    with open(OUT, "w") as f:
        for i, (a, b, p) in enumerate(cues, 1):
            f.write(f"{i}\n{ts(a)} --> {ts(b)}\n{wrap(p)}\n\n")
    left = sorted(set(re.findall(r"\b(?:[A-Z] ){1,}[A-Z]\b|\b(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)-\w+",
                                 " ".join(c[2] for c in cues))))
    print(len(cues), "cues ->", OUT, "| still spelled out:", left)


if __name__ == "__main__":
    main()
