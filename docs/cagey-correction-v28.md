# Production shortlist v28: price edge with the cagey-match correction

Policy `48h-ah-price-edge-cagey-v28` (`price_edge_cagey_shortlist.py`) became
production after its pre-registered holdout gate passed. v27 and every older
policy stay replayable.

## The correction (`narrow_margin.py`)

The market-implied matrix from `market_implied.py` comes from fit B (Pinnacle
1X2, O/U 2.5 and main AH), or fit A only when B is unusable. It overstates big
goal margins. Two logistic regressions recalibrate:

- P(|margin| ≥ 2);
- P(|margin| ≥ 3).

Each uses standardised features, all margin-free Pinnacle values:

- logit(matrix P for that target);
- P(over 2.5);
- |P(home) − P(away)|;
- draw probability.

The score matrix is then rescaled by margin class ({≤1}, {=2}, {≥3}) to the
corrected totals. Each class keeps its internal shape and its home/away split,
and P(≥3) is capped at P(≥2). Every AH line is priced exactly from the
corrected matrix. `corrected_cagey_score` is the corrected P(|margin| ≥ 2).

Models are stored in `narrow_margin_models/`, with `index.json` recording both versions:

| Version | Training data | Use |
|---|---|---|
| `cagey-correction-pre2024-v1` | 6,841 matches before 2024 | Holdout gate |
| `cagey-correction-through-2425-v1` | 10,956 matches through 2024/25 | Production |

Refits happen only in a future PR.

## Holdout gate (`cagey_correction_report.py`)

**GATE: PASS** on 5,434 test matches from 2024 onward. Report:
`football_output_v2/performance/cagey_correction/report.md`.

- **(a)** The 2+ margin log-loss gain is +2.35 × 1e-3 [+0.89, +3.87].
- **(b)** The pooled return on +1 to +2 is −0.04% [−0.94, +0.88] at the corrected
  fair price and +1.23% [+0.30, +2.20] at the uncorrected fair price.
- **(c)** No test season's interval is entirely below zero.

The cagiest quintile, `low_total` and `high_draw` still show a positive return
at the corrected price. These are reported, not tuned.

## Value tier

The value tier is v27 except for one change. A plus line of +1.0 or more
whose fair reference is the derived matrix (type c) is priced from the
corrected matrix. Its reference type becomes `c-cagey`, and the threshold
stays at 3%. Pinnacle-quoted lines (types a and b) keep Pinnacle as the fair
price, and the corrected-vs-Pinnacle gap is recorded. Minus lines are never
corrected. Each row records `fair_odds_uncorrected` and
`qualified_only_by_correction`.

## Cagey tier (separate list)

`cagey_tier_shortlist.csv` is never merged into the value tier.

1. **Eligible fixtures:** the cagiest 20% by `corrected_cagey_score` of the
   run's fixtures in the 48 h window. The cutoff is that run's 20th percentile,
   but never above the training-data 20th percentile. Both cutoffs are recorded.
2. **Candidates:** AH +1 to +2.25 on either side, at Pinnacle or 1xBet, with
   v27's freshness, sync, overround and odds guards. The suspicious-price
   guard (offered at most 1.15 × fair odds) applies against both v27's fair
   odds and the corrected fair odds.
3. **Qualify:** expected profit ≥ 0 under the corrected matrix, and corrected
   no-loss probability ≥ 0.85.
4. **Selection:** one row per fixture with no cap, sorted safest first. A fixture
   may also be in the value tier; `in_value_tier` marks it.

Each tier row also shows, for display only, how the bet settles under the
corrected matrix (full win, half win, push, half loss, full loss, and the
profit probability = full win + half win) and the uncorrected matrix fair
odds next to the corrected ones. None of these columns changes selection.

## Switches

`cagey_correction_config.json` holds `cagey_correction_enabled` and
`cagey_tier_enabled`, plus the model version. A switch can be on only when the
recorded gate result is PASS. With both switches off, v28 returns exactly v27's
picks and decisions. A replay uses the switches and model version recorded in
that run's summary.

## Tags

`even_odds` means both Pinnacle 1X2 win odds are at least 2.50 (raw quoted
odds). It sits alongside `balanced`, `low_total` and `high_draw`: tracking only,
and tagged fixtures always have their +1 to +2.25 lines evaluated.

## Tracking

`price_edge_tracking.py` grades both tiers in every review and writes the results to `football_output_v2/performance/price_edge_v27/`, including `cagey_tier_picks.csv`. The cagey-tier list is captured into each snapshot (`cagey_tier_shortlist.csv`) like the tagged-candidate list.

Both tiers are graded by CLV against the Pinnacle close and by realised profit. The splits are:

- tier and policy;
- bookmaker;
- reference type (a, b, c, c-cagey);
- `corrected_cagey_score` quintile;
- each tag (balanced, low_total, high_draw, even_odds);
- "qualified only because of correction".

Two flags can appear in the report:

- **CAGEY REVIEW:** at least 50 graded correction-only value picks with mean CLV below 0. It recommends `cagey_correction_enabled = false`.
- **CAGEY TIER REVIEW:** at least 50 graded cagey-tier picks whose realised ROI 95% interval is entirely below 0. It recommends `cagey_tier_enabled = false`.

Neither flag switches anything off by itself.
