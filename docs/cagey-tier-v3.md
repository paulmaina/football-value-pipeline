# Cagey tier: narrow-67-per-market-v3

The current cagey list uses a corrected Pinnacle-implied distribution and ranks
by the probability of avoiding a net loss (including pushes when execution cost
is zero). It is independent of the research-probability value shortlist.

- Kickoff: inclusive 20 minutes to 48 hours after evaluation.
- Corrected P(narrow) >= 67%: a draw or either side winning by exactly one goal.
- Actual quoted home/away win, double chance 1X/X2/12, Asian Handicap (either
  sign, any supported quoted line), and Over 1.5. No invented offered odds.
- Offered decimal odds strictly above 1.15 and at most 2.00.
- One pick per fixture and market group: match winner, double chance, AH, totals
  Over 1.5. An actual AH +/-0.5 remains in AH, not its equivalent win/DC group.
- Rank by corrected no-loss probability, then net expected return, then odds.
  There is no EV floor, no no-loss floor, no fixed number of fixtures or picks.
  Negative expected return remains eligible and is flagged.
- Existing bookmaker allowlist remains in force. Require valid Pinnacle inputs,
  acceptable overrounds/fit, fresh pre-cutoff quotes, and synchronization within
  ten minutes. A price above 1.15 times corrected gross fair odds remains a
  suspected-price-error exclusion. Missing distribution means unavailable,
  without a fallback to the research model or a different probability source.
- Weather, injury headlines and research coverage do not alter cagey selection.

## One coherent distribution

Use the existing corrected margin masses from the Pinnacle-implied fit B, or
its usable fit A fallback when B is unavailable. For margin d, multiply every
original grid cell with home-away=d by corrected_mass(d)/original_mass(d).
This preserves the conditional score distribution within each margin and exactly
reproduces the corrected margins. Reject mass outside the original grid support.

The margin correction alone does not uniquely determine total goals. The
within-margin preservation above explicitly defines how the corrected full grid
prices Over 1.5. Win, double chance, quarter-line AH, expected return and stakes
use that same distribution. In this new cagey tier, minus lines and match-winner
markets also use the corrected distribution, as requested. Legacy value-tier
fair-reference behavior and the main research shortlist's probabilities are
unchanged. The historical correction gate is not a new validation of Over 1.5
or of this expanded selection policy; forward tracking must assess those markets.

Net returns are price-1, (price-1)/2, zero, -0.5 and -1 minus the recorded stake
cost. A cost can turn a push into a small net loss. Labels and probabilities
therefore consistently describe net no-loss and positive return at that cost.

## Comparable output columns

Both raw lists add `shortlist_schema_version: comparable-shortlist-v1` and share:

| Fields | Meaning |
| --- | --- |
| fixture_key, market_to_bet, value_market_group, bookmaker, offered_decimal_odds | Stable fixture identity and actual offered selection; join on fixture plus market/bookmaker, not team names alone |
| shortlist_source, selection_rule, selection_objective, source_probability_basis | Keep the source and objective visible when lists overlap |
| settlement_p_win/half_win/push/half_loss/loss | Full settlement distribution from that list's own probability basis |
| chance_of_positive_return, chance_of_no_loss | Probabilities after the same recorded execution cost |
| expected_return_after_cost, fair_odds_after_cost, model_price_edge, price_assessment | Comparable expected return, break-even price and edge; negative EV flagged |
| p_narrow | Corrected Pinnacle P(narrow), where available; a gate only for cagey |

The corresponding readable columns use identical names, order and formatting in
both CSVs. Additional form/coverage/news fields remain on the value list; cagey
keeps its overlap label. Source-specific legacy columns remain in raw files for
replay compatibility. Harmonizing labels does not replace one list's probabilities
with the other's: value uses unvalidated team_form_poisson_v1; cagey uses
pinnacle_cagey_corrected_matrix_v1. Advisory cagey stakes use the complete corrected
settlement, including binary markets. Missing settlement stays unavailable.

Older value-v1 and narrow-63-flagged-v2 summaries retain their rules and original
CSV layouts on replay. Tracking preserves the new rule label and all market groups
from the latest pre-kickoff generation of a fixture, without carrying an older
market group forward when it disappears. Master-list filters are not changed by
this release. The common fields support a future explicit master policy; overlap
alone is not evidence of independent agreement.
