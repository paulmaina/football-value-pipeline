# Research shortlist: accuracy safeguards and implementation stages

The comparison foundation and complete published-grid export are implemented.
PR #128 also changes main-shortlist qualification to
`local-research-profit-115-200-dc12-v2`: offered odds strictly above 1.15 and
at most 2.00, including Double Chance 12. Its probability basis is the
unvalidated `team_form_poisson_v1` research model introduced in PR #126.
`research_backtest.py` results are still pending; software tests cannot establish
predictive improvement or non-degradation. No newly fitted calibration/blend
coefficients are promoted. Staking, cagey correction and the published forecast
probabilities retain their existing behavior.

## Phase 1: implemented diagnostic foundation

`score_matrix_json` contains every cell of the final published square grid,
after 1X2 blending and any successful totals anchor. Row index is home goals;
column index is away goals, both starting at zero. The JSON is normalized, uses
full floating-point precision and has `score_matrix_version` equal to
`published-score-matrix-v1`. Existing prediction CSV/snapshot capture retains
these fields. Missing historic grids stay unavailable, never reconstructed
from raw lambdas, margins or the top 20 scorelines.

`research_backtest.py` compares:

- A: full archived published grid, or an explicitly labelled CSV production
  proxy in historical mode;
- B: uncorrected Pinnacle fit B, requiring usable 1X2, O/U 2.5 and main AH;
- C: the frozen PR 126 independent-Poisson research specification.

Historical mode shares `historical_benchmark.load_history` and `fold_windows`,
including the audit boundary. Production half-life, market blend, totals anchor
and gated CSV shots are reconstructed from the benchmark configuration. BBS
statistics and historic internet research are unavailable. Form uses only
training rows before the fold origin. Nominal opening CSV prices are
untimestamped: results are retrospective model diagnostics, not evidence of
available prices, ROI or CLV. Required pinned-input hashes are checked by CLI.

Archive mode reuses integrity-checked snapshots and the verified cached
regulation results. It chooses the latest eligible generation per fixture
before seeing the result, requiring generation AND capture at least 20 minutes
before kickoff. It never calls the internet. B requires fresh pre-cutoff quotes;
C requires supported, frozen research observed by the evaluation cutoff.
Older archives may have no A grid or no C research. Coverage gaps are explicit.
Replay after an outcome is known is not automatically a preregistered trial.

Outputs include five-way AH log loss/Brier on predeclared home lines -2 through
+2 in quarter increments, 1X2 and Over 1.5 probability scores, and comparisons
by development/audit phase and league. Positive-return reliability and binary
scores use actual fresh archived offers and the archived execution cost/policy;
pushes and half wins below cost do not count as positive returns. Reliability
bins are offer-weighted descriptive diagnostics, not independent trials.

Log-loss comparisons use the same fixtures/markets for each pair. The bootstrap
resamples calendar weeks, retaining correlated fixtures/lines together. Fewer
than two weeks produces no interval. Intervals are descriptive, not adjusted
for multiple comparisons, and cannot authorize promotion. ROI stays in existing
tracking of actual shortlist decisions. This script does not create or stake bets.

Example commands (use the actual source SHA):

```sh
python research_backtest.py --mode historical --cache .football_cache --output football_output_v2/performance/research_historical --source-commit <sha>
python research_backtest.py --mode archives --root football_output_v2 --output football_output_v2/performance/research_archives --source-commit <sha>
```

`results.json` records configuration/hash, source commit, input hashes, fold
cutoffs, training hashes, candidate versions, gaps and shadow-only status.
`scores.csv` permits fixture-paired inspection. UCL/UEL appear separately when
eligible European archives exist; domestic CSV history cannot manufacture them.

Still required before promotion: a frozen forward comparison window, candidate
and research-settings preregistration, sample-size/power review, top-ranked-pick
comparison at fixed selection coverage, calibration slope/intercept uncertainty,
and correction for candidate/market searches. Existing retrospective audit
periods have already been examined and cannot become untouched tests again.

## Phases 2–5: proposed candidates, not production changes

1. **Tilting is an experiment.** Multiplying cells by exp(a*i+b*j) retains
   certain relative dependence ratios, not the original draw probability or
   calibrated 1X2/totals anchors. Keeping a DC-shaped interaction does not prove
   accurate draws after changing means. Use convergence/residual checks, valid
   attainable targets and sufficient grid support; a couple of unchecked Newton
   steps is insufficient. The hand-set form target remains unvalidated even if
   the solver is perfect. Compare against the unchanged published grid first.
2. **Blend coherently.** Test a simple arithmetic grid blend as a baseline
   before geometric pooling. Align goal axes and control tail mass; geometric
   pooling can erase cells when either input has zero/truncated support. Fit
   weights on development only, include published-only and market-only options,
   and account for market information already in the published forecast.
3. **Calibrate coherently.** Independently calibrating P(margin > k) at each k
   can create crossing thresholds and negative implied masses. A margin CDF
   must be monotone across thresholds, not merely in the input probability.
   Margin calibration alone cannot calibrate totals. Use a constrained joint
   distribution/settlement scheme, fit on separate chronological data, and
   verify quarter-line ranking/EV/staking from the same probabilities. Pooling
   Europe with a competition indicator does not create European evidence.
4. **Residual form still needs testing.** Use out-of-sample expectations saved
   at each historical date. In-sample fitted expectations leak fit information
   into residual evaluation. Recent results already influence refitted team
   rates; subtracting expected goals does not automatically remove duplication.
   Fit beta using chronological validation, with beta=0 as the baseline.
5. **Identity before domestic features.** Require unambiguous canonical team
   IDs, season-aware domestic membership, competition and regulation status.
   A +/-1 day/name match is only a candidate match: it must not merge two real
   fixtures or count postponed fixtures twice. Quarantine conflicting scores.
   Existing xG availability and observation times still apply.
6. **Congestion/strength/coverage weights need evidence.** Rest features must
   include schedule information available before prediction, including scheduled
   matches between prediction time and kickoff. Distinguish planned from
   actually played matches. Shrink sparse country effects; test opponent
   effects, coverage weights and market-gap flags separately before combining.
7. **Late information needs an operational window.** A repeating due-fixture
   collector is more reliable than one exact T-75 trigger. It must handle
   postponements, quota/timeouts, stale/absent confirmed lineups and duplicate
   captures. Freeze new research and odds together. Never backtest with realized
   weather or lineups learned after prediction.

The existing restriction remains: minus-line references never receive cagey
correction; Pinnacle-quoted value lines are not automatically corrected just
because they are plus lines. No correction is applied to diagnostic B here.

## Phase 6 and promotion

Keep selection, odds floors, deduplication and stake/exposure decisions separate
from probability experiments. Retain negative-EV eligibility with visible warnings
and missing-research eligibility. Better hit rate alone does not establish ROI.

Do not promote on an AH average alone when the list also ranks 1X2, double chance
and totals. Assess probability accuracy and the actual positive-return ranking
on a fixed common quote cohort, plus market/league segments. Calibration slope
0.9–1.1 alone is insufficient: inspect intercept, reliability and uncertainty.
An inconclusive European result means insufficient evidence; it is not a pass
for non-degradation. The default is to retain the baseline in that segment.

`benchmark_promotion_rules.json` registers these as shadow comparisons under the
existing human-reviewed minimum of 300 distinct paired fixtures and six gameweeks;
those are minimum review conditions, not a guarantee of statistical power.
