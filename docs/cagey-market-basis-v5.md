# Market-specific no-loss tier (v5)

Current rule: `no-loss-market-reference-v5`. The strict offered-price range
(1.15, 2.00], 20-minute–48-hour window, one pick per fixture/market group,
no-loss/expected-return/odds ranking, and no narrow/EV/no-loss eligibility floors
remain unchanged. Weather remains context. Main value selection is unchanged.

## Probability source, EV and stakes

Over 1.5 uses the **uncorrected Pinnacle-implied grid** from the same usable
fixture fit (B, or its existing usable A fallback). Do not fall back to the
corrected grid when this source is unavailable. The same settlement distribution
supplies ranking, positive-return probability, EV, value/below-fair flag,
cost-adjusted fair odds and advisory stakes. Its basis is
`pinnacle_uncorrected_matrix_v1`. Other cagey markets retain
`pinnacle_cagey_corrected_matrix_v1`.

V5 records source-neutral `cagey_p_*`, `cagey_no_loss_probability`,
`cagey_expected_return` and related fields. Legacy `corrected_*` figures retain
their literal corrected meaning and are not relabelled uncorrected values.
The shared readable columns use the actual chosen market source. Missing
settlement/timing means unavailable staking, never source substitution.

Corrected and uncorrected Over 1.5 probabilities, their delta, and the corrected
draw delta against fresh margin-free Pinnacle 1X2 are visible comparisons.
Narrow-margin validation is not independent validation of those totals/draw
changes. The existing grid lift need not preserve Pinnacle totals. Re-anchoring
Over 2.5 alone would not establish Over 1.5 calibration. No new coefficients,
blend or claimed accuracy gain are introduced here.

## Independent binary price check

For home/away win, use fresh proportional-margin-free Pinnacle 1X2. For double
chance use the appropriate sums of those probabilities (not margin-removing
three overlapping DC selections as though they were mutually exclusive).
For Over 1.5 use a complete fresh Pinnacle Over/Under 1.5 pair. Actual AH
-0.5/+0.5 quotes use the same 1X2 reference as their win/DC equivalents,
while retaining their AH market group and corrected settlement source.

Require acceptable overround and synchronization within ten minutes. A price
above 1.15 times this independent fair price retains the existing suspected-error
exclusion. This is a heuristic, not proof the bookmaker is wrong. Missing,
stale, future, unsynchronized or invalid references produce an explicit
`UNAVAILABLE` status and warning, not a fallback to corrected/model fair odds.
The bet still needs a valid primary distribution and offered quote. On value-list
rows these price-check fields are diagnostics only; value qualification is unchanged. Other AH
markets retain their prior corrected-fair guard.

The 67% narrow threshold remains market-specific supporting information.
Corrected-grid narrow contributions/bounds are not bounds on the uncorrected
Over 1.5 source or the value list's research model. Source labels stay visible.

V1–v4 summaries replay with their original probabilities, gates and checks.
Existing generated outputs are not hand-edited. After merge, regenerate through
the normal pipeline. See [tracking views and private placed bets](recommendation-and-bet-tracking.md).
