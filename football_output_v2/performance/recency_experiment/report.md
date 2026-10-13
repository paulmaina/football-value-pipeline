# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 126/134 fixture-markets; 2 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 1 | 0.2602 | 0.7135 | +0.0000 | +0.0000 | -51.0% |
| ALL | over_1_5 | half_life_1000000000 | 1 | 0.2602 | 0.7135 | +0.0000 | +0.0000 | -51.0% |
| ALL | over_1_5 | half_life_120 | 1 | 0.0994 | 0.3788 | +0.1607 | +0.3347 | -31.5% |
| ALL | over_1_5 | half_life_240 | 1 | 0.1695 | 0.5305 | +0.0907 | +0.1829 | -41.2% |
| ALL | over_1_5 | half_life_365 | 1 | 0.1952 | 0.5831 | +0.0649 | +0.1304 | -44.2% |
| ALL | over_1_5 | half_life_730 | 1 | 0.2278 | 0.6486 | +0.0324 | +0.0649 | -47.7% |
| ALL | over_1_5 | production_raw | 1 | 0.2602 | 0.7135 | +0.0000 | +0.0000 | -51.0% |
| ALL | btts_yes | development_1x2 | 1 | 0.0501 | 0.2534 | +0.0000 | +0.0000 | +22.4% |
| ALL | btts_yes | half_life_1000000000 | 1 | 0.0501 | 0.2534 | +0.0000 | +0.0000 | +22.4% |
| ALL | btts_yes | half_life_120 | 1 | 0.2168 | 0.6267 | -0.1667 | -0.3733 | +46.6% |
| ALL | btts_yes | half_life_240 | 1 | 0.1004 | 0.3811 | -0.0503 | -0.1277 | +31.7% |
| ALL | btts_yes | half_life_365 | 1 | 0.0744 | 0.3186 | -0.0243 | -0.0652 | +27.3% |
| ALL | btts_yes | half_life_730 | 1 | 0.0587 | 0.2773 | -0.0086 | -0.0240 | +24.2% |
| ALL | btts_yes | production_raw | 1 | 0.0501 | 0.2534 | +0.0000 | +0.0000 | +22.4% |
| UEFA Champions League | over_1_5 | development_1x2 | 1 | 0.2602 | 0.7135 | +0.0000 | +0.0000 | -51.0% |
| UEFA Champions League | over_1_5 | half_life_1000000000 | 1 | 0.2602 | 0.7135 | +0.0000 | +0.0000 | -51.0% |
| UEFA Champions League | over_1_5 | half_life_120 | 1 | 0.0994 | 0.3788 | +0.1607 | +0.3347 | -31.5% |
| UEFA Champions League | over_1_5 | half_life_240 | 1 | 0.1695 | 0.5305 | +0.0907 | +0.1829 | -41.2% |
| UEFA Champions League | over_1_5 | half_life_365 | 1 | 0.1952 | 0.5831 | +0.0649 | +0.1304 | -44.2% |
| UEFA Champions League | over_1_5 | half_life_730 | 1 | 0.2278 | 0.6486 | +0.0324 | +0.0649 | -47.7% |
| UEFA Champions League | over_1_5 | production_raw | 1 | 0.2602 | 0.7135 | +0.0000 | +0.0000 | -51.0% |
| UEFA Champions League | btts_yes | development_1x2 | 1 | 0.0501 | 0.2534 | +0.0000 | +0.0000 | +22.4% |
| UEFA Champions League | btts_yes | half_life_1000000000 | 1 | 0.0501 | 0.2534 | +0.0000 | +0.0000 | +22.4% |
| UEFA Champions League | btts_yes | half_life_120 | 1 | 0.2168 | 0.6267 | -0.1667 | -0.3733 | +46.6% |
| UEFA Champions League | btts_yes | half_life_240 | 1 | 0.1004 | 0.3811 | -0.0503 | -0.1277 | +31.7% |
| UEFA Champions League | btts_yes | half_life_365 | 1 | 0.0744 | 0.3186 | -0.0243 | -0.0652 | +27.3% |
| UEFA Champions League | btts_yes | half_life_730 | 1 | 0.0587 | 0.2773 | -0.0086 | -0.0240 | +24.2% |
| UEFA Champions League | btts_yes | production_raw | 1 | 0.0501 | 0.2534 | +0.0000 | +0.0000 | +22.4% |

Positive paired gain means lower error than the raw production model on those same matches. A 30-match review prompt is not statistical proof.

Calibration buckets, approximate paired-gain intervals, gameweek comparisons and historical selection stability for each frozen run are retained in summary.json. Historical audits overlap and are not additional forward samples.

## Latest historical development/audit diagnostics

| League | Market | Goal half-life | Development N | Audit N | Audit log-loss gain | Development fold wins |
|---|---|---:|---:|---:|---:|---|
| Premier League | over_1_5 | 1000000000.0 | 310 | 60 | +0.0041 | {'240.0': 1, '1000000000.0': 3} |
| Premier League | btts_yes | 730.0 | 310 | 60 | -0.0000 | {'1000000000.0': 2, '365.0': 1, '120.0': 1} |
| La Liga | over_1_5 | 120.0 | 300 | 78 | +0.0002 | {'120.0': 4} |
| La Liga | btts_yes | 240.0 | 300 | 78 | +0.0025 | {'730.0': 1, '120.0': 3} |
| Bundesliga | over_1_5 | 365.0 | 252 | 45 | -0.0067 | {'730.0': 1, '1000000000.0': 2, '120.0': 1} |
| Bundesliga | btts_yes | 240.0 | 252 | 45 | -0.0036 | {'120.0': 2, '365.0': 2} |
| Serie A | over_1_5 | 240.0 | 320 | 60 | -0.0010 | {'120.0': 2, '1000000000.0': 1, '365.0': 1} |
| Serie A | btts_yes | 730.0 | 320 | 60 | -0.0017 | {'1000000000.0': 2, '120.0': 1, '365.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 243 | 54 | -0.0175 | {'1000000000.0': 3, '120.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 243 | 54 | -0.0041 | {'1000000000.0': 3, '120.0': 1} |
| UEFA Champions League | over_1_5 | None | 184 | 23 | +0.0171 | {'120.0': 3, '240.0': 1} |
| UEFA Champions League | btts_yes | None | 184 | 23 | +0.0186 | {'365.0': 1, '120.0': 1, '1000000000.0': 2} |