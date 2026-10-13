# UEFA Champions League — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 521 |
| Training data through | 2026-09-10 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1537.063 |
| Base scoring parameter | 0.141 |
| Home-advantage parameter | 0.278 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0 |
| Training data health | {'completed_matches': 18, 'latest_completed_utc': '2026-09-10T19:00:00+00:00', 'latest_completed_date': '2026-09-10', 'next_fixture_utc': '2026-10-13T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-13T16:01:02.491950+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '6b2e058b56b3cd8dea308786a01d5e6ce3c35a4be9a4959bdd52667544a33082', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0006471313888888889, 'training_end': '2026-09-10', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 18.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 18.00 |
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

## 2026-10-13 — Arsenal vs Lille

The model's most likely 1X2 outcome is **Arsenal win** at **74.7%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.5%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 49.6%; Under 3.5 goals: 73.0%; Double Chance 1X: 90.8%; Double Chance X2: 25.3%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 39.4%; BTTS No (at least one team does not score): 60.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 74.7% | 1.34 |
| Draw | 16.1% | 6.20 |
| Lille win | 9.2% | 10.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.93 |
| Lille expected goals | 0.65 |
| Expected total goals | 2.58 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.49% |
| 2 | 2-0 | 15.40% |
| 3 | 2-1 | 10.07% |
| 4 | 3-0 | 9.90% |
| 5 | 1-1 | 7.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 74.7% | 81.2% | 1.23 | -8.1% |
| Draw | 16.1% | 12.7% | 7.22 | +16.4% |
| Lille win | 9.2% | 6.1% | 15.50 | +42.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 93177465a42a0fb7802f1c8b06d6ee3a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 39.4% |
| P btts no | 60.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.17 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.71 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.87 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 72.5% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 40.6% |
| P home draw | 90.8% |
| P draw away | 25.3% |
| Raw p home draw | 87.8% |
| Raw p draw away | 31.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.23 |
| Reference draw odds | 7.80 |
| Reference away odds | 16.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -6.5% |
| Draw probability edge | +3.5% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | -16.7% |
| Under 2.5 probability edge | +16.7% |
| Raw edge prob home | -0.1302 |
| Raw ev home | -0.1615 |
| Raw edge prob draw | 0.0693 |
| Raw ev draw | 0.4146 |
| Raw edge prob away | 0.0609 |
| Raw ev away | 0.8963 |
| Market p home draw | 93.4% |
| Market home draw odds | 1.03 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 20.7% |
| Market draw away odds | 4.68 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.03 |
| Market reference dc draw away odds | 4.65 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 86.0% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:59:56Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.1% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:59:56Z |
| Market reference under 3 5 odds | 1.70 |
| Market reference under 3 5 opposite odds | 2.23 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 43.5% |
| Market btts yes odds | 2.11 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 2.28 |
| Market reference btts yes opposite odds | 1.76 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **64.2%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.8%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.8%; Under 3.5 goals: 24.5%; Double Chance 1X: 82.5%; Double Chance X2: 35.8%; Under 4.5 goals: 42.4%; BTTS Yes (both teams score): 78.8%; BTTS No (at least one team does not score): 21.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 64.2% | 1.56 |
| Draw | 18.3% | 5.48 |
| Manchester United win | 17.5% | 5.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 3.73 |
| Manchester United expected goals | 1.54 |
| Expected total goals | 5.27 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 87.8% |
| Under 2.5 | 12.2% |
| Over 3.5 | 75.5% |
| Under 3.5 | 24.5% |
| Over 4.5 | 57.6% |
| Under 4.5 | 42.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.82% |
| 2 | 3-1 | 5.71% |
| 3 | 4-1 | 5.32% |
| 4 | 2-1 | 4.60% |
| 5 | 1-1 | 4.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 64.2% | 51.3% | 1.91 | +22.6% |
| Draw | 18.3% | 25.1% | 3.88 | -29.2% |
| Manchester United win | 17.5% | 23.6% | 4.26 | -25.3% |
| Over 2.5 | 87.8% | 59.8% | 1.74 | +52.8% |
| Under 2.5 | 12.2% | 40.2% | 2.27 | -72.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | a9c22e08b395ee5753c8a65bc0eb97cf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 78.8% |
| P btts no | 21.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 170.12 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.65 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.21 |
| Fair Over 3.5 odds | 1.32 |
| Fair Under 3.5 odds | 4.09 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 77.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 23.0% |
| Raw p btts yes | 76.6% |
| P home draw | 82.5% |
| P draw away | 35.8% |
| Raw p home draw | 88.5% |
| Raw p draw away | 22.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.94 |
| Reference draw odds | 3.95 |
| Reference away odds | 4.20 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +12.9% |
| Draw probability edge | -6.8% |
| Away probability edge | -6.0% |
| Over 2.5 probability edge | +28.0% |
| Under 2.5 probability edge | -28.0% |
| Raw edge prob home | 0.2576 |
| Raw ev home | 0.4724 |
| Raw edge prob draw | -0.1368 |
| Raw ev draw | -0.5572 |
| Raw edge prob away | -0.1209 |
| Raw ev away | -0.5101 |
| Market p home draw | 76.9% |
| Market home draw odds | 1.26 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.7% |
| Market draw away odds | 1.99 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.26 |
| Market reference dc draw away odds | 1.99 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.1% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:59:55Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.4% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:59:55Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.71 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.1% |
| Market btts yes odds | 1.59 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.42 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **68.3%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 77.8%; Under 3.5 goals: 41.7%; Double Chance 1X: 31.7%; Double Chance X2: 83.7%; Under 4.5 goals: 61.0%; BTTS Yes (both teams score): 70.8%; BTTS No (at least one team does not score): 29.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 16.3% | 6.12 |
| Draw | 15.4% | 6.50 |
| Barcelona win | 68.3% | 1.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.53 |
| Barcelona expected goals | 2.51 |
| Expected total goals | 4.04 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 77.8% |
| Under 2.5 | 22.2% |
| Over 3.5 | 58.3% |
| Under 3.5 | 41.7% |
| Over 4.5 | 39.0% |
| Under 4.5 | 61.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.76% |
| 2 | 1-3 | 8.17% |
| 3 | 0-2 | 6.36% |
| 4 | 2-3 | 6.27% |
| 5 | 2-2 | 5.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 16.3% | 9.8% | 9.00 | +47.0% |
| Draw | 15.4% | 12.9% | 6.76 | +4.1% |
| Barcelona win | 68.3% | 77.3% | 1.32 | -9.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | dd431688ed5c8f383b6434fd4f01e883 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.8% |
| P btts no | 29.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 82.18 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.32 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.51 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.40 |
| Fair Over 4.5 odds | 2.56 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.5% |
| Raw p btts yes | 71.7% |
| P home draw | 31.7% |
| P draw away | 83.7% |
| Raw p home draw | 40.8% |
| Raw p draw away | 77.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 10.00 |
| Reference draw odds | 7.60 |
| Reference away odds | 1.29 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.60 |
| Home probability edge | +6.6% |
| Draw probability edge | +2.5% |
| Away probability edge | -9.1% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | 0.1312 |
| Raw ev home | 1.0608 |
| Raw edge prob draw | 0.0499 |
| Raw ev draw | 0.2092 |
| Raw edge prob away | -0.1811 |
| Raw ev away | -0.2184 |
| Market p home draw | 25.7% |
| Market home draw odds | 3.70 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.1% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.75 |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 94.6% |
| Market over 1 5 odds | 1.01 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:57:56Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 7.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 34.8% |
| Market under 3 5 odds | 2.45 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:57:56Z |
| Market reference under 3 5 odds | 2.67 |
| Market reference under 3 5 opposite odds | 1.49 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.41 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 3.10 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **69.9%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 56.4%; Under 3.5 goals: 66.8%; Double Chance 1X: 87.1%; Double Chance X2: 30.1%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 69.9% | 1.43 |
| Draw | 17.2% | 5.82 |
| Club Brugge win | 12.9% | 7.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.92 |
| Club Brugge expected goals | 0.94 |
| Expected total goals | 2.86 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 56.4% |
| Under 2.5 | 43.6% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.22% |
| 2 | 2-0 | 12.11% |
| 3 | 2-1 | 11.44% |
| 4 | 1-1 | 8.13% |
| 5 | 3-0 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 69.9% | 79.2% | 1.27 | -11.2% |
| Draw | 17.2% | 13.6% | 6.76 | +16.2% |
| Club Brugge win | 12.9% | 7.2% | 12.00 | +54.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | ca3f4b075d835413f9cb7bd3c439fdd0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.28 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.63 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.84 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 51.6% |
| P home draw | 87.1% |
| P draw away | 30.1% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.26 |
| Reference draw odds | 7.20 |
| Reference away odds | 13.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.40 |
| Home probability edge | -9.2% |
| Draw probability edge | +3.6% |
| Away probability edge | +5.7% |
| Over 2.5 probability edge | -18.2% |
| Under 2.5 probability edge | +18.2% |
| Raw edge prob home | -0.1848 |
| Raw ev home | -0.2291 |
| Raw edge prob draw | 0.0715 |
| Raw ev draw | 0.4032 |
| Raw edge prob away | 0.1133 |
| Raw ev away | 1.2250 |
| Market p home draw | 91.6% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 23.2% |
| Market draw away odds | 4.14 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 4.15 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 90.5% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:50:21Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 6.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 46.1% |
| Market under 3 5 odds | 2.05 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:50:21Z |
| Market reference under 3 5 odds | 2.10 |
| Market reference under 3 5 opposite odds | 1.81 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.0% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **48.6%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 10.5%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 68.3%; Under 3.5 goals: 53.7%; Double Chance 1X: 68.7%; Double Chance X2: 51.4%; Under 4.5 goals: 72.2%; BTTS Yes (both teams score): 67.7%; BTTS No (at least one team does not score): 32.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 48.6% | 2.06 |
| Draw | 20.1% | 4.97 |
| PSV Eindhoven win | 31.3% | 3.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.65 |
| PSV Eindhoven expected goals | 1.87 |
| Expected total goals | 3.52 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 85.9% |
| Under 1.5 | 14.1% |
| Over 2.5 | 68.3% |
| Under 2.5 | 31.7% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.8% |
| Under 4.5 | 72.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.50% |
| 2 | 1-1 | 8.25% |
| 3 | 1-0 | 7.45% |
| 4 | 2-2 | 6.68% |
| 5 | 1-2 | 6.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 48.6% | 62.3% | 1.61 | -21.7% |
| Draw | 20.1% | 19.0% | 5.08 | +2.1% |
| PSV Eindhoven win | 31.3% | 18.7% | 5.03 | +57.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | da9e9e9eb9a238ed97827c4a8fbe6044 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.7% |
| P btts no | 32.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.90 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.08 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.16 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.60 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 35.0% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 67.8% |
| P home draw | 68.7% |
| P draw away | 51.4% |
| Raw p home draw | 56.2% |
| Raw p draw away | 65.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.60 |
| Reference draw odds | 5.20 |
| Reference away odds | 5.30 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Home probability edge | -13.7% |
| Draw probability edge | +1.1% |
| Away probability edge | +12.6% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | -0.2733 |
| Raw ev home | -0.4369 |
| Raw edge prob draw | 0.0216 |
| Raw ev draw | 0.0762 |
| Raw edge prob away | 0.2517 |
| Raw ev away | 1.2051 |
| Market p home draw | 80.6% |
| Market home draw odds | 1.21 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 38.8% |
| Market draw away odds | 2.46 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.47 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 93.4% |
| Market over 1 5 odds | 1.02 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:53:08Z |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 40.8% |
| Market under 3 5 odds | 2.28 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:53:08Z |
| Market reference under 3 5 odds | 2.35 |
| Market reference under 3 5 opposite odds | 1.65 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 71.1% |
| Market btts yes odds | 1.32 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 3.40 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **41.3%**. Expected goals are 1.28 for RC Lens and 1.60 for Sporting Lisbon (2.89 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 54.5%; Under 3.5 goals: 67.4%; Double Chance 1X: 58.7%; Double Chance X2: 66.2%; Under 4.5 goals: 83.7%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 33.8% | 2.96 |
| Draw | 24.9% | 4.01 |
| Sporting Lisbon win | 41.3% | 2.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.28 |
| Sporting Lisbon expected goals | 1.60 |
| Expected total goals | 2.89 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 54.5% |
| Under 2.5 | 45.5% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.3% |
| Under 4.5 | 83.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.64% |
| 2 | 0-1 | 8.64% |
| 3 | 1-0 | 8.36% |
| 4 | 1-2 | 8.36% |
| 5 | 2-1 | 7.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 33.8% | 36.3% | 2.77 | -6.4% |
| Draw | 24.9% | 26.5% | 3.78 | -5.8% |
| Sporting Lisbon win | 41.3% | 37.2% | 2.57 | +6.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T16:45:00+00:00 |
| Fixture id | 2b0a946cac613732fcbf57ce931490a1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Sporting Clube de Portugal |
| Home-name matching confidence | 86/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.73 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.12 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.2% |
| P home draw | 58.7% |
| P draw away | 66.2% |
| Raw p home draw | 54.6% |
| Raw p draw away | 68.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.74 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.68 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.43 |
| Home probability edge | -2.6% |
| Draw probability edge | -1.6% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | -0.0512 |
| Raw ev home | -0.1354 |
| Raw edge prob draw | -0.0317 |
| Raw ev draw | -0.1177 |
| Raw edge prob away | 0.0829 |
| Raw ev away | 0.1680 |
| Market p home draw | 61.7% |
| Market home draw odds | 1.57 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.2% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.56 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:53:55Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.9% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:53:55Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.7% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.49 |
| Market reference btts yes opposite odds | 2.76 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **55.3%**. Expected goals are 0.38 for Sabah FK and 1.28 for Slavia Praha (1.66 combined). The most likely exact score is 0-1 at 22.8%. Goal-market probabilities: at least one goal: 82.6%; Over 2.5 goals: 23.0%; Under 3.5 goals: 91.6%; Double Chance 1X: 44.7%; Double Chance X2: 82.2%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 22.2%; BTTS No (at least one team does not score): 77.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 17.8% | 5.61 |
| Draw | 26.8% | 3.73 |
| Slavia Praha win | 55.3% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.38 |
| Slavia Praha expected goals | 1.28 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.6% |
| Under 0.5 | 17.4% |
| Over 1.5 | 47.7% |
| Under 1.5 | 52.3% |
| Over 2.5 | 23.0% |
| Under 2.5 | 77.0% |
| Over 3.5 | 8.4% |
| Under 3.5 | 91.6% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.84% |
| 2 | 0-0 | 17.44% |
| 3 | 0-2 | 14.35% |
| 4 | 1-0 | 12.00% |
| 5 | 1-1 | 8.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 17.8% | 24.2% | 3.96 | -29.4% |
| Draw | 26.8% | 25.2% | 3.98 | +6.8% |
| Slavia Praha win | 55.3% | 50.6% | 1.95 | +7.9% |
| Over 2.5 | 23.0% | 61.5% | 1.64 | -62.4% |
| Under 2.5 | 77.0% | 38.5% | 2.46 | +89.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T16:45:00+00:00 |
| Fixture id | 46f726554e6876fb828c767bfbfdfdad |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 22.2% |
| P btts no | 77.8% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.73 |
| Fair Over 1.5 odds | 2.10 |
| Fair Under 1.5 odds | 1.91 |
| Fair Over 2.5 odds | 4.36 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.97 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 38.06 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.4% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 60.1% |
| Raw p over 1 5 | 49.0% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 22.4% |
| P home draw | 44.7% |
| P draw away | 82.2% |
| Raw p home draw | 39.9% |
| Raw p draw away | 88.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 4.10 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.97 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -6.4% |
| Draw probability edge | +1.7% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -38.6% |
| Under 2.5 probability edge | +38.6% |
| Raw edge prob home | -0.1282 |
| Raw ev home | -0.5478 |
| Raw edge prob draw | 0.0335 |
| Raw ev draw | 0.1347 |
| Raw edge prob away | 0.0947 |
| Raw ev away | 0.1714 |
| Market p home draw | 49.8% |
| Market home draw odds | 1.95 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.8% |
| Market draw away odds | 1.29 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.94 |
| Market reference dc draw away odds | 1.29 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 82.8% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.6% |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 61.6% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.56 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **90.8%**. Expected goals are 0.70 for Viking FK and 4.47 for Bayern Munich (5.17 combined). The most likely exact score is 0-4 at 9.2%. Goal-market probabilities: at least one goal: 99.3%; Over 2.5 goals: 87.7%; Under 3.5 goals: 25.5%; Double Chance 1X: 9.2%; Double Chance X2: 96.8%; Under 4.5 goals: 42.8%; BTTS Yes (both teams score): 50.5%; BTTS No (at least one team does not score): 49.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 3.2% | 31.08 |
| Draw | 6.0% | 16.59 |
| Bayern Munich win | 90.8% | 1.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.70 |
| Bayern Munich expected goals | 4.47 |
| Expected total goals | 5.17 |
| Over 0.5 | 99.3% |
| Under 0.5 | 0.7% |
| Over 1.5 | 95.9% |
| Under 1.5 | 4.1% |
| Over 2.5 | 87.7% |
| Under 2.5 | 12.3% |
| Over 3.5 | 74.5% |
| Under 3.5 | 25.5% |
| Over 4.5 | 57.2% |
| Under 4.5 | 42.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.23% |
| 2 | 0-3 | 8.26% |
| 3 | 0-5 | 8.25% |
| 4 | 1-4 | 6.43% |
| 5 | 0-6 | 6.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 3.2% | 4.5% | 19.50 | -37.3% |
| Draw | 6.0% | 7.9% | 12.90 | -22.3% |
| Bayern Munich win | 90.8% | 87.7% | 1.13 | +2.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 8a9d20b23417357011c10585a99335e9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.5% |
| P btts no | 49.5% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 142.57 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 24.56 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.13 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.92 |
| Fair Over 4.5 odds | 1.75 |
| Fair Under 4.5 odds | 2.34 |
| Unadjusted home-win probability | 2.0% |
| Unadjusted draw probability | 4.2% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.4% |
| Raw p btts yes | 49.5% |
| P home draw | 9.2% |
| P draw away | 96.8% |
| Raw p home draw | 6.1% |
| Raw p draw away | 98.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 22.00 |
| Reference draw odds | 12.50 |
| Reference away odds | 1.14 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.50 |
| Home probability edge | -1.2% |
| Draw probability edge | -1.9% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | -0.0249 |
| Raw ev home | -0.6157 |
| Raw edge prob draw | -0.0371 |
| Raw ev draw | -0.4620 |
| Raw edge prob away | 0.0621 |
| Raw ev away | 0.0606 |
| Market p home draw | 14.0% |
| Market home draw odds | 7.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 94.3% |
| Market draw away odds | 1.03 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 6.85 |
| Market reference dc draw away odds | 1.02 |
| Market reference dc home away odds | 1.05 |
| Market p over 1 5 | 95.8% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:56:21Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 8.60 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 31.1% |
| Market under 3 5 odds | 2.72 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:56:21Z |
| Market reference under 3 5 odds | 2.75 |
| Market reference under 3 5 opposite odds | 1.38 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.1% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.42 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **38.5%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.7%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 40.0%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.5%; Double Chance X2: 64.7%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 44.6%; BTTS No (at least one team does not score): 55.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 35.3% | 2.83 |
| Draw | 26.2% | 3.82 |
| Napoli win | 38.5% | 2.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.90 |
| Napoli expected goals | 1.42 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 65.6% |
| Under 1.5 | 34.4% |
| Over 2.5 | 40.0% |
| Under 2.5 | 60.0% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.71% |
| 2 | 1-1 | 12.11% |
| 3 | 0-1 | 11.33% |
| 4 | 0-0 | 9.39% |
| 5 | 2-1 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 35.3% | 46.2% | 2.15 | -24.1% |
| Draw | 26.2% | 26.5% | 3.76 | -1.6% |
| Napoli win | 38.5% | 27.3% | 3.50 | +34.8% |
| Over 2.5 | 40.0% | 58.1% | 1.72 | -31.1% |
| Under 2.5 | 60.0% | 41.9% | 2.30 | +37.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 09e41b63d1d59bd4d971c54ffce154d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.6% |
| P btts no | 55.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.66 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.09 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.14 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 44.3% |
| P home draw | 61.5% |
| P draw away | 64.7% |
| Raw p home draw | 50.2% |
| Raw p draw away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.16 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.65 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -10.9% |
| Draw probability edge | -0.4% |
| Away probability edge | +11.2% |
| Over 2.5 probability edge | -18.1% |
| Under 2.5 probability edge | +18.1% |
| Raw edge prob home | -0.2172 |
| Raw ev home | -0.4743 |
| Raw edge prob draw | -0.0075 |
| Raw ev draw | -0.0301 |
| Raw edge prob away | 0.2248 |
| Raw ev away | 0.7414 |
| Market p home draw | 72.1% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.2% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 81.1% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:47:56Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.5% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:47:56Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.72 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **49.6%**. Expected goals are 1.18 for AS Roma and 1.67 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 54.1%; Under 3.5 goals: 67.9%; Double Chance 1X: 50.4%; Double Chance X2: 73.4%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 56.0%; BTTS No (at least one team does not score): 44.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.6% | 3.76 |
| Draw | 23.8% | 4.19 |
| Real Madrid win | 49.6% | 2.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.18 |
| Real Madrid expected goals | 1.67 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.20% |
| 2 | 0-1 | 10.22% |
| 3 | 1-2 | 9.54% |
| 4 | 0-2 | 8.08% |
| 5 | 1-0 | 7.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.6% | 25.6% | 3.85 | +2.3% |
| Draw | 23.8% | 24.7% | 4.16 | -0.8% |
| Real Madrid win | 49.6% | 49.7% | 1.94 | -3.8% |

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
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.0% |
| P btts no | 44.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.62 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.40 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.12 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.24 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 27.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 49.5% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.0% |
| Raw p btts yes | 55.7% |
| P home draw | 50.4% |
| P draw away | 73.4% |
| Raw p home draw | 50.5% |
| Raw p draw away | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.85 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Home probability edge | +0.9% |
| Draw probability edge | -0.8% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -14.8% |
| Under 2.5 probability edge | +14.8% |
| Raw edge prob home | 0.0186 |
| Raw ev home | 0.0591 |
| Raw edge prob draw | -0.0166 |
| Raw ev draw | -0.0424 |
| Raw edge prob away | -0.0020 |
| Raw ev away | -0.0403 |
| Market p home draw | 49.6% |
| Market home draw odds | 1.96 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.3% |
| Market draw away odds | 1.30 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.95 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:49:06Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.4% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:49:06Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.0% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 3.05 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **67.3%**. Expected goals are 2.23 for Aston Villa and 0.61 for Fenerbahce (2.84 combined). The most likely exact score is 2-0 at 13.1%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 51.7%; Under 3.5 goals: 69.8%; Double Chance 1X: 86.8%; Double Chance X2: 32.7%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 41.6%; BTTS No (at least one team does not score): 58.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 67.3% | 1.49 |
| Draw | 19.6% | 5.11 |
| Fenerbahce win | 13.2% | 7.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.23 |
| Fenerbahce expected goals | 0.61 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 51.7% |
| Under 2.5 | 48.3% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.07% |
| 2 | 1-0 | 12.07% |
| 3 | 3-0 | 9.73% |
| 4 | 1-1 | 9.15% |
| 5 | 2-1 | 7.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 67.3% | 59.7% | 1.69 | +13.7% |
| Draw | 19.6% | 23.0% | 4.26 | -16.7% |
| Fenerbahce win | 13.2% | 17.3% | 5.33 | -29.9% |
| Over 2.5 | 51.7% | 58.3% | 1.69 | -12.6% |
| Under 2.5 | 48.3% | 41.7% | 2.36 | +13.9% |

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
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
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
| P btts yes | 41.6% |
| P btts no | 58.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.12 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.09 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.74 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.1% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 40.3% |
| P home draw | 86.8% |
| P draw away | 32.7% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.67 |
| Reference draw odds | 4.30 |
| Reference away odds | 5.70 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | +7.6% |
| Draw probability edge | -3.5% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | 0.1525 |
| Raw ev home | 0.2660 |
| Raw edge prob draw | -0.0690 |
| Raw ev draw | -0.3137 |
| Raw edge prob away | -0.0834 |
| Raw ev away | -0.5213 |
| Market p home draw | 81.7% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 41.7% |
| Market draw away odds | 2.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.18 |
| Market reference dc draw away odds | 2.31 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 82.1% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.6% |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.54 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.7% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **44.7%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 70.5%; Under 3.5 goals: 50.0%; Double Chance 1X: 55.3%; Double Chance X2: 66.9%; Under 4.5 goals: 69.6%; BTTS Yes (both teams score): 70.3%; BTTS No (at least one team does not score): 29.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 33.1% | 3.02 |
| Draw | 22.2% | 4.50 |
| Borussia Dortmund win | 44.7% | 2.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 1.73 |
| Borussia Dortmund expected goals | 1.94 |
| Expected total goals | 3.67 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 70.5% |
| Under 2.5 | 29.5% |
| Over 3.5 | 50.0% |
| Under 3.5 | 50.0% |
| Over 4.5 | 30.4% |
| Under 4.5 | 69.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.71% |
| 2 | 1-2 | 8.48% |
| 3 | 2-2 | 7.68% |
| 4 | 2-1 | 6.90% |
| 5 | 0-1 | 5.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 33.1% | 30.6% | 3.29 | +8.8% |
| Draw | 22.2% | 23.7% | 4.11 | -8.7% |
| Borussia Dortmund win | 44.7% | 45.7% | 2.14 | -4.3% |

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
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
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
| Fair Under 0.5 odds | 43.94 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.40 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.29 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 35.5% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 50.1% |
| Raw p btts yes | 70.0% |
| P home draw | 55.3% |
| P draw away | 66.9% |
| Raw p home draw | 56.2% |
| Raw p draw away | 64.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.25 |
| Reference draw odds | 4.20 |
| Reference away odds | 2.18 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +2.4% |
| Draw probability edge | -1.5% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +1.5% |
| Under 2.5 probability edge | -1.5% |
| Raw edge prob home | 0.0489 |
| Raw ev home | 0.1680 |
| Raw edge prob draw | -0.0292 |
| Raw ev draw | -0.1472 |
| Raw edge prob away | -0.0197 |
| Raw ev away | -0.0637 |
| Market p home draw | 53.8% |
| Market home draw odds | 1.79 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.3% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.79 |
| Market reference dc draw away odds | 1.37 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 88.2% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.90 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 51.8% |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 69.7% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.42 |
| Market reference btts yes opposite odds | 3.20 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **62.3%**. Expected goals are 1.82 for Feyenoord and 3.81 for Como (5.63 combined). The most likely exact score is 2-2 at 6.2%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.8%; Under 3.5 goals: 19.7%; Double Chance 1X: 37.7%; Double Chance X2: 79.8%; Under 4.5 goals: 35.9%; BTTS Yes (both teams score): 83.3%; BTTS No (at least one team does not score): 16.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 20.2% | 4.94 |
| Draw | 17.4% | 5.74 |
| Como win | 62.3% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 1.82 |
| Como expected goals | 3.81 |
| Expected total goals | 5.63 |
| Over 0.5 | 99.7% |
| Under 0.5 | 0.3% |
| Over 1.5 | 97.3% |
| Under 1.5 | 2.7% |
| Over 2.5 | 90.8% |
| Under 2.5 | 9.2% |
| Over 3.5 | 80.3% |
| Under 3.5 | 19.7% |
| Over 4.5 | 64.1% |
| Under 4.5 | 35.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.18% |
| 2 | 1-3 | 5.10% |
| 3 | 1-4 | 4.87% |
| 4 | 3-3 | 4.76% |
| 5 | 2-3 | 4.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 20.2% | 26.3% | 3.58 | -27.6% |
| Draw | 17.4% | 22.7% | 4.32 | -24.7% |
| Como win | 62.3% | 51.0% | 1.98 | +23.4% |

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
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 83.3% |
| P btts no | 16.7% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 297.67 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 36.92 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.93 |
| Fair Over 3.5 odds | 1.25 |
| Fair Under 3.5 odds | 5.07 |
| Fair Over 4.5 odds | 1.56 |
| Fair Under 4.5 odds | 2.79 |
| Unadjusted home-win probability | 14.2% |
| Unadjusted draw probability | 12.2% |
| Unadjusted away-win probability | 73.7% |
| Raw p over 1 5 | 97.5% |
| Raw p under 3 5 | 18.8% |
| Raw p btts yes | 81.8% |
| P home draw | 37.7% |
| P draw away | 79.8% |
| Raw p home draw | 26.3% |
| Raw p draw away | 85.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.80 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.96 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -6.1% |
| Draw probability edge | -5.3% |
| Away probability edge | +11.3% |
| Over 2.5 probability edge | +22.3% |
| Under 2.5 probability edge | -22.3% |
| Raw edge prob home | -0.1213 |
| Raw ev home | -0.4928 |
| Raw edge prob draw | -0.1054 |
| Raw ev draw | -0.4745 |
| Raw edge prob away | 0.2267 |
| Raw ev away | 0.4586 |
| Market p home draw | 50.5% |
| Market home draw odds | 1.92 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.5% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.91 |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 87.8% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:59:31Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.4% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:59:31Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.4% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.98 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **71.5%**. Expected goals are 0.28 for LASK and 1.45 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 27.4%. Goal-market probabilities: at least one goal: 86.0%; Over 2.5 goals: 26.5%; Under 3.5 goals: 89.8%; Double Chance 1X: 28.5%; Double Chance X2: 91.6%; Under 4.5 goals: 96.6%; BTTS Yes (both teams score): 17.7%; BTTS No (at least one team does not score): 82.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 8.4% | 11.97 |
| Draw | 20.2% | 4.95 |
| Liverpool win | 71.5% | 1.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.45 |
| Expected total goals | 1.74 |
| Over 0.5 | 86.0% |
| Under 0.5 | 14.0% |
| Over 1.5 | 52.5% |
| Under 1.5 | 47.5% |
| Over 2.5 | 26.5% |
| Under 2.5 | 73.5% |
| Over 3.5 | 10.2% |
| Under 3.5 | 89.8% |
| Over 4.5 | 3.4% |
| Under 4.5 | 96.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 27.38% |
| 2 | 0-2 | 19.64% |
| 3 | 0-0 | 14.00% |
| 4 | 0-3 | 9.52% |
| 5 | 1-0 | 6.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 8.4% | 9.4% | 9.10 | -24.0% |
| Draw | 20.2% | 15.5% | 6.24 | +26.0% |
| Liverpool win | 71.5% | 75.1% | 1.34 | -4.2% |

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
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 17.7% |
| P btts no | 82.3% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.14 |
| Fair Over 1.5 odds | 1.90 |
| Fair Under 1.5 odds | 2.11 |
| Fair Over 2.5 odds | 3.77 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 9.78 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 29.68 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 67.8% |
| Raw p over 1 5 | 51.4% |
| Raw p under 3 5 | 90.1% |
| Raw p btts yes | 18.5% |
| P home draw | 28.5% |
| P draw away | 91.6% |
| Raw p home draw | 32.2% |
| Raw p draw away | 92.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 10.50 |
| Reference draw odds | 6.40 |
| Reference away odds | 1.33 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -1.1% |
| Draw probability edge | +4.7% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -45.1% |
| Under 2.5 probability edge | +45.1% |
| Raw edge prob home | -0.0213 |
| Raw ev home | -0.3368 |
| Raw edge prob draw | 0.0940 |
| Raw ev draw | 0.5529 |
| Raw edge prob away | -0.0726 |
| Raw ev away | -0.0911 |
| Market p home draw | 26.8% |
| Market home draw odds | 3.56 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.3% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.60 |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 88.7% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:53:56Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.6% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:53:56Z |
| Market reference under 3 5 odds | 1.88 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.0% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **44.1%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 69.1%; Under 3.5 goals: 51.9%; Double Chance 1X: 55.9%; Double Chance X2: 65.6%; Under 4.5 goals: 71.1%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 34.4% | 2.90 |
| Draw | 21.5% | 4.66 |
| Paris Saint Germain win | 44.1% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.40 |
| Paris Saint Germain expected goals | 2.23 |
| Expected total goals | 3.63 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 69.1% |
| Under 2.5 | 30.9% |
| Over 3.5 | 48.1% |
| Under 3.5 | 51.9% |
| Over 4.5 | 28.9% |
| Under 4.5 | 71.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.73% |
| 2 | 2-1 | 8.31% |
| 3 | 2-2 | 7.19% |
| 4 | 1-2 | 7.18% |
| 5 | 1-0 | 5.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 34.4% | 44.8% | 2.23 | -23.2% |
| Draw | 21.5% | 23.6% | 4.11 | -11.8% |
| Paris Saint Germain win | 44.1% | 31.5% | 3.08 | +35.9% |

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
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.9% |
| P btts no | 32.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.32 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.52 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.24 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.46 |
| Fair Under 4.5 odds | 1.41 |
| Unadjusted home-win probability | 24.0% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 56.7% |
| Raw p over 1 5 | 87.3% |
| Raw p under 3 5 | 50.8% |
| Raw p btts yes | 66.9% |
| P home draw | 55.9% |
| P draw away | 65.6% |
| Raw p home draw | 43.3% |
| Raw p draw away | 76.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.22 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -10.4% |
| Draw probability edge | -2.2% |
| Away probability edge | +12.6% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | -0.2082 |
| Raw ev home | -0.4643 |
| Raw edge prob draw | -0.0432 |
| Raw ev draw | -0.2068 |
| Raw edge prob away | 0.2514 |
| Raw ev away | 0.7457 |
| Market p home draw | 67.9% |
| Market home draw odds | 1.43 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.1% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.42 |
| Market reference dc draw away odds | 1.72 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 86.6% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.20 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 55.1% |
| Market reference under 3 5 odds | 1.76 |
| Market reference under 3 5 opposite odds | 2.14 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 67.4% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.98 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **62.0%**. Expected goals are 3.29 for Real Betis and 1.29 for Porto (4.58 combined). The most likely exact score is 2-2 at 7.0%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 81.1%; Under 3.5 goals: 35.0%; Double Chance 1X: 80.8%; Double Chance X2: 38.0%; Under 4.5 goals: 54.7%; BTTS Yes (both teams score): 72.2%; BTTS No (at least one team does not score): 27.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 62.0% | 1.61 |
| Draw | 18.8% | 5.32 |
| Porto win | 19.2% | 5.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 3.29 |
| Porto expected goals | 1.29 |
| Expected total goals | 4.58 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 93.3% |
| Under 1.5 | 6.7% |
| Over 2.5 | 81.1% |
| Under 2.5 | 18.9% |
| Over 3.5 | 65.0% |
| Under 3.5 | 35.0% |
| Over 4.5 | 45.3% |
| Under 4.5 | 54.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.99% |
| 2 | 3-1 | 6.40% |
| 3 | 1-1 | 6.25% |
| 4 | 2-1 | 5.83% |
| 5 | 4-1 | 5.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 62.0% | 47.9% | 2.16 | +34.0% |
| Draw | 18.8% | 25.2% | 3.76 | -29.3% |
| Porto win | 19.2% | 26.9% | 3.50 | -32.9% |
| Over 2.5 | 81.1% | 57.6% | 1.79 | +45.1% |
| Under 2.5 | 18.9% | 42.4% | 2.19 | -58.6% |

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
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
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
| P btts yes | 72.2% |
| P btts no | 27.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 82.03 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.88 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.29 |
| Fair Over 3.5 odds | 1.54 |
| Fair Under 3.5 odds | 2.86 |
| Fair Over 4.5 odds | 2.21 |
| Fair Under 4.5 odds | 1.83 |
| Unadjusted home-win probability | 76.1% |
| Unadjusted draw probability | 12.4% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 94.1% |
| Raw p under 3 5 | 32.9% |
| Raw p btts yes | 69.6% |
| P home draw | 80.8% |
| P draw away | 38.0% |
| Raw p home draw | 88.6% |
| Raw p draw away | 23.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.08 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +14.1% |
| Draw probability edge | -6.4% |
| Away probability edge | -7.7% |
| Over 2.5 probability edge | +23.5% |
| Under 2.5 probability edge | -23.5% |
| Raw edge prob home | 0.2818 |
| Raw ev home | 0.6441 |
| Raw edge prob draw | -0.1274 |
| Raw ev draw | -0.5324 |
| Raw edge prob away | -0.1544 |
| Raw ev away | -0.5993 |
| Market p home draw | 72.2% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.9% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 80.1% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:56:46Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.6% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:56:46Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.6% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.35 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.5%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 50.9%; Under 3.5 goals: 70.6%; Double Chance 1X: 65.7%; Double Chance X2: 60.5%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.5% | 2.53 |
| Draw | 26.2% | 3.82 |
| AEK Athens win | 34.3% | 2.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.49 |
| AEK Athens expected goals | 1.25 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.36% |
| 2 | 1-0 | 9.33% |
| 3 | 0-1 | 9.16% |
| 4 | 2-1 | 8.17% |
| 5 | 1-2 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.5% | 35.8% | 2.73 | +7.9% |
| Draw | 26.2% | 28.1% | 3.47 | -9.2% |
| AEK Athens win | 34.3% | 36.1% | 2.77 | -5.0% |
| Over 2.5 | 50.9% | 50.4% | 1.95 | -0.7% |
| Under 2.5 | 49.1% | 49.6% | 1.99 | -2.4% |

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
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
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
| P btts yes | 55.3% |
| P btts no | 44.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.78 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.41 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.12 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 54.7% |
| P home draw | 65.7% |
| P draw away | 60.5% |
| Raw p home draw | 67.4% |
| Raw p draw away | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.76 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.74 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.91 |
| Home probability edge | +3.7% |
| Draw probability edge | -2.0% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0744 |
| Raw ev home | 0.1804 |
| Raw edge prob draw | -0.0395 |
| Raw ev draw | -0.1604 |
| Raw edge prob away | -0.0349 |
| Raw ev away | -0.0979 |
| Market p home draw | 63.5% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:32Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.4% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:32Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.52 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 75.6% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:57:33Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:57:33Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.30 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.26 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **65.4%**. Expected goals are 1.46 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.6%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 72.5%; Under 3.5 goals: 48.5%; Double Chance 1X: 34.6%; Double Chance X2: 82.7%; Under 4.5 goals: 67.8%; BTTS Yes (both teams score): 67.4%; BTTS No (at least one team does not score): 32.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.3% | 5.79 |
| Draw | 17.3% | 5.79 |
| VfB Stuttgart win | 65.4% | 1.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.46 |
| VfB Stuttgart expected goals | 2.25 |
| Expected total goals | 3.71 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 72.5% |
| Under 2.5 | 27.5% |
| Over 3.5 | 51.5% |
| Under 3.5 | 48.5% |
| Over 4.5 | 32.2% |
| Under 4.5 | 67.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.60% |
| 2 | 1-3 | 7.95% |
| 3 | 0-2 | 7.28% |
| 4 | 0-1 | 6.94% |
| 5 | 1-1 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.3% | 9.7% | 10.00 | +72.8% |
| Draw | 17.3% | 15.3% | 6.48 | +12.0% |
| VfB Stuttgart win | 65.4% | 74.9% | 1.31 | -14.3% |

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
| Market best home last update utc | 2026-10-13T15:59:35Z |
| Market best draw last update utc | 2026-10-13T15:59:35Z |
| Market best away last update utc | 2026-10-13T15:59:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.4% |
| P btts no | 32.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 54.21 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.65 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.63 |
| Fair Over 3.5 odds | 1.94 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.10 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 24.8% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 55.9% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 68.2% |
| P home draw | 34.6% |
| P draw away | 82.7% |
| Raw p home draw | 44.1% |
| Raw p draw away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 10.00 |
| Reference draw odds | 6.40 |
| Reference away odds | 1.33 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Home probability edge | +7.5% |
| Draw probability edge | +2.0% |
| Away probability edge | -9.5% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.1507 |
| Raw ev home | 1.4815 |
| Raw edge prob draw | 0.0395 |
| Raw ev draw | 0.2477 |
| Raw edge prob away | -0.1902 |
| Raw ev away | -0.2673 |
| Market p home draw | 25.4% |
| Market home draw odds | 3.78 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T15:59:35Z |
| Market reference home draw last update utc | 2026-10-13T16:01:32Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.0% |
| Market draw away odds | 1.06 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T15:59:35Z |
| Market reference draw away last update utc | 2026-10-13T16:01:32Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.82 |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 88.4% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T15:47:57Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 7.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 50.0% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T15:47:57Z |
| Market reference under 3 5 odds | 1.93 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.3% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T15:59:35Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.27 |
| Market btts yes bookmakers | 1 |

</details>


---
