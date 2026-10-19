# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 284/300 fixture-markets; 110 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 55 | 0.1718 | 0.5219 | +0.0023 | +0.0076 | -2.4% |
| ALL | over_1_5 | goal_selected | 40 | 0.1833 | 0.5530 | -0.0038 | -0.0108 | -0.4% |
| ALL | over_1_5 | half_life_1000000000 | 55 | 0.1751 | 0.5326 | -0.0010 | -0.0030 | -2.7% |
| ALL | over_1_5 | half_life_120 | 55 | 0.1735 | 0.5393 | +0.0006 | -0.0098 | -0.9% |
| ALL | over_1_5 | half_life_240 | 55 | 0.1732 | 0.5305 | +0.0009 | -0.0009 | -1.8% |
| ALL | over_1_5 | half_life_365 | 55 | 0.1734 | 0.5294 | +0.0007 | +0.0001 | -2.2% |
| ALL | over_1_5 | half_life_730 | 55 | 0.1741 | 0.5303 | -0.0000 | -0.0008 | -2.5% |
| ALL | over_1_5 | production_raw | 55 | 0.1741 | 0.5295 | +0.0000 | +0.0000 | -2.4% |
| ALL | btts_yes | development_1x2 | 55 | 0.2612 | 0.7214 | +0.0027 | +0.0056 | +0.7% |
| ALL | btts_yes | goal_selected | 40 | 0.2508 | 0.6972 | +0.0041 | +0.0081 | +0.9% |
| ALL | btts_yes | half_life_1000000000 | 55 | 0.2626 | 0.7244 | +0.0013 | +0.0027 | +0.6% |
| ALL | btts_yes | half_life_120 | 55 | 0.2729 | 0.7491 | -0.0089 | -0.0220 | +1.2% |
| ALL | btts_yes | half_life_240 | 55 | 0.2658 | 0.7317 | -0.0019 | -0.0047 | +0.8% |
| ALL | btts_yes | half_life_365 | 55 | 0.2628 | 0.7250 | +0.0012 | +0.0020 | +0.8% |
| ALL | btts_yes | half_life_730 | 55 | 0.2618 | 0.7227 | +0.0022 | +0.0044 | +0.7% |
| ALL | btts_yes | production_raw | 55 | 0.2640 | 0.7270 | +0.0000 | +0.0000 | +0.7% |
| Bundesliga | over_1_5 | development_1x2 | 7 | 0.1684 | 0.4912 | +0.0035 | +0.0091 | +6.3% |
| Bundesliga | over_1_5 | goal_selected | 7 | 0.1751 | 0.5081 | -0.0032 | -0.0077 | +6.2% |
| Bundesliga | over_1_5 | half_life_1000000000 | 7 | 0.1684 | 0.4912 | +0.0035 | +0.0091 | +6.3% |
| Bundesliga | over_1_5 | half_life_120 | 7 | 0.1814 | 0.5188 | -0.0096 | -0.0185 | +7.5% |
| Bundesliga | over_1_5 | half_life_240 | 7 | 0.1778 | 0.5138 | -0.0060 | -0.0134 | +6.4% |
| Bundesliga | over_1_5 | half_life_365 | 7 | 0.1751 | 0.5081 | -0.0032 | -0.0077 | +6.2% |
| Bundesliga | over_1_5 | half_life_730 | 7 | 0.1718 | 0.5003 | +0.0000 | +0.0000 | +6.2% |
| Bundesliga | over_1_5 | production_raw | 7 | 0.1718 | 0.5003 | +0.0000 | +0.0000 | +6.2% |
| Bundesliga | btts_yes | development_1x2 | 7 | 0.1961 | 0.5815 | -0.0001 | +0.0003 | -16.7% |
| Bundesliga | btts_yes | goal_selected | 7 | 0.1946 | 0.5795 | +0.0013 | +0.0023 | -16.1% |
| Bundesliga | btts_yes | half_life_1000000000 | 7 | 0.1961 | 0.5815 | -0.0001 | +0.0003 | -16.7% |
| Bundesliga | btts_yes | half_life_120 | 7 | 0.1907 | 0.5702 | +0.0053 | +0.0116 | -15.0% |
| Bundesliga | btts_yes | half_life_240 | 7 | 0.1946 | 0.5795 | +0.0013 | +0.0023 | -16.1% |
| Bundesliga | btts_yes | half_life_365 | 7 | 0.1956 | 0.5813 | +0.0004 | +0.0005 | -16.4% |
| Bundesliga | btts_yes | half_life_730 | 7 | 0.1960 | 0.5818 | +0.0000 | +0.0000 | -16.6% |
| Bundesliga | btts_yes | production_raw | 7 | 0.1960 | 0.5818 | +0.0000 | +0.0000 | -16.6% |
| La Liga | over_1_5 | development_1x2 | 8 | 0.2269 | 0.6524 | +0.0015 | +0.0041 | +2.4% |
| La Liga | over_1_5 | goal_selected | 8 | 0.2240 | 0.6441 | +0.0045 | +0.0124 | +4.0% |
| La Liga | over_1_5 | half_life_1000000000 | 8 | 0.2301 | 0.6615 | -0.0017 | -0.0050 | +1.7% |
| La Liga | over_1_5 | half_life_120 | 8 | 0.2240 | 0.6441 | +0.0045 | +0.0124 | +4.0% |
| La Liga | over_1_5 | half_life_240 | 8 | 0.2258 | 0.6494 | +0.0027 | +0.0071 | +2.8% |
| La Liga | over_1_5 | half_life_365 | 8 | 0.2269 | 0.6524 | +0.0015 | +0.0041 | +2.4% |
| La Liga | over_1_5 | half_life_730 | 8 | 0.2285 | 0.6565 | +0.0000 | +0.0000 | +2.0% |
| La Liga | over_1_5 | production_raw | 8 | 0.2285 | 0.6565 | +0.0000 | +0.0000 | +2.0% |
| La Liga | btts_yes | development_1x2 | 8 | 0.3262 | 0.8571 | +0.0037 | +0.0074 | -8.2% |
| La Liga | btts_yes | goal_selected | 8 | 0.3239 | 0.8533 | +0.0060 | +0.0112 | -7.6% |
| La Liga | btts_yes | half_life_1000000000 | 8 | 0.3349 | 0.8754 | -0.0051 | -0.0109 | -8.9% |
| La Liga | btts_yes | half_life_120 | 8 | 0.3221 | 0.8546 | +0.0077 | +0.0099 | -5.9% |
| La Liga | btts_yes | half_life_240 | 8 | 0.3239 | 0.8533 | +0.0060 | +0.0112 | -7.6% |
| La Liga | btts_yes | half_life_365 | 8 | 0.3262 | 0.8571 | +0.0037 | +0.0074 | -8.2% |
| La Liga | btts_yes | half_life_730 | 8 | 0.3299 | 0.8645 | +0.0000 | +0.0000 | -8.6% |
| La Liga | btts_yes | production_raw | 8 | 0.3299 | 0.8645 | +0.0000 | +0.0000 | -8.6% |
| Ligue 1 | over_1_5 | development_1x2 | 6 | 0.1443 | 0.4573 | +0.0125 | +0.0430 | -4.0% |
| Ligue 1 | over_1_5 | goal_selected | 6 | 0.1637 | 0.5261 | -0.0069 | -0.0258 | -4.1% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 6 | 0.1637 | 0.5261 | -0.0069 | -0.0258 | -4.1% |
| Ligue 1 | over_1_5 | half_life_120 | 6 | 0.1277 | 0.4063 | +0.0290 | +0.0941 | -3.9% |
| Ligue 1 | over_1_5 | half_life_240 | 6 | 0.1443 | 0.4573 | +0.0125 | +0.0430 | -4.0% |
| Ligue 1 | over_1_5 | half_life_365 | 6 | 0.1503 | 0.4777 | +0.0065 | +0.0227 | -4.1% |
| Ligue 1 | over_1_5 | half_life_730 | 6 | 0.1567 | 0.5003 | +0.0000 | +0.0000 | -4.1% |
| Ligue 1 | over_1_5 | production_raw | 6 | 0.1567 | 0.5003 | +0.0000 | +0.0000 | -4.1% |
| Ligue 1 | btts_yes | development_1x2 | 6 | 0.2945 | 0.7850 | +0.0060 | +0.0122 | -11.2% |
| Ligue 1 | btts_yes | goal_selected | 6 | 0.3047 | 0.8062 | -0.0042 | -0.0090 | -11.2% |
| Ligue 1 | btts_yes | half_life_1000000000 | 6 | 0.3047 | 0.8062 | -0.0042 | -0.0090 | -11.2% |
| Ligue 1 | btts_yes | half_life_120 | 6 | 0.2886 | 0.7753 | +0.0119 | +0.0219 | -10.9% |
| Ligue 1 | btts_yes | half_life_240 | 6 | 0.2945 | 0.7850 | +0.0060 | +0.0122 | -11.2% |
| Ligue 1 | btts_yes | half_life_365 | 6 | 0.2972 | 0.7903 | +0.0033 | +0.0069 | -11.2% |
| Ligue 1 | btts_yes | half_life_730 | 6 | 0.3006 | 0.7971 | +0.0000 | +0.0000 | -11.2% |
| Ligue 1 | btts_yes | production_raw | 6 | 0.3006 | 0.7971 | +0.0000 | +0.0000 | -11.2% |
| Premier League | over_1_5 | development_1x2 | 10 | 0.1955 | 0.5768 | -0.0031 | -0.0069 | +7.6% |
| Premier League | over_1_5 | goal_selected | 10 | 0.2046 | 0.6020 | -0.0122 | -0.0322 | +7.6% |
| Premier League | over_1_5 | half_life_1000000000 | 10 | 0.2046 | 0.6020 | -0.0122 | -0.0322 | +7.6% |
| Premier League | over_1_5 | half_life_120 | 10 | 0.1906 | 0.5748 | +0.0018 | -0.0050 | +7.7% |
| Premier League | over_1_5 | half_life_240 | 10 | 0.1924 | 0.5699 | +0.0000 | +0.0000 | +7.7% |
| Premier League | over_1_5 | half_life_365 | 10 | 0.1955 | 0.5768 | -0.0031 | -0.0069 | +7.6% |
| Premier League | over_1_5 | half_life_730 | 10 | 0.1997 | 0.5878 | -0.0074 | -0.0180 | +7.6% |
| Premier League | over_1_5 | production_raw | 10 | 0.1924 | 0.5699 | +0.0000 | +0.0000 | +7.7% |
| Premier League | btts_yes | development_1x2 | 10 | 0.2541 | 0.7020 | +0.0029 | +0.0061 | +14.0% |
| Premier League | btts_yes | goal_selected | 10 | 0.2534 | 0.7007 | +0.0035 | +0.0074 | +13.8% |
| Premier League | btts_yes | half_life_1000000000 | 10 | 0.2549 | 0.7039 | +0.0021 | +0.0041 | +13.6% |
| Premier League | btts_yes | half_life_120 | 10 | 0.2747 | 0.7464 | -0.0178 | -0.0383 | +14.0% |
| Premier League | btts_yes | half_life_240 | 10 | 0.2570 | 0.7081 | +0.0000 | +0.0000 | +14.1% |
| Premier League | btts_yes | half_life_365 | 10 | 0.2541 | 0.7020 | +0.0029 | +0.0061 | +14.0% |
| Premier League | btts_yes | half_life_730 | 10 | 0.2534 | 0.7007 | +0.0035 | +0.0074 | +13.8% |
| Premier League | btts_yes | production_raw | 10 | 0.2570 | 0.7081 | +0.0000 | +0.0000 | +14.1% |
| Serie A | over_1_5 | development_1x2 | 9 | 0.1381 | 0.4555 | +0.0050 | +0.0147 | -16.4% |
| Serie A | over_1_5 | goal_selected | 9 | 0.1431 | 0.4702 | +0.0000 | +0.0000 | -15.8% |
| Serie A | over_1_5 | half_life_1000000000 | 9 | 0.1322 | 0.4386 | +0.0110 | +0.0316 | -17.1% |
| Serie A | over_1_5 | half_life_120 | 9 | 0.1548 | 0.5151 | -0.0116 | -0.0449 | -14.2% |
| Serie A | over_1_5 | half_life_240 | 9 | 0.1431 | 0.4702 | +0.0000 | +0.0000 | -15.8% |
| Serie A | over_1_5 | half_life_365 | 9 | 0.1381 | 0.4555 | +0.0050 | +0.0147 | -16.4% |
| Serie A | over_1_5 | half_life_730 | 9 | 0.1343 | 0.4449 | +0.0088 | +0.0253 | -16.8% |
| Serie A | over_1_5 | production_raw | 9 | 0.1431 | 0.4702 | +0.0000 | +0.0000 | -15.8% |
| Serie A | btts_yes | development_1x2 | 9 | 0.1954 | 0.5829 | +0.0063 | +0.0126 | +15.2% |
| Serie A | btts_yes | goal_selected | 9 | 0.1907 | 0.5735 | +0.0109 | +0.0221 | +15.4% |
| Serie A | btts_yes | half_life_1000000000 | 9 | 0.1883 | 0.5684 | +0.0133 | +0.0272 | +15.7% |
| Serie A | btts_yes | half_life_120 | 9 | 0.2132 | 0.6188 | -0.0116 | -0.0232 | +15.2% |
| Serie A | btts_yes | half_life_240 | 9 | 0.2016 | 0.5956 | +0.0000 | +0.0000 | +15.1% |
| Serie A | btts_yes | half_life_365 | 9 | 0.1954 | 0.5829 | +0.0063 | +0.0126 | +15.2% |
| Serie A | btts_yes | half_life_730 | 9 | 0.1907 | 0.5735 | +0.0109 | +0.0221 | +15.4% |
| Serie A | btts_yes | production_raw | 9 | 0.2016 | 0.5956 | +0.0000 | +0.0000 | +15.1% |
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
| Premier League | over_1_5 | 1000000000.0 | 303 | 69 | -0.0107 | {'1000000000.0': 3, '240.0': 1} |
| Premier League | btts_yes | 1000000000.0 | 303 | 69 | -0.0117 | {'1000000000.0': 2, '365.0': 1, '120.0': 1} |
| La Liga | over_1_5 | 120.0 | 295 | 87 | -0.0125 | {'120.0': 2, '730.0': 1, '1000000000.0': 1} |
| La Liga | btts_yes | 120.0 | 295 | 87 | -0.0020 | {'240.0': 1, '1000000000.0': 1, '120.0': 2} |
| Bundesliga | over_1_5 | 1000000000.0 | 245 | 54 | +0.0032 | {'1000000000.0': 3, '240.0': 1} |
| Bundesliga | btts_yes | 240.0 | 245 | 54 | +0.0005 | {'730.0': 1, '240.0': 1, '1000000000.0': 1, '120.0': 1} |
| Serie A | over_1_5 | 240.0 | 316 | 68 | -0.0085 | {'240.0': 2, '120.0': 1, '1000000000.0': 1} |
| Serie A | btts_yes | 365.0 | 316 | 68 | -0.0037 | {'730.0': 1, '120.0': 1, '1000000000.0': 1, '240.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 239 | 63 | +0.0000 | {'1000000000.0': 2, '120.0': 1, '240.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 239 | 63 | +0.0000 | {'1000000000.0': 3, '120.0': 1} |
| UEFA Champions League | over_1_5 | 120.0 | 152 | 37 | -0.0230 | {'240.0': 2, '120.0': 2} |
| UEFA Champions League | btts_yes | 730.0 | 152 | 37 | +0.0030 | {'240.0': 1, '1000000000.0': 3} |