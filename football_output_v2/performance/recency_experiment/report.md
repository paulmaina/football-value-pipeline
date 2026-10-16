# Goal recency experiment

Same-snapshot raw baseline; paired available variants, not identical cohorts across variants. Historical audit periods overlap across runs and must not be added together. Approximate intervals assume independent fixtures, do not adjust for multiple comparisons and do not prove profitability. No automatic promotion.

Coverage: 268/284 fixture-markets; 36 graded.
Rejected snapshot data: 0 commit(s); details in summary.json.

| League | Market | Variant | N | Brier | Log loss | Brier gain | Log-loss gain | Overconfidence |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ALL | over_1_5 | development_1x2 | 18 | 0.1372 | 0.4420 | +0.0006 | +0.0020 | -8.3% |
| ALL | over_1_5 | goal_selected | 3 | 0.0275 | 0.1780 | +0.0017 | +0.0072 | -16.2% |
| ALL | over_1_5 | half_life_1000000000 | 18 | 0.1370 | 0.4416 | +0.0008 | +0.0024 | -8.3% |
| ALL | over_1_5 | half_life_120 | 18 | 0.1386 | 0.4753 | -0.0008 | -0.0313 | -5.9% |
| ALL | over_1_5 | half_life_240 | 18 | 0.1377 | 0.4578 | +0.0001 | -0.0138 | -7.0% |
| ALL | over_1_5 | half_life_365 | 18 | 0.1376 | 0.4521 | +0.0002 | -0.0080 | -7.5% |
| ALL | over_1_5 | half_life_730 | 18 | 0.1376 | 0.4473 | +0.0002 | -0.0032 | -7.9% |
| ALL | over_1_5 | production_raw | 18 | 0.1378 | 0.4441 | +0.0000 | +0.0000 | -8.5% |
| ALL | btts_yes | development_1x2 | 18 | 0.2812 | 0.7693 | -0.0006 | -0.0016 | +0.3% |
| ALL | btts_yes | goal_selected | 3 | 0.2297 | 0.6528 | +0.0137 | +0.0292 | -2.6% |
| ALL | btts_yes | half_life_1000000000 | 18 | 0.2779 | 0.7620 | +0.0027 | +0.0057 | +0.4% |
| ALL | btts_yes | half_life_120 | 18 | 0.3062 | 0.8287 | -0.0256 | -0.0609 | +0.2% |
| ALL | btts_yes | half_life_240 | 18 | 0.2928 | 0.7949 | -0.0122 | -0.0272 | -0.1% |
| ALL | btts_yes | half_life_365 | 18 | 0.2843 | 0.7768 | -0.0037 | -0.0090 | +0.2% |
| ALL | btts_yes | half_life_730 | 18 | 0.2797 | 0.7662 | +0.0009 | +0.0016 | +0.4% |
| ALL | btts_yes | production_raw | 18 | 0.2806 | 0.7678 | +0.0000 | +0.0000 | +0.1% |
| La Liga | over_1_5 | development_1x2 | 1 | 0.0218 | 0.1598 | +0.0005 | +0.0021 | -14.8% |
| La Liga | over_1_5 | goal_selected | 1 | 0.0160 | 0.1353 | +0.0063 | +0.0266 | -12.7% |
| La Liga | over_1_5 | half_life_1000000000 | 1 | 0.0224 | 0.1621 | -0.0001 | -0.0003 | -15.0% |
| La Liga | over_1_5 | half_life_120 | 1 | 0.0160 | 0.1353 | +0.0063 | +0.0266 | -12.7% |
| La Liga | over_1_5 | half_life_240 | 1 | 0.0208 | 0.1558 | +0.0015 | +0.0060 | -14.4% |
| La Liga | over_1_5 | half_life_365 | 1 | 0.0218 | 0.1598 | +0.0005 | +0.0021 | -14.8% |
| La Liga | over_1_5 | half_life_730 | 1 | 0.0223 | 0.1618 | +0.0000 | +0.0000 | -14.9% |
| La Liga | over_1_5 | production_raw | 1 | 0.0223 | 0.1618 | +0.0000 | +0.0000 | -14.9% |
| La Liga | btts_yes | development_1x2 | 1 | 0.1283 | 0.4435 | +0.0015 | +0.0032 | -35.8% |
| La Liga | btts_yes | goal_selected | 1 | 0.1252 | 0.4368 | +0.0046 | +0.0100 | -35.4% |
| La Liga | btts_yes | half_life_1000000000 | 1 | 0.1299 | 0.4470 | -0.0001 | -0.0003 | -36.0% |
| La Liga | btts_yes | half_life_120 | 1 | 0.1084 | 0.3993 | +0.0214 | +0.0474 | -32.9% |
| La Liga | btts_yes | half_life_240 | 1 | 0.1252 | 0.4368 | +0.0046 | +0.0100 | -35.4% |
| La Liga | btts_yes | half_life_365 | 1 | 0.1283 | 0.4435 | +0.0015 | +0.0032 | -35.8% |
| La Liga | btts_yes | half_life_730 | 1 | 0.1298 | 0.4467 | +0.0000 | +0.0000 | -36.0% |
| La Liga | btts_yes | production_raw | 1 | 0.1298 | 0.4467 | +0.0000 | +0.0000 | -36.0% |
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
| Premier League | over_1_5 | 1000000000.0 | 310 | 60 | +0.0039 | {'240.0': 1, '1000000000.0': 3} |
| Premier League | btts_yes | 730.0 | 310 | 60 | -0.0000 | {'1000000000.0': 2, '365.0': 1, '120.0': 1} |
| La Liga | over_1_5 | 120.0 | 300 | 78 | +0.0002 | {'120.0': 4} |
| La Liga | btts_yes | 240.0 | 300 | 78 | +0.0025 | {'730.0': 1, '120.0': 3} |
| Bundesliga | over_1_5 | 365.0 | 252 | 46 | -0.0103 | {'730.0': 1, '1000000000.0': 2, '120.0': 1} |
| Bundesliga | btts_yes | 240.0 | 252 | 46 | -0.0051 | {'120.0': 2, '730.0': 1, '240.0': 1} |
| Serie A | over_1_5 | 240.0 | 320 | 60 | -0.0010 | {'120.0': 2, '1000000000.0': 1, '365.0': 1} |
| Serie A | btts_yes | 730.0 | 320 | 60 | -0.0017 | {'1000000000.0': 2, '120.0': 1, '365.0': 1} |
| Ligue 1 | over_1_5 | 1000000000.0 | 243 | 54 | -0.0175 | {'1000000000.0': 3, '120.0': 1} |
| Ligue 1 | btts_yes | 1000000000.0 | 243 | 54 | -0.0041 | {'1000000000.0': 3, '120.0': 1} |
| UEFA Champions League | over_1_5 | 120.0 | 152 | 37 | -0.0230 | {'240.0': 2, '120.0': 2} |
| UEFA Champions League | btts_yes | 730.0 | 152 | 37 | +0.0030 | {'240.0': 1, '1000000000.0': 3} |