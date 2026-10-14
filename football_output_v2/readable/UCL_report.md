# UEFA Champions League — football model report

Fixtures in this report: **7**.

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
| Training data health | {'completed_matches': 27, 'latest_completed_utc': '2026-10-13T19:00:00+00:00', 'latest_completed_date': '2026-10-13', 'next_fixture_utc': '2026-10-14T19:00:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-14T18:13:35.002134+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '6db8120b63c6c22412ce55f444567108adbd7fbc03f612bc6fd8922ee1570dc9', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0015566822222222222, 'training_end': '2026-10-13', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Additional event odds calls used before this league | 21.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
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

The model's most likely 1X2 outcome is **Real Madrid win** at **49.3%**. Expected goals are 1.22 for AS Roma and 1.64 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.4%; Under 3.5 goals: 67.9%; Double Chance 1X: 50.7%; Double Chance X2: 72.6%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 27.4% | 3.65 |
| Draw | 23.3% | 4.29 |
| Real Madrid win | 49.3% | 2.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.22 |
| Real Madrid expected goals | 1.64 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 54.4% |
| Under 2.5 | 45.6% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.92% |
| 2 | 0-1 | 10.32% |
| 3 | 1-2 | 9.70% |
| 4 | 0-2 | 7.96% |
| 5 | 1-0 | 7.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 27.4% | 25.8% | 3.78 | +3.6% |
| Draw | 23.3% | 23.3% | 3.98 | -7.3% |
| Real Madrid win | 49.3% | 50.9% | 2.00 | -1.4% |

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
| Market best home last update utc | 2026-10-14T18:13:09Z |
| Market best draw last update utc | 2026-10-14T18:13:09Z |
| Market best away last update utc | 2026-10-14T18:13:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.27 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.20 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 29.0% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 47.7% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.0% |
| Raw p btts yes | 56.2% |
| P home draw | 50.7% |
| P draw away | 72.6% |
| Raw p home draw | 52.3% |
| Raw p draw away | 71.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.74 |
| Reference draw odds | 4.12 |
| Reference away odds | 1.93 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | +1.6% |
| Draw probability edge | -0.1% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | 0.0324 |
| Raw ev home | 0.0971 |
| Raw edge prob draw | -0.0010 |
| Raw ev draw | -0.0751 |
| Raw edge prob away | -0.0314 |
| Raw ev away | -0.0453 |
| Market p home draw | 50.6% |
| Market home draw odds | 1.90 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:13:09Z |
| Market reference home draw last update utc | 2026-10-14T18:13:42Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.2% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:13:09Z |
| Market reference draw away last update utc | 2026-10-14T18:13:42Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.88 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 86.9% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 54.2% |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 67.7% |
| Market btts yes odds | 1.41 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:13:09Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 3.05 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **66.4%**. Expected goals are 2.20 for Aston Villa and 0.60 for Fenerbahce (2.79 combined). The most likely exact score is 2-0 at 13.1%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 50.5%; Under 3.5 goals: 70.9%; Double Chance 1X: 86.1%; Double Chance X2: 33.6%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 40.9%; BTTS No (at least one team does not score): 59.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 66.4% | 1.51 |
| Draw | 19.7% | 5.07 |
| Fenerbahce win | 13.9% | 7.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.20 |
| Fenerbahce expected goals | 0.60 |
| Expected total goals | 2.79 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 74.5% |
| Under 1.5 | 25.5% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.14% |
| 2 | 1-0 | 12.33% |
| 3 | 3-0 | 9.62% |
| 4 | 1-1 | 9.17% |
| 5 | 2-1 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 66.4% | 58.2% | 1.72 | +14.2% |
| Draw | 19.7% | 23.0% | 4.21 | -17.0% |
| Fenerbahce win | 13.9% | 18.8% | 5.12 | -28.7% |
| Over 2.5 | 50.5% | 61.3% | 1.64 | -17.1% |
| Under 2.5 | 49.5% | 38.7% | 2.46 | +21.7% |

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
| Market best home last update utc | 2026-10-14T18:13:09Z |
| Market best draw last update utc | 2026-10-14T18:13:09Z |
| Market best away last update utc | 2026-10-14T18:13:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 40.9% |
| P btts no | 59.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.53 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.93 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.10 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 74.6% |
| Unadjusted draw probability | 16.4% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 76.4% |
| Raw p under 3 5 | 69.4% |
| Raw p btts yes | 39.6% |
| P home draw | 86.1% |
| P draw away | 33.6% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.69 |
| Reference draw odds | 4.15 |
| Reference away odds | 5.05 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +8.2% |
| Draw probability edge | -3.3% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | 0.1637 |
| Raw ev home | 0.2823 |
| Raw edge prob draw | -0.0662 |
| Raw ev draw | -0.3094 |
| Raw edge prob away | -0.0976 |
| Raw ev away | -0.5370 |
| Market p home draw | 80.2% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:13:09Z |
| Market reference home draw last update utc | 2026-10-14T18:13:42Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.8% |
| Market draw away odds | 2.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:13:09Z |
| Market reference draw away last update utc | 2026-10-14T18:13:42Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.18 |
| Market reference dc draw away odds | 2.21 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T18:06:08Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.2% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T18:06:08Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.52 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.6% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:13:09Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.42 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **41.9%**. Expected goals are 1.71 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.65 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 70.0%; Under 3.5 goals: 50.5%; Double Chance 1X: 58.1%; Double Chance X2: 64.9%; Under 4.5 goals: 70.1%; BTTS Yes (both teams score): 70.3%; BTTS No (at least one team does not score): 29.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 35.1% | 2.85 |
| Draw | 23.1% | 4.34 |
| Borussia Dortmund win | 41.9% | 2.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 1.71 |
| Borussia Dortmund expected goals | 1.94 |
| Expected total goals | 3.65 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 87.5% |
| Under 1.5 | 12.5% |
| Over 2.5 | 70.0% |
| Under 2.5 | 30.0% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 29.9% |
| Under 4.5 | 70.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.09% |
| 2 | 2-2 | 7.94% |
| 3 | 1-2 | 7.92% |
| 4 | 2-1 | 7.38% |
| 5 | 0-1 | 5.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 35.1% | 35.1% | 2.79 | -2.1% |
| Draw | 23.1% | 25.3% | 3.94 | -9.2% |
| Borussia Dortmund win | 41.9% | 39.6% | 2.48 | +3.8% |

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
| Market best home last update utc | 2026-10-14T18:13:09Z |
| Market best draw last update utc | 2026-10-14T18:13:09Z |
| Market best away last update utc | 2026-10-14T18:13:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.3% |
| P btts no | 29.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.60 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.02 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.33 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.35 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 44.2% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 50.4% |
| Raw p btts yes | 69.7% |
| P home draw | 58.1% |
| P draw away | 64.9% |
| Raw p home draw | 55.8% |
| Raw p draw away | 64.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.78 |
| Reference draw odds | 3.82 |
| Reference away odds | 2.47 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -0.0% |
| Draw probability edge | -2.3% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.0000 |
| Raw ev home | -0.0215 |
| Raw edge prob draw | -0.0455 |
| Raw ev draw | -0.1815 |
| Raw edge prob away | 0.0456 |
| Raw ev away | 0.0950 |
| Market p home draw | 61.0% |
| Market home draw odds | 1.61 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:13:09Z |
| Market reference home draw last update utc | 2026-10-14T18:13:42Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.5% |
| Market draw away odds | 1.50 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:13:09Z |
| Market reference draw away last update utc | 2026-10-14T18:13:42Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.56 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 89.5% |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.9% |
| Market reference under 3 5 odds | 1.85 |
| Market reference under 3 5 opposite odds | 2.07 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 70.6% |
| Market btts yes odds | 1.32 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:13:09Z |
| Market reference btts yes odds | 1.41 |
| Market reference btts yes opposite odds | 3.35 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **42.2%**. Expected goals are 1.41 for Manchester City and 2.21 for Paris Saint Germain (3.61 combined). The most likely exact score is 2-1 at 8.9%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 68.9%; Under 3.5 goals: 52.5%; Double Chance 1X: 57.8%; Double Chance X2: 63.1%; Under 4.5 goals: 71.4%; BTTS Yes (both teams score): 67.6%; BTTS No (at least one team does not score): 32.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 36.9% | 2.71 |
| Draw | 20.9% | 4.77 |
| Paris Saint Germain win | 42.2% | 2.37 |

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
| Over 2.5 | 68.9% |
| Under 2.5 | 31.1% |
| Over 3.5 | 47.5% |
| Under 3.5 | 52.5% |
| Over 4.5 | 28.6% |
| Under 4.5 | 71.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.88% |
| 2 | 1-1 | 8.56% |
| 3 | 2-2 | 6.99% |
| 4 | 1-2 | 6.94% |
| 5 | 1-0 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 36.9% | 49.3% | 2.06 | -24.1% |
| Draw | 20.9% | 22.4% | 4.26 | -10.8% |
| Paris Saint Germain win | 42.2% | 28.3% | 3.38 | +42.6% |

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
| Market best home last update utc | 2026-10-14T18:13:09Z |
| Market best draw last update utc | 2026-10-14T18:13:09Z |
| Market best away last update utc | 2026-10-14T18:13:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.6% |
| P btts no | 32.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.70 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.35 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.21 |
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
| P home draw | 57.8% |
| P draw away | 63.1% |
| Raw p home draw | 43.9% |
| Raw p draw away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.99 |
| Reference draw odds | 4.28 |
| Reference away odds | 3.42 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | -12.4% |
| Draw probability edge | -1.5% |
| Away probability edge | +13.9% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.2488 |
| Raw ev home | -0.4969 |
| Raw edge prob draw | -0.0299 |
| Raw ev draw | -0.1712 |
| Raw edge prob away | 0.2787 |
| Raw ev away | 0.8970 |
| Market p home draw | 71.1% |
| Market home draw odds | 1.37 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:13:09Z |
| Market reference home draw last update utc | 2026-10-14T18:13:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.2% |
| Market draw away odds | 1.85 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:13:09Z |
| Market reference draw away last update utc | 2026-10-14T18:13:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.85 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 88.5% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.8% |
| Market reference under 3 5 odds | 1.85 |
| Market reference under 3 5 opposite odds | 2.06 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 68.9% |
| Market btts yes odds | 1.35 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:13:09Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 3.20 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **59.2%**. Expected goals are 3.10 for Real Betis and 1.32 for Porto (4.42 combined). The most likely exact score is 2-2 at 7.4%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 79.3%; Under 3.5 goals: 37.5%; Double Chance 1X: 79.3%; Double Chance X2: 40.8%; Under 4.5 goals: 57.6%; BTTS Yes (both teams score): 72.2%; BTTS No (at least one team does not score): 27.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 59.2% | 1.69 |
| Draw | 20.1% | 4.97 |
| Porto win | 20.7% | 4.82 |

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
| Over 2.5 | 79.3% |
| Under 2.5 | 20.7% |
| Over 3.5 | 62.5% |
| Under 3.5 | 37.5% |
| Over 4.5 | 42.4% |
| Under 4.5 | 57.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.42% |
| 2 | 1-1 | 6.89% |
| 3 | 3-1 | 6.40% |
| 4 | 2-1 | 6.20% |
| 5 | 1-2 | 5.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 59.2% | 45.3% | 2.22 | +31.3% |
| Draw | 20.1% | 26.5% | 3.78 | -24.0% |
| Porto win | 20.7% | 28.1% | 3.33 | -31.0% |
| Over 2.5 | 79.3% | 56.8% | 1.76 | +39.5% |
| Under 2.5 | 20.7% | 43.2% | 2.23 | -53.8% |

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
| Market best home last update utc | 2026-10-14T18:13:09Z |
| Market best draw last update utc | 2026-10-14T18:13:09Z |
| Market best away last update utc | 2026-10-14T18:13:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 72.2% |
| P btts no | 27.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 70.94 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.34 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.83 |
| Fair Over 3.5 odds | 1.60 |
| Fair Under 3.5 odds | 2.66 |
| Fair Over 4.5 odds | 2.36 |
| Fair Under 4.5 odds | 1.74 |
| Unadjusted home-win probability | 73.0% |
| Unadjusted draw probability | 13.7% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 93.2% |
| Raw p under 3 5 | 35.6% |
| Raw p btts yes | 69.8% |
| P home draw | 79.3% |
| P draw away | 40.8% |
| Raw p home draw | 86.7% |
| Raw p draw away | 27.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.16 |
| Reference draw odds | 3.64 |
| Reference away odds | 3.44 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | +13.8% |
| Draw probability edge | -6.4% |
| Away probability edge | -7.4% |
| Over 2.5 probability edge | +22.5% |
| Under 2.5 probability edge | -22.5% |
| Raw edge prob home | 0.2762 |
| Raw ev home | 0.6198 |
| Raw edge prob draw | -0.1284 |
| Raw ev draw | -0.4825 |
| Raw edge prob away | -0.1478 |
| Raw ev away | -0.5557 |
| Market p home draw | 70.6% |
| Market home draw odds | 1.38 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:13:09Z |
| Market reference home draw last update utc | 2026-10-14T18:13:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.5% |
| Market draw away odds | 1.74 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:13:09Z |
| Market reference draw away last update utc | 2026-10-14T18:13:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.0% |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 3.95 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.5% |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.73 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 61.2% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:13:09Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.56 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.2%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.29 for AEK Athens (2.78 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 51.8%; Under 3.5 goals: 69.8%; Double Chance 1X: 65.5%; Double Chance X2: 60.8%; Under 4.5 goals: 85.4%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.2% | 2.55 |
| Draw | 26.3% | 3.81 |
| AEK Athens win | 34.5% | 2.90 |

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
| 1 | 1-1 | 12.37% |
| 2 | 1-0 | 9.11% |
| 3 | 0-1 | 8.90% |
| 4 | 2-1 | 8.20% |
| 5 | 1-2 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.2% | 36.0% | 2.75 | +7.9% |
| Draw | 26.3% | 28.4% | 3.38 | -11.3% |
| AEK Athens win | 34.5% | 35.6% | 2.80 | -3.4% |
| Over 2.5 | 51.8% | 50.5% | 2.02 | +4.6% |
| Under 2.5 | 48.2% | 49.5% | 1.92 | -7.4% |

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
| Market best home last update utc | 2026-10-14T18:13:09Z |
| Market best draw last update utc | 2026-10-14T18:13:09Z |
| Market best away last update utc | 2026-10-14T18:13:09Z |
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
| Fair Under 0.5 odds | 16.27 |
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
| P home draw | 65.5% |
| P draw away | 60.8% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.71 |
| Reference draw odds | 3.41 |
| Reference away odds | 2.74 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +3.3% |
| Draw probability edge | -2.2% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | 0.0650 |
| Raw ev home | 0.1685 |
| Raw edge prob draw | -0.0436 |
| Raw ev draw | -0.1863 |
| Raw edge prob away | -0.0214 |
| Raw ev away | -0.0638 |
| Market p home draw | 65.0% |
| Market home draw odds | 1.50 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:13:09Z |
| Market reference home draw last update utc | 2026-10-14T18:13:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.2% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:13:09Z |
| Market reference draw away last update utc | 2026-10-14T18:13:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.48 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 76.1% |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.81 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 71.5% |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.24 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 56.5% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:13:09Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.28 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **64.9%**. Expected goals are 1.37 for ŠK Slovan Bratislava and 2.33 for VfB Stuttgart (3.70 combined). The most likely exact score is 1-2 at 10.1%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 72.1%; Under 3.5 goals: 48.9%; Double Chance 1X: 35.1%; Double Chance X2: 82.3%; Under 4.5 goals: 68.2%; BTTS Yes (both teams score): 66.4%; BTTS No (at least one team does not score): 33.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.7% | 5.64 |
| Draw | 17.4% | 5.75 |
| VfB Stuttgart win | 64.9% | 1.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.37 |
| VfB Stuttgart expected goals | 2.33 |
| Expected total goals | 3.70 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 88.3% |
| Under 1.5 | 11.7% |
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 51.1% |
| Under 3.5 | 48.9% |
| Over 4.5 | 31.8% |
| Under 4.5 | 68.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.06% |
| 2 | 1-3 | 7.81% |
| 3 | 0-2 | 7.35% |
| 4 | 1-1 | 7.01% |
| 5 | 0-1 | 6.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.7% | 13.4% | 7.70 | +36.5% |
| Draw | 17.4% | 16.2% | 5.54 | -3.6% |
| VfB Stuttgart win | 64.9% | 70.4% | 1.42 | -7.9% |

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
| Market best home last update utc | 2026-10-14T18:13:09Z |
| Market best draw last update utc | 2026-10-14T18:13:09Z |
| Market best away last update utc | 2026-10-14T18:13:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.4% |
| P btts no | 33.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 51.44 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.53 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.58 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.14 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 22.1% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 59.3% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.4% |
| Raw p btts yes | 66.9% |
| P home draw | 35.1% |
| P draw away | 82.3% |
| Raw p home draw | 40.7% |
| Raw p draw away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.90 |
| Reference draw odds | 5.75 |
| Reference away odds | 1.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.40 |
| Home probability edge | +4.4% |
| Draw probability edge | +1.2% |
| Away probability edge | -5.6% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | 0.0870 |
| Raw ev home | 0.7005 |
| Raw edge prob draw | 0.0244 |
| Raw ev draw | 0.0315 |
| Raw edge prob away | -0.1114 |
| Raw ev away | -0.1580 |
| Market p home draw | 30.5% |
| Market home draw odds | 3.12 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:13:09Z |
| Market reference home draw last update utc | 2026-10-14T18:13:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 87.4% |
| Market draw away odds | 1.10 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:13:09Z |
| Market reference draw away last update utc | 2026-10-14T18:13:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.15 |
| Market reference dc draw away odds | 1.10 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 90.5% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 6.20 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 47.9% |
| Market reference under 3 5 odds | 2.04 |
| Market reference under 3 5 opposite odds | 1.88 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 62.8% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:13:09Z |
| Market reference btts yes odds | 1.59 |
| Market reference btts yes opposite odds | 2.68 |
| Market btts yes bookmakers | 1 |

</details>


---
