# Optional goal-market recency experiment

Add `--recency-experiment` to the normal full-league command. It requires
`--tune-half-life` and automatically writes the existing goal-blend sidecar,
even when `--goal-blend-experiment` is omitted. It does not create an additional
snapshot file or change production probabilities, calibration, shortlist rules,
1xBet eligibility, odds requests or stakes. It is incompatible with backtesting
through the existing tuning/backtest guard.

```powershell
git pull
py football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life --goal-blend-experiment --additional-odds-coverage all --market-led-experiment --recency-experiment
py format_football_output.py
```

Commit and push `football_output_v2` before kickoff. The forward review workflow
captures the exact goal JSON and its nested `recency_experiment` section using
the existing SHA-256 manifest. Both generation and real capture must precede
kickoff by more than 20 minutes. Existing Windows/LF newline compatibility
checks still apply. Old snapshots are preserved and not backfilled.

## Comparisons

The experiment focuses on **Over 1.5** and **BTTS Yes**. It compares:

- `production_raw`: the original unblended Dixon-Coles probability from this
  same frozen forecast, using the production-selected half-life.
- Fixed half-lives from `--half-life-candidates` (default 120, 240, 365, 730 and
  1e9 days). The production candidate reuses its existing raw probabilities.
- `goal_selected`: a per-market half-life selected using early historical
  goal-market binary log loss, with Brier and half-life as tie-breakers.
- `development_1x2`: a match-result selector using the same early historical
  folds, for an honest later historical comparison.

Every alternate current model uses an independent copy of the exact history
used for the production model, identical L2 regularization/max-goals settings,
and the same latest-training-match recency anchor. No bookmaker blending,
calibration or additional live data is applied to these raw comparisons. They
isolate recency weighting; comparison with the final production probability
would mix recency, blending and calibration effects.

Historical goal diagnostics reuse the scoreline matrices and model fits already
made by production decay tuning. Production 1X2 selection is unchanged. The
extra runtime is principally up to four alternate current-model fits per league
with the default grid. There are no additional odds API requests.

## Historical selection, stability and holdout

The first approximately two-thirds of eligible chronological folds select goal
and comparison 1X2 half-lives. The remaining folds are an audit and cannot alter
those choices. At least three common folds and the configured
`--tune-min-validation-matches` (default 25) in each phase are required to label
goal selection supported. If history is insufficient, fixed candidates still
collect forward evidence; a goal-selected variant is omitted.

The production selector continues to use its entire tuning period. Therefore
the later historical audit compares goal selection against the **development
1X2 selector**, not against a production selector that already saw the audit.
Actual forward comparisons use the original production raw forecast frozen in
the same new snapshot. Historical reports record phase sample sizes, candidate
scores, chosen half-lives, development fold winners and the margin over the
second candidate. Audits from repeated runs overlap and must not be summed as
new independent evidence.

## Automatic reports

Verified regulation-time results produce:

- `performance/recency_experiment/report.md`: paired score comparisons and
  latest historical selection/audit diagnostics.
- `summary.json`: league/market/variant comparisons, calibration buckets with
  observed-rate intervals, weekly comparisons, approximate paired-score-gain
  intervals, historical audit provenance and rejected snapshots.
- `graded.csv`: each recorded variant, its actual half-life, probability,
  outcome, Brier/log loss, same-snapshot baseline scores and verified match ID.
- `coverage.csv`: pending/unverified/unavailable markets and candidate errors.

The main performance dashboard and native Excel **Pipeline Health** sheet show
recency capture status; the dashboard links to the detailed report. Daily
health observations retain its current summary. One first eligible recency
observation is frozen per fixture/market; missing candidates cannot be replaced
later to improve apparent coverage. Comparisons are paired to the baseline on
each variant's available matches, but different variants can have different
sample counts. Unknown teams, failed fits and missing raw values are recorded,
not invented. Pending/unverified fixtures are never counted as wins or graded
errors. A recency failure preserves the existing goal-blend experiment and
baseline capture/reporting.

Positive paired gain means lower prediction error than the raw control on
those same matches. Approximate intervals assume independent fixtures and are
not adjusted for multiple comparisons. Thirty samples is only a review prompt,
not proof. The experiment defines no betting policy, simulated ROI, automatic
promotion or guaranteed four-week improvement. Promising changes require a
later untouched validation period and separate production-market assessment.
