# Coverage cost of the live list changes (Parts 1-2, 24 Nov 2026)

Information only (docs/plan.md Phase 4d, "After the release"). Locked backtest, development and validation; the holdout is never read. Offline offers are Home win, Away win and the main AH line, so double chance and alternate lines are exercised only live.

## Value shortlist and cagey tier (Part 1: odds above 1.20)

Offline, each list nominates its best offer in each market group of each fixture (the master backtest's rule, evaluation_harness.master_fixture), without the live lists' entry thresholds. So both lists nominate the same number of bets by construction, and the floor costs a bet only where every offline offer in a group is at 1.20 or below. Where a group keeps an offer above 1.20, the list nominates that offer instead.

| period | weeks | list | bets/week before | after | lost | matches/week before | after | lost |
|---|---|---|---|---|---|---|---|---|
| development | 106 | value shortlist | 100.02 | 98.69 | 1.33 | 64.86 | 64.86 | 0.00 |
| development | 106 | cagey tier | 100.02 | 98.69 | 1.33 | 64.86 | 64.86 | 0.00 |
| validation | 22 | value shortlist | 91.00 | 89.86 | 1.14 | 59.32 | 59.32 | 0.00 |
| validation | 22 | cagey tier | 91.00 | 89.86 | 1.14 | 59.32 | 59.32 | 0.00 |

## Strong master (Parts 1-2: odds floor and research no-loss >= 0.70)

| period | weeks | picks/week before | after | lost | weeks reaching 15 before | after | weeks at the offline maximum (12) before | after | offers left out by the research gate |
|---|---|---|---|---|---|---|---|---|---|
| development | 106 | 11.62 | 8.70 | 2.92 | 0 | 0 | 99 | 29 | 10038 |
| validation | 22 | 11.41 | 7.82 | 3.59 | 0 | 0 | 20 | 3 | 1915 |

Offline the strong master can hold at most 12 picks a week (6 match result, 6 Asian handicap; no double chance offline), so it reaches 15 in no week either before or after; live runs also offer double chance and alternate lines.
