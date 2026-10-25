# Production model v2 (`dc-blend70-hl480-pinnacle-ou25-anchor-v2`)

Every new forecast row and league diagnostic carries `model_version`. Rows without
the column were produced by the legacy profile `dc-blend50-tuned-half-life-v1`
(market weight 0.50, per-run tuned half-life). Both profiles stay defined in
`MODEL_PROFILES`; archived forecasts and selections are never rewritten. The
experimental shot profile `dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-v2` is used
only with `--experimental-shot-features`. Any other non-default configuration
(`--tune-half-life`, `--no-totals-anchor`, another weight or half-life) gets its own
identity: `dc-blend70-hl480-pinnacle-ou25-anchor-v2+custom-<settings hash>`.

## Changes

1. **Market weight 0.70.** The 1X2 blend target is `0.30 × model + 0.70 × fresh
   bookmaker reference`. Double Chance probabilities are derived from the same
   reweighted score matrix, so they move with it. No fresh reference still means no blend.
2. **Fixed 480-day half-life.** Production no longer tunes the half-life each run.
   `--tune-half-life` and `dc_decay_validation.py` remain for benchmarks and legacy
   replays. `--recency-experiment` still runs the tuning, for its own diagnostic sidecar
   only. `*_decay_tuning.json` records `applied_to_production: false`.
3. **Pinnacle O/U 2.5 totals anchor.** After the blend, both goal rates are scaled
   by one factor until Over 2.5 equals Pinnacle's margin-removed (power) probability.
   This uses `historical_benchmark.anchor_totals`, the same method as the
   `totals_opening_anchor` benchmark variant. Fitted rho and the production
   home/draw/away probabilities are kept exactly. The quote must be Pinnacle's,
   for the same event and within the live freshness window. No other bookmaker is
   ever substituted. When there is no such quote, totals are left alone and the row
   says why in `totals_anchor_status` (`NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE`,
   `..._STALE`, `..._EVENT_MISMATCH`, `..._INCOHERENT_...`, `..._SOLVER_FAILED`).
   Asian handicap, BTTS and every totals line come from the anchored matrix.
   `unanchored_p_over_2_5` keeps the pre-anchor value. Walk-forward validation
   backtests anchor to Pinnacle's nominal-opening CSV columns (`P>2.5`/`P<2.5`) only.
4. **Gated shot features: experimental, off by default** (`--experimental-shot-features`, `shot_features.py`). Lagged HST/AST shot-on-target
   strengths (optionally combined with HS/AS) from the Football-Data CSVs are
   opponent-adjusted and shrunk toward league average. They are converted to goal
   rates with league goals-per-shot-on-target and mixed into the Dixon–Coles rates.
   Only matches dated strictly before the origin are used, so same-day results are
   excluded. Every fit re-runs a chronological audit per league:
   - tune: the 182 days before the audit; it picks shrinkage, component and weight;
   - audit: the last 182 days.

   The audit uses the BBS statistics gates unchanged: minimum counts, Poisson-score
   gain ≥ 0.01, matchday block-bootstrap lower 95% > 0, no worse 1X2/O1.5/U3.5/BTTS
   Brier, and a rate-ratio cap of 1.25. If any gate fails, the league keeps pure
   Dixon–Coles. Diagnostics `shot_features_model` logs the status and `failed_gates`.
   UCL/UEL have no CSV shots and report `NO_SHOT_DATA`. BBS shots/xG can be added
   later through `shot_table(extra_shot_rows=...)` once `BBS_SHOT_SOURCE_ENABLED` is
   switched on, after `bbs_statistics_model` reports VALIDATED. BBS gates are not
   changed. Shots and BBS statistics never stack (`SHOTS_WITH_BBS_VALIDATED = False`).
   BBS, with its unchanged gate, applies first to pure Dixon–Coles rates. Shots apply
   only where BBS did not. Each forecast records `goal_rate_features_used` (`bbs_statistics`,
   `shot_features` or `none`).
