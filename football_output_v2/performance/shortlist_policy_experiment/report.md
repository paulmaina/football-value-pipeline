# Shortlist probability and calibration comparison

Fixed one-factor comparisons, not an optimisation search. All variants use the same first eligible pre-kickoff fixtures, quotes, development-only calibration evidence and fixed audit/quote/matching gates. Primary returns use STRICT picks only; PROVISIONAL rows are watchlist simulations. Returns are simulated at frozen quotes after configured costs, not actual execution. Selected cohorts can differ: their Brier/ROI differences are not paired forecast improvements. Paired returns below use one unit per strict selection and zero for no selection on every verified fixture. Weekly block bootstrap intervals are exploratory, unadjusted for eight comparisons and unavailable before six weeks/100 verified fixtures. No automatic promotion; choose a policy only after review, then confirm it on a later untouched period.

Status: COLLECT_MORE_DATA

| Variant | Tier | Selected | Settled | Net ROI | Brier | Log loss |
|---|---|---:|---:|---:|---:|---:|
| control | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| control | PROVISIONAL | 1 | 0 | n.a. | n.a. | n.a. |
| control | ALL | 3 | 1 | 0.2700 | 0.0388 | 0.2194 |
| blended_lower | STRICT | 4 | 2 | 0.2700 | 0.0394 | 0.2213 |
| blended_lower | PROVISIONAL | 1 | 0 | n.a. | n.a. | n.a. |
| blended_lower | ALL | 5 | 2 | 0.2700 | 0.0394 | 0.2213 |
| blended_higher | STRICT | 0 | 0 | n.a. | n.a. | n.a. |
| blended_higher | PROVISIONAL | 1 | 0 | n.a. | n.a. | n.a. |
| blended_higher | ALL | 1 | 0 | n.a. | n.a. | n.a. |
| raw_lower | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| raw_lower | PROVISIONAL | 1 | 0 | n.a. | n.a. | n.a. |
| raw_lower | ALL | 3 | 1 | 0.2700 | 0.0388 | 0.2194 |
| raw_higher | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| raw_higher | PROVISIONAL | 1 | 0 | n.a. | n.a. | n.a. |
| raw_higher | ALL | 3 | 1 | 0.2700 | 0.0388 | 0.2194 |
| adjusted_lower | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| adjusted_lower | PROVISIONAL | 1 | 0 | n.a. | n.a. | n.a. |
| adjusted_lower | ALL | 3 | 1 | 0.2700 | 0.0388 | 0.2194 |
| adjusted_higher | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| adjusted_higher | PROVISIONAL | 1 | 0 | n.a. | n.a. | n.a. |
| adjusted_higher | ALL | 3 | 1 | 0.2700 | 0.0388 | 0.2194 |
| penalty_half | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| penalty_half | PROVISIONAL | 1 | 0 | n.a. | n.a. | n.a. |
| penalty_half | ALL | 3 | 1 | 0.2700 | 0.0388 | 0.2194 |
| penalty_stronger | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| penalty_stronger | PROVISIONAL | 1 | 0 | n.a. | n.a. | n.a. |
| penalty_stronger | ALL | 3 | 1 | 0.2700 | 0.0388 | 0.2194 |

Frozen grid: blended/raw/adjusted cutoffs each ±3 percentage points independently; calibration penalty ×0.5 or ×1.5. All other settings stay fixed.

Detailed calibration bins, drawdowns, weekly/league/market results, common-cohort scores and paired return uncertainty are in summary.json. All rejected candidates are retained in candidate_decisions.csv. Old captures are never backfilled.
