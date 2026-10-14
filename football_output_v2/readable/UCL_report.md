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
| Training data health | {'completed_matches': 27, 'latest_completed_utc': '2026-10-13T19:00:00+00:00', 'latest_completed_date': '2026-10-13', 'next_fixture_utc': '2026-10-14T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-14T11:22:57.985298+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'a7f09a11287058dc6c944f9931d177bbe8e8a36195a4f7edd862b7f91e59df89', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0006764830555555556, 'training_end': '2026-10-13', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
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

The model's most likely 1X2 outcome is **Real Madrid win** at **49.3%**. Expected goals are 1.22 for AS Roma and 1.64 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.4%; Under 3.5 goals: 67.9%; Double Chance 1X: 50.7%; Double Chance X2: 72.5%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 27.5% | 3.64 |
| Draw | 23.2% | 4.31 |
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
| 1 | 1-1 | 10.89% |
| 2 | 0-1 | 10.31% |
| 3 | 1-2 | 9.70% |
| 4 | 0-2 | 7.96% |
| 5 | 1-0 | 7.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 27.5% | 26.0% | 3.72 | +2.3% |
| Draw | 23.2% | 23.2% | 4.09 | -5.0% |
| Real Madrid win | 49.3% | 50.8% | 1.99 | -1.9% |

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
| Market best home last update utc | 2026-10-14T11:19:43Z |
| Market best draw last update utc | 2026-10-14T11:19:43Z |
| Market best away last update utc | 2026-10-14T11:19:43Z |
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
| Fair Under 0.5 odds | 19.33 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.19 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 29.0% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 47.7% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.0% |
| Raw p btts yes | 56.2% |
| P home draw | 50.7% |
| P draw away | 72.5% |
| Raw p home draw | 52.3% |
| Raw p draw away | 71.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.55 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.89 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | +1.5% |
| Draw probability edge | +0.0% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | 0.0303 |
| Raw ev home | 0.0797 |
| Raw edge prob draw | 0.0004 |
| Raw ev draw | -0.0495 |
| Raw edge prob away | -0.0307 |
| Raw ev away | -0.0500 |
| Market p home draw | 51.2% |
| Market home draw odds | 1.91 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:19:43Z |
| Market reference home draw last update utc | 2026-10-14T11:22:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.9% |
| Market draw away odds | 1.32 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:19:43Z |
| Market reference draw away last update utc | 2026-10-14T11:22:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home draw odds | 1.85 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:20:23Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.3% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:20:23Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.11 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.2% |
| Market btts yes odds | 1.41 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:19:43Z |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 3.00 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **66.3%**. Expected goals are 2.20 for Aston Villa and 0.60 for Fenerbahce (2.79 combined). The most likely exact score is 2-0 at 13.1%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 50.6%; Under 3.5 goals: 71.0%; Double Chance 1X: 85.6%; Double Chance X2: 33.7%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 40.8%; BTTS No (at least one team does not score): 59.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 66.3% | 1.51 |
| Draw | 19.3% | 5.18 |
| Fenerbahce win | 14.4% | 6.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.20 |
| Fenerbahce expected goals | 0.60 |
| Expected total goals | 2.79 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 74.5% |
| Under 1.5 | 25.5% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 29.0% |
| Under 3.5 | 71.0% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.12% |
| 2 | 1-0 | 12.31% |
| 3 | 3-0 | 9.60% |
| 4 | 1-1 | 8.98% |
| 5 | 2-1 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 66.3% | 58.0% | 1.74 | +15.3% |
| Draw | 19.3% | 22.2% | 4.04 | -22.0% |
| Fenerbahce win | 14.4% | 19.8% | 5.18 | -25.2% |

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
| Market best home last update utc | 2026-10-14T11:19:43Z |
| Market best draw last update utc | 2026-10-14T11:19:43Z |
| Market best away last update utc | 2026-10-14T11:19:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 40.8% |
| P btts no | 59.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.84 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.92 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.45 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.10 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 74.6% |
| Unadjusted draw probability | 16.4% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 76.4% |
| Raw p under 3 5 | 69.4% |
| Raw p btts yes | 39.6% |
| P home draw | 85.6% |
| P draw away | 33.7% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.66 |
| Reference draw odds | 4.05 |
| Reference away odds | 4.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | +8.3% |
| Draw probability edge | -2.9% |
| Away probability edge | -5.4% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | 0.1659 |
| Raw ev home | 0.2972 |
| Raw edge prob draw | -0.0580 |
| Raw ev draw | -0.3373 |
| Raw edge prob away | -0.1078 |
| Raw ev away | -0.5316 |
| Market p home draw | 80.4% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:19:43Z |
| Market reference home draw last update utc | 2026-10-14T11:22:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.0% |
| Market draw away odds | 2.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:19:43Z |
| Market reference draw away last update utc | 2026-10-14T11:22:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.26 |
| Market reference dc home draw odds | 1.21 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 83.8% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:16:24Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.7% |
| Market under 3 5 odds | 1.65 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:16:24Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.5% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:19:43Z |
| Market reference btts yes odds | 1.59 |
| Market reference btts yes opposite odds | 2.48 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **44.1%**. Expected goals are 1.71 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.65 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 70.3%; Under 3.5 goals: 50.4%; Double Chance 1X: 55.9%; Double Chance X2: 66.2%; Under 4.5 goals: 69.9%; BTTS Yes (both teams score): 70.0%; BTTS No (at least one team does not score): 30.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 33.8% | 2.96 |
| Draw | 22.0% | 4.54 |
| Borussia Dortmund win | 44.1% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 1.71 |
| Borussia Dortmund expected goals | 1.94 |
| Expected total goals | 3.65 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 87.5% |
| Under 1.5 | 12.5% |
| Over 2.5 | 70.3% |
| Under 2.5 | 29.7% |
| Over 3.5 | 49.6% |
| Under 3.5 | 50.4% |
| Over 4.5 | 30.1% |
| Under 4.5 | 69.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.69% |
| 2 | 1-2 | 8.35% |
| 3 | 2-2 | 7.59% |
| 4 | 2-1 | 7.12% |
| 5 | 0-1 | 5.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 33.8% | 32.6% | 3.15 | +6.6% |
| Draw | 22.0% | 23.3% | 4.05 | -10.7% |
| Borussia Dortmund win | 44.1% | 44.1% | 2.22 | -2.1% |

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
| Market best home last update utc | 2026-10-14T11:19:43Z |
| Market best draw last update utc | 2026-10-14T11:19:43Z |
| Market best away last update utc | 2026-10-14T11:19:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.0% |
| P btts no | 30.0% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.51 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.02 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.37 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.32 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 44.2% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 50.4% |
| Raw p btts yes | 69.7% |
| P home draw | 55.9% |
| P draw away | 66.2% |
| Raw p home draw | 55.8% |
| Raw p draw away | 64.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +1.2% |
| Draw probability edge | -1.3% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0247 |
| Raw ev home | 0.1048 |
| Raw edge prob draw | -0.0254 |
| Raw ev draw | -0.1586 |
| Raw edge prob away | 0.0007 |
| Raw ev away | -0.0198 |
| Market p home draw | 54.7% |
| Market home draw odds | 1.74 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:19:43Z |
| Market reference home draw last update utc | 2026-10-14T11:22:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.6% |
| Market draw away odds | 1.41 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:19:43Z |
| Market reference draw away last update utc | 2026-10-14T11:22:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home draw odds | 1.73 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:22:18Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 50.9% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:22:18Z |
| Market reference under 3 5 odds | 1.92 |
| Market reference under 3 5 opposite odds | 1.99 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.4% |
| Market btts yes odds | 1.34 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:19:43Z |
| Market reference btts yes odds | 1.41 |
| Market reference btts yes opposite odds | 3.30 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **61.0%**. Expected goals are 1.86 for Feyenoord and 4.03 for Como (5.89 combined). The most likely exact score is 2-2 at 5.9%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 92.1%; Under 3.5 goals: 17.5%; Double Chance 1X: 39.0%; Double Chance X2: 78.3%; Under 4.5 goals: 32.7%; BTTS Yes (both teams score): 84.6%; BTTS No (at least one team does not score): 15.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 21.7% | 4.62 |
| Draw | 17.3% | 5.77 |
| Como win | 61.0% | 1.64 |

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
| Over 2.5 | 92.1% |
| Under 2.5 | 7.9% |
| Over 3.5 | 82.5% |
| Under 3.5 | 17.5% |
| Over 4.5 | 67.3% |
| Under 4.5 | 32.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 5.94% |
| 2 | 3-3 | 4.94% |
| 3 | 1-4 | 4.59% |
| 4 | 1-3 | 4.55% |
| 5 | 2-4 | 4.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 21.7% | 30.3% | 3.27 | -29.2% |
| Draw | 17.3% | 23.3% | 3.96 | -31.4% |
| Como win | 61.0% | 46.4% | 2.19 | +33.6% |

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
| Market best home last update utc | 2026-10-14T11:19:43Z |
| Market best draw last update utc | 2026-10-14T11:19:43Z |
| Market best away last update utc | 2026-10-14T11:19:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 84.6% |
| P btts no | 15.4% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 375.91 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 43.67 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 12.61 |
| Fair Over 3.5 odds | 1.21 |
| Fair Under 3.5 odds | 5.72 |
| Fair Over 4.5 odds | 1.49 |
| Fair Under 4.5 odds | 3.06 |
| Unadjusted home-win probability | 13.0% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 75.6% |
| Raw p over 1 5 | 98.0% |
| Raw p under 3 5 | 16.2% |
| Raw p btts yes | 82.8% |
| P home draw | 39.0% |
| P draw away | 78.3% |
| Raw p home draw | 24.4% |
| Raw p draw away | 87.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.05 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.05 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -8.7% |
| Draw probability edge | -6.0% |
| Away probability edge | +14.6% |
| Over 2.5 probability edge | +28.3% |
| Under 2.5 probability edge | -28.3% |
| Raw edge prob home | -0.1731 |
| Raw ev home | -0.5748 |
| Raw edge prob draw | -0.1194 |
| Raw ev draw | -0.5501 |
| Raw edge prob away | 0.2926 |
| Raw ev away | 0.6564 |
| Market p home draw | 54.6% |
| Market home draw odds | 1.76 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:19:43Z |
| Market reference home draw last update utc | 2026-10-14T11:22:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.9% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:19:43Z |
| Market reference draw away last update utc | 2026-10-14T11:22:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.35 |
| Market reference dc home draw odds | 1.73 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 85.4% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:19:19Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.7% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:19:19Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.32 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.0% |
| Market btts yes odds | 1.43 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:19:43Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.75 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **69.1%**. Expected goals are 0.29 for LASK and 1.41 for Liverpool (1.70 combined). The most likely exact score is 0-1 at 27.1%. Goal-market probabilities: at least one goal: 85.3%; Over 2.5 goals: 25.5%; Under 3.5 goals: 90.4%; Double Chance 1X: 30.9%; Double Chance X2: 90.4%; Under 4.5 goals: 96.9%; BTTS Yes (both teams score): 18.2%; BTTS No (at least one team does not score): 81.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 9.6% | 10.37 |
| Draw | 21.3% | 4.70 |
| Liverpool win | 69.1% | 1.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.29 |
| Liverpool expected goals | 1.41 |
| Expected total goals | 1.70 |
| Over 0.5 | 85.3% |
| Under 0.5 | 14.7% |
| Over 1.5 | 51.2% |
| Under 1.5 | 48.8% |
| Over 2.5 | 25.5% |
| Under 2.5 | 74.5% |
| Over 3.5 | 9.6% |
| Under 3.5 | 90.4% |
| Over 4.5 | 3.1% |
| Under 4.5 | 96.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 27.13% |
| 2 | 0-2 | 18.85% |
| 3 | 0-0 | 14.68% |
| 4 | 0-3 | 8.86% |
| 5 | 1-0 | 6.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 9.6% | 11.4% | 7.70 | -25.8% |
| Draw | 21.3% | 16.7% | 5.33 | +13.3% |
| Liverpool win | 69.1% | 71.9% | 1.43 | -1.2% |

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
| Market best home last update utc | 2026-10-14T11:19:43Z |
| Market best draw last update utc | 2026-10-14T11:19:43Z |
| Market best away last update utc | 2026-10-14T11:19:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 18.2% |
| P btts no | 81.8% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.81 |
| Fair Over 1.5 odds | 1.95 |
| Fair Under 1.5 odds | 2.05 |
| Fair Over 2.5 odds | 3.92 |
| Fair Under 2.5 odds | 1.34 |
| Fair Over 3.5 odds | 10.37 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 32.01 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 7.9% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 66.3% |
| Raw p over 1 5 | 50.4% |
| Raw p under 3 5 | 90.6% |
| Raw p btts yes | 18.9% |
| P home draw | 30.9% |
| P draw away | 90.4% |
| Raw p home draw | 33.7% |
| Raw p draw away | 92.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 7.25 |
| Reference draw odds | 5.10 |
| Reference away odds | 1.35 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -1.7% |
| Draw probability edge | +4.5% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -38.3% |
| Under 2.5 probability edge | +38.3% |
| Raw edge prob home | -0.0343 |
| Raw ev home | -0.3898 |
| Raw edge prob draw | 0.0910 |
| Raw ev draw | 0.3758 |
| Raw edge prob away | -0.0566 |
| Raw ev away | -0.0524 |
| Market p home draw | 32.8% |
| Market home draw odds | 3.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:19:43Z |
| Market reference home draw last update utc | 2026-10-14T11:22:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 86.5% |
| Market draw away odds | 1.10 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:19:43Z |
| Market reference draw away last update utc | 2026-10-14T11:22:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.10 |
| Market reference dc home draw odds | 2.90 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 83.8% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:20:46Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.1% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:20:46Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.9% |
| Market btts yes odds | 1.73 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:19:43Z |
| Market reference btts yes odds | 1.81 |
| Market reference btts yes opposite odds | 2.20 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **42.7%**. Expected goals are 1.41 for Manchester City and 2.21 for Paris Saint Germain (3.61 combined). The most likely exact score is 2-1 at 8.8%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 68.9%; Under 3.5 goals: 52.5%; Double Chance 1X: 57.3%; Double Chance X2: 63.4%; Under 4.5 goals: 71.3%; BTTS Yes (both teams score): 67.6%; BTTS No (at least one team does not score): 32.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 36.6% | 2.73 |
| Draw | 20.7% | 4.83 |
| Paris Saint Germain win | 42.7% | 2.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.41 |
| Paris Saint Germain expected goals | 2.21 |
| Expected total goals | 3.61 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 86.4% |
| Under 1.5 | 13.6% |
| Over 2.5 | 68.9% |
| Under 2.5 | 31.1% |
| Over 3.5 | 47.5% |
| Under 3.5 | 52.5% |
| Over 4.5 | 28.7% |
| Under 4.5 | 71.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.82% |
| 2 | 1-1 | 8.47% |
| 3 | 1-2 | 7.02% |
| 4 | 2-2 | 6.91% |
| 5 | 1-0 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 36.6% | 48.8% | 2.06 | -24.6% |
| Draw | 20.7% | 22.0% | 4.21 | -12.8% |
| Paris Saint Germain win | 42.7% | 29.2% | 3.42 | +45.9% |

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
| Market best home last update utc | 2026-10-14T11:19:43Z |
| Market best draw last update utc | 2026-10-14T11:19:43Z |
| Market best away last update utc | 2026-10-14T11:19:43Z |
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
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.15 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.36 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.22 |
| Fair Over 3.5 odds | 2.10 |
| Fair Under 3.5 odds | 1.91 |
| Fair Over 4.5 odds | 3.49 |
| Fair Under 4.5 odds | 1.40 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 56.1% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 51.3% |
| Raw p btts yes | 66.7% |
| P home draw | 57.3% |
| P draw away | 63.4% |
| Raw p home draw | 43.9% |
| Raw p draw away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.95 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -12.2% |
| Draw probability edge | -1.3% |
| Away probability edge | +13.5% |
| Over 2.5 probability edge | +1.9% |
| Under 2.5 probability edge | -1.9% |
| Raw edge prob home | -0.2441 |
| Raw ev home | -0.4969 |
| Raw edge prob draw | -0.0254 |
| Raw ev draw | -0.1810 |
| Raw edge prob away | 0.2694 |
| Raw ev away | 0.9195 |
| Market p home draw | 71.4% |
| Market home draw odds | 1.36 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:19:43Z |
| Market reference home draw last update utc | 2026-10-14T11:22:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.7% |
| Market draw away odds | 1.85 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:19:43Z |
| Market reference draw away last update utc | 2026-10-14T11:22:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.80 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:22:13Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.2% |
| Market under 3 5 odds | 1.83 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:22:13Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.7% |
| Market btts yes odds | 1.38 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:19:43Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 3.05 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **60.1%**. Expected goals are 3.10 for Real Betis and 1.32 for Porto (4.42 combined). The most likely exact score is 2-2 at 7.2%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 79.5%; Under 3.5 goals: 37.4%; Double Chance 1X: 79.6%; Double Chance X2: 39.9%; Under 4.5 goals: 57.4%; BTTS Yes (both teams score): 72.0%; BTTS No (at least one team does not score): 28.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 60.1% | 1.67 |
| Draw | 19.6% | 5.11 |
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
| Over 2.5 | 79.5% |
| Under 2.5 | 20.5% |
| Over 3.5 | 62.6% |
| Under 3.5 | 37.4% |
| Over 4.5 | 42.6% |
| Under 4.5 | 57.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.21% |
| 2 | 1-1 | 6.70% |
| 3 | 3-1 | 6.49% |
| 4 | 2-1 | 6.29% |
| 5 | 4-1 | 5.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 60.1% | 47.1% | 2.11 | +26.7% |
| Draw | 19.6% | 25.4% | 3.80 | -25.7% |
| Porto win | 20.4% | 27.4% | 3.60 | -26.6% |
| Over 2.5 | 79.5% | 56.3% | 1.73 | +37.5% |
| Under 2.5 | 20.5% | 43.7% | 2.28 | -53.2% |

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
| Market best home last update utc | 2026-10-14T11:19:43Z |
| Market best draw last update utc | 2026-10-14T11:19:43Z |
| Market best away last update utc | 2026-10-14T11:19:43Z |
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
| P btts yes | 72.0% |
| P btts no | 28.0% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 72.98 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.40 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.87 |
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
| P draw away | 39.9% |
| Raw p home draw | 86.7% |
| Raw p draw away | 27.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.02 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +12.9% |
| Draw probability edge | -5.9% |
| Away probability edge | -7.1% |
| Over 2.5 probability edge | +23.2% |
| Under 2.5 probability edge | -23.2% |
| Raw edge prob home | 0.2582 |
| Raw ev home | 0.5396 |
| Raw edge prob draw | -0.1172 |
| Raw ev draw | -0.4797 |
| Raw edge prob away | -0.1410 |
| Raw ev away | -0.5196 |
| Market p home draw | 72.9% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:19:43Z |
| Market reference home draw last update utc | 2026-10-14T11:22:51Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.0% |
| Market draw away odds | 1.81 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:19:43Z |
| Market reference draw away last update utc | 2026-10-14T11:22:51Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 81.2% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:19:23Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.0% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:19:23Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.76 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.8% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:19:43Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.46 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.3%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.29 for AEK Athens (2.78 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 52.0%; Under 3.5 goals: 69.8%; Double Chance 1X: 64.7%; Double Chance X2: 60.7%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 55.8%; BTTS No (at least one team does not score): 44.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.3% | 2.54 |
| Draw | 25.4% | 3.94 |
| AEK Athens win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.49 |
| AEK Athens expected goals | 1.29 |
| Expected total goals | 2.78 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 52.0% |
| Under 2.5 | 48.0% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.97% |
| 2 | 1-0 | 9.13% |
| 3 | 0-1 | 9.11% |
| 4 | 2-1 | 8.21% |
| 5 | 1-2 | 8.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.3% | 36.1% | 2.79 | +9.6% |
| Draw | 25.4% | 26.7% | 3.49 | -11.4% |
| AEK Athens win | 35.3% | 37.2% | 2.70 | -4.7% |
| Over 2.5 | 52.0% | 50.0% | 1.95 | +1.4% |
| Under 2.5 | 48.0% | 50.0% | 1.99 | -4.5% |

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
| Market best home last update utc | 2026-10-14T11:19:43Z |
| Market best draw last update utc | 2026-10-14T11:19:43Z |
| Market best away last update utc | 2026-10-14T11:19:43Z |
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
| P btts yes | 55.8% |
| P btts no | 44.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.82 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.82 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 42.5% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 75.9% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 55.5% |
| P home draw | 64.7% |
| P draw away | 60.7% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.53 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | +3.2% |
| Draw probability edge | -1.3% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | 0.0638 |
| Raw ev home | 0.1855 |
| Raw edge prob draw | -0.0264 |
| Raw ev draw | -0.1598 |
| Raw edge prob away | -0.0374 |
| Raw ev away | -0.0972 |
| Market p home draw | 65.2% |
| Market home draw odds | 1.53 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:19:43Z |
| Market reference home draw last update utc | 2026-10-14T11:22:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.6% |
| Market draw away odds | 1.50 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:19:43Z |
| Market reference draw away last update utc | 2026-10-14T11:22:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home draw odds | 1.44 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 77.3% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:22:13Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.94 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.9% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:22:13Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.18 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.7% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:19:43Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.28 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.9%**. Expected goals are 1.37 for ŠK Slovan Bratislava and 2.33 for VfB Stuttgart (3.70 combined). The most likely exact score is 1-2 at 10.4%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 72.3%; Under 3.5 goals: 48.7%; Double Chance 1X: 33.1%; Double Chance X2: 83.8%; Under 4.5 goals: 68.0%; BTTS Yes (both teams score): 66.2%; BTTS No (at least one team does not score): 33.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 16.2% | 6.17 |
| Draw | 16.9% | 5.91 |
| VfB Stuttgart win | 66.9% | 1.50 |

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
| Over 3.5 | 51.3% |
| Under 3.5 | 48.7% |
| Over 4.5 | 32.0% |
| Under 4.5 | 68.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.37% |
| 2 | 1-3 | 8.05% |
| 3 | 0-2 | 7.57% |
| 4 | 0-1 | 6.95% |
| 5 | 1-1 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 16.2% | 10.3% | 9.00 | +45.8% |
| Draw | 16.9% | 15.2% | 5.85 | -1.0% |
| VfB Stuttgart win | 66.9% | 74.5% | 1.36 | -9.0% |

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
| Market best home last update utc | 2026-10-14T11:19:43Z |
| Market best draw last update utc | 2026-10-14T11:19:43Z |
| Market best away last update utc | 2026-10-14T11:19:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.2% |
| P btts no | 33.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 52.88 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.61 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.61 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.12 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 22.1% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 59.3% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.4% |
| Raw p btts yes | 66.9% |
| P home draw | 33.1% |
| P draw away | 83.8% |
| Raw p home draw | 40.7% |
| Raw p draw away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 8.00 |
| Reference draw odds | 5.60 |
| Reference away odds | 1.31 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.40 |
| Home probability edge | +5.9% |
| Draw probability edge | +1.7% |
| Away probability edge | -7.6% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | 0.1177 |
| Raw ev home | 0.9876 |
| Raw edge prob draw | 0.0339 |
| Raw ev draw | 0.0892 |
| Raw edge prob away | -0.1516 |
| Raw ev away | -0.1936 |
| Market p home draw | 28.9% |
| Market home draw odds | 3.42 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:19:43Z |
| Market reference home draw last update utc | 2026-10-14T11:22:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 88.2% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:19:43Z |
| Market reference draw away last update utc | 2026-10-14T11:22:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home draw odds | 3.30 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 91.2% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:22:13Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 7.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 48.0% |
| Market under 3 5 odds | 2.07 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:22:13Z |
| Market reference under 3 5 odds | 2.02 |
| Market reference under 3 5 opposite odds | 1.87 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.8% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:19:43Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.46 |
| Market btts yes bookmakers | 1 |

</details>


---
