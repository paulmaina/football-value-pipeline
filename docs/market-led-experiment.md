# Market-led double-chance experiment

Enable with `--market-led-experiment`. This is a paper experiment, off by default.
It never changes baseline probabilities, the conservative shortlist, training,
goal-blend experiments or staking. Failures are isolated after baseline output
has completed. Historical backtests cannot enable it.

```powershell
git pull
py football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life --goal-blend-experiment --additional-odds-coverage all --market-led-experiment
```

For each securely linked fixture 20 minutes to 72 hours before kickoff, a separate
The Odds API event request collects `h2h,double_chance` together. This uses extra
credits and a separate one-minute cache. It retains the event response as quote
evidence. Existing production requests and their cache remain independent.

Reference: a complete, coherent Pinnacle regulation-time 1X2 quote. The power
method removes its margin; 1X = home + draw and X2 = draw + away. No other book
or model replaces a missing Pinnacle reference. Coverage and rejection reasons
are reported even if there are zero selections. Having Pinnacle in the provider's
bookmaker catalog does not guarantee it is returned for your leagues/regions.
Actual live coverage is established by running with your configured key.

Targets: real complete double-chance offers from independent sportsbooks;
Pinnacle is excluded from target prices. Betfair Exchange and Matchbook are
excluded because this experiment has no executable liquidity/commission adapter.
Use the best valid offer, and require two independent target bookmakers to select.
Matching event ID, teams and kickoff are required. Only exact regulation-time
market keys are used. Reconfirm the sportsbook's settlement terms before betting.

Quote freshness defaults: at most 10 minutes old, with at most 5 minutes between
reference and target updates. Future-dated quotes are rejected. Configure with
`--market-led-max-age-minutes` (0–60, excluding zero) and
`--market-led-max-skew-minutes` (0–max age). These are sampling safeguards;
quotes still require rechecking at execution.

Selection: reference probability at least 80%, estimated EV at least 3% after
configured costs, one market per fixture and at most ten fixtures, ranked by
reference probability then EV. No forced minimum, no provisional selections.
These are inherited probability/EV cutoffs, not a claim that existing model-based
historical validation transfers to a new strategy. The model probability, raw
probability and disagreement are recorded but do not veto the experiment.

Set `--market-led-cost-bps` for a cost charged per unit staked (100 bps = 1%).
EV = reference probability × offered decimal odds − 1 − cost.
Paper P&L = outcome × offered decimal odds − 1 − cost. Default zero means costs
are unconfigured, not that betting is costless. Profit commissions or jurisdiction-
specific tax rules need conversion or a dedicated adapter; this setting is only
an explicit per-stake cost assumption. Feed offers are labelled unverified and
may not be available in your actual account, region or desired stake size.

## Outputs and automatic evaluation

Current run: `football_output_v2/raw/market_led_experiment.json`,
`market_led_candidates.csv`, `market_led_shortlist.csv`, `market_led_report.md`.
The JSON includes timestamped source quote evidence and is bound to the exact
baseline forecast CSV by SHA-256 and generation time. Stale experimental files
from earlier runs cannot join a fresh baseline snapshot.

Commit/push the fresh baseline forecasts, summary and experimental JSON together
before kickoff. The existing forward-performance workflow captures the optional
sidecar immutably and reviews it daily with verified results. There is no new
scheduler and no automatic prediction generation: each prediction command must
include the flag. Existing result verification covers the same forecast fixtures.

Reports: `football_output_v2/performance/market_led_experiment/summary.json`,
`report.md`, `graded_probabilities.csv`, `graded_selections.csv`. These include
coverage/missing reasons, selected/graded/pending counts, paired market vs baseline
vs raw Brier scores and log losses, calibration bins, and paper flat-unit ROI
following configured costs. Paired scores use identical fixtures and require all
three probabilities. Selection ROI is separate from paired forecast coverage.
The first archived pre-match observation per fixture/market is frozen, including
missing quotes; later profitable observations cannot replace initial decisions.

A late-reference value proxy is available only if another valid archived run
contains a newer Pinnacle quote 20–60 minutes before kickoff. It is explicitly
**not true closing-line value**. This change does not schedule near-kickoff quote
collection or purchase historical odds. Missing late quotes remain null. Closing
quotes are evaluation evidence only and never influence earlier selections.

No automatic promotion occurs after four weeks or at any sample count. Outcomes
remain inconclusive pending review of coverage, sample size, calibration, costs
and execution assumptions. Four weeks alone cannot establish profitability.
