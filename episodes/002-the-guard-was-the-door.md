# Episode 002 — The Guard Was the Door

**Title (decided 22 Nov 2026): Inside the $388M Bitget Hack** · thumbnail text: **NO KEY WAS STOLEN**
**Before publishing: YouTube Test & Compare** with (A) this title + "NO KEY WAS STOLEN", (B) "They Stole $388,000,000 Without a Single Key" + "THE GUARD LET THEM IN", (C) "The Exchange That Froze Its Customers, Not the Thief" + "$388M. NO KEY." (CLAUDE.md section 9; reasoning in `research/title-psychology.md`).

**Subject:** the Bitget exchange theft (24 September 2026, UTC). About $388M left Bitget's hot and warm wallets in under three hours. Bitget says no private key was compromised: the attacker got in through third-party *security* products, reached the wallet system and made Bitget's own signing service approve forged withdrawals.
**Angle:** the way in was a tool bought to keep intruders out. The exchange that once rescued Bybit was robbed the same way, and its stolen money later helped investigators name who robbed Binance.
**Status:** DRAFT v3, written 2026-11-22. Same verified facts as v2, rebuilt for suspense after the research in `research/suspense-storytelling.md` (see "Changes from v2" at the end). Proprietarul must check it before rendering (rule 10).
**Target length:** just over 10 minutes (rule 13).
**Thomas on screen:** about 1:15 in 4 segments (intro, bridge, the loan, close); more can be added later with lip re-sync on VO lines, as in ep. 001.
**Length:** 1,577 spoken words (automatic count, cards and cues excluded; v2 had 1,540), Thomas 209 words → about 10:40–11:00 with the countdown cards, pauses, music beats and end card.

Notation (same as ep. 001):
- `[THOMAS]` = Thomas on camera. `[VO]` = voice over b-roll. `[VIS]` = on screen. `[CARD]` = quote shown as text, never voiced as the real person. `[S#]` = source.
- Numbers are written as digits; the pipeline normalizes them.

**Editorial line for this episode (important):**
- **Attribution is NOT settled for Bitget.** The CEO said it looked like North Korea, then said that was based on preliminary indicators [S13]. Chainalysis, Elliptic and TRM lean to North Korea [S10–S12]. **No government has attributed the Bitget hack** [S8]; the FBI's attribution covers Binance, not Bitget [S17][S25]. The script never says "North Korea did it" or names TraderTraitor as Bitget's attacker.
- **The vendor of the hacked security products is unnamed.** No CVE, no vendor name [S8][S16]. We do not guess.
- **"No key stolen" is Bitget's finding.** Mandiant's report says Bitget did not observe evidence of key compromise [S3]; Bitget says key compromise "has been ruled out" [S2]. The script attributes it to Bitget.
- **The employee whose identity was used is not a suspect.** Bitget's CEO said internal collusion was initially excluded [S15]. The script says so.
- **Mandiant and SlowMist reports are preliminary** [S3][S4]. Where they disagree (when the intrusion began, when the first alert fired), the script says so.
- Deductions from one analysis (DFNS) are worded "according to one analysis" [S8].
- **Second person ("if you had money on Bitget…") is used only for what a customer actually saw:** withdrawals blocked at 19:05, back by 2 October [S2]. No invented people, no invented scenes.

**Structure (v3, after `research/suspense-storytelling.md`):**
- Shape: "man in a hole" with a sting. Bitget the rescuer → robbed → covers its customers (rise) → but the money keeps moving and the thief has no official name (sting).
- First line = a small concrete image (a test transfer at 02:31 in Asia). The big number comes after.
- Knowledge gap: from 31 August *we* know someone is inside; Bitget doesn't. The T-minus acts remind the viewer of it.
- Every section ends on a new problem or a question ("but" / "so"), never on a conclusion.
- Planted before the peak, paid after: the fingerprint in the test transfers; the 40,000 ETH loan.
- Designed peak: **"seven transfers in fifteen seconds… five in nine seconds"**, seen from the side of a locked-out customer. Second race at ~6:20: the alarm rang, and the machine kept signing.
- Designed ending: back to the opening test transfer; customers whole, the money still moving, no government name.
- Proposed YouTube chapters (scenes/questions): The test · How an exchange pays you · Someone inside · A borrowed name · 18:31 · Locked out · Why didn't it stop? · The tell · Where did it go? · Who? · The loan · Afterwards.

