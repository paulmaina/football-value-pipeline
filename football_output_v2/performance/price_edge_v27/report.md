# v27/v28 price-edge tracking

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 1120 captured recommendations; 603 graded; 98 distinct fixtures.
cagey: 892 captured recommendations; 406 graded; 81 distinct fixtures.
Actual placed bets: NOT_RECORDED

Reviewed 2026-11-08T14:27:57.418907+00:00. Frozen v27 picks: 311.

**Mean CLV vs Pinnacle close:** -2.36% ± 1.18% (n=49). **Flat-stake profit per bet:** -2.29% ± 10.25% (n=174).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | -0.79% ± 1.81% (n=26) |
| Pinnacle | -4.14% ± 1.12% (n=23) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | +0.43% ± 11.77% (n=3) |
| 1.90-2.10 | -0.53% ± 4.06% (n=8) |
| 2.10-2.40 | -9.29% (n=1) |
| <1.70 | -2.71% ± 0.91% (n=34) |
| >=2.40 | -3.82% ± 5.56% (n=3) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
|  | -3.34% ± 0.77% (n=13) |
| a | -2.17% ± 1.65% (n=34) |
| b | +0.67% ± 3.84% (n=2) |
| c-cagey | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
|  | -3.40% ± 0.64% (n=17) |
| favourite | -0.53% ± 2.16% (n=22) |
| underdog | -4.63% ± 2.30% (n=10) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | -1.12% ± 1.57% (n=30) |
| yes | -4.33% ± 1.41% (n=19) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | -2.10% ± 1.26% (n=45) |
| yes | -5.27% ± 0.75% (n=4) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | -1.74% ± 1.47% (n=37) |
| yes | -4.26% ± 1.17% (n=12) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | -2.07% ± 1.22% (n=45) |
| yes | -5.64% ± 3.97% (n=4) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| any tag | -4.49% ± 1.17% (n=23) |
| no tag | -0.48% ± 1.68% (n=26) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| Q1 cagiest | -4.48% ± 1.49% (n=12) |
| Q2 | -3.74% ± 1.82% (n=10) |
| Q3 | -2.72% ± 1.73% (n=11) |
| Q4 | -0.22% ± 3.38% (n=12) |
| Q5 most open | +1.68% ± 3.41% (n=3) |
| n/a | +2.96% (n=1) |

## CLV by value_market_group

| group | mean CLV (n) |
|---|---|
| asian_handicap | -4.25% ± 1.81% (n=12) |
| double_chance | -2.93% ± 0.73% (n=14) |
| match_winner | -1.90% ± 3.04% (n=13) |
| n/a | +4.15% ± 3.47% (n=5) |
| over_1_5 | -3.95% ± 1.14% (n=5) |

## Master shortlist (10 best bets per run)

Frozen picks: 61; CLV +0.17% ± 4.50% (n=10); realised profit per bet -8.03% ± 24.80% (n=38).

