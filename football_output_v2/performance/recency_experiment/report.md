# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 510/552 fixture-markets; 294 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 147 | 0.1664 | 0.5454 | +0.0014 | +0.0021 | -2.8% |
| ALL | over_1_5 | goal_selected | 132 | 0.1685 | 0.5463 | +0.0002 | +0.0071 | -2.4% |
| ALL | over_1_5 | half_life_1000000000 | 147 | 0.1675 | 0.5488 | +0.0003 | -0.0013 | -3.0% |
| ALL | over_1_5 | half_life_120 | 147 | 0.1696 | 0.5503 | -0.0018 | -0.0028 | -2.2% |
| ALL | over_1_5 | half_life_240 | 147 | 0.1668 | 0.5357 | +0.0010 | +0.0118 | -2.6% |
| ALL | over_1_5 | half_life_365 | 147 | 0.1665 | 0.5387 | +0.0013 | +0.0089 | -2.7% |
| ALL | over_1_5 | half_life_730 | 147 | 0.1668 | 0.5439 | +0.0010 | +0.0036 | -2.8% |
| ALL | over_1_5 | production_raw | 147 | 0.1678 | 0.5475 | +0.0000 | +0.0000 | -2.8% |
| ALL | btts_yes | development_1x2 | 147 | 0.2546 | 0.7155 | +0.0012 | +0.0028 | -2.9% |
| ALL | btts_yes | goal_selected | 132 | 0.2511 | 0.7095 | +0.0011 | +0.0013 | -3.0% |
| ALL | btts_yes | half_life_1000000000 | 147 | 0.2550 | 0.7166 | +0.0008 | +0.0018 | -3.0% |
| ALL | btts_yes | half_life_120 | 147 | 0.2678 | 0.7540 | -0.0120 | -0.0356 | -2.6% |
| ALL | btts_yes | half_life_240 | 147 | 0.2591 | 0.7292 | -0.0033 | -0.0108 | -2.7% |
| ALL | btts_yes | half_life_365 | 147 | 0.2569 | 0.7227 | -0.0011 | -0.0044 | -2.7% |
| ALL | btts_yes | half_life_730 | 147 | 0.2554 | 0.7184 | +0.0004 | -0.0001 | -2.8% |
| ALL | btts_yes | production_raw | 147 | 0.2558 | 0.7183 | +0.0000 | +0.0000 | -2.8% |
| Bundesliga | over_1_5 | development_1x2 | 16 | 0.1063 | 0.3479 | +0.0025 | +0.0063 | -1.0% |
| Bundesliga | over_1_5 | goal_selected | 16 | 0.1100 | 0.3565 | -0.0012 | -0.0023 | -0.7% |
| Bundesliga | over_1_5 | half_life_1000000000 | 16 | 0.1066 | 0.3489 | +0.0022 | +0.0053 | -1.1% |
| Bundesliga | over_1_5 | half_life_120 | 16 | 0.1068 | 0.3387 | +0.0020 | +0.0155 | +1.5% |
| Bundesliga | over_1_5 | half_life_240 | 16 | 0.1095 | 0.3519 | -0.0007 | +0.0023 | +0.0% |
| Bundesliga | over_1_5 | half_life_365 | 16 | 0.1095 | 0.3540 | -0.0007 | +0.0002 | -0.5% |
| Bundesliga | over_1_5 | half_life_730 | 16 | 0.1086 | 0.3531 | +0.0002 | +0.0011 | -0.9% |
| Bundesliga | over_1_5 | production_raw | 16 | 0.1088 | 0.3542 | +0.0000 | +0.0000 | -1.0% |
| Bundesliga | btts_yes | development_1x2 | 16 | 0.2054 | 0.6017 | +0.0013 | +0.0035 | -10.5% |
| Bundesliga | btts_yes | goal_selected | 16 | 0.2014 | 0.5940 | +0.0053 | +0.0112 | -9.2% |
| Bundesliga | btts_yes | half_life_1000000000 | 16 | 0.2062 | 0.6034 | +0.0005 | +0.0017 | -10.6% |
| Bundesliga | btts_yes | half_life_120 | 16 | 0.1928 | 0.5759 | +0.0139 | +0.0293 | -7.8% |
| Bundesliga | btts_yes | half_life_240 | 16 | 0.2014 | 0.5940 | +0.0053 | +0.0112 | -9.2% |
| Bundesliga | btts_yes | half_life_365 | 16 | 0.2041 | 0.5996 | +0.0027 | +0.0056 | -9.7% |
| Bundesliga | btts_yes | half_life_730 | 16 | 0.2058 | 0.6030 | +0.0009 | +0.0021 | -10.2% |
| Bundesliga | btts_yes | production_raw | 16 | 0.2067 | 0.6052 | +0.0000 | +0.0000 | -10.3% |
| Eredivisie | over_1_5 | development_1x2 | 2 | 0.0175 | 0.1347 | +0.0000 | +0.0000 | -12.5% |
| Eredivisie | over_1_5 | goal_selected | 2 | 0.0211 | 0.1505 | -0.0037 | -0.0158 | -13.9% |
| Eredivisie | over_1_5 | half_life_1000000000 | 2 | 0.0246 | 0.1650 | -0.0071 | -0.0303 | -15.1% |
| Eredivisie | over_1_5 | half_life_120 | 2 | 0.0062 | 0.0811 | +0.0112 | +0.0535 | -7.8% |
| Eredivisie | over_1_5 | half_life_240 | 2 | 0.0136 | 0.1182 | +0.0038 | +0.0165 | -11.1% |
| Eredivisie | over_1_5 | half_life_365 | 2 | 0.0175 | 0.1347 | +0.0000 | +0.0000 | -12.5% |
| Eredivisie | over_1_5 | half_life_730 | 2 | 0.0211 | 0.1505 | -0.0037 | -0.0158 | -13.9% |
| Eredivisie | over_1_5 | production_raw | 2 | 0.0175 | 0.1347 | +0.0000 | +0.0000 | -12.5% |
| Eredivisie | btts_yes | development_1x2 | 2 | 0.1136 | 0.4050 | +0.0000 | +0.0000 | -32.9% |
| Eredivisie | btts_yes | goal_selected | 2 | 0.1054 | 0.3853 | +0.0082 | +0.0196 | -31.5% |
| Eredivisie | btts_yes | half_life_1000000000 | 2 | 0.1340 | 0.4518 | -0.0204 | -0.0469 | -36.0% |
| Eredivisie | btts_yes | half_life_120 | 2 | 0.0870 | 0.3422 | +0.0267 | +0.0627 | -28.6% |
| Eredivisie | btts_yes | half_life_240 | 2 | 0.1054 | 0.3853 | +0.0082 | +0.0196 | -31.5% |
| Eredivisie | btts_yes | half_life_365 | 2 | 0.1136 | 0.4050 | +0.0000 | +0.0000 | -32.9% |
| Eredivisie | btts_yes | half_life_730 | 2 | 0.1226 | 0.4264 | -0.0090 | -0.0214 | -34.4% |
| Eredivisie | btts_yes | production_raw | 2 | 0.1136 | 0.4050 | +0.0000 | +0.0000 | -32.9% |
| La Liga | over_1_5 | development_1x2 | 18 | 0.2400 | 0.6903 | +0.0024 | +0.0054 | +6.4% |
| La Liga | over_1_5 | goal_selected | 18 | 0.2231 | 0.6417 | +0.0192 | +0.0539 | +7.9% |
| La Liga | over_1_5 | half_life_1000000000 | 18 | 0.2465 | 0.7072 | -0.0041 | -0.0116 | +5.3% |
| La Liga | over_1_5 | half_life_120 | 18 | 0.2231 | 0.6417 | +0.0192 | +0.0539 | +7.9% |
| La Liga | over_1_5 | half_life_240 | 18 | 0.2327 | 0.6682 | +0.0097 | +0.0274 | +6.7% |
| La Liga | over_1_5 | half_life_365 | 18 | 0.2373 | 0.6812 | +0.0050 | +0.0144 | +6.2% |
| La Liga | over_1_5 | half_life_730 | 18 | 0.2423 | 0.6954 | +0.0001 | +0.0003 | +5.7% |
| La Liga | over_1_5 | production_raw | 18 | 0.2424 | 0.6956 | +0.0000 | +0.0000 | +5.7% |
| La Liga | btts_yes | development_1x2 | 18 | 0.2847 | 0.7680 | +0.0013 | +0.0032 | -0.2% |
| La Liga | btts_yes | goal_selected | 18 | 0.2802 | 0.7587 | +0.0059 | +0.0125 | +0.1% |
| La Liga | btts_yes | half_life_1000000000 | 18 | 0.2899 | 0.7797 | -0.0038 | -0.0085 | -1.1% |
| La Liga | btts_yes | half_life_120 | 18 | 0.2780 | 0.7554 | +0.0081 | +0.0158 | +1.2% |
| La Liga | btts_yes | half_life_240 | 18 | 0.2802 | 0.7587 | +0.0059 | +0.0125 | +0.1% |
| La Liga | btts_yes | half_life_365 | 18 | 0.2827 | 0.7639 | +0.0034 | +0.0073 | -0.3% |
| La Liga | btts_yes | half_life_730 | 18 | 0.2862 | 0.7715 | -0.0002 | -0.0003 | -0.7% |
| La Liga | btts_yes | production_raw | 18 | 0.2861 | 0.7712 | +0.0000 | +0.0000 | -0.7% |
| Ligue 1 | over_1_5 | development_1x2 | 16 | 0.2112 | 0.6093 | +0.0013 | +0.0057 | +9.1% |
| Ligue 1 | over_1_5 | goal_selected | 16 | 0.2145 | 0.6226 | -0.0020 | -0.0076 | +9.0% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 16 | 0.2145 | 0.6226 | -0.0020 | -0.0076 | +9.0% |
| Ligue 1 | over_1_5 | half_life_120 | 16 | 0.2259 | 0.6559 | -0.0134 | -0.0409 | +8.9% |
| Ligue 1 | over_1_5 | half_life_240 | 16 | 0.2190 | 0.6332 | -0.0066 | -0.0182 | +9.2% |
| Ligue 1 | over_1_5 | half_life_365 | 16 | 0.2162 | 0.6256 | -0.0038 | -0.0106 | +9.2% |
| Ligue 1 | over_1_5 | half_life_730 | 16 | 0.2140 | 0.6201 | -0.0016 | -0.0051 | +9.1% |
| Ligue 1 | over_1_5 | production_raw | 16 | 0.2125 | 0.6150 | +0.0000 | +0.0000 | +9.1% |
| Ligue 1 | btts_yes | development_1x2 | 16 | 0.2467 | 0.6868 | -0.0005 | -0.0010 | -9.1% |
| Ligue 1 | btts_yes | goal_selected | 16 | 0.2478 | 0.6893 | -0.0017 | -0.0035 | -9.1% |
| Ligue 1 | btts_yes | half_life_1000000000 | 16 | 0.2478 | 0.6893 | -0.0017 | -0.0035 | -9.1% |
| Ligue 1 | btts_yes | half_life_120 | 16 | 0.2553 | 0.7046 | -0.0092 | -0.0188 | -10.2% |
| Ligue 1 | btts_yes | half_life_240 | 16 | 0.2474 | 0.6883 | -0.0013 | -0.0025 | -9.7% |
| Ligue 1 | btts_yes | half_life_365 | 16 | 0.2460 | 0.6855 | +0.0001 | +0.0003 | -9.4% |
| Ligue 1 | btts_yes | half_life_730 | 16 | 0.2461 | 0.6857 | +0.0001 | +0.0001 | -9.2% |
| Ligue 1 | btts_yes | production_raw | 16 | 0.2461 | 0.6858 | +0.0000 | +0.0000 | -9.0% |
| Premier League | over_1_5 | development_1x2 | 20 | 0.1634 | 0.4987 | -0.0018 | -0.0043 | +2.4% |
| Premier League | over_1_5 | goal_selected | 20 | 0.1674 | 0.5100 | -0.0057 | -0.0155 | +2.3% |
| Premier League | over_1_5 | half_life_1000000000 | 20 | 0.1674 | 0.5100 | -0.0057 | -0.0155 | +2.3% |
| Premier League | over_1_5 | half_life_120 | 20 | 0.1590 | 0.4915 | +0.0026 | +0.0030 | +2.5% |
| Premier League | over_1_5 | half_life_240 | 20 | 0.1616 | 0.4945 | +0.0000 | +0.0000 | +2.4% |
| Premier League | over_1_5 | half_life_365 | 20 | 0.1634 | 0.4987 | -0.0018 | -0.0043 | +2.4% |
| Premier League | over_1_5 | half_life_730 | 20 | 0.1654 | 0.5041 | -0.0038 | -0.0096 | +2.3% |
| Premier League | over_1_5 | production_raw | 20 | 0.1616 | 0.4945 | +0.0000 | +0.0000 | +2.4% |
| Premier League | btts_yes | development_1x2 | 20 | 0.2646 | 0.7236 | +0.0014 | +0.0030 | +19.5% |
| Premier League | btts_yes | goal_selected | 20 | 0.2640 | 0.7225 | +0.0020 | +0.0041 | +19.3% |
| Premier League | btts_yes | half_life_1000000000 | 20 | 0.2643 | 0.7232 | +0.0017 | +0.0034 | +19.0% |
| Premier League | btts_yes | half_life_120 | 20 | 0.2736 | 0.7438 | -0.0076 | -0.0172 | +19.6% |
| Premier League | btts_yes | half_life_240 | 20 | 0.2660 | 0.7266 | +0.0000 | +0.0000 | +19.6% |
| Premier League | btts_yes | half_life_365 | 20 | 0.2646 | 0.7236 | +0.0014 | +0.0030 | +19.5% |
| Premier League | btts_yes | half_life_730 | 20 | 0.2640 | 0.7225 | +0.0020 | +0.0041 | +19.3% |
| Premier League | btts_yes | production_raw | 20 | 0.2660 | 0.7266 | +0.0000 | +0.0000 | +19.6% |
| Primeira Liga | over_1_5 | development_1x2 | 2 | 0.0753 | 0.3139 | -0.0027 | -0.0084 | -26.6% |
| Primeira Liga | over_1_5 | goal_selected | 2 | 0.0702 | 0.2972 | +0.0025 | +0.0083 | -25.3% |
| Primeira Liga | over_1_5 | half_life_1000000000 | 2 | 0.0753 | 0.3139 | -0.0027 | -0.0084 | -26.6% |
| Primeira Liga | over_1_5 | half_life_120 | 2 | 0.0509 | 0.2462 | +0.0218 | +0.0593 | -21.5% |
| Primeira Liga | over_1_5 | half_life_240 | 2 | 0.0608 | 0.2707 | +0.0119 | +0.0348 | -23.3% |
| Primeira Liga | over_1_5 | half_life_365 | 2 | 0.0652 | 0.2827 | +0.0074 | +0.0229 | -24.2% |
| Primeira Liga | over_1_5 | half_life_730 | 2 | 0.0702 | 0.2972 | +0.0025 | +0.0083 | -25.3% |
| Primeira Liga | over_1_5 | production_raw | 2 | 0.0726 | 0.3055 | +0.0000 | +0.0000 | -26.0% |
| Primeira Liga | btts_yes | development_1x2 | 2 | 0.2119 | 0.6168 | +0.0026 | +0.0052 | +46.0% |
| Primeira Liga | btts_yes | goal_selected | 2 | 0.2121 | 0.6171 | +0.0024 | +0.0048 | +46.1% |
| Primeira Liga | btts_yes | half_life_1000000000 | 2 | 0.2119 | 0.6168 | +0.0026 | +0.0052 | +46.0% |
| Primeira Liga | btts_yes | half_life_120 | 2 | 0.2145 | 0.6218 | +0.0000 | +0.0001 | +46.3% |
| Primeira Liga | btts_yes | half_life_240 | 2 | 0.2092 | 0.6114 | +0.0053 | +0.0106 | +45.7% |
| Primeira Liga | btts_yes | half_life_365 | 2 | 0.2105 | 0.6141 | +0.0039 | +0.0079 | +45.9% |
| Primeira Liga | btts_yes | half_life_730 | 2 | 0.2121 | 0.6171 | +0.0024 | +0.0048 | +46.1% |
| Primeira Liga | btts_yes | production_raw | 2 | 0.2145 | 0.6220 | +0.0000 | +0.0000 | +46.3% |
| Serie A | over_1_5 | development_1x2 | 27 | 0.1236 | 0.4186 | +0.0045 | +0.0111 | -15.9% |
| Serie A | over_1_5 | goal_selected | 27 | 0.1263 | 0.4246 | +0.0018 | +0.0051 | -15.5% |
| Serie A | over_1_5 | half_life_1000000000 | 27 | 0.1193 | 0.4069 | +0.0088 | +0.0228 | -15.9% |
| Serie A | over_1_5 | half_life_120 | 27 | 0.1367 | 0.4525 | -0.0086 | -0.0229 | -14.7% |
| Serie A | over_1_5 | half_life_240 | 27 | 0.1263 | 0.4246 | +0.0018 | +0.0051 | -15.5% |
| Serie A | over_1_5 | half_life_365 | 27 | 0.1226 | 0.4159 | +0.0055 | +0.0137 | -15.8% |
| Serie A | over_1_5 | half_life_730 | 27 | 0.1202 | 0.4100 | +0.0079 | +0.0197 | -16.0% |
| Serie A | over_1_5 | production_raw | 27 | 0.1281 | 0.4297 | +0.0000 | +0.0000 | -15.7% |
| Serie A | btts_yes | development_1x2 | 27 | 0.2200 | 0.6327 | +0.0019 | +0.0039 | -3.4% |
| Serie A | btts_yes | goal_selected | 27 | 0.2210 | 0.6347 | +0.0009 | +0.0020 | -3.5% |
| Serie A | btts_yes | half_life_1000000000 | 27 | 0.2164 | 0.6250 | +0.0055 | +0.0117 | -3.2% |
| Serie A | btts_yes | half_life_120 | 27 | 0.2329 | 0.6592 | -0.0110 | -0.0225 | -3.1% |
| Serie A | btts_yes | half_life_240 | 27 | 0.2262 | 0.6454 | -0.0043 | -0.0087 | -3.5% |
| Serie A | btts_yes | half_life_365 | 27 | 0.2224 | 0.6377 | -0.0005 | -0.0010 | -3.5% |
| Serie A | btts_yes | half_life_730 | 27 | 0.2189 | 0.6303 | +0.0030 | +0.0064 | -3.4% |
| Serie A | btts_yes | production_raw | 27 | 0.2219 | 0.6367 | +0.0000 | +0.0000 | -3.4% |
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
| Premier League | over_1_5 | 1000000000.0 | 295 | 80 | -0.0106 | {'730.0': 1, '240.0': 1, '1000000000.0': 2} |
| Premier League | btts_yes | 1000000000.0 | 295 | 80 | -0.0071 | {'1000000000.0': 2, '240.0': 2} |
| La Liga | over_1_5 | 120.0 | 280 | 100 | -0.0068 | {'240.0': 1, '120.0': 2, '1000000000.0': 1} |
| La Liga | btts_yes | 240.0 | 280 | 100 | +0.0018 | {'1000000000.0': 1, '240.0': 1, '120.0': 2} |
| Bundesliga | over_1_5 | 1000000000.0 | 234 | 64 | +0.0013 | {'1000000000.0': 4} |
| Bundesliga | btts_yes | 240.0 | 234 | 64 | +0.0004 | {'1000000000.0': 2, '120.0': 2} |
| Serie A | over_1_5 | 240.0 | 292 | 90 | -0.0078 | {'240.0': 2, '1000000000.0': 1, '120.0': 1} |
| Serie A | btts_yes | 240.0 | 292 | 90 | -0.0125 | {'365.0': 1, '120.0': 1, '1000000000.0': 1, '240.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 216 | 75 | +0.0000 | {'1000000000.0': 2, '240.0': 1, '365.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 216 | 75 | +0.0000 | {'1000000000.0': 3, '240.0': 1} |
| UEFA Champions League | over_1_5 | 365.0 | 144 | 54 | +0.0036 | {'730.0': 1, '120.0': 2, '240.0': 1} |
| UEFA Champions League | btts_yes | 1000000000.0 | 144 | 54 | +0.0032 | {'240.0': 1, '1000000000.0': 3} |
| Eredivisie | over_1_5 | 730.0 | 220 | 90 | -0.0009 | {'1000000000.0': 2, '240.0': 2} |
| Eredivisie | btts_yes | 240.0 | 220 | 90 | +0.0039 | {'730.0': 1, '120.0': 3} |
| Primeira Liga | over_1_5 | 730.0 | 226 | 81 | -0.0020 | {'120.0': 1, '240.0': 1, '1000000000.0': 2} |
| Primeira Liga | btts_yes | 730.0 | 226 | 81 | -0.0040 | {'1000000000.0': 2, '730.0': 2} |
| Super Lig | over_1_5 | 365.0 | 218 | 81 | +0.0001 | {'240.0': 2, '120.0': 1, '1000000000.0': 1} |
| Super Lig | btts_yes | 1000000000.0 | 218 | 81 | +0.0051 | {'120.0': 1, '1000000000.0': 2, '240.0': 1} |