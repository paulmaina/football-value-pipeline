# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 510/552 fixture-markets; 336 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 168 | 0.1610 | 0.5279 | +0.0009 | +0.0010 | -3.0% |
| ALL | over_1_5 | goal_selected | 153 | 0.1619 | 0.5255 | +0.0003 | +0.0066 | -2.6% |
| ALL | over_1_5 | half_life_1000000000 | 168 | 0.1619 | 0.5307 | +0.0001 | -0.0018 | -3.2% |
| ALL | over_1_5 | half_life_120 | 168 | 0.1634 | 0.5302 | -0.0015 | -0.0013 | -2.4% |
| ALL | over_1_5 | half_life_240 | 168 | 0.1614 | 0.5192 | +0.0006 | +0.0097 | -2.8% |
| ALL | over_1_5 | half_life_365 | 168 | 0.1612 | 0.5221 | +0.0008 | +0.0068 | -2.9% |
| ALL | over_1_5 | half_life_730 | 168 | 0.1614 | 0.5268 | +0.0006 | +0.0021 | -3.0% |
| ALL | over_1_5 | production_raw | 168 | 0.1620 | 0.5289 | +0.0000 | +0.0000 | -2.9% |
| ALL | btts_yes | development_1x2 | 168 | 0.2577 | 0.7204 | +0.0014 | +0.0031 | -0.9% |
| ALL | btts_yes | goal_selected | 153 | 0.2541 | 0.7138 | +0.0021 | +0.0037 | -1.0% |
| ALL | btts_yes | half_life_1000000000 | 168 | 0.2585 | 0.7221 | +0.0006 | +0.0014 | -1.3% |
| ALL | btts_yes | half_life_120 | 168 | 0.2674 | 0.7503 | -0.0082 | -0.0268 | -0.6% |
| ALL | btts_yes | half_life_240 | 168 | 0.2605 | 0.7299 | -0.0014 | -0.0064 | -0.7% |
| ALL | btts_yes | half_life_365 | 168 | 0.2592 | 0.7256 | -0.0001 | -0.0021 | -0.8% |
| ALL | btts_yes | half_life_730 | 168 | 0.2587 | 0.7232 | +0.0005 | +0.0003 | -1.0% |
| ALL | btts_yes | production_raw | 168 | 0.2591 | 0.7235 | +0.0000 | +0.0000 | -0.9% |
| Bundesliga | over_1_5 | development_1x2 | 22 | 0.1058 | 0.3470 | +0.0016 | +0.0031 | -1.2% |
| Bundesliga | over_1_5 | goal_selected | 22 | 0.1082 | 0.3518 | -0.0009 | -0.0017 | -0.7% |
| Bundesliga | over_1_5 | half_life_1000000000 | 22 | 0.1057 | 0.3463 | +0.0016 | +0.0038 | -1.0% |
| Bundesliga | over_1_5 | half_life_120 | 22 | 0.1103 | 0.3489 | -0.0029 | +0.0013 | -0.4% |
| Bundesliga | over_1_5 | half_life_240 | 22 | 0.1111 | 0.3571 | -0.0037 | -0.0070 | -1.3% |
| Bundesliga | over_1_5 | half_life_365 | 22 | 0.1094 | 0.3550 | -0.0020 | -0.0048 | -1.3% |
| Bundesliga | over_1_5 | half_life_730 | 22 | 0.1074 | 0.3508 | -0.0001 | -0.0007 | -1.1% |
| Bundesliga | over_1_5 | production_raw | 22 | 0.1073 | 0.3502 | +0.0000 | +0.0000 | -0.9% |
| Bundesliga | btts_yes | development_1x2 | 22 | 0.2085 | 0.6082 | +0.0032 | +0.0071 | -5.0% |
| Bundesliga | btts_yes | goal_selected | 22 | 0.2000 | 0.5915 | +0.0117 | +0.0238 | -4.6% |
| Bundesliga | btts_yes | half_life_1000000000 | 22 | 0.2113 | 0.6140 | +0.0004 | +0.0013 | -4.9% |
| Bundesliga | btts_yes | half_life_120 | 22 | 0.1950 | 0.5811 | +0.0167 | +0.0342 | -3.7% |
| Bundesliga | btts_yes | half_life_240 | 22 | 0.2000 | 0.5915 | +0.0117 | +0.0238 | -4.6% |
| Bundesliga | btts_yes | half_life_365 | 22 | 0.2041 | 0.5999 | +0.0076 | +0.0154 | -4.7% |
| Bundesliga | btts_yes | half_life_730 | 22 | 0.2087 | 0.6092 | +0.0030 | +0.0061 | -4.8% |
| Bundesliga | btts_yes | production_raw | 22 | 0.2117 | 0.6153 | +0.0000 | +0.0000 | -4.8% |
| Eredivisie | over_1_5 | development_1x2 | 6 | 0.1284 | 0.3898 | -0.0009 | -0.0019 | +7.0% |
| Eredivisie | over_1_5 | goal_selected | 6 | 0.1267 | 0.3883 | +0.0007 | -0.0004 | +5.8% |
| Eredivisie | over_1_5 | half_life_1000000000 | 6 | 0.1209 | 0.3740 | +0.0065 | +0.0139 | +4.3% |
| Eredivisie | over_1_5 | half_life_120 | 6 | 0.1217 | 0.3565 | +0.0057 | +0.0314 | +9.0% |
| Eredivisie | over_1_5 | half_life_240 | 6 | 0.1274 | 0.3833 | -0.0000 | +0.0046 | +7.8% |
| Eredivisie | over_1_5 | half_life_365 | 6 | 0.1284 | 0.3898 | -0.0009 | -0.0019 | +7.0% |
| Eredivisie | over_1_5 | half_life_730 | 6 | 0.1267 | 0.3883 | +0.0007 | -0.0004 | +5.8% |
| Eredivisie | over_1_5 | production_raw | 6 | 0.1274 | 0.3879 | +0.0000 | +0.0000 | +6.7% |
| Eredivisie | btts_yes | development_1x2 | 6 | 0.2263 | 0.6429 | -0.0013 | -0.0027 | +9.0% |
| Eredivisie | btts_yes | goal_selected | 6 | 0.2244 | 0.6381 | +0.0006 | +0.0021 | +10.1% |
| Eredivisie | btts_yes | half_life_1000000000 | 6 | 0.2244 | 0.6395 | +0.0006 | +0.0006 | +5.5% |
| Eredivisie | btts_yes | half_life_120 | 6 | 0.2132 | 0.6126 | +0.0118 | +0.0275 | +11.4% |
| Eredivisie | btts_yes | half_life_240 | 6 | 0.2244 | 0.6381 | +0.0006 | +0.0021 | +10.1% |
| Eredivisie | btts_yes | half_life_365 | 6 | 0.2263 | 0.6429 | -0.0013 | -0.0027 | +9.0% |
| Eredivisie | btts_yes | half_life_730 | 6 | 0.2260 | 0.6429 | -0.0010 | -0.0027 | +7.4% |
| Eredivisie | btts_yes | production_raw | 6 | 0.2250 | 0.6401 | +0.0000 | +0.0000 | +8.5% |
| La Liga | over_1_5 | development_1x2 | 20 | 0.2196 | 0.6423 | +0.0018 | +0.0035 | +3.8% |
| La Liga | over_1_5 | goal_selected | 20 | 0.2030 | 0.5935 | +0.0184 | +0.0523 | +5.7% |
| La Liga | over_1_5 | half_life_1000000000 | 20 | 0.2255 | 0.6573 | -0.0041 | -0.0115 | +2.9% |
| La Liga | over_1_5 | half_life_120 | 20 | 0.2030 | 0.5935 | +0.0184 | +0.0523 | +5.7% |
| La Liga | over_1_5 | half_life_240 | 20 | 0.2124 | 0.6205 | +0.0089 | +0.0253 | +4.3% |
| La Liga | over_1_5 | half_life_365 | 20 | 0.2170 | 0.6334 | +0.0044 | +0.0124 | +3.8% |
| La Liga | over_1_5 | half_life_730 | 20 | 0.2217 | 0.6469 | -0.0003 | -0.0011 | +3.3% |
| La Liga | over_1_5 | production_raw | 20 | 0.2214 | 0.6458 | +0.0000 | +0.0000 | +3.4% |
| La Liga | btts_yes | development_1x2 | 20 | 0.2930 | 0.7843 | +0.0023 | +0.0051 | -0.2% |
| La Liga | btts_yes | goal_selected | 20 | 0.2874 | 0.7728 | +0.0079 | +0.0166 | +0.1% |
| La Liga | btts_yes | half_life_1000000000 | 20 | 0.2998 | 0.7994 | -0.0045 | -0.0100 | -1.0% |
| La Liga | btts_yes | half_life_120 | 20 | 0.2855 | 0.7701 | +0.0097 | +0.0193 | +1.4% |
| La Liga | btts_yes | half_life_240 | 20 | 0.2874 | 0.7728 | +0.0079 | +0.0166 | +0.1% |
| La Liga | btts_yes | half_life_365 | 20 | 0.2900 | 0.7782 | +0.0053 | +0.0112 | -0.3% |
| La Liga | btts_yes | half_life_730 | 20 | 0.2943 | 0.7875 | +0.0009 | +0.0020 | -0.7% |
| La Liga | btts_yes | production_raw | 20 | 0.2953 | 0.7895 | +0.0000 | +0.0000 | -0.6% |
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
| Premier League | over_1_5 | development_1x2 | 27 | 0.1586 | 0.4927 | -0.0013 | -0.0032 | -0.3% |
| Premier League | over_1_5 | goal_selected | 27 | 0.1629 | 0.5053 | -0.0056 | -0.0158 | -0.5% |
| Premier League | over_1_5 | half_life_1000000000 | 27 | 0.1636 | 0.5072 | -0.0064 | -0.0177 | -0.6% |
| Premier League | over_1_5 | half_life_120 | 27 | 0.1546 | 0.4844 | +0.0026 | +0.0051 | -0.1% |
| Premier League | over_1_5 | half_life_240 | 27 | 0.1572 | 0.4895 | +0.0000 | +0.0000 | -0.3% |
| Premier League | over_1_5 | half_life_365 | 27 | 0.1592 | 0.4947 | -0.0020 | -0.0052 | -0.4% |
| Premier League | over_1_5 | half_life_730 | 27 | 0.1614 | 0.5009 | -0.0042 | -0.0114 | -0.5% |
| Premier League | over_1_5 | production_raw | 27 | 0.1572 | 0.4895 | +0.0000 | +0.0000 | -0.3% |
| Premier League | btts_yes | development_1x2 | 27 | 0.2779 | 0.7505 | +0.0010 | +0.0022 | +21.5% |
| Premier League | btts_yes | goal_selected | 27 | 0.2787 | 0.7518 | +0.0002 | +0.0009 | +20.7% |
| Premier League | btts_yes | half_life_1000000000 | 27 | 0.2789 | 0.7524 | -0.0000 | +0.0004 | +20.5% |
| Premier League | btts_yes | half_life_120 | 27 | 0.2821 | 0.7614 | -0.0032 | -0.0086 | +21.9% |
| Premier League | btts_yes | half_life_240 | 27 | 0.2789 | 0.7527 | +0.0000 | +0.0000 | +21.6% |
| Premier League | btts_yes | half_life_365 | 27 | 0.2790 | 0.7526 | -0.0001 | +0.0001 | +21.4% |
| Premier League | btts_yes | half_life_730 | 27 | 0.2793 | 0.7530 | -0.0004 | -0.0003 | +21.0% |
| Premier League | btts_yes | production_raw | 27 | 0.2789 | 0.7527 | +0.0000 | +0.0000 | +21.6% |
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
| Serie A | over_1_5 | development_1x2 | 29 | 0.1200 | 0.4111 | +0.0033 | +0.0080 | -16.6% |
| Serie A | over_1_5 | goal_selected | 29 | 0.1207 | 0.4115 | +0.0027 | +0.0077 | -15.9% |
| Serie A | over_1_5 | half_life_1000000000 | 29 | 0.1160 | 0.4002 | +0.0073 | +0.0189 | -16.7% |
| Serie A | over_1_5 | half_life_120 | 29 | 0.1293 | 0.4342 | -0.0060 | -0.0150 | -14.8% |
| Serie A | over_1_5 | half_life_240 | 29 | 0.1207 | 0.4115 | +0.0027 | +0.0077 | -15.9% |
| Serie A | over_1_5 | half_life_365 | 29 | 0.1179 | 0.4054 | +0.0054 | +0.0137 | -16.3% |
| Serie A | over_1_5 | half_life_730 | 29 | 0.1163 | 0.4017 | +0.0070 | +0.0174 | -16.6% |
| Serie A | over_1_5 | production_raw | 29 | 0.1233 | 0.4191 | +0.0000 | +0.0000 | -16.2% |
| Serie A | btts_yes | development_1x2 | 29 | 0.2221 | 0.6370 | +0.0014 | +0.0030 | -6.6% |
| Serie A | btts_yes | goal_selected | 29 | 0.2223 | 0.6372 | +0.0013 | +0.0027 | -6.6% |
| Serie A | btts_yes | half_life_1000000000 | 29 | 0.2187 | 0.6297 | +0.0048 | +0.0102 | -6.4% |
| Serie A | btts_yes | half_life_120 | 29 | 0.2305 | 0.6541 | -0.0070 | -0.0142 | -5.9% |
| Serie A | btts_yes | half_life_240 | 29 | 0.2260 | 0.6448 | -0.0024 | -0.0049 | -6.5% |
| Serie A | btts_yes | half_life_365 | 29 | 0.2236 | 0.6400 | -0.0001 | -0.0001 | -6.7% |
| Serie A | btts_yes | half_life_730 | 29 | 0.2210 | 0.6346 | +0.0025 | +0.0053 | -6.6% |
| Serie A | btts_yes | production_raw | 29 | 0.2236 | 0.6400 | +0.0000 | +0.0000 | -6.5% |
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