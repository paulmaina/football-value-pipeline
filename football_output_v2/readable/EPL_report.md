# Premier League — football model report

Fixtures in this report: **12**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,969 |
| Training data through | 2026-10-18 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | c736b4386263e7d589d674450cebef781014107b1eac01908840954e73b9544c |
| Training as of utc | 2026-10-19T11:18:42.147910+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 69, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 69, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-19T11:18:42.147910+00:00', 'observations': 88, 'observations_sha256': 'd86f7a4520641bf97de242b306e0dea9484b1d40099eef414af45b13ee142da2', 'eligible_training_matches': 18, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 52, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 18, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '52f1cde52d38f74244588d4d20a698e6aac858d03914a9dbea94526f9b2a90eb', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 933.148 |
| Base scoring parameter | 0.210 |
| Home-advantage parameter | 0.183 |
| Dixon-Coles low-score adjustment | -0.090 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 12.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261019T111842147910Z_22be1672955e5cba3fef824263ae87461dfea1aa1213c9028432334b30a7d489.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **58.2%**. Expected goals are 0.74 for Nottingham Forest and 1.52 for Arsenal (2.26 combined). The most likely exact score is 0-1 at 15.7%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 40.3%; Under 3.5 goals: 80.5%; Double Chance 1X: 41.8%; Double Chance X2: 83.8%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 41.3%; BTTS No (at least one team does not score): 58.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.2% | 6.19 |
| Draw | 25.6% | 3.90 |
| Arsenal win | 58.2% | 1.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.74 |
| Arsenal expected goals | 1.52 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 67.4% |
| Under 1.5 | 32.6% |
| Over 2.5 | 40.3% |
| Under 2.5 | 59.7% |
| Over 3.5 | 19.5% |
| Under 3.5 | 80.5% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.75% |
| 2 | 0-2 | 12.79% |
| 3 | 1-1 | 11.70% |
| 4 | 0-0 | 10.52% |
| 5 | 1-2 | 9.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.2% | 15.1% | 6.19 | +0.0% |
| Draw | 25.6% | 23.2% | 4.00 | +2.5% |
| Arsenal win | 58.2% | 61.7% | 1.66 | -3.4% |
| Over 2.5 | 40.3% | 48.0% | 1.99 | -19.9% |
| Under 2.5 | 59.7% | 52.0% | 1.95 | +16.5% |

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
| Dc lambda home | 0.7416 |
| Dc lambda away | 1.5154 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 41.3% |
| P btts no | 58.7% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.51 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.07 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.12 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.27 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 17.2% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 41.9% |
| P home draw | 41.8% |
| P draw away | 83.8% |
| P home away | 74.4% |
| Raw p home draw | 45.3% |
| Raw p draw away | 82.8% |
| Raw p home away | 71.9% |
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
| Draw probability edge | +2.5% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.0210 |
| Raw ev home | 0.0649 |
| Raw edge prob draw | 0.0493 |
| Raw ev draw | 0.1241 |
| Raw edge prob away | -0.0703 |
| Raw ev away | -0.0921 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **56.4%**. Expected goals are 1.49 for Tottenham Hotspur and 1.07 for Coventry City (2.56 combined). The most likely exact score is 1-0 at 12.8%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.1%; Under 3.5 goals: 73.8%; Double Chance 1X: 79.8%; Double Chance X2: 43.6%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 56.4% | 1.77 |
| Draw | 23.5% | 4.26 |
| Coventry City win | 20.2% | 4.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.49 |
| Coventry City expected goals | 1.07 |
| Expected total goals | 2.56 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.3% |
| Under 1.5 | 25.7% |
| Over 2.5 | 49.1% |
| Under 2.5 | 50.9% |
| Over 3.5 | 26.2% |
| Under 3.5 | 73.8% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.79% |
| 2 | 2-1 | 11.29% |
| 3 | 1-1 | 11.21% |
| 4 | 2-0 | 10.57% |
| 5 | 0-0 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 56.4% | 66.8% | 1.54 | -13.2% |
| Draw | 23.5% | 18.8% | 4.67 | +9.6% |
| Coventry City win | 20.2% | 14.3% | 6.50 | +31.1% |
| Over 2.5 | 49.1% | 60.2% | 1.64 | -19.4% |
| Under 2.5 | 50.9% | 39.8% | 2.46 | +25.2% |

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
| Dc lambda home | 1.4933 |
| Dc lambda away | 1.0689 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.57 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.89 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.81 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.05 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 45.9% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 26.0% |
| Raw p over 1 5 | 73.6% |
| Raw p under 3 5 | 74.4% |
| Raw p btts yes | 52.0% |
| P home draw | 79.8% |
| P draw away | 43.6% |
| P home away | 76.5% |
| Raw p home draw | 74.0% |
| Raw p draw away | 54.1% |
| Raw p home away | 71.9% |
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
| Home probability edge | -10.5% |
| Draw probability edge | +4.7% |
| Away probability edge | +5.8% |
| Over 2.5 probability edge | -11.1% |
| Under 2.5 probability edge | +11.1% |
| Raw edge prob home | -0.2097 |
| Raw ev home | -0.2937 |
| Raw edge prob draw | 0.0930 |
| Raw ev draw | 0.3137 |
| Raw edge prob away | 0.1167 |
| Raw ev away | 0.6904 |
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

