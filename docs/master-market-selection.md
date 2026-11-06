# Master shortlist: market value and protection (v3)

The live research rule writes `master_shortlist.csv`, its readable counterpart,
and `master_shortlist_audit.csv`. It selects **up to ten**, one market per exact
fixture. Zero is valid. Negative-EV or unsupported candidates never fill a quota.
This changes master selection only; value/cagey model probabilities, their own
qualification, and their stakes are unchanged. Recorded master-10-v1/v2 runs
retain their original replay rules.

## Candidate pool and execution

The pool is exactly the union of rows marked SHORTLISTED by the value or cagey
selector in this run, corresponding to conservative_bet_shortlist.csv and
cagey_tier_shortlist.csv. Duplicate membership is a label, never extra evidence.
Choose the best eligible offered price among these shortlisted offers for the
same outcome, then one market per fixture. A quote not in either list is not
introduced. Fixture identity includes competition, canonical teams and kickoff.

Require odds strictly above 1.15 and at most 2.00, kickoff 20 minutes–48 hours,
allowed bookmaker, finite stake cost, and a unique matching frozen fixture.
Offered and reference timestamps must be observed by evaluation, at most six
minutes old, and synchronized within ten minutes. Stored age columns are not
trusted. An explicitly new evaluation time rejects old generations; refreshing
stored predictions must collect new offers through the normal workflow first.
Archived replay deliberately uses the recorded generation clock, without web
requests or future information. Ambiguous research fixture identity fails closed.

## One consistent probability source

Win, DC 1X/X2/12, Over 1.5 and equivalent AH half lines use a fresh complete
margin-free Pinnacle binary reference. Other AH lines use the uncorrected
Pinnacle fit B, with all its inputs checked. No corrected-grid, raw goal-rate,
research-model or fit-A fallback substitutes for a missing source.

Compute five-way settlement at the actual offered price: full win, half win,
push, half loss, loss. Per-unit returns are odds-1, (odds-1)/2, 0, -0.5, -1,
minus the recorded cost. Profit means net return >0; no-loss means >=0 (within
numerical tolerance). A push with a nonzero cost is a net loss. Price edge is
shown separately from net EV; they are not generally equal for handicap lines.
Minimum qualifying odds are solved from this same distribution and cost.
Reject prices above 1.15 times the independently reconstructed fair price.

## Qualification, ranking and uncertainty

Require net EV >=2%. **This is a provisional policy buffer, not an empirically
validated error margin or confidence bound.** The source probabilities and the
selection rule do not constitute guaranteed win rates. Corrected/research
profit probabilities and disagreement are diagnostics only; no fixed blend or
probability bonus is invented. Missing context and disagreement remain visible.
No general P(narrow) gate or weather coefficient is added.

Rank by no-loss probability, then probability of positive return, then net EV,
then offered odds; stable fixture/market/bookmaker/time keys break ties. Choose
one market per fixture and at most ten fixtures. In the audit file, WATCHLIST
means the reference was usable but the net-EV buffer was not met; EXCLUDED
records missing execution evidence or invalid/suspect input. ELIGIBLE is an audit
eligibility status, not proof that the offer was ultimately selected.

All suggested master stakes are zero until promotion. No automatic betting,
binary Kelly formula for AH, or flat stake on negative-EV watchlist picks is
introduced. The existing private placed-bet ledger records actual bets separately
from hypothetical captured recommendations. The normal snapshot/tracking path
continues to retain and grade master selections at their captured prices.

## Validation and promotion

Workflow checks reconstruct both the selected file and full audit from frozen
predictions and decisions, comparing all fields. Test partial settlement, cost,
missing references/times, future data, exact identity, best price, one-per-match,
empty output, the ten-row cap, old replay, formatting and audit tampering.

Before enabling stakes, choose thresholds only on development data in time order;
freeze the rule and assess untouched audit/forward runs. Historical research must
be demonstrably available before the prediction. Report settlement calibration,
ROI with uncertainty and costs, drawdown and margin-free same-line Pinnacle CLV.
Treat repeated fixtures and overlapping sources as correlated. Do not promise a
promotion after a fixed number of bets, and do not tune the buffer on today's list.
