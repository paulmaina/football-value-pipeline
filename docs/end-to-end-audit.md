# End-to-end audit — football-value-pipeline

Inspection only. No code, config, outputs or history were changed. Audited at
`main` = `e1eccb9f3` on 2026-11-07. Evidence was gathered with local commands,
the committed outputs, the GitHub Actions run history (`gh run list`,
2026-10-24 → 2026-11-07, 611 runs) and failed-run logs.

Every finding has a severity, a location, evidence and a suggested fix.
**Verified** = reproduced from data or code here. **Suspected** = strong
evidence but not proven end to end.

---

## 0. Baseline

| Check | Result |
|---|---|
| `python -m pytest -q tests` | **1 failed, 1297 passed, 1 skipped, 967 subtests** (22 min). Failure: `tests/test_local_research_v2.py::CachedTrainingResearchTests::test_ucl_can_train_from_local_cache_without_api_key` — `assertTrue(pipe.football_data_org.cache_only)` is False. Local environment only (see B-1). |
| `python run_offline_tests.py` | **Ran 1292 tests in 1470 s — FAILED (failures=1, skipped=1).** Same single failure as pytest (`test_ucl_can_train_from_local_cache_without_api_key`). |
| `python workflow_checks.py raw` (latest committed run) | **FAILS**: `ValueError: Current cagey-tier shortlist differs from deterministic replay (row 27, handicap_line: saved=-1.0, replay=-0.5)`. Also fails at the run's own commit `af73fbfee` (sparse worktree), so PR #132 is not the cause (see L-5). |
| Local env vs run env | Local: Python 3.14.8, pandas 3.0.6, numpy 2.5.3. The run recorded: Python 3.12.16, pandas 3.1.1, numpy 2.5.4 (`pipeline_run_metadata.json`). |

**Latest committed run** (`football_output_v2/raw`, run id `d292e568…`, commit `af73fbfee`):

| Field | Recorded in run | Config on `main` now | Match? |
|---|---|---|---|
| generated_at_utc | 2026-11-07T13:54:13Z | — | — |
| selection_policy_version | `48h-ah-price-edge-cagey-v28` | `asian_handicap.PRODUCTION_POLICY = CAGEY_POLICY` (v28) | yes |
| value rule | `local-research-profit-115-200-dc12-v2` | same (`cagey_correction_config.json`) | yes |
| cagey tier rule | `no-loss-market-reference-v5` | same | yes |
| cagey model | `cagey-correction-through-2425-v1` | same | yes |
| quote timing rule | `observed-by-cutoff-v2` | same | yes |
| excluded_markets | *(not recorded → none)* | `["Over 1.5"]` | **NO** |
| master version | `master-profit-no-dc-v6` | `master-profit-no-dc-no-over15-v7` (`master_shortlist_config.json`) | **NO** |

