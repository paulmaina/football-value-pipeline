# Odds providers: pinnapi, pinnodds, then The Odds API

Built 23 Nov 2026 for Paul and **switched on the same day** (`odds_provider_config.json` `"enabled": true`), after
the live check below. Rolling back is setting `enabled` to `false`: no code change, and saved runs replay as
before. With the switch off, nothing below runs, and every output is byte-identical to before. Offline tests
always hold the switch off (`tests/offline_test_case.py` points `odds_provider.CONFIG` at a missing file); the
adapter's own tests attach their routers explicitly.

## What it does

`odds_provider.py` is one adapter that returns the same normalised Pinnacle data whatever the source:

- 1X2;
- every Asian handicap line, as the home handicap;
- every goal line, including 2.5;
- team totals;
- corners when the provider offers them;
- kickoff (UTC);
- team names mapped to our canonical names;
- the fetch time.

Each request the pipeline already makes to The Odds API goes through `OddsProviderRouter.fetch` instead. These
are the schedule, the per-league odds, the per-event extra markets and the closing collector (and, until it was
retired on 24 Nov 2026, the shadow corner list's closes).

The router asks the providers in the configured order:

| Order | Provider | Key | API |
|---|---|---|---|
| 1 | pinnapi | `PINNAPI_API_KEY` | Pinnacle kit API (`/kit/v1/prematch/fixtures`, header `x-portal-apikey`) |
| 2 | pinnodds | `PINNODDS_API_KEY` | the same kit API on another host |
| 3 | The Odds API | the existing three keys | final fallback only |

The Odds API is called for a request only when both pinnapi and pinnodds have failed for it. A failure is an
error, a timeout, a 429, the daily allowance being used up, a Retry-After still running, a key that isn't
set, or an empty answer (`empty`, since 24 Nov 2026). An answer is empty when it succeeds (HTTP 200) but holds
no fixture in the requested league and window (schedule and league odds requests), or doesn't hold the requested
event at all (per-event requests). On 24 Nov 2026 pinnapi's board held no UCL or UEL events; no other provider
was asked, so the run had no UCL fixtures and no prices. A provider that holds the event but not a requested
market has not failed: the kit API never offers some markets (double chance, draw no bet), and those requests
must not spend Odds API credits. Only The Odds API's own answer, the last in the chain, is returned empty; the
run summary counts events that no provider found.

The answer is normalised from whichever provider gave it (`normalise_kit_event`, `normalise_odds_api_event`).
It is then handed back in The Odds API's v4 event shape (`to_odds_api_event`), with Pinnacle as the only book.
The existing parsers therefore run unchanged, and identical prices give byte-identical lists through any
provider. The Odds API parser itself is untouched, so old saved runs, grading and replay read it exactly as
before.

One kit request (the whole soccer board, every line) answers every league and event for `board_ttl_seconds`
(60 s; closing requests at most 30 s). A forecast run is therefore about one kit request rather than one per
league plus one per fixture.

## Failover, daily counts and returning to pinnapi

- **Daily count.** Each kit key's daily count is tracked per UTC day against `daily_allowance` (100 on the free
  plans; `null` means no cap). Every attempt counts.
- **Retry-After.** A 429 blocks that provider until its `Retry-After` header (or `retry_after_ms`) has passed. A
  `"window": "day"` 429 blocks it until UTC midnight.
- **Across runs.** Counts and blocks are written to the usage log (`odds_api_usage.LOG`, an `odds_provider` block
  per record) and seeded from it. A closing session therefore knows what the forecast run spent today, and the
  closing collector now writes a usage line when only kit providers answered.
