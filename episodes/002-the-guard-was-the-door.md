# Episode 002 — The Guard Was the Door

**Subject:** the Bitget exchange theft (24 September 2026, UTC). About $387.5M left Bitget's hot and warm wallets in under three hours. No private key was stolen: the attacker got in through third-party *security* products, reached the wallet system and made Bitget's own signing service approve forged withdrawals.
**Angle:** the intruder was inside for at least 24 days, and the way in was a tool bought to keep intruders out.
**Status:** DRAFT v1, written 2026-11-22. Proprietarul must check it before rendering (rule 10).
**Target length:** just over 10 minutes (rule 13).
**Thomas on screen:** about 1:25 in 3 segments (intro, bridge, close). Everything else is voice-over with graphics and illustration.

Notation (same as ep. 001):
- `[THOMAS]` = Thomas on camera. `[VO]` = voice over b-roll. `[VIS]` = on screen. `[CARD]` = quote shown as text, never voiced as the real person. `[S#]` = source.
- Numbers are written as digits; the pipeline normalizes them.

**Editorial line for this episode (important):**
- **Attribution is NOT settled.** Bitget's CEO said North Korea was likely, then said this was based on preliminary indicators [S13]. Chainalysis links it to North Korea-associated actors, Elliptic says "highly likely", TRM says "likely" [S10–S12]. **No government has attributed it** [S8]. The script says exactly that, and never says "North Korea did it" or names TraderTraitor as the culprit.
- **The vendor of the hacked security products is unnamed.** No CVE, no vendor name [S8]. We do not guess.
- **Mandiant and SlowMist reports are preliminary** [S7]. Where they disagree (when the intrusion began, when the first alert fired), the script says so.

**Structure:**
- Teaser with cut-off lines, all paid off later.
- Result first, then how.
- **T-minus countdown** to 18:31 UTC on 24 September.
- Designed peak: **"seven transfers in fifteen seconds… five in nine seconds"**. Designed ending: the alarm rang, the doors were closed for customers, and the machine kept signing.

---

## Title and thumbnail options (to choose)

1. **Inside the Bitget Hack: $388 Million Out, Not a Single Key Stolen** (recommended: it matches the first 30 seconds exactly)
2. The Bitget Hack: The Intruder Who Waited 24 Days
3. How a Security Tool Let Hackers Rob Bitget of $388 Million

Thumbnail idea (from code, as in ep. 001): a security camera pointed at a vault, the vault door open behind it. Amber text: **"$388M. / NO KEY."** No real logos.

---

## 0:00 — TEASER

`[MUSIC: full]` About 13 dB under the voice. Bass hit on every cut-off line. Fade over 5 s after the last line.

`[VO]`
They didn't steal a single key. They didn't break the blockchain. They walked in through the one thing that was supposed to stop them—

`[CARD]` **"Nobody stole a key."** — DFNS analysis [S8]

`[VO]`
At 19:05, the alarm went off. Bitget froze every customer withdrawal. And the money kept leaving for another—

`[VO]`
And the first sign that someone was inside? It's in the logs. Dated twenty-four days—

`[VIS]` Hard cut to black. ~1.6 s of bass. Title fades in: **SIPHON FILES · THE GUARD WAS THE DOOR**.

---

## 0:30 — THE RESULT

`[MUSIC: out]`

`[VO]`
On the 24th of September 2026, 387 and a half million dollars left the crypto exchange Bitget. [S2]
It came out of hot and warm wallets — the ones that pay customers every day. The cold wallets weren't touched. [S1][S8]

`[VIS]` Big number card: **$387.5M** · "24 SEP 2026 · BITGET" · source [S2].

`[THOMAS]`
I'm Thomas Archer, the AI narrator of Siphon Files. Every claim in this episode has a source, and they're all in the description.
Here's the strange part. Bitget's forensic firm, Mandiant, found no evidence that a single private key was compromised. [S3]
So how do you steal 387 million dollars without the keys?
You make the exchange sign it for you.

---

## 1:05 — HOW AN EXCHANGE PAYS YOU

`[VO]`
To see how, you need to know where an exchange keeps its money.
Most of it sits in cold wallets — offline, slow, hard to reach. [S8]
Then there are warm wallets. They hold the float that keeps the next layer topped up.
And hot wallets. They pay your withdrawals automatically, around the clock. [S8]

