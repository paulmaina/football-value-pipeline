# La Liga — football model report

Fixtures in this report: **14**.

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
| Training sha256 | be0a8dd32aac079fb0106994a7e51426250cd236e9f3884cde0ee53788d6fa2a |
| Training as of utc | 2026-10-19T11:19:05.367220+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 87, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 87, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-19T11:19:05.367220+00:00', 'observations': 106, 'observations_sha256': '8d570194510323203e756d6dad7442317066873eb859a76b2d1ebd0f96921734', 'eligible_training_matches': 45, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 73, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 8, 'retrospective_eligible_training_matches': 45, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '3e47382096de29d01d9d75ff6e34cdea596d346a0827343481150a62111aca9d', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 5519.514 |
| Base scoring parameter | 0.090 |
| Home-advantage parameter | 0.278 |
| Dixon-Coles low-score adjustment | -0.019 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 14.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261019T111905367220Z_8370b2956c3e6e2db85b262f2e525700679f912336677cb8a6bb16694edf0921.json |
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

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **50.9%**. Expected goals are 0.68 for Málaga and 1.55 for Real Sociedad (2.23 combined). The most likely exact score is 0-1 at 14.4%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 37.7%; Under 3.5 goals: 82.1%; Double Chance 1X: 49.1%; Double Chance X2: 77.1%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 92.7%; BTTS Yes (both teams score): 39.5%; BTTS No (at least one team does not score): 60.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 22.9% | 4.38 |
| Draw | 26.2% | 3.81 |
| Real Sociedad win | 50.9% | 1.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.68 |
| Real Sociedad expected goals | 1.55 |
| Expected total goals | 2.23 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 64.3% |
| Under 1.5 | 35.7% |
| Over 2.5 | 37.7% |
| Under 2.5 | 62.3% |
| Over 3.5 | 17.9% |
| Under 3.5 | 82.1% |
| Over 4.5 | 7.3% |
| Under 4.5 | 92.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.44% |
| 2 | 1-1 | 11.70% |
| 3 | 0-2 | 11.33% |
| 4 | 0-0 | 11.12% |
| 5 | 1-0 | 10.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 22.9% | 29.6% | 3.31 | -24.4% |
| Draw | 26.2% | 26.5% | 3.67 | -3.8% |
| Real Sociedad win | 50.9% | 43.8% | 2.27 | +15.6% |
| Over 2.5 | 37.7% | 57.0% | 1.74 | -34.3% |
| Under 2.5 | 62.3% | 43.0% | 2.27 | +41.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T16:30:00+00:00 |
| Fixture id | 1051298b4aca6f07113309bff598a5c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6804 |
| Dc lambda away | 1.5479 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 39.5% |
| P btts no | 60.5% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.99 |
| Fair Over 1.5 odds | 1.55 |
| Fair Under 1.5 odds | 2.80 |
| Fair Over 2.5 odds | 2.65 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.58 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.76 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 16.1% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 58.0% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 81.4% |
| Raw p btts yes | 39.1% |
| P home draw | 49.1% |
| P draw away | 77.1% |
| P home away | 73.8% |
| Raw p home draw | 42.0% |
| Raw p draw away | 83.9% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.22 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.21 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:36Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:36Z |
| Home probability edge | -6.8% |
| Draw probability edge | -0.3% |
| Away probability edge | +7.1% |
| Over 2.5 probability edge | -19.3% |
| Under 2.5 probability edge | +19.3% |
| Raw edge prob home | -0.1356 |
| Raw ev home | -0.4681 |
| Raw edge prob draw | -0.0063 |
| Raw ev draw | -0.0492 |
| Raw edge prob away | 0.1419 |
| Raw ev away | 0.3171 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **76.0%**. Expected goals are 2.43 for Real Madrid and 0.76 for Sevilla (3.19 combined). The most likely exact score is 2-0 at 12.5%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 62.4%; Under 3.5 goals: 60.1%; Double Chance 1X: 91.1%; Double Chance X2: 24.0%; Double Chance 12 (either team wins): 84.9%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 76.0% | 1.32 |
| Draw | 15.1% | 6.63 |
| Sevilla win | 8.9% | 11.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.43 |
| Sevilla expected goals | 0.76 |
| Expected total goals | 3.19 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 62.4% |
| Under 2.5 | 37.6% |
| Over 3.5 | 39.9% |
| Under 3.5 | 60.1% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.47% |
| 2 | 1-0 | 10.12% |
| 3 | 3-0 | 10.11% |
| 4 | 2-1 | 9.47% |
| 5 | 3-1 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 76.0% | 77.8% | 1.29 | -2.0% |
| Draw | 15.1% | 13.8% | 6.70 | +1.1% |
| Sevilla win | 8.9% | 8.3% | 10.90 | -2.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T19:00:00+00:00 |
| Fixture id | eccd63bf768e2f2a358b871d3f33a63d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4305 |
| Dc lambda away | 0.7589 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 48.2% |
| P btts no | 51.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.37 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.94 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.66 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.53 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 74.1% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 9.6% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 60.5% |
| Raw p btts yes | 48.6% |
| P home draw | 91.1% |
| P draw away | 24.0% |
| P home away | 84.9% |
| Raw p home draw | 90.4% |
| Raw p draw away | 25.9% |
| Raw p home away | 83.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.27 |
| Reference draw odds | 6.60 |
| Reference away odds | 10.75 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.99 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:55Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:55Z |
| Home probability edge | -1.9% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | -0.0374 |
| Raw ev home | -0.0440 |
| Raw edge prob draw | 0.0247 |
| Raw ev draw | 0.0935 |
| Raw edge prob away | 0.0126 |
| Raw ev away | 0.0431 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **36.1%**. Expected goals are 1.00 for Getafe and 0.78 for Rayo Vallecano (1.77 combined). The most likely exact score is 0-0 at 16.6%. Goal-market probabilities: at least one goal: 83.4%; Over 2.5 goals: 26.4%; Under 3.5 goals: 89.6%; Double Chance 1X: 68.3%; Double Chance X2: 63.9%; Double Chance 12 (either team wins): 67.8%; Under 4.5 goals: 96.5%; BTTS Yes (both teams score): 34.1%; BTTS No (at least one team does not score): 65.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 36.1% | 2.77 |
| Draw | 32.2% | 3.10 |
| Rayo Vallecano win | 31.7% | 3.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 1.00 |
| Rayo Vallecano expected goals | 0.78 |
| Expected total goals | 1.77 |
| Over 0.5 | 83.4% |
| Under 0.5 | 16.6% |
| Over 1.5 | 53.0% |
| Under 1.5 | 47.0% |
| Over 2.5 | 26.4% |
| Under 2.5 | 73.6% |
| Over 3.5 | 10.4% |
| Under 3.5 | 89.6% |
| Over 4.5 | 3.5% |
| Under 4.5 | 96.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 16.63% |
| 2 | 1-0 | 15.33% |
| 3 | 0-1 | 15.01% |
| 4 | 1-1 | 12.92% |
| 5 | 2-0 | 7.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 36.1% | 33.0% | 2.98 | +7.7% |
| Draw | 32.2% | 31.0% | 3.17 | +2.1% |
| Rayo Vallecano win | 31.7% | 36.0% | 2.74 | -13.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T19:00:00+00:00 |
| Fixture id | 4a88bc4de574d43ef34677fd8d78722f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9953 |
| Dc lambda away | 0.7770 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 34.1% |
| P btts no | 65.9% |
| Fair Over 0.5 odds | 1.20 |
| Fair Under 0.5 odds | 6.01 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.13 |
| Fair Over 2.5 odds | 3.78 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 9.63 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 28.84 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 39.3% |
| Unadjusted draw probability | 33.4% |
| Unadjusted away-win probability | 27.3% |
| Raw p over 1 5 | 53.1% |
| Raw p under 3 5 | 89.6% |
| Raw p btts yes | 34.3% |
| P home draw | 68.3% |
| P draw away | 63.9% |
| P home away | 67.8% |
| Raw p home draw | 72.7% |
| Raw p draw away | 60.7% |
| Raw p home away | 66.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.94 |
| Reference draw odds | 3.12 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.60 |
| Reference Under 2.5 odds | 1.51 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:58Z |
| Home probability edge | +3.2% |
| Draw probability edge | +1.2% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | 0.0631 |
| Raw ev home | 0.1707 |
| Raw edge prob draw | 0.0239 |
| Raw ev draw | 0.0591 |
| Raw edge prob away | -0.0869 |
| Raw ev away | -0.2518 |
| Market p home draw | 64.3% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:33:36Z |
| Market reference home draw last update utc | 2026-10-18T14:34:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.4% |
| Market draw away odds | 1.45 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:33:36Z |
| Market reference draw away last update utc | 2026-10-18T14:34:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 67.4% |
| Market home away odds | 1.41 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:33:36Z |
| Market reference home away last update utc | 2026-10-18T14:34:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.50 |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home away odds | 1.43 |
| Market p over 1 5 | 63.8% |
| Market reference over 1 5 odds | 1.53 |
| Market reference over 1 5 opposite odds | 2.61 |
| Market reference over 1 5 last update utc | 2026-10-18T14:33:56Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 83.8% |
| Market reference under 3 5 odds | 1.18 |
| Market reference under 3 5 opposite odds | 5.50 |
| Market reference under 3 5 last update utc | 2026-10-18T14:33:38Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 45.0% |
| Market btts yes odds | 2.07 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:36Z |
| Market reference btts yes odds | 2.13 |
| Market reference btts yes opposite odds | 1.76 |
| Market reference btts yes last update utc | 2026-10-18T14:34:05Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **44.2%**. Expected goals are 1.24 for Levante and 1.54 for Athletic Bilbao (2.78 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 52.2%; Under 3.5 goals: 69.7%; Double Chance 1X: 55.8%; Double Chance X2: 70.9%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 29.1% | 3.43 |
| Draw | 26.7% | 3.75 |
| Athletic Bilbao win | 44.2% | 2.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.24 |
| Athletic Bilbao expected goals | 1.54 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 52.2% |
| Under 2.5 | 47.8% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.61% |
| 2 | 0-1 | 9.37% |
| 3 | 1-2 | 9.16% |
| 4 | 0-2 | 7.39% |
| 5 | 1-0 | 7.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 29.1% | 27.8% | 3.52 | +2.5% |
| Draw | 26.7% | 27.8% | 3.52 | -6.2% |
| Athletic Bilbao win | 44.2% | 44.4% | 2.24 | -0.9% |
| Over 2.5 | 52.2% | 48.6% | 2.02 | +5.5% |
| Under 2.5 | 47.8% | 51.4% | 1.92 | -8.2% |

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
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2403 |
| Dc lambda away | 1.5395 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.89 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.76 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 30.5% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 76.8% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 56.1% |
| P home draw | 55.8% |
| P draw away | 70.9% |
| P home away | 73.3% |
| Raw p home draw | 56.0% |
| Raw p draw away | 69.5% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.42 |
| Reference draw odds | 3.42 |
| Reference away odds | 2.18 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:36Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:36Z |
| Home probability edge | +1.3% |
| Draw probability edge | -1.1% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Raw edge prob home | 0.0267 |
| Raw ev home | 0.0721 |
| Raw edge prob draw | -0.0228 |
| Raw ev draw | -0.1018 |
| Raw edge prob away | -0.0039 |
| Raw ev away | -0.0138 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **57.5%**. Expected goals are 1.63 for Alavés and 0.60 for Málaga (2.23 combined). The most likely exact score is 1-0 at 16.0%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 37.9%; Under 3.5 goals: 81.8%; Double Chance 1X: 82.8%; Double Chance X2: 42.5%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 92.6%; BTTS Yes (both teams score): 37.0%; BTTS No (at least one team does not score): 63.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 57.5% | 1.74 |
| Draw | 25.3% | 3.96 |
| Málaga win | 17.2% | 5.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.63 |
| Málaga expected goals | 0.60 |
| Expected total goals | 2.23 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 64.7% |
| Under 1.5 | 35.3% |
| Over 2.5 | 37.9% |
| Under 2.5 | 62.1% |
| Over 3.5 | 18.2% |
| Under 3.5 | 81.8% |
| Over 4.5 | 7.4% |
| Under 4.5 | 92.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.99% |
| 2 | 2-0 | 13.17% |
| 3 | 0-0 | 11.24% |
| 4 | 1-1 | 11.06% |
| 5 | 0-1 | 8.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 57.5% | 52.9% | 1.89 | +8.7% |
| Draw | 25.3% | 26.0% | 3.73 | -5.7% |
| Málaga win | 17.2% | 21.1% | 4.57 | -21.5% |
| Over 2.5 | 37.9% | 47.3% | 2.07 | -21.6% |
| Under 2.5 | 62.1% | 52.7% | 1.88 | +16.8% |

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
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6283 |
| Dc lambda away | 0.6041 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 37.0% |
| P btts no | 63.0% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.90 |
| Fair Over 1.5 odds | 1.55 |
| Fair Under 1.5 odds | 2.83 |
| Fair Over 2.5 odds | 2.64 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.51 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.59 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 62.1% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 36.6% |
| P home draw | 82.8% |
| P draw away | 42.5% |
| P home away | 74.7% |
| Raw p home draw | 86.7% |
| Raw p draw away | 37.9% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.84 |
| Reference draw odds | 3.64 |
| Reference away odds | 4.45 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.01 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:36Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:36Z |
| Home probability edge | +4.6% |
| Draw probability edge | -0.7% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | 0.0918 |
| Raw ev home | 0.1741 |
| Raw edge prob draw | -0.0141 |
| Raw ev draw | -0.0832 |
| Raw edge prob away | -0.0777 |
| Raw ev away | -0.3922 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **73.7%**. Expected goals are 2.28 for Atlético Madrid and 0.89 for Deportivo La Coruña (3.17 combined). The most likely exact score is 2-0 at 11.7%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 62.5%; Under 3.5 goals: 60.1%; Double Chance 1X: 90.1%; Double Chance X2: 26.3%; Double Chance 12 (either team wins): 83.6%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 52.2%; BTTS No (at least one team does not score): 47.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 73.7% | 1.36 |
| Draw | 16.4% | 6.08 |
| Deportivo La Coruña win | 9.9% | 10.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.28 |
| Deportivo La Coruña expected goals | 0.89 |
| Expected total goals | 3.17 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 62.5% |
| Under 2.5 | 37.5% |
| Over 3.5 | 39.9% |
| Under 3.5 | 60.1% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.74% |
| 2 | 2-1 | 10.44% |
| 3 | 1-0 | 10.12% |
| 4 | 3-0 | 8.93% |
| 5 | 3-1 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 73.7% | 78.8% | 1.27 | -6.4% |
| Draw | 16.4% | 14.4% | 6.46 | +6.2% |
| Deportivo La Coruña win | 9.9% | 6.8% | 13.10 | +29.4% |

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
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2806 |
| Dc lambda away | 0.8894 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 52.2% |
| P btts no | 47.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.75 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.98 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.52 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 68.5% |
| Unadjusted draw probability | 18.5% |
| Unadjusted away-win probability | 13.0% |
| Raw p over 1 5 | 82.6% |
| Raw p under 3 5 | 60.9% |
| Raw p btts yes | 53.1% |
| P home draw | 90.1% |
| P draw away | 26.3% |
| P home away | 83.6% |
| Raw p home draw | 87.0% |
| Raw p draw away | 31.5% |
| Raw p home away | 81.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.25 |
| Reference draw odds | 6.15 |
| Reference away odds | 12.50 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.60 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:55Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:55Z |
| Home probability edge | -5.1% |
| Draw probability edge | +2.0% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.1028 |
| Raw ev home | -0.1295 |
| Raw edge prob draw | 0.0406 |
| Raw ev draw | 0.1934 |
| Raw edge prob away | 0.0622 |
| Raw ev away | 0.7013 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **51.8%**. Expected goals are 1.40 for Rayo Vallecano and 0.90 for Elche CF (2.29 combined). The most likely exact score is 1-0 at 14.9%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 40.9%; Under 3.5 goals: 79.8%; Double Chance 1X: 78.0%; Double Chance X2: 48.2%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 44.4%; BTTS No (at least one team does not score): 55.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 51.8% | 1.93 |
| Draw | 26.2% | 3.82 |
| Elche CF win | 22.0% | 4.54 |

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
| Over 2.5 | 40.9% |
| Under 2.5 | 59.1% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.86% |
| 2 | 1-1 | 12.13% |
| 3 | 2-0 | 10.55% |
| 4 | 0-0 | 9.72% |
| 5 | 2-1 | 9.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 51.8% | 55.4% | 1.81 | -6.2% |
| Draw | 26.2% | 24.5% | 3.94 | +3.0% |
| Elche CF win | 22.0% | 20.1% | 4.78 | +5.2% |
| Over 2.5 | 40.9% | 52.7% | 1.88 | -23.1% |
| Under 2.5 | 59.1% | 47.3% | 2.07 | +22.4% |

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
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
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
| Dc lambda away | 0.8984 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.4% |
| P btts no | 55.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.28 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.45 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.96 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.77 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 44.8% |
| P home draw | 78.0% |
| P draw away | 48.2% |
| P home away | 73.8% |
| Raw p home draw | 76.0% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.76 |
| Reference draw odds | 3.84 |
| Reference away odds | 4.65 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.01 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:36Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:36Z |
| Home probability edge | -3.6% |
| Draw probability edge | +1.6% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -11.8% |
| Under 2.5 probability edge | +11.8% |
| Raw edge prob home | -0.0714 |
| Raw ev home | -0.1264 |
| Raw edge prob draw | 0.0326 |
| Raw ev draw | 0.0945 |
| Raw edge prob away | 0.0388 |
| Raw ev away | 0.1452 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Espanyol win** at **39.6%**. Expected goals are 1.91 for Real Racing Club de Santander and 2.13 for Espanyol (4.04 combined). The most likely exact score is 1-1 at 8.3%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 76.0%; Under 3.5 goals: 42.7%; Double Chance 1X: 60.4%; Double Chance X2: 63.1%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 62.8%; BTTS Yes (both teams score): 75.7%; BTTS No (at least one team does not score): 24.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 36.9% | 2.71 |
| Draw | 23.5% | 4.26 |
| Espanyol win | 39.6% | 2.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.91 |
| Espanyol expected goals | 2.13 |
| Expected total goals | 4.04 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 76.0% |
| Under 2.5 | 24.0% |
| Over 3.5 | 57.3% |
| Under 3.5 | 42.7% |
| Over 4.5 | 37.2% |
| Under 4.5 | 62.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.27% |
| 2 | 2-2 | 8.24% |
| 3 | 2-1 | 7.15% |
| 4 | 1-2 | 6.88% |
| 5 | 1-3 | 4.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 36.9% | 38.6% | 2.57 | -5.1% |
| Draw | 23.5% | 26.2% | 3.71 | -12.8% |
| Espanyol win | 39.6% | 35.2% | 2.80 | +10.8% |
| Over 2.5 | 76.0% | 55.9% | 1.77 | +34.5% |
| Under 2.5 | 24.0% | 44.1% | 2.22 | -46.7% |

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
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9051 |
| Dc lambda away | 2.1322 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 75.7% |
| P btts no | 24.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.45 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.37 |
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
| Raw p btts yes | 75.2% |
| P home draw | 60.4% |
| P draw away | 63.1% |
| P home away | 76.5% |
| Raw p home draw | 56.0% |
| Raw p draw away | 64.7% |
| Raw p home away | 79.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.50 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.73 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:36Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:36Z |
| Home probability edge | -1.6% |
| Draw probability edge | -2.7% |
| Away probability edge | +4.4% |
| Over 2.5 probability edge | +20.0% |
| Under 2.5 probability edge | -20.0% |
| Raw edge prob home | -0.0330 |
| Raw ev home | -0.0936 |
| Raw edge prob draw | -0.0549 |
| Raw ev draw | -0.2300 |
| Raw edge prob away | 0.0878 |
| Raw ev away | 0.2313 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **44.2%**. Expected goals are 1.27 for Valencia and 1.51 for Villarreal (2.78 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.6%; Double Chance 1X: 55.8%; Double Chance X2: 69.9%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.1% | 3.32 |
| Draw | 25.7% | 3.89 |
| Villarreal win | 44.2% | 2.26 |

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
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.16% |
| 2 | 0-1 | 9.50% |
| 3 | 1-2 | 9.33% |
| 4 | 0-2 | 7.33% |
| 5 | 1-0 | 7.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.1% | 28.3% | 3.45 | +3.8% |
| Draw | 25.7% | 25.7% | 3.78 | -2.9% |
| Villarreal win | 44.2% | 45.9% | 2.17 | -4.1% |
| Over 2.5 | 52.6% | 55.6% | 1.78 | -6.5% |
| Under 2.5 | 47.4% | 44.4% | 2.20 | +4.4% |

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
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2725 |
| Dc lambda away | 1.5058 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.49 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.71 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.2% |
| P home draw | 55.8% |
| P draw away | 69.9% |
| P home away | 74.3% |
| Raw p home draw | 57.5% |
| Raw p draw away | 68.1% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.36 |
| Reference draw odds | 3.68 |
| Reference away odds | 2.11 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:36Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:36Z |
| Home probability edge | +1.8% |
| Draw probability edge | -0.0% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | 0.0357 |
| Raw ev home | 0.0997 |
| Raw edge prob draw | -0.0009 |
| Raw ev draw | -0.0303 |
| Raw edge prob away | -0.0348 |
| Raw ev away | -0.0784 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **55.5%**. Expected goals are 1.27 for Athletic Bilbao and 0.62 for Getafe (1.89 combined). The most likely exact score is 1-0 at 20.3%. Goal-market probabilities: at least one goal: 86.3%; Over 2.5 goals: 30.4%; Under 3.5 goals: 87.4%; Double Chance 1X: 82.5%; Double Chance X2: 44.5%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 95.5%; BTTS Yes (both teams score): 32.8%; BTTS No (at least one team does not score): 67.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 55.5% | 1.80 |
| Draw | 27.0% | 3.71 |
| Getafe win | 17.5% | 5.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.27 |
| Getafe expected goals | 0.62 |
| Expected total goals | 1.89 |
| Over 0.5 | 86.3% |
| Under 0.5 | 13.7% |
| Over 1.5 | 57.1% |
| Under 1.5 | 42.9% |
| Over 2.5 | 30.4% |
| Under 2.5 | 69.6% |
| Over 3.5 | 12.6% |
| Under 3.5 | 87.4% |
| Over 4.5 | 4.5% |
| Under 4.5 | 95.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.25% |
| 2 | 0-0 | 13.74% |
| 3 | 2-0 | 12.97% |
| 4 | 1-1 | 10.90% |
| 5 | 0-1 | 8.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 55.5% | 59.2% | 1.70 | -5.6% |
| Draw | 27.0% | 23.8% | 4.04 | +8.9% |
| Getafe win | 17.5% | 17.0% | 5.60 | -1.7% |
| Over 2.5 | 30.4% | 43.0% | 2.27 | -31.0% |
| Under 2.5 | 69.6% | 57.0% | 1.74 | +21.1% |

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
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2652 |
| Dc lambda away | 0.6243 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 32.8% |
| P btts no | 67.2% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.28 |
| Fair Over 1.5 odds | 1.75 |
| Fair Under 1.5 odds | 2.33 |
| Fair Over 2.5 odds | 3.29 |
| Fair Under 2.5 odds | 1.44 |
| Fair Over 3.5 odds | 7.93 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 22.14 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 51.8% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 18.1% |
| Raw p over 1 5 | 56.6% |
| Raw p under 3 5 | 87.6% |
| Raw p btts yes | 33.6% |
| P home draw | 82.5% |
| P draw away | 44.5% |
| P home away | 73.0% |
| Raw p home draw | 81.9% |
| Raw p draw away | 48.2% |
| Raw p home away | 69.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.65 |
| Reference draw odds | 3.94 |
| Reference away odds | 5.45 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.69 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:36Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:36Z |
| Home probability edge | -3.7% |
| Draw probability edge | +3.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | -0.0743 |
| Raw ev home | -0.1197 |
| Raw edge prob draw | 0.0626 |
| Raw ev draw | 0.2154 |
| Raw edge prob away | 0.0117 |
| Raw ev away | 0.0154 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **56.5%**. Expected goals are 1.78 for Barcelona and 1.33 for Real Madrid (3.11 combined). The most likely exact score is 2-1 at 11.1%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 61.3%; Under 3.5 goals: 61.8%; Double Chance 1X: 77.0%; Double Chance X2: 43.5%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 79.0%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 56.5% | 1.77 |
| Draw | 20.5% | 4.88 |
| Real Madrid win | 23.0% | 4.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.78 |
| Real Madrid expected goals | 1.33 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 82.2% |
| Under 1.5 | 17.8% |
| Over 2.5 | 61.3% |
| Under 2.5 | 38.7% |
| Over 3.5 | 38.2% |
| Under 3.5 | 61.8% |
| Over 4.5 | 21.0% |
| Under 4.5 | 79.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.12% |
| 2 | 1-1 | 9.36% |
| 3 | 1-0 | 9.16% |
| 4 | 2-0 | 8.34% |
| 5 | 3-1 | 6.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 56.5% | 65.4% | 1.54 | -12.9% |
| Draw | 20.5% | 17.4% | 5.44 | +11.6% |
| Real Madrid win | 23.0% | 17.2% | 5.49 | +26.1% |

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
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7753 |
| Dc lambda away | 1.3333 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.66 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.61 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.62 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.76 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 47.7% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 28.7% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 61.4% |
| P home draw | 77.0% |
| P draw away | 43.5% |
| P home away | 79.5% |
| Raw p home draw | 71.3% |
| Raw p draw away | 52.3% |
| Raw p home away | 76.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.50 |
| Reference draw odds | 5.30 |
| Reference away odds | 5.35 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.23 |
| Reference Under 2.5 odds | 4.23 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:56Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:56Z |
| Home probability edge | -8.8% |
| Draw probability edge | +3.1% |
| Away probability edge | +5.7% |
| Over 2.5 probability edge | -18.3% |
| Under 2.5 probability edge | +18.3% |
| Raw edge prob home | -0.1768 |
| Raw ev home | -0.2656 |
| Raw edge prob draw | 0.0621 |
| Raw ev draw | 0.2845 |
| Raw edge prob away | 0.1147 |
| Raw ev away | 0.5756 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **36.6%**. Expected goals are 1.33 for Celta Vigo and 1.28 for Real Betis (2.61 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.3%; Under 3.5 goals: 73.4%; Double Chance 1X: 63.7%; Double Chance X2: 63.4%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 53.4%; BTTS No (at least one team does not score): 46.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 36.6% | 2.73 |
| Draw | 27.1% | 3.69 |
| Real Betis win | 36.3% | 2.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.33 |
| Real Betis expected goals | 1.28 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.3% |
| Under 2.5 | 51.7% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.89% |
| 2 | 0-1 | 9.38% |
| 3 | 1-0 | 9.26% |
| 4 | 1-2 | 8.20% |
| 5 | 2-1 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 36.6% | 35.6% | 2.77 | +1.5% |
| Draw | 27.1% | 27.4% | 3.57 | -3.3% |
| Real Betis win | 36.3% | 37.0% | 2.67 | -3.1% |
| Over 2.5 | 48.3% | 51.7% | 1.91 | -7.7% |
| Under 2.5 | 51.7% | 48.3% | 2.03 | +4.9% |

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
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3279 |
| Dc lambda away | 1.2828 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.4% |
| P btts no | 46.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.04 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.08 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 37.7% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 53.4% |
| P home draw | 63.7% |
| P draw away | 63.4% |
| P home away | 72.9% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.3% |
| Raw p home away | 73.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.70 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:36Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:36Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0205 |
| Raw ev home | 0.0431 |
| Raw edge prob draw | -0.0056 |
| Raw ev draw | -0.0433 |
| Raw edge prob away | -0.0149 |
| Raw ev away | -0.0509 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **58.3%**. Expected goals are 2.01 for Real Sociedad and 1.04 for Levante (3.05 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 58.5%; Under 3.5 goals: 63.7%; Double Chance 1X: 80.4%; Double Chance X2: 41.7%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 56.4%; BTTS No (at least one team does not score): 43.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 58.3% | 1.72 |
| Draw | 22.1% | 4.52 |
| Levante win | 19.6% | 5.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 2.01 |
| Levante expected goals | 1.04 |
| Expected total goals | 3.05 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 58.5% |
| Under 2.5 | 41.5% |
| Over 3.5 | 36.3% |
| Under 3.5 | 63.7% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.34% |
| 2 | 2-1 | 9.75% |
| 3 | 2-0 | 9.34% |
| 4 | 1-0 | 9.13% |
| 5 | 3-1 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 58.3% | 57.1% | 1.76 | +2.6% |
| Draw | 22.1% | 22.6% | 4.26 | -5.8% |
| Levante win | 19.6% | 20.3% | 4.72 | -7.4% |
| Over 2.5 | 58.5% | 58.1% | 1.71 | +0.1% |
| Under 2.5 | 41.5% | 41.9% | 2.32 | -3.8% |

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
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0053 |
| Dc lambda away | 1.0441 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.84 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.21 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 59.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 18.9% |
| Raw p over 1 5 | 81.0% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 56.3% |
| P home draw | 80.4% |
| P draw away | 41.7% |
| P home away | 77.9% |
| Raw p home draw | 81.1% |
| Raw p draw away | 40.6% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.71 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:36Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:36Z |
| Home probability edge | +1.2% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0236 |
| Raw ev home | 0.0463 |
| Raw edge prob draw | -0.0099 |
| Raw ev draw | -0.0793 |
| Raw edge prob away | -0.0136 |
| Raw ev away | -0.1060 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **49.0%**. Expected goals are 1.48 for Sevilla and 0.98 for CA Osasuna (2.46 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.5%; Double Chance 1X: 75.9%; Double Chance X2: 51.0%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 49.0% | 2.04 |
| Draw | 26.9% | 3.72 |
| CA Osasuna win | 24.1% | 4.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.48 |
| CA Osasuna expected goals | 0.98 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 70.7% |
| Under 1.5 | 29.3% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.72% |
| 2 | 1-0 | 12.50% |
| 3 | 2-0 | 9.44% |
| 4 | 2-1 | 9.25% |
| 5 | 0-0 | 8.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 49.0% | 49.3% | 2.02 | -1.1% |
| Draw | 26.9% | 27.1% | 3.60 | -3.2% |
| CA Osasuna win | 24.1% | 23.6% | 4.11 | -0.8% |
| Over 2.5 | 44.6% | 44.7% | 2.19 | -2.3% |
| Under 2.5 | 55.4% | 55.3% | 1.79 | -0.8% |

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
| Market best home last update utc | 2026-10-18T14:33:36Z |
| Market best draw last update utc | 2026-10-18T14:33:36Z |
| Market best away last update utc | 2026-10-18T14:33:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.4831 |
| Dc lambda away | 0.9791 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:05.367220+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.32 |
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
| P home draw | 75.9% |
| P draw away | 51.0% |
| P home away | 73.1% |
| Raw p home draw | 75.3% |
| Raw p draw away | 51.4% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.97 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-18T14:33:58Z |
| Market reference home last update utc | 2026-10-18T14:33:58Z |
| Market reference draw last update utc | 2026-10-18T14:33:58Z |
| Market reference away last update utc | 2026-10-18T14:33:58Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:58Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:36Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:36Z |
| Home probability edge | -0.4% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0070 |
| Raw ev home | -0.0178 |
| Raw edge prob draw | -0.0043 |
| Raw ev draw | -0.0401 |
| Raw edge prob away | 0.0114 |
| Raw ev away | 0.0157 |

</details>


---