---

## 0:00 — TEASER

`[MUSIC: full]` About 13 dB under the voice. Bass hit on every cut-off line. Fade over 5 s after the last line.

`[VIS]` Black. One line of a block explorer types itself out: **93 TRX · 18:31:xx UTC**.

`[VO]`
Half past two in the morning, in Asia. A tiny transfer leaves the crypto exchange Bitget. Nobody looks at it.

`[VO]`
Less than three hours later, about 388 million dollars is gone. And Bitget says not a single key was stolen.

`[CARD]` **"Nobody stole a key."** — DFNS analysis [S8]

`[VO]`
At 19:05, the alarm went off. Bitget froze every customer withdrawal. And the money kept leaving for another two hours.

`[VO]`
And the first sign that someone was inside? It's in the logs. Dated twenty-four days earlier.

*(Generated with full stops, as ep. 001; the cut is made in the edit, on the bass hit, before the last words.)*

`[VIS]` Hard cut to black. ~1.6 s of bass. Title fades in: **SIPHON FILES · THE GUARD WAS THE DOOR**.

---

## 0:35 — THE RESCUER

`[MUSIC: out]`

`[VO]`
To understand why this one hurts, go back nineteen months.
February 2025. The exchange Bybit has just lost one and a half billion dollars. The FBI blames North Korea. [S31]
Customers are rushing to pull their money out. [S28]

`[VO]`
That same day, a rival sends help. Bitget lends Bybit 40,000 ether to keep its withdrawals running. No interest. No collateral. [S27][S28]

`[VIS]` Two towers at night; one dark, one lit. A line of light runs from the lit tower to the dark one: **40,000 ETH · 21 FEB 2025**.

`[VO]`
Remember that loan. It comes back at the end.

`[VO]`
On the 24th of September 2026, the exchange that came to help became the one robbed. [S2]
At the time, the biggest crypto theft of the year. [S29]

`[VIS]` Big number card: **$388M** · "24 SEP 2026 · BITGET" · source [S2].

`[THOMAS]`
I'm Thomas Archer, the AI narrator of Siphon Files. Every claim in this episode has a source, and they're all in the description.
Here's the strange part. Bitget says not a single private key was compromised. [S2][S3]
So how do you steal 388 million dollars without the keys?
You make the exchange sign it for you.

---

## 1:35 — HOW AN EXCHANGE PAYS YOU

`[VO]`
An exchange keeps most of its money in cold wallets — offline, slow, hard to reach. Those weren't touched. [S2]
Warm wallets hold a reserve. Hot wallets pay your withdrawals automatically, around the clock. [S8]

`[VIS]` Three vaults stacked like a building: COLD (dark, sealed) · WARM · HOT (lit, doors swinging). Arrows show money moving up from cold to hot.

`[VO]`
When you press "withdraw", a request goes into a pipeline. Risk checks look at it. Then a signing service puts a cryptographic signature on it, and the money moves.
Without that signature, nothing leaves.
With it, anything does.

`[VO]`
So the attacker never needed the secret behind the signature.
They needed to get close to the machine that uses it.
And for that, they needed a way in that nobody would watch.

---

## 2:15 — T-MINUS 24 DAYS

`[CARD]` **T-MINUS 24 DAYS** — bass hit, 1 s silence.

`[VO]`
The 31st of August. That's the earliest malicious activity investigators found in the logs. [S4][S7]
Not inside the wallets. Inside a security product — one of two third-party tools Bitget ran to protect its systems. [S3][S4]

`[VIS]` Illustration: a security appliance in a dark server room, one small red light that shouldn't be there.

