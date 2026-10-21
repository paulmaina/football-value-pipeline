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
| Training as of utc | 2026-10-21T09:20:14.079252+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 31, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T09:20:14.079252+00:00', 'observations': 145, 'observations_sha256': 'be1065fe63c17ac32f8b443dc26d018c2d15e8b410f98fb4c1093f74b4f661d7', 'eligible_training_matches': 43, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 71, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 43, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '943a8b10539374c5b6d1cc29ce92768e5ddc69e5a085af9305e4efd559d49ae5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2441.962 |
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
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261021T092014079252Z_b285f850048f8efe70a2d650d4be1b2bc7b2b2df22dd913f553d3c8f096e6167.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **46.9%**. Expected goals are 1.51 for Torino and 1.00 for Monza (2.51 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 45.7%; Under 3.5 goals: 75.7%; Double Chance 1X: 73.8%; Double Chance X2: 53.1%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 89.1%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 46.9% | 2.13 |
| Draw | 27.0% | 3.71 |
| Monza win | 26.2% | 3.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.51 |
| Monza expected goals | 1.00 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 71.7% |
| Under 1.5 | 28.3% |
| Over 2.5 | 45.7% |
| Under 2.5 | 54.3% |
| Over 3.5 | 24.3% |
| Under 3.5 | 75.7% |
| Over 4.5 | 10.9% |
| Under 4.5 | 89.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.80% |
| 2 | 1-0 | 11.41% |
| 3 | 2-0 | 8.94% |
| 4 | 2-1 | 8.90% |
| 5 | 0-0 | 8.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 46.9% | 44.9% | 2.20 | +3.1% |
| Draw | 27.0% | 27.2% | 3.60 | -3.0% |
| Monza win | 26.2% | 27.9% | 3.52 | -7.9% |
| Over 2.5 | 45.7% | 48.7% | 2.02 | -7.7% |
| Under 2.5 | 54.3% | 51.3% | 1.92 | +4.3% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.7% |
| P btts no | 50.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.59 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.19 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.14 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 48.8% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 71.9% |
| Raw p under 3 5 | 75.5% |
| Raw p btts yes | 49.6% |
| P home draw | 73.8% |
| P draw away | 53.1% |
| P home away | 73.0% |
| Raw p home draw | 75.5% |
| Raw p draw away | 51.2% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.20 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.52 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | +2.0% |
| Draw probability edge | -0.3% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | 0.0394 |
| Raw ev home | 0.0746 |
| Raw edge prob draw | -0.0056 |
| Raw ev draw | -0.0396 |
| Raw edge prob away | -0.0338 |
| Raw ev away | -0.1384 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **42.3%**. Expected goals are 1.04 for Cagliari and 1.43 for Bologna (2.47 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 44.0%; Under 3.5 goals: 76.7%; Double Chance 1X: 57.7%; Double Chance X2: 71.8%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 28.2% | 3.54 |
| Draw | 29.4% | 3.40 |
| Bologna win | 42.3% | 2.36 |

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
| 1 | 1-1 | 13.97% |
| 2 | 0-1 | 10.88% |
| 3 | 0-0 | 9.56% |
| 4 | 1-0 | 8.76% |
| 5 | 1-2 | 8.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 28.2% | 29.4% | 3.35 | -5.5% |
| Draw | 29.4% | 31.5% | 3.13 | -7.8% |
| Bologna win | 42.3% | 39.2% | 2.55 | +8.0% |
| Over 2.5 | 44.0% | 43.9% | 2.24 | -1.4% |
| Under 2.5 | 56.0% | 56.1% | 1.76 | -1.5% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:12Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.46 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.43 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.80 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 27.1% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 45.5% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 76.5% |
| Raw p btts yes | 49.6% |
| P home draw | 57.7% |
| P draw away | 71.8% |
| P home away | 70.6% |
| Raw p home draw | 54.5% |
| Raw p draw away | 72.9% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.35 |
| Reference draw odds | 3.13 |
| Reference away odds | 2.52 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.24 |
| Reference Under 2.5 odds | 1.76 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | -1.1% |
| Draw probability edge | -2.0% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.0229 |
| Raw ev home | -0.0931 |
| Raw edge prob draw | -0.0401 |
| Raw ev draw | -0.1410 |
| Raw edge prob away | 0.0630 |
| Raw ev away | 0.1598 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **63.6%**. Expected goals are 2.12 for Como and 0.96 for Sassuolo (3.08 combined). The most likely exact score is 2-0 at 10.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 59.4%; Under 3.5 goals: 62.9%; Double Chance 1X: 84.3%; Double Chance X2: 36.4%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 54.7%; BTTS No (at least one team does not score): 45.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 63.6% | 1.57 |
| Draw | 20.8% | 4.81 |
| Sassuolo win | 15.7% | 6.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.12 |
| Sassuolo expected goals | 0.96 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
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
| 1 | 2-0 | 10.31% |
| 2 | 2-1 | 9.92% |
| 3 | 1-1 | 9.77% |
| 4 | 1-0 | 9.42% |
| 5 | 3-0 | 7.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 63.6% | 63.5% | 1.57 | -0.2% |
| Draw | 20.8% | 21.0% | 4.63 | -3.8% |
| Sassuolo win | 15.7% | 15.5% | 6.23 | -2.4% |

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
| Market best home last update utc | 2026-10-21T09:20:12Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.7% |
| P btts no | 45.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.17 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.42 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.05 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 63.6% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 15.8% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 54.7% |
| P home draw | 84.3% |
| P draw away | 36.4% |
| P home away | 79.2% |
| Raw p home draw | 84.2% |
| Raw p draw away | 36.4% |
| Raw p home away | 79.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.56 |
| Reference draw odds | 4.63 |
| Reference away odds | 6.23 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.72 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:13Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:13Z |
| Home probability edge | +0.0% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -7.2% |
| Under 2.5 probability edge | +7.2% |
| Raw edge prob home | 0.0000 |
| Raw ev home | -0.0022 |
| Raw edge prob draw | -0.0036 |
| Raw ev draw | -0.0461 |
| Raw edge prob away | 0.0036 |
| Raw ev away | -0.0129 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **63.1%**. Expected goals are 1.60 for Lazio and 0.71 for Parma (2.31 combined). The most likely exact score is 1-0 at 16.7%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 41.8%; Under 3.5 goals: 79.3%; Double Chance 1X: 86.2%; Double Chance X2: 36.9%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 91.2%; BTTS Yes (both teams score): 40.1%; BTTS No (at least one team does not score): 59.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 63.1% | 1.59 |
| Draw | 23.1% | 4.32 |
| Parma win | 13.8% | 7.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.60 |
| Parma expected goals | 0.71 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 68.2% |
| Under 1.5 | 31.8% |
| Over 2.5 | 41.8% |
| Under 2.5 | 58.2% |
| Over 3.5 | 20.7% |
| Under 3.5 | 79.3% |
| Over 4.5 | 8.8% |
| Under 4.5 | 91.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.74% |
| 2 | 2-0 | 13.74% |
| 3 | 1-1 | 10.52% |
| 4 | 2-1 | 9.71% |
| 5 | 0-0 | 9.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 63.1% | 67.6% | 1.47 | -7.3% |
| Draw | 23.1% | 20.7% | 4.71 | +8.9% |
| Parma win | 13.8% | 11.7% | 8.25 | +14.0% |
| Over 2.5 | 41.8% | 50.8% | 1.94 | -19.0% |
| Under 2.5 | 58.2% | 49.2% | 2.00 | +16.5% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 40.1% |
| P btts no | 59.9% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.72 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.14 |
| Fair Over 2.5 odds | 2.40 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.82 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.34 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 58.5% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 15.9% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 79.7% |
| Raw p btts yes | 40.9% |
| P home draw | 86.2% |
| P draw away | 36.9% |
| P home away | 76.9% |
| Raw p home draw | 84.1% |
| Raw p draw away | 41.5% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.47 |
| Reference draw odds | 4.71 |
| Reference away odds | 8.25 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.94 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | -4.5% |
| Draw probability edge | +2.4% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.0907 |
| Raw ev home | -0.1396 |
| Raw edge prob draw | 0.0486 |
| Raw ev draw | 0.2035 |
| Raw edge prob away | 0.0421 |
| Raw ev away | 0.3132 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **36.4%**. Expected goals are 1.20 for Napoli and 1.06 for AS Roma (2.26 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.7%; Under 3.5 goals: 80.7%; Double Chance 1X: 64.9%; Double Chance X2: 63.6%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 46.0%; BTTS No (at least one team does not score): 54.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 36.4% | 2.75 |
| Draw | 28.6% | 3.50 |
| AS Roma win | 35.1% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.20 |
| AS Roma expected goals | 1.06 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 39.7% |
| Under 2.5 | 60.3% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.31% |
| 2 | 0-1 | 11.69% |
| 3 | 1-0 | 11.30% |
| 4 | 0-0 | 10.53% |
| 5 | 1-2 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 36.4% | 33.9% | 2.90 | +5.4% |
| Draw | 28.6% | 27.7% | 3.54 | +1.2% |
| AS Roma win | 35.1% | 38.4% | 2.57 | -9.9% |
| Over 2.5 | 39.7% | 50.8% | 1.94 | -23.0% |
| Under 2.5 | 60.3% | 49.2% | 2.00 | +20.7% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Dc lambda away | 1.0611 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.0% |
| P btts no | 54.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.50 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.98 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.49 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 31.8% |
| Raw p over 1 5 | 66.5% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 46.2% |
| P home draw | 64.9% |
| P draw away | 63.6% |
| P home away | 71.4% |
| Raw p home draw | 68.2% |
| Raw p draw away | 61.2% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.90 |
| Reference draw odds | 3.54 |
| Reference away odds | 2.57 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.94 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | +2.4% |
| Draw probability edge | +0.9% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -11.1% |
| Under 2.5 probability edge | +11.1% |
| Raw edge prob home | 0.0486 |
| Raw ev home | 0.1249 |
| Raw edge prob draw | 0.0173 |
| Raw ev draw | 0.0422 |
| Raw edge prob away | -0.0659 |
| Raw ev away | -0.1835 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **58.8%**. Expected goals are 2.25 for Atalanta BC and 1.11 for Frosinone (3.35 combined). The most likely exact score is 1-1 at 9.7%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.4%; Under 3.5 goals: 57.3%; Double Chance 1X: 80.2%; Double Chance X2: 41.2%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 60.8%; BTTS No (at least one team does not score): 39.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 58.8% | 1.70 |
| Draw | 21.4% | 4.67 |
| Frosinone win | 19.8% | 5.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.25 |
| Frosinone expected goals | 1.11 |
| Expected total goals | 3.35 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 64.4% |
| Under 2.5 | 35.6% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.66% |
| 2 | 2-1 | 9.14% |
| 3 | 2-0 | 8.25% |
| 4 | 1-0 | 7.07% |
| 5 | 3-1 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 58.8% | 54.7% | 1.83 | +7.5% |
| Draw | 21.4% | 22.9% | 4.26 | -8.7% |
| Frosinone win | 19.8% | 22.3% | 4.37 | -13.4% |

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
| Market best home last update utc | 2026-10-21T09:20:12Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2476 |
| Dc lambda away | 1.1073 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.58 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.56 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.13 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 17.3% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.8% |
| Raw p btts yes | 60.2% |
| P home draw | 80.2% |
| P draw away | 41.2% |
| P home away | 78.6% |
| Raw p home draw | 82.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.81 |
| Reference draw odds | 4.26 |
| Reference away odds | 4.37 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.92 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:13Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:13Z |
| Home probability edge | +4.0% |
| Draw probability edge | -1.5% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | 0.0807 |
| Raw ev home | 0.1491 |
| Raw edge prob draw | -0.0301 |
| Raw ev draw | -0.1513 |
| Raw edge prob away | -0.0506 |
| Raw ev away | -0.2448 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **47.7%**. Expected goals are 1.40 for Genoa and 0.86 for Venezia (2.26 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 39.1%; Under 3.5 goals: 80.9%; Double Chance 1X: 76.0%; Double Chance X2: 52.3%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 47.7% | 2.10 |
| Draw | 28.4% | 3.53 |
| Venezia win | 24.0% | 4.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.40 |
| Venezia expected goals | 0.86 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 66.2% |
| Under 1.5 | 33.8% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.78% |
| 2 | 1-1 | 13.07% |
| 3 | 0-0 | 10.95% |
| 4 | 2-0 | 9.92% |
| 5 | 0-1 | 9.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 47.7% | 46.2% | 2.15 | +2.5% |
| Draw | 28.4% | 28.5% | 3.44 | -2.4% |
| Venezia win | 24.0% | 25.3% | 3.89 | -6.7% |
| Over 2.5 | 39.1% | 50.1% | 2.02 | -21.0% |
| Under 2.5 | 60.9% | 49.9% | 1.98 | +20.5% |

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
| Market best home last update utc | 2026-10-21T09:20:12Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:12Z |
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
| Dc lambda home | 1.3977 |
| Dc lambda away | 0.8591 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.9% |
| P btts no | 56.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.13 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.24 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.77 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 66.3% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 43.8% |
| P home draw | 76.0% |
| P draw away | 52.3% |
| P home away | 71.6% |
| Raw p home draw | 77.3% |
| Raw p draw away | 50.9% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.14 |
| Reference draw odds | 3.44 |
| Reference away odds | 3.87 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:12Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | +1.5% |
| Draw probability edge | -0.2% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0295 |
| Raw ev home | 0.0563 |
| Raw edge prob draw | -0.0032 |
| Raw ev draw | -0.0299 |
| Raw edge prob away | -0.0264 |
| Raw ev away | -0.1183 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **70.0%**. Expected goals are 2.41 for Inter Milan and 0.94 for Fiorentina (3.34 combined). The most likely exact score is 2-0 at 10.3%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 65.0%; Under 3.5 goals: 57.0%; Double Chance 1X: 87.6%; Double Chance X2: 30.0%; Double Chance 12 (either team wins): 82.4%; Under 4.5 goals: 75.4%; BTTS Yes (both teams score): 55.6%; BTTS No (at least one team does not score): 44.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.0% | 1.43 |
| Draw | 17.6% | 5.68 |
| Fiorentina win | 12.4% | 8.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.41 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.34 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 65.0% |
| Under 2.5 | 35.0% |
| Over 3.5 | 43.0% |
| Under 3.5 | 57.0% |
| Over 4.5 | 24.6% |
| Under 4.5 | 75.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.28% |
| 2 | 2-1 | 9.65% |
| 3 | 1-0 | 8.28% |
| 4 | 3-0 | 8.24% |
| 5 | 1-1 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.0% | 70.4% | 1.41 | -1.3% |
| Draw | 17.6% | 17.4% | 5.75 | +1.3% |
| Fiorentina win | 12.4% | 12.2% | 8.05 | -0.2% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:12Z |
| Market best away last update utc | 2026-10-21T09:20:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4050 |
| Dc lambda away | 0.9382 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.6% |
| P btts no | 44.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.64 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.66 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.06 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 69.5% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.1% |
| Raw p btts yes | 55.6% |
| P home draw | 87.6% |
| P draw away | 30.0% |
| P home away | 82.4% |
| Raw p home draw | 87.4% |
| Raw p draw away | 30.5% |
| Raw p home away | 82.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.41 |
| Reference draw odds | 5.56 |
| Reference away odds | 7.90 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:13Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:13Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0092 |
| Raw ev home | -0.0197 |
| Raw edge prob draw | 0.0044 |
| Raw ev draw | 0.0256 |
| Raw edge prob away | 0.0048 |
| Raw ev away | 0.0175 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **61.9%**. Expected goals are 0.62 for Lecce and 1.48 for Juventus (2.11 combined). The most likely exact score is 0-1 at 18.9%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 36.4%; Under 3.5 goals: 83.3%; Double Chance 1X: 38.1%; Double Chance X2: 86.2%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 93.4%; BTTS Yes (both teams score): 35.5%; BTTS No (at least one team does not score): 64.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 13.8% | 7.23 |
| Draw | 24.2% | 4.13 |
| Juventus win | 61.9% | 1.61 |

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
| 1 | 0-1 | 18.94% |
| 2 | 0-2 | 14.35% |
| 3 | 0-0 | 11.23% |
| 4 | 1-1 | 10.42% |
| 5 | 1-2 | 8.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 13.8% | 12.5% | 8.19 | +13.3% |
| Draw | 24.2% | 21.4% | 4.53 | +9.8% |
| Juventus win | 61.9% | 66.1% | 1.50 | -7.1% |
| Over 2.5 | 36.4% | 51.3% | 1.92 | -30.2% |
| Under 2.5 | 63.6% | 48.7% | 2.02 | +28.6% |

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
| Market best home last update utc | 2026-10-21T09:20:12Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Dc lambda home | 0.6239 |
| Dc lambda away | 1.4832 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.5% |
| P btts no | 64.5% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.90 |
| Fair Over 1.5 odds | 1.58 |
| Fair Under 1.5 odds | 2.72 |
| Fair Over 2.5 odds | 2.75 |
| Fair Under 2.5 odds | 1.57 |
| Fair Over 3.5 odds | 6.00 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.26 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 15.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 57.7% |
| Raw p over 1 5 | 62.6% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 36.3% |
| P home draw | 38.1% |
| P draw away | 86.2% |
| P home away | 75.8% |
| Raw p home draw | 42.3% |
| Raw p draw away | 84.8% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 7.70 |
| Reference draw odds | 4.53 |
| Reference away odds | 1.50 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | +1.4% |
| Draw probability edge | +2.8% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -14.9% |
| Under 2.5 probability edge | +14.9% |
| Raw edge prob home | 0.0275 |
| Raw ev home | 0.2457 |
| Raw edge prob draw | 0.0564 |
| Raw ev draw | 0.2256 |
| Raw edge prob away | -0.0839 |
| Raw ev away | -0.1340 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **55.2%**. Expected goals are 1.04 for Udinese and 1.69 for AC Milan (2.74 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 51.9%; Under 3.5 goals: 70.3%; Double Chance 1X: 44.8%; Double Chance X2: 79.4%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 85.5%; BTTS Yes (both teams score): 53.0%; BTTS No (at least one team does not score): 47.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 20.6% | 4.86 |
| Draw | 24.2% | 4.14 |
| AC Milan win | 55.2% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.69 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 76.4% |
| Under 1.5 | 23.6% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.50% |
| 2 | 0-1 | 11.20% |
| 3 | 1-2 | 10.26% |
| 4 | 0-2 | 9.82% |
| 5 | 0-0 | 6.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 20.6% | 18.2% | 5.48 | +12.9% |
| Draw | 24.2% | 23.5% | 4.17 | +0.7% |
| AC Milan win | 55.2% | 58.3% | 1.70 | -6.1% |
| Over 2.5 | 51.9% | 51.0% | 1.93 | +0.2% |
| Under 2.5 | 48.1% | 49.0% | 2.01 | -3.4% |

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
| Market best home last update utc | 2026-10-21T09:20:12Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Dc lambda away | 1.6924 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.0% |
| P btts no | 47.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.00 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.24 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.92 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 23.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 53.3% |
| P home draw | 44.8% |
| P draw away | 79.4% |
| P home away | 75.8% |
| Raw p home draw | 47.9% |
| Raw p draw away | 77.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 5.35 |
| Reference draw odds | 4.17 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 2.01 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | +2.4% |
| Draw probability edge | +0.7% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.0478 |
| Raw ev home | 0.2596 |
| Raw edge prob draw | 0.0142 |
| Raw ev draw | 0.0370 |
| Raw edge prob away | -0.0619 |
| Raw ev away | -0.1135 |

</details>


---

## 2026-10-27 — AS Roma vs Cagliari

The model's most likely 1X2 outcome is **AS Roma win** at **68.4%**. Expected goals are 1.92 for AS Roma and 0.71 for Cagliari (2.63 combined). The most likely exact score is 1-0 at 14.0%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 49.7%; Under 3.5 goals: 72.5%; Double Chance 1X: 88.5%; Double Chance X2: 31.6%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 43.2%; BTTS No (at least one team does not score): 56.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 68.4% | 1.46 |
| Draw | 20.1% | 4.97 |
| Cagliari win | 11.5% | 8.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.92 |
| Cagliari expected goals | 0.71 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.7% |
| Under 2.5 | 50.3% |
| Over 3.5 | 27.5% |
| Under 3.5 | 72.5% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.04% |
| 2 | 2-0 | 13.81% |
| 3 | 2-1 | 9.81% |
| 4 | 1-1 | 9.47% |
| 5 | 3-0 | 8.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 68.4% | 71.0% | 1.40 | -4.3% |
| Draw | 20.1% | 18.7% | 5.20 | +4.7% |
| Cagliari win | 11.5% | 10.3% | 9.84 | +13.0% |
| Over 2.5 | 49.7% | 55.5% | 1.78 | -11.6% |
| Under 2.5 | 50.3% | 44.5% | 2.21 | +11.2% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:12Z |
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
| Dc lambda home | 1.9214 |
| Dc lambda away | 0.7103 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 43.2% |
| P btts no | 56.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.24 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.70 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 65.8% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 43.7% |
| P home draw | 88.5% |
| P draw away | 31.6% |
| P home away | 79.9% |
| Raw p home draw | 87.3% |
| Raw p draw away | 34.2% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.40 |
| Reference draw odds | 5.20 |
| Reference away odds | 9.35 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | -2.6% |
| Draw probability edge | +1.4% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0526 |
| Raw ev home | -0.0795 |
| Raw edge prob draw | 0.0289 |
| Raw ev draw | 0.1222 |
| Raw edge prob away | 0.0238 |
| Raw ev away | 0.2464 |

</details>


---

## 2026-10-27 — Sassuolo vs Lazio

The model's most likely 1X2 outcome is **Lazio win** at **43.9%**. Expected goals are 1.17 for Sassuolo and 1.67 for Lazio (2.84 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 53.3%; Under 3.5 goals: 68.6%; Double Chance 1X: 56.1%; Double Chance X2: 70.2%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 29.8% | 3.36 |
| Draw | 26.4% | 3.79 |
| Lazio win | 43.9% | 2.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.17 |
| Lazio expected goals | 1.67 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.3% |
| Under 2.5 | 46.7% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.45% |
| 2 | 1-2 | 8.58% |
| 3 | 0-1 | 8.45% |
| 4 | 2-1 | 7.55% |
| 5 | 0-2 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 29.8% | 33.3% | 2.96 | -11.9% |
| Draw | 26.4% | 27.7% | 3.54 | -6.7% |
| Lazio win | 43.9% | 39.0% | 2.53 | +11.0% |
| Over 2.5 | 53.3% | 54.2% | 1.82 | -2.9% |
| Under 2.5 | 46.7% | 45.8% | 2.15 | +0.3% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Dc lambda home | 1.1682 |
| Dc lambda away | 1.6708 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.20 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.14 |
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
| P home draw | 56.1% |
| P draw away | 70.2% |
| P home away | 73.6% |
| Raw p home draw | 51.3% |
| Raw p draw away | 73.7% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.96 |
| Reference draw odds | 3.54 |
| Reference away odds | 2.53 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | -3.5% |
| Draw probability edge | -1.4% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0696 |
| Raw ev home | -0.2215 |
| Raw edge prob draw | -0.0277 |
| Raw ev draw | -0.1161 |
| Raw edge prob away | 0.0973 |
| Raw ev away | 0.2329 |

</details>


---

## 2026-10-27 — Torino vs Como

The model's most likely 1X2 outcome is **Como win** at **51.7%**. Expected goals are 0.94 for Torino and 1.48 for Como (2.41 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 43.8%; Under 3.5 goals: 77.4%; Double Chance 1X: 48.3%; Double Chance X2: 78.0%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 22.0% | 4.54 |
| Draw | 26.2% | 3.81 |
| Como win | 51.7% | 1.93 |

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
| 1 | 0-1 | 13.42% |
| 2 | 1-1 | 12.36% |
| 3 | 0-2 | 10.24% |
| 4 | 1-2 | 9.58% |
| 5 | 0-0 | 9.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 22.0% | 20.6% | 4.89 | +7.7% |
| Draw | 26.2% | 25.3% | 3.86 | +1.3% |
| Como win | 51.7% | 54.1% | 1.83 | -5.3% |
| Over 2.5 | 43.8% | 54.2% | 1.82 | -20.3% |
| Under 2.5 | 56.2% | 45.8% | 2.15 | +20.8% |

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
| Market best home last update utc | 2026-10-21T09:20:12Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.05 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.28 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.43 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.10 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 23.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 49.4% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.6% |
| Raw p btts yes | 47.3% |
| P home draw | 48.3% |
| P draw away | 78.0% |
| P home away | 73.8% |
| Raw p home draw | 50.6% |
| Raw p draw away | 76.5% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 4.74 |
| Reference draw odds | 3.86 |
| Reference away odds | 1.83 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | +1.5% |
| Draw probability edge | +0.9% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | 0.0291 |
| Raw ev home | 0.1480 |
| Raw edge prob draw | 0.0182 |
| Raw ev draw | 0.0480 |
| Raw edge prob away | -0.0473 |
| Raw ev away | -0.0965 |

</details>


---

## 2026-10-28 — AC Milan vs Bologna

The model's most likely 1X2 outcome is **AC Milan win** at **55.2%**. Expected goals are 1.62 for AC Milan and 1.04 for Bologna (2.66 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 50.3%; Under 3.5 goals: 71.9%; Double Chance 1X: 79.4%; Double Chance X2: 44.8%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 55.2% | 1.81 |
| Draw | 24.2% | 4.13 |
| Bologna win | 20.6% | 4.86 |

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
| 1 | 1-0 | 11.98% |
| 2 | 1-1 | 11.54% |
| 3 | 2-1 | 10.47% |
| 4 | 2-0 | 10.03% |
| 5 | 0-0 | 6.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 55.2% | 60.1% | 1.65 | -8.9% |
| Draw | 24.2% | 22.8% | 4.28 | +3.6% |
| Bologna win | 20.6% | 17.0% | 5.71 | +17.4% |
| Over 2.5 | 50.3% | 52.5% | 1.88 | -5.4% |
| Under 2.5 | 49.7% | 47.5% | 2.07 | +2.8% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Dc lambda home | 1.6166 |
| Dc lambda away | 1.0433 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.30 |
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
| P home draw | 79.4% |
| P draw away | 44.8% |
| P home away | 75.8% |
| Raw p home draw | 75.9% |
| Raw p draw away | 49.7% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.65 |
| Reference draw odds | 4.28 |
| Reference away odds | 5.71 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | -4.9% |
| Draw probability edge | +1.4% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.0981 |
| Raw ev home | -0.1698 |
| Raw edge prob draw | 0.0277 |
| Raw ev draw | 0.0957 |
| Raw edge prob away | 0.0704 |
| Raw ev away | 0.3751 |

</details>


---

## 2026-10-28 — Genoa vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **55.2%**. Expected goals are 0.78 for Genoa and 1.43 for Juventus (2.21 combined). The most likely exact score is 0-1 at 16.1%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 38.8%; Under 3.5 goals: 81.4%; Double Chance 1X: 44.8%; Double Chance X2: 81.3%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 41.2%; BTTS No (at least one team does not score): 58.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 18.7% | 5.35 |
| Draw | 26.1% | 3.83 |
| Juventus win | 55.2% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 0.78 |
| Juventus expected goals | 1.43 |
| Expected total goals | 2.21 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
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
| 1 | 0-1 | 16.14% |
| 2 | 0-2 | 11.87% |
| 3 | 1-1 | 11.86% |
| 4 | 0-0 | 10.62% |
| 5 | 1-2 | 9.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 18.7% | 17.3% | 5.61 | +4.9% |
| Draw | 26.1% | 24.4% | 4.01 | +4.7% |
| Juventus win | 55.2% | 58.3% | 1.70 | -6.2% |
| Over 2.5 | 38.8% | 46.6% | 2.11 | -18.1% |
| Under 2.5 | 61.2% | 53.4% | 1.85 | +13.2% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.42 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.58 |
| Fair Under 2.5 odds | 1.63 |
| Fair Over 3.5 odds | 5.37 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.15 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 20.1% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 41.7% |
| P home draw | 44.8% |
| P draw away | 81.3% |
| P home away | 73.9% |
| Raw p home draw | 47.9% |
| Raw p draw away | 79.9% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 5.61 |
| Reference draw odds | 4.01 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.11 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | +1.4% |
| Draw probability edge | +1.7% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | 0.0276 |
| Raw ev home | 0.1264 |
| Raw edge prob draw | 0.0349 |
| Raw ev draw | 0.1173 |
| Raw edge prob away | -0.0625 |
| Raw ev away | -0.1150 |

</details>


---

## 2026-10-28 — Monza vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **56.3%**. Expected goals are 0.81 for Monza and 1.88 for Napoli (2.69 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 49.6%; Under 3.5 goals: 72.3%; Double Chance 1X: 43.7%; Double Chance X2: 80.1%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 19.9% | 5.03 |
| Draw | 23.8% | 4.21 |
| Napoli win | 56.3% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 0.81 |
| Napoli expected goals | 1.88 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
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
| 1 | 1-1 | 11.30% |
| 2 | 0-1 | 11.20% |
| 3 | 0-2 | 10.82% |
| 4 | 1-2 | 8.82% |
| 5 | 0-0 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 19.9% | 24.4% | 4.01 | -20.2% |
| Draw | 23.8% | 25.0% | 3.92 | -6.8% |
| Napoli win | 56.3% | 50.5% | 1.96 | +10.4% |
| Over 2.5 | 49.6% | 54.8% | 1.80 | -10.8% |
| Under 2.5 | 50.4% | 45.2% | 2.17 | +9.5% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Dc lambda away | 1.8785 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 48.2% |
| P btts no | 51.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.32 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.61 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.60 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 62.1% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 71.6% |
| Raw p btts yes | 47.6% |
| P home draw | 43.7% |
| P draw away | 80.1% |
| P home away | 76.2% |
| Raw p home draw | 37.9% |
| Raw p draw away | 84.7% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 4.01 |
| Reference draw odds | 3.92 |
| Reference away odds | 1.96 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.17 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | -4.6% |
| Draw probability edge | -1.2% |
| Away probability edge | +5.8% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.0912 |
| Raw ev home | -0.3854 |
| Raw edge prob draw | -0.0249 |
| Raw ev draw | -0.1170 |
| Raw edge prob away | 0.1162 |
| Raw ev away | 0.2181 |

</details>


---

## 2026-10-28 — Parma vs Udinese

The model's most likely 1X2 outcome is **Udinese win** at **38.9%**. Expected goals are 1.05 for Parma and 1.17 for Udinese (2.22 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 38.3%; Under 3.5 goals: 81.6%; Double Chance 1X: 61.1%; Double Chance X2: 68.2%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 92.5%; BTTS Yes (both teams score): 45.1%; BTTS No (at least one team does not score): 54.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.8% | 3.15 |
| Draw | 29.4% | 3.40 |
| Udinese win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.05 |
| Udinese expected goals | 1.17 |
| Expected total goals | 2.22 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 38.3% |
| Under 2.5 | 61.7% |
| Over 3.5 | 18.4% |
| Under 3.5 | 81.6% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.58% |
| 2 | 0-1 | 12.54% |
| 3 | 0-0 | 11.18% |
| 4 | 1-0 | 10.87% |
| 5 | 1-2 | 7.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.8% | 31.4% | 3.13 | -0.6% |
| Draw | 29.4% | 28.9% | 3.40 | -0.1% |
| Udinese win | 38.9% | 39.6% | 2.49 | -3.2% |
| Over 2.5 | 38.3% | 44.2% | 2.22 | -15.0% |
| Under 2.5 | 61.7% | 55.8% | 1.77 | +9.2% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.1% |
| P btts no | 54.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.95 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.61 |
| Fair Under 2.5 odds | 1.62 |
| Fair Over 3.5 odds | 5.43 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.40 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 32.1% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 45.2% |
| P home draw | 61.1% |
| P draw away | 68.2% |
| P home away | 70.6% |
| Raw p home draw | 61.9% |
| Raw p draw away | 67.9% |
| Raw p home away | 70.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.13 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.49 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.22 |
| Reference Under 2.5 odds | 1.77 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | 0.0063 |
| Raw ev home | 0.0037 |
| Raw edge prob draw | 0.0093 |
| Raw ev draw | 0.0144 |
| Raw edge prob away | -0.0155 |
| Raw ev away | -0.0514 |

</details>


---

## 2026-10-28 — Venezia vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **76.4%**. Expected goals are 0.69 for Venezia and 2.67 for Inter Milan (3.36 combined). The most likely exact score is 0-2 at 11.9%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 64.7%; Under 3.5 goals: 57.3%; Double Chance 1X: 23.6%; Double Chance X2: 90.9%; Double Chance 12 (either team wins): 85.4%; Under 4.5 goals: 75.6%; BTTS Yes (both teams score): 47.1%; BTTS No (at least one team does not score): 52.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 9.1% | 11.05 |
| Draw | 14.6% | 6.86 |
| Inter Milan win | 76.4% | 1.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.69 |
| Inter Milan expected goals | 2.67 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 84.6% |
| Under 1.5 | 15.4% |
| Over 2.5 | 64.7% |
| Under 2.5 | 35.3% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.4% |
| Under 4.5 | 75.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 11.94% |
| 2 | 0-3 | 10.65% |
| 3 | 0-1 | 8.73% |
| 4 | 1-2 | 8.23% |
| 5 | 1-3 | 7.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 9.1% | 11.1% | 8.55 | -22.6% |
| Draw | 14.6% | 15.3% | 6.28 | -8.4% |
| Inter Milan win | 76.4% | 73.6% | 1.35 | +3.1% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Dc lambda away | 2.6745 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 47.1% |
| P btts no | 52.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.90 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.49 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.83 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.09 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 7.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 79.2% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 46.6% |
| P home draw | 23.6% |
| P draw away | 90.9% |
| P home away | 85.4% |
| Raw p home draw | 20.8% |
| Raw p draw away | 93.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 8.55 |
| Reference draw odds | 6.28 |
| Reference away odds | 1.35 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:13Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:13Z |
| Home probability edge | -2.1% |
| Draw probability edge | -0.7% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | -0.0419 |
| Raw ev home | -0.4051 |
| Raw edge prob draw | -0.0140 |
| Raw ev draw | -0.1282 |
| Raw edge prob away | 0.0558 |
| Raw ev away | 0.0687 |

</details>


---

## 2026-10-29 — Fiorentina vs Atalanta BC

The model's most likely 1X2 outcome is **Atalanta BC win** at **38.5%**. Expected goals are 1.25 for Fiorentina and 1.59 for Atalanta BC (2.84 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.7%; Under 3.5 goals: 68.5%; Double Chance 1X: 61.5%; Double Chance X2: 64.6%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 35.4% | 2.82 |
| Draw | 26.0% | 3.84 |
| Atalanta BC win | 38.5% | 2.60 |

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
| 1 | 1-1 | 12.28% |
| 2 | 2-1 | 8.67% |
| 3 | 1-0 | 8.24% |
| 4 | 1-2 | 7.93% |
| 5 | 0-1 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 35.4% | 41.2% | 2.40 | -14.9% |
| Draw | 26.0% | 26.6% | 3.69 | -3.9% |
| Atalanta BC win | 38.5% | 32.2% | 3.06 | +17.9% |
| Over 2.5 | 53.7% | 55.5% | 1.78 | -4.4% |
| Under 2.5 | 46.3% | 44.5% | 2.21 | +2.3% |

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
| Market best home last update utc | 2026-10-21T09:20:19Z |
| Market best draw last update utc | 2026-10-21T09:20:19Z |
| Market best away last update utc | 2026-10-21T09:20:19Z |
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
| Dc lambda away | 1.5903 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.72 |
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
| P home draw | 61.5% |
| P draw away | 64.6% |
| P home away | 74.0% |
| Raw p home draw | 55.1% |
| Raw p draw away | 70.3% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.40 |
| Reference draw odds | 3.69 |
| Reference away odds | 3.06 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:19Z |
| Market reference home last update utc | 2026-10-21T09:20:19Z |
| Market reference draw last update utc | 2026-10-21T09:20:19Z |
| Market reference away last update utc | 2026-10-21T09:20:19Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:19Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:19Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:19Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:19Z |
| Home probability edge | -5.7% |
| Draw probability edge | -0.6% |
| Away probability edge | +6.3% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | -0.1148 |
| Raw ev home | -0.2872 |
| Raw edge prob draw | -0.0119 |
| Raw ev draw | -0.0612 |
| Raw edge prob away | 0.1267 |
| Raw ev away | 0.3727 |

</details>


---

## 2026-10-29 — Frosinone vs Lecce

The model's most likely 1X2 outcome is **Frosinone win** at **50.0%**. Expected goals are 1.56 for Frosinone and 0.97 for Lecce (2.53 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 46.6%; Under 3.5 goals: 75.1%; Double Chance 1X: 75.8%; Double Chance X2: 50.0%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 50.0% | 2.00 |
| Draw | 25.8% | 3.87 |
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
| 1 | 1-1 | 12.27% |
| 2 | 1-0 | 11.83% |
| 3 | 2-0 | 9.55% |
| 4 | 2-1 | 9.27% |
| 5 | 0-0 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 50.0% | 49.3% | 2.01 | +0.4% |
| Draw | 25.8% | 25.5% | 3.85 | -0.5% |
| Lecce win | 24.2% | 25.3% | 3.88 | -6.2% |
| Over 2.5 | 46.6% | 58.5% | 1.69 | -21.3% |
| Under 2.5 | 53.4% | 41.5% | 2.37 | +26.7% |

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
| Market best home last update utc | 2026-10-21T09:20:18Z |
| Market best draw last update utc | 2026-10-21T09:20:18Z |
| Market best away last update utc | 2026-10-21T09:20:18Z |
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
| Dc lambda home | 1.5623 |
| Dc lambda away | 0.9711 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:20:14.079252+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.16 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.61 |
| Fair Over 2.5 odds | 2.15 |
| Fair Under 2.5 odds | 1.87 |
| Fair Over 3.5 odds | 4.01 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.82 |
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
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.01 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.88 |
| Market reference 1x2 last update utc | 2026-10-21T09:20:18Z |
| Market reference home last update utc | 2026-10-21T09:20:18Z |
| Market reference draw last update utc | 2026-10-21T09:20:18Z |
| Market reference away last update utc | 2026-10-21T09:20:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.37 |
| Market reference over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:18Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:18Z |
| Home probability edge | +0.7% |
| Draw probability edge | +0.4% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -12.0% |
| Under 2.5 probability edge | +12.0% |
| Raw edge prob home | 0.0144 |
| Raw ev home | 0.0190 |
| Raw edge prob draw | 0.0074 |
| Raw ev draw | 0.0091 |
| Raw edge prob away | -0.0218 |
| Raw ev away | -0.1039 |

</details>


---
