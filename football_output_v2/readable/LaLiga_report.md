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
| Training sha256 | dd0a3492e0e34113febb071c360185f56a9bd5ae879331fbafe0e82847d46971 |
| Training as of utc | 2026-10-18T11:56:55.150173+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 83, 'bbs_added_results': 5, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 83, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T11:56:55.150173+00:00', 'observations': 97, 'observations_sha256': '0718e1ca9a242ccbcd438a2ed7a7e4114300226c2ff33980426c06842d97102d', 'eligible_training_matches': 41, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 69, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 4, 'retrospective_eligible_training_matches': 41, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '2fb2a3551ebba0e1748b88759b7124e0d6de36819e8118ca2ff1e6e13649b77d', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 2001.687 |
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
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261018T115655150173Z_363edff488e458d545b1f2980db96a242a884a7637e0976a383554adc09f474c.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
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

The model's most likely 1X2 outcome is **CA Osasuna win** at **55.8%**. Expected goals are 2.78 for CA Osasuna and 1.56 for Real Racing Club de Santander (4.34 combined). The most likely exact score is 2-2 at 7.6%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.4%; Under 3.5 goals: 37.7%; Double Chance 1X: 77.4%; Double Chance X2: 44.2%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 57.6%; BTTS Yes (both teams score): 75.5%; BTTS No (at least one team does not score): 24.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 55.8% | 1.79 |
| Draw | 21.6% | 4.63 |
| Real Racing Club de Santander win | 22.6% | 4.42 |

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
| Over 2.5 | 79.4% |
| Under 2.5 | 20.6% |
| Over 3.5 | 62.3% |
| Under 3.5 | 37.7% |
| Over 4.5 | 42.4% |
| Under 4.5 | 57.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.65% |
| 2 | 1-1 | 7.25% |
| 3 | 2-1 | 6.96% |
| 4 | 3-1 | 6.45% |
| 5 | 1-2 | 5.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 55.8% | 48.6% | 1.95 | +8.8% |
| Draw | 21.6% | 25.9% | 3.76 | -18.8% |
| Real Racing Club de Santander win | 22.6% | 25.5% | 3.80 | -14.0% |
| Over 2.5 | 79.4% | 58.5% | 1.67 | +32.7% |
| Under 2.5 | 20.6% | 41.5% | 2.20 | -54.8% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
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
| Dc lambda away | 1.5624 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 75.5% |
| P btts no | 24.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 54.73 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 14.21 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.86 |
| Fair Over 3.5 odds | 1.60 |
| Fair Under 3.5 odds | 2.65 |
| Fair Over 4.5 odds | 2.36 |
| Fair Under 4.5 odds | 1.74 |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 17.3% |
| Unadjusted away-win probability | 19.7% |
| Raw p over 1 5 | 93.2% |
| Raw p under 3 5 | 37.0% |
| Raw p btts yes | 74.3% |
| P home draw | 77.4% |
| P draw away | 44.2% |
| P home away | 78.4% |
| Raw p home draw | 80.3% |
| Raw p draw away | 37.1% |
| Raw p home away | 82.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.01 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.75 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:57Z |
| Market reference home last update utc | 2026-10-18T11:56:57Z |
| Market reference draw last update utc | 2026-10-18T11:56:57Z |
| Market reference away last update utc | 2026-10-18T11:56:57Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | +7.2% |
| Draw probability edge | -4.3% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | +21.0% |
| Under 2.5 probability edge | -21.0% |
| Raw edge prob home | 0.1432 |
| Raw ev home | 0.2272 |
| Raw edge prob draw | -0.0853 |
| Raw ev draw | -0.3479 |
| Raw edge prob away | -0.0579 |
| Raw ev away | -0.2504 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **46.0%**. Expected goals are 1.49 for Celta Vigo and 0.95 for Alavés (2.44 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 43.3%; Under 3.5 goals: 77.3%; Double Chance 1X: 74.7%; Double Chance X2: 54.0%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 48.4%; BTTS No (at least one team does not score): 51.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 46.0% | 2.17 |
| Draw | 28.7% | 3.49 |
| Alavés win | 25.3% | 3.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.49 |
| Alavés expected goals | 0.95 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 43.3% |
| Under 2.5 | 56.7% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.54% |
| 2 | 1-0 | 11.75% |
| 3 | 0-0 | 9.68% |
| 4 | 2-0 | 9.02% |
| 5 | 2-1 | 8.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 46.0% | 42.5% | 2.37 | +9.1% |
| Draw | 28.7% | 30.5% | 3.23 | -7.4% |
| Alavés win | 25.3% | 27.0% | 3.51 | -11.1% |
| Over 2.5 | 43.3% | 35.6% | 2.54 | +10.1% |
| Under 2.5 | 56.7% | 64.4% | 1.61 | -8.8% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4927 |
| Dc lambda away | 0.9475 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.33 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.31 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.15 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.5% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.4% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 47.8% |
| P home draw | 74.7% |
| P draw away | 54.0% |
| P home away | 71.3% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.29 |
| Reference draw odds | 3.16 |
| Reference away odds | 3.55 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:57Z |
| Market reference home last update utc | 2026-10-18T11:56:57Z |
| Market reference draw last update utc | 2026-10-18T11:56:57Z |
| Market reference away last update utc | 2026-10-18T11:56:57Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 2.32 |
| Reference Under 2.5 odds | 1.43 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | +3.5% |
| Draw probability edge | -1.8% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | +7.8% |
| Under 2.5 probability edge | -7.8% |
| Raw edge prob home | 0.0703 |
| Raw ev home | 0.1738 |
| Raw edge prob draw | -0.0362 |
| Raw ev draw | -0.1324 |
| Raw edge prob away | -0.0341 |
| Raw ev away | -0.1713 |
| Market p home draw | 72.7% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:56:33Z |
| Market reference home draw last update utc | 2026-10-18T11:56:51Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.2% |
| Market draw away odds | 1.66 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:56:33Z |
| Market reference draw away last update utc | 2026-10-18T11:56:51Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.1% |
| Market home away odds | 1.40 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:56:33Z |
| Market reference home away last update utc | 2026-10-18T11:56:51Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.66 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.40 |
| Market p over 1 5 | 64.1% |
| Market reference over 1 5 odds | 1.52 |
| Market reference over 1 5 opposite odds | 2.62 |
| Market reference over 1 5 last update utc | 2026-10-18T11:56:51Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 82.4% |
| Market reference under 3 5 odds | 1.20 |
| Market reference under 3 5 opposite odds | 5.10 |
| Market reference under 3 5 last update utc | 2026-10-18T11:56:36Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 46.0% |
| Market btts yes odds | 2.02 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:56:33Z |
| Market reference btts yes odds | 2.16 |
| Market reference btts yes opposite odds | 1.84 |
| Market reference btts yes last update utc | 2026-10-18T11:56:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **47.3%**. Expected goals are 0.63 for Málaga and 1.28 for Real Sociedad (1.92 combined). The most likely exact score is 0-1 at 16.9%. Goal-market probabilities: at least one goal: 85.7%; Over 2.5 goals: 30.1%; Under 3.5 goals: 87.5%; Double Chance 1X: 52.7%; Double Chance X2: 75.8%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 95.5%; BTTS Yes (both teams score): 34.0%; BTTS No (at least one team does not score): 66.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 24.2% | 4.13 |
| Draw | 28.4% | 3.52 |
| Real Sociedad win | 47.3% | 2.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.28 |
| Expected total goals | 1.92 |
| Over 0.5 | 85.7% |
| Under 0.5 | 14.3% |
| Over 1.5 | 56.8% |
| Under 1.5 | 43.2% |
| Over 2.5 | 30.1% |
| Under 2.5 | 69.9% |
| Over 3.5 | 12.5% |
| Under 3.5 | 87.5% |
| Over 4.5 | 4.5% |
| Under 4.5 | 95.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.89% |
| 2 | 0-0 | 14.28% |
| 3 | 1-0 | 12.07% |
| 4 | 1-1 | 11.65% |
| 5 | 0-2 | 11.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 24.2% | 30.5% | 3.31 | -19.8% |
| Draw | 28.4% | 26.9% | 3.67 | +4.4% |
| Real Sociedad win | 47.3% | 42.7% | 2.27 | +7.4% |
| Over 2.5 | 30.1% | 56.9% | 1.74 | -47.6% |
| Under 2.5 | 69.9% | 43.1% | 2.27 | +58.7% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
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
| Dc lambda home | 0.6324 |
| Dc lambda away | 1.2828 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 34.0% |
| P btts no | 66.0% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 7.00 |
| Fair Over 1.5 odds | 1.76 |
| Fair Under 1.5 odds | 2.31 |
| Fair Over 2.5 odds | 3.32 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 8.01 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 22.30 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 18.0% |
| Unadjusted draw probability | 30.0% |
| Unadjusted away-win probability | 52.0% |
| Raw p over 1 5 | 57.4% |
| Raw p under 3 5 | 87.2% |
| Raw p btts yes | 34.2% |
| P home draw | 52.7% |
| P draw away | 75.8% |
| P home away | 71.6% |
| Raw p home draw | 48.0% |
| Raw p draw away | 82.0% |
| Raw p home away | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 3.16 |
| Reference draw odds | 3.57 |
| Reference away odds | 2.28 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:57Z |
| Market reference home last update utc | 2026-10-18T11:56:57Z |
| Market reference draw last update utc | 2026-10-18T11:56:57Z |
| Market reference away last update utc | 2026-10-18T11:56:57Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | -6.2% |
| Draw probability edge | +1.6% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -26.8% |
| Under 2.5 probability edge | +26.8% |
| Raw edge prob home | -0.1245 |
| Raw ev home | -0.4038 |
| Raw edge prob draw | 0.0317 |
| Raw ev draw | 0.1020 |
| Raw edge prob away | 0.0928 |
| Raw ev away | 0.1795 |
| Market p home draw | 57.9% |
| Market home draw odds | 1.71 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:56:33Z |
| Market reference home draw last update utc | 2026-10-18T11:56:57Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.0% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:56:33Z |
| Market reference draw away last update utc | 2026-10-18T11:56:57Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.1% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:56:33Z |
| Market reference home away last update utc | 2026-10-18T11:56:57Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home draw odds | 1.68 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-18T11:56:36Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.9% |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.63 |
| Market reference under 3 5 last update utc | 2026-10-18T11:56:51Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 62.7% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:56:33Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.56 |
| Market reference btts yes last update utc | 2026-10-18T11:56:57Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.2%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.8%; Under 3.5 goals: 56.2%; Double Chance 1X: 92.2%; Double Chance X2: 21.8%; Double Chance 12 (either team wins): 86.1%; Under 4.5 goals: 74.7%; BTTS Yes (both teams score): 48.7%; BTTS No (at least one team does not score): 51.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.2% | 1.28 |
| Draw | 13.9% | 7.17 |
| Sevilla win | 7.8% | 12.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.63 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.8% |
| Under 2.5 | 34.2% |
| Over 3.5 | 43.8% |
| Under 3.5 | 56.2% |
| Over 4.5 | 25.3% |
| Under 4.5 | 74.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.97% |
| 2 | 3-0 | 10.49% |
| 3 | 2-1 | 8.92% |
| 4 | 1-0 | 8.91% |
| 5 | 3-1 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 78.2% | 79.1% | 1.29 | +0.9% |
| Draw | 13.9% | 13.3% | 6.70 | -6.6% |
| Sevilla win | 7.8% | 7.6% | 10.90 | -14.7% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.6283 |
| Dc lambda away | 0.7450 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 48.7% |
| P btts no | 51.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.96 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.82 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
| Fair Over 3.5 odds | 2.28 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.96 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.6% |
| Unadjusted away-win probability | 8.0% |
| Raw p over 1 5 | 85.2% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 48.9% |
| P home draw | 92.2% |
| P draw away | 21.8% |
| P home away | 86.1% |
| Raw p home draw | 92.0% |
| Raw p draw away | 22.6% |
| Raw p home away | 85.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.25 |
| Reference draw odds | 6.85 |
| Reference away odds | 11.60 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:57Z |
| Market reference home last update utc | 2026-10-18T11:56:57Z |
| Market reference draw last update utc | 2026-10-18T11:56:57Z |
| Market reference away last update utc | 2026-10-18T11:56:57Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:34Z |
| Home probability edge | -0.9% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | -0.0175 |
| Raw ev home | -0.0021 |
| Raw edge prob draw | 0.0136 |
| Raw ev draw | -0.0203 |
| Raw edge prob away | 0.0039 |
| Raw ev away | -0.1259 |
| Market p home draw | 91.3% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:56:33Z |
| Market reference home draw last update utc | 2026-10-18T11:56:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.2% |
| Market draw away odds | 3.98 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:56:33Z |
| Market reference draw away last update utc | 2026-10-18T11:56:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.5% |
| Market home away odds | 1.14 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:56:33Z |
| Market reference home away last update utc | 2026-10-18T11:56:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.40 |
| Market reference dc home draw odds | 1.07 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 86.8% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-10-18T11:56:36Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 53.4% |
| Market reference under 3 5 odds | 1.81 |
| Market reference under 3 5 opposite odds | 2.06 |
| Market reference under 3 5 last update utc | 2026-10-18T11:56:51Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 51.8% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:56:33Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 2.06 |
| Market reference btts yes last update utc | 2026-10-18T11:56:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **34.4%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 19.0%. Goal-market probabilities: at least one goal: 81.0%; Over 2.5 goals: 23.1%; Under 3.5 goals: 91.5%; Double Chance 1X: 68.4%; Double Chance X2: 65.6%; Double Chance 12 (either team wins): 66.0%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 31.2%; BTTS No (at least one team does not score): 68.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 34.4% | 2.91 |
| Draw | 34.0% | 2.94 |
| Rayo Vallecano win | 31.6% | 3.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.0% |
| Under 0.5 | 19.0% |
| Over 1.5 | 49.3% |
| Under 1.5 | 50.7% |
| Over 2.5 | 23.1% |
| Under 2.5 | 76.9% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.96% |
| 2 | 0-1 | 15.91% |
| 3 | 1-0 | 15.88% |
| 4 | 1-1 | 12.80% |
| 5 | 2-0 | 7.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 34.4% | 31.7% | 2.98 | +2.4% |
| Draw | 34.0% | 32.7% | 3.17 | +7.8% |
| Rayo Vallecano win | 31.6% | 35.6% | 2.74 | -13.3% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
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
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 31.2% |
| P btts no | 68.8% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.27 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.33 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.79 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.78 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.1% |
| Unadjusted draw probability | 35.3% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.3% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.5% |
| P home draw | 68.4% |
| P draw away | 65.6% |
| P home away | 66.0% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.9% |
| Raw p home away | 64.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 3.05 |
| Reference draw odds | 2.96 |
| Reference away odds | 2.72 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:57Z |
| Market reference home last update utc | 2026-10-18T11:56:57Z |
| Market reference draw last update utc | 2026-10-18T11:56:57Z |
| Market reference away last update utc | 2026-10-18T11:56:57Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 2.32 |
| Reference Under 2.5 odds | 1.44 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Home probability edge | +2.7% |
| Draw probability edge | +1.3% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -12.8% |
| Under 2.5 probability edge | +12.8% |
| Raw edge prob home | 0.0537 |
| Raw ev home | 0.1042 |
| Raw edge prob draw | 0.0265 |
| Raw ev draw | 0.1196 |
| Raw edge prob away | -0.0802 |
| Raw ev away | -0.2430 |
| Market p home draw | 64.3% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:56:33Z |
| Market reference home draw last update utc | 2026-10-18T11:56:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.4% |
| Market draw away odds | 1.45 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:56:33Z |
| Market reference draw away last update utc | 2026-10-18T11:56:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 67.4% |
| Market home away odds | 1.41 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:56:33Z |
| Market reference home away last update utc | 2026-10-18T11:56:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home draw odds | 1.50 |
| Market reference dc home away odds | 1.43 |
| Market p over 1 5 | 63.7% |
| Market reference over 1 5 odds | 1.53 |
| Market reference over 1 5 opposite odds | 2.60 |
| Market reference over 1 5 last update utc | 2026-10-18T11:56:51Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 83.8% |
| Market reference under 3 5 odds | 1.18 |
| Market reference under 3 5 opposite odds | 5.50 |
| Market reference under 3 5 last update utc | 2026-10-18T11:56:36Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 45.7% |
| Market btts yes odds | 2.07 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:56:33Z |
| Market reference btts yes odds | 2.16 |
| Market reference btts yes opposite odds | 1.82 |
| Market reference btts yes last update utc | 2026-10-18T11:56:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.2%**. Expected goals are 1.27 for Levante and 1.36 for Athletic Bilbao (2.63 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 48.3%; Under 3.5 goals: 73.0%; Double Chance 1X: 58.8%; Double Chance X2: 69.9%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 54.2%; BTTS No (at least one team does not score): 45.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 30.1% | 3.32 |
| Draw | 28.7% | 3.48 |
| Athletic Bilbao win | 41.2% | 2.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.27 |
| Athletic Bilbao expected goals | 1.36 |
| Expected total goals | 2.63 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 48.3% |
| Under 2.5 | 51.7% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.69% |
| 2 | 0-1 | 10.04% |
| 3 | 1-2 | 9.00% |
| 4 | 0-0 | 8.09% |
| 5 | 1-0 | 7.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 30.1% | 25.9% | 3.52 | +6.0% |
| Draw | 28.7% | 30.6% | 3.52 | +1.2% |
| Athletic Bilbao win | 41.2% | 43.5% | 2.24 | -7.8% |
| Over 2.5 | 48.3% | 47.6% | 2.02 | -2.5% |
| Under 2.5 | 51.7% | 52.4% | 1.92 | -0.7% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
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
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.2% |
| P btts no | 45.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.36 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.87 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.70 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.01 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 34.3% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 38.8% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 73.0% |
| Raw p btts yes | 53.8% |
| P home draw | 58.8% |
| P draw away | 69.9% |
| P home away | 71.3% |
| Raw p home draw | 61.2% |
| Raw p draw away | 65.7% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.70 |
| Reference draw odds | 3.15 |
| Reference away odds | 2.24 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:54Z |
| Market reference home last update utc | 2026-10-18T11:56:54Z |
| Market reference draw last update utc | 2026-10-18T11:56:54Z |
| Market reference away last update utc | 2026-10-18T11:56:54Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.71 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | +4.2% |
| Draw probability edge | -1.8% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0838 |
| Raw ev home | 0.2070 |
| Raw edge prob draw | -0.0369 |
| Raw ev draw | -0.0529 |
| Raw edge prob away | -0.0469 |
| Raw ev away | -0.1308 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **56.9%**. Expected goals are 1.39 for Alavés and 0.44 for Málaga (1.84 combined). The most likely exact score is 1-0 at 20.6%. Goal-market probabilities: at least one goal: 84.1%; Over 2.5 goals: 27.6%; Under 3.5 goals: 88.9%; Double Chance 1X: 84.3%; Double Chance X2: 43.1%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 96.2%; BTTS Yes (both teams score): 27.2%; BTTS No (at least one team does not score): 72.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 56.9% | 1.76 |
| Draw | 27.4% | 3.65 |
| Málaga win | 15.7% | 6.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.39 |
| Málaga expected goals | 0.44 |
| Expected total goals | 1.84 |
| Over 0.5 | 84.1% |
| Under 0.5 | 15.9% |
| Over 1.5 | 54.2% |
| Under 1.5 | 45.8% |
| Over 2.5 | 27.6% |
| Under 2.5 | 72.4% |
| Over 3.5 | 11.1% |
| Under 3.5 | 88.9% |
| Over 4.5 | 3.8% |
| Under 4.5 | 96.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.57% |
| 2 | 0-0 | 15.89% |
| 3 | 2-0 | 14.52% |
| 4 | 1-1 | 9.92% |
| 5 | 0-1 | 9.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 56.9% | 53.2% | 1.89 | +7.5% |
| Draw | 27.4% | 26.8% | 3.73 | +2.2% |
| Málaga win | 15.7% | 20.0% | 4.57 | -28.3% |
| Over 2.5 | 27.6% | 46.6% | 2.07 | -42.8% |
| Under 2.5 | 72.4% | 53.4% | 1.88 | +36.1% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
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
| Dc lambda home | 1.3935 |
| Dc lambda away | 0.4432 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 27.2% |
| P btts no | 72.8% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.29 |
| Fair Over 1.5 odds | 1.84 |
| Fair Under 1.5 odds | 2.18 |
| Fair Over 2.5 odds | 3.62 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.00 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 26.25 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 60.6% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 55.1% |
| Raw p under 3 5 | 88.5% |
| Raw p btts yes | 27.2% |
| P home draw | 84.3% |
| P draw away | 43.1% |
| P home away | 72.6% |
| Raw p home draw | 88.6% |
| Raw p draw away | 39.4% |
| Raw p home away | 72.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.85 |
| Reference draw odds | 3.60 |
| Reference away odds | 4.80 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:54Z |
| Market reference home last update utc | 2026-10-18T11:56:54Z |
| Market reference draw last update utc | 2026-10-18T11:56:54Z |
| Market reference away last update utc | 2026-10-18T11:56:54Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.68 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | +3.7% |
| Draw probability edge | +0.6% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -19.0% |
| Under 2.5 probability edge | +19.0% |
| Raw edge prob home | 0.0745 |
| Raw ev home | 0.1457 |
| Raw edge prob draw | 0.0113 |
| Raw ev draw | 0.0434 |
| Raw edge prob away | -0.0857 |
| Raw ev away | -0.4787 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **72.7%**. Expected goals are 2.25 for Atlético Madrid and 0.90 for Deportivo La Coruña (3.15 combined). The most likely exact score is 2-0 at 11.7%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 62.0%; Under 3.5 goals: 60.7%; Double Chance 1X: 89.6%; Double Chance X2: 27.3%; Double Chance 12 (either team wins): 83.1%; Under 4.5 goals: 78.3%; BTTS Yes (both teams score): 52.4%; BTTS No (at least one team does not score): 47.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 72.7% | 1.37 |
| Draw | 16.9% | 5.93 |
| Deportivo La Coruña win | 10.4% | 9.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.25 |
| Deportivo La Coruña expected goals | 0.90 |
| Expected total goals | 3.15 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 62.0% |
| Under 2.5 | 38.0% |
| Over 3.5 | 39.3% |
| Under 3.5 | 60.7% |
| Over 4.5 | 21.7% |
| Under 4.5 | 78.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.68% |
| 2 | 2-1 | 10.50% |
| 3 | 1-0 | 10.13% |
| 4 | 3-0 | 8.75% |
| 5 | 1-1 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 72.7% | 77.8% | 1.27 | -7.6% |
| Draw | 16.9% | 14.7% | 6.46 | +9.0% |
| Deportivo La Coruña win | 10.4% | 7.4% | 13.10 | +36.2% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2468 |
| Dc lambda away | 0.8989 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 52.4% |
| P btts no | 47.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.73 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.89 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.62 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 67.6% |
| Unadjusted draw probability | 19.0% |
| Unadjusted away-win probability | 13.4% |
| Raw p over 1 5 | 82.4% |
| Raw p under 3 5 | 61.5% |
| Raw p btts yes | 53.3% |
| P home draw | 89.6% |
| P draw away | 27.3% |
| P home away | 83.1% |
| Raw p home draw | 86.6% |
| Raw p draw away | 32.4% |
| Raw p home away | 81.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.28 |
| Reference draw odds | 6.60 |
| Reference away odds | 13.00 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:54Z |
| Market reference home last update utc | 2026-10-18T11:56:54Z |
| Market reference draw last update utc | 2026-10-18T11:56:54Z |
| Market reference away last update utc | 2026-10-18T11:56:54Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.55 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:34Z |
| Home probability edge | -5.1% |
| Draw probability edge | +2.1% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | -0.1024 |
| Raw ev home | -0.1414 |
| Raw edge prob draw | 0.0427 |
| Raw ev draw | 0.2279 |
| Raw edge prob away | 0.0597 |
| Raw ev away | 0.7532 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **49.0%**. Expected goals are 1.35 for Rayo Vallecano and 1.04 for Elche CF (2.39 combined). The most likely exact score is 1-0 at 13.6%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 43.4%; Under 3.5 goals: 77.8%; Double Chance 1X: 75.7%; Double Chance X2: 51.0%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 90.3%; BTTS Yes (both teams score): 47.9%; BTTS No (at least one team does not score): 52.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 49.0% | 2.04 |
| Draw | 26.7% | 3.75 |
| Elche CF win | 24.3% | 4.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.35 |
| Elche CF expected goals | 1.04 |
| Expected total goals | 2.39 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 69.6% |
| Under 1.5 | 30.4% |
| Over 2.5 | 43.4% |
| Under 2.5 | 56.6% |
| Over 3.5 | 22.2% |
| Under 3.5 | 77.8% |
| Over 4.5 | 9.7% |
| Under 4.5 | 90.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.55% |
| 2 | 1-1 | 12.58% |
| 3 | 2-1 | 9.82% |
| 4 | 2-0 | 9.40% |
| 5 | 0-0 | 9.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 49.0% | 54.8% | 1.81 | -11.3% |
| Draw | 26.7% | 25.2% | 3.94 | +5.0% |
| Elche CF win | 24.3% | 20.0% | 4.78 | +16.3% |
| Over 2.5 | 43.4% | 53.4% | 1.88 | -18.5% |
| Under 2.5 | 56.6% | 46.6% | 2.07 | +17.2% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
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
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.9% |
| P btts no | 52.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.04 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.29 |
| Fair Over 2.5 odds | 2.31 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.51 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.35 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 28.7% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.1% |
| Raw p btts yes | 48.3% |
| P home draw | 75.7% |
| P draw away | 51.0% |
| P home away | 73.3% |
| Raw p home draw | 71.3% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.74 |
| Reference draw odds | 3.55 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:53Z |
| Market reference home last update utc | 2026-10-18T11:56:53Z |
| Market reference draw last update utc | 2026-10-18T11:56:53Z |
| Market reference away last update utc | 2026-10-18T11:56:53Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | -5.8% |
| Draw probability edge | +1.4% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | -0.1152 |
| Raw ev home | -0.2171 |
| Raw edge prob draw | 0.0285 |
| Raw ev draw | 0.1065 |
| Raw edge prob away | 0.0867 |
| Raw ev away | 0.3700 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **38.3%**. Expected goals are 1.96 for Real Racing Club de Santander and 1.97 for Espanyol (3.93 combined). The most likely exact score is 1-1 at 8.9%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 74.3%; Under 3.5 goals: 44.8%; Double Chance 1X: 62.5%; Double Chance X2: 61.7%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 64.9%; BTTS Yes (both teams score): 74.7%; BTTS No (at least one team does not score): 25.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 38.3% | 2.61 |
| Draw | 24.2% | 4.13 |
| Espanyol win | 37.5% | 2.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.96 |
| Espanyol expected goals | 1.97 |
| Expected total goals | 3.93 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 90.5% |
| Under 1.5 | 9.5% |
| Over 2.5 | 74.3% |
| Under 2.5 | 25.7% |
| Over 3.5 | 55.2% |
| Under 3.5 | 44.8% |
| Over 4.5 | 35.1% |
| Under 4.5 | 64.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.87% |
| 2 | 2-2 | 8.31% |
| 3 | 2-1 | 7.29% |
| 4 | 1-2 | 7.07% |
| 5 | 3-1 | 4.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 38.3% | 37.6% | 2.57 | -1.6% |
| Draw | 24.2% | 27.1% | 3.71 | -10.1% |
| Espanyol win | 37.5% | 35.3% | 2.80 | +4.9% |
| Over 2.5 | 74.3% | 57.6% | 1.77 | +31.5% |
| Under 2.5 | 25.7% | 42.4% | 2.22 | -43.0% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
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
| Dc lambda home | 1.9554 |
| Dc lambda away | 1.9732 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 74.7% |
| P btts no | 25.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.26 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.52 |
| Fair Over 2.5 odds | 1.35 |
| Fair Under 2.5 odds | 3.89 |
| Fair Over 3.5 odds | 1.81 |
| Fair Under 3.5 odds | 2.23 |
| Fair Over 4.5 odds | 2.85 |
| Fair Under 4.5 odds | 1.54 |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 39.7% |
| Raw p over 1 5 | 90.5% |
| Raw p under 3 5 | 44.8% |
| Raw p btts yes | 74.1% |
| P home draw | 62.5% |
| P draw away | 61.7% |
| P home away | 75.8% |
| Raw p home draw | 60.3% |
| Raw p draw away | 61.0% |
| Raw p home away | 78.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.56 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.72 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:54Z |
| Market reference home last update utc | 2026-10-18T11:56:54Z |
| Market reference draw last update utc | 2026-10-18T11:56:54Z |
| Market reference away last update utc | 2026-10-18T11:56:54Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | +0.7% |
| Draw probability edge | -2.9% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +16.7% |
| Under 2.5 probability edge | -16.7% |
| Raw edge prob home | 0.0140 |
| Raw ev home | 0.0019 |
| Raw edge prob draw | -0.0579 |
| Raw ev draw | -0.2081 |
| Raw edge prob away | 0.0439 |
| Raw ev away | 0.1108 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **44.3%**. Expected goals are 1.29 for Valencia and 1.58 for Villarreal (2.88 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 54.8%; Under 3.5 goals: 67.5%; Double Chance 1X: 55.7%; Double Chance X2: 69.7%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 58.0%; BTTS No (at least one team does not score): 42.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.3% | 3.30 |
| Draw | 25.4% | 3.94 |
| Villarreal win | 44.3% | 2.26 |

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
| Over 3.5 | 32.5% |
| Under 3.5 | 67.5% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.93% |
| 2 | 1-2 | 9.23% |
| 3 | 0-1 | 8.67% |
| 4 | 2-1 | 7.32% |
| 5 | 0-2 | 7.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.3% | 29.7% | 3.45 | +4.5% |
| Draw | 25.4% | 25.5% | 3.78 | -4.0% |
| Villarreal win | 44.3% | 44.8% | 2.17 | -3.9% |
| Over 2.5 | 54.8% | 56.5% | 1.78 | -2.4% |
| Under 2.5 | 45.2% | 43.5% | 2.20 | -0.7% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
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
| Dc lambda home | 1.2936 |
| Dc lambda away | 1.5839 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.0% |
| P btts no | 42.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.69 |
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
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 67.5% |
| Raw p btts yes | 58.0% |
| P home draw | 55.7% |
| P draw away | 69.7% |
| P home away | 74.6% |
| Raw p home draw | 56.2% |
| Raw p draw away | 69.1% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.20 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.16 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:54Z |
| Market reference home last update utc | 2026-10-18T11:56:54Z |
| Market reference draw last update utc | 2026-10-18T11:56:54Z |
| Market reference away last update utc | 2026-10-18T11:56:54Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | +0.6% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | 0.0118 |
| Raw ev home | 0.0656 |
| Raw edge prob draw | -0.0026 |
| Raw ev draw | -0.0450 |
| Raw edge prob away | -0.0092 |
| Raw ev away | -0.0485 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **55.3%**. Expected goals are 1.20 for Athletic Bilbao and 0.61 for Getafe (1.81 combined). The most likely exact score is 1-0 at 21.3%. Goal-market probabilities: at least one goal: 85.4%; Over 2.5 goals: 28.5%; Under 3.5 goals: 88.6%; Double Chance 1X: 82.8%; Double Chance X2: 44.7%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 96.1%; BTTS Yes (both teams score): 31.4%; BTTS No (at least one team does not score): 68.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 55.3% | 1.81 |
| Draw | 27.5% | 3.64 |
| Getafe win | 17.2% | 5.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.20 |
| Getafe expected goals | 0.61 |
| Expected total goals | 1.81 |
| Over 0.5 | 85.4% |
| Under 0.5 | 14.6% |
| Over 1.5 | 55.1% |
| Under 1.5 | 44.9% |
| Over 2.5 | 28.5% |
| Under 2.5 | 71.5% |
| Over 3.5 | 11.4% |
| Under 3.5 | 88.6% |
| Over 4.5 | 3.9% |
| Under 4.5 | 96.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 21.30% |
| 2 | 0-0 | 14.61% |
| 3 | 2-0 | 13.00% |
| 4 | 1-1 | 10.78% |
| 5 | 0-1 | 8.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 55.3% | 60.5% | 1.70 | -6.0% |
| Draw | 27.5% | 23.5% | 4.04 | +11.0% |
| Getafe win | 17.2% | 16.0% | 5.60 | -3.5% |
| Over 2.5 | 28.5% | 41.4% | 2.27 | -35.3% |
| Under 2.5 | 71.5% | 58.6% | 1.74 | +24.4% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
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
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 31.4% |
| P btts no | 68.6% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.84 |
| Fair Over 1.5 odds | 1.81 |
| Fair Under 1.5 odds | 2.23 |
| Fair Over 2.5 odds | 3.51 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.80 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 25.41 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 50.1% |
| Unadjusted draw probability | 31.4% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 54.4% |
| Raw p under 3 5 | 89.0% |
| Raw p btts yes | 32.3% |
| P home draw | 82.8% |
| P draw away | 44.7% |
| P home away | 72.5% |
| Raw p home draw | 81.5% |
| Raw p draw away | 49.9% |
| Raw p home away | 68.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.61 |
| Reference draw odds | 3.95 |
| Reference away odds | 5.70 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:54Z |
| Market reference home last update utc | 2026-10-18T11:56:54Z |
| Market reference draw last update utc | 2026-10-18T11:56:54Z |
| Market reference away last update utc | 2026-10-18T11:56:54Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.56 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | -5.2% |
| Draw probability edge | +4.0% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -12.9% |
| Under 2.5 probability edge | +12.9% |
| Raw edge prob home | -0.1047 |
| Raw ev home | -0.1489 |
| Raw edge prob draw | 0.0793 |
| Raw ev draw | 0.2697 |
| Raw edge prob away | 0.0254 |
| Raw ev away | 0.0365 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **58.9%**. Expected goals are 2.08 for Barcelona and 1.43 for Real Madrid (3.51 combined). The most likely exact score is 2-1 at 10.4%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 69.2%; Under 3.5 goals: 53.0%; Double Chance 1X: 77.5%; Double Chance X2: 41.1%; Double Chance 12 (either team wins): 81.4%; Under 4.5 goals: 71.6%; BTTS Yes (both teams score): 65.9%; BTTS No (at least one team does not score): 34.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 58.9% | 1.70 |
| Draw | 18.6% | 5.38 |
| Real Madrid win | 22.5% | 4.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.08 |
| Real Madrid expected goals | 1.43 |
| Expected total goals | 3.51 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 87.0% |
| Under 1.5 | 13.0% |
| Over 2.5 | 69.2% |
| Under 2.5 | 30.8% |
| Over 3.5 | 47.0% |
| Under 3.5 | 53.0% |
| Over 4.5 | 28.4% |
| Under 4.5 | 71.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.43% |
| 2 | 1-1 | 7.85% |
| 3 | 2-0 | 7.28% |
| 4 | 3-1 | 7.22% |
| 5 | 1-0 | 6.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 58.9% | 65.6% | 1.54 | -9.3% |
| Draw | 18.6% | 15.5% | 5.44 | +1.1% |
| Real Madrid win | 22.5% | 18.9% | 5.49 | +23.7% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0761 |
| Dc lambda away | 1.4328 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 65.9% |
| P btts no | 34.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.89 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.70 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.25 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.89 |
| Fair Over 4.5 odds | 3.52 |
| Fair Under 4.5 odds | 1.40 |
| Unadjusted home-win probability | 52.2% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 26.2% |
| Raw p over 1 5 | 86.8% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 66.8% |
| P home draw | 77.5% |
| P draw away | 41.1% |
| P home away | 81.4% |
| Raw p home draw | 73.8% |
| Raw p draw away | 47.8% |
| Raw p home away | 78.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.51 |
| Reference draw odds | 6.20 |
| Reference away odds | 5.10 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:55Z |
| Market reference home last update utc | 2026-10-18T11:56:55Z |
| Market reference draw last update utc | 2026-10-18T11:56:55Z |
| Market reference away last update utc | 2026-10-18T11:56:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.15 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:34Z |
| Home probability edge | -6.7% |
| Draw probability edge | +3.1% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | -0.1346 |
| Raw ev home | -0.1969 |
| Raw edge prob draw | 0.0620 |
| Raw ev draw | 0.1794 |
| Raw edge prob away | 0.0727 |
| Raw ev away | 0.4367 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **37.5%**. Expected goals are 1.49 for Celta Vigo and 1.31 for Real Betis (2.80 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 52.8%; Under 3.5 goals: 69.3%; Double Chance 1X: 63.9%; Double Chance X2: 62.5%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 84.9%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 37.5% | 2.67 |
| Draw | 26.4% | 3.79 |
| Real Betis win | 36.1% | 2.77 |

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
| 1 | 1-1 | 12.48% |
| 2 | 1-2 | 8.49% |
| 3 | 0-1 | 8.33% |
| 4 | 2-1 | 8.07% |
| 5 | 1-0 | 7.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 37.5% | 34.0% | 2.77 | +3.9% |
| Draw | 26.4% | 27.0% | 3.57 | -5.7% |
| Real Betis win | 36.1% | 39.1% | 2.67 | -3.7% |
| Over 2.5 | 52.8% | 50.7% | 1.91 | +0.9% |
| Under 2.5 | 47.2% | 49.3% | 2.03 | -4.2% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
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
| Dc lambda away | 1.3116 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.23 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.26 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.61 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 41.1% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 33.1% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 56.9% |
| P home draw | 63.9% |
| P draw away | 62.5% |
| P home away | 73.6% |
| Raw p home draw | 66.9% |
| Raw p draw away | 58.9% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.84 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.48 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:54Z |
| Market reference home last update utc | 2026-10-18T11:56:54Z |
| Market reference draw last update utc | 2026-10-18T11:56:54Z |
| Market reference away last update utc | 2026-10-18T11:56:54Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 1.80 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | +3.6% |
| Draw probability edge | -0.6% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | 0.0710 |
| Raw ev home | 0.1375 |
| Raw edge prob draw | -0.0110 |
| Raw ev draw | -0.0768 |
| Raw edge prob away | -0.0600 |
| Raw ev away | -0.1169 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **54.0%**. Expected goals are 1.87 for Real Sociedad and 1.20 for Levante (3.07 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 59.3%; Under 3.5 goals: 63.0%; Double Chance 1X: 77.4%; Double Chance X2: 46.0%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 59.5%; BTTS No (at least one team does not score): 40.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 54.0% | 1.85 |
| Draw | 23.4% | 4.27 |
| Levante win | 22.6% | 4.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.87 |
| Levante expected goals | 1.20 |
| Expected total goals | 3.07 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 81.5% |
| Under 1.5 | 18.5% |
| Over 2.5 | 59.3% |
| Under 2.5 | 40.7% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.82% |
| 2 | 2-1 | 10.00% |
| 3 | 1-0 | 8.59% |
| 4 | 2-0 | 8.31% |
| 5 | 3-1 | 6.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 54.0% | 55.5% | 1.76 | -4.9% |
| Draw | 23.4% | 23.6% | 4.26 | -0.3% |
| Levante win | 22.6% | 20.9% | 4.72 | +6.5% |
| Over 2.5 | 59.3% | 61.6% | 1.71 | +1.3% |
| Under 2.5 | 40.7% | 38.4% | 2.32 | -5.5% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
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
| Dc lambda home | 1.8662 |
| Dc lambda away | 1.2045 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.5% |
| P btts no | 40.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.07 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.41 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.07 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 52.6% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 81.4% |
| Raw p under 3 5 | 63.1% |
| Raw p btts yes | 59.5% |
| P home draw | 77.4% |
| P draw away | 46.0% |
| P home away | 76.6% |
| Raw p home draw | 75.8% |
| Raw p draw away | 47.4% |
| Raw p home away | 76.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.76 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.50 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:55Z |
| Market reference home last update utc | 2026-10-18T11:56:55Z |
| Market reference draw last update utc | 2026-10-18T11:56:55Z |
| Market reference away last update utc | 2026-10-18T11:56:55Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | -1.5% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | -0.0295 |
| Raw ev home | -0.0751 |
| Raw edge prob draw | -0.0039 |
| Raw ev draw | -0.0109 |
| Raw edge prob away | 0.0334 |
| Raw ev away | 0.1436 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **47.8%**. Expected goals are 1.55 for Sevilla and 1.13 for CA Osasuna (2.68 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 50.0%; Under 3.5 goals: 71.8%; Double Chance 1X: 74.5%; Double Chance X2: 52.2%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 47.8% | 2.09 |
| Draw | 26.7% | 3.75 |
| CA Osasuna win | 25.5% | 3.92 |

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
| 1 | 1-1 | 12.70% |
| 2 | 1-0 | 10.55% |
| 3 | 2-1 | 9.57% |
| 4 | 2-0 | 8.43% |
| 5 | 0-0 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 47.8% | 49.2% | 2.02 | -3.4% |
| Draw | 26.7% | 27.4% | 3.60 | -4.0% |
| CA Osasuna win | 25.5% | 23.4% | 4.11 | +4.8% |
| Over 2.5 | 50.0% | 43.3% | 2.19 | +9.5% |
| Under 2.5 | 50.0% | 56.7% | 1.79 | -10.5% |

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
| Market best home last update utc | 2026-10-18T11:56:33Z |
| Market best draw last update utc | 2026-10-18T11:56:33Z |
| Market best away last update utc | 2026-10-18T11:56:33Z |
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
| Bbs statistics cutoff utc | 2026-10-18T11:56:55.150173+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.53 |
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
| P home draw | 74.5% |
| P draw away | 52.2% |
| P home away | 73.3% |
| Raw p home draw | 72.4% |
| Raw p draw away | 53.6% |
| Raw p home away | 74.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.97 |
| Reference draw odds | 3.45 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:55Z |
| Market reference home last update utc | 2026-10-18T11:56:55Z |
| Market reference draw last update utc | 2026-10-18T11:56:55Z |
| Market reference away last update utc | 2026-10-18T11:56:55Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.60 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:53Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:33Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:33Z |
| Home probability edge | -1.4% |
| Draw probability edge | -0.7% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +6.7% |
| Under 2.5 probability edge | -6.7% |
| Raw edge prob home | -0.0275 |
| Raw ev home | -0.0620 |
| Raw edge prob draw | -0.0138 |
| Raw ev draw | -0.0644 |
| Raw edge prob away | 0.0413 |
| Raw ev away | 0.1333 |

</details>


---
