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
| Training as of utc | 2026-10-21T09:17:50.184455+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 40, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T09:17:50.184455+00:00', 'observations': 152, 'observations_sha256': '7573f203656dce3257b0e3666ffe98c3211b68f54f117ef6dd3e93f2c9e9607e', 'eligible_training_matches': 75, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 85, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 8, 'retrospective_eligible_training_matches': 75, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '8521052ef16ec15c97fbfedbc2a955e8add385a56194b1b9f67f1a0cfb0f06a5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 930.943 |
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
| Bbs statistics model artifact | bbs/feature_models/EPL/20261021T091750184455Z_a53d1c9c56588e7bdc7925d088faf5e9024bc821c2945fed323b58ae0a3f8650.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **44.1%**. Expected goals are 1.32 for Ipswich Town and 1.69 for Nottingham Forest (3.01 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 57.6%; Under 3.5 goals: 64.5%; Double Chance 1X: 55.9%; Double Chance X2: 70.7%; Double Chance 12 (either team wins): 73.4%; Under 4.5 goals: 81.5%; BTTS Yes (both teams score): 61.0%; BTTS No (at least one team does not score): 39.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 29.3% | 3.41 |
| Draw | 26.6% | 3.77 |
| Nottingham Forest win | 44.1% | 2.27 |

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
| Over 2.5 | 57.6% |
| Under 2.5 | 42.4% |
| Over 3.5 | 35.5% |
| Under 3.5 | 64.5% |
| Over 4.5 | 18.5% |
| Under 4.5 | 81.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.34% |
| 2 | 1-2 | 9.07% |
| 3 | 2-1 | 7.33% |
| 4 | 0-1 | 7.16% |
| 5 | 0-2 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 29.3% | 29.6% | 3.31 | -2.9% |
| Draw | 26.6% | 27.3% | 3.57 | -5.2% |
| Nottingham Forest win | 44.1% | 43.0% | 2.31 | +1.9% |
| Over 2.5 | 57.6% | 54.2% | 1.83 | +5.5% |
| Under 2.5 | 42.4% | 45.8% | 2.14 | -9.4% |

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
| Market best home last update utc | 2026-10-21T09:17:13Z |
| Market best draw last update utc | 2026-10-21T09:17:13Z |
| Market best away last update utc | 2026-10-21T09:17:13Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:17:50.184455+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.0% |
| P btts no | 39.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.45 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.31 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.82 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.40 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 29.0% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 45.2% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 64.5% |
| Raw p btts yes | 60.8% |
| P home draw | 55.9% |
| P draw away | 70.7% |
| P home away | 73.4% |
| Raw p home draw | 54.8% |
| Raw p draw away | 71.0% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.22 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-21T09:17:56Z |
| Market reference home last update utc | 2026-10-21T09:17:56Z |
| Market reference draw last update utc | 2026-10-21T09:17:56Z |
| Market reference away last update utc | 2026-10-21T09:17:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:13Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:13Z |
| Home probability edge | -0.3% |
| Draw probability edge | -0.8% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +3.5% |
| Under 2.5 probability edge | -3.5% |
| Raw edge prob home | -0.0059 |
| Raw ev home | -0.0385 |
| Raw edge prob draw | -0.0157 |
| Raw ev draw | -0.0802 |
| Raw edge prob away | 0.0216 |
| Raw ev away | 0.0439 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **66.7%**. Expected goals are 1.72 for Arsenal and 0.58 for Everton (2.29 combined). The most likely exact score is 1-0 at 17.1%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.1%; Under 3.5 goals: 79.8%; Double Chance 1X: 89.0%; Double Chance X2: 33.3%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 36.2%; BTTS No (at least one team does not score): 63.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 66.7% | 1.50 |
| Draw | 22.3% | 4.48 |
| Everton win | 11.0% | 9.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.72 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
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
| 1 | 1-0 | 17.07% |
| 2 | 2-0 | 15.44% |
| 3 | 0-0 | 9.96% |
| 4 | 1-1 | 9.86% |
| 5 | 2-1 | 8.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 66.7% | 69.1% | 1.46 | -2.7% |
| Draw | 22.3% | 20.0% | 4.72 | +5.4% |
| Everton win | 11.0% | 10.9% | 8.59 | -5.6% |
| Over 2.5 | 41.1% | 52.4% | 1.89 | -22.3% |
| Under 2.5 | 58.9% | 47.6% | 2.06 | +21.3% |

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
| Market best home last update utc | 2026-10-21T09:17:13Z |
| Market best draw last update utc | 2026-10-21T09:17:13Z |
| Market best away last update utc | 2026-10-21T09:17:52Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:17:50.184455+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.2% |
| P btts no | 63.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.04 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.13 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.94 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.73 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 11.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 36.8% |
| P home draw | 89.0% |
| P draw away | 33.3% |
| P home away | 77.7% |
| Raw p home draw | 88.9% |
| Raw p draw away | 35.7% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.42 |
| Reference draw odds | 4.60 |
| Reference away odds | 8.20 |
| Market reference 1x2 last update utc | 2026-10-21T09:17:56Z |
| Market reference home last update utc | 2026-10-21T09:17:56Z |
| Market reference draw last update utc | 2026-10-21T09:17:56Z |
| Market reference away last update utc | 2026-10-21T09:17:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:13Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:13Z |
| Home probability edge | -2.4% |
| Draw probability edge | +2.3% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | -0.0484 |
| Raw ev home | -0.0619 |
| Raw edge prob draw | 0.0462 |
| Raw ev draw | 0.1630 |
| Raw edge prob away | 0.0022 |
| Raw ev away | -0.0460 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **55.0%**. Expected goals are 1.12 for Aston Villa and 1.82 for Manchester City (2.95 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 56.9%; Under 3.5 goals: 65.7%; Double Chance 1X: 45.0%; Double Chance X2: 78.7%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 82.2%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 21.3% | 4.69 |
| Draw | 23.7% | 4.21 |
| Manchester City win | 55.0% | 1.82 |

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
| Over 2.5 | 56.9% |
| Under 2.5 | 43.1% |
| Over 3.5 | 34.3% |
| Under 3.5 | 65.7% |
| Over 4.5 | 17.8% |
| Under 4.5 | 82.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.18% |
| 2 | 1-2 | 10.20% |
| 3 | 0-2 | 9.09% |
| 4 | 0-1 | 8.97% |
| 5 | 1-3 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 21.3% | 20.3% | 4.72 | +0.6% |
| Draw | 23.7% | 22.6% | 4.28 | +1.6% |
| Manchester City win | 55.0% | 57.1% | 1.76 | -3.3% |

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
| Market best home last update utc | 2026-10-21T09:17:13Z |
| Market best draw last update utc | 2026-10-21T09:17:52Z |
| Market best away last update utc | 2026-10-21T09:17:13Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1220 |
| Dc lambda away | 1.8243 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:17:50.184455+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.86 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.10 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.62 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.8% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 57.5% |
| P home draw | 45.0% |
| P draw away | 78.7% |
| P home away | 76.3% |
| Raw p home draw | 47.2% |
| Raw p draw away | 77.7% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.60 |
| Reference draw odds | 4.15 |
| Reference away odds | 1.71 |
| Market reference 1x2 last update utc | 2026-10-21T09:17:56Z |
| Market reference home last update utc | 2026-10-21T09:17:56Z |
| Market reference draw last update utc | 2026-10-21T09:17:56Z |
| Market reference away last update utc | 2026-10-21T09:17:56Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.58 |
| Market reference over 2 5 last update utc | 2026-10-21T09:17:32Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:17:32Z |
| Home probability edge | +1.0% |
| Draw probability edge | +1.1% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | 0.0200 |
| Raw ev home | 0.0528 |
| Raw edge prob draw | 0.0225 |
| Raw ev draw | 0.0637 |
| Raw edge prob away | -0.0425 |
| Raw ev away | -0.0700 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **57.6%**. Expected goals are 2.13 for Chelsea and 1.19 for Tottenham Hotspur (3.33 combined). The most likely exact score is 1-1 at 9.9%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 64.6%; Under 3.5 goals: 57.5%; Double Chance 1X: 79.6%; Double Chance X2: 42.4%; Double Chance 12 (either team wins): 78.0%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 62.2%; BTTS No (at least one team does not score): 37.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 57.6% | 1.74 |
| Draw | 22.0% | 4.55 |
| Tottenham Hotspur win | 20.4% | 4.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.13 |
| Tottenham Hotspur expected goals | 1.19 |
| Expected total goals | 3.33 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 64.6% |
| Under 2.5 | 35.4% |
| Over 3.5 | 42.5% |
| Under 3.5 | 57.5% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.89% |
| 2 | 2-1 | 9.68% |
| 3 | 2-0 | 8.11% |
| 4 | 3-1 | 6.88% |
| 5 | 1-0 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 57.6% | 57.1% | 1.75 | +0.8% |
| Draw | 22.0% | 21.8% | 4.41 | -3.1% |
| Tottenham Hotspur win | 20.4% | 21.1% | 4.57 | -6.6% |

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
| Market best home last update utc | 2026-10-21T09:17:13Z |
| Market best draw last update utc | 2026-10-21T09:17:13Z |
| Market best away last update utc | 2026-10-21T09:17:13Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:17:50.184455+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.2% |
| P btts no | 37.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.84 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.78 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.83 |
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
| P draw away | 42.4% |
| P home away | 78.0% |
| Raw p home draw | 80.2% |
| Raw p draw away | 42.0% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.71 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.45 |
| Market reference 1x2 last update utc | 2026-10-21T09:17:56Z |
| Market reference home last update utc | 2026-10-21T09:17:56Z |
| Market reference draw last update utc | 2026-10-21T09:17:56Z |
| Market reference away last update utc | 2026-10-21T09:17:56Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.66 |
| Market reference over 2 5 last update utc | 2026-10-21T09:17:32Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:17:32Z |
| Home probability edge | +0.5% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0091 |
| Raw ev home | 0.0157 |
| Raw edge prob draw | 0.0030 |
| Raw ev draw | -0.0243 |
| Raw edge prob away | -0.0122 |
| Raw ev away | -0.0935 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **41.6%**. Expected goals are 1.10 for Coventry City and 1.37 for Fulham (2.47 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.4%; Double Chance 1X: 58.4%; Double Chance X2: 69.7%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 89.4%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 30.3% | 3.30 |
| Draw | 28.1% | 3.56 |
| Fulham win | 41.6% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.10 |
| Fulham expected goals | 1.37 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.38% |
| 2 | 0-1 | 10.42% |
| 3 | 0-0 | 9.26% |
| 4 | 1-2 | 8.69% |
| 5 | 1-0 | 8.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 30.3% | 31.5% | 3.12 | -5.6% |
| Draw | 28.1% | 27.0% | 3.61 | +1.5% |
| Fulham win | 41.6% | 41.5% | 2.39 | -0.5% |
| Over 2.5 | 45.2% | 54.6% | 1.81 | -18.3% |
| Under 2.5 | 54.8% | 45.4% | 2.15 | +17.9% |

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
| Market best home last update utc | 2026-10-21T09:17:13Z |
| Market best draw last update utc | 2026-10-21T09:17:13Z |
| Market best away last update utc | 2026-10-21T09:17:13Z |
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
| Dc lambda away | 1.3664 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:17:50.184455+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.80 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.47 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 29.1% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 41.7% |
| Raw p over 1 5 | 71.7% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 50.9% |
| P home draw | 58.4% |
| P draw away | 69.7% |
| P home away | 71.9% |
| Raw p home draw | 58.3% |
| Raw p draw away | 70.9% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.04 |
| Reference draw odds | 3.52 |
| Reference away odds | 2.33 |
| Market reference 1x2 last update utc | 2026-10-21T09:17:56Z |
| Market reference home last update utc | 2026-10-21T09:17:56Z |
| Market reference draw last update utc | 2026-10-21T09:17:56Z |
| Market reference away last update utc | 2026-10-21T09:17:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:13Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:13Z |
| Home probability edge | -1.2% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.0241 |
| Raw ev home | -0.0932 |
| Raw edge prob draw | 0.0217 |
| Raw ev draw | 0.0539 |
| Raw edge prob away | 0.0024 |
| Raw ev away | -0.0024 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **39.9%**. Expected goals are 1.50 for Crystal Palace and 1.58 for Newcastle United (3.08 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 59.2%; Under 3.5 goals: 63.0%; Double Chance 1X: 60.1%; Double Chance X2: 66.1%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 62.6%; BTTS No (at least one team does not score): 37.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 33.9% | 2.95 |
| Draw | 26.2% | 3.82 |
| Newcastle United win | 39.9% | 2.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.50 |
| Newcastle United expected goals | 1.58 |
| Expected total goals | 3.08 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 59.2% |
| Under 2.5 | 40.8% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.03% |
| 2 | 1-2 | 8.84% |
| 3 | 2-1 | 7.85% |
| 4 | 2-2 | 6.52% |
| 5 | 0-1 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 33.9% | 32.6% | 3.02 | +2.3% |
| Draw | 26.2% | 26.5% | 3.67 | -3.8% |
| Newcastle United win | 39.9% | 40.9% | 2.42 | -3.4% |
| Over 2.5 | 59.2% | 58.9% | 1.69 | +0.1% |
| Under 2.5 | 40.8% | 41.1% | 2.36 | -3.8% |

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
| Market best home last update utc | 2026-10-21T09:17:13Z |
| Market best draw last update utc | 2026-10-21T09:17:13Z |
| Market best away last update utc | 2026-10-21T09:17:13Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:17:50.184455+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.6% |
| P btts no | 37.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.67 |
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
| P home draw | 60.1% |
| P draw away | 66.1% |
| P home away | 73.8% |
| Raw p home draw | 61.1% |
| Raw p draw away | 64.8% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.94 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.36 |
| Market reference 1x2 last update utc | 2026-10-21T09:17:56Z |
| Market reference home last update utc | 2026-10-21T09:17:56Z |
| Market reference draw last update utc | 2026-10-21T09:17:56Z |
| Market reference away last update utc | 2026-10-21T09:17:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.29 |
| Market reference over 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:13Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:13Z |
| Home probability edge | +1.3% |
| Draw probability edge | -0.3% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.0266 |
| Raw ev home | 0.0636 |
| Raw edge prob draw | -0.0064 |
| Raw ev draw | -0.0501 |
| Raw edge prob away | -0.0202 |
| Raw ev away | -0.0587 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **43.8%**. Expected goals are 1.19 for Hull City and 1.05 for Brentford (2.24 combined). The most likely exact score is 0-1 at 14.1%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 40.1%; Under 3.5 goals: 81.0%; Double Chance 1X: 56.2%; Double Chance X2: 71.1%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 28.9% | 3.46 |
| Draw | 27.3% | 3.66 |
| Brentford win | 43.8% | 2.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.19 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 66.8% |
| Under 1.5 | 33.2% |
| Over 2.5 | 40.1% |
| Under 2.5 | 59.9% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.07% |
| 2 | 1-1 | 12.74% |
| 3 | 0-0 | 10.37% |
| 4 | 1-2 | 9.88% |
| 5 | 1-0 | 8.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 28.9% | 19.9% | 4.82 | +39.4% |
| Draw | 27.3% | 23.6% | 4.11 | +12.3% |
| Brentford win | 43.8% | 56.5% | 1.77 | -22.6% |
| Over 2.5 | 40.1% | 57.3% | 1.73 | -30.7% |
| Under 2.5 | 59.9% | 42.7% | 2.28 | +36.6% |

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
| Market best home last update utc | 2026-10-21T09:17:13Z |
| Market best draw last update utc | 2026-10-21T09:17:13Z |
| Market best away last update utc | 2026-10-21T09:17:13Z |
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
| Dc lambda home | 1.1912 |
| Dc lambda away | 1.0531 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:17:50.184455+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.65 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.27 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.53 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 31.1% |
| Unadjusted away-win probability | 31.0% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 46.5% |
| P home draw | 56.2% |
| P draw away | 71.1% |
| P home away | 72.7% |
| Raw p home draw | 69.0% |
| Raw p draw away | 62.1% |
| Raw p home away | 68.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.70 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.73 |
| Market reference 1x2 last update utc | 2026-10-21T09:17:56Z |
| Market reference home last update utc | 2026-10-21T09:17:56Z |
| Market reference draw last update utc | 2026-10-21T09:17:56Z |
| Market reference away last update utc | 2026-10-21T09:17:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:13Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:13Z |
| Home probability edge | +9.0% |
| Draw probability edge | +3.7% |
| Away probability edge | -12.7% |
| Over 2.5 probability edge | -17.2% |
| Under 2.5 probability edge | +17.2% |
| Raw edge prob home | 0.1797 |
| Raw ev home | 0.8272 |
| Raw edge prob draw | 0.0749 |
| Raw ev draw | 0.2770 |
| Raw edge prob away | -0.2546 |
| Raw ev away | -0.4509 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **43.1%**. Expected goals are 1.64 for Liverpool and 1.47 for Brighton and Hove Albion (3.11 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.4%; Under 3.5 goals: 62.1%; Double Chance 1X: 68.1%; Double Chance X2: 56.9%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 62.9%; BTTS No (at least one team does not score): 37.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 43.1% | 2.32 |
| Draw | 25.0% | 4.00 |
| Brighton and Hove Albion win | 31.9% | 3.14 |

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
| Over 2.5 | 60.4% |
| Under 2.5 | 39.6% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.41% |
| 2 | 2-1 | 9.32% |
| 3 | 1-2 | 7.51% |
| 4 | 1-0 | 6.70% |
| 5 | 2-2 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 43.1% | 45.5% | 2.19 | -5.6% |
| Draw | 25.0% | 24.4% | 4.01 | +0.2% |
| Brighton and Hove Albion win | 31.9% | 30.2% | 3.25 | +3.7% |
| Over 2.5 | 60.4% | 60.0% | 1.64 | -1.0% |
| Under 2.5 | 39.6% | 40.0% | 2.47 | -2.2% |

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
| Market best home last update utc | 2026-10-21T09:17:13Z |
| Market best draw last update utc | 2026-10-21T09:17:51Z |
| Market best away last update utc | 2026-10-21T09:17:13Z |
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
| Dc lambda away | 1.4736 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:17:50.184455+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.95 |
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
| P home draw | 68.1% |
| P draw away | 56.9% |
| P home away | 75.0% |
| Raw p home draw | 66.4% |
| Raw p draw away | 59.3% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.13 |
| Reference draw odds | 3.88 |
| Reference away odds | 3.16 |
| Market reference 1x2 last update utc | 2026-10-21T09:17:56Z |
| Market reference home last update utc | 2026-10-21T09:17:56Z |
| Market reference draw last update utc | 2026-10-21T09:17:56Z |
| Market reference away last update utc | 2026-10-21T09:17:56Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-21T09:17:32Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:17:32Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:13Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:13Z |
| Home probability edge | -2.4% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | -0.0475 |
| Raw ev home | -0.1079 |
| Raw edge prob draw | 0.0128 |
| Raw ev draw | 0.0279 |
| Raw edge prob away | 0.0347 |
| Raw ev away | 0.0929 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **50.2%**. Expected goals are 1.76 for Manchester United and 1.27 for Bournemouth (3.04 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 58.8%; Under 3.5 goals: 63.8%; Double Chance 1X: 74.8%; Double Chance X2: 49.8%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 50.2% | 1.99 |
| Draw | 24.6% | 4.07 |
| Bournemouth win | 25.2% | 3.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.76 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 36.2% |
| Under 3.5 | 63.8% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.41% |
| 2 | 2-1 | 9.93% |
| 3 | 1-0 | 7.85% |
| 4 | 2-0 | 7.81% |
| 5 | 1-2 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 50.2% | 52.3% | 1.91 | -4.1% |
| Draw | 24.6% | 23.9% | 4.05 | -0.5% |
| Bournemouth win | 25.2% | 23.8% | 4.07 | +2.7% |

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
| Market best home last update utc | 2026-10-21T09:17:14Z |
| Market best draw last update utc | 2026-10-21T09:17:14Z |
| Market best away last update utc | 2026-10-21T09:17:14Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7643 |
| Dc lambda away | 1.2710 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:17:50.184455+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.84 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.46 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.20 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 48.1% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 60.6% |
| P home draw | 74.8% |
| P draw away | 49.8% |
| P home away | 75.4% |
| Raw p home draw | 73.3% |
| Raw p draw away | 51.9% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.86 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.96 |
| Market reference 1x2 last update utc | 2026-10-21T09:17:56Z |
| Market reference home last update utc | 2026-10-21T09:17:56Z |
| Market reference draw last update utc | 2026-10-21T09:17:56Z |
| Market reference away last update utc | 2026-10-21T09:17:56Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T09:17:51Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:17:51Z |
| Home probability edge | -2.1% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | -0.0429 |
| Raw ev home | -0.0822 |
| Raw edge prob draw | 0.0142 |
| Raw ev draw | 0.0240 |
| Raw edge prob away | 0.0287 |
| Raw ev away | 0.0853 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **38.3%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.28 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 40.1%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.7%; Double Chance X2: 68.5%; Double Chance 12 (either team wins): 69.9%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 47.1%; BTTS No (at least one team does not score): 52.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 31.5% | 3.17 |
| Draw | 30.1% | 3.32 |
| Leeds United win | 38.3% | 2.61 |

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
| Over 2.5 | 40.1% |
| Under 2.5 | 59.9% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.11% |
| 2 | 0-1 | 11.27% |
| 3 | 0-0 | 11.16% |
| 4 | 1-0 | 9.90% |
| 5 | 1-2 | 8.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 31.5% | 32.0% | 3.17 | -0.0% |
| Draw | 30.1% | 29.4% | 3.33 | +0.3% |
| Leeds United win | 38.3% | 38.6% | 2.57 | -1.4% |
| Over 2.5 | 40.1% | 44.7% | 2.19 | -12.2% |
| Under 2.5 | 59.9% | 55.3% | 1.79 | +7.2% |

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
| Market best home last update utc | 2026-10-21T09:17:51Z |
| Market best draw last update utc | 2026-10-21T09:17:14Z |
| Market best away last update utc | 2026-10-21T09:17:14Z |
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
| Dc lambda away | 1.2111 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:17:50.184455+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.1% |
| P btts no | 52.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.96 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.20 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.3% |
| Raw p btts yes | 47.3% |
| P home draw | 61.7% |
| P draw away | 68.5% |
| P home away | 69.9% |
| Raw p home draw | 61.9% |
| Raw p draw away | 68.9% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.99 |
| Reference draw odds | 3.24 |
| Reference away odds | 2.50 |
| Market reference 1x2 last update utc | 2026-10-21T09:17:56Z |
| Market reference home last update utc | 2026-10-21T09:17:56Z |
| Market reference draw last update utc | 2026-10-21T09:17:56Z |
| Market reference away last update utc | 2026-10-21T09:17:56Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:17:56Z |
| Market best over 2 5 last update utc | 2026-10-21T09:17:14Z |
| Market best under 2 5 last update utc | 2026-10-21T09:17:14Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.0093 |
| Raw ev home | -0.0150 |
| Raw edge prob draw | 0.0135 |
| Raw ev draw | 0.0253 |
| Raw edge prob away | -0.0042 |
| Raw ev away | -0.0198 |

</details>


---
