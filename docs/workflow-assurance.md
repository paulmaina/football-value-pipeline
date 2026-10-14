# Workflow checks and evidence

## Pipeline self-test

Each code PR and relevant branch push runs four combinations: Python 3.12 and
3.14 on Ubuntu and Windows. Manual dispatch is supported. Read-only permissions,
20-minute job limits, and branch concurrency avoid overlapping duplicate runs.
All matrix legs run even if one fails.

Each leg checks installed dependencies, compiles every root/test Python module,
exercises all nine CLI help pages (including argparse percent formatting), runs
the offline Dixon–Coles self-test, and runs the complete unittest suite under
coverage. Tests cover chronological leakage protection, model gradients,
market/decay validation, odds failover and sanitization, environment precedence,
shortlist rules, scores including extra time/penalties, both shadow experiments,
immutable capture, report math and native Excel, cache refresh, and publishing
races. A six-league integration test runs prediction outputs through both
experiments, readable formatting, capture and verified grading with live network
access explicitly disabled.

Application statement coverage must be at least 75%, excluding tests. Critical
modules have additional floors recorded in `workflow_checks.COVERAGE_FLOORS`.
Measured baseline before this change was about 77%; the broader suite reaches
about 79%. A coverage percentage is a regression guard, not proof every behavior
is tested. JSON/XML coverage and smoke results are retained for 30 days, including
failed runs. The standalone legacy pipeline and formatter still have coverage
gaps; reports show those rather than excluding them to inflate coverage.

Install local test dependencies with:

```powershell
py -m pip install -r football_value_dev_requirements.txt
py workflow_checks.py smoke
py -m coverage run run_offline_tests.py
py -m coverage json --fail-under=0
py workflow_checks.py coverage
```

## Forward performance review

The workflow reviews daily around 10:30 EAT, on relevant main data/code pushes,
and on manual dispatch. Triggers cover both experimental sidecars and every
report-generation dependency. Write permissions are restricted to this main
workflow. Existing concurrency serializes reviews, and the publisher continues
retrying from fresh main when another process pushes first.

A code-only push never invents a prediction snapshot. Data pushes compare the
actual before/source commits, including goal-blend and market-led JSON. Initial
pushes with an all-zero previous SHA are handled. The capture checkout must
match the event SHA. Manual capture still requires explicit dispatch permission;
scheduled reviews do not capture old forecasts. Forecast rows, probability
simplexes, unique fixture identities, selected prices and summary counts are
validated before capture. Existing actual-capture-time and 20-minute pre-kickoff
checks remain authoritative.

Snapshot validation checks required SHA-256 manifests, file names/path safety,
commit identity, timestamps and row/eligible counts. Broken core archives stop
publication. Broken optional experimental files are excluded and reported as
warnings while baseline grading remains independent. Archives are never repaired
or retroactively rewritten by these checks.

The full offline suite runs before publishing. GitHub's result-provider secret
must be configured; CI uses explicit environment mode rather than your local
.env. Provider outages can still use previously verified cached results, with
provider errors prominently reported as degraded health rather than invented
scores. Missing results stay pending. Missing live quote/provider coverage cannot
be repaired by a workflow or inferred from a passing test suite.

Reports are regenerated on the latest main and independently checked **before
push**: frozen selection/policy/tier/price/probability provenance, verified-cache
scores, regulation-time outcomes, Brier and flat-unit P&L, cumulative and group
counts/rates, prediction coverage and mean Brier, pending exclusions, workbook
summary-cell reconciliation, ZIP/XML and native charts, plus experimental report timestamps and coverage.
Policy groups now appear in metrics and Markdown, alongside existing market,
league, week and STRICT/PROVISIONAL groups. Excel already contains policy groups.

`football_output_v2/performance/workflow_health.json` and the Actions step summary
expose archive counts, graded/pending samples, policy groups, provider health,
training-end dates and both experiments. Training dates are informative; the
review does not retrain, refresh CSVs or assume every league plays each week.
Experimental comparisons remain research-only, with no automatic promotion.

Artifacts retain this attempt's regenerated reports, workbook, preflight
checks and archived snapshots for 30 days, even when validation or push fails.
The exporter preserves preflight diagnostics and never copies .env/live request
credentials. Invalid reports are retained for debugging and never published.
Stored experiment odds are paper evidence, not confirmed executable offers.

Useful manual checks:

```powershell
py workflow_checks.py raw
py workflow_checks.py archives
py workflow_checks.py reports
```

A new code merge can update reports from existing evidence; it cannot turn new
forecasts into settled results or prove profitability. Cross-platform CI executes
on GitHub; local verification alone does not claim Windows/Python 3.14 coverage.

## Windows experiment binding repair

Replay of commit `fbfe5af89d0633da4bf4e581e42347272b5e913e` confirmed that both
experiment files held the CRLF forecast hash, while the committed/captured CSV
used LF. Their generation timestamps matched, but the old exact-byte binding
excluded both sidecars. Capture now accepts only exact, LF or CRLF versions of
the same forecast bytes, still requiring the matching run timestamp. A changed
probability, price, row or other CSV content remains invalid. Snapshot manifests
continue hashing exact archived bytes. `.gitattributes` fixes current raw CSV
checkout representation and disables text normalization inside immutable archives.

Existing snapshots are not backfilled or rewritten. Rerun with both experimental
flags and commit/push the fresh files before kickoff to begin correctly captured
experimental evidence. Older raw experiment files are not retroactively graded.

Daily source, execution and experimental capture evidence is described in [daily evidence](daily-evidence.md). The new UCL refresh CLI is included in smoke checks; its validation/publishing modules, quote policy and health reporting have dedicated regression and coverage gates.

Offline checks use `run_offline_tests.py` to isolate synthetic bookmaker fixtures from personal account allowlists. Use `py run_offline_tests.py --model-self-test` for the model-only check. Production still loads `shortlist_quote_policy.json`.

The optional recency extension reuses the goal sidecar manifest. Fresh recency reports are additionally reconciled with first frozen variant probabilities, half-lives, official finished scores, complete graded/coverage cohorts, paired score differences, calibration and weekly aggregates before publication. See [recency experiment](recency-experiment.md).

The automatic filter-sensitivity sidecar freezes all six-market candidate decisions at 1.5%, 3%, and 5% adjusted net EV. Review validates complete ledgers and reconciles every published selection, result, ROI, drawdown and calibration aggregate against the frozen forecast and verified result cache. Optional corrupted evidence is isolated from the baseline. See [guide](filter-sensitivity-experiment.md).

The Historical model benchmark workflow runs separately on pinned, hash-verified CSVs with read-only permissions and no API secrets. Its prediction ledger and fold chronology are reconciled before artifact publication. Closing odds are oracle/reference-only; nominal-opening CSVs lack exact availability timestamps. Statistical underperformance or insufficient Pinnacle coverage is reported as evidence, not a CI failure or reason to alter production.

The benchmark forward bridge binds a development-selected registry, candidate probabilities, production score matrix and actual control to immutable forecast snapshots. Reports are reconciled against verified results before publishing. Readiness requires paired coverage and preregistered gates; issue notifications are idempotent and never promote production. Scheduled generation captures its forecast commit explicitly before publishing reviews, preserving concurrent main changes through fresh worktree retries. Missing cloud credentials are reported as setup required.

## Local close collection and totals trial

The forward workflow now includes the separate totals registry/sidecar and closing quote observation pushes. Optional failures preserve baseline capture. Totals and closing reports are recalculated during report validation; hash, temporal and same-event quote checks fail closed. See [local setup](closing-odds-and-totals-trial.md).
