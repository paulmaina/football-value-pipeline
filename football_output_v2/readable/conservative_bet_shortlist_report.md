# Conservative shortlisted matches and markets

Stored forecasts re-ranked; no new odds or model fitting; UCL historical validation missing: rerun the full six-league pipeline
**Candidates:** 5 of target 10 distinct matches.
**Strictly qualified:** 1. **Provisional watchlist:** 4.
**Pipeline status:** BELOW_TARGET_WITH_PROVISIONAL.
**Generated (UTC):** 2026-10-11T08:16:48.175077+00:00.
**Kickoffs within next 72 hours of run:** Yes (span: 30.0 hours).

> WARNING: PROVISIONAL watchlist entries FAILED one or more strict historical/EV rules; they are for research only, NOT qualified bets. Even STRICT candidates are not guaranteed outcomes or proven profitable selections. Do not treat ten candidates as a ten-leg betslip.

## Shortlisted market for each match

| Match | Shortlisted market | Qualification | Kickoff (UTC) | Model chance | Reliability-adjusted chance | Bookmaker | Quoted decimal odds | Conservative estimated EV | Near-miss reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Atalanta BC vs Venezia | Home win | STRICT | 2026-10-12T16:30:00+00:00 | 68.9% | 68.2% | 1xBet | 1.63 | +11.2% | — |
| Real Racing Club de Santander vs Valencia | Over 1.5 | PROVISIONAL | 2026-10-11T19:00:00+00:00 | 90.0% | 90.0% | Coolbet | 1.24 | +11.5% | 85plus market history: INSUFFICIENT_HIGH_CONFIDENCE_HISTORY |
| Lecce vs Bologna | Under 3.5 | PROVISIONAL | 2026-10-11T13:00:00+00:00 | 83.6% | 79.6% | Coolbet | 1.28 | +1.9% | reliability-adjusted EV below +3% or missing |
| Hull City vs Everton | Under 3.5 | PROVISIONAL | 2026-10-11T13:00:00+00:00 | 90.3% | 83.3% | Coolbet | 1.32 | +10.0% | 85plus market history: INSUFFICIENT_HIGH_CONFIDENCE_HISTORY |
| Coventry City vs Newcastle United | Under 3.5 | PROVISIONAL | 2026-10-12T19:00:00+00:00 | 84.4% | 83.7% | Coolbet | 1.50 | +25.5% | 75plus market history: HIGH_CONFIDENCE_OVERESTIMATION |

## Interpretation

**STRICT** means every configured historical, probability, odds and EV rule passed. **PROVISIONAL** means the specified historical or small adjusted-EV checks FAILED, although the essential source, reference-market integrity, team and price rules passed. Never count provisional candidates as verified reliable bets. Model chance describes the selected market, not necessarily the home or away match winner.

Reliability-adjusted chance discounts historical overconfidence using an earlier chronological development sample; a later audit must pass the predefined quality gate. It remains an estimate.

When forecast probability is 75% or higher, the chosen market must separately pass the >=75% historical audit; >=85% forecasts must pass the >=85% audit. The readable CSV includes the group sample size, observed rate and Wilson 95% uncertainty range.

Conservative estimated EV uses that adjusted chance and the quoted price. Neither the original EV nor the adjusted EV is assured; bookmaker prices may change before kickoff.

**Four-day selection:** Strict-first ranking within the next 72 hours of the run

The readable CSV includes raw Dixon-Coles probabilities, bookmaker-implied probabilities, and unblended EV for audit.
