# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 268/284 fixture-markets; 50 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 25 | 0.1922 | 0.5651 | +0.0028 | +0.0082 | +2.1% |
| ALL | over_1_5 | goal_selected | 10 | 0.2567 | 0.7110 | -0.0085 | -0.0214 | +15.6% |
| ALL | over_1_5 | half_life_1000000000 | 25 | 0.1894 | 0.5578 | +0.0056 | +0.0155 | +1.8% |
| ALL | over_1_5 | half_life_120 | 25 | 0.2048 | 0.6246 | -0.0098 | -0.0512 | +4.9% |
| ALL | over_1_5 | half_life_240 | 25 | 0.1974 | 0.5894 | -0.0024 | -0.0160 | +3.3% |
| ALL | over_1_5 | half_life_365 | 25 | 0.1943 | 0.5770 | +0.0007 | -0.0037 | +2.7% |
| ALL | over_1_5 | half_life_730 | 25 | 0.1917 | 0.5669 | +0.0033 | +0.0065 | +2.2% |
| ALL | over_1_5 | production_raw | 25 | 0.1950 | 0.5733 | +0.0000 | +0.0000 | +2.2% |
| ALL | btts_yes | development_1x2 | 25 | 0.2736 | 0.7506 | +0.0009 | +0.0017 | +5.7% |
| ALL | btts_yes | goal_selected | 10 | 0.2480 | 0.6907 | +0.0062 | +0.0127 | +12.6% |
| ALL | btts_yes | half_life_1000000000 | 25 | 0.2693 | 0.7416 | +0.0052 | +0.0107 | +5.5% |
| ALL | btts_yes | half_life_120 | 25 | 0.2993 | 0.8096 | -0.0248 | -0.0573 | +6.2% |
| ALL | btts_yes | half_life_240 | 25 | 0.2846 | 0.7746 | -0.0101 | -0.0224 | +5.5% |
| ALL | btts_yes | half_life_365 | 25 | 0.2766 | 0.7576 | -0.0020 | -0.0053 | +5.6% |
| ALL | btts_yes | half_life_730 | 25 | 0.2717 | 0.7468 | +0.0028 | +0.0055 | +5.5% |
| ALL | btts_yes | production_raw | 25 | 0.2745 | 0.7523 | +0.0000 | +0.0000 | +5.6% |
| Bundesliga | over_1_5 | development_1x2 | 4 | 0.2857 | 0.7744 | +0.0058 | +0.0150 | +19.1% |
| Bundesliga | over_1_5 | goal_selected | 4 | 0.2973 | 0.8034 | -0.0058 | -0.0141 | +18.9% |
| Bundesliga | over_1_5 | half_life_1000000000 | 4 | 0.2857 | 0.7744 | +0.0058 | +0.0150 | +19.1% |
| Bundesliga | over_1_5 | half_life_120 | 4 | 0.3107 | 0.8337 | -0.0191 | -0.0444 | +20.1% |
| Bundesliga | over_1_5 | half_life_240 | 4 | 0.3024 | 0.8155 | -0.0109 | -0.0261 | +19.0% |
| Bundesliga | over_1_5 | half_life_365 | 4 | 0.2973 | 0.8034 | -0.0058 | -0.0141 | +18.9% |
| Bundesliga | over_1_5 | half_life_730 | 4 | 0.2916 | 0.7893 | +0.0000 | +0.0000 | +18.9% |
| Bundesliga | over_1_5 | production_raw | 4 | 0.2916 | 0.7893 | +0.0000 | +0.0000 | +18.9% |
| Bundesliga | btts_yes | development_1x2 | 4 | 0.2541 | 0.7035 | +0.0026 | +0.0055 | -3.8% |
| Bundesliga | btts_yes | goal_selected | 4 | 0.2604 | 0.7175 | -0.0037 | -0.0084 | -3.8% |
| Bundesliga | btts_yes | half_life_1000000000 | 4 | 0.2541 | 0.7035 | +0.0026 | +0.0055 | -3.8% |
| Bundesliga | btts_yes | half_life_120 | 4 | 0.2628 | 0.7233 | -0.0061 | -0.0143 | -3.3% |
| Bundesliga | btts_yes | half_life_240 | 4 | 0.2604 | 0.7175 | -0.0037 | -0.0084 | -3.8% |
| Bundesliga | btts_yes | half_life_365 | 4 | 0.2588 | 0.7138 | -0.0021 | -0.0047 | -3.9% |
| Bundesliga | btts_yes | half_life_730 | 4 | 0.2567 | 0.7090 | +0.0000 | +0.0000 | -3.9% |
| Bundesliga | btts_yes | production_raw | 4 | 0.2567 | 0.7090 | +0.0000 | +0.0000 | -3.9% |
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
| Serie A | over_1_5 | development_1x2 | 2 | 0.3095 | 0.8267 | +0.0293 | +0.0859 | +28.4% |
| Serie A | over_1_5 | goal_selected | 2 | 0.3388 | 0.9126 | +0.0000 | +0.0000 | +29.5% |
| Serie A | over_1_5 | half_life_1000000000 | 2 | 0.2699 | 0.7198 | +0.0689 | +0.1928 | +27.4% |
| Serie A | over_1_5 | half_life_120 | 2 | 0.4086 | 1.1698 | -0.0698 | -0.2572 | +32.6% |
| Serie A | over_1_5 | half_life_240 | 2 | 0.3388 | 0.9126 | +0.0000 | +0.0000 | +29.5% |
| Serie A | over_1_5 | half_life_365 | 2 | 0.3095 | 0.8267 | +0.0293 | +0.0859 | +28.4% |
| Serie A | over_1_5 | half_life_730 | 2 | 0.2860 | 0.7626 | +0.0528 | +0.1500 | +27.7% |
| Serie A | over_1_5 | production_raw | 2 | 0.3388 | 0.9126 | +0.0000 | +0.0000 | +29.5% |
| Serie A | btts_yes | development_1x2 | 2 | 0.1700 | 0.5314 | +0.0116 | +0.0239 | +1.8% |
| Serie A | btts_yes | goal_selected | 2 | 0.1614 | 0.5134 | +0.0202 | +0.0419 | +2.5% |
| Serie A | btts_yes | half_life_1000000000 | 2 | 0.1566 | 0.5028 | +0.0250 | +0.0524 | +3.5% |
| Serie A | btts_yes | half_life_120 | 2 | 0.2027 | 0.5982 | -0.0211 | -0.0429 | +1.4% |
| Serie A | btts_yes | half_life_240 | 2 | 0.1816 | 0.5553 | +0.0000 | +0.0000 | +1.3% |
| Serie A | btts_yes | half_life_365 | 2 | 0.1700 | 0.5314 | +0.0116 | +0.0239 | +1.8% |
| Serie A | btts_yes | half_life_730 | 2 | 0.1614 | 0.5134 | +0.0202 | +0.0419 | +2.5% |
| Serie A | btts_yes | production_raw | 2 | 0.1816 | 0.5553 | +0.0000 | +0.0000 | +1.3% |
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