`[VO]`
The investigators call them Product A and Product B. The vendor hasn't been named. [S8]
On Product A, a flaw nobody had found yet — a zero-day — let the attacker run a hidden script. [S4]
The script found a database password, sitting in plain text. [S4][S8]
A spare key taped under the doormat — except the doormat was inside the security office.

`[VO]`
From here on, we know someone is inside.
Bitget doesn't. [S4][S7]

`[VO]`
One caveat. Mandiant dates the attacker's privileged access only to the 24th of September. The two reports haven't been reconciled. [S3][S7]

`[VO]`
But a hidden script on a guard's machine can't move money.
To get near the wallets, they needed something else.
A name. A real one.

---

## 3:15 — THE BRIDGE

`[THOMAS]`
Let me stop here for a second.
Companies buy security products to watch the doors. They give them deep access, because that's how they see everything.
Which means if someone takes over the guard, they don't need to break any doors.
They're already standing in every corridor.

---

## 3:35 — T-MINUS 2 HOURS 24 MINUTES

`[CARD]` **T-MINUS 2 HOURS 24 MINUTES** · 24 SEP · 16:07 UTC — bass hit.

`[VO]`
The same script had spread. A second machine on the 23rd of September. A third, the night of the theft. [S4][S7]
At 16:07 UTC, someone logged into Product B's management platform. [S4][S7]
With the identity of a real Bitget employee. [S15]

`[VO]`
That person wasn't there. Bitget says the credentials were stolen through the zero-day, and that it has ruled out, for now, anyone on the inside. [S15]

`[VIS]` Corridor animation: a door labelled "B" opens with a staff badge, a thin amber line runs down a corridor to a door labelled "WALLET JOB SERVER".

`[VO]`
Mandiant found a web shell on appliance B, and a channel back to the attacker. [S3]
From there, they moved sideways, to the production wallet job server — the machine that builds withdrawal transactions. And installed malicious packages on it. [S3]

`[VO]`
Now they were standing next to the money.
But every withdrawal still had to get past one more thing. Risk control.

---

## 4:25 — T-MINUS 42 MINUTES

`[CARD]` **T-MINUS 42 MINUTES** · 17:49 UTC — bass hit.

`[VO]`
At 17:49, a tool started on the wallet host. SlowMist later recovered it from deleted files. [S4][S7]
It didn't fight risk control. It forged its answers. [S4][S7]
Then it built withdrawal requests, and pushed them into Bitget's normal withdrawal process. [S4][S7]

`[VIS]` A form with three boxes: "AML ✓", "LIMIT ✓", "RISK ✓", ticked by an invisible hand. A stamp hovers over it, not yet down.

`[VO]`
According to one analysis, the system simply took the requester's word that the checks had passed. [S8]
On paper, that was enough.
There was only one way to find out if it worked in practice.
Try it.

---

## 5:05 — 18:31

`[CARD]` **18:31 UTC** — bass hit. In Asia it's half past two in the morning. [S3]

`[MUSIC: drums]`

`[VO]`
18:31. Two tiny transfers. 93 TRX. Then 0.84 ETH. [S6]
Tests. Bitget's CEO says they were below the risk threshold, so no alert went off. [S15]

`[VIS]` The stamp comes down: SIGNED.

`[VO]`
And there was something odd about these transfers. Something that could have given them away. Hold on to it.

`[VO]`
Then, nothing. For almost half an hour.
18:58. 34.75 million USDT leaves in one transfer. [S6]
Still no alarm.
So they stopped testing.

---

## 5:45 — LOCKED OUT

`[MUSIC: full]` (vault_run piece or a new one)

`[VO]`
19:01. Seven transfers. Five blockchains. Fifteen seconds. [S6]

`[VIS]` Five chain columns light up one after another; each transfer is a streak of light leaving a lit tower.

`[VO]`
19:03. One more small test, from a different wallet. [S6][S8]
19:05. Bitget's reconciliation finally flags the gap. [S2]

`[VO]`
If you had money on Bitget at that moment, this is what you saw: your withdrawal stopped. Risk control had blocked withdrawals for every customer on the platform. [S2]
19:14. Highest-level emergency. [S2]

