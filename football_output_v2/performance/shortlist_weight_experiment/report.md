# Shortlist probability / EV weighting comparison

Forward-only paper comparison: 100/0, 75/25, 50/50 (control), 25/75 probability/EV weights. All use the same frozen seven-market pool, 48-hour horizon, prices, costs and one-market-per-match top ten. Primary results include ALL selections, with STRICT/PROVISIONAL shown separately. First eligible usable capture per fixture only; no historical backfill or repeated stakes. Win rates include Wilson intervals. Profit differences pair each verified usable fixture with control, using one unit for a selection and zero if skipped. Weekly block bootstrap intervals are exploratory, unadjusted for three comparisons, and unavailable before six weeks/100 paired fixtures. Selection-cohort Brier scores do not prove improved forecasts. Readiness requires 300 verified usable fixtures, six ISO weeks, 80% resolved coverage and 100 settled picks per weighting. No automatic production change. Confirm any chosen weighting on a later untouched period.

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

| Alternative | Profit delta / usable fixture vs 50/50 | Weekly bootstrap 95% interval |
|---|---:|---|
| probability_100_ev_0 | n.a. | Collect more data |
| probability_75_ev_25 | n.a. | Collect more data |
| probability_25_ev_75 | n.a. | Collect more data |

Full calibration, Brier/log-loss diagnostics, league/market/week breakdowns and review gates are in summary.json. Frozen selections and every candidate decision are retained in CSV. A ready report permits review only; it never changes production.
