# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 36/300 | 1/6 | 0.9473684210526315 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9011383730502769 | 0.9068411923380189 | 0.5283199663452485 | 0.5322228216360647 |
| over_1_5 | 0.5526680450555359 | 0.5566269509619138 | 0.1846119722941059 | 0.1858879128043605 |
| under_3_5 | 0.7010837157239804 | 0.671428556002847 | 0.2461312716378004 | 0.23713195140428958 |
| btts_yes | 0.6962643543348879 | 0.6785190060968138 | 0.25038754080527753 | 0.24258366592120206 |
| over_2_5 | 0.6955127428034129 | 0.6778094558036555 | 0.25025568392175385 | 0.2429672527492691 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 36/300 | 1/6 | 0.9473684210526315 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9011383730502769 | 0.9012983895960063 | 0.5283199663452485 | 0.5285929196878043 |
| over_1_5 | 0.5526680450555359 | 0.5492319004496549 | 0.1846119722941059 | 0.18374082013947116 |
| under_3_5 | 0.7010837157239804 | 0.6938340604663051 | 0.2461312716378004 | 0.24369987348576774 |
| btts_yes | 0.6962643543348879 | 0.689493387058686 | 0.25038754080527753 | 0.2470992800144533 |
| over_2_5 | 0.6955127428034129 | 0.6864815474314915 | 0.25025568392175385 | 0.24571528645438123 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

