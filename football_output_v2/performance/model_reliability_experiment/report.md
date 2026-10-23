# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 45/300 | 2/6 | 0.9574468085106383 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.944693140830745 | 0.9485221319767719 | 0.560036658078628 | 0.562103612399743 |
| over_1_5 | 0.5136876982699092 | 0.5143813971129596 | 0.16698135068464187 | 0.16681556995530358 |
| under_3_5 | 0.6940690747759358 | 0.6699742846172099 | 0.24536135868299713 | 0.23788914070480516 |
| btts_yes | 0.702453686740614 | 0.6830059390961428 | 0.25345036231242385 | 0.2447136479246624 |
| over_2_5 | 0.6903721062342387 | 0.6752151293136119 | 0.24832520277311285 | 0.2419538588867203 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.0036663214208331064]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 45/300 | 2/6 | 0.9574468085106383 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.944693140830745 | 0.9492735399768978 | 0.560036658078628 | 0.5631542971007267 |
| over_1_5 | 0.5136876982699092 | 0.5080038847719615 | 0.16698135068464187 | 0.1650894466081312 |
| under_3_5 | 0.6940690747759358 | 0.6865369289193665 | 0.24536135868299713 | 0.24261242699303207 |
| btts_yes | 0.702453686740614 | 0.692098048247974 | 0.25345036231242385 | 0.24832939529971979 |
| over_2_5 | 0.6903721062342387 | 0.6787756104896389 | 0.24832520277311285 | 0.24252874224842774 |

Primary familywise 95% gain interval: [-0.02226192954784672, -0.00016001654572931948]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

