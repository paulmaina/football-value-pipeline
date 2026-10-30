# Forward-only football performance dashboard

Only immutable **Git-archived before-kickoff predictions** are scored.
Asian handicaps settle full/half wins, refunds and full/half losses. ROI includes every settled stake; refunds are not wins. Probability/Brier follows the frozen event: v23-v25 profitable outcome; v22, v26 and older Asian no net loss.
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
| All selections | 62 | 47-14 | 75.8% | +6.8% |

Unsettled / unverified entries: **15**.
Whole-fixture 1X2 multiclass Brier (n=177): 0.5692

## First-prediction reference — historical comparison

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Unique fixtures | 62 | 51-10 | 82.3% | +13.1% |

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
| 2026-10-19T16:28:42.464993+00:00 | 11 | 7-4 | 63.6% | -12.5% |
| 2026-10-22T10:58:13.963804+00:00 | 1 | 1-0 | 100.0% | +20.0% |
| 2026-10-23T14:36:42.857608+00:00 | 6 | 6-0 | 100.0% | +36.2% |
| 2026-10-23T16:24:03.614429+00:00 | 0 | 0-0 | — | — |
| 2026-10-24T14:22:17.608235+00:00 | 2 | 2-0 | 100.0% | +81.0% |
| 2026-10-24T14:27:12.490111+00:00 | 1 | 0-1 | 0.0% | -100.0% |
| 2026-10-25T10:24:47.847996+00:00 | 12 | 9-3 | 75.0% | +3.8% |
| 2026-10-26T11:01:43.961218+00:00 | 1 | 0-0 | 0.0% | +0.0% |
| 2026-10-26T11:45:55.025240+00:00 | 0 | 0-0 | — | — |
| 2026-10-29T12:08:22.532184+00:00 | 1 | 1-0 | 100.0% | +34.0% |
| 2026-10-30T12:03:48.308948+00:00 | 0 | 0-0 | — | — |

## STRICT versus PROVISIONAL

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| PROVISIONAL | 27 | 18-9 | 66.7% | -10.7% |
| STRICT | 35 | 29-5 | 82.9% | +20.3% |

## By policy

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 48h-top-ten-probability-ev-no-under35-v14 | 8 | 6-2 | 75.0% | +0.6% |
| 48h-top-twelve-probability-ev-no-under35-v15 | 11 | 7-4 | 63.6% | -12.5% |
| 48h-top-twelve-profitable-win-probability-v23 | 0 | 0-0 | — | — |
| 48h-two-per-market-group-probability-ev-corners-cards-v25 | 12 | 9-3 | 75.0% | +3.8% |
| 48h-two-per-market-group-probability-ev-v24 | 3 | 2-1 | 66.7% | +20.7% |
| 48h-zero-tolerance-ev05-no-loss75-corners-v26 | 2 | 1-0 | 50.0% | +17.0% |
| 48h-zero-tolerance-ev1-common-no-loss75-v22 | 7 | 7-0 | 100.0% | +33.9% |
| 72h-all-markets-ev15-one-book-v6 | 1 | 1-0 | 100.0% | +45.0% |
| 72h-all-markets-net-ev15-execution-v7 | 4 | 4-0 | 100.0% | +43.5% |
| 72h-seven-markets-fresh-references-net-ev15-v11 | 5 | 4-1 | 80.0% | +7.2% |
| 72h-ucl-v2 | 1 | 1-0 | 100.0% | +28.0% |
| 72h-ucl-v3 | 6 | 3-3 | 50.0% | -28.5% |
| legacy/unspecified | 2 | 2-0 | 100.0% | +32.0% |

