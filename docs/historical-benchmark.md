# Reproducible historical model benchmark

This offline benchmark tests the proposals in Claude's review without changing production predictions, calibration, shortlist filters or the four existing sidecars. It makes no API requests and does not calculate historical betting profit or claim closing-line value.

## Fixed data and temporal evaluation

The input manifest pins 20 domestic league CSVs from repository commit `1caa1ee2ad9ac255f2952727df8e91ba4081d389` by exact SHA-256. Four seasons provide training history for EPL, La Liga, Bundesliga, Serie A and Ligue 1. UCL is deliberately excluded because it does not have the same Pinnacle CSV schema.

The fixed evaluation starts 1 August 2025 and ends before 14 October 2026. Models refit every 14 days, using only completed matches dated strictly before the fold origin. The audit boundary on 1 November 2025 is also a refit boundary, so a fold never straddles development and audit. This boundary was selected from odds coverage, before inspecting scores: the pinned Pinnacle columns stop in January 2026, making a February boundary unsuitable for market-informed audit comparisons.

Both periods were already exposed to Claude's analysis. They are retrospective development and audit diagnostics, **not genuinely untouched validation**. The prospective validation start is 14 October 2026, and no results from that period enter this benchmark. Updating the frozen window or input manifest is a versioned methodological change, not extra independent evidence.

Dates, completed scores, team identities, duplicates and input hashes are validated. Unknown teams are explicitly excluded rather than receiving league-average predictions. Fit and solver failures are counted. Each fold retains its training count, end date and training-row hash.

## Independent comparisons

The reference uses a fixed 240-day half-life, L2 0.08 and fitted Dixon–Coles correlation. It is a named, uncalibrated configuration reference, not a replay of production's league-specific half-life tuning or reliability-adjusted shortlist probabilities.

- Raw Dixon–Coles and a 50/50 blend with nominal-opening Pinnacle 1X2 probabilities.
- L2 0.8 and 3.0 with the same 240-day half-life, reported raw and with the same 50/50 blend.
- Half-life 365 and 480 days with the same L2 0.08, reported raw and blended.
- Market weights 0.75 and 0.85 using the reference fit.
- Totals anchoring using nominal-opening Pinnacle O/U 2.5, retaining fitted correlation and the reference 1X2 blend target.
- A separately labelled closing-totals oracle diagnostic, plus closing Pinnacle 1X2 evaluation reference.

Totals anchoring rescales both fitted goal intensities by one proportional factor. A bounded numerical solver matches the O/U 2.5 probability **after** the matrix is reweighted to its 1X2 target. It keeps that target exactly, preserves fitted correlation, and reports invalid/unreachable cases. This is not a joint estimation of two independent intensities, and it does not use Claude's fixed correlation of -0.06.

There is no bookmaker fallback. Missing Pinnacle odds are recorded as missing. Historical nominal-opening CSV odds have no precise availability timestamps; they cannot establish that a quote existed at a particular earlier forecast time. Closing inputs remain explicitly evaluation/oracle-only and cannot qualify for promotion.

## Metrics and candidate selection

The report includes 1X2 log loss, multiclass Brier and normalized RPS using the declared Home–Draw–Away order. Goal markets include Over 1.5, Under 3.5, BTTS Yes and Over 2.5, with binary log loss/Brier, calibration buckets and high-confidence diagnostics. Under 3.5 remains excluded from production selections.

Every paired comparison uses intersecting fixture identities, with equal baseline/candidate counts. The JSON also compares variants with the raw model and, for 1X2, Pinnacle closing probabilities. Do not compare unpaired overall scores as if their cohorts were identical. Candidate selection within each factor family uses a common development cohort, with log loss first, Brier second and baseline-first deterministic ties. Audit results cannot select the candidate. Family-level coverage thresholds are enforced separately.

Approximate paired-gain intervals assume independent fixtures and do not adjust for multiple comparisons. They are diagnostic, not a sufficient promotion test. Closing comparison coverage below 1,000 matches is clearly reported and does not fail CI or silently substitute another bookmaker.

## Running and automation

The existing prediction command is unchanged. This is a separate command:

```powershell
git pull
py historical_benchmark.py --materialize-pinned-data
```

It reads the pinned CSVs from local Git objects into `workflow_artifacts/historical_benchmark/pinned_inputs`, leaving the production cache unchanged. The pinned commit must be present locally; a complete Git checkout normally has it. Alternatively, use `--cache-dir` with exact manifest-matching files. Changed cache bytes fail closed with an instruction to materialize the pinned data.

To reconcile an existing run:

```powershell
py historical_benchmark.py --validate-only
```

The Historical model benchmark workflow runs on benchmark-code/config pushes to main, weekly on Monday at 11:15 EAT, and on manual dispatch. It has read-only repository permissions, uses no API secrets and uploads a 90-day artifact containing the full prediction ledger, folds, report, summary, integrity manifest and pinned inputs. It does not publish forecasts, modify production settings or repeatedly download live data. The weekly rerun checks reproducibility and software changes against a fixed dataset; it does not accumulate fresh prospective evidence.

The normal self-test workflow covers temporal separation, opening/closing independence, unknown-team exclusion, malformed inputs, pinned bytes, fitted-correlation totals matching, paired cohorts, development-only selection and report tampering. Coverage floors and CLI smoke checks include the new module.

## Interpreting the result

Stronger regularisation, higher market weighting or totals anchoring can improve probability diagnostics without establishing a betting edge. Actual bet-time prices, accepted stakes, accurate timestamps and prospective outcomes are required for betting claims.

`benchmark_promotion_rules.json` records the future trial requirements before any new candidate is generated forward. A prospective review needs at least 300 distinct paired fixtures across six gameweeks, a predeclared uncertainty analysis, calibration checks and human approval. These are review gates, not guarantees. The existing four-week review remains an initial collection check.

The new candidate settings currently exist only in offline comparisons. Dedicated closing collection and execution recording remain future work. No candidate is automatically promoted.

## v2: production model upgrade comparison

Benchmark v2 (`historical-dc-benchmark-v2`) keeps every v1 variant unchanged and adds
`model_upgrade_comparison`, scored on one common cohort per league, phase and market:

- `production_v1`: replays the per-run half-life tuning at each fold origin on that
  fold's training rows (production tuning defaults), with market weight 0.50;
- `upgrade_market_weight_70`, `upgrade_half_life_480`, `upgrade_pinnacle_ou25_anchor`,
  `upgrade_gated_shot_features`: each change on its own;
- `production_v2`: all four together.

Markets are 1X2, Over 1.5, Under 3.5, BTTS Yes, Over 2.5, and the home Asian handicap
at −2.5, −1.5, −1, 0, +1, +1.5 and +2.5. The away side is the complement. Integer lines
drop refunded outcomes from scoring. The summary also reports anchor coverage,
per-line probability shifts against `production_v1` on anchored fixtures, per-fold
tuned half-lives and the shot-feature gate outcome for every league and fold.
Historical totals anchoring uses Pinnacle's nominal-opening O/U 2.5. Fixtures without
it stay unanchored. The pinned inputs hold four seasons, while production trains on six.
v1 artifacts still pass `--validate-only`.
