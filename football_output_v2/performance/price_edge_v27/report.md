# v27/v28 price-edge tracking

## Headline: closing-line value first, returns second

| List | View | With a close | Mean CLV | 95% interval | Beat the close | Settled | Return per unit | 95% interval |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| value shortlist | per pick | 85 | -1.9% | -2.7% to -1.1% | 24% | 316 | +2.1% | -5.3% to +9.6% |
| value shortlist | per fixture (a match's picks averaged) | 35 | -1.2% | -2.3% to +0.0% | 23% | 101 | -0.0% | -8.3% to +8.2% |
| cagey tier | per pick | 64 | -1.5% | -2.7% to -0.4% | 28% | 206 | +4.0% | -4.4% to +12.4% |
| cagey tier | per fixture (a match's picks averaged) | 28 | -1.7% | -2.7% to -0.6% | 25% | 83 | +4.1% | -3.6% to +11.9% |
| new master (live) | per pick | 14 | -3.0% | -4.1% to -2.0% | 0% | 4 | -66.5% | -132.2% to -0.8% |
| new master (live) | per fixture (a match's picks averaged) | 14 | -3.0% | -4.1% to -2.0% | 0% | 4 | -66.5% | -132.2% to -0.8% |
| old master (shadow) | per pick | 23 | -1.2% | -3.3% to +1.0% | 22% | 65 | -3.3% | -20.0% to +13.3% |
| old master (shadow) | per fixture (a match's picks averaged) | 23 | -1.2% | -3.3% to +1.0% | 22% | 65 | -3.3% | -20.0% to +13.3% |

Closing-line value (CLV) leads because it is the less noisy measure: it compares the frozen price with the Pinnacle fair close and does not wait for results. Returns come second: with few matches they are mostly luck. Intervals are mean ± 1.96 standard errors, clustered by fixture. Near-kickoff feed quotes are not verified official closing prices. The headline CLV is clv_report's (the Pinnacle close with the margin removed by the power method). The STOP REVIEW rule and the tables below use this report's own CLV, with the same margin removal, priced from the latest near-kickoff observation after each pick was captured, so the two can still differ slightly.

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 1482 captured recommendations; 1131 graded; 148 distinct fixtures.
cagey: 968 captured recommendations; 890 graded; 105 distinct fixtures.
Actual placed bets: NOT_RECORDED

Reviewed 2026-11-21T15:29:38.346331+00:00. Frozen v27 picks: 403.

**Mean CLV vs Pinnacle close:** -1.96% ± 0.87% (n=85). **Flat-stake profit per bet:** +2.14% ± 7.44% (n=316).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | -0.50% ± 2.05% (n=26) |
| Pinnacle | -2.60% ± 0.83% (n=59) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | -0.72% ± 2.59% (n=15) |
| 1.90-2.10 | -2.39% ± 2.70% (n=16) |
| 2.10-2.40 | -10.12% (n=1) |
| <1.70 | -1.83% ± 0.78% (n=50) |
| >=2.40 | -5.31% ± 6.49% (n=3) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
|  | -3.19% ± 0.71% (n=13) |
| a | -1.92% ± 1.19% (n=59) |
| b | -0.88% ± 1.43% (n=13) |
| c-cagey | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
|  | -2.80% ± 0.72% (n=17) |
| favourite | -1.07% ± 1.34% (n=45) |
| underdog | -3.07% ± 1.68% (n=23) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | -1.18% ± 1.02% (n=60) |
| yes | -3.84% ± 1.44% (n=25) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | -1.83% ± 0.90% (n=81) |
| yes | -4.53% ± 1.44% (n=4) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | -1.52% ± 1.03% (n=64) |
| yes | -3.29% ± 1.46% (n=21) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | -1.79% ± 0.89% (n=78) |
| yes | -3.85% ± 3.69% (n=7) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| any tag | -3.82% ± 1.21% (n=34) |
| no tag | -0.71% ± 1.08% (n=51) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| Q1 cagiest | -4.35% ± 1.83% (n=16) |
| Q2 | -2.82% ± 1.46% (n=14) |
| Q3 | -2.27% ± 1.73% (n=13) |
| Q4 | -0.07% ± 3.05% (n=14) |
| Q5 most open | +0.54% ± 3.48% (n=6) |
| n/a | -1.37% ± 1.41% (n=22) |

## CLV by value_market_group

| group | mean CLV (n) |
|---|---|
| asian_handicap | -2.49% ± 1.32% (n=28) |
| double_chance | -3.02% ± 0.70% (n=23) |
| match_winner | -1.88% ± 2.05% (n=24) |
| n/a | +5.47% ± 3.69% (n=5) |
| over_1_5 | -1.91% ± 1.42% (n=5) |

## Master shortlist: new master (live since 14 Nov 2026) beside the old master (shadow)

Frozen picks: 33; CLV -3.09% ± 1.10% (n=14); realised profit per bet -66.50% ± 65.66% (n=4). Old master: 93 frozen picks, realised profit per bet -3.32% ± 16.67% (n=65).

Comparison rule (decided 13 Nov 2026, before any live result of the new master): After at least 150 graded matches over at least 3 calendar weeks (on each list), compare flat-stake return per bet at Pinnacle prices: new master minus live master, whole kickoff weeks resampled (the same weeks for both lists), 95% interval. Hit rate, average price, vetoed, ignored and missing-view counts are context only. The new master is better only if the interval is entirely above zero.

Rollback rule (release, decided by Paul 14 Nov 2026): After at least 150 graded matches over at least 3 calendar weeks on each list, compare flat-stake return per bet at Pinnacle prices, new master minus old master, whole kickoff weeks resampled (the same weeks for both), 95% interval. If the interval is entirely below zero, the weekly report says ROLLBACK TRIGGERED at the top and in the run summary. Nothing switches automatically: Paul decides, and rolling back is setting live to "old".

**Rollback status: WAITING.** Not triggered: waiting for at least 150 graded matches over at least 3 weeks on each list.

Release incidents: new master failed (old master published) in 0 runs; comparison baseline missing (old master shadow failed) in 0 runs.

| list | graded matches | weeks | flat-stake return per bet | hit rate | average price |
|---|---|---|---|---|---|
| new master | 4 | 1 | -66.50% | 25.0% | 1.34 |
| old master | 65 | 2 | -3.32% | 64.6% | 1.55 |

**Status:** waiting for at least 150 graded matches over at least 3 weeks on each list (not yet comparable).
Context, new master offers (newest pre-kickoff generation per fixture): 80 offers on 50 fixtures; included (cagey safe) 8; labels: both agree 1, research too optimistic 5, research strongly disagrees 0, one view missing 65, no research check 0, unvalidated view 0; no view 0.

By tier (context only; the comparison rule never reads it):

| tier | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| fill | -2.12% ± 1.43% (n=4) | -100.00% (n=1) |
| safe | -3.48% ± 1.40% (n=10) | -55.33% ± 87.55% (n=3) |

| labels | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.67% ± 2.75% (n=3) | n/a (0) |
| both agree | -1.46% (n=1) | -100.00% (n=1) |
| one view missing | -1.89% ± 1.19% (n=5) | -100.00% (n=1) |
| research too optimistic | -4.26% ± 2.00% (n=5) | -33.00% ± 131.32% (n=2) |

## Old master (shadow since 14 Nov 2026; master_shortlist_old.csv)

Frozen picks: 93; CLV -1.27% ± 2.12% (n=23); realised profit per bet -3.32% ± 16.67% (n=65).

| price flag | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below value threshold | -0.95% ± 6.95% (n=4) | -21.95% ± 44.11% (n=19) |
| negative market EV nomination | -2.71% ± 0.78% (n=15) | +3.56% ± 14.77% (n=34) |
| value | +3.82% ± 9.37% (n=4) | +6.67% ± 39.87% (n=12) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 246; CLV -1.37% ± 0.92% (n=66); realised profit per bet +3.99% ± 7.66% (n=206). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-v5) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-v5 (active) | +3.63% ± 7.91% (n=199) | +23.00% ± 33.26% (n=13) | +2.27% ± 8.13% (n=186) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -1.37% ± 0.92% (n=66) | +3.99% ± 7.66% (n=206) |
| value | -1.96% ± 0.87% (n=85) | +2.14% ± 7.44% (n=316) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -1.70% ± 0.63% (n=151) | +2.87% ± 5.42% (n=522) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -0.38% ± 1.23% (n=52) | +7.86% ± 8.11% (n=242) |
| Pinnacle | -2.40% ± 0.68% (n=99) | -1.44% ± 7.25% (n=280) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.27% ± 0.55% (n=21) | -1.49% ± 9.55% (n=118) |
| a | -1.54% ± 0.83% (n=108) | +4.11% ± 7.38% (n=341) |
| b | -1.01% ± 1.33% (n=22) | +0.41% ± 13.71% (n=46) |
| c-cagey | n/a (0) | +14.82% ± 3.70% (n=17) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -3.65% ± 1.20% (n=27) | +2.12% ± 14.50% (n=91) |
| Q2 | -2.47% ± 1.21% (n=28) | -6.67% ± 13.43% (n=93) |
| Q3 | -2.03% ± 0.94% (n=26) | +8.79% ± 11.46% (n=107) |
| Q4 | +0.50% ± 1.88% (n=28) | +3.92% ± 12.80% (n=101) |
| Q5 most open | -1.01% ± 2.16% (n=20) | +5.51% ± 10.75% (n=99) |
| n/a | -1.37% ± 1.41% (n=22) | +1.42% ± 20.89% (n=31) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.08% ± 0.76% (n=106) | +6.07% ± 6.37% (n=353) |
| yes | -3.17% ± 1.02% (n=45) | -3.82% ± 10.11% (n=169) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.56% ± 0.66% (n=143) | +2.48% ± 5.66% (n=475) |
| yes | -4.24% ± 1.07% (n=8) | +6.81% ± 18.74% (n=47) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.31% ± 0.76% (n=114) | +4.42% ± 5.93% (n=411) |
| yes | -2.93% ± 0.98% (n=37) | -2.87% ± 12.95% (n=111) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.61% ± 0.66% (n=140) | +3.69% ± 5.55% (n=480) |
| yes | -2.83% ± 2.47% (n=11) | -6.50% ± 22.70% (n=42) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.70% ± 0.63% (n=151) | +2.87% ± 5.42% (n=522) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -1.96% ± 0.87% (n=85) | +2.14% ± 7.44% (n=316) |
| narrow-63-flagged-v2 | -6.39% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-v5 | -1.30% ± 0.93% (n=65) | +3.63% ± 7.91% (n=199) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -1.82% ± 0.89% (n=60) | +2.74% ± 7.93% (n=191) |
| n/a | -1.96% ± 0.87% (n=85) | +2.14% ± 7.44% (n=316) |
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

Fixtures: eligible 134, pending 24, graded 110, excluded 60.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: over_2_5) | 44 |
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 16 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 5 | 40.0% [25.0%, 100.0%] | 28.2% | 32.2% | 0.0% [0.0%, 0.0%] | 9.7% | 11.3% |
| Q2 | 13 | 30.8% [25.0%, 100.0%] | 31.2% | 34.0% | 0.0% [0.0%, 0.0%] | 11.1% | 12.5% |
| Q3 | 24 | 20.8% [20.8%, 20.8%] | 35.0% | 36.9% | 4.2% [4.2%, 4.2%] | 13.9% | 14.6% |
| Q4 | 43 | 41.9% [0.0%, 42.9%] | 40.2% | 41.1% | 7.0% [0.0%, 7.1%] | 18.1% | 18.1% |
| Q5 most open | 25 | 40.0% [0.0%, 41.7%] | 53.8% | 54.5% | 28.0% [0.0%, 29.2%] | 31.1% | 31.2% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6519 | 0.6552 | +3.359 [-19.810, +4.233] (n=110) |
| 3+ margin | 0.3209 | 0.3290 | +8.105 [+7.870, +14.337] (n=110) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +3.179% [+3.085, +5.689] (n=1100)
- at the uncorrected fair price: +4.043% [+3.920, +7.284] (n=1100)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (power method, as clv_report). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