5. **bet365 vs Pinnacle list** (`bet365_pinnacle.py`, raw `bet365_vs_pinnacle.csv`,
   readable `bet365_vs_pinnacle_report.md`). For each fixture and market quoted by
   both books in the same odds response, the list compares bet365's price with
   Pinnacle's margin-removed probability. An entry needs an EV of at least 2% and both
   quotes within the 24-hour freshness window. Each entry records both prices, the
   fair probability, EV, capture time and each quote's age. Double Chance fair
   probabilities are sums of Pinnacle's 1X2 fair probabilities; no Pinnacle DC price
   is invented. The list is never merged into any shortlist. Entries are archived at
   capture and become closing-collection targets, with `bet365` added to the
   collector's bookmaker list. The forward review writes
   `performance/closing_odds/bet365_vs_pinnacle_summary.json`, which holds bet365
   price CLV and EV against Pinnacle's closing fair probability.

   No extra API requests are made: the comparison reads the main `h2h,totals,spreads`
   response and the per-event additional-markets response that are already requested.
   Naming bet365 in the closing request costs nothing extra (≤10 bookmakers count as
   one region). **The Odds API currently has no bet365 football feed.** Its only bet365
   book is `bet365_au`, which is paid and AFL/NRL only. None of the cached responses
   contain bet365, so this list stays empty until a supported bet365 football source
   is integrated. Adding regions would raise costs without adding bet365.

## Legacy model alongside, and the forward comparison

Every live run also computes `dc-blend50-tuned-half-life-v1` for the same fixtures and
odds snapshot: market weight 0.50, the half-life tuned that run, no anchor, no shots.
The results are written as `legacy_*` columns in the forecast files
(`legacy_p_home/draw/away`, `legacy_p_over_1_5`, `legacy_p_under_3_5`,
`legacy_p_btts_yes`, `legacy_p_over_2_5`, `legacy_goal_margin_distribution`,
`legacy_status`). No selection or staking code reads them. `--no-legacy-comparison`
skips them.

The Forward performance review (`model_comparison.py`) grades both models on the same
settled matches. It writes `performance/model_comparison/report.md` and `summary.json`
with log loss, Brier, match counts and mean distance to the Pinnacle closing fair
probabilities, per league and market (1X2, Over 1.5, Under 3.5, BTTS, Over 2.5 and home
Asian handicap lines). Only the first eligible pre-kickoff forecast per fixture counts,
with no backfill. Fixtures whose first forecast lacks the legacy columns are excluded and
counted. The status stays `COLLECT_MORE_DATA` until there are 300 paired matches across
at least six ISO weeks. Production is never changed automatically.

## Validation caches and fingerprints

The goal-market validation cache key includes `model_version`, `totals_anchor` and
`shot_features`. The validation code fingerprint and `pipeline_health` model component
hashes cover `shot_features.py`, `historical_benchmark.py` and `bet365_pinnacle.py`.
Changing any of these settings or files forces revalidation.

## Forward experiments

These trials compare a candidate against a frozen production basis. They exclude
new-model forecasts explicitly rather than silently: each row records why, and every
summary/report lists `excluded_forecast_reasons` with counts.

- `market-weight-085-v1` (frozen basis: weight 0.50):
  `production_weight_outside_frozen_trial` and
  `production_model_dc-blend70-hl480-pinnacle-ou25-anchor-v2_outside_frozen_trial_basis`.
- `pinnacle-totals-anchor-v1`: `candidate_adopted_in_production`, plus the model reason.
- Reliability trial: candidates are fitted with production's feature settings and receive
  production's blend and, when production anchored a fixture, the same Pinnacle totals
  target. Only the declared factor differs. Non-comparable forecasts are excluded with
  `feature_application_differs`, `candidate_anchor_solver_failed` or
  `production_anchor_target_missing`. `fixed_half_life` reports
  `candidate_equals_production_half_life`, because production now uses 480 days.
  `stronger_l2` continues.
