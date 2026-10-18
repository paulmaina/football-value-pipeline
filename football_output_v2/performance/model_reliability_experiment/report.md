# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 24/300 | 1/6 | 0.9230769230769231 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9308424559962698 | 0.9340427880912326 | 0.5514055452157275 | 0.5532277916802179 |
| over_1_5 | 0.5865032670723838 | 0.5984745555466916 | 0.1997134921693892 | 0.20451325700126413 |
| under_3_5 | 0.640666699928418 | 0.6148607102652341 | 0.22123586784115856 | 0.2126066176251313 |
| btts_yes | 0.6953259787858413 | 0.6783454633680712 | 0.2493462865410541 | 0.24216077163011773 |
| over_2_5 | 0.6939293354264192 | 0.6781594842909499 | 0.24905756978949908 | 0.2429503603498692 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 24/300 | 1/6 | 0.9230769230769231 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9308424559962698 | 0.9284344694753398 | 0.5514055452157275 | 0.5500429960000527 |
| over_1_5 | 0.5865032670723838 | 0.5830596910248547 | 0.1997134921693892 | 0.19899826066028478 |
| under_3_5 | 0.640666699928418 | 0.6365899661056013 | 0.22123586784115856 | 0.21963855031853 |
| btts_yes | 0.6953259787858413 | 0.6917497349073014 | 0.2493462865410541 | 0.2475874277297236 |
| over_2_5 | 0.6939293354264192 | 0.6868099845707415 | 0.24905756978949908 | 0.24530073609578376 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

