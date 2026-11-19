# Simplification audit, November 2026

Audit only: no code, config or output was changed. Taken on branch `audit/simplification` from `main` at `cc3850c4f` (17 Nov 2026). No `--declaration` was run and no holdout score was read. Nothing listed below may touch the holdout ledgers, `evaluation/declarations/`, locked fit files and their hash tests, evaluation reports cited in `docs/plan.md`, or anything the rollback and shadow checks read. Where a proposal would come close to one of these, the section says so.

**Status labels.** *Confirmed*: the evidence is complete (static import graph, `git grep`, git history, the saved run and snapshots). *Needs check*: something could not be traced from the repo, such as a manual run, a person's intent or a test that may depend on the item.

**Behaviour checks used below** (section 5 of the brief):

- **H**: a locked harness run (`evaluation_harness.py --output DIR`) is byte-identical to main on every output file.
- **R**: the replay of the saved live runs (`evaluation_harness.py --mode live` plus `workflow_checks.py raw` on the saved bundle) is byte-identical on every file.
- **T**: the full suite passes, and no test is deleted unless the code it tests is removed (each proposal says which).
- **L**: the live outputs of a scheduled run are unchanged, except files that only the removed code wrote.

## Status (19 Nov 2026)

Worked through with Paul's agreement on 18–19 Nov 2026 (plan "Open items", items 2 and 3). Each PR ran the behaviour checks listed below for its items and states the results in its description. No PR changed a live probability, pick or stake. No `--declaration` was run, and no holdout score was read.

