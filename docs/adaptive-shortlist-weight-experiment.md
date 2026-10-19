# Adaptive shortlist weighting: forward experiment v2

The existing automatic shortlist-weight experiment now compares its four fixed
policies (100/0, 75/25, 50/50 control and 25/75 probability/EV) with
`adaptive_evidence`. Production remains 50/50. The normal prediction command
creates the sidecar automatically; capture and the existing performance workflow
freeze, grade and report it without extra API requests.

The adaptive option changes ranking weights per **fixture and market**, not
forecast probabilities. From the same usable candidate pool and percentiles:

```
history     = clamp(development_validation_matches / 300, 0, 1)
calibration = 1 - clamp(development_calibration_penalty / 0.10, 0, 1)
agreement   = 1 - clamp(abs(raw_model_probability - reference_probability) / 0.25, 0, 1)
freshness   = 1 - clamp(quote_age_hours / 24, 0, 1)
quality     = history * calibration * agreement * freshness
p_weight    = 0.90 - 0.40 * quality
score       = p_weight * probability_percentile + (1-p_weight) * EV_percentile
```

Missing, invalid or negative evidence contributes zero quality for that factor.
The probability weight ranges from 50% to 90%; EV ranges from 50% to 10%.
Development calibration penalties include the existing development-only
high-confidence penalty when applicable. Audit outcomes, audit Brier scores,
future results and returns do not determine weights. Match statistics already
influence the model probabilities; this variant tests whether evidence quality
should change how those probabilities and quoted value are ranked.

These constants are a frozen hypothesis, not learned optimal settings. Greater
probability weight does not guarantee a safer selection: a high-probability,
negative-EV market can still rank highly. Existing probabilities, penalties,
prices, costs and hard eligibility rules are preserved, including exact quote
validation, the 48-hour window, one market per match, twelve-match cap and
Under 3.5 exclusion. Soft reliability warnings remain visible.

Every adaptive candidate records its four quality factors, combined quality,
weights and ranking score before kickoff. The variant grid and rule version are
frozen, forecast-hash-bound and replayed at capture and reporting. Changes to
rules, weights, inputs or decisions fail validation. Original production output
files are not rewritten by the experiment.

V1 archives continue to validate with their original four fixed variants.
V2 starts a new cohort: the first eligible usable pre-off capture per fixture
freezes **all five alternatives together**, using the existing 20-minute lead
rule. Repeated runs do not create repeated paper stakes within a cohort.
V1 selections remain visible in a separately labelled legacy section in Markdown
and Excel; they do not supply v2 readiness or paired control returns. A fixture
may appear once in each separately reported cohort, never twice in one cohort.
No adaptive selections are inferred from old v1 archives.

The performance report's **Experiments** sheet includes adaptive win rates,
Wilson intervals, simulated flat-stake returns, drawdown, Brier score, log loss,
calibration gap and selected weight ranges. JSON/CSV retain calibration bins,
league/market/week breakdowns and every candidate decision. Paired profit
differences use contemporaneous controls, with weekly block-bootstrap intervals
after six weeks and 100 paired fixtures. Intervals are exploratory and unadjusted
for four comparisons. Selection-cohort calibration differences are descriptive;
the forecast probabilities themselves have not changed.

Existing review gates still require 300 verified unique v2 fixtures, six weeks,
80% resolved coverage and 100 settled selections for every variant. No variant
automatically changes production. A promising result needs review and a later
untouched confirmation period before adoption.
