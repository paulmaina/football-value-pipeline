# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 166/178 fixture-markets; 16 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 8 | 0.1564 | 0.4800 | +0.0000 | +0.0000 | -8.1% |
| ALL | over_1_5 | half_life_1000000000 | 8 | 0.1564 | 0.4800 | +0.0000 | +0.0000 | -8.1% |
| ALL | over_1_5 | half_life_120 | 8 | 0.1446 | 0.4841 | +0.0118 | -0.0041 | -5.8% |
| ALL | over_1_5 | half_life_240 | 8 | 0.1483 | 0.4710 | +0.0080 | +0.0089 | -7.0% |
| ALL | over_1_5 | half_life_365 | 8 | 0.1507 | 0.4716 | +0.0056 | +0.0083 | -7.3% |
| ALL | over_1_5 | half_life_730 | 8 | 0.1540 | 0.4766 | +0.0023 | +0.0034 | -7.7% |
| ALL | over_1_5 | production_raw | 8 | 0.1564 | 0.4800 | +0.0000 | +0.0000 | -8.1% |
| ALL | btts_yes | development_1x2 | 8 | 0.2676 | 0.7338 | +0.0000 | +0.0000 | +3.1% |
| ALL | btts_yes | half_life_1000000000 | 8 | 0.2676 | 0.7338 | +0.0000 | +0.0000 | +3.1% |
| ALL | btts_yes | half_life_120 | 8 | 0.2193 | 0.6300 | +0.0482 | +0.1038 | +5.3% |
| ALL | btts_yes | half_life_240 | 8 | 0.2399 | 0.6731 | +0.0277 | +0.0607 | +3.9% |
| ALL | btts_yes | half_life_365 | 8 | 0.2492 | 0.6932 | +0.0183 | +0.0406 | +3.5% |
| ALL | btts_yes | half_life_730 | 8 | 0.2586 | 0.7135 | +0.0090 | +0.0203 | +3.1% |
| ALL | btts_yes | production_raw | 8 | 0.2676 | 0.7338 | +0.0000 | +0.0000 | +3.1% |
| UEFA Champions League | over_1_5 | development_1x2 | 8 | 0.1564 | 0.4800 | +0.0000 | +0.0000 | -8.1% |
| UEFA Champions League | over_1_5 | half_life_1000000000 | 8 | 0.1564 | 0.4800 | +0.0000 | +0.0000 | -8.1% |
| UEFA Champions League | over_1_5 | half_life_120 | 8 | 0.1446 | 0.4841 | +0.0118 | -0.0041 | -5.8% |
| UEFA Champions League | over_1_5 | half_life_240 | 8 | 0.1483 | 0.4710 | +0.0080 | +0.0089 | -7.0% |
| UEFA Champions League | over_1_5 | half_life_365 | 8 | 0.1507 | 0.4716 | +0.0056 | +0.0083 | -7.3% |
| UEFA Champions League | over_1_5 | half_life_730 | 8 | 0.1540 | 0.4766 | +0.0023 | +0.0034 | -7.7% |
| UEFA Champions League | over_1_5 | production_raw | 8 | 0.1564 | 0.4800 | +0.0000 | +0.0000 | -8.1% |
| UEFA Champions League | btts_yes | development_1x2 | 8 | 0.2676 | 0.7338 | +0.0000 | +0.0000 | +3.1% |
| UEFA Champions League | btts_yes | half_life_1000000000 | 8 | 0.2676 | 0.7338 | +0.0000 | +0.0000 | +3.1% |
| UEFA Champions League | btts_yes | half_life_120 | 8 | 0.2193 | 0.6300 | +0.0482 | +0.1038 | +5.3% |
| UEFA Champions League | btts_yes | half_life_240 | 8 | 0.2399 | 0.6731 | +0.0277 | +0.0607 | +3.9% |
| UEFA Champions League | btts_yes | half_life_365 | 8 | 0.2492 | 0.6932 | +0.0183 | +0.0406 | +3.5% |
| UEFA Champions League | btts_yes | half_life_730 | 8 | 0.2586 | 0.7135 | +0.0090 | +0.0203 | +3.1% |
| UEFA Champions League | btts_yes | production_raw | 8 | 0.2676 | 0.7338 | +0.0000 | +0.0000 | +3.1% |

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
| UEFA Champions League | over_1_5 | 240.0 | 152 | 28 | +0.0117 | {'240.0': 2, '120.0': 2} |
| UEFA Champions League | btts_yes | 730.0 | 152 | 28 | +0.0128 | {'120.0': 1, '730.0': 1, '1000000000.0': 2} |