| # | Item | Status | PR |
| --- | --- | --- | --- |
| 1 | Stale docs | Done: README quick start is the production command; ten leagues, live markets, v22 text under History; three docs moved to `docs/archive/`; CLAUDE.md bullets merged; note on the earlier audit | #197 |
| 2 | UCL refresh health step | Done: step removed | #200 |
| 3 | Full suite before reports | Done for `forward-performance.yml`; `historical-benchmark.yml` keeps its suite (Paul) | #200 |
| 4 | Experiment review queue | Done: module, notify jobs, CLI entry, floor and health entry removed (#200); last queue files deleted here | #200, this PR |
| 5 | Dead modules | Done; the pipeline docstring pointer went in #203 (fingerprinted file) | #198 |
| 6 | Stale tracked files | Done: market-led files removed; `Commands.txt` and `.football_cache/match_research/` untracked | #198 |
| 7 | Branch-only Europa workflows | Done (branch last pushed 22 Oct 2026); the branch itself is not deleted | #198 |
| 8 | Dead branches | Done: `LIVE_SIDECARS` loop and the recency path; live code no longer imports `archive/` | #198 |
| 9 | Legacy comparison default | Done: opt-in `--legacy-comparison`; `--no-legacy-comparison` kept as a no-op | #203 |
| 10 | Harness `devig_method` | Done, docs only (plan, data and periods); key unchanged | #197 |
| 11 | Price check | Done, option (a): retired | #203 |
| 12 | bet365 vs Pinnacle list | Done: no longer computed or written; column stays `[]` | #203 |
| 13 | Margin removal core | Follow-up, after 2g-4 is scored (fingerprinted files; plan open item 6) | — |
| 14 | Retired sidecars in the checkout | No change (Paul) | — |
| 15 | Fixture identity | No change (Paul) | — |
| 16 | Historical file loaders | Follow-up, after 2g-4 is scored (plan open item 6) | — |
| 17 | Score-grid builders | No change (as recommended) | — |
| 18 | AH settlement copies | No change (Paul) | — |
| 19 | Version forks | Follow-up, after the master rollback window (plan open item 7) | — |
| 20 | Dormant per-run work | Partly done: BTTS parsing removed (#203). `count_model` declined: kept for the shadow corner list (Paul, 18 Nov 2026) | #203 |
| 21 | 1xBet monitoring columns | No change (as recommended) | — |
| 22 | Understat fetch | Done: `research_config.json` `understat_live`, off by default | #206 |

Section 6 ("Looks like a bug"):

| Bug | Status | PR |
| --- | --- | --- |
| 1. Two fair-close methods | Done: `price_edge_tracking` reads `clv_report.fair_closing_prices` (power). Every graded pick was recomputed both ways first; no trigger changes state | #205 |
| 2. README runs a non-production model | Done with item 1 | #197 |
| 3. Price-check refresh drift | Gone with item 11 (retired) | #203 |
| 4. Silent cagey rule fallback | Done | #194 |

## 1. What is live

Built from an AST import graph of every tracked `.py` file, starting from the scripts the workflows run (helper at the end of this section).

| Entry point | Trigger | Scripts it runs | Writes |
| --- | --- | --- | --- |
| `scheduled-forecasts.yml` | cron 05:45 daily, manual | `publish_scheduled_forecasts.py` → pipeline (`--no-legacy-comparison --research-free-sources --additional-odds-coverage all`), `workflow_checks.py raw`, `format_football_output.py`, `narrow_margin_report.py`, `model_activity.record_forecast`, `performance_tracking.py capture` and `review`, `workflow_checks.py reports`; then `experiment_review_queue.py --notify` | `football_output_v2/raw/` (run bundle, value list, cagey tier, both masters, monitoring, stakes, tagged candidates, bet365 list), `readable/`, `performance/`, `model_activity/`, `odds_api_usage/` |
| `forward-performance.yml` | cron 07:30, push on ~40 paths, manual | `workflow_checks.py smoke`, **`run_offline_tests.py` (full suite)**, `workflow_checks.py archives` and `capture`, `publish_performance.py` (review plus reports check), `experiment_review_queue.py --notify` | `performance/`, `readable/football_performance_report.xlsx` |
| `closing-odds.yml` | cron every 15–60 min 05–21 UTC | `github_closing_odds.py plan / standby` → `closing_odds.py` | `closing_odds/observations/` |
| `refresh-training-data.yml` | cron every 4 h | `league_registry.py`, `refresh_training_data.py --publish` | `.football_cache/` |
| `refresh-ucl-training.yml` | cron every 4 h | `refresh_ucl_training.py --publish`, **`publish_performance.py`** | UCL cache, `performance/` |
| `collect-api-football-data.yml`, `collect-bbs-data.yml` | cron 3×/day | collectors and publishers | `.football_cache/` |
| `research-c6-fits.yml` | cron Monday 17:05 (fortnightly publish) | `scripts/build_research_c6_fits.py`, `scripts/build_research_ce3n_fits.py` | `research_c6_live_fits.json`, `research_ce3n_live_fits.json`, activity log |
| `historical-benchmark.yml` | cron Monday 08:15, push | **`run_offline_tests.py`**, `historical_benchmark.py` | Actions artifact only |
| `pipeline-self-test.yml` | every push and PR | smoke, self-test, suite under coverage, pytest pass, coverage floors | Actions artifact only |
| `price-checks.yml` | cron hourly, job gated off (`vars.PRICE_CHECKS_ENABLED`) | `price_check.py` → `refresh_conservative_shortlist._refresh` | a new run bundle (if enabled) |
| `europa-production-check.yml`, `audit-europa-access.yml` | push to branch `audit/europa-league-access`, manual | pipeline for UEL; `scripts/audit_europa_access.py` | Actions artifact only |
| `fetch-understat-history.yml` | manual | `scripts/fetch_understat_history.py` | a separate data branch |
| Evaluation harness | manual | `evaluation_harness.py`, `evaluation_diagnostics.py` | `evaluation/...` (by hand) |
| Monitoring and rollback | inside `performance_tracking.py review` | `research_monitoring.py` (v5 and v6 triggers), master rollback in `price_edge_tracking.py`/`performance_report_layout.py`, `model_activity.py` | weekly report, `research_v5_monitoring.json`, activity log |

Live shortlists, as configured today:

- **Value shortlist**: policy `48h-ah-price-edge-cagey-v28` (`asian_handicap.PRODUCTION_POLICY`), value rule `local-research-profit-115-200-dc12-v2`, research v5/v6 (`research_config.json`), Pinnacle only (`shortlist_quote_policy.json`).
- **Cagey tier**: `no-loss-market-reference-v5` (`cagey_tier_v3.py`, `cagey_market_basis.py`), correction `cagey-correction-through-2425-v1`, timing `observed-by-cutoff-v2`, excluded markets Over 1.5, DC 12, both DNB (`cagey_correction_config.json`).
- **Masters**: new master live (`master_reconciliation.py`, `master-new-fill-rule-v4-live-v10`); old master in shadow, `master-profit-15-pinnacle-markets-v9`, built through the chain `master_selection` → `_ah` → `_no_totals` → `_fifteen` → `_pinnacle_markets` (`master_shortlist_config.json`, `live: "new"`).

Reachability: 112 of 323 tracked Python files (45,059 lines) are reachable from these entry points. The 211 others are the 168 test files (37,417 lines) and 43 non-test files (10,231 lines). Those 43 are 10 `archive/` modules, 25 `scripts/` reports and replays, and 8 top-level or doc modules. Section 4 takes up the 8. Reachable does not mean used: for example, `research_backtest.py` is reachable only through the harness, and the superseded policy modules only through dispatch tables.

Since 9 Nov the Odds API keys have been exhausted, so no forecast has been published (the latest saved run is 8 Nov 12:21 UTC). Every observation about "the latest run" therefore comes from that run and the 82 archived snapshots.

<details><summary>How the map was built</summary>

`ast` walk over every `git ls-files '*.py'` file; edges from `import`, `from … import`, and literal `importlib.import_module`; reachability from the workflow entry scripts above. Non-literal dynamic imports exist only in `workflow_checks.py` (the empty `LIVE_SIDECARS` loop) and `tests/archived_hooks.py`.
</details>

## 2. Ranked findings

Ranked by value against risk: safe, high-value removals first; anything that touches live probabilities last. "Lines" counts code plus tests removed. Collisions refer to Prompt 5 work in flight: the C8 declaration (`holdout/research-c8`), the D_pow2 declaration (`holdout/cagey-dpow2`), `INPUT_SCHEMA`, the last-ten form, `research_config.json`, `cagey_correction_config.json` and `research_monitoring.py`.

| # | Item | Group | Status | Saves | Behaviour risk | Checks | Effort | Collides? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Stale docs: README quick start, competitions, markets, v22 text; CLAUDE.md duplicate bullet; earlier audit's stale claims | c | Confirmed | ~900 doc lines (archive `football_value_V2_README.md`) | none (docs) | T | S | No |
| 2 | Timestamp-only report commits from `refresh-ucl-training.yml` | d | Needs check | ~5 runs and ~5 commits a day | report freshness only | T, L | S | No |
| 3 | Full offline suite rerun inside `forward-performance.yml` and `historical-benchmark.yml` | d | Needs check | ~40 runner-min/day + ~11 min/week | weaker pre-report guard | T | S | No |
| 4 | `experiment_review_queue.py`, empty since 3 Nov, plus two notify jobs | a | Needs check (tests) | 60 lines, 2 jobs per run | none (empty output) | T, L | S | No |
| 5 | Dead modules: `pipeline_service.py`, `match_simulation.py`, `refresh_europa_training.py`, `docs/audits/history_window_audit.py` | a | Confirmed | 374 code + 161 test lines, 6 files | none | H, R, T, L | S | No |
| 6 | Stale tracked files: `raw/market_led_*`, `Commands.txt`, `.football_cache/match_research/` | a | Confirmed (a test reads `Commands.txt`) | 78 files, 6.4 MB | none | T, L | S | No |
| 7 | Branch-only Europa workflows | a | Needs check | 2 workflows, 112 lines, ≤7 credits per dispatch | none | T | S | No |
| 8 | Dead branches: `LIVE_SIDECARS` loop, `dc_decay_validation` recency path | a | Confirmed (tests need check) | ~35 lines; drops a live → `archive/` import | none | H, R, T, L | S | No |
| 9 | Legacy comparison on by default for manual runs | d | Confirmed | removes a trap; no lines | manual runs only | R, T, L | S | No |
| 10 | Harness config `devig_method: "power"` reads as global; it governs only A | c | Confirmed | doc clarity | none (docs) | T | S | Yes (config is in `SETUP_FILES`): docs only |
| 11 | Price check: disabled, mislabelled v27, its refresh duplicates the run's tail and has drifted | b, d | Confirmed | 310 lines + workflow if retired | none while disabled | T, L | M | No |
| 12 | bet365 vs Pinnacle list: never fed under Pinnacle-only | c | Needs check (tests) | one dead sidecar per run | removes a file only it writes | R, T, L | S | No |
| 13 | Margin removal: six implementations, two "fair close" methods | b | Confirmed | ~45 lines | byte-identical if done exactly | H, R, T, L | M | **Yes**: `SETUP_FILES` (after C8 and D_pow2 are scored) |
| 14 | Retired-experiment sidecars and `shortlist_history` copies in the tree | d | Needs check | ~680 MB checkout (history keeps them) | archive-check warnings; `clv_report` reads `shortlist_history` | R, T, L | M | No |
| 15 | Fixture identity built four ways | b | Needs check | ~10 lines | workbook overlap column may change | R, T, L | S | No |
| 16 | Historical file loaders: three parsers of the same CSVs | b | Needs check | an equality test, not a merge | none (test only) | T | S | **Yes**: touching them changes `SETUP_FILES` |
| 17 | Score-grid builders: four copies | b | Confirmed | none recommended | merging changes M and D | — | — | Yes |
| 18 | AH settlement: two copies of the split-line rule | b | Confirmed | 6 lines | low | H, R, T, L | S | Partly (`ah_close_backtest` in `SETUP_FILES`) |
| 19 | Version forks: master v1–v9 chain, cagey/value/timing rules, policies v2–v27 | d | Needs check | large, but blocked | high | — | L | **Yes**: the old-master shadow and rollback read the v9 chain |
| 20 | Dormant per-run work: corner/card count models, BTTS parsing | a, c | Confirmed | CPU per run; one raw column | changes `all_leagues_predictions.csv` | R, T, L | S | No |
| 21 | 1xBet monitoring columns, empty from the next run | c | Confirmed (code) | none; keep | replay needs the columns | — | — | No |
| 22 | Understat still fetched live from a maintenance page | c | Confirmed | ~10 HTTP requests per run | **live probabilities** if Understat returns | R, L | S | **Yes**: research inputs, the last-ten form |

## 3. Items

### 1. Stale docs (group c, confirmed)

**What.** Docs that describe superseded decisions, and one instruction that produces a non-production model.

**Evidence.**
- `README.md:16-32`: lists BTTS among estimated markets (dropped) and six competitions (the registry has ten: `league_registry.py`, `python league_registry.py`).
- `README.md:107-126` and `:304-310` ("Quick start", "Recommended usage"): `--tune-half-life` with no `--no-legacy-comparison`. `_generate_main` sets `applied_to_production = True` and replaces the fixed 480-day half-life with the tuned one (`football_value_pipeline_v2_standalone.py:4378-4382`). A run that follows the README therefore produces forecasts from a model other than `production_v2` and also fits the legacy companion. See the bugs section.
- `README.md:186-202`: the "archived v22" paragraph reads as current text (Pinnacle/bet365/1xBet, DC 12). Since `d9d9682f7` (8 Nov) the shortlists use Pinnacle only.
- `README.md:333`: calls `football_value_V2_README.md` (818 lines, last edited 20 Oct, `f15c8d15b`) "authoritative". It describes policy `72h-ucl-v3`.
- `PIPELINE_AUDIT.md` (11 Oct), `DATABASE_DESIGN.md` (8 Oct): predate v20.
- `CLAUDE.md:38-39`: two "Map" bullets for `research_rate_calibration.py` that overlap ("C8 is the research candidate…"; "C7 and C8 … C7 is dropped").
- `docs/architecture.md:15,22,77-94`: presents `pipeline_service.py` and `match_simulation.py` as the service layer (see item 5).
- `docs/end-to-end-audit.md` (8–11 Nov): says `price_check.py` reruns v27; it reruns `PRODUCTION_POLICY` (v28) (`refresh_conservative_shortlist.py:14,33-35`). It also lists `research_backtest.py` as dead; the harness now imports it.
- `.github/workflows/price-checks.yml:1`: titled "Price checks (v27, off by default)"; same mismatch.

**Smallest change.** Edit the README sections (drop BTTS, list the ten leagues, replace the quick start with the scheduled command from `publish_scheduled_forecasts.py`, move the v22 paragraph under a "History" heading). Move `football_value_V2_README.md`, `PIPELINE_AUDIT.md` and `DATABASE_DESIGN.md` to `docs/archive/` with a one-line banner. Merge the two `CLAUDE.md` bullets. Add a note at the top of `docs/end-to-end-audit.md` pointing here. Retitle the price-check workflow.

**Risk and proof.** No code changes. T only: `tests/test_publish_scheduled_forecasts.py:161-172` scans `README.md`, `docs/*.md` and `Commands.txt` for retired command flags, so a doc edit must keep it passing.

**Effort.** Small. **Collisions.** `CLAUDE.md` and `docs/plan.md` are also edited by the open holdout branches: rebase them, or take this last.

### 2. Timestamp-only report commits (group d, needs check)

**What.** `refresh-ucl-training.yml` runs `publish_performance.py` (full review plus reports check) every four hours, after the UCL refresh.

**Evidence.** 51 commits "Update forward-only gameweek performance reports [skip ci]" since 9 Nov (8 days), with no forecast in that time. A typical one (`cc3850c4f`) touches 14 files, 36 lines each way: `reviewed_at`/`generated_at` stamps in `metrics.json`, `pipeline_health.json`, `workflow_health.json`, `health_history.json`, `experiment_review_queue.json` and the report headers. Runs: 13 UCL refreshes at a median of 3.2 min (`gh run list`, 12–17 Nov).

**Smallest change.** Remove the "Update visible performance health" step from `refresh-ucl-training.yml`. The daily `forward-performance.yml` run and the review after each forecast still refresh health.

**Saves.** About 5 runs and 5 commits a day, and the noise they add to `git log`.

**Risk.** The UCL training freshness shown in `performance/README.md` can lag by up to a day. No grading or pick changes. *Needs check*: whether Paul wants health refreshed within four hours.

**Proof.** T, L (the scheduled forecast's outputs are untouched; only report timestamps move less often). **Effort.** One step. **Collisions.** None.

### 3. Full suite rerun before writing reports (group d, needs check)

**What.** `forward-performance.yml:89` and `historical-benchmark.yml:42` both run `run_offline_tests.py`, the whole suite.

**Evidence.** Forward performance: 19 runs from 12–17 Nov (15 on push, 4 scheduled), medians 13.8 and 19.2 min; most of that is the suite (about 11 min, PR #164). Code reaching main has already passed `pipeline-self-test.yml` on its PR (33 PR runs, median 25 min) and on push. The report itself is validated independently by `workflow_checks.py reports`.

**Smallest change.** Delete the suite step from both workflows; keep `workflow_checks.py smoke` and `archives`.

**Saves.** About 11 min per forward-performance run (≈40 runner-min/day at the current rate) and 11 min a week on the benchmark.

**Risk.** A report could be written by code whose tests fail on the runner's environment and not on CI's (same OS and Python, so unlikely). This is a deliberate guard ("Run complete offline regression suite before writing reports"), so it is Paul's call. **Proof.** T. **Effort.** Two lines. **Collisions.** None.

### 4. Experiment review queue (group a, needs check)

**What.** `experiment_review_queue.py` builds a queue that is always empty: `build_queue` returns `'experiments': []` unconditionally since `0ec0ece41` (3 Nov, "Archive the benchmark-forward and totals-anchor trials").

**Evidence.** It is run from `performance_tracking.review`, from the `notify` job of `scheduled-forecasts.yml:58` and from the `notify` job of `forward-performance.yml:136`: two extra runners with pip installs per run. Its files `performance/experiment_review_queue.{json,md}` change only their timestamp. It has a coverage floor (`workflow_checks.py:44`, 85%) and a `CLI_FILES` entry. Four test files reference it, all archived-experiment tests (`test_benchmark_forward_experiment`, `test_model_reliability_experiment`, `test_shortlist_policy_experiment`, `test_shortlist_weight_experiment`).

**Smallest change.** Remove the module, its call in the review, both `notify` jobs, the `CLI_FILES` entry and its coverage floor (a floor for deleted code, not a loosened threshold), and the queue references in those tests. Keep the last committed `experiment_review_queue.{json,md}` frozen or delete them (only this module wrote them).

**Risk.** None for picks or grades. *Needs check*: what exactly the four tests assert about the queue. **Proof.** T (state which assertions go), L (only the queue files change). **Effort.** Small. **Collisions.** None.

### 5. Dead modules (group a, confirmed)

**What and evidence.**

| File | Lines | Last change | Importers outside tests | Tests |
| --- | --- | --- | --- | --- |
| `pipeline_service.py` | 150 | 23 Oct `da1291d4c` | none (named in a docstring, `football_value_pipeline_v2_standalone.py:53`) | `tests/test_pipeline_service.py` (97) |
| `match_simulation.py` | 128 | 23 Oct `ec3c6f0e1` | `pipeline_service.py` only | `tests/test_match_simulation.py` (64) |
| `refresh_europa_training.py` | 4 | 22 Oct `16a3e7fe2` | none; the Europa refresh runs inside `refresh_training_data.py` | none |
| `docs/audits/history_window_audit.py` | 92 | 19 Oct `31e429e2a` | none; cited by `docs/six-season-history.md:35` | none |

`pipeline_service.py` and `match_simulation.py` hold coverage floors (`workflow_checks.py:46`, 90 and 95). `europa_training.py:139` still tells the user to "run refresh_europa_training.py". No workflow, config or output depends on any of them, and none appears in `docs/plan.md` or an evaluation report.

**Smallest change.** Delete the four files and the two tests (the code they test is removed). Drop their coverage floors, the docstring mention, the `docs/architecture.md` rows, and change the `europa_training.py:139` message to name `refresh_training_data.py`. For the history audit, either delete it and keep its conclusion in `docs/six-season-history.md`, or leave it: it is documentation.

**Saves.** 374 code lines, 161 test lines, 6 files. **Risk.** None. **Proof.** H, R, T (two tests removed with their code), L; all four are mechanical here because nothing imports them. **Effort.** Small. **Collisions.** None.

### 6. Stale tracked files (group a, confirmed)

**Evidence.**
- `football_output_v2/raw/market_led_candidates.csv`, `market_led_shortlist.csv`, `market_led_report.md` (61 KB): written only by `archive/market_led_experiment.py:178-181`, which nothing runs; last written 1 Nov (`a1f198d2e`); not in the run bundle.
- `Commands.txt` (86 lines): listed in `.gitignore:18`, yet tracked. `tests/test_publish_scheduled_forecasts.py:161-172` reads it and asserts a hit at `Commands.txt:12`.
- `.football_cache/match_research/` (74 files, 6.3 MB): listed in `.gitignore:50`, yet tracked; replay uses the frozen research inside each forecast, not these responses.

**Smallest change.** `git rm` the three market-led files. `git rm --cached` the match-research folder. For `Commands.txt`, either untrack it and drop it from that test's source list, or remove the `.gitignore` line so the file is intentionally tracked. The second keeps the test as it is.

**Risk.** None. **Proof.** T, L. **Effort.** Small. **Collisions.** None.

### 7. Branch-only Europa workflows (group a, needs check)

**Evidence.** `europa-production-check.yml` and `audit-europa-access.yml` trigger only on pushes to `audit/europa-league-access` (it still exists on origin) or by hand; no run in the last 200 (12–17 Nov). The production check runs the pipeline for UEL with `--goal-market-validation --additional-odds-coverage ranked --max-extra-event-odds-requests 1`, about 7 credits per dispatch (`docs/odds-api-credits.md`). UEL has been in the scheduled run since the 22 Oct audit (`docs/audits/2026-10-22-europa-production.md`). `tests/` references `audit_europa_access` once (`scripts/audit_europa_access.py`).

**Smallest change.** Delete both workflow files (and the branch, if Paul agrees). Keep `scripts/audit_europa_access.py` and its test, or delete them together.

**Risk.** None for live outputs. *Needs check*: whether Paul still dispatches either one. **Proof.** T. **Effort.** Small. **Collisions.** None.

### 8. Dead branches in live modules (group a, confirmed)

**Evidence.**
- `workflow_checks.py:29,384-393`: `LIVE_SIDECARS = ()`, so the loop in `raw_check` never runs. It is the only non-literal `importlib` call in live code.
- `dc_decay_validation.py:71,127-142,164`: `collect_recency_metrics` defaults to `False`, and no caller outside `tests/` sets it (the pipeline at `:4362` and `historical_benchmark.py:213` don't). That branch is the only place where live code imports `archive/` (`archive.recency_experiment`).

**Smallest change.** Delete the loop and the empty constant. Delete the `collect_recency_metrics` parameter and branch, and move any test that sets it into the archived-experiment tests, calling the archive functions directly. *Needs check*: which tests pass `collect_recency_metrics=True`.

**Saves.** About 35 lines, and live code no longer reaches into `archive/`. **Risk.** None (unreachable under today's callers). **Proof.** H (`dc_decay_validation.py` is not in `SETUP_FILES`, but `historical_benchmark` imports it), R, T, L. **Effort.** Small. **Collisions.** None.

### 9. Legacy comparison is on by default for manual runs (group d, confirmed)

**Evidence.** `legacy_comparison = not args.backtest and not args.no_legacy_comparison` (`football_value_pipeline_v2_standalone.py:4264`). The scheduled run passes `--no-legacy-comparison`; in the saved run every league records `legacy_comparison_status: {"None": n}` and all `legacy_*` columns are empty. A manual run without the flag tunes the half-life per league and fits a second model (`:4353-4391`, `:3193-3236`). README's quick start omits the flag (item 1). The legacy columns' only readers were archived trials (`forward_trial_basis.py`, used by `archive/benchmark_forward_experiment.py` and `archive/totals_anchor_experiment.py`). Memory: superseded since 7 Nov.

**Smallest change.** Make it opt-in: add `--legacy-comparison` and keep `--no-legacy-comparison` as an accepted no-op, so `publish_scheduled_forecasts.py` and the docs keep working. Keep `LEGACY_COLUMNS` and `forward_trial_basis.py`: archived snapshots and `pipeline_health.py:131` (component hashes) use them.

**Risk.** Changes only manual runs that omit the flag. **Proof.** R, T, L (the scheduled command already disables it, so its outputs are byte-identical). **Effort.** Small. **Collisions.** None.

### 10. Harness `devig_method` (group c, confirmed)

**Evidence.** `evaluation_harness_config.json` has `"devig_method": "power"`. In code it is read only by `published_proxy` (A) at `evaluation_harness.py:342,346`. M and D are built by `market_matrix`/`cagey_matrix` with `method='proportional'` by default (`:229-256`), and QPROP is proportional by definition. The cagey tier's live grid is also proportional (`market_implied.py:31-33`). The key reads as if it governed every market reference.

**Smallest change.** Docs only: one line in the harness docstring and in `docs/plan.md` ("`devig_method` applies to A, the published-grid proxy; M, D and QPROP remove the margin proportionally"). Do not rename the key: the config is hashed into the setup fingerprint and declarations validate against it.

**Risk.** None. **Proof.** T. **Effort.** Small. **Collisions.** None if docs only; a config change would alter the setup fingerprint in the middle of Prompt 5.

### 11. Price check (groups b and d, confirmed)

**Evidence.** The `price-checks.yml` job is gated off (`if: vars.PRICE_CHECKS_ENABLED == 'true'`); the earlier audit found 10 of 10 runs skipped. `price_check.check` → `refresh_conservative_shortlist._refresh` re-ranks with `PRODUCTION_POLICY` (v28), not v27 as the workflow title and `docs/end-to-end-audit.md` say. `_refresh` (`refresh_conservative_shortlist.py:18-60`) re-implements the tail of `_generate_main` (`football_value_pipeline_v2_standalone.py:4605-4683`) and has drifted from it. It writes no `ce3n_ucl_live_check`, no `league_availability`, no `bet365_vs_pinnacle.csv` and no `shortlist_history/` snapshot. Unlike the run, it lets a staking failure abort (the run catches it at `:4637-4646`). Tests: `test_odds_api_credits.py`, `test_price_check.py`, `test_master_shortlist.py:255`, `test_goal_market_validation_switch.py:100`, plus two more.

**Smallest change.** Either (a) retire the price check (delete the workflow, `price_check.py` and the `_refresh` path of `refresh_conservative_shortlist.py`, about 310 lines and their tests) if Paul has no plan to enable it; or (b) extract the shared tail into one function that both `_generate_main` and `_refresh` call, so they cannot drift.

**Risk.** None while the check is disabled. (b) touches the live run's tail and must leave the scheduled run's outputs byte-identical. **Proof.** (a) T (tests removed with their code), L. (b) R, T, L. **Effort.** (a) Small, (b) Medium. **Collisions.** None.

### 12. bet365 vs Pinnacle list (group c, needs check)

**Evidence.** The forecast requests `bookmakers=pinnacle` only (`quote_policy.odds_api_bookmaker_scope`, `quote_policy.py:92-101`, with `shortlist_quote_policy.json` listing only Pinnacle). bet365 is therefore never in a payload, yet every run computes and writes `bet365_vs_pinnacle.csv` (`football_value_pipeline_v2_standalone.py:4659-4664`, plus `compare_event` per event at `:1375-1378`). The file has 0 rows in the saved run and in all 31 snapshots that carry it. Closing collection adds bet365 only for entries in that list (`closing_odds.py:135-157`), so never. Capture and the archive check treat it as optional.

**Smallest change.** Stop calling `write_bet365_list` and `compare_event` in the live run. Keep `bet365_pinnacle.py` for archived snapshots and `closing_odds.frozen_entries`.

**Risk.** Removes a file only this code writes. *Needs check*: the five tests that reference `bet365_pinnacle` (`test_value_model_independence`, `test_cagey_market_independence`, `test_model_upgrades_v1/v2`, the frozen fixture), and whether any reports test expects the file in a new bundle. **Proof.** R, T, L. **Effort.** Small. **Collisions.** None.

### 13. Margin removal (group b, confirmed; behaviour-sensitive)

**Evidence.** Six implementations:

| Function | Methods | Notes | Live callers |
| --- | --- | --- | --- |
| `football_value_pipeline_v2_standalone.devig` | power, proportional | returns `None`s for odds ≤ 1 | pipeline 1X2 and totals (power, `--devig` default), `bet365_pinnacle`, `closing_odds:60,75`, **`clv_report._power_devig`**, harness A and QPOW, `historical_benchmark`, `format_football_output:581` (proportional) |
| `market_implied.devig_power` | power | "the same bisection as `devig(odds, 'power')`… a test pins that" | cagey offline candidates |
| `market_implied.devig_three_way` | proportional inline, else power/Shin | | M, D, QPROP, cagey grid |
| `ah_close_backtest.devig_proportional` | proportional, two-way | | `price_edge_shortlist`, `price_edge_cagey_shortlist`, **`price_edge_tracking.close_win_share`/`close_over_share`** |
| `ah_close_backtest.devig_shin` | Shin, two-way | | `price_edge_shortlist`, cagey Over 1.5 |
| `market_implied.devig_shin_n` | Shin, n-way | "with two outcomes it is `ah_close_backtest.devig_shin`, step for step" | offline |

Drift:
- Input guards differ: the standalone function returns `None` on invalid odds, while the others divide and can raise or return garbage.
- Two "fair close" methods for the same picks: `clv_report` (dashboard headline CLV) removes Pinnacle's closing margin by **power**, while `price_edge_tracking` (weekly price-edge report, cagey and value close shares) uses **proportional**. See the bugs section.

**Smallest change.** Keep the two arithmetic cores in `market_implied` (`devig_power`, `devig_shin_n`, plus proportional). Make the standalone `devig` delegate its power branch after its `None` guard, and make `ah_close_backtest.devig_shin` delegate to `devig_shin_n`. Leave every call site and every method choice as it is. Same operations in the same order, so the floats are byte-identical; the existing equality test proves it.

**Saves.** About 45 lines, and one place to fix a margin bug. **Risk.** If any operation order changes, last-bit differences propagate into M, D and every harness output. **Proof.** H, R, T, L, all four.

**Effort.** Medium. **Collisions.** Yes: `football_value_pipeline_v2_standalone.py`, `market_implied.py` and `ah_close_backtest.py` are all in `SETUP_FILES` (`evaluation_harness.py:172-178`), and D_pow2's branch also edits `market_implied`/`narrow_margin` paths. Do this only after the C8 and D_pow2 holdout runs are scored and merged.

### 14. Checkout size: retired sidecars and decision copies (group d, needs check)

**Evidence.** Tracked HEAD is 177,159 files and 1,259 MB (`git ls-tree -r -l HEAD`). Of that:
- `performance/snapshots/` is 598 MB. 478 MB of it is 272 retired-experiment sidecars (`shortlist_policy` 196, `filter_sensitivity` 98, `model_reliability` 45, `shortlist_weight` 42, `market_led` 36, `totals_anchor` 31, `goal_blend` 20, `benchmark_forward` 12 MB). None has been written since 3 Nov.
- `raw/shortlist_history/` is 199 MB in 102 files. Each holds a run's full decisions, also stored as `conservative_bet_rejections.csv` and inside the run bundle.
- `.football_cache/oddsapi_*` is 558 hand-committed responses, 4.6 MB.

Creating this audit's worktree took over two minutes. `archive_check` hashes the sidecars as optional (`workflow_checks.py:451-456`) and turns a missing one into a warning. `clv_report` reads `shortlist_history`.

**Smallest change.** Not deletion. Move the retired sidecars to a release asset or LFS with their digests kept in `metadata.json`, and teach `archive_check` that "moved" is not "tampered". For decisions, keep them only in the run bundle and point `clv_report` there. History keeps every byte either way, so the saving is checkout time and disk, not repository size.

**Risk.** Archive checks and `clv_report` must give the same results. These snapshots are evidence for archived trials, not for anything in `docs/plan.md`, and no rollback or shadow check reads them. *Needs check*: Paul's view on moving archived evidence at all. **Proof.** R (archive check identical apart from the expected relocation), T, L. **Effort.** Medium. **Collisions.** None.

### 15. Fixture identity built four ways (group b, needs check)

**Evidence.**
- `performance_tracking.fixture_key`: league, canonical team keys, kickoff date. 103 call sites, the grading identity.
- `performance_report_layout.fixture_identity`: raw names and the full kickoff timestamp. Used for the workbook's "in the other master" flags (`:149,173`).
- `predictions_workbook._fixture_key`: `_offer_key[:4]`.
- `conservative_bet_filter` local `fixture_keys`: `fixture_id` first, then names plus kickoff (`:674`).
- `evaluation_harness.fixture_key`: same name, different domain (historical rows); fine.

Drift: a match whose kickoff time or team spelling differs between the two masters' rows is one fixture to grading but two to the workbook flag.

**Smallest change.** Make `fixture_identity` return `performance_tracking.fixture_key(row)`. **Risk.** Reporting only; the workbook flag may change where the two disagreed. **Proof.** R, T (golden workbook fixture may need regenerating, stated), L (workbook only). **Effort.** Small. **Collisions.** None.

### 16. Historical file loaders (group b, needs check)

**Evidence.** The same `.football_cache/{season}_{div}.csv` files are parsed by:
- `historical_benchmark.load_history`: its own decoding with a latin1 fallback, mixed day-first dates and goal validation. Used by the harness and the fit builders.
- `ah_close_backtest.load_division`: `read_csv_bytes` plus `validated_match_history`.
- `count_markets.load_history`.
- The live `FootballDataUK.season`/`history`.

A difference between the harness's and live's training rows feeds the open parity gap (plan Phase 1, "Release-gate parity").

**Smallest change.** Do not merge: the files are in `SETUP_FILES` and in live training. Add one test asserting that `hb.load_history` and `FootballDataUK.history` give identical (Date, HomeTeam, AwayTeam, FTHG, FTAG) rows for every cached league and season.

**Risk.** None (test only). **Proof.** T. **Effort.** Small. **Collisions.** A loader merge would; the test does not.

### 17. Score-grid builders (group b, confirmed; no change recommended)

**Evidence.** Four builders:
- `score_probability.score_grid`: tail-bounded, omitted mass ≤ 1e-10. The canonical builder for research, the pipeline and C0.
- `market_implied.dixon_coles_matrix`: fixed 0–20 goals. With λ ≤ 6 (`LAMBDA_BOUNDS`) the omitted mass is at most about 1.5e-6 per side.
- `historical_benchmark.adjusted_matrix`: fixed `max_goals`. Used by `anchor_totals` when `tail_bounded=False` (archived snapshots) and by tests.
- `research_low_score`: a vectorised pmf for likelihoods only.

The plan already records one consequence of truncation drift (C0 0.9810 vs 0.9813, `docs/plan.md:124-126`).

**Recommendation.** Leave them. Merging the market grid into `score_grid` changes M and D in the last digits, and with them every harness output and the live cagey tier. Add a docstring cross-reference so the next reader knows why there are two.

### 18. AH settlement, two copies (group b, confirmed)

**Evidence.** `ah_close_backtest.settle` (vectorised `split_line`; harness, backtests, `market_implied`) and `asian_handicap.settlement` (scalar `components`; live grading through `profit`, and pricing through `probabilities`) implement the same quarter-line rule. No drift found: same ±0.25 split, same strict comparisons. The other "settlement" functions (`master_selection.settlement`, `staking.settlement_returns`, `master_reconciliation.settlement_mass`) work on probability masses, not results.

**Smallest change.** Leave the code; add a test that both agree for every line in `asian_handicap.LINES` and margins −10 to 10. A delegation would save 6 lines but touch live grading and a `SETUP_FILES` module.

**Proof.** T. **Effort.** Small. **Collisions.** None if test only.

### 19. Version forks (group d, needs check; blocked)

**Evidence.**
- `asian_handicap.py:15-40` keeps policies v17–v28 and dispatches to `win_first_shortlist`, `per_market_shortlist`, `corners_cards_shortlist`, `no_loss_corners_shortlist` and `price_edge_shortlist`. `conservative_bet_filter.py` (826 lines) carries v2–v16.
- `price_edge_cagey_shortlist.py:81-98`: 5 tier rules, 4 value rules, 2 timing rules.
- `master_shortlist.py:27-36`: master v1–v9 plus the live v10. Old master v9 is built through five wrapper modules.
- `master_rule_v1.py` (#171's rule, harness only) and `cagey_sharpen.py` (failed its rule, harness only).

The 82 snapshots record 25 distinct policy and rule combinations (v2 to v28). `raw_check` replays only the current bundle, with the switches it recorded; `archive_check` only hashes; grading reads frozen shortlists. Whether anything still re-executes v2–v27 could not be fully traced (the `--mode live` replay, and tests that build old policies).

**Recommendation.** No removal now. The v9 chain is the old-master shadow and feeds the master rollback check, which must stay until the rollback window has passed (plan Phase 5). Next step: a short "which versions re-execute" table in `docs/` (from coverage of a `--mode live` run plus `raw_check` on every saved bundle). Only versions that never re-execute become candidates.

### 20. Dormant per-run work (groups a and c, confirmed)

**Evidence.**
- Corner/card count models run for every domestic league in every forecast and fill `count_model` (`football_value_pipeline_v2_standalone.py:3626-3631`). Its only readers are `corners_cards_shortlist.py` and `no_loss_corners_shortlist.py` (v25 and v26, replay). Corners and cards were dropped, and the Odds API no longer requests those markets (`:1278-1279`).
- `extra_markets_for_event` still parses a `btts` market (`:1314,1353-1356`) that `EXTRA_EVENT_MARKETS` never requests (`:98`), so `btts_yes` offers are always empty.
- `p_btts_*` and `p_under_3_5` columns are still computed and shown in readable reports. They are cheap and some readers use them.

**Smallest change.** Stop computing `count_model` in the live run (keep the module for replay). Delete the `btts` branch of the event parser. Both remove or empty raw columns (`count_model`, the BTTS quote columns) in `all_leagues_predictions.csv`. That file is not written only by the removed code, so this needs Paul's agreement under rule L.

**Risk.** No probability or pick changes; raw columns change. **Proof.** R (old bundles still replay, since they carry their own frozen columns), T, L (with the stated column change). **Effort.** Small. **Collisions.** None.

### 21. 1xBet monitoring columns (group c, confirmed; keep)

**Evidence.** `MONITOR_BOOKS = ('Pinnacle', '1xBet')` (`price_edge_cagey_shortlist.py:413`) adds 20 1xBet columns to `cagey_correction_monitoring.csv`. The saved run (8 Nov 12:21 UTC) still has 116 non-empty 1xBet cells, because it predates the Pinnacle-only switch (`d9d9682f7`, 8 Nov 20:12 UTC). From the next run they will be empty, since 1xBet is no longer requested.

**Recommendation.** Keep. `raw_check` requires the monitoring columns to equal `MONITOR_COLUMNS` exactly (`workflow_checks.py:359-360`), so removing them would break replay of every earlier monitored run. Note the expected blank columns in `docs/cagey-correction-v28.md`. The closing collector still asks for 1xBet on non-handicap picks (`closing_odds.py:196`); bookmakers in one request cost one region, so no credits are lost.

### 22. Understat still fetched live (group c, confirmed; touches live probabilities)

**Evidence.** For every domestic fixture in the five big leagues, `team_research` requests two Understat season pages (`team_research.py:544-555`). The site answers HTTP 200 with a maintenance page (`understat_check`, `:873-877`; memory of PRs #148/#149), so no xG row has been added. The frozen research evidence records "no match data (maintenance page)".

The live research uses xG in the form whenever both sides have at least five xG matches. If Understat comes back, live v5 probabilities would start using xG again with no release decision. The harness's C3 (the xG candidate) was clear only on Over 1.5, and xG is outside the C8 plan.

**Options for Paul.** (a) Leave it, accepting that live research may change by itself when the site returns. (b) Add a switch in `research_config.json` that keeps the fetch off until xG is decided. That changes the frozen evidence text of new forecasts, but not their probabilities while the site is down.

**Proof.** R, L (probabilities identical while the site is down; evidence lists change). **Effort.** Small. **Collisions.** Yes: research inputs, `research_config.json`, the last-ten form work and `INPUT_SCHEMA`. Decide after Prompt 5.

## 4. Totals

| | Code | Tests | Files | Other |
| --- | --- | --- | --- | --- |
| Confirmed and collision-free (items 5, 6, 8, 9) | ~410 lines | ~160 lines | 9 files (+ 74 cache files untracked) | 6.4 MB |
| With Paul's agreement (items 2, 3, 4, 7, 11a, 12, 20) | ~700 lines | ~300 lines (estimate) | ~8 files, 3 workflows | ~5 runs/day, ~40 runner-min/day, ≤7 credits per Europa dispatch |
| Docs (item 1) | — | — | 3 files archived | ~970 doc lines out of the root |
| After Prompt 5 (item 13) | ~45 lines | — | — | one margin-removal core |
| Storage (item 14) | — | — | — | up to ~680 MB checkout (history unchanged) |

All together: about 1,150 lines of code, about 460 lines of tests, roughly 20 files and 3 workflows, about 970 lines of stale docs, around 680 MB of checkout, and around 40–50 runner-minutes a day. None of it changes a live probability, pick or stake.

## 5. The three changes I would make first

1. **Docs pass (item 1).** The README currently tells a reader to run a model other than production. Zero code risk, and it removes the most misleading text.
2. **Dead code and stale files (items 5, 6, 8).** Purely mechanical deletions with complete evidence; all four behaviour checks pass trivially because nothing live imports them.
3. **Workflow trims (items 2 and 3, then 4).** The largest recurring saving (runner time, commit noise) for no change to any forecast, pick or grade. Each is a one-line workflow edit, pending Paul's view on report freshness and the pre-report test guard.

One PR each, with the diff and test results shown before merging (fix-branch rules).

## 6. Looks like a bug, not complexity

1. **Two different "fair close" calculations for the same picks.** `clv_report.py:89-91` (the dashboard's headline closing-line value) removes Pinnacle's closing margin by the power method. `price_edge_tracking.close_win_share`/`close_over_share` (`:698-722`, the weekly price-edge report's closing figures for value and cagey picks) remove it proportionally. Power gives favourites a larger fair share than proportional, so the two reports can disagree on the sign of CLV for a favourite. No doc states this choice (`docs/ah-close-backtest.md:65` says proportional for the backtest). Needs Paul's decision on one method; reporting only.
2. **README quick start runs a non-production model.** `--tune-half-life` applies the tuned half-life to production (`football_value_pipeline_v2_standalone.py:4381-4382`) instead of the fixed 480 days of `production_v2`, and, without `--no-legacy-comparison`, also fits the legacy companion. The model version string records the tuning, so such a run is labelled, but anyone following the README gets forecasts the live pipeline never makes.
3. **The price-check refresh has drifted from the run it imitates (latent; the check is disabled).** If enabled, its bundles would lack `ce3n_ucl_live_check`, `league_availability`, the bet365 list and the `shortlist_history` snapshot. A staking error would also abort them, where the forecast run carries on (item 11).
4. **Silent fallback to a superseded cagey rule.** If `cagey_tier_rule`, `value_rule` or `quote_timing_rule` were ever removed from `cagey_correction_config.json`, `tier_rule()`/`value_rule()`/`timing_rule()` would quietly fall back to `value-v1`, `one-per-fixture-v1` and `skew-5min-v1` (`price_edge_cagey_shortlist.py:101-102,133-162`), the rules of 3 Nov, instead of failing. Latent; the config sets all three today. A one-line check in `load_settings` that requires the keys would close it, but `cagey_correction_config.json` is in Prompt 5's scope.
