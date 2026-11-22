# ASR check ep001 (medium.en)

| line | result | differences (script → heard) | heard |
|---|---|---|---|
| a8_s2 | BAD 0.87 | the twenty fourth of → 24 | One caveat, Mandiant dates the attacker's privileged access only to 24 September. The two reports haven't been reconciled. |
| a8_s3 | BAD 0.87 | the twenty fourth of → 24 | One caveat, Mandiant dates the attacker's privileged access only to 24 September. The two reports haven't been reconciled. |
| a8_s4 | BAD 0.82 | attacker's → attackers'; the twenty fourth of → 24 | 1. Caveat. Mandiant dates the attackers' privileged access only to 24 September. The two reports haven't been reconciled. |
| b3_s2 | OK 1.00 |  | with the identity of a real BitGet employee. |
| b3_s3 | OK 1.00 |  | with the identity of a real BitGet employee. |
| b3_s4 | OK 1.00 |  | with the identity of a real BitGet employee. |
| c3_s2 | BAD 0.85 | withdrawal → withdraw; bitget's → bitchet's | Then it built withdraw requests, and pushed them into Bitchet's normal withdrawal process. |
| c3_s3 | CHECK 0.92 | bitget's → bitjet's | Then it built withdrawal requests and pushed them into BitJet's normal withdrawal process. |
| c3_s4 | BAD 0.77 | withdrawal → withdraw; bitget's → bitjet's; withdrawal → withdraw | Then it built withdraw requests, and pushed them into BitJet's normal withdraw process. |
| c6_s2 | BAD 0.44 | ∅ → the fear at for you | Try it. The fear at for you. |
| c6_s3 | BAD 0.67 | ∅ → you on | Try it. You on? |
| c6_s4 | BAD 0.80 | ∅ → chetty | Try it. Chetty. |
| f10_s2 | BAD 0.55 | ∅ → i fore the destine i | The attacker hadn't. I fore The destine I |
| f10_s3 | BAD 0.75 | ∅ → and to | The attacker hadn't. And to… |
| f10_s4 | BAD 0.67 | ∅ → won't i'm she | The attacker hadn't. Won't. I'm she. |
| g5_s2 | CHECK 0.91 | twenty forty → 2040 | At 2040, BitGet started moving funds into cold storage, still not sure whether keys had been taken. |
| g5_s3 | CHECK 0.91 | twenty forty → 2040 | At 2040, BitGet started moving funds into cold storage, still not sure whether keys had been taken. |
| g5_s4 | BAD 0.83 | twenty forty → 2040; whether → where the | At 2040, Bitget started moving funds into cold storage. Still not sure where the keys had been taken. |
| g8_s2 | BAD 0.75 | twenty one forty four → 21 44 | At 21.44, BitGet shut down the withdrawal services, signing included. |
| g8_s3 | BAD 0.64 | twenty one forty four bitget → 21 44 bit gets | At 21.44, BIT gets shut down the withdrawal services, signing included. |
| g8_s4 | BAD 0.64 | twenty one forty four bitget → 21 44 bit gets | At 21.44, BIT gets shut down the withdrawal services, signing included. |
| h1_s2 | BAD 0.76 | bitget's → bit gets; sixty three thousand → 63 000 | every ethereum transfer sets a fuel limit gas bit gets normal customer payouts used about 63,000 |
| h1_s3 | BAD 0.71 | gas bitget's → gasp it gets; sixty three thousand → 63 000 | Every Ethereum transfer sets a fuel limit. Gasp! It gets normal customer payouts used about 63,000. |
| h1_s4 | BAD 0.76 | bitget's → bit gets; sixty three thousand → 63 000 | every ethereum transfer sets a fuel limit gas bit gets normal customer payouts used about 63,000 |
| l1_s2 | BAD 0.67 | twenty twenty five → 2025; bitget → bit gets; forty thousand → 40 000 | In February 2025, when Bybit was robbed, Bit gets sent 40,000 Ether the same day. |
| l1_s3 | BAD 0.69 | twenty twenty five → 2025; bitget → bichette; forty thousand → 40 000 | In February 2025, when Bybit was robbed, Bichette sent 40,000 Ether the same day. |
| l1_s4 | BAD 0.67 | twenty twenty five → 2025; bitget → bit gets; forty thousand → 40 000 | In February 2025, when Bybit was robbed, Bit gets sent 40,000 Ether the same day. |
| l4_s2 | BAD 0.88 | nineteen → 19 | 19 months later, the money was leaving BitGet. |
| l4_s3 | BAD 0.88 | nineteen → 19 | 19 months later, the money was leaving BitGet. |
| l4_s4 | BAD 0.88 | nineteen → 19 | 19 months later, the money was leaving BitGet. |
| r2_s2 | BAD 0.84 | a rival → arrival; forty thousand → 40 000 | That same day, Arrival sends help, BitGet lends Bybit 40,000 Ether to keep its withdrawals running. No interest. No collateral. |
| r2_s3 | BAD 0.73 | a rival → arrival; lends bybit forty thousand → lens by bit 40 000 | That same day, Arrival sends help, BitGet lens by bit 40,000 ether to keep its withdrawals running, no interest, no collateral. |
| r2_s4 | BAD 0.73 | a rival → arrival; bitget → bitjet; bybit forty thousand → by bit 40 000 | That same day, Arrival sends help. BitJet lends by bit 40,000 ether to keep its withdrawals running. No interest, no collateral. |
| t3_s2 | BAD 0.84 | nineteen oh five → 19 05; bitget → bidget | At 19.05, the alarm went off, Bidget froze every customer withdrawal, and the money kept leaving for another two hours. |
| t3_s3 | BAD 0.84 | nineteen oh five → 19 05; bitget → bitgett | At 19.05 the alarm went off, Bitgett froze every customer withdrawal, and the money kept leaving for another two hours. |
| t3_s4 | BAD 0.82 | nineteen oh five → 19 05; bitget → bitch get | At 19.05, the alarm went off, Bitch-Get froze every customer withdrawal, and the money kept leaving for another two hours. |
| x6_s2 | OK 1.00 |  | And Chainalysis watched the stolen Binance money meet the BitGet money on the blockchain. |
| x6_s3 | BAD 0.90 | bitget → bitch get | And Chainalysis watched the stolen Binance money meet the bitch get money on the blockchain. |
| x6_s4 | BAD 0.90 | bitget → bitch get | And Chainalysis watched the stolen Binance money meet the bitch get money on the blockchain. |

