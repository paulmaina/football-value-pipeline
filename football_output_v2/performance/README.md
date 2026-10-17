# Forward-only football performance dashboard

Only immutable **Git-archived before-kickoff predictions** are scored.
Actual results come from football-data.org v4 FINISHED matches;
normal 90-minute results are used, never extra-time/penalty scorelines.
**PROVISIONAL candidates are not audited betting recommendations.**

## Cumulative shortlist

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| All selections | 14 | 10-4 | 71.4% | -2.5% |

Unsettled / unverified entries: **10**.
Whole-fixture 1X2 multiclass Brier (n=46): 0.5747

## STRICT versus PROVISIONAL

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| PROVISIONAL | 5 | 2-3 | 40.0% | -49.6% |
| STRICT | 9 | 8-1 | 88.9% | +23.7% |

## By policy

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 72h-all-markets-net-ev15-execution-v7 | 2 | 1-1 | 50.0% | -36.5% |
| 72h-seven-markets-fresh-references-net-ev15-v11 | 0 | 0-0 | — | — |
| 72h-six-markets-dc12-probability-odds-net-ev15-v9 | 1 | 1-0 | 100.0% | +27.0% |
| 72h-ucl-v3 | 6 | 5-1 | 83.3% | +16.0% |
| legacy/unspecified | 5 | 3-2 | 60.0% | -17.0% |

## By market

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Away win | 1 | 0-1 | 0.0% | -100.0% |
| Both Teams to Score - Yes | 1 | 1-0 | 100.0% | +49.0% |
| Double Chance 12 | 0 | 0-0 | — | — |
| Double Chance 1X | 1 | 1-0 | 100.0% | +27.0% |
| Double Chance X2 | 0 | 0-0 | — | — |
| Home win | 2 | 2-0 | 100.0% | +68.5% |
| Over 1.5 | 5 | 5-0 | 100.0% | +24.8% |
| Under 3.5 | 4 | 1-3 | 25.0% | -68.0% |

## By league

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Bundesliga | 1 | 1-0 | 100.0% | +27.0% |
| La Liga | 3 | 3-0 | 100.0% | +28.3% |
| Premier League | 3 | 0-3 | 0.0% | -100.0% |
| Serie A | 3 | 2-1 | 66.7% | -3.0% |
| UEFA Champions League | 4 | 4-0 | 100.0% | +40.5% |

## Gameweeks

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 2026-W41 | 4 | 2-2 | 50.0% | -37.0% |
| 2026-W42 | 10 | 8-2 | 80.0% | +11.3% |
| 2026-W43 | 0 | 0-0 | — | — |

## Confidence calibration of shortlisted markets

| Forecast bin | Samples | Average forecast | Observed win rate | Binary Brier |
|---|---:|---:|---:|---:|
| 60%–70% | 3 | 66.9% | 66.7% | 0.2167 |
| 70%–80% | 4 | 76.0% | 75.0% | 0.1865 |
| 80%–90% | 5 | 84.4% | 60.0% | 0.2934 |
| 90%–100% | 2 | 93.0% | 100.0% | 0.0052 |

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
| Bundesliga | 2026-10-16 | 964 | 1 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| EPL | 2026-10-12 | 1200 | 5 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| LaLiga | 2026-10-16 | 1219 | 1 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Ligue1 | 2026-10-16 | 973 | 1 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| SerieA | 2026-10-16 | 1201 | 1 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| UCL | 2026-10-14 | 539 | 3 | CURRENT_WITHIN_PROVIDER_SCHEDULE |

Latest shortlist audit: {"selected_quotes": 2, "exchange_quotes": 0, "missing_quote_age": 0, "quote_age_over_24h": 0, "costs_recorded": 2, "bookmakers": {"1xBet": 2}, "account_availability": "NOT_VERIFIED_WITH_BOOKMAKER_ACCOUNTS"}.

Source refresh does not retrain stored forecasts. Days since the last match do not by themselves establish missing data.

| Snapshot | Goal blend | Market led | Recency | Filter sensitivity |
|---|---|---|---|---|
| 0dba961b0bbe | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 962a7a22cb5b | CAPTURED | CAPTURED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| aea62120d25e | CAPTURED | CAPTURED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 95dc22b24994 | CAPTURED | CAPTURED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| ea202e9e045b | CAPTURED | CAPTURED | LEGACY_NOT_RECORDED | LEGACY_NOT_RECORDED |
| 6556638142ba | CAPTURED | CAPTURED | CAPTURED | LEGACY_NOT_RECORDED |
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

Dependency versions at review: {"python": "3.12.15", "numpy": "2.5.4", "pandas": "3.0.6", "scipy": "1.18.1", "requests": "2.34.2", "python-dotenv": "1.2.4", "coverage": "NOT_INSTALLED", "PyYAML": "NOT_INSTALLED"}. Forecast-generation versions are recorded in new frozen snapshot health; legacy generation environments are unknown.

Closing odds: [report](closing_odds/report.md). Locally observed near-close quotes, coverage and offered-price comparisons; official close and accepted execution are unverified.

Totals anchoring: [report](totals_anchor_experiment/report.md). Separate Pinnacle trial, no production probability changes.

Experiment review queue: [report](experiment_review_queue.md). Benchmark candidate capture and readiness are evaluated automatically; no production promotion.

Filter sensitivity: [report](filter_sensitivity_experiment/report.md). Frozen 1.5%, 3% and 5% adjusted EV policies; production unchanged.

Probability/calibration policies: [report](shortlist_policy_experiment/report.md). Fixed one-factor cutoffs and development-only penalty strengths; production unchanged.

Recency comparisons: [report](recency_experiment/report.md). Raw goal probabilities, chronological selection/audit and paired forward scores; no automatic promotion.

Daily observations: [health_history.json](health_history.json). Frozen forecast health: [pipeline_health.json](pipeline_health.json).

Policy and gameweek results above show sample counts, ROI and calibration. Compare experiments on paired settled forecasts; small samples and changing cohorts cannot establish improvement. Historical missing experimental data is not backfilled.
