# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 84/300 | 3/6 | 0.9767441860465116 |

Excluded stronger_l2 forecasts (not comparable like for like): ValueError: 2

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9558823337635215 | 0.9577153158424155 | 0.5679456063891146 | 0.5688077025270633 |
| over_1_5 | 0.5160808498329457 | 0.5203127554234571 | 0.16825216600881493 | 0.1696687426845139 |
| under_3_5 | 0.6053118302601275 | 0.5924924468606234 | 0.20646531958900868 | 0.20209793688360306 |
| btts_yes | 0.6945665718414761 | 0.6858478535557929 | 0.24997155475886704 | 0.24608245138545656 |
| over_2_5 | 0.6675635791210838 | 0.6633874981180463 | 0.23760201681703175 | 0.23595367281139104 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.0012794862284424835]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 83/300 | 3/6 | 0.9651162790697675 |

Excluded fixed_half_life forecasts (not comparable like for like): ValueError: 2, candidate_equals_production_half_life: 10

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

