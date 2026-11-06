# Master shortlist: ten cautious consensus nominations (v4)

The live research rule writes master_shortlist.csv, its readable counterpart,
and master_shortlist_audit.csv. It nominates exactly ten when the union of the
two source lists contains ten executable, distinct fixtures. One market per
match. If fewer distinct fixtures pass the execution checks, return all of them
and record the numerical shortfall; never invent a match, reuse a match, accept
future/stale prices or expand the user's odds/window to manufacture ten.

This changes master nomination only. The value/cagey probabilities, qualification
and stakes are unchanged. Archived master-10-v1/v2 replay is unchanged. The
unreleased v3 proposal's 2% EV eligibility gate is replaced by this v4 nomination
rule. The new rule is unvalidated and suggested stakes are zero.

## Pool and execution

The pool is exactly the union of rows marked SHORTLISTED by either source
selector in this generation, corresponding to conservative_bet_shortlist.csv
and cagey_tier_shortlist.csv. Membership in both is a label, not an independent
confirmation or a probability bonus. Compare valid shortlisted offers before
choosing one market per fixture. A quote outside both lists is not introduced.

Require odds strictly above 1.15 and at most 2.00, kickoff 20 minutes–48 hours,
allowed bookmaker, finite cost and a unique matching frozen fixture. Identity
includes competition, canonical teams and kickoff. Offer and reference timestamps
must be observed by evaluation, at most six minutes old and synchronized within
ten minutes. Recompute ages from timestamps; do not trust stored age columns.
Replay deliberately uses the recorded clock and frozen quotes, without network
requests. A new refresh must use its new evaluation clock and new quotes.

Missing/ambiguous optional research does not invalidate an independently matched
market fixture. It is warned about and omitted from ranking scenarios. Missing
or ambiguous essential fixture identity or market references still exclude an
offer. These integrity checks are not relaxed to reach ten.

## Probability sources and comparison

The primary source for win, DC 1X/X2/12, Over 1.5 and equivalent AH half lines is
a fresh complete margin-free Pinnacle binary reference. Other AH lines require
the uncorrected Pinnacle fit B and all its fresh inputs. No corrected-grid,
research, raw goal-rate or fit-A fallback substitutes for this source.

For the same pick and offered price, compute five-way settlement and per-unit
returns: full win odds-1, half win (odds-1)/2, push 0, half loss -0.5, loss -1,
minus the recorded stake cost. Net return >0 is profit, >=0 is no loss (within
numerical tolerance). A push with nonzero cost is a net loss. Compute EV, fair
odds and the indicative minimum price for 2% net EV from these same outcomes.
Price edge and net EV are different for push/quarter markets. The independent
1.15-times-fair suspected-price check still applies.

The two lists exchange notes through additional settlement scenarios:

- Research: use its valid five-way mass only when both teams have form evidence
  and its fixture identity is not flagged missing/ambiguous.
- Corrected: use valid mass only when its recorded input timing is synchronized.
  The unvalidated totals correction is never used to rank Over 1.5; its corrected
  probability is displayed only for comparison.
- Market: always required. Missing optional scenarios produce visible warnings.

## Ranking and nomination

For each offer, retain the primary market probabilities unchanged. Separately
record the lowest no-loss probability, lowest profit probability and lowest EV
across usable scenarios, together with the exact scenario names/count. These
minima can come from different models. They are conservative sensitivity
summaries, NOT a coherent new distribution, posterior, confidence interval,
validated probability or guarantee. The models share inputs and are correlated.
No averaging weight or overlap boost is invented.

Order by lowest no-loss scenario, lowest profit scenario, lowest EV scenario,
primary market EV, then odds. Stable fixture/market/bookmaker/time keys break ties.
Choose the first offer per exact fixture, then the first ten fixtures. There is
no EV or probability eligibility floor. This prioritizes protection and cautious
agreement while allowing weak-price nominations to complete the ten.

Label every selected offer: market net EV >=2%, nonnegative market EV below 2%,
or negative market EV nomination. The 2% threshold is only an indicative price
label, not an evidence-backed universal threshold or an eligibility gate.
Negative EV remains visible; nomination does not make it a profitable value bet.
All suggested stakes are zero pending validation. No binary Kelly for AH, flat
stake on negative EV or automatic bookmaker execution is introduced.

The audit contains ELIGIBLE and EXCLUDED offers with reasons. ELIGIBLE does not
mean ultimately selected. The summary records target ten, actual count, shortfall,
value-label count, below-threshold count and negative-EV count. Readable output
shows scenario estimates separately from the primary probabilities, source labels,
coverage warnings, model disagreement, price assessment and nomination reason.

## Validation

Replay checks both master and audit fields against the frozen generation. Tests
cover ten negative-EV nominations, duplicate memberships/matches, real fit B,
partial settlement and costs, missing/future/stale quotes, optional coverage,
conservative model comparison, no unvalidated totals penalty, shortfall, formatting,
audit tampering and archived v1/v2 replay. No general narrow/weather gate is added.

Before stakes are enabled, freeze the rule and assess forward settlement calibration,
ROI with uncertainty/costs, drawdown and margin-free same-line closing value.
Historical research must have been available before prediction. Treat repeated
fixtures and shared model inputs as correlated. Ten nominations do not guarantee
that any will win or that the set has positive expected return.
