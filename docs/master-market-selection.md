# Master shortlist: ten profit-first nominations, no DC or Over 1.5 (v7)

The live rule writes master_shortlist.csv, its readable counterpart and
master_shortlist_audit.csv. Nominate ten when the two source shortlists contain
ten executable distinct fixtures. One market per exact fixture. If fewer pass,
record the numerical shortfall; never invent/repeat matches or accept invalid
inputs to fill ten. No minimum EV or probability gate is added. Negative EV is
labelled and all suggested stakes remain zero while the rule is unvalidated.

## Native AH replacements for Pinnacle multi-bets

The live v7 master retains v6’s exclusion of Double Chance offers. A nominated DC 1X outcome
may nominate home AH +0.5; X2 may nominate away AH +0.5. These are equivalent
regulation-time outcomes, but their bookmaker prices need not be equal. Only an
actual, complete, valid Pinnacle spreads/alternate-spreads quote for the right
side and +0.5 line can replace a DC offer. Never reuse a DC price, other-book
quote, draw-no-bet line, inferred price or relabelled DC record.

Each replacement passes the existing odds, freshness, synchronization, fixture,
price-error and cost checks. Recompute fair-price comparison and EV at its actual
AH quote, then compete with the fixture's other nominated markets. Provenance
columns retain the original nomination, bookmaker/price, replacement reason and
actual offered market type. Source-membership flags identify the originating
nomination; they do not claim the substituted AH quote appeared in a source CSV.

DC 12 (either team wins, excluding a draw) has no equivalent single AH line and
is excluded. If a replacement is absent, stale or invalid, exclude that offer
and select another eligible market/match if possible. Preserve one bet per match,
target ten and an explicit shortfall rather than inventing unavailable bets.
The DC replacement itself does not alter source value/cagey selection or staking. The master
exception to its original-offer-only pool is limited to these equivalent 1X/X2
nominations with genuine Pinnacle AH quotes from the same frozen fixture.

## Explicit version and one generation clock

master_shortlist_config.json explicitly selects the live version. A missing or
invalid config is an error; presence/absence of research columns never selects
a version. Archived replay uses the immutable recorded version and ignores live
config. Archived master-10-v1/v2 and released master-profit-market-v5/v6 behavior/schema are unchanged. The unmerged PR's v3/v4
proposals were superseded by v5; v6 added DC removal and v7 excludes Over 1.5. No production runs used those proposals.

Before any master/audit file is written, generated_at_utc must equal every
nonempty decision row's evaluated_at_utc. Invalid, mixed or mismatched clocks
raise an error rather than silently publishing an empty shortlist. Workflow
replay checks the same invariant and derives evaluation from those same rows.
Replay uses frozen inputs without network calls or future information. A new
refresh must use its new generation time, not reset ages to the fetch time.

## Candidate pool and integrity

Take only offers marked SHORTLISTED by value or cagey selectors in this run,
corresponding to conservative_bet_shortlist.csv and cagey_tier_shortlist.csv.
Membership in both is a label, not independent confirmation or a probability
bonus. Never introduce an unshortlisted line. Compare valid offered prices and
choose one market per fixture, then the first ten fixtures. The explicit DC-to-native-AH replacement above is the only extension to those nominated outcomes.

Require odds strictly above 1.15 and at most 2.00; kickoff 20 minutes–48 hours;
allowed bookmaker; finite cost; and unique matching frozen fixture identity
(competition, canonical teams and kickoff). Essential market/fixture information
is mandatory. Missing optional research produces visible coverage warnings.

Offered quotes and every input to the market reference must be observed by the
generation clock and no more than 15 minutes old, inclusive. Future timestamps,
missing timestamps and quotes over 15 minutes old remain excluded. Reference
and offered/input quotes must still be synchronized within ten minutes.
The 15-minute allowance prevents collection runtime from discarding otherwise
usable snapshots; it does not establish that a price remains executable now.

Expose offered/reference ages in minutes, freshness status, and a mandatory
re-check-price indicator for every nomination. Snapshots over six minutes old
receive an additional RECHECK_PRICE warning. Re-check the exact line and price
before placing any bet. Capture/evaluation times are never relabelled to make
old information appear fresh.

