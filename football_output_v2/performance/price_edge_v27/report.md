# v27/v28 price-edge tracking

## Headline: closing-line value first, returns second

| List | View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| value shortlist | per pick | 53 | -1.7% | -2.9% to -0.5% | 26% | 312 | +2.4% | -5.1% to +9.9% |
| value shortlist | per fixture (a match's picks averaged) | 21 | -0.5% | -2.3% to +1.3% | 33% | 99 | +0.4% | -8.1% to +8.8% |
| cagey tier | per pick | 41 | -0.9% | -2.2% to +0.5% | 32% | 202 | +4.7% | -3.9% to +13.2% |
| cagey tier | per fixture (a match's picks averaged) | 17 | -1.2% | -2.6% to +0.2% | 24% | 81 | +5.0% | -2.8% to +12.8% |
| new master (live) | per pick | 2 | -3.4% | -4.0% to -2.8% | 0% | 2 | -33.0% | -164.3% to +98.3% |
| new master (live) | per fixture (a match's picks averaged) | 2 | -3.4% | -4.0% to -2.8% | 0% | 2 | -33.0% | -164.3% to +98.3% |
| old master (shadow) | per pick | 12 | +0.2% | -3.7% to +4.1% | 42% | 63 | -0.3% | -16.9% to +16.4% |
| old master (shadow) | per fixture (a match's picks averaged) | 12 | +0.2% | -3.7% to +4.1% | 42% | 63 | -0.3% | -16.9% to +16.4% |

Closing-line value (CLV) leads because it is the less noisy measure: it compares the frozen price with the Pinnacle fair close and does not wait for results. Returns come second: with few matches they are mostly luck. Intervals are mean ± 1.96 standard errors, clustered by fixture. Near-kickoff feed quotes are not verified official closing prices. The headline CLV is clv_report's (the Pinnacle close with the margin removed by the power method). The STOP REVIEW rule and the tables below use this report's own CLV, with the same margin removal, priced from the latest near-kickoff observation after each pick was captured, so the two can still differ slightly.

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 1243 captured recommendations; 1111 graded; 135 distinct fixtures.
cagey: 944 captured recommendations; 882 graded; 101 distinct fixtures.
Actual placed bets: NOT_RECORDED

Reviewed 2026-11-21T06:15:28.525464+00:00. Frozen v27 picks: 381.

**Mean CLV vs Pinnacle close:** -1.80% ± 1.22% (n=53). **Flat-stake profit per bet:** +2.42% ± 7.46% (n=312).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | -0.50% ± 2.05% (n=26) |
| Pinnacle | -3.04% ± 1.21% (n=27) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | -0.32% ± 9.33% (n=4) |
| 1.90-2.10 | -0.98% ± 3.94% (n=9) |
| 2.10-2.40 | -10.12% (n=1) |
| <1.70 | -1.64% ± 0.97% (n=36) |
| >=2.40 | -5.31% ± 6.49% (n=3) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
|  | -3.19% ± 0.71% (n=13) |
| a | -1.49% ± 1.64% (n=38) |
| b | +1.39% ± 4.24% (n=2) |
| c-cagey | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
|  | -2.80% ± 0.72% (n=17) |
| favourite | +0.15% ± 2.24% (n=23) |
| underdog | -3.91% ± 2.21% (n=13) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | -0.32% ± 1.54% (n=32) |
| yes | -4.04% ± 1.58% (n=21) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | -1.57% ± 1.29% (n=49) |
| yes | -4.53% ± 1.44% (n=4) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | -1.06% ± 1.51% (n=39) |
| yes | -3.85% ± 1.49% (n=14) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | -1.49% ± 1.22% (n=49) |
| yes | -5.59% ± 5.45% (n=4) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| any tag | -4.12% ± 1.34% (n=25) |
| no tag | +0.28% ± 1.63% (n=28) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| Q1 cagiest | -4.92% ± 1.98% (n=11) |
| Q2 | -2.73% ± 1.68% (n=12) |
| Q3 | -2.21% ± 1.88% (n=12) |
| Q4 | +0.53% ± 3.39% (n=12) |
| Q5 most open | +1.63% ± 3.36% (n=5) |
| n/a | +3.84% (n=1) |

## CLV by value_market_group

| group | mean CLV (n) |
|---|---|
| asian_handicap | -3.13% ± 1.77% (n=14) |
| double_chance | -2.91% ± 0.83% (n=15) |
| match_winner | -1.82% ± 3.20% (n=14) |
| n/a | +5.47% ± 3.69% (n=5) |
| over_1_5 | -1.91% ± 1.42% (n=5) |

## Master shortlist: new master (live since 14 Nov 2026) beside the old master (shadow)

Frozen picks: 27; CLV -3.42% ± 0.62% (n=2); realised profit per bet -33.00% ± 131.32% (n=2). Old master: 87 frozen picks, realised profit per bet -0.25% ± 16.65% (n=63).

Comparison rule (decided 13 Nov 2026, before any live result of the new master): After at least 150 graded matches over at least 3 calendar weeks (on each list), compare flat-stake return per bet at Pinnacle prices: new master minus live master, whole kickoff weeks resampled (the same weeks for both lists), 95% interval. Hit rate, average price, vetoed, ignored and missing-view counts are context only. The new master is better only if the interval is entirely above zero.

Rollback rule (release, decided by Paul 14 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, new master minus old master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top and in the run summary. Nothing switches automatically: Paul decides, and rolling back is setting live to "old".

**Rollback status: WAITING.** Not triggered: waiting for at least 150 graded matches over at least 3 weeks on each list.

Release incidents: new master failed (old master published) in 0 runs; comparison baseline missing (old master shadow failed) in 0 runs.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| new master | 2 | 1 | -33.00% | 50.0% | 1.34 |
| old master | 63 | 2 | -0.25% | 66.7% | 1.56 |

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).
Context, new master offers (newest pre-kickoff generation per fixture): 61 offers on 37 fixtures; included (cagey safe) 7; labels: both agree 1, research too optimistic 5, research strongly disagrees 0, one view missing 51, no research check 0, unvalidated view 0; no view 0.

By tier (context only; the comparison rule never reads it):

| tier | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| fill | n/a (0) | n/a (0) |
| safe | -3.42% ± 0.62% (n=2) | -33.00% ± 131.32% (n=2) |

| labels | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | n/a (0) | n/a (0) |
| both agree | n/a (0) | n/a (0) |
| one view missing | n/a (0) | n/a (0) |
| research too optimistic | -3.42% ± 0.62% (n=2) | -33.00% ± 131.32% (n=2) |

## Old master (shadow since 14 Nov 2026; master_shortlist_old.csv)

Frozen picks: 87; CLV -0.01% ± 3.90% (n=12); realised profit per bet -0.25% ± 16.65% (n=63).

| price flag | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below value threshold | -0.95% ± 6.95% (n=4) | -21.95% ± 44.11% (n=19) |
| negative market EV nomination | -2.89% ± 1.04% (n=4) | +10.03% ± 12.59% (n=32) |
| value | +3.82% ± 9.37% (n=4) | +6.67% ± 39.87% (n=12) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 241; CLV -0.68% ± 1.09% (n=42); realised profit per bet +4.67% ± 7.66% (n=202). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-v5) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-v5 (active) | +4.33% ± 7.92% (n=195) | +33.25% ± 28.82% (n=12) | +2.43% ± 8.17% (n=183) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -0.68% ± 1.09% (n=42) | +4.67% ± 7.66% (n=202) |
| value | -1.80% ± 1.22% (n=53) | +2.42% ± 7.46% (n=312) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -1.30% ± 0.84% (n=95) | +3.31% ± 5.43% (n=514) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -0.38% ± 1.23% (n=52) | +7.86% ± 8.11% (n=242) |
| Pinnacle | -2.42% ± 1.01% (n=43) | -0.74% ± 7.29% (n=272) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.27% ± 0.55% (n=21) | -1.49% ± 9.55% (n=118) |
| a | -0.90% ± 1.09% (n=67) | +4.50% ± 7.44% (n=334) |
| b | +0.73% ± 3.02% (n=7) | +2.64% ± 13.28% (n=45) |
| c-cagey | n/a (0) | +14.82% ± 3.70% (n=17) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -3.86% ± 1.29% (n=18) | +2.56% ± 14.79% (n=88) |
| Q2 | -2.58% ± 1.46% (n=23) | -8.63% ± 13.05% (n=99) |
| Q3 | -1.99% ± 1.11% (n=22) | +11.23% ± 11.35% (n=105) |
| Q4 | +1.54% ± 2.22% (n=21) | +4.32% ± 12.84% (n=99) |
| Q5 most open | +1.26% ± 2.02% (n=10) | +5.94% ± 10.95% (n=95) |
| n/a | +3.84% (n=1) | +5.64% ± 19.83% (n=28) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -0.10% ± 1.04% (n=58) | +6.34% ± 6.37% (n=349) |
| yes | -3.19% ± 1.17% (n=37) | -3.12% ± 10.20% (n=165) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.03% ± 0.89% (n=87) | +2.87% ± 5.66% (n=470) |
| yes | -4.24% ± 1.07% (n=8) | +8.00% ± 19.37% (n=44) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -0.50% ± 1.03% (n=69) | +4.63% ± 5.93% (n=407) |
| yes | -3.43% ± 0.99% (n=26) | -1.74% ± 13.16% (n=107) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.12% ± 0.84% (n=89) | +4.18% ± 5.56% (n=472) |
| yes | -4.03% ± 4.04% (n=6) | -6.50% ± 22.70% (n=42) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.30% ± 0.84% (n=95) | +3.31% ± 5.43% (n=514) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -1.80% ± 1.22% (n=53) | +2.42% ± 7.46% (n=312) |
| narrow-63-flagged-v2 | -6.39% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-v5 | -0.54% ± 1.08% (n=41) | +4.33% ± 7.92% (n=195) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -1.31% ± 1.03% (n=36) | +2.90% ± 7.97% (n=188) |
| n/a | -1.80% ± 1.22% (n=53) | +2.42% ± 7.46% (n=312) |
| value | +3.09% ± 3.28% (n=6) | +28.50% ± 25.34% (n=14) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 2620 (2620 with an offered price).
1xBet edge vs fair at capture: -3.80% ± 0.21% (n=529).
Return at the capture fair price, all tagged lines: +0.79% ± 3.93% (n=1918); plus lines only: +2.17% ± 3.06% (n=1119).

- balanced: +1.89% ± 4.32% (n=1645)
- low_total: -4.91% ± 9.18% (n=259)
- high_draw: -0.45% ± 6.21% (n=738)
- even_odds: +2.95% ± 11.65% (n=292)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 134, pending 26, graded 108, excluded 60.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: over_2_5) | 44 |
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 16 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 4 | 25.0% [25.0%, 25.0%] | 28.1% | 32.4% | 0.0% [0.0%, 0.0%] | 9.8% | 11.4% |
| Q2 | 13 | 30.8% [25.0%, 100.0%] | 31.2% | 34.0% | 0.0% [0.0%, 0.0%] | 11.1% | 12.5% |
| Q3 | 24 | 20.8% [20.8%, 20.8%] | 35.0% | 36.9% | 4.2% [4.2%, 4.2%] | 13.9% | 14.6% |
| Q4 | 43 | 41.9% [0.0%, 42.9%] | 40.2% | 41.1% | 7.0% [0.0%, 7.1%] | 18.1% | 18.1% |
| Q5 most open | 24 | 41.7% [41.7%, 41.7%] | 53.9% | 54.6% | 29.2% [29.2%, 29.2%] | 31.2% | 31.3% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6459 | 0.6500 | +4.100 [-2.958, +4.233] (n=108) |
| 3+ margin | 0.3229 | 0.3309 | +8.068 [+7.870, +18.543] (n=108) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +3.068% [+2.166, +3.085] (n=1080)
- at the uncorrected fair price: +3.926% [+3.920, +4.209] (n=1080)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (power method, as clv_report). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