- **Daily projection** (reporting only, 23 Nov 2026). Each routed forecast and closing record in the usage log
  carries `odds_provider_projection`, also shown in the run summary. It projects kit requests per UTC day as
  requests per run x runs per day, for a normal day and a busy day, against pinnapi's `daily_allowance`
  (`odds_provider.daily_projection`).
  - Requests per run count both kit keys, which is what pinnapi would carry alone. A normal day uses the median
    routed run and a busy day the largest. Until a workflow has a routed run, its Odds API calls per run stand in
    as an upper bound: a routed request needs at most one board request.
  - Runs per day: forecast runs are the scheduled ones from the cron (1 a day; each manual run adds its requests).
    Closing sessions are the ones that called, taking the median day and the busiest day in the log. The busiest
    day of any weekday is used, so a busy day is at least a busy Saturday.
  - The only reader is the once-a-day UCL/UEL 48-hour step (`european_alternates.py`, plan open item 15). It runs
    only while the busy-day projection plus its own requests stays within 80 of the 100 a day. Its requests are
    inside the forecast runs' own and are also shown on their own line.
- **Back to pinnapi.** Every request starts from the first provider. The router goes back to pinnapi as soon as
  its allowance resets at UTC midnight or its Retry-After has passed.
- **Switches.** A switch is any change of serving provider, including to "none" when all three failed. It is
  recorded with its time, the providers skipped and why, and the request.
- **All three failed.** The Odds API's own error is raised as before (for example `CREDITS_EXHAUSTED`), so the
  run outcome and the failure line behave as they do today.

## Identity: one schedule per run

The run's fixture ids and team names come from whoever supplied the schedule. A later answer from another
provider is aligned to it: same league, kickoff within 5 minutes, same teams by `canonical_team_key`. The answer
then takes the schedule's id and names, so a mid-run switch never splits a fixture.

pinnapi and pinnodds share Pinnacle's event ids. When The Odds API has to price an event another provider
scheduled, it finds its own id first: from an earlier answer in the same run, or from its free events list.

Closing requests carry the saved row's kickoff and teams, so a fixture forecast under one provider closes
under another.

Team names come from reviewed aliases (`odds_provider_team_aliases.json`, per league), otherwise the provider's
own spelling. The adapter never fuzzy-matches. League mapping is by Pinnacle league name or id
(`odds_provider_config.json` `leagues`). The names there are unverified until the price check below runs with
real keys (`leagues_verified: false`).

## Provenance

Every quote records which provider supplied it (switch on only):

- **Forecast rows:** `odds_provider` (1X2, main lines), `odds_extra_markets_provider` (per-event markets) and
  `odds_schedule_provider` (fixtures), in the prediction files, `all_leagues_predictions.csv` included (the first
  two were dropped there until 23 Nov 2026). List files are unchanged: decisions carry fixed columns, so provenance
  cannot change a list (tested).
- **Saved payloads:** each payload the adapter returns carries `odds_provider`, which the parsers ignore. Closing
  observations therefore keep it with the evidence.
- **Forecast summary:** `conservative_bet_summary.json` `odds_provider` holds requests, served requests and
  failures per provider, every switch, and `first_served` (the provider that served the run's first request, and
  why any earlier one in the order did not). The run outcome and the GitHub run summary show the same (an "Odds
  providers" table).
- **Usage log:** one `odds_provider` block per forecast and closing record.
- **Model activity log:** one "Odds provider switch" line per change of serving provider, within a run and at
  run start. Each workflow (forecast runs, closing collector) is one chain: a run that starts on another provider
  than its previous run ended on gets a run-start line (`request` "run start", with the reasons), including the
  first routed run (from The Odds API) and a run with the switch off (back to The Odds API). A switch made by a
  run's first request is that run-start line, not a second one. The run being published comes from its summary;
  earlier forecast runs and the closing collector come from the usage log (source "closing odds") at the next
  forecast run. The whole usage log is read every run and ids are fixed, so nothing is logged twice. The first
  routed forecast run (23 Nov 2026, 06:15 UTC) is logged from the usage log at its own time.
- **Weekly report:** the week's file gains an "Odds providers" section: requests, served requests, failures and
  switches per provider, and Odds API credits spent that week across every workflow. Weeks with the switch off
  get no section.

`odds_source` stays "The Odds API" on priced rows: about a dozen readers use that value to mean "live
bookmaker odds were attached", so it is a marker, not a provider name. The provider is in `odds_provider`.

## What changes when it is on

| | The Odds API today | Kit providers |
|---|---|---|
| Bookmakers | Pinnacle (forecast); Pinnacle, 1xBet, bet365 (closing) | Pinnacle only, whatever the source |
| Double chance, draw no bet | yes | not offered: absent (never derived) |
| Alternate lines | Pinnacle's alternates as The Odds API lists them | every line on Pinnacle's board |
| Main line | The Odds API's `spreads`/`totals` (Pinnacle's own main line) | the most balanced pair: the live board carries no main-line flag (`is_alternate` is absent even with `line_meta=1`). It agreed with Pinnacle's main line in 94 of 106 fixtures for Asian handicap and 94 of 106 for goal lines (23 Nov 2026); otherwise it is the adjacent line |
| Quote time | Pinnacle's `last_update` per market | fetch time on a fresh board; a board flagged `stale` dates from its `last_change` (so freshness rules drop old quotes) |
| Corners | `alternate_totals_corners` (no longer requested since the shadow corner list was retired, 24 Nov 2026) | Pinnacle corner child events (`parent_id`, "(Corners)", leagues such as "Italy - Serie A Corners"); 117 on the board on 23 Nov 2026 |
| Other child events | not applicable | skipped: the board lists two specials per near-term fixture under the match's own teams and league (`parent_id` set, no draw, no lines, 750 limit); they are never a fixture |
| Odds API credit guard | applies | does not apply: the providers decide |

