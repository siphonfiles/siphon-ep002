"""Build translated SRTs for ep. 002 from episodes/publish/subs/<code>.json, with the exact timings of the English
SRT, and check them. Usage: python3 scripts/build_subs_ep002.py [code ...]  (default: every <code>.json present)

Checks (printed; exit code 1 if any hard error):
  hard  - 197 cues, same ids/order, none empty, no line breaks; every brand/name present in the English cue is
          present verbatim.
  notes - every cue whose digits differ from the English (3億8800万, "ساعتين", "tháng 9", "19 h 05" are fine
          grammar): listed so the reviewer confirms the value is exactly the same.
  soft  - reading speed (characters per second) and length vs the English.
"""
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PUB = os.path.join(ROOT, "episodes/publish")
SUBS = os.path.join(PUB, "subs")
SRC = json.load(open(os.path.join(SUBS, "source.json")))
EN = open(os.path.join(PUB, "002-captions-en.srt")).read().strip().split("\n\n")
TIMES = [b.split("\n")[1] for b in EN]
NAMES = ["Bitget", "Bybit", "Binance", "Mandiant", "SlowMist", "Chainalysis", "Elliptic", "TRM Labs", "ZachXBT",
         "THORChain", "Zcash", "CoinJoin", "Kelp DAO", "TraderTraitor", "Gracy Chen", "Thomas Archer", "Siphon Files",
         "FBI", "VPN", "IP", "USDT", "TRX", "XRP", "Bitcoin", "Ethereum"]
MONTHS = {"February": 2, "April": 4, "August": 8, "September": 9, "October": 10, "November": 11}
CJK = {"ja", "zh-Hans", "zh-Hant"}
FREE_NUM = {"ja", "ko", "zh-Hans", "zh-Hant", "hi"}
LINE = {"ja": 18, "zh-Hans": 18, "zh-Hant": 18, "ko": 24}


def width(s):
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)


def nums(s):
    s = re.sub(r"(?<=\d)[.,    '’](?=\d)", "", s)
    return sorted(re.findall(r"\d+", s))


def wrap(p, code):
    """Two balanced lines when one is too long; CJK by characters, others at a space."""
    if code in CJK:
        n = LINE[code]
        if len(p) <= n:
            return p
        best = min(range(1, len(p)), key=lambda i: max(i, len(p) - i) + (0 if p[i - 1] in "、。，！？：；」）" else 4)
                   + (50 if p[i - 1].isdigit() and p[i].isdigit() else 0) + (50 if p[i - 1].isascii() and p[i].isascii()
                                                                            and p[i - 1].isalnum() and p[i].isalnum() else 0))
        return p[:best] + "\n" + p[best:]
    n = LINE.get(code, 42)
    if len(p) <= n:
        return p
    sp = [i for i, ch in enumerate(p) if ch == " "]
    if not sp:
        return p
    i = min(sp, key=lambda k: max(k, len(p) - k - 1) + (0 if p[k - 1] in ",.;:?!،" else 3)
            + (8 if re.match(r"\d", p[k - 1]) else 0))
    return p[:i] + "\n" + p[i + 1:]


def check(code):
    hard, soft, numnote = [], [], []
    data = json.load(open(os.path.join(SUBS, f"{code}.json")))
    if [d.get("id") for d in data] != [s["id"] for s in SRC]:
        hard.append("ids/order differ from source.json")
        return hard, soft, numnote, None
    for s, d in zip(SRC, data):
        t = d.get("text", "")
        if not t.strip() or "\n" in t:
            hard.append(f"{s['id']}: empty or contains a line break")
        for nm in NAMES:
            if re.search(rf"\b{re.escape(nm)}\b", s["en"]) and nm not in t:
                hard.append(f"{s['id']}: name '{nm}' missing")
        tn = nums(t)
        for m, k in MONTHS.items():  # "tháng 9", "9月": a month written as a number is fine
            if re.search(rf"\b{m}\b", s["en"]) and str(k) in tn and tn.count(str(k)) > nums(s["en"]).count(str(k)):
                tn.remove(str(k))
        if nums(s["en"]) != tn:
            numnote.append(f"{s['id']}: numbers {nums(s['en'])} -> {nums(t)} | {t}")
        L = width(t) / 2 if code in CJK else len(t)
        cps = L / max(s["sec"], 0.3)
        ratio = (width(t) if code in CJK else len(t)) / len(s["en"])
        lim = 13 if code in CJK else 23
        if cps > lim or (code not in CJK and ratio > 1.45):
            soft.append(f"{s['id']}: {cps:.0f} cps, x{ratio:.2f} | {t}")
    srt = "".join(f"{i}\n{tm}\n{wrap(d['text'].strip(), code)}\n\n" for i, (tm, d) in enumerate(zip(TIMES, data), 1))
    return hard, soft, numnote, srt


def main():
    codes = sys.argv[1:] or sorted(f[:-5] for f in os.listdir(SUBS) if f.endswith(".json") and f != "source.json")
    bad = False
    for c in codes:
        hard, soft, numnote, srt = check(c)
        if srt and not hard:
            open(os.path.join(PUB, f"002-captions-{c}.srt"), "w").write(srt)
        print(f"== {c}: {len(hard)} hard, {len(soft)} soft, {len(numnote)} number notes"
              + ("" if hard else f" -> 002-captions-{c}.srt"))
        for x in hard + ["soft  " + y for y in soft] + ["num   " + y for y in numnote]:
            print("   ", x)
        bad |= bool(hard)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
