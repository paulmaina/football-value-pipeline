# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 115/300 | 3/6 | 0.8518518518518519 |

Excluded stronger_l2 forecasts (not comparable like for like): ValueError: 2, feature_application_differs: 19

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.912764126824062 | 0.9150865679223178 | 0.535648704861361 | 0.536923986760478 |
| over_1_5 | 0.4823250337419929 | 0.48618802973009567 | 0.1539927381609508 | 0.15520372735878388 |
| under_3_5 | 0.6402652621935138 | 0.6287094506365746 | 0.22282345637747075 | 0.21866428592528153 |
| btts_yes | 0.7077067140357635 | 0.6984756079045983 | 0.2565238385782437 | 0.2523422965369968 |
| over_2_5 | 0.6756249379464239 | 0.6717448029691463 | 0.2416153376210839 | 0.2399678026143937 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.0012794862284424835]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 83/300 | 3/6 | 0.6148148148148148 |

Excluded fixed_half_life forecasts (not comparable like for like): ValueError: 2, candidate_equals_production_half_life: 63

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9580523985281798 | 0.9587546816256675 | 0.5695186460850841 | 0.5703416151933064 |
| over_1_5 | 0.5189973111834616 | 0.513815667823398 | 0.16958717981777177 | 0.16770141852614825 |
| under_3_5 | 0.5978448143242985 | 0.5936462846726691 | 0.20294310713428015 | 0.20119360595066546 |
| btts_yes | 0.6956304549765588 | 0.6897569330659802 | 0.25049319669288045 | 0.24744015373031572 |
| over_2_5 | 0.66762481739547 | 0.660724371889156 | 0.23763732148201008 | 0.2342501747815382 |

Primary familywise 95% gain interval: [-0.012012894841159194, -0.00016001654572931948]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

