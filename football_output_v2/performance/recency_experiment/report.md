# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 378/416 fixture-markets; 206 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 103 | 0.1705 | 0.5720 | +0.0018 | +0.0031 | -4.3% |
| ALL | over_1_5 | goal_selected | 88 | 0.1781 | 0.5898 | -0.0035 | -0.0011 | -4.2% |
| ALL | over_1_5 | half_life_1000000000 | 103 | 0.1729 | 0.5792 | -0.0005 | -0.0040 | -4.5% |
| ALL | over_1_5 | half_life_120 | 103 | 0.1743 | 0.5794 | -0.0019 | -0.0042 | -4.2% |
| ALL | over_1_5 | half_life_240 | 103 | 0.1712 | 0.5598 | +0.0012 | +0.0154 | -4.3% |
| ALL | over_1_5 | half_life_365 | 103 | 0.1712 | 0.5643 | +0.0012 | +0.0109 | -4.3% |
| ALL | over_1_5 | half_life_730 | 103 | 0.1719 | 0.5721 | +0.0005 | +0.0031 | -4.4% |
| ALL | over_1_5 | production_raw | 103 | 0.1724 | 0.5752 | +0.0000 | +0.0000 | -4.3% |
| ALL | btts_yes | development_1x2 | 103 | 0.2655 | 0.7434 | +0.0016 | +0.0036 | -5.9% |
| ALL | btts_yes | goal_selected | 88 | 0.2647 | 0.7446 | -0.0012 | -0.0041 | -6.8% |
| ALL | btts_yes | half_life_1000000000 | 103 | 0.2671 | 0.7470 | -0.0001 | -0.0000 | -6.0% |
| ALL | btts_yes | half_life_120 | 103 | 0.2833 | 0.7963 | -0.0162 | -0.0494 | -5.9% |
| ALL | btts_yes | half_life_240 | 103 | 0.2719 | 0.7628 | -0.0048 | -0.0159 | -5.7% |
| ALL | btts_yes | half_life_365 | 103 | 0.2691 | 0.7544 | -0.0020 | -0.0074 | -5.7% |
| ALL | btts_yes | half_life_730 | 103 | 0.2674 | 0.7489 | -0.0004 | -0.0020 | -5.8% |
| ALL | btts_yes | production_raw | 103 | 0.2670 | 0.7470 | +0.0000 | +0.0000 | -5.9% |
| Bundesliga | over_1_5 | development_1x2 | 8 | 0.1487 | 0.4437 | +0.0032 | +0.0088 | +4.2% |
| Bundesliga | over_1_5 | goal_selected | 8 | 0.1548 | 0.4595 | -0.0029 | -0.0071 | +4.0% |
| Bundesliga | over_1_5 | half_life_1000000000 | 8 | 0.1487 | 0.4437 | +0.0032 | +0.0088 | +4.2% |
| Bundesliga | over_1_5 | half_life_120 | 8 | 0.1599 | 0.4666 | -0.0080 | -0.0141 | +5.3% |
| Bundesliga | over_1_5 | half_life_240 | 8 | 0.1571 | 0.4643 | -0.0052 | -0.0118 | +4.2% |
| Bundesliga | over_1_5 | half_life_365 | 8 | 0.1548 | 0.4595 | -0.0029 | -0.0071 | +4.0% |
| Bundesliga | over_1_5 | half_life_730 | 8 | 0.1519 | 0.4524 | +0.0000 | +0.0000 | +4.0% |
| Bundesliga | over_1_5 | production_raw | 8 | 0.1519 | 0.4524 | +0.0000 | +0.0000 | +4.0% |
| Bundesliga | btts_yes | development_1x2 | 8 | 0.1868 | 0.5624 | +0.0008 | +0.0023 | -19.0% |
| Bundesliga | btts_yes | goal_selected | 8 | 0.1881 | 0.5662 | -0.0005 | -0.0015 | -18.8% |
| Bundesliga | btts_yes | half_life_1000000000 | 8 | 0.1868 | 0.5624 | +0.0008 | +0.0023 | -19.0% |
| Bundesliga | btts_yes | half_life_120 | 8 | 0.1859 | 0.5610 | +0.0016 | +0.0037 | -18.0% |
| Bundesliga | btts_yes | half_life_240 | 8 | 0.1881 | 0.5662 | -0.0005 | -0.0015 | -18.8% |
| Bundesliga | btts_yes | half_life_365 | 8 | 0.1881 | 0.5662 | -0.0005 | -0.0015 | -19.0% |
| Bundesliga | btts_yes | half_life_730 | 8 | 0.1876 | 0.5647 | +0.0000 | +0.0000 | -19.0% |
| Bundesliga | btts_yes | production_raw | 8 | 0.1876 | 0.5647 | +0.0000 | +0.0000 | -19.0% |
| La Liga | over_1_5 | development_1x2 | 13 | 0.2187 | 0.6384 | +0.0029 | +0.0063 | +0.2% |
| La Liga | over_1_5 | goal_selected | 13 | 0.2136 | 0.6300 | +0.0081 | +0.0147 | +2.3% |
| La Liga | over_1_5 | half_life_1000000000 | 13 | 0.2250 | 0.6527 | -0.0033 | -0.0080 | -0.8% |
| La Liga | over_1_5 | half_life_120 | 13 | 0.2136 | 0.6300 | +0.0081 | +0.0147 | +2.3% |
| La Liga | over_1_5 | half_life_240 | 13 | 0.2164 | 0.6339 | +0.0052 | +0.0108 | +0.8% |
| La Liga | over_1_5 | half_life_365 | 13 | 0.2187 | 0.6384 | +0.0029 | +0.0063 | +0.2% |
| La Liga | over_1_5 | half_life_730 | 13 | 0.2217 | 0.6447 | +0.0000 | +0.0000 | -0.4% |
| La Liga | over_1_5 | production_raw | 13 | 0.2217 | 0.6447 | +0.0000 | +0.0000 | -0.4% |
| La Liga | btts_yes | development_1x2 | 13 | 0.3041 | 0.8097 | +0.0014 | +0.0035 | -7.4% |
| La Liga | btts_yes | goal_selected | 13 | 0.3038 | 0.8091 | +0.0017 | +0.0041 | -6.9% |
| La Liga | btts_yes | half_life_1000000000 | 13 | 0.3082 | 0.8196 | -0.0027 | -0.0064 | -8.3% |
| La Liga | btts_yes | half_life_120 | 13 | 0.3070 | 0.8179 | -0.0015 | -0.0047 | -5.4% |
| La Liga | btts_yes | half_life_240 | 13 | 0.3038 | 0.8091 | +0.0017 | +0.0041 | -6.9% |
| La Liga | btts_yes | half_life_365 | 13 | 0.3041 | 0.8097 | +0.0014 | +0.0035 | -7.4% |
| La Liga | btts_yes | half_life_730 | 13 | 0.3056 | 0.8132 | +0.0000 | +0.0000 | -7.9% |
| La Liga | btts_yes | production_raw | 13 | 0.3056 | 0.8132 | +0.0000 | +0.0000 | -7.9% |
| Ligue 1 | over_1_5 | development_1x2 | 8 | 0.1216 | 0.4086 | +0.0108 | +0.0362 | -8.8% |
| Ligue 1 | over_1_5 | goal_selected | 8 | 0.1391 | 0.4681 | -0.0067 | -0.0233 | -9.4% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 8 | 0.1391 | 0.4681 | -0.0067 | -0.0233 | -9.4% |
| Ligue 1 | over_1_5 | half_life_120 | 8 | 0.1100 | 0.3728 | +0.0224 | +0.0720 | -8.9% |
| Ligue 1 | over_1_5 | half_life_240 | 8 | 0.1216 | 0.4086 | +0.0108 | +0.0362 | -8.8% |
| Ligue 1 | over_1_5 | half_life_365 | 8 | 0.1266 | 0.4252 | +0.0058 | +0.0196 | -9.0% |
| Ligue 1 | over_1_5 | half_life_730 | 8 | 0.1324 | 0.4448 | +0.0000 | +0.0000 | -9.2% |
| Ligue 1 | over_1_5 | production_raw | 8 | 0.1324 | 0.4448 | +0.0000 | +0.0000 | -9.2% |
| Ligue 1 | btts_yes | development_1x2 | 8 | 0.2720 | 0.7391 | +0.0064 | +0.0129 | -19.7% |
| Ligue 1 | btts_yes | goal_selected | 8 | 0.2841 | 0.7639 | -0.0057 | -0.0120 | -20.2% |
| Ligue 1 | btts_yes | half_life_1000000000 | 8 | 0.2841 | 0.7639 | -0.0057 | -0.0120 | -20.2% |
| Ligue 1 | btts_yes | half_life_120 | 8 | 0.2709 | 0.7386 | +0.0075 | +0.0133 | -19.9% |
| Ligue 1 | btts_yes | half_life_240 | 8 | 0.2720 | 0.7391 | +0.0064 | +0.0129 | -19.7% |
| Ligue 1 | btts_yes | half_life_365 | 8 | 0.2744 | 0.7438 | +0.0040 | +0.0081 | -19.7% |
| Ligue 1 | btts_yes | half_life_730 | 8 | 0.2784 | 0.7519 | +0.0000 | +0.0000 | -19.9% |
| Ligue 1 | btts_yes | production_raw | 8 | 0.2784 | 0.7519 | +0.0000 | +0.0000 | -19.9% |
| Premier League | over_1_5 | development_1x2 | 15 | 0.1756 | 0.5282 | -0.0029 | -0.0065 | +4.0% |
| Premier League | over_1_5 | goal_selected | 15 | 0.1821 | 0.5458 | -0.0094 | -0.0241 | +4.1% |
| Premier League | over_1_5 | half_life_1000000000 | 15 | 0.1821 | 0.5458 | -0.0094 | -0.0241 | +4.1% |
| Premier League | over_1_5 | half_life_120 | 15 | 0.1689 | 0.5179 | +0.0039 | +0.0038 | +4.1% |
| Premier League | over_1_5 | half_life_240 | 15 | 0.1728 | 0.5217 | +0.0000 | +0.0000 | +4.0% |
| Premier League | over_1_5 | half_life_365 | 15 | 0.1756 | 0.5282 | -0.0029 | -0.0065 | +4.0% |
| Premier League | over_1_5 | half_life_730 | 15 | 0.1789 | 0.5365 | -0.0061 | -0.0148 | +4.0% |
| Premier League | over_1_5 | production_raw | 15 | 0.1728 | 0.5217 | +0.0000 | +0.0000 | +4.0% |
| Premier League | btts_yes | development_1x2 | 15 | 0.2446 | 0.6828 | +0.0001 | +0.0002 | +13.7% |
| Premier League | btts_yes | goal_selected | 15 | 0.2458 | 0.6855 | -0.0012 | -0.0024 | +13.6% |
| Premier League | btts_yes | half_life_1000000000 | 15 | 0.2482 | 0.6907 | -0.0035 | -0.0077 | +13.5% |
| Premier League | btts_yes | half_life_120 | 15 | 0.2517 | 0.6985 | -0.0070 | -0.0155 | +13.7% |
| Premier League | btts_yes | half_life_240 | 15 | 0.2447 | 0.6830 | +0.0000 | +0.0000 | +13.8% |
| Premier League | btts_yes | half_life_365 | 15 | 0.2446 | 0.6828 | +0.0001 | +0.0002 | +13.7% |
| Premier League | btts_yes | half_life_730 | 15 | 0.2458 | 0.6855 | -0.0012 | -0.0024 | +13.6% |
| Premier League | btts_yes | production_raw | 15 | 0.2447 | 0.6830 | +0.0000 | +0.0000 | +13.8% |
| Serie A | over_1_5 | development_1x2 | 13 | 0.1269 | 0.4322 | +0.0049 | +0.0120 | -21.0% |
| Serie A | over_1_5 | goal_selected | 13 | 0.1317 | 0.4442 | +0.0000 | +0.0000 | -20.7% |
| Serie A | over_1_5 | half_life_1000000000 | 13 | 0.1209 | 0.4174 | +0.0108 | +0.0268 | -21.3% |
| Serie A | over_1_5 | half_life_120 | 13 | 0.1447 | 0.4823 | -0.0129 | -0.0381 | -19.8% |
| Serie A | over_1_5 | half_life_240 | 13 | 0.1317 | 0.4442 | +0.0000 | +0.0000 | -20.7% |
| Serie A | over_1_5 | half_life_365 | 13 | 0.1269 | 0.4322 | +0.0049 | +0.0120 | -21.0% |
| Serie A | over_1_5 | half_life_730 | 13 | 0.1231 | 0.4232 | +0.0086 | +0.0209 | -21.3% |
| Serie A | over_1_5 | production_raw | 13 | 0.1317 | 0.4442 | +0.0000 | +0.0000 | -20.7% |
| Serie A | btts_yes | development_1x2 | 13 | 0.2209 | 0.6347 | +0.0019 | +0.0040 | +1.8% |
| Serie A | btts_yes | goal_selected | 13 | 0.2193 | 0.6313 | +0.0034 | +0.0074 | +1.9% |
| Serie A | btts_yes | half_life_1000000000 | 13 | 0.2182 | 0.6286 | +0.0046 | +0.0101 | +2.1% |
| Serie A | btts_yes | half_life_120 | 13 | 0.2255 | 0.6437 | -0.0027 | -0.0051 | +1.8% |
| Serie A | btts_yes | half_life_240 | 13 | 0.2228 | 0.6387 | +0.0000 | +0.0000 | +1.7% |
| Serie A | btts_yes | half_life_365 | 13 | 0.2209 | 0.6347 | +0.0019 | +0.0040 | +1.8% |
| Serie A | btts_yes | half_life_730 | 13 | 0.2193 | 0.6313 | +0.0034 | +0.0074 | +1.9% |
| Serie A | btts_yes | production_raw | 13 | 0.2228 | 0.6387 | +0.0000 | +0.0000 | +1.7% |
| UEFA Champions League | over_1_5 | development_1x2 | 39 | 0.1944 | 0.7159 | +0.0015 | -0.0033 | -0.2% |
| UEFA Champions League | over_1_5 | goal_selected | 24 | 0.2252 | 0.8329 | -0.0066 | +0.0152 | +1.6% |
| UEFA Champions League | over_1_5 | half_life_1000000000 | 39 | 0.1944 | 0.7159 | +0.0015 | -0.0033 | -0.2% |
| UEFA Champions League | over_1_5 | half_life_120 | 39 | 0.2006 | 0.7191 | -0.0047 | -0.0065 | -0.6% |
| UEFA Champions League | over_1_5 | half_life_240 | 39 | 0.1943 | 0.6754 | +0.0016 | +0.0372 | -0.3% |
| UEFA Champions League | over_1_5 | half_life_365 | 39 | 0.1947 | 0.6889 | +0.0012 | +0.0238 | -0.1% |
| UEFA Champions League | over_1_5 | half_life_730 | 39 | 0.1951 | 0.7058 | +0.0008 | +0.0068 | -0.1% |
| UEFA Champions League | over_1_5 | production_raw | 39 | 0.1959 | 0.7126 | +0.0000 | +0.0000 | -0.3% |
| UEFA Champions League | btts_yes | development_1x2 | 39 | 0.2772 | 0.7695 | +0.0029 | +0.0071 | -8.2% |
| UEFA Champions League | btts_yes | goal_selected | 24 | 0.2773 | 0.7811 | -0.0023 | -0.0096 | -13.4% |
| UEFA Champions League | btts_yes | half_life_1000000000 | 39 | 0.2772 | 0.7695 | +0.0029 | +0.0071 | -8.2% |
| UEFA Champions League | btts_yes | half_life_120 | 39 | 0.3202 | 0.8991 | -0.0401 | -0.1225 | -8.2% |
| UEFA Champions League | btts_yes | half_life_240 | 39 | 0.2955 | 0.8234 | -0.0154 | -0.0468 | -7.8% |
| UEFA Champions League | btts_yes | half_life_365 | 39 | 0.2880 | 0.8018 | -0.0080 | -0.0251 | -7.7% |
| UEFA Champions League | btts_yes | half_life_730 | 39 | 0.2818 | 0.7834 | -0.0017 | -0.0067 | -7.9% |
| UEFA Champions League | btts_yes | production_raw | 39 | 0.2801 | 0.7767 | +0.0000 | +0.0000 | -8.2% |
| UEFA Europa League | over_1_5 | development_1x2 | 7 | 0.0991 | 0.3346 | -0.0057 | -0.0071 | -26.2% |
| UEFA Europa League | over_1_5 | goal_selected | 7 | 0.0991 | 0.3346 | -0.0057 | -0.0071 | -26.2% |
| UEFA Europa League | over_1_5 | half_life_1000000000 | 7 | 0.0991 | 0.3346 | -0.0057 | -0.0071 | -26.2% |
| UEFA Europa League | over_1_5 | half_life_120 | 7 | 0.1113 | 0.3837 | -0.0179 | -0.0562 | -30.3% |
| UEFA Europa League | over_1_5 | half_life_240 | 7 | 0.1013 | 0.3561 | -0.0079 | -0.0286 | -28.4% |
| UEFA Europa League | over_1_5 | half_life_365 | 7 | 0.0938 | 0.3347 | -0.0004 | -0.0071 | -26.9% |
| UEFA Europa League | over_1_5 | half_life_730 | 7 | 0.0934 | 0.3276 | +0.0000 | +0.0000 | -26.1% |
| UEFA Europa League | over_1_5 | production_raw | 7 | 0.0934 | 0.3276 | +0.0000 | +0.0000 | -26.1% |
| UEFA Europa League | btts_yes | development_1x2 | 7 | 0.3388 | 1.0183 | -0.0078 | -0.0191 | -15.4% |
| UEFA Europa League | btts_yes | goal_selected | 7 | 0.3388 | 1.0183 | -0.0078 | -0.0191 | -15.4% |
| UEFA Europa League | btts_yes | half_life_1000000000 | 7 | 0.3388 | 1.0183 | -0.0078 | -0.0191 | -15.4% |
| UEFA Europa League | btts_yes | half_life_120 | 7 | 0.3336 | 1.0114 | -0.0026 | -0.0123 | -20.4% |
| UEFA Europa League | btts_yes | half_life_240 | 7 | 0.3263 | 0.9927 | +0.0047 | +0.0065 | -16.4% |
| UEFA Europa League | btts_yes | half_life_365 | 7 | 0.3268 | 0.9909 | +0.0042 | +0.0083 | -15.2% |
| UEFA Europa League | btts_yes | half_life_730 | 7 | 0.3310 | 0.9992 | +0.0000 | +0.0000 | -15.1% |
| UEFA Europa League | btts_yes | production_raw | 7 | 0.3310 | 0.9992 | +0.0000 | +0.0000 | -15.1% |