## By market

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Asian Handicap Away +0.00 | 0 | 0-0 | — | — |
| Asian Handicap Away +0.25 | 0 | 0-0 | — | — |
| Asian Handicap Away +0.50 | 0 | 0-0 | — | — |
| Asian Handicap Away +0.75 | 0 | 0-0 | — | — |
| Asian Handicap Away +1.00 | 2 | 2-0 | 100.0% | +46.0% |
| Asian Handicap Away +1.25 | 1 | 1-0 | 100.0% | +16.0% |
| Asian Handicap Away +1.50 | 0 | 0-0 | — | — |
| Asian Handicap Away +1.75 | 0 | 0-0 | — | — |
| Asian Handicap Away +2.00 | 4 | 3-0 | 75.0% | +29.2% |
| Asian Handicap Away +2.25 | 0 | 0-0 | — | — |
| Asian Handicap Away +2.50 | 0 | 0-0 | — | — |
| Asian Handicap Away +2.75 | 0 | 0-0 | — | — |
| Asian Handicap Away +3.00 | 0 | 0-0 | — | — |
| Asian Handicap Away -0.25 | 0 | 0-0 | — | — |
| Asian Handicap Away -0.50 | 0 | 0-0 | — | — |
| Asian Handicap Away -0.75 | 0 | 0-0 | — | — |
| Asian Handicap Away -1.00 | 0 | 0-0 | — | — |
| Asian Handicap Away -1.25 | 0 | 0-0 | — | — |
| Asian Handicap Away -1.50 | 0 | 0-0 | — | — |
| Asian Handicap Away -1.75 | 0 | 0-0 | — | — |
| Asian Handicap Away -2.00 | 0 | 0-0 | — | — |
| Asian Handicap Away -2.25 | 0 | 0-0 | — | — |
| Asian Handicap Away -2.50 | 0 | 0-0 | — | — |
| Asian Handicap Away -2.75 | 0 | 0-0 | — | — |
| Asian Handicap Away -3.00 | 0 | 0-0 | — | — |
| Asian Handicap Home +0.00 | 0 | 0-0 | — | — |
| Asian Handicap Home +0.25 | 0 | 0-0 | — | — |
| Asian Handicap Home +0.50 | 0 | 0-0 | — | — |
| Asian Handicap Home +0.75 | 0 | 0-0 | — | — |
| Asian Handicap Home +1.00 | 0 | 0-0 | — | — |
| Asian Handicap Home +1.25 | 1 | 1-0 | 100.0% | +60.0% |
| Asian Handicap Home +1.50 | 0 | 0-0 | — | — |
| Asian Handicap Home +1.75 | 0 | 0-0 | — | — |
| Asian Handicap Home +2.00 | 1 | 1-0 | 100.0% | +26.0% |
| Asian Handicap Home +2.25 | 1 | 1-0 | 100.0% | +35.0% |
| Asian Handicap Home +2.50 | 0 | 0-0 | — | — |
| Asian Handicap Home +2.75 | 0 | 0-0 | — | — |
| Asian Handicap Home +3.00 | 0 | 0-0 | — | — |
| Asian Handicap Home -0.25 | 0 | 0-0 | — | — |
| Asian Handicap Home -0.50 | 0 | 0-0 | — | — |
| Asian Handicap Home -0.75 | 0 | 0-0 | — | — |
| Asian Handicap Home -1.00 | 0 | 0-0 | — | — |
| Asian Handicap Home -1.25 | 0 | 0-0 | — | — |
| Asian Handicap Home -1.50 | 0 | 0-0 | — | — |
| Asian Handicap Home -1.75 | 0 | 0-0 | — | — |
| Asian Handicap Home -2.00 | 0 | 0-0 | — | — |
| Asian Handicap Home -2.25 | 0 | 0-0 | — | — |
| Asian Handicap Home -2.50 | 0 | 0-0 | — | — |
| Asian Handicap Home -2.75 | 0 | 0-0 | — | — |
| Asian Handicap Home -3.00 | 0 | 0-0 | — | — |
| Away win | 4 | 2-2 | 50.0% | +11.5% |
| Both Teams to Score - Yes | 3 | 2-1 | 66.7% | +0.7% |
| Corners Over 10.5 | 0 | 0-0 | — | — |
| Corners Over 11.5 | 0 | 0-0 | — | — |
| Corners Over 12.5 | 0 | 0-0 | — | — |
| Corners Over 7.5 | 0 | 0-0 | — | — |
| Corners Over 8.5 | 0 | 0-0 | — | — |
| Corners Over 9.5 | 0 | 0-0 | — | — |
| Corners Under 10.5 | 1 | 1-0 | 100.0% | +53.0% |
| Corners Under 11.5 | 0 | 0-0 | — | — |
| Corners Under 12.5 | 0 | 0-0 | — | — |
| Corners Under 7.5 | 0 | 0-0 | — | — |
| Corners Under 8.5 | 0 | 0-0 | — | — |
| Corners Under 9.5 | 0 | 0-0 | — | — |
| Double Chance 12 | 7 | 6-1 | 85.7% | +5.4% |
| Double Chance 1X | 8 | 7-1 | 87.5% | +7.8% |
| Double Chance X2 | 8 | 6-2 | 75.0% | +11.2% |
| Draw | 0 | 0-0 | — | — |
| Home win | 8 | 5-3 | 62.5% | -5.9% |
| Over 1.5 | 8 | 7-1 | 87.5% | +7.8% |
| Under 3.5 | 5 | 2-3 | 40.0% | -46.0% |

## By league

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Bundesliga | 8 | 7-1 | 87.5% | +10.8% |
| Eredivisie | 2 | 1-1 | 50.0% | -32.5% |
| La Liga | 10 | 10-0 | 100.0% | +33.5% |
| Ligue 1 | 5 | 3-2 | 60.0% | -18.4% |
| Premier League | 10 | 6-4 | 60.0% | -9.1% |
| Primeira Liga | 1 | 1-0 | 100.0% | +109.0% |
| Serie A | 14 | 9-4 | 64.3% | -4.4% |
| UEFA Champions League | 12 | 10-2 | 83.3% | +16.8% |

