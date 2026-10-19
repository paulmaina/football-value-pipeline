# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 40/300 | 2/6 | 0.9523809523809523 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9047197160402082 | 0.9099358442385321 | 0.5307835697676195 | 0.5343245146134239 |
| over_1_5 | 0.5416434140317377 | 0.5431993888005753 | 0.17939142750924583 | 0.1796032852865904 |
| under_3_5 | 0.7444482571110613 | 0.7146518230843406 | 0.26598342724459256 | 0.2568580543685013 |
| btts_yes | 0.7149196614812239 | 0.6949160590549514 | 0.2594818939773659 | 0.25053654193422 |
| over_2_5 | 0.6941910625992758 | 0.6767165404104721 | 0.2500074021780875 | 0.24265345963906731 |

Primary familywise 95% gain interval: [-0.0057028192877419575, -0.0008359083935625122]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 40/300 | 2/6 | 0.9523809523809523 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9047197160402082 | 0.903217528863397 | 0.5307835697676195 | 0.5297813430276108 |
| over_1_5 | 0.5416434140317377 | 0.5388621417683004 | 0.17939142750924583 | 0.17875885814749953 |
| under_3_5 | 0.7444482571110613 | 0.7383031797521877 | 0.26598342724459256 | 0.2639501071713145 |
| btts_yes | 0.7149196614812239 | 0.7065691906567554 | 0.2594818939773659 | 0.25537686102959645 |
| over_2_5 | 0.6941910625992758 | 0.686260897623281 | 0.2500074021780875 | 0.24603177687829483 |

Primary familywise 95% gain interval: [-0.00016001654572931948, 0.016462020679675782]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

