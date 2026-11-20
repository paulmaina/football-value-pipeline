# v27/v28 price-edge tracking

## Headline: closing-line value first, returns second

| List | View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| value shortlist | per pick | 49 | -1.6% | -2.9% to -0.3% | 27% | 307 | +3.7% | -3.8% to +11.1% |
| value shortlist | per fixture (a match's picks averaged) | 19 | -0.2% | -2.2% to +1.7% | 37% | 96 | +2.8% | -5.3% to +10.9% |
| cagey tier | per pick | 38 | -0.7% | -2.2% to +0.7% | 32% | 199 | +5.6% | -3.0% to +14.2% |
| cagey tier | per fixture (a match's picks averaged) | 15 | -0.9% | -2.4% to +0.5% | 27% | 79 | +6.8% | -0.7% to +14.3% |
| new master (live) | per pick | 0 | — | — | — | 0 | — | — |
| new master (live) | per fixture (a match's picks averaged) | 0 | — | — | — | 0 | — | — |
| old master (shadow) | per pick | 10 | +0.9% | -3.8% to +5.5% | 50% | 61 | +0.9% | -16.0% to +17.8% |
| old master (shadow) | per fixture (a match's picks averaged) | 10 | +0.9% | -3.8% to +5.5% | 50% | 61 | +0.9% | -16.0% to +17.8% |

Closing-line value (CLV) leads because it is the less noisy measure: it compares the frozen price with the Pinnacle fair close and does not wait for results. Returns come second: with few matches they are mostly luck. Intervals are mean ± 1.96 standard errors, clustered by fixture. Near-kickoff feed quotes are not verified official closing prices. The headline CLV is clv_report's (the Pinnacle close with the margin removed by the power method). The STOP REVIEW rule and the tables below use this report's own CLV, with the same margin removal, priced from the latest near-kickoff observation after each pick was captured, so the two can still differ slightly.

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 1187 captured recommendations; 1102 graded; 122 distinct fixtures.
cagey: 939 captured recommendations; 875 graded; 99 distinct fixtures.
Actual placed bets: NOT_RECORDED

Reviewed 2026-11-20T16:54:18.918847+00:00. Frozen v27 picks: 361.

**Mean CLV vs Pinnacle close:** -1.73% ± 1.29% (n=49). **Flat-stake profit per bet:** +3.67% ± 7.46% (n=307).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | -0.50% ± 2.05% (n=26) |
| Pinnacle | -3.12% ± 1.30% (n=23) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | +1.17% ± 12.54% (n=3) |
| 1.90-2.10 | -0.40% ± 4.28% (n=8) |
| 2.10-2.40 | -10.12% (n=1) |
| <1.70 | -1.74% ± 0.99% (n=34) |
| >=2.40 | -5.31% ± 6.49% (n=3) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
|  | -3.19% ± 0.71% (n=13) |
| a | -1.36% ± 1.79% (n=34) |
| b | +1.39% ± 4.24% (n=2) |
| c-cagey | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
|  | -2.80% ± 0.72% (n=17) |
| favourite | +0.02% ± 2.33% (n=22) |
| underdog | -3.75% ± 2.88% (n=10) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | -0.34% ± 1.62% (n=30) |
| yes | -3.92% ± 1.74% (n=19) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | -1.48% ± 1.37% (n=45) |
| yes | -4.53% ± 1.44% (n=4) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | -1.11% ± 1.57% (n=37) |
| yes | -3.63% ± 1.71% (n=12) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | -1.39% ± 1.29% (n=45) |
| yes | -5.59% ± 5.45% (n=4) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| any tag | -4.03% ± 1.45% (n=23) |
| no tag | +0.30% ± 1.73% (n=26) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| Q1 cagiest | -4.45% ± 2.33% (n=10) |
| Q2 | -2.92% ± 1.80% (n=11) |
| Q3 | -2.24% ± 1.73% (n=13) |
| Q4 | +0.81% ± 3.66% (n=11) |
| Q5 most open | +2.73% ± 4.57% (n=3) |
| n/a | +3.84% (n=1) |

## CLV by value_market_group

| group | mean CLV (n) |
|---|---|
| asian_handicap | -2.95% ± 2.03% (n=12) |
| double_chance | -2.77% ± 0.85% (n=14) |
| match_winner | -2.18% ± 3.37% (n=13) |
| n/a | +5.47% ± 3.69% (n=5) |
| over_1_5 | -1.91% ± 1.42% (n=5) |

## Master shortlist: new master (live since 14 Nov 2026) beside the old master (shadow)

Frozen picks: 18; CLV n/a (0); realised profit per bet n/a (0). Old master: 79 frozen picks, realised profit per bet +0.90% ± 16.86% (n=61).

Comparison rule (decided 13 Nov 2026, before any live result of the new master): After at least 150 graded matches over at least 3 calendar weeks (on each list), compare flat-stake return per bet at Pinnacle prices: new master minus live master, whole kickoff weeks resampled (the same weeks for both lists), 95% interval. Hit rate, average price, vetoed, ignored and missing-view counts are context only. The new master is better only if the interval is entirely above zero.

Rollback rule (release, decided by Paul 14 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, new master minus old master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top and in the run summary. Nothing switches automatically: Paul decides, and rolling back is setting live to "old".

**Rollback status: WAITING.** Not triggered: waiting for at least 150 graded matches over at least 3 weeks on each list.

Release incidents: new master failed (old master published) in 0 runs; comparison baseline missing (old master shadow failed) in 0 runs.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| new master | 0 | 0 | n/a | n/a | n/a |
| old master | 61 | 1 | +0.90% | 67.2% | 1.57 |

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).
Context, new master offers (newest pre-kickoff generation per fixture): 58 offers on 24 fixtures; included (cagey safe) 23; labels: both agree 3, research too optimistic 18, research strongly disagrees 0, one view missing 18, no research check 0, unvalidated view 0; no view 0.

By tier (context only; the comparison rule never reads it):

| tier | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| fill | n/a (0) | n/a (0) |
| safe | n/a (0) | n/a (0) |

| labels | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | n/a (0) | n/a (0) |
| both agree | n/a (0) | n/a (0) |
| one view missing | n/a (0) | n/a (0) |
| research too optimistic | n/a (0) | n/a (0) |

## Old master (shadow since 14 Nov 2026; master_shortlist_old.csv)

Frozen picks: 79; CLV +0.58% ± 4.63% (n=10); realised profit per bet +0.90% ± 16.86% (n=61).

| price flag | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below value threshold | -0.95% ± 6.95% (n=4) | -21.95% ± 44.11% (n=19) |
| negative market EV nomination | -2.84% ± 2.55% (n=2) | +13.07% ± 11.15% (n=30) |
| value | +3.82% ± 9.37% (n=4) | +6.67% ± 39.87% (n=12) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 241; CLV -0.57% ± 1.12% (n=39); realised profit per bet +5.58% ± 7.63% (n=199). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-v5) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-v5 (active) | +5.26% ± 7.89% (n=192) | +33.25% ± 28.82% (n=12) | +3.39% ± 8.14% (n=180) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -0.57% ± 1.12% (n=39) | +5.58% ± 7.63% (n=199) |
| value | -1.73% ± 1.29% (n=49) | +3.67% ± 7.46% (n=307) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -1.22% ± 0.88% (n=88) | +4.42% ± 5.43% (n=506) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -0.38% ± 1.23% (n=52) | +7.86% ± 8.11% (n=242) |
| Pinnacle | -2.42% ± 1.09% (n=36) | +1.27% ± 7.27% (n=264) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.27% ± 0.55% (n=21) | -1.49% ± 9.55% (n=118) |
| a | -0.72% ± 1.17% (n=60) | +6.26% ± 7.46% (n=326) |
| b | +0.73% ± 3.02% (n=7) | +2.64% ± 13.28% (n=45) |
| c-cagey | n/a (0) | +14.82% ± 3.70% (n=17) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -3.56% ± 1.51% (n=15) | +3.85% ± 14.20% (n=92) |
| Q2 | -2.58% ± 1.46% (n=23) | -7.64% ± 13.11% (n=96) |
| Q3 | -1.85% ± 1.07% (n=24) | +10.82% ± 11.61% (n=105) |
| Q4 | +1.73% ± 2.42% (n=19) | +6.62% ± 12.46% (n=99) |
| Q5 most open | +2.24% ± 2.30% (n=6) | +6.50% ± 11.35% (n=87) |
| n/a | +3.84% (n=1) | +9.56% ± 18.98% (n=27) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -0.09% ± 1.10% (n=54) | +7.12% ± 6.37% (n=344) |
| yes | -3.00% ± 1.25% (n=34) | -1.32% ± 10.19% (n=162) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -0.91% ± 0.93% (n=80) | +4.08% ± 5.66% (n=462) |
| yes | -4.24% ± 1.07% (n=8) | +8.00% ± 19.37% (n=44) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -0.52% ± 1.08% (n=65) | +5.28% ± 5.93% (n=402) |
| yes | -3.19% ± 1.08% (n=23) | +1.09% ± 13.14% (n=104) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.01% ± 0.88% (n=82) | +5.41% ± 5.55% (n=464) |
| yes | -4.03% ± 4.04% (n=6) | -6.50% ± 22.70% (n=42) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.22% ± 0.88% (n=88) | +4.42% ± 5.43% (n=506) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -1.73% ± 1.29% (n=49) | +3.67% ± 7.46% (n=307) |
| narrow-63-flagged-v2 | -6.39% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-v5 | -0.42% ± 1.11% (n=38) | +5.26% ± 7.89% (n=192) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -1.23% ± 1.06% (n=33) | +3.84% ± 7.94% (n=185) |
| n/a | -1.73% ± 1.29% (n=49) | +3.67% ± 7.46% (n=307) |
| value | +3.09% ± 3.28% (n=6) | +28.50% ± 25.34% (n=14) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 2551 (2551 with an offered price).
1xBet edge vs fair at capture: -3.80% ± 0.21% (n=529).
Return at the capture fair price, all tagged lines: +0.75% ± 3.94% (n=1889); plus lines only: +2.73% ± 3.07% (n=1101).

- balanced: +1.86% ± 4.34% (n=1616)
- low_total: -4.91% ± 9.18% (n=259)
- high_draw: -0.61% ± 6.26% (n=709)
- even_odds: +2.95% ± 11.65% (n=292)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 133, pending 27, graded 106, excluded 57.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: over_2_5) | 41 |
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 16 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 4 | 25.0% [25.0%, 25.0%] | 28.1% | 32.4% | 0.0% [0.0%, 0.0%] | 9.8% | 11.4% |
| Q2 | 12 | 25.0% [25.0%, 25.0%] | 31.1% | 34.0% | 0.0% [0.0%, 0.0%] | 11.0% | 12.4% |
| Q3 | 24 | 20.8% [20.8%, 20.8%] | 35.0% | 36.9% | 4.2% [4.2%, 4.2%] | 13.9% | 14.6% |
| Q4 | 42 | 42.9% [42.9%, 42.9%] | 40.2% | 41.0% | 7.1% [7.1%, 7.1%] | 18.1% | 18.0% |
| Q5 most open | 24 | 41.7% [41.7%, 41.7%] | 53.9% | 54.6% | 29.2% [29.2%, 29.2%] | 31.2% | 31.3% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6423 | 0.6466 | +4.233 [+4.233, +4.233] (n=106) |
| 3+ margin | 0.3257 | 0.3336 | +7.870 [+7.870, +7.870] (n=106) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +3.085% [+3.085, +3.085] (n=1060)
- at the uncorrected fair price: +3.920% [+3.920, +3.920] (n=1060)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (power method, as clv_report). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
