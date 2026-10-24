# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 378/416 fixture-markets; 172 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 86 | 0.1754 | 0.5937 | +0.0024 | +0.0037 | -2.3% |
| ALL | over_1_5 | goal_selected | 71 | 0.1851 | 0.6184 | -0.0036 | +0.0004 | -1.9% |
| ALL | over_1_5 | half_life_1000000000 | 86 | 0.1785 | 0.6031 | -0.0008 | -0.0057 | -2.6% |
| ALL | over_1_5 | half_life_120 | 86 | 0.1787 | 0.5977 | -0.0010 | -0.0003 | -1.9% |
| ALL | over_1_5 | half_life_240 | 86 | 0.1759 | 0.5769 | +0.0018 | +0.0205 | -2.2% |
| ALL | over_1_5 | half_life_365 | 86 | 0.1765 | 0.5843 | +0.0012 | +0.0130 | -2.3% |
| ALL | over_1_5 | half_life_730 | 86 | 0.1775 | 0.5947 | +0.0002 | +0.0027 | -2.4% |
| ALL | over_1_5 | production_raw | 86 | 0.1777 | 0.5974 | +0.0000 | +0.0000 | -2.3% |
| ALL | btts_yes | development_1x2 | 86 | 0.2601 | 0.7243 | +0.0024 | +0.0056 | -5.9% |
| ALL | btts_yes | goal_selected | 71 | 0.2576 | 0.7210 | -0.0005 | -0.0027 | -7.2% |
| ALL | btts_yes | half_life_1000000000 | 86 | 0.2630 | 0.7305 | -0.0005 | -0.0006 | -6.1% |
| ALL | btts_yes | half_life_120 | 86 | 0.2803 | 0.7852 | -0.0179 | -0.0553 | -5.5% |
| ALL | btts_yes | half_life_240 | 86 | 0.2682 | 0.7485 | -0.0057 | -0.0187 | -5.6% |
| ALL | btts_yes | half_life_365 | 86 | 0.2652 | 0.7395 | -0.0028 | -0.0096 | -5.7% |
| ALL | btts_yes | half_life_730 | 86 | 0.2634 | 0.7333 | -0.0010 | -0.0034 | -5.9% |
| ALL | btts_yes | production_raw | 86 | 0.2625 | 0.7299 | +0.0000 | +0.0000 | -5.9% |
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
| La Liga | over_1_5 | development_1x2 | 10 | 0.2012 | 0.5884 | +0.0033 | +0.0076 | -3.3% |
| La Liga | over_1_5 | goal_selected | 10 | 0.1936 | 0.5707 | +0.0108 | +0.0252 | -1.4% |
| La Liga | over_1_5 | half_life_1000000000 | 10 | 0.2078 | 0.6041 | -0.0034 | -0.0082 | -4.4% |
| La Liga | over_1_5 | half_life_120 | 10 | 0.1936 | 0.5707 | +0.0108 | +0.0252 | -1.4% |
| La Liga | over_1_5 | half_life_240 | 10 | 0.1983 | 0.5820 | +0.0061 | +0.0139 | -2.8% |
| La Liga | over_1_5 | half_life_365 | 10 | 0.2012 | 0.5884 | +0.0033 | +0.0076 | -3.3% |
| La Liga | over_1_5 | half_life_730 | 10 | 0.2045 | 0.5959 | +0.0000 | +0.0000 | -3.9% |
| La Liga | over_1_5 | production_raw | 10 | 0.2045 | 0.5959 | +0.0000 | +0.0000 | -3.9% |
| La Liga | btts_yes | development_1x2 | 10 | 0.3197 | 0.8435 | +0.0045 | +0.0097 | -16.3% |
| La Liga | btts_yes | goal_selected | 10 | 0.3164 | 0.8368 | +0.0078 | +0.0164 | -15.8% |
| La Liga | btts_yes | half_life_1000000000 | 10 | 0.3296 | 0.8656 | -0.0055 | -0.0124 | -17.2% |
| La Liga | btts_yes | half_life_120 | 10 | 0.3126 | 0.8319 | +0.0116 | +0.0213 | -14.2% |
| La Liga | btts_yes | half_life_240 | 10 | 0.3164 | 0.8368 | +0.0078 | +0.0164 | -15.8% |
| La Liga | btts_yes | half_life_365 | 10 | 0.3197 | 0.8435 | +0.0045 | +0.0097 | -16.3% |
| La Liga | btts_yes | half_life_730 | 10 | 0.3242 | 0.8532 | +0.0000 | +0.0000 | -16.8% |
| La Liga | btts_yes | production_raw | 10 | 0.3242 | 0.8532 | +0.0000 | +0.0000 | -16.8% |
| Ligue 1 | over_1_5 | development_1x2 | 7 | 0.1302 | 0.4263 | +0.0111 | +0.0380 | -6.5% |
| Ligue 1 | over_1_5 | goal_selected | 7 | 0.1483 | 0.4895 | -0.0070 | -0.0251 | -6.9% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 7 | 0.1483 | 0.4895 | -0.0070 | -0.0251 | -6.9% |
| Ligue 1 | over_1_5 | half_life_120 | 7 | 0.1173 | 0.3862 | +0.0240 | +0.0781 | -6.7% |
| Ligue 1 | over_1_5 | half_life_240 | 7 | 0.1302 | 0.4263 | +0.0111 | +0.0380 | -6.5% |
| Ligue 1 | over_1_5 | half_life_365 | 7 | 0.1353 | 0.4437 | +0.0059 | +0.0207 | -6.6% |
| Ligue 1 | over_1_5 | half_life_730 | 7 | 0.1413 | 0.4643 | +0.0000 | +0.0000 | -6.7% |
| Ligue 1 | over_1_5 | production_raw | 7 | 0.1413 | 0.4643 | +0.0000 | +0.0000 | -6.7% |
| Ligue 1 | btts_yes | development_1x2 | 7 | 0.2787 | 0.7528 | +0.0048 | +0.0096 | -15.7% |
| Ligue 1 | btts_yes | goal_selected | 7 | 0.2890 | 0.7741 | -0.0055 | -0.0117 | -15.9% |
| Ligue 1 | btts_yes | half_life_1000000000 | 7 | 0.2890 | 0.7741 | -0.0055 | -0.0117 | -15.9% |
| Ligue 1 | btts_yes | half_life_120 | 7 | 0.2790 | 0.7554 | +0.0045 | +0.0071 | -16.1% |
| Ligue 1 | btts_yes | half_life_240 | 7 | 0.2787 | 0.7528 | +0.0048 | +0.0096 | -15.7% |
| Ligue 1 | btts_yes | half_life_365 | 7 | 0.2802 | 0.7557 | +0.0032 | +0.0067 | -15.6% |
| Ligue 1 | btts_yes | half_life_730 | 7 | 0.2835 | 0.7624 | +0.0000 | +0.0000 | -15.7% |
| Ligue 1 | btts_yes | production_raw | 7 | 0.2835 | 0.7624 | +0.0000 | +0.0000 | -15.7% |
| Premier League | over_1_5 | development_1x2 | 11 | 0.1813 | 0.5444 | -0.0031 | -0.0072 | +5.1% |
| Premier League | over_1_5 | goal_selected | 11 | 0.1902 | 0.5695 | -0.0121 | -0.0324 | +4.9% |
| Premier League | over_1_5 | half_life_1000000000 | 11 | 0.1902 | 0.5695 | -0.0121 | -0.0324 | +4.9% |
| Premier League | over_1_5 | half_life_120 | 11 | 0.1761 | 0.5403 | +0.0020 | -0.0031 | +5.4% |
| Premier League | over_1_5 | half_life_240 | 11 | 0.1781 | 0.5372 | +0.0000 | +0.0000 | +5.3% |
| Premier League | over_1_5 | half_life_365 | 11 | 0.1813 | 0.5444 | -0.0031 | -0.0072 | +5.1% |
| Premier League | over_1_5 | half_life_730 | 11 | 0.1854 | 0.5554 | -0.0073 | -0.0183 | +5.0% |
| Premier League | over_1_5 | production_raw | 11 | 0.1781 | 0.5372 | +0.0000 | +0.0000 | +5.3% |
| Premier League | btts_yes | development_1x2 | 11 | 0.2470 | 0.6877 | +0.0014 | +0.0030 | +8.9% |
| Premier League | btts_yes | goal_selected | 11 | 0.2476 | 0.6889 | +0.0008 | +0.0018 | +8.6% |
| Premier League | btts_yes | half_life_1000000000 | 11 | 0.2499 | 0.6939 | -0.0015 | -0.0031 | +8.2% |
| Premier League | btts_yes | half_life_120 | 11 | 0.2625 | 0.7213 | -0.0141 | -0.0305 | +9.3% |
| Premier League | btts_yes | half_life_240 | 11 | 0.2484 | 0.6908 | +0.0000 | +0.0000 | +9.2% |
| Premier League | btts_yes | half_life_365 | 11 | 0.2470 | 0.6877 | +0.0014 | +0.0030 | +8.9% |
| Premier League | btts_yes | half_life_730 | 11 | 0.2476 | 0.6889 | +0.0008 | +0.0018 | +8.6% |
| Premier League | btts_yes | production_raw | 11 | 0.2484 | 0.6908 | +0.0000 | +0.0000 | +9.2% |
| Serie A | over_1_5 | development_1x2 | 11 | 0.1267 | 0.4303 | +0.0038 | +0.0100 | -18.4% |
| Serie A | over_1_5 | goal_selected | 11 | 0.1305 | 0.4403 | +0.0000 | +0.0000 | -17.7% |
| Serie A | over_1_5 | half_life_1000000000 | 11 | 0.1247 | 0.4239 | +0.0058 | +0.0164 | -19.5% |
| Serie A | over_1_5 | half_life_120 | 11 | 0.1427 | 0.4791 | -0.0122 | -0.0388 | -16.2% |
| Serie A | over_1_5 | half_life_240 | 11 | 0.1305 | 0.4403 | +0.0000 | +0.0000 | -17.7% |
| Serie A | over_1_5 | half_life_365 | 11 | 0.1267 | 0.4303 | +0.0038 | +0.0100 | -18.4% |
| Serie A | over_1_5 | half_life_730 | 11 | 0.1246 | 0.4249 | +0.0059 | +0.0155 | -19.0% |
| Serie A | over_1_5 | production_raw | 11 | 0.1305 | 0.4403 | +0.0000 | +0.0000 | -17.7% |
| Serie A | btts_yes | development_1x2 | 11 | 0.1997 | 0.5918 | -0.0007 | -0.0015 | +12.6% |
| Serie A | btts_yes | goal_selected | 11 | 0.2015 | 0.5952 | -0.0025 | -0.0049 | +12.5% |
| Serie A | btts_yes | half_life_1000000000 | 11 | 0.2042 | 0.6004 | -0.0052 | -0.0102 | +12.4% |
| Serie A | btts_yes | half_life_120 | 11 | 0.1970 | 0.5847 | +0.0020 | +0.0055 | +13.3% |
| Serie A | btts_yes | half_life_240 | 11 | 0.1990 | 0.5903 | +0.0000 | +0.0000 | +12.8% |
| Serie A | btts_yes | half_life_365 | 11 | 0.1997 | 0.5918 | -0.0007 | -0.0015 | +12.6% |
| Serie A | btts_yes | half_life_730 | 11 | 0.2015 | 0.5952 | -0.0025 | -0.0049 | +12.5% |
| Serie A | btts_yes | production_raw | 11 | 0.1990 | 0.5903 | +0.0000 | +0.0000 | +12.8% |
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