`[VIS]` Three vaults stacked like a building: COLD (dark, sealed) · WARM · HOT (lit, doors swinging). Arrows show money moving up from cold to hot.

`[VO]`
When you press "withdraw", a request goes into a pipeline. Risk checks look at it. Then a signing service puts a cryptographic signature on it, and the money moves.
The signature is what matters. Without it, nothing leaves.
With it, anything does.

`[VO]`
Remember that. The attacker never needed the signature's secret. Only the machine that uses it.

---

## 2:00 — T-MINUS 24 DAYS

`[CARD]` **T-MINUS 24 DAYS** — bass hit, 1 s silence.

`[VO]`
The 31st of August. That's the earliest malicious activity investigators found in the logs. [S4][S7]
It wasn't inside the wallets. It was inside a security product — one of two third-party tools running in Bitget's production environment. [S3][S4]

`[VIS]` Illustration: a security appliance in a dark server room, one small red light that shouldn't be there.

`[VO]`
The investigators call them simply Product A and Product B. The vendor hasn't been named. There's no public vulnerability number. [S8]
On Product A, a flaw nobody knew about — a zero-day — let the attacker run a hidden script. [S4]

`[VO]`
A zero-day means exactly that: the people who make the product have had zero days to fix it, because they don't know it exists.
The script read a database password. It was sitting in plain text, in an environment variable. [S4][S8]

`[VO]`
Think of it as a spare key taped under the doormat — except the doormat was inside the security office.
With that password, the script connected straight to the database. [S4]

`[VO]`
The same activity turned up on a second machine on the 23rd of September. And on a third, on the 25th. [S7]

`[VO]`
One caveat. Mandiant dates the attacker's privileged access to the 24th of September. SlowMist's logs go back to the 31st of August. The two reports haven't been reconciled yet. [S7]

---

## 3:05 — THE BRIDGE

`[THOMAS]`
Let me stop here for a second.
Companies buy security products to watch the doors. They give them deep access, because that's how they see everything.
Which means if someone takes over the guard, they don't need to break any doors.
They're already standing in every corridor.

---

## 3:25 — T-MINUS 2 HOURS 24 MINUTES

`[CARD]` **T-MINUS 2 HOURS 24 MINUTES** · 24 SEP · 16:07 UTC — bass hit.

`[VO]`
At 16:07 UTC, someone logged into Product B's console. [S4][S8]

`[VO]`
Product B is described as a management platform — the kind of tool administrators use to run tasks across many machines. [S7]
They used the identity of a real Bitget employee. How they got it is still under investigation. [S8]

`[VO]`
They tried three command injections. Then they submitted code through a web execution endpoint. [S7]
Mandiant found what came next: a web shell, and a command-and-control channel back to the attacker. [S3]

`[VIS]` Corridor animation: a door labelled "B" opens, a thin amber line runs down a corridor to a door labelled "WALLET JOB SERVER".

`[VO]`
From there, they moved sideways. To the production wallet job server — the machine that builds withdrawal transactions. [S3][S8]
They installed malicious packages on it. [S3]

---

## 4:25 — T-MINUS 42 MINUTES

`[CARD]` **T-MINUS 42 MINUTES** · 17:49 UTC — bass hit.

`[VO]`
At 17:49, a tool started on the wallet host. [S7]
SlowMist later recovered it from deleted files. [S4]
It did three things. It forged the risk-control results. It built withdrawal requests. And it pushed them into Bitget's normal withdrawal process. [S4][S8]

`[VO]`
That's the whole trick.
The risk checks were reported by whoever made the request. So the tool simply said the checks had passed — checks that had never run. [S8]
And the signer signed. It produced valid signatures without verifying who was really asking. [S8]

`[VIS]` A form with three boxes: "AML ✓", "LIMIT ✓", "RISK ✓", ticked by an invisible hand. A stamp comes down: SIGNED.

---

## 5:15 — T-MINUS ZERO: 18:31

`[CARD]` **18:31 UTC** — bass hit. In Asia it's half past two in the morning. [S14]

`[MUSIC: drums]`

`[VO]`
18:31. Two tiny transfers. 93 TRX. Then 0.84 ETH. [S7]
Tests. Small enough to stay under the alert thresholds. And no alarm went off. [S7][S8]

`[VO]`
Then, nothing. For almost half an hour.

