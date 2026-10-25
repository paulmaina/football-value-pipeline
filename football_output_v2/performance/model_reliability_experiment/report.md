# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 79/300 | 2/6 | 0.9753086419753086 |

Excluded stronger_l2 forecasts (not comparable like for like): ValueError: 2

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9652269304007923 | 0.9668867353788748 | 0.5744948769230404 | 0.5751943945897208 |
| over_1_5 | 0.5330191245083884 | 0.5373700307625803 | 0.17572155980342424 | 0.17717777631063034 |
| under_3_5 | 0.6069163710478703 | 0.5932935560757014 | 0.20714824376266036 | 0.2025139285820248 |
| btts_yes | 0.7004901117402039 | 0.691051340287572 | 0.2528410739647716 | 0.24862240872615776 |
| over_2_5 | 0.6732499786851309 | 0.6686332429369792 | 0.24039194756423485 | 0.2385523249723706 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.0017250442114002099]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 79/300 | 2/6 | 0.9753086419753086 |

Excluded fixed_half_life forecasts (not comparable like for like): ValueError: 2

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9652269304007923 | 0.9653601449871891 | 0.5744948769230404 | 0.5749285331721379 |
| over_1_5 | 0.5330191245083884 | 0.5284454543583741 | 0.17572155980342424 | 0.17404133303607824 |
| under_3_5 | 0.6069163710478703 | 0.6010708970134017 | 0.20714824376266036 | 0.20467081886373859 |
| btts_yes | 0.7004901117402039 | 0.6941112470213713 | 0.2528410739647716 | 0.24951197152994628 |
| over_2_5 | 0.6732499786851309 | 0.6659113093696625 | 0.24039194756423485 | 0.23675991780353098 |

Primary familywise 95% gain interval: [-0.00016001654572931948, -0.00011077573672297685]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

