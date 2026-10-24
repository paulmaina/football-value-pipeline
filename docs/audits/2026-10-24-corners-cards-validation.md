# Corner and card total models: walk-forward validation (2026-10-24)

**Decision:** every corner total line (7.5 to 12.5, Over and Under) passes in EPL, LaLiga, Bundesliga, Serie A and Ligue 1, and every card total line (2.5 to 6.5) passes in Bundesliga, Serie A and Ligue 1. Each league/line/side is approved on its own audit with the goal-market thresholds unchanged.

> **Validation covers probability accuracy only.** No historical corner or card odds exist in the repository or the CSVs, so nothing here shows that these markets can be bet profitably. Every Corners and Cards pick carries the warning `UNPROVEN EDGE: probability-only validation; no historical corner/card odds`.

## Scope

The Odds API was checked on 2026-10-24 with one fixture per league (9 credits):

| League | Pinnacle corner totals | Pinnacle card totals | Modelled |
|---|---|---|---|
| EPL, LaLiga | yes | no | corners |
| Bundesliga, Serie A, Ligue 1 | yes | yes | corners and cards |
| UCL, UEL (fixtures 10+ days out) | no | no | no |
| Eredivisie, Primeira Liga | no | no | no |

bet365 never appeared in the `eu,uk` responses. Requesting `alternate_totals_corners` (and `alternate_totals_cards` where modelled) adds those markets to each per-event odds request in the five leagues, which increases its credit cost.

## Model

`count_markets.py` (`count-markets-nb2-v1`): a negative-binomial (NB2) regression for the match total, because corner and card totals are overdispersed (corners: mean 9.4–10.3, variance 11.0–11.5; cards: mean 3.9–5.0, variance 4.4–6.8).

- **Inputs:** football-data.co.uk HC, AC, HS, AS for corners; HY, AY, HR, AR, HF, AF for cards. Each yellow and each red card counts once. Bookmaker settlement rules (booking points, second yellows) may differ, and that difference is not validated.
- **Features:** each team's exponentially weighted form (half-life 10 matches, shrunk toward the league mean with 3 prior matches): totals for and against, plus shots (corners) or fouls (cards) for and against. They are expressed as log ratios to the drifting league mean, with the league mean as an offset. A match uses results from earlier calendar days only.
- **Fit:** maximum likelihood with an L2 penalty of 1.0 on slopes. The dispersion is fitted, bounded to [1e-4, 5]. Settings were fixed before validation and not tuned on the audit.
- BBS statistics were not used: the Free plan holds only the current season (see `docs/bbs-data-integration.md`).

## Method

Same as the goal-market validation: six committed seasons (2021-22 to 2026-27), a 500-match burn-in, refit every 56 days on all earlier matches, and forecasts for the next 56 days. The forecasts are split 75% development / 25% audit by date, never splitting a day. A line/side is `RELIABLE_FOR_RANKING` with at least 80 development and 25 audit matches, audit |overconfidence| ≤ 0.12 and audit Brier ≤ constant-frequency baseline + 0.005. The 75%+ and 85%+ tiers need 30/12 matches and overconfidence ≤ 0.10. The penalty is development overconfidence shrunk by n/(n+100). These are `goal_market_validation.py`'s functions and constants, imported unchanged.

## Results

The count log loss compares the full count distribution with a constant-rate negative binomial fitted to the development totals (a hindsight baseline).

| league | market | forecasts | dev / audit n | count log loss audit (model / constant) | dev (model / constant) | lines passing |
|---|---|---|---:|---|---|---:|
| EPL | corners | 2022-12-26 to 2026-10-19 | 1079 / 365 | 2.5792 / 2.5900 | 2.6398 / 2.6472 | 12 / 12 |
| LaLiga | corners | 2022-12-30 to 2026-10-21 | 1098 / 368 | 2.6768 / 2.6884 | 2.5886 / 2.5928 | 12 / 12 |
| Bundesliga | corners | 2023-04-22 to 2026-10-18 | 764 / 260 | 2.6385 / 2.6403 | 2.6094 / 2.6092 | 12 / 12 |
| Bundesliga | cards | 2023-04-22 to 2026-10-18 | 764 / 260 | 2.1207 / 2.1483 | 2.2063 / 2.2153 | 10 / 10 |
| SerieA | corners | 2023-01-04 to 2026-10-19 | 1080 / 360 | 2.5716 / 2.5840 | 2.6401 / 2.6477 | 12 / 12 |
| SerieA | cards | 2023-01-04 to 2026-10-19 | 1080 / 360 | 2.0346 / 2.0992 | 2.1468 / 2.1821 | 10 / 10 |
| Ligue1 | corners | 2022-12-28 to 2026-10-18 | 906 / 305 | 2.6432 / 2.6443 | 2.5899 / 2.5849 | 12 / 12 |
| Ligue1 | cards | 2022-12-28 to 2026-10-18 | 906 / 305 | 2.0282 / 2.0521 | 2.1130 / 2.1349 | 10 / 10 |

### Corners: audit Brier excess over constant baseline / audit overconfidence / 75%+ and 85%+ tiers

