# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 476/518 fixture-markets; 278 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 139 | 0.1585 | 0.5296 | +0.0015 | +0.0025 | -4.7% |
| ALL | over_1_5 | goal_selected | 124 | 0.1614 | 0.5335 | -0.0013 | +0.0029 | -4.5% |
| ALL | over_1_5 | half_life_1000000000 | 139 | 0.1595 | 0.5328 | +0.0005 | -0.0008 | -4.9% |
| ALL | over_1_5 | half_life_120 | 139 | 0.1630 | 0.5390 | -0.0030 | -0.0070 | -4.1% |
| ALL | over_1_5 | half_life_240 | 139 | 0.1594 | 0.5214 | +0.0006 | +0.0106 | -4.5% |
| ALL | over_1_5 | half_life_365 | 139 | 0.1590 | 0.5238 | +0.0011 | +0.0082 | -4.6% |
| ALL | over_1_5 | half_life_730 | 139 | 0.1591 | 0.5285 | +0.0010 | +0.0036 | -4.7% |
| ALL | over_1_5 | production_raw | 139 | 0.1600 | 0.5320 | +0.0000 | +0.0000 | -4.7% |
| ALL | btts_yes | development_1x2 | 139 | 0.2567 | 0.7208 | +0.0012 | +0.0029 | -4.1% |
| ALL | btts_yes | goal_selected | 124 | 0.2541 | 0.7168 | +0.0003 | -0.0005 | -4.4% |
| ALL | btts_yes | half_life_1000000000 | 139 | 0.2570 | 0.7216 | +0.0009 | +0.0020 | -4.2% |
| ALL | btts_yes | half_life_120 | 139 | 0.2715 | 0.7633 | -0.0135 | -0.0397 | -3.7% |
| ALL | btts_yes | half_life_240 | 139 | 0.2618 | 0.7360 | -0.0039 | -0.0123 | -3.8% |
| ALL | btts_yes | half_life_365 | 139 | 0.2593 | 0.7288 | -0.0013 | -0.0051 | -3.9% |
| ALL | btts_yes | half_life_730 | 139 | 0.2576 | 0.7238 | +0.0004 | -0.0001 | -4.0% |
| ALL | btts_yes | production_raw | 139 | 0.2580 | 0.7237 | +0.0000 | +0.0000 | -4.0% |
| Bundesliga | over_1_5 | development_1x2 | 14 | 0.1194 | 0.3789 | +0.0026 | +0.0062 | +0.6% |
| Bundesliga | over_1_5 | goal_selected | 14 | 0.1234 | 0.3876 | -0.0014 | -0.0024 | +1.1% |
| Bundesliga | over_1_5 | half_life_1000000000 | 14 | 0.1194 | 0.3789 | +0.0026 | +0.0062 | +0.6% |
| Bundesliga | over_1_5 | half_life_120 | 14 | 0.1212 | 0.3754 | +0.0008 | +0.0097 | +2.8% |
| Bundesliga | over_1_5 | half_life_240 | 14 | 0.1236 | 0.3869 | -0.0017 | -0.0018 | +1.5% |
| Bundesliga | over_1_5 | half_life_365 | 14 | 0.1234 | 0.3876 | -0.0014 | -0.0024 | +1.1% |
| Bundesliga | over_1_5 | half_life_730 | 14 | 0.1219 | 0.3849 | +0.0000 | +0.0002 | +0.8% |
| Bundesliga | over_1_5 | production_raw | 14 | 0.1220 | 0.3851 | +0.0000 | +0.0000 | +0.7% |
| Bundesliga | btts_yes | development_1x2 | 14 | 0.2214 | 0.6355 | +0.0008 | +0.0024 | -7.6% |
| Bundesliga | btts_yes | goal_selected | 14 | 0.2192 | 0.6325 | +0.0030 | +0.0054 | -6.5% |
| Bundesliga | btts_yes | half_life_1000000000 | 14 | 0.2214 | 0.6355 | +0.0008 | +0.0024 | -7.6% |
| Bundesliga | btts_yes | half_life_120 | 14 | 0.2118 | 0.6179 | +0.0105 | +0.0199 | -5.4% |
| Bundesliga | btts_yes | half_life_240 | 14 | 0.2192 | 0.6325 | +0.0030 | +0.0054 | -6.5% |
| Bundesliga | btts_yes | half_life_365 | 14 | 0.2210 | 0.6359 | +0.0012 | +0.0020 | -6.9% |
| Bundesliga | btts_yes | half_life_730 | 14 | 0.2218 | 0.6370 | +0.0004 | +0.0009 | -7.3% |
| Bundesliga | btts_yes | production_raw | 14 | 0.2222 | 0.6379 | +0.0000 | +0.0000 | -7.3% |
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
| La Liga | over_1_5 | development_1x2 | 16 | 0.1841 | 0.5560 | +0.0032 | +0.0079 | -3.2% |
| La Liga | over_1_5 | goal_selected | 16 | 0.1772 | 0.5391 | +0.0101 | +0.0248 | -0.7% |
| La Liga | over_1_5 | half_life_1000000000 | 16 | 0.1908 | 0.5728 | -0.0035 | -0.0089 | -4.4% |
| La Liga | over_1_5 | half_life_120 | 16 | 0.1772 | 0.5391 | +0.0101 | +0.0248 | -0.7% |
| La Liga | over_1_5 | half_life_240 | 16 | 0.1814 | 0.5495 | +0.0059 | +0.0144 | -2.5% |
| La Liga | over_1_5 | half_life_365 | 16 | 0.1841 | 0.5560 | +0.0032 | +0.0079 | -3.2% |
| La Liga | over_1_5 | half_life_730 | 16 | 0.1873 | 0.5639 | +0.0000 | +0.0000 | -3.9% |
| La Liga | over_1_5 | production_raw | 16 | 0.1873 | 0.5639 | +0.0000 | +0.0000 | -3.9% |
| La Liga | btts_yes | development_1x2 | 16 | 0.2814 | 0.7621 | +0.0021 | +0.0047 | -7.1% |
| La Liga | btts_yes | goal_selected | 16 | 0.2806 | 0.7602 | +0.0029 | +0.0066 | -6.5% |
| La Liga | btts_yes | half_life_1000000000 | 16 | 0.2869 | 0.7746 | -0.0034 | -0.0078 | -8.2% |
| La Liga | btts_yes | half_life_120 | 16 | 0.2822 | 0.7645 | +0.0013 | +0.0022 | -4.8% |
| La Liga | btts_yes | half_life_240 | 16 | 0.2806 | 0.7602 | +0.0029 | +0.0066 | -6.5% |
| La Liga | btts_yes | half_life_365 | 16 | 0.2814 | 0.7621 | +0.0021 | +0.0047 | -7.1% |
| La Liga | btts_yes | half_life_730 | 16 | 0.2835 | 0.7668 | +0.0000 | +0.0000 | -7.7% |
| La Liga | btts_yes | production_raw | 16 | 0.2835 | 0.7668 | +0.0000 | +0.0000 | -7.7% |
| Ligue 1 | over_1_5 | development_1x2 | 13 | 0.1837 | 0.5536 | +0.0016 | +0.0070 | +1.9% |
| Ligue 1 | over_1_5 | goal_selected | 13 | 0.1878 | 0.5699 | -0.0025 | -0.0094 | +1.8% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 13 | 0.1878 | 0.5699 | -0.0025 | -0.0094 | +1.8% |
| Ligue 1 | over_1_5 | half_life_120 | 13 | 0.1968 | 0.5974 | -0.0115 | -0.0368 | +2.2% |
| Ligue 1 | over_1_5 | half_life_240 | 13 | 0.1903 | 0.5744 | -0.0049 | -0.0138 | +2.3% |
| Ligue 1 | over_1_5 | half_life_365 | 13 | 0.1887 | 0.5698 | -0.0034 | -0.0092 | +2.2% |
| Ligue 1 | over_1_5 | half_life_730 | 13 | 0.1875 | 0.5670 | -0.0022 | -0.0064 | +2.0% |
| Ligue 1 | over_1_5 | production_raw | 13 | 0.1853 | 0.5606 | +0.0000 | +0.0000 | +1.9% |
| Ligue 1 | btts_yes | development_1x2 | 13 | 0.2483 | 0.6902 | -0.0005 | -0.0010 | -14.9% |
| Ligue 1 | btts_yes | goal_selected | 13 | 0.2497 | 0.6934 | -0.0019 | -0.0041 | -14.9% |
| Ligue 1 | btts_yes | half_life_1000000000 | 13 | 0.2497 | 0.6934 | -0.0019 | -0.0041 | -14.9% |
| Ligue 1 | btts_yes | half_life_120 | 13 | 0.2512 | 0.6964 | -0.0033 | -0.0072 | -15.8% |
| Ligue 1 | btts_yes | half_life_240 | 13 | 0.2445 | 0.6826 | +0.0033 | +0.0067 | -15.3% |
| Ligue 1 | btts_yes | half_life_365 | 13 | 0.2450 | 0.6835 | +0.0028 | +0.0057 | -15.1% |
| Ligue 1 | btts_yes | half_life_730 | 13 | 0.2470 | 0.6877 | +0.0008 | +0.0015 | -14.9% |
| Ligue 1 | btts_yes | production_raw | 13 | 0.2478 | 0.6893 | +0.0000 | +0.0000 | -14.8% |
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
| Primeira Liga | over_1_5 | development_1x2 | 1 | 0.1103 | 0.4037 | -0.0003 | -0.0007 | -33.2% |
| Primeira Liga | over_1_5 | goal_selected | 1 | 0.1100 | 0.4030 | +0.0000 | +0.0000 | -33.2% |
| Primeira Liga | over_1_5 | half_life_1000000000 | 1 | 0.1103 | 0.4037 | -0.0003 | -0.0007 | -33.2% |
| Primeira Liga | over_1_5 | half_life_120 | 1 | 0.0798 | 0.3320 | +0.0302 | +0.0710 | -28.3% |
| Primeira Liga | over_1_5 | half_life_240 | 1 | 0.0984 | 0.3764 | +0.0116 | +0.0266 | -31.4% |
| Primeira Liga | over_1_5 | half_life_365 | 1 | 0.1050 | 0.3917 | +0.0050 | +0.0113 | -32.4% |
| Primeira Liga | over_1_5 | half_life_730 | 1 | 0.1100 | 0.4030 | +0.0000 | +0.0000 | -33.2% |
| Primeira Liga | over_1_5 | production_raw | 1 | 0.1100 | 0.4030 | +0.0000 | +0.0000 | -33.2% |
| Primeira Liga | btts_yes | development_1x2 | 1 | 0.2159 | 0.6248 | -0.0042 | -0.0084 | +46.5% |
| Primeira Liga | btts_yes | goal_selected | 1 | 0.2117 | 0.6164 | +0.0000 | +0.0000 | +46.0% |
| Primeira Liga | btts_yes | half_life_1000000000 | 1 | 0.2159 | 0.6248 | -0.0042 | -0.0084 | +46.5% |
| Primeira Liga | btts_yes | half_life_120 | 1 | 0.2339 | 0.6609 | -0.0221 | -0.0444 | +48.4% |
| Primeira Liga | btts_yes | half_life_240 | 1 | 0.2140 | 0.6211 | -0.0023 | -0.0046 | +46.3% |
| Primeira Liga | btts_yes | half_life_365 | 1 | 0.2114 | 0.6158 | +0.0003 | +0.0006 | +46.0% |
| Primeira Liga | btts_yes | half_life_730 | 1 | 0.2117 | 0.6164 | +0.0000 | +0.0000 | +46.0% |
| Primeira Liga | btts_yes | production_raw | 1 | 0.2117 | 0.6164 | +0.0000 | +0.0000 | +46.0% |
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
| La Liga | over_1_5 | 120.0 | 281 | 99 | -0.0068 | {'120.0': 2, '1000000000.0': 1, '240.0': 1} |
| La Liga | btts_yes | 240.0 | 281 | 99 | +0.0019 | {'1000000000.0': 1, '365.0': 1, '120.0': 2} |
| Bundesliga | over_1_5 | 1000000000.0 | 236 | 63 | +0.0014 | {'1000000000.0': 2, '730.0': 2} |
| Bundesliga | btts_yes | 240.0 | 236 | 63 | -0.0001 | {'1000000000.0': 1, '120.0': 2, '730.0': 1} |
| Serie A | over_1_5 | 240.0 | 292 | 90 | -0.0078 | {'240.0': 2, '1000000000.0': 1, '120.0': 1} |
| Serie A | btts_yes | 240.0 | 292 | 90 | -0.0125 | {'365.0': 1, '120.0': 1, '1000000000.0': 1, '240.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 225 | 72 | +0.0000 | {'1000000000.0': 2, '240.0': 1, '365.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 225 | 72 | +0.0000 | {'1000000000.0': 3, '240.0': 1} |
| Eredivisie | over_1_5 | 730.0 | 220 | 90 | -0.0009 | {'1000000000.0': 2, '240.0': 2} |
| Eredivisie | btts_yes | 240.0 | 220 | 90 | +0.0039 | {'730.0': 1, '120.0': 3} |
| Primeira Liga | over_1_5 | 730.0 | 226 | 81 | -0.0020 | {'120.0': 1, '240.0': 1, '1000000000.0': 2} |
| Primeira Liga | btts_yes | 730.0 | 226 | 81 | -0.0040 | {'1000000000.0': 2, '730.0': 2} |
| Super Lig | over_1_5 | 365.0 | 218 | 81 | +0.0001 | {'240.0': 1, '120.0': 2, '1000000000.0': 1} |
| Super Lig | btts_yes | 1000000000.0 | 218 | 81 | +0.0051 | {'120.0': 1, '1000000000.0': 2, '240.0': 1} |