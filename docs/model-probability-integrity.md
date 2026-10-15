# Model probability and validation-cache integrity

The `dc-positive-tail-bounded-v1` score engine fixes three correctness gaps.
It introduces no experiment, threshold, staking, calibration or training-decay
change. Existing commands still work.

## Training corrections invalidate validation

Cached goal-market validation now requires the full canonical training-frame
SHA-256, including historical price columns, and a fingerprint of the relevant
model/validation code. Correcting a score, team identity or opening price
invalidates the cache even if the match count and latest date stay unchanged.
Missing legacy fingerprints fail closed and trigger a rebuild. Validator
version 6 separates these reports from earlier caches.

Production retains a private copy of its training frame. Validation uses that
copy, so an intervening provider refresh cannot bind a report to a different
dataset. Canonical hashing does not modify the frame and ignores row/column
ordering. An unchanged dataset and implementation can reuse the rebuilt cache.

## Invalid probability matrices are rejected

All four low-score Dixon-Coles correction factors must be positive for the
forecast fixture, including scorelines not observed in training. The matrix
must have finite, nonnegative entries and positive total mass. Invalid
parameters fail explicitly rather than being clipped or normalized into a
published forecast. Reweighting also rejects malformed matrices and targets.

## Probability mass is retained

`--max-goals` remains available with default 10, now specifying the minimum
grid. The engine expands the square grid when needed so omitted probability
mass is at most `1e-10`. A 100-goal numerical safety ceiling rejects parameter
sets that cannot meet that tolerance. No adjustment is made to the fitted
intensities, rho or regularization. Forecast probabilities can change where
the old truncated grid discarded material mass; this is the intended fix.

Predictions record `score_engine_version`, `score_grid_max_goals` and
`score_grid_omitted_mass`. Diagnostics retain the configured minimum grid.
New totals-experiment inputs carry the actual matrix size and engine version;
their reconstruction and solver use the same bounded-tail method. Archived
inputs without that version retain the original fixed-grid solver and bounds.
The historical benchmark records the new helper's code hash on future runs.

Existing archived forecasts, selections, registries, reports and captured
matrices are not rewritten. New reliability/benchmark comparisons use their
existing grids of candidate settings and the corrected model engine. No claim
of increased predictive accuracy or returns is inferred from numerical fixes.

Recency anchoring is deliberately unchanged: production/backtesting retain
their existing anchor and tuning retains its explicit forecast-date anchor.
Changing that convention would change fitted models and needs a separate
compatibility decision, beyond these three correctness repairs.

After merging, pull and use the usual full pipeline command. The first run
rebuilds old validation caches and can take longer; subsequent unchanged runs
can reuse them. Existing stored forecasts require regeneration to receive the
new engine's probabilities and metadata.
