# Forward prediction performance — readable dashboard

This dashboard formats the **immutable pre-kickoff** evaluation outputs.
It does not refresh results, settle bets, or change the model.

**Evaluation status:** `AWAITING_VERIFIED_RESULTS`

## At a glance

| Measure | Result |
|---|---|
| Selections tracked | 10 |
| Verified selections graded | 0 |
| Wins | 0 |
| Losses | 0 |
| Pending / unverified | 10 |
| Win rate (graded only) | — |
| Binary Brier (lower is better) | — |
| Settled selections with recorded odds | 0 |
| Total simulated profit (units) | — |
| Simulated flat-stake ROI (priced only) | — |

**Full-fixture predictions graded:** 0
**1X2 multiclass Brier (lower is better):** —

_Win rate counts only WON/LOST shortlist selections. Pending or unverifiable scores are not losses. ROI is a one-unit-per-selection simulation for settled bets with genuine recorded odds, not actual betting returns._

## STRICT versus PROVISIONAL

| Qualification tier | Verified selections graded | Wins | Losses | Pending / unverified | Win rate (graded only) | Simulated flat-stake ROI (priced only) |
|---|---|---|---|---|---|---|
| PROVISIONAL | 0 | 0 | 0 | 8 | — | — |
| STRICT | 0 | 0 | 0 | 2 | — | — |

## Performance by market

| Market | Verified selections graded | Wins | Losses | Pending / unverified | Win rate (graded only) | Simulated flat-stake ROI (priced only) |
|---|---|---|---|---|---|---|
| Away win | 0 | 0 | 0 | 0 | — | — |
| Both Teams to Score - Yes | 0 | 0 | 0 | 0 | — | — |
| Home win | 0 | 0 | 0 | 2 | — | — |
| Over 1.5 | 0 | 0 | 0 | 3 | — | — |
| Under 3.5 | 0 | 0 | 0 | 5 | — | — |

## Performance by league

| League | Verified selections graded | Wins | Losses | Pending / unverified | Win rate (graded only) | Simulated flat-stake ROI (priced only) |
|---|---|---|---|---|---|---|
| La Liga | 0 | 0 | 0 | 3 | — | — |
| Premier League | 0 | 0 | 0 | 5 | — | — |
| Serie A | 0 | 0 | 0 | 2 | — | — |

## Performance by ISO gameweek

| ISO gameweek | Verified selections graded | Wins | Losses | Pending / unverified | Win rate (graded only) | Simulated flat-stake ROI (priced only) |
|---|---|---|---|---|---|---|
| 2026-W41 | 0 | 0 | 0 | 3 | — | — |
| 2026-W42 | 0 | 0 | 0 | 6 | — | — |
| 2026-W43 | 0 | 0 | 0 | 1 | — | — |

## All-fixture direction accuracy

This checks whether each predicted event crossed a **50% cutoff**; it is **not** the selected-bet hit rate.

| Prediction type | Verified predictions scored | Correct | Hit rate |
|---|---|---|---|
| Most likely 1X2 | 0 | 0 | — |
| Over 1.5 (50% cutoff) | 0 | 0 | — |
| Under 3.5 (50% cutoff) | 0 | 0 | — |
| BTTS Yes (50% cutoff) | 0 | 0 | — |
| BTTS No (50% cutoff) | 0 | 0 | — |

## Confidence calibration (selected bets)

_No observations yet._

_Compare mean forecast with observed win rate. Empty bins or small samples do not establish calibration._

## Cumulative simulated results by gameweek

| Week | Graded | Wins | Losses | Week profit (units) | Cumulative ROI |
|---|---|---|---|---|---|
| 2026-W41 | 0 | 0 | 0 | — | — |
| 2026-W42 | 0 | 0 | 0 | — | — |
| 2026-W43 | 0 | 0 | 0 | — | — |

## Pending/unverified and data-quality issues

| Reason | Selections |
|---|---|
| Awaiting kickoff or verified 90-minute result | 10 |

### Result-provider errors

_No observations yet._

## Weekly match-by-match grades

- [2026-W41 details](performance_weekly/2026-W41_report.md)
- [2026-W42 details](performance_weekly/2026-W42_report.md)
- [2026-W43 details](performance_weekly/2026-W43_report.md)

## Audit and interpretation

- Source of truth: `../performance/metrics.json`, `shortlist_grades.csv` and `prediction_grades.csv`.
- Snapshot commit and source fixture identifiers remain available in the detailed readable CSV files.
- `STRICT` and `PROVISIONAL` are reported separately; provisional selections are not audited recommendations.
- Win rate is not calibration; short-run results and simulated ROI can be noisy.
- The original 90-minute verification rules and eligibility checks remain in `performance_tracking.py`.