The odds client is still built only when an Odds API key is set (as today), so keep at least one; the
forecast and closing workflows don't start without one.

Through the adapter, The Odds API's answers are also cut to Pinnacle, so 1xBet and bet365 closing quotes stop
while the switch is on (bets are placed at Pinnacle only). Closing requests without a handicap pick still expect
1xBet quotes, so each such fixture gets its one retry (one more board request) before it is capped.

## Checks run (23 Nov 2026)

- **Switch off is byte-identical to `main`.** I ran the same mocked Odds API replies (real cached UCL payloads,
  re-stamped) through `main`'s and this branch's client, for UCL and EPL. The request URLs and parameters were
  identical, and so were the events, odds rows, per-event markets and the closing observation. Unit tests also
  check that the client has no router, no provenance columns, nothing in the summaries and nothing in the
  weekly report.
- **Identical prices give byte-identical lists through any provider.** One fixture is priced identically by
  pinnapi, pinnodds and The Odds API. The forecast quotes (odds row plus per-event markets: Asian handicap,
  price-edge, corner offers) serialise to the same bytes whichever provider serves them. The schedule's id is
  kept even when The Odds API prices a kit-scheduled fixture. The shortlist and decision files are also the
  same bytes with or without the provenance columns.
- **Failover paths:** error (HTTP 503), timeout, 429 with Retry-After (blocked, then back to pinnapi), daily cap
  (local count, and a 429 day window until UTC midnight), a mid-run switch to The Odds API keeping the schedule
  identity, reset at UTC midnight back to pinnapi, and all three exhausted (`CREDITS_EXHAUSTED`, a switch to
  none). Also a key that isn't set, a block seeded from the usage log, and closing under another provider's
  event id. Every test is in `tests/test_odds_provider.py`.
- **Cross-provider prices:** run against live data on 23 Nov 2026 in GitHub Actions (see "Live check"). The check is `scripts/odds_provider_compare.py` (tolerance 2% of the lower price, `price_tolerance` in the
  config); it reports every difference and every fixture not matched at every provider.

## Live check (23 Nov 2026, GitHub Actions)

The keys exist only as repository secrets, so the check ran in `odds-provider-compare.yml` (manual, commits
nothing) on #212's branch, three times:

| Run | Actions run | pinnapi | pinnodds | The Odds API | What it found |
|---|---|---|---|---|---|
| 1 | 45112906138 | 1 request | 1 request | 10 free events calls, 0 credits | Nine of ten league names right; Süper Lig is "Turkey - Super League" (id 2592). 38 fixtures with other team spellings. Each near-term fixture listed three times. |
| 2 | 45113356611 | 1 request | 1 request | 10 events calls; 12 odds calls, 15 credits | All ten found; every fixture outside Süper Lig matched with the new aliases. The repeats are child specials (`parent_id` set, no draw, no lines). |
| 3 | 45113640328 | 1 request | 1 request | 10 events calls; 10 odds calls, 30 credits | All ten found; all 159 board fixtures matched; repeats skipped. |

