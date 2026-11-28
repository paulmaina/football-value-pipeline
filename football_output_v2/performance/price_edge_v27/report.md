# v27/v28 price-edge tracking

## Headline: closing-line value first, returns second

| List | View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| value shortlist | per pick | 160 | -2.0% | -2.7% to -1.4% | 28% | 476 | +1.4% | -4.8% to +7.6% |
| value shortlist | per fixture (a match's picks averaged) | 80 | -1.9% | -2.9% to -1.0% | 24% | 193 | +1.3% | -6.0% to +8.6% |
| cagey tier | per pick | 127 | -2.2% | -3.1% to -1.3% | 28% | 310 | +1.4% | -6.3% to +9.1% |
| cagey tier | per fixture (a match's picks averaged) | 68 | -2.3% | -3.2% to -1.4% | 26% | 146 | +2.1% | -5.7% to +9.9% |
| strong master (live) | per pick | 17 | -1.9% | -4.0% to +0.1% | 41% | 20 | -13.1% | -39.3% to +13.1% |
| strong master (live) | per fixture (a match's picks averaged) | 17 | -1.9% | -4.0% to +0.1% | 41% | 20 | -13.1% | -39.3% to +13.1% |
| today's master (shadow) | per pick | 63 | -2.4% | -3.4% to -1.4% | 24% | 89 | -4.0% | -17.5% to +9.5% |
| today's master (shadow) | per fixture (a match's picks averaged) | 63 | -2.4% | -3.4% to -1.4% | 24% | 89 | -4.0% | -17.5% to +9.5% |

Closing-line value (CLV) leads because it is the less noisy measure: it compares the frozen price with the Pinnacle fair close and does not wait for results. Returns come second: with few matches they are mostly luck. Intervals are mean ± 1.96 standard errors, clustered by fixture. Near-kickoff feed quotes are not verified official closing prices. The headline CLV is clv_report's (the Pinnacle close with the margin removed by the power method). The STOP REVIEW rule and the tables below use this report's own CLV, with the same margin removal, priced from the latest near-kickoff observation after each pick was captured, so the two can still differ slightly.

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 1843 captured recommendations; 1727 graded; 226 distinct fixtures.
cagey: 1255 captured recommendations; 1146 graded; 178 distinct fixtures.
Actual placed bets: NOT_RECORDED

> **STOP REVIEW**: 157 graded picks with mean CLV -2.16% (below zero). Review the policy before relying on further picks.

Reviewed 2026-11-28T06:38:23.826376+00:00. Frozen v27 picks: 527.

**Mean CLV vs Pinnacle close:** -2.16% ± 0.67% (n=157). **Flat-stake profit per bet:** +1.37% ± 6.37% (n=476).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | -0.50% ± 2.05% (n=26) |
| Pinnacle | -2.48% ± 0.69% (n=131) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | -1.94% ± 2.25% (n=31) |
| 1.90-2.10 | -2.13% ± 1.68% (n=28) |
| 2.10-2.40 | -10.12% (n=1) |
| <1.70 | -2.05% ± 0.65% (n=94) |
| >=2.40 | -5.31% ± 6.49% (n=3) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
|  | -3.19% ± 0.71% (n=13) |
| a | -2.14% ± 0.88% (n=115) |
| b | -1.74% ± 0.95% (n=29) |
| c-cagey | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
|  | -2.80% ± 0.72% (n=17) |
| favourite | -1.51% ± 0.90% (n=90) |
| underdog | -3.10% ± 1.29% (n=50) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | -1.79% ± 0.75% (n=121) |
| yes | -3.40% ± 1.44% (n=36) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | -2.09% ± 0.70% (n=151) |
| yes | -3.91% ± 1.19% (n=6) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | -1.92% ± 0.75% (n=127) |
| yes | -3.17% ± 1.52% (n=30) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | -2.06% ± 0.70% (n=146) |
| yes | -3.41% ± 2.39% (n=11) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| any tag | -3.36% ± 1.20% (n=47) |
| no tag | -1.64% ± 0.80% (n=110) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| Q1 cagiest | -3.13% ± 1.52% (n=25) |
| Q2 | -2.11% ± 1.43% (n=20) |
| Q3 | -1.93% ± 1.17% (n=20) |
| Q4 | -1.04% ± 2.01% (n=23) |
| Q5 most open | -2.69% ± 3.01% (n=13) |
| n/a | -2.15% ± 1.24% (n=56) |

## CLV by value_market_group

| group | mean CLV (n) |
|---|---|
| asian_handicap | -2.47% ± 1.06% (n=72) |
| double_chance | -3.02% ± 0.70% (n=23) |
| match_winner | -2.09% ± 1.17% (n=52) |
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

Frozen picks: 109; CLV -2.46% ± 1.01% (n=63); realised profit per bet -3.99% ± 13.47% (n=89). Live master: 112 frozen picks, realised profit per bet -0.81% ± 12.79% (n=112).

Comparison rule (decided 13 Nov 2026, before any live result of the new master): After at least 150 graded matches over at least 3 calendar weeks (on each list), compare flat-stake return per bet at Pinnacle prices: new master minus live master, whole kickoff weeks resampled (the same weeks for both lists), 95% interval. Hit rate, average price, vetoed, ignored and missing-view counts are context only. The new master is better only if the interval is entirely above zero.

Rollback rule (release, decided by Paul 14 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, new master minus old master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top and in the run summary. Nothing switches automatically: Paul decides, and rolling back is setting live to "old".

**Rollback status: OLD MASTER LIVE.** The old master is live (master_shortlist_config.json, live "old"); the rollback rule does not apply.

Release incidents: new master failed (old master published) in 0 runs; comparison baseline missing (old master shadow failed) in 0 runs.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| new master | 89 | 2 | -3.99% | 62.9% | 1.41 |
| live master | 112 | 3 | -0.81% | 67.0% | 1.53 |

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).
Context, new master offers (newest pre-kickoff generation per fixture): 276 offers on 140 fixtures; included (cagey safe) 94; labels: both agree 6, research too optimistic 69, research strongly disagrees 0, one view missing 95, no research check 0, unvalidated view 73; no view 0.

By tier (context only; the comparison rule never reads it):

| tier | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| fill | -1.25% ± 1.04% (n=28) | +4.20% ± 22.56% (n=41) |
| safe | -3.43% ± 1.55% (n=35) | -10.99% ± 15.84% (n=48) |

| labels | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.04% ± 1.59% (n=10) | -37.28% ± 35.96% (n=14) |
| both agree | -0.72% ± 1.46% (n=2) | +14.07% ± 60.48% (n=5) |
| one view missing | -1.47% ± 1.36% (n=17) | +5.38% ± 24.92% (n=29) |
| one view missing; unvalidated view | -0.81% ± 4.94% (n=3) | +15.95% ± 57.77% (n=5) |
| research too optimistic | -2.65% ± 1.59% (n=12) | -9.28% ± 43.44% (n=11) |
| research too optimistic; unvalidated view | -5.23% ± 5.84% (n=8) | -13.52% ± 37.90% (n=10) |
| unvalidated view | -1.99% ± 2.03% (n=11) | +6.52% ± 22.84% (n=15) |

## Strong-team master (live since 23 Nov 2026) beside today's master (shadow, the rollback baseline)

Frozen picks: 29; CLV -1.81% ± 2.02% (n=17); realised profit per bet -13.07% ± 26.22% (n=20). Research gate (research no-loss at least 0.70 on every pick, since 24 Nov 2026): 20 graded picks (reviewed at 50).

Weak-link flags (flag only, since 24 Nov 2026): 11 flagged picks graded; each reason is reviewed once 50 flagged picks are graded.

| picks | graded | realised profit per bet (n) | mean CLV (n) | observed minus market no-loss (points) |
|---|---|---|---|---|
| weak link | 11 | -17.20% ± 39.48% (n=11) | -1.11% ± 3.49% (n=8) | -9.1 |
| not flagged | 9 | -8.01% ± 34.98% (n=9) | -2.41% ± 2.68% (n=8) | -3.4 |
| reason (a) | 0 | n/a (0) | n/a (0) | n/a |
| reason (b) | 8 | -34.82% ± 49.32% (n=8) | +1.20% ± 2.04% (n=5) | -20.5 |
| reason (c) | 0 | n/a (0) | n/a (0) | n/a |
| reason (d) | 1 | +27.25% (n=1) | -1.16% (n=1) | +18.8 |
| reason (e) | 1 | +37.59% (n=1) | n/a (0) | +38.9 |
| reason (f) | 6 | -29.75% ± 61.82% (n=6) | +0.18% ± 2.92% (n=3) | -17.5 |
| reason (g) | 4 | -34.49% ± 74.28% (n=4) | -3.38% ± 6.32% (n=4) | -23.3 |

Comparison rule (decided 23 Nov 2026): Decided 23 Nov 2026, before any strong-master pick: after at least 150 graded matches over at least 3 calendar weeks on each list, flat-stake return per bet at Pinnacle prices, strong master minus live master, whole kickoff weeks resampled (the same weeks for both), 95% interval. The strong master is better only if the interval is entirely above zero. Results by market group, tier and research label are context only.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| strong master | 20 | 1 | -13.07% | 55.0% | 1.34 |
| today's master | 89 | 2 | -3.99% | 62.9% | 1.41 |

Rollback rule (strong release, decided by Paul 23 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, strong master minus today's master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top. Nothing switches automatically: Paul decides, and rolling back is setting live to "new".

**Rollback status: WAITING.** waiting for at least 150 graded matches over at least 3 weeks on each list

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).

By tier (context only; the comparison rule never reads it):

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| not proven: fill | -0.54% ± 2.50% (n=4) | -29.75% ± 61.82% (n=6) |
| not proven: safe | -3.17% ± 3.47% (n=9) | -5.41% ± 32.06% (n=10) |
| proven | -0.03% ± 1.68% (n=4) | -7.18% ± 61.09% (n=4) |

By market group (context only; the comparison rule never reads it):

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| asian_handicap | -1.32% ± 1.79% (n=14) | -5.09% ± 26.66% (n=17) |
| match_result | -4.10% ± 8.71% (n=3) | -58.29% ± 81.75% (n=3) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 358; CLV -2.15% ± 0.77% (n=127); realised profit per bet +1.42% ± 6.73% (n=310). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-120-200-v6) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-120-200-v6 (active) | -5.39% ± 16.51% (n=54) | +34.69% ± 4.34% (n=2) | -6.93% ± 17.01% (n=52) |
| no-loss-market-reference-v5 | +2.54% ± 7.57% (n=249) | +23.00% ± 33.26% (n=13) | +1.41% ± 7.76% (n=236) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -2.15% ± 0.77% (n=127) | +1.42% ± 6.73% (n=310) |
| value | -2.16% ± 0.67% (n=157) | +1.37% ± 6.37% (n=476) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -2.15% ± 0.50% (n=284) | +1.39% ± 4.68% (n=786) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -0.38% ± 1.23% (n=52) | +7.86% ± 8.11% (n=242) |
| Pinnacle | -2.55% ± 0.54% (n=232) | -1.49% ± 5.71% (n=544) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.27% ± 0.55% (n=21) | -1.49% ± 9.55% (n=118) |
| a | -2.06% ± 0.62% (n=218) | +2.36% ± 6.02% (n=550) |
| b | -2.06% ± 0.99% (n=45) | -2.79% ± 11.30% (n=101) |
| c-cagey | n/a (0) | +14.82% ± 3.70% (n=17) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -2.51% ± 1.01% (n=46) | +3.49% ± 12.29% (n=135) |
| Q2 | -2.21% ± 0.95% (n=46) | -4.51% ± 11.30% (n=135) |
| Q3 | -1.73% ± 0.74% (n=42) | +8.66% ± 11.34% (n=125) |
| Q4 | -1.29% ± 1.27% (n=50) | -0.93% ± 10.68% (n=137) |
| Q5 most open | -3.10% ± 1.86% (n=44) | +0.82% ± 9.88% (n=128) |
| n/a | -2.15% ± 1.24% (n=56) | +1.35% ± 13.13% (n=126) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.88% ± 0.59% (n=215) | +1.13% ± 5.52% (n=565) |
| yes | -3.01% ± 0.95% (n=69) | +2.05% ± 8.84% (n=221) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -2.08% ± 0.52% (n=272) | +0.97% ± 4.85% (n=737) |
| yes | -3.82% ± 0.79% (n=12) | +7.75% ± 18.02% (n=49) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.98% ± 0.58% (n=229) | +0.82% ± 5.13% (n=637) |
| yes | -2.87% ± 0.96% (n=55) | +3.84% ± 11.33% (n=149) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -2.12% ± 0.53% (n=265) | +1.32% ± 4.82% (n=726) |
| yes | -2.57% ± 1.55% (n=19) | +2.22% ± 18.99% (n=60) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -2.15% ± 0.50% (n=284) | +1.39% ± 4.68% (n=786) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -2.16% ± 0.67% (n=157) | +1.37% ± 6.37% (n=476) |
| narrow-63-flagged-v2 | -6.39% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-120-200-v6 | -3.25% ± 1.41% (n=50) | -5.39% ± 16.51% (n=54) |
| no-loss-market-reference-v5 | -1.37% ± 0.84% (n=76) | +2.54% ± 7.57% (n=249) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -2.43% ± 0.77% (n=119) | +0.25% ± 6.95% (n=293) |
| n/a | -2.16% ± 0.67% (n=157) | +1.37% ± 6.37% (n=476) |
| value | +1.97% ± 2.79% (n=8) | +21.67% ± 25.55% (n=17) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 3679 (3679 with an offered price).
1xBet edge vs fair at capture: -3.80% ± 0.21% (n=529).
Return at the capture fair price, all tagged lines: +1.26% ± 3.42% (n=2592); plus lines only: +1.78% ± 2.66% (n=1521).

- balanced: +1.88% ± 3.74% (n=2204)
- low_total: -1.68% ± 9.35% (n=302)
- high_draw: +0.64% ± 5.15% (n=1127)
- even_odds: +1.18% ± 8.72% (n=453)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 214, pending 40, graded 174, excluded 106.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: over_2_5) | 74 |
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 32 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 6 | 33.3% [0.0%, 100.0%] | 28.0% | 32.0% | 0.0% [0.0%, 0.0%] | 9.6% | 11.1% |
| Q2 | 24 | 25.0% [25.0%, 25.0%] | 31.4% | 34.1% | 0.0% [0.0%, 0.0%] | 11.2% | 12.5% |
| Q3 | 36 | 25.0% [20.8%, 40.0%] | 34.8% | 36.6% | 8.3% [4.2%, 20.0%] | 13.6% | 14.4% |
| Q4 | 62 | 43.5% [42.9%, 50.0%] | 40.2% | 41.1% | 8.1% [7.1%, 16.7%] | 18.2% | 18.1% |
| Q5 most open | 46 | 39.1% [31.2%, 50.0%] | 54.3% | 55.3% | 23.9% [12.5%, 33.3%] | 31.5% | 32.0% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6535 | 0.6573 | +3.833 [-3.629, +7.995] (n=174) |
| 3+ margin | 0.3484 | 0.3543 | +5.872 [+1.029, +7.870] (n=174) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +4.438% [-0.062, +11.174] (n=1740)
- at the uncorrected fair price: +5.379% [+0.988, +12.317] (n=1740)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (power method, as clv_report). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
