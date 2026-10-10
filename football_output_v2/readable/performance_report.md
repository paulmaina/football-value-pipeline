# Football model — performance and improvement review

_Forward-only evaluation · all reported results must be verified 90-minute scores_

## Verdict

**NOT EVALUABLE YET — no verified shortlisted outcomes.**

Do not change model parameters or selection thresholds based on pending fixtures.

## Overall scorecard

| Tracked | Verified | Pending | W–L | Hit rate | Simulated ROI | Profit (units) |
|---|---|---|---|---|---|---|
| 10 | 0 | 10 | — | — | — | — |

**ROI sample:** 0 independently priced, settled selections. Each is simulated at a 1-unit flat stake; no parlays or real-money profit are implied.

## What works by market?

| Market | Graded | Pending | W–L | Hit rate | Sim. ROI |
|---|---|---|---|---|---|
| Under 3.5 | 0 | 5 | — | — | — |
| Over 1.5 | 0 | 3 | — | — | — |
| Home win | 0 | 2 | — | — | — |

_A market needs its own meaningful verified sample. A high hit rate may still lose money at low odds._

**STRICT vs PROVISIONAL**

| Tier | Graded | W–L | Hit rate | Sim. ROI |
|---|---|---|---|---|
| PROVISIONAL | 0 | — | — | — |
| STRICT | 0 | — | — | — |

## Forecast quality

**1X2 multiclass Brier (lower is better):** — (n=0)

_No verified full-fixture prediction grades yet. Direction accuracy and calibration cannot be assessed._

**Calibration:** too few verified observations per probability band to draw a meaningful conclusion (minimum shown: 20).

## Top priorities for model improvement

1. **Collect more forward-verified results.** Archive each forecast before kickoff; grade only matched 90-minute finals. Avoid parameter tuning for now.
2. **Benchmark prediction quality:** compare 1X2 Brier and market-specific hit rates against de-vigged bookmaker probabilities on identical verified fixtures; lower Brier alone is not proof of an edge.
3. **Keep STRICT and PROVISIONAL separate.** Compare their verified ROI and calibration only after each group has sufficient settled observations.

## Data integrity

Tracker state: **AWAITING VERIFIED RESULTS**. Unverified selections: **10**; graded full-fixture forecasts: **0**.

Only Git-archived pre-kickoff selections and verified regulation-time results count. Pending/postponed/ambiguous fixtures are **not** losses. PROVISIONAL selections are exploratory. The report never updates forecasts, thresholds, source grades or snapshots.

_Detailed audit data remains in `../performance/metrics.json`, `shortlist_grades.csv` and `prediction_grades.csv`._

