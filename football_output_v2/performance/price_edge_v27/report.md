# v27/v28 price-edge tracking

## Headline: closing-line value first, returns second

| List | View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| value shortlist | per pick | 122 | -1.9% | -2.7% to -1.1% | 29% | 426 | +2.8% | -3.9% to +9.5% |
| value shortlist | per fixture (a match's picks averaged) | 57 | -1.6% | -2.8% to -0.4% | 28% | 162 | +4.2% | -3.8% to +12.1% |
| cagey tier | per pick | 75 | -1.6% | -2.6% to -0.6% | 32% | 254 | +3.7% | -4.8% to +12.1% |
| cagey tier | per fixture (a match's picks averaged) | 35 | -1.9% | -2.9% to -0.8% | 29% | 110 | +4.6% | -4.2% to +13.4% |
| strong master (live) | per pick | 0 | — | — | — | 0 | — | — |
| strong master (live) | per fixture (a match's picks averaged) | 0 | — | — | — | 0 | — | — |
| today's master (shadow) | per pick | 32 | -2.1% | -3.1% to -1.1% | 22% | 52 | -5.6% | -25.2% to +13.9% |
| today's master (shadow) | per fixture (a match's picks averaged) | 32 | -2.1% | -3.1% to -1.1% | 22% | 52 | -5.6% | -25.2% to +13.9% |

Closing-line value (CLV) leads because it is the less noisy measure: it compares the frozen price with the Pinnacle fair close and does not wait for results. Returns come second: with few matches they are mostly luck. Intervals are mean ± 1.96 standard errors, clustered by fixture. Near-kickoff feed quotes are not verified official closing prices. The headline CLV is clv_report's (the Pinnacle close with the margin removed by the power method). The STOP REVIEW rule and the tables below use this report's own CLV, with the same margin removal, priced from the latest near-kickoff observation after each pick was captured, so the two can still differ slightly.

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 1618 captured recommendations; 1579 graded; 173 distinct fixtures.
cagey: 1010 captured recommendations; 980 graded; 118 distinct fixtures.
Actual placed bets: NOT_RECORDED

> **STOP REVIEW**: 122 graded picks with mean CLV -1.95% (below zero). Review the policy before relying on further picks.

Reviewed 2026-11-24T12:10:50.244615+00:00. Frozen v27 picks: 448.

**Mean CLV vs Pinnacle close:** -1.95% ± 0.78% (n=122). **Flat-stake profit per bet:** +2.83% ± 6.78% (n=426).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | -0.50% ± 2.05% (n=26) |
| Pinnacle | -2.34% ± 0.82% (n=96) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | -1.71% ± 2.34% (n=29) |
| 1.90-2.10 | -1.95% ± 1.79% (n=26) |
| 2.10-2.40 | -10.12% (n=1) |
| <1.70 | -1.77% ± 0.70% (n=63) |
| >=2.40 | -5.31% ± 6.49% (n=3) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
|  | -3.19% ± 0.71% (n=13) |
| a | -1.92% ± 1.09% (n=85) |
| b | -1.37% ± 0.91% (n=24) |
| c-cagey | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
|  | -2.80% ± 0.72% (n=17) |
| favourite | -0.99% ± 1.02% (n=70) |
| underdog | -3.46% ± 1.67% (n=35) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | -1.33% ± 0.87% (n=91) |
| yes | -3.77% ± 1.59% (n=31) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | -1.86% ± 0.80% (n=118) |
| yes | -4.53% ± 1.44% (n=4) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | -1.54% ± 0.86% (n=97) |
| yes | -3.53% ± 1.78% (n=25) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | -1.81% ± 0.80% (n=114) |
| yes | -4.00% ± 3.21% (n=8) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| any tag | -3.77% ± 1.33% (n=40) |
| no tag | -1.06% ± 0.92% (n=82) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| Q1 cagiest | -3.79% ± 2.00% (n=18) |
| Q2 | -2.26% ± 1.47% (n=16) |
| Q3 | -1.96% ± 1.26% (n=20) |
| Q4 | -0.39% ± 2.91% (n=15) |
| Q5 most open | +1.63% ± 3.36% (n=5) |
| n/a | -2.01% ± 1.35% (n=48) |

## CLV by value_market_group

| group | mean CLV (n) |
|---|---|
| asian_handicap | -2.50% ± 1.35% (n=50) |
| double_chance | -3.02% ± 0.70% (n=23) |
| match_winner | -1.57% ± 1.38% (n=39) |
| n/a | +5.47% ± 3.69% (n=5) |
| over_1_5 | -1.91% ± 1.42% (n=5) |

## Master shortlist (10 best bets per run)

Frozen picks: 112; CLV -1.02% ± 1.37% (n=41); realised profit per bet -0.81% ± 12.79% (n=112).

| price flag | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below value threshold | -0.95% ± 6.95% (n=4) | -21.95% ± 44.11% (n=19) |
| negative market EV nomination | -1.61% ± 0.99% (n=33) | +3.05% ± 13.14% (n=81) |
| value | +3.82% ± 9.37% (n=4) | +6.67% ± 39.87% (n=12) |

## New master (shadow, fill rule) beside the live master

Frozen picks: 60; CLV -2.28% ± 1.02% (n=32); realised profit per bet -5.63% ± 19.52% (n=52). Live master: 112 frozen picks, realised profit per bet -0.81% ± 12.79% (n=112).

Comparison rule (decided 13 Nov 2026, before any live result of the new master): After at least 150 graded matches over at least 3 calendar weeks (on each list), compare flat-stake return per bet at Pinnacle prices: new master minus live master, whole kickoff weeks resampled (the same weeks for both lists), 95% interval. Hit rate, average price, vetoed, ignored and missing-view counts are context only. The new master is better only if the interval is entirely above zero.

Rollback rule (release, decided by Paul 14 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, new master minus old master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top and in the run summary. Nothing switches automatically: Paul decides, and rolling back is setting live to "old".

**Rollback status: OLD MASTER LIVE.** The old master is live (master_shortlist_config.json, live "old"); the rollback rule does not apply.

Release incidents: new master failed (old master published) in 0 runs; comparison baseline missing (old master shadow failed) in 0 runs.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| new master | 52 | 2 | -5.63% | 65.4% | 1.47 |
| live master | 112 | 3 | -0.81% | 67.0% | 1.53 |

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).
Context, new master offers (newest pre-kickoff generation per fixture): 133 offers on 75 fixtures; included (cagey safe) 28; labels: both agree 3, research too optimistic 18, research strongly disagrees 0, one view missing 86, no research check 0, unvalidated view 24; no view 0.

By tier (context only; the comparison rule never reads it):

| tier | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| fill | -1.15% ± 1.27% (n=19) | +5.43% ± 27.74% (n=30) |
| safe | -3.93% ± 1.28% (n=13) | -20.72% ± 25.82% (n=22) |

| labels | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.55% ± 2.44% (n=6) | -44.70% ± 46.25% (n=10) |
| both agree | -0.72% ± 1.46% (n=2) | +14.07% ± 60.48% (n=5) |
| one view missing | -1.47% ± 1.36% (n=17) | +5.38% ± 24.92% (n=29) |
| one view missing; unvalidated view | n/a (0) | n/a (0) |
| research too optimistic | -3.59% ± 2.22% (n=7) | -9.03% ± 53.58% (n=8) |
| research too optimistic; unvalidated view | n/a (0) | n/a (0) |
| unvalidated view | n/a (0) | n/a (0) |

## Strong-team master (live since 23 Nov 2026) beside today's master (shadow, the rollback baseline)

Frozen picks: 0; CLV n/a (0); realised profit per bet n/a (0). Research gate (research no-loss at least 0.70 on every pick, since 24 Nov 2026): 0 graded picks (reviewed at 50).

Weak-link flags (flag only, since 24 Nov 2026): 0 flagged picks graded; each reason is reviewed once 50 flagged picks are graded.

| picks | graded | realised profit per bet (n) | mean CLV (n) | observed minus market no-loss (points) |
|---|---|---|---|---|
| weak link | 0 | n/a (0) | n/a (0) | n/a |
| not flagged | 0 | n/a (0) | n/a (0) | n/a |
| reason (a) | 0 | n/a (0) | n/a (0) | n/a |
| reason (b) | 0 | n/a (0) | n/a (0) | n/a |
| reason (c) | 0 | n/a (0) | n/a (0) | n/a |
| reason (d) | 0 | n/a (0) | n/a (0) | n/a |
| reason (e) | 0 | n/a (0) | n/a (0) | n/a |
| reason (f) | 0 | n/a (0) | n/a (0) | n/a |
| reason (g) | 0 | n/a (0) | n/a (0) | n/a |

Comparison rule (decided 23 Nov 2026): Decided 23 Nov 2026, before any strong-master pick: after at least 150 graded matches over at least 3 calendar weeks on each list, flat-stake return per bet at Pinnacle prices, strong master minus live master, whole kickoff weeks resampled (the same weeks for both), 95% interval. The strong master is better only if the interval is entirely above zero. Results by market group, tier and research label are context only.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| strong master | 0 | 0 | n/a | n/a | n/a |
| today's master | 52 | 2 | -5.63% | 65.4% | 1.47 |

Rollback rule (strong release, decided by Paul 23 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, strong master minus today's master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top. Nothing switches automatically: Paul decides, and rolling back is setting live to "new".

**Rollback status: WAITING.** waiting for at least 150 graded matches over at least 3 weeks on each list

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).

## Both tiers (value and cagey)

Cagey-tier picks frozen: 269; CLV -1.44% ± 0.84% (n=77); realised profit per bet +3.67% ± 7.34% (n=254). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-120-200-v6) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-v5 | +3.37% ± 7.54% (n=247) | +23.00% ± 33.26% (n=13) | +2.27% ± 7.74% (n=234) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -1.44% ± 0.84% (n=77) | +3.67% ± 7.34% (n=254) |
| value | -1.95% ± 0.78% (n=122) | +2.83% ± 6.78% (n=426) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -1.75% ± 0.58% (n=199) | +3.14% ± 5.05% (n=680) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -0.38% ± 1.23% (n=52) | +7.86% ± 8.11% (n=242) |
| Pinnacle | -2.24% ± 0.64% (n=147) | +0.54% ± 6.44% (n=438) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.27% ± 0.55% (n=21) | -1.49% ± 9.55% (n=118) |
| a | -1.64% ± 0.76% (n=144) | +4.49% ± 6.73% (n=457) |
| b | -1.28% ± 0.93% (n=34) | +0.09% ± 11.86% (n=88) |
| c-cagey | n/a (0) | +14.82% ± 3.70% (n=17) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -3.55% ± 1.26% (n=31) | +2.73% ± 13.63% (n=114) |
| Q2 | -1.71% ± 1.06% (n=36) | -5.18% ± 12.35% (n=119) |
| Q3 | -2.06% ± 0.80% (n=36) | +10.70% ± 11.41% (n=115) |
| Q4 | +0.50% ± 1.88% (n=28) | +4.52% ± 11.97% (n=112) |
| Q5 most open | -1.01% ± 2.16% (n=20) | +6.21% ± 10.13% (n=108) |
| n/a | -2.01% ± 1.35% (n=48) | +0.30% ± 14.25% (n=112) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.15% ± 0.66% (n=145) | +3.01% ± 5.99% (n=481) |
| yes | -3.37% ± 1.07% (n=54) | +3.47% ± 9.45% (n=199) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.65% ± 0.60% (n=191) | +2.87% ± 5.25% (n=633) |
| yes | -4.24% ± 1.07% (n=8) | +6.81% ± 18.74% (n=47) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.31% ± 0.66% (n=155) | +2.72% ± 5.56% (n=543) |
| yes | -3.31% ± 1.13% (n=44) | +4.80% ± 12.01% (n=137) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.65% ± 0.60% (n=186) | +2.93% ± 5.20% (n=628) |
| yes | -3.16% ± 2.12% (n=13) | +5.69% ± 20.74% (n=52) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.75% ± 0.58% (n=199) | +3.14% ± 5.05% (n=680) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -1.95% ± 0.78% (n=122) | +2.83% ± 6.78% (n=426) |
| narrow-63-flagged-v2 | -6.39% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-v5 | -1.37% ± 0.84% (n=76) | +3.37% ± 7.54% (n=247) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -1.82% ± 0.81% (n=71) | +2.65% ± 7.59% (n=239) |
| n/a | -1.95% ± 0.78% (n=122) | +2.83% ± 6.78% (n=426) |
| value | +3.09% ± 3.28% (n=6) | +19.93% ± 28.96% (n=15) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 2855 (2855 with an offered price).
1xBet edge vs fair at capture: -3.80% ± 0.21% (n=529).
Return at the capture fair price, all tagged lines: +0.97% ± 3.74% (n=2169); plus lines only: +1.61% ± 2.94% (n=1261).

- balanced: +2.01% ± 4.09% (n=1867)
- low_total: -3.67% ± 9.47% (n=274)
- high_draw: -0.07% ± 5.68% (n=925)
- even_odds: +2.83% ± 10.47% (n=346)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 153, pending 15, graded 138, excluded 88.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: over_2_5) | 57 |
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 31 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 5 | 40.0% [25.0%, 100.0%] | 28.2% | 32.2% | 0.0% [0.0%, 0.0%] | 9.7% | 11.3% |
| Q2 | 20 | 25.0% [25.0%, 25.0%] | 31.3% | 34.0% | 0.0% [0.0%, 0.0%] | 11.1% | 12.4% |
| Q3 | 33 | 24.2% [20.8%, 50.0%] | 34.9% | 36.8% | 9.1% [4.2%, 50.0%] | 13.8% | 14.5% |
| Q4 | 50 | 46.0% [42.9%, 100.0%] | 40.2% | 41.2% | 10.0% [7.1%, 50.0%] | 18.2% | 18.2% |
| Q5 most open | 30 | 43.3% [41.7%, 50.0%] | 53.6% | 54.4% | 30.0% [29.2%, 33.3%] | 30.9% | 31.2% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6527 | 0.6547 | +1.907 [-20.981, +4.233] (n=138) |
| 3+ margin | 0.3580 | 0.3638 | +5.802 [-15.586, +7.870] (n=138) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +1.745% [-21.118, +3.085] (n=1380)
- at the uncorrected fair price: +2.613% [-20.656, +3.920] (n=1380)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (power method, as clv_report). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