`[MUSIC: out]` — 1 s silence.

`[VO]`
19:16.
Five transfers. Five chains. Nine seconds.
About 203 million dollars. [S6]

`[VO]`
The customers had been locked out eleven minutes earlier.
The attacker hadn't.

---

## 6:30 — WHY DIDN'T IT STOP?

`[VO]`
Blocking customer withdrawals was the wrong switch. The forged requests weren't customer withdrawals.
According to one analysis, on the warm wallets nothing stood between a request and a signature. No second person. No list of allowed destinations. [S8]
So the signing service kept running. For 2 hours and 39 minutes after the first alert. [S2][S8]

`[VIS]` Split screen: left, a customer's app with a grey "Withdrawals suspended" banner; right, the SIGNED stamp coming down again and again.

`[VO]`
Two separate estimates put the money that left after the alarm at about 238 million dollars. More than half of the theft. [S7][S20]

`[VO]`
At 20:40, Bitget started moving funds into cold storage — still not sure whether keys had been taken. [S2][S7]
The last traced transfer left at 21:23. [S6]
Then the attacker tried to rewrite withdrawal records directly in the database. Covering tracks, or going for more — the reports don't say. Two fake Bitcoin orders returned errors. [S4][S7]
At 21:44, Bitget shut down the withdrawal services, signing included. [S2]

`[VIS]` A clock face: 18:31 → 21:23. Text: **2 h 52 min**.

`[VO]`
The next morning, Bitget found the root cause and reported the theft to law enforcement. [S2]
And when investigators went back to those first test transfers, the odd detail was right there.

---

## 7:30 — THE TELL

`[VO]`
Every Ethereum transfer sets a fuel limit — gas. Bitget's normal customer payouts used about 63 thousand.
The attacker's transfers used exactly 100 thousand, or 200 thousand. [S6]
In the eight days before, those wallets sent 35,678 transactions. Not one customer payout did that. [S6]

`[VO]`
On Zcash, it was even louder. Each stolen transfer pulled together about a thousand pieces of coin. The wallet's biggest transaction before that had used 54. [S7]
The forged commands were deleted after each transfer. [S8][S16]
The fingerprints weren't. Nobody was watching for them.

`[VO]`
Now the thief had 388 million dollars. And a new problem: how to keep it.

---

## 8:10 — WHERE DID IT GO?

`[VO]`
The stablecoins went first, because stablecoins can be frozen. All the USDT was swapped for ETH within 20 minutes. [S7]
The XRP went to Bitcoin through THORChain. Part of the Zcash disappeared into a private pool, where it can't be followed. [S6]

`[VIS]` Flow map: ETH parked in eight holding wallets, six with exactly 10,000 ETH each [S7]; XRP → THORChain → BTC; ZEC → private pool.

`[VO]`
Bitget asked THORChain to block the addresses. THORChain declined, citing its permissionless design. [S7]
In the end, less than 0.3 percent was frozen. [S7][S9]

`[VO]`
In November, the Bitcoin started moving again. About 161 million dollars in eleven days, most of it through CoinJoin, which mixes many people's coins into one transaction. [S21][S22]

`[VO]`
And the people moving it weren't hiding very well.
ZachXBT says the launderers asked for customer support in the public chats of the services they were using. Failed swaps. Missing payouts. [S23][S30]
He says one of them had handled stolen money before. From the Kelp DAO exploit in April. [S23]

---

## 9:00 — WHO?

`[VO]`
So who was behind it?
On the night of the hack, Bitget's CEO, Gracy Chen, said some IP addresses matched VPN services used by a North Korean group. [S19]

`[CARD]` **"The pattern looks very much like what the North Korean team did before."** — Gracy Chen, X livestream [S19]

`[VO]`
Four days later, she was more careful. That, she said, was based on preliminary indicators. [S13]
Chainalysis, Elliptic and TRM Labs all lean the same way. [S10][S11][S12]

