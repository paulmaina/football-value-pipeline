> **ARCHIVED 2026-11-02.** No longer generated, captured or reviewed. This is the last report, frozen as committed; the code is kept for replay in `archive/recency_experiment.py`.

# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 556/598 fixture-markets; 404 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 202 | 0.1566 | 0.5125 | +0.0009 | +0.0013 | -3.8% |
| ALL | over_1_5 | goal_selected | 187 | 0.1577 | 0.5111 | -0.0004 | +0.0042 | -3.5% |
| ALL | over_1_5 | half_life_1000000000 | 202 | 0.1580 | 0.5172 | -0.0005 | -0.0034 | -4.1% |
| ALL | over_1_5 | half_life_120 | 202 | 0.1575 | 0.5098 | +0.0000 | +0.0040 | -3.0% |
| ALL | over_1_5 | half_life_240 | 202 | 0.1567 | 0.5038 | +0.0009 | +0.0100 | -3.4% |
| ALL | over_1_5 | half_life_365 | 202 | 0.1568 | 0.5076 | +0.0007 | +0.0062 | -3.6% |
| ALL | over_1_5 | half_life_730 | 202 | 0.1574 | 0.5130 | +0.0002 | +0.0008 | -3.8% |
| ALL | over_1_5 | production_raw | 202 | 0.1575 | 0.5138 | +0.0000 | +0.0000 | -3.7% |
| ALL | btts_yes | development_1x2 | 202 | 0.2616 | 0.7271 | +0.0013 | +0.0027 | +1.1% |
| ALL | btts_yes | goal_selected | 187 | 0.2604 | 0.7259 | +0.0004 | -0.0006 | +1.4% |
| ALL | btts_yes | half_life_1000000000 | 202 | 0.2613 | 0.7260 | +0.0016 | +0.0038 | +0.6% |
| ALL | btts_yes | half_life_120 | 202 | 0.2703 | 0.7547 | -0.0073 | -0.0249 | +1.7% |
| ALL | btts_yes | half_life_240 | 202 | 0.2648 | 0.7375 | -0.0019 | -0.0076 | +1.5% |
| ALL | btts_yes | half_life_365 | 202 | 0.2634 | 0.7326 | -0.0005 | -0.0028 | +1.3% |
| ALL | btts_yes | half_life_730 | 202 | 0.2621 | 0.7285 | +0.0008 | +0.0013 | +1.0% |
| ALL | btts_yes | production_raw | 202 | 0.2629 | 0.7298 | +0.0000 | +0.0000 | +1.1% |
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
| Ligue 1 | over_1_5 | development_1x2 | 23 | 0.1589 | 0.4908 | +0.0006 | +0.0029 | +0.3% |
| Ligue 1 | over_1_5 | goal_selected | 23 | 0.1612 | 0.5000 | -0.0017 | -0.0064 | +0.3% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 23 | 0.1612 | 0.5000 | -0.0017 | -0.0064 | +0.3% |
| Ligue 1 | over_1_5 | half_life_120 | 23 | 0.1660 | 0.5112 | -0.0065 | -0.0176 | +1.2% |
| Ligue 1 | over_1_5 | half_life_240 | 23 | 0.1625 | 0.5012 | -0.0030 | -0.0075 | +0.9% |
| Ligue 1 | over_1_5 | half_life_365 | 23 | 0.1612 | 0.4981 | -0.0017 | -0.0045 | +0.7% |
| Ligue 1 | over_1_5 | half_life_730 | 23 | 0.1603 | 0.4964 | -0.0008 | -0.0028 | +0.5% |
| Ligue 1 | over_1_5 | production_raw | 23 | 0.1595 | 0.4936 | +0.0000 | +0.0000 | +0.4% |
| Ligue 1 | btts_yes | development_1x2 | 23 | 0.2529 | 0.6997 | -0.0014 | -0.0027 | -2.0% |
| Ligue 1 | btts_yes | goal_selected | 23 | 0.2537 | 0.7015 | -0.0022 | -0.0045 | -2.0% |
| Ligue 1 | btts_yes | half_life_1000000000 | 23 | 0.2537 | 0.7015 | -0.0022 | -0.0045 | -2.0% |
| Ligue 1 | btts_yes | half_life_120 | 23 | 0.2555 | 0.7050 | -0.0040 | -0.0080 | -1.7% |
| Ligue 1 | btts_yes | half_life_240 | 23 | 0.2506 | 0.6950 | +0.0009 | +0.0020 | -1.9% |
| Ligue 1 | btts_yes | half_life_365 | 23 | 0.2509 | 0.6957 | +0.0006 | +0.0013 | -1.9% |
| Ligue 1 | btts_yes | half_life_730 | 23 | 0.2521 | 0.6981 | -0.0006 | -0.0011 | -1.9% |
| Ligue 1 | btts_yes | production_raw | 23 | 0.2515 | 0.6970 | +0.0000 | +0.0000 | -1.9% |
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
| Primeira Liga | over_1_5 | development_1x2 | 8 | 0.1335 | 0.4430 | +0.0058 | +0.0144 | -15.9% |
| Primeira Liga | over_1_5 | goal_selected | 8 | 0.1386 | 0.4545 | +0.0008 | +0.0029 | -15.7% |
| Primeira Liga | over_1_5 | half_life_1000000000 | 8 | 0.1335 | 0.4430 | +0.0058 | +0.0144 | -15.9% |
| Primeira Liga | over_1_5 | half_life_120 | 8 | 0.1294 | 0.4303 | +0.0099 | +0.0270 | -13.3% |
| Primeira Liga | over_1_5 | half_life_240 | 8 | 0.1368 | 0.4497 | +0.0026 | +0.0077 | -14.4% |
| Primeira Liga | over_1_5 | half_life_365 | 8 | 0.1385 | 0.4543 | +0.0008 | +0.0031 | -15.1% |
| Primeira Liga | over_1_5 | half_life_730 | 8 | 0.1386 | 0.4545 | +0.0008 | +0.0029 | -15.7% |
| Primeira Liga | over_1_5 | production_raw | 8 | 0.1393 | 0.4574 | +0.0000 | +0.0000 | -15.6% |
| Primeira Liga | btts_yes | development_1x2 | 8 | 0.2288 | 0.6506 | -0.0028 | -0.0055 | +34.5% |
| Primeira Liga | btts_yes | goal_selected | 8 | 0.2288 | 0.6507 | -0.0028 | -0.0056 | +34.5% |
| Primeira Liga | btts_yes | half_life_1000000000 | 8 | 0.2288 | 0.6506 | -0.0028 | -0.0055 | +34.5% |
| Primeira Liga | btts_yes | half_life_120 | 8 | 0.2272 | 0.6475 | -0.0012 | -0.0024 | +34.4% |
| Primeira Liga | btts_yes | half_life_240 | 8 | 0.2310 | 0.6550 | -0.0050 | -0.0099 | +34.8% |
| Primeira Liga | btts_yes | half_life_365 | 8 | 0.2303 | 0.6537 | -0.0043 | -0.0086 | +34.7% |
| Primeira Liga | btts_yes | half_life_730 | 8 | 0.2288 | 0.6507 | -0.0028 | -0.0056 | +34.5% |
| Primeira Liga | btts_yes | production_raw | 8 | 0.2260 | 0.6451 | +0.0000 | +0.0000 | +35.5% |
| Serie A | over_1_5 | development_1x2 | 34 | 0.1160 | 0.4024 | +0.0015 | +0.0031 | -18.4% |
| Serie A | over_1_5 | goal_selected | 34 | 0.1146 | 0.3964 | +0.0029 | +0.0091 | -17.3% |
| Serie A | over_1_5 | half_life_1000000000 | 34 | 0.1126 | 0.3931 | +0.0049 | +0.0124 | -18.5% |
| Serie A | over_1_5 | half_life_120 | 34 | 0.1211 | 0.4126 | -0.0036 | -0.0071 | -16.2% |
| Serie A | over_1_5 | half_life_240 | 34 | 0.1146 | 0.3964 | +0.0029 | +0.0091 | -17.3% |
| Serie A | over_1_5 | half_life_365 | 34 | 0.1126 | 0.3928 | +0.0049 | +0.0127 | -17.8% |
| Serie A | over_1_5 | half_life_730 | 34 | 0.1119 | 0.3919 | +0.0056 | +0.0136 | -18.2% |
| Serie A | over_1_5 | production_raw | 34 | 0.1175 | 0.4055 | +0.0000 | +0.0000 | -17.8% |
| Serie A | btts_yes | development_1x2 | 34 | 0.2290 | 0.6510 | +0.0045 | +0.0093 | -7.2% |
| Serie A | btts_yes | goal_selected | 34 | 0.2351 | 0.6643 | -0.0017 | -0.0040 | -6.7% |
| Serie A | btts_yes | half_life_1000000000 | 34 | 0.2261 | 0.6448 | +0.0074 | +0.0155 | -7.1% |
| Serie A | btts_yes | half_life_120 | 34 | 0.2435 | 0.6827 | -0.0101 | -0.0224 | -5.8% |
| Serie A | btts_yes | half_life_240 | 34 | 0.2380 | 0.6703 | -0.0045 | -0.0100 | -6.6% |
| Serie A | btts_yes | half_life_365 | 34 | 0.2345 | 0.6625 | -0.0010 | -0.0022 | -6.9% |
| Serie A | btts_yes | half_life_730 | 34 | 0.2302 | 0.6532 | +0.0033 | +0.0070 | -7.0% |
| Serie A | btts_yes | production_raw | 34 | 0.2335 | 0.6603 | +0.0000 | +0.0000 | -6.8% |
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