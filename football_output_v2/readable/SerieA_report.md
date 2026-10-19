# Serie A — football model report

Fixtures in this report: **20**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,968 |
| Training data through | 2026-10-18 |
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
| Training sha256 | 9da7f8899ce338f16efc44629a2e053696e86a4110a909809c193d30cec5c7b7 |
| Training as of utc | 2026-10-19T16:27:34.363041+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 68, 'bbs_added_results': 8, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 68, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-19T16:27:34.363041+00:00', 'observations': 94, 'observations_sha256': 'bd2cc9704e0cde6e04ed2c0efebf8db1f428c3eee108103050f90cc20711c00e', 'eligible_training_matches': 18, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 44, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 18, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '568702e380d5655769790b5dd145e94d116861f046a8cb350b66c72d83f20455', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 2437.534 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.125 |
| Dixon-Coles low-score adjustment | -0.034 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 2.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261019T162734363041Z_1e20d5b188b8920431ad83d871a265e2c40b40939358d011510b3a9daef14505.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
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

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Monza win** at **35.8%**. Expected goals are 1.21 for Monza and 1.30 for Cagliari (2.51 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 45.4%; Under 3.5 goals: 75.7%; Double Chance 1X: 64.7%; Double Chance X2: 64.2%; Double Chance 12 (either team wins): 71.1%; Under 4.5 goals: 89.2%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 35.8% | 2.79 |
| Draw | 28.9% | 3.46 |
| Cagliari win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.21 |
| Cagliari expected goals | 1.30 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.4% |
| Under 2.5 | 54.6% |
| Over 3.5 | 24.3% |
| Under 3.5 | 75.7% |
| Over 4.5 | 10.8% |
| Under 4.5 | 89.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.74% |
| 2 | 1-0 | 9.92% |
| 3 | 0-1 | 9.39% |
| 4 | 0-0 | 8.92% |
| 5 | 2-1 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 35.8% | 37.5% | 2.75 | -1.6% |
| Draw | 28.9% | 30.0% | 3.16 | -8.8% |
| Cagliari win | 35.3% | 32.5% | 2.77 | -2.1% |
| Over 2.5 | 45.4% | 45.5% | 1.98 | -10.1% |
| Under 2.5 | 54.6% | 54.5% | 1.88 | +2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T16:30:00+00:00 |
| Fixture id | ce94aca384a20f6af459366da6e1dd21 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2097 |
| Dc lambda away | 1.2963 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.21 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.22 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 34.0% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 38.2% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 75.6% |
| Raw p btts yes | 51.4% |
| P home draw | 64.7% |
| P draw away | 64.2% |
| P home away | 71.1% |
| Raw p home draw | 61.8% |
| Raw p draw away | 66.0% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.56 |
| Reference draw odds | 3.18 |
| Reference away odds | 2.94 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:32Z |
| Market reference home last update utc | 2026-10-19T16:27:32Z |
| Market reference draw last update utc | 2026-10-19T16:27:32Z |
| Market reference away last update utc | 2026-10-19T16:27:32Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.76 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -1.8% |
| Draw probability edge | -1.1% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0351 |
| Raw ev home | -0.0640 |
| Raw edge prob draw | -0.0215 |
| Raw ev draw | -0.1215 |
| Raw edge prob away | 0.0566 |
| Raw ev away | 0.0571 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.6%**. Expected goals are 0.97 for Parma and 1.06 for Torino (2.03 combined). The most likely exact score is 0-1 at 14.2%. Goal-market probabilities: at least one goal: 86.5%; Over 2.5 goals: 33.2%; Under 3.5 goals: 85.1%; Double Chance 1X: 61.4%; Double Chance X2: 69.8%; Double Chance 12 (either team wins): 68.8%; Under 4.5 goals: 94.4%; BTTS Yes (both teams score): 41.0%; BTTS No (at least one team does not score): 59.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 30.2% | 3.32 |
| Draw | 31.2% | 3.20 |
| Torino win | 38.6% | 2.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 0.97 |
| Torino expected goals | 1.06 |
| Expected total goals | 2.03 |
| Over 0.5 | 86.5% |
| Under 0.5 | 13.5% |
| Over 1.5 | 60.7% |
| Under 1.5 | 39.3% |
| Over 2.5 | 33.2% |
| Under 2.5 | 66.8% |
| Over 3.5 | 14.9% |
| Under 3.5 | 85.1% |
| Over 4.5 | 5.6% |
| Under 4.5 | 94.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.18% |
| 2 | 1-1 | 13.86% |
| 3 | 0-0 | 13.49% |
| 4 | 1-0 | 11.62% |
| 5 | 0-2 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 30.2% | 28.6% | 3.43 | +3.5% |
| Draw | 31.2% | 31.0% | 3.17 | -1.0% |
| Torino win | 38.6% | 40.4% | 2.45 | -5.4% |
| Over 2.5 | 33.2% | 38.8% | 2.49 | -17.3% |
| Under 2.5 | 66.8% | 61.2% | 1.63 | +8.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T18:45:00+00:00 |
| Fixture id | 07014d9adc65ca39710bd9f0c7c0d3f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9669 |
| Dc lambda away | 1.0632 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 41.0% |
| P btts no | 59.0% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.41 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.55 |
| Fair Over 2.5 odds | 3.01 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 6.73 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 17.98 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 31.8% |
| Unadjusted draw probability | 31.4% |
| Unadjusted away-win probability | 36.8% |
| Raw p over 1 5 | 60.7% |
| Raw p under 3 5 | 85.2% |
| Raw p btts yes | 41.0% |
| P home draw | 61.4% |
| P draw away | 69.8% |
| P home away | 68.8% |
| Raw p home draw | 63.2% |
| Raw p draw away | 68.2% |
| Raw p home away | 68.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.38 |
| Reference draw odds | 3.12 |
| Reference away odds | 2.41 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:32Z |
| Market reference home last update utc | 2026-10-19T16:27:32Z |
| Market reference draw last update utc | 2026-10-19T16:27:32Z |
| Market reference away last update utc | 2026-10-19T16:27:32Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.41 |
| Reference Under 2.5 odds | 1.58 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +1.6% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | 0.0322 |
| Raw ev home | 0.0899 |
| Raw edge prob draw | 0.0043 |
| Raw ev draw | -0.0034 |
| Raw edge prob away | -0.0366 |
| Raw ev away | -0.0987 |
| Market p home draw | 59.8% |
| Market home draw odds | 1.62 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-19T16:27:26Z |
| Market reference home draw last update utc | 2026-10-19T16:27:32Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.4% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-19T16:27:26Z |
| Market reference draw away last update utc | 2026-10-19T16:27:32Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 68.8% |
| Market home away odds | 1.41 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-19T16:27:26Z |
| Market reference home away last update utc | 2026-10-19T16:27:32Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.61 |
| Market reference dc draw away odds | 1.35 |
| Market reference dc home away odds | 1.40 |
| Market p over 1 5 | 65.9% |
| Market over 1 5 odds | 1.44 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-19T16:26:09Z |
| Market reference over 1 5 odds | 1.48 |
| Market reference over 1 5 opposite odds | 2.75 |
| Market reference over 1 5 last update utc | 2026-10-19T16:27:27Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 82.0% |
| Market under 3 5 odds | 1.18 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-19T16:26:09Z |
| Market reference under 3 5 odds | 1.18 |
| Market reference under 3 5 opposite odds | 4.20 |
| Market reference under 3 5 last update utc | 2026-10-19T16:27:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 48.8% |
| Market btts yes odds | 1.98 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-19T16:27:26Z |
| Market reference btts yes odds | 1.91 |
| Market reference btts yes opposite odds | 1.83 |
| Market reference btts yes last update utc | 2026-10-19T16:27:27Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **48.0%**. Expected goals are 1.51 for Torino and 0.96 for Monza (2.46 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 44.5%; Under 3.5 goals: 76.7%; Double Chance 1X: 74.8%; Double Chance X2: 52.0%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 48.4%; BTTS No (at least one team does not score): 51.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 48.0% | 2.08 |
| Draw | 26.9% | 3.72 |
| Monza win | 25.2% | 3.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.51 |
| Monza expected goals | 0.96 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.5% |
| Under 2.5 | 55.5% |
| Over 3.5 | 23.3% |
| Under 3.5 | 76.7% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.71% |
| 2 | 1-0 | 12.02% |
| 3 | 2-0 | 9.35% |
| 4 | 0-0 | 8.96% |
| 5 | 2-1 | 8.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 48.0% | 46.3% | 2.15 | +3.2% |
| Draw | 26.9% | 26.9% | 3.62 | -2.7% |
| Monza win | 25.2% | 26.7% | 3.64 | -8.5% |
| Over 2.5 | 44.5% | 46.5% | 2.11 | -6.0% |
| Under 2.5 | 55.5% | 53.5% | 1.85 | +2.6% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5062 |
| Dc lambda away | 0.9556 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.16 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.29 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.68 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 49.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.9% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 48.3% |
| P home draw | 74.8% |
| P draw away | 52.0% |
| P home away | 73.1% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.4% |
| Raw p home away | 73.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.09 |
| Reference draw odds | 3.52 |
| Reference away odds | 3.54 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:32Z |
| Market reference home last update utc | 2026-10-19T16:27:32Z |
| Market reference draw last update utc | 2026-10-19T16:27:32Z |
| Market reference away last update utc | 2026-10-19T16:27:32Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +1.6% |
| Draw probability edge | -0.0% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | 0.0328 |
| Raw ev home | 0.0669 |
| Raw edge prob draw | -0.0008 |
| Raw ev draw | -0.0290 |
| Raw edge prob away | -0.0319 |
| Raw ev away | -0.1427 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **41.8%**. Expected goals are 1.06 for Cagliari and 1.40 for Bologna (2.45 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 43.7%; Under 3.5 goals: 76.9%; Double Chance 1X: 58.2%; Double Chance X2: 71.4%; Double Chance 12 (either team wins): 70.5%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 50.0%; BTTS No (at least one team does not score): 50.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 28.6% | 3.49 |
| Draw | 29.5% | 3.39 |
| Bologna win | 41.8% | 2.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.06 |
| Bologna expected goals | 1.40 |
| Expected total goals | 2.45 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 70.5% |
| Under 1.5 | 29.5% |
| Over 2.5 | 43.7% |
| Under 2.5 | 56.3% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.99% |
| 2 | 0-1 | 10.96% |
| 3 | 0-0 | 9.64% |
| 4 | 1-0 | 8.85% |
| 5 | 1-2 | 8.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 28.6% | 29.2% | 3.35 | -4.1% |
| Draw | 29.5% | 31.3% | 3.13 | -7.6% |
| Bologna win | 41.8% | 39.4% | 2.52 | +5.4% |
| Over 2.5 | 43.7% | 43.5% | 2.24 | -2.1% |
| Under 2.5 | 56.3% | 56.5% | 1.76 | -0.9% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0562 |
| Dc lambda away | 1.3953 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.37 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.29 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.96 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 28.0% |
| Unadjusted draw probability | 27.7% |
| Unadjusted away-win probability | 44.3% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.8% |
| Raw p btts yes | 49.5% |
| P home draw | 58.2% |
| P draw away | 71.4% |
| P home away | 70.5% |
| Raw p home draw | 55.7% |
| Raw p draw away | 72.0% |
| Raw p home away | 72.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.25 |
| Reference draw odds | 3.04 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:32Z |
| Market reference home last update utc | 2026-10-19T16:27:32Z |
| Market reference draw last update utc | 2026-10-19T16:27:32Z |
| Market reference away last update utc | 2026-10-19T16:27:32Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.17 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -0.6% |
| Draw probability edge | -1.8% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | -0.0119 |
| Raw ev home | -0.0606 |
| Raw edge prob draw | -0.0365 |
| Raw ev draw | -0.1332 |
| Raw edge prob away | 0.0484 |
| Raw ev away | 0.1155 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **65.8%**. Expected goals are 2.12 for Como and 0.96 for Sassuolo (3.08 combined). The most likely exact score is 2-0 at 10.7%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 60.0%; Under 3.5 goals: 62.5%; Double Chance 1X: 85.6%; Double Chance X2: 34.2%; Double Chance 12 (either team wins): 80.2%; Under 4.5 goals: 79.8%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 65.8% | 1.52 |
| Draw | 19.8% | 5.05 |
| Sassuolo win | 14.4% | 6.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.12 |
| Sassuolo expected goals | 0.96 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 81.9% |
| Under 1.5 | 18.1% |
| Over 2.5 | 60.0% |
| Under 2.5 | 40.0% |
| Over 3.5 | 37.5% |
| Under 3.5 | 62.5% |
| Over 4.5 | 20.2% |
| Under 4.5 | 79.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.65% |
| 2 | 2-1 | 10.25% |
| 3 | 1-0 | 9.72% |
| 4 | 1-1 | 9.30% |
| 5 | 3-0 | 7.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 65.8% | 68.0% | 1.49 | -1.9% |
| Draw | 19.8% | 19.0% | 4.94 | -2.2% |
| Sassuolo win | 14.4% | 13.0% | 7.10 | +2.1% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1218 |
| Dc lambda away | 0.9624 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.23 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.51 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.67 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.96 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 63.7% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 15.8% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 62.8% |
| Raw p btts yes | 54.7% |
| P home draw | 85.6% |
| P draw away | 34.2% |
| P home away | 80.2% |
| Raw p home draw | 84.2% |
| Raw p draw away | 36.3% |
| Raw p home away | 79.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.44 |
| Reference draw odds | 4.80 |
| Reference away odds | 6.90 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:32Z |
| Market reference home last update utc | 2026-10-19T16:27:32Z |
| Market reference draw last update utc | 2026-10-19T16:27:32Z |
| Market reference away last update utc | 2026-10-19T16:27:32Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:27Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:27Z |
| Home probability edge | -2.2% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.0435 |
| Raw ev home | -0.0516 |
| Raw edge prob draw | 0.0153 |
| Raw ev draw | 0.0156 |
| Raw edge prob away | 0.0283 |
| Raw ev away | 0.1212 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **61.2%**. Expected goals are 1.57 for Lazio and 0.72 for Parma (2.29 combined). The most likely exact score is 1-0 at 16.6%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 41.0%; Under 3.5 goals: 79.8%; Double Chance 1X: 85.0%; Double Chance X2: 38.8%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 40.4%; BTTS No (at least one team does not score): 59.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 61.2% | 1.63 |
| Draw | 23.8% | 4.20 |
| Parma win | 15.0% | 6.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.57 |
| Parma expected goals | 0.72 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 67.5% |
| Under 1.5 | 32.5% |
| Over 2.5 | 41.0% |
| Under 2.5 | 59.0% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.61% |
| 2 | 2-0 | 13.32% |
| 3 | 1-1 | 10.82% |
| 4 | 0-0 | 9.62% |
| 5 | 2-1 | 9.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 61.2% | 65.2% | 1.55 | -5.1% |
| Draw | 23.8% | 21.5% | 4.43 | +5.4% |
| Parma win | 15.0% | 13.3% | 7.00 | +5.0% |
| Over 2.5 | 41.0% | 48.7% | 2.02 | -17.1% |
| Under 2.5 | 59.0% | 51.3% | 1.92 | +13.2% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5652 |
| Dc lambda away | 0.7215 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 40.4% |
| P btts no | 59.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.39 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.08 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.95 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.75 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 57.2% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 16.7% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 41.0% |
| P home draw | 85.0% |
| P draw away | 38.8% |
| P home away | 76.2% |
| Raw p home draw | 83.3% |
| Raw p draw away | 42.8% |
| Raw p home away | 73.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.50 |
| Reference draw odds | 4.30 |
| Reference away odds | 6.80 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:32Z |
| Market reference home last update utc | 2026-10-19T16:27:32Z |
| Market reference draw last update utc | 2026-10-19T16:27:32Z |
| Market reference away last update utc | 2026-10-19T16:27:32Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -4.0% |
| Draw probability edge | +2.3% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | -0.0805 |
| Raw ev home | -0.1137 |
| Raw edge prob draw | 0.0458 |
| Raw ev draw | 0.1556 |
| Raw edge prob away | 0.0347 |
| Raw ev away | 0.1714 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **36.4%**. Expected goals are 1.20 for Napoli and 1.06 for AS Roma (2.27 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.7%; Under 3.5 goals: 80.6%; Double Chance 1X: 64.9%; Double Chance X2: 63.6%; Double Chance 12 (either team wins): 71.5%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 46.0%; BTTS No (at least one team does not score): 54.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 36.4% | 2.75 |
| Draw | 28.5% | 3.51 |
| AS Roma win | 35.1% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.20 |
| AS Roma expected goals | 1.06 |
| Expected total goals | 2.27 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 39.7% |
| Under 2.5 | 60.3% |
| Over 3.5 | 19.4% |
| Under 3.5 | 80.6% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.28% |
| 2 | 0-1 | 11.69% |
| 3 | 1-0 | 11.29% |
| 4 | 0-0 | 10.49% |
| 5 | 1-2 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 36.4% | 33.9% | 2.90 | +5.4% |
| Draw | 28.5% | 27.6% | 3.54 | +0.9% |
| AS Roma win | 35.1% | 38.5% | 2.57 | -9.7% |
| Over 2.5 | 39.7% | 50.7% | 1.94 | -22.9% |
| Under 2.5 | 60.3% | 49.3% | 2.00 | +20.5% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
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
| Dc lambda home | 1.2030 |
| Dc lambda away | 1.0625 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.0% |
| P btts no | 54.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.54 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.17 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.45 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 31.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 46.2% |
| P home draw | 64.9% |
| P draw away | 63.6% |
| P home away | 71.5% |
| Raw p home draw | 68.2% |
| Raw p draw away | 61.2% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.82 |
| Reference draw odds | 3.44 |
| Reference away odds | 2.50 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:32Z |
| Market reference home last update utc | 2026-10-19T16:27:32Z |
| Market reference draw last update utc | 2026-10-19T16:27:32Z |
| Market reference away last update utc | 2026-10-19T16:27:32Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:32Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +2.4% |
| Draw probability edge | +0.9% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0484 |
| Raw ev home | 0.1245 |
| Raw edge prob draw | 0.0184 |
| Raw ev draw | 0.0419 |
| Raw edge prob away | -0.0668 |
| Raw ev away | -0.1829 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **59.1%**. Expected goals are 2.25 for Atalanta BC and 1.11 for Frosinone (3.36 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 64.5%; Under 3.5 goals: 57.2%; Double Chance 1X: 80.4%; Double Chance X2: 40.9%; Double Chance 12 (either team wins): 78.8%; Under 4.5 goals: 75.6%; BTTS Yes (both teams score): 60.8%; BTTS No (at least one team does not score): 39.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 59.1% | 1.69 |
| Draw | 21.2% | 4.71 |
| Frosinone win | 19.6% | 5.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.25 |
| Frosinone expected goals | 1.11 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 64.5% |
| Under 2.5 | 35.5% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.4% |
| Under 4.5 | 75.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.57% |
| 2 | 2-1 | 9.18% |
| 3 | 2-0 | 8.29% |
| 4 | 1-0 | 7.09% |
| 5 | 3-1 | 6.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 59.1% | 55.4% | 1.81 | +7.0% |
| Draw | 21.2% | 22.6% | 4.26 | -9.5% |
| Frosinone win | 19.6% | 22.0% | 4.37 | -14.2% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2511 |
| Dc lambda away | 1.1075 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.83 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.59 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.82 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.11 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 17.2% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 60.2% |
| P home draw | 80.4% |
| P draw away | 40.9% |
| P home away | 78.8% |
| Raw p home draw | 82.8% |
| Raw p draw away | 37.1% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.76 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.25 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:27Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:27Z |
| Home probability edge | +3.7% |
| Draw probability edge | -1.3% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | 0.0748 |
| Raw ev home | 0.1377 |
| Raw edge prob draw | -0.0269 |
| Raw ev draw | -0.1523 |
| Raw edge prob away | -0.0479 |
| Raw ev away | -0.2463 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **47.8%**. Expected goals are 1.40 for Genoa and 0.86 for Venezia (2.26 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 89.1%; Over 2.5 goals: 39.2%; Under 3.5 goals: 80.8%; Double Chance 1X: 76.1%; Double Chance X2: 52.2%; Double Chance 12 (either team wins): 71.7%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 47.8% | 2.09 |
| Draw | 28.3% | 3.54 |
| Venezia win | 23.9% | 4.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.40 |
| Venezia expected goals | 0.86 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.1% |
| Under 0.5 | 10.9% |
| Over 1.5 | 66.3% |
| Under 1.5 | 33.7% |
| Over 2.5 | 39.2% |
| Under 2.5 | 60.8% |
| Over 3.5 | 19.2% |
| Under 3.5 | 80.8% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.81% |
| 2 | 1-1 | 13.04% |
| 3 | 0-0 | 10.91% |
| 4 | 2-0 | 9.95% |
| 5 | 0-1 | 9.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 47.8% | 46.5% | 2.14 | +2.4% |
| Draw | 28.3% | 28.4% | 3.44 | -2.7% |
| Venezia win | 23.9% | 25.1% | 3.87 | -7.6% |
| Over 2.5 | 39.2% | 50.1% | 1.97 | -22.7% |
| Under 2.5 | 60.8% | 49.9% | 1.98 | +20.4% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3992 |
| Dc lambda away | 0.8599 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.9% |
| P btts no | 56.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.17 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.22 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.71 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 49.2% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 43.9% |
| P home draw | 76.1% |
| P draw away | 52.2% |
| P home away | 71.7% |
| Raw p home draw | 77.3% |
| Raw p draw away | 50.8% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.08 |
| Reference draw odds | 3.34 |
| Reference away odds | 3.76 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +1.3% |
| Draw probability edge | -0.1% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | 0.0261 |
| Raw ev home | 0.0519 |
| Raw edge prob draw | -0.0020 |
| Raw ev draw | -0.0304 |
| Raw edge prob away | -0.0242 |
| Raw ev away | -0.1230 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **70.6%**. Expected goals are 2.41 for Inter Milan and 0.94 for Fiorentina (3.35 combined). The most likely exact score is 2-0 at 10.4%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.3%; Under 3.5 goals: 56.8%; Double Chance 1X: 87.9%; Double Chance X2: 29.4%; Double Chance 12 (either team wins): 82.7%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 55.5%; BTTS No (at least one team does not score): 44.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.6% | 1.42 |
| Draw | 17.3% | 5.78 |
| Fiorentina win | 12.1% | 8.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.41 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.35 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 65.3% |
| Under 2.5 | 34.7% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.35% |
| 2 | 2-1 | 9.73% |
| 3 | 1-0 | 8.33% |
| 4 | 3-0 | 8.31% |
| 5 | 1-1 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.6% | 71.7% | 1.41 | -0.4% |
| Draw | 17.3% | 16.8% | 5.56 | -3.8% |
| Fiorentina win | 12.1% | 11.5% | 7.90 | -4.5% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4078 |
| Dc lambda away | 0.9397 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.5% |
| P btts no | 44.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.19 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.71 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.88 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.04 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 69.5% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.0% |
| Raw p btts yes | 55.7% |
| P home draw | 87.9% |
| P draw away | 29.4% |
| P home away | 82.7% |
| Raw p home draw | 87.4% |
| Raw p draw away | 30.5% |
| Raw p home away | 82.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.37 |
| Reference draw odds | 5.40 |
| Reference away odds | 7.70 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:32Z |
| Market reference home last update utc | 2026-10-19T16:27:32Z |
| Market reference draw last update utc | 2026-10-19T16:27:32Z |
| Market reference away last update utc | 2026-10-19T16:27:32Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:27Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:27Z |
| Home probability edge | -1.1% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | -0.0213 |
| Raw ev home | -0.0195 |
| Raw edge prob draw | 0.0103 |
| Raw ev draw | -0.0091 |
| Raw edge prob away | 0.0110 |
| Raw ev away | -0.0015 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **62.5%**. Expected goals are 0.62 for Lecce and 1.49 for Juventus (2.11 combined). The most likely exact score is 0-1 at 19.0%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 36.6%; Under 3.5 goals: 83.2%; Double Chance 1X: 37.5%; Double Chance X2: 86.4%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 93.4%; BTTS Yes (both teams score): 35.5%; BTTS No (at least one team does not score): 64.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 13.6% | 7.37 |
| Draw | 24.0% | 4.17 |
| Juventus win | 62.5% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.62 |
| Juventus expected goals | 1.49 |
| Expected total goals | 2.11 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 63.4% |
| Under 1.5 | 36.6% |
| Over 2.5 | 36.6% |
| Under 2.5 | 63.4% |
| Over 3.5 | 16.8% |
| Under 3.5 | 83.2% |
| Over 4.5 | 6.6% |
| Under 4.5 | 93.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.04% |
| 2 | 0-2 | 14.46% |
| 3 | 0-0 | 11.10% |
| 4 | 1-1 | 10.32% |
| 5 | 1-2 | 9.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 13.6% | 11.9% | 7.70 | +4.4% |
| Draw | 24.0% | 21.0% | 4.53 | +8.7% |
| Juventus win | 62.5% | 67.1% | 1.50 | -6.3% |
| Over 2.5 | 36.6% | 51.3% | 1.92 | -29.8% |
| Under 2.5 | 63.4% | 48.7% | 2.02 | +28.2% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6241 |
| Dc lambda away | 1.4866 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.5% |
| P btts no | 64.5% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.01 |
| Fair Over 1.5 odds | 1.58 |
| Fair Under 1.5 odds | 2.74 |
| Fair Over 2.5 odds | 2.74 |
| Fair Under 2.5 odds | 1.58 |
| Fair Over 3.5 odds | 5.96 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.11 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 15.2% |
| Unadjusted draw probability | 27.0% |
| Unadjusted away-win probability | 57.8% |
| Raw p over 1 5 | 62.7% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 36.3% |
| P home draw | 37.5% |
| P draw away | 86.4% |
| P home away | 76.0% |
| Raw p home draw | 42.2% |
| Raw p draw away | 84.8% |
| Raw p home away | 73.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 7.50 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.46 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +1.6% |
| Draw probability edge | +3.0% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -14.7% |
| Under 2.5 probability edge | +14.7% |
| Raw edge prob home | 0.0323 |
| Raw ev home | 0.1685 |
| Raw edge prob draw | 0.0605 |
| Raw ev draw | 0.2235 |
| Raw edge prob away | -0.0928 |
| Raw ev away | -0.1328 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **55.7%**. Expected goals are 1.05 for Udinese and 1.70 for AC Milan (2.74 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 52.1%; Under 3.5 goals: 70.2%; Double Chance 1X: 44.3%; Double Chance X2: 79.6%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 85.5%; BTTS Yes (both teams score): 53.0%; BTTS No (at least one team does not score): 47.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 20.4% | 4.91 |
| Draw | 24.0% | 4.17 |
| AC Milan win | 55.7% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.05 |
| AC Milan expected goals | 1.70 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 52.1% |
| Under 2.5 | 47.9% |
| Over 3.5 | 29.8% |
| Under 3.5 | 70.2% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.40% |
| 2 | 0-1 | 11.25% |
| 3 | 1-2 | 10.34% |
| 4 | 0-2 | 9.89% |
| 5 | 0-0 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 20.4% | 17.8% | 5.35 | +8.9% |
| Draw | 24.0% | 23.1% | 4.17 | -0.1% |
| AC Milan win | 55.7% | 59.2% | 1.70 | -5.3% |
| Over 2.5 | 52.1% | 51.0% | 1.93 | +0.6% |
| Under 2.5 | 47.9% | 49.0% | 2.01 | -3.7% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0456 |
| Dc lambda away | 1.6955 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.0% |
| P btts no | 47.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.17 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.26 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.36 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.87 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 23.0% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 52.2% |
| Raw p over 1 5 | 76.3% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 53.3% |
| P home draw | 44.3% |
| P draw away | 79.6% |
| P home away | 76.0% |
| Raw p home draw | 47.8% |
| Raw p draw away | 77.0% |
| Raw p home away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 5.20 |
| Reference draw odds | 4.05 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.94 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +2.6% |
| Draw probability edge | +0.9% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | 0.0520 |
| Raw ev home | 0.2283 |
| Raw edge prob draw | 0.0176 |
| Raw ev draw | 0.0359 |
| Raw edge prob away | -0.0696 |
| Raw ev away | -0.1126 |

</details>


---

## 2026-10-27 — AS Roma vs Cagliari

The model's most likely 1X2 outcome is **AS Roma win** at **68.3%**. Expected goals are 1.88 for AS Roma and 0.72 for Cagliari (2.60 combined). The most likely exact score is 1-0 at 14.4%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 49.2%; Under 3.5 goals: 73.1%; Double Chance 1X: 88.5%; Double Chance X2: 31.7%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 43.2%; BTTS No (at least one team does not score): 56.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 68.3% | 1.46 |
| Draw | 20.1% | 4.96 |
| Cagliari win | 11.5% | 8.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.88 |
| Cagliari expected goals | 0.72 |
| Expected total goals | 2.60 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 49.2% |
| Under 2.5 | 50.8% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.42% |
| 2 | 2-0 | 13.87% |
| 3 | 2-1 | 10.02% |
| 4 | 1-1 | 9.47% |
| 5 | 3-0 | 8.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 68.3% | 72.2% | 1.40 | -4.3% |
| Draw | 20.1% | 18.1% | 5.20 | +4.7% |
| Cagliari win | 11.5% | 9.7% | 9.35 | +7.7% |
| Over 2.5 | 49.2% | 55.7% | 1.78 | -12.5% |
| Under 2.5 | 50.8% | 44.3% | 2.21 | +12.4% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8776 |
| Dc lambda away | 0.7220 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 43.2% |
| P btts no | 56.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.16 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.87 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.91 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 64.5% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 73.6% |
| Raw p under 3 5 | 73.6% |
| Raw p btts yes | 43.9% |
| P home draw | 88.5% |
| P draw away | 31.7% |
| P home away | 79.9% |
| Raw p home draw | 86.7% |
| Raw p draw away | 35.5% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.36 |
| Reference draw odds | 5.00 |
| Reference away odds | 9.00 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -3.8% |
| Draw probability edge | +2.0% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | -0.0765 |
| Raw ev home | -0.0968 |
| Raw edge prob draw | 0.0403 |
| Raw ev draw | 0.1522 |
| Raw edge prob away | 0.0361 |
| Raw ev away | 0.2463 |

</details>


---

## 2026-10-27 — Sassuolo vs Lazio

The model's most likely 1X2 outcome is **Lazio win** at **44.0%**. Expected goals are 1.17 for Sassuolo and 1.67 for Lazio (2.84 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.5%; Under 3.5 goals: 68.6%; Double Chance 1X: 56.0%; Double Chance X2: 70.3%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 29.7% | 3.36 |
| Draw | 26.3% | 3.81 |
| Lazio win | 44.0% | 2.27 |

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
| Over 2.5 | 53.5% |
| Under 2.5 | 46.5% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.42% |
| 2 | 1-2 | 8.60% |
| 3 | 0-1 | 8.44% |
| 4 | 2-1 | 7.54% |
| 5 | 0-2 | 7.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 29.7% | 33.2% | 2.96 | -12.0% |
| Draw | 26.3% | 27.6% | 3.54 | -7.0% |
| Lazio win | 44.0% | 39.2% | 2.53 | +11.3% |
| Over 2.5 | 53.5% | 54.5% | 1.82 | -2.7% |
| Under 2.5 | 46.5% | 45.5% | 2.15 | +0.1% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sassuolo |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1687 |
| Dc lambda away | 1.6740 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.28 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.41 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 26.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 48.8% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 56.4% |
| P home draw | 56.0% |
| P draw away | 70.3% |
| P home away | 73.7% |
| Raw p home draw | 51.2% |
| Raw p draw away | 73.7% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.88 |
| Reference draw odds | 3.44 |
| Reference away odds | 2.46 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -3.5% |
| Draw probability edge | -1.3% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | -0.0697 |
| Raw ev home | -0.2227 |
| Raw edge prob draw | -0.0267 |
| Raw ev draw | -0.1169 |
| Raw edge prob away | 0.0964 |
| Raw ev away | 0.2345 |

</details>


---

## 2026-10-27 — Torino vs Como

The model's most likely 1X2 outcome is **Como win** at **52.5%**. Expected goals are 0.92 for Torino and 1.49 for Como (2.41 combined). The most likely exact score is 0-1 at 13.6%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 43.7%; Under 3.5 goals: 77.5%; Double Chance 1X: 47.5%; Double Chance X2: 78.5%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 46.7%; BTTS No (at least one team does not score): 53.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 21.5% | 4.65 |
| Draw | 26.0% | 3.84 |
| Como win | 52.5% | 1.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 0.92 |
| Como expected goals | 1.49 |
| Expected total goals | 2.41 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 43.7% |
| Under 2.5 | 56.3% |
| Over 3.5 | 22.5% |
| Under 3.5 | 77.5% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.56% |
| 2 | 1-1 | 12.26% |
| 3 | 0-2 | 10.45% |
| 4 | 1-2 | 9.59% |
| 5 | 0-0 | 9.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 21.5% | 20.2% | 4.74 | +1.9% |
| Draw | 26.0% | 25.1% | 3.86 | +0.5% |
| Como win | 52.5% | 54.7% | 1.83 | -4.0% |
| Over 2.5 | 43.7% | 54.5% | 1.82 | -20.4% |
| Under 2.5 | 56.3% | 45.5% | 2.15 | +21.0% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9178 |
| Dc lambda away | 1.4931 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 46.7% |
| P btts no | 53.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.05 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.29 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.44 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.14 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 22.8% |
| Unadjusted draw probability | 27.0% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 69.8% |
| Raw p under 3 5 | 77.6% |
| Raw p btts yes | 47.0% |
| P home draw | 47.5% |
| P draw away | 78.5% |
| P home away | 74.0% |
| Raw p home draw | 49.8% |
| Raw p draw away | 77.2% |
| Raw p home away | 73.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.60 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +1.3% |
| Draw probability edge | +1.0% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | 0.0253 |
| Raw ev home | 0.0793 |
| Raw edge prob draw | 0.0195 |
| Raw ev draw | 0.0428 |
| Raw edge prob away | -0.0447 |
| Raw ev away | -0.0811 |

</details>


---

## 2026-10-28 — AC Milan vs Bologna

The model's most likely 1X2 outcome is **AC Milan win** at **55.7%**. Expected goals are 1.62 for AC Milan and 1.04 for Bologna (2.66 combined). The most likely exact score is 1-0 at 12.1%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 50.5%; Under 3.5 goals: 71.9%; Double Chance 1X: 79.7%; Double Chance X2: 44.3%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 55.7% | 1.80 |
| Draw | 24.0% | 4.16 |
| Bologna win | 20.3% | 4.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.62 |
| Bologna expected goals | 1.04 |
| Expected total goals | 2.66 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.1% |
| Under 3.5 | 71.9% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.05% |
| 2 | 1-1 | 11.44% |
| 3 | 2-1 | 10.56% |
| 4 | 2-0 | 10.10% |
| 5 | 0-0 | 6.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 55.7% | 61.0% | 1.65 | -8.1% |
| Draw | 24.0% | 22.4% | 4.28 | +2.8% |
| Bologna win | 20.3% | 16.5% | 5.71 | +16.0% |
| Over 2.5 | 50.5% | 52.5% | 1.88 | -5.1% |
| Under 2.5 | 49.5% | 47.5% | 2.07 | +2.5% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6174 |
| Dc lambda away | 1.0449 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.45 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.04 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.42 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 50.3% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 24.1% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 52.4% |
| P home draw | 79.7% |
| P draw away | 44.3% |
| P home away | 76.0% |
| Raw p home draw | 75.9% |
| Raw p draw away | 49.7% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.60 |
| Reference draw odds | 4.15 |
| Reference away odds | 5.55 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -5.4% |
| Draw probability edge | +1.6% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.1074 |
| Raw ev home | -0.1701 |
| Raw edge prob draw | 0.0316 |
| Raw ev draw | 0.0955 |
| Raw edge prob away | 0.0758 |
| Raw ev away | 0.3765 |

</details>


---

## 2026-10-28 — Genoa vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **55.6%**. Expected goals are 0.78 for Genoa and 1.43 for Juventus (2.22 combined). The most likely exact score is 0-1 at 16.2%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.3%; Double Chance 1X: 44.4%; Double Chance X2: 81.5%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 92.3%; BTTS Yes (both teams score): 41.2%; BTTS No (at least one team does not score): 58.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 18.5% | 5.41 |
| Draw | 25.9% | 3.86 |
| Juventus win | 55.6% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 0.78 |
| Juventus expected goals | 1.43 |
| Expected total goals | 2.22 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 65.8% |
| Under 1.5 | 34.2% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.7% |
| Under 3.5 | 81.3% |
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.23% |
| 2 | 0-2 | 11.96% |
| 3 | 1-1 | 11.77% |
| 4 | 0-0 | 10.52% |
| 5 | 1-2 | 9.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 18.5% | 16.9% | 5.61 | +3.6% |
| Draw | 25.9% | 24.0% | 4.01 | +3.9% |
| Juventus win | 55.6% | 59.1% | 1.70 | -5.5% |
| Over 2.5 | 39.0% | 46.5% | 2.11 | -17.7% |
| Under 2.5 | 61.0% | 53.5% | 1.85 | +12.9% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Genoa |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7833 |
| Dc lambda away | 1.4344 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.51 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.92 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.35 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.06 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 20.1% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 41.8% |
| P home draw | 44.4% |
| P draw away | 81.5% |
| P home away | 74.1% |
| Raw p home draw | 47.9% |
| Raw p draw away | 79.9% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 5.45 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +1.6% |
| Draw probability edge | +1.9% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | 0.0318 |
| Raw ev home | 0.1256 |
| Raw edge prob draw | 0.0386 |
| Raw ev draw | 0.1164 |
| Raw edge prob away | -0.0704 |
| Raw ev away | -0.1144 |

</details>


---

## 2026-10-28 — Monza vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **58.2%**. Expected goals are 0.78 for Monza and 1.91 for Napoli (2.68 combined). The most likely exact score is 0-1 at 11.6%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.6%; Double Chance 1X: 41.8%; Double Chance X2: 81.5%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 46.9%; BTTS No (at least one team does not score): 53.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 18.5% | 5.39 |
| Draw | 23.3% | 4.29 |
| Napoli win | 58.2% | 1.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 0.78 |
| Napoli expected goals | 1.91 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 74.3% |
| Under 1.5 | 25.7% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 27.4% |
| Under 3.5 | 72.6% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 11.59% |
| 2 | 0-2 | 11.35% |
| 3 | 1-1 | 11.04% |
| 4 | 1-2 | 8.80% |
| 5 | 0-0 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 18.5% | 22.9% | 4.22 | -21.8% |
| Draw | 23.3% | 24.5% | 3.95 | -8.0% |
| Napoli win | 58.2% | 52.6% | 1.90 | +10.5% |
| Over 2.5 | 49.3% | 55.4% | 1.79 | -11.8% |
| Under 2.5 | 50.7% | 44.6% | 2.19 | +11.1% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7755 |
| Dc lambda away | 1.9065 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 46.9% |
| P btts no | 53.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.18 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.90 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.65 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.70 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 14.2% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 63.8% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 46.3% |
| P home draw | 41.8% |
| P draw away | 81.5% |
| P home away | 76.7% |
| Raw p home draw | 36.2% |
| Raw p draw away | 85.8% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.10 |
| Reference draw odds | 3.84 |
| Reference away odds | 1.85 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -4.4% |
| Draw probability edge | -1.2% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | -0.0871 |
| Raw ev home | -0.4015 |
| Raw edge prob draw | -0.0246 |
| Raw ev draw | -0.1287 |
| Raw edge prob away | 0.1118 |
| Raw ev away | 0.2114 |

</details>


---

## 2026-10-28 — Parma vs Udinese

The model's most likely 1X2 outcome is **Udinese win** at **38.3%**. Expected goals are 1.07 for Parma and 1.14 for Udinese (2.21 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 38.2%; Under 3.5 goals: 81.7%; Double Chance 1X: 61.7%; Double Chance X2: 67.7%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 92.6%; BTTS Yes (both teams score): 45.0%; BTTS No (at least one team does not score): 55.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 32.3% | 3.10 |
| Draw | 29.4% | 3.41 |
| Udinese win | 38.3% | 2.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.07 |
| Udinese expected goals | 1.14 |
| Expected total goals | 2.21 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 65.3% |
| Under 1.5 | 34.7% |
| Over 2.5 | 38.2% |
| Under 2.5 | 61.8% |
| Over 3.5 | 18.3% |
| Under 3.5 | 81.7% |
| Over 4.5 | 7.4% |
| Under 4.5 | 92.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.57% |
| 2 | 0-1 | 12.54% |
| 3 | 0-0 | 11.20% |
| 4 | 1-0 | 10.95% |
| 5 | 1-2 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 32.3% | 31.4% | 3.13 | +1.1% |
| Draw | 29.4% | 28.8% | 3.40 | -0.1% |
| Udinese win | 38.3% | 39.8% | 2.49 | -4.5% |
| Over 2.5 | 38.2% | 43.9% | 2.22 | -15.2% |
| Under 2.5 | 61.8% | 56.1% | 1.77 | +9.4% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0690 |
| Dc lambda away | 1.1419 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.0% |
| P btts no | 55.0% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.93 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.88 |
| Fair Over 2.5 odds | 2.62 |
| Fair Under 2.5 odds | 1.62 |
| Fair Over 3.5 odds | 5.46 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.49 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 29.9% |
| Unadjusted away-win probability | 36.9% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.7% |
| Raw p btts yes | 45.2% |
| P home draw | 61.7% |
| P draw away | 67.7% |
| P home away | 70.6% |
| Raw p home draw | 63.1% |
| Raw p draw away | 66.8% |
| Raw p home away | 70.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.04 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.42 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.71 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:33Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +0.9% |
| Draw probability edge | +0.6% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | 0.0182 |
| Raw ev home | 0.0393 |
| Raw edge prob draw | 0.0112 |
| Raw ev draw | 0.0175 |
| Raw edge prob away | -0.0294 |
| Raw ev away | -0.0820 |

</details>


---

## 2026-10-28 — Venezia vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **76.8%**. Expected goals are 0.69 for Venezia and 2.68 for Inter Milan (3.37 combined). The most likely exact score is 0-2 at 12.0%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 64.9%; Under 3.5 goals: 57.1%; Double Chance 1X: 23.2%; Double Chance X2: 91.2%; Double Chance 12 (either team wins): 85.6%; Under 4.5 goals: 75.4%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 8.8% | 11.36 |
| Draw | 14.4% | 6.96 |
| Inter Milan win | 76.8% | 1.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.69 |
| Inter Milan expected goals | 2.68 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 64.9% |
| Under 2.5 | 35.1% |
| Over 3.5 | 42.9% |
| Under 3.5 | 57.1% |
| Over 4.5 | 24.6% |
| Under 4.5 | 75.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 11.99% |
| 2 | 0-3 | 10.71% |
| 3 | 0-1 | 8.74% |
| 4 | 1-2 | 8.26% |
| 5 | 1-3 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 8.8% | 10.7% | 8.55 | -24.7% |
| Draw | 14.4% | 14.9% | 6.28 | -9.8% |
| Inter Milan win | 76.8% | 74.4% | 1.35 | +3.7% |

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
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6893 |
| Dc lambda away | 2.6798 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:34.363041+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.35 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.55 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.85 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.06 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 6.9% |
| Unadjusted draw probability | 13.8% |
| Unadjusted away-win probability | 79.2% |
| Raw p over 1 5 | 85.2% |
| Raw p under 3 5 | 56.5% |
| Raw p btts yes | 46.6% |
| P home draw | 23.2% |
| P draw away | 91.2% |
| P home away | 85.6% |
| Raw p home draw | 20.8% |
| Raw p draw away | 93.1% |
| Raw p home away | 86.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 8.20 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.32 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:33Z |
| Market reference home last update utc | 2026-10-19T16:27:33Z |
| Market reference draw last update utc | 2026-10-19T16:27:33Z |
| Market reference away last update utc | 2026-10-19T16:27:33Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:27Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:27Z |
| Home probability edge | -1.9% |
| Draw probability edge | -0.5% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.0374 |
| Raw ev home | -0.4070 |
| Raw edge prob draw | -0.0104 |
| Raw ev draw | -0.1306 |
| Raw edge prob away | 0.0478 |
| Raw ev away | 0.0695 |

</details>


---
