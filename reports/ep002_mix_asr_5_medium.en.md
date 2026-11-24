# ASR check (medium.en)

| line | result | differences (script → heard) | heard |
|---|---|---|---|
| a1 | BAD 0.81 | the thirty first of → 31 | 31 August. That's the earliest malicious activity, investigators found in the logs. |
| a2 | OK 1.00 |  | Not inside the wallets. Inside a security product. One of two third-party tools BitGet ran to protect its systems. |
| a3 | OK 1.00 |  | The investigators call them product A and product B. The vendor hasn't been named. |
| a4 | OK 1.00 |  | On product A, a flaw nobody had found yet. A zero-day. Let the attacker run a hidden script. |
| a5 | OK 1.00 |  | The script found a database password, sitting in plain text. |
| a6 | OK 1.00 |  | a spare key taped under the doormat, except the doormat was inside the security office. |
| a7 | OK 1.00 |  | From here on, we know someone is inside. BitGet doesn't. |
| a8 | BAD 0.87 | the twenty fourth of → 24 | One caveat, Mandiant dates the attacker's privileged access only to 24 September. The two reports haven't been reconciled. |
| a9 | OK 1.00 |  | But a hidden script on a guard's machine can't move money. To get near the wallets, they needed something else. |
| a10 | OK 1.00 |  | A name. A real one. |
| b1 | BAD 0.87 | the twenty third of → 23 | The same script had spread. A second machine on 23 September. A third the night of the theft. |
| b2 | BAD 0.80 | sixteen oh seven → 1607 | At 1607, someone logged into Product B's management platform. |
| b3 | OK 1.00 |  | with the identity of a real BitGet employee. |
| b4 | OK 1.00 |  | That person wasn't there. BitGet says the credentials were stolen through the zero day, and that it has ruled out, for now, anyone on the inside. |
| b5 | OK 1.00 |  | Mandiant found a web shell on appliance B and a channel back to the attacker. |
| b6 | OK 1.00 |  | From there they moved sideways, to the production wallet job server, the machine that builds withdrawal transactions, and installed malicious packages on it. |
| b7 | OK 1.00 |  | Now they were standing next to the money. |
| b8 | OK 1.00 |  | But every withdrawal still had to get past one more thing, risk control. |
| c1 | BAD 0.88 | seventeen forty nine → 1749 | At 1749, a tool started on the wallet host. Slowmist later recovered it from deleted files. |
| c2 | OK 1.00 |  | It didn't fight risk control. It forged its answers. |
| c3 | OK 1.00 |  | Then it built withdrawal requests, and pushed them into BitGet's normal withdrawal process. |
| c4 | OK 1.00 |  | According to one analysis, the system simply took the requester's word that the checks had passed. |
| c5 | OK 1.00 |  | On paper, that was enough. There was only one way to find out if it worked in practice. |
| c6 | OK 1.00 |  | Try it. |
| d1 | OK 1.00 |  | Let me stop here for a second. |
| d2 | OK 1.00 |  | Companies buy security products to watch the doors, they give them deep access, because that's how they see everything. |
| d3 | OK 1.00 |  | which means if someone takes over the guard, they don't need to break any doors. |
| d4 | OK 1.00 |  | They're already standing in every corridor. |
| e1 | BAD 0.44 | eighteen thirty one → 1831; ninety three t r x → 93 trx; point eight four → 84 | 1831. Two tiny transfers, 93 TRX, then 0.84 ether. |
| e2 | OK 1.00 |  | Tests, BitGet's CEO says they were below the risk threshold, so no alert went off. |
| e3 | OK 1.00 |  | And there was something odd about these transfers, something that could have given them away. Hold on to it. |
| e4 | OK 1.00 |  | Then, nothing. For almost half an hour. |
| e5 | BAD 0.38 | eighteen fifty eight thirty four point seven five → 1858 34 75; u s d t → usdt | 1858, 34.75 million USDT leaves in one transfer. |
| e6 | OK 1.00 |  | Still no alarm. |
| e7 | OK 1.00 |  | So they stopped testing. |
| f1 | BAD 0.62 | nineteen oh one → 1901; fifteen → 15 | 1901, 7 Transfers, 5 Blockchains, 15 Seconds |
| f2 | BAD 0.80 | nineteen oh three → 1903 | 1903, one more small test from a different wallet. |
| f3 | BAD 0.59 | nineteen oh five bitget's → 1905 bit gets | 1905. Bit gets reconciliation finally flags the gap. |
| f4 | OK 1.00 |  | If you had money on Bitget at that moment, this is what you saw. Your withdrawal stopped. Risk control had blocked withdrawals for every customer on the platform. |
| f5 | BAD 0.67 | nineteen fourteen → 1914 | 1914 highest level emergency |
| f6 | BAD 0.00 | nineteen sixteen → 1916 | 1916. |
| f7 | OK 1.00 |  | 5 Transfers, 5 Chains, 9 Seconds |
| f8 | BAD 0.40 | two hundred and three → 203; dollars → ∅ | about $203 million. |
| f9 | OK 1.00 |  | The customers had been locked out 11 minutes earlier. |
| f10 | OK 1.00 |  | The attacker hadn't. |
| g1 | OK 1.00 |  | Blocking customer withdrawals was the wrong switch. The forged requests weren't customer withdrawals. |
| g2 | OK 1.00 |  | According to one analysis, on the warm wallets nothing stood between a request and a signature. No second person. No list of allowed destinations. |
| g3 | CHECK 0.91 | thirty nine → 39 | So the signing service kept running for two hours and 39 minutes after the first alert. |
| g4 | BAD 0.85 | two hundred and thirty eight → 238; dollars → ∅ | Two separate estimates put the money that left after the alarm at about $238 million, more than half of the theft. |
| g5 | CHECK 0.91 | twenty forty → 2040 | At 2040, BitGet started moving funds into cold storage, still not sure whether keys had been taken. |
| g6 | BAD 0.56 | traced → trace; twenty one twenty three → 21 23 | The last trace transfer, left at 21.23. |
| g7 | OK 1.00 |  | Then the attacker tried to rewrite withdrawal records directly in the database, covering tracks or going for more. The reports don't say. Two fake bitcoin orders returned errors. |
| g8 | BAD 0.64 | twenty one forty four bitget → 21 44 bit gets | At 21.44, BIT gets shut down the withdrawal services, signing included. |
| g9 | OK 1.00 |  | The next morning BitGet found the root cause and reported the theft to law enforcement. |
| g10 | OK 1.00 |  | And when investigators went back to those first test transfers, the odd detail was right there. |
| h1 | BAD 0.76 | bitget's → bit gets; sixty three thousand → 63 000 | Every Ethereum transfer sets a fuel limit. Gas. Bit gets normal customer payouts used about 63,000. |
| h2 | BAD 0.55 | one hundred thousand → 100 000; two hundred thousand → 200 000 | The attacker's transfers used exactly 100,000 or 200,000. |
| h3 | BAD 0.75 | thirty five thousand six hundred and seventy eight → 35 678 | In the eight days before, those wallets sent 35,678 transactions. Not one customer payout did that. |
| h4 | BAD 0.87 | a thousand → one 000; fifty four → 54 | On Zcash, it was even louder. Each stolen transfer pulled together about 1,000 pieces of coin, the wallet's biggest transaction before that had used 54. |
| h5 | OK 1.00 |  | The forged commands were deleted after each transfer. |
| h6 | OK 1.00 |  | The fingerprints weren't. Nobody was watching for them. |
| h7 | BAD 0.82 | three hundred and eighty eight → 388 | Now the thief had 388 million dollars and a new problem how to keep it |
| i1 | OK 1.00 |  | I'm Thomas Archer, the AI narrator of Siphon Files. |
| i2 | OK 1.00 |  | Every claim in this episode has a source, and they're all in the description. |
| i3 | OK 1.00 |  | Here's the strange part, Bitget says not a single private key was compromised. |
| i4 | BAD 0.77 | three hundred and eighty eight → 388 | So how do you steal 388 million dollars without the keys? |
| i5 | OK 1.00 |  | you make the exchange sign it for you. |
| k1 | OK 1.00 |  | If you had money on BitGet, you didn't lose it. BitGet says it covered the loss from its own protection fund. |
| k2 | BAD 0.75 | the second of → two | Every withdrawal was back by 2 October. |
| k3 | BAD 0.87 | three hundred → 300; dollars → ∅ | The fund has been rebuilt to just over $300 million, still less than before. |
| k4 | OK 1.00 |  | The vulnerability is fixed. Critical operations now need more than one approval. |
| k5 | CHECK 0.94 | bitget → bidget | And BidGet says it is reviewing how it picks its security vendors. The vendor still hasn't been named. |
| l1 | BAD 0.67 | twenty twenty five → 2025; bitget → bit gets; forty thousand → 40 000 | In February 2025, when Bybit was robbed, Bit gets sent 40,000 Ether the same day. |
| l2 | OK 1.00 |  | No interest, no collateral. |
| l3 | OK 1.00 |  | The FBI blamed that theft on North Korea. |
| l4 | OK 1.00 |  | Nineteen months later, the money was leaving BitGet. |
| l5 | OK 1.00 |  | No government has named anyone, but the analysts point the same way. |
| p1 | OK 1.00 |  | An exchange keeps most of its money in cold wallets. Offline. Slow. Hard to reach. Those weren't touched. |
| p2 | OK 1.00 |  | Warm wallets hold a reserve. Hot wallets pay your withdrawals automatically around the clock. |
| p3 | OK 1.00 |  | When you press Withdraw, a request goes into a pipeline, risk checks look at it, then a signing service puts a cryptographic signature on it, and the money moves. |
| p4 | OK 1.00 |  | Without that signature, nothing leaves, with it anything does. |
| p5 | OK 1.00 |  | So the attacker never needed the secret behind the signature. They needed to get close to the machine that uses it. |
| p6 | OK 1.00 |  | And for that, they needed a way in that nobody would watch. |
| r1 | BAD 0.85 | nineteen → 19; twenty twenty five → 2025; and a half → five; dollars → ∅ | To understand why this one hurts, go back 19 months. February 2025. The exchange Bybit has just lost $1.5 billion. The FBI blames North Korea. Customers are rushing to pull their money out. |
| r2 | BAD 0.84 | a rival → arrival; forty thousand → 40 000 | That same day, Arrival sends help. BitGet lends Bybit 40,000 Ether to keep its withdrawals running. No interest. No collateral. |
| r3 | OK 1.00 |  | Remember that loan. It comes back at the end. |
| r4 | BAD 0.83 | the twenty fourth of → 24; twenty twenty six → 2026 | On 24 September, 2026, the exchange that came to help became the one robbed, at the time, the biggest crypto theft of the year. |
| t1 | OK 1.00 |  | Half past two in the morning, in Asia. A tiny transfer, leaves the crypto exchange Bitget. Nobody looks at it. |
| t2 | BAD 0.79 | three hundred and eighty eight → 388; dollars → ∅; bitget → bitgett | Less than three hours later, about $388 million is gone, and Bitgett says not a single key was stolen. |
| t3 | BAD 0.84 | nineteen oh five → 19 05; bitget → bitgett | At 19.05 the alarm went off, Bitgett froze every customer withdrawal and the money kept leaving for another two hours. |
| t4 | CHECK 0.91 | twenty four → 24 | And the first sign that someone was inside, it's in the logs. Dated 24 days earlier. |
| w1 | BAD 0.83 | u s d t → usdt; twenty → 20 | The stablecoins went first, because stablecoins can be frozen. All the USDT was swapped for Ether within 20 minutes. |
| w2 | BAD 0.84 | x r p → xrp; thor chain → thorchain | The XRP went to Bitcoin through ThorChain. Part of the Zcash disappeared into a private pool, where it can't be followed. |
| w3 | BAD 0.79 | thor chain → thorchain; thor chain → thorchain | Bitget asked ThorChain to block the addresses. ThorChain declined, citing its permissionless design. |
| w4 | BAD 0.90 | point → ∅; percent → ∅ | In the end, less than 0.3% was frozen. |
| w5 | BAD 0.83 | one hundred and sixty one → 161; dollars → ∅; coin join → coinjoin | In November, the Bitcoin started moving again, about $161 million in 11 days, most of it through CoinJoin, which mixes many people's coins into one transaction. |
| w6 | OK 1.00 |  | and the people moving it weren't hiding very well. |
| w7 | BAD 0.89 | zach x b t → zacxbt | ZacXBT says the launderers asked for customer support in the public chats of the services they were using. Failed swaps. Missing payouts. |
| w8 | OK 1.00 |  | He says one of them had handled stolen money before, from the Kelp Dao exploit in April. |
| x1 | OK 1.00 |  | So who was behind it? |
| x2 | CHECK 0.96 | gracy → gracie | On the night of the hack, BitGet's CEO, Gracie Chen, said some IP addresses matched VPN services used by a North Korean group. |
| x3 | OK 1.00 |  | Four days later, she was more careful. That, she said, was based on preliminary indicators. |
| x4 | OK 1.00 |  | The analysts at Chainalysis, Elliptic and TRM Labs all lean the same way. |
| x5 | CHECK 0.95 | dollars → ∅ | Then, five weeks later, Binance lost more than $6 billion. |
| x6 | OK 1.00 |  | And Chainalysis watched the stolen Binance money meet the BitGet money on the blockchain. |
| x7 | BAD 0.67 | zach x b t → zacxbt; thor chain → thorchain | ZacXBT says both arrived through ThorChain at the same address. |
| x8 | OK 1.00 |  | Two days after the Binance theft, the FBI named the thieves, North Korea's trader-traitor. |
| x9 | OK 1.00 |  | For BitGet, no government has said a word, and Mandiant's report names no one at all. |
| x10 | OK 1.00 |  | Which brings us back to that loan. |
| z1 | BAD 0.85 | ninety three t r x → 93trx | It started with a transfer of 93TRX at half past two in the morning. Nobody looked at it. |
| z2 | OK 1.00 |  | Bitget bought tools to guard the door. For weeks, someone else may have been holding them. |
| z3 | OK 1.00 |  | And when the alarm finally rang, the exchange locked out its customers and left the signing machine running. |
| z4 | OK 1.00 |  | I'm Thomas Archer. This was Siphon Files. |

