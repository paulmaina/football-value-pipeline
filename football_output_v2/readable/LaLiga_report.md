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
| Training as of utc | 2026-10-21T09:18:43.688384+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 88, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 88, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 25, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T09:18:43.688384+00:00', 'observations': 156, 'observations_sha256': '88ae16c82ec3f29404233aee0b5fbe9864ade6c2711906328255efb780ecac4f', 'eligible_training_matches': 72, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 98, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 9, 'retrospective_eligible_training_matches': 72, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'dec7117e3771c4fbb91d2d998ebd06beae2010bec224861ab9f2bd7044e243f8', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
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
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261021T091843688384Z_9f33b771d7f12db6bd4f6e667437317ffb3d718f5a50719e9d9c892d8f7380b7.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
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

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **44.0%**. Expected goals are 1.24 for Levante and 1.54 for Athletic Bilbao (2.78 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 51.8%; Under 3.5 goals: 69.7%; Double Chance 1X: 56.0%; Double Chance X2: 72.0%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 85.4%; BTTS Yes (both teams score): 56.7%; BTTS No (at least one team does not score): 43.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 28.0% | 3.57 |
| Draw | 28.0% | 3.57 |
| Athletic Bilbao win | 44.0% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.24 |
| Athletic Bilbao expected goals | 1.54 |
| Expected total goals | 2.78 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 51.8% |
| Under 2.5 | 48.2% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.6% |
| Under 4.5 | 85.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.24% |
| 2 | 0-1 | 9.32% |
| 3 | 1-2 | 9.12% |
| 4 | 0-2 | 7.35% |
| 5 | 0-0 | 7.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 28.0% | 25.6% | 3.73 | +4.4% |
| Draw | 28.0% | 30.4% | 3.52 | -1.5% |
| Athletic Bilbao win | 44.0% | 44.0% | 2.24 | -1.4% |
| Over 2.5 | 51.8% | 49.0% | 2.07 | +7.2% |
| Under 2.5 | 48.2% | 51.0% | 1.92 | -7.4% |

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
| Market best home last update utc | 2026-10-21T09:18:34Z |
| Market best draw last update utc | 2026-10-21T09:17:37Z |
| Market best away last update utc | 2026-10-21T09:17:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.17 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.30 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.84 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 30.4% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 76.8% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 56.1% |
| P home draw | 56.0% |
| P draw away | 72.0% |
| P home away | 72.0% |
| Raw p home draw | 56.0% |
| Raw p draw away | 69.6% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 3.74 |
| Reference draw odds | 3.16 |
| Reference away odds | 2.21 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:53Z |
| Market reference home last update utc | 2026-10-21T09:18:53Z |
| Market reference draw last update utc | 2026-10-21T09:18:53Z |
| Market reference away last update utc | 2026-10-21T09:18:53Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market best over 2 5 last update utc | 2026-10-21T09:18:34Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:37Z |
| Home probability edge | +2.4% |
| Draw probability edge | -2.4% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | +2.8% |
| Under 2.5 probability edge | -2.8% |
| Raw edge prob home | 0.0490 |
| Raw ev home | 0.1357 |
| Raw edge prob draw | -0.0488 |
| Raw ev draw | -0.1011 |
| Raw edge prob away | -0.0002 |
| Raw ev away | -0.0141 |
| Market p home draw | 55.8% |
| Market home draw odds | 1.76 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T09:18:37Z |
| Market reference home draw last update utc | 2026-10-21T09:18:56Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.9% |
| Market draw away odds | 1.35 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-21T09:17:37Z |
| Market reference draw away last update utc | 2026-10-21T09:18:56Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.3% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-21T09:18:37Z |
| Market reference home away last update utc | 2026-10-21T09:18:56Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home draw odds | 1.70 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 74.2% |
| Market over 1 5 odds | 1.33 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-21T09:18:34Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.30 |
| Market reference over 1 5 last update utc | 2026-10-21T09:18:56Z |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 74.1% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T09:18:34Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.60 |
| Market reference under 3 5 last update utc | 2026-10-21T09:18:35Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 52.2% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T09:18:37Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-10-21T09:18:56Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **58.1%**. Expected goals are 1.63 for Alavés and 0.60 for Málaga (2.23 combined). The most likely exact score is 1-0 at 16.1%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 37.9%; Under 3.5 goals: 81.8%; Double Chance 1X: 83.4%; Double Chance X2: 41.9%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 92.6%; BTTS Yes (both teams score): 37.0%; BTTS No (at least one team does not score): 63.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 58.1% | 1.72 |
| Draw | 25.3% | 3.95 |
| Málaga win | 16.6% | 6.03 |

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
| Over 2.5 | 37.9% |
| Under 2.5 | 62.1% |
| Over 3.5 | 18.2% |
| Under 3.5 | 81.8% |
| Over 4.5 | 7.4% |
| Under 4.5 | 92.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.14% |
| 2 | 2-0 | 13.30% |
| 3 | 0-0 | 11.27% |
| 4 | 1-1 | 11.08% |
| 5 | 2-1 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 58.1% | 54.1% | 1.84 | +6.9% |
| Draw | 25.3% | 26.1% | 3.76 | -4.8% |
| Málaga win | 16.6% | 19.9% | 4.97 | -17.6% |
| Over 2.5 | 37.9% | 45.7% | 2.12 | -19.6% |
| Under 2.5 | 62.1% | 54.3% | 1.84 | +14.2% |

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
| Market best home last update utc | 2026-10-21T09:17:37Z |
| Market best draw last update utc | 2026-10-21T09:18:34Z |
| Market best away last update utc | 2026-10-21T09:18:34Z |
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
| Dc lambda away | 0.6038 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
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
| Fair Over 2.5 odds | 2.64 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.49 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.55 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 62.1% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 36.6% |
| P home draw | 83.4% |
| P draw away | 41.9% |
| P home away | 74.7% |
| Raw p home draw | 86.7% |
| Raw p draw away | 37.9% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.81 |
| Reference draw odds | 3.66 |
| Reference away odds | 4.75 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:53Z |
| Market reference home last update utc | 2026-10-21T09:18:53Z |
| Market reference draw last update utc | 2026-10-21T09:18:53Z |
| Market reference away last update utc | 2026-10-21T09:18:53Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.77 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:37Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:37Z |
| Home probability edge | +4.0% |
| Draw probability edge | -0.7% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | 0.0805 |
| Raw ev home | 0.1429 |
| Raw edge prob draw | -0.0145 |
| Raw ev draw | -0.0750 |
| Raw edge prob away | -0.0660 |
| Raw ev away | -0.3396 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **72.8%**. Expected goals are 2.28 for Atlético Madrid and 0.89 for Deportivo La Coruña (3.17 combined). The most likely exact score is 2-0 at 11.6%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 62.4%; Under 3.5 goals: 60.2%; Double Chance 1X: 89.5%; Double Chance X2: 27.2%; Double Chance 12 (either team wins): 83.3%; Under 4.5 goals: 78.0%; BTTS Yes (both teams score): 52.3%; BTTS No (at least one team does not score): 47.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 72.8% | 1.37 |
| Draw | 16.7% | 5.99 |
| Deportivo La Coruña win | 10.5% | 9.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.28 |
| Deportivo La Coruña expected goals | 0.89 |
| Expected total goals | 3.17 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 62.4% |
| Under 2.5 | 37.6% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 22.0% |
| Under 4.5 | 78.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.61% |
| 2 | 2-1 | 10.32% |
| 3 | 1-0 | 10.00% |
| 4 | 3-0 | 8.82% |
| 5 | 1-1 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 72.8% | 77.1% | 1.31 | -4.6% |
| Draw | 16.7% | 14.9% | 6.48 | +8.2% |
| Deportivo La Coruña win | 10.5% | 8.0% | 10.18 | +6.8% |

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
| Market best home last update utc | 2026-10-21T09:17:37Z |
| Market best draw last update utc | 2026-10-21T09:17:37Z |
| Market best away last update utc | 2026-10-21T09:18:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2800 |
| Dc lambda away | 0.8891 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 52.3% |
| P btts no | 47.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.33 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.94 |
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
| P home draw | 89.5% |
| P draw away | 27.2% |
| P home away | 83.3% |
| Raw p home draw | 87.0% |
| Raw p draw away | 31.5% |
| Raw p home away | 81.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.28 |
| Reference draw odds | 6.10 |
| Reference away odds | 11.00 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:53Z |
| Market reference home last update utc | 2026-10-21T09:18:53Z |
| Market reference draw last update utc | 2026-10-21T09:18:53Z |
| Market reference away last update utc | 2026-10-21T09:18:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:15Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:15Z |
| Home probability edge | -4.3% |
| Draw probability edge | +1.8% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0858 |
| Raw ev home | -0.1023 |
| Raw edge prob draw | 0.0360 |
| Raw ev draw | 0.1984 |
| Raw edge prob away | 0.0498 |
| Raw ev away | 0.3214 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **51.5%**. Expected goals are 1.40 for Rayo Vallecano and 0.90 for Elche CF (2.29 combined). The most likely exact score is 1-0 at 14.7%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 40.9%; Under 3.5 goals: 79.8%; Double Chance 1X: 77.6%; Double Chance X2: 48.5%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 44.4%; BTTS No (at least one team does not score): 55.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 51.5% | 1.94 |
| Draw | 26.1% | 3.83 |
| Elche CF win | 22.4% | 4.47 |

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
| 1 | 1-0 | 14.74% |
| 2 | 1-1 | 12.13% |
| 3 | 2-0 | 10.48% |
| 4 | 0-0 | 9.72% |
| 5 | 2-1 | 9.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 51.5% | 54.7% | 1.81 | -6.8% |
| Draw | 26.1% | 24.5% | 3.94 | +3.0% |
| Elche CF win | 22.4% | 20.8% | 4.78 | +6.8% |
| Over 2.5 | 40.9% | 52.4% | 1.88 | -23.1% |
| Under 2.5 | 59.1% | 47.6% | 2.07 | +22.3% |

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
| Market best home last update utc | 2026-10-21T09:17:37Z |
| Market best draw last update utc | 2026-10-21T09:17:37Z |
| Market best away last update utc | 2026-10-21T09:17:37Z |
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
| Dc lambda home | 1.3967 |
| Dc lambda away | 0.8983 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.4% |
| P btts no | 55.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.29 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.96 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.76 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 67.1% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 44.9% |
| P home draw | 77.6% |
| P draw away | 48.5% |
| P home away | 73.9% |
| Raw p home draw | 76.1% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.79 |
| Reference draw odds | 3.89 |
| Reference away odds | 4.56 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:53Z |
| Market reference home last update utc | 2026-10-21T09:18:53Z |
| Market reference draw last update utc | 2026-10-21T09:18:53Z |
| Market reference away last update utc | 2026-10-21T09:18:53Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:37Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:37Z |
| Home probability edge | -3.2% |
| Draw probability edge | +1.6% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | -0.0643 |
| Raw ev home | -0.1260 |
| Raw edge prob draw | 0.0329 |
| Raw ev draw | 0.0948 |
| Raw edge prob away | 0.0314 |
| Raw ev away | 0.1435 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Espanyol win** at **38.5%**. Expected goals are 1.90 for Real Racing Club de Santander and 2.13 for Espanyol (4.04 combined). The most likely exact score is 1-1 at 8.3%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 75.9%; Under 3.5 goals: 42.8%; Double Chance 1X: 61.5%; Double Chance X2: 62.1%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 62.9%; BTTS Yes (both teams score): 75.8%; BTTS No (at least one team does not score): 24.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 37.9% | 2.64 |
| Draw | 23.6% | 4.23 |
| Espanyol win | 38.5% | 2.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.90 |
| Espanyol expected goals | 2.13 |
| Expected total goals | 4.04 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 75.9% |
| Under 2.5 | 24.1% |
| Over 3.5 | 57.2% |
| Under 3.5 | 42.8% |
| Over 4.5 | 37.1% |
| Under 4.5 | 62.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.32% |
| 2 | 2-2 | 8.28% |
| 3 | 2-1 | 7.33% |
| 4 | 1-2 | 6.69% |
| 5 | 3-2 | 4.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 37.9% | 40.5% | 2.46 | -6.8% |
| Draw | 23.6% | 26.5% | 3.76 | -11.2% |
| Espanyol win | 38.5% | 33.1% | 2.92 | +12.4% |
| Over 2.5 | 75.9% | 57.3% | 1.73 | +31.3% |
| Under 2.5 | 24.1% | 42.7% | 2.28 | -45.1% |

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
| Market best home last update utc | 2026-10-21T09:17:37Z |
| Market best draw last update utc | 2026-10-21T09:17:37Z |
| Market best away last update utc | 2026-10-21T09:17:37Z |
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
| Dc lambda home | 1.9048 |
| Dc lambda away | 2.1314 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 75.8% |
| P btts no | 24.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.04 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.36 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.15 |
| Fair Over 3.5 odds | 1.75 |
| Fair Under 3.5 odds | 2.34 |
| Fair Over 4.5 odds | 2.69 |
| Fair Under 4.5 odds | 1.59 |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 91.2% |
| Raw p under 3 5 | 42.6% |
| Raw p btts yes | 75.2% |
| P home draw | 61.5% |
| P draw away | 62.1% |
| P home away | 76.4% |
| Raw p home draw | 56.0% |
| Raw p draw away | 64.7% |
| Raw p home away | 79.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.40 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.92 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:53Z |
| Market reference home last update utc | 2026-10-21T09:18:53Z |
| Market reference draw last update utc | 2026-10-21T09:18:53Z |
| Market reference away last update utc | 2026-10-21T09:18:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:21Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:21Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:37Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:37Z |
| Home probability edge | -2.6% |
| Draw probability edge | -2.8% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | +18.6% |
| Under 2.5 probability edge | -18.6% |
| Raw edge prob home | -0.0521 |
| Raw ev home | -0.1324 |
| Raw edge prob draw | -0.0570 |
| Raw ev draw | -0.2190 |
| Raw edge prob away | 0.1091 |
| Raw ev away | 0.2836 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **43.2%**. Expected goals are 1.27 for Valencia and 1.51 for Villarreal (2.78 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 52.5%; Under 3.5 goals: 69.7%; Double Chance 1X: 56.8%; Double Chance X2: 69.0%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 31.0% | 3.23 |
| Draw | 25.9% | 3.86 |
| Villarreal win | 43.2% | 2.32 |

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
| Over 2.5 | 52.5% |
| Under 2.5 | 47.5% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.24% |
| 2 | 0-1 | 9.27% |
| 3 | 1-2 | 9.11% |
| 4 | 1-0 | 7.45% |
| 5 | 2-1 | 7.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 31.0% | 30.1% | 3.45 | +6.8% |
| Draw | 25.9% | 26.1% | 3.78 | -2.2% |
| Villarreal win | 43.2% | 43.9% | 2.18 | -5.9% |
| Over 2.5 | 52.5% | 55.8% | 1.78 | -6.6% |
| Under 2.5 | 47.5% | 44.2% | 2.20 | +4.6% |

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
| Market best home last update utc | 2026-10-21T09:17:37Z |
| Market best draw last update utc | 2026-10-21T09:17:37Z |
| Market best away last update utc | 2026-10-21T09:18:34Z |
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
| Dc lambda home | 1.2722 |
| Dc lambda away | 1.5057 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.37 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.30 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.72 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 76.8% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.2% |
| P home draw | 56.8% |
| P draw away | 69.0% |
| P home away | 74.1% |
| Raw p home draw | 57.5% |
| Raw p draw away | 68.1% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 3.20 |
| Reference draw odds | 3.67 |
| Reference away odds | 2.22 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:53Z |
| Market reference home last update utc | 2026-10-21T09:18:53Z |
| Market reference draw last update utc | 2026-10-21T09:18:53Z |
| Market reference away last update utc | 2026-10-21T09:18:53Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.14 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:37Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:37Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0180 |
| Raw ev home | 0.0992 |
| Raw edge prob draw | -0.0041 |
| Raw ev draw | -0.0295 |
| Raw edge prob away | -0.0139 |
| Raw ev away | -0.0743 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **56.0%**. Expected goals are 1.27 for Athletic Bilbao and 0.62 for Getafe (1.89 combined). The most likely exact score is 1-0 at 20.4%. Goal-market probabilities: at least one goal: 86.3%; Over 2.5 goals: 30.4%; Under 3.5 goals: 87.3%; Double Chance 1X: 82.9%; Double Chance X2: 44.0%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 95.5%; BTTS Yes (both teams score): 32.8%; BTTS No (at least one team does not score): 67.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 56.0% | 1.79 |
| Draw | 26.9% | 3.71 |
| Getafe win | 17.1% | 5.85 |

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
| Over 2.5 | 30.4% |
| Under 2.5 | 69.6% |
| Over 3.5 | 12.7% |
| Under 3.5 | 87.3% |
| Over 4.5 | 4.5% |
| Under 4.5 | 95.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.39% |
| 2 | 0-0 | 13.73% |
| 3 | 2-0 | 13.08% |
| 4 | 1-1 | 10.90% |
| 5 | 0-1 | 8.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 56.0% | 60.1% | 1.67 | -6.5% |
| Draw | 26.9% | 23.8% | 4.09 | +10.2% |
| Getafe win | 17.1% | 16.1% | 5.96 | +1.9% |
| Over 2.5 | 30.4% | 39.6% | 2.36 | -28.1% |
| Under 2.5 | 69.6% | 60.4% | 1.69 | +17.5% |

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
| Market best home last update utc | 2026-10-21T09:17:37Z |
| Market best draw last update utc | 2026-10-21T09:18:34Z |
| Market best away last update utc | 2026-10-21T09:17:37Z |
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
| Dc lambda home | 1.2664 |
| Dc lambda away | 0.6244 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
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
| Fair Over 3.5 odds | 7.90 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 22.04 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 51.8% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 18.1% |
| Raw p over 1 5 | 56.6% |
| Raw p under 3 5 | 87.6% |
| Raw p btts yes | 33.6% |
| P home draw | 82.9% |
| P draw away | 44.0% |
| P home away | 73.1% |
| Raw p home draw | 81.9% |
| Raw p draw away | 48.2% |
| Raw p home away | 69.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.62 |
| Reference draw odds | 3.90 |
| Reference away odds | 5.65 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:53Z |
| Market reference home last update utc | 2026-10-21T09:18:53Z |
| Market reference draw last update utc | 2026-10-21T09:18:53Z |
| Market reference away last update utc | 2026-10-21T09:18:53Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.46 |
| Reference Under 2.5 odds | 1.63 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:34Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:37Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:37Z |
| Home probability edge | -4.2% |
| Draw probability edge | +3.1% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -9.1% |
| Under 2.5 probability edge | +9.1% |
| Raw edge prob home | -0.0831 |
| Raw ev home | -0.1348 |
| Raw edge prob draw | 0.0629 |
| Raw ev draw | 0.2305 |
| Raw edge prob away | 0.0201 |
| Raw ev away | 0.0792 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **53.7%**. Expected goals are 1.78 for Barcelona and 1.33 for Real Madrid (3.11 combined). The most likely exact score is 2-1 at 10.6%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 61.5%; Under 3.5 goals: 62.0%; Double Chance 1X: 73.5%; Double Chance X2: 46.3%; Double Chance 12 (either team wins): 80.2%; Under 4.5 goals: 79.0%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 53.7% | 1.86 |
| Draw | 19.8% | 5.06 |
| Real Madrid win | 26.5% | 3.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.78 |
| Real Madrid expected goals | 1.33 |
| Expected total goals | 3.11 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 21.0% |
| Under 4.5 | 79.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.58% |
| 2 | 1-1 | 9.01% |
| 3 | 1-0 | 8.70% |
| 4 | 2-0 | 7.94% |
| 5 | 1-2 | 6.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 53.7% | 59.8% | 1.63 | -12.4% |
| Draw | 19.8% | 15.9% | 5.81 | +14.8% |
| Real Madrid win | 26.5% | 24.3% | 4.52 | +19.8% |

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
| Market best home last update utc | 2026-10-21T09:17:37Z |
| Market best draw last update utc | 2026-10-21T09:18:34Z |
| Market best away last update utc | 2026-10-21T09:17:37Z |
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
| Dc lambda away | 1.3329 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.56 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.58 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.75 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 47.7% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 28.7% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 61.4% |
| P home draw | 73.5% |
| P draw away | 46.3% |
| P home away | 80.2% |
| Raw p home draw | 71.3% |
| Raw p draw away | 52.3% |
| Raw p home away | 76.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.64 |
| Reference draw odds | 5.88 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:53Z |
| Market reference home last update utc | 2026-10-21T09:18:53Z |
| Market reference draw last update utc | 2026-10-21T09:18:53Z |
| Market reference away last update utc | 2026-10-21T09:18:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.19 |
| Reference Under 2.5 odds | 4.85 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:15Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:15Z |
| Home probability edge | -6.1% |
| Draw probability edge | +3.9% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -21.1% |
| Under 2.5 probability edge | +21.1% |
| Raw edge prob home | -0.1213 |
| Raw ev home | -0.2227 |
| Raw edge prob draw | 0.0776 |
| Raw ev draw | 0.3730 |
| Raw edge prob away | 0.0437 |
| Raw ev away | 0.2965 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Real Betis win** at **37.1%**. Expected goals are 1.33 for Celta Vigo and 1.28 for Real Betis (2.61 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 48.4%; Under 3.5 goals: 73.4%; Double Chance 1X: 62.9%; Double Chance X2: 63.9%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 53.4%; BTTS No (at least one team does not score): 46.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 36.1% | 2.77 |
| Draw | 26.8% | 3.73 |
| Real Betis win | 37.1% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.33 |
| Real Betis expected goals | 1.28 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.4% |
| Under 2.5 | 51.6% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.77% |
| 2 | 0-1 | 9.58% |
| 3 | 1-0 | 9.11% |
| 4 | 1-2 | 8.38% |
| 5 | 2-1 | 7.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 36.1% | 34.5% | 2.81 | +1.4% |
| Draw | 26.8% | 26.8% | 3.57 | -4.2% |
| Real Betis win | 37.1% | 38.6% | 2.67 | -1.0% |
| Over 2.5 | 48.4% | 52.9% | 1.91 | -7.5% |
| Under 2.5 | 51.6% | 47.1% | 2.03 | +4.7% |

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
| Market best home last update utc | 2026-10-21T09:18:34Z |
| Market best draw last update utc | 2026-10-21T09:17:37Z |
| Market best away last update utc | 2026-10-21T09:17:37Z |
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
| Dc lambda home | 1.3278 |
| Dc lambda away | 1.2828 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.4% |
| P btts no | 46.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.15 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.06 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 37.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 53.4% |
| P home draw | 62.9% |
| P draw away | 63.9% |
| P home away | 73.2% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.4% |
| Raw p home away | 73.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.80 |
| Reference draw odds | 3.57 |
| Reference away odds | 2.51 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:53Z |
| Market reference home last update utc | 2026-10-21T09:18:53Z |
| Market reference draw last update utc | 2026-10-21T09:18:53Z |
| Market reference away last update utc | 2026-10-21T09:18:53Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:37Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:37Z |
| Home probability edge | +1.6% |
| Draw probability edge | -0.0% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | 0.0313 |
| Raw ev home | 0.0577 |
| Raw edge prob draw | -0.0003 |
| Raw ev draw | -0.0425 |
| Raw edge prob away | -0.0310 |
| Raw ev away | -0.0512 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **57.4%**. Expected goals are 2.01 for Real Sociedad and 1.04 for Levante (3.05 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 58.4%; Under 3.5 goals: 63.8%; Double Chance 1X: 79.8%; Double Chance X2: 42.6%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 56.6%; BTTS No (at least one team does not score): 43.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 57.4% | 1.74 |
| Draw | 22.4% | 4.46 |
| Levante win | 20.2% | 4.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 2.01 |
| Levante expected goals | 1.04 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 80.8% |
| Under 1.5 | 19.2% |
| Over 2.5 | 58.4% |
| Under 2.5 | 41.6% |
| Over 3.5 | 36.2% |
| Under 3.5 | 63.8% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.49% |
| 2 | 2-1 | 9.61% |
| 3 | 2-0 | 9.20% |
| 4 | 1-0 | 8.99% |
| 5 | 3-1 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 57.4% | 55.4% | 1.76 | +1.0% |
| Draw | 22.4% | 23.2% | 4.26 | -4.5% |
| Levante win | 20.2% | 21.4% | 4.72 | -4.8% |
| Over 2.5 | 58.4% | 60.1% | 1.71 | -0.1% |
| Under 2.5 | 41.6% | 39.9% | 2.32 | -3.5% |

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
| Market best home last update utc | 2026-10-21T09:17:37Z |
| Market best draw last update utc | 2026-10-21T09:17:37Z |
| Market best away last update utc | 2026-10-21T09:17:37Z |
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
| Dc lambda home | 2.0053 |
| Dc lambda away | 1.0441 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 56.6% |
| P btts no | 43.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.54 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.22 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.40 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.24 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 59.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 18.9% |
| Raw p over 1 5 | 81.0% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 56.3% |
| P home draw | 79.8% |
| P draw away | 42.6% |
| P home away | 77.6% |
| Raw p home draw | 81.1% |
| Raw p draw away | 40.6% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.77 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.43 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:53Z |
| Market reference home last update utc | 2026-10-21T09:18:53Z |
| Market reference draw last update utc | 2026-10-21T09:18:53Z |
| Market reference away last update utc | 2026-10-21T09:18:53Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:34Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:34Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:37Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:37Z |
| Home probability edge | +2.0% |
| Draw probability edge | -0.8% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | 0.0407 |
| Raw ev home | 0.0461 |
| Raw edge prob draw | -0.0158 |
| Raw ev draw | -0.0785 |
| Raw edge prob away | -0.0249 |
| Raw ev away | -0.1064 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **48.6%**. Expected goals are 1.48 for Sevilla and 0.98 for CA Osasuna (2.46 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 44.3%; Under 3.5 goals: 76.6%; Double Chance 1X: 76.4%; Double Chance X2: 51.4%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 48.8%; BTTS No (at least one team does not score): 51.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 48.6% | 2.06 |
| Draw | 27.8% | 3.59 |
| CA Osasuna win | 23.6% | 4.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.48 |
| CA Osasuna expected goals | 0.98 |
| Expected total goals | 2.46 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 70.7% |
| Under 1.5 | 29.3% |
| Over 2.5 | 44.3% |
| Under 2.5 | 55.7% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.18% |
| 2 | 1-0 | 12.39% |
| 3 | 2-0 | 9.37% |
| 4 | 2-1 | 9.17% |
| 5 | 0-0 | 9.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 48.6% | 48.6% | 2.02 | -1.9% |
| Draw | 27.8% | 29.0% | 3.60 | +0.3% |
| CA Osasuna win | 23.6% | 22.4% | 4.37 | +3.0% |
| Over 2.5 | 44.3% | 42.7% | 2.19 | -3.0% |
| Under 2.5 | 55.7% | 57.3% | 1.79 | -0.3% |

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
| Market best home last update utc | 2026-10-21T09:17:37Z |
| Market best draw last update utc | 2026-10-21T09:17:37Z |
| Market best away last update utc | 2026-10-21T09:18:34Z |
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
| Dc lambda away | 0.9790 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.8% |
| P btts no | 51.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.92 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.27 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.73 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 48.5% |
| P home draw | 76.4% |
| P draw away | 51.4% |
| P home away | 72.2% |
| Raw p home draw | 75.3% |
| Raw p draw away | 51.4% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.99 |
| Reference draw odds | 3.25 |
| Reference away odds | 4.15 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:53Z |
| Market reference home last update utc | 2026-10-21T09:18:53Z |
| Market reference draw last update utc | 2026-10-21T09:18:53Z |
| Market reference away last update utc | 2026-10-21T09:18:53Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 2.21 |
| Reference Under 2.5 odds | 1.68 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:53Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:37Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:37Z |
| Home probability edge | +0.0% |
| Draw probability edge | -1.2% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | 0.0006 |
| Raw ev home | -0.0180 |
| Raw edge prob draw | -0.0232 |
| Raw ev draw | -0.0392 |
| Raw edge prob away | 0.0226 |
| Raw ev away | 0.0794 |

</details>


---

## 2026-10-30 — Villarreal vs Espanyol

The model's most likely 1X2 outcome is **Villarreal win** at **64.3%**. Expected goals are 2.22 for Villarreal and 0.99 for Espanyol (3.21 combined). The most likely exact score is 2-0 at 9.8%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 62.0%; Under 3.5 goals: 60.2%; Double Chance 1X: 84.2%; Double Chance X2: 35.7%; Double Chance 12 (either team wins): 80.0%; Under 4.5 goals: 78.0%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 64.3% | 1.56 |
| Draw | 20.0% | 5.01 |
| Espanyol win | 15.8% | 6.34 |

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
| Over 2.5 | 62.0% |
| Under 2.5 | 38.0% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 22.0% |
| Under 4.5 | 78.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.84% |
| 2 | 2-1 | 9.70% |
| 3 | 1-1 | 9.26% |
| 4 | 1-0 | 8.67% |
| 5 | 3-0 | 7.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 64.3% | 63.3% | 1.60 | +2.8% |
| Draw | 20.0% | 20.4% | 4.62 | -7.8% |
| Espanyol win | 15.8% | 16.2% | 5.70 | -10.0% |
| Over 2.5 | 62.0% | 60.0% | 1.66 | +2.9% |
| Under 2.5 | 38.0% | 40.0% | 2.42 | -8.0% |

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
| Market best home last update utc | 2026-10-21T09:17:37Z |
| Market best draw last update utc | 2026-10-21T09:17:37Z |
| Market best away last update utc | 2026-10-21T09:17:37Z |
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
| Dc lambda home | 2.2235 |
| Dc lambda away | 0.9857 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:18:43.688384+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.13 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.91 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.55 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 65.2% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 15.3% |
| Raw p over 1 5 | 83.2% |
| Raw p under 3 5 | 60.0% |
| Raw p btts yes | 56.1% |
| P home draw | 84.2% |
| P draw away | 35.7% |
| P home away | 80.0% |
| Raw p home draw | 84.7% |
| Raw p draw away | 34.8% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.48 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.75 |
| Market reference 1x2 last update utc | 2026-10-21T09:18:48Z |
| Market reference home last update utc | 2026-10-21T09:18:48Z |
| Market reference draw last update utc | 2026-10-21T09:18:48Z |
| Market reference away last update utc | 2026-10-21T09:18:48Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-21T09:18:21Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:18:21Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:37Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:37Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | 0.0193 |
| Raw ev home | 0.0437 |
| Raw edge prob draw | -0.0100 |
| Raw ev draw | -0.1013 |
| Raw edge prob away | -0.0093 |
| Raw ev away | -0.1269 |

</details>


---
