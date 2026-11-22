# v27/v28 price-edge tracking

## Headline: closing-line value first, returns second

| List | View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| value shortlist | per pick | 89 | -1.9% | -2.7% to -1.2% | 24% | 375 | +3.4% | -3.4% to +10.1% |
| value shortlist | per fixture (a match's picks averaged) | 37 | -1.2% | -2.3% to -0.1% | 22% | 132 | +2.8% | -5.1% to +10.7% |
| cagey tier | per pick | 64 | -1.5% | -2.7% to -0.4% | 28% | 235 | +4.6% | -3.6% to +12.8% |
| cagey tier | per fixture (a match's picks averaged) | 28 | -1.7% | -2.7% to -0.6% | 25% | 98 | +6.2% | -1.8% to +14.2% |
| new master (live) | per pick | 16 | -2.9% | -3.9% to -1.8% | 6% | 26 | -4.3% | -30.0% to +21.4% |
| new master (live) | per fixture (a match's picks averaged) | 16 | -2.9% | -3.9% to -1.8% | 6% | 26 | -4.3% | -30.0% to +21.4% |
| old master (shadow) | per pick | 25 | -1.2% | -3.2% to +0.8% | 24% | 86 | -0.6% | -14.9% to +13.6% |
| old master (shadow) | per fixture (a match's picks averaged) | 25 | -1.2% | -3.2% to +0.8% | 24% | 86 | -0.6% | -14.9% to +13.6% |

Closing-line value (CLV) leads because it is the less noisy measure: it compares the frozen price with the Pinnacle fair close and does not wait for results. Returns come second: with few matches they are mostly luck. Intervals are mean ± 1.96 standard errors, clustered by fixture. Near-kickoff feed quotes are not verified official closing prices. The headline CLV is clv_report's (the Pinnacle close with the margin removed by the power method). The STOP REVIEW rule and the tables below use this report's own CLV, with the same margin removal, priced from the latest near-kickoff observation after each pick was captured, so the two can still differ slightly.

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 1587 captured recommendations; 1430 graded; 160 distinct fixtures.
cagey: 987 captured recommendations; 944 graded; 108 distinct fixtures.
Actual placed bets: NOT_RECORDED

Reviewed 2026-11-22T13:51:09.621583+00:00. Frozen v27 picks: 424.

**Mean CLV vs Pinnacle close:** -1.97% ± 0.83% (n=89). **Flat-stake profit per bet:** +3.36% ± 7.02% (n=375).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | -0.50% ± 2.05% (n=26) |
| Pinnacle | -2.57% ± 0.78% (n=63) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | -0.91% ± 2.45% (n=16) |
| 1.90-2.10 | -2.45% ± 2.54% (n=17) |
| 2.10-2.40 | -10.12% (n=1) |
| <1.70 | -1.79% ± 0.75% (n=52) |
| >=2.40 | -5.31% ± 6.49% (n=3) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
|  | -3.19% ± 0.71% (n=13) |
| a | -1.98% ± 1.15% (n=61) |
| b | -0.87% ± 1.24% (n=15) |
| c-cagey | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
|  | -2.80% ± 0.72% (n=17) |
| favourite | -1.06% ± 1.28% (n=47) |
| underdog | -3.12% ± 1.54% (n=25) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | -1.24% ± 0.96% (n=64) |
| yes | -3.84% ± 1.44% (n=25) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | -1.85% ± 0.86% (n=85) |
| yes | -4.53% ± 1.44% (n=4) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | -1.56% ± 0.98% (n=68) |
| yes | -3.29% ± 1.46% (n=21) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | -1.81% ± 0.85% (n=82) |
| yes | -3.85% ± 3.69% (n=7) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| any tag | -3.82% ± 1.21% (n=34) |
| no tag | -0.82% ± 1.02% (n=55) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| Q1 cagiest | -4.35% ± 1.83% (n=16) |
| Q2 | -2.82% ± 1.46% (n=14) |
| Q3 | -2.27% ± 1.73% (n=13) |
| Q4 | -0.07% ± 3.05% (n=14) |
| Q5 most open | +0.54% ± 3.48% (n=6) |
| n/a | -1.50% ± 1.22% (n=26) |

## CLV by value_market_group

| group | mean CLV (n) |
|---|---|
| asian_handicap | -2.57% ± 1.23% (n=30) |
| double_chance | -3.02% ± 0.70% (n=23) |
| match_winner | -1.79% ± 1.90% (n=26) |
| n/a | +5.47% ± 3.69% (n=5) |
| over_1_5 | -1.91% ± 1.42% (n=5) |

## Master shortlist: new master (live since 14 Nov 2026) beside the old master (shadow)

Frozen picks: 48; CLV -2.99% ± 1.01% (n=16); realised profit per bet -4.27% ± 25.71% (n=26). Old master: 108 frozen picks, realised profit per bet -0.63% ± 14.22% (n=86).

Comparison rule (decided 13 Nov 2026, before any live result of the new master): After at least 150 graded matches over at least 3 calendar weeks (on each list), compare flat-stake return per bet at Pinnacle prices: new master minus live master, whole kickoff weeks resampled (the same weeks for both lists), 95% interval. Hit rate, average price, vetoed, ignored and missing-view counts are context only. The new master is better only if the interval is entirely above zero.

Rollback rule (release, decided by Paul 14 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, new master minus old master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top and in the run summary. Nothing switches automatically: Paul decides, and rolling back is setting live to "old".

**Rollback status: WAITING.** Not triggered: waiting for at least 150 graded matches over at least 3 weeks on each list.

Release incidents: new master failed (old master published) in 0 runs; comparison baseline missing (old master shadow failed) in 0 runs.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| new master | 26 | 1 | -4.27% | 69.2% | 1.40 |
| old master | 86 | 2 | -0.63% | 67.4% | 1.52 |

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).
Context, new master offers (newest pre-kickoff generation per fixture): 99 offers on 62 fixtures; included (cagey safe) 9; labels: both agree 2, research too optimistic 7, research strongly disagrees 0, one view missing 80, no research check 0, unvalidated view 0; no view 0.

By tier (context only; the comparison rule never reads it):

| tier | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| fill | -2.18% ± 1.24% (n=6) | +12.96% ± 39.49% (n=12) |
| safe | -3.48% ± 1.40% (n=10) | -19.04% ± 33.02% (n=14) |

| labels | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.67% ± 2.75% (n=3) | -11.80% ± 74.96% (n=5) |
| both agree | -1.46% (n=1) | -15.33% ± 84.37% (n=3) |
| one view missing | -2.01% ± 1.10% (n=7) | +6.92% ± 33.72% (n=13) |
| research too optimistic | -4.26% ± 2.00% (n=5) | -19.20% ± 64.89% (n=5) |

## Old master (shadow since 14 Nov 2026; master_shortlist_old.csv)

Frozen picks: 108; CLV -1.35% ± 1.96% (n=25); realised profit per bet -0.63% ± 14.22% (n=86).

| price flag | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below value threshold | -0.95% ± 6.95% (n=4) | -21.95% ± 44.11% (n=19) |
| negative market EV nomination | -2.66% ± 0.74% (n=17) | +5.14% ± 13.73% (n=55) |
| value | +3.82% ± 9.37% (n=4) | +6.67% ± 39.87% (n=12) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 251; CLV -1.37% ± 0.92% (n=66); realised profit per bet +4.58% ± 7.33% (n=235). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-v5) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-v5 (active) | +4.29% ± 7.54% (n=228) | +23.00% ± 33.26% (n=13) | +3.15% ± 7.74% (n=215) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -1.37% ± 0.92% (n=66) | +4.58% ± 7.33% (n=235) |
| value | -1.97% ± 0.83% (n=89) | +3.36% ± 7.02% (n=375) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -1.72% ± 0.62% (n=155) | +3.83% ± 5.15% (n=610) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -0.38% ± 1.23% (n=52) | +7.86% ± 8.11% (n=242) |
| Pinnacle | -2.39% ± 0.66% (n=103) | +1.18% ± 6.67% (n=368) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.27% ± 0.55% (n=21) | -1.49% ± 9.55% (n=118) |
| a | -1.58% ± 0.81% (n=110) | +5.34% ± 6.94% (n=404) |
| b | -0.99% ± 1.22% (n=24) | +1.45% ± 12.18% (n=71) |
| c-cagey | n/a (0) | +14.82% ± 3.70% (n=17) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -3.65% ± 1.20% (n=27) | +1.45% ± 14.31% (n=103) |
| Q2 | -2.47% ± 1.21% (n=28) | -4.29% ± 12.91% (n=98) |
| Q3 | -2.03% ± 0.94% (n=26) | +7.26% ± 11.48% (n=113) |
| Q4 | +0.50% ± 1.88% (n=28) | +4.61% ± 11.95% (n=110) |
| Q5 most open | -1.01% ± 2.16% (n=20) | +7.66% ± 10.00% (n=111) |
| n/a | -1.50% ± 1.22% (n=26) | +5.73% ± 16.37% (n=75) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.12% ± 0.74% (n=110) | +5.10% ± 6.08% (n=424) |
| yes | -3.17% ± 1.02% (n=45) | +0.92% ± 9.70% (n=186) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.58% ± 0.64% (n=147) | +3.58% ± 5.36% (n=563) |
| yes | -4.24% ± 1.07% (n=8) | +6.81% ± 18.74% (n=47) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.34% ± 0.74% (n=118) | +4.00% ± 5.64% (n=482) |
| yes | -2.93% ± 0.98% (n=37) | +3.19% ± 12.37% (n=128) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.63% ± 0.64% (n=144) | +3.95% ± 5.30% (n=562) |
| yes | -2.83% ± 2.47% (n=11) | +2.40% ± 21.12% (n=48) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.72% ± 0.62% (n=155) | +3.83% ± 5.15% (n=610) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -1.97% ± 0.83% (n=89) | +3.36% ± 7.02% (n=375) |
| narrow-63-flagged-v2 | -6.39% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-v5 | -1.30% ± 0.93% (n=65) | +4.29% ± 7.54% (n=228) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -1.82% ± 0.89% (n=60) | +3.54% ± 7.57% (n=220) |
| n/a | -1.97% ± 0.83% (n=89) | +3.36% ± 7.02% (n=375) |
| value | +3.09% ± 3.28% (n=6) | +19.93% ± 28.96% (n=15) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 2654 (2654 with an offered price).
1xBet edge vs fair at capture: -3.80% ± 0.21% (n=529).
Return at the capture fair price, all tagged lines: +1.05% ± 3.84% (n=2050); plus lines only: +1.81% ± 3.01% (n=1194).

- balanced: +2.18% ± 4.22% (n=1748)
- low_total: -3.67% ± 9.47% (n=274)
- high_draw: +0.21% ± 5.97% (n=836)
- even_odds: +2.83% ± 11.14% (n=318)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 136, pending 11, graded 125, excluded 67.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: over_2_5) | 51 |
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 16 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 5 | 40.0% [25.0%, 100.0%] | 28.2% | 32.2% | 0.0% [0.0%, 0.0%] | 9.7% | 11.3% |
| Q2 | 17 | 23.5% [20.0%, 25.0%] | 31.3% | 34.0% | 0.0% [0.0%, 0.0%] | 11.1% | 12.4% |
| Q3 | 28 | 25.0% [20.8%, 50.0%] | 35.0% | 36.9% | 7.1% [4.2%, 25.0%] | 13.9% | 14.6% |
| Q4 | 46 | 41.3% [25.0%, 42.9%] | 40.3% | 41.2% | 6.5% [0.0%, 7.1%] | 18.2% | 18.2% |
| Q5 most open | 29 | 44.8% [41.7%, 60.0%] | 53.4% | 54.2% | 31.0% [29.2%, 40.0%] | 30.7% | 30.9% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6453 | 0.6480 | +2.636 [-6.276, +4.233] (n=125) |
| 3+ margin | 0.3350 | 0.3422 | +7.181 [+3.333, +7.870] (n=125) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +2.334% [-1.856, +3.085] (n=1250)
- at the uncorrected fair price: +3.201% [-0.813, +3.920] (n=1250)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (power method, as clv_report). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
