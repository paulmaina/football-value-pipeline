# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 33/300 | 1/6 | 0.9428571428571428 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.902356006542193 | 0.9092978900473897 | 0.5293262373866875 | 0.5339759633309471 |
| over_1_5 | 0.5818406031003389 | 0.5864172939117575 | 0.19685147921248045 | 0.19840864528216334 |
| under_3_5 | 0.7126088691888988 | 0.6799573334894419 | 0.2503691367263048 | 0.2404742825175004 |
| btts_yes | 0.7102573037814804 | 0.6902482307661906 | 0.25697732998237455 | 0.24816523486079045 |
| over_2_5 | 0.707516124117426 | 0.6886437844309726 | 0.255822868413931 | 0.2481089872549605 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 33/300 | 1/6 | 0.9428571428571428 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.902356006542193 | 0.9026152339684719 | 0.5293262373866875 | 0.5297478753851798 |
| over_1_5 | 0.5818406031003389 | 0.5783265451454737 | 0.19685147921248045 | 0.19602864295434783 |
| under_3_5 | 0.7126088691888988 | 0.7048955931484762 | 0.2503691367263048 | 0.24784386578940792 |
| btts_yes | 0.7102573037814804 | 0.7025413586458241 | 0.25697732998237455 | 0.2532438318179456 |
| over_2_5 | 0.707516124117426 | 0.6979561540959183 | 0.255822868413931 | 0.2510211309555593 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

