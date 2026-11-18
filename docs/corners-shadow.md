# Shadow corner list (corners-shadow-v1)

Decided by Paul on 18 Nov 2026. A record of corner bets the pipeline would take, kept to collect the evidence no
historical data can give: closing-line value against Pinnacle. **Unvalidated, not bet, zero stake.**

## Why a shadow list

The offline study (`docs/corners-candidate.md`, PR #199) found corner skill beyond the league average on
development only, and no historical corner prices at all, so returns and CLV cannot be tested offline. Collecting
Pinnacle's corner prices at entry and near kickoff for a fixed rule is the only way to learn whether the count
model finds value.

## The list

- Every forecast run writes `corners_shadow.csv` beside the live lists, after all of them.
- One row per domestic fixture that has a count-model forecast and a fresh, complete Pinnacle corner-totals pair:
  the line and side with the best expected return (model probability × Pinnacle price − 1) among prices in
  (1.15, 2.20]. Lines 7.5-12.5, half lines only. The row is written even when the best expected return is negative.
- Model: `count_markets` (count-markets-nb2-v1), unchanged and still run in every forecast (`count_model`). It
  covers EPL, LaLiga, Bundesliga, Serie A and Ligue 1; the step-2 candidate K1 did not clearly beat it.
- Every row: `status` "unvalidated, not bet", `stake` 0, `list_version` corners-shadow-v1.
- Not part of the value shortlist, the cagey tier, the new or old master. Rebuilding every live list from the
  8 Nov 2026 run with and without corner prices in the predictions gives byte-identical files (48 files).

## Prices

- Entry: domestic per-event requests add `alternate_totals_corners` (UCL/UEL never; Pinnacle does not price their
  corners). Parsed by `count_markets.parse_quotes`, with their own event-identity check, into the prediction
  column `count_market_offers`. No live field changes when the market is present (tested).
- Close: `closing_odds.py`'s collection loop also calls `corners_shadow.collect_closing`, which requests
  Pinnacle `alternate_totals_corners` for shadow picks kicking off within 6 minutes, keeps quotes no older than
  120 seconds (the live collector's rules), and stores hash-named observations in
  `football_output_v2/corners_shadow/closing/`. Own daily cap (40 requests), at most 2 requests per fixture,
  skipped when credits are low. It never reads or writes the live collector's observations or budget.
- Credits: about one per big-five fixture per forecast run while it is in the 72-hour window, plus one or two per
  pick at close: roughly 0.8-1k a month on the 20K plan.

## Grading (weekly, `performance_tracking.py review`)

Each fixture's latest pre-kickoff archived pick is graded from the committed football-data corner counts
(`count_markets.verified_total`, only when the row's score matches the verified final score):

- win rate and return per unit had each pick been staked;
- CLV = entry odds × Pinnacle's power-de-vigged closing probability for the same line and side − 1
  (clv_report's definition), with the share of picks beating the close;
- overall, picks with positive expected return at entry, and by kickoff week.

Written to `football_output_v2/performance/corners_shadow/` (`grades.csv`, `summary.json`, `report.md`).
Corner counts arrive with the training-data refresh, so recent picks show `AWAITING_COUNT_RESULT` until then.
