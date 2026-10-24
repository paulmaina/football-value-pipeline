# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 47/300 | 2/6 | 0.9591836734693877 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9434554545370583 | 0.9467037454183836 | 0.5594029437691178 | 0.5610150966671449 |
| over_1_5 | 0.501134967386052 | 0.502587695500607 | 0.16185385020010495 | 0.16184406284361244 |
| under_3_5 | 0.6882482778601091 | 0.6614916527747668 | 0.24304176444814685 | 0.23405595700957507 |
| btts_yes | 0.6932466611908807 | 0.676118566234251 | 0.24924742837910932 | 0.2414716447174298 |
| over_2_5 | 0.6792138573404265 | 0.6665253820962923 | 0.2431237282444866 | 0.23774401754042038 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.004784711176037515]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 47/300 | 2/6 | 0.9591836734693877 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9434554545370583 | 0.9479077931819909 | 0.5594029437691178 | 0.56239979991594 |
| over_1_5 | 0.501134967386052 | 0.49640868147864586 | 0.16185385020010495 | 0.16023156024961743 |
| under_3_5 | 0.6882482778601091 | 0.6784462442872548 | 0.24304176444814685 | 0.23915768012522565 |
| btts_yes | 0.6932466611908807 | 0.6839024188861156 | 0.24924742837910932 | 0.24452785118376644 |
| over_2_5 | 0.6792138573404265 | 0.6688522279001924 | 0.2431237282444866 | 0.23782030296588805 |

Primary familywise 95% gain interval: [-0.018499938242325834, -0.00016001654572931948]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

