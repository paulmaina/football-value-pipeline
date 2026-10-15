# BTTS in the conservative shortlist

Policy `72h-seven-markets-dc12-btts-probability-odds-net-ev15-v10` adds
**Both Teams to Score - Yes** to the existing six markets. It restores the
existing BTTS thresholds: at least 70% model probability, 63% raw Dixon-Coles
probability and 70% reliability-adjusted probability. Adjusted EV after
configured costs must be at least +1.5%, and raw-model EV must be nonnegative.

BTTS uses the same historical reliability and high-confidence audit gates,
development-only calibration adjustments, bookmaker allowlist, complete
same-book Yes/No reference prices, quote freshness, team matching and kickoff
window checks as the other goal markets. Missing evidence remains a rejection.
BTTS No is not added: the current quote and validation path supports BTTS Yes.

Qualifying BTTS competes by adjusted probability, then offered odds and adjusted
EV. Only one market per fixture can be selected, with at most ten fixtures in
the next 72 hours. Existing provisional watchlist rules remain separately
labelled; a provisional row is not a strict qualifier.

The existing EV and probability/calibration comparisons include BTTS in new
captures; their grids are unchanged and no experiment is added. Six-market v9
captures replay with their original market set and rankings. Earlier EV
comparison captures also retain their original market sets. Archived results
are not rewritten or backfilled. Reports retain each selection's policy version
so the change can be identified during review.

After merging, pull and run the usual pipeline and formatter, or allow the
next scheduled forecast run to generate fresh outputs. Old output files do
not acquire BTTS selections merely because the code changes.