`[VO]`
Then, five weeks later, Binance lost more than six billion dollars.
And Chainalysis watched the stolen Binance money meet the Bitget money on the blockchain. [S24]
ZachXBT says both arrived, through THORChain, at the same address. [S26]
Two days after the Binance theft, the FBI named the thieves: North Korea's TraderTraitor. [S17][S25]

`[VO]`
For Bitget, no government has said a word. And Mandiant's report names no one at all. [S3][S8]
Which brings us back to that loan.

---

## 9:55 — THE LOAN

`[THOMAS]`
In February 2025, when Bybit was robbed, Bitget sent 40,000 ether the same day. No interest. No collateral.
The FBI blamed that theft on North Korea.
Nineteen months later, the money was leaving Bitget.
No government has named anyone. But the analysts point the same way.

---

## 10:20 — AFTERWARDS

`[MUSIC: memory piano, low]`

`[VO]`
If you had money on Bitget, you didn't lose it. Bitget says it covered the loss from its own protection fund. [S2][S16]
Every withdrawal was back by the 2nd of October. [S2]
The fund has been rebuilt to just over 300 million dollars. Still less than before. [S2][S16]

`[VO]`
The vulnerability is fixed. Critical operations now need more than one approval. [S2][S16]
And Bitget says it is reviewing how it picks its security vendors. The vendor still hasn't been named. [S2][S16]

`[THOMAS]`
It started with a transfer of 93 TRX, at half past two in the morning. Nobody looked at it.
Bitget bought tools to guard the door. For weeks, someone else may have been holding them.
And when the alarm finally rang, the exchange locked out its customers — and left the signing machine running.
I'm Thomas Archer. This was Siphon Files.

`[VIS]` End card (as ep. 001): subscribe, ep. 001 Drift as the linked video.

---

## Sources

