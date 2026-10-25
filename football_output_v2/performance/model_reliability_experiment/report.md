# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 63/300 | 2/6 | 0.9692307692307692 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9505396777370705 | 0.952036864021591 | 0.5630345295576699 | 0.5636083858948872 |
| over_1_5 | 0.5432176472961374 | 0.5477981005363949 | 0.17856498643951985 | 0.1801687414595954 |
| under_3_5 | 0.6382881554016532 | 0.6206512432447951 | 0.22077818617528683 | 0.21491819959975988 |
| btts_yes | 0.7007773946177155 | 0.689055680873636 | 0.2529491537365934 | 0.24774261961687877 |
| over_2_5 | 0.6896450997638885 | 0.6825731341111594 | 0.24823641057589324 | 0.24530687699385148 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.00411032438644141]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 63/300 | 2/6 | 0.9692307692307692 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9505396777370705 | 0.9510075859049366 | 0.5630345295576699 | 0.5635811731065276 |
| over_1_5 | 0.5432176472961374 | 0.5326498807353828 | 0.17856498643951985 | 0.17470999119730163 |
| under_3_5 | 0.6382881554016532 | 0.6308794530569715 | 0.22077818617528683 | 0.2177157034291255 |
| btts_yes | 0.7007773946177155 | 0.6944515189450594 | 0.2529491537365934 | 0.24959636882124508 |
| over_2_5 | 0.6896450997638885 | 0.6797469032337835 | 0.24823641057589324 | 0.24326475815063167 |

Primary familywise 95% gain interval: [-0.0008784303307150685, -0.00016001654572931948]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

