# v27/v28 price-edge tracking

## Recommendation history and placed bets

Every captured generation is graded at its own offered odds; re-uploads deduplicate. Repeated fixtures and overlapping lists are correlated recommendations, not independent bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.

Latest-view tables below are simulated recommendations, not executed-bet ROI.
value: 942 captured recommendations; 420 graded; 97 distinct fixtures.
cagey: 714 captured recommendations; 226 graded; 80 distinct fixtures.
Actual placed bets: NOT_RECORDED

Reviewed 2026-11-07T18:24:59.557693+00:00. Frozen v27 picks: 308.

**Mean CLV vs Pinnacle close:** -2.70% ± 1.62% (n=29). **Flat-stake profit per bet:** -1.39% ± 11.78% (n=135).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | -1.44% ± 2.55% (n=16) |
| Pinnacle | -4.25% ± 1.52% (n=13) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | +0.43% ± 11.77% (n=3) |
| 1.90-2.10 | -4.31% ± 7.39% (n=3) |
| 2.10-2.40 | -9.29% (n=1) |
| <1.70 | -2.42% ± 1.17% (n=19) |
| >=2.40 | -3.82% ± 5.56% (n=3) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
|  | -3.81% ± 1.10% (n=7) |
| a | -2.65% ± 2.26% (n=20) |
| b | +0.67% ± 3.84% (n=2) |
| c-cagey | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
|  | -3.73% ± 0.87% (n=10) |
| favourite | -1.07% ± 3.16% (n=13) |
| underdog | -4.50% ± 2.94% (n=6) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | -0.38% ± 2.82% (n=12) |
| yes | -4.34% ± 1.57% (n=17) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | -2.29% ± 1.83% (n=25) |
| yes | -5.27% ± 0.75% (n=4) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | -1.88% ± 2.31% (n=19) |
| yes | -4.26% ± 1.39% (n=10) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | -2.23% ± 1.73% (n=25) |
| yes | -5.64% ± 3.97% (n=4) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| any tag | -4.51% ± 1.28% (n=21) |
| no tag | +2.06% ± 2.96% (n=8) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| Q1 cagiest | -4.73% ± 1.51% (n=14) |
| Q2 | -2.86% ± 2.38% (n=5) |
| Q3 | -4.62% ± 5.74% (n=3) |
| Q4 | +1.85% ± 4.82% (n=5) |
| Q5 most open | +3.82% (n=1) |
| n/a | +2.96% (n=1) |

## CLV by value_market_group

| group | mean CLV (n) |
|---|---|
| asian_handicap | -4.02% ± 2.60% (n=6) |
| double_chance | -3.24% ± 1.18% (n=7) |
| match_winner | -5.19% ± 3.34% (n=7) |
| n/a | +4.15% ± 3.47% (n=5) |
| over_1_5 | -3.98% ± 1.47% (n=4) |

## Master shortlist (10 best bets per run)

Frozen picks: 48; CLV -0.62% ± 4.20% (n=7); realised profit per bet -19.75% ± 30.77% (n=28).

| price flag | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below value threshold | -0.55% ± 7.33% (n=4) | -31.50% ± 47.16% (n=16) |
| negative market EV nomination | n/a (0) | +17.75% ± 2.81% (n=4) |
| value | -0.72% ± 3.97% (n=3) | -15.00% ± 51.94% (n=8) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 222; CLV -2.94% ± 1.30% (n=19); realised profit per bet -7.13% ± 14.26% (n=55). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (no-loss-market-reference-v5) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### Cagey-tier realised profit per bet by rule

| rule | all picks | value-priced | below fair |
|---|---|---|---|
| narrow-63-flagged-v2 | +14.29% ± 11.83% (n=7) | +0.00% (n=2) | +20.00% ± 13.57% (n=5) |
| no-loss-market-reference-v5 (active) | -10.25% ± 16.09% (n=48) | n/a (0) | -10.25% ± 16.09% (n=48) |

