# Premier League — football model report

Fixtures in this report: **10**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,970 |
| Training data through | 2026-10-19 |
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
| Training sha256 | 55462e9201d62112ea046050590e9692ab7b8110bef89cd30cbd21970f01b8aa |
| Training as of utc | 2026-10-21T10:36:38.744520+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 40, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T10:36:38.744520+00:00', 'observations': 152, 'observations_sha256': '7573f203656dce3257b0e3666ffe98c3211b68f54f117ef6dd3e93f2c9e9607e', 'eligible_training_matches': 75, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 85, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 8, 'retrospective_eligible_training_matches': 75, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '8521052ef16ec15c97fbfedbc2a955e8add385a56194b1b9f67f1a0cfb0f06a5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 930.796 |
| Base scoring parameter | 0.212 |
| Home-advantage parameter | 0.185 |
| Dixon-Coles low-score adjustment | -0.089 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 10.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261021T103638744520Z_fcd7e98d57f2800679c0689a4e81ff7890dc8b39433d3575f779eaaeaf49c237.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **43.8%**. Expected goals are 1.32 for Ipswich Town and 1.69 for Nottingham Forest (3.01 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 57.5%; Under 3.5 goals: 64.6%; Double Chance 1X: 56.2%; Double Chance X2: 70.7%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 81.5%; BTTS Yes (both teams score): 61.0%; BTTS No (at least one team does not score): 39.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 29.3% | 3.41 |
| Draw | 26.8% | 3.73 |
| Nottingham Forest win | 43.8% | 2.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.32 |
| Nottingham Forest expected goals | 1.69 |
| Expected total goals | 3.01 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 57.5% |
| Under 2.5 | 42.5% |
| Over 3.5 | 35.4% |
| Under 3.5 | 64.6% |
| Over 4.5 | 18.5% |
| Under 4.5 | 81.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.47% |
| 2 | 1-2 | 9.01% |
| 3 | 2-1 | 7.33% |
| 4 | 0-1 | 7.12% |
| 5 | 0-2 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 29.3% | 29.6% | 3.31 | -2.9% |
| Draw | 26.8% | 27.9% | 3.57 | -4.2% |
| Nottingham Forest win | 43.8% | 42.5% | 2.31 | +1.3% |
| Over 2.5 | 57.5% | 54.6% | 1.83 | +5.3% |
| Under 2.5 | 42.5% | 45.4% | 2.14 | -9.1% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3211 |
| Dc lambda away | 1.6907 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:36:38.744520+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.0% |
| P btts no | 39.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.27 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.31 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.82 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.41 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 29.0% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 45.2% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 64.5% |
| Raw p btts yes | 60.8% |
| P home draw | 56.2% |
| P draw away | 70.7% |
| P home away | 73.2% |
| Raw p home draw | 54.8% |
| Raw p draw away | 71.0% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.35 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.34 |
| Market reference 1x2 last update utc | 2026-10-21T10:36:33Z |
| Market reference home last update utc | 2026-10-21T10:36:33Z |
| Market reference draw last update utc | 2026-10-21T10:36:33Z |
| Market reference away last update utc | 2026-10-21T10:36:33Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:33Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:33Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:31Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:31Z |
| Home probability edge | -0.3% |
| Draw probability edge | -1.1% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | -0.0055 |
| Raw ev home | -0.0385 |
| Raw edge prob draw | -0.0216 |
| Raw ev draw | -0.0802 |
| Raw edge prob away | 0.0271 |
| Raw ev away | 0.0439 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **66.7%**. Expected goals are 1.72 for Arsenal and 0.58 for Everton (2.29 combined). The most likely exact score is 1-0 at 17.1%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 41.1%; Under 3.5 goals: 79.8%; Double Chance 1X: 89.3%; Double Chance X2: 33.3%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 36.3%; BTTS No (at least one team does not score): 63.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 66.7% | 1.50 |
| Draw | 22.6% | 4.43 |
| Everton win | 10.7% | 9.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.72 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 68.1% |
| Under 1.5 | 31.9% |
| Over 2.5 | 41.1% |
| Under 2.5 | 58.9% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.08% |
| 2 | 2-0 | 15.45% |
| 3 | 0-0 | 10.09% |
| 4 | 1-1 | 9.98% |
| 5 | 2-1 | 8.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 66.7% | 69.2% | 1.46 | -2.6% |
| Draw | 22.6% | 20.6% | 4.72 | +6.7% |
| Everton win | 10.7% | 10.2% | 8.63 | -8.0% |
| Over 2.5 | 41.1% | 53.0% | 1.89 | -22.4% |
| Under 2.5 | 58.9% | 47.0% | 2.06 | +21.4% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7158 |
| Dc lambda away | 0.5763 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:36:38.744520+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.3% |
| P btts no | 63.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.92 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.13 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.94 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.74 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 11.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 36.8% |
| P home draw | 89.3% |
| P draw away | 33.3% |
| P home away | 77.4% |
| Raw p home draw | 88.9% |
| Raw p draw away | 35.7% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.44 |
| Reference draw odds | 4.80 |
| Reference away odds | 9.60 |
| Market reference 1x2 last update utc | 2026-10-21T10:36:33Z |
| Market reference home last update utc | 2026-10-21T10:36:33Z |
| Market reference draw last update utc | 2026-10-21T10:36:33Z |
| Market reference away last update utc | 2026-10-21T10:36:33Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:33Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:33Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:31Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:31Z |
| Home probability edge | -2.5% |
| Draw probability edge | +2.0% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -11.9% |
| Under 2.5 probability edge | +11.9% |
| Raw edge prob home | -0.0497 |
| Raw ev home | -0.0619 |
| Raw edge prob draw | 0.0408 |
| Raw ev draw | 0.1630 |
| Raw edge prob away | 0.0089 |
| Raw ev away | -0.0416 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **54.9%**. Expected goals are 1.12 for Aston Villa and 1.82 for Manchester City (2.95 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 57.0%; Under 3.5 goals: 65.7%; Double Chance 1X: 45.1%; Double Chance X2: 78.5%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 82.2%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 21.5% | 4.64 |
| Draw | 23.5% | 4.25 |
| Manchester City win | 54.9% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.12 |
| Manchester City expected goals | 1.82 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 57.0% |
| Under 2.5 | 43.0% |
| Over 3.5 | 34.3% |
| Under 3.5 | 65.7% |
| Over 4.5 | 17.8% |
| Under 4.5 | 82.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.09% |
| 2 | 1-2 | 10.19% |
| 3 | 0-2 | 9.08% |
| 4 | 0-1 | 8.96% |
| 5 | 1-3 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 21.5% | 20.8% | 4.72 | +1.7% |
| Draw | 23.5% | 22.2% | 4.29 | +1.0% |
| Manchester City win | 54.9% | 57.0% | 1.76 | -3.3% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1221 |
| Dc lambda away | 1.8244 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:36:38.744520+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.00 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.10 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.61 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.8% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 57.5% |
| P home draw | 45.1% |
| P draw away | 78.5% |
| P home away | 76.5% |
| Raw p home draw | 47.2% |
| Raw p draw away | 77.7% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 4.70 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.74 |
| Market reference 1x2 last update utc | 2026-10-21T10:36:33Z |
| Market reference home last update utc | 2026-10-21T10:36:33Z |
| Market reference draw last update utc | 2026-10-21T10:36:33Z |
| Market reference away last update utc | 2026-10-21T10:36:33Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:09Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:09Z |
| Home probability edge | +0.8% |
| Draw probability edge | +1.3% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.0152 |
| Raw ev home | 0.0528 |
| Raw edge prob draw | 0.0263 |
| Raw ev draw | 0.0662 |
| Raw edge prob away | -0.0415 |
| Raw ev away | -0.0700 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **57.5%**. Expected goals are 2.13 for Chelsea and 1.19 for Tottenham Hotspur (3.33 combined). The most likely exact score is 1-1 at 9.9%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 64.6%; Under 3.5 goals: 57.5%; Double Chance 1X: 79.6%; Double Chance X2: 42.5%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 62.3%; BTTS No (at least one team does not score): 37.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 57.5% | 1.74 |
| Draw | 22.1% | 4.53 |
| Tottenham Hotspur win | 20.4% | 4.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.13 |
| Tottenham Hotspur expected goals | 1.19 |
| Expected total goals | 3.33 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 64.6% |
| Under 2.5 | 35.4% |
| Over 3.5 | 42.5% |
| Under 3.5 | 57.5% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.93% |
| 2 | 2-1 | 9.66% |
| 3 | 2-0 | 8.09% |
| 4 | 3-1 | 6.87% |
| 5 | 1-0 | 6.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 57.5% | 56.9% | 1.75 | +0.6% |
| Draw | 22.1% | 22.0% | 4.41 | -2.7% |
| Tottenham Hotspur win | 20.4% | 21.1% | 4.57 | -6.5% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1329 |
| Dc lambda away | 1.1934 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:36:38.744520+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.3% |
| P btts no | 37.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.75 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.78 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.82 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.13 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 58.0% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 19.8% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.2% |
| P home draw | 79.6% |
| P draw away | 42.5% |
| P home away | 77.9% |
| Raw p home draw | 80.2% |
| Raw p draw away | 42.0% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.75 |
| Reference draw odds | 4.50 |
| Reference away odds | 4.70 |
| Market reference 1x2 last update utc | 2026-10-21T10:36:34Z |
| Market reference home last update utc | 2026-10-21T10:36:34Z |
| Market reference draw last update utc | 2026-10-21T10:36:34Z |
| Market reference away last update utc | 2026-10-21T10:36:34Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:09Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:09Z |
| Home probability edge | +0.6% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | 0.0111 |
| Raw ev home | 0.0157 |
| Raw edge prob draw | 0.0012 |
| Raw ev draw | -0.0243 |
| Raw edge prob away | -0.0123 |
| Raw ev away | -0.0935 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **41.4%**. Expected goals are 1.10 for Coventry City and 1.37 for Fulham (2.47 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 45.0%; Under 3.5 goals: 76.4%; Double Chance 1X: 58.6%; Double Chance X2: 70.0%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 30.0% | 3.33 |
| Draw | 28.6% | 3.50 |
| Fulham win | 41.4% | 2.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.10 |
| Fulham expected goals | 1.37 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.0% |
| Under 2.5 | 55.0% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.59% |
| 2 | 0-1 | 10.36% |
| 3 | 0-0 | 9.41% |
| 4 | 1-2 | 8.65% |
| 5 | 1-0 | 8.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 30.0% | 31.0% | 3.12 | -6.3% |
| Draw | 28.6% | 27.9% | 3.61 | +3.1% |
| Fulham win | 41.4% | 41.1% | 2.39 | -1.0% |
| Over 2.5 | 45.0% | 55.1% | 1.81 | -18.5% |
| Under 2.5 | 55.0% | 44.9% | 2.15 | +18.2% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1011 |
| Dc lambda away | 1.3667 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:36:38.744520+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.63 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.22 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.51 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 29.1% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 41.7% |
| Raw p over 1 5 | 71.7% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 50.9% |
| P home draw | 58.6% |
| P draw away | 70.0% |
| P home away | 71.4% |
| Raw p home draw | 58.3% |
| Raw p draw away | 70.9% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.20 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.42 |
| Market reference 1x2 last update utc | 2026-10-21T10:36:33Z |
| Market reference home last update utc | 2026-10-21T10:36:33Z |
| Market reference draw last update utc | 2026-10-21T10:36:33Z |
| Market reference away last update utc | 2026-10-21T10:36:33Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.14 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:33Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:33Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:31Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:31Z |
| Home probability edge | -1.0% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | -0.0194 |
| Raw ev home | -0.0934 |
| Raw edge prob draw | 0.0127 |
| Raw ev draw | 0.0538 |
| Raw edge prob away | 0.0068 |
| Raw ev away | -0.0022 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **39.6%**. Expected goals are 1.50 for Crystal Palace and 1.58 for Newcastle United (3.08 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.3%; Under 3.5 goals: 63.0%; Double Chance 1X: 60.4%; Double Chance X2: 65.8%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 62.6%; BTTS No (at least one team does not score): 37.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 34.2% | 2.92 |
| Draw | 26.1% | 3.83 |
| Newcastle United win | 39.6% | 2.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.50 |
| Newcastle United expected goals | 1.58 |
| Expected total goals | 3.08 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 59.3% |
| Under 2.5 | 40.7% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.00% |
| 2 | 1-2 | 8.78% |
| 3 | 2-1 | 7.93% |
| 4 | 2-2 | 6.51% |
| 5 | 0-1 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 34.2% | 33.3% | 3.02 | +3.4% |
| Draw | 26.1% | 26.4% | 3.67 | -4.1% |
| Newcastle United win | 39.6% | 40.4% | 2.42 | -4.1% |
| Over 2.5 | 59.3% | 59.1% | 1.69 | +0.2% |
| Under 2.5 | 40.7% | 40.9% | 2.36 | -3.9% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4954 |
| Dc lambda away | 1.5800 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:36:38.744520+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.6% |
| P btts no | 37.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.72 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.60 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.71 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.07 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 35.2% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 62.6% |
| P home draw | 60.4% |
| P draw away | 65.8% |
| P home away | 73.9% |
| Raw p home draw | 61.1% |
| Raw p draw away | 64.8% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.98 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.46 |
| Market reference 1x2 last update utc | 2026-10-21T10:36:34Z |
| Market reference home last update utc | 2026-10-21T10:36:34Z |
| Market reference draw last update utc | 2026-10-21T10:36:34Z |
| Market reference away last update utc | 2026-10-21T10:36:34Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:32Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:32Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:31Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:31Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.0196 |
| Raw ev home | 0.0636 |
| Raw edge prob draw | -0.0050 |
| Raw ev draw | -0.0501 |
| Raw edge prob away | -0.0146 |
| Raw ev away | -0.0587 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **43.8%**. Expected goals are 1.19 for Hull City and 1.05 for Brentford (2.25 combined). The most likely exact score is 0-1 at 14.1%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 40.0%; Under 3.5 goals: 81.0%; Double Chance 1X: 56.2%; Double Chance X2: 71.3%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 28.7% | 3.48 |
| Draw | 27.5% | 3.64 |
| Brentford win | 43.8% | 2.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.19 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.25 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 66.8% |
| Under 1.5 | 33.2% |
| Over 2.5 | 40.0% |
| Under 2.5 | 60.0% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.09% |
| 2 | 1-1 | 12.80% |
| 3 | 0-0 | 10.41% |
| 4 | 1-2 | 9.90% |
| 5 | 1-0 | 8.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 28.7% | 19.5% | 4.82 | +38.4% |
| Draw | 27.5% | 23.9% | 4.11 | +12.9% |
| Brentford win | 43.8% | 56.6% | 1.77 | -22.4% |
| Over 2.5 | 40.0% | 56.3% | 1.73 | -30.7% |
| Under 2.5 | 60.0% | 43.7% | 2.28 | +36.7% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Dc lambda home | 1.1917 |
| Dc lambda away | 1.0538 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:36:38.744520+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.61 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.27 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.52 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 31.1% |
| Unadjusted away-win probability | 31.0% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 46.5% |
| P home draw | 56.2% |
| P draw away | 71.3% |
| P home away | 72.5% |
| Raw p home draw | 69.0% |
| Raw p draw away | 62.1% |
| Raw p home away | 68.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 5.00 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.75 |
| Market reference 1x2 last update utc | 2026-10-21T10:36:34Z |
| Market reference home last update utc | 2026-10-21T10:36:34Z |
| Market reference draw last update utc | 2026-10-21T10:36:34Z |
| Market reference away last update utc | 2026-10-21T10:36:34Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.17 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:32Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:32Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:31Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:31Z |
| Home probability edge | +9.2% |
| Draw probability edge | +3.6% |
| Away probability edge | -12.8% |
| Over 2.5 probability edge | -16.3% |
| Under 2.5 probability edge | +16.3% |
| Raw edge prob home | 0.1841 |
| Raw ev home | 0.8271 |
| Raw edge prob draw | 0.0721 |
| Raw ev draw | 0.2766 |
| Raw edge prob away | -0.2561 |
| Raw ev away | -0.4507 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **42.9%**. Expected goals are 1.64 for Liverpool and 1.47 for Brighton and Hove Albion (3.11 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.3%; Under 3.5 goals: 62.2%; Double Chance 1X: 68.0%; Double Chance X2: 57.1%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 62.9%; BTTS No (at least one team does not score): 37.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 42.9% | 2.33 |
| Draw | 25.1% | 3.98 |
| Brighton and Hove Albion win | 32.0% | 3.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.64 |
| Brighton and Hove Albion expected goals | 1.47 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.47% |
| 2 | 2-1 | 9.27% |
| 3 | 1-2 | 7.53% |
| 4 | 1-0 | 6.67% |
| 5 | 2-2 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 42.9% | 45.0% | 2.19 | -6.1% |
| Draw | 25.1% | 24.6% | 4.00 | +0.5% |
| Brighton and Hove Albion win | 32.0% | 30.4% | 3.25 | +4.0% |
| Over 2.5 | 60.3% | 60.0% | 1.64 | -1.0% |
| Under 2.5 | 39.7% | 40.0% | 2.47 | -2.0% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6381 |
| Dc lambda away | 1.4737 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:36:38.744520+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.86 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.78 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.88 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 40.7% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 33.6% |
| Raw p over 1 5 | 82.7% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.1% |
| P home draw | 68.0% |
| P draw away | 57.1% |
| P home away | 74.9% |
| Raw p home draw | 66.4% |
| Raw p draw away | 59.3% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.20 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-21T10:36:34Z |
| Market reference home last update utc | 2026-10-21T10:36:34Z |
| Market reference draw last update utc | 2026-10-21T10:36:34Z |
| Market reference away last update utc | 2026-10-21T10:36:34Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:32Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:32Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:31Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:31Z |
| Home probability edge | -2.2% |
| Draw probability edge | +0.5% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | -0.0431 |
| Raw ev home | -0.1079 |
| Raw edge prob draw | 0.0103 |
| Raw ev draw | 0.0253 |
| Raw edge prob away | 0.0328 |
| Raw ev away | 0.0930 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **49.3%**. Expected goals are 1.76 for Manchester United and 1.27 for Bournemouth (3.04 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 58.6%; Under 3.5 goals: 63.9%; Double Chance 1X: 74.4%; Double Chance X2: 50.7%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 49.3% | 2.03 |
| Draw | 25.1% | 3.99 |
| Bournemouth win | 25.6% | 3.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.76 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 58.6% |
| Under 2.5 | 41.4% |
| Over 3.5 | 36.1% |
| Under 3.5 | 63.9% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.64% |
| 2 | 2-1 | 9.76% |
| 3 | 1-0 | 7.72% |
| 4 | 2-0 | 7.68% |
| 5 | 1-2 | 6.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 49.3% | 50.6% | 1.91 | -5.8% |
| Draw | 25.1% | 24.9% | 4.05 | +1.6% |
| Bournemouth win | 25.6% | 24.6% | 4.07 | +4.2% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7644 |
| Dc lambda away | 1.2709 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:36:38.744520+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.48 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.44 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 48.1% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 60.6% |
| P home draw | 74.4% |
| P draw away | 50.7% |
| P home away | 74.9% |
| Raw p home draw | 73.3% |
| Raw p draw away | 51.9% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.96 |
| Reference draw odds | 3.95 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-21T10:36:34Z |
| Market reference home last update utc | 2026-10-21T10:36:34Z |
| Market reference draw last update utc | 2026-10-21T10:36:34Z |
| Market reference away last update utc | 2026-10-21T10:36:34Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:32Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:32Z |
| Home probability edge | -1.3% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | -0.0253 |
| Raw ev home | -0.0822 |
| Raw edge prob draw | 0.0041 |
| Raw ev draw | 0.0240 |
| Raw edge prob away | 0.0211 |
| Raw ev away | 0.0853 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **38.7%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.28 combined). The most likely exact score is 1-1 at 14.2%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 40.0%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.3%; Double Chance X2: 69.0%; Double Chance 12 (either team wins): 69.7%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 47.2%; BTTS No (at least one team does not score): 52.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 31.0% | 3.22 |
| Draw | 30.3% | 3.30 |
| Leeds United win | 38.7% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.07 |
| Leeds United expected goals | 1.21 |
| Expected total goals | 2.28 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 67.7% |
| Under 1.5 | 32.3% |
| Over 2.5 | 40.0% |
| Under 2.5 | 60.0% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.18% |
| 2 | 0-1 | 11.37% |
| 3 | 0-0 | 11.22% |
| 4 | 1-0 | 9.74% |
| 5 | 1-2 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 31.0% | 31.0% | 3.17 | -1.6% |
| Draw | 30.3% | 29.7% | 3.33 | +0.8% |
| Leeds United win | 38.7% | 39.2% | 2.57 | -0.6% |
| Over 2.5 | 40.0% | 44.9% | 2.19 | -12.3% |
| Under 2.5 | 60.0% | 55.1% | 1.79 | +7.3% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0685 |
| Dc lambda away | 1.2112 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:36:38.744520+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.2% |
| P btts no | 52.8% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.91 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.22 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.3% |
| Raw p btts yes | 47.3% |
| P home draw | 61.3% |
| P draw away | 69.0% |
| P home away | 69.7% |
| Raw p home draw | 61.9% |
| Raw p draw away | 68.9% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.15 |
| Reference draw odds | 3.28 |
| Reference away odds | 2.50 |
| Market reference 1x2 last update utc | 2026-10-21T10:36:36Z |
| Market reference home last update utc | 2026-10-21T10:36:36Z |
| Market reference draw last update utc | 2026-10-21T10:36:36Z |
| Market reference away last update utc | 2026-10-21T10:36:36Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.14 |
| Reference Under 2.5 odds | 1.76 |
| Market reference over 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:36:36Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:31Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:31Z |
| Home probability edge | +0.0% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | 0.0007 |
| Raw ev home | -0.0150 |
| Raw edge prob draw | 0.0104 |
| Raw ev draw | 0.0252 |
| Raw edge prob away | -0.0111 |
| Raw ev away | -0.0198 |

</details>


---
