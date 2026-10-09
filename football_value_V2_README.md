# Football Value Pipeline V2

V2 is a multi-league football probability and value pipeline built around a recency-weighted Dixon-Coles score model.

## Recommended daily-use model (single configuration)

**Use this command for the next several weeks.** It runs one consistent
Dixon-Coles model, with a **fixed 50% Dixon-Coles / 50% de-vigged
bookmaker 1X2 blend**, and tunes each competition's historical recency
half-life. You choose only the competitions and whether to tune decay:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life
```

- The market blend is **0.50 by default**; do not pass `--market-weight`
  or `--auto-market-weight` in normal use. Keeping a single fixed rule
  avoids changing the model definition between prediction runs.
- Dixon-Coles uses historical match results; the market contribution uses
  a coherent de-vigged live 1X2 bookmaker snapshot. Without complete
  bookmaker 1X2 odds, that fixture remains a pure Dixon-Coles prediction.
- Historical audit results indicated that a fixed 0.50 blend improved 1X2
  log loss over pure Dixon-Coles in all five **domestic** league audit
  samples. This was a retrospective comparison, not an untouched final
  test; it does **not** prove better exact-score or betting performance.
  **UCL has no usable historical opening-odds audit yet**, so its 50%
  blend is an unvalidated extrapolation.
- The CSV includes final `p_home/p_draw/p_away` and retained raw
  `raw_p_home/raw_p_draw/raw_p_away`, plus `raw_ev_*`
  and `raw_edge_prob_*` for independent model-signal auditing.
- Send back actual match results alongside saved forecast CSVs after a few
  matchweeks to measure accuracy, calibration, and whether betting edges
  are meaningful. Do not use ROI from only a handful of bets as evidence
  of predictive improvement.

The automatic weight tuner remains in the codebase for future research,
but is **not part of the recommended daily-use model**.

## Eight-match, five-market shortlist (experimental)

Running the existing command (no extra flags) now also produces a
**target of eight distinct match candidates per run**, with at most one
market selected from each football match:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life
```

Markets evaluated: **Home win, Away win, Over 1.5, Under 3.5,
Both Teams to Score — Yes**. UCL is still forecast, but excluded
from this shortlist due to missing historical opening-price validation.

Outputs remain in `football_output_v2/raw/`:

- `conservative_bet_shortlist.csv`: up to eight distinct fixtures,
  one market each, sorted by forecast win probability, then EV.
- `conservative_bet_rejections.csv`: five decisions per fixture,
  including rejected/alternate markets and the reasons.
- `conservative_bet_summary.json`: `TARGET_MET`, `BELOW_TARGET`
  or `NO BET`, with the shortfall to eight.
- `shortlist_history/conservative_decisions_<timestamp>.csv`:
  immutable dated audit snapshots for later feedback.

**Eight is a target, never a minimum guaranteed by relaxation.** No
market gets picked without a verified bookmaker price. If fewer than
eight qualifying matches are available, the result is short with
`BELOW_TARGET` or `NO BET`. Multiple markets on the same football
fixture are not counted as different picks. A selection report is not
an automatically placed multi-leg betslip.

The default model remains fixed 50/50 Dixon-Coles / de-vigged
bookmaker 1X2. Specific threshold gates:

| Market | Blended probability at least | Raw DC probability at least |
| --- | ---: | ---: |
| Home win | 65% | 50%, with DC also favoring home over draw and away |
| Away win | 65% | 50%, with DC also favoring away over draw and home |
| Over 1.5 | 78% | 72% |
| Under 3.5 | 76% | 70% |
| BTTS Yes | 70% | 63% |

All candidates must have estimated positive EV **at least +3%**
at an actual bookmaker quote and **non-negative unblended DC EV**,
team-name matching confidence **at least 90** for both teams,
a valid 50/50 blended market and current future UTC kickoff at least
20 minutes away. Quote timestamp must be no more than 24 hours old.

For 1X2, at least two complete reference bookmakers are required.
For alternate totals and BTTS Yes, one verified bookmaker with both
complementary outcomes is sufficient. The market's own coherent
quote pair (not unrelated line or h2h quotes) must be available.

**Additional The Odds API quota cost:** The standard sports odds
endpoint retrieves h2h and featured totals, usually 2.5. The
additional `alternate_totals,btts` markets require a separate
`/events/{eventId}/odds` request. The pipeline makes no more than
**24** of these requests per run across domestic leagues, and only
for fixtures where the model and team-matching confidence suggest
plausible additional-market candidates. The endpoint may not offer
these markets in every competition, region or bookmaker; absent
prices are rejected rather than invented. A bounded request budget
can also reduce the number of potential shortlist candidates.

