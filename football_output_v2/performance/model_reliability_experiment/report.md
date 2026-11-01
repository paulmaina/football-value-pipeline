# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 103/300 | 3/6 | 0.8583333333333333 |

Excluded stronger_l2 forecasts (not comparable like for like): ValueError: 2, feature_application_differs: 19

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9387734808821063 | 0.9404286244502896 | 0.554222809462405 | 0.5550278840771011 |
| over_1_5 | 0.4997907600191055 | 0.5037351861676383 | 0.16122071193898332 | 0.1625545799111769 |
| under_3_5 | 0.641867199687539 | 0.6317635889398928 | 0.22307019511451798 | 0.21973983486461554 |
| btts_yes | 0.6982671748641993 | 0.6897667261706442 | 0.2519165370421495 | 0.24806854456100524 |
| over_2_5 | 0.6698957258653481 | 0.6663496743120372 | 0.2386477934279361 | 0.23726099597817366 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.0012794862284424835]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 83/300 | 3/6 | 0.6916666666666667 |

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

