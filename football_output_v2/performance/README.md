# Forward-only football performance dashboard

Only immutable **Git-archived before-kickoff predictions** are scored.
Actual results come from football-data.org v4 FINISHED matches;
normal 90-minute results are used, never extra-time/penalty scorelines.
**PROVISIONAL candidates are not audited betting recommendations.**

## Cumulative shortlist

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| All selections | 9 | 6-3 | 66.7% | -9.7% |

Unsettled / unverified entries: **10**.
Whole-fixture 1X2 multiclass Brier (n=27): 0.6024

## STRICT versus PROVISIONAL

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| PROVISIONAL | 5 | 2-3 | 40.0% | -49.6% |
| STRICT | 4 | 4-0 | 100.0% | +40.2% |

## By policy

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 72h-ucl-v3 | 4 | 3-1 | 75.0% | -0.5% |
| legacy/unspecified | 5 | 3-2 | 60.0% | -17.0% |

## By market

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Away win | 0 | 0-0 | — | — |
| Both Teams to Score - Yes | 1 | 1-0 | 100.0% | +49.0% |
| Double Chance 1X | 0 | 0-0 | — | — |
| Double Chance X2 | 0 | 0-0 | — | — |
| Home win | 1 | 1-0 | 100.0% | +63.0% |
| Over 1.5 | 3 | 3-0 | 100.0% | +24.3% |
| Under 3.5 | 4 | 1-3 | 25.0% | -68.0% |

## By league

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| La Liga | 2 | 2-0 | 100.0% | +29.0% |
| Premier League | 3 | 0-3 | 0.0% | -100.0% |
| Serie A | 2 | 2-0 | 100.0% | +45.5% |
| UEFA Champions League | 2 | 2-0 | 100.0% | +32.0% |

## Gameweeks

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 2026-W41 | 4 | 2-2 | 50.0% | -37.0% |
| 2026-W42 | 5 | 4-1 | 80.0% | +12.2% |
| 2026-W43 | 0 | 0-0 | — | — |

## Confidence calibration of shortlisted markets

| Forecast bin | Samples | Average forecast | Observed win rate | Binary Brier |
|---|---:|---:|---:|---:|
| 60%–70% | 1 | 68.2% | 100.0% | 0.1009 |
| 70%–80% | 4 | 76.0% | 75.0% | 0.1865 |
| 80%–90% | 3 | 85.7% | 33.3% | 0.4683 |
| 90%–100% | 1 | 94.5% | 100.0% | 0.0031 |

Calibration bins report observed outcomes against the originally
recorded reliability-adjusted chance; small buckets are unstable.

## Result-source problems

No provider errors detected.

Accuracy is not calibration or profit. Simulated ROI assumes
one unit staked separately on each settled selection with recorded
pre-kickoff bookmaker decimal odds. These are **not real stakes**;
it is not the return from a ten-leg accumulator.
New execution-policy simulations deduct frozen per-stake costs. Legacy snapshots retain their original gross assumptions; compare policy cohorts separately.
Small samples and stale/invalid prices can undermine conclusions.
A missing, ambiguous or unverified result is **never called a win**.

## Data, execution and experiment health

| League | Model training end | Matches | Days since result | Source check |
|---|---|---:|---:|---|
| Bundesliga | 2026-10-11 | 963 | 3 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| EPL | 2026-10-12 | 1200 | 2 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| LaLiga | 2026-10-12 | 1218 | 2 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Ligue1 | 2026-10-11 | 972 | 3 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| SerieA | 2026-10-12 | 1200 | 2 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| UCL | 2026-09-10 | 521 | 34 | MODEL_BEHIND_VERIFIED_SOURCE |

Latest shortlist audit: {"selected_quotes": 4, "exchange_quotes": 0, "missing_quote_age": 0, "quote_age_over_24h": 0, "costs_recorded": 4, "bookmakers": {"1xBet": 4}, "account_availability": "NOT_VERIFIED_WITH_BOOKMAKER_ACCOUNTS"}.

Source refresh does not retrain stored forecasts. Days since the last match do not by themselves establish missing data.

| Snapshot | Goal blend | Market led | Recency | Filter sensitivity |
|---|---|---|---|---|
| 2fd31d337223 | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| bdc690a8c706 | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| b9c15c09504a | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 648ca5973f8d | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 660b75e4a311 | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| a2cdead106b5 | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 5fb257972ff2 | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| f1a72cc22d71 | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 4f7af2f470a0 | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 5496e9ba03ae | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| f6306ebd6d74 | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| fbfe5af89d06 | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 87b1676077a4 | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 0dba961b0bbe | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 962a7a22cb5b | CAPTURED | CAPTURED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| aea62120d25e | CAPTURED | CAPTURED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 95dc22b24994 | CAPTURED | CAPTURED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| ea202e9e045b | CAPTURED | CAPTURED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 6556638142ba | CAPTURED | CAPTURED | CAPTURED | LEGACY_NOT_RECORDED |
| 010ef527d5bf | CAPTURED | CAPTURED | CAPTURED | CAPTURED |

Dependency versions at review: {"python": "3.12.15", "numpy": "2.5.4", "pandas": "3.0.6", "scipy": "1.18.1", "requests": "2.34.2", "python-dotenv": "1.2.4", "coverage": "NOT_INSTALLED", "PyYAML": "NOT_INSTALLED"}. Forecast-generation versions are recorded in new frozen snapshot health; legacy generation environments are unknown.

Filter sensitivity: [report](filter_sensitivity_experiment/report.md). Frozen 1.5%, 3% and 5% adjusted EV policies; production unchanged.

Recency comparisons: [report](recency_experiment/report.md). Raw goal probabilities, chronological selection/audit and paired forward scores; no automatic promotion.

Daily observations: [health_history.json](health_history.json). Frozen forecast health: [pipeline_health.json](pipeline_health.json).

Policy and gameweek results above show sample counts, ROI and calibration. Compare experiments on paired settled forecasts; small samples and changing cohorts cannot establish improvement. Historical missing experimental data is not backfilled.
