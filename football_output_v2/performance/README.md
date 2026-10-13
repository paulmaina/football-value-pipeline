# Forward-only football performance dashboard

Only immutable **Git-archived before-kickoff predictions** are scored.
Actual results come from football-data.org v4 FINISHED matches;
normal 90-minute results are used, never extra-time/penalty scorelines.
**PROVISIONAL candidates are not audited betting recommendations.**

## Cumulative shortlist

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| All selections | 7 | 4-3 | 57.1% | -21.6% |

Unsettled / unverified entries: **12**.
Whole-fixture 1X2 multiclass Brier (n=18): 0.5584

## STRICT versus PROVISIONAL

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| PROVISIONAL | 5 | 2-3 | 40.0% | -49.6% |
| STRICT | 2 | 2-0 | 100.0% | +48.5% |

## By policy

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 72h-ucl-v3 | 2 | 1-1 | 50.0% | -33.0% |
| legacy/unspecified | 5 | 3-2 | 60.0% | -17.0% |

## By market

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Away win | 0 | 0-0 | — | — |
| Both Teams to Score - Yes | 0 | 0-0 | — | — |
| Double Chance 1X | 0 | 0-0 | — | — |
| Double Chance X2 | 0 | 0-0 | — | — |
| Home win | 1 | 1-0 | 100.0% | +63.0% |
| Over 1.5 | 2 | 2-0 | 100.0% | +29.0% |
| Under 3.5 | 4 | 1-3 | 25.0% | -68.0% |

## By league

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| La Liga | 2 | 2-0 | 100.0% | +29.0% |
| Premier League | 3 | 0-3 | 0.0% | -100.0% |
| Serie A | 2 | 2-0 | 100.0% | +45.5% |
| UEFA Champions League | 0 | 0-0 | — | — |

## Gameweeks

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 2026-W41 | 4 | 2-2 | 50.0% | -37.0% |
| 2026-W42 | 3 | 2-1 | 66.7% | -1.0% |
| 2026-W43 | 0 | 0-0 | — | — |

## Confidence calibration of shortlisted markets

| Forecast bin | Samples | Average forecast | Observed win rate | Binary Brier |
|---|---:|---:|---:|---:|
| 60%–70% | 1 | 68.2% | 100.0% | 0.1009 |
| 70%–80% | 3 | 77.8% | 66.7% | 0.2197 |
| 80%–90% | 3 | 85.7% | 33.3% | 0.4683 |

Calibration bins report observed outcomes against the originally
recorded reliability-adjusted chance; small buckets are unstable.

## Result-source problems

No provider errors detected.

Accuracy is not calibration or profit. Simulated ROI assumes
one unit staked separately on each settled selection with recorded
pre-kickoff bookmaker decimal odds. These are **not real stakes**;
it is not the return from a ten-leg accumulator.
Small samples and stale/invalid prices can undermine conclusions.
A missing, ambiguous or unverified result is **never called a win**.
