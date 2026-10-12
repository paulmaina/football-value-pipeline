# Optional goal-market shadow experiment

This experiment is disabled by default. It never modifies model fitting, baseline probabilities, qualification rules, shortlist selection, or the Excel workbook. It makes no additional API requests. There is no automatic promotion, experimental betting policy, or claim of improved profitability.

Enable it on a normal forecast run:

```powershell
py football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life --goal-blend-experiment
py format_football_output.py
```

Commit and push the raw outputs as usual, including `football_output_v2/raw/goal_blend_experiment.json`. The existing forecast capture workflow includes the experiment only when its generation timestamp and SHA-256 of the combined baseline CSV match the current run. Old sidecars from an earlier enabled run are ignored. Historical snapshots are not backfilled.

For each fixture and exact goal market (Over 1.5, Under 3.5, BTTS Yes), the experiment stores raw model, 25% bookmaker, 50% bookmaker, bookmaker-only and current baseline probabilities. The current baseline means the probability after 1X2 score-matrix reweighting, before shortlist-specific calibration deductions. Variants are uncalibrated. They use the existing de-vigged exact-market reference; the blend starts from raw DC, avoiding a second application of the 1X2 blend.

Opposing probabilities are stored as complements. Inconsistent goal-total lines are excluded rather than silently repaired. Missing model estimates, invalid exact-market references, missing quotes, insufficient lead time and quotes older than 24 hours are unavailable. The 24-hour quote ceiling mirrors the current policy; prices are not guaranteed executable. The quote timestamp stored is that of the selected offered price, not a separately verified timestamp for every reference bookmaker.

Daily performance review uses the same verified regulation-time results and makes no extra result requests. It retains the first eligible archived fixture-market observation, including unavailable observations, and compares every variant on identical available fixtures. Both capture and generation must be at least 20 minutes before kickoff. No variants are selected retrospectively. A corrupt experiment cannot invalidate baseline snapshot grading.

Separate reports are published automatically under:

- `football_output_v2/performance/goal_blend_experiment/report.md`
- `football_output_v2/performance/goal_blend_experiment/summary.json`
- `football_output_v2/performance/goal_blend_experiment/graded.csv`

These show coverage, sample count, Brier score, mean probability and observed event rate by market and variant. They are created after the first eligible experimental archive. Reports do not compare betting ROI because v1 defines no experimental betting policy. No report is added to Excel. For disablement, omit the flag; accumulated valid experimental archives continue to be evaluated.

## Interpretation and future work

This is prospective data collection, not historical weight optimization. Archived pre-existing matches used in software replay are not counted as forward experimental evidence. Historical odds coverage for these exact markets remains to be assessed before historical evaluation. Any later calibration or weight selection requires chronological development/calibration/test separation with nested decay tuning. Do not choose a weight based on the October 11 results. Improvements must be assessed on future paired observations; Brier alone does not establish profitability.

## Verification

Regression tests exercise baseline CLI output byte equality with the flag off/on, blend arithmetic, complements, missing/stale/future odds, lead time, line consistency, CSV hash and timestamp binding, immutable capture, paired grading and experiment-tamper isolation. No new dependency is required.