- [S1] Bitget, *Security Notice: Bitget exchange hot wallets Incident*, 24 Sep 2026: https://www.bitget.com/support/articles/12560603896024
- [S2] Bitget Academy, *Bitget Hack Explained: Timeline, Impact and Security Response* (UTC timeline, "final verified figure", 12 addresses, 11 chains, 13 assets, remediation, bounty): https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response
- [S3] Mandiant (Google Cloud), *Bitget Incident Response Status Report*, dated 28 Sep 2026 (preliminary; times in UTC+8): https://img.bgstatic.com/multiLang/events/MFR26-1029_Status_Update_Bitget_0930.pdf
- [S4] SlowMist, *Investigation Progress Report on Bitget*, as of 29 Sep 2026: https://github.com/slowmist/Knowledge-Base/blob/master/open-report-V2/incident-response/SlowMist%20Investigation%20Progress%20Report%20-%20Bitget_en-us.pdf (direct reading blocked for us; findings checked through S7 and The Hacker News, https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html)
- [S5] Bitget, *Update On SlowMist and Mandiant Report*, 30 Sep 2026: https://www.bitget.com/support/articles/12560603896305
- [S6] Bitquery Research, *Bitget hack: how $387M left, and where it is now* (23 transfers incl. 3 tests, bursts, gas limits, XRP route, Zcash pool): https://bitquery.io/investigations/bitget-hack
- [S7] Halborn, *The Bitget Hack: a CISO's Technical Analysis*, 8 Oct 2026 (UTC reconstruction, $238M after the alarm, laundering, THORChain refusal, frozen total): https://www.halborn.com/blog/post/bitget-hack-technical-analysis-september-2026
- [S8] DFNS, *The Bitget Hack*, 14 Oct 2026 (own analysis tagged separately from reported facts): https://dfns.co/article/the-bitget-hack
- [S9] CNBC, *Bitget not expecting to recover a lot from $388 million hack, CEO tells CNBC*, 2 Oct 2026: https://www.cnbc.com/2026/10/02/bitget-crypto-stolen-hack-recovery.html
- [S10] Decrypt, *Chainalysis Used AI to Trace the $387M Bitget Hack Back to North Korea*, 3 Oct 2026: https://decrypt.co/380005/chainalysis-ai-87m-bitget-hack-north-korea
- [S11] Elliptic, *Bitget attack pushes suspected North Korea crypto heists over $1 billion in 2026*, 25 Sep 2026: https://www.elliptic.co/insights/bitget-attack-pushes-suspected-north-korea-crypto-heists-over-1-billion-in-2026/
- [S12] TRM Labs, *Bitget Loses USD 351.6 Million in Hot Wallet Breach in Likely North Korea Attack*, 25 Sep 2026: https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack
- [S13] Cointelegraph, *Bitget CEO says $388M hack exploited third-party security vulnerability*, 28 Sep 2026: https://cointelegraph.com/news/bitget-388m-hack-third-party-security-vulnerability
- [S14] BleepingComputer, *Bitget hacked via zero-day in third-party security products*, 30 Sep 2026: https://bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products
- [S15] Wu Blockchain via ChainCatcher, transcript of the Bitget CEO AMA, 28 Sep 2026 (credentials stolen via the zero-day; tests below the risk threshold, no alert; internal collusion initially excluded): https://www.chaincatcher.com/en/article/2292843
- [S16] Bitget, *Security Incident Official Progress Update*, last updated 13 Oct 2026 (vulnerability fixed, vendor notified and unnamed, fund $314M+ / 3,705 BTC): https://www.bitget.com/campaigns/bitget-security-incident-2026
- [S17] BleepingComputer, *FBI links $6.3 billion Binance crypto heist to North Korean hackers*, 1 Nov 2026: https://www.bleepingcomputer.com/news/security/fbi-links-63-billion-binance-crypto-heist-to-north-korean-hackers/
- [S18] Tom's Hardware, *North Korea named as primary suspect in $387 million Bitget crypto hack*: https://www.tomshardware.com/tech-industry/cryptocurrency/north-korea-named-as-primary-suspect-in-usd387-million-bitget-crypto-hack-investigators-identify-ip-addresses-tied-to-vpn-infrastructure-previously-used-by-north-korean-hacker-groups-thieves-swapped-stablecoins-for-eth-in-minutes-to-dodge-freezes
- [S19] Cointelegraph, *Bitget CEO suspects North Korea behind $352M hack, citing IP clues*, 25 Sep 2026 (X livestream quotes): https://cointelegraph.com/news/bitget-ceo-suspects-north-korea-behind-352m-hack-citing-ip-clues
- [S20] BeInCrypto, *Bitget CEO Talks About the $387 Million Hack* (Certora estimate: ~$238M after the first block): https://beincrypto.com/bitget-hack-ceo-interview-gracy-chen/
- [S21] Arkham Research, *Bitget Hacker Moves Millions in BTC to New Wallets*, 16 Nov 2026: https://arkm.com/research/bitget-hacker-moves-millions-in-btc-to-new-wallets-on-chain-data
- [S22] TokenPost, *Wallets Tied to Bitget Hack Move 2,266.68 Bitcoin (BTC) in 11 Days*, 16 Nov 2026 (Arkham data: $161.04M, mostly mixers/CoinJoin): https://www.tokenpost.com/news/investing/59038
- [S23] BeInCrypto, *Investigator Finds $387M Bitget Hack Suspects Asking for Help in Public Chats*, 28 Sep 2026 (ZachXBT; Kelp DAO link not independently confirmed): https://beincrypto.com/bitget-hack-launderers-public-discord-chats/
- [S24] Chainalysis, *The $6.4 Billion Binance Hack: Tracing the North Korea Link* (Binance funds commingled on-chain with Bitget funds): https://chainalysis.com/blog/binance-exploit-latest-findings-and-response/
- [S25] South China Morning Post, *FBI blames North Korea for stolen billions from Binance*, 31 Oct 2026: https://scmp.com/news/world/united-states-canada/article/3372858/fbi-blames-north-korea-stolen-billions-binance-biggest-hack-history
- [S26] Coin Edition, *Chainalysis Flags Never-Seen-Before Laundering Tactics in Binance Hack*, 30 Oct 2026 (ZachXBT: both hacks' funds reached one address via THORChain): https://coinedition.com/chainalysis-flags-never-seen-before-laundering-tactics-in-binance-hack/
- [S27] Cointelegraph, *Bybit repays Bitget's 40,000 ETH loan after $1.4B hack*, 25 Feb 2025 (no interest, no collateral, per Bitget's CEO): https://cointelegraph.com/news/bybit-repays-bitget-loan-after-hack
- [S28] Bitcoinist, *Bybit turns to Bitget and Binance for ETH loan* (Arkham: 40,000 ETH sent on 21 Feb 2025, 19:44 UTC): https://bitcoinist.com/bybit-turns-to-bitget-and-binance-for-239-million-eth-loan-amid-withdrawal-spike/
- [S29] Yahoo Finance (Decrypt), *Bitget Hack Losses Climb to $387M* ("believed to be the biggest crypto hack of the year"; Drift $285M, Kelp DAO $292M and Liquid Network ~$320M were smaller): https://finance.yahoo.com/markets/crypto/articles/bitget-hack-losses-climb-387m-170857616.html
- [S30] The Crypto Times, *ZachXBT Exposes 5 Launderers Moving $387.5M Bitget Hack Funds*, 28 Sep 2026 (help requests over failed XRP-to-Bitcoin swaps and missing payouts): https://www.cryptotimes.io/2026/09/28/zachxbt-exposes-5-launderers-moving-387-5m-bitget-hack-funds-for-north-korea/

