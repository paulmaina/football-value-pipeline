# Asian handicap backtest: production model vs Pinnacle close

`ah_close_backtest.py` is a read-only, walk-forward historical evaluation of the
production model's full-time Asian handicap probabilities against Pinnacle's
closing main line. It changes no production model, policy, threshold or
workflow and is not wired into any scheduled job. Nothing in its output is a
promotion or a recommendation to change production.

```powershell
py ah_close_backtest.py            # all 8 divisions, 2000 bootstrap draws
py ah_close_backtest.py --divisions E0 --workers 1 --bootstrap 300   # quick check
```

Outputs go to `football_output_v2/performance/ah_close_backtest/`:
`report.md` (tables and verdict), `summary.json` (every metric) and
`per_match.csv` (one row per scored match, including the refit date and the
last training date so the lookahead rule can be audited).

## Data

- football-data.co.uk CSVs already in `.football_cache`: E0, SP1, D1, I1, F1,
  N1, P1, T1, seasons 2122 to 2526. No downloads.
- A match is scored only when it has Pinnacle opening (`AHh`, `PAHH`, `PAHA`)
  and closing (`AHCh`, `PCAHH`, `PCAHA`) Asian handicap prices plus Pinnacle
  opening 1X2 (`PSH`, `PSD`, `PSA`). The 2526 CSVs carry Pinnacle AH on only
  about half the rows; coverage per league/season is in `summary.json`.
- Training uses every completed match, with or without odds.
- 2122 is warm-up only: it trains but is never scored.
- UCL/UEL are excluded because there are no historical odds.
- `AHh`/`AHCh` are the **home** handicap (negative = home gives goals). The run
  prints, and fails on, three known matches: Man City 5-1 Luton (AHCh -2.75),
  Sheffield United 1-2 Man City (+1.75) and Almeria 1-3 Real Madrid (+1.25).

## Model variants

All variants share one fit per league per week and use the production
prediction path (`FootballValuePipelineV2._predict_row`).

| variant | what it is |
|---|---|
| `dc` | Dixon-Coles, half-life 480 days, L2 0.08, plus the gated CSV shot features (HST/AST/HS/AS). No odds inputs. |
| `blend70` | `dc` with H/D/A reweighted to 0.70 x Pinnacle opening 1X2 (power de-vig), as production blends. |
| `prod` | `blend70` plus the Pinnacle opening O/U 2.5 totals anchor. Its model-version tag matches the production identity. |

BBS and API-Football statistics cannot be rebuilt from the CSVs and are off.
Production trains on up to six seasons; here the training window grows from
one season (2122) at the first scored week.

**No lookahead.** Refits happen every Tuesday, using matches dated strictly
before the refit date, and predict that week's matches (Tuesday to Monday).
`walk_forward` asserts that the last training date precedes the refit and every
predicted match, and `main` re-checks this for the whole of `per_match.csv`.
Closing prices are evaluation targets only. As in production, fixtures with a
team the model has not yet seen (newly promoted sides) are skipped.

## Asian handicap probabilities

The model's full score grid gives a home-minus-away goal-margin distribution.
For the closing line it gives home full win, half win, push, half loss and full
loss. Quarter lines stake half on each adjacent line. The comparable single
probability is the effective `q = W / (W + L)`, where `W` and `L` are the
expected won and lost fractions of stake. 1/q is then the zero-EV price, and q
equals P(home covers) on half lines.

Pinnacle fair probabilities come from proportional margin removal on
`PCAHH`/`PCAHA` (closing) and `PAHH`/`PAHA` (opening). Shin removal is reported
alongside as a check.

## Metrics

- **Primary**: half closing lines only (no push). Binary "home covers" log loss
  and Brier, model vs Pinnacle fair close. Gain = Pinnacle log loss minus model
  log loss (positive = model better). The 95% interval comes from a paired
  bootstrap that resamples whole gameweeks (refit weeks, pooled across leagues).
- **Secondary**: all lines. With R as the settled home return per unit at
  Pinnacle's fair closing odds and E as the model's expected return at those
  odds: skill = mean(R^2) - mean((R - E)^2). Pinnacle predicts zero at its
  own fair price, so positive skill means the model explains settled returns
  better. Also reports the return from 1 unit on whichever side the model
  prefers at fair close.
- **Breakdowns** (primary metric): league, season, closing line bucket,
  home/away favourite, and model-minus-Pinnacle gap. The requested buckets left
  -1.25/+1.25 uncovered, so they fall into `<= -1.25` and `>= +1.25`.
- **Simulated CLV**: bet the side where model EV at the Pinnacle opening price
  and line is at least 2%. CLV = opening odds x Pinnacle fair closing probability
  - 1, computed only where the opening and closing lines match. For moved lines
  the report gives the share that moved in the bet's favour. ROI settles at
  opening odds on the opening line. This is **simulated**: it assumes every
  opening price could have been bet at Pinnacle limits, which is not
  achievable execution.

The verdict lists every breakdown cell whose interval excludes zero in the
model's favour, with the number expected by chance across that many cells.

## Results (run 2026-11-02)

9,465 matches scored, 2,323 of them on half closing lines. Full tables are in
`report.md`.

| variant | half-line LL gain vs close [95%] | all-line return skill [95%] | simulated CLV, same line [95%] |
|---|---|---|---|
| `dc` | -0.0188 [-0.0264, -0.0112] | -0.0401 [-0.0468, -0.0334] | -2.50% [-2.64, -2.34] |
| `blend70` | -0.0059 [-0.0099, -0.0017] | -0.0142 [-0.0181, -0.0103] | -2.48% [-2.67, -2.27] |
| `prod` | -0.0048 [-0.0086, -0.0011] | -0.0119 [-0.0155, -0.0084] | -2.47% [-2.68, -2.25] |

**Verdict: the model does not beat Pinnacle's closing Asian handicap anywhere
we can detect.** All three variants are worse than the close on both the
primary and secondary metrics, and every interval excludes zero. None of the 66
breakdown cells has an interval that excludes zero in the model's favour. The
few point estimates above zero (`prod` D1 and N1, `dc`/`blend70` D1) are all
within noise. The model's errors against the close grow with its disagreement:
the `>= 10pp` gap bucket is the worst for every variant, so large model-vs-close
gaps are mostly model error, not edge. Simulated CLV is about -2.5% for every
variant, and only about 30% of same-line bets beat the close. Blending Pinnacle
opening 1X2 removes most of the pure model's deficit but none of the gap to the
close. Pinnacle's own close beats its open (LL 0.6923 vs 0.6930) on unchanged
half lines, as expected.

On +/-0.5 lines `blend70` and `prod` give identical results. Those lines settle
on the plain home-win probability, which the totals anchor preserves exactly.
