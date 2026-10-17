# Ligue 1 — football model report

Fixtures in this report: **17**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 973 |
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
| Training sha256 | 75ebaa9e6571ba3c4633ccd8bd8ebb0826422e54cfea55e8c4bce399057271f8 |
| Training as of utc | 2026-10-17T14:11:04.884519+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 55, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 55, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-17T14:11:04.884519+00:00', 'observations': 55, 'observations_sha256': '300682fa8e5854576dee3422fe0572df2b8211a19842d66fb266e02d1f9b6c6d', 'eligible_training_matches': 10, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 39, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 10, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'dd631ec61de7fe08a005e919879687723ae0fe311137e97bc492a0202dca4168', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 1674.211 |
| Base scoring parameter | 0.195 |
| Home-advantage parameter | 0.198 |
| Dixon-Coles low-score adjustment | -0.043 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-16', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 17.00 |
| Additional event odds calls used before this league | 24.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261017T141104884519Z_a4a70a8640c871495e9239864f899987f652bb3fcfdf76880bfcbdb2fc0b441c.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **53.0%**. Expected goals are 1.76 for Lille and 0.96 for Brest (2.72 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.2%; Double Chance 1X: 77.5%; Double Chance X2: 47.0%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 53.0% | 1.89 |
| Draw | 24.5% | 4.08 |
| Brest win | 22.5% | 4.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.76 |
| Brest expected goals | 0.96 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.7% |
| Under 1.5 | 24.3% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.67% |
| 2 | 1-0 | 10.59% |
| 3 | 2-0 | 9.70% |
| 4 | 2-1 | 9.34% |
| 5 | 0-0 | 7.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 53.0% | 50.5% | 1.99 | +5.5% |
| Draw | 24.5% | 24.6% | 3.88 | -5.0% |
| Brest win | 22.5% | 25.0% | 3.90 | -12.3% |
| Over 2.5 | 50.9% | 55.4% | 1.77 | -9.9% |
| Under 2.5 | 49.1% | 44.6% | 2.22 | +8.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | ad25a350c89b64715e15c59cde5653d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7570 |
| Dc lambda away | 0.9627 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.09 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.47 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.20 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 55.6% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 20.0% |
| Raw p over 1 5 | 76.0% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 51.6% |
| P home draw | 77.5% |
| P draw away | 47.0% |
| P home away | 75.5% |
| Raw p home draw | 80.0% |
| Raw p draw away | 44.4% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | +2.6% |
| Draw probability edge | -0.1% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | 0.0512 |
| Raw ev home | 0.1061 |
| Raw edge prob draw | -0.0020 |
| Raw ev draw | -0.0537 |
| Raw edge prob away | -0.0493 |
| Raw ev away | -0.2189 |
| Market p home draw | 73.3% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:08Z |
| Market reference home draw last update utc | 2026-10-17T09:10:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.1% |
| Market draw away odds | 1.91 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:08Z |
| Market reference draw away last update utc | 2026-10-17T09:10:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.6% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:08Z |
| Market reference home away last update utc | 2026-10-17T09:10:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.85 |
| Market reference dc home draw odds | 1.29 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 79.0% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:10:24Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:51Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.7% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:10:24Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:51Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:08Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-17T09:10:29Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **64.1%**. Expected goals are 1.22 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.8%; Under 3.5 goals: 56.7%; Double Chance 1X: 35.9%; Double Chance X2: 83.0%; Double Chance 12 (either team wins): 81.1%; Under 4.5 goals: 75.0%; BTTS Yes (both teams score): 61.4%; BTTS No (at least one team does not score): 38.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.0% | 5.89 |
| Draw | 18.9% | 5.28 |
| Paris Saint Germain win | 64.1% | 1.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.22 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.8% |
| Under 2.5 | 34.2% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.90% |
| 2 | 0-2 | 8.90% |
| 3 | 1-1 | 8.46% |
| 4 | 0-1 | 8.02% |
| 5 | 1-3 | 7.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.0% | 12.7% | 6.81 | +15.7% |
| Draw | 18.9% | 16.3% | 5.54 | +5.0% |
| Paris Saint Germain win | 64.1% | 71.0% | 1.45 | -7.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T15:15:00+00:00 |
| Fixture id | f3034246520a2ee4ff0ac0d5074966f8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Strasbourg |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2248 |
| Dc lambda away | 2.1019 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.4% |
| P btts no | 38.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.57 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.80 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.92 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.00 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 57.1% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.4% |
| Raw p btts yes | 62.4% |
| P home draw | 35.9% |
| P draw away | 83.0% |
| P home away | 81.1% |
| Raw p home draw | 42.9% |
| Raw p draw away | 78.7% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 6.40 |
| Reference draw odds | 5.10 |
| Reference away odds | 1.36 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.31 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:32Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:32Z |
| Home probability edge | +4.3% |
| Draw probability edge | +2.6% |
| Away probability edge | -7.0% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | 0.0863 |
| Raw ev home | 0.4507 |
| Raw edge prob draw | 0.0527 |
| Raw ev draw | 0.1958 |
| Raw edge prob away | -0.1391 |
| Raw ev away | -0.1719 |
| Market p home draw | 35.0% |
| Market home draw odds | 2.96 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:08Z |
| Market reference home draw last update utc | 2026-10-17T09:10:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.3% |
| Market draw away odds | 1.13 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:08Z |
| Market reference draw away last update utc | 2026-10-17T09:10:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.7% |
| Market home away odds | 1.18 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:08Z |
| Market reference home away last update utc | 2026-10-17T09:10:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.12 |
| Market reference dc home draw odds | 2.70 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 89.2% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:09:29Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 7.60 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:51Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.3% |
| Market under 3 5 odds | 2.06 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:09:29Z |
| Market reference under 3 5 odds | 1.97 |
| Market reference under 3 5 opposite odds | 1.92 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:51Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.5% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:08Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.60 |
| Market reference btts yes last update utc | 2026-10-17T09:10:29Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **63.0%**. Expected goals are 0.64 for Troyes and 2.21 for RC Lens (2.84 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 51.7%; Under 3.5 goals: 70.2%; Double Chance 1X: 37.0%; Double Chance X2: 83.9%; Double Chance 12 (either team wins): 79.0%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 43.8%; BTTS No (at least one team does not score): 56.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 16.1% | 6.23 |
| Draw | 21.0% | 4.77 |
| RC Lens win | 63.0% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.64 |
| RC Lens expected goals | 2.21 |
| Expected total goals | 2.84 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 51.7% |
| Under 2.5 | 48.3% |
| Over 3.5 | 29.8% |
| Under 3.5 | 70.2% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.23% |
| 2 | 0-1 | 10.79% |
| 3 | 1-1 | 9.90% |
| 4 | 0-3 | 8.99% |
| 5 | 1-2 | 7.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 16.1% | 23.2% | 4.09 | -34.3% |
| Draw | 21.0% | 23.9% | 3.98 | -16.5% |
| RC Lens win | 63.0% | 52.9% | 1.92 | +20.9% |
| Over 2.5 | 51.7% | 62.6% | 1.66 | -14.2% |
| Under 2.5 | 48.3% | 37.4% | 2.42 | +16.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | b077aa049133c0358bcd643bfee48da3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6361 |
| Dc lambda away | 2.2061 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 43.8% |
| P btts no | 56.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.94 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.16 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.36 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.80 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 8.9% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 73.0% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 42.2% |
| P home draw | 37.0% |
| P draw away | 83.9% |
| P home away | 79.0% |
| Raw p home draw | 27.0% |
| Raw p draw away | 91.1% |
| Raw p home away | 81.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 3.85 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.80 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | -7.2% |
| Draw probability edge | -2.9% |
| Away probability edge | +10.1% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | -0.1432 |
| Raw ev home | -0.6363 |
| Raw edge prob draw | -0.0581 |
| Raw ev draw | -0.2807 |
| Raw edge prob away | 0.2014 |
| Raw ev away | 0.4023 |
| Market p home draw | 49.1% |
| Market home draw odds | 1.98 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:08Z |
| Market reference home draw last update utc | 2026-10-17T09:10:31Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.4% |
| Market draw away odds | 1.28 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:08Z |
| Market reference draw away last update utc | 2026-10-17T09:10:31Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:08Z |
| Market reference home away last update utc | 2026-10-17T09:10:31Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.29 |
| Market reference dc home draw odds | 1.98 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.8% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:09:15Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:51Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:09:15Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.56 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:51Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.7% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:08Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.48 |
| Market reference btts yes last update utc | 2026-10-17T09:10:31Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **50.9%**. Expected goals are 0.94 for Angers and 1.71 for Marseille (2.66 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.7%; Double Chance 1X: 49.1%; Double Chance X2: 75.9%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 24.1% | 4.15 |
| Draw | 25.0% | 4.01 |
| Marseille win | 50.9% | 1.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.94 |
| Marseille expected goals | 1.71 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 74.5% |
| Under 1.5 | 25.5% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 27.3% |
| Under 3.5 | 72.7% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.90% |
| 2 | 0-1 | 10.67% |
| 3 | 0-2 | 9.53% |
| 4 | 1-2 | 9.00% |
| 5 | 0-0 | 7.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 24.1% | 28.0% | 3.56 | -14.2% |
| Draw | 25.0% | 25.1% | 3.82 | -4.6% |
| Marseille win | 50.9% | 46.8% | 2.12 | +8.0% |
| Over 2.5 | 49.3% | 61.6% | 1.67 | -17.7% |
| Under 2.5 | 50.7% | 38.4% | 2.40 | +21.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | c7a60aa94470fe959fbf6b0c68060fc1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9439 |
| Dc lambda away | 1.7144 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.27 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.92 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.66 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.75 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 55.0% |
| Raw p over 1 5 | 74.9% |
| Raw p under 3 5 | 72.3% |
| Raw p btts yes | 50.6% |
| P home draw | 49.1% |
| P draw away | 75.9% |
| P home away | 75.0% |
| Raw p home draw | 45.0% |
| Raw p draw away | 79.8% |
| Raw p home away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 3.25 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.02 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | -3.9% |
| Draw probability edge | -0.1% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -12.3% |
| Under 2.5 probability edge | +12.3% |
| Raw edge prob home | -0.0789 |
| Raw ev home | -0.2825 |
| Raw edge prob draw | -0.0030 |
| Raw ev draw | -0.0519 |
| Raw edge prob away | 0.0819 |
| Raw ev away | 0.1666 |
| Market p home draw | 52.7% |
| Market home draw odds | 1.81 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:08Z |
| Market reference home draw last update utc | 2026-10-17T09:10:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.5% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:08Z |
| Market reference draw away last update utc | 2026-10-17T09:10:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.8% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:08Z |
| Market reference home away last update utc | 2026-10-17T09:10:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home draw odds | 1.83 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.7% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:10:22Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:51Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:10:22Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:51Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.4% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:08Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.51 |
| Market reference btts yes last update utc | 2026-10-17T09:10:33Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **38.7%**. Expected goals are 1.17 for Le Havre and 1.17 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 41.9%; Under 3.5 goals: 79.0%; Double Chance 1X: 66.8%; Double Chance X2: 61.3%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 47.9%; BTTS No (at least one team does not score): 52.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 38.7% | 2.58 |
| Draw | 28.1% | 3.56 |
| Auxerre win | 33.2% | 3.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.17 |
| Auxerre expected goals | 1.17 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 68.5% |
| Under 1.5 | 31.5% |
| Over 2.5 | 41.9% |
| Under 2.5 | 58.1% |
| Over 3.5 | 21.0% |
| Under 3.5 | 79.0% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.24% |
| 2 | 1-0 | 11.69% |
| 3 | 0-1 | 10.03% |
| 4 | 0-0 | 9.80% |
| 5 | 2-1 | 8.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 38.7% | 42.0% | 2.42 | -6.3% |
| Draw | 28.1% | 27.0% | 3.51 | -1.3% |
| Auxerre win | 33.2% | 31.0% | 3.14 | +4.1% |
| Over 2.5 | 41.9% | 51.0% | 1.95 | -18.4% |
| Under 2.5 | 58.1% | 49.0% | 1.99 | +15.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | d637845b9760bb02b55bbbaa32b5c21e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Havre |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1727 |
| Dc lambda away | 1.1691 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 47.9% |
| P btts no | 52.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.20 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.39 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.77 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.15 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 35.5% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.3% |
| Raw p over 1 5 | 68.4% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 48.2% |
| P home draw | 66.8% |
| P draw away | 61.3% |
| P home away | 71.9% |
| Raw p home draw | 64.7% |
| Raw p draw away | 64.5% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.23 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | -3.2% |
| Draw probability edge | +1.1% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -9.2% |
| Under 2.5 probability edge | +9.2% |
| Raw edge prob home | -0.0649 |
| Raw ev home | -0.1412 |
| Raw edge prob draw | 0.0218 |
| Raw ev draw | 0.0249 |
| Raw edge prob away | 0.0431 |
| Raw ev away | 0.1088 |
| Market p home draw | 69.9% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:08Z |
| Market reference home draw last update utc | 2026-10-17T09:10:31Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.1% |
| Market draw away odds | 1.63 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:08Z |
| Market reference draw away last update utc | 2026-10-17T09:10:31Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.0% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:08Z |
| Market reference home away last update utc | 2026-10-17T09:10:31Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.66 |
| Market reference dc home draw odds | 1.38 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 75.1% |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.56 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:51Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 72.1% |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.23 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:51Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.3% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:08Z |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.23 |
| Market reference btts yes last update utc | 2026-10-17T09:10:31Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **47.4%**. Expected goals are 1.37 for Lorient and 1.81 for AS Monaco (3.18 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.1%; Under 3.5 goals: 60.7%; Double Chance 1X: 52.6%; Double Chance X2: 72.8%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 27.2% | 3.68 |
| Draw | 25.4% | 3.94 |
| AS Monaco win | 47.4% | 2.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.37 |
| AS Monaco expected goals | 1.81 |
| Expected total goals | 3.18 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.1% |
| Under 2.5 | 38.9% |
| Over 3.5 | 39.3% |
| Under 3.5 | 60.7% |
| Over 4.5 | 21.3% |
| Under 4.5 | 78.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.47% |
| 2 | 1-2 | 9.31% |
| 3 | 0-1 | 7.07% |
| 4 | 2-2 | 6.82% |
| 5 | 0-2 | 6.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 27.2% | 25.8% | 3.87 | +5.2% |
| Draw | 25.4% | 27.0% | 3.58 | -9.1% |
| AS Monaco win | 47.4% | 47.2% | 2.10 | -0.4% |
| Over 2.5 | 61.1% | 50.3% | 1.97 | +20.3% |
| Under 2.5 | 38.9% | 49.7% | 1.97 | -23.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | 53f5fe7ed0ba0fbf6345c73270e4cd00 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lorient |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3669 |
| Dc lambda away | 1.8139 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.37 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.90 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.57 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.69 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 28.6% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 47.6% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 60.7% |
| Raw p btts yes | 62.8% |
| P home draw | 52.6% |
| P draw away | 72.8% |
| P home away | 74.6% |
| Raw p home draw | 52.4% |
| Raw p draw away | 71.4% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | +1.4% |
| Draw probability edge | -1.6% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | +10.7% |
| Under 2.5 probability edge | -10.7% |
| Raw edge prob home | 0.0284 |
| Raw ev home | 0.1069 |
| Raw edge prob draw | -0.0323 |
| Raw ev draw | -0.1484 |
| Raw edge prob away | 0.0039 |
| Raw ev away | -0.0002 |
| Market p home draw | 52.9% |
| Market home draw odds | 1.82 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:08Z |
| Market reference home draw last update utc | 2026-10-17T09:10:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.7% |
| Market draw away odds | 1.30 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:08Z |
| Market reference draw away last update utc | 2026-10-17T09:10:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.4% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:08Z |
| Market reference home away last update utc | 2026-10-17T09:10:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.29 |
| Market reference dc home draw odds | 1.82 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 73.9% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:09:15Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.42 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:51Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.3% |
| Market under 3 5 odds | 1.30 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:09:15Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.35 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:51Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.3% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:08Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.05 |
| Market reference btts yes last update utc | 2026-10-17T09:10:29Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **55.9%**. Expected goals are 1.77 for Lyon and 1.09 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 54.8%; Under 3.5 goals: 67.6%; Double Chance 1X: 79.6%; Double Chance X2: 44.1%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 83.7%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 55.9% | 1.79 |
| Draw | 23.7% | 4.22 |
| Nice win | 20.4% | 4.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.77 |
| Nice expected goals | 1.09 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.6% |
| Under 1.5 | 21.4% |
| Over 2.5 | 54.8% |
| Under 2.5 | 45.2% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.3% |
| Under 4.5 | 83.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.22% |
| 2 | 2-1 | 10.32% |
| 3 | 1-0 | 10.22% |
| 4 | 2-0 | 9.50% |
| 5 | 3-1 | 6.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 55.9% | 58.8% | 1.71 | -4.4% |
| Draw | 23.7% | 23.1% | 4.26 | +0.9% |
| Nice win | 20.4% | 18.2% | 5.13 | +4.8% |
| Over 2.5 | 54.8% | 56.5% | 1.72 | -5.8% |
| Under 2.5 | 45.2% | 43.5% | 2.31 | +4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T18:45:00+00:00 |
| Fixture id | 471f891b1f6516a864ad94c8eb649f5e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lyon |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7729 |
| Dc lambda away | 1.0860 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.54 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.66 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.12 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 53.0% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| P home draw | 79.6% |
| P draw away | 44.1% |
| P home away | 76.3% |
| Raw p home draw | 77.3% |
| Raw p draw away | 47.0% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.63 |
| Reference draw odds | 3.85 |
| Reference away odds | 4.80 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | -2.9% |
| Draw probability edge | +0.6% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0579 |
| Raw ev home | -0.0939 |
| Raw edge prob draw | 0.0124 |
| Raw ev draw | 0.0359 |
| Raw edge prob away | 0.0454 |
| Raw ev away | 0.1644 |
| Market p home draw | 81.0% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:08Z |
| Market reference home draw last update utc | 2026-10-17T09:10:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.5% |
| Market draw away odds | 2.27 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:08Z |
| Market reference draw away last update utc | 2026-10-17T09:10:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.5% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:08Z |
| Market reference home away last update utc | 2026-10-17T09:10:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.27 |
| Market reference dc home draw odds | 1.19 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:51Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.9% |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:51Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:08Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-17T09:10:29Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **42.6%**. Expected goals are 1.57 for Paris FC and 1.37 for Rennes (2.94 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 56.0%; Under 3.5 goals: 66.1%; Double Chance 1X: 68.9%; Double Chance X2: 57.4%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 82.6%; BTTS Yes (both teams score): 59.7%; BTTS No (at least one team does not score): 40.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 42.6% | 2.35 |
| Draw | 26.3% | 3.80 |
| Rennes win | 31.1% | 3.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.57 |
| Rennes expected goals | 1.37 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 79.7% |
| Under 1.5 | 20.3% |
| Over 2.5 | 56.0% |
| Under 2.5 | 44.0% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.4% |
| Under 4.5 | 82.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.27% |
| 2 | 2-1 | 9.09% |
| 3 | 1-0 | 7.95% |
| 4 | 1-2 | 7.39% |
| 5 | 2-0 | 6.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 42.6% | 43.2% | 2.37 | +0.9% |
| Draw | 26.3% | 27.2% | 3.45 | -9.2% |
| Rennes win | 31.1% | 29.6% | 3.29 | +2.4% |
| Over 2.5 | 56.0% | 59.3% | 1.72 | -3.6% |
| Under 2.5 | 44.0% | 40.7% | 2.30 | +1.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | 27f7222d2abde93fc6e8d17b5b05b272 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paris FC |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5744 |
| Dc lambda away | 1.3658 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.7% |
| P btts no | 40.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.73 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.92 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.76 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 41.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.1% |
| Raw p btts yes | 59.5% |
| P home draw | 68.9% |
| P draw away | 57.4% |
| P home away | 73.7% |
| Raw p home draw | 67.3% |
| Raw p draw away | 58.1% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.18 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | -0.6% |
| Draw probability edge | -0.9% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | -0.0130 |
| Raw ev home | -0.0066 |
| Raw edge prob draw | -0.0180 |
| Raw ev draw | -0.1234 |
| Raw edge prob away | 0.0310 |
| Raw ev away | 0.0750 |
| Market p home draw | 70.3% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:08Z |
| Market reference home draw last update utc | 2026-10-17T09:10:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.4% |
| Market draw away odds | 1.66 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:08Z |
| Market reference draw away last update utc | 2026-10-17T09:10:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.3% |
| Market home away odds | 1.36 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:08Z |
| Market reference home away last update utc | 2026-10-17T09:10:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.65 |
| Market reference dc home draw odds | 1.37 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:51Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.9% |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:51Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 64.1% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:08Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.63 |
| Market reference btts yes last update utc | 2026-10-17T09:10:31Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **43.5%**. Expected goals are 1.56 for Brest and 1.28 for Nice (2.84 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.9%; Under 3.5 goals: 68.3%; Double Chance 1X: 69.5%; Double Chance X2: 56.5%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 57.6%; BTTS No (at least one team does not score): 42.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 43.5% | 2.30 |
| Draw | 26.1% | 3.84 |
| Nice win | 30.5% | 3.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Nice expected goals | 1.28 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 31.7% |
| Under 3.5 | 68.3% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.29% |
| 2 | 2-1 | 9.12% |
| 3 | 1-0 | 8.64% |
| 4 | 1-2 | 7.38% |
| 5 | 2-0 | 7.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 43.5% | 43.6% | 2.31 | +0.4% |
| Draw | 26.1% | 26.3% | 3.49 | -9.0% |
| Nice win | 30.5% | 30.1% | 3.37 | +2.7% |
| Over 2.5 | 53.9% | 57.6% | 1.76 | -5.2% |
| Under 2.5 | 46.1% | 42.4% | 2.23 | +2.8% |

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
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brest |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5576 |
| Dc lambda away | 1.2811 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.6% |
| P btts no | 42.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.59 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.55 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.16 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.32 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 30.9% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 57.5% |
| P home draw | 69.5% |
| P draw away | 56.5% |
| P home away | 73.9% |
| Raw p home draw | 69.1% |
| Raw p draw away | 56.7% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.16 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | -0.2% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | -0.0030 |
| Raw ev home | 0.0004 |
| Raw edge prob draw | -0.0051 |
| Raw ev draw | -0.0991 |
| Raw edge prob away | 0.0081 |
| Raw ev away | 0.0407 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **49.1%**. Expected goals are 1.58 for RC Lens and 1.00 for Paris FC (2.58 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.1%; Under 3.5 goals: 74.0%; Double Chance 1X: 74.1%; Double Chance X2: 50.9%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 49.1% | 2.04 |
| Draw | 25.0% | 4.00 |
| Paris FC win | 25.9% | 3.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.58 |
| Paris FC expected goals | 1.00 |
| Expected total goals | 2.58 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 73.4% |
| Under 1.5 | 26.6% |
| Over 2.5 | 48.1% |
| Under 2.5 | 51.9% |
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.91% |
| 2 | 1-0 | 11.15% |
| 3 | 2-1 | 9.24% |
| 4 | 2-0 | 9.21% |
| 5 | 0-1 | 7.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 49.1% | 47.9% | 2.09 | +2.6% |
| Draw | 25.0% | 23.8% | 3.90 | -2.4% |
| Paris FC win | 25.9% | 28.3% | 3.58 | -7.3% |
| Over 2.5 | 48.1% | 61.1% | 1.68 | -19.2% |
| Under 2.5 | 51.9% | 38.9% | 2.38 | +23.6% |

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
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5805 |
| Dc lambda away | 1.0032 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.00 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.76 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.26 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 50.3% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 50.8% |
| P home draw | 74.1% |
| P draw away | 50.9% |
| P home away | 75.0% |
| Raw p home draw | 76.5% |
| Raw p draw away | 49.7% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.97 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.17 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | +1.2% |
| Draw probability edge | +1.2% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -13.0% |
| Under 2.5 probability edge | +13.0% |
| Raw edge prob home | 0.0236 |
| Raw ev home | 0.0505 |
| Raw edge prob draw | 0.0240 |
| Raw ev draw | 0.0224 |
| Raw edge prob away | -0.0476 |
| Raw ev away | -0.1579 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **66.6%**. Expected goals are 2.32 for Toulouse and 0.61 for Troyes (2.94 combined). The most likely exact score is 2-0 at 12.6%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 54.0%; Under 3.5 goals: 68.1%; Double Chance 1X: 86.0%; Double Chance X2: 33.4%; Double Chance 12 (either team wins): 80.6%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 43.2%; BTTS No (at least one team does not score): 56.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 66.6% | 1.50 |
| Draw | 19.4% | 5.15 |
| Troyes win | 14.0% | 7.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 2.32 |
| Troyes expected goals | 0.61 |
| Expected total goals | 2.94 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 54.0% |
| Under 2.5 | 46.0% |
| Over 3.5 | 31.9% |
| Under 3.5 | 68.1% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.61% |
| 2 | 1-0 | 10.58% |
| 3 | 3-0 | 9.76% |
| 4 | 1-1 | 9.19% |
| 5 | 2-1 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 66.6% | 57.6% | 1.75 | +16.5% |
| Draw | 19.4% | 22.1% | 4.21 | -18.2% |
| Troyes win | 14.0% | 20.2% | 4.88 | -31.6% |
| Over 2.5 | 54.0% | 60.6% | 1.69 | -8.8% |
| Under 2.5 | 46.0% | 39.4% | 2.36 | +8.6% |

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
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3206 |
| Dc lambda away | 0.6144 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 43.2% |
| P btts no | 56.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.25 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.46 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.13 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.17 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 75.5% |
| Unadjusted draw probability | 16.7% |
| Unadjusted away-win probability | 7.8% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 66.2% |
| Raw p btts yes | 41.7% |
| P home draw | 86.0% |
| P draw away | 33.4% |
| P home away | 80.6% |
| Raw p home draw | 92.2% |
| Raw p draw away | 24.5% |
| Raw p home away | 83.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.66 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.35 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | +8.9% |
| Draw probability edge | -2.7% |
| Away probability edge | -6.2% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | 0.1786 |
| Raw ev home | 0.3211 |
| Raw edge prob draw | -0.0544 |
| Raw ev draw | -0.2967 |
| Raw edge prob away | -0.1242 |
| Raw ev away | -0.6194 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **43.5%**. Expected goals are 1.46 for AS Monaco and 1.27 for Lille (2.73 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 51.5%; Under 3.5 goals: 70.7%; Double Chance 1X: 69.7%; Double Chance X2: 56.5%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 85.8%; BTTS Yes (both teams score): 55.6%; BTTS No (at least one team does not score): 44.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 43.5% | 2.30 |
| Draw | 26.2% | 3.82 |
| Lille win | 30.3% | 3.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.46 |
| Lille expected goals | 1.27 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 76.2% |
| Under 1.5 | 23.8% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 29.3% |
| Under 3.5 | 70.7% |
| Over 4.5 | 14.2% |
| Under 4.5 | 85.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.45% |
| 2 | 1-0 | 9.51% |
| 3 | 2-1 | 9.31% |
| 4 | 2-0 | 7.36% |
| 5 | 0-1 | 7.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 43.5% | 45.6% | 2.18 | -5.3% |
| Draw | 26.2% | 25.9% | 3.60 | -5.6% |
| Lille win | 30.3% | 28.5% | 3.60 | +9.2% |
| Over 2.5 | 51.5% | 57.6% | 1.77 | -8.8% |
| Under 2.5 | 48.5% | 42.4% | 2.22 | +7.7% |

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
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monaco |
| Matched away-team name | Lille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4647 |
| Dc lambda away | 1.2650 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.6% |
| P btts no | 44.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.38 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.21 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.41 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.03 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 41.3% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 32.2% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.8% |
| Raw p btts yes | 55.7% |
| P home draw | 69.7% |
| P draw away | 56.5% |
| P home away | 73.8% |
| Raw p home draw | 67.8% |
| Raw p draw away | 58.7% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.07 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | -2.2% |
| Draw probability edge | +0.3% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.0431 |
| Raw ev home | -0.0996 |
| Raw edge prob draw | 0.0066 |
| Raw ev draw | -0.0444 |
| Raw edge prob away | 0.0365 |
| Raw ev away | 0.1576 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **37.0%**. Expected goals are 1.10 for Angers and 1.24 for Lorient (2.34 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 41.4%; Under 3.5 goals: 79.2%; Double Chance 1X: 63.0%; Double Chance X2: 65.8%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 91.2%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 34.2% | 2.93 |
| Draw | 28.8% | 3.47 |
| Lorient win | 37.0% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.10 |
| Lorient expected goals | 1.24 |
| Expected total goals | 2.34 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 68.3% |
| Under 1.5 | 31.7% |
| Over 2.5 | 41.4% |
| Under 2.5 | 58.6% |
| Over 3.5 | 20.8% |
| Under 3.5 | 79.2% |
| Over 4.5 | 8.8% |
| Under 4.5 | 91.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.57% |
| 2 | 0-1 | 10.84% |
| 3 | 1-0 | 10.75% |
| 4 | 0-0 | 10.13% |
| 5 | 1-2 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 34.2% | 36.5% | 2.69 | -8.1% |
| Draw | 28.8% | 28.6% | 3.40 | -1.9% |
| Lorient win | 37.0% | 35.0% | 2.85 | +5.4% |
| Over 2.5 | 41.4% | 45.3% | 2.19 | -9.3% |
| Under 2.5 | 58.6% | 54.7% | 1.79 | +4.8% |

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
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Lorient |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0960 |
| Dc lambda away | 1.2404 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.87 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.15 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.81 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.34 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 29.1% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 68.3% |
| Raw p under 3 5 | 79.2% |
| Raw p btts yes | 47.9% |
| P home draw | 63.0% |
| P draw away | 65.8% |
| P home away | 71.2% |
| Raw p home draw | 61.0% |
| Raw p draw away | 68.1% |
| Raw p home away | 70.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.55 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.65 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.65 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | -2.3% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0458 |
| Raw ev home | -0.1422 |
| Raw edge prob draw | 0.0059 |
| Raw ev draw | -0.0093 |
| Raw edge prob away | 0.0399 |
| Raw ev away | 0.1107 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **45.8%**. Expected goals are 1.83 for Auxerre and 1.40 for Le Mans FC (3.22 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 61.9%; Under 3.5 goals: 59.9%; Double Chance 1X: 70.8%; Double Chance X2: 54.2%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 45.8% | 2.19 |
| Draw | 25.1% | 3.99 |
| Le Mans FC win | 29.2% | 3.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.83 |
| Le Mans FC expected goals | 1.40 |
| Expected total goals | 3.22 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 83.5% |
| Under 1.5 | 16.5% |
| Over 2.5 | 61.9% |
| Under 2.5 | 38.1% |
| Over 3.5 | 40.1% |
| Under 3.5 | 59.9% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.24% |
| 2 | 2-1 | 8.98% |
| 3 | 1-2 | 7.12% |
| 4 | 2-2 | 6.86% |
| 5 | 1-0 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 45.8% | 44.2% | 2.23 | +2.0% |
| Draw | 25.1% | 26.5% | 3.70 | -7.2% |
| Le Mans FC win | 29.2% | 29.3% | 3.37 | -1.7% |
| Over 2.5 | 61.9% | 54.4% | 1.78 | +10.3% |
| Under 2.5 | 38.1% | 45.6% | 2.20 | -16.3% |

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
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8256 |
| Dc lambda away | 1.3953 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.9% |
| P btts no | 36.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.31 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.07 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.49 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.53 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 23.7% |
| Unadjusted away-win probability | 29.1% |
| Raw p over 1 5 | 83.6% |
| Raw p under 3 5 | 59.8% |
| Raw p btts yes | 63.5% |
| P home draw | 70.8% |
| P draw away | 54.2% |
| P home away | 74.9% |
| Raw p home draw | 70.9% |
| Raw p draw away | 52.7% |
| Raw p home away | 76.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.12 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | +1.5% |
| Draw probability edge | -1.4% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | +7.6% |
| Under 2.5 probability edge | -7.6% |
| Raw edge prob home | 0.0304 |
| Raw ev home | 0.0542 |
| Raw edge prob draw | -0.0282 |
| Raw ev draw | -0.1244 |
| Raw edge prob away | -0.0022 |
| Raw ev away | -0.0205 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **63.8%**. Expected goals are 2.13 for Marseille and 0.86 for Le Havre (2.99 combined). The most likely exact score is 2-0 at 11.0%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 57.2%; Under 3.5 goals: 65.3%; Double Chance 1X: 84.2%; Double Chance X2: 36.2%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 63.8% | 1.57 |
| Draw | 20.5% | 4.89 |
| Le Havre win | 15.8% | 6.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.13 |
| Le Havre expected goals | 0.86 |
| Expected total goals | 2.99 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 80.0% |
| Under 1.5 | 20.0% |
| Over 2.5 | 57.2% |
| Under 2.5 | 42.8% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.99% |
| 2 | 1-0 | 9.93% |
| 3 | 1-1 | 9.72% |
| 4 | 2-1 | 9.46% |
| 5 | 3-0 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 63.8% | 61.4% | 1.64 | +4.6% |
| Draw | 20.5% | 20.7% | 4.57 | -6.5% |
| Le Havre win | 15.8% | 17.9% | 5.33 | -16.0% |
| Over 2.5 | 57.2% | 62.2% | 1.66 | -5.1% |
| Under 2.5 | 42.8% | 37.8% | 2.42 | +3.6% |

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
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1311 |
| Dc lambda away | 0.8604 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.23 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.01 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.52 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 66.2% |
| Unadjusted draw probability | 20.2% |
| Unadjusted away-win probability | 13.6% |
| Raw p over 1 5 | 80.4% |
| Raw p under 3 5 | 64.9% |
| Raw p btts yes | 51.2% |
| P home draw | 84.2% |
| P draw away | 36.2% |
| P home away | 79.5% |
| Raw p home draw | 86.4% |
| Raw p draw away | 33.8% |
| Raw p home away | 79.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.80 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:50Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:08Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:08Z |
| Home probability edge | +2.4% |
| Draw probability edge | -0.3% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | 0.0479 |
| Raw ev home | 0.0854 |
| Raw edge prob draw | -0.0051 |
| Raw ev draw | -0.0767 |
| Raw edge prob away | -0.0428 |
| Raw ev away | -0.2745 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **67.4%**. Expected goals are 2.30 for Paris Saint Germain and 1.06 for Lyon (3.36 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 66.0%; Under 3.5 goals: 56.3%; Double Chance 1X: 85.4%; Double Chance X2: 32.6%; Double Chance 12 (either team wins): 82.0%; Under 4.5 goals: 74.7%; BTTS Yes (both teams score): 58.7%; BTTS No (at least one team does not score): 41.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 67.4% | 1.48 |
| Draw | 18.0% | 5.57 |
| Lyon win | 14.6% | 6.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.30 |
| Lyon expected goals | 1.06 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 66.0% |
| Under 2.5 | 34.0% |
| Over 3.5 | 43.7% |
| Under 3.5 | 56.3% |
| Over 4.5 | 25.3% |
| Under 4.5 | 74.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.12% |
| 2 | 2-0 | 9.54% |
| 3 | 1-1 | 8.14% |
| 4 | 1-0 | 7.91% |
| 5 | 3-1 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 67.4% | 70.0% | 1.43 | -3.6% |
| Draw | 18.0% | 16.5% | 5.44 | -2.3% |
| Lyon win | 14.6% | 13.5% | 7.60 | +11.2% |

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
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3030 |
| Dc lambda away | 1.0615 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 58.7% |
| P btts no | 41.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.34 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.89 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.94 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.95 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 64.8% |
| Unadjusted draw probability | 19.4% |
| Unadjusted away-win probability | 15.7% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 59.2% |
| P home draw | 85.4% |
| P draw away | 32.6% |
| P home away | 82.0% |
| Raw p home draw | 84.3% |
| Raw p draw away | 35.2% |
| Raw p home away | 80.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.38 |
| Reference draw odds | 5.10 |
| Reference away odds | 6.10 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:29Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:29Z |
| Home probability edge | -2.6% |
| Draw probability edge | +1.5% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | -0.0520 |
| Raw ev home | -0.0732 |
| Raw edge prob draw | 0.0297 |
| Raw ev draw | 0.0577 |
| Raw edge prob away | 0.0223 |
| Raw ev away | 0.1965 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **51.9%**. Expected goals are 1.86 for Rennes and 1.49 for Strasbourg (3.34 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 65.4%; Under 3.5 goals: 56.8%; Double Chance 1X: 74.1%; Double Chance X2: 48.1%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 65.3%; BTTS No (at least one team does not score): 34.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 51.9% | 1.93 |
| Draw | 22.2% | 4.50 |
| Strasbourg win | 25.9% | 3.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.86 |
| Strasbourg expected goals | 1.49 |
| Expected total goals | 3.34 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 65.4% |
| Under 2.5 | 34.6% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.20% |
| 2 | 1-1 | 9.69% |
| 3 | 1-0 | 6.92% |
| 4 | 2-0 | 6.86% |
| 5 | 2-2 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 51.9% | 57.7% | 1.70 | -11.8% |
| Draw | 22.2% | 21.1% | 4.57 | +1.5% |
| Strasbourg win | 25.9% | 21.1% | 4.83 | +25.0% |

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
| Market best home last update utc | 2026-10-17T09:10:08Z |
| Market best draw last update utc | 2026-10-17T09:10:08Z |
| Market best away last update utc | 2026-10-17T09:10:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8564 |
| Dc lambda away | 1.4869 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:11:04.884519+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.3% |
| P btts no | 34.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.56 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.89 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.02 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 46.0% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 30.6% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 57.1% |
| Raw p btts yes | 65.7% |
| P home draw | 74.1% |
| P draw away | 48.1% |
| P home away | 77.8% |
| Raw p home draw | 69.4% |
| Raw p draw away | 54.0% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.66 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.20 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:50Z |
| Market reference home last update utc | 2026-10-17T09:10:50Z |
| Market reference draw last update utc | 2026-10-17T09:10:50Z |
| Market reference away last update utc | 2026-10-17T09:10:50Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:29Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:29Z |
| Home probability edge | -5.9% |
| Draw probability edge | +1.1% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -1.4% |
| Under 2.5 probability edge | +1.4% |
| Raw edge prob home | -0.1170 |
| Raw ev home | -0.2172 |
| Raw edge prob draw | 0.0218 |
| Raw ev draw | 0.0651 |
| Raw edge prob away | 0.0952 |
| Raw ev away | 0.4803 |

</details>


---
