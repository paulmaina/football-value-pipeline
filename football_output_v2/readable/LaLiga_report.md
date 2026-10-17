# La Liga — football model report

Fixtures in this report: **20**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,219 |
| Training data through | 2026-10-16 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | a32bcfcb0abd89d95f4fb6e942cb1d377383bf1fa987ec46f60f0411154b793c |
| Training as of utc | 2026-10-17T09:44:55.167943+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 79, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 79, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-17T09:44:55.167943+00:00', 'observations': 79, 'observations_sha256': '09ee652fb0801385b9b93d539e5236e3b3e94f2d69791645c860852e9e1dbc09', 'eligible_training_matches': 37, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 65, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 37, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '284e2ff5d85d84a188517479ca9d5434803aebacfdbda43e5fffd896faf93b32', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 1991.394 |
| Base scoring parameter | 0.087 |
| Home-advantage parameter | 0.282 |
| Dixon-Coles low-score adjustment | -0.023 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-16', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 10.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261017T094455167943Z_2aad77ff3cf467903bebbc6a5de598f2f5858d89eff9e115781b48045e3fcff9.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
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

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **53.6%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 0-1 at 12.2%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 48.9%; Under 3.5 goals: 73.1%; Double Chance 1X: 46.4%; Double Chance X2: 78.2%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 21.8% | 4.59 |
| Draw | 24.6% | 4.06 |
| Atlético Madrid win | 53.6% | 1.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.02 |
| Atlético Madrid expected goals | 1.59 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 74.0% |
| Under 1.5 | 26.0% |
| Over 2.5 | 48.9% |
| Under 2.5 | 51.1% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.17% |
| 2 | 1-1 | 11.71% |
| 3 | 1-2 | 10.13% |
| 4 | 0-2 | 9.88% |
| 5 | 0-0 | 7.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 21.8% | 19.3% | 4.98 | +8.5% |
| Draw | 24.6% | 23.6% | 4.12 | +1.4% |
| Atlético Madrid win | 53.6% | 57.1% | 1.75 | -6.2% |
| Over 2.5 | 48.9% | 55.3% | 1.79 | -12.4% |
| Under 2.5 | 51.1% | 44.7% | 2.19 | +11.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T12:00:00+00:00 |
| Fixture id | 6436925dd15916d7041ba32b60000d48 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:37Z |
| Market best draw last update utc | 2026-10-17T09:08:37Z |
| Market best away last update utc | 2026-10-17T09:08:37Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Espanol |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0248 |
| Dc lambda away | 1.5865 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.69 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.85 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.92 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.1% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.3% |
| P home draw | 46.4% |
| P draw away | 78.2% |
| P home away | 75.4% |
| Raw p home draw | 49.9% |
| Raw p draw away | 75.8% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.90 |
| Reference draw odds | 4.05 |
| Reference away odds | 1.72 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:37Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:37Z |
| Home probability edge | +2.4% |
| Draw probability edge | +1.0% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | 0.0487 |
| Raw ev home | 0.2060 |
| Raw edge prob draw | 0.0209 |
| Raw ev draw | 0.0567 |
| Raw edge prob away | -0.0696 |
| Raw ev away | -0.1226 |
| Market p home draw | 42.2% |
| Market home draw odds | 2.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:38Z |
| Market reference home draw last update utc | 2026-10-17T09:09:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.2% |
| Market draw away odds | 1.21 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:38Z |
| Market reference draw away last update utc | 2026-10-17T09:09:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.7% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:38Z |
| Market reference home away last update utc | 2026-10-17T09:09:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.20 |
| Market reference dc home draw odds | 2.31 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 80.0% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:23Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.8% |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:23Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 56.5% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:37Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-17T09:09:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **60.7%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.43 combined). The most likely exact score is 1-2 at 10.6%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.4%; Under 3.5 goals: 54.7%; Double Chance 1X: 39.3%; Double Chance X2: 80.2%; Double Chance 12 (either team wins): 80.5%; Under 4.5 goals: 73.3%; BTTS Yes (both teams score): 64.3%; BTTS No (at least one team does not score): 35.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.8% | 5.05 |
| Draw | 19.5% | 5.14 |
| Barcelona win | 60.7% | 1.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.35 |
| Barcelona expected goals | 2.07 |
| Expected total goals | 3.43 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 45.3% |
| Under 3.5 | 54.7% |
| Over 4.5 | 26.7% |
| Under 4.5 | 73.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.65% |
| 2 | 1-1 | 8.42% |
| 3 | 0-2 | 7.88% |
| 4 | 1-3 | 7.36% |
| 5 | 0-1 | 7.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.8% | 15.1% | 6.29 | +24.6% |
| Draw | 19.5% | 17.4% | 5.48 | +6.7% |
| Barcelona win | 60.7% | 67.5% | 1.48 | -10.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | 846e496fc232b2fc20214754836727d0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3520 |
| Dc lambda away | 2.0745 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.3% |
| P btts no | 35.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.03 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.21 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.74 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 55.3% |
| Raw p btts yes | 65.0% |
| P home draw | 39.3% |
| P draw away | 80.2% |
| P home away | 80.5% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.5% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 6.20 |
| Reference draw odds | 5.40 |
| Reference away odds | 1.46 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.20 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | +4.7% |
| Draw probability edge | +2.1% |
| Away probability edge | -6.8% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | 0.0947 |
| Raw ev home | 0.5433 |
| Raw edge prob draw | 0.0416 |
| Raw ev draw | 0.1810 |
| Raw edge prob away | -0.1362 |
| Raw ev away | -0.2021 |
| Market p home draw | 33.3% |
| Market home draw odds | 2.85 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:38Z |
| Market reference home draw last update utc | 2026-10-17T09:09:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.4% |
| Market draw away odds | 1.14 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:38Z |
| Market reference draw away last update utc | 2026-10-17T09:09:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.4% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:38Z |
| Market reference home away last update utc | 2026-10-17T09:09:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.17 |
| Market reference dc home draw odds | 2.93 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 93.4% |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 10.00 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:23Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 39.1% |
| Market reference under 3 5 odds | 2.26 |
| Market reference under 3 5 opposite odds | 1.54 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:23Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 72.2% |
| Market btts yes odds | 1.32 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:38Z |
| Market reference btts yes odds | 1.36 |
| Market reference btts yes opposite odds | 3.36 |
| Market reference btts yes last update utc | 2026-10-17T09:09:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **39.9%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 89.2%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.1%; Double Chance 1X: 60.1%; Double Chance X2: 68.9%; Double Chance 12 (either team wins): 71.1%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.6%; BTTS No (at least one team does not score): 54.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 31.1% | 3.21 |
| Draw | 28.9% | 3.46 |
| Athletic Bilbao win | 39.9% | 2.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.07 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.2% |
| Under 0.5 | 10.8% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.9% |
| Under 3.5 | 81.1% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.43% |
| 2 | 0-1 | 12.84% |
| 3 | 0-0 | 10.76% |
| 4 | 1-0 | 10.48% |
| 5 | 1-2 | 8.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 31.1% | 29.2% | 3.35 | +4.3% |
| Draw | 28.9% | 28.5% | 3.43 | -0.7% |
| Athletic Bilbao win | 39.9% | 42.2% | 2.35 | -6.2% |
| Over 2.5 | 39.0% | 45.4% | 2.15 | -16.1% |
| Under 2.5 | 61.0% | 54.6% | 1.81 | +10.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T19:00:00+00:00 |
| Fixture id | f00cd1ea41fa39149729d14ebc07aa6c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0748 |
| Dc lambda away | 1.1675 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.6% |
| P btts no | 54.4% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.29 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.28 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.89 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.0% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 65.9% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 45.7% |
| P home draw | 60.1% |
| P draw away | 68.9% |
| P home away | 71.1% |
| Raw p home draw | 62.4% |
| Raw p draw away | 67.0% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.26 |
| Reference draw odds | 3.34 |
| Reference away odds | 2.29 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.09 |
| Reference Under 2.5 odds | 1.76 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:38Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:38Z |
| Home probability edge | +1.9% |
| Draw probability edge | +0.4% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.0376 |
| Raw ev home | 0.1057 |
| Raw edge prob draw | 0.0084 |
| Raw ev draw | 0.0071 |
| Raw edge prob away | -0.0460 |
| Raw ev away | -0.1157 |
| Market p home draw | 57.8% |
| Market home draw odds | 1.67 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:38Z |
| Market reference home draw last update utc | 2026-10-17T09:09:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.4% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:38Z |
| Market reference draw away last update utc | 2026-10-17T09:09:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.9% |
| Market home away odds | 1.36 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:38Z |
| Market reference home away last update utc | 2026-10-17T09:09:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home draw odds | 1.68 |
| Market reference dc home away odds | 1.37 |
| Market p over 1 5 | 71.3% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:08:16Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 3.10 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.8% |
| Market under 3 5 odds | 1.23 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:08:16Z |
| Market reference under 3 5 odds | 1.25 |
| Market reference under 3 5 opposite odds | 3.45 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:23Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 51.5% |
| Market btts yes odds | 1.80 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:38Z |
| Market reference btts yes odds | 1.88 |
| Market reference btts yes opposite odds | 1.99 |
| Market reference btts yes last update utc | 2026-10-17T09:09:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **66.8%**. Expected goals are 2.42 for Villarreal and 1.19 for Elche CF (3.61 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 70.1%; Under 3.5 goals: 51.0%; Double Chance 1X: 85.1%; Double Chance X2: 33.2%; Double Chance 12 (either team wins): 81.7%; Under 4.5 goals: 70.2%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 66.8% | 1.50 |
| Draw | 18.3% | 5.47 |
| Elche CF win | 14.9% | 6.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.42 |
| Elche CF expected goals | 1.19 |
| Expected total goals | 3.61 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 87.9% |
| Under 1.5 | 12.1% |
| Over 2.5 | 70.1% |
| Under 2.5 | 29.9% |
| Over 3.5 | 49.0% |
| Under 3.5 | 51.0% |
| Over 4.5 | 29.8% |
| Under 4.5 | 70.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.77% |
| 2 | 2-0 | 8.23% |
| 3 | 3-1 | 7.89% |
| 4 | 1-1 | 7.83% |
| 5 | 3-0 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 66.8% | 69.1% | 1.46 | -2.5% |
| Draw | 18.3% | 18.0% | 5.24 | -4.2% |
| Elche CF win | 14.9% | 12.9% | 7.19 | +7.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:15:00+00:00 |
| Fixture id | aef660734585649651415961a9d177c6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4220 |
| Dc lambda away | 1.1877 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.28 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.25 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.35 |
| Fair Over 3.5 odds | 2.04 |
| Fair Under 3.5 odds | 1.96 |
| Fair Over 4.5 odds | 3.36 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 64.4% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 87.7% |
| Raw p under 3 5 | 51.3% |
| Raw p btts yes | 63.5% |
| P home draw | 85.1% |
| P draw away | 33.2% |
| P home away | 81.7% |
| Raw p home draw | 83.0% |
| Raw p draw away | 35.6% |
| Raw p home away | 81.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.42 |
| Reference draw odds | 5.10 |
| Reference away odds | 7.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | -2.4% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | -0.0473 |
| Raw ev home | -0.0597 |
| Raw edge prob draw | 0.0060 |
| Raw ev draw | -0.0259 |
| Raw edge prob away | 0.0412 |
| Raw ev away | 0.2229 |
| Market p home draw | 85.7% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:38Z |
| Market reference home draw last update utc | 2026-10-17T09:09:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 32.2% |
| Market draw away odds | 2.94 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:38Z |
| Market reference draw away last update utc | 2026-10-17T09:09:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.1% |
| Market home away odds | 1.20 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:38Z |
| Market reference home away last update utc | 2026-10-17T09:09:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.03 |
| Market reference dc home draw odds | 1.14 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 88.3% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:23Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 53.9% |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 1.97 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:23Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 60.6% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:38Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.43 |
| Market reference btts yes last update utc | 2026-10-17T09:09:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **56.1%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.32 combined). The most likely exact score is 2-2 at 7.6%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.2%; Under 3.5 goals: 38.0%; Double Chance 1X: 77.5%; Double Chance X2: 43.9%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 58.0%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 56.1% | 1.78 |
| Draw | 21.5% | 4.66 |
| Real Racing Club de Santander win | 22.5% | 4.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 2.78 |
| Real Racing Club de Santander expected goals | 1.55 |
| Expected total goals | 4.32 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 92.8% |
| Under 1.5 | 7.2% |
| Over 2.5 | 79.2% |
| Under 2.5 | 20.8% |
| Over 3.5 | 62.0% |
| Under 3.5 | 38.0% |
| Over 4.5 | 42.0% |
| Under 4.5 | 58.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.62% |
| 2 | 1-1 | 7.25% |
| 3 | 2-1 | 7.00% |
| 4 | 3-1 | 6.48% |
| 5 | 1-2 | 5.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 56.1% | 48.8% | 2.04 | +14.3% |
| Draw | 21.5% | 25.7% | 3.78 | -18.8% |
| Real Racing Club de Santander win | 22.5% | 25.4% | 3.82 | -14.2% |
| Over 2.5 | 79.2% | 59.2% | 1.68 | +33.1% |
| Under 2.5 | 20.8% | 40.8% | 2.38 | -50.5% |

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
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
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
| Dc lambda home | 2.7776 |
| Dc lambda away | 1.5461 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 75.1% |
| P btts no | 24.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.19 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.94 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.81 |
| Fair Over 3.5 odds | 1.61 |
| Fair Under 3.5 odds | 2.63 |
| Fair Over 4.5 odds | 2.38 |
| Fair Under 4.5 odds | 1.73 |
| Unadjusted home-win probability | 63.3% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 19.5% |
| Raw p over 1 5 | 93.1% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 73.9% |
| P home draw | 77.5% |
| P draw away | 43.9% |
| P home away | 78.5% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Raw p home away | 82.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.99 |
| Reference draw odds | 3.68 |
| Reference away odds | 3.72 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:38Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:38Z |
| Home probability edge | +7.2% |
| Draw probability edge | -4.3% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | +20.0% |
| Under 2.5 probability edge | -20.0% |
| Raw edge prob home | 0.1445 |
| Raw ev home | 0.2908 |
| Raw edge prob draw | -0.0850 |
| Raw ev draw | -0.3487 |
| Raw edge prob away | -0.0595 |
| Raw ev away | -0.2554 |
| Market p home draw | 73.7% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:38Z |
| Market reference home draw last update utc | 2026-10-17T09:09:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.9% |
| Market draw away odds | 1.86 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:38Z |
| Market reference draw away last update utc | 2026-10-17T09:09:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.3% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:38Z |
| Market reference home away last update utc | 2026-10-17T09:09:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.86 |
| Market reference dc home draw odds | 1.31 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.5% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:23Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.7% |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.35 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:23Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 62.4% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:38Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.52 |
| Market reference btts yes last update utc | 2026-10-17T09:09:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **47.1%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.43 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 43.5%; Under 3.5 goals: 77.3%; Double Chance 1X: 74.8%; Double Chance X2: 52.9%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.9%; BTTS No (at least one team does not score): 52.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 47.1% | 2.12 |
| Draw | 27.7% | 3.61 |
| Alavés win | 25.2% | 3.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.49 |
| Alavés expected goals | 0.94 |
| Expected total goals | 2.43 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 43.5% |
| Under 2.5 | 56.5% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.06% |
| 2 | 1-0 | 12.13% |
| 3 | 0-0 | 9.36% |
| 4 | 2-0 | 9.24% |
| 5 | 2-1 | 8.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 47.1% | 44.6% | 2.23 | +5.1% |
| Draw | 27.7% | 28.6% | 3.42 | -5.3% |
| Alavés win | 25.2% | 26.8% | 3.64 | -8.3% |
| Over 2.5 | 43.5% | 42.3% | 2.30 | +0.1% |
| Under 2.5 | 56.5% | 57.7% | 1.72 | -2.8% |

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
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4911 |
| Dc lambda away | 0.9434 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.9% |
| P btts no | 52.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.68 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.30 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.41 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.12 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 47.6% |
| P home draw | 74.8% |
| P draw away | 52.9% |
| P home away | 72.3% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.18 |
| Reference draw odds | 3.34 |
| Reference away odds | 3.56 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.23 |
| Reference Under 2.5 odds | 1.67 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:38Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:38Z |
| Home probability edge | +2.5% |
| Draw probability edge | -1.0% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | 0.0510 |
| Raw ev home | 0.1076 |
| Raw edge prob draw | -0.0191 |
| Raw ev draw | -0.0860 |
| Raw edge prob away | -0.0319 |
| Raw ev away | -0.1407 |
| Market p home draw | 72.5% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:38Z |
| Market reference home draw last update utc | 2026-10-17T09:09:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.1% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:38Z |
| Market reference draw away last update utc | 2026-10-17T09:09:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.4% |
| Market home away odds | 1.36 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:38Z |
| Market reference home away last update utc | 2026-10-17T09:09:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.69 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.37 |
| Market p over 1 5 | 70.8% |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 3.00 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:23Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 79.0% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 3.75 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:23Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 47.8% |
| Market btts yes odds | 1.90 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:38Z |
| Market reference btts yes odds | 2.01 |
| Market reference btts yes opposite odds | 1.85 |
| Market reference btts yes last update utc | 2026-10-17T09:09:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **47.6%**. Expected goals are 0.63 for Málaga and 1.27 for Real Sociedad (1.90 combined). The most likely exact score is 0-1 at 17.2%. Goal-market probabilities: at least one goal: 85.6%; Over 2.5 goals: 29.8%; Under 3.5 goals: 87.7%; Double Chance 1X: 52.4%; Double Chance X2: 76.0%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 95.6%; BTTS Yes (both teams score): 33.8%; BTTS No (at least one team does not score): 66.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 24.0% | 4.17 |
| Draw | 28.4% | 3.52 |
| Real Sociedad win | 47.6% | 2.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.27 |
| Expected total goals | 1.90 |
| Over 0.5 | 85.6% |
| Under 0.5 | 14.4% |
| Over 1.5 | 56.4% |
| Under 1.5 | 43.6% |
| Over 2.5 | 29.8% |
| Under 2.5 | 70.2% |
| Over 3.5 | 12.3% |
| Under 3.5 | 87.7% |
| Over 4.5 | 4.4% |
| Under 4.5 | 95.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.18% |
| 2 | 0-0 | 14.35% |
| 3 | 1-0 | 12.04% |
| 4 | 1-1 | 11.58% |
| 5 | 0-2 | 11.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 24.0% | 29.8% | 3.29 | -21.1% |
| Draw | 28.4% | 26.8% | 3.63 | +3.2% |
| Real Sociedad win | 47.6% | 43.4% | 2.29 | +9.0% |
| Over 2.5 | 29.8% | 53.2% | 1.86 | -44.5% |
| Under 2.5 | 70.2% | 46.8% | 2.10 | +47.3% |

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
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6303 |
| Dc lambda away | 1.2741 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 33.8% |
| P btts no | 66.2% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.97 |
| Fair Over 1.5 odds | 1.77 |
| Fair Under 1.5 odds | 2.29 |
| Fair Over 2.5 odds | 3.35 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 8.11 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 22.69 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 18.1% |
| Unadjusted draw probability | 30.0% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 57.0% |
| Raw p under 3 5 | 87.4% |
| Raw p btts yes | 33.9% |
| P home draw | 52.4% |
| P draw away | 76.0% |
| P home away | 71.6% |
| Raw p home draw | 48.2% |
| Raw p draw away | 81.9% |
| Raw p home away | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.20 |
| Reference draw odds | 3.54 |
| Reference away odds | 2.23 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.03 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:38Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:38Z |
| Home probability edge | -5.8% |
| Draw probability edge | +1.6% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -23.4% |
| Under 2.5 probability edge | +23.4% |
| Raw edge prob home | -0.1165 |
| Raw ev home | -0.4030 |
| Raw edge prob draw | 0.0320 |
| Raw ev draw | 0.0896 |
| Raw edge prob away | 0.0845 |
| Raw ev away | 0.1871 |
| Market p home draw | 55.0% |
| Market home draw odds | 1.70 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:38Z |
| Market reference home draw last update utc | 2026-10-17T09:09:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.2% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:38Z |
| Market reference draw away last update utc | 2026-10-17T09:09:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.8% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:38Z |
| Market reference home away last update utc | 2026-10-17T09:09:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.34 |
| Market reference dc home draw odds | 1.76 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 77.8% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:23Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 68.9% |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:23Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.9% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:38Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.32 |
| Market reference btts yes last update utc | 2026-10-17T09:09:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.3%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.7%; Under 3.5 goals: 56.3%; Double Chance 1X: 92.4%; Double Chance X2: 21.7%; Double Chance 12 (either team wins): 85.9%; Under 4.5 goals: 74.8%; BTTS Yes (both teams score): 48.6%; BTTS No (at least one team does not score): 51.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.3% | 1.28 |
| Draw | 14.1% | 7.09 |
| Sevilla win | 7.6% | 13.13 |

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
| Over 2.5 | 65.7% |
| Under 2.5 | 34.3% |
| Over 3.5 | 43.7% |
| Under 3.5 | 56.3% |
| Over 4.5 | 25.2% |
| Under 4.5 | 74.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.00% |
| 2 | 3-0 | 10.51% |
| 3 | 1-0 | 8.98% |
| 4 | 2-1 | 8.91% |
| 5 | 3-1 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 78.3% | 79.1% | 1.27 | -0.6% |
| Draw | 14.1% | 13.7% | 6.76 | -4.7% |
| Sevilla win | 7.6% | 7.2% | 12.40 | -5.6% |

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
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.6276 |
| Dc lambda away | 0.7421 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 48.6% |
| P btts no | 51.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.68 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.78 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.97 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 77.5% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.0% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.5% |
| Raw p btts yes | 48.8% |
| P home draw | 92.4% |
| P draw away | 21.7% |
| P home away | 85.9% |
| Raw p home draw | 92.0% |
| Raw p draw away | 22.5% |
| Raw p home away | 85.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.25 |
| Reference draw odds | 6.65 |
| Reference away odds | 12.25 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.4% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | -0.0166 |
| Raw ev home | -0.0164 |
| Raw edge prob draw | 0.0084 |
| Raw ev draw | -0.0183 |
| Raw edge prob away | 0.0082 |
| Raw ev away | -0.0048 |
| Market p home draw | 91.1% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:38Z |
| Market reference home draw last update utc | 2026-10-17T09:09:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.6% |
| Market draw away odds | 4.18 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:38Z |
| Market reference draw away last update utc | 2026-10-17T09:09:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.3% |
| Market home away odds | 1.14 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:38Z |
| Market reference home away last update utc | 2026-10-17T09:09:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.31 |
| Market reference dc home draw odds | 1.07 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:01:26Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.5% |
| Market under 3 5 odds | 1.84 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:01:26Z |
| Market reference under 3 5 odds | 1.70 |
| Market reference under 3 5 opposite odds | 1.99 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:23Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 51.0% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:38Z |
| Market reference btts yes odds | 1.88 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-10-17T09:09:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.1%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.5%. Goal-market probabilities: at least one goal: 81.5%; Over 2.5 goals: 23.2%; Under 3.5 goals: 91.5%; Double Chance 1X: 68.2%; Double Chance X2: 64.9%; Double Chance 12 (either team wins): 66.9%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 31.0%; BTTS No (at least one team does not score): 69.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.1% | 2.85 |
| Draw | 33.1% | 3.02 |
| Rayo Vallecano win | 31.8% | 3.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.5% |
| Under 0.5 | 18.5% |
| Over 1.5 | 49.2% |
| Under 1.5 | 50.8% |
| Over 2.5 | 23.2% |
| Under 2.5 | 76.8% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.47% |
| 2 | 1-0 | 16.24% |
| 3 | 0-1 | 16.07% |
| 4 | 1-1 | 12.44% |
| 5 | 2-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.1% | 32.9% | 2.99 | +4.9% |
| Draw | 33.1% | 31.0% | 3.16 | +4.6% |
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
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9068 |
| Dc lambda away | 0.7369 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 31.0% |
| P btts no | 69.0% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.41 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.30 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.76 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.46 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.2% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.2% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.4% |
| P home draw | 68.2% |
| P draw away | 64.9% |
| P home away | 66.9% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.8% |
| Raw p home away | 64.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.91 |
| Reference draw odds | 3.08 |
| Reference away odds | 2.67 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.60 |
| Reference Under 2.5 odds | 1.51 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Home probability edge | +2.1% |
| Draw probability edge | +2.1% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -12.5% |
| Under 2.5 probability edge | +12.5% |
| Raw edge prob home | 0.0430 |
| Raw ev home | 0.1132 |
| Raw edge prob draw | 0.0410 |
| Raw ev draw | 0.1107 |
| Raw edge prob away | -0.0840 |
| Raw ev away | -0.2432 |
| Market p home draw | 64.3% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:38Z |
| Market reference home draw last update utc | 2026-10-17T09:09:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.4% |
| Market draw away odds | 1.45 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:38Z |
| Market reference draw away last update utc | 2026-10-17T09:09:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 67.4% |
| Market home away odds | 1.41 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:38Z |
| Market reference home away last update utc | 2026-10-17T09:09:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home draw odds | 1.50 |
| Market reference dc home away odds | 1.43 |
| Market p over 1 5 | 63.8% |
| Market reference over 1 5 odds | 1.50 |
| Market reference over 1 5 opposite odds | 2.50 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:23Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 84.4% |
| Market reference under 3 5 odds | 1.15 |
| Market reference under 3 5 opposite odds | 4.60 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:23Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 44.3% |
| Market btts yes odds | 2.07 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:38Z |
| Market reference btts yes odds | 2.16 |
| Market reference btts yes opposite odds | 1.74 |
| Market reference btts yes last update utc | 2026-10-17T09:09:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.6%**. Expected goals are 1.28 for Levante and 1.37 for Athletic Bilbao (2.65 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 49.4%; Under 3.5 goals: 72.4%; Double Chance 1X: 58.4%; Double Chance X2: 68.8%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 31.2% | 3.21 |
| Draw | 27.2% | 3.68 |
| Athletic Bilbao win | 41.6% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.28 |
| Athletic Bilbao expected goals | 1.37 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.4% |
| Under 2.5 | 50.6% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.94% |
| 2 | 0-1 | 10.05% |
| 3 | 1-2 | 9.11% |
| 4 | 1-0 | 7.88% |
| 5 | 0-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 31.2% | 27.8% | 3.52 | +9.8% |
| Draw | 27.2% | 27.8% | 3.52 | -4.3% |
| Athletic Bilbao win | 41.6% | 44.4% | 2.24 | -6.8% |
| Over 2.5 | 49.4% | 48.6% | 2.02 | -0.3% |
| Under 2.5 | 50.6% | 51.4% | 1.92 | -2.8% |

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
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2822 |
| Dc lambda away | 1.3727 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.38 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.70 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 34.6% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 38.8% |
| Raw p over 1 5 | 74.6% |
| Raw p under 3 5 | 72.4% |
| Raw p btts yes | 54.2% |
| P home draw | 58.4% |
| P draw away | 68.8% |
| P home away | 72.8% |
| Raw p home draw | 61.2% |
| Raw p draw away | 65.4% |
| Raw p home away | 73.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.42 |
| Reference draw odds | 3.42 |
| Reference away odds | 2.18 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:38Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:38Z |
| Home probability edge | +3.4% |
| Draw probability edge | -0.6% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | 0.0681 |
| Raw ev home | 0.2180 |
| Raw edge prob draw | -0.0119 |
| Raw ev draw | -0.0637 |
| Raw edge prob away | -0.0562 |
| Raw ev away | -0.1309 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **56.8%**. Expected goals are 1.39 for Alavés and 0.44 for Málaga (1.83 combined). The most likely exact score is 1-0 at 20.7%. Goal-market probabilities: at least one goal: 84.3%; Over 2.5 goals: 27.5%; Under 3.5 goals: 89.0%; Double Chance 1X: 83.7%; Double Chance X2: 43.2%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 96.2%; BTTS Yes (both teams score): 26.9%; BTTS No (at least one team does not score): 73.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 56.8% | 1.76 |
| Draw | 27.0% | 3.71 |
| Málaga win | 16.3% | 6.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.39 |
| Málaga expected goals | 0.44 |
| Expected total goals | 1.83 |
| Over 0.5 | 84.3% |
| Under 0.5 | 15.7% |
| Over 1.5 | 53.9% |
| Under 1.5 | 46.1% |
| Over 2.5 | 27.5% |
| Under 2.5 | 72.5% |
| Over 3.5 | 11.0% |
| Under 3.5 | 89.0% |
| Over 4.5 | 3.8% |
| Under 4.5 | 96.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.67% |
| 2 | 0-0 | 15.71% |
| 3 | 2-0 | 14.50% |
| 4 | 0-1 | 9.73% |
| 5 | 1-1 | 9.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 56.8% | 52.9% | 1.89 | +7.3% |
| Draw | 27.0% | 26.0% | 3.73 | +0.5% |
| Málaga win | 16.3% | 21.1% | 4.57 | -25.7% |
| Over 2.5 | 27.5% | 47.3% | 2.07 | -43.1% |
| Under 2.5 | 72.5% | 52.7% | 1.88 | +36.3% |

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
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3887 |
| Dc lambda away | 0.4405 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 26.9% |
| P btts no | 73.1% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.36 |
| Fair Over 1.5 odds | 1.86 |
| Fair Under 1.5 odds | 2.17 |
| Fair Over 2.5 odds | 3.64 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.11 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 26.60 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 60.6% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 54.8% |
| Raw p under 3 5 | 88.7% |
| Raw p btts yes | 27.0% |
| P home draw | 83.7% |
| P draw away | 43.2% |
| P home away | 73.0% |
| Raw p home draw | 88.6% |
| Raw p draw away | 39.4% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.84 |
| Reference draw odds | 3.64 |
| Reference away odds | 4.45 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.01 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:38Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:38Z |
| Home probability edge | +3.8% |
| Draw probability edge | +1.0% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -19.9% |
| Under 2.5 probability edge | +19.9% |
| Raw edge prob home | 0.0769 |
| Raw ev home | 0.1459 |
| Raw edge prob draw | 0.0194 |
| Raw ev draw | 0.0417 |
| Raw edge prob away | -0.0963 |
| Raw ev away | -0.4771 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **74.1%**. Expected goals are 2.25 for Atlético Madrid and 0.91 for Deportivo La Coruña (3.16 combined). The most likely exact score is 2-0 at 11.8%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 62.6%; Under 3.5 goals: 60.2%; Double Chance 1X: 90.3%; Double Chance X2: 25.9%; Double Chance 12 (either team wins): 83.9%; Under 4.5 goals: 78.0%; BTTS Yes (both teams score): 52.4%; BTTS No (at least one team does not score): 47.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 74.1% | 1.35 |
| Draw | 16.1% | 6.19 |
| Deportivo La Coruña win | 9.7% | 10.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.25 |
| Deportivo La Coruña expected goals | 0.91 |
| Expected total goals | 3.16 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 62.6% |
| Under 2.5 | 37.4% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 22.0% |
| Under 4.5 | 78.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.83% |
| 2 | 2-1 | 10.73% |
| 3 | 1-0 | 10.31% |
| 4 | 3-0 | 8.87% |
| 5 | 3-1 | 8.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 74.1% | 80.8% | 1.24 | -8.1% |
| Draw | 16.1% | 13.4% | 6.92 | +11.7% |
| Deportivo La Coruña win | 9.7% | 5.9% | 14.90 | +44.8% |

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
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2485 |
| Dc lambda away | 0.9072 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 52.4% |
| P btts no | 47.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.29 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.97 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.54 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 67.5% |
| Unadjusted draw probability | 18.9% |
| Unadjusted away-win probability | 13.6% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 61.2% |
| Raw p btts yes | 53.5% |
| P home draw | 90.3% |
| P draw away | 25.9% |
| P home away | 83.9% |
| Raw p home draw | 86.4% |
| Raw p draw away | 32.5% |
| Raw p home away | 81.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.22 |
| Reference draw odds | 6.50 |
| Reference away odds | 14.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | -6.6% |
| Draw probability edge | +2.8% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | -2.9% |
| Under 2.5 probability edge | +2.9% |
| Raw edge prob home | -0.1325 |
| Raw ev home | -0.1629 |
| Raw edge prob draw | 0.0554 |
| Raw ev draw | 0.3093 |
| Raw edge prob away | 0.0771 |
| Raw ev away | 1.0227 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **49.8%**. Expected goals are 1.40 for Rayo Vallecano and 1.07 for Elche CF (2.46 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.3%; Double Chance 1X: 75.8%; Double Chance X2: 50.2%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 89.4%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 49.8% | 2.01 |
| Draw | 25.9% | 3.86 |
| Elche CF win | 24.2% | 4.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.40 |
| Elche CF expected goals | 1.07 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 23.7% |
| Under 3.5 | 76.3% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.08% |
| 2 | 1-1 | 12.30% |
| 3 | 2-1 | 9.98% |
| 4 | 2-0 | 9.37% |
| 5 | 0-0 | 8.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 49.8% | 55.4% | 1.81 | -9.8% |
| Draw | 25.9% | 24.5% | 3.94 | +2.2% |
| Elche CF win | 24.2% | 20.1% | 4.78 | +15.9% |
| Over 2.5 | 45.3% | 52.7% | 1.88 | -14.9% |
| Under 2.5 | 54.7% | 47.3% | 2.07 | +13.3% |

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
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Vallecano |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3976 |
| Dc lambda away | 1.0655 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.98 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.46 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.22 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.42 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 44.3% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 28.4% |
| Raw p over 1 5 | 70.8% |
| Raw p under 3 5 | 76.5% |
| Raw p btts yes | 49.6% |
| P home draw | 75.8% |
| P draw away | 50.2% |
| P home away | 74.1% |
| Raw p home draw | 71.6% |
| Raw p draw away | 55.7% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.76 |
| Reference draw odds | 3.84 |
| Reference away odds | 4.65 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.01 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:38Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:38Z |
| Home probability edge | -5.6% |
| Draw probability edge | +1.4% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.1115 |
| Raw ev home | -0.1991 |
| Raw edge prob draw | 0.0283 |
| Raw ev draw | 0.0777 |
| Raw edge prob away | 0.0832 |
| Raw ev away | 0.3574 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **39.4%**. Expected goals are 1.96 for Real Racing Club de Santander and 2.00 for Espanyol (3.95 combined). The most likely exact score is 1-1 at 8.6%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 74.8%; Under 3.5 goals: 44.4%; Double Chance 1X: 63.1%; Double Chance X2: 60.6%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 64.4%; BTTS Yes (both teams score): 74.9%; BTTS No (at least one team does not score): 25.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 39.4% | 2.54 |
| Draw | 23.7% | 4.22 |
| Espanyol win | 36.9% | 2.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.96 |
| Espanyol expected goals | 2.00 |
| Expected total goals | 3.95 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 90.6% |
| Under 1.5 | 9.4% |
| Over 2.5 | 74.8% |
| Under 2.5 | 25.2% |
| Over 3.5 | 55.6% |
| Under 3.5 | 44.4% |
| Over 4.5 | 35.6% |
| Under 4.5 | 64.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.58% |
| 2 | 2-2 | 8.19% |
| 3 | 2-1 | 7.49% |
| 4 | 1-2 | 6.87% |
| 5 | 3-1 | 4.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 39.4% | 40.2% | 2.47 | -2.6% |
| Draw | 23.7% | 26.2% | 3.72 | -11.9% |
| Espanyol win | 36.9% | 33.6% | 2.93 | +8.1% |
| Over 2.5 | 74.8% | 55.7% | 1.78 | +33.1% |
| Under 2.5 | 25.2% | 44.3% | 2.21 | -44.3% |

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
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9562 |
| Dc lambda away | 1.9957 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 74.9% |
| P btts no | 25.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.75 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 10.68 |
| Fair Over 2.5 odds | 1.34 |
| Fair Under 2.5 odds | 3.97 |
| Fair Over 3.5 odds | 1.80 |
| Fair Under 3.5 odds | 2.25 |
| Fair Over 4.5 odds | 2.81 |
| Fair Under 4.5 odds | 1.55 |
| Unadjusted home-win probability | 38.6% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 40.2% |
| Raw p over 1 5 | 90.7% |
| Raw p under 3 5 | 44.3% |
| Raw p btts yes | 74.4% |
| P home draw | 63.1% |
| P draw away | 60.6% |
| P home away | 76.3% |
| Raw p home draw | 59.8% |
| Raw p draw away | 61.4% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.40 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.85 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.14 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:38Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:38Z |
| Home probability edge | -0.8% |
| Draw probability edge | -2.5% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | +19.1% |
| Under 2.5 probability edge | -19.1% |
| Raw edge prob home | -0.0154 |
| Raw ev home | -0.0454 |
| Raw edge prob draw | -0.0503 |
| Raw ev draw | -0.2124 |
| Raw edge prob away | 0.0657 |
| Raw ev away | 0.1773 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **45.1%**. Expected goals are 1.33 for Valencia and 1.63 for Villarreal (2.96 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.5%; Under 3.5 goals: 65.7%; Double Chance 1X: 54.9%; Double Chance X2: 70.3%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 59.4%; BTTS No (at least one team does not score): 40.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.7% | 3.37 |
| Draw | 25.2% | 3.96 |
| Villarreal win | 45.1% | 2.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.33 |
| Villarreal expected goals | 1.63 |
| Expected total goals | 2.96 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 79.7% |
| Under 1.5 | 20.3% |
| Over 2.5 | 56.5% |
| Under 2.5 | 43.5% |
| Over 3.5 | 34.3% |
| Under 3.5 | 65.7% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.74% |
| 2 | 1-2 | 9.33% |
| 3 | 0-1 | 8.38% |
| 4 | 2-1 | 7.14% |
| 5 | 0-2 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.7% | 28.3% | 3.45 | +2.4% |
| Draw | 25.2% | 25.7% | 3.78 | -4.6% |
| Villarreal win | 45.1% | 45.9% | 2.17 | -2.1% |
| Over 2.5 | 56.5% | 55.6% | 1.78 | +0.6% |
| Under 2.5 | 43.5% | 44.4% | 2.20 | -4.3% |

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
| Market best home last update utc | 2026-10-17T09:08:38Z |
| Market best draw last update utc | 2026-10-17T09:08:38Z |
| Market best away last update utc | 2026-10-17T09:08:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3279 |
| Dc lambda away | 1.6271 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.4% |
| P btts no | 40.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.94 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.92 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.66 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 31.0% |
| Unadjusted draw probability | 24.7% |
| Unadjusted away-win probability | 44.2% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.7% |
| Raw p btts yes | 59.3% |
| P home draw | 54.9% |
| P draw away | 70.3% |
| P home away | 74.8% |
| Raw p home draw | 55.8% |
| Raw p draw away | 69.0% |
| Raw p home away | 75.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.36 |
| Reference draw odds | 3.68 |
| Reference away odds | 2.11 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:38Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:38Z |
| Home probability edge | +1.4% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | 0.0274 |
| Raw ev home | 0.0709 |
| Raw edge prob draw | -0.0103 |
| Raw ev draw | -0.0656 |
| Raw edge prob away | -0.0171 |
| Raw ev away | -0.0400 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **54.8%**. Expected goals are 1.21 for Athletic Bilbao and 0.62 for Getafe (1.83 combined). The most likely exact score is 1-0 at 20.8%. Goal-market probabilities: at least one goal: 85.6%; Over 2.5 goals: 28.9%; Under 3.5 goals: 88.3%; Double Chance 1X: 82.2%; Double Chance X2: 45.2%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 95.9%; BTTS Yes (both teams score): 31.8%; BTTS No (at least one team does not score): 68.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 54.8% | 1.82 |
| Draw | 27.4% | 3.65 |
| Getafe win | 17.8% | 5.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.21 |
| Getafe expected goals | 0.62 |
| Expected total goals | 1.83 |
| Over 0.5 | 85.6% |
| Under 0.5 | 14.4% |
| Over 1.5 | 55.6% |
| Under 1.5 | 44.4% |
| Over 2.5 | 28.9% |
| Under 2.5 | 71.1% |
| Over 3.5 | 11.7% |
| Under 3.5 | 88.3% |
| Over 4.5 | 4.1% |
| Under 4.5 | 95.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.85% |
| 2 | 0-0 | 14.40% |
| 3 | 2-0 | 12.84% |
| 4 | 1-1 | 10.85% |
| 5 | 0-1 | 9.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 54.8% | 59.2% | 1.70 | -6.8% |
| Draw | 27.4% | 23.8% | 4.04 | +10.7% |
| Getafe win | 17.8% | 17.0% | 5.60 | -0.5% |
| Over 2.5 | 28.9% | 43.0% | 2.27 | -34.3% |
| Under 2.5 | 71.1% | 57.0% | 1.74 | +23.6% |

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
| Market best home last update utc | 2026-10-17T09:08:39Z |
| Market best draw last update utc | 2026-10-17T09:08:39Z |
| Market best away last update utc | 2026-10-17T09:08:39Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2146 |
| Dc lambda away | 0.6173 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 31.8% |
| P btts no | 68.2% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.95 |
| Fair Over 1.5 odds | 1.80 |
| Fair Under 1.5 odds | 2.25 |
| Fair Over 2.5 odds | 3.45 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.56 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.51 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 50.4% |
| Unadjusted draw probability | 31.0% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 54.9% |
| Raw p under 3 5 | 88.6% |
| Raw p btts yes | 32.7% |
| P home draw | 82.2% |
| P draw away | 45.2% |
| P home away | 72.6% |
| Raw p home draw | 81.4% |
| Raw p draw away | 49.6% |
| Raw p home away | 69.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.65 |
| Reference draw odds | 3.94 |
| Reference away odds | 5.45 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.69 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:39Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:39Z |
| Home probability edge | -4.4% |
| Draw probability edge | +3.6% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -14.0% |
| Under 2.5 probability edge | +14.0% |
| Raw edge prob home | -0.0880 |
| Raw ev home | -0.1429 |
| Raw edge prob draw | 0.0718 |
| Raw ev draw | 0.2525 |
| Raw edge prob away | 0.0162 |
| Raw ev away | 0.0405 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **58.0%**. Expected goals are 2.04 for Barcelona and 1.41 for Real Madrid (3.45 combined). The most likely exact score is 2-1 at 10.4%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.8%; Under 3.5 goals: 54.2%; Double Chance 1X: 78.1%; Double Chance X2: 42.0%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 72.9%; BTTS Yes (both teams score): 65.4%; BTTS No (at least one team does not score): 34.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 58.0% | 1.72 |
| Draw | 20.1% | 4.98 |
| Real Madrid win | 21.9% | 4.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.04 |
| Real Madrid expected goals | 1.41 |
| Expected total goals | 3.45 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 86.4% |
| Under 1.5 | 13.6% |
| Over 2.5 | 67.8% |
| Under 2.5 | 32.2% |
| Over 3.5 | 45.8% |
| Under 3.5 | 54.2% |
| Over 4.5 | 27.1% |
| Under 4.5 | 72.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.39% |
| 2 | 1-1 | 8.58% |
| 3 | 2-0 | 7.36% |
| 4 | 3-1 | 7.08% |
| 5 | 1-0 | 6.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 58.0% | 64.1% | 1.57 | -9.0% |
| Draw | 20.1% | 18.3% | 5.18 | +3.9% |
| Real Madrid win | 21.9% | 17.6% | 5.38 | +18.1% |

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
| Market best home last update utc | 2026-10-17T09:08:39Z |
| Market best draw last update utc | 2026-10-17T09:08:39Z |
| Market best away last update utc | 2026-10-17T09:08:39Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0424 |
| Dc lambda away | 1.4125 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 65.4% |
| P btts no | 34.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.28 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.34 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.11 |
| Fair Over 3.5 odds | 2.18 |
| Fair Under 3.5 odds | 1.84 |
| Fair Over 4.5 odds | 3.69 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 51.9% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 66.0% |
| P home draw | 78.1% |
| P draw away | 42.0% |
| P home away | 79.9% |
| Raw p home draw | 73.7% |
| Raw p draw away | 48.1% |
| Raw p home away | 78.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.53 |
| Reference draw odds | 5.05 |
| Reference away odds | 5.25 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.00 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | -6.1% |
| Draw probability edge | +1.7% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -11.8% |
| Under 2.5 probability edge | +11.8% |
| Raw edge prob home | -0.1214 |
| Raw ev home | -0.1849 |
| Raw edge prob draw | 0.0345 |
| Raw ev draw | 0.1288 |
| Raw edge prob away | 0.0868 |
| Raw ev away | 0.4144 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **37.9%**. Expected goals are 1.44 for Celta Vigo and 1.30 for Real Betis (2.74 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 51.3%; Under 3.5 goals: 70.7%; Double Chance 1X: 64.7%; Double Chance X2: 62.1%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 85.8%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 37.9% | 2.64 |
| Draw | 26.7% | 3.74 |
| Real Betis win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.44 |
| Real Betis expected goals | 1.30 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 51.3% |
| Under 2.5 | 48.7% |
| Over 3.5 | 29.3% |
| Under 3.5 | 70.7% |
| Over 4.5 | 14.2% |
| Under 4.5 | 85.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.67% |
| 2 | 1-0 | 8.54% |
| 3 | 0-1 | 8.53% |
| 4 | 1-2 | 8.23% |
| 5 | 2-1 | 8.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 37.9% | 35.6% | 2.77 | +5.1% |
| Draw | 26.7% | 27.4% | 3.57 | -4.6% |
| Real Betis win | 35.3% | 37.0% | 2.67 | -5.6% |
| Over 2.5 | 51.3% | 51.7% | 1.91 | -2.0% |
| Under 2.5 | 48.7% | 48.3% | 2.03 | -1.1% |

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
| Market best home last update utc | 2026-10-17T09:08:39Z |
| Market best draw last update utc | 2026-10-17T09:08:39Z |
| Market best away last update utc | 2026-10-17T09:08:39Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4407 |
| Dc lambda away | 1.2961 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.46 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.17 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.41 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.06 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 40.3% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 33.6% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 55.7% |
| P home draw | 64.7% |
| P draw away | 62.1% |
| P home away | 73.3% |
| Raw p home draw | 66.4% |
| Raw p draw away | 59.7% |
| Raw p home away | 73.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.70 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:39Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:39Z |
| Home probability edge | +2.3% |
| Draw probability edge | -0.6% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.0465 |
| Raw ev home | 0.1153 |
| Raw edge prob draw | -0.0127 |
| Raw ev draw | -0.0688 |
| Raw edge prob away | -0.0339 |
| Raw ev away | -0.1015 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **54.9%**. Expected goals are 1.86 for Real Sociedad and 1.20 for Levante (3.06 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 59.2%; Under 3.5 goals: 63.1%; Double Chance 1X: 77.7%; Double Chance X2: 45.1%; Double Chance 12 (either team wins): 77.1%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 59.1%; BTTS No (at least one team does not score): 40.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 54.9% | 1.82 |
| Draw | 22.9% | 4.37 |
| Levante win | 22.3% | 4.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.86 |
| Levante expected goals | 1.20 |
| Expected total goals | 3.06 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 59.2% |
| Under 2.5 | 40.8% |
| Over 3.5 | 36.9% |
| Under 3.5 | 63.1% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.57% |
| 2 | 2-1 | 10.14% |
| 3 | 1-0 | 8.83% |
| 4 | 2-0 | 8.46% |
| 5 | 3-1 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 54.9% | 57.1% | 1.76 | -3.4% |
| Draw | 22.9% | 22.6% | 4.26 | -2.6% |
| Levante win | 22.3% | 20.3% | 4.72 | +5.1% |
| Over 2.5 | 59.2% | 58.1% | 1.71 | +1.3% |
| Under 2.5 | 40.8% | 41.9% | 2.32 | -5.5% |

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
| Market best home last update utc | 2026-10-17T09:08:39Z |
| Market best draw last update utc | 2026-10-17T09:08:39Z |
| Market best away last update utc | 2026-10-17T09:08:39Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8634 |
| Dc lambda away | 1.1991 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.1% |
| P btts no | 40.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.58 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.37 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.71 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.09 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 52.7% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 63.3% |
| Raw p btts yes | 59.3% |
| P home draw | 77.7% |
| P draw away | 45.1% |
| P home away | 77.1% |
| Raw p home draw | 75.8% |
| Raw p draw away | 47.3% |
| Raw p home away | 76.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.71 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:39Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:39Z |
| Home probability edge | -2.2% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | -0.0441 |
| Raw ev home | -0.0729 |
| Raw edge prob draw | 0.0050 |
| Raw ev draw | -0.0156 |
| Raw edge prob away | 0.0391 |
| Raw ev away | 0.1430 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **48.0%**. Expected goals are 1.55 for Sevilla and 1.13 for CA Osasuna (2.68 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 49.9%; Under 3.5 goals: 71.9%; Double Chance 1X: 74.4%; Double Chance X2: 52.0%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 86.7%; BTTS Yes (both teams score): 53.7%; BTTS No (at least one team does not score): 46.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 48.0% | 2.09 |
| Draw | 26.5% | 3.78 |
| CA Osasuna win | 25.6% | 3.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.55 |
| CA Osasuna expected goals | 1.13 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 75.0% |
| Under 1.5 | 25.0% |
| Over 2.5 | 49.9% |
| Under 2.5 | 50.1% |
| Over 3.5 | 28.1% |
| Under 3.5 | 71.9% |
| Over 4.5 | 13.3% |
| Under 4.5 | 86.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.60% |
| 2 | 1-0 | 10.66% |
| 3 | 2-1 | 9.57% |
| 4 | 2-0 | 8.45% |
| 5 | 0-0 | 7.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 48.0% | 49.3% | 2.02 | -3.1% |
| Draw | 26.5% | 27.1% | 3.60 | -4.7% |
| CA Osasuna win | 25.6% | 23.6% | 4.11 | +5.1% |
| Over 2.5 | 49.9% | 44.7% | 2.19 | +9.3% |
| Under 2.5 | 50.1% | 55.3% | 1.79 | -10.3% |

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
| Market best home last update utc | 2026-10-17T09:08:39Z |
| Market best draw last update utc | 2026-10-17T09:08:39Z |
| Market best away last update utc | 2026-10-17T09:08:39Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.5453 |
| Dc lambda away | 1.1316 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:55.167943+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.7% |
| P btts no | 46.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.66 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.50 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 46.6% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.9% |
| Raw p btts yes | 53.6% |
| P home draw | 74.4% |
| P draw away | 52.0% |
| P home away | 73.5% |
| Raw p home draw | 72.4% |
| Raw p draw away | 53.4% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.97 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:31Z |
| Market reference home last update utc | 2026-10-17T09:09:31Z |
| Market reference draw last update utc | 2026-10-17T09:09:31Z |
| Market reference away last update utc | 2026-10-17T09:09:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:31Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:39Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:39Z |
| Home probability edge | -1.4% |
| Draw probability edge | -0.6% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +5.2% |
| Under 2.5 probability edge | -5.2% |
| Raw edge prob home | -0.0275 |
| Raw ev home | -0.0591 |
| Raw edge prob draw | -0.0125 |
| Raw ev draw | -0.0696 |
| Raw edge prob away | 0.0400 |
| Raw ev away | 0.1333 |

</details>


---