Every kit request returned HTTP 200 in under 2 s (about 2.8 MB) with no rate-limit headers, so usage is counted
from our own request log: 3 requests on each key against a daily allowance of 100.

Final results (run 3):

- **League names:** every competition is found under its configured name: EPL 21, LaLiga 21, Bundesliga 18,
  SerieA 21, Ligue1 18, Eredivisie 9, PrimeiraLiga 9, SuperLig 6, UCL 18, UEL 18 board fixtures
  (`leagues_verified: true`).
- **Team names:** all 159 board fixtures in our competitions match The Odds API's schedule (aliases in
  `odds_provider_team_aliases.json`; each target is The Odds API's own spelling for the same fixture). Two
  Süper Lig schedule fixtures (29 Nov) were not on Pinnacle's board yet.
- **Prices:** pinnapi against pinnodds, 7,751 shared prices, none outside 2%. The board against The Odds API's
  Pinnacle prices, 106 fixtures and 742 shared prices: 4 outside 2% (0.54%), all in two fixtures (largest 3.3%,
  a 14.04 against 13.59 away price), consistent with a price moving between the two fetches.
- **Main lines:** see "Main line" above: 12 of 106 fixtures differ in each market. The cagey grid's fit B uses
  the main AH line, so for those fixtures it is fitted on the adjacent Pinnacle line.

## Before turning it on

1. **Terms check.** On 23 Nov 2026 the published terms said:
   - **pinnodds:** the free key is "so you can evaluate the service before paying" ($0 to test, $99–$229 a month
     in production), and its terms forbid "use multiple trial accounts to evade limits".
   - **pinnapi:** "One account per person or company", and "Don't ... exceed your plan's rate limits".
   - **The two services:** they look like one backend (same `/kit/v1` endpoints, header, rate table and an
     identical 429 example).

   Switching from a free pinnapi key to a free pinnodds key when the daily cap runs out would breach those
   terms. The config records each key's `plan`. Use a paid plan on at least one of them (pinnapi REST or pinnodds
   Pro is $99 a month, 10 requests a second, no daily cap: set `daily_allowance` to `null`), or confirm with the
   provider.
2. Add the keys as repository secrets and pass them to the forecast and closing workflows. Done 23 Nov 2026:
   Paul added both secrets; `scheduled-forecasts.yml` and `closing-odds.yml` pass `PINNAPI_API_KEY` and
   `PINNODDS_API_KEY` as optional secrets (an absent secret is an empty key, and that provider is skipped).
3. Run the check (`odds-provider-compare.yml`, or `python scripts/odds_provider_compare.py --output <dir>
   --odds-api` with local keys). Fix the league names (`leagues_verified`) and add reviewed aliases for every
   fixture not matched at every provider. Check that the differences are within tolerance. The report lists
   them all. Done 23 Nov 2026 (see "Live check").
4. Confirm that the main-line flag (`is_alternate`) arrives on the board, or accept the most-balanced-pair rule.
   Confirm whether corner child events appear. Done 23 Nov 2026: no flag (most balanced pair, 89% agreement);
   corner children appear.
5. Set `"enabled": true` in a reviewed PR. Rolling back is setting it to `false`: no code change is needed, and
   saved runs replay as before. Done 23 Nov 2026. Item 1 was Paul's call: he added both keys and asked for the
   switch on; the config still records both keys' plans as `free` (100 requests a day each), so failing over from
   pinnapi to pinnodds on the daily cap is the case the terms check describes.

## Files

- `odds_provider.py`: adapter, router, summaries, weekly section and price check.
- `odds_provider_config.json`: the switch, the order, the keys, allowances, league mapping and tolerance.
- `odds_provider_team_aliases.json`: reviewed team-name aliases.
- `scripts/odds_provider_compare.py`: the cross-provider price check.
- `tests/test_odds_provider.py`.
