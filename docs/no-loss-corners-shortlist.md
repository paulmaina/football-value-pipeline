# No-loss shortlist with Corners (v26)

Policy `48h-zero-tolerance-ev1-no-loss75-corners-v26` is v22's common no-loss rules plus Corners totals. It replaces v25 for new prediction runs and shortlist refreshes.

## Selection

Unchanged from v22 ([asian-handicap-shortlist.md](asian-handicap-shortlist.md)):

- Adjusted probability of avoiding a loss of at least 75%. Asian handicap refunds count as avoiding a loss; half-losses do not.
- Adjusted EV of at least +1.0%, and unblended EV not negative.
- Zero risk tolerance: for each fixture, the lowest conservative estimated loss risk wins; adjusted EV, unblended EV and refund probability break equal-risk ties.
- One market per fixture, at most 12 fixtures, no market quotas. Kickoff within 20 minutes to 48 hours.
- Markets: Asian handicap lines, Home win, Away win, Over 1.5, Double Chance 1X, X2 and 12, and Corners Over/Under 7.5 to 12.5.

Fewer than 12 picks are returned when too few candidates pass the floors; the list is never padded.

## Corners

Corner candidates come from the v25 count-market gates unchanged ([corners-cards-shortlist.md](corners-cards-shortlist.md)): a fresh same-book Pinnacle or bet365 pair, the league's own audit for that exact line and side, the high-confidence tier for forecasts of 75% or more, and the usual window, identity and blend checks. They then face the same floors as every other market. Corner lines are half lines, so avoiding a loss means winning. The count model has no independent second forecast, so its unpenalized EV stands in for the unblended-EV check.

Every Corners pick carries the `UNPROVEN EDGE` warning: the model is validated on probability accuracy only and no historical corner odds exist. Card totals are excluded.

## Approval

Every league is approved per market, as in v25. A league/market whose audit is not `RELIABLE_FOR_RANKING` is rejected with `per-market approval: …`; the league's other markets stay eligible.

## Production and replay

`asian_handicap.PRODUCTION_POLICY` names the policy for new shortlists; both the full pipeline and `refresh_conservative_shortlist.py` read it. Routing is by each capture's recorded version, so v17–v25 replay and grade unchanged. `shortlist_quote_policy.json` records the zero risk tolerance and the 75% floor. The workflow replay check rebuilds v26 shortlists deterministically, enforces the 12 cap and v22's summary fields, and requires the unproven-edge flag on every Corners pick.
