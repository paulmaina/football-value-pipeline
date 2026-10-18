# Ligue 1 — football model report

Fixtures in this report: **14**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 976 |
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
| Training sha256 | 74d6134500ba57ec29dd296882053f2cf7aa59229208dfc7f22a5588b708bd8c |
| Training as of utc | 2026-10-18T11:57:54.647523+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 58, 'bbs_added_results': 4, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 58, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T11:57:54.647523+00:00', 'observations': 68, 'observations_sha256': 'a74cb441e64280e25062dab142c26d9b97315a701bfbee182dbe23959bfa4910', 'eligible_training_matches': 13, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 42, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 3, 'retrospective_eligible_training_matches': 13, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'c9bf9fbdc26f7d800ac51ee0e9d7addc1205d3230fa3ec0b4607b989bff50e70', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 1680.255 |
| Base scoring parameter | 0.201 |
| Home-advantage parameter | 0.195 |
| Dixon-Coles low-score adjustment | -0.046 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-17', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 14.00 |
| Additional event odds calls used before this league | 16.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261018T115754647523Z_6a984afee1fe61784d4e9e5bec1862cb7923902a51153009f3b735953e22a263.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **52.1%**. Expected goals are 0.94 for Angers and 1.71 for Marseille (2.65 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 49.2%; Under 3.5 goals: 72.7%; Double Chance 1X: 47.9%; Double Chance X2: 77.1%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 22.9% | 4.37 |
| Draw | 25.1% | 3.99 |
| Marseille win | 52.1% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.94 |
| Marseille expected goals | 1.71 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 74.5% |
| Under 1.5 | 25.5% |
| Over 2.5 | 49.2% |
| Under 2.5 | 50.8% |
| Over 3.5 | 27.3% |
| Under 3.5 | 72.7% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.94% |
| 2 | 0-1 | 10.91% |
| 3 | 0-2 | 9.77% |
| 4 | 1-2 | 9.19% |
| 5 | 0-0 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 22.9% | 25.7% | 3.78 | -13.5% |
| Draw | 25.1% | 25.2% | 3.85 | -3.5% |
| Marseille win | 52.1% | 49.1% | 2.04 | +6.2% |
| Over 2.5 | 49.2% | 59.2% | 1.68 | -17.3% |
| Under 2.5 | 50.8% | 40.8% | 2.38 | +20.8% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
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
| Dc lambda home | 0.9401 |
| Dc lambda away | 1.7125 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.13 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.92 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.67 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.77 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 55.0% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 50.5% |
| P home draw | 47.9% |
| P draw away | 77.1% |
| P home away | 74.9% |
| Raw p home draw | 45.0% |
| Raw p draw away | 80.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.68 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.98 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | -2.8% |
| Draw probability edge | -0.2% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | -0.0567 |
| Raw ev home | -0.2422 |
| Raw edge prob draw | -0.0030 |
| Raw ev draw | -0.0408 |
| Raw edge prob away | 0.0597 |
| Raw ev away | 0.1228 |
| Market p home draw | 51.4% |
| Market home draw odds | 1.87 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:57:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.0% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:57:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.6% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:57:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.87 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:56:21Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:12Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.8% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:56:21Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.57 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:49Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.8% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-18T11:57:38Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **38.9%**. Expected goals are 1.17 for Le Havre and 1.17 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 41.9%; Under 3.5 goals: 79.0%; Double Chance 1X: 67.1%; Double Chance X2: 61.1%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 38.9% | 2.57 |
| Draw | 28.2% | 3.54 |
| Auxerre win | 32.9% | 3.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.17 |
| Auxerre expected goals | 1.17 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 68.6% |
| Under 1.5 | 31.4% |
| Over 2.5 | 41.9% |
| Under 2.5 | 58.1% |
| Over 3.5 | 21.0% |
| Under 3.5 | 79.0% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.29% |
| 2 | 1-0 | 11.70% |
| 3 | 0-1 | 9.90% |
| 4 | 0-0 | 9.85% |
| 5 | 2-1 | 8.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 38.9% | 42.4% | 2.34 | -9.0% |
| Draw | 28.2% | 27.2% | 3.60 | +1.6% |
| Auxerre win | 32.9% | 30.4% | 3.23 | +6.2% |
| Over 2.5 | 41.9% | 52.9% | 1.87 | -21.7% |
| Under 2.5 | 58.1% | 47.1% | 2.08 | +20.9% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
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
| Dc lambda home | 1.1714 |
| Dc lambda away | 1.1715 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.16 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.18 |
| Fair Over 2.5 odds | 2.39 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.77 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.14 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 35.4% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 48.2% |
| P home draw | 67.1% |
| P draw away | 61.1% |
| P home away | 71.8% |
| Raw p home draw | 64.6% |
| Raw p draw away | 64.6% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.28 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.14 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | -3.5% |
| Draw probability edge | +1.1% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -11.1% |
| Under 2.5 probability edge | +11.1% |
| Raw edge prob home | -0.0707 |
| Raw ev home | -0.1727 |
| Raw edge prob draw | 0.0212 |
| Raw ev draw | 0.0542 |
| Raw edge prob away | 0.0495 |
| Raw ev away | 0.1422 |
| Market p home draw | 69.4% |
| Market home draw odds | 1.40 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:57:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.1% |
| Market draw away odds | 1.67 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:57:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.5% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:57:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.39 |
| Market reference dc draw away odds | 1.66 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 78.0% |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 4.11 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:49Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 69.4% |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 3.05 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:49Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.31 |
| Market reference btts yes last update utc | 2026-10-18T11:57:44Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **47.1%**. Expected goals are 1.36 for Lorient and 1.81 for AS Monaco (3.18 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 60.8%; Under 3.5 goals: 60.8%; Double Chance 1X: 52.9%; Double Chance X2: 73.0%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 78.8%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 27.0% | 3.70 |
| Draw | 25.9% | 3.86 |
| AS Monaco win | 47.1% | 2.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.36 |
| AS Monaco expected goals | 1.81 |
| Expected total goals | 3.18 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 60.8% |
| Under 2.5 | 39.2% |
| Over 3.5 | 39.2% |
| Under 3.5 | 60.8% |
| Over 4.5 | 21.2% |
| Under 4.5 | 78.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.72% |
| 2 | 1-2 | 9.23% |
| 3 | 0-1 | 7.00% |
| 4 | 2-2 | 6.92% |
| 5 | 0-2 | 6.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 27.0% | 25.6% | 3.80 | +2.7% |
| Draw | 25.9% | 28.0% | 3.49 | -9.6% |
| AS Monaco win | 47.1% | 46.4% | 2.15 | +1.2% |
| Over 2.5 | 60.8% | 47.8% | 2.05 | +24.7% |
| Under 2.5 | 39.2% | 52.2% | 1.89 | -26.0% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
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
| Dc lambda home | 1.3622 |
| Dc lambda away | 1.8143 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.80 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.88 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.72 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 28.5% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 47.7% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 62.7% |
| P home draw | 52.9% |
| P draw away | 73.0% |
| P home away | 74.1% |
| Raw p home draw | 52.3% |
| Raw p draw away | 71.5% |
| Raw p home away | 76.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.70 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.09 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | +1.4% |
| Draw probability edge | -2.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | +13.1% |
| Under 2.5 probability edge | -13.1% |
| Raw edge prob home | 0.0284 |
| Raw ev home | 0.0811 |
| Raw edge prob draw | -0.0410 |
| Raw ev draw | -0.1671 |
| Raw edge prob away | 0.0127 |
| Raw ev away | 0.0252 |
| Market p home draw | 54.1% |
| Market home draw odds | 1.79 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:57:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.1% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:57:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.8% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:57:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.78 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 75.1% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:56:38Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:49Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.7% |
| Market under 3 5 odds | 1.27 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:56:38Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.39 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:49Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.6% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-18T11:57:38Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **52.4%**. Expected goals are 1.77 for Lyon and 1.09 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 54.4%; Under 3.5 goals: 67.9%; Double Chance 1X: 77.0%; Double Chance X2: 47.6%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 55.6%; BTTS No (at least one team does not score): 44.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 52.4% | 1.91 |
| Draw | 24.6% | 4.07 |
| Nice win | 23.0% | 4.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.77 |
| Nice expected goals | 1.09 |
| Expected total goals | 2.86 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 54.4% |
| Under 2.5 | 45.6% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.63% |
| 2 | 2-1 | 9.69% |
| 3 | 1-0 | 9.55% |
| 4 | 2-0 | 8.91% |
| 5 | 0-0 | 6.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 52.4% | 51.9% | 1.92 | +0.6% |
| Draw | 24.6% | 24.7% | 3.94 | -3.2% |
| Nice win | 23.0% | 23.4% | 4.16 | -4.2% |
| Over 2.5 | 54.4% | 56.6% | 1.75 | -4.8% |
| Under 2.5 | 45.6% | 43.4% | 2.25 | +2.7% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
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
| Dc lambda home | 1.7717 |
| Dc lambda away | 1.0876 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 55.6% |
| P btts no | 44.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.91 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.62 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.12 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.20 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 52.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| P home draw | 77.0% |
| P draw away | 47.6% |
| P home away | 75.4% |
| Raw p home draw | 77.3% |
| Raw p draw away | 47.1% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.89 |
| Reference draw odds | 3.88 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | +0.5% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -2.2% |
| Under 2.5 probability edge | +2.2% |
| Raw edge prob home | 0.0099 |
| Raw ev home | 0.0154 |
| Raw edge prob draw | -0.0033 |
| Raw ev draw | -0.0384 |
| Raw edge prob away | -0.0066 |
| Raw ev away | -0.0552 |
| Market p home draw | 76.2% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:57:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.9% |
| Market draw away odds | 1.98 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:57:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:57:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.27 |
| Market reference dc draw away odds | 1.98 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.1% |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:12Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.6% |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:49Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.7% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.32 |
| Market reference btts yes last update utc | 2026-10-18T11:57:44Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **42.8%**. Expected goals are 1.57 for Paris FC and 1.37 for Rennes (2.94 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.2%; Double Chance 1X: 69.4%; Double Chance X2: 57.2%; Double Chance 12 (either team wins): 73.4%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 59.7%; BTTS No (at least one team does not score): 40.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 42.8% | 2.33 |
| Draw | 26.6% | 3.76 |
| Rennes win | 30.6% | 3.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.57 |
| Rennes expected goals | 1.37 |
| Expected total goals | 2.94 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.8% |
| Under 3.5 | 66.2% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.40% |
| 2 | 2-1 | 9.17% |
| 3 | 1-0 | 8.01% |
| 4 | 1-2 | 7.26% |
| 5 | 2-0 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 42.8% | 44.0% | 2.26 | -3.2% |
| Draw | 26.6% | 27.6% | 3.54 | -5.9% |
| Rennes win | 30.6% | 28.4% | 3.44 | +5.2% |
| Over 2.5 | 55.9% | 59.3% | 1.73 | -3.3% |
| Under 2.5 | 44.1% | 40.7% | 2.29 | +1.0% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
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
| Dc lambda home | 1.5687 |
| Dc lambda away | 1.3672 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.7% |
| P btts no | 40.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.46 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.96 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.79 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 41.7% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 32.8% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 66.2% |
| Raw p btts yes | 59.5% |
| P home draw | 69.4% |
| P draw away | 57.2% |
| P home away | 73.4% |
| Raw p home draw | 67.2% |
| Raw p draw away | 58.3% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.20 |
| Reference draw odds | 3.44 |
| Reference away odds | 3.35 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:51Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:51Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | -1.1% |
| Draw probability edge | -1.0% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.0229 |
| Raw ev home | -0.0575 |
| Raw edge prob draw | -0.0210 |
| Raw ev draw | -0.0965 |
| Raw edge prob away | 0.0438 |
| Raw ev away | 0.1274 |
| Market p home draw | 71.3% |
| Market home draw odds | 1.36 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:57:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.3% |
| Market draw away odds | 1.71 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:57:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.4% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:57:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.35 |
| Market reference dc draw away odds | 1.71 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 81.9% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:12Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.8% |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:49Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 62.6% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.54 |
| Market reference btts yes last update utc | 2026-10-18T11:57:55Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **43.2%**. Expected goals are 1.56 for Brest and 1.27 for Nice (2.83 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 53.4%; Under 3.5 goals: 68.6%; Double Chance 1X: 70.1%; Double Chance X2: 56.8%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 57.6%; BTTS No (at least one team does not score): 42.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 43.2% | 2.31 |
| Draw | 27.0% | 3.71 |
| Nice win | 29.9% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Nice expected goals | 1.27 |
| Expected total goals | 2.83 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 77.9% |
| Under 1.5 | 22.1% |
| Over 2.5 | 53.4% |
| Under 2.5 | 46.6% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.72% |
| 2 | 2-1 | 9.06% |
| 3 | 1-0 | 8.60% |
| 4 | 1-2 | 7.25% |
| 5 | 2-0 | 7.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 43.2% | 43.0% | 2.31 | -0.2% |
| Draw | 27.0% | 28.0% | 3.49 | -5.9% |
| Nice win | 29.9% | 29.0% | 3.37 | +0.6% |
| Over 2.5 | 53.4% | 56.2% | 1.76 | -6.0% |
| Under 2.5 | 46.6% | 43.8% | 2.23 | +3.9% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brest |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5564 |
| Dc lambda away | 1.2733 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.6% |
| P btts no | 42.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.93 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.53 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.42 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.5% |
| Raw p btts yes | 57.4% |
| P home draw | 70.1% |
| P draw away | 56.8% |
| P home away | 73.0% |
| Raw p home draw | 69.3% |
| Raw p draw away | 56.6% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.25 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.28 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | +0.2% |
| Draw probability edge | -1.0% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | 0.0041 |
| Raw ev home | 0.0026 |
| Raw edge prob draw | -0.0204 |
| Raw ev draw | -0.0950 |
| Raw edge prob away | 0.0163 |
| Raw ev away | 0.0334 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **49.1%**. Expected goals are 1.59 for RC Lens and 1.01 for Paris FC (2.59 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 48.2%; Under 3.5 goals: 73.8%; Double Chance 1X: 74.6%; Double Chance X2: 50.9%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 87.8%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 49.1% | 2.04 |
| Draw | 25.6% | 3.91 |
| Paris FC win | 25.4% | 3.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.59 |
| Paris FC expected goals | 1.01 |
| Expected total goals | 2.59 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 48.2% |
| Under 2.5 | 51.8% |
| Over 3.5 | 26.2% |
| Under 3.5 | 73.8% |
| Over 4.5 | 12.2% |
| Under 4.5 | 87.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.17% |
| 2 | 1-0 | 11.02% |
| 3 | 2-1 | 9.24% |
| 4 | 2-0 | 9.18% |
| 5 | 0-0 | 7.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 49.1% | 47.8% | 2.09 | +2.6% |
| Draw | 25.6% | 24.9% | 3.90 | -0.3% |
| Paris FC win | 25.4% | 27.3% | 3.58 | -9.2% |
| Over 2.5 | 48.2% | 59.2% | 1.68 | -19.0% |
| Under 2.5 | 51.8% | 40.8% | 2.38 | +23.3% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5879 |
| Dc lambda away | 1.0071 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.80 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.81 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.19 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 50.3% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 51.1% |
| P home draw | 74.6% |
| P draw away | 50.9% |
| P home away | 74.4% |
| Raw p home draw | 76.5% |
| Raw p draw away | 49.7% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.03 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.48 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | +1.2% |
| Draw probability edge | +0.7% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0249 |
| Raw ev home | 0.0516 |
| Raw edge prob draw | 0.0133 |
| Raw ev draw | 0.0226 |
| Raw edge prob away | -0.0381 |
| Raw ev away | -0.1599 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **67.6%**. Expected goals are 2.45 for Toulouse and 0.66 for Troyes (3.11 combined). The most likely exact score is 2-0 at 11.8%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.7%; Under 3.5 goals: 64.2%; Double Chance 1X: 86.8%; Double Chance X2: 32.4%; Double Chance 12 (either team wins): 80.8%; Under 4.5 goals: 81.0%; BTTS Yes (both teams score): 46.3%; BTTS No (at least one team does not score): 53.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 67.6% | 1.48 |
| Draw | 19.2% | 5.20 |
| Troyes win | 13.2% | 7.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 2.45 |
| Troyes expected goals | 0.66 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 35.8% |
| Under 3.5 | 64.2% |
| Over 4.5 | 19.0% |
| Under 4.5 | 81.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.83% |
| 2 | 3-0 | 9.64% |
| 3 | 1-0 | 9.37% |
| 4 | 1-1 | 9.17% |
| 5 | 2-1 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 67.6% | 58.9% | 1.71 | +15.6% |
| Draw | 19.2% | 22.6% | 4.26 | -18.1% |
| Troyes win | 13.2% | 18.6% | 5.13 | -32.4% |
| Over 2.5 | 57.7% | 59.6% | 1.67 | -3.6% |
| Under 2.5 | 42.3% | 40.4% | 2.40 | +1.5% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4462 |
| Dc lambda away | 0.6631 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 46.3% |
| P btts no | 53.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.22 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.10 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.26 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 76.3% |
| Unadjusted draw probability | 15.9% |
| Unadjusted away-win probability | 7.8% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 44.6% |
| P home draw | 86.8% |
| P draw away | 32.4% |
| P home away | 80.8% |
| Raw p home draw | 92.2% |
| Raw p draw away | 23.7% |
| Raw p home away | 84.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.66 |
| Reference draw odds | 4.15 |
| Reference away odds | 5.00 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | +8.7% |
| Draw probability edge | -3.3% |
| Away probability edge | -5.4% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.1747 |
| Raw ev home | 0.3052 |
| Raw edge prob draw | -0.0667 |
| Raw ev draw | -0.3228 |
| Raw edge prob away | -0.1080 |
| Raw ev away | -0.6011 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **43.6%**. Expected goals are 1.46 for AS Monaco and 1.26 for Lille (2.72 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.0%; Double Chance 1X: 70.5%; Double Chance X2: 56.4%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 55.5%; BTTS No (at least one team does not score): 44.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 43.6% | 2.30 |
| Draw | 26.9% | 3.72 |
| Lille win | 29.5% | 3.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.46 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 29.0% |
| Under 3.5 | 71.0% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.79% |
| 2 | 1-0 | 9.58% |
| 3 | 2-1 | 9.33% |
| 4 | 2-0 | 7.43% |
| 5 | 0-0 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 43.6% | 45.7% | 2.18 | -5.1% |
| Draw | 26.9% | 27.1% | 3.60 | -3.1% |
| Lille win | 29.5% | 27.1% | 3.60 | +6.3% |
| Over 2.5 | 51.0% | 55.9% | 1.77 | -9.7% |
| Under 2.5 | 49.0% | 44.1% | 2.22 | +8.8% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monaco |
| Matched away-team name | Lille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4612 |
| Dc lambda away | 1.2553 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.5% |
| P btts no | 44.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.83 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.17 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.45 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.17 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 41.4% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 31.9% |
| Raw p over 1 5 | 76.0% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 55.5% |
| P home draw | 70.5% |
| P draw away | 56.4% |
| P home away | 73.1% |
| Raw p home draw | 68.1% |
| Raw p draw away | 58.6% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.12 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.50 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | -2.2% |
| Draw probability edge | -0.2% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0436 |
| Raw ev home | -0.0980 |
| Raw edge prob draw | -0.0044 |
| Raw ev draw | -0.0390 |
| Raw edge prob away | 0.0479 |
| Raw ev away | 0.1494 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **36.8%**. Expected goals are 1.09 for Angers and 1.24 for Lorient (2.33 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.3%; Double Chance 1X: 63.2%; Double Chance X2: 65.8%; Double Chance 12 (either team wins): 71.0%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 47.7%; BTTS No (at least one team does not score): 52.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 34.2% | 2.92 |
| Draw | 29.0% | 3.45 |
| Lorient win | 36.8% | 2.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.09 |
| Lorient expected goals | 1.24 |
| Expected total goals | 2.33 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 68.2% |
| Under 1.5 | 31.8% |
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
| Over 3.5 | 20.7% |
| Under 3.5 | 79.3% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.63% |
| 2 | 1-0 | 10.79% |
| 3 | 0-1 | 10.79% |
| 4 | 0-0 | 10.24% |
| 5 | 2-1 | 7.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 34.2% | 36.7% | 2.69 | -7.9% |
| Draw | 29.0% | 28.7% | 3.40 | -1.4% |
| Lorient win | 36.8% | 34.5% | 2.85 | +4.8% |
| Over 2.5 | 41.3% | 44.7% | 2.19 | -9.6% |
| Under 2.5 | 58.7% | 55.3% | 1.79 | +5.1% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Lorient |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0917 |
| Dc lambda away | 1.2386 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.7% |
| P btts no | 52.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.77 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.14 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.84 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.44 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 31.8% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 68.2% |
| Raw p under 3 5 | 79.3% |
| Raw p btts yes | 47.8% |
| P home draw | 63.2% |
| P draw away | 65.8% |
| P home away | 71.0% |
| Raw p home draw | 61.0% |
| Raw p draw away | 68.2% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.62 |
| Reference draw odds | 3.32 |
| Reference away odds | 2.78 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | -2.5% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.0498 |
| Raw ev home | -0.1457 |
| Raw edge prob draw | 0.0055 |
| Raw ev draw | -0.0047 |
| Raw edge prob away | 0.0443 |
| Raw ev away | 0.1106 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **45.8%**. Expected goals are 1.82 for Auxerre and 1.40 for Le Mans FC (3.22 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 62.0%; Under 3.5 goals: 59.9%; Double Chance 1X: 70.9%; Double Chance X2: 54.2%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 45.8% | 2.18 |
| Draw | 25.1% | 3.99 |
| Le Mans FC win | 29.1% | 3.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.82 |
| Le Mans FC expected goals | 1.40 |
| Expected total goals | 3.22 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 83.6% |
| Under 1.5 | 16.4% |
| Over 2.5 | 62.0% |
| Under 2.5 | 38.0% |
| Over 3.5 | 40.1% |
| Under 3.5 | 59.9% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.23% |
| 2 | 2-1 | 9.03% |
| 3 | 1-2 | 7.10% |
| 4 | 2-2 | 6.83% |
| 5 | 1-0 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 45.8% | 44.6% | 2.23 | +2.2% |
| Draw | 25.1% | 26.3% | 3.70 | -7.3% |
| Le Mans FC win | 29.1% | 29.0% | 3.37 | -1.9% |
| Over 2.5 | 62.0% | 55.6% | 1.78 | +10.3% |
| Under 2.5 | 38.0% | 44.4% | 2.20 | -16.3% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8205 |
| Dc lambda away | 1.3990 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.9% |
| P btts no | 36.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.22 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.08 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.49 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.53 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 29.2% |
| Raw p over 1 5 | 83.6% |
| Raw p under 3 5 | 59.8% |
| Raw p btts yes | 63.6% |
| P home draw | 70.9% |
| P draw away | 54.2% |
| P home away | 74.9% |
| Raw p home draw | 70.8% |
| Raw p draw away | 53.0% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.17 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.28 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | +1.2% |
| Draw probability edge | -1.3% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +6.4% |
| Under 2.5 probability edge | -6.4% |
| Raw edge prob home | 0.0241 |
| Raw ev home | 0.0490 |
| Raw edge prob draw | -0.0258 |
| Raw ev draw | -0.1207 |
| Raw edge prob away | 0.0017 |
| Raw ev away | -0.0160 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **63.6%**. Expected goals are 2.13 for Marseille and 0.86 for Le Havre (2.99 combined). The most likely exact score is 2-0 at 11.0%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 57.0%; Under 3.5 goals: 65.4%; Double Chance 1X: 84.3%; Double Chance X2: 36.4%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 63.6% | 1.57 |
| Draw | 20.7% | 4.84 |
| Le Havre win | 15.7% | 6.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.13 |
| Le Havre expected goals | 0.86 |
| Expected total goals | 2.99 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 80.0% |
| Under 1.5 | 20.0% |
| Over 2.5 | 57.0% |
| Under 2.5 | 43.0% |
| Over 3.5 | 34.6% |
| Under 3.5 | 65.4% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.98% |
| 2 | 1-0 | 9.92% |
| 3 | 1-1 | 9.82% |
| 4 | 2-1 | 9.45% |
| 5 | 3-0 | 7.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 63.6% | 61.2% | 1.64 | +4.3% |
| Draw | 20.7% | 21.0% | 4.57 | -5.6% |
| Le Havre win | 15.7% | 17.8% | 5.33 | -16.1% |
| Over 2.5 | 57.0% | 60.0% | 1.66 | -5.3% |
| Under 2.5 | 43.0% | 40.0% | 2.42 | +4.0% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1258 |
| Dc lambda away | 0.8608 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.97 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.00 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.55 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 66.0% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 13.6% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 65.0% |
| Raw p btts yes | 51.3% |
| P home draw | 84.3% |
| P draw away | 36.4% |
| P home away | 79.3% |
| Raw p home draw | 86.4% |
| Raw p draw away | 34.0% |
| Raw p home away | 79.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.60 |
| Reference draw odds | 4.45 |
| Reference away odds | 5.20 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:56Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | +2.4% |
| Draw probability edge | -0.3% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | 0.0487 |
| Raw ev home | 0.0831 |
| Raw edge prob draw | -0.0067 |
| Raw ev draw | -0.0712 |
| Raw edge prob away | -0.0420 |
| Raw ev away | -0.2732 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **67.8%**. Expected goals are 2.31 for Paris Saint Germain and 1.06 for Lyon (3.37 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 66.1%; Under 3.5 goals: 56.0%; Double Chance 1X: 86.2%; Double Chance X2: 32.2%; Double Chance 12 (either team wins): 81.7%; Under 4.5 goals: 74.5%; BTTS Yes (both teams score): 58.8%; BTTS No (at least one team does not score): 41.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 67.8% | 1.47 |
| Draw | 18.3% | 5.46 |
| Lyon win | 13.8% | 7.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.31 |
| Lyon expected goals | 1.06 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 85.7% |
| Under 1.5 | 14.3% |
| Over 2.5 | 66.1% |
| Under 2.5 | 33.9% |
| Over 3.5 | 44.0% |
| Under 3.5 | 56.0% |
| Over 4.5 | 25.5% |
| Under 4.5 | 74.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.14% |
| 2 | 2-0 | 9.57% |
| 3 | 1-1 | 8.30% |
| 4 | 1-0 | 7.86% |
| 5 | 3-1 | 7.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 67.8% | 70.7% | 1.43 | -3.0% |
| Draw | 18.3% | 17.2% | 5.44 | -0.4% |
| Lyon win | 13.8% | 12.1% | 7.60 | +5.2% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3135 |
| Dc lambda away | 1.0601 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 58.8% |
| P btts no | 41.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.76 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.97 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.95 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.93 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 65.0% |
| Unadjusted draw probability | 19.4% |
| Unadjusted away-win probability | 15.6% |
| Raw p over 1 5 | 85.4% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 59.3% |
| P home draw | 86.2% |
| P draw away | 32.2% |
| P home away | 81.7% |
| Raw p home draw | 84.4% |
| Raw p draw away | 35.0% |
| Raw p home away | 80.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.39 |
| Reference draw odds | 5.30 |
| Reference away odds | 7.40 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:10Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:10Z |
| Home probability edge | -2.8% |
| Draw probability edge | +1.1% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.0565 |
| Raw ev home | -0.0703 |
| Raw edge prob draw | 0.0218 |
| Raw ev draw | 0.0556 |
| Raw edge prob away | 0.0347 |
| Raw ev away | 0.1842 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **52.1%**. Expected goals are 1.87 for Rennes and 1.48 for Strasbourg (3.36 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 65.6%; Under 3.5 goals: 56.6%; Double Chance 1X: 74.3%; Double Chance X2: 47.9%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 65.5%; BTTS No (at least one team does not score): 34.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 52.1% | 1.92 |
| Draw | 22.3% | 4.49 |
| Strasbourg win | 25.7% | 3.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.87 |
| Strasbourg expected goals | 1.48 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.4% |
| Under 3.5 | 56.6% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.18% |
| 2 | 1-1 | 9.70% |
| 3 | 2-0 | 6.86% |
| 4 | 1-0 | 6.83% |
| 5 | 2-2 | 6.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 52.1% | 57.8% | 1.74 | -9.4% |
| Draw | 22.3% | 21.2% | 4.52 | +0.6% |
| Strasbourg win | 25.7% | 21.0% | 4.58 | +17.5% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8707 |
| Dc lambda away | 1.4845 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:54.647523+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.5% |
| P btts no | 34.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.55 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.85 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.99 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 46.4% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 85.2% |
| Raw p under 3 5 | 56.8% |
| Raw p btts yes | 65.9% |
| P home draw | 74.3% |
| P draw away | 47.9% |
| P home away | 77.7% |
| Raw p home draw | 69.7% |
| Raw p draw away | 53.6% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.69 |
| Reference draw odds | 4.40 |
| Reference away odds | 4.45 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:56Z |
| Market reference home last update utc | 2026-10-18T11:57:56Z |
| Market reference draw last update utc | 2026-10-18T11:57:56Z |
| Market reference away last update utc | 2026-10-18T11:57:56Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:10Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:10Z |
| Home probability edge | -5.7% |
| Draw probability edge | +1.0% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | -0.1139 |
| Raw ev home | -0.1929 |
| Raw edge prob draw | 0.0205 |
| Raw ev draw | 0.0528 |
| Raw edge prob away | 0.0933 |
| Raw ev away | 0.3888 |

</details>


---
