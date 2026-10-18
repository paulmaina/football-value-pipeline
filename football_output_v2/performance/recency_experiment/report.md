# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 268/284 fixture-markets; 86 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 43 | 0.1700 | 0.5174 | +0.0012 | +0.0043 | +0.4% |
| ALL | over_1_5 | goal_selected | 28 | 0.1831 | 0.5494 | -0.0056 | -0.0139 | +4.2% |
| ALL | over_1_5 | half_life_1000000000 | 43 | 0.1714 | 0.5224 | -0.0002 | -0.0008 | -0.2% |
| ALL | over_1_5 | half_life_120 | 43 | 0.1747 | 0.5464 | -0.0035 | -0.0247 | +2.7% |
| ALL | over_1_5 | half_life_240 | 43 | 0.1720 | 0.5286 | -0.0008 | -0.0069 | +1.3% |
| ALL | over_1_5 | half_life_365 | 43 | 0.1713 | 0.5245 | -0.0001 | -0.0029 | +0.7% |
| ALL | over_1_5 | half_life_730 | 43 | 0.1712 | 0.5228 | -0.0000 | -0.0011 | +0.2% |
| ALL | over_1_5 | production_raw | 43 | 0.1712 | 0.5216 | +0.0000 | +0.0000 | +0.5% |
| ALL | btts_yes | development_1x2 | 43 | 0.2609 | 0.7220 | +0.0007 | +0.0014 | +3.7% |
| ALL | btts_yes | goal_selected | 28 | 0.2466 | 0.6889 | +0.0009 | +0.0015 | +5.1% |
| ALL | btts_yes | half_life_1000000000 | 43 | 0.2622 | 0.7244 | -0.0005 | -0.0010 | +3.3% |
| ALL | btts_yes | half_life_120 | 43 | 0.2765 | 0.7590 | -0.0149 | -0.0356 | +4.5% |
| ALL | btts_yes | half_life_240 | 43 | 0.2661 | 0.7338 | -0.0045 | -0.0104 | +3.8% |
| ALL | btts_yes | half_life_365 | 43 | 0.2622 | 0.7252 | -0.0005 | -0.0018 | +3.7% |
| ALL | btts_yes | half_life_730 | 43 | 0.2610 | 0.7221 | +0.0007 | +0.0013 | +3.5% |
| ALL | btts_yes | production_raw | 43 | 0.2616 | 0.7234 | +0.0000 | +0.0000 | +3.7% |
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
| La Liga | over_1_5 | development_1x2 | 5 | 0.2722 | 0.7618 | -0.0007 | +0.0001 | +25.2% |
| La Liga | over_1_5 | goal_selected | 5 | 0.2768 | 0.7686 | -0.0052 | -0.0066 | +26.5% |
| La Liga | over_1_5 | half_life_1000000000 | 5 | 0.2720 | 0.7651 | -0.0004 | -0.0032 | +24.9% |
| La Liga | over_1_5 | half_life_120 | 5 | 0.2768 | 0.7686 | -0.0052 | -0.0066 | +26.5% |
| La Liga | over_1_5 | half_life_240 | 5 | 0.2736 | 0.7638 | -0.0020 | -0.0018 | +25.5% |
| La Liga | over_1_5 | half_life_365 | 5 | 0.2722 | 0.7618 | -0.0007 | +0.0001 | +25.2% |
| La Liga | over_1_5 | half_life_730 | 5 | 0.2716 | 0.7620 | +0.0000 | +0.0000 | +25.0% |
| La Liga | over_1_5 | production_raw | 5 | 0.2716 | 0.7620 | +0.0000 | +0.0000 | +25.0% |
| La Liga | btts_yes | development_1x2 | 5 | 0.2931 | 0.7908 | -0.0004 | -0.0017 | +23.7% |
| La Liga | btts_yes | goal_selected | 5 | 0.2956 | 0.7974 | -0.0029 | -0.0083 | +24.1% |
| La Liga | btts_yes | half_life_1000000000 | 5 | 0.2948 | 0.7935 | -0.0022 | -0.0044 | +23.5% |
| La Liga | btts_yes | half_life_120 | 5 | 0.3055 | 0.8253 | -0.0128 | -0.0362 | +25.6% |
| La Liga | btts_yes | half_life_240 | 5 | 0.2956 | 0.7974 | -0.0029 | -0.0083 | +24.1% |
| La Liga | btts_yes | half_life_365 | 5 | 0.2931 | 0.7908 | -0.0004 | -0.0017 | +23.7% |
| La Liga | btts_yes | half_life_730 | 5 | 0.2927 | 0.7891 | +0.0000 | +0.0000 | +23.5% |
| La Liga | btts_yes | production_raw | 5 | 0.2927 | 0.7891 | +0.0000 | +0.0000 | +23.5% |
| Ligue 1 | over_1_5 | development_1x2 | 4 | 0.0328 | 0.1946 | +0.0053 | +0.0182 | -17.6% |
| Ligue 1 | over_1_5 | goal_selected | 4 | 0.0413 | 0.2224 | -0.0033 | -0.0096 | -19.8% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 4 | 0.0413 | 0.2224 | -0.0033 | -0.0096 | -19.8% |
| Ligue 1 | over_1_5 | half_life_120 | 4 | 0.0296 | 0.1778 | +0.0084 | +0.0350 | -16.1% |
| Ligue 1 | over_1_5 | half_life_240 | 4 | 0.0328 | 0.1946 | +0.0053 | +0.0182 | -17.6% |
| Ligue 1 | over_1_5 | half_life_365 | 4 | 0.0351 | 0.2033 | +0.0029 | +0.0095 | -18.3% |
| Ligue 1 | over_1_5 | half_life_730 | 4 | 0.0380 | 0.2128 | +0.0000 | +0.0000 | -19.1% |
| Ligue 1 | over_1_5 | production_raw | 4 | 0.0380 | 0.2128 | +0.0000 | +0.0000 | -19.1% |
| Ligue 1 | btts_yes | development_1x2 | 4 | 0.2840 | 0.7647 | +0.0011 | +0.0013 | -18.2% |
| Ligue 1 | btts_yes | goal_selected | 4 | 0.2885 | 0.7728 | -0.0034 | -0.0068 | -20.2% |
| Ligue 1 | btts_yes | half_life_1000000000 | 4 | 0.2885 | 0.7728 | -0.0034 | -0.0068 | -20.2% |
| Ligue 1 | btts_yes | half_life_120 | 4 | 0.2918 | 0.7840 | -0.0067 | -0.0181 | -16.4% |
| Ligue 1 | btts_yes | half_life_240 | 4 | 0.2840 | 0.7647 | +0.0011 | +0.0013 | -18.2% |
| Ligue 1 | btts_yes | half_life_365 | 4 | 0.2837 | 0.7634 | +0.0014 | +0.0025 | -18.9% |
| Ligue 1 | btts_yes | half_life_730 | 4 | 0.2851 | 0.7660 | +0.0000 | +0.0000 | -19.6% |
| Ligue 1 | btts_yes | production_raw | 4 | 0.2851 | 0.7660 | +0.0000 | +0.0000 | -19.6% |
| Premier League | over_1_5 | development_1x2 | 8 | 0.1763 | 0.5368 | -0.0033 | -0.0076 | +4.1% |
| Premier League | over_1_5 | goal_selected | 8 | 0.1851 | 0.5629 | -0.0121 | -0.0336 | +3.3% |
| Premier League | over_1_5 | half_life_1000000000 | 8 | 0.1851 | 0.5629 | -0.0121 | -0.0336 | +3.3% |
| Premier League | over_1_5 | half_life_120 | 8 | 0.1702 | 0.5338 | +0.0028 | -0.0045 | +5.5% |
| Premier League | over_1_5 | half_life_240 | 8 | 0.1730 | 0.5292 | +0.0000 | +0.0000 | +4.5% |
| Premier League | over_1_5 | half_life_365 | 8 | 0.1763 | 0.5368 | -0.0033 | -0.0076 | +4.1% |
| Premier League | over_1_5 | half_life_730 | 8 | 0.1805 | 0.5485 | -0.0075 | -0.0192 | +3.7% |
| Premier League | over_1_5 | production_raw | 8 | 0.1730 | 0.5292 | +0.0000 | +0.0000 | +4.5% |
| Premier League | btts_yes | development_1x2 | 8 | 0.2652 | 0.7245 | +0.0028 | +0.0059 | +18.0% |
| Premier League | btts_yes | goal_selected | 8 | 0.2649 | 0.7239 | +0.0031 | +0.0066 | +17.5% |
| Premier League | btts_yes | half_life_1000000000 | 8 | 0.2668 | 0.7282 | +0.0011 | +0.0023 | +17.1% |
| Premier League | btts_yes | half_life_120 | 8 | 0.2863 | 0.7707 | -0.0183 | -0.0402 | +19.1% |
| Premier League | btts_yes | half_life_240 | 8 | 0.2680 | 0.7305 | +0.0000 | +0.0000 | +18.4% |
| Premier League | btts_yes | half_life_365 | 8 | 0.2652 | 0.7245 | +0.0028 | +0.0059 | +18.0% |
| Premier League | btts_yes | half_life_730 | 8 | 0.2649 | 0.7239 | +0.0031 | +0.0066 | +17.5% |
| Premier League | btts_yes | production_raw | 8 | 0.2680 | 0.7305 | +0.0000 | +0.0000 | +18.4% |
| Serie A | over_1_5 | development_1x2 | 5 | 0.1693 | 0.5197 | +0.0076 | +0.0237 | -4.7% |
| Serie A | over_1_5 | goal_selected | 5 | 0.1769 | 0.5434 | +0.0000 | +0.0000 | -3.4% |
| Serie A | over_1_5 | half_life_1000000000 | 5 | 0.1607 | 0.4959 | +0.0162 | +0.0474 | -6.5% |
| Serie A | over_1_5 | half_life_120 | 5 | 0.1938 | 0.6168 | -0.0168 | -0.0735 | -0.0% |
| Serie A | over_1_5 | half_life_240 | 5 | 0.1769 | 0.5434 | +0.0000 | +0.0000 | -3.4% |
| Serie A | over_1_5 | half_life_365 | 5 | 0.1693 | 0.5197 | +0.0076 | +0.0237 | -4.7% |
| Serie A | over_1_5 | half_life_730 | 5 | 0.1637 | 0.5040 | +0.0132 | +0.0394 | -5.7% |
| Serie A | over_1_5 | production_raw | 5 | 0.1769 | 0.5434 | +0.0000 | +0.0000 | -3.4% |
| Serie A | btts_yes | development_1x2 | 5 | 0.1758 | 0.5434 | +0.0031 | +0.0064 | +9.0% |
| Serie A | btts_yes | goal_selected | 5 | 0.1756 | 0.5427 | +0.0034 | +0.0071 | +9.1% |
| Serie A | btts_yes | half_life_1000000000 | 5 | 0.1790 | 0.5494 | -0.0001 | +0.0005 | +9.2% |
| Serie A | btts_yes | half_life_120 | 5 | 0.1880 | 0.5678 | -0.0090 | -0.0180 | +9.6% |
| Serie A | btts_yes | half_life_240 | 5 | 0.1789 | 0.5498 | +0.0000 | +0.0000 | +9.1% |
| Serie A | btts_yes | half_life_365 | 5 | 0.1758 | 0.5434 | +0.0031 | +0.0064 | +9.0% |
| Serie A | btts_yes | half_life_730 | 5 | 0.1756 | 0.5427 | +0.0034 | +0.0071 | +9.1% |
| Serie A | btts_yes | production_raw | 5 | 0.1789 | 0.5498 | +0.0000 | +0.0000 | +9.1% |
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