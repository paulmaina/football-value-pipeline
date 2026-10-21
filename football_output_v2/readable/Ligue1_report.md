# Ligue 1 — football model report

Fixtures in this report: **12**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,743 |
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
| Training sha256 | 359363df003abc706b71c69ccefb7e1dd54225d4ae9b42ac96efd978dbaafcec |
| Training as of utc | 2026-10-21T10:38:28.492805+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 21, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T10:38:28.492805+00:00', 'observations': 121, 'observations_sha256': '6d3e2e4053b41331642e9563b4aa5e7f807dafe763cad056c1e2376af4123b1a', 'eligible_training_matches': 35, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 65, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 35, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '3786470daba7872b84a2a6d54208843f79e997d77dde78d621802e4101332154', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5079.453 |
| Base scoring parameter | 0.216 |
| Home-advantage parameter | 0.187 |
| Dixon-Coles low-score adjustment | -0.057 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 12.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261021T103828492805Z_2cac3ffe03cbeac557dc8f3ab5f3f8b531404ad9410fb17c76167d6b46693e1a.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **39.4%**. Expected goals are 1.22 for Brest and 1.24 for Nice (2.46 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 45.0%; Under 3.5 goals: 76.6%; Double Chance 1X: 66.9%; Double Chance X2: 60.6%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 50.5%; BTTS No (at least one team does not score): 49.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 39.4% | 2.54 |
| Draw | 27.5% | 3.63 |
| Nice win | 33.1% | 3.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.22 |
| Nice expected goals | 1.24 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 71.2% |
| Under 1.5 | 28.8% |
| Over 2.5 | 45.0% |
| Under 2.5 | 55.0% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.09% |
| 2 | 1-0 | 10.87% |
| 3 | 0-1 | 9.04% |
| 4 | 0-0 | 8.90% |
| 5 | 2-1 | 8.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 39.4% | 43.6% | 2.31 | -9.0% |
| Draw | 27.5% | 26.3% | 3.49 | -3.9% |
| Nice win | 33.1% | 30.1% | 3.37 | +11.5% |
| Over 2.5 | 45.0% | 56.2% | 1.76 | -20.9% |
| Under 2.5 | 55.0% | 43.8% | 2.23 | +22.7% |

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
| Market best home last update utc | 2026-10-21T10:37:56Z |
| Market best draw last update utc | 2026-10-21T10:37:56Z |
| Market best away last update utc | 2026-10-21T10:37:56Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Dc lambda home | 1.2187 |
| Dc lambda away | 1.2397 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.5% |
| P btts no | 49.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.24 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.47 |
| Fair Over 2.5 odds | 2.22 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.27 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.57 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 50.8% |
| P home draw | 66.9% |
| P draw away | 60.6% |
| P home away | 72.5% |
| Raw p home draw | 63.9% |
| Raw p draw away | 64.9% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.93 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:27Z |
| Market reference home last update utc | 2026-10-21T10:38:27Z |
| Market reference draw last update utc | 2026-10-21T10:38:27Z |
| Market reference away last update utc | 2026-10-21T10:38:27Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:56Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:56Z |
| Home probability edge | -4.3% |
| Draw probability edge | +1.2% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | -11.3% |
| Under 2.5 probability edge | +11.3% |
| Raw edge prob home | -0.0850 |
| Raw ev home | -0.1887 |
| Raw edge prob draw | 0.0242 |
| Raw ev draw | 0.0031 |
| Raw edge prob away | 0.0608 |
| Raw ev away | 0.2178 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **46.7%**. Expected goals are 1.68 for RC Lens and 1.03 for Paris FC (2.70 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.8%; Double Chance 1X: 72.4%; Double Chance X2: 53.3%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 53.1%; BTTS No (at least one team does not score): 46.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 46.7% | 2.14 |
| Draw | 25.7% | 3.90 |
| Paris FC win | 27.6% | 3.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.68 |
| Paris FC expected goals | 1.03 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.24% |
| 2 | 1-0 | 9.52% |
| 3 | 2-1 | 8.69% |
| 4 | 2-0 | 8.48% |
| 5 | 0-1 | 7.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 46.7% | 41.5% | 2.40 | +12.2% |
| Draw | 25.7% | 25.8% | 3.79 | -2.7% |
| Paris FC win | 27.6% | 32.7% | 2.98 | -17.7% |
| Over 2.5 | 50.4% | 58.1% | 1.71 | -13.8% |
| Under 2.5 | 49.6% | 41.9% | 2.32 | +15.1% |

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
| Market best home last update utc | 2026-10-21T10:37:56Z |
| Market best draw last update utc | 2026-10-21T10:37:56Z |
| Market best away last update utc | 2026-10-21T10:37:56Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Dc lambda home | 1.6772 |
| Dc lambda away | 1.0253 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.1% |
| P btts no | 46.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.53 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.38 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 22.5% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 52.8% |
| P home draw | 72.4% |
| P draw away | 53.3% |
| P home away | 74.3% |
| Raw p home draw | 77.5% |
| Raw p draw away | 48.0% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.37 |
| Reference away odds | 2.72 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:27Z |
| Market reference home last update utc | 2026-10-21T10:38:27Z |
| Market reference draw last update utc | 2026-10-21T10:38:27Z |
| Market reference away last update utc | 2026-10-21T10:38:27Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:56Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:56Z |
| Home probability edge | +5.2% |
| Draw probability edge | -0.1% |
| Away probability edge | -5.1% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.1049 |
| Raw ev home | 0.2474 |
| Raw edge prob draw | -0.0022 |
| Raw ev draw | -0.0314 |
| Raw edge prob away | -0.1027 |
| Raw ev away | -0.3305 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **60.9%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 11.0%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.7%; Double Chance 1X: 83.0%; Double Chance X2: 39.1%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 60.9% | 1.64 |
| Draw | 22.1% | 4.53 |
| Troyes win | 17.0% | 5.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 77.9% |
| Under 1.5 | 22.1% |
| Over 2.5 | 53.8% |
| Under 2.5 | 46.2% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.00% |
| 2 | 1-0 | 10.94% |
| 3 | 1-1 | 10.51% |
| 4 | 2-1 | 10.02% |
| 5 | 3-0 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 60.9% | 61.7% | 1.71 | +4.2% |
| Draw | 22.1% | 21.1% | 4.26 | -6.1% |
| Troyes win | 17.0% | 17.2% | 5.13 | -12.6% |
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
| Market best home last update utc | 2026-10-21T10:37:56Z |
| Market best draw last update utc | 2026-10-21T10:37:56Z |
| Market best away last update utc | 2026-10-21T10:37:56Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9076 |
| Dc lambda away | 0.9104 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.89 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.52 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.39 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 83.0% |
| P draw away | 39.1% |
| P home away | 77.9% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.53 |
| Reference draw odds | 3.93 |
| Reference away odds | 4.70 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:27Z |
| Market reference home last update utc | 2026-10-21T10:38:27Z |
| Market reference draw last update utc | 2026-10-21T10:38:27Z |
| Market reference away last update utc | 2026-10-21T10:38:27Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:56Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:56Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0151 |
| Raw ev home | 0.0288 |
| Raw edge prob draw | 0.0189 |
| Raw ev draw | -0.0203 |
| Raw edge prob away | -0.0039 |
| Raw ev away | -0.1363 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **44.7%**. Expected goals are 1.56 for AS Monaco and 1.26 for Lille (2.82 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 53.5%; Under 3.5 goals: 68.7%; Double Chance 1X: 71.2%; Double Chance X2: 55.3%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 44.7% | 2.24 |
| Draw | 26.5% | 3.77 |
| Lille win | 28.8% | 3.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.56 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.5% |
| Under 2.5 | 46.5% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.53% |
| 2 | 2-1 | 9.38% |
| 3 | 1-0 | 8.84% |
| 4 | 2-0 | 7.42% |
| 5 | 1-2 | 7.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 44.7% | 45.9% | 2.22 | -0.7% |
| Draw | 26.5% | 26.8% | 3.43 | -9.1% |
| Lille win | 28.8% | 27.3% | 3.83 | +10.2% |
| Over 2.5 | 53.5% | 53.2% | 1.86 | -0.5% |
| Under 2.5 | 46.5% | 46.8% | 2.10 | -2.3% |

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
| Market best home last update utc | 2026-10-21T10:37:56Z |
| Market best draw last update utc | 2026-10-21T10:37:56Z |
| Market best away last update utc | 2026-10-21T10:37:56Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monaco |
| Matched away-team name | Lille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5579 |
| Dc lambda away | 1.2641 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.94 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 43.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.3% |
| P home draw | 71.2% |
| P draw away | 55.3% |
| P home away | 73.5% |
| Raw p home draw | 69.7% |
| Raw p draw away | 56.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.23 |
| Reference away odds | 3.18 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:28Z |
| Market reference home last update utc | 2026-10-21T10:38:28Z |
| Market reference draw last update utc | 2026-10-21T10:38:28Z |
| Market reference away last update utc | 2026-10-21T10:38:28Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.03 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:56Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:56Z |
| Home probability edge | -1.2% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | -0.0240 |
| Raw ev home | -0.0339 |
| Raw edge prob draw | -0.0061 |
| Raw ev draw | -0.1015 |
| Raw edge prob away | 0.0301 |
| Raw ev away | 0.1599 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **39.9%**. Expected goals are 1.19 for Angers and 1.30 for Lorient (2.49 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 45.5%; Under 3.5 goals: 75.9%; Double Chance 1X: 60.1%; Double Chance X2: 67.9%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 89.2%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 32.1% | 3.12 |
| Draw | 28.1% | 3.56 |
| Lorient win | 39.9% | 2.51 |

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
| Over 2.5 | 45.5% |
| Under 2.5 | 54.5% |
| Over 3.5 | 24.1% |
| Under 3.5 | 75.9% |
| Over 4.5 | 10.8% |
| Under 4.5 | 89.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.37% |
| 2 | 0-1 | 10.44% |
| 3 | 0-0 | 8.90% |
| 4 | 1-0 | 8.84% |
| 5 | 1-2 | 8.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 32.1% | 31.0% | 3.10 | -0.6% |
| Draw | 28.1% | 27.7% | 3.38 | -5.1% |
| Lorient win | 39.9% | 41.4% | 2.52 | +0.4% |
| Over 2.5 | 45.5% | 47.1% | 2.08 | -5.4% |
| Under 2.5 | 54.5% | 52.9% | 1.87 | +1.9% |

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
| Market best home last update utc | 2026-10-21T10:37:56Z |
| Market best draw last update utc | 2026-10-21T10:37:56Z |
| Market best away last update utc | 2026-10-21T10:37:56Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Dc lambda away | 1.2991 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.24 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.55 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.16 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.27 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 51.3% |
| P home draw | 60.1% |
| P draw away | 67.9% |
| P home away | 71.9% |
| Raw p home draw | 61.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.15 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:28Z |
| Market reference home last update utc | 2026-10-21T10:38:28Z |
| Market reference draw last update utc | 2026-10-21T10:38:28Z |
| Market reference away last update utc | 2026-10-21T10:38:28Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:56Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:56Z |
| Home probability edge | +1.1% |
| Draw probability edge | +0.4% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | 0.0221 |
| Raw ev home | 0.0281 |
| Raw edge prob draw | 0.0081 |
| Raw ev draw | -0.0373 |
| Raw edge prob away | -0.0301 |
| Raw ev away | -0.0335 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **44.2%**. Expected goals are 1.73 for Auxerre and 1.52 for Le Mans FC (3.24 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 62.7%; Under 3.5 goals: 59.3%; Double Chance 1X: 69.2%; Double Chance X2: 55.8%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 77.4%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 44.2% | 2.26 |
| Draw | 25.0% | 4.00 |
| Le Mans FC win | 30.8% | 3.25 |

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
| 1 | 1-1 | 11.12% |
| 2 | 2-1 | 9.22% |
| 3 | 1-2 | 7.15% |
| 4 | 2-2 | 6.89% |
| 5 | 1-0 | 6.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 44.2% | 46.1% | 2.23 | -1.4% |
| Draw | 25.0% | 25.7% | 3.76 | -6.0% |
| Le Mans FC win | 30.8% | 28.2% | 3.37 | +3.8% |
| Over 2.5 | 62.7% | 55.6% | 1.78 | +11.6% |
| Under 2.5 | 37.3% | 44.4% | 2.20 | -17.9% |

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
| Market best home last update utc | 2026-10-21T10:37:56Z |
| Market best draw last update utc | 2026-10-21T10:37:57Z |
| Market best away last update utc | 2026-10-21T10:37:56Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7277 |
| Dc lambda away | 1.5164 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.67 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.26 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.45 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.42 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 84.0% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 64.8% |
| P home draw | 69.2% |
| P draw away | 55.8% |
| P home away | 75.0% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.7% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.37 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:28Z |
| Market reference home last update utc | 2026-10-21T10:38:28Z |
| Market reference draw last update utc | 2026-10-21T10:38:28Z |
| Market reference away last update utc | 2026-10-21T10:38:28Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:56Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:56Z |
| Home probability edge | -1.9% |
| Draw probability edge | -0.7% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | +7.1% |
| Under 2.5 probability edge | -7.1% |
| Raw edge prob home | -0.0373 |
| Raw ev home | -0.0558 |
| Raw edge prob draw | -0.0143 |
| Raw ev draw | -0.0872 |
| Raw edge prob away | 0.0516 |
| Raw ev away | 0.1250 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **65.2%**. Expected goals are 2.11 for Marseille and 0.81 for Le Havre (2.92 combined). The most likely exact score is 2-0 at 11.7%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.8%; Under 3.5 goals: 66.7%; Double Chance 1X: 85.4%; Double Chance X2: 34.8%; Double Chance 12 (either team wins): 79.8%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 65.2% | 1.53 |
| Draw | 20.2% | 4.95 |
| Le Havre win | 14.6% | 6.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.11 |
| Le Havre expected goals | 0.81 |
| Expected total goals | 2.92 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.8% |
| Under 2.5 | 44.2% |
| Over 3.5 | 33.3% |
| Under 3.5 | 66.7% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.69% |
| 2 | 1-0 | 10.56% |
| 3 | 1-1 | 9.64% |
| 4 | 2-1 | 9.47% |
| 5 | 3-0 | 8.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 65.2% | 63.5% | 1.61 | +5.0% |
| Draw | 20.2% | 20.0% | 4.89 | -1.2% |
| Le Havre win | 14.6% | 16.5% | 5.44 | -20.6% |
| Over 2.5 | 55.8% | 60.5% | 1.65 | -7.9% |
| Under 2.5 | 44.2% | 39.5% | 2.45 | +8.2% |

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
| Market best home last update utc | 2026-10-21T10:37:56Z |
| Market best draw last update utc | 2026-10-21T10:37:57Z |
| Market best away last update utc | 2026-10-21T10:37:56Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1127 |
| Dc lambda away | 0.8100 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.11 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.80 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 66.5% |
| Raw p btts yes | 49.3% |
| P home draw | 85.4% |
| P draw away | 34.8% |
| P home away | 79.8% |
| Raw p home draw | 87.3% |
| Raw p draw away | 33.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.49 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.85 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:28Z |
| Market reference home last update utc | 2026-10-21T10:38:28Z |
| Market reference draw last update utc | 2026-10-21T10:38:28Z |
| Market reference away last update utc | 2026-10-21T10:38:28Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:56Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:56Z |
| Home probability edge | +1.7% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | 0.0345 |
| Raw ev home | 0.0774 |
| Raw edge prob draw | 0.0039 |
| Raw ev draw | -0.0023 |
| Raw edge prob away | -0.0384 |
| Raw ev away | -0.3102 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **67.8%**. Expected goals are 2.42 for Paris Saint Germain and 1.10 for Lyon (3.52 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 68.8%; Under 3.5 goals: 53.0%; Double Chance 1X: 85.5%; Double Chance X2: 32.2%; Double Chance 12 (either team wins): 82.3%; Under 4.5 goals: 71.9%; BTTS Yes (both teams score): 60.8%; BTTS No (at least one team does not score): 39.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 67.8% | 1.47 |
| Draw | 17.7% | 5.67 |
| Lyon win | 14.5% | 6.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.42 |
| Lyon expected goals | 1.10 |
| Expected total goals | 3.52 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 87.2% |
| Under 1.5 | 12.8% |
| Over 2.5 | 68.8% |
| Under 2.5 | 31.2% |
| Over 3.5 | 47.0% |
| Under 3.5 | 53.0% |
| Over 4.5 | 28.1% |
| Under 4.5 | 71.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.77% |
| 2 | 2-0 | 8.92% |
| 3 | 3-1 | 7.89% |
| 4 | 1-1 | 7.82% |
| 5 | 3-0 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 67.8% | 69.5% | 1.47 | -0.3% |
| Draw | 17.7% | 16.5% | 5.41 | -4.5% |
| Lyon win | 14.5% | 14.0% | 6.88 | -0.2% |

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
| Market best home last update utc | 2026-10-21T10:37:56Z |
| Market best draw last update utc | 2026-10-21T10:37:56Z |
| Market best away last update utc | 2026-10-21T10:37:56Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4237 |
| Dc lambda away | 1.0958 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.20 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.81 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.89 |
| Fair Over 4.5 odds | 3.55 |
| Fair Under 4.5 odds | 1.39 |
| Unadjusted home-win probability | 66.2% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.2% |
| Raw p btts yes | 61.1% |
| P home draw | 85.5% |
| P draw away | 32.2% |
| P home away | 82.3% |
| Raw p home draw | 84.9% |
| Raw p draw away | 33.8% |
| Raw p home away | 81.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.37 |
| Reference draw odds | 4.75 |
| Reference away odds | 5.50 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:28Z |
| Market reference home last update utc | 2026-10-21T10:38:28Z |
| Market reference draw last update utc | 2026-10-21T10:38:28Z |
| Market reference away last update utc | 2026-10-21T10:38:28Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.90 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:17Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:17Z |
| Home probability edge | -1.7% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | -0.0334 |
| Raw ev home | -0.0273 |
| Raw edge prob draw | 0.0224 |
| Raw ev draw | 0.0154 |
| Raw edge prob away | 0.0110 |
| Raw ev away | 0.0360 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **54.6%**. Expected goals are 1.90 for Rennes and 1.25 for Strasbourg (3.16 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 61.6%; Under 3.5 goals: 61.0%; Double Chance 1X: 76.9%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 61.0%; BTTS No (at least one team does not score): 39.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 54.6% | 1.83 |
| Draw | 22.2% | 4.49 |
| Strasbourg win | 23.1% | 4.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.90 |
| Strasbourg expected goals | 1.25 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.6% |
| Under 2.5 | 38.4% |
| Over 3.5 | 39.0% |
| Under 3.5 | 61.0% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.17% |
| 2 | 2-1 | 10.14% |
| 3 | 2-0 | 8.11% |
| 4 | 1-0 | 7.91% |
| 5 | 3-1 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 54.6% | 57.2% | 1.79 | -2.2% |
| Draw | 22.2% | 21.0% | 4.45 | -1.0% |
| Strasbourg win | 23.1% | 21.8% | 4.36 | +0.9% |

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
| Market best home last update utc | 2026-10-21T10:37:56Z |
| Market best draw last update utc | 2026-10-21T10:37:57Z |
| Market best away last update utc | 2026-10-21T10:37:56Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9036 |
| Dc lambda away | 1.2515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.0% |
| P btts no | 39.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.81 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.88 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.67 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 52.1% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 61.3% |
| Raw p btts yes | 61.3% |
| P home draw | 76.9% |
| P draw away | 45.4% |
| P home away | 77.8% |
| Raw p home draw | 75.5% |
| Raw p draw away | 47.9% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.64 |
| Reference draw odds | 3.98 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:28Z |
| Market reference home last update utc | 2026-10-21T10:38:28Z |
| Market reference draw last update utc | 2026-10-21T10:38:28Z |
| Market reference away last update utc | 2026-10-21T10:38:28Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:17Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:17Z |
| Home probability edge | -2.6% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.0514 |
| Raw ev home | -0.0683 |
| Raw edge prob draw | 0.0248 |
| Raw ev draw | 0.0453 |
| Raw edge prob away | 0.0265 |
| Raw ev away | 0.0664 |

</details>


---

## 2026-10-25 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **60.3%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.8%; Double Chance 1X: 82.5%; Double Chance X2: 39.7%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 60.3% | 1.66 |
| Draw | 22.2% | 4.51 |
| Troyes win | 17.5% | 5.71 |

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
| 1 | 2-0 | 10.89% |
| 2 | 1-0 | 10.83% |
| 3 | 1-1 | 10.58% |
| 4 | 2-1 | 9.91% |
| 5 | 3-0 | 6.92% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 18e4425261f7dd6b245f82056d424411 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 5.00 |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9076 |
| Dc lambda away | 0.9104 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.79 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.41 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 82.5% |
| P draw away | 39.7% |
| P home away | 77.8% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.50 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:56Z |
| Market reference home last update utc | 2026-10-21T10:37:56Z |
| Market reference draw last update utc | 2026-10-21T10:37:56Z |
| Market reference away last update utc | 2026-10-21T10:37:56Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:56Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:56Z |
| Home probability edge | -0.1% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | -0.0025 |
| Raw edge prob draw | 0.0161 |
| Raw edge prob away | -0.0135 |

</details>


---

## 2026-10-30 — Le Havre vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **75.3%**. Expected goals are 0.82 for Le Havre and 2.31 for Paris Saint Germain (3.13 combined). The most likely exact score is 0-2 at 12.5%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 62.1%; Under 3.5 goals: 61.0%; Double Chance 1X: 24.7%; Double Chance X2: 90.4%; Double Chance 12 (either team wins): 84.9%; Under 4.5 goals: 78.5%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 9.6% | 10.46 |
| Draw | 15.1% | 6.60 |
| Paris Saint Germain win | 75.3% | 1.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 0.82 |
| Paris Saint Germain expected goals | 2.31 |
| Expected total goals | 3.13 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 39.0% |
| Under 3.5 | 61.0% |
| Over 4.5 | 21.5% |
| Under 4.5 | 78.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.49% |
| 2 | 0-1 | 10.32% |
| 3 | 1-2 | 10.25% |
| 4 | 0-3 | 9.60% |
| 5 | 1-3 | 7.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 9.6% | 7.9% | 11.00 | +5.1% |
| Draw | 15.1% | 11.8% | 7.11 | +7.7% |
| Paris Saint Germain win | 75.3% | 80.3% | 1.27 | -4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T18:00:00+00:00 |
| Fixture id | 9a9f6c78276f74f15f42b013b033aa5d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:56Z |
| Market best draw last update utc | 2026-10-21T10:37:56Z |
| Market best away last update utc | 2026-10-21T10:37:56Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Le Havre |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8210 |
| Dc lambda away | 2.3072 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 49.7% |
| P btts no | 50.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.15 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.90 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.65 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 11.2% |
| Unadjusted draw probability | 18.5% |
| Unadjusted away-win probability | 70.3% |
| Raw p over 1 5 | 82.4% |
| Raw p under 3 5 | 61.9% |
| Raw p btts yes | 50.9% |
| P home draw | 24.7% |
| P draw away | 90.4% |
| P home away | 84.9% |
| Raw p home draw | 29.7% |
| Raw p draw away | 88.8% |
| Raw p home away | 81.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 8.25 |
| Reference draw odds | 5.90 |
| Reference away odds | 1.20 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:28Z |
| Market reference home last update utc | 2026-10-21T10:38:28Z |
| Market reference draw last update utc | 2026-10-21T10:38:28Z |
| Market reference away last update utc | 2026-10-21T10:38:28Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:17Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:17Z |
| Home probability edge | +1.7% |
| Draw probability edge | +3.3% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0334 |
| Raw ev home | 0.2349 |
| Raw edge prob draw | 0.0667 |
| Raw ev draw | 0.3140 |
| Raw edge prob away | -0.1001 |
| Raw ev away | -0.1073 |

</details>


---

## 2026-10-30 — Lille vs RC Lens

The model's most likely 1X2 outcome is **Lille win** at **40.8%**. Expected goals are 1.25 for Lille and 1.12 for RC Lens (2.37 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 43.0%; Under 3.5 goals: 78.4%; Double Chance 1X: 67.9%; Double Chance X2: 59.2%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 90.6%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 40.8% | 2.45 |
| Draw | 27.1% | 3.69 |
| RC Lens win | 32.1% | 3.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.25 |
| RC Lens expected goals | 1.12 |
| Expected total goals | 2.37 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 69.4% |
| Under 1.5 | 30.6% |
| Over 2.5 | 43.0% |
| Under 2.5 | 57.0% |
| Over 3.5 | 21.6% |
| Under 3.5 | 78.4% |
| Over 4.5 | 9.4% |
| Under 4.5 | 90.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.80% |
| 2 | 1-0 | 11.60% |
| 3 | 0-1 | 9.69% |
| 4 | 0-0 | 9.34% |
| 5 | 2-1 | 8.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 40.8% | 43.2% | 2.45 | -0.1% |
| Draw | 27.1% | 24.9% | 3.65 | -1.1% |
| RC Lens win | 32.1% | 31.9% | 3.02 | -2.9% |
| Over 2.5 | 43.0% | 56.6% | 1.75 | -24.8% |
| Under 2.5 | 57.0% | 43.4% | 2.25 | +28.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:05:00+00:00 |
| Fixture id | 7932d9a82dcdb164a3e4ef5e03694ee3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:37:56Z |
| Market best draw last update utc | 2026-10-21T10:37:56Z |
| Market best away last update utc | 2026-10-21T10:37:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2460 |
| Dc lambda away | 1.1238 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:28.492805+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.71 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.27 |
| Fair Over 2.5 odds | 2.33 |
| Fair Under 2.5 odds | 1.75 |
| Fair Over 3.5 odds | 4.63 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.61 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 38.3% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 69.2% |
| Raw p under 3 5 | 78.5% |
| Raw p btts yes | 48.8% |
| P home draw | 67.9% |
| P draw away | 59.2% |
| P home away | 72.9% |
| Raw p home draw | 67.6% |
| Raw p draw away | 61.7% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.12 |
| Reference draw odds | 3.47 |
| Reference away odds | 2.78 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:28Z |
| Market reference home last update utc | 2026-10-21T10:38:28Z |
| Market reference draw last update utc | 2026-10-21T10:38:28Z |
| Market reference away last update utc | 2026-10-21T10:38:28Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:37:56Z |
| Market best under 2 5 last update utc | 2026-10-21T10:37:56Z |
| Home probability edge | -2.4% |
| Draw probability edge | +2.2% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -13.6% |
| Under 2.5 probability edge | +13.6% |
| Raw edge prob home | -0.0486 |
| Raw ev home | -0.0609 |
| Raw edge prob draw | 0.0439 |
| Raw ev draw | 0.0692 |
| Raw edge prob away | 0.0047 |
| Raw ev away | -0.0223 |

</details>


---
