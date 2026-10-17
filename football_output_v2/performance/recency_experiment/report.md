# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 268/284 fixture-markets; 74 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 37 | 0.1894 | 0.5628 | +0.0020 | +0.0065 | +3.8% |
| ALL | over_1_5 | goal_selected | 22 | 0.2185 | 0.6329 | -0.0055 | -0.0135 | +11.1% |
| ALL | over_1_5 | half_life_1000000000 | 37 | 0.1898 | 0.5656 | +0.0016 | +0.0036 | +3.3% |
| ALL | over_1_5 | half_life_120 | 37 | 0.1969 | 0.6027 | -0.0055 | -0.0334 | +5.9% |
| ALL | over_1_5 | half_life_240 | 37 | 0.1924 | 0.5777 | -0.0010 | -0.0084 | +4.7% |
| ALL | over_1_5 | half_life_365 | 37 | 0.1910 | 0.5712 | +0.0004 | -0.0019 | +4.2% |
| ALL | over_1_5 | half_life_730 | 37 | 0.1902 | 0.5676 | +0.0012 | +0.0017 | +3.7% |
| ALL | over_1_5 | production_raw | 37 | 0.1914 | 0.5693 | +0.0000 | +0.0000 | +3.8% |
| ALL | btts_yes | development_1x2 | 37 | 0.2572 | 0.7140 | +0.0013 | +0.0027 | +0.5% |
| ALL | btts_yes | goal_selected | 22 | 0.2386 | 0.6705 | -0.0003 | -0.0004 | -0.2% |
| ALL | btts_yes | half_life_1000000000 | 37 | 0.2597 | 0.7190 | -0.0012 | -0.0024 | +0.2% |
| ALL | btts_yes | half_life_120 | 37 | 0.2732 | 0.7516 | -0.0148 | -0.0350 | +0.9% |
| ALL | btts_yes | half_life_240 | 37 | 0.2638 | 0.7286 | -0.0053 | -0.0120 | +0.4% |
| ALL | btts_yes | half_life_365 | 37 | 0.2597 | 0.7198 | -0.0012 | -0.0031 | +0.4% |
| ALL | btts_yes | half_life_730 | 37 | 0.2585 | 0.7167 | -0.0000 | -0.0001 | +0.3% |
| ALL | btts_yes | production_raw | 37 | 0.2585 | 0.7167 | +0.0000 | +0.0000 | +0.4% |
| Bundesliga | over_1_5 | development_1x2 | 5 | 0.2300 | 0.6370 | +0.0045 | +0.0110 | +13.6% |
| Bundesliga | over_1_5 | goal_selected | 5 | 0.2390 | 0.6585 | -0.0045 | -0.0104 | +13.6% |
| Bundesliga | over_1_5 | half_life_1000000000 | 5 | 0.2300 | 0.6370 | +0.0045 | +0.0110 | +13.6% |
| Bundesliga | over_1_5 | half_life_120 | 5 | 0.2497 | 0.6825 | -0.0152 | -0.0345 | +14.6% |
| Bundesliga | over_1_5 | half_life_240 | 5 | 0.2430 | 0.6675 | -0.0085 | -0.0195 | +13.7% |
| Bundesliga | over_1_5 | half_life_365 | 5 | 0.2390 | 0.6585 | -0.0045 | -0.0104 | +13.6% |
| Bundesliga | over_1_5 | half_life_730 | 5 | 0.2345 | 0.6481 | +0.0000 | +0.0000 | +13.5% |
| Bundesliga | over_1_5 | production_raw | 5 | 0.2345 | 0.6481 | +0.0000 | +0.0000 | +13.5% |
| Bundesliga | btts_yes | development_1x2 | 5 | 0.2239 | 0.6403 | +0.0026 | +0.0057 | -9.5% |
| Bundesliga | btts_yes | goal_selected | 5 | 0.2298 | 0.6536 | -0.0033 | -0.0075 | -9.6% |
| Bundesliga | btts_yes | half_life_1000000000 | 5 | 0.2239 | 0.6403 | +0.0026 | +0.0057 | -9.5% |
| Bundesliga | btts_yes | half_life_120 | 5 | 0.2324 | 0.6597 | -0.0059 | -0.0137 | -9.3% |
| Bundesliga | btts_yes | half_life_240 | 5 | 0.2298 | 0.6536 | -0.0033 | -0.0075 | -9.6% |
| Bundesliga | btts_yes | half_life_365 | 5 | 0.2285 | 0.6504 | -0.0020 | -0.0044 | -9.6% |
| Bundesliga | btts_yes | half_life_730 | 5 | 0.2265 | 0.6460 | +0.0000 | +0.0000 | -9.6% |
| Bundesliga | btts_yes | production_raw | 5 | 0.2265 | 0.6460 | +0.0000 | +0.0000 | -9.6% |
| La Liga | over_1_5 | development_1x2 | 4 | 0.3392 | 0.9347 | -0.0009 | -0.0002 | +33.3% |
| La Liga | over_1_5 | goal_selected | 4 | 0.3453 | 0.9468 | -0.0070 | -0.0123 | +34.5% |
| La Liga | over_1_5 | half_life_1000000000 | 4 | 0.3388 | 0.9384 | -0.0005 | -0.0040 | +32.9% |
| La Liga | over_1_5 | half_life_120 | 4 | 0.3453 | 0.9468 | -0.0070 | -0.0123 | +34.5% |
| La Liga | over_1_5 | half_life_240 | 4 | 0.3409 | 0.9379 | -0.0026 | -0.0034 | +33.5% |
| La Liga | over_1_5 | half_life_365 | 4 | 0.3392 | 0.9347 | -0.0009 | -0.0002 | +33.3% |
| La Liga | over_1_5 | half_life_730 | 4 | 0.3383 | 0.9345 | +0.0000 | +0.0000 | +33.0% |
| La Liga | over_1_5 | production_raw | 4 | 0.3383 | 0.9345 | +0.0000 | +0.0000 | +33.0% |
| La Liga | btts_yes | development_1x2 | 4 | 0.2271 | 0.6453 | +0.0021 | +0.0049 | +11.0% |
| La Liga | btts_yes | goal_selected | 4 | 0.2264 | 0.6436 | +0.0027 | +0.0066 | +11.2% |
| La Liga | btts_yes | half_life_1000000000 | 4 | 0.2333 | 0.6594 | -0.0041 | -0.0093 | +10.9% |
| La Liga | btts_yes | half_life_120 | 4 | 0.2258 | 0.6414 | +0.0033 | +0.0088 | +12.3% |
| La Liga | btts_yes | half_life_240 | 4 | 0.2264 | 0.6436 | +0.0027 | +0.0066 | +11.2% |
| La Liga | btts_yes | half_life_365 | 4 | 0.2271 | 0.6453 | +0.0021 | +0.0049 | +11.0% |
| La Liga | btts_yes | half_life_730 | 4 | 0.2292 | 0.6502 | +0.0000 | +0.0000 | +10.9% |
| La Liga | btts_yes | production_raw | 4 | 0.2292 | 0.6502 | +0.0000 | +0.0000 | +10.9% |
| Ligue 1 | over_1_5 | development_1x2 | 4 | 0.0328 | 0.1946 | +0.0053 | +0.0182 | -17.6% |
| Ligue 1 | over_1_5 | goal_selected | 4 | 0.0413 | 0.2224 | -0.0033 | -0.0096 | -19.8% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 4 | 0.0413 | 0.2224 | -0.0033 | -0.0096 | -19.8% |
| Ligue 1 | over_1_5 | half_life_120 | 4 | 0.0296 | 0.1778 | +0.0084 | +0.0350 | -16.1% |
| Ligue 1 | over_1_5 | half_life_240 | 4 | 0.0328 | 0.1946 | +0.0053 | +0.0182 | -17.6% |
| Ligue 1 | over_1_5 | half_life_365 | 4 | 0.0351 | 0.2033 | +0.0029 | +0.0095 | -18.3% |
| Ligue 1 | over_1_5 | half_life_730 | 4 | 0.0380 | 0.2128 | +0.0000 | +0.0000 | -19.1% |
| Ligue 1 | over_1_5 | production_raw | 4 | 0.0380 | 0.2128 | +0.0000 | +0.0000 | -19.1% |
| Ligue 1 | btts_yes | development_1x2 | 4 | 0.2840 | 0.7647 | +0.0011 | +0.0013 | -18.2% |
| Ligue 1 | btts_yes | goal_selected | 4 | 0.2885 | 0.7728 | -0.0034 | -0.0068 | -20.2% |
| Ligue 1 | btts_yes | half_life_1000000000 | 4 | 0.2885 | 0.7728 | -0.0034 | -0.0068 | -20.2% |
| Ligue 1 | btts_yes | half_life_120 | 4 | 0.2918 | 0.7840 | -0.0067 | -0.0181 | -16.4% |
| Ligue 1 | btts_yes | half_life_240 | 4 | 0.2840 | 0.7647 | +0.0011 | +0.0013 | -18.2% |
| Ligue 1 | btts_yes | half_life_365 | 4 | 0.2837 | 0.7634 | +0.0014 | +0.0025 | -18.9% |
| Ligue 1 | btts_yes | half_life_730 | 4 | 0.2851 | 0.7660 | +0.0000 | +0.0000 | -19.6% |
| Ligue 1 | btts_yes | production_raw | 4 | 0.2851 | 0.7660 | +0.0000 | +0.0000 | -19.6% |
| Premier League | over_1_5 | development_1x2 | 5 | 0.2500 | 0.7016 | -0.0030 | -0.0052 | +20.4% |
| Premier League | over_1_5 | goal_selected | 5 | 0.2583 | 0.7280 | -0.0113 | -0.0316 | +20.2% |
| Premier League | over_1_5 | half_life_1000000000 | 5 | 0.2583 | 0.7280 | -0.0113 | -0.0316 | +20.2% |
| Premier League | over_1_5 | half_life_120 | 5 | 0.2461 | 0.7164 | +0.0009 | -0.0201 | +21.1% |
| Premier League | over_1_5 | half_life_240 | 5 | 0.2470 | 0.6964 | +0.0000 | +0.0000 | +20.5% |
| Premier League | over_1_5 | half_life_365 | 5 | 0.2500 | 0.7016 | -0.0030 | -0.0052 | +20.4% |
| Premier League | over_1_5 | half_life_730 | 5 | 0.2539 | 0.7126 | -0.0069 | -0.0163 | +20.2% |
| Premier League | over_1_5 | production_raw | 5 | 0.2470 | 0.6964 | +0.0000 | +0.0000 | +20.5% |
| Premier League | btts_yes | development_1x2 | 5 | 0.2668 | 0.7282 | +0.0028 | +0.0063 | +15.7% |
| Premier League | btts_yes | goal_selected | 5 | 0.2673 | 0.7291 | +0.0023 | +0.0054 | +15.4% |
| Premier League | btts_yes | half_life_1000000000 | 5 | 0.2708 | 0.7367 | -0.0012 | -0.0023 | +15.0% |
| Premier League | btts_yes | half_life_120 | 5 | 0.2918 | 0.7844 | -0.0222 | -0.0500 | +17.3% |
| Premier League | btts_yes | half_life_240 | 5 | 0.2696 | 0.7344 | +0.0000 | +0.0000 | +16.2% |
| Premier League | btts_yes | half_life_365 | 5 | 0.2668 | 0.7282 | +0.0028 | +0.0063 | +15.7% |
| Premier League | btts_yes | half_life_730 | 5 | 0.2673 | 0.7291 | +0.0023 | +0.0054 | +15.4% |
| Premier League | btts_yes | production_raw | 5 | 0.2696 | 0.7344 | +0.0000 | +0.0000 | +16.2% |
| Serie A | over_1_5 | development_1x2 | 4 | 0.1819 | 0.5439 | +0.0119 | +0.0349 | +2.8% |
| Serie A | over_1_5 | goal_selected | 4 | 0.1938 | 0.5788 | +0.0000 | +0.0000 | +4.0% |
| Serie A | over_1_5 | half_life_1000000000 | 4 | 0.1673 | 0.5057 | +0.0266 | +0.0731 | +1.1% |
| Serie A | over_1_5 | half_life_120 | 4 | 0.2221 | 0.6878 | -0.0283 | -0.1090 | +7.0% |
| Serie A | over_1_5 | half_life_240 | 4 | 0.1938 | 0.5788 | +0.0000 | +0.0000 | +4.0% |
| Serie A | over_1_5 | half_life_365 | 4 | 0.1819 | 0.5439 | +0.0119 | +0.0349 | +2.8% |
| Serie A | over_1_5 | half_life_730 | 4 | 0.1728 | 0.5196 | +0.0210 | +0.0592 | +1.8% |
| Serie A | over_1_5 | production_raw | 4 | 0.1938 | 0.5788 | +0.0000 | +0.0000 | +4.0% |
| Serie A | btts_yes | development_1x2 | 4 | 0.1744 | 0.5406 | +0.0017 | +0.0036 | +0.6% |
| Serie A | btts_yes | goal_selected | 4 | 0.1759 | 0.5434 | +0.0002 | +0.0008 | +0.9% |
| Serie A | btts_yes | half_life_1000000000 | 4 | 0.1815 | 0.5542 | -0.0053 | -0.0101 | +1.2% |
| Serie A | btts_yes | half_life_120 | 4 | 0.1795 | 0.5506 | -0.0033 | -0.0065 | +0.2% |
| Serie A | btts_yes | half_life_240 | 4 | 0.1761 | 0.5441 | +0.0000 | +0.0000 | +0.4% |
| Serie A | btts_yes | half_life_365 | 4 | 0.1744 | 0.5406 | +0.0017 | +0.0036 | +0.6% |
| Serie A | btts_yes | half_life_730 | 4 | 0.1759 | 0.5434 | +0.0002 | +0.0008 | +0.9% |
| Serie A | btts_yes | production_raw | 4 | 0.1761 | 0.5441 | +0.0000 | +0.0000 | +0.4% |
| UEFA Champions League | over_1_5 | development_1x2 | 15 | 0.1595 | 0.4958 | +0.0000 | +0.0000 | -6.8% |
| UEFA Champions League | over_1_5 | half_life_1000000000 | 15 | 0.1595 | 0.4958 | +0.0000 | +0.0000 | -6.8% |
| UEFA Champions League | over_1_5 | half_life_120 | 15 | 0.1612 | 0.5371 | -0.0016 | -0.0413 | -4.0% |
| UEFA Champions League | over_1_5 | half_life_240 | 15 | 0.1598 | 0.5140 | -0.0003 | -0.0182 | -5.2% |
| UEFA Champions League | over_1_5 | half_life_365 | 15 | 0.1598 | 0.5072 | -0.0003 | -0.0114 | -5.7% |
| UEFA Champions League | over_1_5 | half_life_730 | 15 | 0.1599 | 0.5019 | -0.0004 | -0.0061 | -6.3% |
| UEFA Champions League | over_1_5 | production_raw | 15 | 0.1595 | 0.4958 | +0.0000 | +0.0000 | -6.8% |
| UEFA Champions League | btts_yes | development_1x2 | 15 | 0.2880 | 0.7849 | +0.0000 | +0.0000 | +0.9% |
| UEFA Champions League | btts_yes | half_life_1000000000 | 15 | 0.2880 | 0.7849 | +0.0000 | +0.0000 | +0.9% |
| UEFA Champions League | btts_yes | half_life_120 | 15 | 0.3134 | 0.8457 | -0.0253 | -0.0608 | +0.6% |
| UEFA Champions League | btts_yes | half_life_240 | 15 | 0.3011 | 0.8140 | -0.0130 | -0.0291 | +0.4% |
| UEFA Champions League | btts_yes | half_life_365 | 15 | 0.2927 | 0.7962 | -0.0047 | -0.0113 | +0.8% |
| UEFA Champions League | btts_yes | half_life_730 | 15 | 0.2889 | 0.7870 | -0.0009 | -0.0021 | +1.0% |
| UEFA Champions League | btts_yes | production_raw | 15 | 0.2880 | 0.7849 | +0.0000 | +0.0000 | +0.9% |

