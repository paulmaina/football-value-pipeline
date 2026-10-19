# Ligue 1 — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,741 |
| Training data through | 2026-10-18 |
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
| Training sha256 | b220396b4c5eca6ad05b84187c4e9d1ef5b15accc2804b0e7bd2dd584c68676e |
| Training as of utc | 2026-10-19T16:28:05.805695+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-19T16:28:05.805695+00:00', 'observations': 85, 'observations_sha256': '452543417f7dbd804ab8869ed03935fe5f7cffae398e23344fb26bc15376cb6b', 'eligible_training_matches': 17, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 47, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 17, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '56c1e03ad8f06b5eae0de5c2783f40728a2da70b6eb5917b267cd4c3667b1ca6', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 5075.352 |
| Base scoring parameter | 0.216 |
| Home-advantage parameter | 0.187 |
| Dixon-Coles low-score adjustment | -0.055 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Additional event odds calls used before this league | 3.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261019T162805805695Z_9a0dafe1d854a842f8bd59aaeef7d74b3003f0f47a773b5d955de448bf5e8647.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **39.8%**. Expected goals are 1.22 for Brest and 1.24 for Nice (2.46 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 44.7%; Under 3.5 goals: 76.6%; Double Chance 1X: 67.9%; Double Chance X2: 60.2%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 39.8% | 2.51 |
| Draw | 28.1% | 3.56 |
| Nice win | 32.1% | 3.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.22 |
| Nice expected goals | 1.24 |
| Expected total goals | 2.46 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 44.7% |
| Under 2.5 | 55.3% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.37% |
| 2 | 1-0 | 11.00% |
| 3 | 0-0 | 9.09% |
| 4 | 2-1 | 8.92% |
| 5 | 0-1 | 8.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 39.8% | 44.4% | 2.31 | -8.1% |
| Draw | 28.1% | 27.6% | 3.49 | -1.8% |
| Nice win | 32.1% | 28.0% | 3.37 | +8.1% |
| Over 2.5 | 44.7% | 56.6% | 1.76 | -21.3% |
| Under 2.5 | 55.3% | 43.4% | 2.23 | +23.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 8aa36b30d655d6c81ed98bf9ec1b4039 |
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
| Matched home-team name | Brest |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2185 |
| Dc lambda away | 1.2395 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:05.805695+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.00 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.46 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.63 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 36.2% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 50.8% |
| P home draw | 67.9% |
| P draw away | 60.2% |
| P home away | 71.9% |
| Raw p home draw | 63.8% |
| Raw p draw away | 64.9% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:07Z |
| Market reference home last update utc | 2026-10-19T16:28:07Z |
| Market reference draw last update utc | 2026-10-19T16:28:07Z |
| Market reference away last update utc | 2026-10-19T16:28:07Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.14 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -4.6% |
| Draw probability edge | +0.6% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -11.9% |
| Under 2.5 probability edge | +11.9% |
| Raw edge prob home | -0.0928 |
| Raw ev home | -0.1881 |
| Raw edge prob draw | 0.0114 |
| Raw ev draw | 0.0015 |
| Raw edge prob away | 0.0813 |
| Raw ev away | 0.2185 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **47.0%**. Expected goals are 1.68 for RC Lens and 1.02 for Paris FC (2.70 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 50.6%; Under 3.5 goals: 71.7%; Double Chance 1X: 72.0%; Double Chance X2: 53.0%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 47.0% | 2.13 |
| Draw | 25.0% | 4.00 |
| Paris FC win | 28.0% | 3.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.68 |
| Paris FC expected goals | 1.02 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 28.3% |
| Under 3.5 | 71.7% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.91% |
| 2 | 1-0 | 9.59% |
| 3 | 2-1 | 8.74% |
| 4 | 2-0 | 8.53% |
| 5 | 0-1 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 47.0% | 42.0% | 2.40 | +12.8% |
| Draw | 25.0% | 24.4% | 3.79 | -5.3% |
| Paris FC win | 28.0% | 33.5% | 2.98 | -16.5% |
| Over 2.5 | 50.6% | 60.5% | 1.71 | -13.4% |
| Under 2.5 | 49.4% | 39.5% | 2.32 | +14.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | fc6c50376190b578cfeb38c029db8487 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6771 |
| Dc lambda away | 1.0249 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:05.805695+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.91 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.34 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 22.5% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 52.8% |
| P home draw | 72.0% |
| P draw away | 53.0% |
| P home away | 75.0% |
| Raw p home draw | 77.5% |
| Raw p draw away | 48.0% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:07Z |
| Market reference home last update utc | 2026-10-19T16:28:07Z |
| Market reference draw last update utc | 2026-10-19T16:28:07Z |
| Market reference away last update utc | 2026-10-19T16:28:07Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +5.0% |
| Draw probability edge | +0.5% |
| Away probability edge | -5.5% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | 0.0999 |
| Raw ev home | 0.2481 |
| Raw edge prob draw | 0.0107 |
| Raw ev draw | -0.0330 |
| Raw edge prob away | -0.1106 |
| Raw ev away | -0.3300 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **60.2%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.8%; Double Chance 1X: 82.1%; Double Chance X2: 39.8%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 60.2% | 1.66 |
| Draw | 21.9% | 4.56 |
| Troyes win | 17.9% | 5.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 53.8% |
| Under 2.5 | 46.2% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.87% |
| 2 | 1-0 | 10.82% |
| 3 | 1-1 | 10.46% |
| 4 | 2-1 | 9.89% |
| 5 | 3-0 | 6.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 60.2% | 60.2% | 1.71 | +3.0% |
| Draw | 21.9% | 20.9% | 4.26 | -6.6% |
| Troyes win | 17.9% | 18.9% | 5.13 | -8.4% |
| Over 2.5 | 53.8% | 59.6% | 1.67 | -10.1% |
| Under 2.5 | 46.2% | 40.4% | 2.40 | +10.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T15:15:00+00:00 |
| Fixture id | 0bbce95e5764e706e6c428bb52dc5536 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9081 |
| Dc lambda away | 0.9102 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:05.805695+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.00 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.40 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 82.1% |
| P draw away | 39.8% |
| P home away | 78.1% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.50 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:07Z |
| Market reference home last update utc | 2026-10-19T16:28:07Z |
| Market reference draw last update utc | 2026-10-19T16:28:07Z |
| Market reference away last update utc | 2026-10-19T16:28:07Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -0.0% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0002 |
| Raw ev home | 0.0294 |
| Raw edge prob draw | 0.0204 |
| Raw ev draw | -0.0221 |
| Raw edge prob away | -0.0202 |
| Raw ev away | -0.1358 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **44.5%**. Expected goals are 1.56 for AS Monaco and 1.26 for Lille (2.82 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 53.3%; Under 3.5 goals: 68.7%; Double Chance 1X: 71.4%; Double Chance X2: 55.5%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 44.5% | 2.25 |
| Draw | 27.0% | 3.71 |
| Lille win | 28.6% | 3.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.56 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 77.9% |
| Under 1.5 | 22.1% |
| Over 2.5 | 53.3% |
| Under 2.5 | 46.7% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.75% |
| 2 | 2-1 | 9.32% |
| 3 | 1-0 | 8.81% |
| 4 | 2-0 | 7.37% |
| 5 | 1-2 | 6.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 44.5% | 45.4% | 2.18 | -3.1% |
| Draw | 27.0% | 27.8% | 3.60 | -2.9% |
| Lille win | 28.6% | 26.9% | 3.60 | +2.9% |
| Over 2.5 | 53.3% | 56.6% | 1.77 | -5.6% |
| Under 2.5 | 46.7% | 43.4% | 2.22 | +3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | c177a3c900d7febf9870ca8de90a9e35 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monaco |
| Matched away-team name | Lille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5580 |
| Dc lambda away | 1.2637 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:05.805695+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.70 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.53 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.46 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 43.6% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.3% |
| P home draw | 71.4% |
| P draw away | 55.5% |
| P home away | 73.0% |
| Raw p home draw | 69.7% |
| Raw p draw away | 56.4% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:07Z |
| Market reference home last update utc | 2026-10-19T16:28:07Z |
| Market reference draw last update utc | 2026-10-19T16:28:07Z |
| Market reference away last update utc | 2026-10-19T16:28:07Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.14 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -0.9% |
| Draw probability edge | -0.8% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | -0.0181 |
| Raw ev home | -0.0506 |
| Raw edge prob draw | -0.0163 |
| Raw ev draw | -0.0585 |
| Raw edge prob away | 0.0344 |
| Raw ev away | 0.0907 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **38.0%**. Expected goals are 1.19 for Angers and 1.30 for Lorient (2.49 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 45.4%; Under 3.5 goals: 76.0%; Double Chance 1X: 62.0%; Double Chance X2: 66.2%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 89.2%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 33.8% | 2.96 |
| Draw | 28.2% | 3.54 |
| Lorient win | 38.0% | 2.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.19 |
| Lorient expected goals | 1.30 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.4% |
| Under 2.5 | 54.6% |
| Over 3.5 | 24.0% |
| Under 3.5 | 76.0% |
| Over 4.5 | 10.8% |
| Under 4.5 | 89.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.44% |
| 2 | 0-1 | 9.96% |
| 3 | 1-0 | 9.34% |
| 4 | 0-0 | 8.94% |
| 5 | 1-2 | 8.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 33.8% | 34.4% | 2.83 | -4.3% |
| Draw | 28.2% | 28.0% | 3.43 | -3.2% |
| Lorient win | 38.0% | 37.5% | 2.70 | +2.5% |
| Over 2.5 | 45.4% | 45.2% | 2.10 | -4.6% |
| Under 2.5 | 54.6% | 54.8% | 1.86 | +1.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 1a83b5ebabe7cb572ae6e029b3149c42 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Lorient |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1904 |
| Dc lambda away | 1.2988 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:05.805695+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.19 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.16 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.30 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 28.4% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 51.3% |
| P home draw | 62.0% |
| P draw away | 66.2% |
| P home away | 71.8% |
| Raw p home draw | 61.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 71.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:07Z |
| Market reference home last update utc | 2026-10-19T16:28:07Z |
| Market reference draw last update utc | 2026-10-19T16:28:07Z |
| Market reference away last update utc | 2026-10-19T16:28:07Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -0.6% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | -0.0125 |
| Raw ev home | -0.0606 |
| Raw edge prob draw | 0.0041 |
| Raw ev draw | -0.0246 |
| Raw edge prob away | 0.0084 |
| Raw ev away | 0.0360 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **44.0%**. Expected goals are 1.73 for Auxerre and 1.52 for Le Mans FC (3.24 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 62.7%; Under 3.5 goals: 59.3%; Double Chance 1X: 68.8%; Double Chance X2: 56.0%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 77.4%; BTTS Yes (both teams score): 64.8%; BTTS No (at least one team does not score): 35.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 44.0% | 2.27 |
| Draw | 24.8% | 4.03 |
| Le Mans FC win | 31.2% | 3.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.73 |
| Le Mans FC expected goals | 1.52 |
| Expected total goals | 3.24 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 62.7% |
| Under 2.5 | 37.3% |
| Over 3.5 | 40.7% |
| Under 3.5 | 59.3% |
| Over 4.5 | 22.6% |
| Under 4.5 | 77.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.04% |
| 2 | 2-1 | 9.17% |
| 3 | 1-2 | 7.24% |
| 4 | 2-2 | 6.85% |
| 5 | 1-0 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 44.0% | 45.6% | 2.23 | -1.9% |
| Draw | 24.8% | 25.4% | 3.70 | -8.2% |
| Le Mans FC win | 31.2% | 29.0% | 3.37 | +5.1% |
| Over 2.5 | 62.7% | 54.4% | 1.78 | +11.7% |
| Under 2.5 | 37.3% | 45.6% | 2.20 | -18.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 8eab078a37a63df32ffa443302a2a7ba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7277 |
| Dc lambda away | 1.5161 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:05.805695+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 64.8% |
| P btts no | 35.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.88 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.26 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.45 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.42 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 42.4% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 84.0% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 64.7% |
| P home draw | 68.8% |
| P draw away | 56.0% |
| P home away | 75.2% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.6% |
| Raw p home away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:07Z |
| Market reference home last update utc | 2026-10-19T16:28:07Z |
| Market reference draw last update utc | 2026-10-19T16:28:07Z |
| Market reference away last update utc | 2026-10-19T16:28:07Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -1.6% |
| Draw probability edge | -0.6% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +8.4% |
| Under 2.5 probability edge | -8.4% |
| Raw edge prob home | -0.0323 |
| Raw ev home | -0.0553 |
| Raw edge prob draw | -0.0116 |
| Raw ev draw | -0.1031 |
| Raw edge prob away | 0.0439 |
| Raw ev away | 0.1254 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **64.9%**. Expected goals are 2.11 for Marseille and 0.81 for Le Havre (2.92 combined). The most likely exact score is 2-0 at 11.6%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.1%; Under 3.5 goals: 66.8%; Double Chance 1X: 84.2%; Double Chance X2: 35.1%; Double Chance 12 (either team wins): 80.8%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 64.9% | 1.54 |
| Draw | 19.2% | 5.20 |
| Le Havre win | 15.8% | 6.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.11 |
| Le Havre expected goals | 0.81 |
| Expected total goals | 2.92 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 56.1% |
| Under 2.5 | 43.9% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.65% |
| 2 | 1-0 | 10.54% |
| 3 | 2-1 | 9.43% |
| 4 | 1-1 | 9.17% |
| 5 | 3-0 | 8.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 64.9% | 63.0% | 1.61 | +4.6% |
| Draw | 19.2% | 18.1% | 4.72 | -9.3% |
| Le Havre win | 15.8% | 19.0% | 5.44 | -13.9% |
| Over 2.5 | 56.1% | 61.1% | 1.65 | -7.5% |
| Under 2.5 | 43.9% | 38.9% | 2.45 | +7.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | fcc34b753fc61a0cc0e11d7cb0a0c36b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:27:26Z |
| Market best draw last update utc | 2026-10-19T16:27:26Z |
| Market best away last update utc | 2026-10-19T16:27:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1125 |
| Dc lambda away | 0.8098 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:05.805695+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.00 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.79 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.83 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 66.5% |
| Raw p btts yes | 49.3% |
| P home draw | 84.2% |
| P draw away | 35.1% |
| P home away | 80.8% |
| Raw p home draw | 87.3% |
| Raw p draw away | 33.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.52 |
| Reference draw odds | 4.70 |
| Reference away odds | 4.50 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:07Z |
| Market reference home last update utc | 2026-10-19T16:28:07Z |
| Market reference draw last update utc | 2026-10-19T16:28:07Z |
| Market reference away last update utc | 2026-10-19T16:28:07Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:47Z |
| Market best over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market best under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +2.0% |
| Draw probability edge | +1.1% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | 0.0398 |
| Raw ev home | 0.0776 |
| Raw edge prob draw | 0.0229 |
| Raw ev draw | -0.0385 |
| Raw edge prob away | -0.0627 |
| Raw ev away | -0.3094 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **69.6%**. Expected goals are 2.42 for Paris Saint Germain and 1.10 for Lyon (3.52 combined). The most likely exact score is 2-1 at 10.0%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 69.2%; Under 3.5 goals: 52.8%; Double Chance 1X: 86.2%; Double Chance X2: 30.4%; Double Chance 12 (either team wins): 83.5%; Under 4.5 goals: 71.6%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 69.6% | 1.44 |
| Draw | 16.5% | 6.05 |
| Lyon win | 13.8% | 7.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.42 |
| Lyon expected goals | 1.10 |
| Expected total goals | 3.52 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 87.3% |
| Under 1.5 | 12.7% |
| Over 2.5 | 69.2% |
| Under 2.5 | 30.8% |
| Over 3.5 | 47.2% |
| Under 3.5 | 52.8% |
| Over 4.5 | 28.4% |
| Under 4.5 | 71.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.03% |
| 2 | 2-0 | 9.15% |
| 3 | 3-1 | 8.10% |
| 4 | 3-0 | 7.40% |
| 5 | 1-1 | 7.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 69.6% | 73.1% | 1.43 | -0.4% |
| Draw | 16.5% | 14.3% | 5.44 | -10.2% |
| Lyon win | 13.8% | 12.6% | 7.60 | +5.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 8664b2167f22c59026d86615421463b1 |
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
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4235 |
| Dc lambda away | 1.0955 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:05.805695+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.41 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.89 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.25 |
| Fair Over 3.5 odds | 2.12 |
| Fair Under 3.5 odds | 1.90 |
| Fair Over 4.5 odds | 3.51 |
| Fair Under 4.5 odds | 1.40 |
| Unadjusted home-win probability | 66.2% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 61.1% |
| P home draw | 86.2% |
| P draw away | 30.4% |
| P home away | 83.5% |
| Raw p home draw | 84.9% |
| Raw p draw away | 33.8% |
| Raw p home away | 81.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.32 |
| Reference draw odds | 5.60 |
| Reference away odds | 6.25 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:07Z |
| Market reference home last update utc | 2026-10-19T16:28:07Z |
| Market reference draw last update utc | 2026-10-19T16:28:07Z |
| Market reference away last update utc | 2026-10-19T16:28:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:25Z |
| Home probability edge | -3.4% |
| Draw probability edge | +2.2% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.0690 |
| Raw ev home | -0.0535 |
| Raw edge prob draw | 0.0445 |
| Raw ev draw | 0.0195 |
| Raw edge prob away | 0.0245 |
| Raw ev away | 0.1452 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **54.3%**. Expected goals are 1.90 for Rennes and 1.25 for Strasbourg (3.15 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.6%; Under 3.5 goals: 61.1%; Double Chance 1X: 76.3%; Double Chance X2: 45.7%; Double Chance 12 (either team wins): 78.0%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 54.3% | 1.84 |
| Draw | 22.0% | 4.54 |
| Strasbourg win | 23.7% | 4.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.90 |
| Strasbourg expected goals | 1.25 |
| Expected total goals | 3.15 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.6% |
| Under 2.5 | 38.4% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.07% |
| 2 | 1-1 | 10.06% |
| 3 | 2-0 | 8.05% |
| 4 | 1-0 | 7.88% |
| 5 | 3-1 | 6.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 54.3% | 56.5% | 1.79 | -2.9% |
| Draw | 22.0% | 20.6% | 4.42 | -2.7% |
| Strasbourg win | 23.7% | 23.0% | 4.36 | +3.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 31dcb6d13ed240fc4a5c7a696149967e |
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
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9036 |
| Dc lambda away | 1.2513 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:05.805695+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.09 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.67 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 52.1% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 61.3% |
| Raw p btts yes | 61.3% |
| P home draw | 76.3% |
| P draw away | 45.7% |
| P home away | 78.0% |
| Raw p home draw | 75.5% |
| Raw p draw away | 47.9% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.68 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.80 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:07Z |
| Market reference home last update utc | 2026-10-19T16:28:07Z |
| Market reference draw last update utc | 2026-10-19T16:28:07Z |
| Market reference away last update utc | 2026-10-19T16:28:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:25Z |
| Home probability edge | -2.2% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.0438 |
| Raw ev home | -0.0678 |
| Raw edge prob draw | 0.0288 |
| Raw ev draw | 0.0366 |
| Raw edge prob away | 0.0150 |
| Raw ev away | 0.0670 |

</details>


---