`master-profit-market-v5` (the version named in the brief) is **not current**.
It was used by exactly one archived snapshot. v6 replaced it on 2026-11-07
(commit `9dfb7f2f6`), and v7 was merged at 18:20Z (PR #132, `7c53948ba`),
four and a half hours **after** the latest run. See D-1.

**D-1 (MEDIUM, verified) — published lists predate the merged rules.** The
latest run still selected 32 Over 1.5 value picks, 32 Over 1.5 cagey picks and
3 Over 1.5 master picks, all excluded under v7. `scheduled-forecasts.yml`
triggers on push only for `.github/workflows/scheduled-forecasts.yml` and
`publish_scheduled_forecasts.py`, so merging rule changes (PR #132) does not
regenerate outputs. The next refresh is the 05:45 cron, which in practice
starts 6–8 h late. *Fix:* add the rule/config files (`cagey_correction_config.json`,
`master_shortlist_config.json`, selection modules) to the push paths, or
dispatch once after rule merges — but only after the credit fixes in §6.

---

## 1. Model inventory

Call chain for everything marked LIVE (verified by reading the code):

```
.github/workflows/scheduled-forecasts.yml  (cron 45 5 * * *, push on 2 paths, workflow_dispatch)
 └ publish_scheduled_forecasts.publish()                      publish_scheduled_forecasts.py:33
    └ football_value_pipeline_v2_standalone.py --leagues <10> --additional-odds-coverage all
         --api-key-source environment --no-legacy-comparison --research-free-sources
       └ main() → prediction_runs.stage_run → _generate_main()           :4602, :4161
          ├ FootballValuePipelineV2.run_league()  (Dixon-Coles + Odds API + per-event odds)
          ├ team_research.enrich()                                        :4511
          ├ conservative_bet_filter.build_conservative_shortlist(policy=PRODUCTION_POLICY) :4522
          │  └ price_edge_cagey_shortlist.build_shortlist  (v28)
          │     ├ price_edge_shortlist (v27 Pinnacle references a/b/c, quote capture)
          │     ├ market_implied (fit A / fit B)
          │     ├ narrow_margin (cagey correction model) + cagey_tier_v3 + cagey_market_basis
          │     └ profit_shortlist.annotate (team_form_poisson_v1 research probabilities)
          ├ cagey_tier_list() → cagey_tier_shortlist.csv                  :4536
          ├ master_shortlist.refresh() → master_selection_no_totals → _ah → master_selection :4541
          ├ staking.write_shortlist_stakes (advisory)                     :4549
          ├ bet365_pinnacle.write_list, price_edge_tracking.write_list    :4566, :4573
          └ workflow_checks.raw_check → prediction_runs.publish_run       :4616
    └ workflow_checks.py raw → format_football_output.py → narrow_margin_report.py
    └ commit → performance_tracking.py capture / review → workflow_checks.py reports → push (3 attempts)
```

| # | Name / ID / version | File(s) | Produces | STATUS | Proof | Run cost | Last validation / metrics |
|---|---|---|---|---|---|---|---|
| 1 | v28 policy `48h-ah-price-edge-cagey-v28` | price_edge_cagey_shortlist.py, conservative_bet_filter.py | conservative_bet_shortlist.csv (value tier) | **LIVE** | chain above; `asian_handicap.py:40` | part of the forecast run; credits come from the odds fetch | Forward: 942 value recs captured, 420 graded. **Mean CLV vs Pinnacle close −2.70% ± 1.62% (n=29)**, flat-stake −1.39% (n=135) (`performance/price_edge_v27/report.md`) |
| 2 | Value rule `local-research-profit-115-200-dc12-v2`, probability basis `team_form_poisson_v1` | profit_shortlist.py, team_research.py, match_context.py | ranks the value tier (profit probability) | **LIVE** | `selection_summary.model_role = "Researched settlement probabilities select and rank the main shortlist"` | free-source HTTP (no Odds API) | **No calibration or backtest.** The summary itself says *"has not passed a forward calibration gate"*. `research_backtest.py` exists but nothing calls it (DEAD). |
| 3 | v27 price-edge base `price_edge_shortlist` | price_edge_shortlist.py | Pinnacle references (a: same AH line, b: equivalent market, c: derived), quote capture | **LIVE** (inside v28) | imported by v28 and by the pipeline at :975, :1343 | — | Historical backtest (opening line, ≥2% edge): +2.46% CLV [+1.78, +3.17], n=256, max-price only (upper bound) (`performance/price_edge_backtest/report.md`) |
| 4 | Market-implied fit A/B `market-implied-dc-v1` | market_implied.py | reference type c / c-cagey; master fallback | **LIVE** | v28 `corrected_context`, master probability_basis | CPU only | Calibration 2026-11-02: 553/1176 intervals exclude zero (≈59 expected). Plus-line bias +0.66% (fit B) (`performance/market_implied_calibration/report.md`) |
| 5 | Cagey correction `cagey-correction-through-2425-v1` | narrow_margin.py, narrow_margin_models/ | c-cagey prices, cagey tier probabilities | **LIVE** | config + `narrow_margin.load` in v28 | CPU only | **GATE: PASS** 2026-11-03, but on `cagey-correction-pre2024-v1`. The production model is a refit through 2025-06 with the same spec (`narrow_margin_models/index.json`) and has no holdout of its own (L-8). |
| 6 | Cagey tier `no-loss-market-reference-v5` | cagey_tier_v3.py, cagey_market_basis.py | cagey_tier_shortlist.csv | **LIVE** | `cagey_tier_list(decisions)` :4536 | — | Forward: 714 recs, 226 graded. No separate CLV gate. 95% of the current list is negative-EV vs Pinnacle. |
| 7 | Master v7 `master-profit-no-dc-no-over15-v7` (v6 in latest run) | master_shortlist.py, master_selection_no_totals.py, master_selection_ah.py, master_selection.py | master_shortlist.csv (+ audit) | **LIVE** | :4541 | — | `validation_status: UNVALIDATED_SELECTION_RULE`. Latest run: 10/10 picks negative-EV. |
| 8 | Quote policy / freshness | quote_policy.py, quote_freshness.py, shortlist_quote_policy.json | bookmaker allow-list, freshness | **LIVE** | imported throughout | — | n/a (rules). Note the 24h freshness limit (L-6). |
| 9 | Narrow support `corrected-narrow-support-v1` | narrow_support.py | informational columns | DIAGNOSTIC | tier rule text: "narrow support is informational" | — | — |
| 10 | Staking (fractional Kelly) | staking.py | stake_recommendations*.csv | DIAGNOSTIC | `automatic_staking: false` | — | — |
| 11 | Production Dixon-Coles (+ shots, BBS statistics, Elo, totals anchor, 0.70 market blend) | football_value_pipeline_v2_standalone.py, shot_features.py, bbs_statistics_model.py, elo_ratings.py, historical_benchmark.anchor_totals | p_* columns, readable reports | **DIAGNOSTIC** under v28 | grep of v28/master modules: they read `p_*` only as Pinnacle-devigged inputs (`price_edge_cagey_shortlist.py:261-263`) and DC `p_over_1_5` only as `model_win_share` (`:619, :662`) | **largest CPU cost** in the run (fit per league). The totals anchor drives the `alternate_totals` credit (§6). | AH close backtest 2026-11-02: production replica loses to the close (dc: return skill −4.0%, blend70: −1.4%) (`performance/ah_close_backtest/report.md`) |
| 12 | Corner/card NB2 models | count_markets.py | count forecasts in predictions | **DORMANT** | runs every forecast (`:3550`); no odds requested (`:1255` comment), no policy reads it | CPU | — |
| 13 | bet365 vs Pinnacle list | bet365_pinnacle.py | bet365_vs_pinnacle.csv | **DORMANT** | **0 entries in 29/29 snapshots**, 0/63 fixtures with a bet365 quote: bet365 is not in region `eu` | adds `bet365` to closing requests when entries exist (never) | — |
| 14 | v27 tagged-candidate tracking | price_edge_tracking.py | price_edge_tagged_candidates.csv | DIAGNOSTIC | `tags.use = "tracking only; never changes a decision"` | — | — |
| 15 | Goal-market validation | goal_market_validation.py | `_goal_market_validation.json` | DORMANT (validation); the budget helpers are LIVE | diagnostics: `"SKIPPED: not required by …v28"` | — | — |
| 16 | Half-life tuning / legacy comparison | dc_decay_validation.py (+ archive/recency_experiment.py) | `legacy_*` columns, decay_tuning.json | **DORMANT** in production | publish passes `--no-legacy-comparison`; `legacy_comparison_status: {"None": n}` in every league | — | — |
| 17 | Auto market weight | market_blend_validation.py | — | DORMANT | `--auto-market-weight` never passed | — | — |
| 18 | Europa / UCL training | europa_training.py, scripts/europa_research.py, ucl_training.py | UEL/UCL histories | LIVE (data) | `forecast_availability` :4237 | football-data.org key | UEL: `LIVE_REFRESH_FAILED_USING_VERIFIED_CACHE`, verified 2026-11-05 (inside the 10-day `MAX_FALLBACK_AGE`) |
| 19 | Historical benchmark | historical_benchmark.py | weekly benchmark | DIAGNOSTIC | historical-benchmark.yml | none | weekly run 2026-11-02 |
| 20 | Superseded policies v2–v27 (conservative v6–v16, AH v17–v21, win-first v23, per-market v24, corners v25/v26, v27) | conservative_bet_filter.py, asian_handicap.py, win_first_shortlist.py, per_market_shortlist.py, corners_cards_shortlist.py, no_loss_corners_shortlist.py, price_edge_shortlist.py | replay of archived captures | DORMANT (replay only) | `asian_handicap.py:36-38` comment; snapshots record 20 distinct versions (§2) | — | — |
| 21 | v27 price-check | price_check.py, refresh_conservative_shortlist.py, price-checks.yml | re-ranked v27 list | **DORMANT/disabled** | `if: vars.PRICE_CHECKS_ENABLED == 'true'`; 10 runs, all `skipped` | would cost 3 credits/league/run | — |
| 22 | research_backtest | research_backtest.py | offline diagnostics | **DEAD** | no importer, no workflow; only tests/test_research_backtest.py | — | never run in CI |
| 23 | Monte Carlo pricing / service layer | match_simulation.py, pipeline_service.py | — | **DEAD** | pipeline_service is only named in a docstring (`:53`); match_simulation is only imported by pipeline_service | — | — |

**Flags**
- **Computed every run, output unused:** #11 Dixon-Coles stack (DIAGNOSTIC; spends CPU, and its totals anchor needs `alternate_totals` credits), #12 count_markets, #13 bet365 list.
- **LIVE with no backtest/calibration evidence:** #2 research ranking model (it ranks the main list), #7 master v7 (`UNVALIDATED_SELECTION_RULE`), #6 cagey tier v5 (no CLV gate). The forward evidence that does exist is negative (CLV −2.70%, n=29).

---

## 2. Repo cleanup inventory (junk) — nothing deleted

Repo: **134,106 tracked files, 1.18 GB tracked content, 285 MB pack**.
By top-level path: `football_output_v2/` 945 MB (1,566 files),
`.football_cache/` 231 MB (132,188 files; 199 MB / 122,959 files are `bbs/`).

**30 largest tracked files**

| Bytes | Path |
|---|---|
| 23,798,122 | football_output_v2/raw/shortlist_history/conservative_decisions_20261107T114859287499Z.csv |
| 22,780,270 | football_output_v2/raw/shortlist_history/conservative_decisions_20261107T135444589992Z.csv |
| 22,780,270 | football_output_v2/raw/prediction_runs/d292e568…/shortlist_history/conservative_decisions_20261107T135444589992Z.csv |
| 22,780,270 | football_output_v2/raw/prediction_runs/d292e568…/conservative_bet_rejections.csv |
| 22,780,270 | football_output_v2/raw/conservative_bet_rejections.csv |
| 18,265,004 | football_output_v2/raw/shortlist_history/conservative_decisions_20261106T134051320726Z.csv |
| 16,409,325 | …/shortlist_history/conservative_decisions_20261106T121745544607Z.csv |
| 16,148,372 | …/shortlist_history/conservative_decisions_20261106T112648544582Z.csv |
| 15,921,551 | …/shortlist_history/conservative_decisions_20261105T165033138342Z.csv |
| 15,527,327 | football_output_v2/performance/snapshots/3a3ff5eef0382745/shortlist_policy_experiment.json |
| 15,369,075 | …/snapshots/7a6c9d44b7c20308/shortlist_policy_experiment.json |
| 15,340,753 | …/snapshots/98adf7e32c9e19d0/shortlist_policy_experiment.json |
| 15,339,240 | …/snapshots/2a86586863a4a6d3/shortlist_policy_experiment.json |
| 15,212,864 | football_output_v2/performance/price_edge_v27/all_recommendation_generations.csv |
| 14,305,576 | …/snapshots/9425e536c27cdb34/shortlist_policy_experiment.json |
| 13,076,566 | …/snapshots/2db2af40cdce5284/shortlist_policy_experiment.json |
| 12,568,530 | …/snapshots/67fd2fe2099c1790/shortlist_policy_experiment.json |
| 12,568,376 | …/snapshots/b4dfb7c51677ddf4/shortlist_policy_experiment.json |
| 12,195,909 | …/snapshots/f7295b8c0c24a17c/shortlist_policy_experiment.json |
| 12,066,395 | …/snapshots/4827bd2b80141dd5/shortlist_policy_experiment.json |
| 11,898,475 | …/snapshots/a18515a42a8daaed/shortlist_policy_experiment.json |
| 11,881,246 | …/snapshots/ca1e126489f9dedd/shortlist_policy_experiment.json |
| 11,739,405 | …/snapshots/e93027ea804f64ef/shortlist_policy_experiment.json |
| 11,074,584 | …/snapshots/4c569effb9e72617/shortlist_policy_experiment.json |
| 11,058,944 | …/snapshots/4613e5b8880d2d0c/shortlist_policy_experiment.json |
| 8,714,137 | …/shortlist_history/conservative_decisions_20261105T133755785475Z.csv |
| 7,513,839 | …/snapshots/775022176692974f/predictions.csv |
| 7,186,151 | football_output_v2/performance/ah_close_backtest/per_match.csv |
| 6,836,514 | …/snapshots/e93027ea804f64ef/shortlist_weight_experiment.json |
| 6,828,373 | …/snapshots/1dabcf85eb639cd0/predictions.csv |

**Growth (MEDIUM, verified).** Each forecast run adds a ~16–24 MB
`conservative_decisions_*.csv` to `raw/shortlist_history/` (100 files,
171 MB). It also stores the same content as `raw/conservative_bet_rejections.csv`
and inside the run bundle (git dedups identical blobs, but every run is a new
blob). At 1–5 runs a day that is roughly 0.5–3.5 GB of history a month.
*Fix:* store decisions gzip-compressed or as Parquet, or keep them only in the
run bundle and drop the `shortlist_history` copy. `clv_report.py` reads
`shortlist_history`, so update it at the same time.

### 2a. Dead code

| Path | Size | Why it looks unused | Evidence | Risk |
|---|---|---|---|---|
| research_backtest.py | 361 lines | no importer, no workflow | AST import graph from all workflow entry points; only `tests/test_research_backtest.py` | SAFE (with its test) |
| pipeline_service.py | 150 lines | only named in a docstring | `football_value_pipeline_v2_standalone.py:53` | SAFE |
| match_simulation.py | 128 lines | only imported by pipeline_service | grep | SAFE (with tests/test_match_simulation.py) |
| forward_trial_basis.py | 37 lines | only listed in pipeline_health component hashes (`pipeline_health.py:131`) | grep | CHECK FIRST (remove from the hash list too) |
| scripts/compare_europa_history.py | 148 lines | no importer, no workflow | grep; tests/test_europa_history_comparison.py | CHECK FIRST (Europa research protocol) |
| scripts/europa_validation.py | 162 lines | no importer, no workflow | grep | CHECK FIRST |
| refresh_europa_training.py | 4 lines | no importer, no workflow (Europa refresh runs via refresh_training_data) | grep | SAFE |
| cagey_correction_report.py | 309 lines | manual offline gate report | no workflow | KEEP (reproduces the GATE) |
| `MAX_EXTRA_EVENT_ODDS` budget path (`--max-extra-event-odds-requests 24`) | — | bypassed: production always passes `--additional-odds-coverage all` (`:3433`, `:3451`) | code | KEEP the code, but see §6 |

### 2b. Superseded versions

| Path | Why | Evidence | Risk |
|---|---|---|---|
| Policies v2–v27 inside conservative_bet_filter.py, asian_handicap.py, win_first_shortlist.py, per_market_shortlist.py, corners_cards_shortlist.py, no_loss_corners_shortlist.py, profit_shortlist.py (team-research-profit-v1) | replaced by v28 | archived snapshots record 20 policy versions (v28: 16, v26: 13, v7: 10, v11: 7, …) and replay dispatches on the recorded version | **KEEP** (needed to replay archived captures) |
| master v2 / v5 / v6 (master_shortlist.VERSIONS) | replaced by v7 | snapshots: master-10-v2 ×10, v5 ×1, v6 ×1 | KEEP (replay) |
| cagey rules narrow-63-flagged-v2, v3, v4 | replaced by v5 | snapshots: narrow-63 ×7, v5 ×6 | KEEP (replay) |
| price_check.py + refresh_conservative_shortlist.py + price-checks.yml | re-runs **v27** selection, which is no longer production; job disabled | 10 runs, all skipped | CHECK FIRST — remove, or port to v28 before any enablement |
| archive/*.py (10 experiments) | retired forward trials | `archive/recency_experiment` is still imported by `dc_decay_validation.py:129,139` (dormant path), and archive modules are imported by ~10 test files | CHECK FIRST |

### 2c. Stale outputs and data

| Path | Size | Why | Evidence | Risk |
|---|---|---|---|---|
| football_output_v2/raw/market_led_candidates.csv, market_led_shortlist.csv, market_led_report.md | 61 KB | no writer in code; not in the run bundle; last written 2026-11-01 (`a1f198d2e`) | grep finds no reference in *.py; `comm` vs bundle listing | SAFE |
| `.football_cache/match_research/` (74 files) | 6.3 MB | **gitignored but still tracked** (ignore rule added after they were committed; last touched by PR #128 `af0ea89d5`) | `git ls-tree`; `.gitignore: .football_cache/match_research/` | SAFE to untrack (`git rm --cached`); replay uses frozen prediction evidence per the ignore comment |
| `.football_cache/oddsapi_*` response caches (~330 files: market_led_v1, additional_v1/dc_v1/ah_v1/ah_dc_v2, odds_*_eu) | ~10 MB | hand-committed old Odds API responses. Production runs in a temporary worktree and never reads them fresh (TTL 5–10 min). | `ls .football_cache \| grep oddsapi`; `_get_json` comment "Odds caches are committed by hand" | CHECK FIRST (tests or replays may load specific files) |
| Snapshot experiment sidecars: shortlist_policy (196 MB), filter_sensitivity (98 MB), model_reliability (45 MB), shortlist_weight (42 MB), market_led (36 MB), totals_anchor (31 MB), goal_blend (20 MB), benchmark_forward (12 MB) | **≈480 MB** | no longer written. The latest snapshots contain none of them. | file listing of the newest 3 snapshots | **KEEP** in history (archive hashes are verified by `workflow_checks archives`). Consider moving out of the working tree with Git LFS or a release asset — CHECK FIRST |
| Commands.txt | 4.9 KB | listed in .gitignore but tracked | `git ls-files` | SAFE to untrack (no secrets found by grep) |

### 2d. Orphaned tests
tests/test_research_backtest.py, tests/test_match_simulation.py, and
tests/test_europa_history_comparison.py only cover the dead modules in 2a.
The tests for archived experiments (test_goal_blend_experiment,
test_filter_sensitivity_experiment, test_model_reliability_experiment,
test_benchmark_forward_experiment, parts of test_forecast_integrity,
test_full_project_audit) cover replay of archived artefacts: **KEEP** while
those archives stay.

### 2e. Workflows, jobs, secrets

| Workflow | State | Evidence | Risk |
|---|---|---|---|
| price-checks.yml | disabled (`vars.PRICE_CHECKS_ENABLED`); v27 | 10/10 skipped | CHECK FIRST |
| audit-europa-access.yml, europa-production-check.yml | trigger only on branch `audit/europa-league-access` or dispatch; 0 runs in 14 days | run history | SAFE to remove if the branch is gone |
| card-bookings-research.yml | checks out `research/card-bookings`; runs `card_bookings.py`, which is not on main | 5 runs | RETIRED 2026-11-11: collection complete (658/658); PR #96 closed, cached events and study artifacts deleted |
| pipeline-self-test.yml | push on `**` → 91 of 128 push runs cancelled | run history | KEEP; consider `paths-ignore` for generated outputs |

Secrets referenced: THE_ODDS_API_KEY(+_FALLBACK_1/_2), FOOTBALL_DATA_API_KEY,
API_FOOTBALL_KEY, plus BBS keys in the collectors. None looked unused.

### 2f. Dependencies
`football_value_requirements.txt`: numpy, pandas, requests, scipy, rapidfuzz,
python-dotenv — all imported. Dev: coverage, pytest (CI), PyYAML and openpyxl
(imported by tests only) — all used. `matplotlib` is imported optionally
(`:2745`) and is not in any requirements file: harmless, but the reliability
PNG is never produced in CI. Nothing to remove.

### 2g. Docs describing behaviour that no longer exists
- `football_value_V2_README.md` (40 KB, last edited 2026-10-20) describes
  policy `72h-ucl-v3` (`:802`). Stale. CHECK FIRST (archive or rewrite).
- `README.md:143` still introduces "New policy v22". The rest of the README
  matches v28 (`:171-187`). Update.
- `PIPELINE_AUDIT.md` (2026-10-11) and `DATABASE_DESIGN.md` (2026-10-08) predate v20+. Review.
- `docs/` contains about 25 per-policy docs for retired versions (v6, btts,
  per-market, corners, win-first, …). KEEP as replay documentation, but add an
  index that marks them retired.

---

## 3. Data layer

### Fixtures (verified)
All 63 fixtures in `all_leagues_predictions.csv` came from The Odds API and are
linked (`live_odds_matched` = fixtures in every league). There are 0
`excluded_unresolved_team_fixtures` and 0 duplicate fixture rows or ids.

| League | Fixtures | Event calls | Status |
|---|---|---|---|
| EPL, LaLiga, Bundesliga, Ligue1, Eredivisie | 8 each | 8 each | RECEIVED_VALID_DC_QUOTES |
| SerieA | 9 | 7 | 2 `NOT_REQUESTED_OUTSIDE_WINDOW` (Cagliari–Frosinone, Torino–Lecce: <20 min to kickoff) |
| PrimeiraLiga | 8 | 8 | RESPONSE_WITHOUT_VALID_DC_QUOTES |
| SuperLig | 6 | 6 | 5 received, **1 REQUEST_FAILED — CREDITS_EXHAUSTED** |
| UCL, UEL | 0 | 0 | no events in window (no `/odds` call made — correct) |

The Odds API and football-data.org windows still end at different times
(existing follow-up memo). Not re-tested here.

### Odds coverage (verified)

| Finding | Severity | Evidence | Fix |
|---|---|---|---|
| **D-2** Primeira Liga: all 8 fixtures have **Pinnacle only**: no 1xBet on any market, only 1 bookmaker for 1X2 (`odds_bookmakers_1x2 = 1`). Any Primeira pick is priced at the reference book itself, so it is negative-EV by construction. Each fixture still gets a ~4-credit per-event call. | MEDIUM | per-fixture scan of `price_edge_quotes` / `asian_handicap_offers` | Skip per-event calls when the main response has no allowed non-reference bookmaker; review whether Primeira earns its credits |
| Pinnacle and 1xBet present for AH and h2h on every other fixture. Gaps: DC missing for Eredivisie (Pinnacle) and SuperLig (Pinnacle); totals missing for some 1xBet fixtures | LOW | coverage table in the evidence run | none |

### Freshness (verified)
At generation, offered and Pinnacle quote ages were: value median 2.8 / max
8.5 min, cagey 3.1 / 9.8, master 2.1 / 8.3. None was over 15 min and none was
in the future. Master had 2 picks over 6 min, tagged `RECHECK_PRICE`. No mixed
clocks: every list uses `evaluated_at_utc = generated_at_utc`.

**L-6 (MEDIUM, verified):** the shared freshness gate allows **24 hours**
(`quote_freshness.py:4 MAX_QUOTE_AGE_HOURS = 24.0`). Value and cagey only
look fresh because the quotes were just fetched. A cached or delayed quote up
to 24 h old would pass. Only master enforces 15 min (`master_selection.py`).
*Fix:* give value and cagey an explicit max age, e.g. 15 min, matching master.

### Research inputs
- UEL training: live refresh failed and the verified cache from 2026-11-05 was
  used (2 days old, inside `MAX_FALLBACK_AGE = 10 days`, `europa_training.py:23`). OK.
- **D-3 (HIGH, verified): research form lookups miss teams through exact name
  matching.** 15 of 63 fixtures carry `form unavailable`, and in 6 of them
  *both* teams have 0 history rows. `team_research.form_history` compares
  `canonical_team_key` strings exactly (`team_research.py:76-78`), while the
  main model resolves names with rapidfuzz. Reproduced:
  `canonical_team_key('1. FC Köln')='1 koln'` vs `'FC Koln'→'koln'`;
  `'Bayer Leverkusen'` vs `'Leverkusen'`; `'FSV Mainz 05'` vs `'Mainz'`;
  `'Atalanta BC'`, `'CA Osasuna'`, `'RC Lens'`, `'Besiktas JK'`,
  `'Vitória SC'`→`'Guimaraes'` all fail. Promoted teams such as Amed SK and
  Çorum FK legitimately have no history. The research model still outputs
  probabilities for these fixtures, far from the market (Besiktas home 0.64
  vs market 0.82; Galatasaray 0.53 vs 0.69; Monza–Atalanta away 0.62 vs
  0.46). **42 of 178 value picks and 2 of 10 master picks** come from these
  fixtures. *Fix:* reuse the main model's resolved team identity
  (`_history_for_league` mapping) in team_research. Set the research
  probability to missing, not a prior, when a side has fewer than N matches.
- xG: `xg unavailable` on 33/63 fixtures; venue, lineups and tactics are
  unconfirmed almost everywhere. These are visible warnings, not silent (policy
  `research_missing_policy = eligible with visible coverage warnings`).

### Caches
**D-4 (LOW, verified):** `.football_cache/match_research/` is **tracked** (74
files, 6.3 MB) despite the ignore rule. *Fix:* `git rm -r --cached`.

### Sanity (verified)
All 28 probability columns are in [0, 1]. Model and market 1X2 triples sum to
1.000000. No odds below 1.01 (the only hit, `odds_bookmakers_1x2`, is a count
column). No duplicate fixture rows. All kickoffs are UTC `+00:00` with 0 NaT.

---

## 4. Logic layer

| Check | Result |
|---|---|
| De-margining | Pinnacle references use **proportional** devig (`price_edge_shortlist`, `market_implied.devig_three_way`, `devig_proportional`). The model snapshot uses `--devig power` (default). They are internally consistent within each list, but the two lists use different methods (L-7). Fit A/B reproduce Pinnacle 1X2 exactly (calibration report), so the AH ±0.5 and DC references agree with 1X2 by construction. |
| Score grid | Model 1X2 sums are exactly 1. `asian_handicap.margins` rejects grids with \|sum−1\| > 1e-8. |
| Settlement | Verified 14 hand cases with `asian_handicap.profit`: −0.25, −0.75, +0.25, +0.75, ±1.0, +1.25, +1.75, ±0.5, 0 — all correct (e.g. home −0.25 wins 1-0 = full win; home +0.75 loses 0-1 = half loss). `probabilities()` sets no-loss to `net ≥ 0` (win, half-win, push), which matches `chance_of_no_loss = w + hw + push` to 2e-16 on all 178 value rows. |
| EV recompute (20 sampled value picks, `random_state=1`) | `ER = w(o−1) + hw(o−1)/2 − hl/2 − loss` reproduces `profit_expected_return`, `cagey_expected_return`, `uncorrected_expected_profit` and `expected_return_after_cost` to ≤ 4.5e-16. `edge = fair_probability × odds − 1` matches on all 125 rows with a reference. **Arithmetic is correct.** |
| NaN handling | Rows with missing cagey/uncorrected settlement probabilities have `NaN` expected return (not −1 or 0). No `fillna(0)` in selection modules. No bare `except:`. |

**Silent failures**

| ID | Sev | Location | Evidence | Fix |
|---|---|---|---|---|
| **L-1** | **HIGH** (verified) | `football_value_pipeline_v2_standalone.py:2969-2976` | A league odds failure is only a `warnings.warn`, and the run continues without odds. Four generations fetched no odds and were **published as current**: 2026-11-01 12:23, 11-05 16:17, 11-05 16:27, 11-06 13:21. Each is `status: NO BET`, 0 picks in all three lists, with the reason text *"No candidate cleared the price-edge rule against a Pinnacle reference"*, which hides the real cause (odds unavailable or credits exhausted). | Fail the run, or publish an explicit `ODDS_UNAVAILABLE` status. Never replace a valid current run with a no-odds run. |
| L-2 | MEDIUM | `:3522-3531` | A per-event request failure sets `REQUEST_FAILED` in diagnostics and the fixture continues with main-market data only. This is visible in diagnostics but not in the summary or readable report. | Surface a count in `conservative_bet_summary.json`. |
| L-3 | LOW | `:4551` | Staking errors are swallowed with a warning (by design, advisory). | none |
| L-4 | LOW | `:544-550`, `:1521` | A failed historical season is skipped with a warning. Training continues on fewer seasons. | Record skipped seasons in diagnostics (partly done via `training_seasons_loaded`). |
| **L-5** | MEDIUM (suspected) | workflow_checks.py:209-230 | The deterministic replay of the cagey tier differs on this machine (Arsenal–Hull, saved AH −1.0 vs replay −0.5), even at the run's own commit. AH −1.0 and AH −0.5 have the **same no-loss probability** (P(home win)). The pick is therefore decided by an expected-return/odds tie-break that can flip between environments (Python 3.14/pandas 3.0.6 here vs 3.12/3.1.1 in CI). | Add a deterministic final tie-break key (e.g. line, then bookmaker). Pin dependency versions in the requirements file. |
| L-7 | LOW | `--devig power` vs proportional references | Two devig methods coexist. Harmless while the DC model is diagnostic. | Document or unify. |
| L-8 | LOW | narrow_margin_models/index.json | The gate passed on `pre2024-v1`. Production runs `through-2425-v1`, refit on data that includes the gate's test period. This is disclosed, but the deployed model has no out-of-sample check. | Add a forward check on 2025/26+ for the deployed model. |

---

## 5. Shortlists — gaps and consistency (latest run)

| List | Candidates (rows) | Rejected | Not selected | Selected | Fixtures |
|---|---|---|---|---|---|
| Value (v28) | 2,263 | 1,250 | 835 | **178** | 61 / 63 |
| Cagey tier (v5) | 2,263 | 1,300 | 792 | **171** | 58 / 63 |
| Master (v6) | union of the above | — | — | **10** | 10 |

**Rejection reasons — value:** odds > 2.00 (938), lost to a higher
profit-probability pick in the same group (835), no allowed bookmaker quote
(167), stale/unavailable quote (167), odds ≤ 1.15 (138), outside the
20-minute to 48h window (26).
**Cagey:** odds outside (1.15, 2.00] (1,243), corrected inputs unavailable,
stale or > 10 min apart (198), bookmaker unavailable (167), stale (167),
corrected distribution unavailable (114), window (26).

**Gaps:** value missed Cagliari–Frosinone and Torino–Lecce (kickoff < 20 min).
Cagey also missed Besiktas–Genclerbirligi, Mainz–Bayern and Leipzig–Augsburg
(`corrected Pinnacle distribution unavailable`, i.e. fit A/B unusable).

**Duplicates (verified):** no settlement-equivalent duplicates in value or
master. **Cagey tier has 2 pairs:** Celta Vigo–Levante (AH Home +0.50
@ Pinnacle 1.27 **and** DC 1X @ 1xBet 1.27) and Genoa–AC Milan (AH Away +0.50
@ Pinnacle 1.22 **and** DC X2 @ 1xBet 1.22). LOW–MEDIUM. *Fix:* deduplicate
by settlement-equivalence class in `cagey_tier_list`, as master v6 already does.

**Correlated picks (verified):** the value list takes the best pick per
market group, about 3 per fixture. On 27 fixtures it holds both sides of the
same match (e.g. Valencia–Real Madrid: AH Home +2.25 **and** Away win). These
are not strictly contradictory, but they are heavily correlated. Value and
cagey disagree on side for 64 fixture pairs. MEDIUM for bet quality.

**Cross-list consistency (verified):** 103 identical fixture+market pairs
appear in value and cagey with the same bookmaker and price. All 10 master
picks are found in a source list with the same book and price. No
inconsistencies.

**Negative-EV share (verified)**

| List | vs Pinnacle fair (`edge`) | vs cagey-corrected | vs research model |
|---|---|---|---|
| Value | 119/125 (95%) | 162/171 (95%) | 109/178 (61%) |
| Cagey | 125/133 (94%) | 163/171 (95%) | 136/171 (80%) |
| Master | **10/10 (100%)** | — | `master_expected_return` 10/10 negative |

**D-5 (HIGH, verified): many picks are priced at the reference book.** 89/178
value, 76/171 cagey and **6/10 master** picks are bets at **Pinnacle**, the
same book whose margin-free price is the fair reference. Such a bet is
negative-EV by construction (it carries Pinnacle's margin). The research model
(row 2) is what lets them rank highly. Its EV agrees in **sign** with the
Pinnacle edge on only **53%** of value rows (n=125); 55 picks have research
ER > 0 but Pinnacle edge < 0. In addition, 41 value picks (all DC 12) have
**no market reference at all** (`reference_type` NaN).
*Fix:* require offered-book ≠ reference-book, or require a positive Pinnacle
edge, for any list labelled "value". Do not rank by an unvalidated model.

**Grading coverage (verified):** `closing_odds.collection_targets`
(`closing_odds.py:125-154`) collects for frozen picks from **every**
archived snapshot plus cagey and master rows, not only the latest generation.
Good. But actual coverage is poor (`performance/closing_odds/report.md`,
latest-selection cohort): **1xBet 37 covered / 227 missing; Pinnacle 85
covered / 179 missing**; bet365 0 / 264. Causes: credit exhaustion since
2026-11-06 19:56Z, 19 failed and 5 cancelled closing runs in 14 days, and
GitHub queue delays against a 6-minute pre-kickoff window. HIGH, because the
STOP-REVIEW rule (≥100 graded picks with mean CLV < 0) can never be reached.

---

## 6. Odds API credits

### Call sites (verified)

| Call site | Endpoint | Markets × regions | Credits per call | Calls per run | Trigger |
|---|---|---|---|---|---|
| `TheOddsAPI.events` `:825` | `/sports/{k}/events` | — | **0** (free endpoint) | 10 (one per league) | forecast |
| `TheOddsAPI.odds` `:1174` | `/sports/{k}/odds` | h2h, totals, spreads × `eu` | **3** | leagues with ≥1 event in **72h** (8 in the latest run) | forecast |
| `TheOddsAPI.extra_markets_for_event` `:1237` | `/events/{id}/odds` | alternate_totals, alternate_spreads, draw_no_bet, double_chance × `eu` | **≈4** (cached responses: 4 markets returned in most files) | every linked fixture kicking off between 20 min and 48h (61 in the latest run). `coverage=all` **bypasses the 24-call cap** (`:3433, :3451`). | forecast |
| `closing_odds.fetch` `:117` | `/events/{id}/odds`, `bookmakers=pinnacle[,onexbet]` | h2h + totals always; + alternate_totals / double_chance / spreads + alternate_spreads + draw_no_bet by pick | **2–7** (observed mix) | every fixture in the 6-min pre-kickoff window, **including fixtures with no pick** | closing-odds.yml (cron `52 5-21` + `7,22,37 6-21`), cap 100 requests/day |
| `price_check.py` | `/odds` | h2h, spreads, totals | 3 per league | disabled | price-checks.yml |
| archive/market_led_experiment.py `:37` | per-event | — | — | not called | — |

`x-requests-remaining/used/last` are logged **only on failure**
(`odds_provider_health.http_details`, closing `provider_status.json`). Successful
responses do not record them, and the HTTP cache stores only
`fetched_at_utc` + payload (`:361-366`). **C-4 (MEDIUM):** add header capture
on every successful Odds API response and write a per-run credit ledger.

### Current state (verified)
**All three keys are exhausted.** At 2026-11-07T13:54Z (SuperLig per-event call)
and 17:54Z (closing collector): `THE_ODDS_API_KEY` used 497 / remaining 3,
`FALLBACK_1` 500 / 0, `FALLBACK_2` 499 / 1, all `OUT_OF_USAGE_CREDITS`. The
incident started 2026-11-06T19:56:54Z (`football_output_v2/closing_odds/provider_status.json`).
About 1,500 credits are gone by day 7 of the month.

### 14-day run history (GitHub Actions)

| Workflow | schedule | push | dispatch | Outcomes |
|---|---|---|---|---|
| Scheduled forecast collection | 15 | 9 | 15 | 25 success, 9 failure, 5 cancelled |
| Closing odds collection | 98 | 1 | 0 | 74 success, 19 failure, 5 cancelled |
| Price checks | 10 | — | — | 10 skipped |

The forecast cron `45 5 * * *` actually started at **11:56–13:51 UTC** on
failing days (e.g. 2026-11-07 11:56Z), 6–8 h late. That is a GitHub
scheduling delay, and it moves the forecast close to the 12:00–15:00 UTC
kickoffs.

Forecast generations per day: Oct 24–31 averaged 1–2. **Nov 4: 3, Nov 5: 5,
Nov 6: 4, Nov 7: 2** (committed). Manual dispatches made up 15 of 39 runs.

### Credit reconstruction
*Forecast runs* (estimate = 3 × leagues with odds + 4 × in-window linked
fixtures, from each archived snapshot's predictions):

| Day | Est. credits (captured generations) |
|---|---|
| Nov 1 | 342 |
| Nov 3 | 164 |
| Nov 4 | 302 |
| Nov 5 | 402 |
| Nov 6 | 533 |
| Nov 7 | 556 |
| **Nov 1–7** | **≈2,300** |

*Closing collector* (from the 448 committed observations; credits = distinct
markets returned): Nov 1–7 ≈ **461**, with Oct 24 at 328 and Oct 25 at 289 at
weekend peaks. 150 of the 448 observations were `h2h,totals` only, i.e.
fixtures with **no pick**.

*Burned but not captured* (suspected, not countable): runs that fetched odds
and then failed in post-generation checks, so nothing was pushed. 2026-11-03
13:52 (`capture`: correction-monitoring replay), 11-04 13:21 (`reports`:
unique fixture count mismatch), 11-07 12:11 (`reports`: snapshot
`n_pre_kickoff_forecasts` mismatch). Each was followed by manual re-dispatches
that fetched again.

**Total: ≥ 2,760 credits in 7 days, about 395/day, against a budget of
~1,500/month ≈ 50/day. That is roughly 8× over budget.**

### Per-market verdicts (13 v28 generations, Nov 3–7)

| Requested market | Used by (LIVE) | Unique published picks sourced from it (value / cagey / master) | Verdict |
|---|---|---|---|
| h2h (league) | Pinnacle 1X2 reference, fit A/B, value/cagey 1X2 picks | 70 / 41 / — | KEEP |
| spreads (league) | main AH for fit B; AH picks | 8 / 2 / — | KEEP |
| totals (league) | O/U 2.5 for fit A/B; all Over 1.5 picks came from here (63 / 45) | 63 / 45 / — | KEEP (Over 1.5 is now excluded by v7, but O/U 2.5 feeds the fits) |
| alternate_spreads (event) | AH lines and Pinnacle same-line references (type a) | **138 / 127** / — | KEEP |
| double_chance (event) | DC 1X/X2/12 picks (value/cagey); master excludes DC | 85 / 63 / 0 | KEEP for value/cagey; DROP if DC is retired |
| **draw_no_bet** (event) | parsed as AH 0 offer and "Pinnacle draw no bet" reference (type b) | **3 / 2 / 0** (reference for 4 / 3) | **DROP** — saves 1 credit per event (~25% of per-event cost). Pinnacle AH 0 comes from `alternate_spreads`. |
| **alternate_totals** (event) | 0 published picks. Only uses: the totals-anchor (DC model, DIAGNOSTIC) and fit B's O/U 2.5 fallback when Pinnacle's main line ≠ 2.5 (`price_edge_shortlist.py:207-216`) | **0 / 0 / 0** | **NARROW** — drop now that Over 1.5 is excluded. If the fit-B fallback matters, request it only for fixtures whose main Pinnacle total ≠ 2.5. |

### Waste (verified unless marked)

| ID | Sev | Waste | Evidence | Fix | Saving |
|---|---|---|---|---|---|
| **C-1** | **CRITICAL** | Several full forecast runs per day (scheduled + push + manual dispatch) at 150–290 credits each | Nov 5: 5 generations, Nov 6: 4 | One scheduled run per day. Make manual dispatch reuse that day's odds (cache odds in an Actions cache or artifact, TTL ~10 min). | −50–75% of forecast credits |
| **C-2** | **HIGH** | Post-generation check failures discard a run that has already paid for its odds, then the user re-dispatches | 3 failed runs (11-03, 11-04, 11-07) after generation | Run `capture`/`reports` checks before the odds fetch where possible. On failure, keep the generated raw/ as an artifact and retry only the checks. | 1 run per failure |
| C-3 | HIGH | Push-race retry re-runs the **entire pipeline** with new API calls | `publish_scheduled_forecasts.py:33-70`, loop of 3 attempts, comment "regenerate forecasts on latest main" | Rebase the generated commit (data-only paths) or re-use the staged raw/ instead of regenerating | up to 2 runs per race |
| **C-5** | **HIGH** | `--additional-odds-coverage all` bypasses the 24-call cap. 61 per-event calls ≈ 244 credits on a weekend run | `:3433, :3451`; latest diagnostics | Use `ranked` with a cap, or only fixtures where the main response has an allowed non-reference book | ~−50% per-event |
| C-6 | HIGH | Closing collector requests every in-window fixture, including those with no pick (`keys = current \| …`, `closing_odds.py:151-152`; default 1X2 target `:162`) | 150/448 observations were pick-less `h2h,totals` | Collect only fixtures with frozen picks | ≈ −30% closing |
| C-7 | MEDIUM | Closing requests `draw_no_bet` and `spreads` for every AH pick; `h2h,totals` always | `closing_odds.py:199-204` | Request only the market each pick settles on (AH → alternate_spreads; AH 0 → spreads) | −1–3 per call |
| C-8 | MEDIUM | Primeira Liga per-event calls return Pinnacle only (no bettable non-reference price) | §3 | Skip per-event calls when no allowed non-reference book is in the main response | −32/run |
| C-9 | LOW | `/odds` league call uses the 72h lookahead; per-event calls use 48h. A league whose fixtures are all 48–72h out pays 3 credits for nothing | `:1180` vs `goal_market_validation.py:157-160` | Call `/odds` only when `/events` (free) has a fixture inside 48h | small |
| C-10 | LOW | DORMANT models trigger no API calls themselves; the bet365 closing add-on never fires | — | none | 0 |

### Budget projection (credits/day, steady state)

| Scenario | Forecast | Closing | Total | vs 50/day |
|---|---|---|---|---|
| Current (Nov 1–7) | ~330 | ~66 | **~395** | 8× |
| + one run/day, no reruns (C-1..C-3) | ~200 | ~66 | ~265 | 5× |
| + drop draw_no_bet, alternate_totals (2 credits/event) | ~125 | ~66 | ~190 | 4× |
| + skip non-bettable events, cap or ranked coverage (C-5, C-8) | ~70 | ~66 | ~135 | 2.7× |
| + closing only for picked fixtures, exact markets (C-6, C-7) | ~70 | ~25 | **~95** | 1.9× |
| + forecasts only on matchdays / fewer leagues, or 1 run every 2 days | ~35–45 | ~25 | **~60–70** | ≈1.2–1.4× |

Even with every fix the free allowance is tight. Fitting 1,500/month also
needs a scope cut: fewer leagues (e.g. drop Primeira, where there is no 1xBet
price) or capped per-event coverage such as 24 events/run. The alternative is
a paid tier.

---

## 7. Summary

**LIVE:** v28 policy · value rule `local-research-profit-115-200-dc12-v2` (team_form_poisson_v1 research ranking) · v27 price-edge references · market-implied fit A/B · cagey correction `through-2425-v1` · cagey tier `no-loss-market-reference-v5` · master `v7` (latest run v6) · quote policy and freshness · Europa/UCL training data.
**Unused:** DIAGNOSTIC — Dixon-Coles stack (shots, BBS statistics, Elo, totals anchor, market blend), staking, narrow support, tagged tracking, historical benchmark · DORMANT — count_markets, bet365 list, goal-market validation, half-life tuning/legacy comparison, auto market weight, price_check (v27), superseded policies v2–v27 (replay) · DEAD — research_backtest, pipeline_service, match_simulation, forward_trial_basis, compare_europa_history, europa_validation, refresh_europa_training.

### Top 10 issues (impact on bet quality and credits)

1. **C-1/C-2/C-3 CRITICAL — credits ~8× over budget; all 3 keys exhausted on day 7.** Multiple forecast runs a day, re-dispatches after post-generation failures, and full regeneration on push races.
2. **D-5 HIGH — value and master lists are 95–100% negative-EV vs Pinnacle.** 6/10 master and 89/178 value picks are bets *at* Pinnacle (the reference book). 41 DC-12 picks have no reference.
3. **Row 2 HIGH — the main list is ranked by an unvalidated research model.** Its EV agrees in sign with the Pinnacle edge only 53% of the time. Live CLV is −2.70% (n=29).
4. **D-3 HIGH — research form lookup misses teams through exact name matching.** 15/63 fixtures affected, producing 42/178 value picks and 2 master picks. Research probabilities are far from market (e.g. 0.64 vs 0.82).
5. **L-1 HIGH — an odds failure publishes a misleading "NO BET" run as current.** Four times in 7 days.
6. **Closing grading coverage HIGH — 68–86% of latest selections have no closing quote.** The CLV stop rule cannot trigger.
7. **C-5/C-6 HIGH — uncapped per-event coverage (`all`) and closing calls for fixtures with no pick.**
8. **D-1 MEDIUM — committed raw/ still reflects v6 / Over 1.5 rules.** The PR #132 push does not trigger a forecast, and `workflow_checks raw` fails locally on the committed run.
9. **L-5 MEDIUM — replay is not deterministic across environments.** AH −1.0 vs −0.5 have tied no-loss probability, and dependency versions are unpinned.
10. **L-6 MEDIUM — 24-hour quote freshness limit for value and cagey** (master uses 15 min). Also: correlated opposite-side picks in the value list, and 2 settlement-equivalent duplicates in the cagey tier.

### Cleanup list

**SAFE to remove now:** `football_output_v2/raw/market_led_{candidates,shortlist}.csv`, `market_led_report.md` · untrack `.football_cache/match_research/` (74 files) and `Commands.txt` · `research_backtest.py` + its test · `pipeline_service.py`, `match_simulation.py` + its test · `refresh_europa_training.py` · `audit-europa-access.yml`, `europa-production-check.yml` (if branch `audit/europa-league-access` is gone).

**CHECK FIRST:** `price_check.py` / `refresh_conservative_shortlist.py` / `price-checks.yml` (v27) · `forward_trial_basis.py` (in a hash list) · `scripts/compare_europa_history.py`, `scripts/europa_validation.py` · `archive/` (still imported by dc_decay_validation and tests) · hand-committed `.football_cache/oddsapi_*` caches · snapshot experiment sidecars (~480 MB; archive checks hash them) · `count_markets` and the bet365 list (DORMANT code still run every forecast) · stale docs (`football_value_V2_README.md`, `PIPELINE_AUDIT.md`, `DATABASE_DESIGN.md`).

**KEEP:** policies v2–v27 and master/cagey old versions (replay), `cagey_correction_report.py`, archived snapshots and closing observations.

### Fix plan (ordered)

1. **Stop the credit bleed (today):** one scheduled forecast per day. No manual re-dispatch until odds caching exists. Drop `draw_no_bet` and `alternate_totals` from `EXTRA_EVENT_MARKETS`. Closing: only fixtures with picks, exact markets.
2. **Fail loudly on missing odds (L-1),** and never replace a valid current run with a no-odds run.
3. **Make reruns free:** cache the run's odds responses as an Actions artifact. Retry checks or push without regenerating (C-2, C-3). Log `x-requests-*` on every call (C-4).
4. **Cap per-event coverage** (`ranked`/24, or skip events with no allowed non-reference book) (C-5, C-8).
5. **Bet quality:** exclude reference-book (Pinnacle) offers from "value" ranking, or require a positive Pinnacle edge. Fix team_research name resolution (D-3). Treat missing research as missing.
6. **Determinism and hygiene:** add a final tie-break key (L-5), pin dependencies, set a 15-min freshness limit for value and cagey (L-6), dedupe settlement-equivalents in the cagey tier.
7. **Regenerate raw/ under v7** (dispatch once, after step 1) so the published lists match config.
8. **Cleanup PR:** SAFE items above. Then the CHECK FIRST items one at a time.
