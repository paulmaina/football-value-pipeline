# Forward-only football performance dashboard

Only immutable **Git-archived before-kickoff predictions** are scored.
Actual results come from football-data.org v4 FINISHED matches;
normal 90-minute results are used, never extra-time/penalty scorelines.
**PROVISIONAL candidates are not audited betting recommendations.**

The main totals use the latest eligible pre-kickoff shortlist entry for each match,
with that prediction's original market, probability, odds and costs. Each match counts once.
Later uploads of an older generation never replace a newer prediction.
Earlier predictions remain in shortlist_run_history.csv and the Run Tracking tab;
history rows are correlated records and are excluded from main win-rate/ROI totals.
Whole-fixture model metrics and research experiments retain their unique-fixture cohorts.

## Cumulative shortlist — latest prediction per match

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| All selections | 30 | 22-8 | 73.3% | +1.1% |

Unsettled / unverified entries: **12**.
Whole-fixture 1X2 multiclass Brier (n=76): 0.5338

## First-prediction reference — historical comparison

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Unique fixtures | 30 | 23-7 | 76.7% | +4.5% |

## Latest selections by prediction run (generation UTC)

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 2026-10-11T06:38:36.451450+00:00 | 2 | 2-0 | 100.0% | +32.0% |
| 2026-10-11T08:16:48.175077+00:00 | 1 | 1-0 | 100.0% | +28.0% |
| 2026-10-11T11:26:44.338551+00:00 | 4 | 2-2 | 50.0% | -28.2% |
| 2026-10-12T16:32:02.915037+00:00 | 2 | 1-1 | 50.0% | -29.0% |
| 2026-10-13T11:03:50.762232+00:00 | 1 | 1-0 | 100.0% | +45.0% |
| 2026-10-13T17:02:53.437005+00:00 | 1 | 1-0 | 100.0% | +18.0% |
| 2026-10-14T11:23:06.552356+00:00 | 0 | 0-0 | — | — |
| 2026-10-14T18:13:48.803955+00:00 | 2 | 2-0 | 100.0% | +64.5% |
| 2026-10-14T21:07:53.015698+00:00 | 1 | 1-0 | 100.0% | +27.0% |
| 2026-10-16T22:16:28.500933+00:00 | 1 | 1-0 | 100.0% | +27.0% |
| 2026-10-17T09:46:12.155774+00:00 | 2 | 1-1 | 50.0% | -36.0% |
| 2026-10-17T14:11:18.520879+00:00 | 1 | 1-0 | 100.0% | +61.0% |
| 2026-10-18T09:58:14.607821+00:00 | 1 | 1-0 | 100.0% | +20.0% |
| 2026-10-18T14:35:10.311946+00:00 | 7 | 6-1 | 85.7% | +15.0% |
| 2026-10-19T11:20:16.296665+00:00 | 1 | 0-1 | 0.0% | -100.0% |
| 2026-10-19T16:28:42.464993+00:00 | 3 | 1-2 | 33.3% | -49.0% |

## STRICT versus PROVISIONAL

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| PROVISIONAL | 19 | 12-7 | 63.2% | -15.7% |
| STRICT | 11 | 10-1 | 90.9% | +30.2% |

## By policy

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 48h-top-ten-probability-ev-no-under35-v14 | 8 | 6-2 | 75.0% | +0.6% |
| 48h-top-twelve-probability-ev-no-under35-v15 | 3 | 1-2 | 33.3% | -49.0% |
| 72h-all-markets-ev15-one-book-v6 | 1 | 1-0 | 100.0% | +45.0% |
| 72h-all-markets-net-ev15-execution-v7 | 4 | 4-0 | 100.0% | +43.5% |
| 72h-seven-markets-fresh-references-net-ev15-v11 | 5 | 4-1 | 80.0% | +7.2% |
| 72h-ucl-v2 | 1 | 1-0 | 100.0% | +28.0% |
| 72h-ucl-v3 | 6 | 3-3 | 50.0% | -28.5% |
| legacy/unspecified | 2 | 2-0 | 100.0% | +32.0% |

## By market

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Away win | 1 | 0-1 | 0.0% | -100.0% |
| Both Teams to Score - Yes | 2 | 2-0 | 100.0% | +51.0% |
| Double Chance 12 | 2 | 2-0 | 100.0% | +27.5% |
| Double Chance 1X | 4 | 3-1 | 75.0% | +0.0% |
| Double Chance X2 | 5 | 3-2 | 60.0% | -15.8% |
| Home win | 5 | 5-0 | 100.0% | +50.6% |
| Over 1.5 | 6 | 5-1 | 83.3% | +5.5% |
| Under 3.5 | 5 | 2-3 | 40.0% | -46.0% |

