# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 268/284 fixture-markets; 78 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 39 | 0.1829 | 0.5466 | +0.0016 | +0.0057 | +2.6% |
| ALL | over_1_5 | goal_selected | 24 | 0.2050 | 0.5992 | -0.0049 | -0.0117 | +8.6% |
| ALL | over_1_5 | half_life_1000000000 | 39 | 0.1837 | 0.5502 | +0.0008 | +0.0020 | +2.1% |
| ALL | over_1_5 | half_life_120 | 39 | 0.1889 | 0.5818 | -0.0044 | -0.0295 | +4.8% |
| ALL | over_1_5 | half_life_240 | 39 | 0.1854 | 0.5601 | -0.0009 | -0.0079 | +3.4% |
| ALL | over_1_5 | half_life_365 | 39 | 0.1844 | 0.5546 | +0.0001 | -0.0023 | +2.9% |
| ALL | over_1_5 | half_life_730 | 39 | 0.1838 | 0.5516 | +0.0006 | +0.0006 | +2.4% |
| ALL | over_1_5 | production_raw | 39 | 0.1845 | 0.5522 | +0.0000 | +0.0000 | +2.6% |
| ALL | btts_yes | development_1x2 | 39 | 0.2629 | 0.7268 | +0.0012 | +0.0023 | +3.5% |
| ALL | btts_yes | goal_selected | 24 | 0.2498 | 0.6960 | -0.0007 | -0.0018 | +4.7% |
| ALL | btts_yes | half_life_1000000000 | 39 | 0.2645 | 0.7299 | -0.0005 | -0.0008 | +3.2% |
| ALL | btts_yes | half_life_120 | 39 | 0.2809 | 0.7694 | -0.0168 | -0.0404 | +4.1% |
| ALL | btts_yes | half_life_240 | 39 | 0.2698 | 0.7422 | -0.0057 | -0.0131 | +3.4% |
| ALL | btts_yes | half_life_365 | 39 | 0.2653 | 0.7323 | -0.0012 | -0.0032 | +3.4% |
| ALL | btts_yes | half_life_730 | 39 | 0.2637 | 0.7283 | +0.0004 | +0.0008 | +3.3% |
| ALL | btts_yes | production_raw | 39 | 0.2641 | 0.7291 | +0.0000 | +0.0000 | +3.4% |
| Bundesliga | over_1_5 | development_1x2 | 5 | 0.2300 | 0.6370 | +0.0045 | +0.0110 | +13.6% |
| Bundesliga | over_1_5 | goal_selected | 5 | 0.2390 | 0.6585 | -0.0045 | -0.0104 | +13.6% |
| Bundesliga | over_1_5 | half_life_1000000000 | 5 | 0.2300 | 0.6370 | +0.0045 | +0.0110 | +13.6% |
| Bundesliga | over_1_5 | half_life_120 | 5 | 0.2497 | 0.6825 | -0.0152 | -0.0345 | +14.6% |
| Bundesliga | over_1_5 | half_life_240 | 5 | 0.2430 | 0.6675 | -0.0085 | -0.0195 | +13.7% |
| Bundesliga | over_1_5 | half_life_365 | 5 | 0.2390 | 0.6585 | -0.0045 | -0.0104 | +13.6% |
| Bundesliga | over_1_5 | half_life_730 | 5 | 0.2345 | 0.6481 | +0.0000 | +0.0000 | +13.5% |
| Bundesliga | over_1_5 | production_raw | 5 | 0.2345 | 0.6481 | +0.0000 | +0.0000 | +13.5% |
| Bundesliga | btts_yes | development_1x2 | 5 | 0.2239 | 0.6403 | +0.0026 | +0.0057 | -9.5% |
| Bundesliga | btts_yes | goal_selected | 5 | 0.2298 | 0.6536 | -0.0033 | -0.0075 | -9.6% |
| Bundesliga | btts_yes | half_life_1000000000 | 5 | 0.2239 | 0.6403 | +0.0026 | +0.0057 | -9.5% |
| Bundesliga | btts_yes | half_life_120 | 5 | 0.2324 | 0.6597 | -0.0059 | -0.0137 | -9.3% |
| Bundesliga | btts_yes | half_life_240 | 5 | 0.2298 | 0.6536 | -0.0033 | -0.0075 | -9.6% |
| Bundesliga | btts_yes | half_life_365 | 5 | 0.2285 | 0.6504 | -0.0020 | -0.0044 | -9.6% |
| Bundesliga | btts_yes | half_life_730 | 5 | 0.2265 | 0.6460 | +0.0000 | +0.0000 | -9.6% |
| Bundesliga | btts_yes | production_raw | 5 | 0.2265 | 0.6460 | +0.0000 | +0.0000 | -9.6% |
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
| Premier League | over_1_5 | development_1x2 | 5 | 0.2500 | 0.7016 | -0.0030 | -0.0052 | +20.4% |
| Premier League | over_1_5 | goal_selected | 5 | 0.2583 | 0.7280 | -0.0113 | -0.0316 | +20.2% |
| Premier League | over_1_5 | half_life_1000000000 | 5 | 0.2583 | 0.7280 | -0.0113 | -0.0316 | +20.2% |
| Premier League | over_1_5 | half_life_120 | 5 | 0.2461 | 0.7164 | +0.0009 | -0.0201 | +21.1% |
| Premier League | over_1_5 | half_life_240 | 5 | 0.2470 | 0.6964 | +0.0000 | +0.0000 | +20.5% |
| Premier League | over_1_5 | half_life_365 | 5 | 0.2500 | 0.7016 | -0.0030 | -0.0052 | +20.4% |
| Premier League | over_1_5 | half_life_730 | 5 | 0.2539 | 0.7126 | -0.0069 | -0.0163 | +20.2% |
| Premier League | over_1_5 | production_raw | 5 | 0.2470 | 0.6964 | +0.0000 | +0.0000 | +20.5% |
| Premier League | btts_yes | development_1x2 | 5 | 0.2668 | 0.7282 | +0.0028 | +0.0063 | +15.7% |
| Premier League | btts_yes | goal_selected | 5 | 0.2673 | 0.7291 | +0.0023 | +0.0054 | +15.4% |
| Premier League | btts_yes | half_life_1000000000 | 5 | 0.2708 | 0.7367 | -0.0012 | -0.0023 | +15.0% |
| Premier League | btts_yes | half_life_120 | 5 | 0.2918 | 0.7844 | -0.0222 | -0.0500 | +17.3% |
| Premier League | btts_yes | half_life_240 | 5 | 0.2696 | 0.7344 | +0.0000 | +0.0000 | +16.2% |
| Premier League | btts_yes | half_life_365 | 5 | 0.2668 | 0.7282 | +0.0028 | +0.0063 | +15.7% |
| Premier League | btts_yes | half_life_730 | 5 | 0.2673 | 0.7291 | +0.0023 | +0.0054 | +15.4% |
| Premier League | btts_yes | production_raw | 5 | 0.2696 | 0.7344 | +0.0000 | +0.0000 | +16.2% |
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