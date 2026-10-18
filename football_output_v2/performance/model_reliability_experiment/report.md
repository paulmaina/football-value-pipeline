# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 23/300 | 1/6 | 0.92 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9459967897102702 | 0.9479581443422384 | 0.5626732528135941 | 0.5635520178839535 |
| over_1_5 | 0.6087639518988864 | 0.6195415012853231 | 0.2081725497184024 | 0.21290097183191184 |
| under_3_5 | 0.6264195823019955 | 0.6094213609840313 | 0.2141260766940297 | 0.20996374164937276 |
| btts_yes | 0.6649675721028203 | 0.6559704132181993 | 0.2356125816657597 | 0.23158667451600912 |
| over_2_5 | 0.6559176478728305 | 0.6523222503291489 | 0.23264275611798765 | 0.23098392909525195 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 23/300 | 1/6 | 0.92 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9459967897102702 | 0.9432672166914569 | 0.5626732528135941 | 0.5610904310369227 |
| over_1_5 | 0.6087639518988864 | 0.6052083455244306 | 0.2081725497184024 | 0.2074312188905519 |
| under_3_5 | 0.6264195823019955 | 0.6218970059936101 | 0.2141260766940297 | 0.21233293929561162 |
| btts_yes | 0.6649675721028203 | 0.6607015083103746 | 0.2356125816657597 | 0.2335786691110243 |
| over_2_5 | 0.6559176478728305 | 0.6481323417079007 | 0.23264275611798765 | 0.22860533193512378 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

