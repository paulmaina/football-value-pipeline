# Shortlist probability and calibration comparison

Fixed one-factor comparisons, not an optimisation search. All variants use the same first eligible pre-kickoff fixtures, quotes, development-only calibration evidence and fixed audit/quote/matching gates. Primary returns use STRICT picks only; PROVISIONAL rows are watchlist simulations. Returns are simulated at frozen quotes after configured costs, not actual execution. Selected cohorts can differ: their Brier/ROI differences are not paired forecast improvements. Paired returns below use one unit per strict selection and zero for no selection on every verified fixture. Weekly block bootstrap intervals are exploratory, unadjusted for eight comparisons and unavailable before six weeks/100 verified fixtures. No automatic promotion; choose a policy only after review, then confirm it on a later untouched period.

Status: COLLECT_MORE_DATA

| Variant | Tier | Selected | Settled | Net ROI | Brier | Log loss |
|---|---|---:|---:|---:|---:|---:|
| control | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| control | PROVISIONAL | 2 | 1 | 0.2600 | 0.0287 | 0.1857 |
| control | ALL | 4 | 2 | 0.2650 | 0.0338 | 0.2026 |
| blended_lower | STRICT | 4 | 3 | 0.2867 | 0.0421 | 0.2293 |
| blended_lower | PROVISIONAL | 2 | 1 | 0.2600 | 0.0287 | 0.1857 |
| blended_lower | ALL | 6 | 4 | 0.2800 | 0.0387 | 0.2184 |
| blended_higher | STRICT | 0 | 0 | n.a. | n.a. | n.a. |
| blended_higher | PROVISIONAL | 2 | 1 | 0.2600 | 0.0287 | 0.1857 |
| blended_higher | ALL | 2 | 1 | 0.2600 | 0.0287 | 0.1857 |
| raw_lower | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| raw_lower | PROVISIONAL | 2 | 1 | 0.2600 | 0.0287 | 0.1857 |
| raw_lower | ALL | 4 | 2 | 0.2650 | 0.0338 | 0.2026 |
| raw_higher | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| raw_higher | PROVISIONAL | 2 | 1 | 0.2600 | 0.0287 | 0.1857 |
| raw_higher | ALL | 4 | 2 | 0.2650 | 0.0338 | 0.2026 |
| adjusted_lower | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| adjusted_lower | PROVISIONAL | 2 | 1 | 0.2600 | 0.0287 | 0.1857 |
| adjusted_lower | ALL | 4 | 2 | 0.2650 | 0.0338 | 0.2026 |
| adjusted_higher | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| adjusted_higher | PROVISIONAL | 2 | 1 | 0.2600 | 0.0287 | 0.1857 |
| adjusted_higher | ALL | 4 | 2 | 0.2650 | 0.0338 | 0.2026 |
| penalty_half | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| penalty_half | PROVISIONAL | 2 | 1 | 0.2600 | 0.0264 | 0.1774 |
| penalty_half | ALL | 4 | 2 | 0.2650 | 0.0326 | 0.1984 |
| penalty_stronger | STRICT | 2 | 1 | 0.2700 | 0.0388 | 0.2194 |
| penalty_stronger | PROVISIONAL | 2 | 1 | 0.2600 | 0.0311 | 0.1941 |
| penalty_stronger | ALL | 4 | 2 | 0.2650 | 0.0350 | 0.2068 |

Frozen grid: blended/raw/adjusted cutoffs each ±3 percentage points independently; calibration penalty ×0.5 or ×1.5. All other settings stay fixed.

Detailed calibration bins, drawdowns, weekly/league/market results, common-cohort scores and paired return uncertainty are in summary.json. All rejected candidates are retained in candidate_decisions.csv. Old captures are never backfilled.
