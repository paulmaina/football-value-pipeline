# Main shortlist qualification

`value_rule: team-research-profit-v1` replaces the minimum-edge gate for the main
shortlist. Current markets, allowed bookmakers, 20-minute to 48-hour window,
maximum offered odds of 3.00 and one pick per fixture/market group are retained.
These choices preserve the existing scope while changing qualification.

Rank by the model probability that the actual settlement returns more than zero
after the recorded cost. Quarter lines split the stake correctly. Pushes and
half wins that cannot cover cost do not count as profitable. Expected return and
then price break ties. There is no minimum edge, no minimum probability and no
forced number of picks. Negative expected return is visible. Kelly staking may
recommend zero stake for such a pick.

## Numerical evidence

Ten completed matches per side, newest first, use exponential weights with a
five-match rank half-life. Separate home/away summaries are used when there are
at least three venue matches. At least five paired xG records per team are needed
to replace goals in a form rate. Missing xG never becomes synthetic xG.

The recent attacking/defending average is shrunk toward the existing fitted
team goal rate with a ten-match prior. Independent Poisson score probabilities
then produce all settlement probabilities. This is a new, unvalidated model
specification. It does not inherit calibration claims from the old price-edge
rule. Every pick carries that warning until forward evidence supports it.

## Free-source research

Scheduled forecasts pass `--research-free-sources`. Collection first reuses
cached responses, then attempts public ESPN fixture/summary/all-competition team
schedule/standings feeds, Understat public xG pages for covered leagues, dated
Bing news RSS with BBC and Guardian football RSS fallbacks, and Open-Meteo weather
with verified venue coordinates or an unambiguous venue city/country lookup.

These are source adapters, not an exhaustive search of the internet. Public
endpoints can fail or change. Responses have three-hour successful cache TTLs,
ten-minute failure TTLs, a 320-request run budget and bounded timeouts. Sources
remain visible, including failed attempts. No paid API or LLM key is required.

Absences/rosters are provider reports and news headlines are research leads.
They are not automatically confirmed absences or confirmed starting lineups.
Schedules expose congestion and previous venue/travel context. Standings provide
competition context. Motivation, tactics, rivalry, weather and squad information
have no invented numerical coefficients. Their evidence and missing/confirmation
warnings accompany the pick for review. Thus this release automates numerical
form-based qualification and research gathering; it does not claim calibrated
probability effects from all qualitative factors.

## Replay and availability

The run freezes research and source observation times in its prediction CSV.
Replay and price checks never fetch new research. Future observations, later
same-day results and future-dated headlines cannot enter the model. Missing or
stale context stays a visible warning, while a valid goal model and a valid,
pre-cutoff offered quote remain necessary to calculate a bet's probability.

Historical value rules remain selectable from their recorded summaries. The
cagey tier keeps its existing qualification. The master keeps its original
price-edge pool while displaying overlap with the new main shortlist.

## Accuracy comparison foundation

The full published score grid is now archived for offline comparison.
`research_backtest.py` compares published, Pinnacle-fit and frozen research
probabilities without changing live selection or staking. See
[the phased accuracy plan](research_accuracy_plan.md) for commands, evidence
limitations and corrections required before later probability changes.