**Risk and interpretation:** These thresholds are provisional
heuristics, not backtested thresholds with proven bookmaker edge.
A claimed +3% estimated EV can disappear with probability error,
odds movement or bookmaker limits. An eight-leg accumulator is
particularly fragile: all eight selections must win to pay out.
Track real-world outcomes for several weeks before considering
stakes or a higher selection target. No guaranteed or perfect
betslip exists.

## Current data architecture

The pipeline separates historical modelling data, current fixtures, and live market odds.

- **Historical results and historical bookmaker columns:** Football-Data.co.uk season CSVs.
- **Preferred current fixtures:** The Odds API v4 `/events` endpoint when `THE_ODDS_API_KEY` is configured.
- **Preferred current odds:** The Odds API v4 `/odds` endpoint using `h2h` (1X2) and `totals` (O/U).
- **Optional fixture fallback:** football-data.org v4 when `FOOTBALL_DATA_API_KEY` is configured.
- **Last-resort fixture snapshot:** Football-Data.co.uk `fixtures.csv`.

The old FixtureDownload fallback was removed. If a trustworthy current endpoint cannot provide fixtures, the pipeline fails explicitly rather than silently producing predictions for a questionable schedule.

## Supported competitions

- EPL
- La Liga
- Bundesliga
- Serie A
- Ligue 1
- UEFA Champions League (UCL)

### Champions League modelling

UCL is intentionally handled differently from a domestic league.

Current UCL fixtures and odds use The Odds API sport key
`soccer_uefa_champs_league`. Model training uses completed UEFA Champions
League matches from football-data.org competition code `CL`.

This avoids fitting a Champions League prediction from unrelated domestic-league
ratings. A `FOOTBALL_DATA_API_KEY` is therefore required when `UCL` is
included. The free football-data.org tier includes Champions League fixtures and
results; access to older seasons can depend on the account/plan. The pipeline
uses all accessible requested seasons and requires at least 30 completed UCL
matches before fitting the Dixon-Coles model.

## Install

```bash
pip install -r football_value_requirements.txt
```

Optional reliability plots require matplotlib.

## Configure current fixtures and live odds

Do **not** commit API keys to GitHub. The pipeline reads them from environment variables.

PowerShell:

```powershell
$env:THE_ODDS_API_KEY="your-key-here"
```

Optional football-data.org fixture fallback:

```powershell
$env:FOOTBALL_DATA_API_KEY="your-key-here"
```

These variables apply to the current PowerShell session. Keep secrets in your local environment or a secret manager rather than in source files.

## Run the five domestic leagues

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1
```

Include Champions League:

```powershell
$env:THE_ODDS_API_KEY="your-odds-api-key"
$env:FOOTBALL_DATA_API_KEY="your-football-data-org-key"

python football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL
```

UCL only:

```powershell
python football_value_pipeline_v2_standalone.py --leagues UCL
```

Raw model outputs are written by default to:

```text
football_output_v2/raw/
```

The run logs which fixture provider was used and how many fixtures received live odds.

## Odds behavior

For 1X2 and O/U 2.5 the pipeline keeps two concepts separate:

1. **Reference market** — one complete bookmaker market is used for de-vigging, so Home/Draw/Away probabilities are never constructed by mixing bookmakers.
2. **Best available price** — the highest returned price for each individual selection is used for EV.

Outputs include audit fields such as fixture source, fixture ID, odds source, odds-match method, latest odds timestamp, bookmaker counts, and the bookmaker offering each selected best price.

If a current fixture is available but no qualifying bookmaker market is returned, model probabilities remain available and the market/EV fields remain blank.

## API-credit usage

The Odds API charges current odds requests according to requested markets and regions. V2 requests two featured markets (`h2h,totals`). The local five-minute odds cache avoids spending more credits on immediate repeat runs.

Default region:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --odds-regions eu
```

Multiple regions can be comma-separated, but they increase API usage:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --odds-regions uk,eu
```

## Fixture-provider controls

Default:

```text
--fixture-provider auto
```

`auto` tries, in order:

1. The Odds API events endpoint (if `THE_ODDS_API_KEY` exists)
2. football-data.org (if `FOOTBALL_DATA_API_KEY` exists)
3. Football-Data.co.uk current fixture CSV for domestic leagues

For UCL, the third option is not used because Football-Data.co.uk does not provide
a UCL division CSV compatible with the domestic fixture loader.

You can force a provider for debugging:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --fixture-provider the-odds-api
```

