# Conservative filter sensitivity experiment

Every normal current-fixture pipeline run now writes `raw/filter_sensitivity_experiment.json` automatically. No additional flag, fitting, or odds API request is required. Backtests do not generate forward experiment evidence.

Three fixed policies compare reliability-adjusted **net EV floors of 1.5%, 3%, and 5%** across all six conservative markets. The 1.5% control copies the actual production decisions. Higher floors rerun the same conservative evaluator at the same generation time, with the same forecasts, historical reliability report, account allowlist, frozen costs, probability floors, quote/identity checks, ranking, provisional rules, one market per fixture and maximum ten selections per run. A stricter EV policy can select an alternative market for a fixture; it is not merely a subset of the live shortlist. Under 3.5 remains excluded.

All candidate decisions, including rejections and unpriced candidates, are included in the sidecar. Rejected candidates are graded for probability diagnostics where available; they are never treated as placed bets. Missing prices never produce simulated profit.

The existing forward-review workflow freezes the sidecar in the immutable forecast snapshot with its SHA-256 manifest. Generation timestamps and forecast hashes must agree. Both generation and capture must be at least 20 minutes before kickoff. Only fixtures within the conservative 72-hour generation horizon enter the forward comparison; earlier outside-horizon rejections remain archived but do not lock out later eligible forecasts. First eligible experiment snapshot per fixture freezes all market/policy decisions, including rejection, so later runs cannot replace an unfavorable forecast. Old snapshots are not backfilled. Hash or schema failures exclude the experiment while preserving baseline evidence.

Daily review uses the same verified regulation results and pending-score safeguards as production reporting. Outputs are in `performance/filter_sensitivity_experiment/`:

- `report.md`: selection counts, settled/pending counts, net flat-stake ROI, drawdown and Brier for all three floors, with strict and provisional cohorts shown separately.
- `summary.json`: calibration buckets and league, market, gameweek and production-policy breakdowns; rejected snapshot commits.
- `selections.csv`: frozen simulated selections, outcomes, prices, costs, profit and provenance.
- `candidate_decisions.csv`: every frozen candidate, rejection reasons, historical penalties and result diagnostics.

Profit assumes one unit per selected single bet at the recorded price, deducting the frozen per-stake cost on either outcome. Account policy remains 1xBet with zero additional costs. Actual stake acceptance or price availability when placing a bet cannot be verified by this experiment. Drawdown is calculated on the simulated chronological P&L with simultaneous kickoff fixtures grouped; it is not a bankroll or accumulator return.

Reports are automatically reconciled against frozen sidecars and the official result cache before publication. No experiment automatically changes production. Four weeks is an initial review point, not a sufficient-sample guarantee; stricter policies may yield few or no selections. Policy cohorts overlap and can differ, so do not interpret ROI differences as paired model accuracy tests. Select any promising policy for a later untouched validation period before considering adoption.

Use the existing command after `git pull`:

```powershell
py football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life --goal-blend-experiment --additional-odds-coverage all --market-led-experiment --recency-experiment
py format_football_output.py
```

Commit and push generated `football_output_v2` files before kickoff. The pipeline runs on your computer; the repository workflow captures and reviews the uploaded outputs automatically.
