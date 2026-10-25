# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 49/300 | 2/6 | 0.9607843137254902 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.939936555595269 | 0.9433115811807616 | 0.5564316909282107 | 0.5581440329384071 |
| over_1_5 | 0.49679718599198663 | 0.49787250066490757 | 0.1595929990152957 | 0.1594438649249793 |
| under_3_5 | 0.6984642903227287 | 0.6722603917826105 | 0.247287986292343 | 0.23850025248519383 |
| btts_yes | 0.6995751180110332 | 0.6824064169460555 | 0.2524095281530291 | 0.24459038826182206 |
| over_2_5 | 0.6879991706874631 | 0.6752141893776552 | 0.24746254937375467 | 0.24200545958647235 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.0030711723591977935]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 49/300 | 2/6 | 0.9607843137254902 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.939936555595269 | 0.9441811750547808 | 0.5564316909282107 | 0.5592971851894402 |
| over_1_5 | 0.49679718599198663 | 0.49309209940185955 | 0.1595929990152957 | 0.15840375485221642 |
| under_3_5 | 0.6984642903227287 | 0.6895167572475591 | 0.247287986292343 | 0.24369676501163345 |
| btts_yes | 0.6995751180110332 | 0.6918634356292168 | 0.2524095281530291 | 0.24848607741180417 |
| over_2_5 | 0.6879991706874631 | 0.6795221680699328 | 0.24746254937375467 | 0.2430793167174477 |

Primary familywise 95% gain interval: [-0.01555582752844777, -0.00016001654572931948]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