`[VO]`
18:58. 34.75 million USDT leaves in one transfer. [S7]

---

## 5:55 — THE PEAK

`[MUSIC: full]` (vault_run piece or a new one)

`[VO]`
19:01. Seven transfers. Five blockchains. Fifteen seconds. [S7][S8]

`[VIS]` Five chain columns light up one after another; each transfer is a streak of light leaving a lit tower.

`[VO]`
19:05. Bitget's reconciliation finally flags the gap. Risk control blocks withdrawals for every customer on the platform. [S7]
19:14. Highest-level emergency. [S7]

`[MUSIC: out]` — 1 s silence.

`[VO]`
19:16.
Five transfers. Five chains. Nine seconds.
About 203 million dollars, mostly from the warm wallets. [S7][S8]

`[VO]`
The customers had been locked out eleven minutes earlier.
The attacker hadn't. [S8]

`[VO]`
Why the warm wallets? Because that's where the bigger float sits — the reserve that refills the hot wallets.
Two wallets that Bitquery treats as warm sent out about 55 percent of everything that was taken. [S6][S7]
And there was no extra approval step between a request and a signature on that tier. No second person. No list of allowed destinations. On each Ethereum-style chain, the money went to one fresh address. [S8]

---

## 6:50 — WHY IT DIDN'T STOP

`[VO]`
Blocking customer withdrawals was the wrong switch. The forged requests weren't customer withdrawals.
The signing service kept running for 2 hours and 39 minutes after the first alert. [S7][S8]
By one estimate, about 60 percent of the money left after the alarm had already sounded. [S8]

`[VO]`
At 20:40, Bitget started sweeping funds into cold storage. At that point, it still couldn't rule out that keys had been taken. [S7]
The last traced transfer left at 21:23. [S7]
After 21:22, the attacker tried to rewrite withdrawal records directly in the database. Two fake Bitcoin orders returned errors. [S4][S7]
At 21:44, Bitget shut down the withdrawal services, signing included. [S7]

`[VO]`
The next morning, at 08:43, Bitget says it found the root cause. At 13:42, it reported the theft to law enforcement. [S7][S8]
It put up a recovery bounty: 5 percent of anything recovered or frozen, for whoever helps. [S14]
And it brought in two outside teams: Mandiant, part of Google Cloud, and the blockchain security firm SlowMist. [S13]

`[VIS]` A clock face: 18:31 → 21:23. Text: **2 h 52 min**.

---

## 7:45 — THE FINGERPRINT NOBODY WATCHED

`[VO]`
There was a tell, hiding in plain sight.
Every blockchain transfer sets a fuel limit — gas. Bitget's normal customer payouts used about 63 thousand.
The attacker's transfers used exactly 100 thousand, or 200 thousand. [S8]
Out of 35,678 transactions that week, no other transaction did that. [S8]

`[VO]`
And every forged command was deleted after each transfer. [S8]

---

## 8:15 — WHERE THE MONEY WENT

`[VO]`
The stablecoins went first, because stablecoins can be frozen.
All 34.75 million USDT was swapped for ETH within 20 minutes. [S7][S8]
The XRP — more than 40 percent of the haul — was moved to Bitcoin through THORChain. [S7]
Part of the Zcash went into a private pool, where it can't be followed. [S7]

`[VO]`
The ETH was parked in eight wallets. Six of them held exactly 10,000 ETH each. [S7]
Within days, most of it started moving — into THORChain for Bitcoin, and through other bridges to other chains. [S7]
The BNB and TRX were turned into Bitcoin within a day. [S7]

`[VO]`
Bitget asked THORChain to block the addresses. THORChain declined, citing its permissionless design. [S7][S13]

`[VO]`
In the end, about 1.1 million dollars was frozen.
Less than 0.3 percent. [S7][S8]

`[CARD]` Bitget's CEO said she was not expecting to recover much. — CNBC [S9] *(paraphrase on screen, not a quote)*

---

## 8:55 — WHO?

`[VO]`
So who did this?
On the night of the hack, Bitget's CEO, Gracy Chen, said the pattern looked like North Korea's work. She pointed to IP addresses matching VPN services used before by a North Korean group. [S14][S19]

`[CARD]` **"The pattern looks very much like what the North Korean team did before."** — Gracy Chen, X livestream [S19]

