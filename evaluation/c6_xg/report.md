# C6X: C6 plus rolling pre-kickoff xG (docs/plan.md, Phase 2i)

**Not put forward for declaration.** On development, C6X beats C6 on AH all lines by +0.00194 log loss, but the 95% interval includes zero (−0.00039 to +0.00456), so condition (a) of the choice rule fails. Validation is level (+0.00015). Calibration v3 against C6 passes in both periods. Nothing live changes, and the API-Football collector is untouched.

Specification, periods and choice rule were committed before any C6X figure was computed (53c1b60e8, pushed 23 Nov 2026 12:05 +03:00). Development was computed and written first, then validation once (`development.json`, `validation.json`, `choice_rule.json`; `scripts/c6_xg_report.py`).

## Input

- xG: `expected_goals` from the cached API-Football `/fixtures/statistics` responses, extracted offline with no API request (`scripts/extract_api_football_xg.py`; coverage in `extraction_summary.json`). Snapshot of 23 Nov 2026 12:00 UTC: 2,536 five-league matches with xG, 28 Jan 2024 to 25 May 2025 (EPL 552, LaLiga 547, Bundesliga 443, Serie A 548, Ligue 1 446), plus 134 UCL matches, which C6X does not use. Table sha256 `8c7536b5…`.
- Mapping: every five-league fixture with cached xG maps to exactly one football-data row with the same date, teams and score, except Union Berlin v Bochum (14 Dec 2024). That match was awarded to Bochum after it was played, so the provider's score (the one played) differs from the official one. Teams were resolved per league by the live integration's name check (96 domestic, 37 UCL), then `team_research.history_team` (15 domestic, 6 UCL), then reviewed pairs (7 domestic, 9 UCL).
- Left out: 11 domestic play-off fixtures (relegation rounds and the Serie A decider), and for UCL 230 qualifiers, 38 play-offs and 3 AET/PEN. 81 UCL fixtures on or after 21 Jan 2025 (European holdout) were counted, never parsed.
- Periods: run-in 28 Jan – 30 Jun 2024 (not scored), development 1 Jul – 31 Dec 2024, validation 1 Jan – 30 Jun 2025. These are shorter than first planned because the cache has no xG before 28 Jan 2024; Paul chose to run now rather than wait for the collector to fill August 2023 onwards. Run end 1 Jul 2025. All three periods sit inside the harness's development period. Scored: the five leagues only.

## Results

C6 minus C6X log loss (positive = C6X better), with whole weeks resampled and 95% intervals:

| Period | Fixtures (weeks) | AH all lines (primary) | AH draw-sensitive | 1X2 | Over 1.5 |
|---|---|---|---|---|---|
| Development | 809 (18) | +0.00194 (−0.00039 to +0.00456) | +0.00182 (−0.00087 to +0.00486) | +0.00211 (−0.00103 to +0.00566) | −0.00055 (−0.00353 to +0.00274) |
| Validation | 934 (20) | +0.00015 (−0.00265 to +0.00310) | +0.00002 (−0.00376 to +0.00384) | +0.00011 (−0.00434 to +0.00459) | −0.00090 (−0.00365 to +0.00175) |

