# UEFA Champions League — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 530 |
| Training data through | 2026-10-13 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1567.505 |
| Base scoring parameter | 0.159 |
| Home-advantage parameter | 0.286 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0 |
| Training data health | {'completed_matches': 27, 'latest_completed_utc': '2026-10-13T19:00:00+00:00', 'latest_completed_date': '2026-10-13', 'next_fixture_utc': '2026-10-14T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-14T09:46:21.767703+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'a7f09a11287058dc6c944f9931d177bbe8e8a36195a4f7edd862b7f91e59df89', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0006662741666666667, 'training_end': '2026-10-13', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Additional event odds calls used before this league | 4.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **48.5%**. Expected goals are 1.22 for AS Roma and 1.64 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 54.2%; Under 3.5 goals: 67.9%; Double Chance 1X: 51.5%; Double Chance X2: 72.6%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 56.4%; BTTS No (at least one team does not score): 43.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 27.4% | 3.65 |
| Draw | 24.0% | 4.16 |
| Real Madrid win | 48.5% | 2.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.22 |
| Real Madrid expected goals | 1.64 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 54.2% |
| Under 2.5 | 45.8% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.28% |
| 2 | 0-1 | 10.16% |
| 3 | 1-2 | 9.55% |
| 4 | 0-2 | 7.84% |
| 5 | 1-0 | 7.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 27.4% | 25.8% | 3.72 | +2.0% |
| Draw | 24.0% | 24.8% | 4.09 | -1.7% |
| Real Madrid win | 48.5% | 49.3% | 1.99 | -3.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | d4ef112438afa4c2cdbbfc9376a009c9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T09:44:35Z |
| Market best draw last update utc | 2026-10-14T09:44:35Z |
| Market best away last update utc | 2026-10-14T09:44:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.67 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.12 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.24 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 29.0% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 47.7% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.0% |
| Raw p btts yes | 56.2% |
| P home draw | 51.5% |
| P draw away | 72.6% |
| Raw p home draw | 52.3% |
| Raw p draw away | 71.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.85 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.02 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Home probability edge | +1.6% |
| Draw probability edge | -0.8% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -13.3% |
| Under 2.5 probability edge | +13.3% |
| Raw edge prob home | 0.0321 |
| Raw ev home | 0.0797 |
| Raw edge prob draw | -0.0160 |
| Raw ev draw | -0.0495 |
| Raw edge prob away | -0.0161 |
| Raw ev away | -0.0500 |
| Market p home draw | 50.2% |
| Market home draw odds | 1.91 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T09:44:35Z |
| Market reference home draw last update utc | 2026-10-14T09:46:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.0% |
| Market draw away odds | 1.32 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T09:44:35Z |
| Market reference draw away last update utc | 2026-10-14T09:46:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home draw odds | 1.93 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 86.7% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T09:42:36Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.3% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T09:42:36Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.11 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.41 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T09:44:35Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 2.97 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **65.9%**. Expected goals are 2.20 for Aston Villa and 0.60 for Fenerbahce (2.79 combined). The most likely exact score is 2-0 at 13.0%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.0%; Double Chance 1X: 85.8%; Double Chance X2: 34.1%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 41.0%; BTTS No (at least one team does not score): 59.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 65.9% | 1.52 |
| Draw | 20.0% | 5.01 |
| Fenerbahce win | 14.2% | 7.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.20 |
| Fenerbahce expected goals | 0.60 |
| Expected total goals | 2.79 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 74.4% |
| Under 1.5 | 25.6% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 29.0% |
| Under 3.5 | 71.0% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.05% |
| 2 | 1-0 | 12.24% |
| 3 | 3-0 | 9.55% |
| 4 | 1-1 | 9.28% |
| 5 | 2-1 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 65.9% | 57.2% | 1.74 | +14.6% |
| Draw | 20.0% | 23.5% | 4.21 | -16.0% |
| Fenerbahce win | 14.2% | 19.3% | 4.93 | -30.1% |
| Over 2.5 | 50.4% | 61.6% | 1.63 | -17.9% |
| Under 2.5 | 49.6% | 38.4% | 2.49 | +23.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 3f3cb74e560dfcc3e795b667ed9ebdef |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T09:44:35Z |
| Market best draw last update utc | 2026-10-14T09:44:35Z |
| Market best away last update utc | 2026-10-14T09:44:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 41.0% |
| P btts no | 59.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.36 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.91 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.45 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.13 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 74.6% |
| Unadjusted draw probability | 16.4% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 76.4% |
| Raw p under 3 5 | 69.4% |
| Raw p btts yes | 39.6% |
| P home draw | 85.8% |
| P draw away | 34.1% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.74 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.10 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.44 |
| Home probability edge | +8.7% |
| Draw probability edge | -3.5% |
| Away probability edge | -5.1% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | 0.1737 |
| Raw ev home | 0.2972 |
| Raw edge prob draw | -0.0710 |
| Raw ev draw | -0.3094 |
| Raw edge prob away | -0.1028 |
| Raw ev away | -0.5542 |
| Market p home draw | 80.4% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T09:44:35Z |
| Market reference home draw last update utc | 2026-10-14T09:46:03Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.6% |
| Market draw away odds | 2.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T09:44:35Z |
| Market reference draw away last update utc | 2026-10-14T09:46:03Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.23 |
| Market reference dc home draw odds | 1.21 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T09:45:56Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.0% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T09:45:56Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.45 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.8% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T09:44:35Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.49 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **44.0%**. Expected goals are 1.71 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.65 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 70.1%; Under 3.5 goals: 50.4%; Double Chance 1X: 56.0%; Double Chance X2: 66.8%; Under 4.5 goals: 70.0%; BTTS Yes (both teams score): 70.2%; BTTS No (at least one team does not score): 29.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 33.2% | 3.01 |
| Draw | 22.7% | 4.40 |
| Borussia Dortmund win | 44.0% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 1.71 |
| Borussia Dortmund expected goals | 1.94 |
| Expected total goals | 3.65 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 87.6% |
| Under 1.5 | 12.4% |
| Over 2.5 | 70.1% |
| Under 2.5 | 29.9% |
| Over 3.5 | 49.6% |
| Under 3.5 | 50.4% |
| Over 4.5 | 30.0% |
| Under 4.5 | 70.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.96% |
| 2 | 1-2 | 8.33% |
| 3 | 2-2 | 7.83% |
| 4 | 2-1 | 7.00% |
| 5 | 0-1 | 5.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 33.2% | 31.4% | 3.15 | +4.7% |
| Draw | 22.7% | 24.7% | 4.05 | -8.0% |
| Borussia Dortmund win | 44.0% | 43.9% | 2.22 | -2.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | ca87a3874b0eae31b4173ae4a9324957 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T09:44:35Z |
| Market best draw last update utc | 2026-10-14T09:44:35Z |
| Market best away last update utc | 2026-10-14T09:44:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.2% |
| P btts no | 29.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.20 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.04 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.35 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.34 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 44.2% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 50.4% |
| Raw p btts yes | 69.7% |
| P home draw | 56.0% |
| P draw away | 66.8% |
| Raw p home draw | 55.8% |
| Raw p draw away | 64.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.15 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.26 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.08 |
| Home probability edge | +1.8% |
| Draw probability edge | -2.0% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.0366 |
| Raw ev home | 0.1048 |
| Raw edge prob draw | -0.0390 |
| Raw ev draw | -0.1586 |
| Raw edge prob away | 0.0024 |
| Raw ev away | -0.0198 |
| Market p home draw | 56.4% |
| Market home draw odds | 1.74 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T09:44:35Z |
| Market reference home draw last update utc | 2026-10-14T09:46:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.3% |
| Market draw away odds | 1.41 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T09:44:35Z |
| Market reference draw away last update utc | 2026-10-14T09:46:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home draw odds | 1.72 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 91.2% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T09:46:08Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 5.90 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.2% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T09:46:08Z |
| Market reference under 3 5 odds | 1.91 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.1% |
| Market btts yes odds | 1.34 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T09:44:35Z |
| Market reference btts yes odds | 1.42 |
| Market reference btts yes opposite odds | 3.30 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **60.2%**. Expected goals are 1.86 for Feyenoord and 4.03 for Como (5.89 combined). The most likely exact score is 2-2 at 6.3%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 91.9%; Under 3.5 goals: 17.5%; Double Chance 1X: 39.8%; Double Chance X2: 78.5%; Under 4.5 goals: 32.9%; BTTS Yes (both teams score): 84.8%; BTTS No (at least one team does not score): 15.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 21.5% | 4.65 |
| Draw | 18.3% | 5.45 |
| Como win | 60.2% | 1.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 1.86 |
| Como expected goals | 4.03 |
| Expected total goals | 5.89 |
| Over 0.5 | 99.7% |
| Under 0.5 | 0.3% |
| Over 1.5 | 97.7% |
| Under 1.5 | 2.3% |
| Over 2.5 | 91.9% |
| Under 2.5 | 8.1% |
| Over 3.5 | 82.5% |
| Under 3.5 | 17.5% |
| Over 4.5 | 67.1% |
| Under 4.5 | 32.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.29% |
| 2 | 3-3 | 5.23% |
| 3 | 1-4 | 4.52% |
| 4 | 1-3 | 4.49% |
| 5 | 2-4 | 4.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 21.5% | 30.0% | 3.27 | -29.7% |
| Draw | 18.3% | 25.3% | 3.96 | -27.4% |
| Como win | 60.2% | 44.7% | 2.19 | +31.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T16:45:00+00:00 |
| Fixture id | 5d6f9accd6f79ae4216dfd29ccc342b2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T09:44:35Z |
| Market best draw last update utc | 2026-10-14T09:44:35Z |
| Market best away last update utc | 2026-10-14T09:44:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 84.8% |
| P btts no | 15.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 355.25 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 43.79 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 12.39 |
| Fair Over 3.5 odds | 1.21 |
| Fair Under 3.5 odds | 5.71 |
| Fair Over 4.5 odds | 1.49 |
| Fair Under 4.5 odds | 3.04 |
| Unadjusted home-win probability | 13.0% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 75.6% |
| Raw p over 1 5 | 98.0% |
| Raw p under 3 5 | 16.2% |
| Raw p btts yes | 82.8% |
| P home draw | 39.8% |
| P draw away | 78.5% |
| Raw p home draw | 24.4% |
| Raw p draw away | 87.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.30 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.22 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -8.5% |
| Draw probability edge | -7.0% |
| Away probability edge | +15.5% |
| Over 2.5 probability edge | +27.3% |
| Under 2.5 probability edge | -27.3% |
| Raw edge prob home | -0.1697 |
| Raw ev home | -0.5748 |
| Raw edge prob draw | -0.1396 |
| Raw ev draw | -0.5501 |
| Raw edge prob away | 0.3092 |
| Raw ev away | 0.6564 |
| Market p home draw | 54.7% |
| Market home draw odds | 1.76 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T09:44:35Z |
| Market reference home draw last update utc | 2026-10-14T09:46:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.2% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T09:44:35Z |
| Market reference draw away last update utc | 2026-10-14T09:46:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home draw odds | 1.77 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 87.3% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T09:46:12Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.5% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T09:46:12Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.31 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.0% |
| Market btts yes odds | 1.43 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T09:44:35Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 2.86 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **68.5%**. Expected goals are 0.29 for LASK and 1.41 for Liverpool (1.70 combined). The most likely exact score is 0-1 at 26.9%. Goal-market probabilities: at least one goal: 85.0%; Over 2.5 goals: 25.3%; Under 3.5 goals: 90.4%; Double Chance 1X: 31.5%; Double Chance X2: 90.2%; Under 4.5 goals: 96.9%; BTTS Yes (both teams score): 18.3%; BTTS No (at least one team does not score): 81.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 9.8% | 10.20 |
| Draw | 21.7% | 4.61 |
| Liverpool win | 68.5% | 1.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.29 |
| Liverpool expected goals | 1.41 |
| Expected total goals | 1.70 |
| Over 0.5 | 85.0% |
| Under 0.5 | 15.0% |
| Over 1.5 | 51.0% |
| Under 1.5 | 49.0% |
| Over 2.5 | 25.3% |
| Under 2.5 | 74.7% |
| Over 3.5 | 9.6% |
| Under 3.5 | 90.4% |
| Over 4.5 | 3.1% |
| Under 4.5 | 96.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 26.90% |
| 2 | 0-2 | 18.68% |
| 3 | 0-0 | 14.98% |
| 4 | 0-3 | 8.78% |
| 5 | 1-0 | 7.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 9.8% | 11.7% | 7.70 | -24.5% |
| Draw | 21.7% | 17.6% | 5.48 | +18.9% |
| Liverpool win | 68.5% | 70.7% | 1.42 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T16:45:00+00:00 |
| Fixture id | 2903ee092f7e08c549b130a3d394ac3c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T09:44:35Z |
| Market best draw last update utc | 2026-10-14T09:44:35Z |
| Market best away last update utc | 2026-10-14T09:44:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 18.3% |
| P btts no | 81.7% |
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.68 |
| Fair Over 1.5 odds | 1.96 |
| Fair Under 1.5 odds | 2.04 |
| Fair Over 2.5 odds | 3.95 |
| Fair Under 2.5 odds | 1.34 |
| Fair Over 3.5 odds | 10.44 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 32.25 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 7.9% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 66.3% |
| Raw p over 1 5 | 50.4% |
| Raw p under 3 5 | 90.6% |
| Raw p btts yes | 18.9% |
| P home draw | 31.5% |
| P draw away | 90.2% |
| Raw p home draw | 33.7% |
| Raw p draw away | 92.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 8.40 |
| Reference draw odds | 5.60 |
| Reference away odds | 1.41 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.60 |
| Home probability edge | -1.9% |
| Draw probability edge | +4.1% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -38.9% |
| Under 2.5 probability edge | +38.9% |
| Raw edge prob home | -0.0376 |
| Raw ev home | -0.3898 |
| Raw edge prob draw | 0.0822 |
| Raw ev draw | 0.4145 |
| Raw edge prob away | -0.0445 |
| Raw ev away | -0.0591 |
| Market p home draw | 30.6% |
| Market home draw odds | 3.10 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T09:44:35Z |
| Market reference home draw last update utc | 2026-10-14T09:46:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 87.2% |
| Market draw away odds | 1.10 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T09:44:35Z |
| Market reference draw away last update utc | 2026-10-14T09:46:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.12 |
| Market reference dc home draw odds | 3.19 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 84.3% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T09:41:42Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.4% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T09:41:42Z |
| Market reference under 3 5 odds | 1.67 |
| Market reference under 3 5 opposite odds | 2.31 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.9% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T09:44:35Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.18 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **42.3%**. Expected goals are 1.41 for Manchester City and 2.21 for Paris Saint Germain (3.61 combined). The most likely exact score is 2-1 at 8.8%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 68.8%; Under 3.5 goals: 52.5%; Double Chance 1X: 57.7%; Double Chance X2: 63.6%; Under 4.5 goals: 71.5%; BTTS Yes (both teams score): 67.7%; BTTS No (at least one team does not score): 32.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 36.4% | 2.75 |
| Draw | 21.3% | 4.70 |
| Paris Saint Germain win | 42.3% | 2.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.41 |
| Paris Saint Germain expected goals | 2.21 |
| Expected total goals | 3.61 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 86.4% |
| Under 1.5 | 13.6% |
| Over 2.5 | 68.8% |
| Under 2.5 | 31.2% |
| Over 3.5 | 47.5% |
| Under 3.5 | 52.5% |
| Over 4.5 | 28.5% |
| Under 4.5 | 71.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.77% |
| 2 | 1-1 | 8.71% |
| 3 | 2-2 | 7.10% |
| 4 | 1-2 | 6.96% |
| 5 | 1-0 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 36.4% | 48.4% | 2.06 | -25.0% |
| Draw | 21.3% | 23.1% | 4.21 | -10.3% |
| Paris Saint Germain win | 42.3% | 28.4% | 3.42 | +44.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 5a1a6a04c5561897741105e30d5d7ec4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T09:44:35Z |
| Market best draw last update utc | 2026-10-14T09:44:35Z |
| Market best away last update utc | 2026-10-14T09:44:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.7% |
| P btts no | 32.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.04 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.36 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.10 |
| Fair Under 3.5 odds | 1.91 |
| Fair Over 4.5 odds | 3.50 |
| Fair Under 4.5 odds | 1.40 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 56.1% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 51.3% |
| Raw p btts yes | 66.7% |
| P home draw | 57.7% |
| P draw away | 63.6% |
| Raw p home draw | 43.9% |
| Raw p draw away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.06 |
| Reference draw odds | 4.30 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.87 |
| Home probability edge | -12.0% |
| Draw probability edge | -1.8% |
| Away probability edge | +13.8% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | -0.2400 |
| Raw ev home | -0.4969 |
| Raw edge prob draw | -0.0368 |
| Raw ev draw | -0.1810 |
| Raw edge prob away | 0.2768 |
| Raw ev away | 0.9195 |
| Market p home draw | 71.5% |
| Market home draw odds | 1.36 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T09:44:35Z |
| Market reference home draw last update utc | 2026-10-14T09:46:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.0% |
| Market draw away odds | 1.85 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T09:44:35Z |
| Market reference draw away last update utc | 2026-10-14T09:46:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.87 |
| Market reference dc home draw odds | 1.36 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 87.4% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T09:45:07Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.2% |
| Market under 3 5 odds | 1.83 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T09:45:07Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.6% |
| Market btts yes odds | 1.38 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T09:44:35Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 3.01 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **59.7%**. Expected goals are 3.10 for Real Betis and 1.32 for Porto (4.42 combined). The most likely exact score is 2-2 at 7.3%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 79.4%; Under 3.5 goals: 37.5%; Double Chance 1X: 79.6%; Double Chance X2: 40.3%; Under 4.5 goals: 57.5%; BTTS Yes (both teams score): 72.1%; BTTS No (at least one team does not score): 27.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 59.7% | 1.67 |
| Draw | 19.9% | 5.03 |
| Porto win | 20.4% | 4.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 3.10 |
| Porto expected goals | 1.32 |
| Expected total goals | 4.42 |
| Over 0.5 | 98.6% |
| Under 0.5 | 1.4% |
| Over 1.5 | 92.5% |
| Under 1.5 | 7.5% |
| Over 2.5 | 79.4% |
| Under 2.5 | 20.6% |
| Over 3.5 | 62.5% |
| Under 3.5 | 37.5% |
| Over 4.5 | 42.5% |
| Under 4.5 | 57.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.33% |
| 2 | 1-1 | 6.81% |
| 3 | 3-1 | 6.46% |
| 4 | 2-1 | 6.25% |
| 5 | 4-1 | 5.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 59.7% | 46.5% | 2.16 | +29.0% |
| Draw | 19.9% | 26.0% | 3.76 | -25.3% |
| Porto win | 20.4% | 27.5% | 3.50 | -28.5% |
| Over 2.5 | 79.4% | 56.6% | 1.79 | +42.1% |
| Under 2.5 | 20.6% | 43.4% | 2.19 | -54.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 4c7f87780ae5ab8bec9e83d6d6ec9909 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T09:44:35Z |
| Market best draw last update utc | 2026-10-14T09:44:35Z |
| Market best away last update utc | 2026-10-14T09:44:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 72.1% |
| P btts no | 27.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 71.82 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.39 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.85 |
| Fair Over 3.5 odds | 1.60 |
| Fair Under 3.5 odds | 2.67 |
| Fair Over 4.5 odds | 2.35 |
| Fair Under 4.5 odds | 1.74 |
| Unadjusted home-win probability | 73.0% |
| Unadjusted draw probability | 13.7% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 93.2% |
| Raw p under 3 5 | 35.6% |
| Raw p btts yes | 69.8% |
| P home draw | 79.6% |
| P draw away | 40.3% |
| Raw p home draw | 86.7% |
| Raw p draw away | 27.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.14 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | +13.3% |
| Draw probability edge | -6.2% |
| Away probability edge | -7.1% |
| Over 2.5 probability edge | +22.8% |
| Under 2.5 probability edge | -22.8% |
| Raw edge prob home | 0.2651 |
| Raw ev home | 0.5760 |
| Raw edge prob draw | -0.1235 |
| Raw ev draw | -0.4852 |
| Raw edge prob away | -0.1416 |
| Raw ev away | -0.5330 |
| Market p home draw | 72.4% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T09:44:35Z |
| Market reference home draw last update utc | 2026-10-14T09:46:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.6% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T09:44:35Z |
| Market reference draw away last update utc | 2026-10-14T09:46:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.81 |
| Market reference dc home draw odds | 1.34 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 79.4% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T09:37:43Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.35 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.0% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T09:37:43Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.76 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.2% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T09:44:35Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.40 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **38.8%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.29 for AEK Athens (2.78 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 51.8%; Under 3.5 goals: 69.8%; Double Chance 1X: 65.0%; Double Chance X2: 61.2%; Under 4.5 goals: 85.4%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 38.8% | 2.58 |
| Draw | 26.2% | 3.81 |
| AEK Athens win | 35.0% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.49 |
| AEK Athens expected goals | 1.29 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 51.8% |
| Under 2.5 | 48.2% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.6% |
| Under 4.5 | 85.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.36% |
| 2 | 0-1 | 9.03% |
| 3 | 1-0 | 9.00% |
| 4 | 2-1 | 8.10% |
| 5 | 1-2 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 38.8% | 35.0% | 2.79 | +8.1% |
| Draw | 26.2% | 28.4% | 3.49 | -8.4% |
| AEK Athens win | 35.0% | 36.6% | 2.70 | -5.5% |
| Over 2.5 | 51.8% | 50.7% | 1.95 | +0.9% |
| Under 2.5 | 48.2% | 49.3% | 1.99 | -4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 0f961390e790ad2c80ecb3f302cad4a6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T09:44:35Z |
| Market best draw last update utc | 2026-10-14T09:44:35Z |
| Market best away last update utc | 2026-10-14T09:44:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 67/100 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.28 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.87 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 42.5% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 75.9% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 55.5% |
| P home draw | 65.0% |
| P draw away | 61.2% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.84 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.72 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.94 |
| Home probability edge | +3.7% |
| Draw probability edge | -2.2% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | 0.0746 |
| Raw ev home | 0.1855 |
| Raw edge prob draw | -0.0432 |
| Raw ev draw | -0.1598 |
| Raw edge prob away | -0.0314 |
| Raw ev away | -0.0972 |
| Market p home draw | 63.6% |
| Market home draw odds | 1.53 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T09:44:35Z |
| Market reference home draw last update utc | 2026-10-14T09:46:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.9% |
| Market draw away odds | 1.50 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T09:44:35Z |
| Market reference draw away last update utc | 2026-10-14T09:46:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.49 |
| Market reference dc home draw odds | 1.52 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 77.3% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T09:43:50Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.95 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.9% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T09:43:50Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.18 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.0% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T09:44:35Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.28 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **67.4%**. Expected goals are 1.37 for ŠK Slovan Bratislava and 2.33 for VfB Stuttgart (3.70 combined). The most likely exact score is 1-2 at 10.5%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 72.3%; Under 3.5 goals: 48.6%; Double Chance 1X: 32.6%; Double Chance X2: 84.3%; Under 4.5 goals: 68.0%; BTTS Yes (both teams score): 66.1%; BTTS No (at least one team does not score): 33.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 15.7% | 6.38 |
| Draw | 16.9% | 5.90 |
| VfB Stuttgart win | 67.4% | 1.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.37 |
| VfB Stuttgart expected goals | 2.33 |
| Expected total goals | 3.70 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 72.3% |
| Under 2.5 | 27.7% |
| Over 3.5 | 51.4% |
| Under 3.5 | 48.6% |
| Over 4.5 | 32.0% |
| Under 4.5 | 68.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.45% |
| 2 | 1-3 | 8.12% |
| 3 | 0-2 | 7.63% |
| 4 | 0-1 | 7.00% |
| 5 | 1-1 | 6.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 15.7% | 9.2% | 10.00 | +56.6% |
| Draw | 16.9% | 15.3% | 6.48 | +9.8% |
| VfB Stuttgart win | 67.4% | 75.5% | 1.31 | -11.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | d7576351b8cb2396e32cc3de0446f3de |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T09:44:35Z |
| Market best draw last update utc | 2026-10-14T09:44:35Z |
| Market best away last update utc | 2026-10-14T09:44:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.1% |
| P btts no | 33.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 52.83 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.64 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.61 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.12 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 22.1% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 59.3% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.4% |
| Raw p btts yes | 66.9% |
| P home draw | 32.6% |
| P draw away | 84.3% |
| Raw p home draw | 40.7% |
| Raw p draw away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 10.50 |
| Reference draw odds | 6.40 |
| Reference away odds | 1.32 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Home probability edge | +6.4% |
| Draw probability edge | +1.7% |
| Away probability edge | -8.1% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | 0.1284 |
| Raw ev home | 1.2084 |
| Raw edge prob draw | 0.0336 |
| Raw ev draw | 0.2065 |
| Raw edge prob away | -0.1620 |
| Raw ev away | -0.2232 |
| Market p home draw | 25.7% |
| Market home draw odds | 3.78 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T09:44:35Z |
| Market reference home draw last update utc | 2026-10-14T09:46:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.5% |
| Market draw away odds | 1.06 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T09:44:35Z |
| Market reference draw away last update utc | 2026-10-14T09:46:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.09 |
| Market reference dc home draw odds | 3.79 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 89.9% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T09:43:29Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 47.4% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T09:43:29Z |
| Market reference under 3 5 odds | 2.04 |
| Market reference under 3 5 opposite odds | 1.85 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.3% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T09:44:35Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.34 |
| Market btts yes bookmakers | 1 |

</details>


---
