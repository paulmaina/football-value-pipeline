# Conservative EV sensitivity experiment

One unit per simulated selection, net of frozen costs; simultaneous kickoff P&L grouped for drawdown. First eligible fixture snapshot freezes all policies and rejections. Different policies may select different markets/cohorts; results are not paired probability tests. Four weeks or 30 selections do not establish profitability. No automatic promotion; validate a chosen policy on later untouched data.

Frozen fixtures: 73; candidate decisions: 1410; rejected snapshots: 0.

| EV floor | Tier | Selected | Settled | Pending | Net ROI | Drawdown (units) | Brier |
|---|---|---:|---:|---:|---:|---:|---:|
| 1.5% | ALL | 9 | 6 | 3 | +10.2% | 1.00 | 0.1014 |
| 1.5% | STRICT | 7 | 5 | 2 | +7.0% | 1.00 | 0.1155 |
| 1.5% | PROVISIONAL | 2 | 1 | 1 | +26.0% | 0.00 | 0.0308 |
| 3.0% | ALL | 8 | 6 | 2 | +10.2% | 1.00 | 0.1014 |
| 3.0% | STRICT | 6 | 5 | 1 | +7.0% | 1.00 | 0.1155 |
| 3.0% | PROVISIONAL | 2 | 1 | 1 | +26.0% | 0.00 | 0.0308 |
| 5.0% | ALL | 7 | 5 | 2 | +7.0% | 1.00 | 0.1155 |
| 5.0% | STRICT | 5 | 5 | 0 | +7.0% | 1.00 | 0.1155 |
| 5.0% | PROVISIONAL | 2 | 0 | 2 | n.a. | n.a. | n.a. |

Calibration buckets, league/market/gameweek/policy breakdowns and all rejected candidates are in summary.json and candidate_decisions.csv. Older snapshots are not backfilled. Upload fresh outputs before kickoff; reporting runs in the existing forward-review workflow.
