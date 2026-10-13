# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 126/134 fixture-markets; 0 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|

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