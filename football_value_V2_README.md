# Football Value Pipeline V2

This is an extension of `football_value_pipeline.py`. Keep both files in the same folder.

## What V2 borrows from the original PL pipeline

The original PL script had several research controls that were stronger than the first multi-league version:

1. **Same-source 1X2 odds triples** for market probabilities. It never mixes Home from one bookmaker with Draw/Away from another when de-vigging.
2. **Power de-vigging** as the default, with proportional normalization available.
3. **Walk-forward evaluation**: train only on the past and predict the next block.
4. **Calibration/evaluation**: log loss, multiclass Brier, accuracy and a reliability table.
5. **Opening vs closing line benchmarking**. Closing prices are evaluation-only.
6. **Value filters**: minimum EV, maximum suspicious EV, minimum probability and maximum odds.
7. **Fractional Kelly / flat staking**, bankroll tracking, CLV, ROI confidence intervals and maximum drawdown.
8. **Market shrinkage** through `--market-weight`.

## Important improvement over the original market-weight idea

V2 does not simply blend the final 1X2 probability vector while leaving totals unchanged.

When `--market-weight > 0`, it reweights the Home / Draw / Away regions of the **score matrix**. Then 1X2, scorelines and Over/Under markets are recalculated from that same matrix.

This preserves internal consistency.

## What remains from the first multi-league pipeline

- EPL, La Liga, Bundesliga, Serie A, Ligue 1
- automatic Football-Data.co.uk historical/current data loading
- latest fixture loading
- recency-weighted Dixon-Coles Poisson model
- 1X2 fair probabilities/odds
- complete scoreline distribution
- O/U 0.5, 1.5, 2.5, 3.5 and 4.5
- caching/retries/team-name handling
- current value calculations

## Install

```bash
pip install -r football_value_requirements.txt
```

Optional reliability plot:

```bash
pip install matplotlib
```

## Current fixtures

```bash
python football_value_pipeline_v2_standalone.py --leagues EPL
```

All five configured leagues:

```bash
python football_value_pipeline_v2_standalone.py \
  --leagues EPL LaLiga Bundesliga SerieA Ligue1
```

Use a small market shrinkage:

```bash
python football_value_pipeline_v2_standalone.py \
  --leagues EPL \
  --market-weight 0.15
```

`0.0` is the default. Do not tune the market weight on the same test set you report.

## Walk-forward backtest

```bash
python football_value_pipeline_v2_standalone.py \
  --leagues EPL \
  --seasons-back 6 \
  --backtest \
  --test-start 2024-08-01 \
  --min-edge 0.05 \
  --kelly 0.25
```

Backtest outputs include:

- `EPL_backtest_predictions.csv`
- `EPL_backtest_bets.csv`
- `EPL_backtest_metrics.json`
- `EPL_reliability.csv`
- `EPL_reliability.png` if matplotlib is installed

## Why the original logit/GBM model is not directly made the primary model

The original classifier is useful for 1X2, but it does not itself produce a coherent score distribution. If its 1X2 probabilities were substituted while O/U probabilities still came from Dixon-Coles, the markets could contradict each other.

For this V2, the score matrix remains the single probability engine. The next sensible extension is a **contextual goals model** that uses the original Elo/form/chance/rest features to estimate expected home and away goals, then ensembles those expected-goal estimates with Dixon-Coles before the score matrix is generated.