Positive paired gain means lower error than the raw production model on those same matches. A 30-match review prompt is not statistical proof.

Calibration buckets, approximate paired-gain intervals, gameweek comparisons and historical selection stability for each frozen run are retained in summary.json. Historical audits overlap and are not additional forward samples.

## Latest historical development/audit diagnostics

| League | Market | Goal half-life | Development N | Audit N | Audit log-loss gain | Development fold wins |
|---|---|---:|---:|---:|---:|---|
| Premier League | over_1_5 | 1000000000.0 | 310 | 60 | +0.0040 | {'240.0': 1, '1000000000.0': 3} |
| Premier League | btts_yes | 730.0 | 310 | 60 | -0.0000 | {'1000000000.0': 2, '365.0': 1, '120.0': 1} |
| La Liga | over_1_5 | 120.0 | 300 | 79 | -0.0017 | {'120.0': 3, '240.0': 1} |
| La Liga | btts_yes | 240.0 | 300 | 79 | +0.0020 | {'365.0': 1, '120.0': 3} |
| Bundesliga | over_1_5 | 365.0 | 252 | 46 | -0.0103 | {'730.0': 1, '1000000000.0': 2, '120.0': 1} |
| Bundesliga | btts_yes | 240.0 | 252 | 46 | -0.0051 | {'120.0': 2, '730.0': 1, '240.0': 1} |
| Serie A | over_1_5 | 240.0 | 320 | 61 | -0.0015 | {'120.0': 1, '240.0': 1, '1000000000.0': 1, '365.0': 1} |
| Serie A | btts_yes | 1000000000.0 | 320 | 61 | -0.0037 | {'1000000000.0': 2, '120.0': 1, '365.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 243 | 55 | -0.0197 | {'1000000000.0': 3, '120.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 243 | 55 | -0.0087 | {'1000000000.0': 3, '120.0': 1} |
| UEFA Champions League | over_1_5 | 120.0 | 152 | 37 | -0.0232 | {'240.0': 2, '120.0': 2} |
| UEFA Champions League | btts_yes | 730.0 | 152 | 37 | +0.0027 | {'240.0': 1, '1000000000.0': 3} |