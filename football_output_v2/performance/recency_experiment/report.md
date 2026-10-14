# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 208/220 fixture-markets; 18 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 9 | 0.1652 | 0.5005 | +0.0000 | +0.0000 | -12.6% |
| ALL | over_1_5 | half_life_1000000000 | 9 | 0.1652 | 0.5005 | +0.0000 | +0.0000 | -12.6% |
| ALL | over_1_5 | half_life_120 | 9 | 0.1628 | 0.5204 | +0.0024 | -0.0198 | -11.4% |
| ALL | over_1_5 | half_life_240 | 9 | 0.1617 | 0.4998 | +0.0035 | +0.0007 | -12.0% |
| ALL | over_1_5 | half_life_365 | 9 | 0.1625 | 0.4977 | +0.0027 | +0.0028 | -12.1% |
| ALL | over_1_5 | half_life_730 | 9 | 0.1640 | 0.4993 | +0.0012 | +0.0012 | -12.3% |
| ALL | over_1_5 | production_raw | 9 | 0.1652 | 0.5005 | +0.0000 | +0.0000 | -12.6% |
| ALL | btts_yes | development_1x2 | 9 | 0.3117 | 0.8400 | +0.0000 | +0.0000 | -6.3% |
| ALL | btts_yes | half_life_1000000000 | 9 | 0.3117 | 0.8400 | +0.0000 | +0.0000 | -6.3% |
| ALL | btts_yes | half_life_120 | 9 | 0.2686 | 0.7470 | +0.0431 | +0.0930 | -4.3% |
| ALL | btts_yes | half_life_240 | 9 | 0.2869 | 0.7854 | +0.0248 | +0.0547 | -5.6% |
| ALL | btts_yes | half_life_365 | 9 | 0.2950 | 0.8026 | +0.0167 | +0.0374 | -6.0% |
| ALL | btts_yes | half_life_730 | 9 | 0.3031 | 0.8200 | +0.0086 | +0.0200 | -6.2% |
| ALL | btts_yes | production_raw | 9 | 0.3117 | 0.8400 | +0.0000 | +0.0000 | -6.3% |
| UEFA Champions League | over_1_5 | development_1x2 | 9 | 0.1652 | 0.5005 | +0.0000 | +0.0000 | -12.6% |
| UEFA Champions League | over_1_5 | half_life_1000000000 | 9 | 0.1652 | 0.5005 | +0.0000 | +0.0000 | -12.6% |
| UEFA Champions League | over_1_5 | half_life_120 | 9 | 0.1628 | 0.5204 | +0.0024 | -0.0198 | -11.4% |
| UEFA Champions League | over_1_5 | half_life_240 | 9 | 0.1617 | 0.4998 | +0.0035 | +0.0007 | -12.0% |
| UEFA Champions League | over_1_5 | half_life_365 | 9 | 0.1625 | 0.4977 | +0.0027 | +0.0028 | -12.1% |
| UEFA Champions League | over_1_5 | half_life_730 | 9 | 0.1640 | 0.4993 | +0.0012 | +0.0012 | -12.3% |
| UEFA Champions League | over_1_5 | production_raw | 9 | 0.1652 | 0.5005 | +0.0000 | +0.0000 | -12.6% |
| UEFA Champions League | btts_yes | development_1x2 | 9 | 0.3117 | 0.8400 | +0.0000 | +0.0000 | -6.3% |
| UEFA Champions League | btts_yes | half_life_1000000000 | 9 | 0.3117 | 0.8400 | +0.0000 | +0.0000 | -6.3% |
| UEFA Champions League | btts_yes | half_life_120 | 9 | 0.2686 | 0.7470 | +0.0431 | +0.0930 | -4.3% |
| UEFA Champions League | btts_yes | half_life_240 | 9 | 0.2869 | 0.7854 | +0.0248 | +0.0547 | -5.6% |
| UEFA Champions League | btts_yes | half_life_365 | 9 | 0.2950 | 0.8026 | +0.0167 | +0.0374 | -6.0% |
| UEFA Champions League | btts_yes | half_life_730 | 9 | 0.3031 | 0.8200 | +0.0086 | +0.0200 | -6.2% |
| UEFA Champions League | btts_yes | production_raw | 9 | 0.3117 | 0.8400 | +0.0000 | +0.0000 | -6.3% |

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
| UEFA Champions League | over_1_5 | 120.0 | 152 | 30 | +0.0041 | {'240.0': 2, '120.0': 2} |
| UEFA Champions League | btts_yes | 730.0 | 152 | 30 | +0.0126 | {'240.0': 1, '1000000000.0': 3} |