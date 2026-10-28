# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 85/300 | 3/6 | 0.9770114942528736 |

Excluded stronger_l2 forecasts (not comparable like for like): ValueError: 2, feature_application_differs: 1

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9485458470129915 | 0.950437023982131 | 0.5626966317185808 | 0.5635963625121537 |
| over_1_5 | 0.5133823630427314 | 0.5175754625809164 | 0.16700373617661166 | 0.16840776097451857 |
| under_3_5 | 0.6131442939473947 | 0.6005148084316092 | 0.21012614786314385 | 0.2058259060821681 |
| btts_yes | 0.6965939960767545 | 0.6877500082339149 | 0.2509849038233313 | 0.24703024372600893 |
| over_2_5 | 0.6676459466507051 | 0.6635259859221885 | 0.2376385801927341 | 0.23601312223415216 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.0012794862284424835]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 83/300 | 3/6 | 0.9540229885057471 |

Excluded fixed_half_life forecasts (not comparable like for like): ValueError: 2, candidate_equals_production_half_life: 15

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

