# Live quote freshness and reference provenance

Shortlist policy `72h-seven-markets-fresh-references-net-ev15-v11` closes
freshness gaps without changing probability, value, calibration, ranking or
bookmaker-availability thresholds. Commands and the existing experiment grids
are unchanged; no experiment is added.

Live 1X2, Over/Under 2.5, alternate totals (Over 1.5/Under 3.5), BTTS Yes and
all three double-chance markets use a shared timestamp check before choosing
offered prices or reference books. Quotes must be no more than 24 hours old
or five minutes ahead of the evaluation clock, inclusive. Missing, invalid
and expired timestamps fail closed. The existing bookmaker timestamp fallback
applies when a market timestamp is absent; one market's update never makes a
different market fresh. A complete, coherent same-book market is still required.

Reference books are ordered by UTC instant, including when timestamp strings
use different offsets. The best price retains its own bookmaker and timestamp;
another quote from a book with the same display name cannot change its age.
Freshness screening happens before devigging or using live reference prices
to construct the model's 1X2 blend. No fresh reference means no live blend.

Predictions carry `market_reference_1x2_last_update_utc`, the individual
home/draw/away reference timestamps, and reference timestamps for each quoted
goal and double-chance market. The current shortlist checks both its exact
market's reference and the underlying 1X2 blend reference, as well as the
selected offered price. Invalid references cannot be waived for the provisional
watchlist. Reporting-only markets remain reporting-only.

Archived v9 and v10 probability/calibration captures replay with their original
market sets and reference requirements. Older EV comparison ledgers and
closing-price evidence also retain their existing replay rules. No archived
forecast, selection or report input is rewritten or backfilled. Historical
model fitting, historical price parsing and the probability calculations are
unchanged; the new timing screen is applied to live ingestion.

After merging, pull and run the usual full pipeline command, or wait for the
next scheduled forecast collection. Old stored forecasts lack some required
reference timestamps and therefore cannot qualify under v11 merely by running
`refresh_conservative_shortlist.py`. That command does not fetch or invent
missing timestamps. A full fresh forecast run supplies the provenance.
