# Daily data health and forward evidence

UCL current-season training results now refresh independently every four hours.
The refresh requests the full football-data.org season schedule, compares its
finished matches with the previous cache, and records the latest completed date,
new matches, score corrections, next fixture, overdue unfinished matches,
download timestamp and exact cache hash. Invalid or regressive responses leave
the previous files intact. Publishing retries against latest main and preserves
concurrent changes. The existing domestic refresh remains separate.

A training end date several weeks ago does not alone establish stale data.
`CURRENT_WITHIN_PROVIDER_SCHEDULE` means the current download contains the
provider's completed matches without overdue scheduled results; it is not an
independent completeness guarantee. Reports distinguish this from
`DOWNLOAD_NOT_VERIFIED`, `REFRESH_OVERDUE`, `PROVIDER_OVERDUE_RESULTS`, and
`MODEL_BEHIND_VERIFIED_SOURCE`. Refreshing source files does not refit existing
forecasts. The full prediction command refits them.

Local UCL refresh uses the project's `.env` credentials:

```powershell
git pull
py -m pip install -r football_value_requirements.txt
py refresh_ucl_training.py
```

CI explicitly uses the existing `FOOTBALL_DATA_API_KEY` repository secret.
The UCL workflow also regenerates and validates performance health after it
publishes the source update. Forecast generation still requires a local run;
this workflow does not consume odds credits or manufacture forecasts.

## Production execution policy v7

All six conservative markets retain their probability/history/timing thresholds,
one validated bookmaker requirement, and +1.5% adjusted EV floor. Exchange
**target quotes** (Matchbook, Betfair Exchange, Smarkets, Betdaq) are excluded
until commission and executable liquidity are supported. An exchange can still
provide the existing probability reference: model fitting, calibration and
reference selection are unchanged. Fresh runs choose the best permitted actual
bookmaker quote; re-ranking old outputs rejects excluded target quotes rather
than inventing a replacement. Under 3.5 remains excluded.

`shortlist_quote_policy.json` supports:

```json
{"allowed_bookmakers": ["Your bookmaker's exact provider title"], "per_stake_cost_bps": 0}
```

An empty allowlist retains ordinary sportsbook coverage. It does **not** verify
Kenyan availability, your account access, bet acceptance or stake limits. Set the
allowlist to accounts you can actually use. The optional cost is a global
per-stake fee in basis points, not an assumed exchange commission rate.
Nonfinite, negative or invalid settings fail clearly. All candidate EV values
deduct this configured cost; the adjusted +1.5% and nonnegative raw EV gates
use net values. Costs are frozen in shortlisted rows and deducted from both
winning and losing simulated settlements. Native Excel formula caches and
editable formulas use the same costs. Legacy snapshots retain their original
gross assumptions; reports do not retrospectively change their bets.

## Evidence visible in reports

- The performance Markdown dashboard and Excel **Pipeline Health** sheet show
  training/source health, quote problems, capture coverage, daily observations
  and review dependency versions.
- `performance/health_history.json` stores one latest observation per UTC day.
  It records sample counts, ROI, Brier, policies, experiments and data health.
- New immutable snapshots include a hash-bound `pipeline_health.json` with
  capture status and diagnostic hashes. Fresh pipeline runs also emit a
  hash/time-bound `raw/pipeline_run_metadata.json`; its generation dependency
  versions and model code hash enter snapshot health. Capture/review runtime
  versions are distinguished from the generation runtime. Legacy generation
  environments are unknown.
- Each experiment is visibly `CAPTURED`, `NOT_GENERATED`,
  `PRESENT_BUT_REJECTED`, `MISSING_OR_TAMPERED` or `LEGACY_NOT_RECORDED`.
  A missing optional artifact never removes baseline evidence.

The actual October 13 snapshot `962a7a22cb5bd1ec1fb3ceac2b4d2345662a495b`
was captured at 11:07:31 UTC (14:07:31 EAT), with 67 pre-kickoff forecasts and
both experimental sidecars. Earlier missing sidecars are not backfilled.

Software/data health improvements do not establish model improvement. Assess
paired experimental Brier/log loss/calibration, settled net ROI, policy and
market cohorts, and sample counts over coming weeks. Reports do not
automatically promote experiments or retune thresholds from a small sample.
Dependency versions are recorded and compatibility is tested on Linux/Windows
and Python 3.12/3.14; dependencies are not blindly upgraded in the repository.
