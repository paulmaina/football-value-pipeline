# v27/v28 price-edge tracking

## Headline: closing-line value first, returns second

| List | View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| value shortlist | per pick | 141 | -2.0% | -2.7% to -1.2% | 29% | 457 | +2.7% | -3.6% to +9.0% |
| value shortlist | per fixture (a match's picks averaged) | 67 | -1.8% | -2.9% to -0.7% | 25% | 180 | +3.5% | -3.9% to +11.0% |
| cagey tier | per pick | 86 | -1.8% | -2.9% to -0.8% | 30% | 271 | +2.6% | -5.5% to +10.7% |
| cagey tier | per fixture (a match's picks averaged) | 42 | -2.2% | -3.2% to -1.1% | 29% | 121 | +3.6% | -4.7% to +11.9% |
| strong master (live) | per pick | 1 | +2.2% | — | 100% | 5 | -1.6% | -51.4% to +48.2% |
| strong master (live) | per fixture (a match's picks averaged) | 1 | +2.2% | — | 100% | 5 | -1.6% | -51.4% to +48.2% |
| today's master (shadow) | per pick | 41 | -2.4% | -3.5% to -1.3% | 22% | 67 | -0.1% | -16.0% to +15.7% |
| today's master (shadow) | per fixture (a match's picks averaged) | 41 | -2.4% | -3.5% to -1.3% | 22% | 67 | -0.1% | -16.0% to +15.7% |

Closing-line value (CLV) leads because it is the less noisy measure: it compares the frozen price with the Pinnacle fair close and does not wait for results. Returns come second: with few matches they are mostly luck. Intervals are mean ± 1.96 standard errors, clustered by fixture. Near-kickoff feed quotes are not verified official closing prices. The headline CLV is clv_report's (the Pinnacle close with the margin removed by the power method). The STOP REVIEW rule and the tables below use this report's own CLV, with the same margin removal, priced from the latest near-kickoff observation after each pick was captured, so the two can still differ slightly.

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 1716 captured recommendations; 1671 graded; 188 distinct fixtures.
cagey: 1134 captured recommendations; 1031 graded; 141 distinct fixtures.
Actual placed bets: NOT_RECORDED

> **STOP REVIEW**: 138 graded picks with mean CLV -2.11% (below zero). Review the policy before relying on further picks.

Reviewed 2026-11-26T15:50:16.338897+00:00. Frozen v27 picks: 470.

**Mean CLV vs Pinnacle close:** -2.11% ± 0.75% (n=138). **Flat-stake profit per bet:** +2.70% ± 6.49% (n=457).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | -0.50% ± 2.05% (n=26) |
| Pinnacle | -2.48% ± 0.78% (n=112) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | -1.98% ± 2.32% (n=30) |
| 1.90-2.10 | -1.95% ± 1.79% (n=26) |
| 2.10-2.40 | -10.12% (n=1) |
| <1.70 | -1.98% ± 0.72% (n=78) |
| >=2.40 | -5.31% ± 6.49% (n=3) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
|  | -3.19% ± 0.71% (n=13) |
| a | -2.09% ± 1.01% (n=98) |
| b | -1.65% ± 1.01% (n=27) |
| c-cagey | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
|  | -2.80% ± 0.72% (n=17) |
| favourite | -1.20% ± 0.99% (n=79) |
| underdog | -3.53% ± 1.48% (n=42) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | -1.65% ± 0.83% (n=105) |
| yes | -3.54% ± 1.56% (n=33) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | -2.03% ± 0.76% (n=134) |
| yes | -4.53% ± 1.44% (n=4) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | -1.79% ± 0.81% (n=113) |
| yes | -3.53% ± 1.78% (n=25) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | -1.99% ± 0.77% (n=130) |
| yes | -4.00% ± 3.21% (n=8) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| any tag | -3.59% ± 1.31% (n=42) |
| no tag | -1.45% ± 0.88% (n=96) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| Q1 cagiest | -3.79% ± 2.00% (n=18) |
| Q2 | -1.89% ± 1.56% (n=17) |
| Q3 | -2.06% ± 1.21% (n=21) |
| Q4 | -0.39% ± 2.91% (n=15) |
| Q5 most open | -1.85% ± 3.19% (n=11) |
| n/a | -2.15% ± 1.24% (n=56) |

## CLV by value_market_group

| group | mean CLV (n) |
|---|---|
| asian_handicap | -2.69% ± 1.24% (n=60) |
| double_chance | -3.02% ± 0.70% (n=23) |
| match_winner | -1.73% ± 1.28% (n=45) |
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

Frozen picks: 82; CLV -2.51% ± 1.12% (n=41); realised profit per bet -0.15% ± 15.86% (n=67). Live master: 112 frozen picks, realised profit per bet -0.81% ± 12.79% (n=112).

Comparison rule (decided 13 Nov 2026, before any live result of the new master): After at least 150 graded matches over at least 3 calendar weeks (on each list), compare flat-stake return per bet at Pinnacle prices: new master minus live master, whole kickoff weeks resampled (the same weeks for both lists), 95% interval. Hit rate, average price, vetoed, ignored and missing-view counts are context only. The new master is better only if the interval is entirely above zero.

Rollback rule (release, decided by Paul 14 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, new master minus old master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top and in the run summary. Nothing switches automatically: Paul decides, and rolling back is setting live to "old".

**Rollback status: OLD MASTER LIVE.** The old master is live (master_shortlist_config.json, live "old"); the rollback rule does not apply.

Release incidents: new master failed (old master published) in 0 runs; comparison baseline missing (old master shadow failed) in 0 runs.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| new master | 67 | 2 | -0.15% | 67.2% | 1.45 |
| live master | 112 | 3 | -0.81% | 67.0% | 1.53 |

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).
Context, new master offers (newest pre-kickoff generation per fixture): 182 offers on 102 fixtures; included (cagey safe) 43; labels: both agree 3, research too optimistic 34, research strongly disagrees 0, one view missing 93, no research check 0, unvalidated view 73; no view 0.

By tier (context only; the comparison rule never reads it):

| tier | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| fill | -1.24% ± 1.26% (n=22) | +11.34% ± 23.51% (n=36) |
| safe | -3.98% ± 1.74% (n=19) | -13.48% ± 20.11% (n=31) |

| labels | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.55% ± 2.44% (n=6) | -44.70% ± 46.25% (n=10) |
| both agree | -0.72% ± 1.46% (n=2) | +14.07% ± 60.48% (n=5) |
| one view missing | -1.47% ± 1.36% (n=17) | +5.38% ± 24.92% (n=29) |
| one view missing; unvalidated view | -0.81% ± 4.94% (n=3) | +15.95% ± 57.77% (n=5) |
| research too optimistic | -3.59% ± 2.22% (n=7) | -9.03% ± 53.58% (n=8) |
| research too optimistic; unvalidated view | -8.01% ± 13.72% (n=2) | +22.07% ± 21.73% (n=3) |
| unvalidated view | -2.90% ± 4.31% (n=4) | +19.58% ± 10.45% (n=7) |

## Strong-team master (live since 23 Nov 2026) beside today's master (shadow, the rollback baseline)

Frozen picks: 15; CLV +2.21% (n=1); realised profit per bet -1.58% ± 49.81% (n=5). Research gate (research no-loss at least 0.70 on every pick, since 24 Nov 2026): 5 graded picks (reviewed at 50).

Weak-link flags (flag only, since 24 Nov 2026): 4 flagged picks graded; each reason is reviewed once 50 flagged picks are graded.

| picks | graded | realised profit per bet (n) | mean CLV (n) | observed minus market no-loss (points) |
|---|---|---|---|---|
| weak link | 4 | -7.79% ± 62.36% (n=4) | +2.21% (n=1) | +5.7 |
| not flagged | 1 | +23.26% (n=1) | n/a (0) | +16.3 |
| reason (a) | 0 | n/a (0) | n/a (0) | n/a |
| reason (b) | 4 | -7.79% ± 62.36% (n=4) | +2.21% (n=1) | +5.7 |
| reason (c) | 0 | n/a (0) | n/a (0) | n/a |
| reason (d) | 0 | n/a (0) | n/a (0) | n/a |
| reason (e) | 1 | +37.59% (n=1) | n/a (0) | +38.9 |
| reason (f) | 3 | -10.38% ± 87.90% (n=3) | n/a (0) | +0.3 |
| reason (g) | 0 | n/a (0) | n/a (0) | n/a |

Comparison rule (decided 23 Nov 2026): Decided 23 Nov 2026, before any strong-master pick: after at least 150 graded matches over at least 3 calendar weeks on each list, flat-stake return per bet at Pinnacle prices, strong master minus live master, whole kickoff weeks resampled (the same weeks for both), 95% interval. The strong master is better only if the interval is entirely above zero. Results by market group, tier and research label are context only.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| strong master | 5 | 1 | -1.58% | 60.0% | 1.43 |
| today's master | 67 | 2 | -0.15% | 67.2% | 1.45 |

Rollback rule (strong release, decided by Paul 23 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, strong master minus today's master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top. Nothing switches automatically: Paul decides, and rolling back is setting live to "new".

**Rollback status: WAITING.** waiting for at least 150 graded matches over at least 3 weeks on each list

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).

By tier (context only; the comparison rule never reads it):

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| not proven: fill | n/a (0) | -10.38% ± 87.90% (n=3) |
| not proven: safe | +2.21% (n=1) | +11.63% ± 22.79% (n=2) |
| proven | n/a (0) | n/a (0) |

By market group (context only; the comparison rule never reads it):

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| asian_handicap | +2.21% (n=1) | -1.58% ± 49.81% (n=5) |
| match_result | n/a (0) | n/a (0) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 303; CLV -1.78% ± 0.85% (n=86); realised profit per bet +2.59% ± 7.11% (n=271). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-120-200-v6) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-120-200-v6 (active) | -1.98% ± 26.51% (n=15) | +32.47% (n=1) | -4.44% ± 28.00% (n=14) |
| no-loss-market-reference-v5 | +2.54% ± 7.57% (n=249) | +23.00% ± 33.26% (n=13) | +1.41% ± 7.76% (n=236) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -1.78% ± 0.85% (n=86) | +2.59% ± 7.11% (n=271) |
| value | -2.11% ± 0.75% (n=138) | +2.70% ± 6.49% (n=457) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -1.98% ± 0.56% (n=224) | +2.66% ± 4.85% (n=728) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -0.38% ± 1.23% (n=52) | +7.86% ± 8.11% (n=242) |
| Pinnacle | -2.46% ± 0.62% (n=172) | +0.07% ± 6.04% (n=486) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.27% ± 0.55% (n=21) | -1.49% ± 9.55% (n=118) |
| a | -1.88% ± 0.73% (n=164) | +3.87% ± 6.36% (n=498) |
| b | -1.68% ± 1.00% (n=39) | -0.71% ± 11.43% (n=95) |
| c-cagey | n/a (0) | +14.82% ± 3.70% (n=17) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -3.09% ± 1.25% (n=34) | +3.70% ± 13.29% (n=121) |
| Q2 | -2.02% ± 1.09% (n=37) | -5.32% ± 11.58% (n=125) |
| Q3 | -1.85% ± 0.77% (n=42) | +9.99% ± 11.12% (n=127) |
| Q4 | -0.58% ± 1.87% (n=31) | +2.91% ± 11.24% (n=121) |
| Q5 most open | -1.97% ± 2.38% (n=24) | +3.36% ± 10.35% (n=108) |
| n/a | -2.15% ± 1.24% (n=56) | +1.35% ± 13.13% (n=126) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.52% ± 0.66% (n=165) | +2.29% ± 5.75% (n=517) |
| yes | -3.27% ± 1.04% (n=59) | +3.55% ± 9.05% (n=211) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.90% ± 0.58% (n=216) | +2.37% ± 5.03% (n=681) |
| yes | -4.24% ± 1.07% (n=8) | +6.81% ± 18.74% (n=47) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.65% ± 0.64% (n=180) | +2.30% ± 5.30% (n=589) |
| yes | -3.31% ± 1.13% (n=44) | +4.18% ± 11.93% (n=139) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.91% ± 0.58% (n=211) | +2.46% ± 5.00% (n=672) |
| yes | -3.16% ± 2.12% (n=13) | +5.01% ± 19.65% (n=56) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.98% ± 0.56% (n=224) | +2.66% ± 4.85% (n=728) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -2.11% ± 0.75% (n=138) | +2.70% ± 6.49% (n=457) |
| narrow-63-flagged-v2 | -6.39% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-120-200-v6 | -4.70% ± 3.51% (n=9) | -1.98% ± 26.51% (n=15) |
| no-loss-market-reference-v5 | -1.37% ± 0.84% (n=76) | +2.54% ± 7.57% (n=249) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -2.15% ± 0.85% (n=79) | +1.45% ± 7.35% (n=255) |
| n/a | -2.11% ± 0.75% (n=138) | +2.70% ± 6.49% (n=457) |
| value | +2.43% ± 3.06% (n=7) | +20.72% ± 27.13% (n=16) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 3259 (3259 with an offered price).
1xBet edge vs fair at capture: -3.80% ± 0.21% (n=529).
Return at the capture fair price, all tagged lines: +0.97% ± 3.60% (n=2305); plus lines only: +2.12% ± 2.81% (n=1346).

- balanced: +1.94% ± 3.90% (n=2003)
- low_total: -3.67% ± 9.47% (n=274)
- high_draw: -0.01% ± 5.57% (n=954)
- even_odds: +2.05% ± 9.42% (n=398)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 180, pending 31, graded 149, excluded 121.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: over_2_5) | 88 |
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 33 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 5 | 40.0% [25.0%, 100.0%] | 28.2% | 32.2% | 0.0% [0.0%, 0.0%] | 9.7% | 11.3% |
| Q2 | 20 | 25.0% [25.0%, 25.0%] | 31.3% | 34.0% | 0.0% [0.0%, 0.0%] | 11.1% | 12.4% |
| Q3 | 34 | 23.5% [20.8%, 33.3%] | 34.8% | 36.7% | 8.8% [4.2%, 33.3%] | 13.7% | 14.4% |
| Q4 | 55 | 41.8% [28.6%, 50.0%] | 40.2% | 41.0% | 9.1% [7.1%, 16.7%] | 18.1% | 18.0% |
| Q5 most open | 35 | 40.0% [20.0%, 50.0%] | 53.8% | 54.6% | 25.7% [0.0%, 33.3%] | 31.1% | 31.3% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6488 | 0.6509 | +2.097 [-3.629, +4.233] (n=149) |
| 3+ margin | 0.3519 | 0.3573 | +5.350 [-4.390, +7.870] (n=149) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +3.504% [-0.062, +13.129] (n=1490)
- at the uncorrected fair price: +4.339% [+0.988, +13.547] (n=1490)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (power method, as clv_report). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
