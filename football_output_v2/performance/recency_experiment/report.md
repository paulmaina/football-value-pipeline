# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 378/416 fixture-markets; 168 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 84 | 0.1782 | 0.6022 | +0.0022 | +0.0033 | -1.9% |
| ALL | over_1_5 | goal_selected | 69 | 0.1887 | 0.6290 | -0.0037 | +0.0004 | -1.3% |
| ALL | over_1_5 | half_life_1000000000 | 84 | 0.1817 | 0.6123 | -0.0012 | -0.0068 | -2.3% |
| ALL | over_1_5 | half_life_120 | 84 | 0.1809 | 0.6046 | -0.0004 | +0.0009 | -1.3% |
| ALL | over_1_5 | half_life_240 | 84 | 0.1786 | 0.5846 | +0.0019 | +0.0209 | -1.7% |
| ALL | over_1_5 | half_life_365 | 84 | 0.1794 | 0.5926 | +0.0010 | +0.0129 | -1.9% |
| ALL | over_1_5 | half_life_730 | 84 | 0.1806 | 0.6035 | -0.0002 | +0.0020 | -2.0% |
| ALL | over_1_5 | production_raw | 84 | 0.1805 | 0.6055 | +0.0000 | +0.0000 | -1.9% |
| ALL | btts_yes | development_1x2 | 84 | 0.2628 | 0.7303 | +0.0026 | +0.0061 | -6.3% |
| ALL | btts_yes | goal_selected | 69 | 0.2606 | 0.7278 | -0.0001 | -0.0020 | -7.7% |
| ALL | btts_yes | half_life_1000000000 | 84 | 0.2655 | 0.7361 | -0.0001 | +0.0003 | -6.6% |
| ALL | btts_yes | half_life_120 | 84 | 0.2844 | 0.7944 | -0.0190 | -0.0580 | -5.8% |
| ALL | btts_yes | half_life_240 | 84 | 0.2713 | 0.7556 | -0.0059 | -0.0192 | -6.0% |
| ALL | btts_yes | half_life_365 | 84 | 0.2681 | 0.7459 | -0.0027 | -0.0095 | -6.1% |
| ALL | btts_yes | half_life_730 | 84 | 0.2661 | 0.7392 | -0.0006 | -0.0028 | -6.3% |
| ALL | btts_yes | production_raw | 84 | 0.2654 | 0.7364 | +0.0000 | +0.0000 | -6.3% |
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
| La Liga | over_1_5 | development_1x2 | 9 | 0.2226 | 0.6430 | +0.0036 | +0.0082 | -2.7% |
| La Liga | over_1_5 | goal_selected | 9 | 0.2143 | 0.6238 | +0.0119 | +0.0274 | -0.5% |
| La Liga | over_1_5 | half_life_1000000000 | 9 | 0.2299 | 0.6602 | -0.0037 | -0.0090 | -3.8% |
| La Liga | over_1_5 | half_life_120 | 9 | 0.2143 | 0.6238 | +0.0119 | +0.0274 | -0.5% |
| La Liga | over_1_5 | half_life_240 | 9 | 0.2195 | 0.6361 | +0.0067 | +0.0152 | -2.0% |
| La Liga | over_1_5 | half_life_365 | 9 | 0.2226 | 0.6430 | +0.0036 | +0.0082 | -2.7% |
| La Liga | over_1_5 | half_life_730 | 9 | 0.2262 | 0.6512 | +0.0000 | +0.0000 | -3.3% |
| La Liga | over_1_5 | production_raw | 9 | 0.2262 | 0.6512 | +0.0000 | +0.0000 | -3.3% |
| La Liga | btts_yes | development_1x2 | 9 | 0.3481 | 0.9046 | +0.0048 | +0.0105 | -15.3% |
| La Liga | btts_yes | goal_selected | 9 | 0.3445 | 0.8974 | +0.0084 | +0.0177 | -14.7% |
| La Liga | btts_yes | half_life_1000000000 | 9 | 0.3588 | 0.9285 | -0.0059 | -0.0134 | -16.2% |
| La Liga | btts_yes | half_life_120 | 9 | 0.3403 | 0.8923 | +0.0126 | +0.0228 | -13.0% |
| La Liga | btts_yes | half_life_240 | 9 | 0.3445 | 0.8974 | +0.0084 | +0.0177 | -14.7% |
| La Liga | btts_yes | half_life_365 | 9 | 0.3481 | 0.9046 | +0.0048 | +0.0105 | -15.3% |
| La Liga | btts_yes | half_life_730 | 9 | 0.3529 | 0.9151 | +0.0000 | +0.0000 | -15.8% |
| La Liga | btts_yes | production_raw | 9 | 0.3529 | 0.9151 | +0.0000 | +0.0000 | -15.8% |
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
| Serie A | over_1_5 | development_1x2 | 10 | 0.1294 | 0.4355 | +0.0026 | +0.0075 | -17.0% |
| Serie A | over_1_5 | goal_selected | 10 | 0.1320 | 0.4429 | +0.0000 | +0.0000 | -16.1% |
| Serie A | over_1_5 | half_life_1000000000 | 10 | 0.1293 | 0.4334 | +0.0028 | +0.0095 | -18.6% |
| Serie A | over_1_5 | half_life_120 | 10 | 0.1404 | 0.4748 | -0.0084 | -0.0319 | -13.8% |
| Serie A | over_1_5 | half_life_240 | 10 | 0.1320 | 0.4429 | +0.0000 | +0.0000 | -16.1% |
| Serie A | over_1_5 | half_life_365 | 10 | 0.1294 | 0.4355 | +0.0026 | +0.0075 | -17.0% |
| Serie A | over_1_5 | half_life_730 | 10 | 0.1284 | 0.4324 | +0.0037 | +0.0106 | -17.9% |
| Serie A | over_1_5 | production_raw | 10 | 0.1320 | 0.4429 | +0.0000 | +0.0000 | -16.1% |
| Serie A | btts_yes | development_1x2 | 10 | 0.1968 | 0.5860 | +0.0010 | +0.0019 | +9.1% |
| Serie A | btts_yes | goal_selected | 10 | 0.1974 | 0.5870 | +0.0004 | +0.0009 | +8.8% |
| Serie A | btts_yes | half_life_1000000000 | 10 | 0.1997 | 0.5914 | -0.0019 | -0.0035 | +8.7% |
| Serie A | btts_yes | half_life_120 | 10 | 0.2009 | 0.5927 | -0.0031 | -0.0048 | +10.6% |
| Serie A | btts_yes | half_life_240 | 10 | 0.1978 | 0.5879 | +0.0000 | +0.0000 | +9.5% |
| Serie A | btts_yes | half_life_365 | 10 | 0.1968 | 0.5860 | +0.0010 | +0.0019 | +9.1% |
| Serie A | btts_yes | half_life_730 | 10 | 0.1974 | 0.5870 | +0.0004 | +0.0009 | +8.8% |
| Serie A | btts_yes | production_raw | 10 | 0.1978 | 0.5879 | +0.0000 | +0.0000 | +9.5% |
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