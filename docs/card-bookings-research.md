# Card bookings research (free plan, not production)

Card totals stay out of production (`count_markets.CARD_SETTLEMENT_GAP`). This study tests whether a booking total that matches Pinnacle's settlement can be rebuilt and validated. It uses the API-Football free plan only.

## Settlement rule

`card_bookings.booking_points` scores each player: a lone yellow is 1, and any dismissal is 2 plus 1 if a yellow preceded it. This matches Pinnacle's booking total (yellow 1, red 2, the second yellow of a dismissal excluded). API-Football records a second-yellow dismissal as two `Yellow Card` events plus a `Red Card`; both encodings settle the same.

A match is flagged and gets no total if any card is:
- after 90 minutes plus second-half stoppage;
- missing a player or team identity;
- of an unknown type;
- a second yellow without a dismissal.

Card participation cannot be checked without line-ups, which would cost another request per match.

## Data

- **Scope:** Bundesliga, Serie A and Ligue 1, seasons 2022-23 to 2024-25 (the free plan's 2022–2024 start years). Pinnacle quoted card totals only in these leagues. 3,033 of 3,050 football-data.co.uk matches link to an API-Football fixture (date within a day, identical score, similar names).
- **Collection order:** every red-card match (508 linked), then a fixed sample of 50 red-free matches per league to test the shortcut. That is 658 `/fixtures/events` requests, cached in `.football_cache/api_football/card_events/` (local, not committed).
- **Pace:** at most 80 requests a run, leaving room in the shared 100-a-day allowance. About nine daily runs complete it.
- **Where it runs:** the `Card bookings research (free plan)` GitHub workflow (`.github/workflows/card-bookings-research.yml` on `main`) runs daily at 07:47 UTC, plus manual dispatch. It checks out this branch, uses the `API_FOOTBALL_KEY` secret, and shares a concurrency group with the supplementary API-Football collector. Events persist in the Actions cache, not the repository. When collection completes it runs the study once, comments the summary on the draft PR, uploads the full study as an artifact and disables itself.
- **Running it locally instead:** `python card_bookings.py`; check progress with `--plan-only`.

## Study

`python card_bookings.py --study <file outside git>` makes no requests.

1. **Shortcut check:** red-free matches use football-data.co.uk yellows only if every sampled red-free match agrees exactly with its events. Otherwise the shortcut is refused and every match would need events.
2. **Completeness:** every red-card match needs clean events; until then the study reports progress and does not validate, because dropping red-card matches would bias totals down.
3. **Validation:** the booking total replaces the card total in `count_markets`, with the same features, NB2 fit, walk-forward windows and reliability thresholds, per league, line and side.

## Limits

- Three seasons instead of six.
- No current-season events on the free plan, so live card picks could not be graded. Cards therefore stay out of production whatever the study shows.
- Validation covers probability accuracy only; no historical card odds exist.
