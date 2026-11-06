# Corrected no-loss selection with narrow-margin support (v4)

Historical v4 rule retained for replay. Current selection uses
[market-specific sources and independent binary price checks (v5)](cagey-market-basis-v5.md).

Current rule: `corrected-no-loss-per-market-v4`. There is **no general P(narrow)
qualification gate**. A fixture below 67% can qualify in any supported market.
Rank actual quoted bets by corrected net no-loss probability, then expected
return, then odds; retain one per fixture/market group. The 20-minute–48-hour
window, odds (1.15, 2.00], supported markets, bookmaker/quote/fit guards, negative-EV
flags, absence of a no-loss floor, and absence of a list cap are unchanged.

The corrected Pinnacle grid and all settlement probabilities are unchanged from
v3. The main value list's research probabilities and selection are unchanged.
Weather is not an input to this selection. No master filters are introduced.

## What the 67% signal does now

P(narrow) is the corrected probability of a draw or a one-goal winning margin.
`narrow_high_67` highlights that probability >=67% as supporting information,
without excluding, weighting, promoting or demoting a bet. Support is computed
from the same corrected grid as the bet, never from an independently invented
coefficient. Nothing is added to an already computed probability.

| Market | Supplement from narrow outcomes |
| --- | --- |
| AH +1 | At zero execution cost, all narrow results avoid loss; corrected no-loss >= P(narrow). A one-goal defeat pushes, so no equivalent profit lower bound follows. |
| AH +1.25 / +1.5 (and larger plus lines) | Where every narrow settlement remains positive after cost, corrected profit and no-loss probabilities are each >= P(narrow). |
| AH -1.5 (and other minus lines where all narrow results lose) | Corrected profit/no-loss probabilities are <= 1-P(narrow). High narrow probability is a cover caution. |
| Draw / one-goal outcomes | Show corrected draw, home-by-one and away-by-one components; their sum is P(narrow). High P(narrow) alone does not say which component will happen. These informational components do not add new offered markets. |
| Home/away win, DC, Over 1.5 | No standalone directional/totals boost. Joint contributions show the part of the exact bet probability arising from narrow scores, not an additional probability to add. |

Bounds are derived using the actual line, offered price and recorded execution
cost. A push that incurs a cost is a net loss; for example AH +1 no longer gets
the universal no-loss lower bound when a one-goal defeat incurs a cost. A cost
can also consume a quarter-line half win. A missing bound is unavailable/not
implied, not zero. The exact settlement probability remains the ranking input.

## Recorded and readable information

V4 rows include `narrow_support_version: corrected-narrow-support-v1`, the
nullable high-narrow flag, a role/note, corrected draw/home-by-one/away-by-one
probabilities, and corrected narrow joint contributions and lower/upper bounds
for no-loss and positive return. Source fields use `corrected_` prefixes.

Both readable lists expose these fields with **Corrected-grid** labels where
appropriate. They describe the corrected Pinnacle model even on a value-list
row. Do not compare a corrected-grid bound as though it constrained the value
list's `team_form_poisson_v1` probability: those are different distributions.
Keep source labels when preparing a later master filter.

The run summary records `min_p_narrow: null`, `narrow_general_gate: false`, and
`narrow_supplement_threshold: 0.67`. V3 (`narrow-67-per-market-v3`) keeps its
original gate on replay; v1/v2 also retain their original behavior. Forward
tracking preserves v3/v4 rule labels and all latest-generation market groups.
No historical forecast outputs are rewritten.

This adds mathematical explanation and broader candidate coverage, not a new
claim of improved probability calibration. The corrected-margin grid lift and
expanded markets still require forward assessment.
