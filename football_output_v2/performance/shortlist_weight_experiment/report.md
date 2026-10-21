# Shortlist probability / EV weighting comparison

Forward-only paper comparison: 100/0, 75/25, 50/50 (control), 25/75 probability/EV weights and adaptive evidence weights. All use the same frozen candidate market pool within each capture, 48-hour horizon, prices, costs and one-market-per-match policy cap (12 in v15/v16; 10 in archived v14). Primary results include ALL selections, with STRICT/PROVISIONAL shown separately. First eligible usable capture per fixture only; no historical backfill or repeated stakes. Win rates include Wilson intervals. Profit differences pair each verified usable fixture with control, using one unit for a selection and zero if skipped. Weekly block bootstrap intervals are exploratory, unadjusted for four comparisons in v2 (three in legacy v1), and unavailable before six weeks/100 paired fixtures. Selection-cohort Brier scores do not prove improved forecasts. Readiness requires 300 verified usable fixtures, six ISO weeks, 80% resolved coverage and 100 settled picks per weighting. Adaptive probability weight ranges from 50% to 90%, using only frozen development support, development calibration penalties, raw model/reference disagreement and quote age. These bounds are a pre-registered hypothesis, not fitted optimal weights or a safety guarantee. Legacy v1 results remain a separate cohort; v2 readiness and paired returns use only contemporaneous v2 captures. No automatic production change. Confirm any chosen weighting on a later untouched period.

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
| 50% / 50% | ALL | 18 | 17 | 0.8824 | 65.7% to 96.7% | 0.1947 | 3.3100 | 0.3300 |
| 50% / 50% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 50% / 50% | PROVISIONAL | 18 | 17 | 0.8824 | 65.7% to 96.7% | 0.1947 | 3.3100 | 0.3300 |
| 100% / 0% | ALL | 19 | 17 | 0.7647 | 52.7% to 90.4% | -0.1041 | -1.7700 | 1.8600 |
| 100% / 0% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 100% / 0% | PROVISIONAL | 19 | 17 | 0.7647 | 52.7% to 90.4% | -0.1041 | -1.7700 | 1.8600 |
| 75% / 25% | ALL | 19 | 17 | 0.8235 | 59.0% to 93.8% | -0.0259 | -0.4400 | 1.3100 |
| 75% / 25% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 75% / 25% | PROVISIONAL | 19 | 17 | 0.8235 | 59.0% to 93.8% | -0.0259 | -0.4400 | 1.3100 |
| 25% / 75% | ALL | 18 | 18 | 0.5556 | 33.7% to 75.4% | -0.1239 | -2.2300 | 2.3300 |
| 25% / 75% | STRICT | 0 | 0 | n.a. | Collect more data | n.a. | 0.0000 | n.a. |
| 25% / 75% | PROVISIONAL | 18 | 18 | 0.5556 | 33.7% to 75.4% | -0.1239 | -2.2300 | 2.3300 |

| Weighting | Brier | Log loss | Calibration gap | Mean probability weight | Min / max probability weight |
|---|---:|---:|---:|---:|---|
| 50% / 50% | 0.1277 | 0.4204 | -0.1157 | 0.5000 | 0.5000 / 0.5000 |
| 100% / 0% | 0.1722 | 0.5133 | 0.0549 | 1.0000 | 1.0000 / 1.0000 |
| 75% / 25% | 0.1341 | 0.4227 | -0.0075 | 0.7500 | 0.7500 / 0.7500 |
| 25% / 75% | 0.2258 | 0.6370 | 0.1025 | 0.2500 | 0.2500 / 0.2500 |

| Alternative | Profit delta / usable fixture vs 50/50 | Weekly bootstrap 95% interval |
|---|---:|---|
| probability_100_ev_0 | -0.2540 | Collect more data |
| probability_75_ev_25 | -0.1875 | Collect more data |
| probability_25_ev_75 | -0.2770 | Collect more data |

Full calibration, Brier/log-loss diagnostics, league/market/week breakdowns and review gates are in summary.json. Frozen selections and every candidate decision are retained in CSV. A ready report permits review only; it never changes production.
