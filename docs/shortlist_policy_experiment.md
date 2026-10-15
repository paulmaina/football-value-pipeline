# Final shortlist policy comparison

This passive sidecar runs automatically with full current-fixture pipeline
runs. Keep your existing command and experiment flags. No extra odds requests
or model fits are made. Production forecasts, shortlist thresholds, ranking
and CSV schemas are unchanged.

The fixed grid has nine policies: production control; blended entry cutoffs
minus/plus 3 percentage points; raw-model entry cutoffs minus/plus 3 points;
adjusted-probability cutoffs minus/plus 3 points; development-only calibration
penalties multiplied by 0.5 or 1.5. Each candidate changes exactly one setting.
Adjusted double-chance cutoffs start at 75%; their blended entry cutoffs start
at 80%. All three double chances, including 12, are included. From shortlist
policy v10, BTTS Yes is included with the existing 70% model/adjusted and 63%
raw probability thresholds; v9 captures retain their original six-market replay.
See [BTTS shortlist rules](conservative-shortlist-btts.md).
The applied penalty remains the maximum of the overall and matching confidence
group's development-only penalties, scaled once and capped at 1. Audit results
never fit the penalty. Missing calibration evidence remains a rejection.

The minimum 1.5% estimated value, genuine quotes, bookmaker allowlist, costs,
quote age, matching, independent raw-model EV, historical audit gates,
one-market-per-fixture rule and ten-fixture cap remain fixed. This is separate
from the existing EV-floor sensitivity experiment; no factorial search or
automatic tuning is introduced. Provisional watchlist rules remain in force
and are reported separately; STRICT results are the primary selection view.

`raw/shortlist_policy_experiment.json` freezes every candidate decision,
including rejections, the full validation evidence and execution policy.
Capture deterministically replays it against the actual prediction CSV,
checks the production control and current validation reports, and hashes the
sidecar into the immutable archive. Broken optional evidence cannot block
production capture. Older snapshots have no data for this experiment and are
not backfilled. The first valid capture at least 20 minutes before kickoff,
inside the 72-hour horizon, freezes every variant for each fixture.

The normal forward review writes `performance/shortlist_policy_experiment/`
with `summary.json`, `report.md`, `selections.csv` and `candidate_decisions.csv`.
Excel's Experiments sheet and health/review-queue reports show its progress.
It reports counts, probability Brier/log loss, calibration buckets, simulated
ROI after configured costs, drawdown and league/market/week breakdowns.
Selected cohorts differ, so their Brier scores are not paired model tests.
Common-cohort probability scores and paired Brier/log-loss differences with
weekly bootstrap intervals isolate the effect of penalty strength;
threshold changes do not themselves change probabilities. STRICT return
deltas compare every verified fixture, assigning zero to no selection.
Exploratory 95% intervals resample ISO-week blocks; they remain unavailable
before six weeks and 100 verified fixtures. Eight comparisons introduce
multiple-testing risk; these intervals are not promotion tests.

Readiness requires at least 300 distinct verified fixtures, six ISO weeks,
80% verified coverage and no rejected archived captures. These are review
gates, not proof of profitability or adequate statistical power. After review,
freeze one proposed policy and evaluate it on later untouched fixtures before
considering a production change. There is no automatic promotion. Keep this
grid fixed and collect evidence rather than adding more experiments.

Policy v11 also checks fresh exact-market and underlying 1X2 reference
timestamps. Existing v9/v10 captures retain deterministic replay of their
original reference rules. See [live quote freshness](live-quote-freshness.md).

The version binds the grid and baseline policy. Future shortlist-engine
changes must retain historical replay compatibility or use a separately
versioned implementation; do not reinterpret existing captures.
