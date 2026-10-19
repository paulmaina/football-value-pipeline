# Shortlist probability / EV weighting comparison

Forward-only paper comparison: 100/0, 75/25, 50/50 (control), 25/75 probability/EV weights and adaptive evidence weights. All use the same frozen seven-market pool, 48-hour horizon, prices, costs and one-market-per-match policy cap (12 in v15; 10 in archived v14). Primary results include ALL selections, with STRICT/PROVISIONAL shown separately. First eligible usable capture per fixture only; no historical backfill or repeated stakes. Win rates include Wilson intervals. Profit differences pair each verified usable fixture with control, using one unit for a selection and zero if skipped. Weekly block bootstrap intervals are exploratory, unadjusted for four comparisons in v2 (three in legacy v1), and unavailable before six weeks/100 paired fixtures. Selection-cohort Brier scores do not prove improved forecasts. Readiness requires 300 verified usable fixtures, six ISO weeks, 80% resolved coverage and 100 settled picks per weighting. Adaptive probability weight ranges from 50% to 90%, using only frozen development support, development calibration penalties, raw model/reference disagreement and quote age. These bounds are a pre-registered hypothesis, not fitted optimal weights or a safety guarantee. Legacy v1 results remain a separate cohort; v2 readiness and paired returns use only contemporaneous v2 captures. No automatic production change. Confirm any chosen weighting on a later untouched period.

Status: COLLECT_MORE_DATA

| Probability / EV | Tier | Selected | Settled | Win rate | Win rate 95% interval | Net ROI | Profit (units) | Drawdown (units) |
|---|---|---:|---:|---:|---|---:|---:|---:|
| 50% / 50% | ALL | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 50% / 50% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 50% / 50% | PROVISIONAL | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 100% / 0% | ALL | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 100% / 0% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 100% / 0% | PROVISIONAL | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 75% / 25% | ALL | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 75% / 25% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 75% / 25% | PROVISIONAL | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 25% / 75% | ALL | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 25% / 75% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 25% / 75% | PROVISIONAL | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| Adaptive evidence | ALL | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| Adaptive evidence | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| Adaptive evidence | PROVISIONAL | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |

| Weighting | Brier | Log loss | Calibration gap | Mean probability weight | Min / max probability weight |
|---|---:|---:|---:|---:|---|
| 50% / 50% | n.a. | n.a. | n.a. | 0.5000 | 0.5000 / 0.5000 |
| 100% / 0% | n.a. | n.a. | n.a. | 1.0000 | 1.0000 / 1.0000 |
| 75% / 25% | n.a. | n.a. | n.a. | 0.7500 | 0.7500 / 0.7500 |
| 25% / 75% | n.a. | n.a. | n.a. | 0.2500 | 0.2500 / 0.2500 |
| Adaptive evidence | n.a. | n.a. | n.a. | n.a. | n.a. / n.a. |

| Alternative | Profit delta / usable fixture vs 50/50 | Weekly bootstrap 95% interval |
|---|---:|---|
| probability_100_ev_0 | n.a. | Collect more data |
| probability_75_ev_25 | n.a. | Collect more data |
| probability_25_ev_75 | n.a. | Collect more data |
| adaptive_evidence | n.a. | Collect more data |

## Legacy v1 fixed-weight cohort (separate results)

| Probability / EV | Tier | Selected | Settled | Win rate | Win rate 95% interval | Net ROI | Profit (units) | Drawdown (units) |
|---|---|---:|---:|---:|---|---:|---:|---:|
| 50% / 50% | ALL | 18 | 9 | 0.8889 | 56.5% to 98.0% | 0.2167 | 1.9500 | 0.3300 |
| 50% / 50% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 50% / 50% | PROVISIONAL | 18 | 9 | 0.8889 | 56.5% to 98.0% | 0.2167 | 1.9500 | 0.3300 |
| 100% / 0% | ALL | 19 | 9 | 0.7778 | 45.3% to 93.7% | -0.0422 | -0.3800 | 1.0000 |
| 100% / 0% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 100% / 0% | PROVISIONAL | 19 | 9 | 0.7778 | 45.3% to 93.7% | -0.0422 | -0.3800 | 1.0000 |
| 75% / 25% | ALL | 19 | 9 | 0.7778 | 45.3% to 93.7% | -0.0422 | -0.3800 | 1.0000 |
| 75% / 25% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 75% / 25% | PROVISIONAL | 19 | 9 | 0.7778 | 45.3% to 93.7% | -0.0422 | -0.3800 | 1.0000 |
| 25% / 75% | ALL | 18 | 10 | 0.5000 | 23.7% to 76.3% | -0.1670 | -1.6700 | 2.3300 |
| 25% / 75% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 25% / 75% | PROVISIONAL | 18 | 10 | 0.5000 | 23.7% to 76.3% | -0.1670 | -1.6700 | 2.3300 |

| Weighting | Brier | Log loss | Calibration gap | Mean probability weight | Min / max probability weight |
|---|---:|---:|---:|---:|---|
| 50% / 50% | 0.1339 | 0.4462 | -0.1496 | 0.5000 | 0.5000 / 0.5000 |
| 100% / 0% | 0.1755 | 0.5310 | 0.0137 | 1.0000 | 1.0000 / 1.0000 |
| 75% / 25% | 0.1755 | 0.5310 | 0.0137 | 0.7500 | 0.7500 / 0.7500 |
| 25% / 75% | 0.2295 | 0.6464 | 0.1037 | 0.2500 | 0.2500 / 0.2500 |

| Alternative | Profit delta / usable fixture vs 50/50 | Weekly bootstrap 95% interval |
|---|---:|---|
| probability_100_ev_0 | -0.1942 | Collect more data |
| probability_75_ev_25 | -0.1942 | Collect more data |
| probability_25_ev_75 | -0.3017 | Collect more data |

Full calibration, Brier/log-loss diagnostics, league/market/week breakdowns and review gates are in summary.json. Frozen selections and every candidate decision are retained in CSV. A ready report permits review only; it never changes production.