## By league

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Bundesliga | 3 | 3-0 | 100.0% | +24.7% |
| La Liga | 7 | 7-0 | 100.0% | +33.6% |
| Ligue 1 | 2 | 1-1 | 50.0% | -16.5% |
| Premier League | 7 | 3-4 | 42.9% | -44.9% |
| Serie A | 7 | 4-3 | 57.1% | -17.1% |
| UEFA Champions League | 4 | 4-0 | 100.0% | +48.0% |

## Gameweeks

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 2026-W41 | 4 | 2-2 | 50.0% | -37.0% |
| 2026-W42 | 22 | 19-3 | 86.4% | +19.5% |
| 2026-W43 | 4 | 1-3 | 25.0% | -61.8% |

## Confidence calibration of shortlisted markets

| Forecast bin | Samples | Average forecast | Observed win rate | Binary Brier |
|---|---:|---:|---:|---:|
| 0%–50% | 1 | 45.4% | 0.0% | 0.2059 |
| 60%–70% | 8 | 64.9% | 62.5% | 0.2235 |
| 70%–80% | 10 | 75.6% | 80.0% | 0.1675 |
| 80%–90% | 9 | 83.6% | 77.8% | 0.1769 |
| 90%–100% | 2 | 93.3% | 100.0% | 0.0047 |

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
| Bundesliga | 2026-10-18 | 1584 | 2 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| EPL | 2026-10-18 | 1969 | 2 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| LaLiga | 2026-10-18 | 1987 | 2 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Ligue1 | 2026-10-18 | 1741 | 2 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| SerieA | 2026-10-19 | 1969 | 1 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| UCL | 2026-10-14 | 539 | 6 | CURRENT_WITHIN_PROVIDER_SCHEDULE |

Latest shortlist audit: {"selected_quotes": 12, "exchange_quotes": 0, "missing_quote_age": 0, "quote_age_over_24h": 0, "costs_recorded": 12, "bookmakers": {"1xBet": 8, "Pinnacle": 4}, "account_availability": "NOT_VERIFIED_WITH_BOOKMAKER_ACCOUNTS", "past_kickoff_count": 0, "upcoming_kickoff_count": 12, "unknown_kickoff_count": 0}.

Source refresh does not retrain stored forecasts. Days since the last match do not by themselves establish missing data.

| Snapshot | Goal blend | Market led | Recency | Filter sensitivity |
|---|---|---|---|---|
| 010ef527d5bf | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| d3f12df5a2a2 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| e5dcb5f67050 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 54bb8a2c2c95 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| a98524037f73 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 758c1097916a | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 376b9f9ba8a8 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| b57f98f7704e | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 2db2af40cdce | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 9425e536c27c | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 7a6c9d44b7c2 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 98adf7e32c9e | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 2a86586863a4 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 3a3ff5eef038 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| b4dfb7c51677 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 67fd2fe2099c | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 4827bd2b8014 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| f7295b8c0c24 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| ca1e126489f9 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| a18515a42a8d | CAPTURED | CAPTURED | CAPTURED | CAPTURED |

Dependency versions at review: {"python": "3.12.15", "numpy": "2.5.4", "pandas": "3.0.6", "scipy": "1.18.1", "requests": "2.34.2", "rapidfuzz": "3.14.6", "python-dotenv": "1.2.4", "coverage": "NOT_INSTALLED", "PyYAML": "NOT_INSTALLED"}. Forecast-generation versions are recorded in new frozen snapshot health; legacy generation environments are unknown.

Closing odds: [report](closing_odds/report.md). Latest-selection comparison aligned with headline ROI, with a separate first-entry reference; official close and accepted execution are unverified.

Totals anchoring: [report](totals_anchor_experiment/report.md). Separate Pinnacle trial, no production probability changes.

Experiment review queue: [report](experiment_review_queue.md). Benchmark candidate capture and readiness are evaluated automatically; no production promotion.

Filter sensitivity: [report](filter_sensitivity_experiment/report.md). Frozen 1.5%, 3% and 5% adjusted EV policies; production unchanged.

Shortlist probability/EV weights: [report](shortlist_weight_experiment/report.md). Four frozen weightings; production stays 50/50.

Probability/calibration policies: [report](shortlist_policy_experiment/report.md). Fixed one-factor cutoffs and development-only penalty strengths; production unchanged.

Recency comparisons: [report](recency_experiment/report.md). Raw goal probabilities, chronological selection/audit and paired forward scores; no automatic promotion.

Daily observations: [health_history.json](health_history.json). Frozen forecast health: [pipeline_health.json](pipeline_health.json).

Policy and gameweek results above show sample counts, ROI and calibration. Compare experiments on paired settled forecasts; small samples and changing cohorts cannot establish improvement. Historical missing experimental data is not backfilled.
