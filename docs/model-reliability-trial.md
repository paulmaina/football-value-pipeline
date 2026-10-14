# Stronger regularisation and fixed-half-life forward trials

Add `--reliability-experiment` to the normal forecasting command:

```powershell
py football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life --goal-blend-experiment --additional-odds-coverage all --market-led-experiment --reliability-experiment
```

Keep `--recency-experiment` too if already using it. This flag needs no additional API key or odds request. It adds two model fits per league, so forecasting takes longer. It is disabled by default and cannot run with `--backtest`.

The historical development-only ALL 1X2 comparison in `docs/benchmarks/2026-10-14/report.md` nominated L2=3 and a 480-day half-life. Those periods have already been inspected; they are retrospective diagnostics, not untouched confirmation. The stronger-L2 audit was worse on 1X2 even though goal markets improved, so no production promotion is justified by that result.

Each candidate changes just one setting against the actual production run:

| Candidate | Changed | Retained |
|---|---|---|
| stronger_l2 | L2=3 | Production half-life and score-matrix limit |
| fixed_half_life | Half-life=480 days | Production L2 and score-matrix limit |

Both use private copies of the same training history and production's existing 1X2 market blend/reference. They do not combine the two changes. Training hashes, settings, raw candidate score matrices and explicit failures are stored in `raw/model_reliability_experiment.json`. Unreliable team mappings and unsupported leagues are unavailable; UCL is excluded from this trial because the historical nomination covered domestic leagues only. Production still forecasts UCL normally.

Push the new sidecar with the forecasts at least 20 minutes before kickoff. Existing forward-review automation captures and hashes it alongside the exact production CSV. The first eligible snapshot freezes each fixture, including failed/unavailable candidates: reruns do not fill missing candidates after the fact. There is no backfill of already played fixtures. Subsequent reviews grade only verified finished regulation-time results.

Results appear in `football_output_v2/performance/model_reliability_experiment/report.md`, `summary.json` and `graded.json`. The existing review queue, health capture history and Excel Experiments sheet show the two candidates separately. Forecasting flags do not need to change for report regeneration.

Primary metric: paired 1X2 log loss. Reports also show Brier/RPS, top-label calibration, goal-market probability bands and league breakdowns for Over 1.5, Under 3.5, BTTS Yes and Over 2.5. These descriptive breakdowns must not be mined to redefine the primary trial. Each candidate needs 300 paired settled fixtures across six ISO weeks and at least 80% coverage of verified in-scope first observations. Missing candidates remain in the coverage denominator.

Readiness permits review, including negative findings. Supportive forecasting evidence additionally requires a positive primary week-block bootstrap gain interval, no aggregate log-loss/Brier deterioration in the registered markets and no top-label calibration deterioration. Two primary trials use 97.5% intervals each (Bonferroni familywise 95%). Any rejected snapshot blocks supportive evidence. Neither readiness nor positive evidence changes production settings or establishes betting profitability. Production adoption requires a separate decision after review.
