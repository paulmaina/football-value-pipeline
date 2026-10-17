# Bundesliga — football model report

Fixtures in this report: **17**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 964 |
| Training data through | 2026-10-16 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | 55c56458ea548a5d0670a302c859faecd8a7cb07bbad6e099edb1d6d98199e8c |
| Training as of utc | 2026-10-17T09:45:16.687359+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 46, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 46, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-17T09:45:16.687359+00:00', 'observations': 47, 'observations_sha256': 'cc0861631709c5d9d1d7ed9e4cfead9f902902a7c8ab568fcd1484a042263577', 'eligible_training_matches': 9, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 37, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 9, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '3889e4fb76130a3eef5a75ab5ee997e7e3a4475ca0163fb9ea9e738b100222ef', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 2920.827 |
| Base scoring parameter | 0.233 |
| Home-advantage parameter | 0.194 |
| Dixon-Coles low-score adjustment | -0.099 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-16', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 17.00 |
| Additional event odds calls used before this league | 19.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261017T094516687359Z_03a052ea377d6f701c3e7c4e2dedb111704cea34552b492aedb3e7d7d8bcf717.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **74.8%**. Expected goals are 2.75 for Bayern Munich and 1.27 for RB Leipzig (4.02 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 77.9%; Under 3.5 goals: 41.9%; Double Chance 1X: 88.8%; Double Chance X2: 25.2%; Double Chance 12 (either team wins): 86.0%; Under 4.5 goals: 61.2%; BTTS Yes (both teams score): 66.7%; BTTS No (at least one team does not score): 33.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 74.8% | 1.34 |
| Draw | 14.0% | 7.13 |
| RB Leipzig win | 11.2% | 8.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.75 |
| RB Leipzig expected goals | 1.27 |
| Expected total goals | 4.02 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 77.9% |
| Under 2.5 | 22.1% |
| Over 3.5 | 58.1% |
| Under 3.5 | 41.9% |
| Over 4.5 | 38.8% |
| Under 4.5 | 61.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.49% |
| 2 | 3-1 | 8.71% |
| 3 | 2-0 | 7.48% |
| 4 | 3-0 | 6.87% |
| 5 | 4-1 | 5.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 74.8% | 81.6% | 1.23 | -8.0% |
| Draw | 14.0% | 10.6% | 8.30 | +16.4% |
| RB Leipzig win | 11.2% | 7.7% | 12.10 | +35.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | 9a64448205fdc4b95f45641bb946706c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Bayern Munich |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7523 |
| Dc lambda away | 1.2678 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 66.7% |
| P btts no | 33.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 51.41 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.55 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.53 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.38 |
| Fair Over 4.5 odds | 2.58 |
| Fair Under 4.5 odds | 1.63 |
| Unadjusted home-win probability | 67.9% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 14.6% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 43.0% |
| Raw p btts yes | 67.9% |
| P home draw | 88.8% |
| P draw away | 25.2% |
| P home away | 86.0% |
| Raw p home draw | 85.4% |
| Raw p draw away | 32.1% |
| Raw p home away | 82.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.20 |
| Reference draw odds | 7.50 |
| Reference away odds | 10.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.12 |
| Reference Under 2.5 odds | 6.00 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Home probability edge | -6.8% |
| Draw probability edge | +3.4% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.1370 |
| Raw ev home | -0.1642 |
| Raw edge prob draw | 0.0678 |
| Raw ev draw | 0.4455 |
| Raw edge prob away | 0.0691 |
| Raw ev away | 0.7710 |
| Market p home draw | 90.4% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:09:18Z |
| Market reference home draw last update utc | 2026-10-17T09:10:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 20.8% |
| Market draw away odds | 4.70 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:09:18Z |
| Market reference draw away last update utc | 2026-10-17T09:10:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.7% |
| Market home away odds | 1.10 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:09:18Z |
| Market reference home away last update utc | 2026-10-17T09:10:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.56 |
| Market reference dc home draw odds | 1.05 |
| Market reference dc home away odds | 1.07 |
| Market p over 1 5 | 96.9% |
| Market over 1 5 odds | 1.03 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:08:12Z |
| Market reference over 1 5 odds | 1.02 |
| Market reference over 1 5 opposite odds | 9.20 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 26.0% |
| Market under 3 5 odds | 3.14 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:08:12Z |
| Market reference under 3 5 odds | 3.45 |
| Market reference under 3 5 opposite odds | 1.32 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.2% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:09:18Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 3.15 |
| Market reference btts yes last update utc | 2026-10-17T09:10:04Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **48.8%**. Expected goals are 2.12 for Elversberg and 1.14 for Augsburg (3.25 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 62.1%; Under 3.5 goals: 60.1%; Double Chance 1X: 72.9%; Double Chance X2: 51.2%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 61.8%; BTTS No (at least one team does not score): 38.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 48.8% | 2.05 |
| Draw | 24.1% | 4.15 |
| Augsburg win | 27.1% | 3.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.12 |
| Augsburg expected goals | 1.14 |
| Expected total goals | 3.25 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 83.8% |
| Under 1.5 | 16.2% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 39.9% |
| Under 3.5 | 60.1% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.02% |
| 2 | 2-1 | 8.17% |
| 3 | 1-2 | 7.62% |
| 4 | 2-0 | 7.17% |
| 5 | 2-2 | 6.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 48.8% | 38.8% | 2.54 | +24.0% |
| Draw | 24.1% | 25.8% | 3.82 | -7.9% |
| Augsburg win | 27.1% | 35.3% | 2.78 | -24.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 0bf757f3bd903496ce2fa27bd0481869 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Elversberg |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1153 |
| Dc lambda away | 1.1396 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.8% |
| P btts no | 38.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.41 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.19 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.53 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 18.8% |
| Raw p over 1 5 | 84.5% |
| Raw p under 3 5 | 59.0% |
| Raw p btts yes | 60.7% |
| P home draw | 72.9% |
| P draw away | 51.2% |
| P home away | 75.9% |
| Raw p home draw | 81.2% |
| Raw p draw away | 41.2% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.40 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.62 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:42Z |
| Market reference home last update utc | 2026-10-17T09:09:42Z |
| Market reference draw last update utc | 2026-10-17T09:09:42Z |
| Market reference away last update utc | 2026-10-17T09:09:42Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:42Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:42Z |
| Home probability edge | +10.0% |
| Draw probability edge | -1.7% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | 0.1996 |
| Raw ev home | 0.4933 |
| Raw edge prob draw | -0.0348 |
| Raw ev draw | -0.1459 |
| Raw edge prob away | -0.1648 |
| Raw ev away | -0.4760 |
| Market p home draw | 64.9% |
| Market home draw odds | 1.50 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:09:18Z |
| Market reference home draw last update utc | 2026-10-17T09:09:42Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.3% |
| Market draw away odds | 1.58 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:09:18Z |
| Market reference draw away last update utc | 2026-10-17T09:09:42Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.8% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:09:18Z |
| Market reference home away last update utc | 2026-10-17T09:09:42Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.55 |
| Market reference dc home draw odds | 1.44 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 85.4% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:09:15Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:42Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.3% |
| Market under 3 5 odds | 1.74 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:09:15Z |
| Market reference under 3 5 odds | 1.70 |
| Market reference under 3 5 opposite odds | 2.25 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:41Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:09:18Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.80 |
| Market reference btts yes last update utc | 2026-10-17T09:09:42Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **36.8%**. Expected goals are 0.94 for FC Schalke 04 and 0.90 for FSV Mainz 05 (1.84 combined). The most likely exact score is 0-0 at 15.3%. Goal-market probabilities: at least one goal: 84.7%; Over 2.5 goals: 29.1%; Under 3.5 goals: 88.4%; Double Chance 1X: 63.2%; Double Chance X2: 67.9%; Double Chance 12 (either team wins): 68.9%; Under 4.5 goals: 95.9%; BTTS Yes (both teams score): 36.6%; BTTS No (at least one team does not score): 63.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 32.1% | 3.11 |
| Draw | 31.1% | 3.22 |
| FSV Mainz 05 win | 36.8% | 2.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.94 |
| FSV Mainz 05 expected goals | 0.90 |
| Expected total goals | 1.84 |
| Over 0.5 | 84.7% |
| Under 0.5 | 15.3% |
| Over 1.5 | 56.5% |
| Under 1.5 | 43.5% |
| Over 2.5 | 29.1% |
| Under 2.5 | 70.9% |
| Over 3.5 | 11.6% |
| Under 3.5 | 88.4% |
| Over 4.5 | 4.1% |
| Under 4.5 | 95.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 15.26% |
| 2 | 0-1 | 15.20% |
| 3 | 1-1 | 13.07% |
| 4 | 1-0 | 13.07% |
| 5 | 0-2 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 32.1% | 30.9% | 3.16 | +1.6% |
| Draw | 31.1% | 27.0% | 3.67 | +14.1% |
| FSV Mainz 05 win | 36.8% | 42.0% | 2.34 | -13.9% |
| Over 2.5 | 29.1% | 58.9% | 1.70 | -50.5% |
| Under 2.5 | 70.9% | 41.1% | 2.34 | +65.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 606d65d57a9a6d8f9b53faee1ad10009 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Schalke 04 |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9362 |
| Dc lambda away | 0.9021 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 36.6% |
| P btts no | 63.4% |
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.55 |
| Fair Over 1.5 odds | 1.77 |
| Fair Under 1.5 odds | 2.30 |
| Fair Over 2.5 odds | 3.43 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.59 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.30 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 33.4% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 31.5% |
| Raw p over 1 5 | 56.2% |
| Raw p under 3 5 | 88.5% |
| Raw p btts yes | 37.5% |
| P home draw | 63.2% |
| P draw away | 67.9% |
| P home away | 68.9% |
| Raw p home draw | 68.5% |
| Raw p draw away | 66.6% |
| Raw p home away | 64.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.00 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:42Z |
| Market reference home last update utc | 2026-10-17T09:09:42Z |
| Market reference draw last update utc | 2026-10-17T09:09:42Z |
| Market reference away last update utc | 2026-10-17T09:09:42Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:42Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:42Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:18Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:18Z |
| Home probability edge | +1.2% |
| Draw probability edge | +4.0% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | -29.8% |
| Under 2.5 probability edge | +29.8% |
| Raw edge prob home | 0.0245 |
| Raw ev home | 0.0543 |
| Raw edge prob draw | 0.0808 |
| Raw ev draw | 0.2890 |
| Raw edge prob away | -0.1053 |
| Raw ev away | -0.2626 |
| Market p home draw | 58.2% |
| Market home draw odds | 1.67 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:09:18Z |
| Market reference home draw last update utc | 2026-10-17T09:09:42Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.3% |
| Market draw away odds | 1.41 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:09:18Z |
| Market reference draw away last update utc | 2026-10-17T09:09:42Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.5% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:09:18Z |
| Market reference home away last update utc | 2026-10-17T09:09:42Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home draw odds | 1.62 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.7% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:09:17Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:42Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:09:17Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.67 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:41Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:09:18Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-17T09:09:42Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **55.5%**. Expected goals are 1.15 for Hamburger SV and 2.01 for VfB Stuttgart (3.16 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 61.6%; Under 3.5 goals: 61.1%; Double Chance 1X: 44.5%; Double Chance X2: 77.8%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 60.1%; BTTS No (at least one team does not score): 39.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 22.2% | 4.50 |
| Draw | 22.3% | 4.48 |
| VfB Stuttgart win | 55.5% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.15 |
| VfB Stuttgart expected goals | 2.01 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 61.6% |
| Under 2.5 | 38.4% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.29% |
| 2 | 1-2 | 9.71% |
| 3 | 0-2 | 8.44% |
| 4 | 0-1 | 7.43% |
| 5 | 1-3 | 6.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 22.2% | 24.0% | 4.45 | -1.2% |
| Draw | 22.3% | 21.3% | 4.11 | -8.3% |
| VfB Stuttgart win | 55.5% | 54.7% | 1.83 | +1.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 221916b8b36706ec52aa655a64e5f1d2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Hamburg |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1514 |
| Dc lambda away | 2.0111 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.1% |
| P btts no | 39.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.11 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.00 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.68 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 20.4% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 56.3% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 60.2% |
| P home draw | 44.5% |
| P draw away | 77.8% |
| P home away | 77.7% |
| Raw p home draw | 43.7% |
| Raw p draw away | 79.6% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.75 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.75 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:42Z |
| Market reference home last update utc | 2026-10-17T09:09:42Z |
| Market reference draw last update utc | 2026-10-17T09:09:42Z |
| Market reference away last update utc | 2026-10-17T09:09:42Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.90 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:42Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:42Z |
| Home probability edge | -1.8% |
| Draw probability edge | +1.0% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | -0.0367 |
| Raw ev home | -0.0934 |
| Raw edge prob draw | 0.0206 |
| Raw ev draw | -0.0409 |
| Raw edge prob away | 0.0160 |
| Raw ev away | 0.0301 |
| Market p home draw | 47.2% |
| Market home draw odds | 2.09 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:09:18Z |
| Market reference home draw last update utc | 2026-10-17T09:09:42Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.5% |
| Market draw away odds | 1.25 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:09:18Z |
| Market reference draw away last update utc | 2026-10-17T09:09:42Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.3% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:09:18Z |
| Market reference home away last update utc | 2026-10-17T09:09:42Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.25 |
| Market reference dc home draw odds | 2.00 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:09:15Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:42Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.5% |
| Market under 3 5 odds | 1.90 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:09:15Z |
| Market reference under 3 5 odds | 1.86 |
| Market reference under 3 5 opposite odds | 2.05 |
| Market reference under 3 5 last update utc | 2026-10-17T09:09:41Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.5% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:09:18Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 3.00 |
| Market reference btts yes last update utc | 2026-10-17T09:10:04Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **59.9%**. Expected goals are 0.94 for Union Berlin and 1.89 for Borussia Dortmund (2.84 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 54.5%; Under 3.5 goals: 68.2%; Double Chance 1X: 40.1%; Double Chance X2: 82.6%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 52.6%; BTTS No (at least one team does not score): 47.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.4% | 5.74 |
| Draw | 22.6% | 4.42 |
| Borussia Dortmund win | 59.9% | 1.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.89 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 78.7% |
| Under 1.5 | 21.3% |
| Over 2.5 | 54.5% |
| Under 2.5 | 45.5% |
| Over 3.5 | 31.8% |
| Under 3.5 | 68.2% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.80% |
| 2 | 0-2 | 10.75% |
| 3 | 0-1 | 10.30% |
| 4 | 1-2 | 10.15% |
| 5 | 0-3 | 6.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.4% | 17.5% | 5.34 | -7.0% |
| Draw | 22.6% | 21.1% | 4.62 | +4.6% |
| Borussia Dortmund win | 59.9% | 61.4% | 1.63 | -2.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | d8eac776adb07b0e7f01d8736d097291 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Union Berlin |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9447 |
| Dc lambda away | 1.8920 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 52.6% |
| P btts no | 47.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.45 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.70 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.14 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.23 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 58.5% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 52.9% |
| P home draw | 40.1% |
| P draw away | 82.6% |
| P home away | 77.4% |
| Raw p home draw | 41.5% |
| Raw p draw away | 82.7% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 5.00 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.57 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:42Z |
| Market reference home last update utc | 2026-10-17T09:09:42Z |
| Market reference draw last update utc | 2026-10-17T09:09:42Z |
| Market reference away last update utc | 2026-10-17T09:09:42Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:42Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:42Z |
| Home probability edge | -0.1% |
| Draw probability edge | +1.5% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.0017 |
| Raw ev home | -0.0747 |
| Raw edge prob draw | 0.0300 |
| Raw ev draw | 0.1152 |
| Raw edge prob away | -0.0282 |
| Raw ev away | -0.0459 |
| Market p home draw | 39.1% |
| Market home draw odds | 2.42 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:09:18Z |
| Market reference home draw last update utc | 2026-10-17T09:10:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 82.5% |
| Market draw away odds | 1.19 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:09:18Z |
| Market reference draw away last update utc | 2026-10-17T09:10:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.4% |
| Market home away odds | 1.24 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:09:18Z |
| Market reference home away last update utc | 2026-10-17T09:10:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home draw odds | 2.45 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:09:15Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.0% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:09:15Z |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.28 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.2% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:09:18Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.48 |
| Market reference btts yes last update utc | 2026-10-17T09:10:04Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **53.5%**. Expected goals are 1.27 for Werder Bremen and 0.60 for SC Paderborn (1.87 combined). The most likely exact score is 1-0 at 19.0%. Goal-market probabilities: at least one goal: 85.9%; Over 2.5 goals: 30.3%; Under 3.5 goals: 87.8%; Double Chance 1X: 80.6%; Double Chance X2: 46.5%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 95.6%; BTTS Yes (both teams score): 32.7%; BTTS No (at least one team does not score): 67.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 53.5% | 1.87 |
| Draw | 27.1% | 3.69 |
| SC Paderborn win | 19.4% | 5.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.27 |
| SC Paderborn expected goals | 0.60 |
| Expected total goals | 1.87 |
| Over 0.5 | 85.9% |
| Under 0.5 | 14.1% |
| Over 1.5 | 57.4% |
| Under 1.5 | 42.6% |
| Over 2.5 | 30.3% |
| Under 2.5 | 69.7% |
| Over 3.5 | 12.2% |
| Under 3.5 | 87.8% |
| Over 4.5 | 4.4% |
| Under 4.5 | 95.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.03% |
| 2 | 0-0 | 14.06% |
| 3 | 2-0 | 12.86% |
| 4 | 1-1 | 10.98% |
| 5 | 0-1 | 9.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 53.5% | 55.3% | 1.79 | -4.3% |
| Draw | 27.1% | 22.4% | 4.36 | +18.3% |
| SC Paderborn win | 19.4% | 22.4% | 4.42 | -14.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 9a422e1aad1053828eaf629a58d901de |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2714 |
| Dc lambda away | 0.6010 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 32.7% |
| P btts no | 67.3% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.11 |
| Fair Over 1.5 odds | 1.74 |
| Fair Under 1.5 odds | 2.35 |
| Fair Over 2.5 odds | 3.31 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 8.16 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 22.74 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 51.7% |
| Unadjusted draw probability | 31.9% |
| Unadjusted away-win probability | 16.4% |
| Raw p over 1 5 | 57.0% |
| Raw p under 3 5 | 87.9% |
| Raw p btts yes | 33.7% |
| P home draw | 80.6% |
| P draw away | 46.5% |
| P home away | 72.9% |
| Raw p home draw | 83.6% |
| Raw p draw away | 48.3% |
| Raw p home away | 68.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.73 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Home probability edge | -1.8% |
| Draw probability edge | +4.8% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -33.5% |
| Under 2.5 probability edge | +33.5% |
| Raw edge prob home | -0.0362 |
| Raw ev home | -0.0749 |
| Raw edge prob draw | 0.0954 |
| Raw ev draw | 0.3906 |
| Raw edge prob away | -0.0593 |
| Raw ev away | -0.2741 |
| Market p home draw | 77.2% |
| Market home draw odds | 1.25 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:09:18Z |
| Market reference home draw last update utc | 2026-10-17T09:10:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.2% |
| Market draw away odds | 2.15 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:09:18Z |
| Market reference draw away last update utc | 2026-10-17T09:10:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.6% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:09:18Z |
| Market reference home away last update utc | 2026-10-17T09:10:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.07 |
| Market reference dc home draw odds | 1.24 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:08:12Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.5% |
| Market under 3 5 odds | 1.70 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:08:12Z |
| Market reference under 3 5 odds | 1.67 |
| Market reference under 3 5 opposite odds | 2.32 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.2% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:09:18Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.45 |
| Market reference btts yes last update utc | 2026-10-17T09:09:43Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **63.2%**. Expected goals are 2.47 for Bayer Leverkusen and 0.98 for SC Freiburg (3.46 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 66.0%; Under 3.5 goals: 55.7%; Double Chance 1X: 83.4%; Double Chance X2: 36.8%; Double Chance 12 (either team wins): 79.8%; Under 4.5 goals: 74.2%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 63.2% | 1.58 |
| Draw | 20.2% | 4.94 |
| SC Freiburg win | 16.6% | 6.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.47 |
| SC Freiburg expected goals | 0.98 |
| Expected total goals | 3.46 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 66.0% |
| Under 2.5 | 34.0% |
| Over 3.5 | 44.3% |
| Under 3.5 | 55.7% |
| Over 4.5 | 25.8% |
| Under 4.5 | 74.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.24% |
| 2 | 2-0 | 8.81% |
| 3 | 2-1 | 8.66% |
| 4 | 3-0 | 7.26% |
| 5 | 3-1 | 7.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 63.2% | 57.1% | 1.74 | +9.9% |
| Draw | 20.2% | 22.0% | 4.47 | -9.5% |
| SC Freiburg win | 16.6% | 20.9% | 4.62 | -23.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:30:00+00:00 |
| Fixture id | 096d800bcc95c547ef592cbef624d080 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Leverkusen |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4720 |
| Dc lambda away | 0.9831 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.30 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.20 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.94 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.88 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 69.2% |
| Unadjusted draw probability | 18.5% |
| Unadjusted away-win probability | 12.3% |
| Raw p over 1 5 | 86.7% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 58.1% |
| P home draw | 83.4% |
| P draw away | 36.8% |
| P home away | 79.8% |
| Raw p home draw | 87.7% |
| Raw p draw away | 30.8% |
| Raw p home away | 81.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.67 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.20 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Home probability edge | +6.0% |
| Draw probability edge | -1.8% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.1206 |
| Raw ev home | 0.2038 |
| Raw edge prob draw | -0.0352 |
| Raw ev draw | -0.1736 |
| Raw edge prob away | -0.0854 |
| Raw ev away | -0.4304 |
| Market p home draw | 77.8% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:09:18Z |
| Market reference home draw last update utc | 2026-10-17T09:10:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.5% |
| Market draw away odds | 2.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:09:18Z |
| Market reference draw away last update utc | 2026-10-17T09:10:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.8% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:09:18Z |
| Market reference home away last update utc | 2026-10-17T09:10:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.15 |
| Market reference dc home draw odds | 1.23 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 86.1% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:08:11Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.4% |
| Market under 3 5 odds | 1.74 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:08:11Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.19 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.1% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:09:18Z |
| Market reference btts yes odds | 1.54 |
| Market reference btts yes opposite odds | 2.70 |
| Market reference btts yes last update utc | 2026-10-17T09:10:04Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **40.8%**. Expected goals are 1.95 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.74 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 72.1%; Under 3.5 goals: 48.6%; Double Chance 1X: 59.2%; Double Chance X2: 63.9%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 68.0%; BTTS Yes (both teams score): 72.4%; BTTS No (at least one team does not score): 27.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 36.1% | 2.77 |
| Draw | 23.1% | 4.33 |
| TSG Hoffenheim win | 40.8% | 2.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.95 |
| TSG Hoffenheim expected goals | 1.79 |
| Expected total goals | 3.74 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 89.5% |
| Under 1.5 | 10.5% |
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 51.4% |
| Under 3.5 | 48.6% |
| Over 4.5 | 32.0% |
| Under 4.5 | 68.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.12% |
| 2 | 1-2 | 8.57% |
| 3 | 2-2 | 7.25% |
| 4 | 2-1 | 7.02% |
| 5 | 1-3 | 5.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 36.1% | 30.7% | 3.21 | +15.9% |
| Draw | 23.1% | 23.1% | 4.21 | -2.8% |
| TSG Hoffenheim win | 40.8% | 46.2% | 2.15 | -12.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | fd9b8c185737a15615aa0c9daaa3dfbf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | M'gladbach |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9477 |
| Dc lambda away | 1.7934 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 72.4% |
| P btts no | 27.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.26 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.56 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.59 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.12 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 41.5% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 48.6% |
| Raw p btts yes | 72.3% |
| P home draw | 59.2% |
| P draw away | 63.9% |
| P home away | 76.9% |
| Raw p home draw | 64.6% |
| Raw p draw away | 58.5% |
| Raw p home away | 76.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.00 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Home probability edge | +5.4% |
| Draw probability edge | -0.0% |
| Away probability edge | -5.4% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Raw edge prob home | 0.1087 |
| Raw ev home | 0.3334 |
| Raw edge prob draw | -0.0007 |
| Raw ev draw | -0.0293 |
| Raw edge prob away | -0.1080 |
| Raw ev away | -0.2388 |
| Market p home draw | 55.0% |
| Market home draw odds | 1.79 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:09:18Z |
| Market reference home draw last update utc | 2026-10-17T09:10:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.9% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:09:18Z |
| Market reference draw away last update utc | 2026-10-17T09:10:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.1% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:09:18Z |
| Market reference home away last update utc | 2026-10-17T09:10:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home draw odds | 1.73 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 88.5% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:06:11Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.3% |
| Market under 3 5 odds | 1.89 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:06:11Z |
| Market reference under 3 5 odds | 1.86 |
| Market reference under 3 5 opposite odds | 2.03 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.5% |
| Market btts yes odds | 1.35 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:09:18Z |
| Market reference btts yes odds | 1.42 |
| Market reference btts yes opposite odds | 3.15 |
| Market reference btts yes last update utc | 2026-10-17T09:10:04Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **67.4%**. Expected goals are 2.55 for VfB Stuttgart and 1.20 for Borussia Monchengladbach (3.75 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 72.6%; Under 3.5 goals: 48.2%; Double Chance 1X: 85.3%; Double Chance X2: 32.6%; Double Chance 12 (either team wins): 82.1%; Under 4.5 goals: 67.5%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 67.4% | 1.48 |
| Draw | 17.9% | 5.58 |
| Borussia Monchengladbach win | 14.7% | 6.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.55 |
| Borussia Monchengladbach expected goals | 1.20 |
| Expected total goals | 3.75 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 89.6% |
| Under 1.5 | 10.4% |
| Over 2.5 | 72.6% |
| Under 2.5 | 27.4% |
| Over 3.5 | 51.8% |
| Under 3.5 | 48.2% |
| Over 4.5 | 32.5% |
| Under 4.5 | 67.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.41% |
| 2 | 3-1 | 7.99% |
| 3 | 2-0 | 7.83% |
| 4 | 1-1 | 7.55% |
| 5 | 3-0 | 6.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 67.4% | 69.1% | 1.43 | -3.6% |
| Draw | 17.9% | 17.0% | 5.80 | +3.9% |
| Borussia Monchengladbach win | 14.7% | 13.9% | 6.98 | +2.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:30:00+00:00 |
| Fixture id | d4d56a31d8ccd432e3a6183180e093f3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5453 |
| Dc lambda away | 1.2016 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.15 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.65 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.65 |
| Fair Over 3.5 odds | 1.93 |
| Fair Under 3.5 odds | 2.07 |
| Fair Over 4.5 odds | 3.08 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 65.8% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 15.4% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.4% |
| Raw p btts yes | 65.2% |
| P home draw | 85.3% |
| P draw away | 32.6% |
| P home away | 82.1% |
| Raw p home draw | 84.6% |
| Raw p draw away | 34.2% |
| Raw p home away | 81.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.40 |
| Reference draw odds | 5.00 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Home probability edge | -1.6% |
| Draw probability edge | +0.9% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0330 |
| Raw ev home | -0.0596 |
| Raw edge prob draw | 0.0178 |
| Raw ev draw | 0.0904 |
| Raw edge prob away | 0.0152 |
| Raw ev away | 0.0777 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **39.2%**. Expected goals are 0.90 for 1. FC Köln and 0.93 for FC Schalke 04 (1.83 combined). The most likely exact score is 1-0 at 16.3%. Goal-market probabilities: at least one goal: 85.2%; Over 2.5 goals: 29.3%; Under 3.5 goals: 88.4%; Double Chance 1X: 69.2%; Double Chance X2: 60.8%; Double Chance 12 (either team wins): 70.0%; Under 4.5 goals: 95.9%; BTTS Yes (both teams score): 36.2%; BTTS No (at least one team does not score): 63.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 39.2% | 2.55 |
| Draw | 30.0% | 3.33 |
| FC Schalke 04 win | 30.8% | 3.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 0.90 |
| FC Schalke 04 expected goals | 0.93 |
| Expected total goals | 1.83 |
| Over 0.5 | 85.2% |
| Under 0.5 | 14.8% |
| Over 1.5 | 56.4% |
| Under 1.5 | 43.6% |
| Over 2.5 | 29.3% |
| Under 2.5 | 70.7% |
| Over 3.5 | 11.6% |
| Under 3.5 | 88.4% |
| Over 4.5 | 4.1% |
| Under 4.5 | 95.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.28% |
| 2 | 0-0 | 14.78% |
| 3 | 1-1 | 12.58% |
| 4 | 0-1 | 12.56% |
| 5 | 2-0 | 8.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 39.2% | 47.0% | 2.12 | -16.8% |
| Draw | 30.0% | 24.8% | 3.98 | +19.4% |
| FC Schalke 04 win | 30.8% | 28.2% | 3.43 | +5.6% |
| Over 2.5 | 29.3% | 60.5% | 1.64 | -51.9% |
| Under 2.5 | 70.7% | 39.5% | 2.46 | +73.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 983440c6e348b558c6a3e10e2061ba55 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Koln |
| Matched away-team name | Schalke 04 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8983 |
| Dc lambda away | 0.9338 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 36.2% |
| P btts no | 63.8% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.77 |
| Fair Over 1.5 odds | 1.77 |
| Fair Under 1.5 odds | 2.29 |
| Fair Over 2.5 odds | 3.41 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.63 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.27 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 31.4% |
| Unadjusted draw probability | 35.2% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 56.0% |
| Raw p under 3 5 | 88.6% |
| Raw p btts yes | 37.3% |
| P home draw | 69.2% |
| P draw away | 60.8% |
| P home away | 70.0% |
| Raw p home draw | 66.6% |
| Raw p draw away | 68.6% |
| Raw p home away | 64.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.00 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:18Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:18Z |
| Home probability edge | -7.8% |
| Draw probability edge | +5.2% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -31.2% |
| Under 2.5 probability edge | +31.2% |
| Raw edge prob home | -0.1558 |
| Raw ev home | -0.3334 |
| Raw edge prob draw | 0.1039 |
| Raw ev draw | 0.4005 |
| Raw edge prob away | 0.0518 |
| Raw ev away | 0.1446 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **49.4%**. Expected goals are 1.53 for Augsburg and 1.03 for Union Berlin (2.56 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 48.1%; Under 3.5 goals: 74.2%; Double Chance 1X: 75.1%; Double Chance X2: 50.6%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 49.4% | 2.02 |
| Draw | 25.7% | 3.89 |
| Union Berlin win | 24.9% | 4.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.53 |
| Union Berlin expected goals | 1.03 |
| Expected total goals | 2.56 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.1% |
| Under 2.5 | 51.9% |
| Over 3.5 | 25.8% |
| Under 3.5 | 74.2% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.26% |
| 2 | 1-0 | 11.00% |
| 3 | 2-1 | 9.66% |
| 4 | 2-0 | 9.39% |
| 5 | 0-0 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 49.4% | 51.1% | 1.96 | -3.1% |
| Draw | 25.7% | 23.3% | 4.16 | +6.8% |
| Union Berlin win | 24.9% | 25.5% | 3.77 | -6.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04bb232a2940fcf03abf05b308e27577 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5333 |
| Dc lambda away | 1.0288 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.23 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.88 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.33 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.8% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 74.4% |
| Raw p btts yes | 51.6% |
| P home draw | 75.1% |
| P draw away | 50.6% |
| P home away | 74.3% |
| Raw p home draw | 75.8% |
| Raw p draw away | 52.2% |
| Raw p home away | 72.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.85 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.50 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Home probability edge | -1.7% |
| Draw probability edge | +2.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -13.7% |
| Under 2.5 probability edge | +13.7% |
| Raw edge prob home | -0.0339 |
| Raw ev home | -0.0640 |
| Raw edge prob draw | 0.0469 |
| Raw ev draw | 0.1657 |
| Raw edge prob away | -0.0130 |
| Raw ev away | -0.0868 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **63.3%**. Expected goals are 2.27 for Borussia Dortmund and 1.24 for Eintracht Frankfurt (3.51 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 68.9%; Under 3.5 goals: 52.9%; Double Chance 1X: 82.8%; Double Chance X2: 36.7%; Double Chance 12 (either team wins): 80.5%; Under 4.5 goals: 71.8%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 63.3% | 1.58 |
| Draw | 19.5% | 5.13 |
| Eintracht Frankfurt win | 17.2% | 5.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.27 |
| Eintracht Frankfurt expected goals | 1.24 |
| Expected total goals | 3.51 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 87.6% |
| Under 1.5 | 12.4% |
| Over 2.5 | 68.9% |
| Under 2.5 | 31.1% |
| Over 3.5 | 47.1% |
| Under 3.5 | 52.9% |
| Over 4.5 | 28.2% |
| Under 4.5 | 71.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.12% |
| 2 | 1-1 | 8.49% |
| 3 | 2-0 | 8.14% |
| 4 | 3-1 | 7.66% |
| 5 | 1-0 | 6.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 63.3% | 66.9% | 1.48 | -6.3% |
| Draw | 19.5% | 17.8% | 5.39 | +5.1% |
| Eintracht Frankfurt win | 17.2% | 15.3% | 6.42 | +10.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 3ed4d1e775910625c50518a384e9c547 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2714 |
| Dc lambda away | 1.2431 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.57 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.08 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.22 |
| Fair Over 3.5 odds | 2.12 |
| Fair Under 3.5 odds | 1.89 |
| Fair Over 4.5 odds | 3.54 |
| Fair Under 4.5 odds | 1.39 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 87.4% |
| Raw p under 3 5 | 53.4% |
| Raw p btts yes | 64.6% |
| P home draw | 82.8% |
| P draw away | 36.7% |
| P home away | 80.5% |
| Raw p home draw | 80.9% |
| Raw p draw away | 40.3% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.44 |
| Reference draw odds | 4.80 |
| Reference away odds | 5.50 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Home probability edge | -3.6% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | -0.0724 |
| Raw ev home | -0.1167 |
| Raw edge prob draw | 0.0343 |
| Raw ev draw | 0.1430 |
| Raw edge prob away | 0.0381 |
| Raw ev away | 0.2267 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **51.8%**. Expected goals are 1.59 for FSV Mainz 05 and 1.15 for Werder Bremen (2.74 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 52.6%; Under 3.5 goals: 70.2%; Double Chance 1X: 76.6%; Double Chance X2: 48.2%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 51.8% | 1.93 |
| Draw | 24.8% | 4.04 |
| Werder Bremen win | 23.4% | 4.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.59 |
| Werder Bremen expected goals | 1.15 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 29.8% |
| Under 3.5 | 70.2% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.80% |
| 2 | 2-1 | 10.50% |
| 3 | 1-0 | 10.19% |
| 4 | 2-0 | 9.12% |
| 5 | 0-0 | 6.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 51.8% | 57.3% | 1.73 | -10.4% |
| Draw | 24.8% | 22.2% | 4.41 | +9.2% |
| Werder Bremen win | 23.4% | 20.4% | 4.72 | +10.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 4e5820453145833132980b8d190998c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5862 |
| Dc lambda away | 1.1511 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.41 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.36 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.81 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 46.3% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 26.5% |
| Raw p over 1 5 | 77.0% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 55.5% |
| P home draw | 76.6% |
| P draw away | 48.2% |
| P home away | 75.2% |
| Raw p home draw | 73.5% |
| Raw p draw away | 53.7% |
| Raw p home away | 72.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.67 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.33 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Home probability edge | -5.5% |
| Draw probability edge | +2.5% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | -0.1109 |
| Raw ev home | -0.1997 |
| Raw edge prob draw | 0.0502 |
| Raw ev draw | 0.2023 |
| Raw edge prob away | 0.0607 |
| Raw ev away | 0.2498 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **61.3%**. Expected goals are 2.01 for RB Leipzig and 1.39 for Elversberg (3.40 combined). The most likely exact score is 2-1 at 11.3%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 67.4%; Under 3.5 goals: 55.1%; Double Chance 1X: 81.4%; Double Chance X2: 38.7%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 73.5%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 61.3% | 1.63 |
| Draw | 20.1% | 4.97 |
| Elversberg win | 18.6% | 5.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.01 |
| Elversberg expected goals | 1.39 |
| Expected total goals | 3.40 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 44.9% |
| Under 3.5 | 55.1% |
| Over 4.5 | 26.5% |
| Under 4.5 | 73.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.28% |
| 2 | 1-1 | 8.80% |
| 3 | 2-0 | 8.11% |
| 4 | 3-1 | 7.54% |
| 5 | 1-0 | 6.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 61.3% | 71.7% | 1.39 | -14.8% |
| Draw | 20.1% | 16.8% | 6.09 | +22.5% |
| Elversberg win | 18.6% | 11.5% | 7.70 | +43.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04dac5e98ab5fc5564980542ca3fc746 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0056 |
| Dc lambda away | 1.3919 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.31 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.50 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.23 |
| Fair Under 3.5 odds | 1.81 |
| Fair Over 4.5 odds | 3.78 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 50.9% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 25.7% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.9% |
| Raw p btts yes | 66.0% |
| P home draw | 81.4% |
| P draw away | 38.7% |
| P home away | 79.9% |
| Raw p home draw | 74.3% |
| Raw p draw away | 49.1% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.35 |
| Reference draw odds | 5.00 |
| Reference away odds | 7.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Home probability edge | -10.4% |
| Draw probability edge | +3.3% |
| Away probability edge | +7.1% |
| Over 2.5 probability edge | -10.4% |
| Under 2.5 probability edge | +10.4% |
| Raw edge prob home | -0.2083 |
| Raw ev home | -0.2932 |
| Raw edge prob draw | 0.0670 |
| Raw ev draw | 0.4294 |
| Raw edge prob away | 0.1413 |
| Raw ev away | 0.9772 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **Hamburger SV win** at **34.6%**. Expected goals are 0.76 for SC Paderborn and 0.90 for Hamburger SV (1.66 combined). The most likely exact score is 0-0 at 17.0%. Goal-market probabilities: at least one goal: 83.0%; Over 2.5 goals: 24.9%; Under 3.5 goals: 91.0%; Double Chance 1X: 65.4%; Double Chance X2: 65.7%; Double Chance 12 (either team wins): 68.9%; Under 4.5 goals: 97.1%; BTTS Yes (both teams score): 31.9%; BTTS No (at least one team does not score): 68.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 34.3% | 2.91 |
| Draw | 31.1% | 3.21 |
| Hamburger SV win | 34.6% | 2.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.76 |
| Hamburger SV expected goals | 0.90 |
| Expected total goals | 1.66 |
| Over 0.5 | 83.0% |
| Under 0.5 | 17.0% |
| Over 1.5 | 51.3% |
| Under 1.5 | 48.7% |
| Over 2.5 | 24.9% |
| Under 2.5 | 75.1% |
| Over 3.5 | 9.0% |
| Under 3.5 | 91.0% |
| Over 4.5 | 2.9% |
| Under 4.5 | 97.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 17.03% |
| 2 | 1-0 | 16.32% |
| 3 | 0-1 | 15.40% |
| 4 | 1-1 | 12.06% |
| 5 | 0-2 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 34.3% | 40.9% | 2.40 | -17.7% |
| Draw | 31.1% | 25.3% | 3.92 | +22.0% |
| Hamburger SV win | 34.6% | 33.8% | 2.91 | +0.6% |
| Over 2.5 | 24.9% | 60.5% | 1.64 | -59.2% |
| Under 2.5 | 75.1% | 39.5% | 2.47 | +85.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 7630f897583f3acc0f483fa2d17d1ac5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paderborn |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7646 |
| Dc lambda away | 0.9003 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 31.9% |
| P btts no | 68.1% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.87 |
| Fair Over 1.5 odds | 1.95 |
| Fair Under 1.5 odds | 2.05 |
| Fair Over 2.5 odds | 4.02 |
| Fair Under 2.5 odds | 1.33 |
| Fair Over 3.5 odds | 11.16 |
| Fair Under 3.5 odds | 1.10 |
| Fair Over 4.5 odds | 34.04 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 27.7% |
| Unadjusted draw probability | 36.9% |
| Unadjusted away-win probability | 35.3% |
| Raw p over 1 5 | 50.9% |
| Raw p under 3 5 | 91.2% |
| Raw p btts yes | 33.0% |
| P home draw | 65.4% |
| P draw away | 65.7% |
| P home away | 68.9% |
| Raw p home draw | 64.7% |
| Raw p draw away | 72.3% |
| Raw p home away | 63.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.30 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.75 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:18Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:18Z |
| Home probability edge | -6.6% |
| Draw probability edge | +5.8% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -35.6% |
| Under 2.5 probability edge | +35.6% |
| Raw edge prob home | -0.1321 |
| Raw ev home | -0.3351 |
| Raw edge prob draw | 0.1164 |
| Raw ev draw | 0.4483 |
| Raw edge prob away | 0.0157 |
| Raw ev away | 0.0287 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **69.7%**. Expected goals are 1.18 for SC Freiburg and 2.77 for Bayern Munich (3.95 combined). The most likely exact score is 1-2 at 8.7%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 75.7%; Under 3.5 goals: 44.4%; Double Chance 1X: 30.3%; Double Chance X2: 85.6%; Double Chance 12 (either team wins): 84.1%; Under 4.5 goals: 63.8%; BTTS Yes (both teams score): 65.4%; BTTS No (at least one team does not score): 34.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 14.4% | 6.95 |
| Draw | 15.9% | 6.30 |
| Bayern Munich win | 69.7% | 1.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.18 |
| Bayern Munich expected goals | 2.77 |
| Expected total goals | 3.95 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 91.1% |
| Under 1.5 | 8.9% |
| Over 2.5 | 75.7% |
| Under 2.5 | 24.3% |
| Over 3.5 | 55.6% |
| Under 3.5 | 44.4% |
| Over 4.5 | 36.2% |
| Under 4.5 | 63.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.68% |
| 2 | 1-3 | 8.01% |
| 3 | 0-2 | 7.37% |
| 4 | 0-3 | 6.80% |
| 5 | 1-1 | 6.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 14.4% | 15.7% | 6.52 | -6.2% |
| Draw | 15.9% | 14.9% | 5.80 | -7.9% |
| Bayern Munich win | 69.7% | 69.4% | 1.45 | +1.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | f2bd909f25eea6b4ce42d2f52275e5c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Freiburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1779 |
| Dc lambda away | 2.7693 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 65.4% |
| P btts no | 34.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.68 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.21 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.12 |
| Fair Over 3.5 odds | 1.80 |
| Fair Under 3.5 odds | 2.25 |
| Fair Over 4.5 odds | 2.76 |
| Fair Under 4.5 odds | 1.57 |
| Unadjusted home-win probability | 13.0% |
| Unadjusted draw probability | 16.9% |
| Unadjusted away-win probability | 70.0% |
| Raw p over 1 5 | 91.1% |
| Raw p under 3 5 | 44.4% |
| Raw p btts yes | 65.5% |
| P home draw | 30.3% |
| P draw away | 85.6% |
| P home away | 84.1% |
| Raw p home draw | 30.0% |
| Raw p draw away | 87.0% |
| Raw p home away | 83.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 5.50 |
| Reference draw odds | 5.80 |
| Reference away odds | 1.40 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.00 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Home probability edge | -1.3% |
| Draw probability edge | +1.0% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0268 |
| Raw ev home | -0.1492 |
| Raw edge prob draw | 0.0206 |
| Raw ev draw | -0.0193 |
| Raw edge prob away | 0.0062 |
| Raw ev away | 0.0156 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **51.1%**. Expected goals are 1.40 for TSG Hoffenheim and 2.37 for Bayer Leverkusen (3.77 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 72.1%; Under 3.5 goals: 48.7%; Double Chance 1X: 48.9%; Double Chance X2: 72.4%; Double Chance 12 (either team wins): 78.7%; Under 4.5 goals: 67.9%; BTTS Yes (both teams score): 69.6%; BTTS No (at least one team does not score): 30.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 27.6% | 3.63 |
| Draw | 21.3% | 4.69 |
| Bayer Leverkusen win | 51.1% | 1.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.40 |
| Bayer Leverkusen expected goals | 2.37 |
| Expected total goals | 3.77 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 89.5% |
| Under 1.5 | 10.5% |
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 51.3% |
| Under 3.5 | 48.7% |
| Over 4.5 | 32.1% |
| Under 4.5 | 67.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.67% |
| 2 | 1-2 | 7.93% |
| 3 | 2-1 | 7.04% |
| 4 | 2-2 | 6.53% |
| 5 | 1-3 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 27.6% | 34.2% | 2.76 | -23.9% |
| Draw | 21.3% | 22.0% | 4.25 | -9.3% |
| Bayer Leverkusen win | 51.1% | 43.8% | 2.39 | +22.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:30:00+00:00 |
| Fixture id | 2fd479cbb110c8f057e363bb06195f2b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:18Z |
| Market best draw last update utc | 2026-10-17T09:09:18Z |
| Market best away last update utc | 2026-10-17T09:09:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Hoffenheim |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3961 |
| Dc lambda away | 2.3728 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:45:16.687359+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 69.6% |
| P btts no | 30.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.63 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.49 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.59 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.12 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 20.9% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 58.4% |
| Raw p over 1 5 | 89.8% |
| Raw p under 3 5 | 48.0% |
| Raw p btts yes | 69.0% |
| P home draw | 48.9% |
| P draw away | 72.4% |
| P home away | 78.7% |
| Raw p home draw | 41.6% |
| Raw p draw away | 79.1% |
| Raw p home away | 79.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.62 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.10 |
| Market reference 1x2 last update utc | 2026-10-17T09:09:43Z |
| Market reference home last update utc | 2026-10-17T09:09:43Z |
| Market reference draw last update utc | 2026-10-17T09:09:43Z |
| Market reference away last update utc | 2026-10-17T09:09:43Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:43Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:43Z |
| Home probability edge | -6.7% |
| Draw probability edge | -0.7% |
| Away probability edge | +7.3% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.1333 |
| Raw ev home | -0.4232 |
| Raw edge prob draw | -0.0130 |
| Raw ev draw | -0.1211 |
| Raw edge prob away | 0.1463 |
| Raw ev away | 0.3962 |

</details>


---
