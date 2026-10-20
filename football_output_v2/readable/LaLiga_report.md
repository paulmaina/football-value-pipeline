# La Liga — football model report

Fixtures in this report: **11**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,987 |
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
| Training sha256 | 60adcf22ab8438c04a76d37e206583036825977f4fd89f39a227e03cb1b2a181 |
| Training as of utc | 2026-10-20T05:42:08.788208+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 87, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 87, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-20T05:42:08.788208+00:00', 'observations': 119, 'observations_sha256': 'ff8c945314f01675a48476e1e8a7557a0bc6c4f2af85c27de5b93efa62da1e20', 'eligible_training_matches': 45, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 73, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 8, 'retrospective_eligible_training_matches': 45, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'b9f84822d2048c2988ce8b116db89c9a5284908713df03917527fd2883cb81c2', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 5519.514 |
| Base scoring parameter | 0.090 |
| Home-advantage parameter | 0.278 |
| Dixon-Coles low-score adjustment | -0.019 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 11.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261020T054208788208Z_94968a28441c6420f4e7e7efc3a9a7532c3fca877295ce71f1b590b523718afa.json |
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

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **44.2%**. Expected goals are 1.24 for Levante and 1.54 for Athletic Bilbao (2.78 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 52.0%; Under 3.5 goals: 69.7%; Double Chance 1X: 55.8%; Double Chance X2: 71.6%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 56.5%; BTTS No (at least one team does not score): 43.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 28.4% | 3.53 |
| Draw | 27.4% | 3.65 |
| Athletic Bilbao win | 44.2% | 2.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.24 |
| Athletic Bilbao expected goals | 1.54 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 52.0% |
| Under 2.5 | 48.0% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.97% |
| 2 | 0-1 | 9.37% |
| 3 | 1-2 | 9.16% |
| 4 | 0-2 | 7.39% |
| 5 | 1-0 | 6.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 28.4% | 26.3% | 3.80 | +7.8% |
| Draw | 27.4% | 29.3% | 3.52 | -3.5% |
| Athletic Bilbao win | 44.2% | 44.4% | 2.24 | -0.9% |
| Over 2.5 | 52.0% | 48.3% | 2.02 | +5.0% |
| Under 2.5 | 48.0% | 51.7% | 1.92 | -7.8% |

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
| Market best home last update utc | 2026-10-20T05:41:37Z |
| Market best draw last update utc | 2026-10-20T05:41:18Z |
| Market best away last update utc | 2026-10-20T05:41:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2402 |
| Dc lambda away | 1.5394 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:08.788208+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.47 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.30 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.81 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 30.5% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 76.8% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 56.0% |
| P home draw | 55.8% |
| P draw away | 71.6% |
| P home away | 72.6% |
| Raw p home draw | 56.0% |
| Raw p draw away | 69.5% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.67 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:58Z |
| Market reference home last update utc | 2026-10-20T05:41:58Z |
| Market reference draw last update utc | 2026-10-20T05:41:58Z |
| Market reference away last update utc | 2026-10-20T05:41:58Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.01 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:58Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:58Z |
| Market best over 2 5 last update utc | 2026-10-20T05:41:18Z |
| Market best under 2 5 last update utc | 2026-10-20T05:41:18Z |
| Home probability edge | +2.1% |
| Draw probability edge | -1.9% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +3.7% |
| Under 2.5 probability edge | -3.7% |
| Raw edge prob home | 0.0420 |
| Raw ev home | 0.1574 |
| Raw edge prob draw | -0.0377 |
| Raw ev draw | -0.1018 |
| Raw edge prob away | -0.0042 |
| Raw ev away | -0.0139 |
| Market p home draw | 55.8% |
| Market home draw odds | 1.73 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-20T05:41:18Z |
| Market reference home draw last update utc | 2026-10-20T05:41:43Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.3% |
| Market draw away odds | 1.35 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-20T05:41:18Z |
| Market reference draw away last update utc | 2026-10-20T05:41:43Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.9% |
| Market home away odds | 1.38 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-20T05:41:43Z |
| Market reference home away last update utc | 2026-10-20T05:41:43Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home draw odds | 1.73 |
| Market reference dc home away odds | 1.38 |
| Market p over 1 5 | 73.9% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-20T05:41:37Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.55 |
| Market reference over 1 5 last update utc | 2026-10-20T05:41:58Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.4% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:41:37Z |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.50 |
| Market reference under 3 5 last update utc | 2026-10-20T05:41:58Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.74 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-20T05:41:18Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.21 |
| Market reference btts yes last update utc | 2026-10-20T05:41:43Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **59.1%**. Expected goals are 1.63 for Alavés and 0.60 for Málaga (2.23 combined). The most likely exact score is 1-0 at 16.4%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 38.1%; Under 3.5 goals: 81.7%; Double Chance 1X: 84.2%; Double Chance X2: 40.9%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 92.6%; BTTS Yes (both teams score): 36.9%; BTTS No (at least one team does not score): 63.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 59.1% | 1.69 |
| Draw | 25.1% | 3.99 |
| Málaga win | 15.8% | 6.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.63 |
| Málaga expected goals | 0.60 |
| Expected total goals | 2.23 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 65.0% |
| Under 1.5 | 35.0% |
| Over 2.5 | 38.1% |
| Under 2.5 | 61.9% |
| Over 3.5 | 18.3% |
| Under 3.5 | 81.7% |
| Over 4.5 | 7.4% |
| Under 4.5 | 92.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.43% |
| 2 | 2-0 | 13.53% |
| 3 | 0-0 | 11.14% |
| 4 | 1-1 | 10.96% |
| 5 | 2-1 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 59.1% | 56.1% | 1.84 | +8.8% |
| Draw | 25.1% | 25.5% | 3.72 | -6.8% |
| Málaga win | 15.8% | 18.4% | 4.93 | -21.9% |
| Over 2.5 | 38.1% | 46.1% | 2.12 | -19.2% |
| Under 2.5 | 61.9% | 53.9% | 1.84 | +13.8% |

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
| Market best home last update utc | 2026-10-20T05:41:18Z |
| Market best draw last update utc | 2026-10-20T05:41:18Z |
| Market best away last update utc | 2026-10-20T05:41:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6281 |
| Dc lambda away | 0.6042 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:08.788208+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 36.9% |
| P btts no | 63.1% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.98 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.85 |
| Fair Over 2.5 odds | 2.62 |
| Fair Under 2.5 odds | 1.62 |
| Fair Over 3.5 odds | 5.45 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.44 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 62.1% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 36.6% |
| P home draw | 84.2% |
| P draw away | 40.9% |
| P home away | 74.9% |
| Raw p home draw | 86.7% |
| Raw p draw away | 37.9% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.72 |
| Reference draw odds | 3.60 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:56Z |
| Market reference home last update utc | 2026-10-20T05:41:56Z |
| Market reference draw last update utc | 2026-10-20T05:41:56Z |
| Market reference away last update utc | 2026-10-20T05:41:56Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market best over 2 5 last update utc | 2026-10-20T05:41:18Z |
| Market best under 2 5 last update utc | 2026-10-20T05:41:18Z |
| Home probability edge | +3.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | 0.0602 |
| Raw ev home | 0.1429 |
| Raw edge prob draw | -0.0094 |
| Raw ev draw | -0.0855 |
| Raw edge prob away | -0.0507 |
| Raw ev away | -0.3441 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **73.4%**. Expected goals are 2.28 for Atlético Madrid and 0.89 for Deportivo La Coruña (3.17 combined). The most likely exact score is 2-0 at 11.7%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 62.5%; Under 3.5 goals: 60.1%; Double Chance 1X: 89.9%; Double Chance X2: 26.6%; Double Chance 12 (either team wins): 83.6%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 52.2%; BTTS No (at least one team does not score): 47.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 73.4% | 1.36 |
| Draw | 16.4% | 6.08 |
| Deportivo La Coruña win | 10.1% | 9.89 |

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
| Over 2.5 | 62.5% |
| Under 2.5 | 37.5% |
| Over 3.5 | 39.9% |
| Under 3.5 | 60.1% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.70% |
| 2 | 2-1 | 10.41% |
| 3 | 1-0 | 10.09% |
| 4 | 3-0 | 8.90% |
| 5 | 3-1 | 7.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 73.4% | 78.3% | 1.31 | -3.8% |
| Draw | 16.4% | 14.4% | 6.48 | +6.6% |
| Deportivo La Coruña win | 10.1% | 7.2% | 10.05 | +1.6% |

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
| Market best home last update utc | 2026-10-20T05:41:18Z |
| Market best draw last update utc | 2026-10-20T05:41:18Z |
| Market best away last update utc | 2026-10-20T05:41:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2805 |
| Dc lambda away | 0.8893 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:08.788208+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 52.2% |
| P btts no | 47.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.74 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.97 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.53 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 68.5% |
| Unadjusted draw probability | 18.5% |
| Unadjusted away-win probability | 13.0% |
| Raw p over 1 5 | 82.6% |
| Raw p under 3 5 | 60.9% |
| Raw p btts yes | 53.0% |
| P home draw | 89.9% |
| P draw away | 26.6% |
| P home away | 83.6% |
| Raw p home draw | 87.0% |
| Raw p draw away | 31.5% |
| Raw p home away | 81.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.26 |
| Reference draw odds | 6.25 |
| Reference away odds | 12.00 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:56Z |
| Market reference home last update utc | 2026-10-20T05:41:56Z |
| Market reference draw last update utc | 2026-10-20T05:41:56Z |
| Market reference away last update utc | 2026-10-20T05:41:56Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.56 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:56Z |
| Home probability edge | -4.9% |
| Draw probability edge | +2.0% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | -1.2% |
| Under 2.5 probability edge | +1.2% |
| Raw edge prob home | -0.0979 |
| Raw ev home | -0.1021 |
| Raw edge prob draw | 0.0405 |
| Raw ev draw | 0.1971 |
| Raw edge prob away | 0.0574 |
| Raw ev away | 0.3051 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **52.2%**. Expected goals are 1.40 for Rayo Vallecano and 0.90 for Elche CF (2.29 combined). The most likely exact score is 1-0 at 15.0%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 41.0%; Under 3.5 goals: 79.8%; Double Chance 1X: 78.2%; Double Chance X2: 47.8%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 44.3%; BTTS No (at least one team does not score): 55.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 52.2% | 1.92 |
| Draw | 26.0% | 3.85 |
| Elche CF win | 21.8% | 4.58 |

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
| Over 2.5 | 41.0% |
| Under 2.5 | 59.0% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.97% |
| 2 | 1-1 | 12.05% |
| 3 | 2-0 | 10.62% |
| 4 | 0-0 | 9.66% |
| 5 | 2-1 | 9.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 52.2% | 56.1% | 1.81 | -5.5% |
| Draw | 26.0% | 24.1% | 3.94 | +2.3% |
| Elche CF win | 21.8% | 19.7% | 4.78 | +4.3% |
| Over 2.5 | 41.0% | 52.5% | 1.88 | -23.0% |
| Under 2.5 | 59.0% | 47.5% | 2.07 | +22.2% |

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
| Market best home last update utc | 2026-10-20T05:41:18Z |
| Market best draw last update utc | 2026-10-20T05:41:18Z |
| Market best away last update utc | 2026-10-20T05:41:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Vallecano |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3954 |
| Dc lambda away | 0.8983 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:08.788208+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.3% |
| P btts no | 55.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.36 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.95 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.74 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 44.8% |
| P home draw | 78.2% |
| P draw away | 47.8% |
| P home away | 74.0% |
| Raw p home draw | 76.0% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.72 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:56Z |
| Market reference home last update utc | 2026-10-20T05:41:56Z |
| Market reference draw last update utc | 2026-10-20T05:41:56Z |
| Market reference away last update utc | 2026-10-20T05:41:56Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market best over 2 5 last update utc | 2026-10-20T05:41:18Z |
| Market best under 2 5 last update utc | 2026-10-20T05:41:18Z |
| Home probability edge | -3.9% |
| Draw probability edge | +1.8% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -11.6% |
| Under 2.5 probability edge | +11.6% |
| Raw edge prob home | -0.0788 |
| Raw ev home | -0.1264 |
| Raw edge prob draw | 0.0363 |
| Raw ev draw | 0.0945 |
| Raw edge prob away | 0.0425 |
| Raw ev away | 0.1450 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Espanyol win** at **39.2%**. Expected goals are 1.90 for Real Racing Club de Santander and 2.13 for Espanyol (4.04 combined). The most likely exact score is 1-1 at 8.3%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 76.0%; Under 3.5 goals: 42.8%; Double Chance 1X: 60.8%; Double Chance X2: 62.7%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 62.8%; BTTS Yes (both teams score): 75.7%; BTTS No (at least one team does not score): 24.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 37.3% | 2.68 |
| Draw | 23.5% | 4.25 |
| Espanyol win | 39.2% | 2.55 |

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
| Over 2.5 | 76.0% |
| Under 2.5 | 24.0% |
| Over 3.5 | 57.2% |
| Under 3.5 | 42.8% |
| Over 4.5 | 37.2% |
| Under 4.5 | 62.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.28% |
| 2 | 2-2 | 8.24% |
| 3 | 2-1 | 7.23% |
| 4 | 1-2 | 6.81% |
| 5 | 3-2 | 4.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 37.3% | 39.4% | 2.57 | -4.1% |
| Draw | 23.5% | 26.3% | 3.71 | -12.8% |
| Espanyol win | 39.2% | 34.4% | 2.83 | +10.9% |
| Over 2.5 | 76.0% | 57.4% | 1.77 | +34.4% |
| Under 2.5 | 24.0% | 42.6% | 2.22 | -46.6% |

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
| Market best home last update utc | 2026-10-20T05:41:18Z |
| Market best draw last update utc | 2026-10-20T05:41:18Z |
| Market best away last update utc | 2026-10-20T05:41:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9040 |
| Dc lambda away | 2.1319 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:08.788208+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 75.7% |
| P btts no | 24.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.37 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.36 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.16 |
| Fair Over 3.5 odds | 1.75 |
| Fair Under 3.5 odds | 2.34 |
| Fair Over 4.5 odds | 2.69 |
| Fair Under 4.5 odds | 1.59 |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 91.2% |
| Raw p under 3 5 | 42.6% |
| Raw p btts yes | 75.1% |
| P home draw | 60.8% |
| P draw away | 62.7% |
| P home away | 76.5% |
| Raw p home draw | 56.0% |
| Raw p draw away | 64.7% |
| Raw p home away | 79.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.42 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.75 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:56Z |
| Market reference home last update utc | 2026-10-20T05:41:56Z |
| Market reference draw last update utc | 2026-10-20T05:41:56Z |
| Market reference away last update utc | 2026-10-20T05:41:56Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market best over 2 5 last update utc | 2026-10-20T05:41:18Z |
| Market best under 2 5 last update utc | 2026-10-20T05:41:18Z |
| Home probability edge | -2.1% |
| Draw probability edge | -2.8% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | +18.5% |
| Under 2.5 probability edge | -18.5% |
| Raw edge prob home | -0.0410 |
| Raw ev home | -0.0940 |
| Raw edge prob draw | -0.0550 |
| Raw ev draw | -0.2298 |
| Raw edge prob away | 0.0960 |
| Raw ev away | 0.2449 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **43.0%**. Expected goals are 1.27 for Valencia and 1.51 for Villarreal (2.78 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 52.5%; Under 3.5 goals: 69.7%; Double Chance 1X: 57.0%; Double Chance X2: 68.9%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 31.1% | 3.22 |
| Draw | 25.9% | 3.85 |
| Villarreal win | 43.0% | 2.33 |

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
| 1 | 1-1 | 12.27% |
| 2 | 0-1 | 9.24% |
| 3 | 1-2 | 9.07% |
| 4 | 1-0 | 7.49% |
| 5 | 2-1 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 31.1% | 30.3% | 3.45 | +7.2% |
| Draw | 25.9% | 26.2% | 3.78 | -1.9% |
| Villarreal win | 43.0% | 43.5% | 2.22 | -4.6% |
| Over 2.5 | 52.5% | 55.6% | 1.78 | -6.6% |
| Under 2.5 | 47.5% | 44.4% | 2.20 | +4.6% |

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
| Market best home last update utc | 2026-10-20T05:41:18Z |
| Market best draw last update utc | 2026-10-20T05:41:18Z |
| Market best away last update utc | 2026-10-20T05:41:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2725 |
| Dc lambda away | 1.5059 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:08.788208+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.35 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.30 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.73 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 76.8% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.2% |
| P home draw | 57.0% |
| P draw away | 68.9% |
| P home away | 74.1% |
| Raw p home draw | 57.5% |
| Raw p draw away | 68.1% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 3.10 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:56Z |
| Market reference home last update utc | 2026-10-20T05:41:56Z |
| Market reference draw last update utc | 2026-10-20T05:41:56Z |
| Market reference away last update utc | 2026-10-20T05:41:56Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market best over 2 5 last update utc | 2026-10-20T05:41:18Z |
| Market best under 2 5 last update utc | 2026-10-20T05:41:18Z |
| Home probability edge | +0.8% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | 0.0160 |
| Raw ev home | 0.0997 |
| Raw edge prob draw | -0.0059 |
| Raw ev draw | -0.0304 |
| Raw edge prob away | -0.0101 |
| Raw ev away | -0.0571 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **54.7%**. Expected goals are 1.27 for Athletic Bilbao and 0.62 for Getafe (1.89 combined). The most likely exact score is 1-0 at 20.0%. Goal-market probabilities: at least one goal: 85.7%; Over 2.5 goals: 30.0%; Under 3.5 goals: 87.4%; Double Chance 1X: 82.8%; Double Chance X2: 45.3%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 95.5%; BTTS Yes (both teams score): 33.1%; BTTS No (at least one team does not score): 66.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 54.7% | 1.83 |
| Draw | 28.1% | 3.56 |
| Getafe win | 17.2% | 5.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.27 |
| Getafe expected goals | 0.62 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.7% |
| Under 0.5 | 14.3% |
| Over 1.5 | 57.0% |
| Under 1.5 | 43.0% |
| Over 2.5 | 30.0% |
| Under 2.5 | 70.0% |
| Over 3.5 | 12.6% |
| Under 3.5 | 87.4% |
| Over 4.5 | 4.5% |
| Under 4.5 | 95.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.97% |
| 2 | 0-0 | 14.32% |
| 3 | 2-0 | 12.78% |
| 4 | 1-1 | 11.36% |
| 5 | 0-1 | 8.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 54.7% | 57.6% | 1.70 | -7.0% |
| Draw | 28.1% | 26.1% | 4.11 | +15.4% |
| Getafe win | 17.2% | 16.3% | 5.60 | -3.7% |
| Over 2.5 | 30.0% | 42.2% | 2.27 | -31.8% |
| Under 2.5 | 70.0% | 57.8% | 1.74 | +21.7% |

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
| Market best home last update utc | 2026-10-20T05:41:18Z |
| Market best draw last update utc | 2026-10-20T05:41:37Z |
| Market best away last update utc | 2026-10-20T05:41:18Z |
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
| Dc lambda home | 1.2651 |
| Dc lambda away | 0.6243 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:08.788208+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 33.1% |
| P btts no | 66.9% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.98 |
| Fair Over 1.5 odds | 1.76 |
| Fair Under 1.5 odds | 2.32 |
| Fair Over 2.5 odds | 3.33 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 7.97 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 22.43 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 51.8% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 18.1% |
| Raw p over 1 5 | 56.6% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 82.8% |
| P draw away | 45.3% |
| P home away | 71.9% |
| Raw p home draw | 81.9% |
| Raw p draw away | 48.2% |
| Raw p home away | 69.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.70 |
| Reference draw odds | 3.65 |
| Reference away odds | 5.75 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:56Z |
| Market reference home last update utc | 2026-10-20T05:41:56Z |
| Market reference draw last update utc | 2026-10-20T05:41:56Z |
| Market reference away last update utc | 2026-10-20T05:41:56Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.65 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market best over 2 5 last update utc | 2026-10-20T05:41:18Z |
| Market best under 2 5 last update utc | 2026-10-20T05:41:18Z |
| Home probability edge | -2.9% |
| Draw probability edge | +2.0% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -12.2% |
| Under 2.5 probability edge | +12.2% |
| Raw edge prob home | -0.0587 |
| Raw ev home | -0.1197 |
| Raw edge prob draw | 0.0401 |
| Raw ev draw | 0.2366 |
| Raw edge prob away | 0.0186 |
| Raw ev away | 0.0155 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **54.4%**. Expected goals are 1.78 for Barcelona and 1.33 for Real Madrid (3.11 combined). The most likely exact score is 2-1 at 10.7%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 61.1%; Under 3.5 goals: 61.9%; Double Chance 1X: 75.4%; Double Chance X2: 45.6%; Double Chance 12 (either team wins): 79.0%; Under 4.5 goals: 79.1%; BTTS Yes (both teams score): 60.6%; BTTS No (at least one team does not score): 39.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 54.4% | 1.84 |
| Draw | 21.0% | 4.76 |
| Real Madrid win | 24.6% | 4.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.78 |
| Real Madrid expected goals | 1.33 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 61.1% |
| Under 2.5 | 38.9% |
| Over 3.5 | 38.1% |
| Under 3.5 | 61.9% |
| Over 4.5 | 20.9% |
| Under 4.5 | 79.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.69% |
| 2 | 1-1 | 9.59% |
| 3 | 1-0 | 8.81% |
| 4 | 2-0 | 8.02% |
| 5 | 3-1 | 6.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 54.4% | 61.0% | 1.60 | -13.0% |
| Draw | 21.0% | 18.4% | 5.72 | +20.2% |
| Real Madrid win | 24.6% | 20.6% | 4.99 | +22.9% |

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
| Market best home last update utc | 2026-10-20T05:41:37Z |
| Market best draw last update utc | 2026-10-20T05:41:37Z |
| Market best away last update utc | 2026-10-20T05:41:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7752 |
| Dc lambda away | 1.3332 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:08.788208+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.07 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.59 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.57 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.79 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 47.7% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 28.7% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 61.4% |
| P home draw | 75.4% |
| P draw away | 45.6% |
| P home away | 79.0% |
| Raw p home draw | 71.3% |
| Raw p draw away | 52.3% |
| Raw p home away | 76.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.60 |
| Reference draw odds | 5.00 |
| Reference away odds | 4.50 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:58Z |
| Market reference home last update utc | 2026-10-20T05:41:58Z |
| Market reference draw last update utc | 2026-10-20T05:41:58Z |
| Market reference away last update utc | 2026-10-20T05:41:58Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.21 |
| Reference Under 2.5 odds | 4.60 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:56Z |
| Home probability edge | -6.7% |
| Draw probability edge | +2.6% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -20.1% |
| Under 2.5 probability edge | +20.1% |
| Raw edge prob home | -0.1332 |
| Raw ev home | -0.2370 |
| Raw edge prob draw | 0.0520 |
| Raw ev draw | 0.3506 |
| Raw edge prob away | 0.0813 |
| Raw ev away | 0.4321 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Real Betis win** at **36.4%**. Expected goals are 1.33 for Celta Vigo and 1.28 for Real Betis (2.61 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 48.2%; Under 3.5 goals: 73.4%; Double Chance 1X: 63.6%; Double Chance X2: 63.9%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 87.7%; BTTS Yes (both teams score): 53.5%; BTTS No (at least one team does not score): 46.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 36.1% | 2.77 |
| Draw | 27.5% | 3.63 |
| Real Betis win | 36.4% | 2.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.33 |
| Real Betis expected goals | 1.28 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.2% |
| Under 2.5 | 51.8% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.3% |
| Under 4.5 | 87.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.10% |
| 2 | 0-1 | 9.41% |
| 3 | 1-0 | 9.12% |
| 4 | 1-2 | 8.22% |
| 5 | 2-1 | 7.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 36.1% | 34.5% | 2.81 | +1.4% |
| Draw | 27.5% | 28.2% | 3.57 | -1.8% |
| Real Betis win | 36.4% | 37.3% | 2.67 | -2.8% |
| Over 2.5 | 48.2% | 50.6% | 1.91 | -8.0% |
| Under 2.5 | 51.8% | 49.4% | 2.05 | +6.2% |

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
| Market best home last update utc | 2026-10-20T05:41:37Z |
| Market best draw last update utc | 2026-10-20T05:41:18Z |
| Market best away last update utc | 2026-10-20T05:41:18Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3278 |
| Dc lambda away | 1.2827 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:08.788208+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.5% |
| P btts no | 46.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.83 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.11 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 37.7% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 53.4% |
| P home draw | 63.6% |
| P draw away | 63.9% |
| P home away | 72.5% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.3% |
| Raw p home away | 73.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:56Z |
| Market reference home last update utc | 2026-10-20T05:41:56Z |
| Market reference draw last update utc | 2026-10-20T05:41:56Z |
| Market reference away last update utc | 2026-10-20T05:41:56Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.89 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market best over 2 5 last update utc | 2026-10-20T05:41:18Z |
| Market best under 2 5 last update utc | 2026-10-20T05:41:37Z |
| Home probability edge | +1.6% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | 0.0315 |
| Raw ev home | 0.0581 |
| Raw edge prob draw | -0.0144 |
| Raw ev draw | -0.0433 |
| Raw edge prob away | -0.0171 |
| Raw ev away | -0.0510 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **58.0%**. Expected goals are 2.01 for Real Sociedad and 1.04 for Levante (3.05 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 58.5%; Under 3.5 goals: 63.8%; Double Chance 1X: 80.3%; Double Chance X2: 42.0%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 56.5%; BTTS No (at least one team does not score): 43.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 58.0% | 1.72 |
| Draw | 22.3% | 4.48 |
| Levante win | 19.7% | 5.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 2.01 |
| Levante expected goals | 1.04 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 58.5% |
| Under 2.5 | 41.5% |
| Over 3.5 | 36.2% |
| Under 3.5 | 63.8% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.44% |
| 2 | 2-1 | 9.70% |
| 3 | 2-0 | 9.29% |
| 4 | 1-0 | 9.09% |
| 5 | 3-1 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 58.0% | 56.5% | 1.76 | +2.1% |
| Draw | 22.3% | 23.0% | 4.26 | -4.9% |
| Levante win | 19.7% | 20.4% | 4.72 | -7.1% |
| Over 2.5 | 58.5% | 60.7% | 1.71 | -0.0% |
| Under 2.5 | 41.5% | 39.3% | 2.32 | -3.6% |

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
| Market best home last update utc | 2026-10-20T05:41:18Z |
| Market best draw last update utc | 2026-10-20T05:41:18Z |
| Market best away last update utc | 2026-10-20T05:41:18Z |
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
| Bbs statistics cutoff utc | 2026-10-20T05:42:08.788208+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.64 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.23 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 59.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 18.9% |
| Raw p over 1 5 | 81.0% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 56.3% |
| P home draw | 80.3% |
| P draw away | 42.0% |
| P home away | 77.7% |
| Raw p home draw | 81.1% |
| Raw p draw away | 40.6% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.73 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:56Z |
| Market reference home last update utc | 2026-10-20T05:41:56Z |
| Market reference draw last update utc | 2026-10-20T05:41:56Z |
| Market reference away last update utc | 2026-10-20T05:41:56Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market best over 2 5 last update utc | 2026-10-20T05:41:18Z |
| Market best under 2 5 last update utc | 2026-10-20T05:41:18Z |
| Home probability edge | +1.5% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | 0.0291 |
| Raw ev home | 0.0462 |
| Raw edge prob draw | -0.0142 |
| Raw ev draw | -0.0792 |
| Raw edge prob away | -0.0149 |
| Raw ev away | -0.1059 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **49.4%**. Expected goals are 1.48 for Sevilla and 0.98 for CA Osasuna (2.46 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.5%; Double Chance 1X: 76.4%; Double Chance X2: 50.6%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.6%; BTTS No (at least one team does not score): 51.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 49.4% | 2.03 |
| Draw | 27.1% | 3.69 |
| CA Osasuna win | 23.6% | 4.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.48 |
| CA Osasuna expected goals | 0.98 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
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
| 1 | 1-1 | 12.81% |
| 2 | 1-0 | 12.60% |
| 3 | 2-0 | 9.52% |
| 4 | 2-1 | 9.32% |
| 5 | 0-0 | 8.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 49.4% | 50.1% | 2.02 | -0.3% |
| Draw | 27.1% | 27.5% | 3.60 | -2.5% |
| CA Osasuna win | 23.6% | 22.4% | 4.12 | -3.0% |
| Over 2.5 | 44.6% | 44.2% | 2.19 | -2.4% |
| Under 2.5 | 55.4% | 55.8% | 1.79 | -0.8% |

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
| Market best home last update utc | 2026-10-20T05:41:18Z |
| Market best draw last update utc | 2026-10-20T05:41:18Z |
| Market best away last update utc | 2026-10-20T05:41:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.4831 |
| Dc lambda away | 0.9792 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:08.788208+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.6% |
| P btts no | 51.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.24 |
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
| P home draw | 76.4% |
| P draw away | 50.6% |
| P home away | 72.9% |
| Raw p home draw | 75.3% |
| Raw p draw away | 51.4% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.94 |
| Reference draw odds | 3.45 |
| Reference away odds | 4.20 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:56Z |
| Market reference home last update utc | 2026-10-20T05:41:56Z |
| Market reference draw last update utc | 2026-10-20T05:41:56Z |
| Market reference away last update utc | 2026-10-20T05:41:56Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:56Z |
| Market best over 2 5 last update utc | 2026-10-20T05:41:18Z |
| Market best under 2 5 last update utc | 2026-10-20T05:41:18Z |
| Home probability edge | -0.7% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | -0.0149 |
| Raw ev home | -0.0179 |
| Raw edge prob draw | -0.0083 |
| Raw ev draw | -0.0401 |
| Raw edge prob away | 0.0232 |
| Raw ev away | 0.0182 |

</details>


---
