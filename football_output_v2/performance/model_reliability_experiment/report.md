# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 3/300 | 1/6 | 0.75 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 1.103345720525847 | 1.0953653920848196 | 0.6750237396909681 | 0.6691029207623796 |
| over_1_5 | 0.18726262951440384 | 0.22006551231193724 | 0.029722140450067127 | 0.03936053474793749 |
| under_3_5 | 0.734391011136497 | 0.7018280859036037 | 0.2683520677781895 | 0.25161118587352915 |
| btts_yes | 0.6832021675776464 | 0.6755040276085916 | 0.24394847263559336 | 0.24087752416529415 |
| over_2_5 | 0.685231211937792 | 0.6906294200873427 | 0.24547723355159481 | 0.24851948869644933 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 3/300 | 1/6 | 0.75 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 1.103345720525847 | 1.1229583902584779 | 0.6750237396909681 | 0.6899757090781004 |
| over_1_5 | 0.18726262951440384 | 0.17723334073454863 | 0.029722140450067127 | 0.02664264732665435 |
| under_3_5 | 0.734391011136497 | 0.7136624390670895 | 0.2683520677781895 | 0.2590928148477887 |
| btts_yes | 0.6832021675776464 | 0.6727640585798412 | 0.24394847263559336 | 0.23879957049418843 |
| over_2_5 | 0.685231211937792 | 0.6674756484304184 | 0.24547723355159481 | 0.2368606705540727 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

