# Corners and Cards shortlist (v25)

Policy `48h-two-per-market-group-probability-ev-corners-cards-v25` is v24 with two more market groups, Corners and Cards, and per-market approval for every league. It replaces v24 for new prediction runs and shortlist refreshes.

## Market groups

The seven v24 groups (Asian handicap, Home win, Away win, Over 1.5, Double Chance 1X, X2 and 12), plus:

| Group | Markets | Leagues |
|---|---|---|
| Corners | Over/Under 7.5 to 12.5 total corners | EPL, LaLiga, Bundesliga, Serie A, Ligue 1 |
| Cards | Over/Under 2.5 to 6.5 total cards | None: out of production (below) |

At most two picks per group and 18 in total, one market per fixture. Ranking, allocation and shortfall rules are v24's, unchanged: 0.8 × adjusted-probability percentile + 0.2 × adjusted-EV percentile within the group, and no group fills another group's empty slots. See [per-market-shortlist.md](per-market-shortlist.md).

## Eligibility

- **Every league is approved per market.** A league/market qualifies only if its own audit is `RELIABLE_FOR_RANKING`. A forecast of 75% or more also needs its high-confidence tier `PASSED`. Failed or missing evidence is rejected with `per-market approval: …`; the league's other markets stay eligible. For the existing markets this only labels v23's existing rejections, so eligibility matches v24.
- **Corners and Cards** need: a fresh, complete same-book Pinnacle or bet365 Over/Under pair on a validated half line (combined implied probability 0.98–1.20); kickoff within 20 minutes to 48 hours; a verified live 1X2 blend; reliable team identity; a current count-model forecast; and that league's own audit for that exact line and side.
- **Cards** are rejected in every league with `card totals out of production`: Pinnacle settles bookings (yellow 1, red 2, second yellow excluded) and football-data.co.uk counts cannot reproduce that total, so the model would validate a different outcome from the bet. The group stays in v25 with both slots empty until the data supports it.
- **Probability and EV:** the model probability comes from the NB2 count model (`count_markets.py`). The adjusted probability subtracts the larger of the line's development penalty and its tier penalty. EV uses the quoted price.

## Unproven edge

Count models are validated on probability accuracy only ([audits/2026-10-24-corners-cards-validation.md](audits/2026-10-24-corners-cards-validation.md)); no historical corner or card odds exist. Every Corners pick has `UNPROVEN EDGE` in `selection_warnings`, `unproven_edge=True`, and is counted in the summary's `unproven_edge_selections` and `unproven_edge_markets`. The readable report shows an UNPROVEN EDGE line.

## Grading

Verified scores come from football-data.org and carry no corner counts. A Corners pick settles from the committed football-data.co.uk row for the same model teams within a day of kickoff, and only when that row's score equals the verified final score. Until the training refresh brings in that row, the pick is `AWAITING_COUNT_RESULT`: pending, with no profit or Brier score. Settled picks enter win rate, ROI and calibration like any other market, and the workflow archive check re-verifies each one against the same row.

## Replay

v24 and older keep their definitions, and archived captures replay with their recorded policy. The workflow replay check rebuilds v25 shortlists deterministically, enforces the 18 maximum and two-per-group cap, and requires the unproven-edge flag on every Corners and Cards pick.
