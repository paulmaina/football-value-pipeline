# La Liga — football model report

Fixtures in this report: **16**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,223 |
| Training data through | 2026-10-17 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | 1aa705e00f91bb215ff362c8f1f2e11e693c7f666ed51e06165fd488a243f18f |
| Training as of utc | 2026-10-18T08:35:54.071035+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 83, 'bbs_added_results': 5, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 83, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T08:35:54.071035+00:00', 'observations': 92, 'observations_sha256': '1a43270a9604934dcb9704f8e505df61b4519dd2b23fa52572f0745dfdc35444', 'eligible_training_matches': 41, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 69, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 4, 'retrospective_eligible_training_matches': 41, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'e3fc44bb94a661b71870b111b107b4941167282fe42a40893b7249a21f0bbbc9', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 2001.953 |
| Base scoring parameter | 0.087 |
| Home-advantage parameter | 0.278 |
| Dixon-Coles low-score adjustment | -0.029 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-17', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 16.00 |
| Additional event odds calls used before this league | 5.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261018T083554071035Z_3c5c10e3eef8e77e20194fb7af22e44328382340a40656a54a9f738c467094cd.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **55.9%**. Expected goals are 2.78 for CA Osasuna and 1.56 for Real Racing Club de Santander (4.34 combined). The most likely exact score is 2-2 at 7.6%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.5%; Under 3.5 goals: 37.7%; Double Chance 1X: 77.4%; Double Chance X2: 44.1%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 57.6%; BTTS Yes (both teams score): 75.4%; BTTS No (at least one team does not score): 24.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 55.9% | 1.79 |
| Draw | 21.5% | 4.64 |
| Real Racing Club de Santander win | 22.6% | 4.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 2.78 |
| Real Racing Club de Santander expected goals | 1.56 |
| Expected total goals | 4.34 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 93.0% |
| Under 1.5 | 7.0% |
| Over 2.5 | 79.5% |
| Under 2.5 | 20.5% |
| Over 3.5 | 62.3% |
| Under 3.5 | 37.7% |
| Over 4.5 | 42.4% |
| Under 4.5 | 57.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.62% |
| 2 | 1-1 | 7.23% |
| 3 | 2-1 | 6.98% |
| 4 | 3-1 | 6.46% |
| 5 | 1-2 | 5.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 55.9% | 48.8% | 2.04 | +14.0% |
| Draw | 21.5% | 25.7% | 3.78 | -18.6% |
| Real Racing Club de Santander win | 22.6% | 25.4% | 3.82 | -13.7% |
| Over 2.5 | 79.5% | 59.2% | 1.68 | +33.5% |
| Under 2.5 | 20.5% | 40.8% | 2.38 | -51.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T12:00:00+00:00 |
| Fixture id | 1f566f17c50fe5162724ec2863d2207b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Osasuna |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7784 |
| Dc lambda away | 1.5621 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 75.4% |
| P btts no | 24.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 54.89 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 14.22 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.87 |
| Fair Over 3.5 odds | 1.60 |
| Fair Under 3.5 odds | 2.66 |
| Fair Over 4.5 odds | 2.36 |
| Fair Under 4.5 odds | 1.74 |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 17.3% |
| Unadjusted away-win probability | 19.7% |
| Raw p over 1 5 | 93.2% |
| Raw p under 3 5 | 37.0% |
| Raw p btts yes | 74.3% |
| P home draw | 77.4% |
| P draw away | 44.1% |
| P home away | 78.5% |
| Raw p home draw | 80.3% |
| Raw p draw away | 37.1% |
| Raw p home away | 82.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.99 |
| Reference draw odds | 3.68 |
| Reference away odds | 3.72 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | +7.1% |
| Draw probability edge | -4.2% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | +20.2% |
| Under 2.5 probability edge | -20.2% |
| Raw edge prob home | 0.1411 |
| Raw ev home | 0.2840 |
| Raw edge prob draw | -0.0839 |
| Raw ev draw | -0.3445 |
| Raw edge prob away | -0.0572 |
| Raw ev away | -0.2467 |
| Market p home draw | 74.1% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:08Z |
| Market reference home draw last update utc | 2026-10-18T08:35:53Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.8% |
| Market draw away odds | 1.86 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:08Z |
| Market reference draw away last update utc | 2026-10-18T08:35:53Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:08Z |
| Market reference home away last update utc | 2026-10-18T08:35:53Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.30 |
| Market reference dc draw away odds | 1.86 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 80.9% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-18T08:35:28Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.3% |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.66 |
| Market reference under 3 5 last update utc | 2026-10-18T08:35:49Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 61.0% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:08Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.45 |
| Market reference btts yes last update utc | 2026-10-18T08:35:51Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **46.1%**. Expected goals are 1.49 for Celta Vigo and 0.95 for Alavés (2.44 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 43.5%; Under 3.5 goals: 77.3%; Double Chance 1X: 74.3%; Double Chance X2: 53.9%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 46.1% | 2.17 |
| Draw | 28.2% | 3.54 |
| Alavés win | 25.7% | 3.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.49 |
| Alavés expected goals | 0.95 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 43.5% |
| Under 2.5 | 56.5% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.33% |
| 2 | 1-0 | 11.77% |
| 3 | 0-0 | 9.53% |
| 4 | 2-0 | 9.03% |
| 5 | 0-1 | 8.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 46.1% | 42.6% | 2.33 | +7.3% |
| Draw | 28.2% | 29.6% | 3.31 | -6.6% |
| Alavés win | 25.7% | 27.8% | 3.52 | -9.5% |
| Over 2.5 | 43.5% | 40.0% | 2.42 | +5.2% |
| Under 2.5 | 56.5% | 60.0% | 1.66 | -6.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T14:15:00+00:00 |
| Fixture id | aabe899ecc4c19a1fafe5440151b62e4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4926 |
| Dc lambda away | 0.9475 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.2% |
| P btts no | 51.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.49 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.30 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.11 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.5% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.4% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 47.8% |
| P home draw | 74.3% |
| P draw away | 53.9% |
| P home away | 71.8% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.27 |
| Reference draw odds | 3.22 |
| Reference away odds | 3.42 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.35 |
| Reference Under 2.5 odds | 1.61 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | +3.5% |
| Draw probability edge | -1.4% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | +3.5% |
| Under 2.5 probability edge | -3.5% |
| Raw edge prob home | 0.0693 |
| Raw ev home | 0.1540 |
| Raw edge prob draw | -0.0274 |
| Raw ev draw | -0.1109 |
| Raw edge prob away | -0.0419 |
| Raw ev away | -0.1689 |
| Market p home draw | 72.3% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:08Z |
| Market reference home draw last update utc | 2026-10-18T08:35:53Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.6% |
| Market draw away odds | 1.68 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:08Z |
| Market reference draw away last update utc | 2026-10-18T08:35:53Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.2% |
| Market home away odds | 1.38 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:08Z |
| Market reference home away last update utc | 2026-10-18T08:35:53Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home away odds | 1.37 |
| Market p over 1 5 | 65.1% |
| Market reference over 1 5 odds | 1.50 |
| Market reference over 1 5 opposite odds | 2.70 |
| Market reference over 1 5 last update utc | 2026-10-18T08:35:48Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 81.0% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 4.80 |
| Market reference under 3 5 last update utc | 2026-10-18T08:35:28Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 46.7% |
| Market btts yes odds | 1.95 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:08Z |
| Market reference btts yes odds | 2.12 |
| Market reference btts yes opposite odds | 1.86 |
| Market reference btts yes last update utc | 2026-10-18T08:35:50Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.5%**. Expected goals are 0.63 for Málaga and 1.28 for Real Sociedad (1.92 combined). The most likely exact score is 0-1 at 17.3%. Goal-market probabilities: at least one goal: 85.7%; Over 2.5 goals: 30.2%; Under 3.5 goals: 87.4%; Double Chance 1X: 51.5%; Double Chance X2: 77.0%; Double Chance 12 (either team wins): 71.5%; Under 4.5 goals: 95.5%; BTTS Yes (both teams score): 34.0%; BTTS No (at least one team does not score): 66.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.0% | 4.35 |
| Draw | 28.5% | 3.51 |
| Real Sociedad win | 48.5% | 2.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.28 |
| Expected total goals | 1.92 |
| Over 0.5 | 85.7% |
| Under 0.5 | 14.3% |
| Over 1.5 | 56.9% |
| Under 1.5 | 43.1% |
| Over 2.5 | 30.2% |
| Under 2.5 | 69.8% |
| Over 3.5 | 12.6% |
| Under 3.5 | 87.4% |
| Over 4.5 | 4.5% |
| Under 4.5 | 95.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.32% |
| 2 | 0-0 | 14.31% |
| 3 | 1-1 | 11.67% |
| 4 | 1-0 | 11.45% |
| 5 | 0-2 | 11.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.0% | 28.0% | 3.49 | -19.8% |
| Draw | 28.5% | 27.0% | 3.62 | +3.2% |
| Real Sociedad win | 48.5% | 45.1% | 2.21 | +7.2% |
| Over 2.5 | 30.2% | 55.6% | 1.78 | -46.3% |
| Under 2.5 | 69.8% | 44.4% | 2.20 | +53.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T16:30:00+00:00 |
| Fixture id | 1051298b4aca6f07113309bff598a5c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6328 |
| Dc lambda away | 1.2827 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 34.0% |
| P btts no | 66.0% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.99 |
| Fair Over 1.5 odds | 1.76 |
| Fair Under 1.5 odds | 2.32 |
| Fair Over 2.5 odds | 3.31 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 7.96 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 22.16 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 18.0% |
| Unadjusted draw probability | 30.0% |
| Unadjusted away-win probability | 51.9% |
| Raw p over 1 5 | 57.4% |
| Raw p under 3 5 | 87.2% |
| Raw p btts yes | 34.2% |
| P home draw | 51.5% |
| P draw away | 77.0% |
| P home away | 71.5% |
| Raw p home draw | 48.1% |
| Raw p draw away | 82.0% |
| Raw p home away | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.40 |
| Reference draw odds | 3.52 |
| Reference away odds | 2.15 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | -5.0% |
| Draw probability edge | +1.5% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -25.4% |
| Under 2.5 probability edge | +25.4% |
| Raw edge prob home | -0.0994 |
| Raw ev home | -0.3709 |
| Raw edge prob draw | 0.0306 |
| Raw ev draw | 0.0870 |
| Raw edge prob away | 0.0688 |
| Raw ev away | 0.1480 |
| Market p home draw | 55.3% |
| Market home draw odds | 1.75 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:08Z |
| Market reference home draw last update utc | 2026-10-18T08:35:53Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.8% |
| Market draw away odds | 1.35 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:08Z |
| Market reference draw away last update utc | 2026-10-18T08:35:53Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.9% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:08Z |
| Market reference home away last update utc | 2026-10-18T08:35:53Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.74 |
| Market reference dc draw away odds | 1.34 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-18T08:35:28Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.5% |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.73 |
| Market reference under 3 5 last update utc | 2026-10-18T08:35:49Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 60.9% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:08Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.52 |
| Market reference btts yes last update utc | 2026-10-18T08:35:50Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **77.6%**. Expected goals are 2.63 for Real Madrid and 0.75 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.7%; Under 3.5 goals: 56.4%; Double Chance 1X: 91.8%; Double Chance X2: 22.4%; Double Chance 12 (either team wins): 85.8%; Under 4.5 goals: 74.8%; BTTS Yes (both teams score): 48.8%; BTTS No (at least one team does not score): 51.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.6% | 1.29 |
| Draw | 14.2% | 7.03 |
| Sevilla win | 8.2% | 12.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.63 |
| Sevilla expected goals | 0.75 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 65.7% |
| Under 2.5 | 34.3% |
| Over 3.5 | 43.6% |
| Under 3.5 | 56.4% |
| Over 4.5 | 25.2% |
| Under 4.5 | 74.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.88% |
| 2 | 3-0 | 10.40% |
| 3 | 2-1 | 8.85% |
| 4 | 1-0 | 8.84% |
| 5 | 3-1 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.6% | 77.8% | 1.29 | +0.1% |
| Draw | 14.2% | 13.8% | 6.70 | -4.6% |
| Sevilla win | 8.2% | 8.3% | 10.90 | -11.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T19:00:00+00:00 |
| Fixture id | eccd63bf768e2f2a358b871d3f33a63d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.6284 |
| Dc lambda away | 0.7450 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 48.8% |
| P btts no | 51.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.36 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.97 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.6% |
| Unadjusted away-win probability | 8.0% |
| Raw p over 1 5 | 85.2% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 48.9% |
| P home draw | 91.8% |
| P draw away | 22.4% |
| P home away | 85.8% |
| Raw p home draw | 92.0% |
| Raw p draw away | 22.6% |
| Raw p home away | 85.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.27 |
| Reference draw odds | 6.60 |
| Reference away odds | 10.75 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.99 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:30Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:30Z |
| Home probability edge | -0.2% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | -0.0049 |
| Raw ev home | -0.0021 |
| Raw edge prob draw | 0.0078 |
| Raw ev draw | -0.0203 |
| Raw edge prob away | -0.0029 |
| Raw ev away | -0.1259 |
| Market p home draw | 91.4% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:08Z |
| Market reference home draw last update utc | 2026-10-18T08:35:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.0% |
| Market draw away odds | 3.98 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:08Z |
| Market reference draw away last update utc | 2026-10-18T08:35:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.6% |
| Market home away odds | 1.14 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:08Z |
| Market reference home away last update utc | 2026-10-18T08:35:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.07 |
| Market reference dc draw away odds | 4.44 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 86.8% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-10-18T08:35:28Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 54.0% |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.08 |
| Market reference under 3 5 last update utc | 2026-10-18T08:35:49Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 50.0% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:08Z |
| Market reference btts yes odds | 1.93 |
| Market reference btts yes opposite odds | 1.93 |
| Market reference btts yes last update utc | 2026-10-18T08:35:56Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.0%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.5%. Goal-market probabilities: at least one goal: 81.5%; Over 2.5 goals: 23.3%; Under 3.5 goals: 91.5%; Double Chance 1X: 68.2%; Double Chance X2: 65.0%; Double Chance 12 (either team wins): 66.8%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 31.1%; BTTS No (at least one team does not score): 68.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.0% | 2.86 |
| Draw | 33.2% | 3.01 |
| Rayo Vallecano win | 31.8% | 3.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.5% |
| Under 0.5 | 18.5% |
| Over 1.5 | 49.3% |
| Under 1.5 | 50.7% |
| Over 2.5 | 23.3% |
| Under 2.5 | 76.7% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.50% |
| 2 | 1-0 | 16.17% |
| 3 | 0-1 | 16.01% |
| 4 | 1-1 | 12.49% |
| 5 | 2-0 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.0% | 32.9% | 2.99 | +4.6% |
| Draw | 33.2% | 31.0% | 3.16 | +4.9% |
| Rayo Vallecano win | 31.8% | 36.0% | 2.74 | -12.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T19:00:00+00:00 |
| Fixture id | 4a88bc4de574d43ef34677fd8d78722f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9053 |
| Dc lambda away | 0.7387 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 31.1% |
| P btts no | 68.9% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.40 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.29 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.75 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.38 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.1% |
| Unadjusted draw probability | 35.3% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.3% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.5% |
| P home draw | 68.2% |
| P draw away | 65.0% |
| P home away | 66.8% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.9% |
| Raw p home away | 64.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.91 |
| Reference draw odds | 3.08 |
| Reference away odds | 2.67 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.60 |
| Reference Under 2.5 odds | 1.51 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Home probability edge | +2.1% |
| Draw probability edge | +2.1% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -12.5% |
| Under 2.5 probability edge | +12.5% |
| Raw edge prob home | 0.0412 |
| Raw ev home | 0.1079 |
| Raw edge prob draw | 0.0427 |
| Raw ev draw | 0.1160 |
| Raw edge prob away | -0.0839 |
| Raw ev away | -0.2430 |
| Market p home draw | 64.3% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:08Z |
| Market reference home draw last update utc | 2026-10-18T08:35:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.4% |
| Market draw away odds | 1.45 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:08Z |
| Market reference draw away last update utc | 2026-10-18T08:35:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 67.4% |
| Market home away odds | 1.41 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:08Z |
| Market reference home away last update utc | 2026-10-18T08:35:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.50 |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home away odds | 1.43 |
| Market p over 1 5 | 63.7% |
| Market reference over 1 5 odds | 1.53 |
| Market reference over 1 5 opposite odds | 2.60 |
| Market reference over 1 5 last update utc | 2026-10-18T08:35:49Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 83.8% |
| Market reference under 3 5 odds | 1.18 |
| Market reference under 3 5 opposite odds | 5.50 |
| Market reference under 3 5 last update utc | 2026-10-18T08:35:28Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 44.6% |
| Market btts yes odds | 2.07 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:08Z |
| Market reference btts yes odds | 2.15 |
| Market reference btts yes opposite odds | 1.75 |
| Market reference btts yes last update utc | 2026-10-18T08:35:56Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.6%**. Expected goals are 1.27 for Levante and 1.36 for Athletic Bilbao (2.63 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.8%; Under 3.5 goals: 72.9%; Double Chance 1X: 58.4%; Double Chance X2: 69.0%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 31.0% | 3.22 |
| Draw | 27.3% | 3.66 |
| Athletic Bilbao win | 41.6% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.27 |
| Athletic Bilbao expected goals | 1.36 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 48.8% |
| Under 2.5 | 51.2% |
| Over 3.5 | 27.1% |
| Under 3.5 | 72.9% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.02% |
| 2 | 0-1 | 10.16% |
| 3 | 1-2 | 9.10% |
| 4 | 1-0 | 7.94% |
| 5 | 0-0 | 7.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 31.0% | 27.8% | 3.52 | +9.3% |
| Draw | 27.3% | 27.8% | 3.52 | -3.7% |
| Athletic Bilbao win | 41.6% | 44.4% | 2.24 | -6.8% |
| Over 2.5 | 48.8% | 48.6% | 2.02 | -1.5% |
| Under 2.5 | 51.2% | 51.4% | 1.92 | -1.6% |

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
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2662 |
| Dc lambda away | 1.3630 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.99 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.88 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.70 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.91 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 34.3% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 38.8% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 73.0% |
| Raw p btts yes | 53.8% |
| P home draw | 58.4% |
| P draw away | 69.0% |
| P home away | 72.7% |
| Raw p home draw | 61.2% |
| Raw p draw away | 65.7% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.42 |
| Reference draw odds | 3.42 |
| Reference away odds | 2.18 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | +3.3% |
| Draw probability edge | -0.4% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0650 |
| Raw ev home | 0.2071 |
| Raw edge prob draw | -0.0089 |
| Raw ev draw | -0.0529 |
| Raw edge prob away | -0.0562 |
| Raw ev away | -0.1308 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **56.8%**. Expected goals are 1.39 for Alavés and 0.44 for Málaga (1.84 combined). The most likely exact score is 1-0 at 20.5%. Goal-market probabilities: at least one goal: 84.4%; Over 2.5 goals: 27.7%; Under 3.5 goals: 88.9%; Double Chance 1X: 83.8%; Double Chance X2: 43.2%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 96.2%; BTTS Yes (both teams score): 27.2%; BTTS No (at least one team does not score): 72.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 56.8% | 1.76 |
| Draw | 27.0% | 3.71 |
| Málaga win | 16.2% | 6.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.39 |
| Málaga expected goals | 0.44 |
| Expected total goals | 1.84 |
| Over 0.5 | 84.4% |
| Under 0.5 | 15.6% |
| Over 1.5 | 54.2% |
| Under 1.5 | 45.8% |
| Over 2.5 | 27.7% |
| Under 2.5 | 72.3% |
| Over 3.5 | 11.1% |
| Under 3.5 | 88.9% |
| Over 4.5 | 3.8% |
| Under 4.5 | 96.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.53% |
| 2 | 0-0 | 15.64% |
| 3 | 2-0 | 14.49% |
| 4 | 1-1 | 9.77% |
| 5 | 0-1 | 9.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 56.8% | 52.9% | 1.89 | +7.3% |
| Draw | 27.0% | 26.0% | 3.73 | +0.6% |
| Málaga win | 16.2% | 21.1% | 4.57 | -25.8% |
| Over 2.5 | 27.7% | 47.3% | 2.07 | -42.7% |
| Under 2.5 | 72.3% | 52.7% | 1.88 | +35.9% |

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
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3934 |
| Dc lambda away | 0.4434 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 27.2% |
| P btts no | 72.8% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.39 |
| Fair Over 1.5 odds | 1.85 |
| Fair Under 1.5 odds | 2.18 |
| Fair Over 2.5 odds | 3.61 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.00 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 26.19 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 60.6% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 55.1% |
| Raw p under 3 5 | 88.5% |
| Raw p btts yes | 27.2% |
| P home draw | 83.8% |
| P draw away | 43.2% |
| P home away | 73.0% |
| Raw p home draw | 88.6% |
| Raw p draw away | 39.4% |
| Raw p home away | 72.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.84 |
| Reference draw odds | 3.64 |
| Reference away odds | 4.45 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.01 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | +3.8% |
| Draw probability edge | +1.0% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -19.6% |
| Under 2.5 probability edge | +19.6% |
| Raw edge prob home | 0.0767 |
| Raw ev home | 0.1455 |
| Raw edge prob draw | 0.0199 |
| Raw ev draw | 0.0435 |
| Raw edge prob away | -0.0966 |
| Raw ev away | -0.4784 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **73.2%**. Expected goals are 2.25 for Atlético Madrid and 0.90 for Deportivo La Coruña (3.15 combined). The most likely exact score is 2-0 at 11.8%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 62.1%; Under 3.5 goals: 60.6%; Double Chance 1X: 89.9%; Double Chance X2: 26.8%; Double Chance 12 (either team wins): 83.3%; Under 4.5 goals: 78.3%; BTTS Yes (both teams score): 52.3%; BTTS No (at least one team does not score): 47.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 73.2% | 1.37 |
| Draw | 16.7% | 5.98 |
| Deportivo La Coruña win | 10.1% | 9.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.25 |
| Deportivo La Coruña expected goals | 0.90 |
| Expected total goals | 3.15 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 39.4% |
| Under 3.5 | 60.6% |
| Over 4.5 | 21.7% |
| Under 4.5 | 78.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.76% |
| 2 | 2-1 | 10.57% |
| 3 | 1-0 | 10.20% |
| 4 | 3-0 | 8.81% |
| 5 | 3-1 | 7.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 73.2% | 78.8% | 1.27 | -7.0% |
| Draw | 16.7% | 14.4% | 6.46 | +8.0% |
| Deportivo La Coruña win | 10.1% | 6.8% | 13.10 | +32.0% |

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
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2466 |
| Dc lambda away | 0.8989 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 52.3% |
| P btts no | 47.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.97 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.91 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.60 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 67.6% |
| Unadjusted draw probability | 19.0% |
| Unadjusted away-win probability | 13.4% |
| Raw p over 1 5 | 82.4% |
| Raw p under 3 5 | 61.5% |
| Raw p btts yes | 53.3% |
| P home draw | 89.9% |
| P draw away | 26.8% |
| P home away | 83.3% |
| Raw p home draw | 86.6% |
| Raw p draw away | 32.4% |
| Raw p home away | 81.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.25 |
| Reference draw odds | 6.15 |
| Reference away odds | 12.50 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.60 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:30Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:30Z |
| Home probability edge | -5.6% |
| Draw probability edge | +2.3% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.1122 |
| Raw ev home | -0.1414 |
| Raw edge prob draw | 0.0460 |
| Raw ev draw | 0.2280 |
| Raw edge prob away | 0.0662 |
| Raw ev away | 0.7532 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **49.3%**. Expected goals are 1.35 for Rayo Vallecano and 1.04 for Elche CF (2.39 combined). The most likely exact score is 1-0 at 13.6%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 43.5%; Under 3.5 goals: 77.8%; Double Chance 1X: 75.6%; Double Chance X2: 50.7%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 90.3%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 49.3% | 2.03 |
| Draw | 26.3% | 3.80 |
| Elche CF win | 24.4% | 4.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.35 |
| Elche CF expected goals | 1.04 |
| Expected total goals | 2.39 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 69.6% |
| Under 1.5 | 30.4% |
| Over 2.5 | 43.5% |
| Under 2.5 | 56.5% |
| Over 3.5 | 22.2% |
| Under 3.5 | 77.8% |
| Over 4.5 | 9.7% |
| Under 4.5 | 90.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.64% |
| 2 | 1-1 | 12.41% |
| 3 | 2-1 | 9.88% |
| 4 | 2-0 | 9.46% |
| 5 | 0-0 | 8.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 49.3% | 55.4% | 1.81 | -10.7% |
| Draw | 26.3% | 24.5% | 3.94 | +3.6% |
| Elche CF win | 24.4% | 20.1% | 4.78 | +16.5% |
| Over 2.5 | 43.5% | 52.7% | 1.88 | -18.2% |
| Under 2.5 | 56.5% | 47.3% | 2.07 | +17.0% |

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
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Vallecano |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3457 |
| Dc lambda away | 1.0442 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.19 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.29 |
| Fair Over 2.5 odds | 2.30 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.51 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.31 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 28.7% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.1% |
| Raw p btts yes | 48.3% |
| P home draw | 75.6% |
| P draw away | 50.7% |
| P home away | 73.7% |
| Raw p home draw | 71.3% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.76 |
| Reference draw odds | 3.84 |
| Reference away odds | 4.65 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.01 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | -6.1% |
| Draw probability edge | +1.8% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -9.2% |
| Under 2.5 probability edge | +9.2% |
| Raw edge prob home | -0.1215 |
| Raw ev home | -0.2171 |
| Raw edge prob draw | 0.0356 |
| Raw ev draw | 0.1065 |
| Raw edge prob away | 0.0858 |
| Raw ev away | 0.3701 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **38.8%**. Expected goals are 1.95 for Real Racing Club de Santander and 1.97 for Espanyol (3.93 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 74.4%; Under 3.5 goals: 44.8%; Double Chance 1X: 62.6%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 64.8%; BTTS Yes (both teams score): 74.6%; BTTS No (at least one team does not score): 25.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 38.8% | 2.58 |
| Draw | 23.8% | 4.20 |
| Espanyol win | 37.4% | 2.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.95 |
| Espanyol expected goals | 1.97 |
| Expected total goals | 3.93 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 90.5% |
| Under 1.5 | 9.5% |
| Over 2.5 | 74.4% |
| Under 2.5 | 25.6% |
| Over 3.5 | 55.2% |
| Under 3.5 | 44.8% |
| Over 4.5 | 35.2% |
| Under 4.5 | 64.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.71% |
| 2 | 2-2 | 8.16% |
| 3 | 2-1 | 7.38% |
| 4 | 1-2 | 7.07% |
| 5 | 3-1 | 4.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 38.8% | 38.6% | 2.57 | -0.4% |
| Draw | 23.8% | 26.2% | 3.71 | -11.7% |
| Espanyol win | 37.4% | 35.2% | 2.80 | +4.8% |
| Over 2.5 | 74.4% | 55.9% | 1.77 | +31.7% |
| Under 2.5 | 25.6% | 44.1% | 2.22 | -43.2% |

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
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
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
| Dc lambda home | 1.9549 |
| Dc lambda away | 1.9732 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 74.6% |
| P btts no | 25.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.00 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.52 |
| Fair Over 2.5 odds | 1.34 |
| Fair Under 2.5 odds | 3.91 |
| Fair Over 3.5 odds | 1.81 |
| Fair Under 3.5 odds | 2.23 |
| Fair Over 4.5 odds | 2.84 |
| Fair Under 4.5 odds | 1.54 |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 39.7% |
| Raw p over 1 5 | 90.5% |
| Raw p under 3 5 | 44.8% |
| Raw p btts yes | 74.1% |
| P home draw | 62.6% |
| P draw away | 61.2% |
| P home away | 76.2% |
| Raw p home draw | 60.3% |
| Raw p draw away | 61.0% |
| Raw p home away | 78.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.50 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.73 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | +0.2% |
| Draw probability edge | -2.4% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +18.5% |
| Under 2.5 probability edge | -18.5% |
| Raw edge prob home | 0.0041 |
| Raw ev home | 0.0015 |
| Raw edge prob draw | -0.0490 |
| Raw ev draw | -0.2081 |
| Raw edge prob away | 0.0449 |
| Raw ev away | 0.1112 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **44.9%**. Expected goals are 1.29 for Valencia and 1.58 for Villarreal (2.88 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 54.8%; Under 3.5 goals: 67.4%; Double Chance 1X: 55.1%; Double Chance X2: 70.4%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 58.0%; BTTS No (at least one team does not score): 42.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.6% | 3.38 |
| Draw | 25.5% | 3.92 |
| Villarreal win | 44.9% | 2.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.29 |
| Villarreal expected goals | 1.58 |
| Expected total goals | 2.88 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 54.8% |
| Under 2.5 | 45.2% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.98% |
| 2 | 1-2 | 9.35% |
| 3 | 0-1 | 8.79% |
| 4 | 0-2 | 7.23% |
| 5 | 2-1 | 7.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.6% | 28.3% | 3.45 | +2.1% |
| Draw | 25.5% | 25.7% | 3.78 | -3.6% |
| Villarreal win | 44.9% | 45.9% | 2.17 | -2.6% |
| Over 2.5 | 54.8% | 55.6% | 1.78 | -2.4% |
| Under 2.5 | 45.2% | 44.4% | 2.20 | -0.6% |

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
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2935 |
| Dc lambda away | 1.5838 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.0% |
| P btts no | 42.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.61 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.66 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.08 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 30.9% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 43.9% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 67.5% |
| Raw p btts yes | 58.0% |
| P home draw | 55.1% |
| P draw away | 70.4% |
| P home away | 74.5% |
| Raw p home draw | 56.1% |
| Raw p draw away | 69.1% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.36 |
| Reference draw odds | 3.68 |
| Reference away odds | 2.11 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | +1.3% |
| Draw probability edge | -0.2% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -0.7% |
| Under 2.5 probability edge | +0.7% |
| Raw edge prob home | 0.0258 |
| Raw ev home | 0.0655 |
| Raw edge prob draw | -0.0048 |
| Raw ev draw | -0.0450 |
| Raw edge prob away | -0.0210 |
| Raw ev away | -0.0484 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **54.6%**. Expected goals are 1.20 for Athletic Bilbao and 0.61 for Getafe (1.81 combined). The most likely exact score is 1-0 at 21.0%. Goal-market probabilities: at least one goal: 85.3%; Over 2.5 goals: 28.4%; Under 3.5 goals: 88.7%; Double Chance 1X: 82.3%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 96.1%; BTTS Yes (both teams score): 31.4%; BTTS No (at least one team does not score): 68.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 54.6% | 1.83 |
| Draw | 27.6% | 3.62 |
| Getafe win | 17.7% | 5.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.20 |
| Getafe expected goals | 0.61 |
| Expected total goals | 1.81 |
| Over 0.5 | 85.3% |
| Under 0.5 | 14.7% |
| Over 1.5 | 55.0% |
| Under 1.5 | 45.0% |
| Over 2.5 | 28.4% |
| Under 2.5 | 71.6% |
| Over 3.5 | 11.3% |
| Under 3.5 | 88.7% |
| Over 4.5 | 3.9% |
| Under 4.5 | 96.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 21.05% |
| 2 | 0-0 | 14.69% |
| 3 | 2-0 | 12.85% |
| 4 | 1-1 | 10.84% |
| 5 | 0-1 | 9.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 54.6% | 59.2% | 1.70 | -7.1% |
| Draw | 27.6% | 23.8% | 4.04 | +11.6% |
| Getafe win | 17.7% | 17.0% | 5.60 | -0.7% |
| Over 2.5 | 28.4% | 43.0% | 2.27 | -35.5% |
| Under 2.5 | 71.6% | 57.0% | 1.74 | +24.6% |

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
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1993 |
| Dc lambda away | 0.6104 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 31.4% |
| P btts no | 68.6% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.81 |
| Fair Over 1.5 odds | 1.82 |
| Fair Under 1.5 odds | 2.22 |
| Fair Over 2.5 odds | 3.52 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.83 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 25.52 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 50.1% |
| Unadjusted draw probability | 31.4% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 54.4% |
| Raw p under 3 5 | 89.0% |
| Raw p btts yes | 32.3% |
| P home draw | 82.3% |
| P draw away | 45.4% |
| P home away | 72.4% |
| Raw p home draw | 81.5% |
| Raw p draw away | 49.9% |
| Raw p home away | 68.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.65 |
| Reference draw odds | 3.94 |
| Reference away odds | 5.45 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.69 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | -4.6% |
| Draw probability edge | +3.8% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -14.6% |
| Under 2.5 probability edge | +14.6% |
| Raw edge prob home | -0.0916 |
| Raw ev home | -0.1489 |
| Raw edge prob draw | 0.0761 |
| Raw ev draw | 0.2697 |
| Raw edge prob away | 0.0155 |
| Raw ev away | 0.0366 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **58.8%**. Expected goals are 2.08 for Barcelona and 1.43 for Real Madrid (3.51 combined). The most likely exact score is 2-1 at 10.4%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 68.9%; Under 3.5 goals: 53.0%; Double Chance 1X: 78.3%; Double Chance X2: 41.2%; Double Chance 12 (either team wins): 80.5%; Under 4.5 goals: 71.7%; BTTS Yes (both teams score): 66.1%; BTTS No (at least one team does not score): 33.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 58.8% | 1.70 |
| Draw | 19.5% | 5.12 |
| Real Madrid win | 21.7% | 4.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.08 |
| Real Madrid expected goals | 1.43 |
| Expected total goals | 3.51 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 87.0% |
| Under 1.5 | 13.0% |
| Over 2.5 | 68.9% |
| Under 2.5 | 31.1% |
| Over 3.5 | 47.0% |
| Under 3.5 | 53.0% |
| Over 4.5 | 28.3% |
| Under 4.5 | 71.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.41% |
| 2 | 1-1 | 8.26% |
| 3 | 2-0 | 7.27% |
| 4 | 3-1 | 7.21% |
| 5 | 1-0 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 58.8% | 65.4% | 1.54 | -9.5% |
| Draw | 19.5% | 17.4% | 5.44 | +6.3% |
| Real Madrid win | 21.7% | 17.2% | 5.49 | +19.1% |

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
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0760 |
| Dc lambda away | 1.4328 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 66.1% |
| P btts no | 33.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.13 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.70 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.22 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.89 |
| Fair Over 4.5 odds | 3.54 |
| Fair Under 4.5 odds | 1.39 |
| Unadjusted home-win probability | 52.1% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 26.2% |
| Raw p over 1 5 | 86.8% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 66.8% |
| P home draw | 78.3% |
| P draw away | 41.2% |
| P home away | 80.5% |
| Raw p home draw | 73.8% |
| Raw p draw away | 47.9% |
| Raw p home away | 78.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.50 |
| Reference draw odds | 5.30 |
| Reference away odds | 5.35 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.23 |
| Reference Under 2.5 odds | 4.23 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:30Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:30Z |
| Home probability edge | -6.6% |
| Draw probability edge | +2.1% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | -0.1322 |
| Raw ev home | -0.1969 |
| Raw edge prob draw | 0.0428 |
| Raw ev draw | 0.1794 |
| Raw edge prob away | 0.0894 |
| Raw ev away | 0.4369 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **38.3%**. Expected goals are 1.49 for Celta Vigo and 1.31 for Real Betis (2.80 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 52.8%; Under 3.5 goals: 69.3%; Double Chance 1X: 64.9%; Double Chance X2: 61.7%; Double Chance 12 (either team wins): 73.4%; Under 4.5 goals: 84.9%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 38.3% | 2.61 |
| Draw | 26.6% | 3.76 |
| Real Betis win | 35.1% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.49 |
| Real Betis expected goals | 1.31 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 52.8% |
| Under 2.5 | 47.2% |
| Over 3.5 | 30.7% |
| Under 3.5 | 69.3% |
| Over 4.5 | 15.1% |
| Under 4.5 | 84.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.57% |
| 2 | 1-2 | 8.25% |
| 3 | 2-1 | 8.25% |
| 4 | 1-0 | 8.13% |
| 5 | 0-1 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 38.3% | 35.6% | 2.77 | +6.2% |
| Draw | 26.6% | 27.4% | 3.57 | -5.0% |
| Real Betis win | 35.1% | 37.0% | 2.67 | -6.4% |
| Over 2.5 | 52.8% | 51.7% | 1.91 | +0.8% |
| Under 2.5 | 47.2% | 48.3% | 2.03 | -4.1% |

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
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4879 |
| Dc lambda away | 1.3115 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.12 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.26 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.62 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 41.1% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 33.1% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 56.9% |
| P home draw | 64.9% |
| P draw away | 61.7% |
| P home away | 73.4% |
| Raw p home draw | 66.9% |
| Raw p draw away | 58.9% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.70 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | +2.7% |
| Draw probability edge | -0.7% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | 0.0545 |
| Raw ev home | 0.1375 |
| Raw edge prob draw | -0.0149 |
| Raw ev draw | -0.0768 |
| Raw edge prob away | -0.0396 |
| Raw ev away | -0.1169 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **54.8%**. Expected goals are 1.87 for Real Sociedad and 1.20 for Levante (3.07 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 59.4%; Under 3.5 goals: 63.0%; Double Chance 1X: 77.7%; Double Chance X2: 45.2%; Double Chance 12 (either team wins): 77.1%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 59.3%; BTTS No (at least one team does not score): 40.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 54.8% | 1.82 |
| Draw | 22.9% | 4.36 |
| Levante win | 22.3% | 4.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.87 |
| Levante expected goals | 1.20 |
| Expected total goals | 3.07 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.59% |
| 2 | 2-1 | 10.15% |
| 3 | 1-0 | 8.72% |
| 4 | 2-0 | 8.43% |
| 5 | 3-1 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 54.8% | 57.1% | 1.76 | -3.5% |
| Draw | 22.9% | 22.6% | 4.26 | -2.4% |
| Levante win | 22.3% | 20.3% | 4.72 | +5.1% |
| Over 2.5 | 59.4% | 58.1% | 1.71 | +1.6% |
| Under 2.5 | 40.6% | 41.9% | 2.32 | -5.9% |

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
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8661 |
| Dc lambda away | 1.2046 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.3% |
| P btts no | 40.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.51 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.42 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.05 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 52.5% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 81.4% |
| Raw p under 3 5 | 63.1% |
| Raw p btts yes | 59.5% |
| P home draw | 77.7% |
| P draw away | 45.2% |
| P home away | 77.1% |
| Raw p home draw | 75.8% |
| Raw p draw away | 47.5% |
| Raw p home away | 76.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.71 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | -2.3% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +1.4% |
| Under 2.5 probability edge | -1.4% |
| Raw edge prob home | -0.0454 |
| Raw ev home | -0.0752 |
| Raw edge prob draw | 0.0061 |
| Raw ev draw | -0.0108 |
| Raw edge prob away | 0.0393 |
| Raw ev away | 0.1438 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **47.9%**. Expected goals are 1.55 for Sevilla and 1.13 for CA Osasuna (2.68 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 50.0%; Under 3.5 goals: 71.8%; Double Chance 1X: 74.4%; Double Chance X2: 52.1%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 53.8%; BTTS No (at least one team does not score): 46.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 47.9% | 2.09 |
| Draw | 26.5% | 3.77 |
| CA Osasuna win | 25.6% | 3.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.55 |
| CA Osasuna expected goals | 1.13 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 50.0% |
| Under 2.5 | 50.0% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.63% |
| 2 | 1-0 | 10.56% |
| 3 | 2-1 | 9.58% |
| 4 | 2-0 | 8.44% |
| 5 | 0-0 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 47.9% | 49.3% | 2.02 | -3.3% |
| Draw | 26.5% | 27.1% | 3.60 | -4.4% |
| CA Osasuna win | 25.6% | 23.6% | 4.11 | +5.1% |
| Over 2.5 | 50.0% | 44.7% | 2.19 | +9.6% |
| Under 2.5 | 50.0% | 55.3% | 1.79 | -10.6% |

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
| Market best home last update utc | 2026-10-18T08:35:08Z |
| Market best draw last update utc | 2026-10-18T08:35:08Z |
| Market best away last update utc | 2026-10-18T08:35:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.5458 |
| Dc lambda away | 1.1349 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:35:54.071035+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.8% |
| P btts no | 46.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.60 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.47 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 46.4% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 53.7% |
| P home draw | 74.4% |
| P draw away | 52.1% |
| P home away | 73.5% |
| Raw p home draw | 72.4% |
| Raw p draw away | 53.6% |
| Raw p home away | 74.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.97 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:53Z |
| Market reference home last update utc | 2026-10-18T08:35:53Z |
| Market reference draw last update utc | 2026-10-18T08:35:53Z |
| Market reference away last update utc | 2026-10-18T08:35:53Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:53Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:08Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:08Z |
| Home probability edge | -1.4% |
| Draw probability edge | -0.6% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +5.3% |
| Under 2.5 probability edge | -5.3% |
| Raw edge prob home | -0.0289 |
| Raw ev home | -0.0620 |
| Raw edge prob draw | -0.0111 |
| Raw ev draw | -0.0644 |
| Raw edge prob away | 0.0400 |
| Raw ev away | 0.1333 |

</details>


---
