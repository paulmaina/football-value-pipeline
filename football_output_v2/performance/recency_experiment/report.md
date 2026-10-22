# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 340/378 fixture-markets; 158 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 79 | 0.1853 | 0.6226 | +0.0023 | +0.0037 | -0.5% |
| ALL | over_1_5 | goal_selected | 64 | 0.1990 | 0.6579 | -0.0048 | -0.0010 | +0.4% |
| ALL | over_1_5 | half_life_1000000000 | 79 | 0.1876 | 0.6301 | +0.0001 | -0.0037 | -0.7% |
| ALL | over_1_5 | half_life_120 | 79 | 0.1892 | 0.6285 | -0.0016 | -0.0022 | -0.1% |
| ALL | over_1_5 | half_life_240 | 79 | 0.1861 | 0.6052 | +0.0015 | +0.0212 | -0.4% |
| ALL | over_1_5 | half_life_365 | 79 | 0.1865 | 0.6123 | +0.0011 | +0.0140 | -0.5% |
| ALL | over_1_5 | half_life_730 | 79 | 0.1872 | 0.6224 | +0.0005 | +0.0040 | -0.6% |
| ALL | over_1_5 | production_raw | 79 | 0.1876 | 0.6263 | +0.0000 | +0.0000 | -0.5% |
| ALL | btts_yes | development_1x2 | 79 | 0.2640 | 0.7331 | +0.0033 | +0.0074 | -3.7% |
| ALL | btts_yes | goal_selected | 64 | 0.2608 | 0.7286 | +0.0017 | +0.0015 | -4.5% |
| ALL | btts_yes | half_life_1000000000 | 79 | 0.2650 | 0.7352 | +0.0024 | +0.0054 | -3.8% |
| ALL | btts_yes | half_life_120 | 79 | 0.2886 | 0.8048 | -0.0212 | -0.0643 | -3.3% |
| ALL | btts_yes | half_life_240 | 79 | 0.2738 | 0.7614 | -0.0064 | -0.0208 | -3.4% |
| ALL | btts_yes | half_life_365 | 79 | 0.2695 | 0.7494 | -0.0022 | -0.0089 | -3.4% |
| ALL | btts_yes | half_life_730 | 79 | 0.2665 | 0.7404 | +0.0008 | +0.0001 | -3.6% |
| ALL | btts_yes | production_raw | 79 | 0.2673 | 0.7405 | +0.0000 | +0.0000 | -3.7% |
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
| Serie A | over_1_5 | 240.0 | 311 | 70 | -0.0072 | {'730.0': 1, '120.0': 2, '1000000000.0': 1} |
| Serie A | btts_yes | 730.0 | 311 | 70 | +0.0000 | {'730.0': 1, '120.0': 2, '1000000000.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 239 | 63 | +0.0000 | {'1000000000.0': 2, '120.0': 1, '365.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 239 | 63 | +0.0000 | {'1000000000.0': 3, '120.0': 1} |
| UEFA Champions League | over_1_5 | 365.0 | 144 | 54 | +0.0038 | {'730.0': 1, '120.0': 2, '240.0': 1} |
| UEFA Champions League | btts_yes | 1000000000.0 | 144 | 54 | +0.0016 | {'240.0': 1, '1000000000.0': 3} |
| UEFA Europa League | over_1_5 | 1000000000.0 | 153 | 36 | +0.0000 | {'1000000000.0': 2, '120.0': 1, '730.0': 1} |
| UEFA Europa League | btts_yes | 1000000000.0 | 153 | 36 | +0.0000 | {'1000000000.0': 2, '730.0': 2} |