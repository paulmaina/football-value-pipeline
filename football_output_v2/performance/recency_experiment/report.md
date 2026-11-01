# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 556/598 fixture-markets; 394 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 197 | 0.1589 | 0.5180 | +0.0008 | +0.0010 | -3.2% |
| ALL | over_1_5 | goal_selected | 182 | 0.1601 | 0.5167 | -0.0004 | +0.0042 | -2.9% |
| ALL | over_1_5 | half_life_1000000000 | 197 | 0.1603 | 0.5229 | -0.0006 | -0.0039 | -3.6% |
| ALL | over_1_5 | half_life_120 | 197 | 0.1597 | 0.5151 | +0.0000 | +0.0039 | -2.4% |
| ALL | over_1_5 | half_life_240 | 197 | 0.1588 | 0.5088 | +0.0009 | +0.0102 | -2.8% |
| ALL | over_1_5 | half_life_365 | 197 | 0.1589 | 0.5127 | +0.0008 | +0.0063 | -3.0% |
| ALL | over_1_5 | half_life_730 | 197 | 0.1596 | 0.5184 | +0.0001 | +0.0006 | -3.3% |
| ALL | over_1_5 | production_raw | 197 | 0.1597 | 0.5190 | +0.0000 | +0.0000 | -3.1% |
| ALL | btts_yes | development_1x2 | 197 | 0.2616 | 0.7274 | +0.0012 | +0.0025 | -0.2% |
| ALL | btts_yes | goal_selected | 182 | 0.2605 | 0.7263 | +0.0003 | -0.0010 | +0.0% |
| ALL | btts_yes | half_life_1000000000 | 197 | 0.2613 | 0.7263 | +0.0015 | +0.0036 | -0.7% |
| ALL | btts_yes | half_life_120 | 197 | 0.2694 | 0.7534 | -0.0066 | -0.0235 | +0.4% |
| ALL | btts_yes | half_life_240 | 197 | 0.2643 | 0.7367 | -0.0015 | -0.0069 | +0.2% |
| ALL | btts_yes | half_life_365 | 197 | 0.2630 | 0.7322 | -0.0002 | -0.0023 | -0.0% |
| ALL | btts_yes | half_life_730 | 197 | 0.2619 | 0.7284 | +0.0009 | +0.0015 | -0.3% |
| ALL | btts_yes | production_raw | 197 | 0.2628 | 0.7299 | +0.0000 | +0.0000 | -0.1% |
| Bundesliga | over_1_5 | development_1x2 | 24 | 0.1010 | 0.3384 | +0.0019 | +0.0043 | -2.9% |
| Bundesliga | over_1_5 | goal_selected | 24 | 0.1037 | 0.3442 | -0.0008 | -0.0015 | -2.5% |
| Bundesliga | over_1_5 | half_life_1000000000 | 24 | 0.1014 | 0.3392 | +0.0015 | +0.0035 | -2.8% |
| Bundesliga | over_1_5 | half_life_120 | 24 | 0.1045 | 0.3384 | -0.0016 | +0.0043 | -2.0% |
| Bundesliga | over_1_5 | half_life_240 | 24 | 0.1051 | 0.3456 | -0.0022 | -0.0029 | -2.8% |
| Bundesliga | over_1_5 | half_life_365 | 24 | 0.1038 | 0.3443 | -0.0009 | -0.0016 | -2.8% |
| Bundesliga | over_1_5 | half_life_730 | 24 | 0.1025 | 0.3419 | +0.0004 | +0.0008 | -2.8% |
| Bundesliga | over_1_5 | production_raw | 24 | 0.1029 | 0.3427 | +0.0000 | +0.0000 | -2.7% |
| Bundesliga | btts_yes | development_1x2 | 24 | 0.2072 | 0.6057 | +0.0043 | +0.0093 | -8.2% |
| Bundesliga | btts_yes | goal_selected | 24 | 0.1975 | 0.5863 | +0.0141 | +0.0287 | -7.6% |
| Bundesliga | btts_yes | half_life_1000000000 | 24 | 0.2112 | 0.6138 | +0.0004 | +0.0012 | -8.3% |
| Bundesliga | btts_yes | half_life_120 | 24 | 0.1930 | 0.5772 | +0.0185 | +0.0378 | -6.9% |
| Bundesliga | btts_yes | half_life_240 | 24 | 0.1975 | 0.5863 | +0.0141 | +0.0287 | -7.6% |
| Bundesliga | btts_yes | half_life_365 | 24 | 0.2019 | 0.5955 | +0.0096 | +0.0194 | -7.8% |
| Bundesliga | btts_yes | half_life_730 | 24 | 0.2074 | 0.6066 | +0.0041 | +0.0084 | -8.0% |
| Bundesliga | btts_yes | production_raw | 24 | 0.2115 | 0.6150 | +0.0000 | +0.0000 | -8.2% |
| Eredivisie | over_1_5 | development_1x2 | 14 | 0.1654 | 0.4954 | +0.0010 | +0.0049 | +8.4% |
| Eredivisie | over_1_5 | goal_selected | 14 | 0.1678 | 0.5073 | -0.0014 | -0.0070 | +7.0% |
| Eredivisie | over_1_5 | half_life_1000000000 | 14 | 0.1680 | 0.5107 | -0.0017 | -0.0104 | +5.4% |
| Eredivisie | over_1_5 | half_life_120 | 14 | 0.1585 | 0.4608 | +0.0079 | +0.0396 | +11.1% |
| Eredivisie | over_1_5 | half_life_240 | 14 | 0.1631 | 0.4840 | +0.0033 | +0.0163 | +9.4% |
| Eredivisie | over_1_5 | half_life_365 | 14 | 0.1654 | 0.4954 | +0.0010 | +0.0049 | +8.4% |
| Eredivisie | over_1_5 | half_life_730 | 14 | 0.1678 | 0.5073 | -0.0014 | -0.0070 | +7.0% |
| Eredivisie | over_1_5 | production_raw | 14 | 0.1664 | 0.5003 | +0.0000 | +0.0000 | +7.9% |
| Eredivisie | btts_yes | development_1x2 | 14 | 0.2895 | 0.7819 | -0.0049 | -0.0134 | +19.5% |
| Eredivisie | btts_yes | goal_selected | 14 | 0.2931 | 0.7954 | -0.0084 | -0.0269 | +20.9% |
| Eredivisie | btts_yes | half_life_1000000000 | 14 | 0.2694 | 0.7326 | +0.0153 | +0.0359 | +15.4% |
| Eredivisie | btts_yes | half_life_120 | 14 | 0.2870 | 0.7899 | -0.0023 | -0.0214 | +22.8% |
| Eredivisie | btts_yes | half_life_240 | 14 | 0.2931 | 0.7954 | -0.0084 | -0.0269 | +20.9% |
| Eredivisie | btts_yes | half_life_365 | 14 | 0.2895 | 0.7819 | -0.0049 | -0.0134 | +19.5% |
| Eredivisie | btts_yes | half_life_730 | 14 | 0.2793 | 0.7550 | +0.0054 | +0.0135 | +17.5% |
| Eredivisie | btts_yes | production_raw | 14 | 0.2847 | 0.7685 | +0.0000 | +0.0000 | +18.7% |
| La Liga | over_1_5 | development_1x2 | 24 | 0.2120 | 0.6170 | +0.0015 | +0.0029 | +3.7% |
| La Liga | over_1_5 | goal_selected | 24 | 0.2009 | 0.5801 | +0.0126 | +0.0398 | +5.2% |
| La Liga | over_1_5 | half_life_1000000000 | 24 | 0.2157 | 0.6270 | -0.0022 | -0.0072 | +2.8% |
| La Liga | over_1_5 | half_life_120 | 24 | 0.2009 | 0.5801 | +0.0126 | +0.0398 | +5.2% |
| La Liga | over_1_5 | half_life_240 | 24 | 0.2082 | 0.6028 | +0.0053 | +0.0171 | +4.2% |
| La Liga | over_1_5 | half_life_365 | 24 | 0.2111 | 0.6121 | +0.0024 | +0.0078 | +3.7% |
| La Liga | over_1_5 | half_life_730 | 24 | 0.2137 | 0.6208 | -0.0003 | -0.0009 | +3.2% |
| La Liga | over_1_5 | production_raw | 24 | 0.2135 | 0.6199 | +0.0000 | +0.0000 | +3.3% |
| La Liga | btts_yes | development_1x2 | 24 | 0.3007 | 0.8000 | +0.0019 | +0.0043 | +0.0% |
| La Liga | btts_yes | goal_selected | 24 | 0.2967 | 0.7919 | +0.0060 | +0.0124 | +0.4% |
| La Liga | btts_yes | half_life_1000000000 | 24 | 0.3065 | 0.8127 | -0.0039 | -0.0084 | -0.8% |
| La Liga | btts_yes | half_life_120 | 24 | 0.2943 | 0.7882 | +0.0083 | +0.0161 | +1.3% |
| La Liga | btts_yes | half_life_240 | 24 | 0.2967 | 0.7919 | +0.0060 | +0.0124 | +0.4% |
| La Liga | btts_yes | half_life_365 | 24 | 0.2986 | 0.7958 | +0.0040 | +0.0085 | +0.0% |
| La Liga | btts_yes | half_life_730 | 24 | 0.3019 | 0.8026 | +0.0008 | +0.0016 | -0.4% |
| La Liga | btts_yes | production_raw | 24 | 0.3026 | 0.8043 | +0.0000 | +0.0000 | -0.3% |
| Ligue 1 | over_1_5 | development_1x2 | 21 | 0.1702 | 0.5161 | +0.0011 | +0.0046 | +2.3% |
| Ligue 1 | over_1_5 | goal_selected | 21 | 0.1727 | 0.5262 | -0.0014 | -0.0056 | +2.2% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 21 | 0.1727 | 0.5262 | -0.0014 | -0.0056 | +2.2% |
| Ligue 1 | over_1_5 | half_life_120 | 21 | 0.1800 | 0.5460 | -0.0088 | -0.0254 | +2.6% |
| Ligue 1 | over_1_5 | half_life_240 | 21 | 0.1755 | 0.5322 | -0.0043 | -0.0116 | +2.5% |
| Ligue 1 | over_1_5 | half_life_365 | 21 | 0.1737 | 0.5276 | -0.0025 | -0.0070 | +2.4% |
| Ligue 1 | over_1_5 | half_life_730 | 21 | 0.1723 | 0.5241 | -0.0010 | -0.0035 | +2.3% |
| Ligue 1 | over_1_5 | production_raw | 21 | 0.1712 | 0.5206 | +0.0000 | +0.0000 | +2.3% |
| Ligue 1 | btts_yes | development_1x2 | 21 | 0.2474 | 0.6887 | -0.0035 | -0.0071 | -7.5% |
| Ligue 1 | btts_yes | goal_selected | 21 | 0.2483 | 0.6906 | -0.0044 | -0.0090 | -7.5% |
| Ligue 1 | btts_yes | half_life_1000000000 | 21 | 0.2483 | 0.6906 | -0.0044 | -0.0090 | -7.5% |
| Ligue 1 | btts_yes | half_life_120 | 21 | 0.2384 | 0.6695 | +0.0054 | +0.0121 | -8.2% |
| Ligue 1 | btts_yes | half_life_240 | 21 | 0.2377 | 0.6686 | +0.0061 | +0.0129 | -8.0% |
| Ligue 1 | btts_yes | half_life_365 | 21 | 0.2402 | 0.6739 | +0.0037 | +0.0077 | -7.8% |
| Ligue 1 | btts_yes | half_life_730 | 21 | 0.2439 | 0.6816 | -0.0000 | -0.0000 | -7.7% |
| Ligue 1 | btts_yes | production_raw | 21 | 0.2438 | 0.6816 | +0.0000 | +0.0000 | -7.5% |
| Premier League | over_1_5 | development_1x2 | 29 | 0.1678 | 0.5130 | -0.0012 | -0.0029 | +1.3% |
| Premier League | over_1_5 | goal_selected | 29 | 0.1734 | 0.5288 | -0.0068 | -0.0188 | +1.4% |
| Premier League | over_1_5 | half_life_1000000000 | 29 | 0.1751 | 0.5332 | -0.0085 | -0.0231 | +1.4% |
| Premier League | over_1_5 | half_life_120 | 29 | 0.1622 | 0.5008 | +0.0044 | +0.0092 | +1.2% |
| Premier League | over_1_5 | half_life_240 | 29 | 0.1666 | 0.5101 | +0.0000 | +0.0000 | +1.4% |
| Premier League | over_1_5 | half_life_365 | 29 | 0.1692 | 0.5168 | -0.0026 | -0.0067 | +1.4% |
| Premier League | over_1_5 | half_life_730 | 29 | 0.1721 | 0.5248 | -0.0055 | -0.0147 | +1.4% |
| Premier League | over_1_5 | production_raw | 29 | 0.1666 | 0.5101 | +0.0000 | +0.0000 | +1.4% |
| Premier League | btts_yes | development_1x2 | 29 | 0.2754 | 0.7453 | +0.0010 | +0.0021 | +20.1% |
| Premier League | btts_yes | goal_selected | 29 | 0.2777 | 0.7497 | -0.0014 | -0.0023 | +19.7% |
| Premier League | btts_yes | half_life_1000000000 | 29 | 0.2779 | 0.7502 | -0.0015 | -0.0028 | +19.5% |
| Premier League | btts_yes | half_life_120 | 29 | 0.2786 | 0.7541 | -0.0023 | -0.0067 | +20.2% |
| Premier League | btts_yes | half_life_240 | 29 | 0.2763 | 0.7474 | +0.0000 | +0.0000 | +20.2% |
| Premier League | btts_yes | half_life_365 | 29 | 0.2769 | 0.7482 | -0.0005 | -0.0008 | +20.1% |
| Premier League | btts_yes | half_life_730 | 29 | 0.2777 | 0.7497 | -0.0014 | -0.0023 | +19.9% |
| Premier League | btts_yes | production_raw | 29 | 0.2763 | 0.7474 | +0.0000 | +0.0000 | +20.2% |
| Primeira Liga | over_1_5 | development_1x2 | 6 | 0.1570 | 0.4942 | +0.0003 | +0.0004 | -12.8% |
| Primeira Liga | over_1_5 | goal_selected | 6 | 0.1585 | 0.4961 | -0.0012 | -0.0015 | -11.6% |
| Primeira Liga | over_1_5 | half_life_1000000000 | 6 | 0.1570 | 0.4942 | +0.0003 | +0.0004 | -12.8% |
| Primeira Liga | over_1_5 | half_life_120 | 6 | 0.1372 | 0.4425 | +0.0201 | +0.0521 | -6.9% |
| Primeira Liga | over_1_5 | half_life_240 | 6 | 0.1488 | 0.4723 | +0.0085 | +0.0223 | -8.7% |
| Primeira Liga | over_1_5 | half_life_365 | 6 | 0.1539 | 0.4850 | +0.0034 | +0.0096 | -9.9% |
| Primeira Liga | over_1_5 | half_life_730 | 6 | 0.1585 | 0.4961 | -0.0012 | -0.0015 | -11.6% |
| Primeira Liga | over_1_5 | production_raw | 6 | 0.1573 | 0.4946 | +0.0000 | +0.0000 | -11.0% |
| Primeira Liga | btts_yes | development_1x2 | 6 | 0.2247 | 0.6423 | -0.0003 | -0.0005 | +29.6% |
| Primeira Liga | btts_yes | goal_selected | 6 | 0.2274 | 0.6478 | -0.0030 | -0.0059 | +29.9% |
| Primeira Liga | btts_yes | half_life_1000000000 | 6 | 0.2247 | 0.6423 | -0.0003 | -0.0005 | +29.6% |
| Primeira Liga | btts_yes | half_life_120 | 6 | 0.2288 | 0.6507 | -0.0044 | -0.0088 | +30.2% |
| Primeira Liga | btts_yes | half_life_240 | 6 | 0.2340 | 0.6610 | -0.0096 | -0.0191 | +30.6% |
| Primeira Liga | btts_yes | half_life_365 | 6 | 0.2318 | 0.6567 | -0.0074 | -0.0149 | +30.4% |
| Primeira Liga | btts_yes | half_life_730 | 6 | 0.2274 | 0.6478 | -0.0030 | -0.0059 | +29.9% |
| Primeira Liga | btts_yes | production_raw | 6 | 0.2244 | 0.6419 | +0.0000 | +0.0000 | +31.3% |
| Serie A | over_1_5 | development_1x2 | 33 | 0.1158 | 0.4015 | +0.0017 | +0.0035 | -17.9% |
| Serie A | over_1_5 | goal_selected | 33 | 0.1145 | 0.3957 | +0.0029 | +0.0093 | -16.8% |
| Serie A | over_1_5 | half_life_1000000000 | 33 | 0.1122 | 0.3919 | +0.0052 | +0.0131 | -18.0% |
| Serie A | over_1_5 | half_life_120 | 33 | 0.1212 | 0.4125 | -0.0038 | -0.0075 | -15.6% |
| Serie A | over_1_5 | half_life_240 | 33 | 0.1145 | 0.3957 | +0.0029 | +0.0093 | -16.8% |
| Serie A | over_1_5 | half_life_365 | 33 | 0.1124 | 0.3920 | +0.0050 | +0.0130 | -17.3% |
| Serie A | over_1_5 | half_life_730 | 33 | 0.1116 | 0.3908 | +0.0058 | +0.0141 | -17.7% |
| Serie A | over_1_5 | production_raw | 33 | 0.1174 | 0.4050 | +0.0000 | +0.0000 | -17.3% |
| Serie A | btts_yes | development_1x2 | 33 | 0.2299 | 0.6527 | +0.0044 | +0.0092 | -8.8% |
| Serie A | btts_yes | goal_selected | 33 | 0.2359 | 0.6659 | -0.0016 | -0.0039 | -8.3% |
| Serie A | btts_yes | half_life_1000000000 | 33 | 0.2269 | 0.6464 | +0.0074 | +0.0156 | -8.6% |
| Serie A | btts_yes | half_life_120 | 33 | 0.2447 | 0.6851 | -0.0104 | -0.0231 | -7.4% |
| Serie A | btts_yes | half_life_240 | 33 | 0.2389 | 0.6721 | -0.0046 | -0.0102 | -8.2% |
| Serie A | btts_yes | half_life_365 | 33 | 0.2353 | 0.6642 | -0.0010 | -0.0022 | -8.4% |
| Serie A | btts_yes | half_life_730 | 33 | 0.2309 | 0.6548 | +0.0034 | +0.0072 | -8.6% |
| Serie A | btts_yes | production_raw | 33 | 0.2343 | 0.6620 | +0.0000 | +0.0000 | -8.4% |
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