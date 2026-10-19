# Data, model and workflow review — 19 October 2026

The current sources support score-based forecasting. The review found two
confirmed odds-collection defects, incomplete runtime provenance and health
visibility gaps. It does not establish optimal forecasting accuracy.

## Confirmed defects and fixes

1. **Production extra-odds fetching used the legacy 72-hour window.** The current
   shortlist uses 48 hours. Nine production event requests in the last uploaded
   run were for fixtures between 48 and 72 hours away. Fetching now uses the
   current balanced-policy 48-hour constant. Legacy shortlist replay retains 72
   hours. The separate market-led research experiment keeps its existing window.
2. **Confirmed exhausted keys were retried throughout a prediction run.** After
   every configured credential explicitly reports OUT_OF_USAGE_CREDITS, this
   client instance now blocks further live requests. Valid fresh cache reads
   still work. New credentials, a new UTC day or a new client permit recovery.
   HTTP 429 alone does not create this terminal credit lockout. Safe provider
   classification is persisted in forecast diagnostics and surfaced in reports.
3. **Runtime provenance covered the main script but omitted important helpers.**
   New run metadata adds normalized hashes for model, scoring, data, identity,
   quote and shortlist helpers/configuration, plus the RapidFuzz version. Old
   immutable captures remain unchanged; provenance is not retroactively invented.
4. **Health reports lacked current shortlist activity and forecast-age fields.**
   Reports now count past/upcoming/unknown kickoffs, show generation age, and
   warn when future forecasts are old or the stored shortlist is exhausted while
   future fixtures exist. A normal settled-only historical cohort is not flagged
   as an active forecast outage. Confirmed quota failures at forecast generation
   also become visible report warnings, not a claim about today's account balance.

## Data and numerical checks

- All thirty domestic CSV Git blob hashes matched current main.
- All twelve latest combined-dataset checksums passed; all six enriched CSVs had
  unique match identities. The combined snapshot has 6,136 rows; older domestic
  CSVs are reconciled at load time. The next BBS export can include those rows.
- All 81 stored forecasts had finite valid 1X2 and double-chance probabilities,
  correct probability totals, no duplicate fixture identities and valid checked
  goal-market ordering. No Under 3.5 selection was present.
- Offline score-only fits succeeded for all six competitions using the staged
  six-season domestic source plus verified BBS result additions. All 81 resulting
  score grids were finite, nonnegative and normalized. These smoke fits disable
  BBS statistical features and do not regenerate production forecasts.
- Inspected all eight current workflow definitions and recent runs. The six-season
  PR checks and domestic refresh succeeded. Merge-triggered checks/reviews still
  running at inspection time were not classified as failures.

## Remaining limits that affect interpretation

The latest uploaded prediction run is 18 October at 14:35 UTC, before six-season
consumption was deployed. It needs a new ordinary prediction run. At inspection,
eight of its ten shortlisted fixtures had started; five selections had negative
adjusted EV and all ten were provisional. Negative EV is allowed by the requested
top-ten relative ranking policy and is not silently converted into a positive
edge. This review does not change that policy, its 50/50 weights, or model weights.

Last fitted BBS eligible examples were EPL 15, LaLiga 41, Bundesliga 14, Serie A
14, Ligue 1 13 and UCL 0, below the 120-example evaluation requirement. The new
source CSV history does not automatically turn historical CSV statistics into
BBS predictors. There remain 163 provider-statistic disagreements across 80
matches, nine unavailable UCL statistics and two quarantined UCL records. Keep
the baseline and existing dispute exclusions; do not lower evidence gates to
force features on.

Forward shortlist reporting contains 26 settled matches and the weighting trial
has only eight settled unique fixtures over one gameweek in the inspected report.
Those samples cannot establish optimized weights, sustained ROI or calibrated
accuracy. The existing first-look/promotion gates should remain in force.

Odds-dependent experiments and closing collection still share the provider
allowance. These fixes avoid unnecessary calls and surface failure; they do not
create quota or guarantee that all markets are available. GitHub's warm closing
collector can occupy a runner for five hours; this is an existing timing/reliability
tradeoff, not changed here. Large health reports duplicate historical detail;
blob reads were needed to inspect them in this audit. No claim is made about
local machine state, unpushed data, account billing or notification delivery.

Machine-readable findings and evidence counts are in the adjacent JSON report.
No paid/provider API probes were made during this review.
