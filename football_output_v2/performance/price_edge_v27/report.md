# v27/v28 price-edge tracking

## Headline: closing-line value first, returns second

| List | View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| value shortlist | per pick | 116 | -2.0% | -2.8% to -1.1% | 28% | 407 | +2.7% | -4.0% to +9.4% |
| value shortlist | per fixture (a match's picks averaged) | 53 | -1.7% | -3.0% to -0.5% | 26% | 150 | +3.0% | -5.0% to +10.9% |
| cagey tier | per pick | 69 | -1.4% | -2.5% to -0.4% | 32% | 240 | +4.7% | -3.6% to +13.1% |
| cagey tier | per fixture (a match's picks averaged) | 31 | -1.6% | -2.6% to -0.6% | 29% | 101 | +6.8% | -1.6% to +15.1% |
| new master (live) | per pick | 28 | -1.8% | -2.9% to -0.8% | 21% | 41 | -1.0% | -22.6% to +20.7% |
| new master (live) | per fixture (a match's picks averaged) | 28 | -1.8% | -2.9% to -0.8% | 21% | 41 | -1.0% | -22.6% to +20.7% |
| old master (shadow) | per pick | 37 | -0.9% | -2.4% to +0.5% | 30% | 101 | +0.2% | -13.2% to +13.6% |
| old master (shadow) | per fixture (a match's picks averaged) | 37 | -0.9% | -2.4% to +0.5% | 30% | 101 | +0.2% | -13.2% to +13.6% |

Closing-line value (CLV) leads because it is the less noisy measure: it compares the frozen price with the Pinnacle fair close and does not wait for results. Returns come second: with few matches they are mostly luck. Intervals are mean ± 1.96 standard errors, clustered by fixture. Near-kickoff feed quotes are not verified official closing prices. The headline CLV is clv_report's (the Pinnacle close with the margin removed by the power method). The STOP REVIEW rule and the tables below use this report's own CLV, with the same margin removal, priced from the latest near-kickoff observation after each pick was captured, so the two can still differ slightly.

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 1593 captured recommendations; 1510 graded; 164 distinct fixtures.
cagey: 993 captured recommendations; 957 graded; 112 distinct fixtures.
Actual placed bets: NOT_RECORDED

> **STOP REVIEW**: 116 graded picks with mean CLV -2.02% (below zero). Review the policy before relying on further picks.

Reviewed 2026-11-23T08:52:55.168101+00:00. Frozen v27 picks: 430.

**Mean CLV vs Pinnacle close:** -2.02% ± 0.81% (n=116). **Flat-stake profit per bet:** +2.69% ± 6.88% (n=407).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | -0.50% ± 2.05% (n=26) |
| Pinnacle | -2.45% ± 0.84% (n=90) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | -1.71% ± 2.34% (n=29) |
| 1.90-2.10 | -1.97% ± 1.92% (n=24) |
| 2.10-2.40 | -10.12% (n=1) |
| <1.70 | -1.88% ± 0.68% (n=59) |
| >=2.40 | -5.31% ± 6.49% (n=3) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
|  | -3.19% ± 0.71% (n=13) |
| a | -2.02% ± 1.14% (n=79) |
| b | -1.37% ± 0.91% (n=24) |
| c-cagey | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
|  | -2.80% ± 0.72% (n=17) |
| favourite | -1.07% ± 1.06% (n=65) |
| underdog | -3.43% ± 1.72% (n=34) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | -1.32% ± 0.90% (n=87) |
| yes | -4.10% ± 1.55% (n=29) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | -1.93% ± 0.83% (n=112) |
| yes | -4.53% ± 1.44% (n=4) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | -1.55% ± 0.89% (n=93) |
| yes | -3.92% ± 1.73% (n=23) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | -1.87% ± 0.83% (n=108) |
| yes | -4.00% ± 3.21% (n=8) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| any tag | -4.02% ± 1.29% (n=38) |
| no tag | -1.04% ± 0.96% (n=78) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| Q1 cagiest | -4.39% ± 1.72% (n=17) |
| Q2 | -2.26% ± 1.47% (n=16) |
| Q3 | -2.34% ± 1.67% (n=13) |
| Q4 | +0.03% ± 2.67% (n=16) |
| Q5 most open | +0.54% ± 3.48% (n=6) |
| n/a | -2.01% ± 1.35% (n=48) |

## CLV by value_market_group

| group | mean CLV (n) |
|---|---|
| asian_handicap | -2.70% ± 1.41% (n=46) |
| double_chance | -3.02% ± 0.70% (n=23) |
| match_winner | -1.57% ± 1.44% (n=37) |
| n/a | +5.47% ± 3.69% (n=5) |
| over_1_5 | -1.91% ± 1.42% (n=5) |

## Master shortlist: new master (live since 14 Nov 2026) beside the old master (shadow)

Frozen picks: 52; CLV -2.02% ± 1.06% (n=28); realised profit per bet -0.95% ± 21.70% (n=41). Old master: 112 frozen picks, realised profit per bet +0.17% ± 13.42% (n=101).

Comparison rule (decided 13 Nov 2026, before any live result of the new master): After at least 150 graded matches over at least 3 calendar weeks (on each list), compare flat-stake return per bet at Pinnacle prices: new master minus live master, whole kickoff weeks resampled (the same weeks for both lists), 95% interval. Hit rate, average price, vetoed, ignored and missing-view counts are context only. The new master is better only if the interval is entirely above zero.

Rollback rule (release, decided by Paul 14 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, new master minus old master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top and in the run summary. Nothing switches automatically: Paul decides, and rolling back is setting live to "old".

**Rollback status: WAITING.** Not triggered: waiting for at least 150 graded matches over at least 3 weeks on each list.

Release incidents: new master failed (old master published) in 0 runs; comparison baseline missing (old master shadow failed) in 0 runs.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| new master | 41 | 1 | -0.95% | 68.3% | 1.48 |
| old master | 101 | 2 | +0.17% | 67.3% | 1.53 |

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).
Context, new master offers (newest pre-kickoff generation per fixture): 109 offers on 66 fixtures; included (cagey safe) 12; labels: both agree 5, research too optimistic 9, research strongly disagrees 0, one view missing 80, no research check 0, unvalidated view 0; no view 0.

By tier (context only; the comparison rule never reads it):

| tier | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| fill | -1.22% ± 1.34% (n=18) | +7.50% ± 30.16% (n=25) |
| safe | -3.48% ± 1.40% (n=10) | -14.16% ± 29.49% (n=16) |

| labels | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -2.62% ± 2.83% (n=4) | -26.50% ± 67.65% (n=6) |
| both agree | -1.46% (n=1) | -15.33% ± 84.37% (n=3) |
| one view missing | -1.47% ± 1.36% (n=17) | +6.81% ± 26.30% (n=26) |
| research too optimistic | -3.27% ± 2.52% (n=6) | -1.83% ± 62.98% (n=6) |

## Old master (shadow since 14 Nov 2026; master_shortlist_old.csv)

Frozen picks: 112; CLV -1.15% ± 1.45% (n=37); realised profit per bet +0.17% ± 13.42% (n=101).

| price flag | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below value threshold | -0.95% ± 6.95% (n=4) | -21.95% ± 44.11% (n=19) |
| negative market EV nomination | -1.86% ± 0.94% (n=29) | +5.06% ± 13.65% (n=70) |
| value | +3.82% ± 9.37% (n=4) | +6.67% ± 39.87% (n=12) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 257; CLV -1.29% ± 0.87% (n=71); realised profit per bet +4.75% ± 7.37% (n=240). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-v5) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-v5 (active) | +4.46% ± 7.58% (n=233) | +23.00% ± 33.26% (n=13) | +3.37% ± 7.78% (n=220) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -1.29% ± 0.87% (n=71) | +4.75% ± 7.37% (n=240) |
| value | -2.02% ± 0.81% (n=116) | +2.69% ± 6.88% (n=407) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -1.74% ± 0.60% (n=187) | +3.46% ± 5.12% (n=647) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -0.38% ± 1.23% (n=52) | +7.86% ± 8.11% (n=242) |
| Pinnacle | -2.27% ± 0.67% (n=135) | +0.82% ± 6.58% (n=405) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.27% ± 0.55% (n=21) | -1.49% ± 9.55% (n=118) |
| a | -1.62% ± 0.81% (n=132) | +5.04% ± 6.87% (n=428) |
| b | -1.28% ± 0.93% (n=34) | +0.05% ± 12.11% (n=84) |
| c-cagey | n/a (0) | +14.82% ± 3.70% (n=17) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -3.74% ± 1.12% (n=29) | +3.83% ± 14.00% (n=107) |
| Q2 | -1.71% ± 1.06% (n=36) | -5.73% ± 12.85% (n=107) |
| Q3 | -2.03% ± 0.94% (n=26) | +6.67% ± 12.12% (n=105) |
| Q4 | +0.50% ± 1.88% (n=28) | +5.10% ± 11.61% (n=113) |
| Q5 most open | -1.01% ± 2.16% (n=20) | +8.49% ± 9.93% (n=113) |
| n/a | -2.01% ± 1.35% (n=48) | +1.99% ± 14.73% (n=102) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.13% ± 0.70% (n=137) | +3.64% ± 6.04% (n=456) |
| yes | -3.42% ± 1.07% (n=50) | +3.02% ± 9.63% (n=191) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.63% ± 0.62% (n=179) | +3.19% ± 5.32% (n=600) |
| yes | -4.24% ± 1.07% (n=8) | +6.81% ± 18.74% (n=47) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.30% ± 0.69% (n=147) | +3.09% ± 5.62% (n=516) |
| yes | -3.36% ± 1.12% (n=40) | +4.88% ± 12.25% (n=131) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.64% ± 0.63% (n=174) | +3.24% ± 5.27% (n=597) |
| yes | -3.16% ± 2.12% (n=13) | +6.02% ± 20.87% (n=50) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.74% ± 0.60% (n=187) | +3.46% ± 5.12% (n=647) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -2.02% ± 0.81% (n=116) | +2.69% ± 6.88% (n=407) |
| narrow-63-flagged-v2 | -6.39% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-v5 | -1.22% ± 0.88% (n=70) | +4.46% ± 7.58% (n=233) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -1.70% ± 0.85% (n=65) | +3.74% ± 7.62% (n=225) |
| n/a | -2.02% ± 0.81% (n=116) | +2.69% ± 6.88% (n=407) |
| value | +3.09% ± 3.28% (n=6) | +19.93% ± 28.96% (n=15) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 2726 (2726 with an offered price).
1xBet edge vs fair at capture: -3.80% ± 0.21% (n=529).
Return at the capture fair price, all tagged lines: +1.06% ± 3.82% (n=2079); plus lines only: +1.92% ± 3.00% (n=1208).

- balanced: +2.18% ± 4.19% (n=1777)
- low_total: -3.67% ± 9.47% (n=274)
- high_draw: -0.16% ± 5.89% (n=854)
- even_odds: +2.38% ± 10.81% (n=332)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 140, pending 11, graded 129, excluded 72.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: over_2_5) | 56 |
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 16 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 5 | 40.0% [25.0%, 100.0%] | 28.2% | 32.2% | 0.0% [0.0%, 0.0%] | 9.7% | 11.3% |
| Q2 | 19 | 26.3% [25.0%, 28.6%] | 31.4% | 34.1% | 0.0% [0.0%, 0.0%] | 11.1% | 12.5% |
| Q3 | 29 | 24.1% [20.8%, 40.0%] | 35.0% | 36.9% | 6.9% [4.2%, 20.0%] | 13.9% | 14.6% |
| Q4 | 47 | 42.6% [40.0%, 42.9%] | 40.3% | 41.2% | 8.5% [7.1%, 20.0%] | 18.2% | 18.2% |
| Q5 most open | 29 | 44.8% [41.7%, 60.0%] | 53.4% | 54.2% | 31.0% [29.2%, 40.0%] | 30.7% | 30.9% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6482 | 0.6504 | +2.177 [-7.303, +4.233] (n=129) |
| 3+ margin | 0.3418 | 0.3481 | +6.354 [-0.636, +7.870] (n=129) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +1.949% [-3.284, +3.085] (n=1290)
- at the uncorrected fair price: +2.828% [-2.205, +3.920] (n=1290)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (power method, as clv_report). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