To fetch fixtures without requesting live odds markets:

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --no-live-odds
```

## Model

The score matrix remains the single probability engine:

- recency-weighted Dixon-Coles Poisson
- L2 regularisation
- expected home/away goals
- 1X2 probabilities and fair odds
- top 20 exact-score probabilities per fixture (the full score matrix is used internally, but only the 20 highest-probability scores are serialized)
- O/U 0.5, 1.5, 2.5, 3.5 and 4.5 probabilities

If `--market-weight > 0`, the Home/Draw/Away regions of the score matrix are reweighted toward a de-vigged market target. All downstream markets are then recalculated from the same matrix.

The **recommended default is `0.50`**, a single fixed blend chosen for an extended feedback period. Do not tune market weight on the same test set used for final evaluation.

## Dixon-Coles exponential time-decay tuning

The Dixon-Coles model already uses a low-score correction (rho) and a
recency-weighted likelihood. The default remains a **240-day half-life**.
Do **not** assume 240 days is universally optimal.

The blog's exponential decay coefficient (xi, in reciprocal days) is equivalent
to the pipeline's half-life parameter through:

```text
xi = ln(2) / half_life_days
weight(age_days) = exp(-xi * age_days)
```

You can now compare candidate half-lives using past-only, walk-forward match
result predictions (mean 1X2 log loss; lower is better):

```powershell
python football_value_pipeline_v2_standalone.py --leagues EPL --tune-half-life
```

Customize the candidate half-lives and evaluation window:

```powershell
python football_value_pipeline_v2_standalone.py `
  --leagues EPL LaLiga Bundesliga SerieA Ligue1 `
  --tune-half-life `
  --half-life-candidates 120 240 365 730 1000000000 `
  --tune-validation-days 365 `
  --tune-step-days 56 `
  --tune-min-train 250
```

`1000000000` days approximates no time decay (xi approximately zero).
Each candidate is fitted on results strictly **before** a validation block,
then scored on subsequent results. The optimization re-fits multiple models
per competition, so it is significantly slower than a normal run.

Outputs:

```text
football_output_v2/raw/EPL_decay_tuning.json
football_output_v2/raw/EPL_diagnostics.json
football_output_v2/raw/EPL_predictions.csv
```

The model automatically uses the selected half-life **for that competition
and current prediction run only**. Without `--tune-half-life`, existing
behavior is unchanged. The scoreline top-20 limit, live odds, fixture
providers and scoring matrix calculations are unaffected.

**Evaluation integrity:** the log-loss values used to choose the half-life are
*validation* scores, **not** independent test performance. To determine
whether tuning improves real accuracy, use a later untouched test period or
implement nested walk-forward evaluation. The CLI prevents combining
`--tune-half-life` and `--backtest` in one command because selecting
hyperparameters on the backtest period would introduce selection leakage.

The implementation follows David Sheehan's discussion of Dixon-Coles
time weighting and predictive profile likelihood:
https://dashee87.github.io/football/python/predicting-football-results-with-statistical-modelling-dixon-coles-and-time-weighting/

### Optimizer reliability

V2.2.2 calculates the exact gradient of the Dixon–Coles weighted
log-likelihood instead of asking SciPy to estimate a numerical gradient for
every attack/defence parameter. This is particularly important for UCL, which
includes more distinct clubs than most domestic competitions.

A failed or incomplete optimization is now **rejected** instead of being used
to select a half-life or to produce probability estimates. It is therefore
possible for a tuning run to fail explicitly if all candidate fits are invalid,
rather than returning misleading results.

For every competition, inspect:

- `*_decay_tuning.json`: candidate half-life, log loss, match counts and validity.
- `*_diagnostics.json`: `fit_success`, selected half-life, and optimizer information.

The large `1000000000`-day candidate approximates **no recency decay**,
not an error. It can be selected if it actually yields the best validation
log loss, but it is not proof of superior betting performance.

The self-test and automated unit tests cover the exact objective gradient,
high-dimensional synthetic fitting, and leak-free temporal validation.
Live provider calls and actual historical score validation remain separate
checks.

## Market-weight research (advanced, not part of daily use)

The optional `--auto-market-weight` research mode evaluates historical
opening-bookmaker probability blends by chronological development/audit
splits. It requires historical opening prices and can fall back to the
standard 0.50 weight when no suitable history is available. Results
are written to `<league>_market_weight_validation.json`.

This research helper remains available for a future dedicated experiment.
For now, **do not run it** in the daily-use model. Its historical audit
may overlap with half-life tuning, so it is not a final independent
assessment of prediction performance.

## Walk-forward backtest

```powershell
python football_value_pipeline_v2_standalone.py `
  --leagues EPL `
  --seasons-back 6 `
  --backtest `
  --test-start 2024-08-01 `
  --min-edge 0.05 `
  --kelly 0.25
```

Historical backtesting continues to use Football-Data.co.uk's historical opening/closing market columns; current live prices are not injected into historical matches.

## Self-test

```powershell
python football_value_pipeline_v2_standalone.py --self-test
```

The self-test checks probability normalization, matrix reweighting, and dedicated live-odds parsing, including the distinction between best prices and same-bookmaker reference markets.

## Database direction

See `DATABASE_DESIGN.md` for a proposed SQLite-first storage layer for HTTP cache, fixtures, odds snapshots, prediction runs and backtests. Database storage is intentionally separated from this live-odds change so source correctness can be validated before persistence is changed.
