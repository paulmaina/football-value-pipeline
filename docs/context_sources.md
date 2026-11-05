# Pre-match context sources (reviewed 2026-11-05)

Source availability is not evidence of predictive gain. Existing local training,
recent form and supplied xG feed the research model. Weather, player reports,
lineups, congestion, standings and headlines remain sourced context until an
out-of-time experiment validates their probability effects. No wind threshold,
formation count or injury headline automatically triggers the cagey correction.

| Source | Automated role | Access and limitations |
| --- | --- | --- |
| ESPN public JSON | Exact fixture/summary, all-competition completed form and schedule, standings, named injury reports, rosters, dated team-relevant news metadata | Public endpoints can change; no SLA. A roster is not a confirmed XI. Explicit provider confirmation plus 11 unique identified starters per team is required for the confirmed label. Reports are not independently corroborated medical facts. |
| Understat public pages | Actual supplied xG in the five supported domestic leagues | Minimum paired-match rule remains; no generated xG. Domestic-to-European identity/strength transfer is not implemented here. |
| Open-Meteo forecast API | Temperature, precipitation, rain, snowfall, wind, gusts and humidity over kickoff through 105 minutes | Free hosted API is for noncommercial use, 10,000 calls/day; commercial use requires an appropriate plan. Units and observation time are frozen. Coverage requires temperature/precipitation/wind for every required hour with expected units. Partial data remain visible with warnings. Roof/pitch exposure is unknown. |
| TheSportsDB v1 public key 123 | Venue fallback using exact soccer teams/date/kickoff, then venue ID lookup | Free limit is 30 requests/minute, not 100. Local client enforces 30/minute and the shared run budget; other clients sharing the public key may still cause rate limits. No unrestricted team-search assumption. Ambiguous, scored or mistimed events cannot supply a venue. Only factual venue fields are extracted; website scraping is not used. |
| Premier Injuries | Manual reference link for EPL | Terms restrict reproduction and network storage without permission; no automated injury-table copying. Links do not count as coverage. |
| Sofascore | Manual reference link | No authorized public bulk-data integration configured; do not scrape around access restrictions. Links do not count as evidence. |
| Sports Mole | Manual preview reference link | Article reproduction requires permission; no bulk article copying. No verified RSS adapter is claimed. |
| API-Football | Existing configured adapter remains subject to entitlement | Free plan's 100/day allowance does not grant all current-season data. This project's current-season entitlement failures are not repaired by adding injury calls. No new key, paid plan or repeated blocked-season requests are introduced. |
| football-data.org | Existing UCL training/fixture adapter | Free tier has 10 requests/minute; current pricing places lineups and squads in paid Deep Data. No free lineup coverage is promised. |
| Bing/BBC/Guardian RSS | Existing fallback dated news leads if structured ESPN news is absent | Leads remain unconfirmed context, never article bodies or numerical absence adjustments. |

Weather prefers the verified fixture's stadium coordinates. If absent, a uniquely
matched TheSportsDB fixture may supply its actual venue (including neutral sites).
An unambiguous venue city/country lookup is a labelled city-centre approximation;
there is no guess from the home club's usual stadium. Incomplete core hours,
invalid numeric values or unknown core units never earn complete weather coverage.
Optional missing fields are listed separately. Snowfall units are retained as
returned (typically cm), not relabelled as rainfall mm.

Successful responses normally expire after three hours; failures after ten
minutes. Inside two hours of kickoff, summary requests use a five-minute maximum
age and weather uses fifteen minutes. Collection has a 320-request run budget,
5-second connect/15-second read timeouts and a 4 MB response limit. Cache hits do
not spend request budget. Post-kickoff collection is refused. Every attempt has
its URL, status and observation timestamp; predictions freeze extracted evidence
for offline replay. Raw response caches are not part of this source change.

This does not install a new 60–75-minute pre-kickoff schedule. The existing
scheduled/manual collection can see late information when it runs then; it does
not guarantee confirmed XIs for every match. Predicted-vs-confirmed formation
changes, player xG/minutes value, weather coefficients, travel-distance effects
and motivation scores need dated inputs and historical/forward validation before
changing probabilities. Missing context keeps a match eligible with a warning.

Official documentation and access terms:
- https://open-meteo.com/en/docs
- https://open-meteo.com/en/pricing
- https://www.thesportsdb.com/docs/api
- https://www.thesportsdb.com/pricing
- https://www.thesportsdb.com/terms_of_service
- https://www.premierinjuries.com/terms
- https://www.sofascore.com/terms-and-conditions
- https://www.sportsmole.co.uk/terms-and-conditions.html
- https://www.api-football.com/pricing
- https://www.football-data.org/pricing