`[VO]`
Four days later, she was more careful. What she'd shared, she said, was based on preliminary indicators. [S13]

`[VO]`
The blockchain analytics firms lean the same way.
Chainalysis links the theft to actors associated with North Korea. Elliptic calls it highly likely. TRM Labs calls it likely. [S10][S11][S12]
Some of the laundering ran through wallets that earlier moved money stolen from Bybit. [S11][S12]

`[VO]`
The investigator ZachXBT reported that one of the launderers had also moved funds from the Kelp DAO exploit in April. [S7]
Kelp, Drift, Bitget. Three big thefts in under six months, all leaning the same way in the analysts' reports. [S19]

`[VO]`
But no government has attributed the Bitget hack. [S8]
And Mandiant's report makes no attribution at all. [S7]

---

## 9:35 — THE PATTERN

`[THOMAS]`
Here's what we can say.
In 2025, Bybit lost one and a half billion dollars. The FBI blamed North Korea. And the method was the same idea: don't steal the key — change what the signer believes it's signing. [S12]
A month after Bitget, Binance lost more than six billion. The FBI named North Korea's TraderTraitor group within days. [S17]
For Bitget, that confirmation hasn't come.

---

## 10:00 — CLOSE

`[MUSIC: memory piano, low]`

`[VO]`
Customers didn't lose money. Bitget covered the loss from its protection fund. [S2][S18]
That fund is the reason this story isn't about ruined customers. The loss landed on the company, not on the people with money on the exchange.
Bitcoin withdrawals reopened on the 28th of September. Everything was back by the 2nd of October. [S7][S8]
The vulnerability is patched, and the vendor's feature is switched off. [S8]

`[VO]`
Bitget says it has restricted internal access, added independent verification for withdrawals, and stepped up monitoring for unusual activity. [S13]
Critical operations now need more than one approval. [S8]
In other words, a request on its own should no longer be enough.
The vendor still hasn't been named. [S8]

`[THOMAS]`
Bitget bought tools to guard the door.
For at least twenty-four days, someone else was holding them.
And when the alarm finally rang, the exchange locked out its customers — and left the signing machine running.
I'm Thomas Archer. This was Siphon Files.

`[VIS]` End card (as ep. 001): subscribe, ep. 001 Drift as the linked video.

---

## Sources

- [S1] Bitget, *Security Notice: Bitget exchange hot wallets Incident*, 24 Sep 2026: https://www.bitget.com/support/articles/12560603896024
- [S2] Bitget Academy, *Bitget Hack Explained: Timeline, Impact and Security Response*, 27 Sep 2026, updated 3 Oct 2026: https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response
- [S3] Mandiant (Google Cloud), *Bitget Incident Response Status Report*, dated 28 Sep 2026, published 30 Sep 2026: https://img.bgstatic.com/multiLang/events/MFR26-1029_Status_Update_Bitget_0930.pdf
- [S4] SlowMist, *Investigation Progress Report on Bitget*, as of 29 Sep 2026: https://github.com/slowmist/Knowledge-Base/blob/master/open-report-V2/incident-response/SlowMist%20Investigation%20Progress%20Report%20-%20Bitget_en-us.pdf
- [S5] Bitget, *Update On SlowMist and Mandiant Report*, 30 Sep 2026: https://www.bitget.com/support/articles/12560603896305
- [S6] Bitquery Research, *Bitget hack: how $387M left, and where it is now*, updated 30 Sep 2026: https://bitquery.io/investigations/bitget-hack
- [S7] Halborn, *The Bitget Hack: a CISO's Technical Analysis*, 8 Oct 2026: https://www.halborn.com/blog/post/bitget-hack-technical-analysis-september-2026
- [S8] DFNS, *The Bitget Hack*, 14 Oct 2026: https://dfns.co/article/the-bitget-hack
- [S9] CNBC, *Bitget not expecting to recover a lot from $388 million hack, CEO tells CNBC*, 2 Oct 2026: https://www.cnbc.com/2026/10/02/bitget-crypto-stolen-hack-recovery.html
- [S10] Decrypt, *Chainalysis Used AI to Trace the $387M Bitget Hack Back to North Korea*, 3 Oct 2026: https://decrypt.co/380005/chainalysis-ai-87m-bitget-hack-north-korea
- [S11] Elliptic, *Bitget attack pushes suspected North Korea crypto heists over $1 billion in 2026*, 25 Sep 2026: https://www.elliptic.co/insights/bitget-attack-pushes-suspected-north-korea-crypto-heists-over-1-billion-in-2026/
- [S12] TRM Labs, *Bitget Loses USD 351.6 Million in Hot Wallet Breach in Likely North Korea Attack*, 25 Sep 2026: https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack
- [S13] Cointelegraph, *Bitget CEO says $388M hack exploited third-party security vulnerability*, 28 Sep 2026: https://cointelegraph.com/news/bitget-388m-hack-third-party-security-vulnerability
- [S14] BleepingComputer, *Bitget hacked via zero-day in third-party security products*: https://bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products
- [S15] Wu Blockchain via ChainCatcher, transcript of the Bitget CEO AMA (28 Sep 2026): https://www.chaincatcher.com/en/article/2292843
- [S16] Bitget, *Security Incident Official Progress Update*, last updated 4 Oct 2026: https://www.bitget.com/campaigns/bitget-security-incident-2026
- [S17] BleepingComputer, *FBI links $6.3 billion Binance crypto heist to North Korean hackers*, 1 Nov 2026: https://www.bleepingcomputer.com/news/security/fbi-links-63-billion-binance-crypto-heist-to-north-korean-hackers/
- [S18] Tom's Hardware, *North Korea named as primary suspect in $387 million Bitget crypto hack*: https://www.tomshardware.com/tech-industry/cryptocurrency/north-korea-named-as-primary-suspect-in-usd387-million-bitget-crypto-hack-investigators-identify-ip-addresses-tied-to-vpn-infrastructure-previously-used-by-north-korean-hacker-groups-thieves-swapped-stablecoins-for-eth-in-minutes-to-dodge-freezes
- [S19] Cointelegraph, *Bitget CEO suspects North Korea behind $352M hack, citing IP clues*, 25 Sep 2026: https://cointelegraph.com/news/bitget-ceo-suspects-north-korea-behind-352m-hack-citing-ip-clues