Mean AH all log loss: development C 0.71990, C6 0.71896, C6X 0.71703, M 0.70186; validation C 0.72138, C6 0.72119, C6X 0.72104, M 0.70864. The market (M) remains far ahead: on AH all lines, M minus C6X is −0.01664 on development and −0.01548 on validation, both clear (C6's gap is −0.01830 and −0.01549).

| Choice rule | Result |
|---|---|
| (a) Development AH all positive, interval clear of zero | **No**: +0.00194, interval includes zero |
| (b) Validation AH all not negative | Yes: +0.00015 |
| (c) Calibration v3 against C6 on development | Yes |
| Put forward for declaration | **No** |

Calibration (home / away slopes, five leagues): development C6X 1.012 / 0.953, C6 0.994 / 0.924; validation C6X 1.049 / 1.000, C6 1.013 / 1.004. All four slopes are inside 0.90–1.10 and no band fails (17 checked; the worst on development is away 0.6–0.7, 33 matches, z 1.15; on validation away 0.2–0.3, 208 matches, z 2.54, under the 2.97 bar).

C6X moves C6's 1X2 by up to 2.2 points per fixture on average on development (90th percentile 4.5, max 9.6), and 2.8 on validation (90th percentile 5.6, max 11.7).

Where either side had fewer than 3 xG matches (31 development fixtures), AH all is +0.01024 (−0.00098 to +0.01653), not clear. Every validation fixture had both sides on at least 3.

## Fitted xG effects

F = (X_for, X_against) per side, in goals per match; X = w·(xG − goals) over the side's last 8 xG matches, w = k/(k+4). Across the scored fixtures the standard deviation of X_for is 0.25 and of X_against 0.22 (development). α is the effect of a side's own X on its own scoring, γ that of the opponent's X. Prior sd 0.20; standard errors are from the penalised fit.

| Fit (origin, rows) | α xG for | α xG against | γ xG for | γ xG against |
|---|---|---|---|---|
| First development, 29 Jul 2024, 630 | −0.014 (0.085) | +0.037 (0.092) | +0.155 (0.091) | +0.148 (0.089) |
| Development median (12 windows) | +0.004 | −0.013 | +0.037 | +0.196 |
| Last development, 30 Dec 2024, 1,403 | +0.017 (0.059) | −0.032 (0.066) | +0.018 (0.062) | +0.261 (0.064) |
| Validation median (10 windows) | +0.081 | −0.034 | +0.057 | +0.219 |
| Last validation, 19 May 2025, 2,309 | +0.112 (0.049) | −0.029 (0.051) | +0.038 (0.051) | +0.194 (0.049) |

The one stable effect is γ xG against, at about +0.2 (about four standard errors from zero once there are 1,400 or more rows). When the opponent has conceded fewer goals than its xG against, the side is expected to score more: defensive luck regresses. Each tenth of a goal per match of that gap adds about 2% to the side's goal rate. The attacking counterpart, α xG for, is near zero through development and only rises to about +0.11 (2.3 standard errors) by May 2025. The two terms that should be near zero (α against, γ for) stay near zero.

## Leakage checks

| Check | Result |
|---|---|
| xG rows on or after the run end (1 Jul 2025) | 0 |
| Feature matches on or after their match day | 0 |
| Research rows on or after the run end | 0 |
| UCL rows read by C6X | 0 |
| Odds or market inputs read by C6X | 0 (`research_xg.py` reads no price, market fit or published grid; test `test_no_odds_or_market_input`) |
| C6X with zero features equals C6 | Yes (`test_zero_features_give_c6_exactly`) |
| A fit reads only rows before its origin | Checked in `walk_forward`; result changes after an origin move no fit (`test_walk_forward_fits_only_on_rows_before_each_origin`) |
| Placebo (xG pairs shuffled within each league-season, seed 2611) | No gain: development C6 minus placebo AH all −0.00472 (−0.00841 to −0.00146), so noise features cost accuracy; validation −0.00013 (−0.00207 to +0.00180). The real xG beats the placebo in both periods. |

No holdout match, no harness-validation match and no match after 10 Oct 2026 was forecast, fitted or read. `evaluation_harness.py`, its config and `SETUP_FILES` are unchanged.

## Reading

xG carries some information beyond C's goal rates: the defensive regression term is consistently fitted, the real features beat a shuffled placebo, and C6X is ahead of C6 on every 1X2-based metric on development. The gain is small, though: about 0.002 on 809 fixtures, not distinguishable from zero, and it vanishes on validation. With only 16 months of xG (the free plan's last season is 2024/25, and the cache starts at 28 Jan 2024), a gain of this size cannot be shown either way. A longer run-in would also give steadier early fits, which is where the placebo shows the cost of noise.

**Limits**: even if a later version passed, C6X cannot reach the holdout or go live without a current-season xG source (a paid API-Football plan, or Understat for the big five if it returns). The domestic holdout leagues have no cached xG. Any declaration queues behind 2g-4 (C8 plus the walk-forward slope).