| market | EPL | LaLiga | Bundesliga | SerieA | Ligue1 |
|---|---|---|---|---|---|
| Corners Over 7.5 | OK +0.0005 / +0.005 P/i | OK -0.0023 / +0.028 P/i | OK +0.0016 / -0.033 P/i | OK +0.0013 / -0.006 i/i | OK +0.0010 / +0.010 P/i |
| Corners Under 7.5 | OK +0.0005 / -0.005 i/i | OK -0.0023 / -0.028 i/i | OK +0.0016 / +0.033 i/i | OK +0.0013 / +0.006 i/i | OK +0.0010 / -0.010 i/i |
| Corners Over 8.5 | OK +0.0004 / +0.014 i/i | OK -0.0025 / +0.042 i/i | OK +0.0012 / -0.032 i/i | OK +0.0008 / +0.009 i/i | OK -0.0014 / -0.011 i/i |
| Corners Under 8.5 | OK +0.0004 / -0.014 i/i | OK -0.0025 / -0.042 i/i | OK +0.0012 / +0.032 i/i | OK +0.0008 / -0.009 i/i | OK -0.0014 / +0.011 i/i |
| Corners Over 9.5 | OK -0.0005 / -0.018 i/i | OK -0.0038 / +0.015 i/i | OK -0.0010 / -0.030 i/i | OK -0.0013 / +0.003 i/i | OK -0.0014 / -0.021 i/i |
| Corners Under 9.5 | OK -0.0005 / +0.018 i/i | OK -0.0038 / -0.015 i/i | OK -0.0010 / +0.030 i/i | OK -0.0013 / -0.003 i/i | OK -0.0014 / +0.021 i/i |
| Corners Over 10.5 | OK -0.0009 / -0.019 i/i | OK -0.0049 / +0.018 i/i | OK +0.0002 / -0.016 i/i | OK +0.0012 / +0.003 i/i | OK -0.0019 / -0.001 i/i |
| Corners Under 10.5 | OK -0.0009 / +0.019 i/i | OK -0.0049 / -0.018 i/i | OK +0.0002 / +0.016 i/i | OK +0.0012 / -0.003 P/i | OK -0.0019 / +0.001 i/i |
| Corners Over 11.5 | OK -0.0016 / -0.008 i/i | OK -0.0043 / +0.001 i/i | OK +0.0018 / -0.046 i/i | OK +0.0002 / -0.007 i/i | OK -0.0010 / +0.011 i/i |
| Corners Under 11.5 | OK -0.0016 / +0.008 H/i | OK -0.0043 / -0.001 P/i | OK +0.0018 / +0.046 P/i | OK +0.0002 / +0.007 P/i | OK -0.0010 / -0.011 P/i |
| Corners Over 12.5 | OK -0.0001 / -0.002 i/i | OK -0.0022 / -0.006 i/i | OK +0.0019 / -0.054 i/i | OK +0.0014 / -0.002 i/i | OK +0.0004 / -0.016 i/i |
| Corners Under 12.5 | OK -0.0001 / +0.002 P/i | OK -0.0022 / +0.006 P/P | OK +0.0019 / +0.054 P/P | OK +0.0014 / +0.002 P/P | OK +0.0004 / +0.016 P/P |

### Cards: audit Brier excess over constant baseline / audit overconfidence / 75%+ and 85%+ tiers

| market | Bundesliga | SerieA | Ligue1 |
|---|---|---|---|
| Cards Over 2.5 | OK -0.0037 / +0.025 P/i | OK +0.0005 / -0.006 P/P | OK -0.0099 / -0.018 P/i |
| Cards Under 2.5 | OK -0.0037 / -0.025 i/i | OK +0.0005 / +0.006 i/i | OK -0.0099 / +0.018 i/i |
| Cards Over 3.5 | OK -0.0003 / +0.046 i/i | OK -0.0143 / +0.013 i/i | OK -0.0093 / -0.001 i/i |
| Cards Under 3.5 | OK -0.0003 / -0.046 i/i | OK -0.0143 / -0.013 i/i | OK -0.0093 / +0.001 i/i |
| Cards Over 4.5 | OK +0.0014 / +0.046 i/i | OK -0.0149 / -0.002 i/i | OK -0.0048 / +0.018 i/i |
| Cards Under 4.5 | OK +0.0014 / -0.046 i/i | OK -0.0149 / +0.002 P/i | OK -0.0048 / -0.018 P/i |
| Cards Over 5.5 | OK -0.0007 / +0.044 i/i | OK -0.0052 / +0.005 i/i | OK +0.0025 / +0.059 i/i |
| Cards Under 5.5 | OK -0.0007 / -0.044 P/i | OK -0.0052 / -0.005 P/P | OK +0.0025 / -0.059 P/P |
| Cards Over 6.5 | OK -0.0013 / +0.013 i/i | OK -0.0017 / +0.018 i/i | OK +0.0017 / +0.041 i/i |
| Cards Under 6.5 | OK -0.0013 / -0.013 P/P | OK -0.0017 / -0.018 P/P | OK +0.0017 / -0.041 P/P |

## Reading the results

- **Cards carry real signal:** audit count log loss improves by 0.024 (Ligue 1), 0.028 (Bundesliga) and 0.065 (Serie A), and Serie A's 3.5 and 4.5 lines beat the constant baseline's Brier by about 0.015.
- **Corner skill is marginal:** audit count log loss improves by 0.001 to 0.012. Bundesliga and Ligue 1 corners are no better than the constant rate in development, and several corner lines are slightly worse than the constant baseline in the audit while staying within the +0.005 allowance. They are approved because the unchanged rule approves them, not because they show an edge.
- High-probability picks are rare: most lines lack enough 75%+ forecasts, so the tier rule blocks those forecasts.

## Not covered

- Profitability, closing-line value or any bookmaker margin: no historical prices exist.
- Grading: settled results come from football-data.org scores, which have no corner or card counts, so corner and card picks are recorded but graded `UNSUPPORTED_MARKET` until a verified count-result source is added.