The model's most likely 1X2 outcome is **Nottingham Forest win** at **44.0%**. Expected goals are 1.32 for Ipswich Town and 1.70 for Nottingham Forest (3.02 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.9%; Under 3.5 goals: 64.3%; Double Chance 1X: 56.0%; Double Chance X2: 70.3%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 81.3%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 29.7% | 3.37 |
| Draw | 26.3% | 3.80 |
| Nottingham Forest win | 44.0% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.32 |
| Nottingham Forest expected goals | 1.70 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 81.3% |
| Under 1.5 | 18.7% |
| Over 2.5 | 57.9% |
| Under 2.5 | 42.1% |
| Over 3.5 | 35.7% |
| Under 3.5 | 64.3% |
| Over 4.5 | 18.7% |
| Under 4.5 | 81.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.21% |
| 2 | 1-2 | 9.01% |
| 3 | 2-1 | 7.44% |
| 4 | 0-1 | 7.07% |
| 5 | 0-2 | 6.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 29.7% | 30.6% | 3.10 | -7.9% |
| Draw | 26.3% | 26.9% | 3.63 | -4.5% |
| Nottingham Forest win | 44.0% | 42.5% | 2.39 | +5.1% |
| Over 2.5 | 57.9% | 53.2% | 1.84 | +6.6% |
| Under 2.5 | 42.1% | 46.8% | 2.12 | -10.8% |

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
| Dc lambda home | 1.3203 |
| Dc lambda away | 1.7009 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.67 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.35 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.38 |
| Fair Over 3.5 odds | 2.80 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.34 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 28.8% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 81.4% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 60.9% |
| P home draw | 56.0% |
| P draw away | 70.3% |
| P home away | 73.7% |
| Raw p home draw | 54.6% |
| Raw p draw away | 71.2% |
| Raw p home away | 74.3% |
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
| Home probability edge | -0.9% |
| Draw probability edge | -0.6% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +4.7% |
| Under 2.5 probability edge | -4.7% |
| Raw edge prob home | -0.0171 |
| Raw ev home | -0.1058 |
| Raw edge prob draw | -0.0119 |
| Raw ev draw | -0.0666 |
| Raw edge prob away | 0.0289 |
| Raw ev away | 0.0860 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **67.4%**. Expected goals are 1.72 for Arsenal and 0.58 for Everton (2.30 combined). The most likely exact score is 1-0 at 17.2%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 41.6%; Under 3.5 goals: 79.6%; Double Chance 1X: 89.0%; Double Chance X2: 32.6%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 36.1%; BTTS No (at least one team does not score): 63.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 67.4% | 1.48 |
| Draw | 21.5% | 4.64 |
| Everton win | 11.0% | 9.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.72 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.30 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 68.4% |
| Under 1.5 | 31.6% |
| Over 2.5 | 41.6% |
| Under 2.5 | 58.4% |
| Over 3.5 | 20.4% |
| Under 3.5 | 79.6% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.17% |
| 2 | 2-0 | 15.59% |
| 3 | 0-0 | 9.59% |
| 4 | 1-1 | 9.53% |
| 5 | 2-1 | 8.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 67.4% | 70.5% | 1.43 | -3.6% |
| Draw | 21.5% | 18.5% | 4.93 | +6.2% |
| Everton win | 11.0% | 11.0% | 8.90 | -1.9% |
| Over 2.5 | 41.6% | 53.0% | 1.83 | -23.9% |
| Under 2.5 | 58.4% | 47.0% | 2.14 | +25.0% |

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
| Dc lambda home | 1.7215 |
| Dc lambda away | 0.5769 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.1% |
| P btts no | 63.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.43 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.16 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.89 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.53 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 64.4% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 11.1% |
| Raw p over 1 5 | 67.8% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 36.9% |
| P home draw | 89.0% |
| P draw away | 32.6% |
| P home away | 78.5% |
| Raw p home draw | 88.9% |
| Raw p draw away | 35.6% |
| Raw p home away | 75.4% |
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
| Home probability edge | -3.1% |
| Draw probability edge | +3.0% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -11.4% |
| Under 2.5 probability edge | +11.4% |
| Raw edge prob home | -0.0614 |
| Raw ev home | -0.0797 |
| Raw edge prob draw | 0.0608 |
| Raw ev draw | 0.2120 |
| Raw edge prob away | 0.0006 |
| Raw ev away | -0.0160 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **54.9%**. Expected goals are 1.12 for Aston Villa and 1.83 for Manchester City (2.96 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 57.1%; Under 3.5 goals: 65.6%; Double Chance 1X: 45.1%; Double Chance X2: 78.6%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 82.1%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 21.4% | 4.68 |
| Draw | 23.8% | 4.21 |
| Manchester City win | 54.9% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.12 |
| Manchester City expected goals | 1.83 |
| Expected total goals | 2.96 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 17.9% |
| Under 4.5 | 82.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.20% |
| 2 | 1-2 | 10.14% |
| 3 | 0-2 | 9.05% |
| 4 | 0-1 | 8.87% |
| 5 | 1-3 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 21.4% | 20.6% | 4.72 | +0.9% |
| Draw | 23.8% | 22.8% | 4.26 | +1.3% |
| Manchester City win | 54.9% | 56.6% | 1.76 | -3.5% |

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
| Dc lambda home | 1.1207 |
| Dc lambda away | 1.8345 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.89 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.13 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.58 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 22.1% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 53.1% |
| Raw p over 1 5 | 80.4% |
| Raw p under 3 5 | 65.7% |
| Raw p btts yes | 57.6% |
| P home draw | 45.1% |
| P draw away | 78.6% |
| P home away | 76.2% |
| Raw p home draw | 46.9% |
| Raw p draw away | 77.9% |
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
| Home probability edge | +0.7% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | 0.0148 |
| Raw ev home | 0.0440 |
| Raw edge prob draw | 0.0203 |
| Raw ev draw | 0.0557 |
| Raw edge prob away | -0.0351 |
| Raw ev away | -0.0655 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **56.7%**. Expected goals are 2.13 for Chelsea and 1.16 for Tottenham Hotspur (3.29 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.6%; Double Chance 1X: 79.1%; Double Chance X2: 43.3%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 76.7%; BTTS Yes (both teams score): 61.5%; BTTS No (at least one team does not score): 38.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 56.7% | 1.76 |
| Draw | 22.4% | 4.46 |
| Tottenham Hotspur win | 20.9% | 4.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.13 |
| Tottenham Hotspur expected goals | 1.16 |
| Expected total goals | 3.29 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 63.6% |
| Under 2.5 | 36.4% |
| Over 3.5 | 41.4% |
| Under 3.5 | 58.6% |
| Over 4.5 | 23.3% |
| Under 4.5 | 76.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.18% |
| 2 | 2-1 | 9.46% |
| 3 | 2-0 | 8.17% |
| 4 | 1-0 | 6.87% |
| 5 | 3-1 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 56.7% | 54.6% | 1.81 | +2.6% |
| Draw | 22.4% | 22.7% | 4.30 | -3.6% |
| Tottenham Hotspur win | 20.9% | 22.7% | 4.36 | -8.8% |

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
| Dc lambda home | 2.1298 |
| Dc lambda away | 1.1570 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.5% |
| P btts no | 38.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.58 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.53 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.41 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.29 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 84.8% |
| Raw p under 3 5 | 58.3% |
| Raw p btts yes | 61.2% |
| P home draw | 79.1% |
| P draw away | 43.3% |
| P home away | 77.6% |
| Raw p home draw | 80.9% |
| Raw p draw away | 41.2% |
| Raw p home away | 77.9% |
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
| Home probability edge | +2.1% |
| Draw probability edge | -0.3% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0421 |
| Raw ev home | 0.0640 |
| Raw edge prob draw | -0.0061 |
| Raw ev draw | -0.0496 |
| Raw edge prob away | -0.0360 |
| Raw ev away | -0.1666 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **38.8%**. Expected goals are 1.11 for Coventry City and 1.21 for Fulham (2.32 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 41.6%; Under 3.5 goals: 79.4%; Double Chance 1X: 61.2%; Double Chance X2: 67.5%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 91.2%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 32.5% | 3.07 |
| Draw | 28.7% | 3.48 |
| Fulham win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.11 |
| Fulham expected goals | 1.21 |
| Expected total goals | 2.32 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 68.7% |
| Under 1.5 | 31.3% |
| Over 2.5 | 41.6% |
| Under 2.5 | 58.4% |
| Over 3.5 | 20.6% |
| Under 3.5 | 79.4% |
| Over 4.5 | 8.8% |
| Under 4.5 | 91.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.52% |
| 2 | 0-1 | 11.16% |
| 3 | 0-0 | 10.35% |
| 4 | 1-0 | 9.79% |
| 5 | 1-2 | 8.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 32.5% | 32.7% | 3.12 | +1.5% |
| Draw | 28.7% | 26.9% | 3.61 | +3.6% |
| Fulham win | 38.8% | 40.4% | 2.39 | -7.4% |
| Over 2.5 | 41.6% | 55.2% | 1.81 | -24.7% |
| Under 2.5 | 58.4% | 44.8% | 2.15 | +25.6% |

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
| Dc lambda home | 1.1118 |
| Dc lambda away | 1.2083 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.66 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.86 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.39 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 32.3% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 37.1% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 48.3% |
| P home draw | 61.2% |
| P draw away | 67.5% |
| P home away | 71.3% |
| Raw p home draw | 62.9% |
| Raw p draw away | 67.7% |
| Raw p home away | 69.4% |
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
| Home probability edge | -0.2% |
| Draw probability edge | +1.9% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -13.7% |
| Under 2.5 probability edge | +13.7% |
| Raw edge prob home | -0.0037 |
| Raw ev home | 0.0091 |
| Raw edge prob draw | 0.0371 |
| Raw ev draw | 0.1035 |
| Raw edge prob away | -0.0334 |
| Raw ev away | -0.1136 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **39.3%**. Expected goals are 1.49 for Crystal Palace and 1.59 for Newcastle United (3.08 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.4%; Under 3.5 goals: 62.9%; Double Chance 1X: 60.7%; Double Chance X2: 65.5%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 62.8%; BTTS No (at least one team does not score): 37.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 34.5% | 2.90 |
| Draw | 26.2% | 3.82 |
| Newcastle United win | 39.3% | 2.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.49 |
| Newcastle United expected goals | 1.59 |
| Expected total goals | 3.08 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.3% |
| Under 1.5 | 17.7% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 37.1% |
| Under 3.5 | 62.9% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.00% |
| 2 | 1-2 | 8.69% |
| 3 | 2-1 | 8.00% |
| 4 | 2-2 | 6.53% |
| 5 | 0-1 | 6.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 34.5% | 34.0% | 3.02 | +4.2% |
| Draw | 26.2% | 26.5% | 3.67 | -4.0% |
| Newcastle United win | 39.3% | 39.6% | 2.42 | -4.8% |
| Over 2.5 | 59.4% | 59.2% | 1.69 | +0.4% |
| Under 2.5 | 40.6% | 40.8% | 2.36 | -4.2% |

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
| Dc lambda home | 1.4945 |
| Dc lambda away | 1.5882 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.8% |
| P btts no | 37.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.75 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.64 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.04 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 35.0% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 39.1% |
| Raw p over 1 5 | 82.3% |
| Raw p under 3 5 | 62.9% |
| Raw p btts yes | 62.7% |
| P home draw | 60.7% |
| P draw away | 65.5% |
| P home away | 73.8% |
| Raw p home draw | 60.9% |
| Raw p draw away | 65.0% |
| Raw p home away | 74.1% |
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
| Home probability edge | +0.5% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0107 |
| Raw ev home | 0.0580 |
| Raw edge prob draw | -0.0061 |
| Raw ev draw | -0.0507 |
| Raw edge prob away | -0.0047 |
| Raw ev away | -0.0537 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **42.6%**. Expected goals are 1.21 for Hull City and 1.05 for Brentford (2.27 combined). The most likely exact score is 0-1 at 13.5%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 40.6%; Under 3.5 goals: 80.6%; Double Chance 1X: 57.4%; Double Chance X2: 70.0%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 46.3%; BTTS No (at least one team does not score): 53.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 30.0% | 3.33 |
| Draw | 27.4% | 3.65 |
| Brentford win | 42.6% | 2.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.21 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.27 |
| Over 0.5 | 89.7% |
| Under 0.5 | 10.3% |
| Over 1.5 | 67.3% |
| Under 1.5 | 32.7% |
| Over 2.5 | 40.6% |
| Under 2.5 | 59.4% |
| Over 3.5 | 19.4% |
| Under 3.5 | 80.6% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.54% |
| 2 | 1-1 | 12.81% |
| 3 | 0-0 | 10.26% |
| 4 | 1-2 | 9.71% |
| 5 | 1-0 | 8.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 30.0% | 21.6% | 4.72 | +41.7% |
| Draw | 27.4% | 23.9% | 4.09 | +12.1% |
| Brentford win | 42.6% | 54.5% | 1.79 | -23.8% |
| Over 2.5 | 40.6% | 55.6% | 1.73 | -29.8% |
| Under 2.5 | 59.4% | 44.4% | 2.28 | +35.5% |

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
| Dc lambda home | 1.2120 |
| Dc lambda away | 1.0535 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.3% |
| P btts no | 53.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.74 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.47 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.16 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.19 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 38.5% |
| Unadjusted draw probability | 30.9% |
| Unadjusted away-win probability | 30.6% |
| Raw p over 1 5 | 67.3% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 46.9% |
| P home draw | 57.4% |
| P draw away | 70.0% |
| P home away | 72.6% |
| Raw p home draw | 69.4% |
| Raw p draw away | 61.5% |
| Raw p home away | 69.1% |
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
| Home probability edge | +8.5% |
| Draw probability edge | +3.5% |
| Away probability edge | -12.0% |
| Over 2.5 probability edge | -15.0% |
| Under 2.5 probability edge | +15.0% |
| Raw edge prob home | 0.1692 |
| Raw ev home | 0.8164 |
| Raw edge prob draw | 0.0700 |
| Raw ev draw | 0.2640 |
| Raw edge prob away | -0.2392 |
| Raw ev away | -0.4520 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **43.3%**. Expected goals are 1.64 for Liverpool and 1.48 for Brighton and Hove Albion (3.12 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.4%; Under 3.5 goals: 62.0%; Double Chance 1X: 68.6%; Double Chance X2: 56.7%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 43.3% | 2.31 |
| Draw | 25.3% | 3.95 |
| Brighton and Hove Albion win | 31.4% | 3.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.64 |
| Brighton and Hove Albion expected goals | 1.48 |
| Expected total goals | 3.12 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 60.4% |
| Under 2.5 | 39.6% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.54% |
| 2 | 2-1 | 9.38% |
| 3 | 1-2 | 7.38% |
| 4 | 1-0 | 6.71% |
| 5 | 2-2 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 43.3% | 46.1% | 2.11 | -8.6% |
| Draw | 25.3% | 24.9% | 4.00 | +1.2% |
| Brighton and Hove Albion win | 31.4% | 29.0% | 3.43 | +7.7% |

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
| Dc lambda home | 1.6362 |
| Dc lambda away | 1.4807 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.78 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.81 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.53 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 40.5% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 33.8% |
| Raw p over 1 5 | 82.7% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 63.2% |
| P home draw | 68.6% |
| P draw away | 56.7% |
| P home away | 74.7% |
| Raw p home draw | 66.2% |
| Raw p draw away | 59.5% |
| Raw p home away | 74.4% |
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
| Home probability edge | -2.8% |
| Draw probability edge | +0.4% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.0555 |
| Raw ev home | -0.1447 |
| Raw edge prob draw | 0.0071 |
| Raw ev draw | 0.0257 |
| Raw edge prob away | 0.0484 |
| Raw ev away | 0.1600 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **50.7%**. Expected goals are 1.76 for Manchester United and 1.27 for Bournemouth (3.03 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 59.0%; Under 3.5 goals: 63.7%; Double Chance 1X: 74.8%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 50.7% | 1.97 |
| Draw | 24.1% | 4.15 |
| Bournemouth win | 25.2% | 3.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.76 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.03 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 59.0% |
| Under 2.5 | 41.0% |
| Over 3.5 | 36.3% |
| Under 3.5 | 63.7% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.18% |
| 2 | 2-1 | 10.04% |
| 3 | 1-0 | 7.93% |
| 4 | 2-0 | 7.89% |
| 5 | 1-2 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 50.7% | 53.4% | 1.90 | -3.7% |
| Draw | 24.1% | 22.8% | 4.11 | -1.0% |
| Bournemouth win | 25.2% | 23.7% | 4.07 | +2.7% |

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
| Dc lambda home | 1.7619 |
| Dc lambda away | 1.2729 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.19 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.47 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.18 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 47.9% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 60.6% |
| P home draw | 74.8% |
| P draw away | 49.3% |
| P home away | 75.9% |
| Raw p home draw | 73.3% |
| Raw p draw away | 52.1% |
| Raw p home away | 74.7% |
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
| Home probability edge | -2.7% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.0549 |
| Raw ev home | -0.0892 |
| Raw edge prob draw | 0.0249 |
| Raw ev draw | 0.0409 |
| Raw edge prob away | 0.0300 |
| Raw ev away | 0.0882 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **37.5%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.28 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 40.3%; Under 3.5 goals: 80.3%; Double Chance 1X: 62.5%; Double Chance X2: 67.1%; Double Chance 12 (either team wins): 70.4%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 32.9% | 3.04 |
| Draw | 29.6% | 3.38 |
| Leeds United win | 37.5% | 2.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.07 |
| Leeds United expected goals | 1.21 |
| Expected total goals | 2.28 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 67.7% |
| Under 1.5 | 32.3% |
| Over 2.5 | 40.3% |
| Under 2.5 | 59.7% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.85% |
| 2 | 0-1 | 11.02% |
| 3 | 0-0 | 10.97% |
| 4 | 1-0 | 10.32% |
| 5 | 1-2 | 7.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 32.9% | 34.8% | 2.90 | -4.6% |
| Draw | 29.6% | 28.3% | 3.44 | +1.7% |
| Leeds United win | 37.5% | 36.9% | 2.63 | -1.3% |
| Over 2.5 | 40.3% | 45.2% | 2.14 | -13.8% |
| Under 2.5 | 59.7% | 54.8% | 1.83 | +9.3% |

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
| Dc lambda home | 1.0667 |
| Dc lambda away | 1.2125 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:18:42.147910+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.12 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.15 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 31.0% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 38.2% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 47.3% |
| P home draw | 62.5% |
| P draw away | 67.1% |
| P home away | 70.4% |
| Raw p home draw | 61.8% |
| Raw p draw away | 69.0% |
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
| Home probability edge | -1.9% |
| Draw probability edge | +1.3% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0381 |
| Raw ev home | -0.1016 |
| Raw edge prob draw | 0.0250 |
| Raw ev draw | 0.0602 |
| Raw edge prob away | 0.0131 |
| Raw ev away | 0.0047 |

</details>


---
