# Per-market shortlist (v24)

Policy `48h-two-per-market-group-probability-ev-v24` selects at most two matches
from each market group, up to fourteen in total, from matches kicking off within
48 hours. It replaces v23 for new prediction runs and shortlist refreshes.

## Market groups

| Group | Markets |
|---|---|
| Asian handicap | Every quoted line on either team (one shared group) |
| Home win | Home win |
| Away win | Away win |
| Over 1.5 | Over 1.5 |
| Double Chance 1X | Double Chance 1X |
| Double Chance X2 | Double Chance X2 |
| Double Chance 12 | Double Chance 12 |

Draw is excluded. Under 3.5 and BTTS remain excluded.

## Eligibility

v24 reuses v23 eligibility unchanged: the 48-hour window and 20-minute
pre-kickoff buffer; fresh, exact Pinnacle or bet365 quotes; identity,
competition and historical reliability checks; and probability validity.
Profitable outcomes are defined as in v23: full and half wins count, refunds do
not. See [win-first-shortlist.md](win-first-shortlist.md).

## Ranking and selection

1. Keep the best quote per fixture and market (by adjusted probability, then
   adjusted EV), so duplicate bookmaker rows do not distort percentiles.
2. Within each market group, compute the empirical percentile of the adjusted
   probability and the adjusted EV among that group's eligible candidates.
3. Score = 0.5 × probability percentile + 0.5 × EV percentile.
4. Compute the most slots any allocation can fill, with one market per
   fixture, at most two per group and fourteen in total.
5. Walk all candidates by score, highest first (ties: adjusted probability,
   adjusted EV, unblended EV, odds, then stable fixture/market/bookmaker
   fields). Accept a candidate if its fixture is unused, its group has a free
   slot, and the remaining slots can still be filled to the maximum from
   step 4.

One market per fixture: when a fixture is a candidate in two groups, the
higher-scoring market claims it unless that would leave a fillable slot
empty. Example: Home win has fixtures A, B and C; Double Chance 1X has only A
and B. Taking A and B for Home win would leave 1X empty, so the selector
takes A and C for Home win and B for 1X. Percentiles are relative ranks
within a group, not probabilities, so a group with a single eligible
candidate scores it 1.0.

The shortlist is presented in group order, best score first within each group.

## Value and shortfalls

There is no probability or EV floor. Every selection with negative adjusted EV
is flagged in `selection_warnings`, counted in
`negative_adjusted_ev_selections`, and listed in `negative_adjusted_ev_markets`
and the readable report.

A slot stays empty only when no allocation of the eligible candidates can
fill it: the group has fewer than two eligible fixtures, or its fixtures are
needed by other groups and no rearrangement frees one. Other groups never
fill empty slots.
`group_shortfall` in the summary records eligible matches, selections and
empty slots for each group; the readable report shows the same table.

## Replay

v17–v23 keep their definitions; `win_first_shortlist.py` is unchanged.
Archived captures replay with their recorded policy version. The workflow
replay check rebuilds v24 shortlists deterministically and also enforces the
two-per-group cap and the fourteen maximum.
