# Premier League — football model report

Fixtures in this report: **12**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,205 |
| Training data through | 2026-10-17 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 365 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | ff75dd96de15007c8cc41acef6b16ce522ef237c4977a391c2e0a0df9ffc8e13 |
| Training as of utc | 2026-10-18T14:33:50.197074+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 65, 'bbs_added_results': 5, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 65, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T14:33:50.197074+00:00', 'observations': 78, 'observations_sha256': '450aea933785c85418c78670ab356ec59d4c2865409b43720840f601937b8288', 'eligible_training_matches': 15, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 48, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 4, 'retrospective_eligible_training_matches': 15, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'e32ff2d076e239f96dd776a89521890955df11fd7826b407263adc2a3514fbeb', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 1310.398 |
| Base scoring parameter | 0.223 |
| Home-advantage parameter | 0.165 |
| Dixon-Coles low-score adjustment | -0.092 |
| Xi per day | 0.0019 |
| Training data health | {'training_end': '2026-10-17', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 12.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261018T143350197074Z_f3d8738d9b532f07999ead618f07573defe1bd03455cae13544ab5f0693d34f0.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **58.7%**. Expected goals are 0.77 for Nottingham Forest and 1.59 for Arsenal (2.36 combined). The most likely exact score is 0-1 at 14.7%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 42.8%; Under 3.5 goals: 78.4%; Double Chance 1X: 41.3%; Double Chance X2: 83.9%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 43.2%; BTTS No (at least one team does not score): 56.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.1% | 6.22 |
| Draw | 25.2% | 3.97 |
| Arsenal win | 58.7% | 1.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.77 |
| Arsenal expected goals | 1.59 |
| Expected total goals | 2.36 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 69.7% |
| Under 1.5 | 30.3% |
| Over 2.5 | 42.8% |
| Under 2.5 | 57.2% |
| Over 3.5 | 21.6% |
| Under 3.5 | 78.4% |
| Over 4.5 | 9.3% |
| Under 4.5 | 90.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.70% |
| 2 | 0-2 | 12.55% |
| 3 | 1-1 | 11.70% |
| 4 | 0-0 | 9.74% |
| 5 | 1-2 | 9.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.1% | 15.1% | 6.19 | -0.5% |
| Draw | 25.2% | 23.2% | 4.00 | +0.8% |
| Arsenal win | 58.7% | 61.7% | 1.66 | -2.5% |
| Over 2.5 | 42.8% | 48.0% | 1.99 | -14.9% |
| Under 2.5 | 57.2% | 52.0% | 1.95 | +11.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | f696a248965373d9071dc0662e5c58a8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7711 |
| Dc lambda away | 1.5869 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 43.2% |
| P btts no | 56.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.27 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.30 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.75 |
| Fair Over 3.5 odds | 4.64 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.73 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 55.7% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.7% |
| Raw p btts yes | 43.8% |
| P home draw | 41.3% |
| P draw away | 83.9% |
| P home away | 74.8% |
| Raw p home draw | 44.3% |
| Raw p draw away | 83.0% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 6.00 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.58 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.77 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:49Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:49Z |
| Home probability edge | +1.0% |
| Draw probability edge | +2.0% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | 0.0193 |
| Raw ev home | 0.0546 |
| Raw edge prob draw | 0.0406 |
| Raw ev draw | 0.0890 |
| Raw edge prob away | -0.0599 |
| Raw ev away | -0.0747 |
| Market p home draw | 39.7% |
| Market home draw odds | 2.37 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:33:49Z |
| Market reference home draw last update utc | 2026-10-18T14:33:51Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.2% |
| Market draw away odds | 1.16 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:33:49Z |
| Market reference draw away last update utc | 2026-10-18T14:33:51Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.1% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:33:49Z |
| Market reference home away last update utc | 2026-10-18T14:33:51Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.13 |
| Market reference dc home draw odds | 2.40 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 74.1% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T14:33:21Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.15 |
| Market reference over 1 5 last update utc | 2026-10-18T14:33:51Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 74.3% |
| Market under 3 5 odds | 1.32 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T14:33:21Z |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.20 |
| Market reference under 3 5 last update utc | 2026-10-18T14:33:51Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 47.6% |
| Market btts yes odds | 1.96 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:49Z |
| Market reference btts yes odds | 1.95 |
| Market reference btts yes opposite odds | 1.79 |
| Market reference btts yes last update utc | 2026-10-18T14:33:50Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **57.7%**. Expected goals are 1.59 for Tottenham Hotspur and 1.05 for Coventry City (2.64 combined). The most likely exact score is 1-0 at 12.2%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 50.9%; Under 3.5 goals: 72.1%; Double Chance 1X: 80.8%; Double Chance X2: 42.3%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 57.7% | 1.73 |
| Draw | 23.1% | 4.34 |
| Coventry City win | 19.2% | 5.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.59 |
| Coventry City expected goals | 1.05 |
| Expected total goals | 2.64 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.7% |
| Under 1.5 | 24.3% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.16% |
| 2 | 2-1 | 11.23% |
| 3 | 1-1 | 11.01% |
| 4 | 2-0 | 10.67% |
| 5 | 0-0 | 6.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 57.7% | 66.8% | 1.54 | -11.1% |
| Draw | 23.1% | 18.8% | 4.67 | +7.7% |
| Coventry City win | 19.2% | 14.3% | 6.50 | +25.0% |
| Over 2.5 | 50.9% | 60.2% | 1.64 | -16.5% |
| Under 2.5 | 49.1% | 39.8% | 2.46 | +20.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T19:00:00+00:00 |
| Fixture id | 9baaf4e48b041cfef04e70e42532502e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5853 |
| Dc lambda away | 1.0528 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.35 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.41 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 24.1% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 72.8% |
| Raw p btts yes | 52.9% |
| P home draw | 80.8% |
| P draw away | 42.3% |
| P home away | 76.9% |
| Raw p home draw | 75.9% |
| Raw p draw away | 51.4% |
| Raw p home away | 72.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.46 |
| Reference draw odds | 4.80 |
| Reference away odds | 6.20 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:49Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:49Z |
| Home probability edge | -9.1% |
| Draw probability edge | +4.2% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.1823 |
| Raw ev home | -0.2514 |
| Raw edge prob draw | 0.0845 |
| Raw ev draw | 0.2739 |
| Raw edge prob away | 0.0978 |
| Raw ev away | 0.5673 |
| Market p home draw | 85.9% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:33:49Z |
| Market reference home draw last update utc | 2026-10-18T14:33:53Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 35.3% |
| Market draw away odds | 2.64 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:33:49Z |
| Market reference draw away last update utc | 2026-10-18T14:33:53Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.9% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:33:49Z |
| Market reference home away last update utc | 2026-10-18T14:33:53Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.75 |
| Market reference dc home draw odds | 1.13 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-18T14:33:51Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.4% |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market reference under 3 5 last update utc | 2026-10-18T14:33:51Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 55.7% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:49Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.16 |
| Market reference btts yes last update utc | 2026-10-18T14:33:53Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **46.1%**. Expected goals are 1.22 for Ipswich Town and 1.78 for Nottingham Forest (3.00 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 57.4%; Under 3.5 goals: 64.9%; Double Chance 1X: 53.9%; Double Chance X2: 72.2%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 81.7%; BTTS Yes (both teams score): 59.9%; BTTS No (at least one team does not score): 40.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 27.8% | 3.59 |
| Draw | 26.1% | 3.84 |
| Nottingham Forest win | 46.1% | 2.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.22 |
| Nottingham Forest expected goals | 1.78 |
| Expected total goals | 3.00 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 57.4% |
| Under 2.5 | 42.6% |
| Over 3.5 | 35.1% |
| Under 3.5 | 64.9% |
| Over 4.5 | 18.3% |
| Under 4.5 | 81.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.17% |
| 2 | 1-2 | 8.94% |
| 3 | 0-2 | 7.33% |
| 4 | 0-1 | 7.30% |
| 5 | 2-1 | 7.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 27.8% | 30.6% | 3.10 | -13.7% |
| Draw | 26.1% | 26.9% | 3.63 | -5.4% |
| Nottingham Forest win | 46.1% | 42.5% | 2.39 | +10.1% |
| Over 2.5 | 57.4% | 53.2% | 1.84 | +5.5% |
| Under 2.5 | 42.6% | 46.8% | 2.12 | -9.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T19:00:00+00:00 |
| Fixture id | d0202960708a442401d7fc7bd74a0183 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2199 |
| Dc lambda away | 1.7836 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.9% |
| P btts no | 40.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.27 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.25 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.85 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.46 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 25.1% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 49.6% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 59.6% |
| P home draw | 53.9% |
| P draw away | 72.2% |
| P home away | 73.9% |
| Raw p home draw | 50.4% |
| Raw p draw away | 74.9% |
| Raw p home away | 74.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.26 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:49Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:49Z |
| Home probability edge | -2.7% |
| Draw probability edge | -0.8% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | +4.1% |
| Under 2.5 probability edge | -4.1% |
| Raw edge prob home | -0.0541 |
| Raw ev home | -0.2206 |
| Raw edge prob draw | -0.0166 |
| Raw ev draw | -0.0838 |
| Raw edge prob away | 0.0707 |
| Raw ev away | 0.1858 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **67.2%**. Expected goals are 1.71 for Arsenal and 0.58 for Everton (2.29 combined). The most likely exact score is 1-0 at 17.2%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 41.5%; Under 3.5 goals: 79.6%; Double Chance 1X: 88.8%; Double Chance X2: 32.8%; Double Chance 12 (either team wins): 78.3%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 36.3%; BTTS No (at least one team does not score): 63.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 67.2% | 1.49 |
| Draw | 21.7% | 4.62 |
| Everton win | 11.2% | 8.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.71 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 68.3% |
| Under 1.5 | 31.7% |
| Over 2.5 | 41.5% |
| Under 2.5 | 58.5% |
| Over 3.5 | 20.4% |
| Under 3.5 | 79.6% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.16% |
| 2 | 2-0 | 15.51% |
| 3 | 0-0 | 9.61% |
| 4 | 1-1 | 9.60% |
| 5 | 2-1 | 9.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 67.2% | 70.5% | 1.43 | -3.9% |
| Draw | 21.7% | 18.5% | 4.93 | +6.8% |
| Everton win | 11.2% | 11.0% | 8.90 | -0.7% |
| Over 2.5 | 41.5% | 53.0% | 1.83 | -24.0% |
| Under 2.5 | 58.5% | 47.0% | 2.14 | +25.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:00:00+00:00 |
| Fixture id | f66e4f29c1b7bcfc5ab58c0b88c8850b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7100 |
| Dc lambda away | 0.5843 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.3% |
| P btts no | 63.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.41 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.16 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.90 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.57 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 63.9% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 11.3% |
| Raw p over 1 5 | 67.7% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 37.2% |
| P home draw | 88.8% |
| P draw away | 32.8% |
| P home away | 78.3% |
| Raw p home draw | 88.7% |
| Raw p draw away | 36.1% |
| Raw p home away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.39 |
| Reference draw odds | 4.90 |
| Reference away odds | 8.00 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:49Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:49Z |
| Home probability edge | -3.3% |
| Draw probability edge | +3.2% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -11.4% |
| Under 2.5 probability edge | +11.4% |
| Raw edge prob home | -0.0663 |
| Raw ev home | -0.0866 |
| Raw edge prob draw | 0.0632 |
| Raw ev draw | 0.2237 |
| Raw edge prob away | 0.0031 |
| Raw ev away | 0.0064 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **54.6%**. Expected goals are 1.14 for Aston Villa and 1.83 for Manchester City (2.97 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.5%; Under 3.5 goals: 65.2%; Double Chance 1X: 45.4%; Double Chance X2: 78.4%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 81.8%; BTTS Yes (both teams score): 57.8%; BTTS No (at least one team does not score): 42.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 21.6% | 4.63 |
| Draw | 23.8% | 4.20 |
| Manchester City win | 54.6% | 1.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.14 |
| Manchester City expected goals | 1.83 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.8% |
| Under 1.5 | 19.2% |
| Over 2.5 | 57.5% |
| Under 2.5 | 42.5% |
| Over 3.5 | 34.8% |
| Under 3.5 | 65.2% |
| Over 4.5 | 18.2% |
| Under 4.5 | 81.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.18% |
| 2 | 1-2 | 10.17% |
| 3 | 0-2 | 8.93% |
| 4 | 0-1 | 8.72% |
| 5 | 1-3 | 6.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 21.6% | 20.6% | 4.72 | +1.9% |
| Draw | 23.8% | 22.8% | 4.26 | +1.3% |
| Manchester City win | 54.6% | 56.6% | 1.76 | -3.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T11:30:00+00:00 |
| Fixture id | aca5dd297dbee71f576f7641569fe578 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1388 |
| Dc lambda away | 1.8338 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.8% |
| P btts no | 42.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.11 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.21 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.87 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.49 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 22.5% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 52.6% |
| Raw p over 1 5 | 80.7% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 58.1% |
| P home draw | 45.4% |
| P draw away | 78.4% |
| P home away | 76.2% |
| Raw p home draw | 47.4% |
| Raw p draw away | 77.5% |
| Raw p home away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 4.50 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.72 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:51Z |
| Home probability edge | +0.9% |
| Draw probability edge | +1.0% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | 0.0189 |
| Raw ev home | 0.0633 |
| Raw edge prob draw | 0.0207 |
| Raw ev draw | 0.0574 |
| Raw edge prob away | -0.0396 |
| Raw ev away | -0.0734 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **55.7%**. Expected goals are 2.10 for Chelsea and 1.22 for Tottenham Hotspur (3.32 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 64.4%; Under 3.5 goals: 57.6%; Double Chance 1X: 78.3%; Double Chance X2: 44.3%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 75.9%; BTTS Yes (both teams score): 62.8%; BTTS No (at least one team does not score): 37.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 55.7% | 1.80 |
| Draw | 22.6% | 4.43 |
| Tottenham Hotspur win | 21.7% | 4.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.10 |
| Tottenham Hotspur expected goals | 1.22 |
| Expected total goals | 3.32 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 64.4% |
| Under 2.5 | 35.6% |
| Over 3.5 | 42.4% |
| Under 3.5 | 57.6% |
| Over 4.5 | 24.1% |
| Under 4.5 | 75.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.15% |
| 2 | 2-1 | 9.53% |
| 3 | 2-0 | 7.82% |
| 4 | 3-1 | 6.69% |
| 5 | 1-0 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 55.7% | 54.6% | 1.81 | +0.8% |
| Draw | 22.6% | 22.7% | 4.30 | -2.9% |
| Tottenham Hotspur win | 21.7% | 22.7% | 4.36 | -5.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0382a9faef0bb8df1bcc436536cffb05 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1048 |
| Dc lambda away | 1.2190 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.8% |
| P btts no | 37.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.34 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.76 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.36 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.15 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 56.9% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 20.7% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.7% |
| P home draw | 78.3% |
| P draw away | 44.3% |
| P home away | 77.4% |
| Raw p home draw | 79.3% |
| Raw p draw away | 43.1% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.78 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.51 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:31Z |
| Home probability edge | +1.1% |
| Draw probability edge | -0.1% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | 0.0228 |
| Raw ev home | 0.0290 |
| Raw edge prob draw | -0.0026 |
| Raw ev draw | -0.0343 |
| Raw edge prob away | -0.0202 |
| Raw ev away | -0.0978 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **39.9%**. Expected goals are 1.09 for Coventry City and 1.27 for Fulham (2.35 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 42.3%; Under 3.5 goals: 78.8%; Double Chance 1X: 60.1%; Double Chance X2: 68.4%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 90.9%; BTTS Yes (both teams score): 48.4%; BTTS No (at least one team does not score): 51.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 31.6% | 3.17 |
| Draw | 28.6% | 3.50 |
| Fulham win | 39.9% | 2.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.09 |
| Fulham expected goals | 1.27 |
| Expected total goals | 2.35 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 69.4% |
| Under 1.5 | 30.6% |
| Over 2.5 | 42.3% |
| Under 2.5 | 57.7% |
| Over 3.5 | 21.2% |
| Under 3.5 | 78.8% |
| Over 4.5 | 9.1% |
| Under 4.5 | 90.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.48% |
| 2 | 0-1 | 11.02% |
| 3 | 0-0 | 10.12% |
| 4 | 1-0 | 9.47% |
| 5 | 1-2 | 8.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 31.6% | 32.7% | 3.12 | -1.5% |
| Draw | 28.6% | 26.9% | 3.61 | +3.1% |
| Fulham win | 39.9% | 40.4% | 2.39 | -4.7% |
| Over 2.5 | 42.3% | 55.2% | 1.81 | -23.4% |
| Under 2.5 | 57.7% | 44.8% | 2.15 | +24.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:00:00+00:00 |
| Fixture id | 0fbb2626ed9534b9dcf21d16925f9bd7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0851 |
| Dc lambda away | 1.2661 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.88 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.27 |
| Fair Over 2.5 odds | 2.36 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.72 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.94 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 30.4% |
| Unadjusted draw probability | 30.3% |
| Unadjusted away-win probability | 39.3% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.9% |
| Raw p btts yes | 48.7% |
| P home draw | 60.1% |
| P draw away | 68.4% |
| P home away | 71.4% |
| Raw p home draw | 60.7% |
| Raw p draw away | 69.6% |
| Raw p home away | 69.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.37 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:49Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:49Z |
| Home probability edge | -1.1% |
| Draw probability edge | +1.7% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -12.9% |
| Under 2.5 probability edge | +12.9% |
| Raw edge prob home | -0.0227 |
| Raw ev home | -0.0500 |
| Raw edge prob draw | 0.0340 |
| Raw ev draw | 0.0923 |
| Raw edge prob away | -0.0114 |
| Raw ev away | -0.0609 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **38.6%**. Expected goals are 1.48 for Crystal Palace and 1.52 for Newcastle United (3.01 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.8%; Under 3.5 goals: 64.6%; Double Chance 1X: 61.4%; Double Chance X2: 65.0%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 81.4%; BTTS Yes (both teams score): 61.5%; BTTS No (at least one team does not score): 38.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 35.0% | 2.86 |
| Draw | 26.4% | 3.79 |
| Newcastle United win | 38.6% | 2.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.48 |
| Newcastle United expected goals | 1.52 |
| Expected total goals | 3.01 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 57.8% |
| Under 2.5 | 42.2% |
| Over 3.5 | 35.4% |
| Under 3.5 | 64.6% |
| Over 4.5 | 18.6% |
| Under 4.5 | 81.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.24% |
| 2 | 1-2 | 8.72% |
| 3 | 2-1 | 8.06% |
| 4 | 0-1 | 6.67% |
| 5 | 2-2 | 6.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 35.0% | 34.0% | 3.02 | +5.6% |
| Draw | 26.4% | 26.5% | 3.67 | -3.1% |
| Newcastle United win | 38.6% | 39.6% | 2.42 | -6.5% |
| Over 2.5 | 57.8% | 59.2% | 1.69 | -2.4% |
| Under 2.5 | 42.2% | 40.8% | 2.36 | -0.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | fe235b26408c477368c40672a4488694 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4825 |
| Dc lambda away | 1.5229 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.5% |
| P btts no | 38.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.68 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.32 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.82 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.39 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 36.0% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 37.7% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 61.5% |
| P home draw | 61.4% |
| P draw away | 65.0% |
| P home away | 73.6% |
| Raw p home draw | 62.3% |
| Raw p draw away | 64.0% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.42 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.19 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:49Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:49Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | 0.0199 |
| Raw ev home | 0.0857 |
| Raw edge prob draw | -0.0015 |
| Raw ev draw | -0.0340 |
| Raw edge prob away | -0.0184 |
| Raw ev away | -0.0870 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **42.2%**. Expected goals are 1.24 for Hull City and 1.05 for Brentford (2.29 combined). The most likely exact score is 0-1 at 13.3%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 41.0%; Under 3.5 goals: 80.3%; Double Chance 1X: 57.8%; Double Chance X2: 69.5%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 46.7%; BTTS No (at least one team does not score): 53.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 30.5% | 3.28 |
| Draw | 27.3% | 3.66 |
| Brentford win | 42.2% | 2.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.24 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 67.8% |
| Under 1.5 | 32.2% |
| Over 2.5 | 41.0% |
| Under 2.5 | 59.0% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.32% |
| 2 | 1-1 | 12.80% |
| 3 | 0-0 | 10.11% |
| 4 | 1-2 | 9.75% |
| 5 | 1-0 | 8.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 30.5% | 21.6% | 4.72 | +44.0% |
| Draw | 27.3% | 23.9% | 4.09 | +11.7% |
| Brentford win | 42.2% | 54.5% | 1.79 | -24.5% |
| Over 2.5 | 41.0% | 55.6% | 1.73 | -29.0% |
| Under 2.5 | 59.0% | 44.4% | 2.28 | +34.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 69493b5ebb84f24ab1d6023a30ee89f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2403 |
| Dc lambda away | 1.0459 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.7% |
| P btts no | 53.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.89 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.10 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 5.07 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.87 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 39.4% |
| Unadjusted draw probability | 30.7% |
| Unadjusted away-win probability | 29.8% |
| Raw p over 1 5 | 67.8% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 47.3% |
| P home draw | 57.8% |
| P draw away | 69.5% |
| P home away | 72.7% |
| Raw p home draw | 70.2% |
| Raw p draw away | 60.6% |
| Raw p home away | 69.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 4.30 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.03 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:49Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:49Z |
| Home probability edge | +8.9% |
| Draw probability edge | +3.4% |
| Away probability edge | -12.3% |
| Over 2.5 probability edge | -14.5% |
| Under 2.5 probability edge | +14.5% |
| Raw edge prob home | 0.1788 |
| Raw ev home | 0.8619 |
| Raw edge prob draw | 0.0682 |
| Raw ev draw | 0.2564 |
| Raw edge prob away | -0.2470 |
| Raw ev away | -0.4660 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **46.5%**. Expected goals are 1.79 for Liverpool and 1.35 for Brighton and Hove Albion (3.13 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.6%; Under 3.5 goals: 61.7%; Double Chance 1X: 71.5%; Double Chance X2: 53.5%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 79.2%; BTTS Yes (both teams score): 62.6%; BTTS No (at least one team does not score): 37.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 46.5% | 2.15 |
| Draw | 25.0% | 4.00 |
| Brighton and Hove Albion win | 28.5% | 3.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.79 |
| Brighton and Hove Albion expected goals | 1.35 |
| Expected total goals | 3.13 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 60.6% |
| Under 2.5 | 39.4% |
| Over 3.5 | 38.3% |
| Under 3.5 | 61.7% |
| Over 4.5 | 20.8% |
| Under 4.5 | 79.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.42% |
| 2 | 2-1 | 9.28% |
| 3 | 1-2 | 7.17% |
| 4 | 2-0 | 6.89% |
| 5 | 1-0 | 6.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 46.5% | 46.1% | 2.11 | -1.9% |
| Draw | 25.0% | 24.9% | 4.00 | -0.1% |
| Brighton and Hove Albion win | 28.5% | 29.0% | 3.43 | -2.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 290ba8cd3f3a2e9252effca673bf5549 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 6.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7882 |
| Dc lambda away | 1.3464 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 62.6% |
| P btts no | 37.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.85 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.61 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.81 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 46.9% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 28.0% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 61.7% |
| Raw p btts yes | 62.6% |
| P home draw | 71.5% |
| P draw away | 53.5% |
| P home away | 75.0% |
| Raw p home draw | 72.0% |
| Raw p draw away | 53.1% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.09 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.27 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:51Z |
| Home probability edge | +0.4% |
| Draw probability edge | +0.0% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.0086 |
| Raw ev home | -0.0095 |
| Raw edge prob draw | 0.0009 |
| Raw ev draw | 0.0010 |
| Raw edge prob away | -0.0095 |
| Raw ev away | -0.0386 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **49.8%**. Expected goals are 1.72 for Manchester United and 1.31 for Bournemouth (3.03 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 59.0%; Under 3.5 goals: 63.7%; Double Chance 1X: 74.0%; Double Chance X2: 50.2%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 60.6%; BTTS No (at least one team does not score): 39.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 49.8% | 2.01 |
| Draw | 24.2% | 4.13 |
| Bournemouth win | 26.0% | 3.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.72 |
| Bournemouth expected goals | 1.31 |
| Expected total goals | 3.03 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 59.0% |
| Under 2.5 | 41.0% |
| Over 3.5 | 36.3% |
| Under 3.5 | 63.7% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.23% |
| 2 | 2-1 | 10.10% |
| 3 | 1-0 | 7.86% |
| 4 | 2-0 | 7.70% |
| 5 | 1-2 | 6.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 49.8% | 53.4% | 1.90 | -5.5% |
| Draw | 24.2% | 22.8% | 4.11 | -0.5% |
| Bournemouth win | 26.0% | 23.7% | 4.07 | +5.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 33fb7467b23c91d57dc976d9ab05ea97 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7215 |
| Dc lambda away | 1.3130 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.20 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.48 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.17 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 46.1% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 28.3% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 61.0% |
| P home draw | 74.0% |
| P draw away | 50.2% |
| P home away | 75.8% |
| Raw p home draw | 71.7% |
| Raw p draw away | 53.9% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.82 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.95 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:49Z |
| Home probability edge | -3.7% |
| Draw probability edge | +1.4% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.0735 |
| Raw ev home | -0.1245 |
| Raw edge prob draw | 0.0277 |
| Raw ev draw | 0.0523 |
| Raw edge prob away | 0.0458 |
| Raw ev away | 0.1526 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **37.0%**. Expected goals are 1.10 for Sunderland and 1.20 for Leeds United (2.30 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 89.2%; Over 2.5 goals: 40.7%; Under 3.5 goals: 79.9%; Double Chance 1X: 63.0%; Double Chance X2: 66.5%; Double Chance 12 (either team wins): 70.5%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 47.5%; BTTS No (at least one team does not score): 52.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 33.5% | 2.99 |
| Draw | 29.5% | 3.38 |
| Leeds United win | 37.0% | 2.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.10 |
| Leeds United expected goals | 1.20 |
| Expected total goals | 2.30 |
| Over 0.5 | 89.2% |
| Under 0.5 | 10.8% |
| Over 1.5 | 68.1% |
| Under 1.5 | 31.9% |
| Over 2.5 | 40.7% |
| Under 2.5 | 59.3% |
| Over 3.5 | 20.1% |
| Under 3.5 | 79.9% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.88% |
| 2 | 0-0 | 10.82% |
| 3 | 0-1 | 10.81% |
| 4 | 1-0 | 10.24% |
| 5 | 1-2 | 7.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 33.5% | 34.8% | 2.90 | -2.9% |
| Draw | 29.5% | 28.3% | 3.44 | +1.6% |
| Leeds United win | 37.0% | 36.9% | 2.63 | -2.8% |
| Over 2.5 | 40.7% | 45.2% | 2.14 | -12.8% |
| Under 2.5 | 59.3% | 54.8% | 1.83 | +8.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | e82f6b60fa41b82c8510f5b67ce61849 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:49Z |
| Market best draw last update utc | 2026-10-18T14:33:49Z |
| Market best away last update utc | 2026-10-18T14:33:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0998 |
| Dc lambda away | 1.1972 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:33:50.197074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 47.5% |
| P btts no | 52.5% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.24 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.14 |
| Fair Over 2.5 odds | 2.45 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.99 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.84 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 32.2% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 37.0% |
| Raw p over 1 5 | 68.1% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 47.8% |
| P home draw | 63.0% |
| P draw away | 66.5% |
| P home away | 70.5% |
| Raw p home draw | 63.0% |
| Raw p draw away | 67.8% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.75 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:51Z |
| Market reference home last update utc | 2026-10-18T14:33:51Z |
| Market reference draw last update utc | 2026-10-18T14:33:51Z |
| Market reference away last update utc | 2026-10-18T14:33:51Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.69 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:51Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:49Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:49Z |
| Home probability edge | -1.3% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | -0.0259 |
| Raw ev home | -0.0661 |
| Raw edge prob draw | 0.0246 |
| Raw ev draw | 0.0588 |
| Raw edge prob away | 0.0013 |
| Raw ev away | -0.0265 |

</details>


---
