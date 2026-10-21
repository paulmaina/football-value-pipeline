# Serie A — football model report

Fixtures in this report: **20**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,970 |
| Training data through | 2026-10-19 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 36c278fa2dc4c7c97b3aa4fd88ca7a6175339007ec13e1fffadcaa0bf10addfc |
| Training as of utc | 2026-10-21T10:38:02.420843+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 31, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T10:38:02.420843+00:00', 'observations': 145, 'observations_sha256': 'be1065fe63c17ac32f8b443dc26d018c2d15e8b410f98fb4c1093f74b4f661d7', 'eligible_training_matches': 43, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 71, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 43, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '943a8b10539374c5b6d1cc29ce92768e5ddc69e5a085af9305e4efd559d49ae5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2441.837 |
| Base scoring parameter | 0.132 |
| Home-advantage parameter | 0.126 |
| Dixon-Coles low-score adjustment | -0.034 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261021T103802420843Z_475f81fdcf85defab947ca63c9b1d3f159b7cc5935256ca05f9b223c9c4d90db.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **46.9%**. Expected goals are 1.51 for Torino and 1.00 for Monza (2.51 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 45.6%; Under 3.5 goals: 75.7%; Double Chance 1X: 74.0%; Double Chance X2: 53.1%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 89.1%; BTTS Yes (both teams score): 49.8%; BTTS No (at least one team does not score): 50.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 46.9% | 2.13 |
| Draw | 27.1% | 3.69 |
| Monza win | 26.0% | 3.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.51 |
| Monza expected goals | 1.00 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 71.7% |
| Under 1.5 | 28.3% |
| Over 2.5 | 45.6% |
| Under 2.5 | 54.4% |
| Over 3.5 | 24.3% |
| Under 3.5 | 75.7% |
| Over 4.5 | 10.9% |
| Under 4.5 | 89.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.88% |
| 2 | 1-0 | 11.41% |
| 3 | 2-0 | 8.94% |
| 4 | 2-1 | 8.90% |
| 5 | 0-0 | 8.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 46.9% | 44.9% | 2.20 | +3.1% |
| Draw | 27.1% | 27.6% | 3.60 | -2.4% |
| Monza win | 26.0% | 27.6% | 3.52 | -8.4% |
| Over 2.5 | 45.6% | 48.7% | 2.02 | -7.8% |
| Under 2.5 | 54.4% | 51.3% | 1.92 | +4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 124c70f8f3248a845bdb983a54e74720 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5140 |
| Dc lambda away | 0.9959 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.8% |
| P btts no | 50.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.52 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.19 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.15 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 48.8% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 71.9% |
| Raw p under 3 5 | 75.5% |
| Raw p btts yes | 49.6% |
| P home draw | 74.0% |
| P draw away | 53.1% |
| P home away | 72.9% |
| Raw p home draw | 75.5% |
| Raw p draw away | 51.2% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.10 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.84 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | +2.0% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | 0.0396 |
| Raw ev home | 0.0746 |
| Raw edge prob draw | -0.0088 |
| Raw ev draw | -0.0396 |
| Raw edge prob away | -0.0308 |
| Raw ev away | -0.1384 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **42.2%**. Expected goals are 1.04 for Cagliari and 1.43 for Bologna (2.47 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 44.0%; Under 3.5 goals: 76.7%; Double Chance 1X: 57.8%; Double Chance X2: 71.7%; Double Chance 12 (either team wins): 70.4%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 28.3% | 3.54 |
| Draw | 29.6% | 3.38 |
| Bologna win | 42.2% | 2.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.04 |
| Bologna expected goals | 1.43 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.0% |
| Under 2.5 | 56.0% |
| Over 3.5 | 23.3% |
| Under 3.5 | 76.7% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.02% |
| 2 | 0-1 | 10.83% |
| 3 | 0-0 | 9.60% |
| 4 | 1-0 | 8.78% |
| 5 | 1-2 | 8.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 28.3% | 29.5% | 3.35 | -5.3% |
| Draw | 29.6% | 31.7% | 3.13 | -7.5% |
| Bologna win | 42.2% | 38.9% | 2.55 | +7.5% |
| Over 2.5 | 44.0% | 43.2% | 2.24 | -1.5% |
| Under 2.5 | 56.0% | 56.8% | 1.76 | -1.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | b7f0880e3da978f9481f7cb5697e2aa5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0400 |
| Dc lambda away | 1.4266 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.42 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.82 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 27.1% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 45.5% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 76.5% |
| Raw p btts yes | 49.6% |
| P home draw | 57.8% |
| P draw away | 71.7% |
| P home away | 70.4% |
| Raw p home draw | 54.5% |
| Raw p draw away | 72.9% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 3.10 |
| Reference draw odds | 2.90 |
| Reference away odds | 2.40 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.16 |
| Reference Under 2.5 odds | 1.68 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | -1.2% |
| Draw probability edge | -2.1% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | -0.0240 |
| Raw ev home | -0.0931 |
| Raw edge prob draw | -0.0423 |
| Raw ev draw | -0.1410 |
| Raw edge prob away | 0.0663 |
| Raw ev away | 0.1599 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **63.8%**. Expected goals are 2.12 for Como and 0.96 for Sassuolo (3.08 combined). The most likely exact score is 2-0 at 10.3%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 59.4%; Under 3.5 goals: 62.9%; Double Chance 1X: 84.4%; Double Chance X2: 36.2%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 54.7%; BTTS No (at least one team does not score): 45.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 63.8% | 1.57 |
| Draw | 20.6% | 4.85 |
| Sassuolo win | 15.6% | 6.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.12 |
| Sassuolo expected goals | 0.96 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 37.1% |
| Under 3.5 | 62.9% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.34% |
| 2 | 2-1 | 9.95% |
| 3 | 1-1 | 9.69% |
| 4 | 1-0 | 9.46% |
| 5 | 3-0 | 7.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 63.8% | 64.0% | 1.57 | +0.1% |
| Draw | 20.6% | 20.6% | 4.63 | -4.5% |
| Sassuolo win | 15.6% | 15.3% | 6.23 | -2.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | 08ffd99b2249c81d8a7410598f32b9b0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:39Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1168 |
| Dc lambda away | 0.9623 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.7% |
| P btts no | 45.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.33 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.43 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.04 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 63.6% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 15.8% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 54.7% |
| P home draw | 84.4% |
| P draw away | 36.2% |
| P home away | 79.4% |
| Raw p home draw | 84.2% |
| Raw p draw away | 36.4% |
| Raw p home away | 79.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.50 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.50 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:58Z |
| Home probability edge | -0.2% |
| Draw probability edge | -0.0% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.0047 |
| Raw ev home | -0.0022 |
| Raw edge prob draw | -0.0003 |
| Raw ev draw | -0.0461 |
| Raw edge prob away | 0.0050 |
| Raw ev away | -0.0129 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **63.6%**. Expected goals are 1.60 for Lazio and 0.71 for Parma (2.31 combined). The most likely exact score is 1-0 at 16.9%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 41.9%; Under 3.5 goals: 79.2%; Double Chance 1X: 86.4%; Double Chance X2: 36.4%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 40.0%; BTTS No (at least one team does not score): 60.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 63.6% | 1.57 |
| Draw | 22.8% | 4.38 |
| Parma win | 13.6% | 7.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.60 |
| Parma expected goals | 0.71 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 68.2% |
| Under 1.5 | 31.8% |
| Over 2.5 | 41.9% |
| Under 2.5 | 58.1% |
| Over 3.5 | 20.8% |
| Under 3.5 | 79.2% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.88% |
| 2 | 2-0 | 13.86% |
| 3 | 1-1 | 10.38% |
| 4 | 2-1 | 9.79% |
| 5 | 0-0 | 9.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 63.6% | 68.6% | 1.47 | -6.5% |
| Draw | 22.8% | 20.1% | 4.71 | +7.4% |
| Parma win | 13.6% | 11.3% | 8.25 | +12.4% |
| Over 2.5 | 41.9% | 49.3% | 1.94 | -18.7% |
| Under 2.5 | 58.1% | 50.7% | 2.00 | +16.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | b27cb3ea731fa3f18d05e6a627bdf984 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6029 |
| Dc lambda away | 0.7067 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 40.0% |
| P btts no | 60.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.87 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.15 |
| Fair Over 2.5 odds | 2.39 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.81 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.29 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 58.5% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 15.9% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 79.7% |
| Raw p btts yes | 40.9% |
| P home draw | 86.4% |
| P draw away | 36.4% |
| P home away | 77.2% |
| Raw p home draw | 84.1% |
| Raw p draw away | 41.5% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.40 |
| Reference draw odds | 4.20 |
| Reference away odds | 7.00 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | -5.0% |
| Draw probability edge | +2.7% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.1008 |
| Raw ev home | -0.1396 |
| Raw edge prob draw | 0.0549 |
| Raw ev draw | 0.2035 |
| Raw edge prob away | 0.0459 |
| Raw ev away | 0.3132 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **36.2%**. Expected goals are 1.20 for Napoli and 1.06 for AS Roma (2.26 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 39.6%; Under 3.5 goals: 80.7%; Double Chance 1X: 65.0%; Double Chance X2: 63.8%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 46.1%; BTTS No (at least one team does not score): 53.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 36.2% | 2.76 |
| Draw | 28.8% | 3.47 |
| AS Roma win | 35.0% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.20 |
| AS Roma expected goals | 1.06 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 39.6% |
| Under 2.5 | 60.4% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.41% |
| 2 | 0-1 | 11.65% |
| 3 | 1-0 | 11.27% |
| 4 | 0-0 | 10.61% |
| 5 | 1-2 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 36.2% | 33.7% | 2.90 | +5.1% |
| Draw | 28.8% | 28.2% | 3.54 | +1.9% |
| AS Roma win | 35.0% | 38.2% | 2.57 | -10.2% |
| Over 2.5 | 39.6% | 50.7% | 1.94 | -23.2% |
| Under 2.5 | 60.4% | 49.3% | 2.00 | +20.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:00:00+00:00 |
| Fixture id | 0b4894e9fb123ef3045269f97e339eba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2023 |
| Dc lambda away | 1.0610 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.1% |
| P btts no | 53.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.43 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.98 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.52 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 31.8% |
| Raw p over 1 5 | 66.5% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 46.2% |
| P home draw | 65.0% |
| P draw away | 63.8% |
| P home away | 71.2% |
| Raw p home draw | 68.2% |
| Raw p draw away | 61.2% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.75 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | +2.5% |
| Draw probability edge | +0.6% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -11.1% |
| Under 2.5 probability edge | +11.1% |
| Raw edge prob home | 0.0509 |
| Raw ev home | 0.1249 |
| Raw edge prob draw | 0.0129 |
| Raw ev draw | 0.0422 |
| Raw edge prob away | -0.0638 |
| Raw ev away | -0.1835 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **59.8%**. Expected goals are 2.25 for Atalanta BC and 1.11 for Frosinone (3.35 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 64.7%; Under 3.5 goals: 57.2%; Double Chance 1X: 80.5%; Double Chance X2: 40.2%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 75.6%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 59.8% | 1.67 |
| Draw | 20.7% | 4.84 |
| Frosinone win | 19.5% | 5.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.25 |
| Frosinone expected goals | 1.11 |
| Expected total goals | 3.35 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 64.7% |
| Under 2.5 | 35.3% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.4% |
| Under 4.5 | 75.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.32% |
| 2 | 2-1 | 9.30% |
| 3 | 2-0 | 8.40% |
| 4 | 1-0 | 7.19% |
| 5 | 3-1 | 6.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 59.8% | 56.8% | 1.83 | +9.4% |
| Draw | 20.7% | 21.4% | 4.26 | -11.9% |
| Frosinone win | 19.5% | 21.8% | 4.37 | -14.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 63aa6e3f679ee4c68de5b4bd8d3361bb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:39Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2475 |
| Dc lambda away | 1.1073 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.46 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.60 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.83 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.10 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 17.3% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.8% |
| Raw p btts yes | 60.2% |
| P home draw | 80.5% |
| P draw away | 40.2% |
| P home away | 79.3% |
| Raw p home draw | 82.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.70 |
| Reference draw odds | 4.24 |
| Reference away odds | 4.18 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.92 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:58Z |
| Home probability edge | +3.0% |
| Draw probability edge | -0.8% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | 0.0600 |
| Raw ev home | 0.1491 |
| Raw edge prob draw | -0.0151 |
| Raw ev draw | -0.1512 |
| Raw edge prob away | -0.0448 |
| Raw ev away | -0.2447 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **47.8%**. Expected goals are 1.40 for Genoa and 0.86 for Venezia (2.26 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 89.2%; Over 2.5 goals: 39.3%; Under 3.5 goals: 80.9%; Double Chance 1X: 75.6%; Double Chance X2: 52.2%; Double Chance 12 (either team wins): 72.1%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 43.8%; BTTS No (at least one team does not score): 56.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 47.8% | 2.09 |
| Draw | 27.9% | 3.59 |
| Venezia win | 24.4% | 4.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.40 |
| Venezia expected goals | 0.86 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.2% |
| Under 0.5 | 10.8% |
| Over 1.5 | 66.2% |
| Under 1.5 | 33.8% |
| Over 2.5 | 39.3% |
| Under 2.5 | 60.7% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.82% |
| 2 | 1-1 | 12.84% |
| 3 | 0-0 | 10.77% |
| 4 | 2-0 | 9.94% |
| 5 | 0-1 | 9.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 47.8% | 46.4% | 2.15 | +2.7% |
| Draw | 27.9% | 27.6% | 3.44 | -4.1% |
| Venezia win | 24.4% | 26.0% | 3.89 | -5.3% |
| Over 2.5 | 39.3% | 50.1% | 2.02 | -20.7% |
| Under 2.5 | 60.7% | 49.9% | 1.98 | +20.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 95cfaecfe96bb7ced1fb6af974a4110b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:39Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3976 |
| Dc lambda away | 0.8591 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.8% |
| P btts no | 56.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.29 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.23 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.71 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 66.3% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 43.8% |
| P home draw | 75.6% |
| P draw away | 52.2% |
| P home away | 72.1% |
| Raw p home draw | 77.3% |
| Raw p draw away | 50.9% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.08 |
| Reference draw odds | 3.42 |
| Reference away odds | 3.61 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.89 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:39Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | +1.4% |
| Draw probability edge | +0.3% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | 0.0272 |
| Raw ev home | 0.0563 |
| Raw edge prob draw | 0.0065 |
| Raw ev draw | -0.0299 |
| Raw edge prob away | -0.0337 |
| Raw ev away | -0.1183 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **70.8%**. Expected goals are 2.41 for Inter Milan and 0.94 for Fiorentina (3.34 combined). The most likely exact score is 2-0 at 10.4%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.2%; Under 3.5 goals: 56.9%; Double Chance 1X: 88.2%; Double Chance X2: 29.2%; Double Chance 12 (either team wins): 82.6%; Under 4.5 goals: 75.3%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.8% | 1.41 |
| Draw | 17.4% | 5.76 |
| Fiorentina win | 11.8% | 8.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.41 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.34 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 65.2% |
| Under 2.5 | 34.8% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.40% |
| 2 | 2-1 | 9.76% |
| 3 | 1-0 | 8.38% |
| 4 | 3-0 | 8.34% |
| 5 | 1-1 | 8.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.8% | 72.0% | 1.41 | -0.2% |
| Draw | 17.4% | 16.9% | 5.75 | -0.1% |
| Fiorentina win | 11.8% | 11.1% | 8.05 | -4.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T11:30:00+00:00 |
| Fixture id | c9b6c7048d8dc33dae618f67f462f67a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:39Z |
| Market best away last update utc | 2026-10-21T10:37:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4051 |
| Dc lambda away | 0.9383 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.4% |
| P btts no | 44.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.03 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.70 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.87 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.05 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 69.5% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.1% |
| Raw p btts yes | 55.6% |
| P home draw | 88.2% |
| P draw away | 29.2% |
| P home away | 82.6% |
| Raw p home draw | 87.4% |
| Raw p draw away | 30.5% |
| Raw p home away | 82.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.36 |
| Reference draw odds | 5.30 |
| Reference away odds | 7.89 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:58Z |
| Home probability edge | -1.3% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | -0.0252 |
| Raw ev home | -0.0197 |
| Raw edge prob draw | 0.0094 |
| Raw ev draw | 0.0255 |
| Raw edge prob away | 0.0158 |
| Raw ev away | 0.0175 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **62.4%**. Expected goals are 0.62 for Lecce and 1.48 for Juventus (2.11 combined). The most likely exact score is 0-1 at 19.1%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 36.4%; Under 3.5 goals: 83.3%; Double Chance 1X: 37.6%; Double Chance X2: 86.5%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 93.4%; BTTS Yes (both teams score): 35.5%; BTTS No (at least one team does not score): 64.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 13.5% | 7.40 |
| Draw | 24.1% | 4.15 |
| Juventus win | 62.4% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.62 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.11 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 63.3% |
| Under 1.5 | 36.7% |
| Over 2.5 | 36.4% |
| Under 2.5 | 63.6% |
| Over 3.5 | 16.7% |
| Under 3.5 | 83.3% |
| Over 4.5 | 6.6% |
| Under 4.5 | 93.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.07% |
| 2 | 0-2 | 14.45% |
| 3 | 0-0 | 11.17% |
| 4 | 1-1 | 10.36% |
| 5 | 1-2 | 9.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 13.5% | 11.8% | 8.19 | +10.7% |
| Draw | 24.1% | 21.2% | 4.53 | +9.2% |
| Juventus win | 62.4% | 67.0% | 1.50 | -6.4% |
| Over 2.5 | 36.4% | 51.0% | 1.92 | -30.1% |
| Under 2.5 | 63.6% | 49.0% | 2.02 | +28.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:00:00+00:00 |
| Fixture id | 63af660d4d0d52f8ac7685172ef939c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:39Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6238 |
| Dc lambda away | 1.4832 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.5% |
| P btts no | 64.5% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.95 |
| Fair Over 1.5 odds | 1.58 |
| Fair Under 1.5 odds | 2.73 |
| Fair Over 2.5 odds | 2.74 |
| Fair Under 2.5 odds | 1.57 |
| Fair Over 3.5 odds | 5.98 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.21 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 15.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 57.7% |
| Raw p over 1 5 | 62.6% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 36.3% |
| P home draw | 37.6% |
| P draw away | 86.5% |
| P home away | 75.9% |
| Raw p home draw | 42.3% |
| Raw p draw away | 84.8% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 7.52 |
| Reference draw odds | 4.34 |
| Reference away odds | 1.46 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | +1.7% |
| Draw probability edge | +2.9% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -14.6% |
| Under 2.5 probability edge | +14.6% |
| Raw edge prob home | 0.0338 |
| Raw ev home | 0.2456 |
| Raw edge prob draw | 0.0589 |
| Raw ev draw | 0.2255 |
| Raw edge prob away | -0.0927 |
| Raw ev away | -0.1339 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **54.9%**. Expected goals are 1.04 for Udinese and 1.69 for AC Milan (2.74 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 51.7%; Under 3.5 goals: 70.4%; Double Chance 1X: 45.1%; Double Chance X2: 79.6%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 85.6%; BTTS Yes (both teams score): 53.1%; BTTS No (at least one team does not score): 46.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 20.4% | 4.90 |
| Draw | 24.7% | 4.04 |
| AC Milan win | 54.9% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.69 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 76.4% |
| Under 1.5 | 23.6% |
| Over 2.5 | 51.7% |
| Under 2.5 | 48.3% |
| Over 3.5 | 29.6% |
| Under 3.5 | 70.4% |
| Over 4.5 | 14.4% |
| Under 4.5 | 85.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.77% |
| 2 | 0-1 | 11.13% |
| 3 | 1-2 | 10.19% |
| 4 | 0-2 | 9.76% |
| 5 | 0-0 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 20.4% | 17.8% | 5.47 | +11.6% |
| Draw | 24.7% | 24.6% | 4.17 | +3.1% |
| AC Milan win | 54.9% | 57.6% | 1.70 | -6.7% |
| Over 2.5 | 51.7% | 50.1% | 1.93 | -0.2% |
| Under 2.5 | 48.3% | 49.9% | 2.01 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 3564688383b255192409c9deb8e526ed |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:39Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0448 |
| Dc lambda away | 1.6923 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.1% |
| P btts no | 46.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.65 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.24 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.38 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.96 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 23.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 53.3% |
| P home draw | 45.1% |
| P draw away | 79.6% |
| P home away | 75.3% |
| Raw p home draw | 47.9% |
| Raw p draw away | 77.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 5.25 |
| Reference draw odds | 3.85 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.89 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | +2.6% |
| Draw probability edge | +0.1% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | 0.0517 |
| Raw ev home | 0.2574 |
| Raw edge prob draw | 0.0027 |
| Raw ev draw | 0.0370 |
| Raw edge prob away | -0.0544 |
| Raw ev away | -0.1136 |

</details>


---

## 2026-10-27 — AS Roma vs Cagliari

The model's most likely 1X2 outcome is **AS Roma win** at **68.9%**. Expected goals are 1.92 for AS Roma and 0.71 for Cagliari (2.63 combined). The most likely exact score is 1-0 at 14.1%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 49.8%; Under 3.5 goals: 72.5%; Double Chance 1X: 88.9%; Double Chance X2: 31.1%; Double Chance 12 (either team wins): 80.1%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 43.2%; BTTS No (at least one team does not score): 56.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 68.9% | 1.45 |
| Draw | 19.9% | 5.02 |
| Cagliari win | 11.1% | 8.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.92 |
| Cagliari expected goals | 0.71 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 49.8% |
| Under 2.5 | 50.2% |
| Over 3.5 | 27.5% |
| Under 3.5 | 72.5% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.15% |
| 2 | 2-0 | 13.92% |
| 3 | 2-1 | 9.89% |
| 4 | 1-1 | 9.38% |
| 5 | 3-0 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 68.9% | 72.1% | 1.40 | -3.5% |
| Draw | 19.9% | 18.3% | 5.20 | +3.7% |
| Cagliari win | 11.1% | 9.6% | 9.84 | +9.6% |
| Over 2.5 | 49.8% | 55.6% | 1.78 | -11.4% |
| Under 2.5 | 50.2% | 44.4% | 2.21 | +10.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7eecf109ae6a5f87441a79b0e4111982 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9213 |
| Dc lambda away | 0.7103 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 43.2% |
| P btts no | 56.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.38 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.95 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.63 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.67 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 65.8% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 43.7% |
| P home draw | 88.9% |
| P draw away | 31.1% |
| P home away | 80.1% |
| Raw p home draw | 87.3% |
| Raw p draw away | 34.2% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.36 |
| Reference draw odds | 4.93 |
| Reference away odds | 9.02 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | -3.2% |
| Draw probability edge | +1.6% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0633 |
| Raw ev home | -0.0795 |
| Raw edge prob draw | 0.0328 |
| Raw ev draw | 0.1223 |
| Raw edge prob away | 0.0305 |
| Raw ev away | 0.2465 |

</details>


---

## 2026-10-27 — Sassuolo vs Lazio

The model's most likely 1X2 outcome is **Lazio win** at **43.8%**. Expected goals are 1.17 for Sassuolo and 1.67 for Lazio (2.84 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.4%; Under 3.5 goals: 68.6%; Double Chance 1X: 56.2%; Double Chance X2: 70.1%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 29.9% | 3.34 |
| Draw | 26.2% | 3.81 |
| Lazio win | 43.8% | 2.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.17 |
| Lazio expected goals | 1.67 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.4% |
| Under 2.5 | 46.6% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.40% |
| 2 | 1-2 | 8.58% |
| 3 | 0-1 | 8.45% |
| 4 | 2-1 | 7.58% |
| 5 | 0-2 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 29.9% | 33.5% | 2.96 | -11.5% |
| Draw | 26.2% | 27.5% | 3.54 | -7.1% |
| Lazio win | 43.8% | 39.0% | 2.53 | +10.9% |
| Over 2.5 | 53.4% | 54.7% | 1.82 | -2.8% |
| Under 2.5 | 46.6% | 45.3% | 2.15 | +0.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T17:30:00+00:00 |
| Fixture id | c7445242bf16a8f37afef7863af45a78 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sassuolo |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1681 |
| Dc lambda away | 1.6709 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.27 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 26.3% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 48.7% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 56.3% |
| P home draw | 56.2% |
| P draw away | 70.1% |
| P home away | 73.8% |
| Raw p home draw | 51.3% |
| Raw p draw away | 73.7% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.84 |
| Reference draw odds | 3.43 |
| Reference away odds | 2.46 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | -3.6% |
| Draw probability edge | -1.3% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -1.3% |
| Under 2.5 probability edge | +1.3% |
| Raw edge prob home | -0.0723 |
| Raw ev home | -0.2216 |
| Raw edge prob draw | -0.0254 |
| Raw ev draw | -0.1161 |
| Raw edge prob away | 0.0977 |
| Raw ev away | 0.2330 |

</details>


---

## 2026-10-27 — Torino vs Como

The model's most likely 1X2 outcome is **Como win** at **52.0%**. Expected goals are 0.94 for Torino and 1.48 for Como (2.41 combined). The most likely exact score is 0-1 at 13.5%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 43.8%; Under 3.5 goals: 77.4%; Double Chance 1X: 48.0%; Double Chance X2: 78.2%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 21.8% | 4.58 |
| Draw | 26.2% | 3.82 |
| Como win | 52.0% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 0.94 |
| Como expected goals | 1.48 |
| Expected total goals | 2.41 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 43.8% |
| Under 2.5 | 56.2% |
| Over 3.5 | 22.6% |
| Under 3.5 | 77.4% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.48% |
| 2 | 1-1 | 12.34% |
| 3 | 0-2 | 10.29% |
| 4 | 1-2 | 9.63% |
| 5 | 0-0 | 9.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 21.8% | 20.2% | 4.89 | +6.8% |
| Draw | 26.2% | 25.2% | 3.86 | +1.1% |
| Como win | 52.0% | 54.6% | 1.83 | -4.9% |
| Over 2.5 | 43.8% | 54.7% | 1.82 | -20.2% |
| Under 2.5 | 56.2% | 45.3% | 2.15 | +20.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7d989a0a7bae47eb957731e97c5bd9c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:39Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9359 |
| Dc lambda away | 1.4781 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.07 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.28 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.42 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.09 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 23.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 49.4% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.6% |
| Raw p btts yes | 47.3% |
| P home draw | 48.0% |
| P draw away | 78.2% |
| P home away | 73.8% |
| Raw p home draw | 50.6% |
| Raw p draw away | 76.5% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 4.58 |
| Reference draw odds | 3.71 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:00Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | +1.6% |
| Draw probability edge | +1.0% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | 0.0326 |
| Raw ev home | 0.1479 |
| Raw edge prob draw | 0.0193 |
| Raw ev draw | 0.0480 |
| Raw edge prob away | -0.0519 |
| Raw ev away | -0.0965 |

</details>


---

## 2026-10-28 — AC Milan vs Bologna

The model's most likely 1X2 outcome is **AC Milan win** at **55.1%**. Expected goals are 1.62 for AC Milan and 1.04 for Bologna (2.66 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 50.3%; Under 3.5 goals: 71.9%; Double Chance 1X: 79.3%; Double Chance X2: 44.9%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 55.1% | 1.81 |
| Draw | 24.2% | 4.14 |
| Bologna win | 20.7% | 4.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.62 |
| Bologna expected goals | 1.04 |
| Expected total goals | 2.66 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 50.3% |
| Under 2.5 | 49.7% |
| Over 3.5 | 28.1% |
| Under 3.5 | 71.9% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.96% |
| 2 | 1-1 | 11.51% |
| 3 | 2-1 | 10.45% |
| 4 | 2-0 | 10.02% |
| 5 | 0-0 | 6.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 55.1% | 59.9% | 1.65 | -9.0% |
| Draw | 24.2% | 22.7% | 4.28 | +3.4% |
| Bologna win | 20.7% | 17.3% | 5.71 | +18.3% |
| Over 2.5 | 50.3% | 52.9% | 1.88 | -5.4% |
| Under 2.5 | 49.7% | 47.1% | 2.07 | +2.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 3d0b0fbec194258530882514714c74be |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6165 |
| Dc lambda away | 1.0433 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.33 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.02 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.56 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.46 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 50.3% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 24.1% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.3% |
| Raw p btts yes | 52.3% |
| P home draw | 79.3% |
| P draw away | 44.9% |
| P home away | 75.8% |
| Raw p home draw | 75.9% |
| Raw p draw away | 49.7% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.60 |
| Reference draw odds | 3.90 |
| Reference away odds | 5.00 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:59Z |
| Market reference home last update utc | 2026-10-21T10:37:59Z |
| Market reference draw last update utc | 2026-10-21T10:37:59Z |
| Market reference away last update utc | 2026-10-21T10:37:59Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | -4.8% |
| Draw probability edge | +1.4% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0963 |
| Raw ev home | -0.1698 |
| Raw edge prob draw | 0.0288 |
| Raw ev draw | 0.0957 |
| Raw edge prob away | 0.0675 |
| Raw ev away | 0.3753 |

</details>


---

## 2026-10-28 — Genoa vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **55.0%**. Expected goals are 0.78 for Genoa and 1.43 for Juventus (2.21 combined). The most likely exact score is 0-1 at 16.1%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 38.8%; Under 3.5 goals: 81.4%; Double Chance 1X: 45.0%; Double Chance X2: 81.3%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 41.3%; BTTS No (at least one team does not score): 58.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 18.7% | 5.35 |
| Draw | 26.3% | 3.80 |
| Juventus win | 55.0% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 0.78 |
| Juventus expected goals | 1.43 |
| Expected total goals | 2.21 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 65.7% |
| Under 1.5 | 34.3% |
| Over 2.5 | 38.8% |
| Under 2.5 | 61.2% |
| Over 3.5 | 18.6% |
| Under 3.5 | 81.4% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.08% |
| 2 | 1-1 | 11.94% |
| 3 | 0-2 | 11.83% |
| 4 | 0-0 | 10.70% |
| 5 | 1-2 | 9.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 18.7% | 17.3% | 5.61 | +4.9% |
| Draw | 26.3% | 24.8% | 4.01 | +5.5% |
| Juventus win | 55.0% | 57.9% | 1.70 | -6.5% |
| Over 2.5 | 38.8% | 45.6% | 2.11 | -18.2% |
| Under 2.5 | 61.2% | 54.4% | 1.85 | +13.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | 34848497b90b1392f6a767fc183d3ac1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Genoa |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7826 |
| Dc lambda away | 1.4324 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 41.3% |
| P btts no | 58.7% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.35 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.58 |
| Fair Under 2.5 odds | 1.63 |
| Fair Over 3.5 odds | 5.38 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.18 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 20.1% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 41.7% |
| P home draw | 45.0% |
| P draw away | 81.3% |
| P home away | 73.7% |
| Raw p home draw | 47.9% |
| Raw p draw away | 79.9% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 5.00 |
| Reference draw odds | 3.60 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:59Z |
| Market reference home last update utc | 2026-10-21T10:37:59Z |
| Market reference draw last update utc | 2026-10-21T10:37:59Z |
| Market reference away last update utc | 2026-10-21T10:37:59Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.66 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | +1.4% |
| Draw probability edge | +1.6% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | 0.0277 |
| Raw ev home | 0.1263 |
| Raw edge prob draw | 0.0311 |
| Raw ev draw | 0.1173 |
| Raw edge prob away | -0.0588 |
| Raw ev away | -0.1150 |

</details>


---

## 2026-10-28 — Monza vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **56.5%**. Expected goals are 0.81 for Monza and 1.88 for Napoli (2.69 combined). The most likely exact score is 0-1 at 11.2%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.6%; Under 3.5 goals: 72.3%; Double Chance 1X: 43.5%; Double Chance X2: 80.1%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 19.9% | 5.02 |
| Draw | 23.5% | 4.25 |
| Napoli win | 56.5% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 0.81 |
| Napoli expected goals | 1.88 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 27.7% |
| Under 3.5 | 72.3% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 11.24% |
| 2 | 1-1 | 11.18% |
| 3 | 0-2 | 10.86% |
| 4 | 1-2 | 8.85% |
| 5 | 0-0 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 19.9% | 24.5% | 4.01 | -20.1% |
| Draw | 23.5% | 24.5% | 3.92 | -7.8% |
| Napoli win | 56.5% | 50.9% | 1.96 | +10.8% |
| Over 2.5 | 49.6% | 54.7% | 1.80 | -10.6% |
| Under 2.5 | 50.4% | 45.3% | 2.17 | +9.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | abec89862e33762414fcb8b2232aba08 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8150 |
| Dc lambda away | 1.8784 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.46 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.61 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.58 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 62.1% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 71.6% |
| Raw p btts yes | 47.6% |
| P home draw | 43.5% |
| P draw away | 80.1% |
| P home away | 76.5% |
| Raw p home draw | 37.9% |
| Raw p draw away | 84.7% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 3.60 |
| Reference draw odds | 3.60 |
| Reference away odds | 1.85 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | -4.6% |
| Draw probability edge | -1.0% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.0921 |
| Raw ev home | -0.3854 |
| Raw edge prob draw | -0.0201 |
| Raw ev draw | -0.1170 |
| Raw edge prob away | 0.1122 |
| Raw ev away | 0.2181 |

</details>


---

## 2026-10-28 — Parma vs Udinese

The model's most likely 1X2 outcome is **Udinese win** at **38.6%**. Expected goals are 1.05 for Parma and 1.17 for Udinese (2.22 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 38.2%; Under 3.5 goals: 81.6%; Double Chance 1X: 61.4%; Double Chance X2: 68.2%; Double Chance 12 (either team wins): 70.4%; Under 4.5 goals: 92.6%; BTTS Yes (both teams score): 45.1%; BTTS No (at least one team does not score): 54.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.8% | 3.14 |
| Draw | 29.6% | 3.38 |
| Udinese win | 38.6% | 2.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.05 |
| Udinese expected goals | 1.17 |
| Expected total goals | 2.22 |
| Over 0.5 | 88.7% |
| Under 0.5 | 11.3% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 38.2% |
| Under 2.5 | 61.8% |
| Over 3.5 | 18.4% |
| Under 3.5 | 81.6% |
| Over 4.5 | 7.4% |
| Under 4.5 | 92.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.69% |
| 2 | 0-1 | 12.45% |
| 3 | 0-0 | 11.26% |
| 4 | 1-0 | 10.89% |
| 5 | 1-2 | 7.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.8% | 31.6% | 3.13 | -0.4% |
| Draw | 29.6% | 29.4% | 3.40 | +0.6% |
| Udinese win | 38.6% | 39.1% | 2.49 | -3.9% |
| Over 2.5 | 38.2% | 43.9% | 2.22 | -15.1% |
| Under 2.5 | 61.8% | 56.1% | 1.77 | +9.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 482c18a8081afdfa310324fa8f37e95a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0479 |
| Dc lambda away | 1.1681 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.1% |
| P btts no | 54.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.88 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.62 |
| Fair Under 2.5 odds | 1.62 |
| Fair Over 3.5 odds | 5.44 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.44 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 32.1% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 45.2% |
| P home draw | 61.4% |
| P draw away | 68.2% |
| P home away | 70.4% |
| Raw p home draw | 61.9% |
| Raw p draw away | 67.9% |
| Raw p home away | 70.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.90 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.61 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | 0.0051 |
| Raw ev home | 0.0037 |
| Raw edge prob draw | 0.0048 |
| Raw ev draw | 0.0144 |
| Raw edge prob away | -0.0099 |
| Raw ev away | -0.0514 |

</details>


---

## 2026-10-28 — Venezia vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **76.9%**. Expected goals are 0.69 for Venezia and 2.67 for Inter Milan (3.36 combined). The most likely exact score is 0-2 at 12.0%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 64.8%; Under 3.5 goals: 57.2%; Double Chance 1X: 23.1%; Double Chance X2: 91.3%; Double Chance 12 (either team wins): 85.6%; Under 4.5 goals: 75.5%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 8.7% | 11.44 |
| Draw | 14.4% | 6.95 |
| Inter Milan win | 76.9% | 1.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.69 |
| Inter Milan expected goals | 2.67 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 64.8% |
| Under 2.5 | 35.2% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.5% |
| Under 4.5 | 75.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.02% |
| 2 | 0-3 | 10.72% |
| 3 | 0-1 | 8.78% |
| 4 | 1-2 | 8.28% |
| 5 | 1-3 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 8.7% | 10.5% | 8.55 | -25.3% |
| Draw | 14.4% | 14.9% | 6.28 | -9.7% |
| Inter Milan win | 76.9% | 74.6% | 1.35 | +3.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 33320ad169692216a91dec030e7ef6a6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6888 |
| Dc lambda away | 2.6747 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.25 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.53 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.84 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.08 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 7.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 79.2% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 46.6% |
| P home draw | 23.1% |
| P draw away | 91.3% |
| P home away | 85.6% |
| Raw p home draw | 20.8% |
| Raw p draw away | 93.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 7.50 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.30 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:58Z |
| Home probability edge | -1.8% |
| Draw probability edge | -0.5% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.0357 |
| Raw ev home | -0.4051 |
| Raw edge prob draw | -0.0100 |
| Raw ev draw | -0.1283 |
| Raw edge prob away | 0.0457 |
| Raw ev away | 0.0687 |

</details>


---

## 2026-10-29 — Fiorentina vs Atalanta BC

The model's most likely 1X2 outcome is **Atalanta BC win** at **38.3%**. Expected goals are 1.25 for Fiorentina and 1.59 for Atalanta BC (2.84 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.7%; Under 3.5 goals: 68.5%; Double Chance 1X: 61.7%; Double Chance X2: 64.4%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 35.6% | 2.81 |
| Draw | 26.0% | 3.84 |
| Atalanta BC win | 38.3% | 2.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.25 |
| Atalanta BC expected goals | 1.59 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 53.7% |
| Under 2.5 | 46.3% |
| Over 3.5 | 31.5% |
| Under 3.5 | 68.5% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.27% |
| 2 | 2-1 | 8.72% |
| 3 | 1-0 | 8.29% |
| 4 | 1-2 | 7.89% |
| 5 | 0-1 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 35.6% | 41.6% | 2.40 | -14.5% |
| Draw | 26.0% | 26.6% | 3.69 | -4.0% |
| Atalanta BC win | 38.3% | 31.8% | 3.06 | +17.3% |
| Over 2.5 | 53.7% | 56.9% | 1.78 | -4.4% |
| Under 2.5 | 46.3% | 43.1% | 2.21 | +2.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T19:45:00+00:00 |
| Fixture id | da159a6b84dbb548b4d7b94c722caac5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2523 |
| Dc lambda away | 1.5902 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.73 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.37 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 29.7% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 44.9% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 57.2% |
| P home draw | 61.7% |
| P draw away | 64.4% |
| P home away | 74.0% |
| Raw p home draw | 55.1% |
| Raw p draw away | 70.3% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.25 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.88 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | -5.9% |
| Draw probability edge | -0.6% |
| Away probability edge | +6.5% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | -0.1187 |
| Raw ev home | -0.2872 |
| Raw edge prob draw | -0.0115 |
| Raw ev draw | -0.0611 |
| Raw edge prob away | 0.1303 |
| Raw ev away | 0.3725 |

</details>


---

## 2026-10-29 — Frosinone vs Lecce

The model's most likely 1X2 outcome is **Frosinone win** at **50.0%**. Expected goals are 1.56 for Frosinone and 0.97 for Lecce (2.53 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 46.6%; Under 3.5 goals: 75.1%; Double Chance 1X: 75.8%; Double Chance X2: 50.0%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 50.0% | 2.00 |
| Draw | 25.8% | 3.88 |
| Lecce win | 24.2% | 4.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.56 |
| Lecce expected goals | 0.97 |
| Expected total goals | 2.53 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 72.3% |
| Under 1.5 | 27.7% |
| Over 2.5 | 46.6% |
| Under 2.5 | 53.4% |
| Over 3.5 | 24.9% |
| Under 3.5 | 75.1% |
| Over 4.5 | 11.3% |
| Under 4.5 | 88.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.25% |
| 2 | 1-0 | 11.83% |
| 3 | 2-0 | 9.55% |
| 4 | 2-1 | 9.27% |
| 5 | 0-0 | 8.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 50.0% | 49.2% | 2.01 | +0.4% |
| Draw | 25.8% | 25.4% | 3.85 | -0.7% |
| Lecce win | 24.2% | 25.4% | 3.88 | -6.0% |
| Over 2.5 | 46.6% | 63.5% | 1.69 | -21.3% |
| Under 2.5 | 53.4% | 36.5% | 2.37 | +26.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T17:30:00+00:00 |
| Fixture id | 667cf69986b200753742c90cb9c5126c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:18Z |
| Market best draw last update utc | 2026-10-21T10:37:18Z |
| Market best away last update utc | 2026-10-21T10:37:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Frosinone |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5622 |
| Dc lambda away | 0.9711 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:02.420843+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.18 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.61 |
| Fair Over 2.5 odds | 2.15 |
| Fair Under 2.5 odds | 1.87 |
| Fair Over 3.5 odds | 4.01 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.81 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 50.7% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.1% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.0% |
| Raw p btts yes | 49.5% |
| P home draw | 75.8% |
| P draw away | 50.0% |
| P home away | 74.2% |
| Raw p home draw | 76.9% |
| Raw p draw away | 49.3% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.91 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.50 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:00Z |
| Market reference home last update utc | 2026-10-21T10:38:00Z |
| Market reference draw last update utc | 2026-10-21T10:38:00Z |
| Market reference away last update utc | 2026-10-21T10:38:00Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:58Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:18Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:18Z |
| Home probability edge | +0.7% |
| Draw probability edge | +0.4% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -16.9% |
| Under 2.5 probability edge | +16.9% |
| Raw edge prob home | 0.0145 |
| Raw ev home | 0.0189 |
| Raw edge prob draw | 0.0083 |
| Raw ev draw | 0.0091 |
| Raw edge prob away | -0.0228 |
| Raw ev away | -0.1038 |

</details>


---