---

## Notes for proprietarul's check

- **Correction to what I told you in chat:** the drain lasted **2 h 52 min** (18:31–21:23 UTC), not "34 minutes"; the dwell time is **at least 24 days** (31 Aug → 24 Sep), not 25. The script uses the sourced figures.
- **Loss figures:** $351.6M (first count, 24 Sep), $387.5M (revised next day, adds Zcash and TRON), "about $388M across 12 wallets / 11 chains" (Bitget). Bitquery traced $386.8M across 23 transfers on 9 chains. The script uses **$387.5M** spoken, **$388M** in the title.
- **Times are UTC** (Halborn's reconstruction from Bitget, SlowMist and Bitquery). BleepingComputer gives the same window in UTC+8 (02:31–05:23), which is why the 18:31 card says "half past two in the morning in Asia".
- **Conflicts kept visible in the script:** start of the intrusion (Mandiant 24 Sep vs SlowMist 31 Aug); when the first alert fired (Mandiant background 18:31 vs Bitget's CEO 19:05). The script says "no alarm went off" for the 18:31 tests, quoting the CEO [S7]; Halborn flags the conflict.
- **"About 60%" after the alarm** is an estimate (DFNS ~60%, Halborn 61%), worded as "by one estimate".
- **Gas-limit tell and "forged commands deleted"** come from DFNS's own analysis of the reports [S8]. Worded as fact in the draft; we can soften to "according to one analysis" if you prefer.
- **Protection fund:** Tom's Hardware gives "over $464M" for the fund before the hack; DFNS says Bitget refilled it above $300M afterwards. The script avoids both numbers and only says the loss was covered.
- **CEO quote card:** from her X livestream, reported by Cointelegraph [S19]; 12 words, shown as text only.
- **To re-check before rendering:** any government attribution, vendor name or CVE published after 22 Nov; the final Mandiant report.

---

## Length (estimate)

- Spoken text: **1,554 words** (automatic count, cards and visual cues excluded). Target: ~1,600 words → about 9:40 at ~165 wpm, plus countdown cards, pauses, music beats and the end card ≈ **~10:40**. If the voice runs fast (~196 wpm measured), slow the pace rather than add text (same rule as ep. 001).
- Thomas on screen: intro ~0:30 + bridge ~0:20 + pattern ~0:25 + close ~0:20 ≈ **~1:35**.