## Probability and settlement

Win, DC 1X/X2/12, Over 1.5 and equivalent AH half lines use a fresh complete
margin-free Pinnacle binary reference. Other AH lines require the uncorrected
Pinnacle fit B and all its fresh inputs. No corrected-grid, research, raw-rate
or fit-A fallback replaces a missing primary reference.

Calculate five-way outcomes at the quoted price: full win returns odds-1,
half win (odds-1)/2, push 0, half loss -0.5, full loss -1, less recorded cost.
Positive net return is profit; zero is a refund; negative is loss. A cost-bearing
push is a net loss. No-loss probability remains visible but refunds never count
as profitable outcomes. EV, fair odds and the indicative price for 2% net EV use
this same settlement distribution. Price edge and net EV differ on AH lines.
The independent 1.15-times-fair suspected-price-error check is retained.

## Common-basis ranking

Rank every candidate by:

1. Pinnacle-referenced probability of a positive net return, descending.
2. Market net expected return, descending.
3. Market no-loss probability, descending.
4. Offered odds, descending; stable fixture/market/bookmaker/time keys break ties.

Apply this order to choose one market per fixture and then ten fixtures. A
refund-heavy whole-line AH cannot outrank a higher profit-probability bet merely
because it has more pushes. Changing optional model availability or estimates
does not change this order. Thus missing evidence cannot gain an advantage from
having fewer scenarios over which a minimum is taken.

Research/corrected settlement estimates, model gaps, available scenario sources
and minima remain DIAGNOSTICS ONLY. They are neither blended nor used as ranking
penalties/bonuses. No unsupported missing-data penalty is invented. Research
comparisons require both teams' form and unambiguous research identity;
corrected comparisons require synchronized input timing. Corrected Over 1.5 is
displayed for comparison, never used to price/rank totals. Missing or disagreeing
models generate warnings for human review, not calibrated confidence claims.

## Reporting, stakes and validation

Label market EV >=2%, nonnegative EV below 2%, or negative market EV nomination.
The 2% figure is an indicative price label, not an eligibility threshold. Ten
nominations do not establish positive portfolio EV or guaranteed wins. Suggested
stakes stay zero; no automatic betting or binary Kelly for AH is introduced.
The v5 master rule itself does not change value/cagey probabilities, qualification
or staking. The later live market exclusion is described below.

The audit records ELIGIBLE/EXCLUDED offers and reasons; eligibility does not mean
ultimately selected. The summary records target, actual count, shortfall and
negative-EV count. Workflow replay compares every selected/audit field. Tests
cover profit vs push ranking, identical ranking with/without optional models,
15-minute boundaries and future rejection, explicit config and config-independent
replay, clock mismatch before writing, ten nominations, shortfall, exact partial
settlement/costs, missing references, formatting and audit integrity.

Before enabling stakes, freeze the rule and assess forward profit calibration,
ROI with uncertainty/costs, drawdown and same-line margin-free closing value.
Historical research must have been available before prediction; repeated fixtures
and shared model inputs are correlated. No new narrow/weather gate is added.

## Current live exclusion: Over 1.5

The live source configuration records `excluded_markets: ["Over 1.5"]`.
Value and cagey tiers reject these candidates before selecting their market-group
winners. The strict-qualifier and readable exports inherit the exclusion.
Master rule `master-profit-no-dc-no-over15-v7` also rejects Over 1.5 defensively,
even if passed an older source shortlist. The existing DC-to-native-Pinnacle-AH
replacement rule continues to apply; other eligible markets compete for ten
distinct fixtures, with a visible shortfall when fewer are available.

This is a market eligibility change, not a probability-model change. Full match
forecasts, score grids, research probabilities and quote capture still retain
totals information. No historical picks are erased or left ungraded. Archived
source runs without an exclusion setting retain their original markets, and
master v5/v6 replay uses the original selectors. New outputs are regenerated by
the scheduled pipeline after merge; committed forecast files are not hand-edited.