35 lines to look at

## Words heard with low confidence (p < 0.5)

| line | words |
|---|---|
| a8_s4 | 1.@0.0s p0.18, attackers'@2.5s p0.45 |
| b3_s4 | BitGet@2.1s p0.49 |
| c3_s3 | withdrawal@1.0s p0.43 |
| c6_s2 | for@2.5s p0.39 |
| f10_s2 | fore@3.1s p0.24, The@3.6s p0.11, I@5.0s p0.18 |
| f10_s3 | The@0.0s p0.26, to…@2.3s p0.42 |
| g5_s2 | BitGet@1.7s p0.44 |
| g5_s4 | Bitget@1.7s p0.45, where@5.4s p0.45 |
| g8_s2 | BitGet@2.4s p0.36 |
| h1_s2 | every@0.0s p0.24 |
| h1_s4 | every@0.0s p0.24 |
| l1_s2 | Bit@3.7s p0.38 |
| l1_s3 | Ether@5.3s p0.42 |
| l1_s4 | Bit@3.9s p0.44, gets@4.0s p0.41, Ether@5.2s p0.45 |
| r2_s3 | lens@3.1s p0.39, 40@3.8s p0.32 |
| r2_s4 | ether@5.0s p0.49 |
| t3_s4 | -Get@3.5s p0.25 |
| x6_s2 | And@0.0s p0.46 |
| x6_s3 | bitch@3.3s p0.24 |
| x6_s4 | bitch@3.4s p0.19 |
