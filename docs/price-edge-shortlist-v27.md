# Production shortlist v27: Asian handicap price edge vs Pinnacle

Policy `48h-ah-price-edge-pinnacle-ref-v27` (`price_edge_shortlist.py`) replaced
v26 as production on 2 November 2026. v26 and every older policy stay
replayable: each capture replays under its own recorded version.

Background: [price-edge backtest](price-edge-backtest.md) (+2.46% CLV, upper
bound) and the [market-implied calibration check](market-implied-calibration.md).

## What it bets

Candidates are every Asian handicap line, main and alternate, on both sides, at
the allowed bookmakers: Pinnacle and 1xBet. Pinnacle is the reference, so in
practice picks come from 1xBet. Markets that settle exactly like an AH line are
quotes for that line too:

| Market | Same as |
|---|---|
| 1X2 home / away | home -0.5 / away -0.5 |
| Double chance 1X / X2 | home +0.5 / away +0.5 |
| Draw no bet (home / away) | AH 0 (same side) |

The draw and double chance 12 are never picks.

## Fair reference (first available)

1. **a:** Pinnacle on the same AH line, two-way margin removed proportionally. The
   Shin estimate is recorded alongside.
2. **b:** Pinnacle's equivalent market, margin removed: 1X2 for the ±0.5 lines,
   draw no bet for 0.
3. **c (derived):** the market-implied matrix (fit B: Pinnacle 1X2, O/U 2.5 and main
   AH). It is used only for plus lines (the side receiving goals) and only when the
   fit is usable.

Otherwise the candidate is rejected with `no Pinnacle reference` (fail closed).
Minus lines never use c, because the calibration check shows the matrix
overstates minus-line edges.

## Rule

Edge = offered odds × fair win-share − 1. The win-share excludes refunds, as in the backtest.

- **Qualify:** edge ≥ 2% against reference a or b, and ≥ 3% against reference c.
- **Minimum odds still worth taking:** fair × 1.02, or fair × 1.03 for a derived reference.
- **Guards:** each failure is logged as a rejection reason.
  - Kickoff more than 48 h or less than 20 min away.
  - Either quote stale (24 h freshness window).
  - Offered and Pinnacle quotes more than 10 minutes apart.
  - Pinnacle overround outside [1.00, 1.10].
  - Offered price above 1.15 × fair odds.
  - Offered odds above 3.00.
- **Selection:** one row per fixture, with no cap. The pick is the qualifying
  candidate with the highest Pinnacle no-loss probability, then the higher
  edge, then the higher odds. Other qualifying lines go in `other_value_lines`.
  The shortlist is sorted safest first.
- **Not used:** no model EV requirement and no 75% no-loss floor. The
  production model's gap to Pinnacle is recorded for information only.

The Pinnacle no-loss probability comes from the fit-B matrix (win, half-win or
refund). When the fit is unusable, it is the win-share on half lines and blank
on other lines.

## Narrow-margin tags (tracking only)

These tags never change a decision:

- `balanced`: Pinnacle 1X2 home and away odds both in [2.00, 3.50].
- `low_total`: Pinnacle margin-free P(over 2.5) < 0.45.
- `high_draw`: Pinnacle margin-free draw probability ≥ 0.27.
- `even_odds` (added in PR D): Pinnacle 1X2 home and away raw odds both ≥ 2.50.

For a fixture with any tag, AH +1, +1.5, +1.75, +2 and +2.25 are always
evaluated on both sides. A line nobody quotes is logged as `no offered quote
at an allowed bookmaker`, with its fair price, so the hypothesis can be
measured forward even when no pick is made.

## Outputs

- **Readable shortlist** (`conservative_bet_shortlist_readable.csv`):
  - kickoff, match and tags;
  - Pinnacle draw probability and P(over 2.5);
  - AH line, side (favourite or underdog), market to bet, bookmaker and price;
  - fair odds, reference type, edge and minimum odds;
  - Pinnacle no-loss probability and quote ages;
  - model-vs-Pinnacle gap (information only).
- **Decisions:** every candidate is in `conservative_bet_rejections.csv` with its
  reasons. The summary carries rejection counts by reason and tagged-candidate counts.

## Data capture

