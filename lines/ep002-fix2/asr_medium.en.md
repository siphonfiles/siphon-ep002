# ASR check (medium.en)

| line | result | differences (script → heard) | heard |
|---|---|---|---|
| c3_h5 | BAD 0.85 | withdrawal → withdraw; withdrawal → withdraw | Then it built withdraw requests, and pushed them into BitGet's normal withdraw process. |
| c3_s5 | CHECK 0.92 | bitget's → bigjet's | Then it built withdrawal requests and pushed them into BigJet's normal withdrawal process. |
| c3_h6 | OK 1.00 |  | Then it built withdrawal requests and pushed them into BitGet's normal withdrawal process. |
| c3_s6 | BAD 0.85 | withdrawal → withdraw; bitget's → bitjet's | Then it built withdraw requests and pushed them into BitJet's normal withdrawal process. |
| c3_h7 | OK 1.00 |  | Then it built withdrawal requests and pushed them into BitGet's normal withdrawal process. |
| c3_s7 | CHECK 0.92 | bitget's → bitjet's | Then it built withdrawal requests and pushed them into BitJet's normal withdrawal process. |
| c3_s8 | BAD 0.77 | withdrawal → withdraw; bitget's → bitchget's; withdrawal → withdraw | Then it built withdraw requests and pushed them into BitchGet's normal withdraw process. |
| c3_s9 | CHECK 0.92 | bitget's → bitjet's | Then it built withdrawal requests and pushed them into BitJet's normal withdrawal process. |
| g5_s5 | BAD 0.83 | twenty forty → 2040; whether → where the | At 2040 BitGet started moving funds into cold storage, still not sure where the keys had been taken. |
| g5_s6 | BAD 0.83 | twenty forty → 2040; whether → where the | At 2040 BitGet started moving funds into cold storage, still not sure where the keys had been taken. |
| g5_s7 | BAD 0.83 | twenty forty → 2040; whether → where the | At 2040, BitGet started moving funds into cold storage, still not sure where the keys had been taken. |
| g5_s8 | BAD 0.78 | at twenty forty bitget → a 2040 bit gets | A 2040 bit gets started moving funds into cold storage. Still not sure whether keys had been taken. |
| g5_s9 | CHECK 0.91 | twenty forty → 2040 | At 2040, BitGet started moving funds into cold storage, still not sure whether keys had been taken. |
| g6_s5 | BAD 0.56 | traced → trace; twenty one twenty three → 21 23 | The last trace transfer left at 21.23. |
| g6_s6 | BAD 0.59 | traced → trace; twenty one twenty three → 2123 | The last trace transfer, left at 2123. |
| g6_s7 | BAD 0.56 | traced → trace; twenty one twenty three → 21 23 | The last trace transfer left at 21.23. |
| g6_s8 | BAD 0.56 | traced → trace; twenty one twenty three → 21 23 | The last trace transfer, left at 21.23. |
| g6_s9 | BAD 0.56 | traced → trace; twenty one twenty three → 21 23 | The last trace transfer left at 21 23 |
| orig_i1 | OK 1.00 |  | I'm Thomas Archer, the AI narrator of Siphon Files. |
| orig_z4 | OK 1.00 |  | I'm Thomas Archer, this was Siphon Files. |
| t3_h5 | BAD 0.88 | nineteen oh five → 19 05 | At 19.05, the alarm went off, BitGet froze every customer withdrawal, and the money kept leaving for another two hours. |
| t3_s5 | BAD 0.84 | nineteen oh five → 19 05; bitget → bidget | At 19.05 the alarm went off, Bidget froze every customer withdrawal, and the money kept leaving for another two hours. |
| t3_h6 | BAD 0.88 | nineteen oh five → 19 05 | At 19.05, the alarm went off, BitGet froze every customer withdrawal, and the money kept leaving for another two hours. |
| t3_s6 | BAD 0.84 | nineteen oh five → 19 05; bitget → bidget | At 19.05, the alarm went off. Bidget froze every customer withdrawal, and the money kept leaving for another two hours. |
| t3_h7 | BAD 0.84 | nineteen oh five → 19 05; bitget → bitgett | At 19.05 the alarm went off, Bitgett froze every customer withdrawal, and the money kept leaving for another two hours. |
| t3_s7 | BAD 0.84 | nineteen oh five → 19 05; bitget → bitjet | At 19.05, the alarm went off, BitJet froze every customer withdrawal, and the money kept leaving for another two hours. |
| t3_s8 | BAD 0.84 | nineteen oh five → 19 05; bitget → bitchgett | At 19.05 the alarm went off, Bitchgett froze every customer withdrawal, and the money kept leaving for another two hours. |
| t3_s9 | BAD 0.82 | nineteen oh five → 19 05; bitget → but jet | At 19.05 the alarm went off, but Jet froze every customer withdrawal, and the money kept leaving for another two hours. |
| x4_h5 | OK 1.00 |  | Chainalysis, Elliptic, and TRM Labs all lean the same way. |
| x4_s5 | BAD 0.90 | chainalysis → chanalysis | Chanalysis, Elliptic, and TRM Labs all lean the same way. |
| x4_h6 | BAD 0.90 | chainalysis → shanealysis | Shanealysis, Elliptic, and TRM Labs all lean the same way. |
| x4_s6 | BAD 0.90 | chainalysis → tinalysis | Tinalysis, Elliptic and TRM labs all lean the same way. |
| x4_h7 | BAD 0.90 | chainalysis → shanealysis | Shanealysis, Elliptic, and TRM Labs all lean the same way. |
| x4_s7 | BAD 0.90 | chainalysis → tinalysis | Tinalysis, Elliptic and TRM labs all lean the same way. |
| x4_s8 | BAD 0.90 | chainalysis → chanalysis | Chanalysis, Elliptic and TRM labs all lean the same way. |
| x4_s9 | BAD 0.90 | chainalysis → chanalysis | Chanalysis, Elliptic, and TRM Labs all lean the same way. |
| x6_h5 | OK 1.00 |  | And Chainalysis watched the stolen Binance money meet the BitGet money on the blockchain. |
| x6_s5 | BAD 0.90 | bitget → bit get | And Chainalysis watched the stolen Binance money meet the bit get money on the blockchain. |
| x6_h6 | BAD 0.90 | bitget → bit get | And Chainalysis watched the stolen Binance money meet the bit get money on the blockchain. |
| x6_s6 | BAD 0.87 | bitget → bit to get | And Chainalysis watched the stolen Binance money meet the bit to get money on the blockchain. |
| x6_h7 | OK 1.00 |  | And Chainalysis watched the stolen Binance money meet the BitGet money on the blockchain. |
| x6_s7 | CHECK 0.93 | bitget → bitjet | And Chainalysis watched the stolen Binance money meet the BitJet money on the blockchain. |
| x6_s8 | BAD 0.90 | bitget → bitch get | And Chainalysis watched the stolen Binance money meet the bitch get money on the blockchain. |
| x6_s9 | BAD 0.90 | bitget → bic jet | And Chainalysis watched the stolen Binance money meet the BIC jet money on the blockchain. |

