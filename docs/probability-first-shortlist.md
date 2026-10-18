# Probability and EV shortlist

Production policy `48h-top-ten-probability-ev-no-under35-v14` ranks ten distinct upcoming
fixtures using both adjusted probability and adjusted EV, across all requested
leagues. No fixed probability or EV cutoff is required for selection.

## Combined rating

1. Evaluate usable fixture-market candidates with valid model probabilities,
   identities, fresh allowed-bookmaker prices and coherent reference markets.
2. Deduplicate repeated provider rows by fixture and market.
3. Calculate the percentile rank of adjusted probability and of adjusted EV
   across this candidate pool. Tied values receive the average rank.
4. Score each candidate as `0.5 * probability percentile + 0.5 * EV percentile`.
5. Choose each fixture's highest-scoring market, then the top ten fixtures.

Equal weights give both criteria influence without letting an extreme EV value
dominate because of its numeric scale. They are an explicit policy choice, not
an optimized or proven profitable weighting. Scores are relative to the candidates
available at generation time, not win probabilities. The report shows a combined
score out of 100 and both percentile components.

Ties use adjusted probability, adjusted EV, quoted odds, kickoff, league and team
names in that order. Strict qualification does not take priority over a better
combined score. Underlying prediction probabilities and model fits are unchanged.

Markets are home win, away win, Over 1.5, BTTS Yes and double chance
1X/X2/12. Each fixture contributes one market; no same-fixture stacking.

## Eligibility and warnings

The rolling window ends 48 hours after generation, inclusive. The existing
20-minute minimum kickoff lead, allowed-bookmaker policy, valid team mappings,
real exact-market quotes and reference-market freshness/integrity checks remain.
If fewer than ten distinct fixtures have usable data, the summary records the
available count and a shortfall rather than fabricating matches or prices.

Legacy probability, adjusted EV, raw EV and historical-audit thresholds annotate
qualification instead of eliminating usable candidates. `STRICT` means those
reference rules also passed. `PROVISIONAL` means at least one failed; the report
shows why.
Unassessed calibration is disclosed; invalid calibration data is rejected.

Negative EV remains possible because there is no EV floor; high EV with a lower
win probability is also possible. The rating balances the two criteria without
guaranteeing a minimum for either. Ten selections do not establish accumulator
safety, prediction accuracy or profitability.

## Commands and historical evidence

The prediction command is unchanged. To re-rank stored forecasts without API
calls: `py refresh_conservative_shortlist.py --root football_output_v2`.
This uses saved probabilities and prices; it does not fetch fresh odds.

Historical v9-v11 strict policies and the v12 72-hour probability-first policy
and the v13 balanced policy replay with their original rules, including their
original market sets. New captures identify v14 explicitly. Under 3.5 is excluded
from the new shortlist and percentile pool; its model forecasts and historical
evaluation remain available. EV
sensitivity v3 compares the combined-score control (`No EV gate`) with +1.5%,
+3% and +5% EV-filtered alternatives. Percentiles use the same underlying valid
candidate pool before experimental EV gates, keeping scores comparable.
Older experiment grids and immutable forecasts, prices and selections are not rewritten.