| price flag | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below value threshold | -0.55% ± 7.33% (n=4) | -24.53% ± 46.36% (n=17) |
| negative market EV nomination | -4.62% ± 2.61% (n=2) | +8.64% ± 21.41% (n=11) |
| value | +3.28% ± 8.33% (n=4) | +1.70% ± 46.73% (n=10) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 202; CLV -1.53% ± 1.10% (n=39); realised profit per bet -2.41% ± 11.06% (n=92). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-v5) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-v5 (active) | -3.79% ± 11.90% (n=85) | +39.00% (n=1) | -4.30% ± 12.00% (n=84) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -1.53% ± 1.10% (n=39) | -2.41% ± 11.06% (n=92) |
| value | -2.36% ± 1.18% (n=49) | -2.29% ± 10.25% (n=174) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -1.99% ± 0.82% (n=88) | -2.33% ± 7.71% (n=266) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -0.92% ± 1.13% (n=52) | -1.04% ± 11.40% (n=122) |
| Pinnacle | -3.54% ± 0.98% (n=36) | -3.42% ± 10.49% (n=144) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.45% ± 0.61% (n=21) | -9.61% ± 14.31% (n=61) |
| a | -1.70% ± 1.11% (n=60) | +0.57% ± 10.78% (n=164) |
| b | -0.14% ± 2.88% (n=7) | -9.72% ± 19.04% (n=29) |
| c-cagey | n/a (0) | +12.83% ± 4.82% (n=12) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -4.34% ± 1.12% (n=15) | -3.98% ± 18.45% (n=54) |
| Q2 | -3.44% ± 1.27% (n=23) | +2.83% ± 19.44% (n=41) |
| Q3 | -2.60% ± 0.98% (n=22) | +4.57% ± 17.45% (n=56) |
| Q4 | +0.78% ± 2.20% (n=21) | -24.73% ± 23.18% (n=33) |
| Q5 most open | +1.15% ± 1.90% (n=6) | -2.00% ± 16.01% (n=56) |
| n/a | +2.96% (n=1) | +5.81% ± 18.18% (n=26) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -0.92% ± 1.08% (n=54) | -1.33% ± 9.45% (n=162) |
| yes | -3.70% ± 1.04% (n=34) | -3.89% ± 13.16% (n=104) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.68% ± 0.87% (n=80) | -2.20% ± 8.07% (n=239) |
| yes | -5.12% ± 0.61% (n=8) | -3.48% ± 26.22% (n=27) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.29% ± 1.02% (n=65) | -0.31% ± 8.47% (n=209) |
| yes | -3.98% ± 0.80% (n=23) | -9.74% ± 18.15% (n=57) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.81% ± 0.84% (n=82) | -0.94% ± 7.92% (n=243) |
| yes | -4.49% ± 2.90% (n=6) | -17.04% ± 30.89% (n=23) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.99% ± 0.82% (n=88) | -2.33% ± 7.71% (n=266) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -2.36% ± 1.18% (n=49) | -2.29% ± 10.25% (n=174) |
| narrow-63-flagged-v2 | -7.87% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-v5 | -1.36% ± 1.08% (n=38) | -3.79% ± 11.90% (n=85) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -2.17% ± 1.02% (n=33) | -2.93% ± 11.40% (n=89) |
| n/a | -2.36% ± 1.18% (n=49) | -2.29% ± 10.25% (n=174) |
| value | +2.04% ± 3.38% (n=6) | +13.00% ± 25.48% (n=3) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 2249 (2249 with an offered price).
1xBet edge vs fair at capture: -3.80% ± 0.21% (n=529).
Return at the capture fair price, all tagged lines: -0.19% ± 5.06% (n=1068); plus lines only: +5.04% ± 3.97% (n=624).

- balanced: +1.26% ± 5.50% (n=951)
- low_total: -10.57% ± 10.50% (n=147)
- high_draw: -2.51% ± 8.30% (n=346)
- even_odds: -3.17% ± 13.44% (n=153)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 108, pending 46, graded 62, excluded 20.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 16 |
| no usable market-implied fit (missing input: over_2_5) | 4 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 1 | 0.0% [0.0%, 0.0%] | 29.1% | 33.5% | 0.0% [0.0%, 0.0%] | 10.6% | 12.3% |
| Q2 | 5 | 0.0% [0.0%, 0.0%] | 31.0% | 34.3% | 0.0% [0.0%, 0.0%] | 11.2% | 12.7% |
| Q3 | 15 | 20.0% [20.0%, 20.0%] | 35.0% | 36.7% | 6.7% [6.7%, 6.7%] | 13.7% | 14.4% |
| Q4 | 24 | 41.7% [41.7%, 41.7%] | 40.0% | 40.5% | 4.2% [4.2%, 4.2%] | 17.8% | 17.6% |
| Q5 most open | 17 | 47.1% [47.1%, 47.1%] | 54.1% | 54.9% | 29.4% [29.4%, 29.4%] | 31.2% | 31.6% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6295 | 0.6375 | +8.052 [+8.052, +8.052] (n=62) |
| 3+ margin | 0.3445 | 0.3537 | +9.258 [+9.258, +9.258] (n=62) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +5.236% [+5.236, +5.236] (n=620)
- at the uncorrected fair price: +6.175% [+6.175, +6.175] (n=620)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (proportional). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
