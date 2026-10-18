# Ligue 1 — football model report

Fixtures in this report: **13**.

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
| Training as of utc | 2026-10-18T14:34:48.221876+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 58, 'bbs_added_results': 4, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 58, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T14:34:48.221876+00:00', 'observations': 68, 'observations_sha256': 'a74cb441e64280e25062dab142c26d9b97315a701bfbee182dbe23959bfa4910', 'eligible_training_matches': 13, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 42, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 3, 'retrospective_eligible_training_matches': 13, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'c9bf9fbdc26f7d800ac51ee0e9d7addc1205d3230fa3ec0b4607b989bff50e70', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 1680.081 |
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
| Live odds matched | 13.00 |
| Additional event odds calls used before this league | 10.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261018T143448221876Z_bf40523044f00c4373b5c0d35e88e59fd0f8abe9c0c3127e2dee195a3779a50d.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
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

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **38.8%**. Expected goals are 1.17 for Le Havre and 1.17 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 41.9%; Under 3.5 goals: 79.0%; Double Chance 1X: 66.8%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 47.9%; BTTS No (at least one team does not score): 52.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 38.8% | 2.58 |
| Draw | 28.0% | 3.57 |
| Auxerre win | 33.2% | 3.01 |

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
| 1 | 1-1 | 13.20% |
| 2 | 1-0 | 11.67% |
| 3 | 0-1 | 9.99% |
| 4 | 0-0 | 9.78% |
| 5 | 2-1 | 8.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 38.8% | 42.2% | 2.34 | -9.3% |
| Draw | 28.0% | 26.8% | 3.60 | +0.9% |
| Auxerre win | 33.2% | 31.1% | 3.23 | +7.3% |
| Over 2.5 | 41.9% | 54.8% | 1.79 | -24.9% |
| Under 2.5 | 58.1% | 45.2% | 2.19 | +27.1% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 47.9% |
| P btts no | 52.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.23 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.18 |
| Fair Over 2.5 odds | 2.38 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.76 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.12 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 35.4% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 48.2% |
| P home draw | 66.8% |
| P draw away | 61.2% |
| P home away | 72.0% |
| Raw p home draw | 64.6% |
| Raw p draw away | 64.6% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.25 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.00 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -3.4% |
| Draw probability edge | +1.3% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -12.9% |
| Under 2.5 probability edge | +12.9% |
| Raw edge prob home | -0.0683 |
| Raw ev home | -0.1727 |
| Raw edge prob draw | 0.0252 |
| Raw ev draw | 0.0542 |
| Raw edge prob away | 0.0431 |
| Raw ev away | 0.1422 |
| Market p home draw | 69.3% |
| Market home draw odds | 1.40 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:34:32Z |
| Market reference home draw last update utc | 2026-10-18T14:34:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.2% |
| Market draw away odds | 1.67 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:34:32Z |
| Market reference draw away last update utc | 2026-10-18T14:34:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.5% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:34:32Z |
| Market reference home away last update utc | 2026-10-18T14:34:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.62 |
| Market reference dc home draw odds | 1.36 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 78.0% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 68.0% |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.93 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:51Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.4% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:34:32Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-18T14:34:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **48.3%**. Expected goals are 1.36 for Lorient and 1.81 for AS Monaco (3.18 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.2%; Under 3.5 goals: 60.8%; Double Chance 1X: 51.7%; Double Chance X2: 73.2%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 63.0%; BTTS No (at least one team does not score): 37.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 26.8% | 3.73 |
| Draw | 24.9% | 4.01 |
| AS Monaco win | 48.3% | 2.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.36 |
| AS Monaco expected goals | 1.81 |
| Expected total goals | 3.18 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 61.2% |
| Under 2.5 | 38.8% |
| Over 3.5 | 39.2% |
| Under 3.5 | 60.8% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.26% |
| 2 | 1-2 | 9.47% |
| 3 | 0-1 | 7.18% |
| 4 | 0-2 | 6.95% |
| 5 | 2-2 | 6.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 26.8% | 25.2% | 3.80 | +1.9% |
| Draw | 24.9% | 26.0% | 3.49 | -13.1% |
| AS Monaco win | 48.3% | 48.8% | 2.15 | +3.8% |
| Over 2.5 | 61.2% | 48.5% | 2.05 | +25.4% |
| Under 2.5 | 38.8% | 51.5% | 1.89 | -26.6% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.0% |
| P btts no | 37.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.60 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.90 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.68 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 28.5% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 47.7% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 62.7% |
| P home draw | 51.7% |
| P draw away | 73.2% |
| P home away | 75.1% |
| Raw p home draw | 52.3% |
| Raw p draw away | 71.5% |
| Raw p home away | 76.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.65 |
| Reference draw odds | 3.55 |
| Reference away odds | 1.96 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | +1.6% |
| Draw probability edge | -1.0% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | +12.7% |
| Under 2.5 probability edge | -12.7% |
| Raw edge prob home | 0.0325 |
| Raw ev home | 0.0811 |
| Raw edge prob draw | -0.0209 |
| Raw ev draw | -0.1671 |
| Raw edge prob away | -0.0116 |
| Raw ev away | 0.0252 |
| Market p home draw | 52.2% |
| Market home draw odds | 1.79 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:34:32Z |
| Market reference home draw last update utc | 2026-10-18T14:34:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.9% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:34:32Z |
| Market reference draw away last update utc | 2026-10-18T14:34:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:34:32Z |
| Market reference home away last update utc | 2026-10-18T14:34:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.28 |
| Market reference dc home draw odds | 1.86 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 74.6% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T14:32:53Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:52Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.2% |
| Market under 3 5 odds | 1.27 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T14:32:53Z |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.45 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:51Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.6% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:34:32Z |
| Market reference btts yes odds | 1.81 |
| Market reference btts yes opposite odds | 2.08 |
| Market reference btts yes last update utc | 2026-10-18T14:34:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **52.8%**. Expected goals are 1.77 for Lyon and 1.09 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.6%; Under 3.5 goals: 67.9%; Double Chance 1X: 76.9%; Double Chance X2: 47.2%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 55.5%; BTTS No (at least one team does not score): 44.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 52.8% | 1.89 |
| Draw | 24.1% | 4.15 |
| Nice win | 23.1% | 4.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.77 |
| Nice expected goals | 1.09 |
| Expected total goals | 2.86 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 54.6% |
| Under 2.5 | 45.4% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.40% |
| 2 | 2-1 | 9.78% |
| 3 | 1-0 | 9.63% |
| 4 | 2-0 | 8.99% |
| 5 | 0-0 | 6.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 52.8% | 52.8% | 1.92 | +1.5% |
| Draw | 24.1% | 23.8% | 3.94 | -5.1% |
| Nice win | 23.1% | 23.4% | 4.16 | -4.0% |
| Over 2.5 | 54.6% | 56.7% | 1.75 | -4.5% |
| Under 2.5 | 45.4% | 43.3% | 2.25 | +2.2% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 55.5% |
| P btts no | 44.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.23 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.63 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.17 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 52.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| P home draw | 76.9% |
| P draw away | 47.2% |
| P home away | 75.9% |
| Raw p home draw | 77.3% |
| Raw p draw away | 47.1% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.82 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | +0.0% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | 0.0007 |
| Raw ev home | 0.0154 |
| Raw edge prob draw | 0.0065 |
| Raw ev draw | -0.0384 |
| Raw edge prob away | -0.0072 |
| Raw ev away | -0.0552 |
| Market p home draw | 76.9% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:34:32Z |
| Market reference home draw last update utc | 2026-10-18T14:34:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.1% |
| Market draw away odds | 1.98 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:34:32Z |
| Market reference draw away last update utc | 2026-10-18T14:34:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:34:32Z |
| Market reference home away last update utc | 2026-10-18T14:34:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.95 |
| Market reference dc home draw odds | 1.22 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 81.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.6% |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:51Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:34:32Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-18T14:34:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **44.2%**. Expected goals are 1.57 for Paris FC and 1.37 for Rennes (2.94 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 56.4%; Under 3.5 goals: 66.1%; Double Chance 1X: 69.3%; Double Chance X2: 55.8%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 82.5%; BTTS Yes (both teams score): 59.4%; BTTS No (at least one team does not score): 40.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 44.2% | 2.26 |
| Draw | 25.2% | 3.97 |
| Rennes win | 30.7% | 3.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.57 |
| Rennes expected goals | 1.37 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 79.7% |
| Under 1.5 | 20.3% |
| Over 2.5 | 56.4% |
| Under 2.5 | 43.6% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.5% |
| Under 4.5 | 82.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.76% |
| 2 | 2-1 | 9.45% |
| 3 | 1-0 | 8.26% |
| 4 | 1-2 | 7.28% |
| 5 | 2-0 | 6.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 44.2% | 46.6% | 2.17 | -4.2% |
| Draw | 25.2% | 24.9% | 3.62 | -8.8% |
| Rennes win | 30.7% | 28.5% | 3.60 | +10.4% |
| Over 2.5 | 56.4% | 58.6% | 1.72 | -3.0% |
| Under 2.5 | 43.6% | 41.4% | 2.30 | +0.3% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.4% |
| P btts no | 40.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.36 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.92 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.72 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 41.7% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 32.8% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 66.2% |
| Raw p btts yes | 59.5% |
| P home draw | 69.3% |
| P draw away | 55.8% |
| P home away | 74.8% |
| Raw p home draw | 67.2% |
| Raw p draw away | 58.3% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -2.4% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | -0.0489 |
| Raw ev home | -0.0950 |
| Raw edge prob draw | 0.0066 |
| Raw ev draw | -0.0761 |
| Raw edge prob away | 0.0423 |
| Raw ev away | 0.1798 |
| Market p home draw | 70.9% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:34:32Z |
| Market reference home draw last update utc | 2026-10-18T14:34:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.5% |
| Market draw away odds | 1.77 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:34:32Z |
| Market reference draw away last update utc | 2026-10-18T14:34:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:34:32Z |
| Market reference home away last update utc | 2026-10-18T14:34:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.5% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.8% |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.61 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:51Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 61.3% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:34:32Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-18T14:34:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **43.7%**. Expected goals are 1.56 for Brest and 1.27 for Nice (2.83 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.9%; Under 3.5 goals: 68.5%; Double Chance 1X: 69.2%; Double Chance X2: 56.3%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 43.7% | 2.29 |
| Draw | 25.5% | 3.92 |
| Nice win | 30.8% | 3.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Nice expected goals | 1.27 |
| Expected total goals | 2.83 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 31.5% |
| Under 3.5 | 68.5% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.04% |
| 2 | 2-1 | 9.17% |
| 3 | 1-0 | 8.71% |
| 4 | 1-2 | 7.47% |
| 5 | 2-0 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 43.7% | 44.1% | 2.31 | +1.0% |
| Draw | 25.5% | 25.1% | 3.49 | -11.0% |
| Nice win | 30.8% | 30.9% | 3.37 | +3.7% |
| Over 2.5 | 53.9% | 56.0% | 1.76 | -5.1% |
| Under 2.5 | 46.1% | 44.0% | 2.23 | +2.8% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.78 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.35 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.5% |
| Raw p btts yes | 57.4% |
| P home draw | 69.2% |
| P draw away | 56.3% |
| P home away | 74.5% |
| Raw p home draw | 69.3% |
| Raw p draw away | 56.6% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.0067 |
| Raw ev home | 0.0026 |
| Raw edge prob draw | 0.0086 |
| Raw ev draw | -0.0950 |
| Raw edge prob away | -0.0019 |
| Raw ev away | 0.0334 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **48.5%**. Expected goals are 1.59 for RC Lens and 1.01 for Paris FC (2.59 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.3%; Under 3.5 goals: 73.8%; Double Chance 1X: 73.6%; Double Chance X2: 51.5%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 87.8%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 48.5% | 2.06 |
| Draw | 25.0% | 4.00 |
| Paris FC win | 26.4% | 3.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.59 |
| Paris FC expected goals | 1.01 |
| Expected total goals | 2.59 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 48.3% |
| Under 2.5 | 51.7% |
| Over 3.5 | 26.2% |
| Under 3.5 | 73.8% |
| Over 4.5 | 12.2% |
| Under 4.5 | 87.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.92% |
| 2 | 1-0 | 10.90% |
| 3 | 2-1 | 9.14% |
| 4 | 2-0 | 9.08% |
| 5 | 0-1 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 48.5% | 46.8% | 2.09 | +1.4% |
| Draw | 25.0% | 23.8% | 3.90 | -2.4% |
| Paris FC win | 26.4% | 29.4% | 3.58 | -5.3% |
| Over 2.5 | 48.3% | 58.8% | 1.68 | -18.8% |
| Under 2.5 | 51.7% | 41.2% | 2.38 | +23.0% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.07 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.82 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.16 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 50.3% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 51.1% |
| P home draw | 73.6% |
| P draw away | 51.5% |
| P home away | 75.0% |
| Raw p home draw | 76.5% |
| Raw p draw away | 49.7% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | +1.8% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | 0.0356 |
| Raw ev home | 0.0516 |
| Raw edge prob draw | 0.0241 |
| Raw ev draw | 0.0226 |
| Raw edge prob away | -0.0597 |
| Raw ev away | -0.1599 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **67.9%**. Expected goals are 2.45 for Toulouse and 0.66 for Troyes (3.11 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 58.0%; Under 3.5 goals: 64.1%; Double Chance 1X: 86.4%; Double Chance X2: 32.1%; Double Chance 12 (either team wins): 81.5%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 46.1%; BTTS No (at least one team does not score): 53.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 67.9% | 1.47 |
| Draw | 18.5% | 5.41 |
| Troyes win | 13.6% | 7.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 2.45 |
| Troyes expected goals | 0.66 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 58.0% |
| Under 2.5 | 42.0% |
| Over 3.5 | 35.9% |
| Under 3.5 | 64.1% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.88% |
| 2 | 3-0 | 9.69% |
| 3 | 1-0 | 9.42% |
| 4 | 1-1 | 8.80% |
| 5 | 2-1 | 7.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 67.9% | 59.5% | 1.71 | +16.1% |
| Draw | 18.5% | 21.0% | 4.26 | -21.3% |
| Troyes win | 13.6% | 19.5% | 5.13 | -30.1% |
| Over 2.5 | 58.0% | 59.2% | 1.67 | -3.1% |
| Under 2.5 | 42.0% | 40.8% | 2.40 | +0.8% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 46.1% |
| P btts no | 53.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.94 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.11 |
| Fair Over 2.5 odds | 1.72 |
| Fair Under 2.5 odds | 2.38 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 76.3% |
| Unadjusted draw probability | 15.9% |
| Unadjusted away-win probability | 7.8% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 44.6% |
| P home draw | 86.4% |
| P draw away | 32.1% |
| P home away | 81.5% |
| Raw p home draw | 92.2% |
| Raw p draw away | 23.7% |
| Raw p home away | 84.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.60 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | +8.4% |
| Draw probability edge | -2.6% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -1.2% |
| Under 2.5 probability edge | +1.2% |
| Raw edge prob home | 0.1683 |
| Raw ev home | 0.3052 |
| Raw edge prob draw | -0.0514 |
| Raw ev draw | -0.3228 |
| Raw edge prob away | -0.1168 |
| Raw ev away | -0.6011 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **44.1%**. Expected goals are 1.46 for AS Monaco and 1.26 for Lille (2.72 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 51.4%; Under 3.5 goals: 71.0%; Double Chance 1X: 70.0%; Double Chance X2: 55.9%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 44.1% | 2.27 |
| Draw | 25.9% | 3.87 |
| Lille win | 30.0% | 3.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.46 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.72 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 76.1% |
| Under 1.5 | 23.9% |
| Over 2.5 | 51.4% |
| Under 2.5 | 48.6% |
| Over 3.5 | 29.0% |
| Under 3.5 | 71.0% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.30% |
| 2 | 1-0 | 9.70% |
| 3 | 2-1 | 9.45% |
| 4 | 2-0 | 7.53% |
| 5 | 0-1 | 7.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 44.1% | 46.9% | 2.18 | -3.8% |
| Draw | 25.9% | 25.1% | 3.60 | -6.9% |
| Lille win | 30.0% | 28.1% | 3.60 | +8.0% |
| Over 2.5 | 51.4% | 55.8% | 1.77 | -9.1% |
| Under 2.5 | 48.6% | 44.2% | 2.22 | +8.0% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.38 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.18 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.10 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 41.4% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 31.9% |
| Raw p over 1 5 | 76.0% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 55.5% |
| P home draw | 70.0% |
| P draw away | 55.9% |
| P home away | 74.1% |
| Raw p home draw | 68.1% |
| Raw p draw away | 58.6% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -2.8% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | -0.0551 |
| Raw ev home | -0.0980 |
| Raw edge prob draw | 0.0164 |
| Raw ev draw | -0.0390 |
| Raw edge prob away | 0.0387 |
| Raw ev away | 0.1494 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **37.0%**. Expected goals are 1.09 for Angers and 1.24 for Lorient (2.33 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.5%; Under 3.5 goals: 79.3%; Double Chance 1X: 63.0%; Double Chance X2: 65.4%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 91.2%; BTTS Yes (both teams score): 47.6%; BTTS No (at least one team does not score): 52.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 34.6% | 2.89 |
| Draw | 28.4% | 3.52 |
| Lorient win | 37.0% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.09 |
| Lorient expected goals | 1.24 |
| Expected total goals | 2.33 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 68.2% |
| Under 1.5 | 31.8% |
| Over 2.5 | 41.5% |
| Under 2.5 | 58.5% |
| Over 3.5 | 20.7% |
| Under 3.5 | 79.3% |
| Over 4.5 | 8.8% |
| Under 4.5 | 91.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.34% |
| 2 | 1-0 | 10.90% |
| 3 | 0-1 | 10.87% |
| 4 | 0-0 | 10.02% |
| 5 | 2-1 | 7.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 34.6% | 37.4% | 2.69 | -6.9% |
| Draw | 28.4% | 27.5% | 3.40 | -3.5% |
| Lorient win | 37.0% | 35.1% | 2.85 | +5.5% |
| Over 2.5 | 41.5% | 44.9% | 2.19 | -9.2% |
| Under 2.5 | 58.5% | 55.1% | 1.79 | +4.8% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.6% |
| P btts no | 52.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.98 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.15 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.84 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.37 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 31.8% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 68.2% |
| Raw p under 3 5 | 79.3% |
| Raw p btts yes | 47.8% |
| P home draw | 63.0% |
| P draw away | 65.4% |
| P home away | 71.6% |
| Raw p home draw | 61.0% |
| Raw p draw away | 68.2% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.45 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.19 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -2.8% |
| Draw probability edge | +0.9% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | -0.0569 |
| Raw ev home | -0.1457 |
| Raw edge prob draw | 0.0180 |
| Raw ev draw | -0.0047 |
| Raw edge prob away | 0.0388 |
| Raw ev away | 0.1106 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **46.3%**. Expected goals are 1.82 for Auxerre and 1.40 for Le Mans FC (3.22 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 62.1%; Under 3.5 goals: 59.9%; Double Chance 1X: 70.9%; Double Chance X2: 53.7%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 63.8%; BTTS No (at least one team does not score): 36.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 46.3% | 2.16 |
| Draw | 24.6% | 4.07 |
| Le Mans FC win | 29.1% | 3.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.82 |
| Le Mans FC expected goals | 1.40 |
| Expected total goals | 3.22 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 83.6% |
| Under 1.5 | 16.4% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 40.1% |
| Under 3.5 | 59.9% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.02% |
| 2 | 2-1 | 9.13% |
| 3 | 1-2 | 7.10% |
| 4 | 2-2 | 6.71% |
| 5 | 1-0 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 46.3% | 45.6% | 2.23 | +3.3% |
| Draw | 24.6% | 25.4% | 3.70 | -9.1% |
| Le Mans FC win | 29.1% | 29.0% | 3.37 | -1.9% |
| Over 2.5 | 62.1% | 55.4% | 1.78 | +10.6% |
| Under 2.5 | 37.9% | 44.6% | 2.20 | -16.7% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.8% |
| P btts no | 36.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.63 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.09 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.49 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.52 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 29.2% |
| Raw p over 1 5 | 83.6% |
| Raw p under 3 5 | 59.8% |
| Raw p btts yes | 63.6% |
| P home draw | 70.9% |
| P draw away | 53.7% |
| P home away | 75.4% |
| Raw p home draw | 70.8% |
| Raw p draw away | 53.0% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +6.7% |
| Under 2.5 probability edge | -6.7% |
| Raw edge prob home | 0.0144 |
| Raw ev home | 0.0490 |
| Raw edge prob draw | -0.0163 |
| Raw ev draw | -0.1207 |
| Raw edge prob away | 0.0019 |
| Raw ev away | -0.0160 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **63.2%**. Expected goals are 2.13 for Marseille and 0.86 for Le Havre (2.99 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 57.1%; Under 3.5 goals: 65.5%; Double Chance 1X: 83.7%; Double Chance X2: 36.8%; Double Chance 12 (either team wins): 79.6%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 63.2% | 1.58 |
| Draw | 20.4% | 4.89 |
| Le Havre win | 16.3% | 6.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.13 |
| Le Havre expected goals | 0.86 |
| Expected total goals | 2.99 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 79.9% |
| Under 1.5 | 20.1% |
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.5% |
| Under 3.5 | 65.5% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.91% |
| 2 | 1-0 | 9.86% |
| 3 | 1-1 | 9.72% |
| 4 | 2-1 | 9.39% |
| 5 | 3-0 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 63.2% | 60.4% | 1.64 | +3.7% |
| Draw | 20.4% | 20.6% | 4.57 | -6.6% |
| Le Havre win | 16.3% | 19.0% | 5.33 | -12.9% |
| Over 2.5 | 57.1% | 59.5% | 1.66 | -5.3% |
| Under 2.5 | 42.9% | 40.5% | 2.42 | +3.9% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.16 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.99 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.55 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 66.0% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 13.6% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 65.0% |
| Raw p btts yes | 51.3% |
| P home draw | 83.7% |
| P draw away | 36.8% |
| P home away | 79.6% |
| Raw p home draw | 86.4% |
| Raw p draw away | 34.0% |
| Raw p home away | 79.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.50 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | +2.8% |
| Draw probability edge | -0.1% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | 0.0565 |
| Raw ev home | 0.0831 |
| Raw edge prob draw | -0.0023 |
| Raw ev draw | -0.0712 |
| Raw edge prob away | -0.0541 |
| Raw ev away | -0.2732 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **67.9%**. Expected goals are 2.31 for Paris Saint Germain and 1.06 for Lyon (3.37 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 66.4%; Under 3.5 goals: 56.0%; Double Chance 1X: 85.3%; Double Chance X2: 32.1%; Double Chance 12 (either team wins): 82.6%; Under 4.5 goals: 74.4%; BTTS Yes (both teams score): 58.6%; BTTS No (at least one team does not score): 41.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 67.9% | 1.47 |
| Draw | 17.4% | 5.75 |
| Lyon win | 14.7% | 6.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.31 |
| Lyon expected goals | 1.06 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 85.6% |
| Under 1.5 | 14.4% |
| Over 2.5 | 66.4% |
| Under 2.5 | 33.6% |
| Over 3.5 | 44.0% |
| Under 3.5 | 56.0% |
| Over 4.5 | 25.6% |
| Under 4.5 | 74.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.15% |
| 2 | 2-0 | 9.58% |
| 3 | 1-1 | 7.87% |
| 4 | 1-0 | 7.87% |
| 5 | 3-1 | 7.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 67.9% | 70.8% | 1.43 | -2.9% |
| Draw | 17.4% | 15.3% | 5.44 | -5.5% |
| Lyon win | 14.7% | 13.9% | 7.60 | +11.9% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 58.6% |
| P btts no | 41.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.26 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.97 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.97 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.90 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 65.0% |
| Unadjusted draw probability | 19.4% |
| Unadjusted away-win probability | 15.6% |
| Raw p over 1 5 | 85.4% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 59.3% |
| P home draw | 85.3% |
| P draw away | 32.1% |
| P home away | 82.6% |
| Raw p home draw | 84.4% |
| Raw p draw away | 35.0% |
| Raw p home away | 80.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.36 |
| Reference draw odds | 5.30 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:33Z |
| Home probability edge | -2.9% |
| Draw probability edge | +2.0% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0577 |
| Raw ev home | -0.0703 |
| Raw edge prob draw | 0.0406 |
| Raw ev draw | 0.0556 |
| Raw edge prob away | 0.0171 |
| Raw ev away | 0.1842 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **51.5%**. Expected goals are 1.87 for Rennes and 1.48 for Strasbourg (3.36 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.7%; Under 3.5 goals: 56.6%; Double Chance 1X: 73.5%; Double Chance X2: 48.5%; Double Chance 12 (either team wins): 78.0%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 65.5%; BTTS No (at least one team does not score): 34.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 51.5% | 1.94 |
| Draw | 22.0% | 4.55 |
| Strasbourg win | 26.5% | 3.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.87 |
| Strasbourg expected goals | 1.48 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 65.7% |
| Under 2.5 | 34.3% |
| Over 3.5 | 43.4% |
| Under 3.5 | 56.6% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.06% |
| 2 | 1-1 | 9.57% |
| 3 | 2-0 | 6.78% |
| 4 | 1-0 | 6.75% |
| 5 | 2-2 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 51.5% | 56.6% | 1.74 | -10.4% |
| Draw | 22.0% | 20.7% | 4.52 | -0.6% |
| Strasbourg win | 26.5% | 22.8% | 4.58 | +21.5% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Bbs statistics cutoff utc | 2026-10-18T14:34:48.221876+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.5% |
| P btts no | 34.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.89 |
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
| P home draw | 73.5% |
| P draw away | 48.5% |
| P home away | 78.0% |
| Raw p home draw | 69.7% |
| Raw p draw away | 53.6% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.68 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:33Z |
| Home probability edge | -5.1% |
| Draw probability edge | +1.3% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | -0.1018 |
| Raw ev home | -0.1929 |
| Raw edge prob draw | 0.0261 |
| Raw ev draw | 0.0528 |
| Raw edge prob away | 0.0757 |
| Raw ev away | 0.3888 |

</details>


---
