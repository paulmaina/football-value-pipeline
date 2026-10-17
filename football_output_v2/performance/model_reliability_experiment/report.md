# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 5/300 | 1/6 | 0.8333333333333334 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9712405443566208 | 0.970034022871747 | 0.5791760612565483 | 0.5783233374580898 |
| over_1_5 | 0.4314508214406674 | 0.4498926319458712 | 0.13700370607138518 | 0.14231658968445826 |
| under_3_5 | 0.5747657568329346 | 0.5555439489439491 | 0.19354152992975637 | 0.18364162815527812 |
| btts_yes | 0.721701331614736 | 0.7184579322779168 | 0.2635247898844604 | 0.26236278243672784 |
| over_2_5 | 0.6953256548770756 | 0.6990029076580744 | 0.25074414584117755 | 0.25278708709688363 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 5/300 | 1/6 | 0.8333333333333334 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9712405443566208 | 0.9782333693749722 | 0.5791760612565483 | 0.5844849959275015 |
| over_1_5 | 0.4314508214406674 | 0.4347482678535311 | 0.13700370607138518 | 0.13856487548447188 |
| under_3_5 | 0.5747657568329346 | 0.5542600667881669 | 0.19354152992975637 | 0.18468631220727297 |
| btts_yes | 0.721701331614736 | 0.7031847338113327 | 0.2635247898844604 | 0.25439513611847747 |
| over_2_5 | 0.6953256548770756 | 0.6716951615388964 | 0.25074414584117755 | 0.23909211622710017 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