---
- [S31] FBI, PSA *North Korea Responsible for $1.5 Billion Bybit Hack*, 26 Feb 2025: https://www.ic3.gov/PSA/2025/PSA250226

---

## Notes for proprietarul's check

- **Loss figure:** $351.6M (first count, 24 Sep) → $387.5M (25 Sep) → **"about $388M, final verified figure"** (Bitget, 12 addresses, 11 chains, 13 assets). v2 says "about 388 million" everywhere, so the voice matches the title. Bitquery traced $386.8M in 23 transfers on 9 chains.
- **Number of transfers:** sources differ (CEO: 19 or 17 large; Bitquery: 23 including 3 tests). The script never states a total.
- **Times are UTC** (Bitget Academy, Bitquery, Halborn). Mandiant and SlowMist use UTC+8, which is why the 18:31 card says "half past two in the morning in Asia".
- **Conflicts kept visible:** start of the intrusion (Mandiant 24 Sep vs SlowMist 31 Aug); first alert (Mandiant background: detection at 02:31 UTC+8 = 18:31 UTC; Bitget and the CEO: no alert on the tests, detection at 19:05). The script follows Bitget/CEO and says "Bitget's CEO says".
- **"Twenty-four days"** is the gap from SlowMist's earliest log entry to the theft. In the close it is now "may have been holding them", because Mandiant dates privileged access only to 24 Sep.
- **"238 million after the alarm"**: Halborn's sum ($238M of $387M) and Certora's estimate (via BeInCrypto) agree.
- **Binance link:** Chainalysis' own words: stolen Binance funds "commingled on-chain" with Bitget funds. The FBI statement (31 Oct) names TraderTraitor for Binance only. BleepingComputer's article lists Bitget among TraderTraitor's thefts, but that is the reporter's framing, not the FBI's, so we don't use it.
- **Bybit loan:** 40,000 ETH sent the day of the Bybit hack (21 Feb 2025), repaid within three days. "No interest, no collateral" is Bitget's CEO's statement.
- **November movements:** Arkham's figures cover wallets *labelled* as the Bitget hacker; Arkham says this is not a full accounting of everything the attacker controls. Worded "the wallets labelled as the Bitget hacker".
- **Protection fund:** over $464M (5,500 BTC) before; rebuilt to $300M+ on 30 Sep; $314M+ (3,705 BTC) on the progress page. The script says "just over 300 million — still less than before".
- **To re-check before rendering:** any government attribution for Bitget, vendor name or CVE published after 22 Nov; the final Mandiant/SlowMist reports; Arkham's latest balance.

