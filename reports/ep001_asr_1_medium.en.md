# ASR check ep001 (medium.en)

| line | result | differences (script → heard) | heard |
|---|---|---|---|
| a1 | BAD 0.81 | the thirty first of → 31 | 31 August. That's the earliest malicious activity, investigators found in the logs. |
| a2 | OK 1.00 |  | Not inside the wallets, inside a security product, one of two third-party tools BitGet ran to protect its systems. |
| a3 | OK 1.00 |  | The investigators call them Product A and Product B. The vendor hasn't been named. |
| a4 | OK 1.00 |  | On product A, a flaw nobody had found yet. A zero day. Let the attacker run a hidden script. |
| a5 | OK 1.00 |  | The script found a database password sitting in plain text. |
| a6 | OK 1.00 |  | A spare key taped under the doormat, except the doormat was inside the security office. |
| a7 | OK 1.00 |  | From here on, we know someone is inside. BitGet doesn't. |
| a8 | BAD 0.80 | attacker's → attack as; the twenty fourth of → 24 | One caveat, Mandiant dates the attack as privileged access only to 24 September, the two reports haven't been reconciled. |
| a9 | OK 1.00 |  | But a hidden script on a guard's machine can't move money. To get near the wallets, they needed something else. |
| a10 | OK 1.00 |  | A name, a real one. |
| b1 | BAD 0.87 | the twenty third of → 23 | The same script had spread, a second machine on 23 September, a third the night of the theft. |
| b2 | BAD 0.80 | sixteen oh seven → 1607 | At 1607, someone logged into Product B's management platform. |
| b3 | BAD 0.82 | bitget → bitch get | With the identity of a real bitch get employee. |
| b4 | OK 1.00 |  | That person wasn't there, BitGet says the credentials were stolen through the zero day, and that it has ruled out, for now, anyone on the inside. |
| b5 | OK 1.00 |  | Mandiant found a web shell on appliance B and a channel back to the attacker. |
| b6 | OK 1.00 |  | From there they moved sideways, to the production wallet job server, the machine that builds withdrawal transactions, and installed malicious packages on it. |
| b7 | OK 1.00 |  | Now they were standing next to the money. |
| b8 | OK 1.00 |  | But every withdrawal still had to get past one more thing — risk control. |
| c1 | BAD 0.88 | seventeen forty nine → 1749 | At 1749, a tool started on the wallet host. Slowmist later recovered it from deleted files. |
| c2 | OK 1.00 |  | It didn't fight risk control. It forged its answers. |
| c3 | CHECK 0.92 | bitget's → bitjet's | Then it built withdrawal requests and pushed them into BitJet's normal withdrawal process. |
| c4 | OK 1.00 |  | According to one analysis, the system simply took the requester's word that the checks had passed. |
| c5 | OK 1.00 |  | On paper, that was enough. There was only one way to find out if it worked in practice. |
| c6 | BAD 0.57 | ∅ → and carve chumps | Try it. And carve chumps. |
| d1 | OK 1.00 |  | Let me stop here for a second. |
| d2 | OK 1.00 |  | Companies buy security products to watch the doors, they give them deep access, because that's how they see everything. |
| d3 | OK 1.00 |  | Which means, if someone takes over the guard, they don't need to break any doors. |
| d4 | OK 1.00 |  | They're already standing in every corridor. |
| e1 | BAD 0.44 | eighteen thirty one → 1831; ninety three t r x → 93 trx; point eight four → 84 | 1831, two tiny transfers, 93 TRX, then 0.84 ether. |
| e2 | OK 1.00 |  | Tests, BitGet's CEO says they were below the risk threshold, so no alert went off. |
| e3 | OK 1.00 |  | And there was something odd about these transfers, something that could have given them away. Hold on to it. |
| e4 | OK 1.00 |  | Then, nothing. For almost half an hour. |
| e5 | BAD 0.38 | eighteen fifty eight thirty four point seven five → 1858 34 75; u s d t → usdt | 1858, 34.75 million USDT leaves in one transfer. |
| e6 | OK 1.00 |  | Still no alarm. |
| e7 | OK 1.00 |  | So they stopped testing. |
| f1 | BAD 0.62 | nineteen oh one → 1901; fifteen → 15 | 1901, 7 transfers, 5 blockchains, 15 seconds |
| f2 | BAD 0.80 | nineteen oh three → 1903 | 1903, one more small test from a different wallet. |
| f3 | BAD 0.75 | nineteen oh five → 1905 | 1905. BitGet's reconciliation finally flags the gap. |
| f4 | CHECK 0.96 | withdrawal → withdrawals | If you had money on Bitget at that moment, this is what you saw. Your withdrawals stopped. Risk control had blocked withdrawals for every customer on the platform. |
| f5 | BAD 0.67 | nineteen fourteen → 1914 | 1914. Highest-level emergency. |
| f6 | BAD 0.00 | nineteen sixteen → 1916 | 1916. |
| f7 | OK 1.00 |  | 5 Transfers, 5 chains, 9 seconds |
| f8 | BAD 0.40 | two hundred and three → 203; dollars → ∅ | about $203 million. |
| f9 | OK 1.00 |  | The customers had been locked out 11 minutes earlier. |
| f10 | BAD 0.32 | ∅ → and alright thanks for watching and i'll see you in the next one | The attacker hadn't. And Alright, thanks for watching, and I'll see you in the next one. |
| g1 | OK 1.00 |  | Blocking customer withdrawals was the wrong switch. The forged requests weren't customer withdrawals. |
| g2 | OK 1.00 |  | According to one analysis, on the warm wallets nothing stood between a request and a signature. No second person. No list of allowed destinations. |
| g3 | CHECK 0.91 | thirty nine → 39 | So the signing service kept running, for 2 hours and 39 minutes after the first alert. |
| g4 | BAD 0.85 | two hundred and thirty eight → 238; dollars → ∅ | Two separate estimates put the money that left after the alarm at about $238 million, more than half of the theft. |
| g5 | BAD 0.78 | twenty forty bitget → 2040 bitjet; whether → where the | At 2040 BitJet started moving funds into cold storage, still not sure where the keys had been taken. |
| g6 | BAD 0.56 | traced → trace; twenty one twenty three → 21 23 | The last trace transfer, left at 21.23. |
| g7 | OK 1.00 |  | Then the attacker tried to rewrite withdrawal records directly in the database, covering tracks or going for more. The reports don't say. Two fake Bitcoin orders returned errors. |
| g8 | BAD 0.64 | twenty one forty four bitget → 21 44 bit gets | At 21.44, BIT gets shut down the withdrawal services, signing included. |
| g9 | OK 1.00 |  | The next morning BitGet found the root cause and reported the theft to law enforcement. |
| g10 | OK 1.00 |  | And when investigators went back to those first test transfers, the odd detail was right there. |
| h1 | BAD 0.76 | bitget's → which gets; sixty three thousand → 63 000 | Every Ethereum transfer sets a fuel limit, gas, which gets normal customer payouts used about 63,000. |
| h2 | BAD 0.55 | one hundred thousand → 100 000; two hundred thousand → 200 000 | The attacker's transfers used exactly 100,000 or 200,000. |
| h3 | BAD 0.75 | thirty five thousand six hundred and seventy eight → 35 678 | In the eight days before, those wallets sent 35,678 transactions. Not one customer payout did that. |
| h4 | CHECK 0.94 | fifty four → 54 | On Zcash, it was even louder. Each stolen transfer pulled together about a thousand pieces of coin, the wallet's biggest transaction before that had used 54. |
| h5 | OK 1.00 |  | The forged commands were deleted after each transfer. |
| h6 | OK 1.00 |  | The fingerprints weren't. Nobody was watching for them. |
| h7 | BAD 0.82 | three hundred and eighty eight → 388 | Now the thief had 388 million dollars. And a new problem, how to keep it. |
| i1 | OK 1.00 |  | I'm Thomas Archer, the AI narrator of Siphon Files. |
| i2 | OK 1.00 |  | Every claim in this episode has a source, and they're all in the description. |
| i3 | OK 1.00 |  | Here's the strange part, BitGet says not a single private key was compromised. |
| i4 | BAD 0.77 | three hundred and eighty eight → 388 | So, how do you steal 388 million dollars, without the keys? |
| i5 | OK 1.00 |  | You make the exchange, sign it for you. |
| k1 | CHECK 0.90 | bitget → bitgett; bitget → bitgett | If you had money on Bitgett you didn't lose it. Bitgett says it covered the loss from its own protection fund. |
| k2 | BAD 0.75 | the second of → two | Every withdrawal was back by 2 October. |
| k3 | BAD 0.87 | three hundred → 300; dollars → ∅ | The fund has been rebuilt to just over $300 million, still less than before. |
| k4 | OK 1.00 |  | The vulnerability is fixed. Critical operations now need more than one approval. |
| k5 | OK 1.00 |  | And BitGet says it is reviewing how it picks its security vendors. The vendor still hasn't been named. |
| l1 | BAD 0.67 | twenty twenty five → 2025; bitget → bit gets; forty thousand → 40 000 | In February 2025, when Bybit was robbed, Bit gets sent 40,000 Ether the same day. |
| l2 | OK 1.00 |  | No interest, no collateral. |
| l3 | OK 1.00 |  | The FBI blamed that theft on North Korea. |
| l4 | BAD 0.75 | nineteen → 19; bitget → bichette | 19 months later, the money was leaving Bichette. |
| l5 | OK 1.00 |  | No government has named anyone, but the analysts point the same way. |
| p1 | OK 1.00 |  | An exchange keeps most of its money in cold wallets — offline, slow, hard to reach. Those weren't touched. |
| p2 | OK 1.00 |  | Warm wallets hold a reserve, hot wallets pay your withdrawals automatically around the clock. |
| p3 | OK 1.00 |  | When you press Withdraw, a request goes into a pipeline, risk checks look at it, then a signing service puts a cryptographic signature on it, and the money moves. |
| p4 | OK 1.00 |  | Without that signature, nothing leaves, with it anything does. |
| p5 | OK 1.00 |  | So the attacker never needed the secret behind the signature. They needed to get close to the machine that uses it. |
| p6 | OK 1.00 |  | And for that, they needed a way in that nobody would watch. |
| r1 | BAD 0.85 | nineteen → 19; twenty twenty five → 2025; and a half → five; dollars → ∅ | To understand why this one hurts, go back 19 months. February 2025. The exchange Bybit has just lost $1.5 billion. The FBI blames North Korea. Customers are rushing to pull their money out. |
| r2 | BAD 0.73 | a rival → arrival; bitget → bitgett; bybit forty thousand → by bit 40 000 | That same day Arrival sends help. Bitgett lends by bit 40,000 Ether to keep its withdrawals running, no interest no collateral. |
| r3 | OK 1.00 |  | Remember that loan, it comes back at the end. |
| r4 | BAD 0.83 | the twenty fourth of → 24; twenty twenty six → 2026 | On 24 September, 2026, the exchange that came to help became the one robbed. At the time, the biggest crypto theft of the year. |
| t1 | CHECK 0.93 | bitget → bit get | Half past two in the morning, in Asia. A tiny transfer, leaves the crypto exchange bit get. Nobody looks at it. |
| t2 | BAD 0.84 | three hundred and eighty eight → 388; dollars → ∅ | Less than three hours later, about $388 million is gone. And BitGet says not a single key was stolen. |
| t3 | BAD 0.84 | nineteen oh five → 19 05; bitget → bitchup | At 19.05, the alarm went off, Bitchup froze every customer withdrawal, and the money kept leaving for another two hours. |
| t4 | CHECK 0.91 | twenty four → 24 | And the first sign that someone was inside, it's in the logs, dated 24 days earlier. |
| w1 | BAD 0.83 | u s d t → usdt; twenty → 20 | The stablecoins went first, because stablecoins can be frozen. All the USDT was swapped for Ether within 20 minutes. |
| w2 | BAD 0.84 | x r p → xrp; thor chain → thorchain | The XRP went to Bitcoin through ThorChain. Part of the Zcash disappeared into a private pool, where it can't be followed. |
| w3 | BAD 0.79 | thor chain → thorchain; thor chain → thorchain | Bitget asked ThorChain to block the addresses. ThorChain declined, citing its permissionless design. |
| w4 | BAD 0.90 | point → ∅; percent → ∅ | In the end, less than 0.3% was frozen. |
| w5 | BAD 0.83 | one hundred and sixty one → 161; dollars → ∅; coin join → coinjoin | In November, the bitcoin started moving again, about $161 million in 11 days, most of it through CoinJoin, which mixes many people's coins into one transaction. |
| w6 | OK 1.00 |  | And the people moving it weren't hiding very well. |
| w7 | BAD 0.89 | zach x b t → zacxbt | ZacXBT says the launderers asked for customer support in the public chats of the services they were using, failed swaps, missing payouts. |
| w8 | OK 1.00 |  | He says one of them had handled stolen money before, from the Kelp Dao exploit in April. |
| x1 | OK 1.00 |  | So who was behind it? |
| x2 | CHECK 0.91 | bitget's → bitget; gracy → gracie | On the night of the hack, BitGet CEO Gracie Chen said some IP addresses matched VPN services used by a North Korean group. |
| x3 | OK 1.00 |  | Four days later, she was more careful. That she said, was based on preliminary indicators. |
| x4 | BAD 0.90 | chainalysis → chanalysis | Chanalysis, Elliptic, and TRM Labs all lean the same way. |
| x5 | CHECK 0.95 | dollars → ∅ | Then, five weeks later, Binance lost more than $6 billion. |
| x6 | BAD 0.90 | bitget → bitch get | And Chainalysis watched the stolen Binance money meet the bitch get money on the blockchain. |
| x7 | BAD 0.67 | zach x b t → zacxbt; thor chain → thorchain | ZacXBT says both arrived through ThorChain at the same address. |
| x8 | OK 1.00 |  | Two days after the Binance theft, the FBI named the thieves, North Korea's Trader Traitor. |
| x9 | OK 1.00 |  | For BitGet, no government has said a word. And Mandiant's report names no one at all. |
| x10 | OK 1.00 |  | Which brings us back to that loan. |
| z1 | BAD 0.85 | ninety three t r x → 93trx | It started with a transfer of 93TRX at half past two in the morning. Nobody looked at it. |
| z2 | OK 1.00 |  | BitGet bought tools to guard the door. For weeks, someone else may have been holding them. |
| z3 | OK 1.00 |  | And when the alarm finally rang, the exchange locked out its customers and left the signing machine running. |
| z4 | OK 1.00 |  | I'm Thomas Archer, this was Siphon Files. |

