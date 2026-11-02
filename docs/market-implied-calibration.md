# Market-implied fair price and its calibration check

`market_implied.py` fits, per fixture, home and away goal rates plus a
Dixon-Coles rho so the score matrix reproduces Pinnacle's margin-free prices:

- **Fit A:** 1X2 and O/U 2.5.
- **Fit B:** 1X2, O/U 2.5 and the main Asian handicap line (two-way margin removed).

Any AH line, whole, half or quarter, is then priced exactly from the matrix
(fair win-share = wins / (wins + losses), refunds excluded). The fit reports
the residual on every input. It is **unusable** (fails closed) when an input
is missing or stale, or when any residual exceeds 3pp. The production
Dixon-Coles model is not involved.

## Calibration check (not tuning)

```
py market_implied_calibration.py
```

The script reads the football-data.co.uk CSVs already in `.football_cache`: Pinnacle close 1X2, O/U 2.5 and
main AH, for 8 leagues. For each fit it bets every line from +0.5 to +2.25 and
-0.5 to -2.25, both sides, at the matrix fair price. Results are split by:

- balance (both 1X2 prices in [2.00, 3.50] or [2.00, 2.80]);
- expected total and draw probability bands, and their combinations;
- favourite/underdog side and home/away side;
- league.

Every slice is also split by season half (to the end of 2023, and from 2024).
Intervals resample whole gameweeks. Output goes to
`football_output_v2/performance/market_implied_calibration/` (`report.md`, `summary.json`).

The report states how many intervals exclude zero against the 5% expected by
chance. The slices overlap heavily, so that figure is only a rough yardstick.
It also answers whether fit B removes the plus-line underpricing seen in fit A,
and lists the slices where underpricing remains in both season halves. These
are hypotheses to track forward. No correction is fitted or applied; any
correction would be a separate change with a season holdout.

The v27 shortlist uses fit B only as a last-resort reference for plus lines.
Positive plus-line returns mean the matrix understates a derived edge there,
while minus-line returns show it would overstate one.