Positive paired gain means lower error than the raw production model on those same matches. A 30-match review prompt is not statistical proof.

Calibration buckets, approximate paired-gain intervals, gameweek comparisons and historical selection stability for each frozen run are retained in summary.json. Historical audits overlap and are not additional forward samples.

## Latest historical development/audit diagnostics

| League | Market | Goal half-life | Development N | Audit N | Audit log-loss gain | Development fold wins |
|---|---|---:|---:|---:|---:|---|
| Premier League | over_1_5 | 730.0 | 301 | 70 | -0.0030 | {'1000000000.0': 3, '240.0': 1} |
| Premier League | btts_yes | 1000000000.0 | 301 | 70 | -0.0099 | {'1000000000.0': 1, '365.0': 1, '730.0': 1, '120.0': 1} |
| La Liga | over_1_5 | 120.0 | 290 | 89 | -0.0119 | {'120.0': 2, '1000000000.0': 2} |
| La Liga | btts_yes | 240.0 | 290 | 89 | -0.0001 | {'240.0': 1, '1000000000.0': 1, '120.0': 2} |
| Bundesliga | over_1_5 | 1000000000.0 | 245 | 54 | +0.0059 | {'1000000000.0': 3, '240.0': 1} |
| Bundesliga | btts_yes | 240.0 | 245 | 54 | -0.0007 | {'730.0': 1, '240.0': 1, '1000000000.0': 1, '120.0': 1} |
| Serie A | over_1_5 | 240.0 | 311 | 70 | -0.0071 | {'730.0': 1, '120.0': 2, '1000000000.0': 1} |
| Serie A | btts_yes | 730.0 | 311 | 70 | +0.0000 | {'730.0': 1, '120.0': 2, '1000000000.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 239 | 63 | +0.0000 | {'1000000000.0': 2, '120.0': 1, '365.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 239 | 63 | +0.0000 | {'1000000000.0': 3, '120.0': 1} |