# v27/v28 price-edge tracking

Reviewed 2026-11-04T10:07:44.433878+00:00. Frozen v27 picks: 5.

**Mean CLV vs Pinnacle close:** +7.35% ± 6.93% (n=2). **Flat-stake profit per bet:** -28.50% ± 140.14% (n=2).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | +7.35% ± 6.93% (n=2) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | +10.89% (n=1) |
| 1.90-2.10 | n/a (0) |
| <1.70 | +3.82% (n=1) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
| a | +7.35% ± 6.93% (n=2) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
| favourite | +7.35% ± 6.93% (n=2) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | +7.35% ± 6.93% (n=2) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | +7.35% ± 6.93% (n=2) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | +7.35% ± 6.93% (n=2) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | +7.35% ± 6.93% (n=2) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| no tag | +7.35% ± 6.93% (n=2) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| n/a | +7.35% ± 6.93% (n=2) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 0; CLV n/a (0); realised profit per bet n/a (0). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded value-priced cagey-tier picks made under the active rule (narrow-63-flagged-v2) with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| value | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| a | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

### By cagey_tier_rule

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

### By price_flag

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | +7.35% ± 6.93% (n=2) | -28.50% ± 140.14% (n=2) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 392 (392 with an offered price).
1xBet edge vs fair at capture: -3.16% ± 0.47% (n=87).
Return at the capture fair price, all tagged lines: +5.12% ± 19.20% (n=102); plus lines only: -17.38% ± 15.57% (n=57).

- balanced: +5.12% ± 19.20% (n=102)
- low_total: n/a (0)
- high_draw: n/a (0)
- even_odds: n/a (0)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 19, pending 12, graded 7, excluded 39.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 20 |
| no usable market-implied fit (missing input: over_2_5) | 17 |
| no usable market-implied fit (missing input: over_2_5; Pinnacle overround outside range: h2h) | 2 |

| quintile | n | 2+ actual | 2+ corrected | 2+ uncorrected | 3+ actual | 3+ corrected | 3+ uncorrected |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 cagiest | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| Q2 | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| Q3 | 1 | 0.0% [0.0%, 0.0%] | 35.9% | 37.3% | 0.0% [0.0%, 0.0%] | 14.6% | 14.9% |
| Q4 | 4 | 50.0% [50.0%, 50.0%] | 41.0% | 40.8% | 25.0% [25.0%, 25.0%] | 18.6% | 17.8% |
| Q5 most open | 2 | 100.0% [100.0%, 100.0%] | 49.4% | 49.2% | 100.0% [100.0%, 100.0%] | 27.7% | 25.9% |

| log loss | corrected | uncorrected | paired gain x 1e-3 [95%] |
|---|---:|---:|---|
| 2+ margin | 0.6733 | 0.6841 | +10.805 [+10.805, +10.805] (n=7) |
| 3+ margin | 0.7060 | 0.7358 | +29.795 [+29.795, +29.795] (n=7) |

Calibration diagnostic, NOT achievable bookmaker ROI: return per bet when every AH +1 to +2 line on both sides is settled at its own fair price (no margin). A calibrated price returns about 0.
- at the corrected fair price: -14.504% [-14.504, -14.504] (n=70)
- at the uncorrected fair price: -14.429% [-14.429, -14.429] (n=70)

Actual rates show their 95% interval in brackets. Intervals: gameweek-block bootstrap (2000 resamples); every line of a fixture stays in its gameweek block. CORRECTION REVIEW: >= 200 graded fixtures with the 2+ paired log-loss gain interval entirely below 0; it recommends review only.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (proportional). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
