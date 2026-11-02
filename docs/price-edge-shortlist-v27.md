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
