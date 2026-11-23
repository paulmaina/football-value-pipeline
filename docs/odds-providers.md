# Odds providers: pinnapi, pinnodds, then The Odds API

Built 23 Nov 2026 for Paul. **Off by default** (`odds_provider_config.json` `"enabled": false`); nothing is live.
With the switch off, nothing below runs, and every output is byte-identical to before. Turning it on is a
separate decision. It needs the checks under "Before turning it on", including the terms check.

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
are the schedule, the per-league odds, the per-event extra markets, the closing collector and the shadow corner
closes.

The router asks the providers in the configured order:

| Order | Provider | Key | API |
|---|---|---|---|
| 1 | pinnapi | `PINNAPI_API_KEY` | Pinnacle kit API (`/kit/v1/prematch/fixtures`, header `x-portal-apikey`) |
| 2 | pinnodds | `PINNODDS_API_KEY` | the same kit API on another host |
| 3 | The Odds API | the existing three keys | final fallback only |

The Odds API is called for a request only when both pinnapi and pinnodds have failed for it. A failure is an
error, a timeout, a 429, the daily allowance being used up, a Retry-After still running, or a key that isn't
set. A provider that answers without the event or the market has not failed. The request returns no quote for
it, and the run summary counts events that weren't found.

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
  `odds_schedule_provider` (fixtures), in the prediction files. List files are unchanged: decisions carry fixed
  columns, so provenance cannot change a list (tested).
- **Saved payloads:** each payload the adapter returns carries `odds_provider`, which the parsers ignore. Closing
  observations and shadow corner closes therefore keep it with the evidence.
- **Forecast summary:** `conservative_bet_summary.json` `odds_provider` holds requests, served requests and
  failures per provider, and every switch. The run outcome and the GitHub run summary show the same (an "Odds
  providers" table).
- **Usage log:** one `odds_provider` block per forecast and closing record.
- **Model activity log:** one "Odds provider switch" line per switch. Forecast-run switches come from the
  summary; closing switches come from the usage log (source "closing odds") at the next forecast run. Ids are
  the switch itself, so nothing is logged twice.
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
| Main line | The Odds API's `spreads`/`totals` | the provider's `is_alternate` flag (requested with `line_meta=1`); otherwise the most balanced pair |
| Quote time | Pinnacle's `last_update` per market | fetch time on a fresh board; a board flagged `stale` dates from its `last_change` (so freshness rules drop old quotes) |
| Corners | `alternate_totals_corners` (domestic) | Pinnacle corner child events (`parent_id`, "(Corners)") if the board carries them; not documented by either provider |
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
- **Cross-provider prices:** not run against live data. There are no pinnapi or pinnodds keys
  (`PINNAPI_API_KEY` and `PINNODDS_API_KEY` are not set locally or as repository secrets). The check is
  `scripts/odds_provider_compare.py` (tolerance 2% of the lower price, `price_tolerance` in the config). It
  reports every difference and every fixture not matched at every provider; it is tested on synthetic boards.

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
2. Add the keys as repository secrets and pass them to the forecast and closing workflows (not done here).
3. Run `python scripts/odds_provider_compare.py --output <dir> --odds-api`. Fix the league names
   (`leagues_verified`) and add reviewed aliases for every fixture not matched at every provider. Check that
   the differences are within tolerance. The report lists them all.
4. Confirm that the main-line flag (`is_alternate`) arrives on the board, or accept the most-balanced-pair rule.
   Confirm whether corner child events appear.
5. Set `"enabled": true` in a reviewed PR. Rolling back is setting it to `false`: no code change is needed, and
   saved runs replay as before.

## Files

- `odds_provider.py`: adapter, router, summaries, weekly section and price check.
- `odds_provider_config.json`: the switch, the order, the keys, allowances, league mapping and tolerance.
- `odds_provider_team_aliases.json`: reviewed team-name aliases.
- `scripts/odds_provider_compare.py`: the cross-provider price check.
- `tests/test_odds_provider.py`.
