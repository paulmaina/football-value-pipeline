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
| under_3_5 | 0.7035276570696158 | 0.6760316008033325 | 0.24912831147529585 | 0.24064991889726334 |
| btts_yes | 0.7073814968343807 | 0.689019709231292 | 0.2557411109303981 | 0.2476019579614575 |
| over_2_5 | 0.6941910625992758 | 0.6767165404104721 | 0.2500074021780875 | 0.24265345963906731 |

Primary familywise 95% gain interval: [-0.0057028192877419575, -0.0008359083935625122]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 40/300 | 2/6 | 0.9523809523809523 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9047197160402082 | 0.903217528863397 | 0.5307835697676195 | 0.5297813430276108 |
| over_1_5 | 0.5416434140317377 | 0.5388621417683004 | 0.17939142750924583 | 0.17875885814749953 |
| under_3_5 | 0.7035276570696158 | 0.6970196061749159 | 0.24912831147529585 | 0.2469964836501175 |
| btts_yes | 0.7073814968343807 | 0.6989990214366639 | 0.2557411109303981 | 0.2516204354800605 |
| over_2_5 | 0.6941910625992758 | 0.686260897623281 | 0.2500074021780875 | 0.24603177687829483 |

Primary familywise 95% gain interval: [-0.00016001654572931948, 0.016462020679675782]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