---
- **Second person (v3):** "If you had money on Bitget…" only describes what customers saw (withdrawals blocked at 19:05, back by 2 Oct, loss covered by the fund) [S2][S16].
- **"Covering tracks, or going for more — the reports don't say"**: honest about intent; the reports only record the database attempt and the errors [S4][S7].

---

## Changes from v2 (22 Nov 2026, after `research/suspense-storytelling.md`)

No new facts except [S31] (FBI on Bybit). Same editorial line.
1. **Opening:** first line is the 93 TRX test at 02:31 in Asia (small concrete image), the $388M comes second; the ending returns to it.
2. **Protagonist:** Bitget as the rescuer — the 40,000 ETH loan to Bybit moved from 9:35 to 0:35 ("THE RESCUER"), with a planted "it comes back at the end"; the Thomas segment "The loan" is now the payoff.
3. **Customer point of view** at 19:05 and in the close ("If you had money on Bitget…"), facts only.
4. **Knowledge gap:** "From here on, we know someone is inside. Bitget doesn't."
5. **Every section ends on a "but"/"so"** (a new problem or question) instead of a conclusion; transitions rewritten (16:07, 17:49, 18:31, 19:05, money, who).
6. **Fingerprint planted before the peak** ("something odd about these transfers… hold on to it") and paid after ("THE TELL").
7. **Second race** at ~6:30 retitled "WHY DIDN'T IT STOP?", with a split screen customer app vs signing stamp.
8. **Fewer numbers** in "WHERE DID IT GO?" (removed the 34.75M repeat, "two fifths", 1.1M, "35 bitcoin left"; 35 BTC stays in the notes).
9. Removed from the voice (still true, kept in sources): the 5% bounty, Mandiant/SlowMist hired, Elliptic's "past $1 billion", the Bybit loan details in the WHO act.
10. Proposed YouTube chapters named as scenes/questions.

## Changes from v1 (22 Nov 2026)

1. **Corrected:** "Mandiant found no evidence that a single private key was compromised" → "Bitget says not a single private key was compromised" (Mandiant only reports Bitget's non-observation).
2. **Corrected:** spoken amount $387.5M → "about $388M" (Bitget's final verified figure; matches the title).
3. **Removed:** "two wallets that Bitquery treats as warm sent out about 55%" and "mostly from the warm wallets" (the hot/warm split is Halborn's calculation on a wallet public trackers label cold).
4. **Corrected:** gas-limit tell "that week" → "in the eight days before the theft"; source moved to Bitquery's own data.
5. **Corrected:** third Product A node "on the 25th" → "the night of the theft" (UTC+8 date).
6. **Added:** the employee is not a suspect (internal collusion initially excluded) and credentials stolen via the zero-day (CEO AMA).
7. **Softened:** DFNS deductions (checks asserted by the requester; no second approval or allow-list) → "according to one analysis".
8. **Changed:** "60% after the alarm" → "about 238 million — more than half" (two estimates agree).
9. **Added:** November CoinJoin movements (Arkham) as the end of the money trail.
10. **Added:** the Binance link (Chainalysis commingling, ZachXBT same address, FBI 31 Oct) to close the "WHO?" gap.
11. **Rewritten:** Thomas segment "The pattern" → "The loan" (Bitget's 40,000 ETH loan to Bybit, Feb 2025).
12. **Worded as a claim:** ZachXBT's Kelp DAO link ("ZachXBT says").
13. **Trimmed:** hot/warm/cold explainer and the zero-day definition.
15. **Added (verified details, to reach length):** "biggest crypto theft of the year" at the time; the 19:03 test from a different wallet; the Zcash fingerprint (~1,000 inputs vs 54); ZachXBT's launderers asking for support in public chats; Elliptic's "past $1 billion"; Bitget reviewing how it picks security vendors.
14. **Changed:** close "someone else was holding them" → "may have been holding them" (24 days is SlowMist's earliest log, Mandiant dates access later).
