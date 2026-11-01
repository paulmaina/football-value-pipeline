# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 556/598 fixture-markets; 354 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 177 | 0.1626 | 0.5301 | +0.0009 | +0.0011 | -2.6% |
| ALL | over_1_5 | goal_selected | 162 | 0.1639 | 0.5287 | +0.0000 | +0.0058 | -2.2% |
| ALL | over_1_5 | half_life_1000000000 | 177 | 0.1636 | 0.5337 | -0.0000 | -0.0025 | -2.9% |
| ALL | over_1_5 | half_life_120 | 177 | 0.1652 | 0.5321 | -0.0016 | -0.0009 | -2.1% |
| ALL | over_1_5 | half_life_240 | 177 | 0.1630 | 0.5215 | +0.0006 | +0.0097 | -2.4% |
| ALL | over_1_5 | half_life_365 | 177 | 0.1627 | 0.5244 | +0.0008 | +0.0068 | -2.5% |
| ALL | over_1_5 | half_life_730 | 177 | 0.1630 | 0.5294 | +0.0005 | +0.0018 | -2.7% |
| ALL | over_1_5 | production_raw | 177 | 0.1635 | 0.5312 | +0.0000 | +0.0000 | -2.6% |
| ALL | btts_yes | development_1x2 | 177 | 0.2640 | 0.7333 | +0.0008 | +0.0016 | -0.1% |
| ALL | btts_yes | goal_selected | 162 | 0.2616 | 0.7297 | +0.0010 | +0.0005 | +0.0% |
| ALL | btts_yes | half_life_1000000000 | 177 | 0.2627 | 0.7301 | +0.0021 | +0.0048 | -0.5% |
| ALL | btts_yes | half_life_120 | 177 | 0.2738 | 0.7644 | -0.0091 | -0.0295 | +0.3% |
| ALL | btts_yes | half_life_240 | 177 | 0.2667 | 0.7431 | -0.0020 | -0.0082 | +0.1% |
| ALL | btts_yes | half_life_365 | 177 | 0.2650 | 0.7375 | -0.0002 | -0.0026 | +0.0% |
| ALL | btts_yes | half_life_730 | 177 | 0.2636 | 0.7328 | +0.0012 | +0.0021 | -0.2% |
| ALL | btts_yes | production_raw | 177 | 0.2648 | 0.7349 | +0.0000 | +0.0000 | -0.1% |
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
| Eredivisie | over_1_5 | development_1x2 | 10 | 0.2178 | 0.6116 | +0.0004 | +0.0039 | +19.2% |
| Eredivisie | over_1_5 | goal_selected | 10 | 0.2191 | 0.6220 | -0.0009 | -0.0065 | +17.7% |
| Eredivisie | over_1_5 | half_life_1000000000 | 10 | 0.2174 | 0.6208 | +0.0008 | -0.0053 | +15.9% |
| Eredivisie | over_1_5 | half_life_120 | 10 | 0.2129 | 0.5831 | +0.0054 | +0.0324 | +21.2% |
| Eredivisie | over_1_5 | half_life_240 | 10 | 0.2162 | 0.6017 | +0.0020 | +0.0138 | +20.1% |
| Eredivisie | over_1_5 | half_life_365 | 10 | 0.2178 | 0.6116 | +0.0004 | +0.0039 | +19.2% |
| Eredivisie | over_1_5 | half_life_730 | 10 | 0.2191 | 0.6220 | -0.0009 | -0.0065 | +17.7% |
| Eredivisie | over_1_5 | production_raw | 10 | 0.2182 | 0.6155 | +0.0000 | +0.0000 | +18.7% |
| Eredivisie | btts_yes | development_1x2 | 10 | 0.3296 | 0.8671 | -0.0091 | -0.0236 | +33.1% |
| Eredivisie | btts_yes | goal_selected | 10 | 0.3399 | 0.8971 | -0.0194 | -0.0536 | +34.5% |
| Eredivisie | btts_yes | half_life_1000000000 | 10 | 0.2935 | 0.7817 | +0.0270 | +0.0618 | +28.5% |
| Eredivisie | btts_yes | half_life_120 | 10 | 0.3442 | 0.9178 | -0.0237 | -0.0743 | +36.0% |
| Eredivisie | btts_yes | half_life_240 | 10 | 0.3399 | 0.8971 | -0.0194 | -0.0536 | +34.5% |
| Eredivisie | btts_yes | half_life_365 | 10 | 0.3296 | 0.8671 | -0.0091 | -0.0236 | +33.1% |
| Eredivisie | btts_yes | half_life_730 | 10 | 0.3107 | 0.8199 | +0.0098 | +0.0236 | +30.9% |
| Eredivisie | btts_yes | production_raw | 10 | 0.3205 | 0.8435 | +0.0000 | +0.0000 | +32.3% |
| La Liga | over_1_5 | development_1x2 | 22 | 0.2083 | 0.6148 | +0.0016 | +0.0032 | +1.0% |
| La Liga | over_1_5 | goal_selected | 22 | 0.1956 | 0.5731 | +0.0143 | +0.0449 | +2.6% |
| La Liga | over_1_5 | half_life_1000000000 | 22 | 0.2136 | 0.6288 | -0.0036 | -0.0109 | +0.1% |
| La Liga | over_1_5 | half_life_120 | 22 | 0.1956 | 0.5731 | +0.0143 | +0.0449 | +2.6% |
| La Liga | over_1_5 | half_life_240 | 22 | 0.2028 | 0.5959 | +0.0071 | +0.0221 | +1.4% |
| La Liga | over_1_5 | half_life_365 | 22 | 0.2063 | 0.6069 | +0.0036 | +0.0110 | +0.9% |
| La Liga | over_1_5 | half_life_730 | 22 | 0.2102 | 0.6189 | -0.0003 | -0.0010 | +0.5% |
| La Liga | over_1_5 | production_raw | 22 | 0.2099 | 0.6180 | +0.0000 | +0.0000 | +0.6% |
| La Liga | btts_yes | development_1x2 | 22 | 0.2958 | 0.7897 | +0.0021 | +0.0046 | -5.3% |
| La Liga | btts_yes | goal_selected | 22 | 0.2906 | 0.7793 | +0.0072 | +0.0151 | -5.0% |
| La Liga | btts_yes | half_life_1000000000 | 22 | 0.3030 | 0.8054 | -0.0051 | -0.0110 | -6.2% |
| La Liga | btts_yes | half_life_120 | 22 | 0.2894 | 0.7780 | +0.0085 | +0.0163 | -3.9% |
| La Liga | btts_yes | half_life_240 | 22 | 0.2906 | 0.7793 | +0.0072 | +0.0151 | -5.0% |
| La Liga | btts_yes | half_life_365 | 22 | 0.2928 | 0.7838 | +0.0050 | +0.0106 | -5.4% |
| La Liga | btts_yes | half_life_730 | 22 | 0.2970 | 0.7926 | +0.0008 | +0.0018 | -5.8% |
| La Liga | btts_yes | production_raw | 22 | 0.2979 | 0.7944 | +0.0000 | +0.0000 | -5.7% |
| Ligue 1 | over_1_5 | development_1x2 | 17 | 0.2000 | 0.5829 | +0.0012 | +0.0053 | +7.7% |
| Ligue 1 | over_1_5 | goal_selected | 17 | 0.2031 | 0.5954 | -0.0019 | -0.0072 | +7.6% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 17 | 0.2031 | 0.5954 | -0.0019 | -0.0072 | +7.6% |
| Ligue 1 | over_1_5 | half_life_120 | 17 | 0.2144 | 0.6286 | -0.0132 | -0.0404 | +7.4% |
| Ligue 1 | over_1_5 | half_life_240 | 17 | 0.2076 | 0.6062 | -0.0064 | -0.0180 | +7.7% |
| Ligue 1 | over_1_5 | half_life_365 | 17 | 0.2049 | 0.5985 | -0.0036 | -0.0103 | +7.8% |
| Ligue 1 | over_1_5 | half_life_730 | 17 | 0.2027 | 0.5930 | -0.0015 | -0.0048 | +7.7% |
| Ligue 1 | over_1_5 | production_raw | 17 | 0.2012 | 0.5882 | +0.0000 | +0.0000 | +7.7% |
| Ligue 1 | btts_yes | development_1x2 | 17 | 0.2579 | 0.7102 | -0.0005 | -0.0010 | -4.7% |
| Ligue 1 | btts_yes | goal_selected | 17 | 0.2590 | 0.7126 | -0.0016 | -0.0033 | -4.7% |
| Ligue 1 | btts_yes | half_life_1000000000 | 17 | 0.2590 | 0.7126 | -0.0016 | -0.0033 | -4.7% |
| Ligue 1 | btts_yes | half_life_120 | 17 | 0.2603 | 0.7147 | -0.0029 | -0.0055 | -6.2% |
| Ligue 1 | btts_yes | half_life_240 | 17 | 0.2549 | 0.7034 | +0.0026 | +0.0058 | -5.5% |
| Ligue 1 | btts_yes | half_life_365 | 17 | 0.2553 | 0.7046 | +0.0021 | +0.0046 | -5.1% |
| Ligue 1 | btts_yes | half_life_730 | 17 | 0.2569 | 0.7082 | +0.0005 | +0.0011 | -4.8% |
| Ligue 1 | btts_yes | production_raw | 17 | 0.2574 | 0.7092 | +0.0000 | +0.0000 | -4.6% |
| Premier League | over_1_5 | development_1x2 | 28 | 0.1552 | 0.4857 | -0.0013 | -0.0031 | -1.2% |
| Premier League | over_1_5 | goal_selected | 28 | 0.1590 | 0.4967 | -0.0050 | -0.0141 | -1.3% |
| Premier League | over_1_5 | half_life_1000000000 | 28 | 0.1596 | 0.4982 | -0.0057 | -0.0156 | -1.4% |
| Premier League | over_1_5 | half_life_120 | 28 | 0.1521 | 0.4793 | +0.0019 | +0.0033 | -1.2% |
| Premier League | over_1_5 | half_life_240 | 28 | 0.1539 | 0.4826 | +0.0000 | +0.0000 | -1.2% |
| Premier League | over_1_5 | half_life_365 | 28 | 0.1556 | 0.4870 | -0.0017 | -0.0044 | -1.2% |
| Premier League | over_1_5 | half_life_730 | 28 | 0.1576 | 0.4925 | -0.0036 | -0.0099 | -1.3% |
| Premier League | over_1_5 | production_raw | 28 | 0.1539 | 0.4826 | +0.0000 | +0.0000 | -1.2% |
| Premier League | btts_yes | development_1x2 | 28 | 0.2761 | 0.7468 | +0.0010 | +0.0021 | +19.1% |
| Premier League | btts_yes | goal_selected | 28 | 0.2757 | 0.7456 | +0.0014 | +0.0033 | +18.4% |
| Premier League | btts_yes | half_life_1000000000 | 28 | 0.2759 | 0.7462 | +0.0012 | +0.0028 | +18.2% |
| Premier League | btts_yes | half_life_120 | 28 | 0.2814 | 0.7598 | -0.0043 | -0.0108 | +19.3% |
| Premier League | btts_yes | half_life_240 | 28 | 0.2771 | 0.7490 | +0.0000 | +0.0000 | +19.2% |
| Premier League | btts_yes | half_life_365 | 28 | 0.2767 | 0.7479 | +0.0004 | +0.0011 | +18.9% |
| Premier League | btts_yes | half_life_730 | 28 | 0.2766 | 0.7474 | +0.0005 | +0.0015 | +18.6% |
| Premier League | btts_yes | production_raw | 28 | 0.2771 | 0.7490 | +0.0000 | +0.0000 | +19.2% |
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
| Serie A | over_1_5 | development_1x2 | 30 | 0.1174 | 0.4051 | +0.0030 | +0.0070 | -16.7% |
| Serie A | over_1_5 | goal_selected | 30 | 0.1176 | 0.4041 | +0.0027 | +0.0080 | -16.0% |
| Serie A | over_1_5 | half_life_1000000000 | 30 | 0.1135 | 0.3946 | +0.0069 | +0.0175 | -16.8% |
| Serie A | over_1_5 | half_life_120 | 30 | 0.1257 | 0.4248 | -0.0053 | -0.0127 | -14.8% |
| Serie A | over_1_5 | half_life_240 | 30 | 0.1176 | 0.4041 | +0.0027 | +0.0080 | -16.0% |
| Serie A | over_1_5 | half_life_365 | 30 | 0.1151 | 0.3987 | +0.0053 | +0.0135 | -16.4% |
| Serie A | over_1_5 | half_life_730 | 30 | 0.1136 | 0.3955 | +0.0067 | +0.0166 | -16.7% |
| Serie A | over_1_5 | production_raw | 30 | 0.1204 | 0.4121 | +0.0000 | +0.0000 | -16.3% |
| Serie A | btts_yes | development_1x2 | 30 | 0.2205 | 0.6336 | +0.0010 | +0.0021 | -7.8% |
| Serie A | btts_yes | goal_selected | 30 | 0.2201 | 0.6328 | +0.0013 | +0.0029 | -7.7% |
| Serie A | btts_yes | half_life_1000000000 | 30 | 0.2172 | 0.6266 | +0.0043 | +0.0091 | -7.6% |
| Serie A | btts_yes | half_life_120 | 30 | 0.2271 | 0.6470 | -0.0056 | -0.0112 | -6.9% |
| Serie A | btts_yes | half_life_240 | 30 | 0.2234 | 0.6397 | -0.0019 | -0.0040 | -7.6% |
| Serie A | btts_yes | half_life_365 | 30 | 0.2214 | 0.6355 | +0.0001 | +0.0002 | -7.8% |
| Serie A | btts_yes | half_life_730 | 30 | 0.2191 | 0.6308 | +0.0023 | +0.0049 | -7.7% |
| Serie A | btts_yes | production_raw | 30 | 0.2215 | 0.6357 | +0.0000 | +0.0000 | -7.7% |
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
| Premier League | over_1_5 | 1000000000.0 | 290 | 88 | -0.0102 | {'730.0': 1, '120.0': 1, '1000000000.0': 2} |
| Premier League | btts_yes | 1000000000.0 | 290 | 88 | -0.0073 | {'1000000000.0': 2, '730.0': 1, '120.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 216 | 76 | +0.0000 | {'1000000000.0': 2, '240.0': 1, '365.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 216 | 76 | +0.0000 | {'1000000000.0': 3, '240.0': 1} |
| UEFA Champions League | over_1_5 | 365.0 | 144 | 54 | +0.0035 | {'730.0': 1, '120.0': 2, '240.0': 1} |
| UEFA Champions League | btts_yes | 1000000000.0 | 144 | 54 | +0.0034 | {'240.0': 1, '1000000000.0': 3} |
| Eredivisie | over_1_5 | 730.0 | 220 | 90 | -0.0009 | {'1000000000.0': 2, '240.0': 2} |
| Eredivisie | btts_yes | 240.0 | 220 | 90 | +0.0039 | {'730.0': 1, '120.0': 3} |
| Primeira Liga | over_1_5 | 730.0 | 226 | 81 | -0.0020 | {'120.0': 1, '240.0': 1, '1000000000.0': 2} |
| Primeira Liga | btts_yes | 730.0 | 226 | 81 | -0.0040 | {'1000000000.0': 2, '730.0': 2} |