Each prediction row now carries `price_edge_quotes`: per-book Pinnacle and
1xBet 1X2 and O/U 2.5 from the main request, and double chance and
alternate O/U 2.5 from the per-event request. No extra request is made. Runs
captured before this column existed fall back to fields that are Pinnacle by
construction. Those runs have no 1xBet 1X2 or double-chance prices, because the
old allowlist did not include 1xBet for those markets.

## Tracking

`price_edge_tracking.py` runs in every review (`performance_tracking.py review`)
and writes `football_output_v2/performance/price_edge_v27/`: `summary.json`,
`report.md`, `picks.csv` and `tagged_candidates.csv`.

- **Picks:** every frozen v27 pick (latest pre-kickoff entry per fixture) is graded
  by CLV:
  - CLV = entry odds × Pinnacle's near-kickoff fair win-share on the same AH line − 1;
  - the closing-odds workflow collects the Pinnacle close;
  - margin removal is proportional, as in the rule.
  - CLV is split by bookmaker, odds band, reference type, favourite/underdog
    side and each tag (balanced, low_total, high_draw, any tag, no tag).
  - Flat-stake results are recorded too.
- **STOP REVIEW:** the report shows this flag when at least 100 graded picks have mean CLV below zero.
- **Tagged candidates:** each run writes `price_edge_tagged_candidates.csv`. It
  holds every tagged candidate, picked, rejected or probe, with the offered price
  against fair at capture. It is captured into the snapshot like the bet365 list.
  The review adds the final result and the return at the capture fair price, so
  the narrow-margin hypothesis is measured even when no pick is made.
- **History:** v26 and older history is unchanged.

## More frequent price checks (off by default)

`price_check.py` refreshes only the main odds request (`h2h`, `spreads`,
`totals`), and only for leagues with a stored fixture inside 48 hours. It merges
the fresh quotes into the stored forecast and re-runs v27 selection, then
publishes and captures a new run. Nothing is refit, and no per-event request is
made. The `Price checks` workflow fires hourly but does nothing unless both of these are set:

- the repository variable `PRICE_CHECKS_ENABLED` is `true`;
- the hour matches `PRICE_CHECK_INTERVAL_HOURS` (3, 4 or 6; default 4).

Estimated Odds API credits per month for the price checks alone, from
`python price_check.py --estimate`:

- **Method:** 3 credits per league with a fixture in the next 48 hours, one region.
- **Data:** 2024/25 kickoff dates for the 8 domestic leagues. UCL and UEL are
  approximated by their midweek rounds.

| Interval | Credits per month |
|---|---:|
| 3 hours | ~3,800 |
| 4 hours | ~2,850 |
| 6 hours | ~1,900 |

For comparison, the daily full run uses about 95 credits, or about 2,850 a month.

## Cagey score (tracking only)

`cagey_score` is the market-implied probability of a 2+ goal margin, either
side. It comes from the fit-B matrix, or from fit A when fit B is unusable,
and `cagey_fit` records which fit was used. Lower means cagier. The score is on
every candidate row, the readable shortlist and the tagged-candidate records,
and CLV tracking splits picks by its quintile. It is never read by any
decision. The calibration report compares the actual and predicted rates of
2+ and 3+ goal margins by quintile of the score, for fits A and B and each
season half.

## What CLV can be graded today

The closing-odds collector targets every frozen pick:

- **AH pick (including draw no bet):** it requests `spreads`, `alternate_spreads`
  and `draw_no_bet` from Pinnacle near kickoff and keeps every complete line pair.
  Pinnacle's close on the **same alternate line** is captured whenever Pinnacle
  still quotes that line, and CLV against it is graded.
- **1X2 and double-chance picks** (the ±0.5 equivalents): Pinnacle's 1X2 close is
  captured and CLV is graded from it.

Not gradeable today:

- **1xBet's own close** on an AH pick, because AH collection requests Pinnacle only.
  There is no same-book price CLV for 1xBet AH picks.
- **Tagged candidates that were not picked.** They are not collection targets.
  Their Pinnacle close exists only incidentally, when the same fixture has an AH
  pick and Pinnacle quotes that line. Their final result and the return at the
  capture fair price are always recorded.
- **Any pick whose line Pinnacle withdrew near kickoff.** The same applies if the
  collector found no quote within 6 minutes of kickoff that was at most 120
  seconds old, or if the 100 requests a day cap was hit. These stay missing,
  never estimated.
