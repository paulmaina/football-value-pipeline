# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 10/300 | 1/6 | 0.8333333333333334 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 1.133202224942631 | 1.1284003042355928 | 0.6944050319383143 | 0.6907343639172686 |
| over_1_5 | 0.6846475895309417 | 0.7040391917377875 | 0.2465499011860576 | 0.2538079670753318 |
| under_3_5 | 0.6872999544711936 | 0.6370740175458717 | 0.23469658557618794 | 0.22059076414307213 |
| btts_yes | 0.7046551693948995 | 0.6954787532951703 | 0.2547849488789396 | 0.2510986613292686 |
| over_2_5 | 0.7134534154001082 | 0.6998835209684897 | 0.25928074382583544 | 0.2533338908276762 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 10/300 | 1/6 | 0.8333333333333334 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 1.133202224942631 | 1.1304742428869592 | 0.6944050319383143 | 0.6932064512184286 |
| over_1_5 | 0.6846475895309417 | 0.6712769613212219 | 0.2465499011860576 | 0.2419952018167247 |
| under_3_5 | 0.6872999544711936 | 0.6719773018545917 | 0.23469658557618794 | 0.22780835493077736 |
| btts_yes | 0.7046551693948995 | 0.6933582732894055 | 0.2547849488789396 | 0.24915710444063235 |
| over_2_5 | 0.7134534154001082 | 0.6922501585561667 | 0.25928074382583544 | 0.24862762904811975 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