## Gameweeks

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 2026-W41 | 4 | 2-2 | 50.0% | -37.0% |
| 2026-W42 | 22 | 19-3 | 86.4% | +19.5% |
| 2026-W43 | 34 | 25-9 | 73.5% | +3.1% |
| 2026-W44 | 2 | 1-0 | 50.0% | +17.0% |

## Confidence calibration of shortlisted markets

| Forecast bin | Samples | Average forecast | Observed event rate (frozen probability basis) | Binary Brier |
|---|---:|---:|---:|---:|
| 0%–50% | 5 | 44.7% | 40.0% | 0.2733 |
| 50%–60% | 2 | 56.7% | 50.0% | 0.2721 |
| 60%–70% | 9 | 64.4% | 55.6% | 0.2389 |
| 70%–80% | 22 | 76.2% | 81.8% | 0.1507 |
| 80%–90% | 20 | 83.9% | 90.0% | 0.0936 |
| 90%–100% | 4 | 92.8% | 100.0% | 0.0053 |

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
| Bundesliga | 2026-10-25 | 1595 | 5 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| EPL | 2026-10-25 | 1980 | 5 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Eredivisie | 2026-10-25 | 1620 | 5 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| LaLiga | 2026-10-26 | 1999 | 4 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Ligue1 | 2026-10-26 | 1752 | 4 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| PrimeiraLiga | 2026-10-26 | 1611 | 4 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| SerieA | 2026-10-29 | 1990 | 1 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| SuperLig | 2026-10-26 | 1831 | 4 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| UCL | 2026-10-21 | 557 | 9 | CURRENT_WITHIN_PROVIDER_SCHEDULE |
| UEL | 2026-10-22 | 714 | 8 | VERIFIED_WITHIN_24_HOURS |

Latest shortlist audit: {"selected_quotes": 3, "exchange_quotes": 0, "missing_quote_age": 0, "quote_age_over_24h": 0, "costs_recorded": 3, "bookmakers": {"Pinnacle": 3}, "account_availability": "NOT_VERIFIED_WITH_BOOKMAKER_ACCOUNTS", "past_kickoff_count": 0, "upcoming_kickoff_count": 3, "unknown_kickoff_count": 0}.

Source refresh does not retrain stored forecasts. Days since the last match do not by themselves establish missing data.

| Snapshot | Goal blend | Market led | Recency | Filter sensitivity |
|---|---|---|---|---|
| 4c569effb9e7 | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| 4613e5b8880d | CAPTURED | CAPTURED | CAPTURED | CAPTURED |
| d737a7a239cb | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| 93aabf61cc3a | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| 0117b0e0fe09 | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| 10a7df008090 | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| 2b085cc83b2c | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| 089cdbb10f80 | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| 007f589ff289 | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| ac2ae4201750 | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| b5f46a88705f | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| 61fd07517a6d | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| be93fe1f5e1c | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| 026e1ab4c40e | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| d414de1a572b | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| 04e55dde9bbe | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| fd052ff5e9f0 | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| c75d4ab52706 | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| 02d8d3b21fd6 | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |
| 2f2bbe3e322e | CAPTURED | CAPTURED | CAPTURED | NOT_GENERATED |

Dependency versions at review: {"python": "3.12.15", "numpy": "2.5.4", "pandas": "3.1.0", "scipy": "1.18.1", "requests": "2.34.2", "rapidfuzz": "3.14.6", "python-dotenv": "1.2.4", "coverage": "NOT_INSTALLED", "PyYAML": "NOT_INSTALLED"}. Forecast-generation versions are recorded in new frozen snapshot health; legacy generation environments are unknown.

Closing odds: [report](closing_odds/report.md). Latest-selection comparison aligned with headline ROI, with a separate first-entry reference; official close and accepted execution are unverified.

Totals anchoring: [report](totals_anchor_experiment/report.md). Separate Pinnacle trial, no production probability changes.

Experiment review queue: [report](experiment_review_queue.md). Benchmark candidate capture and readiness are evaluated automatically; no production promotion.

Filter sensitivity: [report](filter_sensitivity_experiment/report.md). Frozen 1.5%, 3% and 5% adjusted EV policies; production unchanged.

Shortlist probability/EV weights: [report](shortlist_weight_experiment/report.md). Four frozen weightings; production stays 50/50.

Probability/calibration policies: [report](shortlist_policy_experiment/report.md). Fixed one-factor cutoffs and development-only penalty strengths; production unchanged.

Recency comparisons: [report](recency_experiment/report.md). Raw goal probabilities, chronological selection/audit and paired forward scores; no automatic promotion.

Daily observations: [health_history.json](health_history.json). Frozen forecast health: [pipeline_health.json](pipeline_health.json).

Policy and gameweek results above show sample counts, ROI and calibration. Compare experiments on paired settled forecasts; small samples and changing cohorts cannot establish improvement. Historical missing experimental data is not backfilled.