53 lines to look at

## Words heard with low confidence (p < 0.5)

| line | words |
|---|---|
| a2 | Not@0.0s p0.43 |
| a3 | The@0.0s p0.46, Product@1.6s p0.46 |
| a8 | attack@2.5s p0.34, privileged@2.9s p0.45 |
| b3 | With@0.0s p0.27, bitch@1.8s p0.41 |
| b4 | That@0.0s p0.21, BitGet@1.9s p0.45 |
| b8 | —@3.2s p0.19 |
| d2 | Companies@0.0s p0.08 |
| d3 | Which@0.0s p0.47 |
| e1 | ether.@6.5s p0.49 |
| e6 | Still@0.0s p0.38 |
| f1 | 1901,@0.0s p0.44 |
| f4 | If@0.0s p0.36, withdrawals@4.3s p0.42 |
| f7 | chains,@2.0s p0.45 |
| f8 | about@0.0s p0.50 |
| f10 | The@0.0s p0.47, Alright,@2.2s p0.00, thanks@2.3s p0.22, in@2.5s p0.34 |
| g3 | 2@2.6s p0.38 |
| g8 | BIT@2.5s p0.31 |
| h1 | which@3.8s p0.42 |
| i3 | BitGet@1.9s p0.45 |
| i5 | You@0.0s p0.40 |
| k1 | If@0.0s p0.43 |
| k2 | Every@0.0s p0.36 |
| k5 | BitGet@0.7s p0.50 |
| l1 | Bit@3.7s p0.44, Ether@5.0s p0.44 |
| p1 | —@3.1s p0.07 |
| r1 | To@0.0s p0.11 |
| r2 | 40@3.9s p0.47, Ether@4.8s p0.50 |
| t1 | bit@5.5s p0.24, get.@5.7s p0.42 |
| t3 | Bitchup@2.8s p0.46 |
| w6 | And@0.0s p0.48 |
| w8 | Dao@4.0s p0.42 |
| x2 | CEO@1.8s p0.31 |
| x3 | she@3.2s p0.28 |
| x4 | Chanalysis,@0.0s p0.44 |
| x6 | And@0.0s p0.45, bitch@3.4s p0.17 |
| x7 | ZacXBT@0.0s p0.45 |
| x8 | Trader@5.2s p0.19 |
| z2 | BitGet@0.0s p0.33 |
