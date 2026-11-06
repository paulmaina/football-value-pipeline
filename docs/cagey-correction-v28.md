# Production shortlist v28: price edge with the cagey-match correction

Current runs use `no-loss-market-reference-v5` without a general narrow-margin gate and the research-based value rule. See [current no-loss selection and narrow support](cagey-market-basis-v5.md). The historical qualification rules below remain documented for replay; they are not the current cagey selection defaults.

Policy `48h-ah-price-edge-cagey-v28` (`price_edge_cagey_shortlist.py`) became
production after its pre-registered holdout gate passed. v27 and every older
policy stay replayable.

## Execution revision 2

New runs record `price_edge_execution_version: 2` in their immutable summary.
Replay treats an absent marker as revision 1 and rejects unknown revisions;
historical bundles and their picks are not rewritten.

Revision 2 checks the span of the offered quote and **every input actually used**
by the corrected distribution against the existing 10-minute synchronisation
limit. A fresh direct AH quote alone cannot satisfy this check. Fit A excludes
the unused main AH timestamp. Candidate rows expose
`corrected_input_timing_status` and `corrected_input_quote_skew_minutes`;
unsynchronised distributions cannot select a cagey-tier pick or size a stake.
New monitoring records also exclude distributions whose used inputs exceed that
span, with an explicit reason; historical revision-1 records remain replayable.

Configured `per_stake_cost_bps` is frozen as `per_stake_cost`. Corrected expected
profit deducts that cost on every settlement outcome, including refunds.
No-loss/profit probabilities also use net returns: a charged refund is a loss,
and a half-win must cover the charge to count as profitable. A
nonzero cost also requires nonnegative net expected profit for value
selection; without synchronised settlement evidence it fails closed. The gross
Pinnacle price-edge statistic and its existing thresholds remain separately
reported. Sizing and the value-tier net-cost check use the **same** matrix source:

| Pick/list | Required matrix | Stake probability basis |
|---|---|---|
| c-cagey value pick | Corrected matrix | `corrected_matrix` |
| Every other value pick, including minus and Pinnacle-quoted plus lines | Uncorrected market-implied fit B, from this fixture's inputs | `uncorrected_matrix` |
| Cagey-tier pick, including a fixture also in the value list | Corrected matrix | `corrected_matrix` |

`value_probability_basis` and `value_expected_profit` expose the value cost-check
source and net result. `uncorrected_fit` must be B; fit A cannot substitute for a
missing uncorrected fit B. Corrected fair prices and settlement columns on other
value rows remain informational and never supply their stakes or net-cost gate.
With both correction switches off, fit B can still supply uncorrected sizing and
cost qualification. The required distribution never falls back to another source.
Missing or unsynchronised inputs produce `NO_STAKE_UNAVAILABLE_DISTRIBUTION`.

Advisory plans are written to `stake_recommendations.csv` (value list) and
`cagey_tier_stake_recommendations.csv` (cagey list). The latter also sizes picks
that are absent from the value list. Each row labels its list and matrix basis.
These are separate alternative plans; exposure caps apply to each list rather
than a combined portfolio. Full generation and stored-forecast/price refreshes
regenerate both plans, preserving recorded bankroll/Kelly settings on refresh.
Older runs without recorded settings use the existing sizing defaults.

Sizing does not combine a direct Pinnacle win-share with unrelated settlement
probabilities or treat no-loss ranking as a calibration penalty. Headline and
tier realised returns deduct the frozen cost; fair-price calibration diagnostics
remain gross and do not represent executable ROI.

Cagey and tagged tracking choose the newest eligible **generation**, not the
last upload. Equal generations retain the first eligible capture. Correction
monitoring separately retains its first-eligible-capture contract.

Monitoring replay allows `max(1e-7, 1e-8 * abs(expected))` numerical drift only for
recomputed probabilities and corrected/uncorrected fair odds. This is far below
quoted decimal-price resolution and the 3-percentage-point fit residual limit.
Fixture identity, quote prices, timestamps, versions, quintile labels and
selection membership retain the strict comparison. Larger changes still fail.

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

## Correction monitoring

Every v28 run writes `cagey_correction_monitoring.csv`: one record per fixture,
including untagged fixtures, built from the market-implied distribution and
correction that run already computed (no extra fit, no extra odds request).
Each record holds:

- fixture identity, generation time and correction model version;
- corrected and uncorrected P(|margin| ≥ 2) and P(|margin| ≥ 3);
- the corrected-score quintile;
- for AH +1, +1.25, +1.5, +1.75 and +2 on both sides: the corrected and
  uncorrected fair odds, and Pinnacle's and 1xBet's offered odds where the run
  already had them, each with its quote timestamp. A price is kept only when its
  quote was fresh at generation (the selection freshness rule) and timestamped
  before kickoff; otherwise it is blank. The review re-checks each price the same way;
- `UNUSABLE` and the reason when no market-implied fit was available.

The deterministic replay check rebuilds these records, and capture archives
them only when they belong to that exact generation.

The quintile boundaries are fixed once from the production model's own
training rows (`narrow_margin_models/cagey-correction-through-2425-v1.quintiles.json`,
bound to the model's content hash and training fingerprint; written by
`py narrow_margin.py --quintiles --version cagey-correction-through-2425-v1`).
They are never recomputed from outcomes. Q1 ≤ 0.2943 < Q2 ≤ 0.3315 < Q3 ≤ 0.3704
< Q4 ≤ 0.4425 < Q5.

The review grades each fixture's first eligible pre-kickoff capture (at least
20 minutes before kickoff, inputs observed before generation). Later captures
and headline betting ROI are unaffected: ROI still uses the latest eligible
selection. The "Correction monitoring" section of the price-edge report shows:

- actual vs predicted 2+ and 3+ margin rates by quintile, with a 95% interval on each actual rate;
- corrected vs uncorrected log loss, with the paired gain;
- returns at the corrected and uncorrected fair prices (a calibration
  diagnostic, not achievable bookmaker ROI);
- eligible, pending, graded and excluded fixture counts, with exclusion reasons.

Intervals use a gameweek-block bootstrap, which keeps all of a fixture's lines in
one block. Monitoring starts with the first run that writes the file; earlier
forecasts are not backfilled. **CORRECTION REVIEW** appears when at least 200
graded fixtures have a paired 2+ log-loss gain whose 95% interval is entirely
below zero. It recommends a review only. It never changes selection, the
correction or stakes.
