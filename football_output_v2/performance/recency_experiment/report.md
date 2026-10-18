# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 268/284 fixture-markets; 96 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 48 | 0.1825 | 0.5464 | +0.0027 | +0.0088 | +1.4% |
| ALL | over_1_5 | goal_selected | 33 | 0.2014 | 0.5954 | -0.0045 | -0.0133 | +5.5% |
| ALL | over_1_5 | half_life_1000000000 | 48 | 0.1867 | 0.5595 | -0.0015 | -0.0043 | +1.1% |
| ALL | over_1_5 | half_life_120 | 48 | 0.1833 | 0.5639 | +0.0019 | -0.0088 | +3.3% |
| ALL | over_1_5 | half_life_240 | 48 | 0.1838 | 0.5554 | +0.0014 | -0.0003 | +2.1% |
| ALL | over_1_5 | half_life_365 | 48 | 0.1843 | 0.5546 | +0.0009 | +0.0005 | +1.7% |
| ALL | over_1_5 | half_life_730 | 48 | 0.1853 | 0.5562 | -0.0001 | -0.0011 | +1.3% |
| ALL | over_1_5 | production_raw | 48 | 0.1852 | 0.5551 | +0.0000 | +0.0000 | +1.4% |
| ALL | btts_yes | development_1x2 | 48 | 0.2641 | 0.7278 | +0.0024 | +0.0051 | +2.0% |
| ALL | btts_yes | goal_selected | 33 | 0.2530 | 0.7018 | +0.0037 | +0.0075 | +2.8% |
| ALL | btts_yes | half_life_1000000000 | 48 | 0.2665 | 0.7331 | -0.0000 | -0.0002 | +1.9% |
| ALL | btts_yes | half_life_120 | 48 | 0.2755 | 0.7557 | -0.0090 | -0.0228 | +2.6% |
| ALL | btts_yes | half_life_240 | 48 | 0.2685 | 0.7378 | -0.0020 | -0.0049 | +2.1% |
| ALL | btts_yes | half_life_365 | 48 | 0.2656 | 0.7314 | +0.0009 | +0.0014 | +2.1% |
| ALL | btts_yes | half_life_730 | 48 | 0.2650 | 0.7299 | +0.0015 | +0.0030 | +2.0% |
| ALL | btts_yes | production_raw | 48 | 0.2665 | 0.7329 | +0.0000 | +0.0000 | +2.0% |
| Bundesliga | over_1_5 | development_1x2 | 6 | 0.1946 | 0.5547 | +0.0037 | +0.0089 | +9.1% |
| Bundesliga | over_1_5 | goal_selected | 6 | 0.2019 | 0.5717 | -0.0036 | -0.0081 | +9.2% |
| Bundesliga | over_1_5 | half_life_1000000000 | 6 | 0.1946 | 0.5547 | +0.0037 | +0.0089 | +9.1% |
| Bundesliga | over_1_5 | half_life_120 | 6 | 0.2100 | 0.5880 | -0.0117 | -0.0244 | +10.3% |
| Bundesliga | over_1_5 | half_life_240 | 6 | 0.2051 | 0.5784 | -0.0068 | -0.0148 | +9.4% |
| Bundesliga | over_1_5 | half_life_365 | 6 | 0.2019 | 0.5717 | -0.0036 | -0.0081 | +9.2% |
| Bundesliga | over_1_5 | half_life_730 | 6 | 0.1983 | 0.5636 | +0.0000 | +0.0000 | +9.1% |
| Bundesliga | over_1_5 | production_raw | 6 | 0.1983 | 0.5636 | +0.0000 | +0.0000 | +9.1% |
| Bundesliga | btts_yes | development_1x2 | 6 | 0.2159 | 0.6243 | -0.0013 | -0.0025 | -14.9% |
| Bundesliga | btts_yes | goal_selected | 6 | 0.2126 | 0.6178 | +0.0020 | +0.0039 | -13.9% |
| Bundesliga | btts_yes | half_life_1000000000 | 6 | 0.2159 | 0.6243 | -0.0013 | -0.0025 | -14.9% |
| Bundesliga | btts_yes | half_life_120 | 6 | 0.2108 | 0.6142 | +0.0038 | +0.0075 | -13.1% |
| Bundesliga | btts_yes | half_life_240 | 6 | 0.2126 | 0.6178 | +0.0020 | +0.0039 | -13.9% |
| Bundesliga | btts_yes | half_life_365 | 6 | 0.2136 | 0.6198 | +0.0010 | +0.0020 | -14.2% |
| Bundesliga | btts_yes | half_life_730 | 6 | 0.2146 | 0.6218 | +0.0000 | +0.0000 | -14.6% |
| Bundesliga | btts_yes | production_raw | 6 | 0.2146 | 0.6218 | +0.0000 | +0.0000 | -14.6% |
| La Liga | over_1_5 | development_1x2 | 6 | 0.2542 | 0.7214 | +0.0036 | +0.0086 | +14.3% |
| La Liga | over_1_5 | goal_selected | 6 | 0.2472 | 0.7036 | +0.0106 | +0.0264 | +16.9% |
| La Liga | over_1_5 | half_life_1000000000 | 6 | 0.2621 | 0.7406 | -0.0043 | -0.0106 | +13.1% |
| La Liga | over_1_5 | half_life_120 | 6 | 0.2472 | 0.7036 | +0.0106 | +0.0264 | +16.9% |
| La Liga | over_1_5 | half_life_240 | 6 | 0.2515 | 0.7149 | +0.0063 | +0.0150 | +15.0% |
| La Liga | over_1_5 | half_life_365 | 6 | 0.2542 | 0.7214 | +0.0036 | +0.0086 | +14.3% |
| La Liga | over_1_5 | half_life_730 | 6 | 0.2578 | 0.7300 | +0.0000 | +0.0000 | +13.6% |
| La Liga | over_1_5 | production_raw | 6 | 0.2578 | 0.7300 | +0.0000 | +0.0000 | +13.6% |
| La Liga | btts_yes | development_1x2 | 6 | 0.3121 | 0.8283 | +0.0053 | +0.0111 | +9.1% |
| La Liga | btts_yes | goal_selected | 6 | 0.3088 | 0.8223 | +0.0086 | +0.0170 | +9.8% |
| La Liga | btts_yes | half_life_1000000000 | 6 | 0.3246 | 0.8554 | -0.0072 | -0.0161 | +8.1% |
| La Liga | btts_yes | half_life_120 | 6 | 0.3065 | 0.8238 | +0.0109 | +0.0155 | +12.0% |
| La Liga | btts_yes | half_life_240 | 6 | 0.3088 | 0.8223 | +0.0086 | +0.0170 | +9.8% |
| La Liga | btts_yes | half_life_365 | 6 | 0.3121 | 0.8283 | +0.0053 | +0.0111 | +9.1% |
| La Liga | btts_yes | half_life_730 | 6 | 0.3174 | 0.8393 | +0.0000 | +0.0000 | +8.5% |
| La Liga | btts_yes | production_raw | 6 | 0.3174 | 0.8393 | +0.0000 | +0.0000 | +8.5% |
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
| Serie A | over_1_5 | development_1x2 | 6 | 0.1534 | 0.4860 | +0.0087 | +0.0256 | -8.4% |
| Serie A | over_1_5 | goal_selected | 6 | 0.1621 | 0.5115 | +0.0000 | +0.0000 | -7.8% |
| Serie A | over_1_5 | half_life_1000000000 | 6 | 0.1414 | 0.4530 | +0.0207 | +0.0585 | -8.9% |
| Serie A | over_1_5 | half_life_120 | 6 | 0.1796 | 0.5807 | -0.0174 | -0.0691 | -5.5% |
| Serie A | over_1_5 | half_life_240 | 6 | 0.1621 | 0.5115 | +0.0000 | +0.0000 | -7.8% |
| Serie A | over_1_5 | half_life_365 | 6 | 0.1534 | 0.4860 | +0.0087 | +0.0256 | -8.4% |
| Serie A | over_1_5 | half_life_730 | 6 | 0.1462 | 0.4663 | +0.0159 | +0.0453 | -8.8% |
| Serie A | over_1_5 | production_raw | 6 | 0.1621 | 0.5115 | +0.0000 | +0.0000 | -7.8% |
| Serie A | btts_yes | development_1x2 | 6 | 0.1843 | 0.5606 | +0.0068 | +0.0138 | -0.4% |
| Serie A | btts_yes | goal_selected | 6 | 0.1794 | 0.5505 | +0.0118 | +0.0239 | +0.1% |
| Serie A | btts_yes | half_life_1000000000 | 6 | 0.1775 | 0.5464 | +0.0136 | +0.0280 | +0.8% |
| Serie A | btts_yes | half_life_120 | 6 | 0.2049 | 0.6018 | -0.0137 | -0.0275 | -0.9% |
| Serie A | btts_yes | half_life_240 | 6 | 0.1911 | 0.5744 | +0.0000 | +0.0000 | -0.8% |
| Serie A | btts_yes | half_life_365 | 6 | 0.1843 | 0.5606 | +0.0068 | +0.0138 | -0.4% |
| Serie A | btts_yes | half_life_730 | 6 | 0.1794 | 0.5505 | +0.0118 | +0.0239 | +0.1% |
| Serie A | btts_yes | production_raw | 6 | 0.1911 | 0.5744 | +0.0000 | +0.0000 | -0.8% |
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
| Premier League | over_1_5 | 1000000000.0 | 310 | 65 | +0.0016 | {'240.0': 1, '1000000000.0': 3} |
| Premier League | btts_yes | 730.0 | 310 | 65 | -0.0014 | {'1000000000.0': 2, '240.0': 1, '120.0': 1} |
| La Liga | over_1_5 | 120.0 | 299 | 83 | -0.0048 | {'120.0': 3, '365.0': 1} |
| La Liga | btts_yes | 240.0 | 299 | 83 | +0.0015 | {'730.0': 1, '240.0': 1, '120.0': 2} |
| Bundesliga | over_1_5 | 365.0 | 251 | 52 | -0.0140 | {'730.0': 1, '1000000000.0': 2, '120.0': 1} |
| Bundesliga | btts_yes | 240.0 | 251 | 52 | -0.0078 | {'120.0': 2, '365.0': 2} |
| Serie A | over_1_5 | 240.0 | 320 | 64 | -0.0041 | {'120.0': 1, '240.0': 1, '1000000000.0': 1, '365.0': 1} |
| Serie A | btts_yes | 730.0 | 320 | 64 | -0.0007 | {'1000000000.0': 2, '120.0': 1, '365.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 242 | 58 | -0.0138 | {'1000000000.0': 3, '120.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 242 | 58 | -0.0070 | {'1000000000.0': 3, '120.0': 1} |
| UEFA Champions League | over_1_5 | 120.0 | 152 | 37 | -0.0230 | {'240.0': 2, '120.0': 2} |
| UEFA Champions League | btts_yes | 730.0 | 152 | 37 | +0.0030 | {'240.0': 1, '1000000000.0': 3} |