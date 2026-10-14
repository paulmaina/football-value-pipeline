# Conservative EV sensitivity experiment

One unit per simulated selection, net of frozen costs; simultaneous kickoff P&L grouped for drawdown. First eligible fixture snapshot freezes all policies and rejections. Different policies may select different markets/cohorts; results are not paired probability tests. Four weeks or 30 selections do not establish profitability. No automatic promotion; validate a chosen policy on later untouched data.

Frozen fixtures: 20; candidate decisions: 360; rejected snapshots: 0.

| EV floor | Tier | Selected | Settled | Pending | Net ROI | Drawdown (units) | Brier |
|---|---|---:|---:|---:|---:|---:|---:|
| 1.5% | ALL | 5 | 1 | 4 | +18.0% | 0.00 | 0.0030 |
| 1.5% | STRICT | 5 | 1 | 4 | +18.0% | 0.00 | 0.0030 |
| 1.5% | PROVISIONAL | 0 | 0 | 0 | n.a. | n.a. | n.a. |
| 3.0% | ALL | 5 | 1 | 4 | +18.0% | 0.00 | 0.0030 |
| 3.0% | STRICT | 5 | 1 | 4 | +18.0% | 0.00 | 0.0030 |
| 3.0% | PROVISIONAL | 0 | 0 | 0 | n.a. | n.a. | n.a. |
| 5.0% | ALL | 5 | 1 | 4 | +18.0% | 0.00 | 0.0030 |
| 5.0% | STRICT | 4 | 1 | 3 | +18.0% | 0.00 | 0.0030 |
| 5.0% | PROVISIONAL | 1 | 0 | 1 | n.a. | n.a. | n.a. |

Calibration buckets, league/market/gameweek/policy breakdowns and all rejected candidates are in summary.json and candidate_decisions.csv. Older snapshots are not backfilled. Upload fresh outputs before kickoff; reporting runs in the existing forward-review workflow.
