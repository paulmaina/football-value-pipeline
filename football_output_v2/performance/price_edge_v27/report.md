# v27/v28 price-edge tracking

## Headline: closing-line value first, returns second

| List | View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| value shortlist | per pick | 118 | -1.9% | -2.7% to -1.1% | 29% | 420 | +2.8% | -3.8% to +9.5% |
| value shortlist | per fixture (a match's picks averaged) | 54 | -1.7% | -2.9% to -0.5% | 28% | 158 | +3.9% | -4.0% to +11.9% |
| cagey tier | per pick | 71 | -1.4% | -2.4% to -0.3% | 34% | 248 | +4.2% | -4.1% to +12.6% |
| cagey tier | per fixture (a match's picks averaged) | 32 | -1.5% | -2.5% to -0.5% | 31% | 106 | +5.6% | -3.0% to +14.2% |
| strong master (live) | per pick | 0 | — | — | — | 0 | — | — |
| strong master (live) | per fixture (a match's picks averaged) | 0 | — | — | — | 0 | — | — |
| today's master (shadow) | per pick | 29 | -1.7% | -2.8% to -0.7% | 24% | 48 | -3.4% | -23.7% to +16.9% |
| today's master (shadow) | per fixture (a match's picks averaged) | 29 | -1.7% | -2.8% to -0.7% | 24% | 48 | -3.4% | -23.7% to +16.9% |

Closing-line value (CLV) leads because it is the less noisy measure: it compares the frozen price with the Pinnacle fair close and does not wait for results. Returns come second: with few matches they are mostly luck. Intervals are mean ± 1.96 standard errors, clustered by fixture. Near-kickoff feed quotes are not verified official closing prices. The headline CLV is clv_report's (the Pinnacle close with the margin removed by the power method). The STOP REVIEW rule and the tables below use this report's own CLV, with the same margin removal, priced from the latest near-kickoff observation after each pick was captured, so the two can still differ slightly.

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 1600 captured recommendations; 1569 graded; 166 distinct fixtures.
cagey: 998 captured recommendations; 970 graded; 113 distinct fixtures.
Actual placed bets: NOT_RECORDED

> **STOP REVIEW**: 118 graded picks with mean CLV -1.98% (below zero). Review the policy before relying on further picks.

Reviewed 2026-11-23T19:23:23.114122+00:00. Frozen v27 picks: 433.

**Mean CLV vs Pinnacle close:** -1.98% ± 0.80% (n=118). **Flat-stake profit per bet:** +2.84% ± 6.83% (n=420).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | -0.50% ± 2.05% (n=26) |
| Pinnacle | -2.39% ± 0.83% (n=92) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | -1.71% ± 2.34% (n=29) |
| 1.90-2.10 | -1.86% ± 1.85% (n=25) |
| 2.10-2.40 | -10.12% (n=1) |
| <1.70 | -1.85% ± 0.67% (n=60) |
| >=2.40 | -5.31% ± 6.49% (n=3) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
|  | -3.19% ± 0.71% (n=13) |
| a | -1.96% ± 1.12% (n=81) |
| b | -1.37% ± 0.91% (n=24) |
| c-cagey | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
|  | -2.80% ± 0.72% (n=17) |
| favourite | -1.03% ± 1.03% (n=67) |
| underdog | -3.43% ± 1.72% (n=34) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | -1.28% ± 0.89% (n=89) |
| yes | -4.10% ± 1.55% (n=29) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | -1.89% ± 0.82% (n=114) |
| yes | -4.53% ± 1.44% (n=4) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | -1.50% ± 0.87% (n=95) |
| yes | -3.92% ± 1.73% (n=23) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | -1.83% ± 0.82% (n=110) |
| yes | -4.00% ± 3.21% (n=8) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| any tag | -4.02% ± 1.29% (n=38) |
| no tag | -1.00% ± 0.93% (n=80) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| Q1 cagiest | -4.39% ± 1.72% (n=17) |
| Q2 | -2.26% ± 1.47% (n=16) |
| Q3 | -1.71% ± 1.51% (n=16) |
| Q4 | -0.10% ± 2.84% (n=15) |
| Q5 most open | +0.54% ± 3.48% (n=6) |
| n/a | -2.01% ± 1.35% (n=48) |

## CLV by value_market_group

| group | mean CLV (n) |
|---|---|
| asian_handicap | -2.64% ± 1.38% (n=47) |
| double_chance | -3.02% ± 0.70% (n=23) |
| match_winner | -1.50% ± 1.41% (n=38) |
| n/a | +5.47% ± 3.69% (n=5) |
| over_1_5 | -1.91% ± 1.42% (n=5) |

## Master shortlist (10 best bets per run)

Frozen picks: 112; CLV -1.12% ± 1.41% (n=38); realised profit per bet -0.99% ± 13.08% (n=108).

| price flag | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below value threshold | -0.95% ± 6.95% (n=4) | -21.95% ± 44.11% (n=19) |
| negative market EV nomination | -1.80% ± 0.92% (n=30) | +2.99% ± 13.47% (n=77) |
| value | +3.82% ± 9.37% (n=4) | +6.67% ± 39.87% (n=12) |

## New master (shadow, fill rule) beside the live master

Frozen picks: 54; CLV -1.95% ± 1.03% (n=29); realised profit per bet -3.40% ± 20.29% (n=48). Live master: 112 frozen picks, realised profit per bet -0.99% ± 13.08% (n=108).

Comparison rule (decided 13 Nov 2026, before any live result of the new master): After at least 150 graded matches over at least 3 calendar weeks (on each list), compare flat-stake return per bet at Pinnacle prices: new master minus live master, whole kickoff weeks resampled (the same weeks for both lists), 95% interval. Hit rate, average price, vetoed, ignored and missing-view counts are context only. The new master is better only if the interval is entirely above zero.

Rollback rule (release, decided by Paul 14 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, new master minus old master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top and in the run summary. Nothing switches automatically: Paul decides, and rolling back is setting live to "old".

**Rollback status: OLD MASTER LIVE.** The old master is live (master_shortlist_config.json, live "old"); the rollback rule does not apply.

Release incidents: new master failed (old master published) in 0 runs; comparison baseline missing (old master shadow failed) in 0 runs.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| new master | 48 | 1 | -3.40% | 66.7% | 1.48 |
| live master | 108 | 2 | -0.99% | 66.7% | 1.53 |

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).
Context, new master offers (newest pre-kickoff generation per fixture): 113 offers on 68 fixtures; included (cagey safe) 16; labels: both agree 3, research too optimistic 11, research strongly disagrees 0, one view missing 82, no research check 0, unvalidated view 4; no view 0.

By tier (context only; the comparison rule never reads it):

| tier | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| fill | -1.15% ± 1.27% (n=19) | +4.53% ± 28.65% (n=29) |
| safe | -3.48% ± 1.40% (n=10) | -15.50% ± 26.71% (n=19) |

| labels | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -2.62% ± 2.83% (n=4) | -30.88% ± 53.98% (n=8) |
| both agree | -0.72% ± 1.46% (n=2) | +9.75% ± 77.30% (n=4) |
| one view missing | -1.47% ± 1.36% (n=17) | +5.38% ± 24.92% (n=29) |
| one view missing; unvalidated view | n/a (0) | n/a (0) |
| research too optimistic | -3.27% ± 2.52% (n=6) | -15.86% ± 59.90% (n=7) |
| unvalidated view | n/a (0) | n/a (0) |

## Strong-team master (live since 23 Nov 2026) beside today's master (shadow, the rollback baseline)

Frozen picks: 5; CLV n/a (0); realised profit per bet n/a (0). Graded European picks: 0 (R3 is reviewed at 50).

Comparison rule (decided 23 Nov 2026): Decided 23 Nov 2026, before any strong-master pick: after at least 150 graded matches over at least 3 calendar weeks on each list, flat-stake return per bet at Pinnacle prices, strong master minus live master, whole kickoff weeks resampled (the same weeks for both), 95% interval. The strong master is better only if the interval is entirely above zero. Results by market group, tier and research label are context only.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| strong master | 0 | 0 | n/a | n/a | n/a |
| today's master | 48 | 1 | -3.40% | 66.7% | 1.48 |

Rollback rule (strong release, decided by Paul 23 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, strong master minus today's master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top. Nothing switches automatically: Paul decides, and rolling back is setting live to "new".

**Rollback status: WAITING.** waiting for at least 150 graded matches over at least 3 weeks on each list

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).

By tier (context only; the comparison rule never reads it):

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| not proven: fill | n/a (0) | n/a (0) |
| not proven: safe | n/a (0) | n/a (0) |

By market group (context only; the comparison rule never reads it):

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| asian_handicap | n/a (0) | n/a (0) |
| match_result | n/a (0) | n/a (0) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 258; CLV -1.23% ± 0.85% (n=73); realised profit per bet +4.22% ± 7.33% (n=248). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-v5) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-v5 (active) | +3.93% ± 7.54% (n=241) | +23.00% ± 33.26% (n=13) | +2.84% ± 7.73% (n=228) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -1.23% ± 0.85% (n=73) | +4.22% ± 7.33% (n=248) |
| value | -1.98% ± 0.80% (n=118) | +2.84% ± 6.83% (n=420) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -1.69% ± 0.59% (n=191) | +3.35% ± 5.08% (n=668) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -0.38% ± 1.23% (n=52) | +7.86% ± 8.11% (n=242) |
| Pinnacle | -2.18% ± 0.65% (n=139) | +0.79% ± 6.49% (n=426) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.27% ± 0.55% (n=21) | -1.49% ± 9.55% (n=118) |
| a | -1.55% ± 0.79% (n=136) | +4.84% ± 6.80% (n=445) |
| b | -1.28% ± 0.93% (n=34) | +0.09% ± 11.86% (n=88) |
| c-cagey | n/a (0) | +14.82% ± 3.70% (n=17) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -3.74% ± 1.12% (n=29) | +3.45% ± 14.09% (n=108) |
| Q2 | -1.71% ± 1.06% (n=36) | -1.82% ± 12.47% (n=114) |
| Q3 | -1.67% ± 0.88% (n=30) | +6.68% ± 12.12% (n=105) |
| Q4 | +0.50% ± 1.88% (n=28) | +2.77% ± 11.87% (n=113) |
| Q5 most open | -1.01% ± 2.16% (n=20) | +8.81% ± 9.69% (n=116) |
| n/a | -2.01% ± 1.35% (n=48) | +0.30% ± 14.25% (n=112) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.08% ± 0.68% (n=141) | +3.32% ± 6.00% (n=473) |
| yes | -3.42% ± 1.07% (n=50) | +3.42% ± 9.57% (n=195) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.58% ± 0.61% (n=183) | +3.09% ± 5.28% (n=621) |
| yes | -4.24% ± 1.07% (n=8) | +6.81% ± 18.74% (n=47) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.25% ± 0.67% (n=151) | +3.00% ± 5.57% (n=535) |
| yes | -3.36% ± 1.12% (n=40) | +4.77% ± 12.23% (n=133) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.58% ± 0.61% (n=178) | +3.15% ± 5.23% (n=616) |
| yes | -3.16% ± 2.12% (n=13) | +5.69% ± 20.74% (n=52) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.69% ± 0.59% (n=191) | +3.35% ± 5.08% (n=668) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -1.98% ± 0.80% (n=118) | +2.84% ± 6.83% (n=420) |
| narrow-63-flagged-v2 | -6.39% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-v5 | -1.16% ± 0.85% (n=72) | +3.93% ± 7.54% (n=241) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -1.62% ± 0.83% (n=67) | +3.21% ± 7.58% (n=233) |
| n/a | -1.98% ± 0.80% (n=118) | +2.84% ± 6.83% (n=420) |
| value | +3.09% ± 3.28% (n=6) | +19.93% ± 28.96% (n=15) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 2781 (2781 with an offered price).
1xBet edge vs fair at capture: -3.80% ± 0.21% (n=529).
Return at the capture fair price, all tagged lines: +1.06% ± 3.78% (n=2114); plus lines only: +1.83% ± 2.97% (n=1227).

- balanced: +2.15% ± 4.14% (n=1812)
- low_total: -3.67% ± 9.47% (n=274)
- high_draw: +0.08% ± 5.82% (n=870)
- even_odds: +2.83% ± 10.47% (n=346)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 149, pending 15, graded 134, excluded 70.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: over_2_5) | 55 |
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 15 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 5 | 40.0% [25.0%, 100.0%] | 28.2% | 32.2% | 0.0% [0.0%, 0.0%] | 9.7% | 11.3% |
| Q2 | 20 | 25.0% [25.0%, 25.0%] | 31.3% | 34.0% | 0.0% [0.0%, 0.0%] | 11.1% | 12.4% |
| Q3 | 31 | 22.6% [20.8%, 28.6%] | 34.9% | 36.8% | 6.5% [4.2%, 14.3%] | 13.8% | 14.5% |
| Q4 | 48 | 43.8% [42.9%, 50.0%] | 40.3% | 41.2% | 8.3% [7.1%, 16.7%] | 18.2% | 18.2% |
| Q5 most open | 30 | 43.3% [41.7%, 50.0%] | 53.6% | 54.4% | 30.0% [29.2%, 33.3%] | 30.9% | 31.2% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6464 | 0.6490 | +2.591 [-3.629, +4.233] (n=134) |
| 3+ margin | 0.3370 | 0.3434 | +6.441 [+1.029, +7.870] (n=134) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +2.427% [-0.062, +3.085] (n=1340)
- at the uncorrected fair price: +3.308% [+0.988, +3.920] (n=1340)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (power method, as clv_report). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
