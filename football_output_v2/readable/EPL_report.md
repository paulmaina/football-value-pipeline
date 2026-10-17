# Premier League — football model report

Fixtures in this report: **20**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,200 |
| Training data through | 2026-10-12 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | 67c2b5120557f98b4491388e7c3cb89191eab0d6b1d812c3a818da0866e50d69 |
| Training as of utc | 2026-10-17T09:44:28.853796+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 60, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 60, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-17T09:44:28.853796+00:00', 'observations': 60, 'observations_sha256': '53fcc3832a13992f7df51f698cb3b070d56fc9b16dd7f449ea0cb761d5026d68', 'eligible_training_matches': 11, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 43, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 11, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'b1360fe2c6b9cd4ecb68e44377aaf5fbd5c0e68000550a78cc571d4ff2f1029c', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 883.722 |
| Base scoring parameter | 0.217 |
| Home-advantage parameter | 0.179 |
| Dixon-Coles low-score adjustment | -0.115 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261017T094428853796Z_f487e1975fbe412c2151525a31bb2faa7b79c9216d3345ec5057bb2e62ecf11d.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 10.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 10.00 |
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

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Brentford win** at **39.2%**. Expected goals are 1.58 for Brentford and 1.48 for Liverpool (3.06 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 58.9%; Under 3.5 goals: 63.4%; Double Chance 1X: 65.9%; Double Chance X2: 60.8%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 80.5%; BTTS Yes (both teams score): 62.6%; BTTS No (at least one team does not score): 37.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 39.2% | 2.55 |
| Draw | 26.7% | 3.75 |
| Liverpool win | 34.1% | 2.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.58 |
| Liverpool expected goals | 1.48 |
| Expected total goals | 3.06 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 82.2% |
| Under 1.5 | 17.8% |
| Over 2.5 | 58.9% |
| Under 2.5 | 41.1% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.5% |
| Under 4.5 | 80.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.31% |
| 2 | 2-1 | 8.72% |
| 3 | 1-2 | 8.02% |
| 4 | 2-2 | 6.45% |
| 5 | 1-0 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 39.2% | 39.4% | 2.51 | -1.7% |
| Draw | 26.7% | 26.9% | 3.73 | -0.4% |
| Liverpool win | 34.1% | 33.7% | 2.86 | -2.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | 8f1945e7272bc7e89016439f5ab321c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Brentford |
| Matched away-team name | Liverpool |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5808 |
| Dc lambda away | 1.4787 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.6% |
| P btts no | 37.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.68 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.62 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.14 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 34.5% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 62.6% |
| P home draw | 65.9% |
| P draw away | 60.8% |
| P home away | 73.3% |
| Raw p home draw | 65.5% |
| Raw p draw away | 61.0% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.38 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.75 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Home probability edge | -0.2% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.0044 |
| Raw ev home | -0.0221 |
| Raw edge prob draw | -0.0033 |
| Raw ev draw | -0.0105 |
| Raw edge prob away | 0.0078 |
| Raw ev away | -0.0129 |
| Market p home draw | 67.4% |
| Market home draw odds | 1.48 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:33Z |
| Market reference home draw last update utc | 2026-10-17T09:08:57Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.1% |
| Market draw away odds | 1.59 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:33Z |
| Market reference draw away last update utc | 2026-10-17T09:08:57Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.32 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:33Z |
| Market reference home away last update utc | 2026-10-17T09:08:57Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.57 |
| Market reference dc home draw odds | 1.40 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:08:52Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-17T09:08:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.5% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:08:52Z |
| Market reference under 3 5 odds | 1.64 |
| Market reference under 3 5 opposite odds | 2.37 |
| Market reference under 3 5 last update utc | 2026-10-17T09:08:56Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.8% |
| Market btts yes odds | 1.46 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:33Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-17T09:08:57Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **38.6%**. Expected goals are 1.40 for Everton and 1.37 for Chelsea (2.76 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 52.6%; Under 3.5 goals: 70.0%; Double Chance 1X: 61.4%; Double Chance X2: 65.7%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 34.3% | 2.92 |
| Draw | 27.2% | 3.68 |
| Chelsea win | 38.6% | 2.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.40 |
| Chelsea expected goals | 1.37 |
| Expected total goals | 2.76 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.0% |
| Under 3.5 | 70.0% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.92% |
| 2 | 1-2 | 9.02% |
| 3 | 0-1 | 7.93% |
| 4 | 2-1 | 7.88% |
| 5 | 0-0 | 7.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 34.3% | 31.9% | 3.07 | +5.2% |
| Draw | 27.2% | 26.1% | 3.84 | +4.4% |
| Chelsea win | 38.6% | 41.9% | 2.33 | -10.2% |
| Over 2.5 | 52.6% | 60.5% | 1.68 | -11.7% |
| Under 2.5 | 47.4% | 39.5% | 2.38 | +12.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T11:30:00+00:00 |
| Fixture id | 764e6513cb3f348881503df70ccb90e0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Everton |
| Matched away-team name | Chelsea |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3966 |
| Dc lambda away | 1.3665 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.50 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.75 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 36.6% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 70.0% |
| Raw p btts yes | 57.5% |
| P home draw | 61.4% |
| P draw away | 65.7% |
| P home away | 72.8% |
| Raw p home draw | 64.8% |
| Raw p draw away | 63.4% |
| Raw p home away | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.90 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | +2.3% |
| Draw probability edge | +1.1% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -7.9% |
| Under 2.5 probability edge | +7.9% |
| Raw edge prob home | 0.0461 |
| Raw ev home | 0.1224 |
| Raw edge prob draw | 0.0213 |
| Raw ev draw | 0.0848 |
| Raw edge prob away | -0.0675 |
| Raw ev away | -0.1801 |
| Market p home draw | 56.8% |
| Market home draw odds | 1.68 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:33Z |
| Market reference home draw last update utc | 2026-10-17T09:08:57Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.7% |
| Market draw away odds | 1.43 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:33Z |
| Market reference draw away last update utc | 2026-10-17T09:08:57Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.5% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:33Z |
| Market reference home away last update utc | 2026-10-17T09:08:57Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home draw odds | 1.67 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 82.9% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:08:52Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market reference over 1 5 last update utc | 2026-10-17T09:08:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.1% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:08:52Z |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.58 |
| Market reference under 3 5 last update utc | 2026-10-17T09:08:56Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.8% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:33Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-17T09:08:57Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.5%**. Expected goals are 0.94 for Fulham and 1.22 for Hull City (2.16 combined). The most likely exact score is 1-0 at 14.7%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 37.8%; Under 3.5 goals: 82.9%; Double Chance 1X: 70.4%; Double Chance X2: 57.5%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 93.0%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.5% | 2.35 |
| Draw | 27.8% | 3.59 |
| Hull City win | 29.6% | 3.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.94 |
| Hull City expected goals | 1.22 |
| Expected total goals | 2.16 |
| Over 0.5 | 88.7% |
| Under 0.5 | 11.3% |
| Over 1.5 | 64.9% |
| Under 1.5 | 35.1% |
| Over 2.5 | 37.8% |
| Under 2.5 | 62.2% |
| Over 3.5 | 17.1% |
| Under 3.5 | 82.9% |
| Over 4.5 | 7.0% |
| Under 4.5 | 93.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.73% |
| 2 | 1-1 | 12.79% |
| 3 | 0-0 | 11.31% |
| 4 | 2-1 | 9.84% |
| 5 | 0-1 | 9.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 42.5% | 58.1% | 1.71 | -27.2% |
| Draw | 27.8% | 23.6% | 4.16 | +15.8% |
| Hull City win | 29.6% | 18.3% | 5.24 | +55.2% |
| Over 2.5 | 37.8% | 54.7% | 1.81 | -31.5% |
| Under 2.5 | 62.2% | 45.3% | 2.15 | +33.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | 7895f97f2f9577f3b13287a3d086859d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fulham |
| Matched away-team name | Hull |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9420 |
| Dc lambda away | 1.2186 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.9% |
| P btts no | 56.1% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.84 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.85 |
| Fair Over 2.5 odds | 2.64 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.84 |
| Fair Under 3.5 odds | 1.21 |
| Fair Over 4.5 odds | 14.27 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 32.1% |
| Unadjusted away-win probability | 40.9% |
| Raw p over 1 5 | 65.1% |
| Raw p under 3 5 | 82.7% |
| Raw p btts yes | 44.5% |
| P home draw | 70.4% |
| P draw away | 57.5% |
| P home away | 72.2% |
| Raw p home draw | 59.1% |
| Raw p draw away | 73.1% |
| Raw p home away | 67.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.65 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.80 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | -15.6% |
| Draw probability edge | +4.3% |
| Away probability edge | +11.3% |
| Over 2.5 probability edge | -16.8% |
| Under 2.5 probability edge | +16.8% |
| Raw edge prob home | -0.3120 |
| Raw ev home | -0.5392 |
| Raw edge prob draw | 0.0857 |
| Raw ev draw | 0.3365 |
| Raw edge prob away | 0.2263 |
| Raw ev away | 1.1445 |
| Market p home draw | 80.2% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:33Z |
| Market reference home draw last update utc | 2026-10-17T09:08:57Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.0% |
| Market draw away odds | 2.27 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:33Z |
| Market reference draw away last update utc | 2026-10-17T09:08:57Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.7% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:33Z |
| Market reference home away last update utc | 2026-10-17T09:08:57Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.15 |
| Market reference dc home draw odds | 1.18 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 79.6% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:08:08Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-17T09:08:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.9% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:08:08Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.92 |
| Market reference under 3 5 last update utc | 2026-10-17T09:08:56Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.8% |
| Market btts yes odds | 1.73 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:33Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-17T09:08:57Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **82.4%**. Expected goals are 3.47 for Manchester City and 0.73 for Ipswich Town (4.20 combined). The most likely exact score is 3-0 at 9.9%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 77.6%; Under 3.5 goals: 40.9%; Double Chance 1X: 94.0%; Double Chance X2: 17.6%; Double Chance 12 (either team wins): 88.5%; Under 4.5 goals: 60.3%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 82.4% | 1.21 |
| Draw | 11.5% | 8.67 |
| Ipswich Town win | 6.0% | 16.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.47 |
| Ipswich Town expected goals | 0.73 |
| Expected total goals | 4.20 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 77.6% |
| Under 2.5 | 22.4% |
| Over 3.5 | 59.1% |
| Under 3.5 | 40.9% |
| Over 4.5 | 39.7% |
| Under 4.5 | 60.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 9.95% |
| 2 | 4-0 | 8.63% |
| 3 | 2-0 | 8.60% |
| 4 | 3-1 | 7.23% |
| 5 | 4-1 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 82.4% | 78.1% | 1.28 | +5.5% |
| Draw | 11.5% | 13.7% | 7.21 | -16.9% |
| Ipswich Town win | 6.0% | 8.2% | 10.40 | -37.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | bf2142d1ca76ba2fc9e61afce80f86c0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man City |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.4694 |
| Dc lambda away | 0.7267 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.76 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.54 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.46 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.44 |
| Fair Over 4.5 odds | 2.52 |
| Fair Under 4.5 odds | 1.66 |
| Unadjusted home-win probability | 86.8% |
| Unadjusted draw probability | 9.4% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 92.6% |
| Raw p under 3 5 | 39.6% |
| Raw p btts yes | 50.5% |
| P home draw | 94.0% |
| P draw away | 17.6% |
| P home away | 88.5% |
| Raw p home draw | 96.2% |
| Raw p draw away | 13.2% |
| Raw p home away | 90.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.25 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.50 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Home probability edge | +4.4% |
| Draw probability edge | -2.2% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +3.5% |
| Under 2.5 probability edge | -3.5% |
| Raw edge prob home | 0.0876 |
| Raw ev home | 0.1114 |
| Raw edge prob draw | -0.0434 |
| Raw ev draw | -0.3254 |
| Raw edge prob away | -0.0441 |
| Raw ev away | -0.6031 |
| Market p home draw | 91.2% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:33Z |
| Market reference home draw last update utc | 2026-10-17T09:09:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 21.7% |
| Market draw away odds | 4.08 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:33Z |
| Market reference draw away last update utc | 2026-10-17T09:09:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.1% |
| Market home away odds | 1.13 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:33Z |
| Market reference home away last update utc | 2026-10-17T09:09:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.50 |
| Market reference dc home draw odds | 1.07 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 91.2% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:08:34Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 7.50 |
| Market reference over 1 5 last update utc | 2026-10-17T09:08:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 47.1% |
| Market under 3 5 odds | 2.10 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:08:34Z |
| Market reference under 3 5 odds | 2.06 |
| Market reference under 3 5 opposite odds | 1.84 |
| Market reference under 3 5 last update utc | 2026-10-17T09:08:56Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:33Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.21 |
| Market reference btts yes last update utc | 2026-10-17T09:09:05Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **42.5%**. Expected goals are 1.76 for Newcastle United and 1.53 for Aston Villa (3.28 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.4%; Double Chance 1X: 68.0%; Double Chance X2: 57.5%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 66.0%; BTTS No (at least one team does not score): 34.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 42.5% | 2.36 |
| Draw | 25.5% | 3.92 |
| Aston Villa win | 32.0% | 3.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.76 |
| Aston Villa expected goals | 1.53 |
| Expected total goals | 3.28 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 63.6% |
| Under 2.5 | 36.4% |
| Over 3.5 | 41.6% |
| Under 3.5 | 58.4% |
| Over 4.5 | 23.4% |
| Under 4.5 | 76.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.34% |
| 2 | 2-1 | 8.87% |
| 3 | 1-2 | 7.57% |
| 4 | 2-2 | 6.81% |
| 5 | 2-0 | 5.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 42.5% | 42.6% | 2.26 | -4.1% |
| Draw | 25.5% | 25.8% | 3.85 | -1.8% |
| Aston Villa win | 32.0% | 31.6% | 3.19 | +2.2% |
| Over 2.5 | 63.6% | 61.6% | 1.67 | +6.3% |
| Under 2.5 | 36.4% | 38.4% | 2.40 | -12.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | d1bbbdcd3d430e70091b518369b559cf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Newcastle |
| Matched away-team name | Aston Villa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7583 |
| Dc lambda away | 1.5250 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 66.0% |
| P btts no | 34.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.15 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.70 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.40 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.28 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 32.5% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 58.4% |
| Raw p btts yes | 65.9% |
| P home draw | 68.0% |
| P draw away | 57.5% |
| P home away | 74.5% |
| Raw p home draw | 67.5% |
| Raw p draw away | 57.7% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.20 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | -0.2% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | -0.0032 |
| Raw ev home | -0.0443 |
| Raw edge prob draw | -0.0053 |
| Raw ev draw | -0.0277 |
| Raw edge prob away | 0.0086 |
| Raw ev away | 0.0354 |
| Market p home draw | 69.7% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:33Z |
| Market reference home draw last update utc | 2026-10-17T09:08:57Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.8% |
| Market draw away odds | 1.71 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:33Z |
| Market reference draw away last update utc | 2026-10-17T09:08:57Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.5% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:33Z |
| Market reference home away last update utc | 2026-10-17T09:08:57Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home draw odds | 1.36 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.8% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:08:53Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-17T09:08:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.6% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:08:53Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.43 |
| Market reference under 3 5 last update utc | 2026-10-17T09:08:56Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.8% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:33Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-17T09:08:57Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.1%**. Expected goals are 1.59 for Bournemouth and 1.06 for Sunderland (2.65 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 49.4%; Under 3.5 goals: 72.6%; Double Chance 1X: 74.8%; Double Chance X2: 52.9%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 53.4%; BTTS No (at least one team does not score): 46.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.1% | 2.12 |
| Draw | 27.6% | 3.62 |
| Sunderland win | 25.2% | 3.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.59 |
| Sunderland expected goals | 1.06 |
| Expected total goals | 2.65 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 49.4% |
| Under 2.5 | 50.6% |
| Over 3.5 | 27.4% |
| Under 3.5 | 72.6% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.20% |
| 2 | 1-0 | 9.64% |
| 3 | 2-1 | 9.24% |
| 4 | 2-0 | 8.73% |
| 5 | 0-0 | 8.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.1% | 46.0% | 2.15 | +1.4% |
| Draw | 27.6% | 27.5% | 3.63 | +0.3% |
| Sunderland win | 25.2% | 26.6% | 3.63 | -8.4% |
| Over 2.5 | 49.4% | 53.1% | 1.96 | -3.2% |
| Under 2.5 | 50.6% | 46.9% | 1.98 | +0.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | dfd5d6648be46426e418801584d46a68 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bournemouth |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5903 |
| Dc lambda away | 1.0581 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.4% |
| P btts no | 46.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.90 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.65 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.73 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 53.4% |
| P home draw | 74.8% |
| P draw away | 52.9% |
| P home away | 72.4% |
| Raw p home draw | 76.1% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.05 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.40 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | +1.2% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | 0.0236 |
| Raw ev home | 0.0391 |
| Raw edge prob draw | 0.0033 |
| Raw ev draw | 0.0085 |
| Raw edge prob away | -0.0269 |
| Raw ev away | -0.1329 |
| Market p home draw | 72.6% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:33Z |
| Market reference home draw last update utc | 2026-10-17T09:09:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.8% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:33Z |
| Market reference draw away last update utc | 2026-10-17T09:09:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:33Z |
| Market reference home away last update utc | 2026-10-17T09:09:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.76 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 77.8% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market reference over 1 5 last update utc | 2026-10-17T09:08:57Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 71.5% |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.24 |
| Market reference under 3 5 last update utc | 2026-10-17T09:08:56Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 55.2% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:33Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.13 |
| Market reference btts yes last update utc | 2026-10-17T09:09:04Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **60.9%**. Expected goals are 2.00 for Brighton and Hove Albion and 1.02 for Crystal Palace (3.02 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 58.9%; Under 3.5 goals: 64.0%; Double Chance 1X: 82.7%; Double Chance X2: 39.1%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 56.0%; BTTS No (at least one team does not score): 44.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 60.9% | 1.64 |
| Draw | 21.8% | 4.59 |
| Crystal Palace win | 17.3% | 5.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 2.00 |
| Crystal Palace expected goals | 1.02 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 58.9% |
| Under 2.5 | 41.1% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.29% |
| 2 | 2-1 | 10.27% |
| 3 | 2-0 | 10.07% |
| 4 | 1-0 | 8.88% |
| 5 | 3-1 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 60.9% | 62.8% | 1.58 | -3.8% |
| Draw | 21.8% | 20.1% | 4.72 | +2.9% |
| Crystal Palace win | 17.3% | 17.2% | 5.80 | +0.5% |
| Over 2.5 | 58.9% | 61.6% | 1.63 | -4.0% |
| Under 2.5 | 41.1% | 38.4% | 2.49 | +2.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 9fc08b390a49c4434f7cf631a0bb88fb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0018 |
| Dc lambda away | 1.0201 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 56.0% |
| P btts no | 44.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.92 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.48 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.22 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 59.0% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 17.5% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 56.5% |
| P home draw | 82.7% |
| P draw away | 39.1% |
| P home away | 78.2% |
| Raw p home draw | 82.5% |
| Raw p draw away | 41.0% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.53 |
| Reference draw odds | 4.33 |
| Reference away odds | 5.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | -1.9% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | -0.0378 |
| Raw ev home | -0.0681 |
| Raw edge prob draw | 0.0342 |
| Raw ev draw | 0.1094 |
| Raw edge prob away | 0.0036 |
| Raw ev away | 0.0159 |
| Market p home draw | 83.7% |
| Market home draw odds | 1.17 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:33Z |
| Market reference home draw last update utc | 2026-10-17T09:09:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.8% |
| Market draw away odds | 2.54 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:33Z |
| Market reference draw away last update utc | 2026-10-17T09:09:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.6% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:33Z |
| Market reference home away last update utc | 2026-10-17T09:09:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.64 |
| Market reference dc home draw odds | 1.16 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-17T09:08:57Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.5% |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.41 |
| Market reference under 3 5 last update utc | 2026-10-17T09:08:56Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:33Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.26 |
| Market reference btts yes last update utc | 2026-10-17T09:09:05Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **39.7%**. Expected goals are 1.42 for Leeds United and 1.28 for Manchester United (2.70 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.4%; Double Chance 1X: 67.3%; Double Chance X2: 60.3%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 39.7% | 2.52 |
| Draw | 27.6% | 3.62 |
| Manchester United win | 32.7% | 3.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.28 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 76.6% |
| Under 1.5 | 23.4% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 28.6% |
| Under 3.5 | 71.4% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.16% |
| 2 | 2-1 | 8.86% |
| 3 | 1-0 | 8.32% |
| 4 | 0-0 | 7.86% |
| 5 | 1-2 | 7.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 39.7% | 40.6% | 2.42 | -4.0% |
| Draw | 27.6% | 26.6% | 3.69 | +1.8% |
| Manchester United win | 32.7% | 32.8% | 3.01 | -1.5% |
| Over 2.5 | 51.0% | 58.4% | 1.71 | -12.9% |
| Under 2.5 | 49.0% | 41.6% | 2.32 | +13.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 676b3b0b609e9cf565da450786618d26 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4152 |
| Dc lambda away | 1.2823 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.72 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.27 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.24 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 76.5% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 56.1% |
| P home draw | 67.3% |
| P draw away | 60.3% |
| P home away | 72.4% |
| Raw p home draw | 67.4% |
| Raw p draw away | 61.2% |
| Raw p home away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.30 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | -0.9% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | -0.0183 |
| Raw ev home | -0.0618 |
| Raw edge prob draw | 0.0200 |
| Raw ev draw | 0.0549 |
| Raw edge prob away | -0.0017 |
| Raw ev away | -0.0174 |
| Market p home draw | 68.1% |
| Market home draw odds | 1.44 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:33Z |
| Market reference home draw last update utc | 2026-10-17T09:09:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.3% |
| Market draw away odds | 1.63 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:33Z |
| Market reference draw away last update utc | 2026-10-17T09:09:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.7% |
| Market home away odds | 1.32 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:33Z |
| Market reference home away last update utc | 2026-10-17T09:09:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.63 |
| Market reference dc home draw odds | 1.42 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 82.5% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:08:08Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-17T09:08:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.5% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:08:08Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.72 |
| Market reference under 3 5 last update utc | 2026-10-17T09:08:56Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.9% |
| Market btts yes odds | 1.52 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:33Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.48 |
| Market reference btts yes last update utc | 2026-10-17T09:09:04Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **56.8%**. Expected goals are 0.76 for Nottingham Forest and 1.53 for Arsenal (2.29 combined). The most likely exact score is 0-1 at 14.8%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 41.0%; Under 3.5 goals: 79.8%; Double Chance 1X: 43.2%; Double Chance X2: 83.4%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 42.6%; BTTS No (at least one team does not score): 57.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.6% | 6.01 |
| Draw | 26.5% | 3.77 |
| Arsenal win | 56.8% | 1.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.76 |
| Arsenal expected goals | 1.53 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 68.4% |
| Under 1.5 | 31.6% |
| Over 2.5 | 41.0% |
| Under 2.5 | 59.0% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.79% |
| 2 | 0-2 | 12.39% |
| 3 | 1-1 | 12.22% |
| 4 | 0-0 | 10.65% |
| 5 | 1-2 | 9.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.6% | 16.0% | 5.78 | -3.8% |
| Draw | 26.5% | 24.5% | 3.90 | +3.4% |
| Arsenal win | 56.8% | 59.5% | 1.71 | -2.8% |
| Over 2.5 | 41.0% | 50.0% | 1.99 | -18.4% |
| Under 2.5 | 59.0% | 50.0% | 1.95 | +15.0% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
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
| Dc lambda home | 0.7633 |
| Dc lambda away | 1.5287 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 42.6% |
| P btts no | 57.4% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.39 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.96 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.76 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 54.2% |
| Raw p over 1 5 | 68.1% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 43.2% |
| P home draw | 43.2% |
| P draw away | 83.4% |
| P home away | 73.5% |
| Raw p home draw | 45.8% |
| Raw p draw away | 82.7% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 5.50 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.62 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | +0.7% |
| Draw probability edge | +2.0% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | 0.0131 |
| Raw ev home | -0.0004 |
| Raw edge prob draw | 0.0405 |
| Raw ev draw | 0.1131 |
| Raw edge prob away | -0.0536 |
| Raw ev away | -0.0738 |
| Market p home draw | 41.2% |
| Market home draw odds | 2.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:33Z |
| Market reference home draw last update utc | 2026-10-17T09:09:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.2% |
| Market draw away odds | 1.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:33Z |
| Market reference draw away last update utc | 2026-10-17T09:09:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.5% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:33Z |
| Market reference home away last update utc | 2026-10-17T09:09:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.15 |
| Market reference dc home draw odds | 2.35 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 75.3% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:08:52Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market reference over 1 5 last update utc | 2026-10-17T09:08:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.0% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:08:52Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.28 |
| Market reference under 3 5 last update utc | 2026-10-17T09:08:56Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 51.0% |
| Market btts yes odds | 1.87 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:33Z |
| Market reference btts yes odds | 1.89 |
| Market reference btts yes opposite odds | 1.96 |
| Market reference btts yes last update utc | 2026-10-17T09:09:04Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **54.9%**. Expected goals are 1.43 for Tottenham Hotspur and 1.06 for Coventry City (2.49 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 47.1%; Under 3.5 goals: 75.4%; Double Chance 1X: 79.9%; Double Chance X2: 45.1%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 54.9% | 1.82 |
| Draw | 25.0% | 3.99 |
| Coventry City win | 20.1% | 4.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.43 |
| Coventry City expected goals | 1.06 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 73.1% |
| Under 1.5 | 26.9% |
| Over 2.5 | 47.1% |
| Under 2.5 | 52.9% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 11.3% |
| Under 4.5 | 88.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.99% |
| 2 | 1-1 | 11.93% |
| 3 | 2-1 | 11.17% |
| 4 | 2-0 | 10.57% |
| 5 | 0-0 | 8.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 54.9% | 65.6% | 1.54 | -15.5% |
| Draw | 25.0% | 20.6% | 4.72 | +18.2% |
| Coventry City win | 20.1% | 13.7% | 6.47 | +30.1% |
| Over 2.5 | 47.1% | 60.5% | 1.64 | -22.8% |
| Under 2.5 | 52.9% | 39.5% | 2.46 | +30.2% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
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
| Dc lambda home | 1.4285 |
| Dc lambda away | 1.0577 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.03 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.72 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 4.07 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.84 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 44.1% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 26.5% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 76.1% |
| Raw p btts yes | 51.1% |
| P home draw | 79.9% |
| P draw away | 45.1% |
| P home away | 75.0% |
| Raw p home draw | 73.5% |
| Raw p draw away | 55.9% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.52 |
| Reference draw odds | 4.80 |
| Reference away odds | 7.20 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | -10.8% |
| Draw probability edge | +4.4% |
| Away probability edge | +6.4% |
| Over 2.5 probability edge | -13.4% |
| Under 2.5 probability edge | +13.4% |
| Raw edge prob home | -0.2154 |
| Raw ev home | -0.3210 |
| Raw edge prob draw | 0.0878 |
| Raw ev draw | 0.3890 |
| Raw edge prob away | 0.1275 |
| Raw ev away | 0.7133 |
| Market p home draw | 85.0% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:08:33Z |
| Market reference home draw last update utc | 2026-10-17T09:09:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.9% |
| Market draw away odds | 2.65 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:08:33Z |
| Market reference draw away last update utc | 2026-10-17T09:09:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.1% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:08:33Z |
| Market reference home away last update utc | 2026-10-17T09:09:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.78 |
| Market reference dc home draw odds | 1.14 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-17T09:08:57Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.6% |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.47 |
| Market reference under 3 5 last update utc | 2026-10-17T09:08:56Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 55.6% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:08:33Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.15 |
| Market reference btts yes last update utc | 2026-10-17T09:09:05Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **46.1%**. Expected goals are 1.22 for Ipswich Town and 1.76 for Nottingham Forest (2.98 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 57.0%; Under 3.5 goals: 65.3%; Double Chance 1X: 53.9%; Double Chance X2: 72.6%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 27.4% | 3.65 |
| Draw | 26.5% | 3.77 |
| Nottingham Forest win | 46.1% | 2.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.22 |
| Nottingham Forest expected goals | 1.76 |
| Expected total goals | 2.98 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 57.0% |
| Under 2.5 | 43.0% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.43% |
| 2 | 1-2 | 9.04% |
| 3 | 0-2 | 7.43% |
| 4 | 0-1 | 7.24% |
| 5 | 2-1 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 27.4% | 29.7% | 3.10 | -15.1% |
| Draw | 26.5% | 27.1% | 3.63 | -3.7% |
| Nottingham Forest win | 46.1% | 43.2% | 2.39 | +10.1% |
| Over 2.5 | 57.0% | 52.2% | 1.84 | +4.8% |
| Under 2.5 | 43.0% | 47.8% | 2.12 | -8.7% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2170 |
| Dc lambda away | 1.7641 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.43 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.56 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 25.1% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 49.0% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 65.1% |
| Raw p btts yes | 59.6% |
| P home draw | 53.9% |
| P draw away | 72.6% |
| P home away | 73.5% |
| Raw p home draw | 51.0% |
| Raw p draw away | 74.9% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.30 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.28 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | -2.3% |
| Draw probability edge | -0.6% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | +4.7% |
| Under 2.5 probability edge | -4.7% |
| Raw edge prob home | -0.0454 |
| Raw ev home | -0.2216 |
| Raw edge prob draw | -0.0121 |
| Raw ev draw | -0.0589 |
| Raw edge prob away | 0.0576 |
| Raw ev away | 0.1702 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **65.7%**. Expected goals are 1.67 for Arsenal and 0.61 for Everton (2.28 combined). The most likely exact score is 1-0 at 16.9%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.9%; Double Chance 1X: 88.5%; Double Chance X2: 34.3%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 37.3%; BTTS No (at least one team does not score): 62.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 65.7% | 1.52 |
| Draw | 22.7% | 4.40 |
| Everton win | 11.5% | 8.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.67 |
| Everton expected goals | 0.61 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 68.3% |
| Under 1.5 | 31.7% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.1% |
| Under 3.5 | 79.9% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.86% |
| 2 | 2-0 | 15.16% |
| 3 | 1-1 | 10.13% |
| 4 | 0-0 | 10.01% |
| 5 | 2-1 | 9.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 65.7% | 69.4% | 1.43 | -6.0% |
| Draw | 22.7% | 19.5% | 4.93 | +12.0% |
| Everton win | 11.5% | 11.2% | 8.90 | +2.7% |
| Over 2.5 | 41.2% | 53.7% | 1.83 | -24.7% |
| Under 2.5 | 58.8% | 46.3% | 2.14 | +25.9% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6724 |
| Dc lambda away | 0.6060 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 37.3% |
| P btts no | 62.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.99 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.15 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.98 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.81 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 62.1% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 11.9% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 38.1% |
| P home draw | 88.5% |
| P draw away | 34.3% |
| P home away | 77.3% |
| Raw p home draw | 88.1% |
| Raw p draw away | 37.9% |
| Raw p home away | 74.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.40 |
| Reference draw odds | 4.50 |
| Reference away odds | 7.50 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | -3.6% |
| Draw probability edge | +3.2% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -12.5% |
| Under 2.5 probability edge | +12.5% |
| Raw edge prob home | -0.0722 |
| Raw ev home | -0.1116 |
| Raw edge prob draw | 0.0649 |
| Raw ev draw | 0.2803 |
| Raw edge prob away | 0.0073 |
| Raw ev away | 0.0593 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **55.9%**. Expected goals are 1.09 for Aston Villa and 1.92 for Manchester City (3.00 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 58.1%; Under 3.5 goals: 64.6%; Double Chance 1X: 44.1%; Double Chance X2: 79.7%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 81.3%; BTTS Yes (both teams score): 57.6%; BTTS No (at least one team does not score): 42.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 20.3% | 4.92 |
| Draw | 23.8% | 4.21 |
| Manchester City win | 55.9% | 1.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.09 |
| Manchester City expected goals | 1.92 |
| Expected total goals | 3.00 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 58.1% |
| Under 2.5 | 41.9% |
| Over 3.5 | 35.4% |
| Under 3.5 | 64.6% |
| Over 4.5 | 18.7% |
| Under 4.5 | 81.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.18% |
| 2 | 1-2 | 9.99% |
| 3 | 0-2 | 9.18% |
| 4 | 0-1 | 8.37% |
| 5 | 1-3 | 6.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 20.3% | 20.6% | 4.72 | -4.2% |
| Draw | 23.8% | 23.0% | 4.26 | +1.2% |
| Manchester City win | 55.9% | 56.4% | 1.76 | -1.6% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0885 |
| Dc lambda away | 1.9160 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.6% |
| P btts no | 42.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.76 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.38 |
| Fair Over 2.5 odds | 1.72 |
| Fair Under 2.5 odds | 2.38 |
| Fair Over 3.5 odds | 2.82 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.36 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 20.0% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 55.5% |
| Raw p over 1 5 | 81.3% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 57.8% |
| P home draw | 44.1% |
| P draw away | 79.7% |
| P home away | 76.2% |
| Raw p home draw | 44.5% |
| Raw p draw away | 80.0% |
| Raw p home away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 4.33 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | -0.0052 |
| Raw ev home | -0.0540 |
| Raw edge prob draw | 0.0147 |
| Raw ev draw | 0.0435 |
| Raw edge prob away | -0.0094 |
| Raw ev away | -0.0239 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **56.0%**. Expected goals are 2.11 for Chelsea and 1.17 for Tottenham Hotspur (3.28 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 63.4%; Under 3.5 goals: 58.7%; Double Chance 1X: 79.3%; Double Chance X2: 44.0%; Double Chance 12 (either team wins): 76.8%; Under 4.5 goals: 76.8%; BTTS Yes (both teams score): 61.9%; BTTS No (at least one team does not score): 38.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 56.0% | 1.78 |
| Draw | 23.2% | 4.31 |
| Tottenham Hotspur win | 20.7% | 4.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.11 |
| Tottenham Hotspur expected goals | 1.17 |
| Expected total goals | 3.28 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 63.4% |
| Under 2.5 | 36.6% |
| Over 3.5 | 41.3% |
| Under 3.5 | 58.7% |
| Over 4.5 | 23.2% |
| Under 4.5 | 76.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.57% |
| 2 | 2-1 | 9.51% |
| 3 | 2-0 | 8.12% |
| 4 | 3-1 | 6.68% |
| 5 | 1-0 | 6.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 56.0% | 54.3% | 1.90 | +6.5% |
| Draw | 23.2% | 23.6% | 4.11 | -4.6% |
| Tottenham Hotspur win | 20.7% | 22.0% | 4.06 | -15.8% |
| Over 2.5 | 63.4% | 62.3% | 1.66 | +5.2% |
| Under 2.5 | 36.6% | 37.7% | 2.42 | -11.4% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 6.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1076 |
| Dc lambda away | 1.1705 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.9% |
| P btts no | 38.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.27 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.59 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.73 |
| Fair Over 3.5 odds | 2.42 |
| Fair Under 3.5 odds | 1.70 |
| Fair Over 4.5 odds | 4.31 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 57.8% |
| Unadjusted draw probability | 22.8% |
| Unadjusted away-win probability | 19.4% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 61.7% |
| P home draw | 79.3% |
| P draw away | 44.0% |
| P home away | 76.8% |
| Raw p home draw | 80.6% |
| Raw p draw away | 42.2% |
| Raw p home away | 77.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.75 |
| Reference draw odds | 3.75 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | +1.7% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | 0.0347 |
| Raw ev home | 0.0978 |
| Raw edge prob draw | -0.0086 |
| Raw ev draw | -0.0632 |
| Raw edge prob away | -0.0261 |
| Raw ev away | -0.2113 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **38.5%**. Expected goals are 1.13 for Coventry City and 1.17 for Fulham (2.30 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.7%; Double Chance 1X: 61.5%; Double Chance X2: 67.6%; Double Chance 12 (either team wins): 71.0%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 32.4% | 3.08 |
| Draw | 29.0% | 3.44 |
| Fulham win | 38.5% | 2.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.13 |
| Fulham expected goals | 1.17 |
| Expected total goals | 2.30 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 68.7% |
| Under 1.5 | 31.3% |
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.67% |
| 2 | 0-1 | 11.10% |
| 3 | 0-0 | 10.65% |
| 4 | 1-0 | 9.53% |
| 5 | 1-2 | 8.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 32.4% | 31.7% | 3.12 | +1.2% |
| Draw | 29.0% | 26.7% | 3.61 | +4.8% |
| Fulham win | 38.5% | 41.7% | 2.39 | -7.9% |
| Over 2.5 | 41.3% | 53.7% | 1.81 | -25.2% |
| Under 2.5 | 58.7% | 46.3% | 2.15 | +26.2% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1293 |
| Dc lambda away | 1.1740 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.39 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.20 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.93 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.59 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 31.4% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.9% |
| Raw p btts yes | 48.3% |
| P home draw | 61.5% |
| P draw away | 67.6% |
| P home away | 71.0% |
| Raw p home draw | 64.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 68.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.90 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | +0.8% |
| Draw probability edge | +2.4% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -12.4% |
| Under 2.5 probability edge | +12.4% |
| Raw edge prob home | 0.0153 |
| Raw ev home | 0.0358 |
| Raw edge prob draw | 0.0472 |
| Raw ev draw | 0.1333 |
| Raw edge prob away | -0.0625 |
| Raw ev away | -0.1538 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **37.3%**. Expected goals are 1.56 for Crystal Palace and 1.57 for Newcastle United (3.12 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 60.3%; Under 3.5 goals: 62.0%; Double Chance 1X: 62.7%; Double Chance X2: 63.9%; Double Chance 12 (either team wins): 73.4%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 63.8%; BTTS No (at least one team does not score): 36.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 36.1% | 2.77 |
| Draw | 26.6% | 3.76 |
| Newcastle United win | 37.3% | 2.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.56 |
| Newcastle United expected goals | 1.57 |
| Expected total goals | 3.12 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.13% |
| 2 | 1-2 | 8.45% |
| 3 | 2-1 | 8.23% |
| 4 | 2-2 | 6.64% |
| 5 | 0-0 | 5.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 36.1% | 35.6% | 2.76 | -0.2% |
| Draw | 26.6% | 26.9% | 3.69 | -1.9% |
| Newcastle United win | 37.3% | 37.5% | 2.61 | -2.7% |
| Over 2.5 | 60.3% | 57.3% | 1.69 | +1.9% |
| Under 2.5 | 39.7% | 42.7% | 2.36 | -6.3% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5576 |
| Dc lambda away | 1.5671 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 63.8% |
| P btts no | 36.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.51 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.91 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.87 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 36.7% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 37.1% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 61.9% |
| Raw p btts yes | 63.7% |
| P home draw | 62.7% |
| P draw away | 63.9% |
| P home away | 73.4% |
| Raw p home draw | 62.9% |
| Raw p draw away | 63.3% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.62 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.50 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | +0.5% |
| Draw probability edge | -0.4% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | 0.0107 |
| Raw ev home | 0.0125 |
| Raw edge prob draw | -0.0072 |
| Raw ev draw | -0.0325 |
| Raw edge prob away | -0.0036 |
| Raw ev away | -0.0318 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **41.5%**. Expected goals are 1.40 for Hull City and 1.05 for Brentford (2.46 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 45.3%; Under 3.5 goals: 77.0%; Double Chance 1X: 58.5%; Double Chance X2: 68.1%; Double Chance 12 (either team wins): 73.4%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 31.9% | 3.14 |
| Draw | 26.6% | 3.76 |
| Brentford win | 41.5% | 2.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.40 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 71.5% |
| Under 1.5 | 28.5% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 23.0% |
| Under 3.5 | 77.0% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.67% |
| 2 | 0-1 | 11.74% |
| 3 | 1-2 | 10.35% |
| 4 | 0-0 | 9.00% |
| 5 | 1-0 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 31.9% | 20.1% | 4.72 | +50.4% |
| Draw | 26.6% | 23.6% | 4.09 | +8.9% |
| Brentford win | 41.5% | 56.3% | 1.79 | -25.7% |
| Over 2.5 | 45.3% | 56.4% | 1.73 | -21.6% |
| Under 2.5 | 54.7% | 43.6% | 2.28 | +24.7% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4049 |
| Dc lambda away | 1.0515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.11 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.51 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.35 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.60 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 43.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 50.6% |
| P home draw | 58.5% |
| P draw away | 68.1% |
| P home away | 73.4% |
| Raw p home draw | 73.3% |
| Raw p draw away | 56.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 4.40 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | +11.7% |
| Draw probability edge | +3.1% |
| Away probability edge | -14.8% |
| Over 2.5 probability edge | -11.1% |
| Under 2.5 probability edge | +11.1% |
| Raw edge prob home | 0.2348 |
| Raw ev home | 1.0578 |
| Raw edge prob draw | 0.0611 |
| Raw ev draw | 0.2141 |
| Raw edge prob away | -0.2959 |
| Raw ev away | -0.5218 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **44.2%**. Expected goals are 1.63 for Liverpool and 1.43 for Brighton and Hove Albion (3.06 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 59.4%; Under 3.5 goals: 63.3%; Double Chance 1X: 69.6%; Double Chance X2: 55.8%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 62.1%; BTTS No (at least one team does not score): 37.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 44.2% | 2.26 |
| Draw | 25.4% | 3.94 |
| Brighton and Hove Albion win | 30.4% | 3.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.63 |
| Brighton and Hove Albion expected goals | 1.43 |
| Expected total goals | 3.06 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 82.3% |
| Under 1.5 | 17.7% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 36.7% |
| Under 3.5 | 63.3% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.70% |
| 2 | 2-1 | 9.57% |
| 3 | 1-2 | 7.33% |
| 4 | 1-0 | 6.86% |
| 5 | 2-0 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 44.2% | 47.3% | 2.11 | -6.7% |
| Draw | 25.4% | 24.3% | 4.00 | +1.5% |
| Brighton and Hove Albion win | 30.4% | 28.4% | 3.43 | +4.3% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6312 |
| Dc lambda away | 1.4279 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.1% |
| P btts no | 37.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.50 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.65 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.72 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.08 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 41.2% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 62.4% |
| P home draw | 69.6% |
| P draw away | 55.8% |
| P home away | 74.6% |
| Raw p home draw | 67.6% |
| Raw p draw away | 58.8% |
| Raw p home away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.00 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Home probability edge | -3.0% |
| Draw probability edge | +1.1% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | -0.0605 |
| Raw ev home | -0.1304 |
| Raw edge prob draw | 0.0212 |
| Raw ev draw | 0.0569 |
| Raw edge prob away | 0.0393 |
| Raw ev away | 0.1101 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **50.7%**. Expected goals are 1.79 for Manchester United and 1.28 for Bournemouth (3.08 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.9%; Under 3.5 goals: 62.8%; Double Chance 1X: 75.0%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 50.7% | 1.97 |
| Draw | 24.3% | 4.11 |
| Bournemouth win | 25.0% | 4.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.79 |
| Bournemouth expected goals | 1.28 |
| Expected total goals | 3.08 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.6% |
| Under 1.5 | 17.4% |
| Over 2.5 | 59.9% |
| Under 2.5 | 40.1% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.26% |
| 2 | 2-1 | 10.00% |
| 3 | 2-0 | 7.79% |
| 4 | 1-0 | 7.40% |
| 5 | 1-2 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 50.7% | 53.1% | 1.86 | -5.8% |
| Draw | 24.3% | 23.1% | 4.26 | +3.7% |
| Bournemouth win | 25.0% | 23.8% | 4.11 | +2.7% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7941 |
| Dc lambda away | 1.2834 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.02 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.74 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 4.99 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 48.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 26.2% |
| Raw p over 1 5 | 82.4% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 61.5% |
| P home draw | 75.0% |
| P draw away | 49.3% |
| P home away | 75.7% |
| Raw p home draw | 73.8% |
| Raw p draw away | 51.8% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.80 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.80 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | -0.0492 |
| Raw ev home | -0.1034 |
| Raw edge prob draw | 0.0247 |
| Raw ev draw | 0.0897 |
| Raw edge prob away | 0.0245 |
| Raw ev away | 0.0775 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **37.7%**. Expected goals are 1.08 for Sunderland and 1.23 for Leeds United (2.31 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 41.0%; Under 3.5 goals: 79.7%; Double Chance 1X: 62.3%; Double Chance X2: 67.7%; Double Chance 12 (either team wins): 70.0%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 32.3% | 3.10 |
| Draw | 30.0% | 3.33 |
| Leeds United win | 37.7% | 2.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.08 |
| Leeds United expected goals | 1.23 |
| Expected total goals | 2.31 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 68.7% |
| Under 1.5 | 31.3% |
| Over 2.5 | 41.0% |
| Under 2.5 | 59.0% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.12% |
| 2 | 0-0 | 11.01% |
| 3 | 0-1 | 10.61% |
| 4 | 1-0 | 9.69% |
| 5 | 1-2 | 8.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 32.3% | 33.8% | 2.90 | -6.3% |
| Draw | 30.0% | 28.7% | 3.44 | +3.2% |
| Leeds United win | 37.7% | 37.4% | 2.63 | -0.9% |
| Over 2.5 | 41.0% | 46.3% | 2.14 | -12.2% |
| Under 2.5 | 59.0% | 53.7% | 1.83 | +7.9% |

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
| Market best home last update utc | 2026-10-17T09:08:33Z |
| Market best draw last update utc | 2026-10-17T09:08:33Z |
| Market best away last update utc | 2026-10-17T09:08:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0815 |
| Dc lambda away | 1.2263 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:44:28.853796+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.08 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.93 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.66 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 30.8% |
| Unadjusted draw probability | 31.3% |
| Unadjusted away-win probability | 37.9% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.8% |
| Raw p btts yes | 48.2% |
| P home draw | 62.3% |
| P draw away | 67.7% |
| P home away | 70.0% |
| Raw p home draw | 62.1% |
| Raw p draw away | 69.2% |
| Raw p home away | 68.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.75 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.50 |
| Market reference 1x2 last update utc | 2026-10-17T09:08:57Z |
| Market reference home last update utc | 2026-10-17T09:08:57Z |
| Market reference draw last update utc | 2026-10-17T09:08:57Z |
| Market reference away last update utc | 2026-10-17T09:08:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.75 |
| Market reference over 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:08:57Z |
| Market best over 2 5 last update utc | 2026-10-17T09:08:33Z |
| Market best under 2 5 last update utc | 2026-10-17T09:08:33Z |
| Home probability edge | -1.5% |
| Draw probability edge | +1.3% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | -0.0301 |
| Raw ev home | -0.1068 |
| Raw edge prob draw | 0.0252 |
| Raw ev draw | 0.0754 |
| Raw edge prob away | 0.0049 |
| Raw ev away | -0.0023 |

</details>


---
