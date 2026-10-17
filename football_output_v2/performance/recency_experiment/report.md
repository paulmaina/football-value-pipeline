# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 268/284 fixture-markets; 40 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 20 | 0.1540 | 0.4796 | -0.0004 | -0.0005 | -5.0% |
| ALL | over_1_5 | goal_selected | 5 | 0.1485 | 0.4604 | -0.0123 | -0.0314 | +0.2% |
| ALL | over_1_5 | half_life_1000000000 | 20 | 0.1540 | 0.4795 | -0.0003 | -0.0004 | -5.1% |
| ALL | over_1_5 | half_life_120 | 20 | 0.1555 | 0.5097 | -0.0018 | -0.0305 | -2.3% |
| ALL | over_1_5 | half_life_240 | 20 | 0.1545 | 0.4939 | -0.0008 | -0.0148 | -3.7% |
| ALL | over_1_5 | half_life_365 | 20 | 0.1544 | 0.4887 | -0.0007 | -0.0096 | -4.2% |
| ALL | over_1_5 | half_life_730 | 20 | 0.1543 | 0.4844 | -0.0007 | -0.0053 | -4.7% |
| ALL | over_1_5 | production_raw | 20 | 0.1537 | 0.4791 | +0.0000 | +0.0000 | -5.0% |
| ALL | btts_yes | development_1x2 | 20 | 0.2820 | 0.7694 | +0.0002 | +0.0002 | +5.7% |
| ALL | btts_yes | goal_selected | 5 | 0.2515 | 0.6962 | +0.0131 | +0.0275 | +19.7% |
| ALL | btts_yes | half_life_1000000000 | 20 | 0.2767 | 0.7582 | +0.0055 | +0.0114 | +5.5% |
| ALL | btts_yes | half_life_120 | 20 | 0.3109 | 0.8361 | -0.0287 | -0.0665 | +6.1% |
| ALL | btts_yes | half_life_240 | 20 | 0.2940 | 0.7959 | -0.0119 | -0.0263 | +5.4% |
| ALL | btts_yes | half_life_365 | 20 | 0.2847 | 0.7761 | -0.0025 | -0.0065 | +5.6% |
| ALL | btts_yes | half_life_730 | 20 | 0.2792 | 0.7639 | +0.0029 | +0.0058 | +5.6% |
| ALL | btts_yes | production_raw | 20 | 0.2822 | 0.7696 | +0.0000 | +0.0000 | +5.5% |
| La Liga | over_1_5 | development_1x2 | 2 | 0.2866 | 0.7585 | -0.0038 | -0.0094 | +29.7% |
| La Liga | over_1_5 | goal_selected | 2 | 0.3015 | 0.7942 | -0.0186 | -0.0452 | +32.0% |
| La Liga | over_1_5 | half_life_1000000000 | 2 | 0.2810 | 0.7442 | +0.0019 | +0.0049 | +29.2% |
| La Liga | over_1_5 | half_life_120 | 2 | 0.3015 | 0.7942 | -0.0186 | -0.0452 | +32.0% |
| La Liga | over_1_5 | half_life_240 | 2 | 0.2913 | 0.7702 | -0.0084 | -0.0211 | +30.3% |
| La Liga | over_1_5 | half_life_365 | 2 | 0.2866 | 0.7585 | -0.0038 | -0.0094 | +29.7% |
| La Liga | over_1_5 | half_life_730 | 2 | 0.2829 | 0.7491 | +0.0000 | +0.0000 | +29.4% |
| La Liga | over_1_5 | production_raw | 2 | 0.2829 | 0.7491 | +0.0000 | +0.0000 | +29.4% |
| La Liga | btts_yes | development_1x2 | 2 | 0.1997 | 0.5893 | -0.0035 | -0.0069 | +8.1% |
| La Liga | btts_yes | goal_selected | 2 | 0.2029 | 0.5956 | -0.0068 | -0.0132 | +8.8% |
| La Liga | btts_yes | half_life_1000000000 | 2 | 0.1933 | 0.5767 | +0.0029 | +0.0058 | +7.3% |
| La Liga | btts_yes | half_life_120 | 2 | 0.2043 | 0.5966 | -0.0081 | -0.0141 | +10.9% |
| La Liga | btts_yes | half_life_240 | 2 | 0.2029 | 0.5956 | -0.0068 | -0.0132 | +8.8% |
| La Liga | btts_yes | half_life_365 | 2 | 0.1997 | 0.5893 | -0.0035 | -0.0069 | +8.1% |
| La Liga | btts_yes | half_life_730 | 2 | 0.1961 | 0.5824 | +0.0000 | +0.0000 | +7.6% |
| La Liga | btts_yes | production_raw | 2 | 0.1961 | 0.5824 | +0.0000 | +0.0000 | +7.6% |
| Ligue 1 | over_1_5 | development_1x2 | 1 | 0.0178 | 0.1432 | +0.0047 | +0.0192 | -13.3% |
| Ligue 1 | over_1_5 | goal_selected | 1 | 0.0237 | 0.1673 | -0.0013 | -0.0050 | -15.4% |
| Ligue 1 | over_1_5 | half_life_1000000000 | 1 | 0.0237 | 0.1673 | -0.0013 | -0.0050 | -15.4% |
| Ligue 1 | over_1_5 | half_life_120 | 1 | 0.0111 | 0.1112 | +0.0114 | +0.0512 | -10.5% |
| Ligue 1 | over_1_5 | half_life_240 | 1 | 0.0178 | 0.1432 | +0.0047 | +0.0192 | -13.3% |
| Ligue 1 | over_1_5 | half_life_365 | 1 | 0.0203 | 0.1538 | +0.0021 | +0.0086 | -14.3% |
| Ligue 1 | over_1_5 | half_life_730 | 1 | 0.0225 | 0.1623 | +0.0000 | +0.0000 | -15.0% |
| Ligue 1 | over_1_5 | production_raw | 1 | 0.0225 | 0.1623 | +0.0000 | +0.0000 | -15.0% |
| Ligue 1 | btts_yes | development_1x2 | 1 | 0.4584 | 1.1303 | -0.0280 | -0.0629 | +67.7% |
| Ligue 1 | btts_yes | goal_selected | 1 | 0.4228 | 1.0506 | +0.0076 | +0.0168 | +65.0% |
| Ligue 1 | btts_yes | half_life_1000000000 | 1 | 0.4228 | 1.0506 | +0.0076 | +0.0168 | +65.0% |
| Ligue 1 | btts_yes | half_life_120 | 1 | 0.5126 | 1.2586 | -0.0821 | -0.1912 | +71.6% |
| Ligue 1 | btts_yes | half_life_240 | 1 | 0.4584 | 1.1303 | -0.0280 | -0.0629 | +67.7% |
| Ligue 1 | btts_yes | half_life_365 | 1 | 0.4427 | 1.0948 | -0.0123 | -0.0274 | +66.5% |
| Ligue 1 | btts_yes | half_life_730 | 1 | 0.4305 | 1.0674 | +0.0000 | +0.0000 | +65.6% |
| Ligue 1 | btts_yes | production_raw | 1 | 0.4305 | 1.0674 | +0.0000 | +0.0000 | +65.6% |
| Premier League | over_1_5 | development_1x2 | 1 | 0.0593 | 0.2790 | -0.0093 | -0.0260 | -24.3% |
| Premier League | over_1_5 | goal_selected | 1 | 0.0730 | 0.3149 | -0.0230 | -0.0618 | -27.0% |
| Premier League | over_1_5 | half_life_1000000000 | 1 | 0.0730 | 0.3149 | -0.0230 | -0.0618 | -27.0% |
| Premier League | over_1_5 | half_life_120 | 1 | 0.0282 | 0.1838 | +0.0218 | +0.0692 | -16.8% |
| Premier League | over_1_5 | half_life_240 | 1 | 0.0500 | 0.2530 | +0.0000 | +0.0000 | -22.4% |
| Premier League | over_1_5 | half_life_365 | 1 | 0.0593 | 0.2790 | -0.0093 | -0.0260 | -24.3% |
| Premier League | over_1_5 | half_life_730 | 1 | 0.0673 | 0.3003 | -0.0173 | -0.0473 | -25.9% |
| Premier League | over_1_5 | production_raw | 1 | 0.0500 | 0.2530 | +0.0000 | +0.0000 | -22.4% |
| Premier League | btts_yes | development_1x2 | 1 | 0.3062 | 0.8060 | +0.0239 | +0.0486 | +55.3% |
| Premier League | btts_yes | goal_selected | 1 | 0.2875 | 0.7682 | +0.0426 | +0.0864 | +53.6% |
| Premier League | btts_yes | half_life_1000000000 | 1 | 0.2742 | 0.7417 | +0.0559 | +0.1129 | +52.4% |
| Premier League | btts_yes | half_life_120 | 1 | 0.4055 | 1.0127 | -0.0754 | -0.1581 | +63.7% |
| Premier League | btts_yes | half_life_240 | 1 | 0.3301 | 0.8546 | +0.0000 | +0.0000 | +57.5% |
| Premier League | btts_yes | half_life_365 | 1 | 0.3062 | 0.8060 | +0.0239 | +0.0486 | +55.3% |
| Premier League | btts_yes | half_life_730 | 1 | 0.2875 | 0.7682 | +0.0426 | +0.0864 | +53.6% |
| Premier League | btts_yes | production_raw | 1 | 0.3301 | 0.8546 | +0.0000 | +0.0000 | +57.5% |
| Serie A | over_1_5 | development_1x2 | 1 | 0.0377 | 0.2159 | +0.0050 | +0.0156 | -19.4% |
| Serie A | over_1_5 | goal_selected | 1 | 0.0427 | 0.2315 | +0.0000 | +0.0000 | -20.7% |
| Serie A | over_1_5 | half_life_1000000000 | 1 | 0.0278 | 0.1824 | +0.0149 | +0.0491 | -16.7% |
| Serie A | over_1_5 | half_life_120 | 1 | 0.0501 | 0.2534 | -0.0074 | -0.0219 | -22.4% |
| Serie A | over_1_5 | half_life_240 | 1 | 0.0427 | 0.2315 | +0.0000 | +0.0000 | -20.7% |
| Serie A | over_1_5 | half_life_365 | 1 | 0.0377 | 0.2159 | +0.0050 | +0.0156 | -19.4% |
| Serie A | over_1_5 | half_life_730 | 1 | 0.0325 | 0.1988 | +0.0102 | +0.0327 | -18.0% |
| Serie A | over_1_5 | production_raw | 1 | 0.0427 | 0.2315 | +0.0000 | +0.0000 | -20.7% |
| Serie A | btts_yes | development_1x2 | 1 | 0.1549 | 0.5003 | +0.0152 | +0.0316 | -39.4% |
| Serie A | btts_yes | goal_selected | 1 | 0.1411 | 0.4711 | +0.0290 | +0.0608 | -37.6% |
| Serie A | btts_yes | half_life_1000000000 | 1 | 0.1293 | 0.4456 | +0.0409 | +0.0863 | -36.0% |
| Serie A | btts_yes | half_life_120 | 1 | 0.1902 | 0.5728 | -0.0200 | -0.0410 | -43.6% |
| Serie A | btts_yes | half_life_240 | 1 | 0.1701 | 0.5319 | +0.0000 | +0.0000 | -41.2% |
| Serie A | btts_yes | half_life_365 | 1 | 0.1549 | 0.5003 | +0.0152 | +0.0316 | -39.4% |
| Serie A | btts_yes | half_life_730 | 1 | 0.1411 | 0.4711 | +0.0290 | +0.0608 | -37.6% |
| Serie A | btts_yes | production_raw | 1 | 0.1701 | 0.5319 | +0.0000 | +0.0000 | -41.2% |
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
| Premier League | over_1_5 | 1000000000.0 | 310 | 60 | +0.0040 | {'240.0': 1, '1000000000.0': 3} |
| Premier League | btts_yes | 730.0 | 310 | 60 | -0.0000 | {'1000000000.0': 2, '365.0': 1, '120.0': 1} |
| La Liga | over_1_5 | 120.0 | 300 | 79 | -0.0017 | {'120.0': 3, '240.0': 1} |
| La Liga | btts_yes | 240.0 | 300 | 79 | +0.0020 | {'365.0': 1, '120.0': 3} |
| Bundesliga | over_1_5 | 365.0 | 252 | 46 | -0.0103 | {'730.0': 1, '1000000000.0': 2, '120.0': 1} |
| Bundesliga | btts_yes | 240.0 | 252 | 46 | -0.0051 | {'120.0': 2, '730.0': 1, '240.0': 1} |
| Serie A | over_1_5 | 240.0 | 320 | 61 | -0.0015 | {'120.0': 1, '240.0': 1, '1000000000.0': 1, '365.0': 1} |
| Serie A | btts_yes | 1000000000.0 | 320 | 61 | -0.0037 | {'1000000000.0': 2, '120.0': 1, '365.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 243 | 55 | -0.0197 | {'1000000000.0': 3, '120.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 243 | 55 | -0.0087 | {'1000000000.0': 3, '120.0': 1} |
| UEFA Champions League | over_1_5 | 120.0 | 152 | 37 | -0.0232 | {'240.0': 2, '120.0': 2} |
| UEFA Champions League | btts_yes | 730.0 | 152 | 37 | +0.0027 | {'240.0': 1, '1000000000.0': 3} |