# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 57/300 | 2/6 | 0.9661016949152542 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9455486508800879 | 0.948564864600293 | 0.5597609030460673 | 0.5614225585852685 |
| over_1_5 | 0.5095853389879169 | 0.5097879218641996 | 0.16484279261335272 | 0.16450589722257164 |
| under_3_5 | 0.6508404547339169 | 0.6282398870220016 | 0.22583081084413822 | 0.2181341169635107 |
| btts_yes | 0.6927064017731264 | 0.6788538582641072 | 0.24910434258606626 | 0.24281708464113733 |
| over_2_5 | 0.695040718584963 | 0.6835980968280466 | 0.25084901908346924 | 0.2459677207876209 |

Primary familywise 95% gain interval: [-0.0057028192877419575, 0.0015893958241439317]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 57/300 | 2/6 | 0.9661016949152542 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9455486508800879 | 0.9461603355100762 | 0.5597609030460673 | 0.5603691885352126 |
| over_1_5 | 0.5095853389879169 | 0.5050726728965745 | 0.16484279261335272 | 0.16328292320051624 |
| under_3_5 | 0.6508404547339169 | 0.6447154786396161 | 0.22583081084413822 | 0.22328829879485043 |
| btts_yes | 0.6927064017731264 | 0.6879272466343407 | 0.24910434258606626 | 0.2466222850773363 |
| over_2_5 | 0.695040718584963 | 0.6867805495416895 | 0.25084901908346924 | 0.24660713088366418 |

Primary familywise 95% gain interval: [-0.0013859727744319444, -0.00016001654572931948]
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

