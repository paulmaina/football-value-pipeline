# Serie A — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,975 |
| Training data through | 2026-10-24 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 9f2383a86dfa8e31dcf32702b53c26bc68bdd7f9561fcd17a1453b763773d916 |
| Training as of utc | 2026-10-25T10:21:23.834393+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 75, 'bbs_added_results': 5, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 75, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 83, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-25T10:21:23.834393+00:00', 'observations': 296, 'observations_sha256': '1b31c5bb2d8dcb229ab80f7795fa4afeaa9e416c94e1dcf49f07ff9b6b1cba3c', 'eligible_training_matches': 118, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 122, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 11, 'retrospective_eligible_training_matches': 118, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '3d5eac9e93b164df671bda037305874aac7c79664cd3e7b4b6fcf63627843d09', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5489.761 |
| Base scoring parameter | 0.135 |
| Home-advantage parameter | 0.138 |
| Dixon-Coles low-score adjustment | -0.043 |
| Xi per day | 0 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1975, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-24'} |
| Training data health | {'training_end': '2026-10-24', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Additional event odds calls used before this league | 12.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261025T102123834393Z_76a3723c9bd68b3a0488b2323553797c7ca5c069011a81abebe99cb33a3d7bce.json |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **59.9%**. Expected goals are 1.73 for Lazio and 0.77 for Parma (2.50 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 45.6%; Under 3.5 goals: 75.8%; Double Chance 1X: 84.2%; Double Chance X2: 40.1%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 89.1%; BTTS Yes (both teams score): 44.6%; BTTS No (at least one team does not score): 55.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 59.9% | 1.67 |
| Draw | 24.3% | 4.12 |
| Parma win | 15.8% | 6.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.73 |
| Parma expected goals | 0.77 |
| Expected total goals | 2.50 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 71.7% |
| Under 1.5 | 28.3% |
| Over 2.5 | 45.6% |
| Under 2.5 | 54.4% |
| Over 3.5 | 24.2% |
| Under 3.5 | 75.8% |
| Over 4.5 | 10.9% |
| Under 4.5 | 89.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.77% |
| 2 | 2-0 | 12.32% |
| 3 | 1-1 | 11.39% |
| 4 | 2-1 | 9.45% |
| 5 | 0-0 | 8.70% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | b27cb3ea731fa3f18d05e6a627bdf984 |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7302 |
| Dc lambda away | 0.7674 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:21:23.834393+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 44.6% |
| P btts no | 55.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.50 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.53 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.13 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.22 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.11076165894808303, "-10": 1.8114836819509246e-09, "-11": 1.251311141730552e-10, "-12": 7.935305797965066e-12, "-13": 4.650677770441556e-13, "-14": 2.5331569609292976e-14, "-15": 1.285076541841469e-15, "-16": 5.69140790147245e-17, "-2": 0.03689891564209638, "-3": 0.0085496128734609, "-4": 0.0015421229437483637, "-5": 0.00022694805759546232, "-6": 2.8157557477441944e-05, "-7": 3.0167089861674966e-06, "-8": 2.8421984780095654e-07, "-9": 2.3886916840353057e-08, "0": 0.24297050465904288, "1": 0.25558814968772514, "10": 6.1471511003774525e-06, "11": 9.573455436324455e-07, "12": 1.3687717152909926e-07, "13": 1.8086209230799257e-08, "14": 2.2210449488458816e-09, "15": 2.540318606924706e-10, "16": 2.536546639224677e-11, "2": 0.1875605493446559, "3": 0.09798019263866059, "4": 0.03984508737871463, "5": 0.01322044887907401, "6": 0.0036981000506074897, "7": 0.0008932664866377574, "8": 0.00018974309151685483, "9": 3.595303964345771e-05} |
| Raw goal margin distribution | {"-1": 0.11076165894808303, "-10": 1.8114836819509246e-09, "-11": 1.251311141730552e-10, "-12": 7.935305797965066e-12, "-13": 4.650677770441556e-13, "-14": 2.5331569609292976e-14, "-15": 1.285076541841469e-15, "-16": 5.69140790147245e-17, "-2": 0.03689891564209638, "-3": 0.0085496128734609, "-4": 0.0015421229437483637, "-5": 0.00022694805759546232, "-6": 2.8157557477441944e-05, "-7": 3.0167089861674966e-06, "-8": 2.8421984780095654e-07, "-9": 2.3886916840353057e-08, "0": 0.24297050465904288, "1": 0.25558814968772514, "10": 6.1471511003774525e-06, "11": 9.573455436324455e-07, "12": 1.3687717152909926e-07, "13": 1.8086209230799257e-08, "14": 2.2210449488458816e-09, "15": 2.540318606924706e-10, "16": 2.536546639224677e-11, "2": 0.1875605493446559, "3": 0.09798019263866059, "4": 0.03984508737871463, "5": 0.01322044887907401, "6": 0.0036981000506074897, "7": 0.0008932664866377574, "8": 0.00018974309151685483, "9": 3.595303964345771e-05} |
| Unadjusted home-win probability | 59.9% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 15.8% |
| Raw p over 1 5 | 71.7% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 44.6% |
| P home draw | 84.2% |
| P draw away | 40.1% |
| P home away | 75.7% |
| Raw p home draw | 84.2% |
| Raw p draw away | 40.1% |
| Raw p home away | 75.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.984675821011816, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,530.9463 |
| Elo away rating | 1,398.0944 |
| Elo rating diff | 192.8519 |
| Elo home expectancy | 0.7522 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **44.7%**. Expected goals are 1.38 for Napoli and 1.01 for AS Roma (2.39 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 42.7%; Under 3.5 goals: 78.1%; Double Chance 1X: 73.0%; Double Chance X2: 55.3%; Double Chance 12 (either team wins): 71.7%; Under 4.5 goals: 90.6%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 44.7% | 2.24 |
| Draw | 28.3% | 3.54 |
| AS Roma win | 27.0% | 3.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.38 |
| AS Roma expected goals | 1.01 |
| Expected total goals | 2.39 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 69.4% |
| Under 1.5 | 30.6% |
| Over 2.5 | 42.7% |
| Under 2.5 | 57.3% |
| Over 3.5 | 21.9% |
| Under 3.5 | 78.1% |
| Over 4.5 | 9.4% |
| Under 4.5 | 90.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.33% |
| 2 | 1-0 | 12.11% |
| 3 | 0-0 | 9.73% |
| 4 | 2-1 | 8.80% |
| 5 | 0-1 | 8.73% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:00:00+00:00 |
| Fixture id | 0b4894e9fb123ef3045269f97e339eba |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3773 |
| Dc lambda away | 1.0102 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:21:23.834393+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.27 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.27 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.75 |
| Fair Over 3.5 odds | 4.57 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.60 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.1687103972084944, "-10": 3.176145090091187e-08, "-11": 2.8865467998605236e-09, "-12": 2.408202678265582e-10, "-13": 1.84946325128998e-11, "-14": 1.2138310592599589e-12, "-2": 0.07275845236312756, "-3": 0.022097043296085778, "-4": 0.0052320328871572844, "-5": 0.0010115861687574495, "-6": 0.00016497446868128364, "-7": 2.3240430325068183e-05, "-8": 2.879735899217021e-06, "-9": 3.1835834035285726e-07, "0": 0.28257668337809366, "1": 0.2320133011337972, "10": 7.050593341355592e-07, "11": 8.736479650637665e-08, "12": 9.93764400244488e-09, "13": 1.0405636233517443e-09, "14": 9.311372747402123e-11, "2": 0.13525350217802556, "3": 0.05600564027341495, "4": 0.018080090435725223, "5": 0.004766126327743035, "6": 0.0010597707733819468, "7": 0.0002035503711165006, "8": 3.438847579605174e-05, "9": 5.183332059097986e-06} |
| Raw goal margin distribution | {"-1": 0.1687103972084944, "-10": 3.176145090091187e-08, "-11": 2.8865467998605236e-09, "-12": 2.408202678265582e-10, "-13": 1.84946325128998e-11, "-14": 1.2138310592599589e-12, "-2": 0.07275845236312756, "-3": 0.022097043296085778, "-4": 0.0052320328871572844, "-5": 0.0010115861687574495, "-6": 0.00016497446868128364, "-7": 2.3240430325068183e-05, "-8": 2.879735899217021e-06, "-9": 3.1835834035285726e-07, "0": 0.28257668337809366, "1": 0.2320133011337972, "10": 7.050593341355592e-07, "11": 8.736479650637665e-08, "12": 9.93764400244488e-09, "13": 1.0405636233517443e-09, "14": 9.311372747402123e-11, "2": 0.13525350217802556, "3": 0.05600564027341495, "4": 0.018080090435725223, "5": 0.004766126327743035, "6": 0.0010597707733819468, "7": 0.0002035503711165006, "8": 3.438847579605174e-05, "9": 5.183332059097986e-06} |
| Unadjusted home-win probability | 44.7% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 27.0% |
| Raw p over 1 5 | 69.4% |
| Raw p under 3 5 | 78.1% |
| Raw p btts yes | 48.1% |
| P home draw | 73.0% |
| P draw away | 55.3% |
| P home away | 71.7% |
| Raw p home draw | 73.0% |
| Raw p draw away | 55.3% |
| Raw p home away | 71.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.268180376022777, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,561.4974 |
| Elo away rating | 1,592.1486 |
| Elo rating diff | 29.3488 |
| Elo home expectancy | 0.5421 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **59.9%**. Expected goals are 2.42 for Atalanta BC and 1.05 for Frosinone (3.47 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 66.1%; Under 3.5 goals: 55.4%; Double Chance 1X: 80.6%; Double Chance X2: 40.1%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 74.1%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 59.9% | 1.67 |
| Draw | 20.7% | 4.83 |
| Frosinone win | 19.4% | 5.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.42 |
| Frosinone expected goals | 1.05 |
| Expected total goals | 3.47 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 85.8% |
| Under 1.5 | 14.2% |
| Over 2.5 | 66.1% |
| Under 2.5 | 33.9% |
| Over 3.5 | 44.6% |
| Under 3.5 | 55.4% |
| Over 4.5 | 25.9% |
| Under 4.5 | 74.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.28% |
| 2 | 2-1 | 8.51% |
| 3 | 2-0 | 8.10% |
| 4 | 3-1 | 6.87% |
| 5 | 3-0 | 6.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 59.9% | 52.4% | 1.90 | +13.7% |
| Draw | 20.7% | 23.0% | 4.15 | -14.1% |
| Frosinone win | 19.4% | 24.5% | 3.82 | -25.7% |

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
| Market best home last update utc | 2026-10-25T10:20:39Z |
| Market best draw last update utc | 2026-10-25T10:20:39Z |
| Market best away last update utc | 2026-10-25T10:20:39Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4233 |
| Dc lambda away | 1.0498 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:21:23.834393+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.78 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.03 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.95 |
| Fair Over 3.5 odds | 2.24 |
| Fair Under 3.5 odds | 1.81 |
| Fair Over 4.5 odds | 3.85 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.1251764560594176, "-10": 2.3666169904266324e-08, "-11": 2.216505490296757e-09, "-12": 1.9083199186910887e-10, "-13": 1.5200016789316975e-11, "-14": 1.1262482155403887e-12, "-15": 7.799959755046239e-14, "-16": 5.0685161883443155e-15, "-17": 3.078911670058799e-16, "-18": 1.5732840678670064e-17, "-2": 0.05021053804307218, "-3": 0.01476876313485106, "-4": 0.0034676053703049515, "-5": 0.0006740160032607553, "-6": 0.00011145974021715307, "-7": 1.6012070856122248e-05, "-8": 2.031281797731945e-06, "-9": 2.3055838699179706e-07, "0": 0.2069830106070916, "1": 0.1936947822315561, "10": 6.678751168962795e-05, "11": 1.4439631231133636e-05, "12": 2.8698452543164812e-06, "13": 5.276808936549929e-07, "14": 9.02571099594363e-08, "15": 1.442977883896514e-08, "16": 2.164552662432168e-09, "17": 3.0353204912968126e-10, "18": 3.580424121767541e-11, "2": 0.17571228069393183, "3": 0.11930849610070403, "4": 0.06466613709011858, "5": 0.029015994849341045, "6": 0.011076569819805347, "7": 0.0036732862377456313, "8": 0.0010757155604447523, "9": 0.00028185659733300465} |
| Raw goal margin distribution | {"-1": 0.09240830619916139, "-10": 1.7470942571155226e-08, "-11": 1.6362782945559775e-09, "-12": 1.4087682054895315e-10, "-13": 1.1221022306565948e-11, "-14": 8.314238414651567e-13, "-15": 5.758120113604393e-14, "-16": 3.741701999340873e-15, "-17": 2.2729275242615354e-16, "-18": 1.161436586866677e-17, "-2": 0.03706664112384237, "-3": 0.010902660363706042, "-4": 0.002559870673163131, "-5": 0.0004975750166859664, "-6": 8.22822927498175e-05, "-7": 1.1820500381100958e-05, "-8": 1.4995416570389042e-06, "-9": 1.7020381222335956e-07, "0": 0.1835692331056611, "1": 0.2177404170390738, "10": 7.507863908753456e-05, "11": 1.6232194228127467e-05, "12": 3.2261132453503633e-06, "13": 5.931881929097756e-07, "14": 1.0146179745727533e-07, "15": 1.6221118741452585e-08, "16": 2.4332643037207916e-09, "17": 3.412130889680418e-10, "18": 4.024904710744519e-11, "2": 0.19752553391678493, "3": 0.13411967734998548, "4": 0.07269391305273064, "5": 0.032618095059195856, "6": 0.0124516360437814, "7": 0.004129294904570328, "8": 0.0012092569146578789, "9": 0.0003168468057912624} |
| Unadjusted home-win probability | 67.3% |
| Unadjusted draw probability | 18.4% |
| Unadjusted away-win probability | 14.4% |
| Raw p over 1 5 | 86.5% |
| Raw p under 3 5 | 54.2% |
| Raw p btts yes | 59.6% |
| P home draw | 80.6% |
| P draw away | 40.1% |
| P home away | 79.3% |
| Raw p home draw | 85.6% |
| Raw p draw away | 32.7% |
| Raw p home away | 81.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:21Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.0, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:21Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.47, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:21:30Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.92, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:21:30Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.45, "price": 2.92, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.88 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.95 |
| Market reference 1x2 last update utc | 2026-10-25T10:21:27Z |
| Market reference home last update utc | 2026-10-25T10:21:27Z |
| Market reference draw last update utc | 2026-10-25T10:21:27Z |
| Market reference away last update utc | 2026-10-25T10:21:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.31 |
| Market reference over 2 5 last update utc | 2026-10-25T10:21:23Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:21:23Z |
| Home probability edge | +7.4% |
| Draw probability edge | -2.3% |
| Away probability edge | -5.1% |
| Over 2.5 probability edge | -6.7% |
| Under 2.5 probability edge | +6.7% |
| Raw edge prob home | 0.1486 |
| Raw ev home | 0.2785 |
| Raw edge prob draw | -0.0468 |
| Raw ev draw | -0.2382 |
| Raw edge prob away | -0.1018 |
| Raw ev away | -0.4517 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 10.22359017061284, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,513.0173 |
| Elo away rating | 1,441.1854 |
| Elo rating diff | 131.8319 |
| Elo home expectancy | 0.6811 |
| Market p home draw | 74.0% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:21:30Z |
| Market reference home draw last update utc | 2026-10-25T10:21:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.5% |
| Market draw away odds | 2.00 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:21:30Z |
| Market reference draw away last update utc | 2026-10-25T10:21:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.5% |
| Market home away odds | 1.25 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:21:30Z |
| Market reference home away last update utc | 2026-10-25T10:21:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.00 |
| Market reference dc home draw odds | 1.31 |
| Market reference dc home away odds | 1.25 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.28, "price": 1.62, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.62, "price": 2.28, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.82, "price": 2.02, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.02, "price": 1.82, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.49, "price": 2.57, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.57, "price": 1.49, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 90.4% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-25T10:21:26Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 47.8% |
| Market under 3 5 odds | 2.03 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:20:39Z |
| Market reference under 3 5 odds | 1.91 |
| Market reference under 3 5 opposite odds | 1.77 |
| Market reference under 3 5 last update utc | 2026-10-25T10:21:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 71.7% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:21:30Z |
| Market reference btts yes odds | 1.37 |
| Market reference btts yes opposite odds | 3.31 |
| Market reference btts yes last update utc | 2026-10-25T10:21:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **46.2%**. Expected goals are 1.34 for Genoa and 0.85 for Venezia (2.20 combined). The most likely exact score is 1-0 at 13.9%. Goal-market probabilities: at least one goal: 88.6%; Over 2.5 goals: 37.8%; Under 3.5 goals: 82.1%; Double Chance 1X: 74.5%; Double Chance X2: 53.8%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 92.8%; BTTS Yes (both teams score): 42.9%; BTTS No (at least one team does not score): 57.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 46.2% | 2.17 |
| Draw | 28.4% | 3.52 |
| Venezia win | 25.5% | 3.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.34 |
| Venezia expected goals | 0.85 |
| Expected total goals | 2.20 |
| Over 0.5 | 88.6% |
| Under 0.5 | 11.4% |
| Over 1.5 | 64.9% |
| Under 1.5 | 35.1% |
| Over 2.5 | 37.8% |
| Under 2.5 | 62.2% |
| Over 3.5 | 17.9% |
| Under 3.5 | 82.1% |
| Over 4.5 | 7.2% |
| Under 4.5 | 92.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.94% |
| 2 | 1-1 | 12.96% |
| 3 | 0-0 | 11.37% |
| 4 | 0-1 | 9.79% |
| 5 | 2-0 | 9.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 46.2% | 44.7% | 2.22 | +2.5% |
| Draw | 28.4% | 27.6% | 3.26 | -7.5% |
| Venezia win | 25.5% | 27.6% | 3.69 | -6.0% |
| Over 2.5 | 37.8% | 49.7% | 2.05 | -22.5% |
| Under 2.5 | 62.2% | 50.3% | 1.87 | +16.3% |

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
| Market best home last update utc | 2026-10-25T10:20:39Z |
| Market best draw last update utc | 2026-10-25T10:20:39Z |
| Market best away last update utc | 2026-10-25T10:20:39Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3417 |
| Dc lambda away | 0.8547 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:21:23.834393+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 42.9% |
| P btts no | 57.1% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.80 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.85 |
| Fair Over 2.5 odds | 2.65 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.58 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.83 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.16999016949574194, "-10": 7.72888753935381e-09, "-11": 5.95398897655639e-10, "-12": 4.2096251346147437e-11, "-13": 2.74253889005356e-12, "-14": 1.5475559705202043e-13, "-2": 0.0639816975673934, "-3": 0.016714726742193046, "-4": 0.0033844274448464845, "-5": 0.0005577690231575632, "-6": 7.738313789475959e-05, "-7": 9.261763402699574e-06, "-8": 9.74181664553953e-07, "-9": 9.136265280744815e-08, "0": 0.2837812810498396, "1": 0.23990577077965988, "10": 6.236507649478618e-07, "11": 7.542037743076675e-08, "12": 8.37105707274575e-09, "13": 8.561421474901544e-10, "14": 7.583953333545639e-11, "2": 0.13996859359712877, "3": 0.05740243627076346, "4": 0.01824620105859632, "5": 0.0047206069672457406, "6": 0.0010281251717692704, "7": 0.00019317438671462436, "8": 3.1897159849385305e-05, "9": 4.69609602473999e-06} |
| Raw goal margin distribution | {"-1": 0.15554761371201195, "-10": 7.0722325706316986e-09, "-11": 5.448131383821987e-10, "-12": 3.851970653678491e-11, "-13": 2.5095297047215836e-12, "-14": 1.4160738765909888e-13, "-2": 0.05854574065885015, "-3": 0.015294624779238224, "-4": 0.003096882686739714, "-5": 0.0005103803402985145, "-6": 7.080857955953108e-05, "-7": 8.474873578446838e-06, "-8": 8.914140958436942e-07, "-9": 8.360037917930064e-08, "0": 0.2912050522261927, "1": 0.24729640803943892, "10": 6.428632105907249e-07, "11": 7.774380904216543e-08, "12": 8.628939349210011e-09, "13": 8.82516819655583e-10, "14": 7.817587763852057e-11, "2": 0.14428052448430984, "3": 0.05917079966996838, "4": 0.01880830114045277, "5": 0.004866031954846149, "6": 0.0010597980247294167, "7": 0.00019912539746125334, "8": 3.287979706272898e-05, "9": 4.840765918019964e-06} |
| Unadjusted home-win probability | 47.6% |
| Unadjusted draw probability | 29.1% |
| Unadjusted away-win probability | 23.3% |
| Raw p over 1 5 | 65.0% |
| Raw p under 3 5 | 82.0% |
| Raw p btts yes | 43.0% |
| P home draw | 74.5% |
| P draw away | 53.8% |
| P home away | 71.6% |
| Raw p home draw | 76.7% |
| Raw p draw away | 52.4% |
| Raw p home away | 70.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.8, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.91, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:21:15Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:21:15Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:21Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.69, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:21Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.69, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.17 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-10-25T10:21:27Z |
| Market reference home last update utc | 2026-10-25T10:21:27Z |
| Market reference draw last update utc | 2026-10-25T10:21:27Z |
| Market reference away last update utc | 2026-10-25T10:21:27Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-25T10:21:27Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:21:27Z |
| Market best over 2 5 last update utc | 2026-10-25T10:20:39Z |
| Market best under 2 5 last update utc | 2026-10-25T10:20:39Z |
| Home probability edge | +1.4% |
| Draw probability edge | +0.7% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -11.9% |
| Under 2.5 probability edge | +11.9% |
| Raw edge prob home | 0.0284 |
| Raw ev home | 0.0561 |
| Raw edge prob draw | 0.0148 |
| Raw ev draw | -0.0507 |
| Raw edge prob away | -0.0433 |
| Raw ev away | -0.1400 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 9.218525691843759, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,396.1582 |
| Elo away rating | 1,364.9563 |
| Elo rating diff | 91.2019 |
| Elo home expectancy | 0.6283 |
| Market p home draw | 73.9% |
| Market home draw odds | 1.32 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:21:15Z |
| Market reference home draw last update utc | 2026-10-25T10:21:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.5% |
| Market draw away odds | 1.72 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:21:15Z |
| Market reference draw away last update utc | 2026-10-25T10:21:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.6% |
| Market home away odds | 1.38 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:21:15Z |
| Market reference home away last update utc | 2026-10-25T10:21:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home draw odds | 1.30 |
| Market reference dc home away odds | 1.36 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:15Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.11, "price": 1.74, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:15Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.74, "price": 2.11, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:15Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.69, "price": 2.18, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:15Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.18, "price": 1.69, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 74.3% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:20:39Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.20 |
| Market reference over 1 5 last update utc | 2026-10-25T10:21:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 74.1% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:20:39Z |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.15 |
| Market reference under 3 5 last update utc | 2026-10-25T10:21:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.9% |
| Market btts yes odds | 1.79 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:21:15Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-25T10:21:21Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **69.9%**. Expected goals are 2.24 for Inter Milan and 0.93 for Fiorentina (3.17 combined). The most likely exact score is 2-0 at 11.1%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 62.2%; Under 3.5 goals: 60.4%; Double Chance 1X: 87.8%; Double Chance X2: 30.1%; Double Chance 12 (either team wins): 82.1%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 69.9% | 1.43 |
| Draw | 17.9% | 5.59 |
| Fiorentina win | 12.2% | 8.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.24 |
| Fiorentina expected goals | 0.93 |
| Expected total goals | 3.17 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 62.2% |
| Under 2.5 | 37.8% |
| Over 3.5 | 39.6% |
| Under 3.5 | 60.4% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.05% |
| 2 | 2-1 | 10.32% |
| 3 | 1-0 | 9.49% |
| 4 | 1-1 | 8.39% |
| 5 | 3-0 | 8.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 69.9% | 73.4% | 1.35 | -5.6% |
| Draw | 17.9% | 16.3% | 5.68 | +1.7% |
| Fiorentina win | 12.2% | 10.4% | 8.29 | +1.0% |

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
| Market best home last update utc | 2026-10-25T10:20:39Z |
| Market best draw last update utc | 2026-10-25T10:20:39Z |
| Market best away last update utc | 2026-10-25T10:20:39Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2354 |
| Dc lambda away | 0.9332 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:21:23.834393+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.79 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.96 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.53 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.57 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.08123147249828949, "-10": 6.093548123548954e-09, "-11": 5.09015265710596e-10, "-12": 3.9067863151761575e-11, "-13": 2.7729971329543965e-12, "-14": 1.8303569908157626e-13, "-15": 1.1286830707671566e-14, "-16": 6.492435488656213e-16, "-17": 3.174435576461286e-17, "-2": 0.030324822238271164, "-3": 0.008143526893606185, "-4": 0.0017306106127695686, "-5": 0.00030290229909126485, "-6": 4.4956573072384646e-05, "-7": 5.78383626214817e-06, "-8": 6.560983621430366e-07, "-9": 6.651662950493581e-08, "0": 0.17904911192254627, "1": 0.24089685578942358, "10": 4.5843782014365036e-05, "11": 9.173059544714047e-06, "12": 1.6864608931867665e-06, "13": 2.8673403714204246e-07, "14": 4.53355452214921e-08, "15": 6.6965060209026e-09, "16": 9.226927483485556e-10, "17": 1.0806602919414881e-10, "2": 0.21048578078786612, "3": 0.1353973753551942, "4": 0.06892397008324155, "5": 0.028896597196765537, "6": 0.010273313586223161, "7": 0.003165968196166162, "8": 0.0008602659300901385, "9": 0.00020891384223087147} |
| Raw goal margin distribution | {"-1": 0.0934265175048245, "-10": 7.0083548029149005e-09, "-11": 5.854322489738847e-10, "-12": 4.49330079631512e-11, "-13": 3.1892991375756164e-12, "-14": 2.1051431690608292e-13, "-15": 1.2981289816043563e-14, "-16": 7.467125969465296e-16, "-17": 3.651004368515455e-17, "-2": 0.034877399713937114, "-3": 0.009366090930981561, "-4": 0.0019904221570199382, "-5": 0.00034837614138901076, "-6": 5.170577279874508e-05, "-7": 6.652146799407129e-06, "-8": 7.545965034295523e-07, "-9": 7.650257787627411e-08, "0": 0.19519766084801157, "1": 0.22903343738082438, "10": 4.358611880955991e-05, "11": 8.72131498744567e-06, "12": 1.6034079569412908e-06, "13": 2.726132805906312e-07, "14": 4.310291109274004e-08, "15": 6.366723996387031e-09, "16": 8.772530098332146e-10, "17": 1.0274411448552865e-10, "2": 0.20012001292275983, "3": 0.12872947713792177, "4": 0.06552967963972481, "5": 0.027473529959102426, "6": 0.009767384950846333, "7": 0.003010054142176728, "8": 0.0008179005175658537, "9": 0.00019862548743432987} |
| Unadjusted home-win probability | 66.5% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 14.0% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 61.0% |
| Raw p btts yes | 54.6% |
| P home draw | 87.8% |
| P draw away | 30.1% |
| P home away | 82.1% |
| Raw p home draw | 86.0% |
| Raw p draw away | 33.5% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:24Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.76, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:24Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 4.87, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:24Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:24Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:24Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.98, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:24Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:24Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:24Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:24Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 4.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:24Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 5.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:21:30Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 6.85, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:21:30Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.13, "price": 6.85, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.35 |
| Reference draw odds | 5.80 |
| Reference away odds | 9.00 |
| Market reference 1x2 last update utc | 2026-10-25T10:21:27Z |
| Market reference home last update utc | 2026-10-25T10:21:27Z |
| Market reference draw last update utc | 2026-10-25T10:21:27Z |
| Market reference away last update utc | 2026-10-25T10:21:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.07 |
| Market reference over 2 5 last update utc | 2026-10-25T10:21:23Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:21:23Z |
| Home probability edge | -3.4% |
| Draw probability edge | +1.6% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | -0.0689 |
| Raw ev home | -0.1026 |
| Raw edge prob draw | 0.0323 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | 0.0366 |
| Raw ev away | 0.1612 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 9.182142600418587, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,671.4331 |
| Elo away rating | 1,448.7633 |
| Elo rating diff | 282.6699 |
| Elo home expectancy | 0.8358 |
| Market p home draw | 88.6% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:21:30Z |
| Market reference home draw last update utc | 2026-10-25T10:21:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 28.8% |
| Market draw away odds | 3.39 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:21:30Z |
| Market reference draw away last update utc | 2026-10-25T10:21:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.6% |
| Market home away odds | 1.18 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:21:30Z |
| Market reference home away last update utc | 2026-10-25T10:21:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.39 |
| Market reference dc home draw odds | 1.10 |
| Market reference dc home away odds | 1.18 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.04, "price": 1.79, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.79, "price": 2.04, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.62, "price": 2.29, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.29, "price": 1.62, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 88.5% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-25T10:21:26Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.8% |
| Market under 3 5 odds | 1.87 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:20:39Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market reference under 3 5 last update utc | 2026-10-25T10:21:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.6% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:21:30Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.43 |
| Market reference btts yes last update utc | 2026-10-25T10:21:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **60.8%**. Expected goals are 0.60 for Lecce and 1.42 for Juventus (2.03 combined). The most likely exact score is 0-1 at 19.6%. Goal-market probabilities: at least one goal: 87.9%; Over 2.5 goals: 34.2%; Under 3.5 goals: 84.8%; Double Chance 1X: 39.2%; Double Chance X2: 85.8%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 94.2%; BTTS Yes (both teams score): 34.1%; BTTS No (at least one team does not score): 65.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 14.2% | 7.03 |
| Draw | 25.0% | 4.00 |
| Juventus win | 60.8% | 1.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.60 |
| Juventus expected goals | 1.42 |
| Expected total goals | 2.03 |
| Over 0.5 | 87.9% |
| Under 0.5 | 12.1% |
| Over 1.5 | 61.3% |
| Under 1.5 | 38.7% |
| Over 2.5 | 34.2% |
| Under 2.5 | 65.8% |
| Over 3.5 | 15.2% |
| Under 3.5 | 84.8% |
| Over 4.5 | 5.8% |
| Under 4.5 | 94.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.63% |
| 2 | 0-2 | 14.32% |
| 3 | 0-0 | 12.12% |
| 4 | 1-1 | 10.49% |
| 5 | 1-2 | 8.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 14.2% | 13.1% | 6.31 | -10.2% |
| Draw | 25.0% | 21.8% | 4.30 | +7.5% |
| Juventus win | 60.8% | 65.0% | 1.56 | -5.2% |
| Over 2.5 | 34.2% | 50.0% | 1.83 | -37.3% |
| Under 2.5 | 65.8% | 50.0% | 2.10 | +38.1% |

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
| Market best home last update utc | 2026-10-25T10:20:39Z |
| Market best draw last update utc | 2026-10-25T10:20:39Z |
| Market best away last update utc | 2026-10-25T10:20:39Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6050 |
| Dc lambda away | 1.4218 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:21:23.834393+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 34.1% |
| P btts no | 65.9% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.25 |
| Fair Over 1.5 odds | 1.63 |
| Fair Under 1.5 odds | 2.58 |
| Fair Over 2.5 odds | 2.92 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.60 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 17.33 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.29626661218245787, "-10": 1.424869711030855e-06, "-11": 1.8298058964548387e-07, "-12": 2.1560532282367578e-08, "-13": 2.3430838323393913e-09, "-14": 2.2417786226453082e-10, "-2": 0.18897360313166223, "-3": 0.08379364337723626, "-4": 0.02858785861315023, "-5": 0.00790683164085192, "-6": 0.001836561326708858, "-7": 0.00036744515728447124, "-8": 6.453887914984233e-05, "-9": 1.0099687790804649e-05, "0": 0.24994530316025457, "1": 0.10622505776663697, "10": 2.3936792757772116e-10, "11": 1.3080289705694406e-11, "12": 6.55833133118471e-13, "13": 3.032796273106245e-14, "14": 1.2347233719733127e-15, "2": 0.029533823027476834, "3": 0.0055725135554027215, "4": 0.0008089901244923297, "5": 9.521066997317276e-05, "6": 9.410443676589269e-06, "7": 8.011590222360693e-07, "8": 5.987825751120884e-08, "9": 3.987284447767875e-09} |
| Raw goal margin distribution | {"-1": 0.2754659252927987, "-10": 1.3248305317950284e-06, "-11": 1.7013364099992774e-07, "-12": 2.0046781279930215e-08, "-13": 2.178577434559074e-09, "-14": 2.0843847980017848e-10, "-2": 0.17570588889212574, "-3": 0.07791054596577279, "-4": 0.02658072358204599, "-5": 0.007351698114198156, "-6": 0.0017076175458720173, "-7": 0.0003416470708599072, "-8": 6.000764625958785e-05, "-9": 9.390595254618145e-06, "0": 0.2816330668976638, "1": 0.11442915616503428, "10": 2.578550724431284e-10, "11": 1.4090522000044494e-11, "12": 7.064852077810563e-13, "13": 3.2670287561943444e-14, "14": 1.3300849773369346e-15, "2": 0.03181481392823558, "3": 0.00600289646595253, "4": 0.0008714709997604561, "5": 0.00010256409223963322, "6": 1.0137242113027135e-05, "7": 8.630350766189067e-07, "8": 6.450284540859306e-08, "9": 4.29523508238886e-09} |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 56.5% |
| Raw p over 1 5 | 60.6% |
| Raw p under 3 5 | 85.2% |
| Raw p btts yes | 34.9% |
| P home draw | 39.2% |
| P draw away | 85.8% |
| P home away | 75.0% |
| Raw p home draw | 43.5% |
| Raw p draw away | 84.7% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.15, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:21:30Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.88, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:21:30Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.21, "price": 4.88, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 7.00 |
| Reference draw odds | 4.30 |
| Reference away odds | 1.51 |
| Market reference 1x2 last update utc | 2026-10-25T10:21:27Z |
| Market reference home last update utc | 2026-10-25T10:21:27Z |
| Market reference draw last update utc | 2026-10-25T10:21:27Z |
| Market reference away last update utc | 2026-10-25T10:21:27Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.89 |
| Market reference over 2 5 last update utc | 2026-10-25T10:21:27Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:21:27Z |
| Market best over 2 5 last update utc | 2026-10-25T10:20:39Z |
| Market best under 2 5 last update utc | 2026-10-25T10:20:39Z |
| Home probability edge | +1.1% |
| Draw probability edge | +3.2% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -15.8% |
| Under 2.5 probability edge | +15.8% |
| Raw edge prob home | 0.0220 |
| Raw ev home | -0.0331 |
| Raw edge prob draw | 0.0634 |
| Raw ev draw | 0.2110 |
| Raw edge prob away | -0.0853 |
| Raw ev away | -0.1184 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.277761217417119, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,374.5856 |
| Elo away rating | 1,557.5355 |
| Elo rating diff | -122.9499 |
| Elo home expectancy | 0.3301 |
| Market p home draw | 37.6% |
| Market home draw odds | 2.59 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:21:30Z |
| Market reference home draw last update utc | 2026-10-25T10:21:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.6% |
| Market draw away odds | 1.15 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:21:30Z |
| Market reference draw away last update utc | 2026-10-25T10:21:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.8% |
| Market home away odds | 1.25 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:21:30Z |
| Market reference home away last update utc | 2026-10-25T10:21:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.15 |
| Market reference dc home draw odds | 2.59 |
| Market reference dc home away odds | 1.25 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.33, "price": 1.6, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.6, "price": 2.33, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.85, "price": 1.99, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.99, "price": 1.85, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.53, "price": 2.47, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:30Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.47, "price": 1.53, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 78.2% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:20:39Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 3.60 |
| Market reference over 1 5 last update utc | 2026-10-25T10:21:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.5% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:20:39Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 2.80 |
| Market reference under 3 5 last update utc | 2026-10-25T10:21:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 50.4% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:21:30Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-10-25T10:21:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **52.9%**. Expected goals are 1.07 for Udinese and 1.71 for AC Milan (2.78 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 52.4%; Under 3.5 goals: 69.6%; Double Chance 1X: 47.1%; Double Chance X2: 78.3%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 54.3%; BTTS No (at least one team does not score): 45.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 21.7% | 4.61 |
| Draw | 25.4% | 3.94 |
| AC Milan win | 52.9% | 1.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.07 |
| AC Milan expected goals | 1.71 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 52.4% |
| Under 2.5 | 47.6% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.06% |
| 2 | 0-1 | 10.36% |
| 3 | 1-2 | 9.92% |
| 4 | 0-2 | 9.27% |
| 5 | 0-0 | 6.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 21.7% | 20.0% | 4.59 | -0.5% |
| Draw | 25.4% | 25.8% | 3.61 | -8.4% |
| AC Milan win | 52.9% | 54.1% | 1.86 | -1.5% |
| Over 2.5 | 52.4% | 50.4% | 1.97 | +3.3% |
| Under 2.5 | 47.6% | 49.6% | 1.93 | -8.2% |

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
| Market best home last update utc | 2026-10-25T10:20:39Z |
| Market best draw last update utc | 2026-10-25T10:20:39Z |
| Market best away last update utc | 2026-10-25T10:20:39Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0709 |
| Dc lambda away | 1.7062 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:21:23.834393+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.3% |
| P btts no | 45.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.65 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.36 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.72 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.23811612077255084, "-10": 4.3250292374178585e-06, "-11": 6.617891170440945e-07, "-12": 9.301489468298994e-08, "-13": 1.2084231061462087e-08, "-14": 1.451170736379322e-09, "-15": 1.4714145564802975e-10, "-2": 0.16366976244468293, "-3": 0.08164073004266537, "-4": 0.03205667070577215, "-5": 0.010334941426245806, "-6": 0.0028199920786248843, "-7": 0.0006661396453580675, "-8": 0.00013862069616826127, "-9": 2.5764522211734527e-05, "0": 0.25377209693237224, "1": 0.1341734201259619, "10": 3.729619304187204e-08, "11": 3.5818179465872403e-09, "12": 3.15969247978866e-10, "13": 2.5764384356021916e-11, "14": 1.9419037095992757e-12, "15": 1.2358127120212703e-13, "2": 0.058610639846533884, "3": 0.018349461383234327, "4": 0.004522132550421901, "5": 0.0009150426191338243, "6": 0.00015670744211647306, "7": 2.323354316440239e-05, "8": 3.034496706790565e-06, "9": 3.53988471815926e-07} |
| Raw goal margin distribution | {"-1": 0.2327453585807281, "-10": 4.227477238706103e-06, "-11": 6.468623159638129e-07, "-12": 9.091692299581904e-08, "-13": 1.1811668535701203e-08, "-14": 1.4184392568829367e-09, "-15": 1.438226473108191e-10, "-2": 0.15997815446270103, "-3": 0.07979930517481787, "-4": 0.03133362535099448, "-5": 0.010101834518209942, "-6": 0.002756386528576532, "-7": 0.0006511147171417174, "-8": 0.0001354940754608133, "-9": 2.5183397669069328e-05, "0": 0.24940824547919996, "1": 0.14426718957838314, "10": 4.010195869697894e-08, "11": 3.851275522755865e-09, "12": 3.3973938620862447e-10, "13": 2.7702620375712765e-11, "14": 2.0879917225983858e-12, "15": 1.3287820094410089e-13, "2": 0.06301987593453406, "3": 0.019729878105149846, "4": 0.004862329314836165, "5": 0.0009838806142300621, "6": 0.00016849642976184538, "7": 2.4981385829843826e-05, "8": 3.2627797015425833e-06, "9": 3.806187687851056e-07} |
| Unadjusted home-win probability | 23.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 77.0% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 54.3% |
| P home draw | 47.1% |
| P draw away | 78.3% |
| P home away | 74.6% |
| Raw p home draw | 48.2% |
| Raw p draw away | 76.7% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.3, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:14Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.04, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:14Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.46, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:21Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.19, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:21Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.33, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:14Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:14Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:20:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.55, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:20:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:21:20Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.36, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:21:20Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.36, "price": 3.36, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 4.80 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.82 |
| Market reference 1x2 last update utc | 2026-10-25T10:21:28Z |
| Market reference home last update utc | 2026-10-25T10:21:28Z |
| Market reference draw last update utc | 2026-10-25T10:21:28Z |
| Market reference away last update utc | 2026-10-25T10:21:28Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-25T10:21:28Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:21:28Z |
| Market best over 2 5 last update utc | 2026-10-25T10:20:39Z |
| Market best under 2 5 last update utc | 2026-10-25T10:20:39Z |
| Home probability edge | +1.6% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | 0.0326 |
| Raw ev home | 0.0697 |
| Raw edge prob draw | -0.0087 |
| Raw ev draw | -0.0996 |
| Raw edge prob away | -0.0239 |
| Raw ev away | -0.0374 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.366566753941214, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,386.6713 |
| Elo away rating | 1,580.4486 |
| Elo rating diff | -133.7773 |
| Elo home expectancy | 0.3165 |
| Market p home draw | 48.2% |
| Market home draw odds | 2.03 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:21:20Z |
| Market reference home draw last update utc | 2026-10-25T10:21:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 78.3% |
| Market draw away odds | 1.23 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:21:20Z |
| Market reference draw away last update utc | 2026-10-25T10:21:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.5% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:21:20Z |
| Market reference home away last update utc | 2026-10-25T10:21:26Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.22 |
| Market reference dc home draw odds | 1.98 |
| Market reference dc home away odds | 1.30 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:20Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 2.65, "price": 1.45, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:20Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 1.45, "price": 2.65, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:20Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.02, "price": 1.81, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:20Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.81, "price": 2.02, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:20Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.62, "price": 2.26, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:21:20Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.26, "price": 1.62, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 76.1% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:20:39Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.35 |
| Market reference over 1 5 last update utc | 2026-10-25T10:21:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.3% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:20:39Z |
| Market reference under 3 5 odds | 1.32 |
| Market reference under 3 5 opposite odds | 3.00 |
| Market reference under 3 5 last update utc | 2026-10-25T10:21:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.2% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:21:20Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-10-25T10:21:22Z |
| Market btts yes bookmakers | 1 |

</details>


---
