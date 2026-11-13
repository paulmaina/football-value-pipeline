# Odds API credits

Since 9 Nov 2026, every scheduled forecast run failed. All three keys
(`THE_ODDS_API_KEY`, `_FALLBACK_1`, `_FALLBACK_2`) are free 500-credit keys,
and each returned `OUT_OF_USAGE_CREDITS` (provider status of 8 Nov: used 500,
500 and 499). The football-data.org fallback found only already-started matches
during the international break, so the raw check stopped with "No forecast rows
to capture". This page records what each workflow costs, what was cut, and how
usage is now recorded and guarded. Predictions, probabilities and shortlist
logic are unchanged.

## Pricing (The Odds API v4)

| Endpoint | Cost |
|---|---|
| `/sports/{sport}/events` | free |
| `/sports/{sport}/odds` | markets × regions; nothing if no event is returned |
| `/sports/{sport}/events/{id}/odds` | unique markets **returned** × regions |

Up to 10 bookmakers named in `bookmakers=` count as one region. Every request
here names Pinnacle (closing adds 1xBet and sometimes bet365), so each call
costs one credit per market.

## Calls per workflow

| Workflow (cron) | Calls per run | Credits per call |
|---|---|---|
| Scheduled forecasts (`45 5 * * *`, plus a push trigger and manual runs) | 10 × events (free); 1 × `/odds` per league with fixtures in 3 days; 1 × event odds per linked fixture in the 24 h window | `/odds` h2h, totals, spreads = 3; event odds alternate_totals, alternate_spreads, draw_no_bet, double_chance = up to 4 |
| Closing odds (`52 5-21 * * *`, `7,22,37 6-21 * * *`) | 1 event-odds call per fixture inside 6 min of kickoff, repeated every 30 s while a required quote is missing | h2h + totals = 2; + alternate_totals, btts, double_chance, spreads/alternate_spreads/draw_no_bet by pick = 2 to 7 (2.98 average over 164 logged requests) |
| Price checks (hourly, off: `PRICE_CHECKS_ENABLED` unset) | 1 × `/odds` per league with a fixture in 24 h | 3 |
| Europa production check / access audit (manual only; last run 22 Oct) | ≤ 1 `/odds` + 1 event odds | ≤ 7 per manual run |

## What the pipeline needs, and what it fetches beyond that

Needed, as decided earlier: Pinnacle 1X2, totals, the main AH line, and double
chance and draw no bet for AH pricing. BTTS and corners were already dropped.

Fetched beyond that list, but read by current outputs, so **not** cut here:

- `alternate_totals`: Pinnacle's exact 2.5 pair anchors the totals model when
  the main line is not 2.5. In five recent runs that was 187 of 330 fixtures
  (`ANCHORED_ALTERNATE`), so dropping it changes predictions. It also prices
  Over 1.5 / Under 3.5 and price-edge quotes.
- `alternate_spreads`: AH lines other than the main one feed every handicap
  candidate line (−3 to +3) on the shortlist, cagey tier and master list.

Together they are half of each per-event call (about 2 × 4 credits per in-window
fixture, roughly 40% of forecast credits). Cutting them is a production change
and needs a candidate through the release gate in `docs/plan.md`.

Regions, bookmakers and leagues: none is wasted. The bookmaker filter already
makes every call one region, and all ten leagues produce predictions.

## Measured monthly credits

Measured 17 Oct – 8 Nov 2026 (23 days) from the committed diagnostics of every
forecast run (`additional_event_odds_calls_this_league`, `live_odds_matched`) and
the closing request budget, scaled to 30 days. Per-call costs are upper bounds
(4 per event call; an event call costs only the markets returned).

| Workflow | Before | After this PR |
|---|---:|---:|
| Scheduled forecasts | 5,056 (32 runs: ~1.4 a day) | 3,885 (one run a day, 130 average) |
| Closing odds | 2,099 (540 requests) | ~906 (~233 requests) |
| Price checks | 0 (off) | 0 (off; 2,119 if enabled at 4 h) |
| Europa checks | 0 | 0 |
| **Total** | **~7,150** | **~4,800** |

Check against reality: the same costs give about 2,450 credits for 1–8 Nov,
more than the 1,500 that three free keys hold. So either the per-call upper
bounds overstate cost (an event call costs only the markets returned), or the
keys reset on different days. The usage log below now records the true cost of
every call (`x-requests-last`), so the next month gives exact figures.

## Waste cut

1. **Scheduled forecasts no longer run on push.** A change to the workflow or
   `publish_scheduled_forecasts.py` on main started a full run (up to ~300
   credits). Of 32 runs from 17 Oct to 8 Nov, 14 were second or later runs on
   the same day. Manual `workflow_dispatch` is unchanged.
2. **Closing odds stop retrying quotes that cannot arrive.** Of 199 fixtures
   collected from 17 Oct to 8 Nov, 34 were requested 2–12 times (about 300 of
   472 calls), and no retry added a single quote:
   - 27 had a handicap pick, so the request asked for Pinnacle only, yet the
     completeness check still expected 1xBet quotes. It now expects only the
     bookmakers requested.
   - 7 wanted a Pinnacle line its alternate totals did not offer (Over 1.5).
     A fixture is now requested at most twice per pre-kickoff window (one retry
     for a quote stale on the first try).

## Usage record

Each Odds API response's `x-requests-remaining`, `x-requests-used` and
`x-requests-last` are read per key slot (`odds_api_usage.UsageLedger`, through a
response hook in `CachedHttpClient`). No key value, URL or response text is kept.
Each run that calls the API:

- writes a table of the credits left per slot to the run summary;
- appends one JSON line to `football_output_v2/odds_api_usage/usage_log.jsonl`
  (workflow, outcome, calls and credits by endpoint, per-slot remaining/used,
  total known remaining), committed by the scheduled forecast, closing odds and
  price check workflows.

## Outcomes and the budget guard

- **No fixtures in the window** (an international break): the run finishes
  green with "No fixtures in the next 3 days; nothing to forecast" in the run
  summary. Nothing is published except the usage log line. If the keys are also
  out of credits, the summary says so but the run stays green: no forecast
  needed odds.
- **All keys out of credits** while fixtures exist and no forecast received
  Odds API prices: the run fails with one line, "Odds API credits exhausted on
  all keys; forecasts not produced", in the run summary and as an error
  annotation, with no traceback. No forecast is published; the usage line is
  committed. If credits run out mid-run after some leagues were priced, the
  priced forecasts are published and the summary notes the shortfall.
- **Budget guard** (`FORECAST_RUN_CREDITS = 300`, the largest measured run of
  288 plus margin): when the known credits on all keys fall below one forecast
  run, optional calls are skipped first so the core forecast (one `/odds` per
  league, 30 credits) can still run:
  - per-event extra coverage (status `NOT_REQUESTED_LOW_CREDITS`; those
    fixtures fall back to the main line);
  - price checks (`SKIPPED_LOW_CREDITS`, no request);
  - closing quotes for fixtures without a pick (picks are still collected).

  Balances come from this run's headers, seeded from the committed log. An
  unknown balance never blocks a call.

## Plan recommendation

About 4,800 credits a month after this PR, plus ~175 per manual rerun. The
**20K plan (20,000 credits, $30/month)** covers that about four times over,
leaving room for manual reruns, the price checks at a 4-hour interval (+2,119)
and a heavy fixture month. The 100K plan ($59) is not needed. Use one paid key
in `THE_ODDS_API_KEY`: the client's own note says the fallback slots are for
provider-authorized redundancy, not for pooling free accounts.