37 lines to look at

## Words heard with low confidence (p < 0.5)

| line | words |
|---|---|
| c3_h6 | withdrawal@1.1s p0.24 |
| c3_s7 | withdrawal@1.1s p0.43 |
| g5_s5 | BitGet@1.5s p0.36 |
| g5_s6 | BitGet@1.5s p0.29 |
| g5_s8 | A@0.0s p0.26 |
| g6_s9 | 23@2.6s p0.31 |
| t3_h5 | BitGet@3.3s p0.35 |
| t3_s5 | Bidget@3.1s p0.47 |
| t3_h6 | BitGet@2.8s p0.48 |
| x4_h5 | Labs@3.3s p0.41 |
| x4_s5 | Chanalysis,@0.0s p0.49, all@3.3s p0.43 |
| x4_h6 | Shanealysis,@0.6s p0.48 |
| x4_s6 | Tinalysis,@0.0s p0.43 |
| x4_h7 | Shanealysis,@0.0s p0.42 |
| x4_s8 | Chanalysis,@0.0s p0.41 |
| x4_s9 | Chanalysis,@0.0s p0.44 |
| x6_s6 | to@3.8s p0.37 |
| x6_s8 | bitch@3.2s p0.29 |
| x6_s9 | jet@3.5s p0.45 |
