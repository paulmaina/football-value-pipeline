# v27/v28 price-edge tracking

## Headline: closing-line value first, returns second

| List | View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| value shortlist | per pick | 89 | -1.9% | -2.7% to -1.2% | 24% | 320 | +2.3% | -5.1% to +9.7% |
| value shortlist | per fixture (a match's picks averaged) | 37 | -1.2% | -2.3% to -0.1% | 22% | 103 | +0.2% | -7.9% to +8.4% |
| cagey tier | per pick | 64 | -1.5% | -2.7% to -0.4% | 28% | 210 | +3.9% | -4.4% to +12.2% |
| cagey tier | per fixture (a match's picks averaged) | 28 | -1.7% | -2.7% to -0.6% | 25% | 85 | +4.1% | -3.6% to +11.7% |
| new master (live) | per pick | 16 | -2.9% | -3.9% to -1.8% | 6% | 6 | -31.2% | -91.8% to +29.4% |
| new master (live) | per fixture (a match's picks averaged) | 16 | -2.9% | -3.9% to -1.8% | 6% | 6 | -31.2% | -91.8% to +29.4% |
| old master (shadow) | per pick | 25 | -1.2% | -3.2% to +0.8% | 24% | 67 | -2.0% | -18.3% to +14.2% |
| old master (shadow) | per fixture (a match's picks averaged) | 25 | -1.2% | -3.2% to +0.8% | 24% | 67 | -2.0% | -18.3% to +14.2% |

Closing-line value (CLV) leads because it is the less noisy measure: it compares the frozen price with the Pinnacle fair close and does not wait for results. Returns come second: with few matches they are mostly luck. Intervals are mean ± 1.96 standard errors, clustered by fixture. Near-kickoff feed quotes are not verified official closing prices. The headline CLV is clv_report's (the Pinnacle close with the margin removed by the power method). The STOP REVIEW rule and the tables below use this report's own CLV, with the same margin removal, priced from the latest near-kickoff observation after each pick was captured, so the two can still differ slightly.

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 1530 captured recommendations; 1155 graded; 153 distinct fixtures.
cagey: 978 captured recommendations; 894 graded; 107 distinct fixtures.
Actual placed bets: NOT_RECORDED

Reviewed 2026-11-21T16:20:10.243575+00:00. Frozen v27 picks: 409.

**Mean CLV vs Pinnacle close:** -1.97% ± 0.83% (n=89). **Flat-stake profit per bet:** +2.30% ± 7.40% (n=320).
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

Frozen picks: 37; CLV -2.99% ± 1.01% (n=16); realised profit per bet -31.17% ± 60.59% (n=6). Old master: 97 frozen picks, realised profit per bet -2.04% ± 16.27% (n=67).

Comparison rule (decided 13 Nov 2026, before any live result of the new master): After at least 150 graded matches over at least 3 calendar weeks (on each list), compare flat-stake return per bet at Pinnacle prices: new master minus live master, whole kickoff weeks resampled (the same weeks for both lists), 95% interval. Hit rate, average price, vetoed, ignored and missing-view counts are context only. The new master is better only if the interval is entirely above zero.

Rollback rule (release, decided by Paul 14 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, new master minus old master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top and in the run summary. Nothing switches automatically: Paul decides, and rolling back is setting live to "old".

**Rollback status: WAITING.** Not triggered: waiting for at least 150 graded matches over at least 3 weeks on each list.

Release incidents: new master failed (old master published) in 0 runs; comparison baseline missing (old master shadow failed) in 0 runs.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| new master | 6 | 1 | -31.17% | 50.0% | 1.36 |
| old master | 67 | 2 | -2.04% | 65.7% | 1.55 |

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).
Context, new master offers (newest pre-kickoff generation per fixture): 86 offers on 55 fixtures; included (cagey safe) 8; labels: both agree 1, research too optimistic 5, research strongly disagrees 0, one view missing 68, no research check 0, unvalidated view 0; no view 0.

By tier (context only; the comparison rule never reads it):

| tier | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| fill | -2.18% ± 1.24% (n=6) | -25.00% ± 147.00% (n=2) |
| safe | -3.48% ± 1.40% (n=10) | -34.25% ± 74.43% (n=4) |

| labels | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.67% ± 2.75% (n=3) | n/a (0) |
| both agree | -1.46% (n=1) | -100.00% (n=1) |
| one view missing | -2.01% ± 1.10% (n=7) | -7.00% ± 91.91% (n=3) |
| research too optimistic | -4.26% ± 2.00% (n=5) | -33.00% ± 131.32% (n=2) |

## Old master (shadow since 14 Nov 2026; master_shortlist_old.csv)

Frozen picks: 97; CLV -1.35% ± 1.96% (n=25); realised profit per bet -2.04% ± 16.27% (n=67).

| price flag | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below value threshold | -0.95% ± 6.95% (n=4) | -21.95% ± 44.11% (n=19) |
| negative market EV nomination | -2.66% ± 0.74% (n=17) | +5.56% ± 14.22% (n=36) |
| value | +3.82% ± 9.37% (n=4) | +6.67% ± 39.87% (n=12) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 249; CLV -1.37% ± 0.92% (n=66); realised profit per bet +3.92% ± 7.59% (n=210). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-v5) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-v5 (active) | +3.57% ± 7.84% (n=203) | +23.00% ± 33.26% (n=13) | +2.24% ± 8.05% (n=190) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -1.37% ± 0.92% (n=66) | +3.92% ± 7.59% (n=210) |
| value | -1.97% ± 0.83% (n=89) | +2.30% ± 7.40% (n=320) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -1.72% ± 0.62% (n=155) | +2.94% ± 5.38% (n=530) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -0.38% ± 1.23% (n=52) | +7.86% ± 8.11% (n=242) |
| Pinnacle | -2.39% ± 0.66% (n=103) | -1.19% ± 7.16% (n=288) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.27% ± 0.55% (n=21) | -1.49% ± 9.55% (n=118) |
| a | -1.58% ± 0.81% (n=110) | +3.99% ± 7.32% (n=347) |
| b | -0.99% ± 1.22% (n=24) | +2.04% ± 13.33% (n=48) |
| c-cagey | n/a (0) | +14.82% ± 3.70% (n=17) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -3.62% ± 1.25% (n=26) | +2.12% ± 14.50% (n=91) |
| Q2 | -2.55% ± 1.18% (n=29) | -6.43% ± 13.29% (n=94) |
| Q3 | -2.03% ± 0.94% (n=26) | +8.11% ± 11.85% (n=103) |
| Q4 | +0.50% ± 1.88% (n=28) | +3.80% ± 12.50% (n=103) |
| Q5 most open | -1.01% ± 2.16% (n=20) | +6.16% ± 10.59% (n=104) |
| n/a | -1.50% ± 1.22% (n=26) | +2.97% ± 20.11% (n=35) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.12% ± 0.74% (n=110) | +6.11% ± 6.31% (n=361) |
| yes | -3.17% ± 1.02% (n=45) | -3.82% ± 10.11% (n=169) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.58% ± 0.64% (n=147) | +2.57% ± 5.62% (n=483) |
| yes | -4.24% ± 1.07% (n=8) | +6.81% ± 18.74% (n=47) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.34% ± 0.74% (n=118) | +4.48% ± 5.88% (n=419) |
| yes | -2.93% ± 0.98% (n=37) | -2.87% ± 12.95% (n=111) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.63% ± 0.64% (n=144) | +3.76% ± 5.51% (n=488) |
| yes | -2.83% ± 2.47% (n=11) | -6.50% ± 22.70% (n=42) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.72% ± 0.62% (n=155) | +2.94% ± 5.38% (n=530) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -1.97% ± 0.83% (n=89) | +2.30% ± 7.40% (n=320) |
| narrow-63-flagged-v2 | -6.39% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-v5 | -1.30% ± 0.93% (n=65) | +3.57% ± 7.84% (n=203) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -1.82% ± 0.89% (n=60) | +2.69% ± 7.86% (n=195) |
| n/a | -1.97% ± 0.83% (n=89) | +2.30% ± 7.40% (n=320) |
| value | +3.09% ± 3.28% (n=6) | +19.93% ± 28.96% (n=15) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 2626 (2626 with an offered price).
1xBet edge vs fair at capture: -3.80% ± 0.21% (n=529).
Return at the capture fair price, all tagged lines: +0.95% ± 3.93% (n=1937); plus lines only: +1.81% ± 3.07% (n=1127).

- balanced: +2.06% ± 4.32% (n=1664)
- low_total: -3.67% ± 9.47% (n=274)
- high_draw: -0.03% ± 6.23% (n=757)
- even_odds: +2.95% ± 11.65% (n=292)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 136, pending 24, graded 112, excluded 58.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: over_2_5) | 42 |
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 16 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 5 | 40.0% [25.0%, 100.0%] | 28.2% | 32.2% | 0.0% [0.0%, 0.0%] | 9.7% | 11.3% |
| Q2 | 13 | 30.8% [25.0%, 100.0%] | 31.2% | 34.0% | 0.0% [0.0%, 0.0%] | 11.1% | 12.5% |
| Q3 | 24 | 20.8% [20.8%, 20.8%] | 35.0% | 36.9% | 4.2% [4.2%, 4.2%] | 13.9% | 14.6% |
| Q4 | 43 | 41.9% [0.0%, 42.9%] | 40.2% | 41.1% | 7.0% [0.0%, 7.1%] | 18.1% | 18.1% |
| Q5 most open | 27 | 44.4% [41.7%, 66.7%] | 53.5% | 54.3% | 29.6% [29.2%, 33.3%] | 30.8% | 31.0% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6525 | 0.6551 | +2.510 [-27.933, +4.233] (n=112) |
| 3+ margin | 0.3304 | 0.3381 | +7.744 [+5.510, +7.870] (n=112) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +2.383% [-10.006, +3.085] (n=1120)
- at the uncorrected fair price: +3.235% [-8.880, +3.920] (n=1120)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (power method, as clv_report). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
