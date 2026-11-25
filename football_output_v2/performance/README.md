# Forward-only football performance dashboard

Only immutable **Git-archived before-kickoff predictions** are scored.
Asian handicaps settle full/half wins, refunds and full/half losses. ROI includes every settled stake; refunds are not wins. Probability/Brier follows the frozen event: v23-v25 profitable outcome; v22, v26 and older Asian no net loss.
Actual results come from football-data.org v4 FINISHED matches;
normal 90-minute results are used, never extra-time/penalty scorelines.
**PROVISIONAL candidates are not audited betting recommendations.**

The main totals use the latest eligible pre-kickoff shortlist entry for each match,
with that prediction's original market, probability, odds and costs. Each match counts once.
Later uploads of an older generation never replace a newer prediction.
Earlier predictions remain in shortlist_run_history.csv;
history rows are correlated records and are excluded from main win-rate/ROI totals.
Whole-fixture model metrics and research experiments retain their unique-fixture cohorts.

## Headline: closing-line value first, returns second

| View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---:|---:|---:|---:|---:|---:|---:|
| per pick | 196 | -2.0% | -2.7% to -1.2% | 30% | 527 | +2.9% | -2.9% to +8.8% |
| per fixture (a match's picks averaged) | 122 | -1.9% | -2.8% to -0.9% | 28% | 254 | +3.6% | -3.1% to +10.3% |

544 picks on 265 matches. A match can hold several picks (one per market group); the per-fixture row averages them, so each match counts once. Closing-line value (CLV) leads because it is the less noisy measure: it compares the frozen price with the Pinnacle fair close and does not wait for results. Returns come second: with few matches they are mostly luck. Intervals are mean ± 1.96 standard errors, clustered by fixture. Near-kickoff feed quotes are not verified official closing prices.

## Research v5 (C6) rollback check

Released on 14 Nov 2026 without holdout proof (Paul's exception). After at least 150 graded matches across at least 3 weeks, roll back research v5 if its research log loss on AH all lines minus v4's, on the same frozen inputs, matches and offers, has a week-resampled 95% interval entirely above zero.

| Graded matches | Weeks | v5 − v4 log loss (AH all) | 95% interval | Status |
|---|---|---|---|---|
| 66 | 2 | +0.00346 | -0.00676 to +0.00412 | not yet eligible (needs 150 matches and 3 weeks) |

## Home favourites in Eredivisie, Primeira Liga and Süper Lig (v5 value picks)

C6 was too confident on these leagues' home sides in the holdout (home slope 0.79). Value-shortlist picks backing the home side when the v5 research makes it favourite; latest pre-kickoff pick per match.

| League | Matches | Picks | Graded | v5 predicted home win | v4 on the same forecasts | Actual home win |
|---|---|---|---|---|---|---|
| Eredivisie | 5 | 7 | 5 | 57.3% | 56.5% | 20.0% |
| Super Lig | 6 | 10 | 6 | 64.8% | 63.7% | 83.3% |
| All three | 11 | 17 | 11 | 61.4% | 60.4% | 54.5% |

## Research v6 (CE3n, UCL/UEL) rollback check

Released on 14 Nov 2026 without holdout proof (Paul's exception; not proven on the European holdout). European rows stay flagged "unvalidated view". After at least 150 graded European matches across at least 3 weeks, roll back research v6 (CE3n, UCL/UEL) if CE3n's research log loss on AH all lines minus CE's, on the same frozen inputs, matches and offers, has a week-resampled 95% interval entirely above zero (pooled over UCL and UEL). Rolling back is setting research_config.json live.european to "v4". Per competition: reported, and a warning (not a rollback) when one competition's interval is entirely above zero before the pooled trigger is eligible.

| Graded European matches | Weeks | CE3n − CE log loss (AH all) | 95% interval | Status |
|---|---|---|---|---|
| 9 | 1 | -0.05825 | — | not yet eligible (needs 150 matches and 3 weeks) |

Calibration on 9 graded European matches (6 with domestic form for both teams); logistic slopes, 1 = calibrated, below 1 too sharp. Reported, not a trigger.

| | Home slope | Away slope |
|---|---|---|
| CE3n | 1.05 | — |
| CE | 0.73 | 2.97 |

By competition (reported; a competition whose interval is entirely above zero before the pooled trigger is eligible gets a warning, not a rollback):

| Competition | Graded matches | Weeks | CE3n − CE log loss (AH all) | 95% interval | CE3n home / away slope | CE home / away slope | Warning |
|---|---|---|---|---|---|---|---|
| UCL | 9 | 1 | -0.05825 | — | 1.05 / — | 0.73 / 2.97 | no |
| UEL | 0 | 0 | — | — | — / — | — / — | no |

UCL live check of research v6: passed on the run of 2026-11-23T18:16 UTC (18 UCL fixtures; snapshot 6ad0ac014ab6ed4951104a9b707d33aa10aca058).

## Cagey correction D_pow2 rollback check

Released for domestic leagues on 17 Nov 2026 after passing its declared holdout test against D (a Bet365 safety check, not a measure of the live effect); UCL and UEL keep D. After at least 150 graded domestic matches across at least 3 weeks, roll back the cagey correction D_pow2 if its log loss on AH all lines minus D's, on the same frozen Pinnacle quotes, matches and offers, has a week-resampled 95% interval entirely above zero. Rolling back is setting cagey_correction_config.json cagey_correction_live.domestic to "D".

| Graded domestic matches | Weeks | D_pow2 − D log loss (AH all) | 95% interval | Status |
|---|---|---|---|---|
| 16 | 2 | +0.00429 | -0.00169 to +0.00628 | not yet eligible (needs 150 matches and 3 weeks) |

Fallbacks to D: where D_pow2's power grid failed its fit check, the run priced the fixture with D (flagged in cagey_correction_fallback) and the match is left out of the comparison above.

| D_pow2 runs | Domestic fixture forecasts | Priced by D (fallback) | Domestic fixtures | Fixtures with a fallback | Graded matches left out |
|---|---|---|---|---|---|
| 22 | 696 | 0 | 83 | 0 | 0 |

## Cumulative shortlist — latest prediction per match

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| All selections | 527 | 373-149 | 70.8% | +2.9% |

Unsettled / unverified entries: **17**.
Whole-fixture 1X2 multiclass Brier (n=452): 0.5451

## First-prediction reference — historical comparison

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Unique fixtures | 254 | 191-60 | 75.2% | +4.3% |

## Latest selections by prediction run (generation UTC)

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 2026-10-11T06:38:36.451450+00:00 | 2 | 2-0 | 100.0% | +32.0% |
| 2026-10-11T08:16:48.175077+00:00 | 1 | 1-0 | 100.0% | +28.0% |
| 2026-10-11T11:26:44.338551+00:00 | 5 | 2-3 | 40.0% | -42.6% |
| 2026-10-12T16:32:02.915037+00:00 | 2 | 1-1 | 50.0% | -29.0% |
| 2026-10-13T11:03:50.762232+00:00 | 1 | 1-0 | 100.0% | +45.0% |
| 2026-10-13T17:02:53.437005+00:00 | 1 | 1-0 | 100.0% | +18.0% |
| 2026-10-14T11:23:06.552356+00:00 | 1 | 1-0 | 100.0% | +11.0% |
| 2026-10-14T18:13:48.803955+00:00 | 2 | 2-0 | 100.0% | +64.5% |
| 2026-10-14T21:07:53.015698+00:00 | 1 | 1-0 | 100.0% | +27.0% |
| 2026-10-16T22:16:28.500933+00:00 | 1 | 1-0 | 100.0% | +27.0% |
| 2026-10-17T09:46:12.155774+00:00 | 2 | 1-1 | 50.0% | -36.0% |
| 2026-10-17T14:11:18.520879+00:00 | 1 | 1-0 | 100.0% | +61.0% |
| 2026-10-18T09:58:14.607821+00:00 | 1 | 1-0 | 100.0% | +20.0% |
| 2026-10-18T14:35:10.311946+00:00 | 8 | 7-1 | 87.5% | +16.5% |
| 2026-10-19T11:20:16.296665+00:00 | 1 | 0-1 | 0.0% | -100.0% |
| 2026-10-19T16:28:42.464993+00:00 | 12 | 8-4 | 66.7% | -11.4% |
| 2026-10-22T10:58:13.963804+00:00 | 1 | 1-0 | 100.0% | +20.0% |
| 2026-10-23T14:36:42.857608+00:00 | 7 | 7-0 | 100.0% | +33.4% |
| 2026-10-23T16:24:03.614429+00:00 | 1 | 1-0 | 100.0% | +15.0% |
| 2026-10-24T14:22:17.608235+00:00 | 2 | 2-0 | 100.0% | +81.0% |
| 2026-10-24T14:27:12.490111+00:00 | 2 | 0-2 | 0.0% | -100.0% |
| 2026-10-25T10:24:47.847996+00:00 | 16 | 12-4 | 75.0% | +2.6% |
| 2026-10-26T11:01:43.961218+00:00 | 1 | 0-0 | 0.0% | +0.0% |
| 2026-10-26T11:45:55.025240+00:00 | 1 | 1-0 | 100.0% | +46.0% |
| 2026-10-29T12:08:22.532184+00:00 | 1 | 1-0 | 100.0% | +34.0% |
| 2026-10-30T12:03:48.308948+00:00 | 1 | 0-0 | 0.0% | +0.0% |
| 2026-10-31T12:03:11.165007+00:00 | 5 | 4-0 | 80.0% | +22.6% |
| 2026-11-01T07:37:30.159727+00:00 | 3 | 1-2 | 33.3% | -58.7% |
| 2026-11-03T13:23:43.479885+00:00 | 1 | 0-1 | 0.0% | -100.0% |
| 2026-11-03T13:58:02.173298+00:00 | 2 | 2-0 | 100.0% | +48.0% |
| 2026-11-04T09:31:03.622249+00:00 | 1 | 1-0 | 100.0% | +107.0% |
| 2026-11-04T10:20:33.895771+00:00 | 1 | 0-1 | 0.0% | -100.0% |
| 2026-11-05T13:37:38.336530+00:00 | 58 | 43-15 | 74.1% | +14.6% |
| 2026-11-05T16:50:22.659919+00:00 | 20 | 14-6 | 70.0% | -8.2% |
| 2026-11-06T12:17:20.125743+00:00 | 2 | 2-0 | 100.0% | +18.0% |
| 2026-11-06T13:40:19.404227+00:00 | 30 | 20-10 | 66.7% | -10.0% |
| 2026-11-07T11:48:25.259368+00:00 | 15 | 11-4 | 73.3% | -1.8% |
| 2026-11-07T13:54:13.645217+00:00 | 84 | 63-21 | 75.0% | +1.7% |
| 2026-11-08T09:01:04.075316+00:00 | 9 | 7-2 | 77.8% | +13.6% |
| 2026-11-08T12:20:11.356382+00:00 | 84 | 64-20 | 76.2% | +5.5% |
| 2026-11-20T14:29:07.564363+00:00 | 1 | 0-1 | 0.0% | -100.0% |
| 2026-11-20T16:53:14.319920+00:00 | 13 | 8-5 | 61.5% | -19.4% |
| 2026-11-21T10:01:28.692132+00:00 | 13 | 7-6 | 53.8% | -11.8% |
| 2026-11-21T14:06:56.472831+00:00 | 23 | 14-8 | 60.9% | +8.5% |
| 2026-11-21T16:19:45.112160+00:00 | 26 | 16-9 | 61.5% | +12.4% |
| 2026-11-22T12:26:43.290856+00:00 | 17 | 11-6 | 64.7% | +7.1% |
| 2026-11-22T13:50:47.131378+00:00 | 20 | 11-9 | 55.0% | -3.4% |
| 2026-11-23T06:15:00.240474+00:00 | 2 | 2-0 | 100.0% | +64.7% |
| 2026-11-23T18:16:57.482339+00:00 | 4 | 2-2 | 50.0% | -28.8% |
| 2026-11-24T08:10:20.197784+00:00 | 3 | 2-1 | 66.7% | -15.3% |
| 2026-11-24T16:35:48.587606+00:00 | 15 | 12-3 | 80.0% | +7.5% |
| 2026-11-25T14:22:45.129589+00:00 | 0 | 0-0 | — | — |

## STRICT versus PROVISIONAL

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| PROVISIONAL | 29 | 20-9 | 69.0% | -9.0% |
| STRICT | 498 | 353-140 | 70.9% | +3.6% |

## By policy

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 48h-ah-price-edge-cagey-v28 | 444 | 312-130 | 70.3% | +2.9% |
| 48h-top-ten-probability-ev-no-under35-v14 | 9 | 7-2 | 77.8% | +3.6% |
| 48h-top-twelve-probability-ev-no-under35-v15 | 12 | 8-4 | 66.7% | -11.4% |
| 48h-top-twelve-profitable-win-probability-v23 | 1 | 1-0 | 100.0% | +15.0% |
| 48h-two-per-market-group-probability-ev-corners-cards-v25 | 16 | 12-4 | 75.0% | +2.6% |
| 48h-two-per-market-group-probability-ev-v24 | 4 | 2-2 | 50.0% | -9.5% |
| 48h-zero-tolerance-ev05-no-loss75-corners-v26 | 12 | 7-2 | 58.3% | +1.4% |
| 48h-zero-tolerance-ev1-common-no-loss75-v22 | 8 | 8-0 | 100.0% | +31.7% |
| 72h-all-markets-ev15-one-book-v6 | 1 | 1-0 | 100.0% | +45.0% |
| 72h-all-markets-net-ev15-execution-v7 | 5 | 5-0 | 100.0% | +37.0% |
| 72h-seven-markets-fresh-references-net-ev15-v11 | 5 | 4-1 | 80.0% | +7.2% |
| 72h-ucl-v2 | 1 | 1-0 | 100.0% | +28.0% |
| 72h-ucl-v3 | 7 | 3-4 | 42.9% | -38.7% |
| legacy/unspecified | 2 | 2-0 | 100.0% | +32.0% |

## By market

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Asian Handicap Away +0.00 | 3 | 3-0 | 100.0% | +92.3% |
| Asian Handicap Away +0.25 | 18 | 12-6 | 66.7% | -0.9% |
| Asian Handicap Away +0.50 | 4 | 3-1 | 75.0% | +44.5% |
| Asian Handicap Away +0.75 | 2 | 1-1 | 50.0% | -8.0% |
| Asian Handicap Away +1.00 | 6 | 2-4 | 33.3% | -51.3% |
| Asian Handicap Away +1.25 | 28 | 21-7 | 75.0% | +3.2% |
| Asian Handicap Away +1.50 | 5 | 3-2 | 60.0% | -9.8% |
| Asian Handicap Away +1.75 | 1 | 0-1 | 0.0% | -100.0% |
| Asian Handicap Away +2.00 | 7 | 4-1 | 57.1% | +7.0% |
| Asian Handicap Away +2.25 | 17 | 15-2 | 88.2% | +30.8% |
| Asian Handicap Away +2.50 | 3 | 2-1 | 66.7% | +2.7% |
| Asian Handicap Away +2.75 | 1 | 1-0 | 100.0% | +97.0% |
| Asian Handicap Away +3.00 | 0 | 0-0 | — | — |
| Asian Handicap Away +3.25 | 1 | 0-1 | 0.0% | -100.0% |
| Asian Handicap Away -0.25 | 0 | 0-0 | — | — |
| Asian Handicap Away -0.50 | 0 | 0-0 | — | — |
| Asian Handicap Away -0.75 | 4 | 4-0 | 100.0% | +64.0% |
| Asian Handicap Away -1.00 | 2 | 0-2 | 0.0% | -100.0% |
| Asian Handicap Away -1.25 | 0 | 0-0 | — | — |
| Asian Handicap Away -1.50 | 0 | 0-0 | — | — |
| Asian Handicap Away -1.75 | 1 | 1-0 | 100.0% | +84.0% |
| Asian Handicap Away -2.00 | 0 | 0-0 | — | — |
| Asian Handicap Away -2.25 | 0 | 0-0 | — | — |
| Asian Handicap Away -2.50 | 0 | 0-0 | — | — |
| Asian Handicap Away -2.75 | 0 | 0-0 | — | — |
| Asian Handicap Away -3.00 | 0 | 0-0 | — | — |
| Asian Handicap Home +0.00 | 6 | 5-1 | 83.3% | +37.0% |
| Asian Handicap Home +0.25 | 14 | 13-1 | 92.9% | +28.5% |
| Asian Handicap Home +0.50 | 7 | 6-1 | 85.7% | +22.3% |
| Asian Handicap Home +0.75 | 2 | 2-0 | 100.0% | +55.0% |
| Asian Handicap Home +1.00 | 8 | 5-2 | 62.5% | +6.9% |
| Asian Handicap Home +1.25 | 18 | 14-4 | 77.8% | +4.4% |
| Asian Handicap Home +1.50 | 4 | 1-3 | 25.0% | -63.2% |
| Asian Handicap Home +1.75 | 0 | 0-0 | — | — |
| Asian Handicap Home +2.00 | 5 | 3-1 | 60.0% | -0.8% |
| Asian Handicap Home +2.25 | 4 | 3-1 | 75.0% | +16.5% |
| Asian Handicap Home +2.50 | 3 | 2-1 | 66.7% | -20.3% |
| Asian Handicap Home +2.75 | 0 | 0-0 | — | — |
| Asian Handicap Home +3.00 | 0 | 0-0 | — | — |
| Asian Handicap Home +3.25 | 0 | 0-0 | — | — |
| Asian Handicap Home -0.25 | 2 | 0-2 | 0.0% | -75.0% |
| Asian Handicap Home -0.50 | 7 | 5-2 | 71.4% | +42.6% |
| Asian Handicap Home -0.75 | 4 | 1-3 | 25.0% | -71.0% |
| Asian Handicap Home -1.00 | 1 | 0-0 | 0.0% | +0.0% |
| Asian Handicap Home -1.25 | 0 | 0-0 | — | — |
| Asian Handicap Home -1.50 | 3 | 2-1 | 66.7% | +20.7% |
| Asian Handicap Home -1.75 | 1 | 0-1 | 0.0% | -100.0% |
| Asian Handicap Home -2.00 | 2 | 0-2 | 0.0% | -100.0% |
| Asian Handicap Home -2.25 | 0 | 0-0 | — | — |
| Asian Handicap Home -2.50 | 0 | 0-0 | — | — |
| Asian Handicap Home -2.75 | 0 | 0-0 | — | — |
| Asian Handicap Home -3.00 | 0 | 0-0 | — | — |
| Away win | 47 | 33-14 | 70.2% | +22.1% |
| Both Teams to Score - Yes | 3 | 2-1 | 66.7% | +0.7% |
| Corners Over 10.5 | 0 | 0-0 | — | — |
| Corners Over 11.5 | 0 | 0-0 | — | — |
| Corners Over 12.5 | 0 | 0-0 | — | — |
| Corners Over 7.5 | 0 | 0-0 | — | — |
| Corners Over 8.5 | 0 | 0-0 | — | — |
| Corners Over 9.5 | 0 | 0-0 | — | — |
| Corners Under 10.5 | 2 | 2-0 | 100.0% | +51.0% |
| Corners Under 11.5 | 0 | 0-0 | — | — |
| Corners Under 12.5 | 0 | 0-0 | — | — |
| Corners Under 7.5 | 0 | 0-0 | — | — |
| Corners Under 8.5 | 0 | 0-0 | — | — |
| Corners Under 9.5 | 0 | 0-0 | — | — |
| Double Chance 12 | 66 | 52-14 | 78.8% | +0.3% |
| Double Chance 1X | 32 | 26-6 | 81.2% | +0.5% |
| Double Chance X2 | 19 | 14-5 | 73.7% | +3.2% |
| Draw | 0 | 0-0 | — | — |
| Home win | 86 | 53-33 | 61.6% | -1.5% |
| Over 1.5 | 73 | 55-18 | 75.3% | -6.9% |
| Under 3.5 | 5 | 2-3 | 40.0% | -46.0% |

## By league

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| Bundesliga | 51 | 40-10 | 78.4% | +14.0% |
| Eredivisie | 45 | 25-20 | 55.6% | -19.0% |
| La Liga | 68 | 47-20 | 69.1% | -1.1% |
| Ligue 1 | 48 | 34-14 | 70.8% | +3.1% |
| Premier League | 69 | 46-22 | 66.7% | +2.1% |
| Primeira Liga | 25 | 20-5 | 80.0% | +17.5% |
| Serie A | 67 | 45-20 | 67.2% | -1.1% |
| Super Lig | 50 | 39-11 | 78.0% | +19.7% |
| UEFA Champions League | 37 | 29-8 | 78.4% | +7.6% |
| UEFA Europa League | 67 | 48-19 | 71.6% | -2.4% |

## Gameweeks

| Group | Graded | W-L | Win rate | Simulated ROI |
|---|---:|---:|---:|---:|
| 2026-W41 | 5 | 2-3 | 40.0% | -49.6% |
| 2026-W42 | 24 | 21-3 | 87.5% | +19.5% |
| 2026-W43 | 41 | 30-11 | 73.2% | +0.5% |
| 2026-W44 | 13 | 8-2 | 61.5% | +2.6% |
| 2026-W45 | 307 | 227-80 | 73.9% | +3.7% |
| 2026-W47 | 113 | 67-44 | 59.3% | +0.6% |
| 2026-W48 | 24 | 18-6 | 75.0% | +3.4% |

## Gameweeks: closing-line value first, per pick and per fixture

| List | View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 2026-W41 | per pick | 0 | — | — | — | 5 | -49.6% | -110.1% to +10.9% |
| 2026-W41 | per fixture (a match's picks averaged) | 0 | — | — | — | 5 | -49.6% | -110.1% to +10.9% |
| 2026-W42 | per pick | 14 | -1.4% | -2.9% to +0.1% | 36% | 24 | +19.5% | -0.2% to +39.1% |
| 2026-W42 | per fixture (a match's picks averaged) | 14 | -1.4% | -2.9% to +0.1% | 36% | 24 | +19.5% | -0.2% to +39.1% |
| 2026-W43 | per pick | 30 | -3.1% | -6.0% to -0.3% | 23% | 41 | +0.5% | -20.4% to +21.3% |
| 2026-W43 | per fixture (a match's picks averaged) | 30 | -3.1% | -6.0% to -0.3% | 23% | 41 | +0.5% | -20.4% to +21.3% |
| 2026-W44 | per pick | 12 | -0.1% | -2.7% to +2.5% | 42% | 13 | +2.6% | -23.3% to +28.5% |
| 2026-W44 | per fixture (a match's picks averaged) | 12 | -0.1% | -2.7% to +2.5% | 42% | 13 | +2.6% | -23.3% to +28.5% |
| 2026-W45 | per pick | 49 | -1.6% | -2.9% to -0.3% | 27% | 307 | +3.7% | -3.8% to +11.1% |
| 2026-W45 | per fixture (a match's picks averaged) | 19 | -0.2% | -2.2% to +1.7% | 37% | 96 | +2.8% | -5.3% to +10.9% |
| 2026-W47 | per pick | 67 | -2.2% | -3.3% to -1.1% | 28% | 113 | +0.6% | -13.8% to +15.0% |
| 2026-W47 | per fixture (a match's picks averaged) | 34 | -2.6% | -4.1% to -1.1% | 21% | 62 | +5.7% | -10.4% to +21.7% |
| 2026-W48 | per pick | 24 | -1.7% | -3.7% to +0.3% | 38% | 24 | +3.4% | -24.3% to +31.0% |
| 2026-W48 | per fixture (a match's picks averaged) | 13 | -1.5% | -3.7% to +0.6% | 23% | 13 | +1.2% | -28.4% to +30.9% |

## Confidence calibration of shortlisted markets

| Forecast bin | Samples | Average forecast | Observed event rate (frozen probability basis) | Binary Brier |
|---|---:|---:|---:|---:|
| 0%–50% | 75 | 42.0% | 52.0% | 0.2575 |
| 50%–60% | 59 | 54.8% | 69.5% | 0.2316 |
| 60%–70% | 79 | 65.2% | 69.6% | 0.2126 |
| 70%–80% | 181 | 75.6% | 71.8% | 0.2018 |
| 80%–90% | 108 | 83.5% | 79.6% | 0.1619 |
| 90%–100% | 25 | 93.6% | 100.0% | 0.0045 |

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
| Bundesliga | 2026-11-22 | 1622 | 3 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| EPL | 2026-11-23 | 2010 | 2 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Eredivisie | 2026-11-22 | 1647 | 3 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| LaLiga | 2026-11-23 | 2029 | 2 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Ligue1 | 2026-11-22 | 1779 | 3 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| PrimeiraLiga | 2026-11-08 | 1628 | 17 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| SerieA | 2026-11-23 | 2020 | 2 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| SuperLig | 2026-11-23 | 1858 | 2 | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| UCL | 2026-11-24 | 584 | 1 | CURRENT_WITHIN_PROVIDER_SCHEDULE |
| UEL | 2026-11-05 | 732 | 20 | VERIFIED_WITHIN_24_HOURS |

Latest shortlist audit: {"selected_quotes": 13, "exchange_quotes": 0, "missing_quote_age": 13, "quote_age_over_24h": 0, "costs_recorded": 13, "bookmakers": {"Pinnacle": 13}, "account_availability": "NOT_VERIFIED_WITH_BOOKMAKER_ACCOUNTS", "past_kickoff_count": 0, "upcoming_kickoff_count": 13, "unknown_kickoff_count": 0}.

Source refresh does not retrain stored forecasts. Days since the last match do not by themselves establish missing data.

No forward model trials are generated or captured. The retired trials, their code and their reports were removed on 25 Nov 2026; they are in git history.

Dependency versions at review: {"python": "3.14.10", "numpy": "2.5.5", "pandas": "3.1.1", "scipy": "1.18.1", "requests": "2.34.2", "rapidfuzz": "3.14.6", "python-dotenv": "1.2.4", "coverage": "7.17.5", "PyYAML": "6.0.4"}. Forecast-generation versions are recorded in new frozen snapshot health; legacy generation environments are unknown.

Closing odds: [report](closing_odds/report.md). Latest-selection comparison aligned with headline ROI, with a separate first-entry reference; official close and accepted execution are unverified.

Daily observations: [health_history.json](health_history.json). Frozen forecast health: [pipeline_health.json](pipeline_health.json).

Policy and gameweek results above show sample counts, ROI and calibration. Compare experiments on paired settled forecasts; small samples and changing cohorts cannot establish improvement. Historical missing experimental data is not backfilled.
