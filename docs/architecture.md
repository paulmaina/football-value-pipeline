# Architecture and service layer

How the modules fit together, where staking, Elo and simulation sit, and
how an HTTP API (FastAPI) attaches without changing forecasting.

## Layers

| Layer | Modules | Responsibility |
|---|---|---|
| Configuration | `api_key_config.py`, `quote_policy.py`, `shortlist_quote_policy.json`, `LEAGUES` in the main pipeline | Credentials, league identities, quote rules |
| Data providers | `TheOddsAPI`, `FootballDataUK`, `FootballDataOrg` (main pipeline); `bbs_data.py`, `api_football_data.py`, `europa_training.py`, `ucl_training.py`, `refresh_training_data.py` | Fetch and cache fixtures, odds and results |
| Training inputs | `bbs_integration.py`, `api_football_integration.py`, `match_scores.py` | Merge histories; regulation-time scores |
| Goal model | `DixonColesModel` (main pipeline), `score_probability.py`, `bbs_statistics_model.py`, `dc_decay_validation.py` | Dixon-Coles fit, bounded score grid, gated statistics features, half-life tuning |
| Ratings | `elo_ratings.py` | Venue-aware Elo, informational fixture columns |
| Markets | `market_snapshot`, `devig`, `reweight_matrix_to_1x2` (main pipeline); `asian_handicap.py`, `double_chance.py`, `match_simulation.py` | De-vigging, market blend, settlement, exact and Monte Carlo prices |
| Validation | `goal_market_validation.py`, `market_blend_validation.py`, `backtest_league` (main pipeline), `historical_benchmark.py` | Chronological development/audit splits, calibration penalties |
| Selection | `conservative_bet_filter.py`, `asian_handicap.build_shortlist`, `quote_freshness.py` | Policy-versioned shortlist |
| Staking | `staking.py` | Advisory fractional-Kelly stakes; shared with backtest staking |
| Run integrity | `prediction_runs.py`, `pipeline_health.py`, `forecast_integrity.py`, `workflow_checks.py` | Immutable bundles, hashes, CI gates |
| Tracking | `performance_tracking.py`, `closing_odds.py`, `github_closing_odds.py`, `performance_excel.py`, `format_football_output.py` | Grading, CLV, reports |
| Experiments | `*_experiment.py` | Shadow research; never alter production outputs |
| Service | `pipeline_service.py` | Read-only, JSON-safe access for an API |

## One forecast run

```text
main()                                    prediction_runs.stage_run (lock + staging dir)
 └─ _generate_main()
     ├─ per league
     │   ├─ dc_decay_validation.tune_half_life          (optional)
     │   ├─ FootballValuePipelineV2.run_league
     │   │   ├─ _history_for_league  -> bbs/api-football augmentation
     │   │   ├─ DixonColesModel.fit  -> bbs_statistics_model (gated)
     │   │   ├─ elo_ratings.fit_history                  informational columns
     │   │   ├─ _current_fixtures / _attach_live_odds    (The Odds API ...)
     │   │   └─ _predict_row: score_grid -> 50/50 market reweight -> markets
     │   └─ goal_market_validation (walk-forward, cached by code fingerprint)
     ├─ conservative_bet_filter.build_conservative_shortlist
     ├─ staking.write_stake_recommendations              stake_recommendations.csv
     └─ shadow experiments (failures never block the run)
 workflow_checks.raw_check -> prediction_runs.publish_run (manifest + pointer)
```

## Stake recommendations

`stake_recommendations.csv` is written beside the shortlist in every run
bundle. It sizes STRICT selections only and never changes the shortlist.

* **Probability basis:** `rank_probability`, the calibration-penalised
  probability. For Asian handicaps the same penalty moves probability from
  winning outcomes to a full loss, so the stake uses exactly the
  distribution behind `conservative_estimated_ev`.
* **Sizing:** `min(kelly_multiplier * f*, stake_cap)`, where `f*`
  maximises expected log growth over the win/half/refund/loss outcomes
  (the closed form `(p*b - q) / b` for win/lose bets). If the combined
  stake exceeds `stake_max_exposure`, every stake is scaled down
  proportionally.
* **Flags:** `--stake-bankroll 100 --stake-kelly-fraction 0.25 --stake-cap 0.025 --stake-max-exposure 0.10`
  (defaults shown). The historical `--backtest` keeps its own `--kelly` and
  `--max-stake-pct`, and computes `f*` with the same `staking.kelly_fraction`.

## Elo ratings

`elo_ratings.py` adds `elo_home_rating`, `elo_away_rating`,
`elo_rating_diff` and `elo_home_expectancy` to every prediction row, plus
`elo_ratings` in each league's diagnostics. Promoted teams enter at the
25th percentile of existing ratings, and ratings regress 20% towards the
mean after a summer gap. The columns are informational: they do not
change probabilities, so any use of Elo in the model must first pass the
same chronological validation as other experiments.
`elo_ratings.pre_match_ratings` produces leakage-free walk-forward
features for that purpose.

## Monte Carlo

`match_simulation.simulate_fixture` samples 10,000 scorelines from the
production score grid and settles 1X2, totals, BTTS and Asian handicaps
with the production settlement rules. It reports the standard error and
the zero-EV "true decimal price" next to the exact grid values. The grid
is exact, so simulation is a consistency check and the place to plug in a
future game-state or in-play score process. It is not a replacement for
grid pricing.

## FastAPI attachment

Forecasting stays in the scheduled CLI. An API should only read the
validated current bundle, so a request never triggers a model fit or a
paid odds call. `pipeline_service.py` is that boundary; a FastAPI app is a
thin wrapper:

```python
from fastapi import FastAPI
import pipeline_service as svc

app = FastAPI()


@app.get("/runs/current")
def current_run():
    return svc.current_run()


@app.get("/predictions")
def predictions(league: str | None = None):
    return svc.predictions(league=league)


@app.get("/shortlist")
def shortlist(tier: str | None = None):
    return svc.shortlist(tier=tier)


@app.get("/stakes")
def stakes(bankroll: float | None = None):
    return svc.stake_plan(bankroll=bankroll)
```

`price_fixture(lambda_home, lambda_away, rho, odds=..., n_simulations=...)`
backs a `POST /price` route for what-if pricing from goal rates.

## Restructuring constraints

The modules stay at the repository root on purpose:

* `goal_market_validation.validation_code_fingerprint` and
  `pipeline_health.model_component_hashes` hash files by root path, and
  forward records store those hashes.
* `workflow_checks.COVERAGE_FLOORS` and `CLI_FILES`, and the GitHub
  workflows, use root file names.
* Tests patch names such as `football_value_pipeline_v2_standalone.datetime`
  and `...minimize`, which affect classes defined in that module.

To split the main pipeline into a package later, move one layer at a time
(providers first), keep the old module re-exporting the moved names, move
each patched dependency with its user, and update the hash lists in the
same commit. That one change resets validation caches once.
