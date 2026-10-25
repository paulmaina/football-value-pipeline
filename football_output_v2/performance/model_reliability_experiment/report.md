# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 64/300 | 2/6 | 0.9696969696969697 |

Excluded stronger_l2 forecasts (not comparable like for like): ValueError: 2

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9411274103625723 | 0.9427149033048792 | 0.5562844366098294 | 0.5569196122176207 |
| over_1_5 | 0.5372606385006261 | 0.541817761544939 | 0.1761242830497626 | 0.1777153373158015 |
| under_3_5 | 0.6371263569722706 | 0.6196304851725707 | 0.22023148875868773 | 0.21439716944093037 |
| btts_yes | 0.6990447461137494 | 0.687452068579973 | 0.25209946034765013 | 0.2469475521597116 |
| over_2_5 | 0.685554409488914 | 0.6786900800692972 | 0.24625088993247013 | 0.24341133351802005 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.0037036409303954055]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 64/300 | 2/6 | 0.9696969696969697 |

Excluded fixed_half_life forecasts (not comparable like for like): ValueError: 2

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9411274103625723 | 0.9413954301705 | 0.5562844366098294 | 0.5567027441704494 |
| over_1_5 | 0.5372606385006261 | 0.5266665206140183 | 0.1761242830497626 | 0.17228224041500464 |
| under_3_5 | 0.6371263569722706 | 0.630445401960845 | 0.22023148875868773 | 0.21751868879379274 |
| btts_yes | 0.6990447461137494 | 0.6926059139050217 | 0.25209946034765013 | 0.24869459858825999 |
| over_2_5 | 0.685554409488914 | 0.6753815970617048 | 0.24625088993247013 | 0.2411645470313376 |

Primary familywise 95% gain interval: [-0.00040688114503984504, -0.00016001654572931948]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

