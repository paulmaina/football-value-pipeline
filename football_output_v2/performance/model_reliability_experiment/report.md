# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 82/300 | 2/6 | 0.9761904761904762 |

Excluded stronger_l2 forecasts (not comparable like for like): ValueError: 2

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9611684354616146 | 0.9629543516549115 | 0.5717995637541881 | 0.5726136807682014 |
| over_1_5 | 0.5211151046710139 | 0.5254091598100753 | 0.1706153748309989 | 0.17205188597993837 |
| under_3_5 | 0.601872386022978 | 0.5885813673319253 | 0.2047458427730488 | 0.20020665913077026 |
| btts_yes | 0.6960254773343879 | 0.6870290474757433 | 0.25068152493369145 | 0.24666522291101062 |
| over_2_5 | 0.6685494258855952 | 0.6641677542575044 | 0.238102201512648 | 0.23636189708671984 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.0012794862284424835]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 82/300 | 2/6 | 0.9761904761904762 |

Excluded fixed_half_life forecasts (not comparable like for like): ValueError: 2

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9611684354616146 | 0.9617327842695453 | 0.5717995637541881 | 0.5725259855460051 |
| over_1_5 | 0.5211151046710139 | 0.5164225360385497 | 0.1706153748309989 | 0.16892710233147287 |
| under_3_5 | 0.601872386022978 | 0.5970644976458801 | 0.2047458427730488 | 0.20276468252637259 |
| btts_yes | 0.6960254773343879 | 0.689146045513345 | 0.25068152493369145 | 0.24712436450174435 |
| over_2_5 | 0.6685494258855952 | 0.6606622800037478 | 0.238102201512648 | 0.23422471549408655 |

Primary familywise 95% gain interval: [-0.0008807827522623999, -0.00016001654572931948]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

