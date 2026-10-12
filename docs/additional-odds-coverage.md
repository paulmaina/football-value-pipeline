# Additional odds coverage

The default `--additional-odds-coverage all` requests additional markets for
**every The Odds API-linked fixture in the conservative shortlist window**
(20 minutes to 72 hours before kickoff). Each event request includes double
chance, alternate totals and BTTS. Existing caches still apply.

Previously, 24 event requests were split equally across the six leagues.
When UCL had all 18 in-window fixtures, it received only four requests;
14 fixtures (28 double-chance candidates) remained unpriced despite unused
allocations in other leagues. Full coverage removes both this quota and the
model-probability prefilter from price collection. It uses more API credits.

Use your usual command after updating, or explicitly add:

```powershell
--additional-odds-coverage all
```

For the previous limited-credit behavior, use `--additional-odds-coverage ranked`.

Each league diagnostics JSON includes `additional_odds_coverage`, with an entry
per fixture: requested event ID, quote availability and status. Statuses distinguish
valid double-chance quotes, a response without valid quotes, request failure,
and requests skipped due to unavailable API, ranking/budget, or window/linkage.
`additional_odds_unrequested_linked_fixtures` counts eligible fixtures not requested.
Budget and quota fields are null when full coverage disables those caps.

Full coverage guarantees requests for linked eligible fixtures when the API is
configured, not that bookmakers offer every market. Missing/invalid prices stay
missing; no synthetic double-chance odds are substituted. Quality, freshness,
bookmaker-count, validation and EV requirements for shortlist inclusion are
unchanged. Existing forecasts and archived results are not rewritten.
