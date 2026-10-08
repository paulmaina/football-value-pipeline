# Football Value Pipeline V2

V2 is a multi-league football probability and value pipeline built around a recency-weighted Dixon-Coles score model.

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

`0.0` remains the default. Do not tune market weight on the same test set used for final evaluation.

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