44 lines to look at

## Words heard with low confidence (p < 0.6)

| line | words |
|---|---|
| a3 | product@1.3s p0.41 |
| a9 | But@0.0s p0.60 |
| b3 | BitGet@1.5s p0.59 |
| b4 | That@0.0s p0.59, BitGet@1.5s p0.56 |
| e1 | ether.@6.0s p0.48 |
| e7 | So@0.0s p0.60 |
| f1 | 1901,@0.0s p0.42 |
| f3 | Bit@1.6s p0.59, gets@1.7s p0.30 |
| f5 | highest@0.9s p0.44 |
| g3 | for@1.8s p0.55, two@2.3s p0.57 |
| g6 | The@0.0s p0.57, 21@2.0s p0.54 |
| g7 | bitcoin@8.2s p0.52 |
| g8 | BIT@1.9s p0.54, gets@2.0s p0.55 |
| g9 | BitGet@0.7s p0.49 |
| h2 | The@0.0s p0.46 |
| h4 | 1@4.2s p0.18 |
| h7 | and@3.0s p0.26, how@4.5s p0.46 |
| i3 | Bitget@1.6s p0.42 |
| k1 | BitGet,@1.0s p0.58 |
| k2 | October.@1.9s p0.52 |
| k5 | And@0.0s p0.52, BidGet@0.3s p0.38 |
| l1 | Bit@3.4s p0.52, gets@3.5s p0.47, Ether@4.7s p0.49 |
| l2 | No@0.0s p0.40 |
| p4 | Without@0.0s p0.55 |
| p6 | And@0.0s p0.48 |
| r2 | Ether@4.2s p0.54 |
| t1 | Half@0.0s p0.31 |
| t3 | Bitgett@2.5s p0.53, and@4.5s p0.56 |
| t4 | And@0.0s p0.56 |
| w3 | Bitget@0.0s p0.54 |
| w5 | Bitcoin@1.0s p0.47 |
| w8 | Dao@3.6s p0.47 |
| x4 | and@2.3s p0.53 |
| x7 | ZacXBT@0.0s p0.45 |
| x8 | trader@4.8s p0.29 |
| x9 | BitGet,@0.3s p0.50 |
| z1 | half@3.6s p0.58 |
| z2 | Bitget@0.0s p0.51 |
