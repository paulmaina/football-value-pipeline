# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 28/300 | 1/6 | 0.9333333333333333 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9049258987147344 | 0.9089812220003992 | 0.5312744688620585 | 0.5337326397365157 |
| over_1_5 | 0.5345763064494814 | 0.5447580876747479 | 0.17709839832388807 | 0.18115776660897925 |
| under_3_5 | 0.6305608747024113 | 0.6092508213744352 | 0.21714870056244387 | 0.2100773383443121 |
| btts_yes | 0.6907388766939748 | 0.6766691374313731 | 0.24735456391724894 | 0.24143856318164625 |
| over_2_5 | 0.6780873317493954 | 0.6660754649031482 | 0.24154186411083386 | 0.23704021507826264 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 28/300 | 1/6 | 0.9333333333333333 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9049258987147344 | 0.9059774104877992 | 0.5312744688620585 | 0.532308763015279 |
| over_1_5 | 0.5345763064494814 | 0.5333186868727645 | 0.17709839832388807 | 0.17708141737454747 |
| under_3_5 | 0.6305608747024113 | 0.6291607178664794 | 0.21714870056244387 | 0.21680448648725154 |
| btts_yes | 0.6907388766939748 | 0.6859605866057162 | 0.24735456391724894 | 0.2450077066872775 |
| over_2_5 | 0.6780873317493954 | 0.6716713723242485 | 0.24154186411083386 | 0.2381618599414664 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

