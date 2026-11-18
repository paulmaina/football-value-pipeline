# Corner-total candidate K1 and its inputs (offline, 18 Nov 2026)

Question (Paul, 18 Nov 2026): is a corners model worth bringing back into the shortlists? Offline research only;
nothing live reads `research_corners.py`. Full tables: `evaluation/corners_candidate/report.md` and `results.json`
(`python scripts/corners_candidate_report.py --output evaluation/corners_candidate --work <scratch>`).

## Data

- Corner counts (football-data HC, AC) are near-complete for all eight domestic leagues from 2015/16
  (Eredivisie, Primeira Liga and Süper Lig from 2017/18) to date. Süper Lig 2022/23 misses 29 of 342.
- Corner prices: none in development or validation. The only stored corner prices are Pinnacle's for 82 big-five
  fixtures kicking off 25 Oct - 2 Nov 2026 (decision logs of the v25/v26 runs), after 10 Oct 2026; Paul ruled
  them out (too few, and matches after 10 Oct stay unread). **Returns cannot be tested.**
- Every input is read only up to 15 Jan 2026 (the end of validation), cut as each file is parsed.

## Models

| Name | What |
|---|---|
| B0 | League average: NB total with the time-weighted league mean (half-life 365 days), refitted daily |
| NB2 | `count-markets-nb2-v1` (count_markets.walk_forward, unchanged) |
| K1 | Team corner rates: Poisson home and away corner counts with team attack/defence terms, a home term and ridge shrinkage to the league mean; time-weighted (half-life chosen on development: 240 days, prior 12 matches); NB total; refitted every match day on earlier days only |
| K1r | K1 through the second stage below with an intercept only (the base each input is tested against) |

Inputs were tested one at a time on top of K1 through a pooled walk-forward NB second stage
(log mu = log mu_K1 + b0 + b.x, refitted every 28 days on earlier matches from Aug 2020), against K1r on the same
fixtures. Keep rule (fixed before scoring): development improvement with the 95% week-resampled interval below
zero, and no worse on validation.

## Results (mean Over log loss, lines 8.5-11.5; first minus second)

| | Development (8,198) | Validation (1,368) |
|---|---|---|
| K1 − B0 | −0.0072 [−0.0104, −0.0040] | +0.0019 [−0.0054, +0.0088] |
| K1 − NB2 | −0.0019 [−0.0039, +0.0001] | +0.0022 [−0.0036, +0.0077] |
| NB2 − B0 | −0.0053 [−0.0076, −0.0032] | −0.0003 [−0.0047, +0.0045] |

- Calibration: every model is overconfident, more so on validation (P(Over) slopes 0.4-0.6 at 9.5-11.5 for K1 and
  NB2; the forecasts spread little, so the slopes are noisy).
- Inputs (odds-free): shots, shots on target, Dixon-Coles expected goals (total, per side), match balance (xGD),
  Elo difference and league add nothing (all within ±0.0003 on development). K1's home term earns its place
  (development −0.0011 [−0.0017, −0.0004], validation −0.0001).
- Market-informed (Pinnacle pre-match 1X2 and O/U 2.5): nothing either (about 0.0000 on development).

## Recommendation

Not worth declaring for a holdout test. Corner skill beyond the league average is visible on development only;
on validation neither K1 nor NB2 beats the league average, and both are too sharp. K1 does not clearly beat NB2,
so the shadow corner list (Paul, 18 Nov 2026) uses NB2. Real evidence can only come from prices: the shadow
list collects Pinnacle corner closes and grades closing-line value, which no historical data allows.