Only the active rule's value-priced picks count toward CAGEY TIER REVIEW.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| cagey | -2.94% ± 1.30% (n=19) | -7.13% ± 14.26% (n=55) |
| value | -2.70% ± 1.62% (n=29) | -1.39% ± 11.78% (n=135) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | -2.79% ± 1.10% (n=48) | -3.05% ± 9.32% (n=190) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | -2.12% ± 1.62% (n=27) | -5.65% ± 14.80% (n=84) |
| Pinnacle | -3.66% ± 1.35% (n=21) | -0.99% ± 11.95% (n=106) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
|  | -3.70% ± 0.77% (n=13) | -11.91% ± 17.67% (n=43) |
| a | -2.60% ± 1.61% (n=31) | +1.06% ± 12.54% (n=122) |
| b | -1.36% ± 3.24% (n=4) | -13.68% ± 24.11% (n=19) |
| c-cagey | n/a (0) | +10.50% ± 7.55% (n=6) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| Q1 cagiest | -4.34% ± 1.12% (n=15) | -11.55% ± 22.63% (n=40) |
| Q2 | -3.54% ± 1.71% (n=17) | +7.52% ± 22.68% (n=31) |
| Q3 | -2.43% ± 1.64% (n=12) | +8.85% ± 20.09% (n=41) |
| Q4 | n/a (0) | -15.18% ± 28.79% (n=22) |
| Q5 most open | +5.78% ± 5.05% (n=3) | -17.70% ± 23.78% (n=30) |
| n/a | +2.96% (n=1) | +5.81% ± 18.18% (n=26) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -1.41% ± 2.07% (n=18) | -3.59% ± 12.03% (n=102) |
| yes | -3.62% ± 1.17% (n=30) | -2.43% ± 14.59% (n=88) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -2.33% ± 1.27% (n=40) | -0.98% ± 9.65% (n=171) |
| yes | -5.12% ± 0.61% (n=8) | -21.68% ± 33.56% (n=19) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -2.05% ± 1.67% (n=29) | -0.19% ± 10.82% (n=133) |
| yes | -3.92% ± 0.95% (n=19) | -9.74% ± 18.15% (n=57) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -2.55% ± 1.18% (n=42) | -0.98% ± 9.47% (n=173) |
| yes | -4.49% ± 2.90% (n=6) | -24.12% ± 39.34% (n=17) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | -2.79% ± 1.10% (n=48) | -3.05% ± 9.32% (n=190) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | -2.70% ± 1.62% (n=29) | -1.39% ± 11.78% (n=135) |
| narrow-63-flagged-v2 | -7.87% (n=1) | +14.29% ± 11.83% (n=7) |
| no-loss-market-reference-v5 | -2.66% ± 1.25% (n=18) | -10.25% ± 16.09% (n=48) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| below fair | -2.94% ± 1.30% (n=19) | -7.40% ± 14.80% (n=53) |
| n/a | -2.70% ± 1.62% (n=29) | -1.39% ± 11.78% (n=135) |
| value | n/a (0) | +0.00% (n=2) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 2049 (2049 with an offered price).
1xBet edge vs fair at capture: -3.72% ± 0.22% (n=469).
Return at the capture fair price, all tagged lines: +0.46% ± 5.56% (n=906); plus lines only: +5.50% ± 4.33% (n=531).

- balanced: +1.64% ± 5.90% (n=832)
- low_total: -10.53% ± 13.01% (n=104)
- high_draw: -2.69% ± 8.50% (n=337)
- even_odds: -6.79% ± 13.43% (n=111)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 107, pending 58, graded 49, excluded 20.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 16 |
| no usable market-implied fit (missing input: over_2_5) | 4 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 1 | 0.0% [0.0%, 0.0%] | 29.1% | 33.5% | 0.0% [0.0%, 0.0%] | 10.6% | 12.3% |
| Q2 | 4 | 0.0% [0.0%, 0.0%] | 31.2% | 34.1% | 0.0% [0.0%, 0.0%] | 11.1% | 12.5% |
| Q3 | 12 | 25.0% [25.0%, 25.0%] | 35.0% | 36.6% | 8.3% [8.3%, 8.3%] | 13.7% | 14.3% |
| Q4 | 21 | 38.1% [38.1%, 38.1%] | 40.2% | 40.7% | 4.8% [4.8%, 4.8%] | 18.1% | 17.8% |
| Q5 most open | 11 | 45.5% [45.5%, 45.5%] | 53.8% | 54.6% | 27.3% [27.3%, 27.3%] | 31.0% | 31.3% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6205 | 0.6274 | +6.890 [+6.890, +6.890] (n=49) |
| 3+ margin | 0.3376 | 0.3479 | +10.280 [+10.280, +10.280] (n=49) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: +5.380% [+5.380, +5.380] (n=490)
- at the uncorrected fair price: +6.257% [+6.257, +6.257] (n=490)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (proportional). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
