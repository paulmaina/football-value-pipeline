# Current rule: local training plus free research

`local-research-profit-115-200-dc12-v2` is the current main-shortlist rule.
It replaces `per-market-v2` in the live configuration and supersedes
`team-research-profit-v1` for new generations. Its probability basis
`team_form_poisson_v1` is unvalidated; `research_backtest.py` results are still
pending. Passing software tests does not demonstrate prediction accuracy. Old summaries retain
and replay their recorded rules, prices and selection behavior.

- Offered decimal odds must be strictly greater than 1.15 and at most 2.00.
- Markets: home win, away win, double chance 1X/X2/12, quoted Asian Handicap
  and Over 1.5. No synthetic odds or invented handicap equivalents for DC 12.
  Forward grading and closing-value tracking also handle DC 12 as a non-draw
  binary market, separately from Over 1.5 and handicap lines.
- Keep one pick per fixture per market group. For AH this means the safest
  actual quoted line inside the odds range: highest positive-net-return
  probability, then expected return, then price. An AH +/-0.5 quote remains
  in the AH group; an actual match-winner/DC quote stays in its own group.
- Rank all picks by positive-net-return probability. Pushes are not profitable.
  Negative EV remains eligible, flagged; Kelly may recommend zero stake.
- Keep the 20-minute–48-hour kickoff window and existing bookmaker allowlist.
  Other shortlists retain their own rules; this odds range is for the main list.

All supported leagues, including UCL and UEL, train on validated local competition
history. Domestic history already comes from cached CSVs and verified sidecar
observations. UCL can now use validated local season JSON without a live API key;
with a key, current-season refresh is still attempted and failure retains cache.
UEL preflight retains a structurally valid, previously verified local snapshot
when live reconciliation fails, without moving its verification timestamp.
Failed-refresh fallback requires verification no more than ten days before the
evaluation time. Older snapshots are excluded as `TRAINING_UNVERIFIED`.
Corrupt, future-verified, duplicate or invalid-score caches are not fallbacks.
Unknown teams and Europa teams below six prior appearances still cannot qualify.
Result grading continues to require corroborated results; fallback training does
not authorize unverified settlement.

Normal forecast generation now enables bounded free-source research by default.
`--research-free-sources` remains supported; `--no-research-free-sources` opts into
cached research only. Source failures remain coverage warnings. Training status,
cutoff and refresh warning are frozen alongside the researched probabilities.
Each league's CSV and readable prediction view includes the same research as the
combined forecast. Replay and price-only refresh remain offline.

The existing published Dixon–Coles forecast remains the baseline. Explicit
`research_p_home/draw/away/over_1_5` columns and `team_research_json` expose the
locally trained rates supplemented by recent sourced form and available xG;
these research settlement probabilities drive this shortlist. Qualitative
injury/news/weather context has no invented numerical coefficients. This update
makes data availability and selection explicit; it does not establish an
accuracy improvement or promote new fitted blend/calibration coefficients.

## Previous rule and numerical research specification

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
ESPN news metadata with Bing/BBC/Guardian RSS fallbacks, and Open-Meteo match-window
weather with verified stadium coordinates, exact-fixture TheSportsDB venue fallback,
or an unambiguous venue city/country lookup. Named availability and lineup records
retain confirmation status. See [source access, cadence and coverage](context_sources.md)
for limits and the distinction between collected context and numerical inputs.

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
cagey tier keeps its existing qualification. The master uses the value/cagey nomination union with its own recorded market-reference rule; see
[master selection](master-market-selection.md).

## Accuracy comparison foundation

The full published score grid is now archived for offline comparison.
`research_backtest.py` compares published, Pinnacle-fit and frozen research
probabilities without changing live selection or staking. See
[the phased accuracy plan](research_accuracy_plan.md) for commands, evidence
limitations and corrections required before later probability changes.

## Research hardening for Pinnacle execution

This production change strengthens evidence quality without fitting new goal-rate,
weather, player-value or probability coefficients. It follows the Pinnacle-only
execution change; exact offered prices/lines and all selection/staking rules remain
subject to that policy. It introduces no experiment lists or parallel live models.

- In-memory research responses now obey the same observation-time and per-call TTL
  checks as disk caches. A previously memoized three-hour observation cannot satisfy
  a later five-minute lineup request. Malformed cached responses are refetched or
  reported unavailable rather than aborting the whole fixture's research.
- ESPN summaries must match the requested event ID, both teams and kickoff. A wrong,
  ambiguous or already-started/completed summary cannot supply injuries, starting
  XIs or venue data. A separately verified scoreboard venue remains available.
- Team IDs and reported names must agree. An opponent's name paired with another
  team's ID cannot attach a player report to a fixture.
- Every newly enriched forecast freezes a versioned factual quality review: both
  confirmed XIs, absence-report availability, weather freshness/completeness, form
  and venue sample counts, xG sample counts, and training status/cutoff warnings.
  Confirmation requires exactly two expected teams and 22 distinct starter IDs.
  Empty injury data never means 'no injuries'.
- Within two hours of kickoff, summary observations must be under five minutes
  old and match-window weather under fifteen minutes old to pass those review
  checks; outside that window the existing three-hour limits apply. These are
  evidence freshness limits, not probability coefficients or new shortlist gates.

Value/cagey readable CSVs and Excel tabs now share research coverage warnings and
quality-review text. The master carries the same warning evidence in its existing
coverage/uncertainty fields. Existing numeric form, xG thresholds, goal-rate
shrinkage, score grids, AH settlement, prices, ranking and staking formulas are
unchanged. Validated, fresher evidence can differ from stale/mismatched material;
that is a data-quality correction, not proof of an accuracy or betting advantage.

On a price refresh, the versioned review is reassessed against the new evaluation
clock using the same frozen facts. Old lineup/weather observations become visibly
stale; no future news is fetched or spliced into replay. Old forecasts without the
new evidence-quality version keep their original research interpretation. Missing
or unconfirmed research remains eligible with warnings, in line with the current
policy. Re-run full forecast collection to obtain newly observed team news.

A 'checks passed' status means the listed evidence checks passed. It is not a
calibrated confidence score, a complete absence assessment, or a promised edge
over Pinnacle. Numerical injury, weather, opponent-strength and other new effects
still require the agreed pre-release comparison on played matches before use.
