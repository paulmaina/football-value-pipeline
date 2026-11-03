# v27/v28 price-edge tracking

Reviewed 2026-11-03T17:23:11.759812+00:00. Frozen v27 picks: 3.

**Mean CLV vs Pinnacle close:** n/a (0). **Flat-stake profit per bet:** n/a (0).
STOP REVIEW rule: >= 100 graded picks with mean CLV < 0.

## CLV by bookmaker

| group | mean CLV (n) |
|---|---|
| 1xBet | n/a (0) |

## CLV by odds_band

| group | mean CLV (n) |
|---|---|
| 1.70-1.90 | n/a (0) |
| <1.70 | n/a (0) |

## CLV by reference_type

| group | mean CLV (n) |
|---|---|
| a | n/a (0) |

## CLV by side_role

| group | mean CLV (n) |
|---|---|
| favourite | n/a (0) |

## CLV by balanced

| group | mean CLV (n) |
|---|---|
| no | n/a (0) |

## CLV by low_total

| group | mean CLV (n) |
|---|---|
| no | n/a (0) |

## CLV by high_draw

| group | mean CLV (n) |
|---|---|
| no | n/a (0) |

## CLV by even_odds

| group | mean CLV (n) |
|---|---|
| no | n/a (0) |

## CLV by tagged

| group | mean CLV (n) |
|---|---|
| no tag | n/a (0) |

## CLV by cagey_quintile

| group | mean CLV (n) |
|---|---|
| n/a | n/a (0) |

## Both tiers (value and cagey)

Cagey-tier picks frozen: 0; CLV n/a (0); realised profit per bet n/a (0). Correction-only value picks: CLV n/a (0).
Flags: >= 50 graded correction-only value picks with mean CLV < 0; recommends cagey_correction_enabled = false; >= 50 graded cagey-tier picks with realised ROI 95% interval entirely below 0; recommends cagey_tier_enabled = false.

### By tier

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| value | n/a (0) | n/a (0) |

### By policy

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| v28 | n/a (0) | n/a (0) |

### By bookmaker

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| 1xBet | n/a (0) | n/a (0) |

### By reference_type

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| a | n/a (0) | n/a (0) |

### By corrected_cagey_quintile

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| n/a | n/a (0) | n/a (0) |

### By balanced

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | n/a (0) | n/a (0) |

### By low_total

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | n/a (0) | n/a (0) |

### By high_draw

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | n/a (0) | n/a (0) |

### By even_odds

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | n/a (0) | n/a (0) |

### By qualified_only_by_correction

| group | mean CLV (n) | realised profit per bet (n) |
|---|---|---|
| no | n/a (0) | n/a (0) |

## Tagged candidates (narrow-margin hypothesis)

Frozen tagged candidates: 322 (322 with an offered price).
1xBet edge vs fair at capture: -3.33% ± 0.50% (n=77).
Return at the capture fair price, all tagged lines: n/a (0); plus lines only: n/a (0).

- balanced: n/a (0)
- low_total: n/a (0)
- high_draw: n/a (0)
- even_odds: n/a (0)

## Correction monitoring

Forward monitoring of cagey-correction-monitoring-v1 started 2026-11-03T13:58:25Z (first eligible capture). Earlier forecasts are not backfilled. One record per fixture: its first pre-kickoff capture at least 20 minutes before kickoff. Quintiles use the fixed training-period boundaries stored with the model.

Fixtures: eligible 19, pending 19, graded 0, excluded 24.

| excluded because | fixtures |
|---|---:|
| no usable market-implied fit (missing input: over_2_5) | 15 |
| no usable market-implied fit (missing input: home; missing input: draw; missing input: away; missing input: over_2_5; missing input: ah_main; missing input: ah_line) | 7 |
| no usable market-implied fit (missing input: over_2_5; Pinnacle overround outside range: h2h) | 2 |

No graded fixtures yet.


CLV = entry odds x Pinnacle near-kickoff fair win-share on the same AH line - 1 (proportional). Near-kickoff feed quotes, not verified official closes or executed bets. Tagged candidates are tracked for the narrow-margin hypothesis only; they never change a decision.
