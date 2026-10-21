# La Liga — football model report

Fixtures in this report: **12**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,988 |
| Training data through | 2026-10-19 |
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
| Training sha256 | 2fbb6cb5b006895481f9b132d9a84c39d6946b757e07af41c299a4eda8b8feeb |
| Training as of utc | 2026-10-21T10:37:09.449184+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 88, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 88, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 25, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T10:37:09.449184+00:00', 'observations': 156, 'observations_sha256': '88ae16c82ec3f29404233aee0b5fbe9864ade6c2711906328255efb780ecac4f', 'eligible_training_matches': 72, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 98, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 9, 'retrospective_eligible_training_matches': 72, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'dec7117e3771c4fbb91d2d998ebd06beae2010bec224861ab9f2bd7044e243f8', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5521.524 |
| Base scoring parameter | 0.090 |
| Home-advantage parameter | 0.278 |
| Dixon-Coles low-score adjustment | -0.020 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 12.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261021T103709449184Z_f416df8a0a0bc28f0f7d4b01307011979ff73dd7105c3d158ab6bbad6c81b62a.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
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

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **44.8%**. Expected goals are 1.24 for Levante and 1.54 for Athletic Bilbao (2.78 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 52.1%; Under 3.5 goals: 69.6%; Double Chance 1X: 55.2%; Double Chance X2: 71.7%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 56.4%; BTTS No (at least one team does not score): 43.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 28.3% | 3.54 |
| Draw | 27.0% | 3.71 |
| Athletic Bilbao win | 44.8% | 2.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.24 |
| Athletic Bilbao expected goals | 1.54 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 52.1% |
| Under 2.5 | 47.9% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.77% |
| 2 | 0-1 | 9.48% |
| 3 | 1-2 | 9.28% |
| 4 | 0-2 | 7.48% |
| 5 | 1-0 | 6.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 28.3% | 26.1% | 3.82 | +7.9% |
| Draw | 27.0% | 28.4% | 3.44 | -7.2% |
| Athletic Bilbao win | 44.8% | 45.5% | 2.19 | -2.0% |
| Over 2.5 | 52.1% | 47.1% | 2.08 | +8.4% |
| Under 2.5 | 47.9% | 52.9% | 1.87 | -10.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T18:00:00+00:00 |
| Fixture id | a362cccad837f1ffae61ff43a3536688 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:56Z |
| Market best draw last update utc | 2026-10-21T10:36:36Z |
| Market best away last update utc | 2026-10-21T10:36:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2403 |
| Dc lambda away | 1.5395 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.69 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.78 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 30.4% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 76.8% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 56.1% |
| P home draw | 55.2% |
| P draw away | 71.7% |
| P home away | 73.0% |
| Raw p home draw | 56.0% |
| Raw p draw away | 69.6% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.64 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.13 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:00Z |
| Market reference home last update utc | 2026-10-21T10:37:00Z |
| Market reference draw last update utc | 2026-10-21T10:37:00Z |
| Market reference away last update utc | 2026-10-21T10:37:00Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:00Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:00Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:36Z |
| Home probability edge | +2.2% |
| Draw probability edge | -1.4% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | +5.1% |
| Under 2.5 probability edge | -5.1% |
| Raw edge prob home | 0.0439 |
| Raw ev home | 0.1632 |
| Raw edge prob draw | -0.0288 |
| Raw ev draw | -0.1215 |
| Raw edge prob away | -0.0151 |
| Raw ev away | -0.0361 |
| Market p home draw | 55.1% |
| Market home draw odds | 1.78 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T10:36:37Z |
| Market reference home draw last update utc | 2026-10-21T10:37:00Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.6% |
| Market draw away odds | 1.32 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-21T10:36:36Z |
| Market reference draw away last update utc | 2026-10-21T10:37:00Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.4% |
| Market home away odds | 1.37 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-21T10:36:37Z |
| Market reference home away last update utc | 2026-10-21T10:37:00Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home draw odds | 1.75 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 73.4% |
| Market over 1 5 odds | 1.33 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-21T10:36:56Z |
| Market reference over 1 5 odds | 1.34 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market reference over 1 5 last update utc | 2026-10-21T10:36:56Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 74.1% |
| Market under 3 5 odds | 1.32 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T10:36:56Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.60 |
| Market reference under 3 5 last update utc | 2026-10-21T10:36:56Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.3% |
| Market btts yes odds | 1.82 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T10:36:37Z |
| Market reference btts yes odds | 1.82 |
| Market reference btts yes opposite odds | 2.06 |
| Market reference btts yes last update utc | 2026-10-21T10:36:37Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **58.3%**. Expected goals are 1.63 for Alavés and 0.60 for Málaga (2.23 combined). The most likely exact score is 1-0 at 16.2%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 38.0%; Under 3.5 goals: 81.7%; Double Chance 1X: 83.6%; Double Chance X2: 41.7%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 92.6%; BTTS Yes (both teams score): 37.0%; BTTS No (at least one team does not score): 63.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 58.3% | 1.72 |
| Draw | 25.4% | 3.94 |
| Málaga win | 16.4% | 6.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.63 |
| Málaga expected goals | 0.60 |
| Expected total goals | 2.23 |
| Over 0.5 | 88.7% |
| Under 0.5 | 11.3% |
| Over 1.5 | 64.8% |
| Under 1.5 | 35.2% |
| Over 2.5 | 38.0% |
| Under 2.5 | 62.0% |
| Over 3.5 | 18.3% |
| Under 3.5 | 81.7% |
| Over 4.5 | 7.4% |
| Under 4.5 | 92.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.19% |
| 2 | 2-0 | 13.34% |
| 3 | 0-0 | 11.27% |
| 4 | 1-1 | 11.09% |
| 5 | 2-1 | 8.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 58.3% | 54.5% | 1.84 | +7.2% |
| Draw | 25.4% | 26.1% | 3.76 | -4.7% |
| Málaga win | 16.4% | 19.4% | 4.97 | -18.6% |
| Over 2.5 | 38.0% | 46.1% | 2.12 | -19.5% |
| Under 2.5 | 62.0% | 53.9% | 1.84 | +14.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T19:00:00+00:00 |
| Fixture id | 903eb4941471ffe20d525b02dd3b77aa |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:36Z |
| Market best draw last update utc | 2026-10-21T10:36:56Z |
| Market best away last update utc | 2026-10-21T10:36:56Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6279 |
| Dc lambda away | 0.6043 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 37.0% |
| P btts no | 63.0% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.87 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.84 |
| Fair Over 2.5 odds | 2.63 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.48 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.53 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 62.1% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 36.7% |
| P home draw | 83.6% |
| P draw away | 41.7% |
| P home away | 74.6% |
| Raw p home draw | 86.7% |
| Raw p draw away | 37.9% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.79 |
| Reference draw odds | 3.62 |
| Reference away odds | 4.80 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:01Z |
| Market reference home last update utc | 2026-10-21T10:37:01Z |
| Market reference draw last update utc | 2026-10-21T10:37:01Z |
| Market reference away last update utc | 2026-10-21T10:37:01Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:36Z |
| Home probability edge | +3.8% |
| Draw probability edge | -0.8% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | 0.0765 |
| Raw ev home | 0.1426 |
| Raw edge prob draw | -0.0150 |
| Raw ev draw | -0.0749 |
| Raw edge prob away | -0.0614 |
| Raw ev away | -0.3390 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **72.5%**. Expected goals are 2.28 for Atlético Madrid and 0.89 for Deportivo La Coruña (3.17 combined). The most likely exact score is 2-0 at 11.6%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 62.4%; Under 3.5 goals: 60.3%; Double Chance 1X: 88.9%; Double Chance X2: 27.5%; Double Chance 12 (either team wins): 83.5%; Under 4.5 goals: 78.0%; BTTS Yes (both teams score): 52.3%; BTTS No (at least one team does not score): 47.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 72.5% | 1.38 |
| Draw | 16.5% | 6.06 |
| Deportivo La Coruña win | 11.1% | 9.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.28 |
| Deportivo La Coruña expected goals | 0.89 |
| Expected total goals | 3.17 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 62.4% |
| Under 2.5 | 37.6% |
| Over 3.5 | 39.7% |
| Under 3.5 | 60.3% |
| Over 4.5 | 22.0% |
| Under 4.5 | 78.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.55% |
| 2 | 2-1 | 10.27% |
| 3 | 1-0 | 9.95% |
| 4 | 3-0 | 8.78% |
| 5 | 3-1 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 72.5% | 76.4% | 1.31 | -5.1% |
| Draw | 16.5% | 14.5% | 6.48 | +6.9% |
| Deportivo La Coruña win | 11.1% | 9.1% | 10.18 | +12.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:00:00+00:00 |
| Fixture id | 70df1835c3b5ddff1c99e0189532136b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:36Z |
| Market best draw last update utc | 2026-10-21T10:36:36Z |
| Market best away last update utc | 2026-10-21T10:36:56Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2804 |
| Dc lambda away | 0.8889 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 52.3% |
| P btts no | 47.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.63 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.92 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.66 |
| Fair Over 3.5 odds | 2.52 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.55 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 68.5% |
| Unadjusted draw probability | 18.5% |
| Unadjusted away-win probability | 13.0% |
| Raw p over 1 5 | 82.6% |
| Raw p under 3 5 | 60.9% |
| Raw p btts yes | 53.0% |
| P home draw | 88.9% |
| P draw away | 27.5% |
| P home away | 83.5% |
| Raw p home draw | 87.0% |
| Raw p draw away | 31.5% |
| Raw p home away | 81.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.29 |
| Reference draw odds | 6.20 |
| Reference away odds | 9.60 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:01Z |
| Market reference home last update utc | 2026-10-21T10:37:01Z |
| Market reference draw last update utc | 2026-10-21T10:37:01Z |
| Market reference away last update utc | 2026-10-21T10:37:01Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:59Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:59Z |
| Home probability edge | -3.9% |
| Draw probability edge | +2.0% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | -0.0784 |
| Raw ev home | -0.1021 |
| Raw edge prob draw | 0.0399 |
| Raw ev draw | 0.1981 |
| Raw edge prob away | 0.0385 |
| Raw ev away | 0.3207 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **51.8%**. Expected goals are 1.40 for Rayo Vallecano and 0.90 for Elche CF (2.29 combined). The most likely exact score is 1-0 at 14.8%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 40.9%; Under 3.5 goals: 79.8%; Double Chance 1X: 78.0%; Double Chance X2: 48.2%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 44.4%; BTTS No (at least one team does not score): 55.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 51.8% | 1.93 |
| Draw | 26.2% | 3.82 |
| Elche CF win | 22.0% | 4.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.40 |
| Elche CF expected goals | 0.90 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 67.3% |
| Under 1.5 | 32.7% |
| Over 2.5 | 40.9% |
| Under 2.5 | 59.1% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.84% |
| 2 | 1-1 | 12.14% |
| 3 | 2-0 | 10.55% |
| 4 | 0-0 | 9.72% |
| 5 | 2-1 | 9.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 51.8% | 55.4% | 1.81 | -6.2% |
| Draw | 26.2% | 24.5% | 3.94 | +3.0% |
| Elche CF win | 22.0% | 20.1% | 4.78 | +5.2% |
| Over 2.5 | 40.9% | 52.7% | 1.88 | -23.1% |
| Under 2.5 | 59.1% | 47.3% | 2.07 | +22.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T12:00:00+00:00 |
| Fixture id | 734ad601156f5f4e6bc42317e5141516 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:36Z |
| Market best draw last update utc | 2026-10-21T10:36:36Z |
| Market best away last update utc | 2026-10-21T10:36:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Vallecano |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3966 |
| Dc lambda away | 0.8983 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.4% |
| P btts no | 55.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.29 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.95 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.75 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 67.1% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 44.9% |
| P home draw | 78.0% |
| P draw away | 48.2% |
| P home away | 73.8% |
| Raw p home draw | 76.1% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.76 |
| Reference draw odds | 3.84 |
| Reference away odds | 4.65 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:01Z |
| Market reference home last update utc | 2026-10-21T10:37:01Z |
| Market reference draw last update utc | 2026-10-21T10:37:01Z |
| Market reference away last update utc | 2026-10-21T10:37:01Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.01 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:36Z |
| Home probability edge | -3.6% |
| Draw probability edge | +1.6% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -11.7% |
| Under 2.5 probability edge | +11.7% |
| Raw edge prob home | -0.0711 |
| Raw ev home | -0.1260 |
| Raw edge prob draw | 0.0327 |
| Raw ev draw | 0.0948 |
| Raw edge prob away | 0.0385 |
| Raw ev away | 0.1437 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Espanyol win** at **38.9%**. Expected goals are 1.90 for Real Racing Club de Santander and 2.13 for Espanyol (4.04 combined). The most likely exact score is 1-1 at 8.2%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 76.0%; Under 3.5 goals: 42.8%; Double Chance 1X: 61.1%; Double Chance X2: 62.2%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 62.8%; BTTS Yes (both teams score): 75.7%; BTTS No (at least one team does not score): 24.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 37.8% | 2.65 |
| Draw | 23.3% | 4.28 |
| Espanyol win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.90 |
| Espanyol expected goals | 2.13 |
| Expected total goals | 4.04 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 76.0% |
| Under 2.5 | 24.0% |
| Over 3.5 | 57.2% |
| Under 3.5 | 42.8% |
| Over 4.5 | 37.2% |
| Under 4.5 | 62.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.22% |
| 2 | 2-2 | 8.18% |
| 3 | 2-1 | 7.33% |
| 4 | 1-2 | 6.76% |
| 5 | 3-2 | 4.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 37.8% | 40.4% | 2.46 | -7.0% |
| Draw | 23.3% | 25.9% | 3.76 | -12.3% |
| Espanyol win | 38.9% | 33.7% | 2.92 | +13.5% |
| Over 2.5 | 76.0% | 57.3% | 1.73 | +31.4% |
| Under 2.5 | 24.0% | 42.7% | 2.28 | -45.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:15:00+00:00 |
| Fixture id | 5960b1b6c20acfd78e78764fed47d505 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:36Z |
| Market best draw last update utc | 2026-10-21T10:36:36Z |
| Market best away last update utc | 2026-10-21T10:36:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9031 |
| Dc lambda away | 2.1319 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 75.7% |
| P btts no | 24.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.56 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.35 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.16 |
| Fair Over 3.5 odds | 1.75 |
| Fair Under 3.5 odds | 2.34 |
| Fair Over 4.5 odds | 2.69 |
| Fair Under 4.5 odds | 1.59 |
| Unadjusted home-win probability | 35.2% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 91.2% |
| Raw p under 3 5 | 42.7% |
| Raw p btts yes | 75.1% |
| P home draw | 61.1% |
| P draw away | 62.2% |
| P home away | 76.7% |
| Raw p home draw | 56.0% |
| Raw p draw away | 64.8% |
| Raw p home away | 79.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.39 |
| Reference draw odds | 3.66 |
| Reference away odds | 2.84 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:01Z |
| Market reference home last update utc | 2026-10-21T10:37:01Z |
| Market reference draw last update utc | 2026-10-21T10:37:01Z |
| Market reference away last update utc | 2026-10-21T10:37:01Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:36Z |
| Home probability edge | -2.6% |
| Draw probability edge | -2.6% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | +18.7% |
| Under 2.5 probability edge | -18.7% |
| Raw edge prob home | -0.0514 |
| Raw ev home | -0.1334 |
| Raw edge prob draw | -0.0513 |
| Raw ev draw | -0.2189 |
| Raw edge prob away | 0.1027 |
| Raw ev away | 0.2848 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **44.2%**. Expected goals are 1.27 for Valencia and 1.51 for Villarreal (2.78 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.6%; Double Chance 1X: 55.8%; Double Chance X2: 69.9%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.1% | 3.32 |
| Draw | 25.7% | 3.89 |
| Villarreal win | 44.2% | 2.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.27 |
| Villarreal expected goals | 1.51 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.16% |
| 2 | 0-1 | 9.49% |
| 3 | 1-2 | 9.33% |
| 4 | 0-2 | 7.33% |
| 5 | 1-0 | 7.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.1% | 28.3% | 3.45 | +3.8% |
| Draw | 25.7% | 25.7% | 3.78 | -2.8% |
| Villarreal win | 44.2% | 45.9% | 2.18 | -3.6% |
| Over 2.5 | 52.6% | 55.6% | 1.78 | -6.5% |
| Under 2.5 | 47.4% | 44.4% | 2.20 | +4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0dae715cc56fe201f9e667917c126691 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:36Z |
| Market best draw last update utc | 2026-10-21T10:36:36Z |
| Market best away last update utc | 2026-10-21T10:36:56Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2726 |
| Dc lambda away | 1.5058 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.48 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.70 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 76.8% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.3% |
| P home draw | 55.8% |
| P draw away | 69.9% |
| P home away | 74.3% |
| Raw p home draw | 57.5% |
| Raw p draw away | 68.1% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.36 |
| Reference draw odds | 3.68 |
| Reference away odds | 2.11 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:01Z |
| Market reference home last update utc | 2026-10-21T10:37:01Z |
| Market reference draw last update utc | 2026-10-21T10:37:01Z |
| Market reference away last update utc | 2026-10-21T10:37:01Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:36Z |
| Home probability edge | +1.8% |
| Draw probability edge | -0.0% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | 0.0356 |
| Raw ev home | 0.0995 |
| Raw edge prob draw | -0.0007 |
| Raw ev draw | -0.0295 |
| Raw edge prob away | -0.0349 |
| Raw ev away | -0.0744 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **56.1%**. Expected goals are 1.27 for Athletic Bilbao and 0.62 for Getafe (1.89 combined). The most likely exact score is 1-0 at 20.4%. Goal-market probabilities: at least one goal: 86.3%; Over 2.5 goals: 30.5%; Under 3.5 goals: 87.3%; Double Chance 1X: 83.0%; Double Chance X2: 43.9%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 95.5%; BTTS Yes (both teams score): 32.8%; BTTS No (at least one team does not score): 67.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 56.1% | 1.78 |
| Draw | 26.9% | 3.71 |
| Getafe win | 17.0% | 5.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.27 |
| Getafe expected goals | 0.62 |
| Expected total goals | 1.89 |
| Over 0.5 | 86.3% |
| Under 0.5 | 13.7% |
| Over 1.5 | 57.2% |
| Under 1.5 | 42.8% |
| Over 2.5 | 30.5% |
| Under 2.5 | 69.5% |
| Over 3.5 | 12.7% |
| Under 3.5 | 87.3% |
| Over 4.5 | 4.5% |
| Under 4.5 | 95.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.43% |
| 2 | 0-0 | 13.73% |
| 3 | 2-0 | 13.10% |
| 4 | 1-1 | 10.90% |
| 5 | 0-1 | 8.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 56.1% | 60.3% | 1.67 | -6.4% |
| Draw | 26.9% | 23.8% | 4.09 | +10.2% |
| Getafe win | 17.0% | 15.9% | 5.96 | +1.3% |
| Over 2.5 | 30.5% | 41.1% | 2.36 | -28.1% |
| Under 2.5 | 69.5% | 58.9% | 1.69 | +17.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T13:00:00+00:00 |
| Fixture id | 9c4254cba9944a839b421db27260504d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:36Z |
| Market best draw last update utc | 2026-10-21T10:36:56Z |
| Market best away last update utc | 2026-10-21T10:36:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2663 |
| Dc lambda away | 0.6244 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 32.8% |
| P btts no | 67.2% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.28 |
| Fair Over 1.5 odds | 1.75 |
| Fair Under 1.5 odds | 2.34 |
| Fair Over 2.5 odds | 3.28 |
| Fair Under 2.5 odds | 1.44 |
| Fair Over 3.5 odds | 7.89 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 22.04 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 51.8% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 18.1% |
| Raw p over 1 5 | 56.6% |
| Raw p under 3 5 | 87.6% |
| Raw p btts yes | 33.6% |
| P home draw | 83.0% |
| P draw away | 43.9% |
| P home away | 73.1% |
| Raw p home draw | 81.9% |
| Raw p draw away | 48.2% |
| Raw p home away | 69.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.62 |
| Reference draw odds | 3.94 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:01Z |
| Market reference home last update utc | 2026-10-21T10:37:01Z |
| Market reference draw last update utc | 2026-10-21T10:37:01Z |
| Market reference away last update utc | 2026-10-21T10:37:01Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.29 |
| Reference Under 2.5 odds | 1.64 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:36Z |
| Home probability edge | -4.3% |
| Draw probability edge | +3.1% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | -0.0854 |
| Raw ev home | -0.1349 |
| Raw edge prob draw | 0.0630 |
| Raw ev draw | 0.2306 |
| Raw edge prob away | 0.0224 |
| Raw ev away | 0.0793 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **54.6%**. Expected goals are 1.78 for Barcelona and 1.33 for Real Madrid (3.11 combined). The most likely exact score is 2-1 at 10.7%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 61.3%; Under 3.5 goals: 61.9%; Double Chance 1X: 75.1%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 79.0%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 54.6% | 1.83 |
| Draw | 20.5% | 4.89 |
| Real Madrid win | 24.9% | 4.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.78 |
| Real Madrid expected goals | 1.33 |
| Expected total goals | 3.11 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 61.3% |
| Under 2.5 | 38.7% |
| Over 3.5 | 38.1% |
| Under 3.5 | 61.9% |
| Over 4.5 | 21.0% |
| Under 4.5 | 79.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.75% |
| 2 | 1-1 | 9.33% |
| 3 | 1-0 | 8.84% |
| 4 | 2-0 | 8.06% |
| 5 | 3-1 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 54.6% | 61.5% | 1.63 | -11.0% |
| Draw | 20.5% | 17.3% | 5.81 | +18.8% |
| Real Madrid win | 24.9% | 21.2% | 4.52 | +12.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T20:00:00+00:00 |
| Fixture id | 72089d103a5fe6a922c35e17efba6ffc |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:36Z |
| Market best draw last update utc | 2026-10-21T10:36:56Z |
| Market best away last update utc | 2026-10-21T10:36:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7752 |
| Dc lambda away | 1.3331 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.69 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.59 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.77 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 47.7% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 28.7% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 61.4% |
| P home draw | 75.1% |
| P draw away | 45.4% |
| P home away | 79.5% |
| Raw p home draw | 71.3% |
| Raw p draw away | 52.3% |
| Raw p home away | 76.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.59 |
| Reference draw odds | 5.35 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:01Z |
| Market reference home last update utc | 2026-10-21T10:37:01Z |
| Market reference draw last update utc | 2026-10-21T10:37:01Z |
| Market reference away last update utc | 2026-10-21T10:37:01Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.18 |
| Reference Under 2.5 odds | 4.70 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:59Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:59Z |
| Home probability edge | -6.9% |
| Draw probability edge | +3.2% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -21.6% |
| Under 2.5 probability edge | +21.6% |
| Raw edge prob home | -0.1385 |
| Raw ev home | -0.2228 |
| Raw edge prob draw | 0.0636 |
| Raw ev draw | 0.3730 |
| Raw edge prob away | 0.0749 |
| Raw ev away | 0.2966 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **36.6%**. Expected goals are 1.33 for Celta Vigo and 1.28 for Real Betis (2.61 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.3%; Under 3.5 goals: 73.4%; Double Chance 1X: 63.7%; Double Chance X2: 63.4%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 53.4%; BTTS No (at least one team does not score): 46.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 36.6% | 2.73 |
| Draw | 27.1% | 3.69 |
| Real Betis win | 36.3% | 2.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.33 |
| Real Betis expected goals | 1.28 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.3% |
| Under 2.5 | 51.7% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.89% |
| 2 | 0-1 | 9.37% |
| 3 | 1-0 | 9.25% |
| 4 | 1-2 | 8.20% |
| 5 | 2-1 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 36.6% | 35.6% | 2.81 | +2.9% |
| Draw | 27.1% | 27.4% | 3.57 | -3.3% |
| Real Betis win | 36.3% | 37.0% | 2.67 | -3.1% |
| Over 2.5 | 48.3% | 51.7% | 1.91 | -7.7% |
| Under 2.5 | 51.7% | 48.3% | 2.03 | +4.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T15:15:00+00:00 |
| Fixture id | 2013e3955186ebe5258e85eb741a7553 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:56Z |
| Market best draw last update utc | 2026-10-21T10:36:36Z |
| Market best away last update utc | 2026-10-21T10:36:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3276 |
| Dc lambda away | 1.2829 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.4% |
| P btts no | 46.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.03 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.08 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 37.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 53.4% |
| P home draw | 63.7% |
| P draw away | 63.4% |
| P home away | 72.9% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.4% |
| Raw p home away | 73.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.70 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:01Z |
| Market reference home last update utc | 2026-10-21T10:37:01Z |
| Market reference draw last update utc | 2026-10-21T10:37:01Z |
| Market reference away last update utc | 2026-10-21T10:37:01Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:36Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0202 |
| Raw ev home | 0.0575 |
| Raw edge prob draw | -0.0053 |
| Raw ev draw | -0.0425 |
| Raw edge prob away | -0.0149 |
| Raw ev away | -0.0510 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **58.3%**. Expected goals are 2.01 for Real Sociedad and 1.04 for Levante (3.05 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 58.5%; Under 3.5 goals: 63.8%; Double Chance 1X: 80.4%; Double Chance X2: 41.7%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 56.5%; BTTS No (at least one team does not score): 43.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 58.3% | 1.72 |
| Draw | 22.1% | 4.52 |
| Levante win | 19.6% | 5.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 2.01 |
| Levante expected goals | 1.04 |
| Expected total goals | 3.05 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 58.5% |
| Under 2.5 | 41.5% |
| Over 3.5 | 36.2% |
| Under 3.5 | 63.8% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.35% |
| 2 | 2-1 | 9.75% |
| 3 | 2-0 | 9.34% |
| 4 | 1-0 | 9.12% |
| 5 | 3-1 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 58.3% | 57.1% | 1.76 | +2.5% |
| Draw | 22.1% | 22.6% | 4.26 | -5.8% |
| Levante win | 19.6% | 20.3% | 4.72 | -7.4% |
| Over 2.5 | 58.5% | 58.1% | 1.71 | +0.1% |
| Under 2.5 | 41.5% | 41.9% | 2.32 | -3.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:30:00+00:00 |
| Fixture id | 3cb8660cd2375b60e81144a7572cfb89 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:36Z |
| Market best draw last update utc | 2026-10-21T10:36:36Z |
| Market best away last update utc | 2026-10-21T10:36:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0051 |
| Dc lambda away | 1.0441 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.81 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.21 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 59.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 18.9% |
| Raw p over 1 5 | 81.0% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 56.3% |
| P home draw | 80.4% |
| P draw away | 41.7% |
| P home away | 77.9% |
| Raw p home draw | 81.1% |
| Raw p draw away | 40.6% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.71 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:01Z |
| Market reference home last update utc | 2026-10-21T10:37:01Z |
| Market reference draw last update utc | 2026-10-21T10:37:01Z |
| Market reference away last update utc | 2026-10-21T10:37:01Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:36Z |
| Home probability edge | +1.2% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0234 |
| Raw ev home | 0.0460 |
| Raw edge prob draw | -0.0098 |
| Raw ev draw | -0.0785 |
| Raw edge prob away | -0.0137 |
| Raw ev away | -0.1063 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **49.0%**. Expected goals are 1.48 for Sevilla and 0.98 for CA Osasuna (2.46 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.5%; Double Chance 1X: 75.9%; Double Chance X2: 51.0%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.6%; BTTS No (at least one team does not score): 51.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 49.0% | 2.04 |
| Draw | 26.9% | 3.72 |
| CA Osasuna win | 24.1% | 4.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.48 |
| CA Osasuna expected goals | 0.98 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.72% |
| 2 | 1-0 | 12.49% |
| 3 | 2-0 | 9.44% |
| 4 | 2-1 | 9.25% |
| 5 | 0-0 | 8.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 49.0% | 49.3% | 2.02 | -1.1% |
| Draw | 26.9% | 27.1% | 3.60 | -3.2% |
| CA Osasuna win | 24.1% | 23.6% | 4.37 | +5.5% |
| Over 2.5 | 44.6% | 44.7% | 2.19 | -2.3% |
| Under 2.5 | 55.4% | 55.3% | 1.79 | -0.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T20:00:00+00:00 |
| Fixture id | 85e464708d03287f24590e1478aeca31 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:36Z |
| Market best draw last update utc | 2026-10-21T10:36:36Z |
| Market best away last update utc | 2026-10-21T10:36:56Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.4830 |
| Dc lambda away | 0.9791 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.6% |
| P btts no | 51.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.31 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.26 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.64 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 48.5% |
| P home draw | 75.9% |
| P draw away | 51.0% |
| P home away | 73.1% |
| Raw p home draw | 75.3% |
| Raw p draw away | 51.4% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.97 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:01Z |
| Market reference home last update utc | 2026-10-21T10:37:01Z |
| Market reference draw last update utc | 2026-10-21T10:37:01Z |
| Market reference away last update utc | 2026-10-21T10:37:01Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:36Z |
| Home probability edge | -0.4% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0072 |
| Raw ev home | -0.0180 |
| Raw edge prob draw | -0.0041 |
| Raw ev draw | -0.0393 |
| Raw edge prob away | 0.0112 |
| Raw ev away | 0.0794 |

</details>


---

## 2026-10-30 — Villarreal vs Espanyol

The model's most likely 1X2 outcome is **Villarreal win** at **64.0%**. Expected goals are 2.22 for Villarreal and 0.99 for Espanyol (3.21 combined). The most likely exact score is 2-0 at 9.8%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 61.9%; Under 3.5 goals: 60.2%; Double Chance 1X: 84.0%; Double Chance X2: 36.0%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 64.0% | 1.56 |
| Draw | 20.1% | 4.98 |
| Espanyol win | 16.0% | 6.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.22 |
| Espanyol expected goals | 0.99 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 61.9% |
| Under 2.5 | 38.1% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.79% |
| 2 | 2-1 | 9.65% |
| 3 | 1-1 | 9.31% |
| 4 | 1-0 | 8.64% |
| 5 | 3-0 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 64.0% | 62.7% | 1.60 | +2.4% |
| Draw | 20.1% | 20.7% | 4.62 | -7.3% |
| Espanyol win | 16.0% | 16.6% | 5.70 | -9.0% |
| Over 2.5 | 61.9% | 60.0% | 1.66 | +2.8% |
| Under 2.5 | 38.1% | 40.0% | 2.42 | -7.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:00:00+00:00 |
| Fixture id | 00b03cb40c27ed23e2ecb18f062a5122 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T10:36:36Z |
| Market best draw last update utc | 2026-10-21T10:36:36Z |
| Market best away last update utc | 2026-10-21T10:36:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2233 |
| Dc lambda away | 0.9860 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:09.449184+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.01 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.90 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.56 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 65.2% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 15.3% |
| Raw p over 1 5 | 83.2% |
| Raw p under 3 5 | 60.0% |
| Raw p btts yes | 56.1% |
| P home draw | 84.0% |
| P draw away | 36.0% |
| P home away | 79.9% |
| Raw p home draw | 84.7% |
| Raw p draw away | 34.8% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.56 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.55 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:01Z |
| Market reference home last update utc | 2026-10-21T10:37:01Z |
| Market reference draw last update utc | 2026-10-21T10:37:01Z |
| Market reference away last update utc | 2026-10-21T10:37:01Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:01Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:36Z |
| Home probability edge | +1.2% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | +1.9% |
| Under 2.5 probability edge | -1.9% |
| Raw edge prob home | 0.0248 |
| Raw ev home | 0.0435 |
| Raw edge prob draw | -0.0121 |
| Raw ev draw | -0.1011 |
| Raw edge prob away | -0.0126 |
| Raw ev away | -0.1264 |

</details>


---
