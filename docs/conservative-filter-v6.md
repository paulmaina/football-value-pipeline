# Conservative policy v6

Policy `72h-all-markets-ev15-one-book-v6` requires adjusted EV at least +1.5%
for every production shortlist market and at least one validated bookmaker.
Probability thresholds are unchanged:

| Market | Blended probability | Raw probability | Adjusted probability | Adjusted EV | Books |
|---|---:|---:|---:|---:|---:|
| Home win | 65% | 50% | 65% | 1.5% | 1 |
| Away win | 65% | 50% | 65% | 1.5% | 1 |
| Over 1.5 | 78% | 72% | 78% | 1.5% | 1 |
| Double Chance 1X | 80% | 75% | 75% | 1.5% | 1 |
| Double Chance X2 | 80% | 75% | 75% | 1.5% | 1 |
| BTTS Yes | 70% | 63% | 70% | 1.5% | 1 |

EV = reliability-adjusted probability × actual offered odds − 1. Inclusive
boundaries allow only a 1e-12 floating-point tolerance.

A validated bookmaker means a named source with an actual quote and complete,
plausible same-book reference market, plus the existing timestamp checks. This
change does not create a sportsbook reputation whitelist or assert that any
bookmaker's probability is truth. Unknown/incomplete/implausible/stale quotes
remain rejected. The quote-age ceiling stays 24 hours. Historical reliability,
team identification, kickoff window, raw-model EV, and winner-direction checks
remain in force. Double chance remains STRICT-only; other markets can still have
a separately labelled provisional watchlist for existing probability/history
near misses. Provisional candidates must also have adjusted EV at least 1.5%.
There is no EV relaxation below that floor.

The market-led experiment keeps its independent policy: Pinnacle reference,
3% EV, 80% probability, two independent target bookmakers, and shorter freshness
limits. Goal-blend experiments, model training, raw/blended probability generation
and archived selections are unaffected. Reports identify new production picks by
policy v6 rather than rewriting earlier policies.

Update with `git pull`, then rerun your usual pipeline command (including optional
experiment flags) and formatter. Commit/push the fresh forecast and experiment
outputs together before kickoff for automatic archive and grading. Existing
outputs are not regenerated merely by merging this code.

These user-selected thresholds permit more candidates and reduce cross-book
corroboration. They are not validated as optimal or profitable. Evaluate v6
separately from earlier policies using forward results and actual price availability.
