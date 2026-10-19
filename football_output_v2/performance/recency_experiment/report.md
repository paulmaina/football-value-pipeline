# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 268/284 fixture-markets; 102 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 51 | 0.1747 | 0.5277 | +0.0026 | +0.0086 | +0.1% |
| ALL | over_1_5 | goal_selected | 36 | 0.1890 | 0.5657 | -0.0042 | -0.0126 | +3.4% |
| ALL | over_1_5 | half_life_1000000000 | 51 | 0.1786 | 0.5400 | -0.0012 | -0.0037 | -0.2% |
| ALL | over_1_5 | half_life_120 | 51 | 0.1757 | 0.5448 | +0.0016 | -0.0086 | +1.9% |
| ALL | over_1_5 | half_life_240 | 51 | 0.1760 | 0.5366 | +0.0013 | -0.0004 | +0.8% |
| ALL | over_1_5 | half_life_365 | 51 | 0.1764 | 0.5357 | +0.0009 | +0.0006 | +0.4% |
| ALL | over_1_5 | half_life_730 | 51 | 0.1773 | 0.5370 | +0.0000 | -0.0007 | +0.1% |
| ALL | over_1_5 | production_raw | 51 | 0.1773 | 0.5363 | +0.0000 | +0.0000 | +0.1% |
| ALL | btts_yes | development_1x2 | 51 | 0.2589 | 0.7166 | +0.0025 | +0.0052 | +1.2% |
| ALL | btts_yes | goal_selected | 36 | 0.2468 | 0.6887 | +0.0034 | +0.0068 | +1.6% |
| ALL | btts_yes | half_life_1000000000 | 51 | 0.2615 | 0.7222 | -0.0002 | -0.0004 | +1.1% |
| ALL | btts_yes | half_life_120 | 51 | 0.2690 | 0.7415 | -0.0077 | -0.0197 | +1.8% |
| ALL | btts_yes | half_life_240 | 51 | 0.2631 | 0.7262 | -0.0017 | -0.0044 | +1.3% |
| ALL | btts_yes | half_life_365 | 51 | 0.2605 | 0.7205 | +0.0008 | +0.0012 | +1.2% |
| ALL | btts_yes | half_life_730 | 51 | 0.2601 | 0.7192 | +0.0013 | +0.0025 | +1.2% |
| ALL | btts_yes | production_raw | 51 | 0.2613 | 0.7218 | +0.0000 | +0.0000 | +1.1% |
| Bundesliga | over_1_5 | development_1x2 | 7 | 0.1684 | 0.4912 | +0.0035 | +0.0091 | +6.3% |
| Bundesliga | over_1_5 | goal_selected | 7 | 0.1751 | 0.5081 | -0.0032 | -0.0077 | +6.2% |
| Bundesliga | over_1_5 | half_life_1000000000 | 7 | 0.1684 | 0.4912 | +0.0035 | +0.0091 | +6.3% |
| Bundesliga | over_1_5 | half_life_120 | 7 | 0.1814 | 0.5188 | -0.0096 | -0.0185 | +7.5% |
| Bundesliga | over_1_5 | half_life_240 | 7 | 0.1778 | 0.5138 | -0.0060 | -0.0134 | +6.4% |
| Bundesliga | over_1_5 | half_life_365 | 7 | 0.1751 | 0.5081 | -0.0032 | -0.0077 | +6.2% |
| Bundesliga | over_1_5 | half_life_730 | 7 | 0.1718 | 0.5003 | +0.0000 | +0.0000 | +6.2% |
| Bundesliga | over_1_5 | production_raw | 7 | 0.1718 | 0.5003 | +0.0000 | +0.0000 | +6.2% |
| Bundesliga | btts_yes | development_1x2 | 7 | 0.1961 | 0.5815 | -0.0001 | +0.0003 | -16.7% |
| Bundesliga | btts_yes | goal_selected | 7 | 0.1946 | 0.5795 | +0.0013 | +0.0023 | -16.1% |
| Bundesliga | btts_yes | half_life_1000000000 | 7 | 0.1961 | 0.5815 | -0.0001 | +0.0003 | -16.7% |
| Bundesliga | btts_yes | half_life_120 | 7 | 0.1907 | 0.5702 | +0.0053 | +0.0116 | -15.0% |
| Bundesliga | btts_yes | half_life_240 | 7 | 0.1946 | 0.5795 | +0.0013 | +0.0023 | -16.1% |
| Bundesliga | btts_yes | half_life_365 | 7 | 0.1956 | 0.5813 | +0.0004 | +0.0005 | -16.4% |
| Bundesliga | btts_yes | half_life_730 | 7 | 0.1960 | 0.5818 | +0.0000 | +0.0000 | -16.6% |
| Bundesliga | btts_yes | production_raw | 7 | 0.1960 | 0.5818 | +0.0000 | +0.0000 | -16.6% |
| La Liga | over_1_5 | development_1x2 | 7 | 0.2211 | 0.6414 | +0.0031 | +0.0074 | +10.1% |
| La Liga | over_1_5 | goal_selected | 7 | 0.2154 | 0.6274 | +0.0087 | +0.0214 | +12.2% |
| La Liga | over_1_5 | half_life_1000000000 | 7 | 0.2279 | 0.6581 | -0.0037 | -0.0093 | +9.0% |
| La Liga | over_1_5 | half_life_120 | 7 | 0.2154 | 0.6274 | +0.0087 | +0.0214 | +12.2% |
| La Liga | over_1_5 | half_life_240 | 7 | 0.2188 | 0.6361 | +0.0054 | +0.0127 | +10.7% |
| La Liga | over_1_5 | half_life_365 | 7 | 0.2211 | 0.6414 | +0.0031 | +0.0074 | +10.1% |
| La Liga | over_1_5 | half_life_730 | 7 | 0.2241 | 0.6488 | +0.0000 | +0.0000 | +9.5% |
| La Liga | over_1_5 | production_raw | 7 | 0.2241 | 0.6488 | +0.0000 | +0.0000 | +9.5% |
| La Liga | btts_yes | development_1x2 | 7 | 0.3042 | 0.8110 | +0.0054 | +0.0112 | +0.6% |
| La Liga | btts_yes | goal_selected | 7 | 0.3008 | 0.8048 | +0.0088 | +0.0174 | +1.3% |
| La Liga | btts_yes | half_life_1000000000 | 7 | 0.3170 | 0.8384 | -0.0074 | -0.0163 | -0.5% |
| La Liga | btts_yes | half_life_120 | 7 | 0.2980 | 0.8043 | +0.0116 | +0.0179 | +3.2% |
| La Liga | btts_yes | half_life_240 | 7 | 0.3008 | 0.8048 | +0.0088 | +0.0174 | +1.3% |
| La Liga | btts_yes | half_life_365 | 7 | 0.3042 | 0.8110 | +0.0054 | +0.0112 | +0.6% |
| La Liga | btts_yes | half_life_730 | 7 | 0.3096 | 0.8222 | +0.0000 | +0.0000 | -0.0% |
| La Liga | btts_yes | production_raw | 7 | 0.3096 | 0.8222 | +0.0000 | +0.0000 | -0.0% |
| Ligue 1 | over_1_5 | development_1x2 | 6 | 0.1443 | 0.4573 | +0.0125 | +0.0430 | -4.0% |
| Ligue 1 | over_1_5 | goal_selected | 6 | 0.1637 | 0.5261 | -0.0069 | -0.0258 | -4.1% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 6 | 0.1637 | 0.5261 | -0.0069 | -0.0258 | -4.1% |
| Ligue 1 | over_1_5 | half_life_120 | 6 | 0.1277 | 0.4063 | +0.0290 | +0.0941 | -3.9% |
| Ligue 1 | over_1_5 | half_life_240 | 6 | 0.1443 | 0.4573 | +0.0125 | +0.0430 | -4.0% |
| Ligue 1 | over_1_5 | half_life_365 | 6 | 0.1503 | 0.4777 | +0.0065 | +0.0227 | -4.1% |
| Ligue 1 | over_1_5 | half_life_730 | 6 | 0.1567 | 0.5003 | +0.0000 | +0.0000 | -4.1% |
| Ligue 1 | over_1_5 | production_raw | 6 | 0.1567 | 0.5003 | +0.0000 | +0.0000 | -4.1% |
| Ligue 1 | btts_yes | development_1x2 | 6 | 0.2945 | 0.7850 | +0.0060 | +0.0122 | -11.2% |
| Ligue 1 | btts_yes | goal_selected | 6 | 0.3047 | 0.8062 | -0.0042 | -0.0090 | -11.2% |
| Ligue 1 | btts_yes | half_life_1000000000 | 6 | 0.3047 | 0.8062 | -0.0042 | -0.0090 | -11.2% |
| Ligue 1 | btts_yes | half_life_120 | 6 | 0.2886 | 0.7753 | +0.0119 | +0.0219 | -10.9% |
| Ligue 1 | btts_yes | half_life_240 | 6 | 0.2945 | 0.7850 | +0.0060 | +0.0122 | -11.2% |
| Ligue 1 | btts_yes | half_life_365 | 6 | 0.2972 | 0.7903 | +0.0033 | +0.0069 | -11.2% |
| Ligue 1 | btts_yes | half_life_730 | 6 | 0.3006 | 0.7971 | +0.0000 | +0.0000 | -11.2% |
| Ligue 1 | btts_yes | production_raw | 6 | 0.3006 | 0.7971 | +0.0000 | +0.0000 | -11.2% |
| Premier League | over_1_5 | development_1x2 | 9 | 0.2100 | 0.6081 | -0.0047 | -0.0107 | +11.3% |
| Premier League | over_1_5 | goal_selected | 9 | 0.2218 | 0.6412 | -0.0166 | -0.0438 | +10.9% |
| Premier League | over_1_5 | half_life_1000000000 | 9 | 0.2218 | 0.6412 | -0.0166 | -0.0438 | +10.9% |
| Premier League | over_1_5 | half_life_120 | 9 | 0.1994 | 0.5935 | +0.0059 | +0.0038 | +12.2% |
| Premier League | over_1_5 | half_life_240 | 9 | 0.2053 | 0.5973 | +0.0000 | +0.0000 | +11.6% |
| Premier League | over_1_5 | half_life_365 | 9 | 0.2100 | 0.6081 | -0.0047 | -0.0107 | +11.3% |
| Premier League | over_1_5 | half_life_730 | 9 | 0.2157 | 0.6231 | -0.0104 | -0.0257 | +11.1% |
| Premier League | over_1_5 | production_raw | 9 | 0.2053 | 0.5973 | +0.0000 | +0.0000 | +11.6% |
| Premier League | btts_yes | development_1x2 | 9 | 0.2571 | 0.7081 | +0.0018 | +0.0040 | +20.8% |
| Premier League | btts_yes | goal_selected | 9 | 0.2574 | 0.7086 | +0.0015 | +0.0034 | +20.5% |
| Premier League | btts_yes | half_life_1000000000 | 9 | 0.2595 | 0.7134 | -0.0006 | -0.0013 | +20.2% |
| Premier League | btts_yes | half_life_120 | 9 | 0.2734 | 0.7441 | -0.0145 | -0.0320 | +21.5% |
| Premier League | btts_yes | half_life_240 | 9 | 0.2589 | 0.7121 | +0.0000 | +0.0000 | +21.1% |
| Premier League | btts_yes | half_life_365 | 9 | 0.2571 | 0.7081 | +0.0018 | +0.0040 | +20.8% |
| Premier League | btts_yes | half_life_730 | 9 | 0.2574 | 0.7086 | +0.0015 | +0.0034 | +20.5% |
| Premier League | btts_yes | production_raw | 9 | 0.2589 | 0.7121 | +0.0000 | +0.0000 | +21.1% |
| Serie A | over_1_5 | development_1x2 | 7 | 0.1479 | 0.4755 | +0.0080 | +0.0231 | -12.1% |
| Serie A | over_1_5 | goal_selected | 7 | 0.1558 | 0.4986 | +0.0000 | +0.0000 | -11.6% |
| Serie A | over_1_5 | half_life_1000000000 | 7 | 0.1374 | 0.4468 | +0.0185 | +0.0518 | -12.4% |
| Serie A | over_1_5 | half_life_120 | 7 | 0.1722 | 0.5610 | -0.0164 | -0.0624 | -9.8% |
| Serie A | over_1_5 | half_life_240 | 7 | 0.1558 | 0.4986 | +0.0000 | +0.0000 | -11.6% |
| Serie A | over_1_5 | half_life_365 | 7 | 0.1479 | 0.4755 | +0.0080 | +0.0231 | -12.1% |
| Serie A | over_1_5 | half_life_730 | 7 | 0.1414 | 0.4580 | +0.0144 | +0.0406 | -12.3% |
| Serie A | over_1_5 | production_raw | 7 | 0.1558 | 0.4986 | +0.0000 | +0.0000 | -11.6% |
| Serie A | btts_yes | development_1x2 | 7 | 0.1856 | 0.5633 | +0.0052 | +0.0105 | +5.9% |
| Serie A | btts_yes | goal_selected | 7 | 0.1817 | 0.5553 | +0.0091 | +0.0185 | +6.4% |
| Serie A | btts_yes | half_life_1000000000 | 7 | 0.1799 | 0.5514 | +0.0109 | +0.0224 | +6.9% |
| Serie A | btts_yes | half_life_120 | 7 | 0.2012 | 0.5945 | -0.0104 | -0.0206 | +5.2% |
| Serie A | btts_yes | half_life_240 | 7 | 0.1908 | 0.5738 | +0.0000 | +0.0000 | +5.5% |
| Serie A | btts_yes | half_life_365 | 7 | 0.1856 | 0.5633 | +0.0052 | +0.0105 | +5.9% |
| Serie A | btts_yes | half_life_730 | 7 | 0.1817 | 0.5553 | +0.0091 | +0.0185 | +6.4% |
| Serie A | btts_yes | production_raw | 7 | 0.1908 | 0.5738 | +0.0000 | +0.0000 | +5.5% |
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
| Premier League | over_1_5 | 1000000000.0 | 303 | 69 | -0.0107 | {'1000000000.0': 3, '240.0': 1} |
| Premier League | btts_yes | 1000000000.0 | 303 | 69 | -0.0117 | {'1000000000.0': 2, '365.0': 1, '120.0': 1} |
| La Liga | over_1_5 | 120.0 | 295 | 87 | -0.0125 | {'120.0': 2, '730.0': 1, '1000000000.0': 1} |
| La Liga | btts_yes | 120.0 | 295 | 87 | -0.0019 | {'240.0': 1, '1000000000.0': 1, '120.0': 2} |
| Bundesliga | over_1_5 | 1000000000.0 | 245 | 54 | +0.0033 | {'1000000000.0': 3, '240.0': 1} |
| Bundesliga | btts_yes | 240.0 | 245 | 54 | +0.0005 | {'730.0': 1, '240.0': 1, '1000000000.0': 1, '120.0': 1} |
| Serie A | over_1_5 | 240.0 | 316 | 68 | -0.0085 | {'240.0': 2, '120.0': 1, '1000000000.0': 1} |
| Serie A | btts_yes | 365.0 | 316 | 68 | -0.0037 | {'730.0': 1, '120.0': 1, '1000000000.0': 1, '240.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 239 | 63 | +0.0000 | {'1000000000.0': 2, '120.0': 1, '240.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 239 | 63 | +0.0000 | {'1000000000.0': 3, '120.0': 1} |
| UEFA Champions League | over_1_5 | 120.0 | 152 | 37 | -0.0231 | {'240.0': 2, '120.0': 2} |
| UEFA Champions League | btts_yes | 730.0 | 152 | 37 | +0.0030 | {'240.0': 1, '1000000000.0': 3} |