# UEFA Champions League — football model report

Fixtures in this report: **16**.

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
| Training data health | {'completed_matches': 18, 'latest_completed_utc': '2026-09-10T19:00:00+00:00', 'latest_completed_date': '2026-09-10', 'next_fixture_utc': '2026-10-13T19:00:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-13T17:02:19.256645+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'fea3971722f92230769c305892f2c9a5f7ce324e0b308cc50bd1d2051e3b8d3d', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0005271069444444445, 'training_end': '2026-09-10', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 16.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 16.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 16.00 |
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

The model's most likely 1X2 outcome is **Arsenal win** at **74.8%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.5%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 49.5%; Under 3.5 goals: 73.0%; Double Chance 1X: 91.1%; Double Chance X2: 25.2%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 39.4%; BTTS No (at least one team does not score): 60.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 74.8% | 1.34 |
| Draw | 16.4% | 6.11 |
| Lille win | 8.9% | 11.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.93 |
| Lille expected goals | 0.65 |
| Expected total goals | 2.58 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.50% |
| 2 | 2-0 | 15.42% |
| 3 | 2-1 | 10.08% |
| 4 | 3-0 | 9.91% |
| 5 | 1-1 | 7.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 74.8% | 81.4% | 1.21 | -9.5% |
| Draw | 16.4% | 13.2% | 7.65 | +25.3% |
| Lille win | 8.9% | 5.5% | 17.00 | +50.6% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
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
| Fair Under 0.5 odds | 16.90 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.70 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.88 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 72.5% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 40.6% |
| P home draw | 91.1% |
| P draw away | 25.2% |
| Raw p home draw | 87.8% |
| Raw p draw away | 31.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.20 |
| Reference draw odds | 6.00 |
| Reference away odds | 13.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -6.6% |
| Draw probability edge | +3.2% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -16.8% |
| Under 2.5 probability edge | +16.8% |
| Raw edge prob home | -0.1318 |
| Raw ev home | -0.1751 |
| Raw edge prob draw | 0.0643 |
| Raw ev draw | 0.4989 |
| Raw edge prob away | 0.0675 |
| Raw ev away | 1.0798 |
| Market p home draw | 94.1% |
| Market home draw odds | 1.03 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:23Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 19.2% |
| Market draw away odds | 5.00 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:23Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.04 |
| Market reference dc draw away odds | 5.09 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 84.9% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T17:00:58Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.3% |
| Market under 3 5 odds | 1.74 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T17:00:58Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.23 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 42.3% |
| Market btts yes odds | 2.16 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 2.25 |
| Market reference btts yes opposite odds | 1.68 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **64.2%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.9%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.8%; Under 3.5 goals: 24.4%; Double Chance 1X: 82.8%; Double Chance X2: 35.8%; Under 4.5 goals: 42.5%; BTTS Yes (both teams score): 78.8%; BTTS No (at least one team does not score): 21.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 64.2% | 1.56 |
| Draw | 18.6% | 5.38 |
| Manchester United win | 17.2% | 5.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 3.73 |
| Manchester United expected goals | 1.54 |
| Expected total goals | 5.27 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.3% |
| Under 1.5 | 3.7% |
| Over 2.5 | 87.8% |
| Under 2.5 | 12.2% |
| Over 3.5 | 75.6% |
| Under 3.5 | 24.4% |
| Over 4.5 | 57.5% |
| Under 4.5 | 42.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.94% |
| 2 | 3-1 | 5.72% |
| 3 | 4-1 | 5.32% |
| 4 | 2-1 | 4.60% |
| 5 | 1-1 | 4.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 64.2% | 51.4% | 1.91 | +22.7% |
| Draw | 18.6% | 25.7% | 3.88 | -27.9% |
| Manchester United win | 17.2% | 22.9% | 4.26 | -26.7% |
| Over 2.5 | 87.8% | 57.4% | 1.74 | +52.7% |
| Under 2.5 | 12.2% | 42.6% | 2.27 | -72.3% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
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
| Fair Under 0.5 odds | 167.12 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.77 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.18 |
| Fair Over 3.5 odds | 1.32 |
| Fair Under 3.5 odds | 4.09 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.35 |
| Unadjusted home-win probability | 77.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 23.0% |
| Raw p btts yes | 76.6% |
| P home draw | 82.8% |
| P draw away | 35.8% |
| Raw p home draw | 88.5% |
| Raw p draw away | 22.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.85 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.90 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +12.9% |
| Draw probability edge | -7.2% |
| Away probability edge | -5.7% |
| Over 2.5 probability edge | +30.4% |
| Under 2.5 probability edge | -30.4% |
| Raw edge prob home | 0.2573 |
| Raw ev home | 0.4724 |
| Raw edge prob draw | -0.1433 |
| Raw ev draw | -0.5572 |
| Raw edge prob away | -0.1140 |
| Raw ev away | -0.5101 |
| Market p home draw | 75.4% |
| Market home draw odds | 1.26 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.8% |
| Market draw away odds | 1.99 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.26 |
| Market reference dc draw away odds | 1.91 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T16:47:47Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T16:47:47Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.3% |
| Market btts yes odds | 1.59 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.44 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **68.4%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 77.8%; Under 3.5 goals: 41.7%; Double Chance 1X: 31.6%; Double Chance X2: 83.9%; Under 4.5 goals: 61.0%; BTTS Yes (both teams score): 70.8%; BTTS No (at least one team does not score): 29.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 16.1% | 6.19 |
| Draw | 15.5% | 6.47 |
| Barcelona win | 68.4% | 1.46 |

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
| 1 | 1-2 | 9.78% |
| 2 | 1-3 | 8.18% |
| 3 | 0-2 | 6.37% |
| 4 | 2-3 | 6.28% |
| 5 | 2-2 | 5.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 16.1% | 9.4% | 9.00 | +45.3% |
| Draw | 15.5% | 13.0% | 6.76 | +4.5% |
| Barcelona win | 68.4% | 77.6% | 1.32 | -9.7% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
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
| Fair Under 0.5 odds | 81.84 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.33 |
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
| P home draw | 31.6% |
| P draw away | 83.9% |
| Raw p home draw | 40.8% |
| Raw p draw away | 77.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 8.00 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.25 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.60 |
| Home probability edge | +6.8% |
| Draw probability edge | +2.4% |
| Away probability edge | -9.2% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | 0.1351 |
| Raw ev home | 1.0608 |
| Raw edge prob draw | 0.0486 |
| Raw ev draw | 0.2092 |
| Raw edge prob away | -0.1837 |
| Raw ev away | -0.2184 |
| Market p home draw | 25.7% |
| Market home draw odds | 3.70 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 88.4% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.72 |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 94.6% |
| Market over 1 5 odds | 1.01 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T17:00:31Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 7.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 35.9% |
| Market under 3 5 odds | 2.45 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T17:00:31Z |
| Market reference under 3 5 odds | 2.43 |
| Market reference under 3 5 opposite odds | 1.47 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.7% |
| Market btts yes odds | 1.41 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 3.15 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **70.2%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 56.5%; Under 3.5 goals: 66.7%; Double Chance 1X: 87.1%; Double Chance X2: 29.8%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.2% | 1.42 |
| Draw | 16.9% | 5.92 |
| Club Brugge win | 12.9% | 7.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.92 |
| Club Brugge expected goals | 0.94 |
| Expected total goals | 2.86 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 56.5% |
| Under 2.5 | 43.5% |
| Over 3.5 | 33.3% |
| Under 3.5 | 66.7% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.27% |
| 2 | 2-0 | 12.16% |
| 3 | 2-1 | 11.48% |
| 4 | 1-1 | 7.99% |
| 5 | 3-0 | 7.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.2% | 79.7% | 1.27 | -10.8% |
| Draw | 16.9% | 13.0% | 6.76 | +14.1% |
| Club Brugge win | 12.9% | 7.3% | 12.00 | +54.8% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.2% |
| P btts no | 49.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.70 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.63 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.82 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 51.6% |
| P home draw | 87.1% |
| P draw away | 29.8% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.22 |
| Reference draw odds | 6.00 |
| Reference away odds | 10.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.40 |
| Home probability edge | -9.5% |
| Draw probability edge | +3.9% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -18.1% |
| Under 2.5 probability edge | +18.1% |
| Raw edge prob home | -0.1904 |
| Raw ev home | -0.2291 |
| Raw edge prob draw | 0.0776 |
| Raw ev draw | 0.4032 |
| Raw edge prob away | 0.1128 |
| Raw ev away | 1.2250 |
| Market p home draw | 91.3% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.4% |
| Market draw away odds | 4.14 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 4.28 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 91.4% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 6.40 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 45.5% |
| Market reference under 3 5 odds | 1.99 |
| Market reference under 3 5 opposite odds | 1.70 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.9% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.36 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **49.5%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 10.7%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 68.4%; Under 3.5 goals: 53.7%; Double Chance 1X: 69.1%; Double Chance X2: 50.5%; Under 4.5 goals: 72.2%; BTTS Yes (both teams score): 67.6%; BTTS No (at least one team does not score): 32.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 49.5% | 2.02 |
| Draw | 19.6% | 5.10 |
| PSV Eindhoven win | 30.9% | 3.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.65 |
| PSV Eindhoven expected goals | 1.87 |
| Expected total goals | 3.52 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 85.9% |
| Under 1.5 | 14.1% |
| Over 2.5 | 68.4% |
| Under 2.5 | 31.6% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.8% |
| Under 4.5 | 72.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.69% |
| 2 | 1-1 | 8.05% |
| 3 | 1-0 | 7.59% |
| 4 | 2-2 | 6.52% |
| 5 | 1-2 | 6.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 49.5% | 64.1% | 1.57 | -22.2% |
| Draw | 19.6% | 18.1% | 5.28 | +3.6% |
| PSV Eindhoven win | 30.9% | 17.9% | 5.28 | +62.9% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.6% |
| P btts no | 32.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.92 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.07 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.17 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.59 |
| Fair Under 4.5 odds | 1.39 |
| Unadjusted home-win probability | 35.0% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 67.8% |
| P home draw | 69.1% |
| P draw away | 50.5% |
| Raw p home draw | 56.2% |
| Raw p draw away | 65.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.50 |
| Reference draw odds | 4.75 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.00 |
| Home probability edge | -14.5% |
| Draw probability edge | +1.6% |
| Away probability edge | +13.0% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | -0.2909 |
| Raw ev home | -0.4509 |
| Raw edge prob draw | 0.0312 |
| Raw ev draw | 0.1185 |
| Raw edge prob away | 0.2598 |
| Raw ev away | 1.3146 |
| Market p home draw | 80.7% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 37.8% |
| Market draw away odds | 2.57 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.18 |
| Market reference dc draw away odds | 2.52 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 93.4% |
| Market over 1 5 odds | 1.01 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T16:58:03Z |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 41.1% |
| Market under 3 5 odds | 2.36 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T16:58:03Z |
| Market reference under 3 5 odds | 2.18 |
| Market reference under 3 5 opposite odds | 1.59 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 71.3% |
| Market btts yes odds | 1.31 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 3.45 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **91.2%**. Expected goals are 0.70 for Viking FK and 4.47 for Bayern Munich (5.17 combined). The most likely exact score is 0-4 at 9.3%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.9%; Under 3.5 goals: 25.4%; Double Chance 1X: 8.8%; Double Chance X2: 96.8%; Under 4.5 goals: 42.5%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 3.2% | 31.52 |
| Draw | 5.6% | 17.92 |
| Bayern Munich win | 91.2% | 1.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.70 |
| Bayern Munich expected goals | 4.47 |
| Expected total goals | 5.17 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.0% |
| Under 1.5 | 4.0% |
| Over 2.5 | 87.9% |
| Under 2.5 | 12.1% |
| Over 3.5 | 74.6% |
| Under 3.5 | 25.4% |
| Over 4.5 | 57.5% |
| Under 4.5 | 42.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.28% |
| 2 | 0-3 | 8.31% |
| 3 | 0-5 | 8.29% |
| 4 | 1-4 | 6.47% |
| 5 | 0-6 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 3.2% | 4.4% | 19.50 | -38.1% |
| Draw | 5.6% | 7.0% | 12.90 | -28.0% |
| Bayern Munich win | 91.2% | 88.6% | 1.13 | +3.1% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 154.01 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 24.86 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.26 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.94 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.35 |
| Unadjusted home-win probability | 2.0% |
| Unadjusted draw probability | 4.2% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.4% |
| Raw p btts yes | 49.5% |
| P home draw | 8.8% |
| P draw away | 96.8% |
| Raw p home draw | 6.1% |
| Raw p draw away | 98.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 15.00 |
| Reference draw odds | 10.00 |
| Reference away odds | 1.11 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.50 |
| Home probability edge | -1.2% |
| Draw probability edge | -1.4% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | +2.5% |
| Under 2.5 probability edge | -2.5% |
| Raw edge prob home | -0.0240 |
| Raw ev home | -0.6157 |
| Raw edge prob draw | -0.0282 |
| Raw ev draw | -0.4620 |
| Raw edge prob away | 0.0522 |
| Raw ev away | 0.0606 |
| Market p home draw | 13.9% |
| Market home draw odds | 7.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 94.8% |
| Market draw away odds | 1.03 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 7.05 |
| Market reference dc draw away odds | 1.03 |
| Market reference dc home away odds | 1.07 |
| Market p over 1 5 | 95.8% |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 8.60 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 31.1% |
| Market reference under 3 5 odds | 2.75 |
| Market reference under 3 5 opposite odds | 1.38 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 59.3% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.44 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **38.9%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.6%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 40.1%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.1%; Double Chance X2: 64.9%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 44.5%; BTTS No (at least one team does not score): 55.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 35.1% | 2.85 |
| Draw | 26.0% | 3.84 |
| Napoli win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.90 |
| Napoli expected goals | 1.42 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 65.6% |
| Under 1.5 | 34.4% |
| Over 2.5 | 40.1% |
| Under 2.5 | 59.9% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.61% |
| 2 | 1-1 | 12.05% |
| 3 | 0-1 | 11.44% |
| 4 | 0-0 | 9.34% |
| 5 | 2-1 | 8.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 35.1% | 45.7% | 2.15 | -24.6% |
| Draw | 26.0% | 26.3% | 3.76 | -2.1% |
| Napoli win | 38.9% | 28.1% | 3.50 | +36.2% |
| Over 2.5 | 40.1% | 56.9% | 1.72 | -31.0% |
| Under 2.5 | 59.9% | 43.1% | 2.30 | +37.8% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.5% |
| P btts no | 55.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.71 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.11 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 44.3% |
| P home draw | 61.1% |
| P draw away | 64.9% |
| Raw p home draw | 50.2% |
| Raw p draw away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.05 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -10.6% |
| Draw probability edge | -0.2% |
| Away probability edge | +10.8% |
| Over 2.5 probability edge | -16.8% |
| Under 2.5 probability edge | +16.8% |
| Raw edge prob home | -0.2121 |
| Raw ev home | -0.4743 |
| Raw edge prob draw | -0.0048 |
| Raw ev draw | -0.0301 |
| Raw edge prob away | 0.2168 |
| Raw ev away | 0.7414 |
| Market p home draw | 71.1% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.1% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.1% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T16:48:59Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.2% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T16:48:59Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.7% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **50.3%**. Expected goals are 1.18 for AS Roma and 1.67 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.4%; Under 3.5 goals: 67.9%; Double Chance 1X: 49.7%; Double Chance X2: 73.5%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 55.8%; BTTS No (at least one team does not score): 44.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.5% | 3.77 |
| Draw | 23.2% | 4.31 |
| Real Madrid win | 50.3% | 1.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.18 |
| Real Madrid expected goals | 1.67 |
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
| 1 | 1-1 | 10.88% |
| 2 | 0-1 | 10.37% |
| 3 | 1-2 | 9.69% |
| 4 | 0-2 | 8.20% |
| 5 | 1-0 | 7.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.5% | 25.5% | 3.85 | +2.1% |
| Draw | 23.2% | 23.3% | 4.16 | -3.6% |
| Real Madrid win | 50.3% | 51.1% | 1.94 | -2.4% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.8% |
| P btts no | 44.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.16 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.12 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.21 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 27.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 49.5% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.0% |
| Raw p btts yes | 55.7% |
| P home draw | 49.7% |
| P draw away | 73.5% |
| Raw p home draw | 50.5% |
| Raw p draw away | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.50 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.85 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Home probability edge | +1.0% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -14.6% |
| Under 2.5 probability edge | +14.6% |
| Raw edge prob home | 0.0199 |
| Raw ev home | 0.0591 |
| Raw edge prob draw | -0.0032 |
| Raw ev draw | -0.0424 |
| Raw edge prob away | -0.0167 |
| Raw ev away | -0.0403 |
| Market p home draw | 51.0% |
| Market home draw odds | 1.96 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.8% |
| Market draw away odds | 1.30 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.87 |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T16:59:43Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.4% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T16:59:43Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.0% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 3.05 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **67.0%**. Expected goals are 2.23 for Aston Villa and 0.61 for Fenerbahce (2.84 combined). The most likely exact score is 2-0 at 13.0%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 51.7%; Under 3.5 goals: 69.9%; Double Chance 1X: 86.4%; Double Chance X2: 33.0%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 41.6%; BTTS No (at least one team does not score): 58.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 67.0% | 1.49 |
| Draw | 19.4% | 5.15 |
| Fenerbahce win | 13.6% | 7.38 |

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
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.02% |
| 2 | 1-0 | 12.02% |
| 3 | 3-0 | 9.69% |
| 4 | 1-1 | 9.08% |
| 5 | 2-1 | 7.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 67.0% | 59.1% | 1.69 | +13.3% |
| Draw | 19.4% | 22.7% | 4.26 | -17.3% |
| Fenerbahce win | 13.6% | 18.1% | 5.33 | -27.8% |
| Over 2.5 | 51.7% | 59.8% | 1.69 | -12.6% |
| Under 2.5 | 48.3% | 40.2% | 2.36 | +13.9% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
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
| Fair Under 0.5 odds | 15.23 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.32 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.75 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.1% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 40.3% |
| P home draw | 86.4% |
| P draw away | 33.0% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.62 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +7.9% |
| Draw probability edge | -3.3% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | 0.1577 |
| Raw ev home | 0.2660 |
| Raw edge prob draw | -0.0662 |
| Raw ev draw | -0.3137 |
| Raw edge prob away | -0.0915 |
| Raw ev away | -0.5213 |
| Market p home draw | 81.0% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:45Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 41.3% |
| Market draw away odds | 2.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:45Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.35 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T16:59:13Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.3% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T16:59:13Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.57 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.9% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.27 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **45.3%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-1 at 8.6%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.0%; Double Chance 1X: 54.7%; Double Chance X2: 67.2%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 70.3%; BTTS No (at least one team does not score): 29.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 32.8% | 3.05 |
| Draw | 22.0% | 4.55 |
| Borussia Dortmund win | 45.3% | 2.21 |

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
| Over 2.5 | 70.6% |
| Under 2.5 | 29.4% |
| Over 3.5 | 50.0% |
| Under 3.5 | 50.0% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.61% |
| 2 | 1-2 | 8.58% |
| 3 | 2-2 | 7.59% |
| 4 | 2-1 | 6.84% |
| 5 | 0-1 | 5.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 32.8% | 30.0% | 3.29 | +7.8% |
| Draw | 22.0% | 23.2% | 4.11 | -9.7% |
| Borussia Dortmund win | 45.3% | 46.8% | 2.14 | -3.1% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
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
| Fair Under 0.5 odds | 44.43 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.40 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.28 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 35.5% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 50.1% |
| Raw p btts yes | 70.0% |
| P home draw | 54.7% |
| P draw away | 67.2% |
| Raw p home draw | 56.2% |
| Raw p draw away | 64.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.00 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +2.7% |
| Draw probability edge | -1.2% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | 0.0548 |
| Raw ev home | 0.1680 |
| Raw edge prob draw | -0.0242 |
| Raw ev draw | -0.1472 |
| Raw edge prob away | -0.0306 |
| Raw ev away | -0.0637 |
| Market p home draw | 53.7% |
| Market home draw odds | 1.79 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:45Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.6% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:45Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.80 |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 88.7% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 51.5% |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 1.98 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 70.9% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.38 |
| Market reference btts yes opposite odds | 3.17 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **61.6%**. Expected goals are 1.82 for Feyenoord and 3.81 for Como (5.63 combined). The most likely exact score is 2-2 at 6.2%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.8%; Under 3.5 goals: 19.8%; Double Chance 1X: 38.4%; Double Chance X2: 79.2%; Under 4.5 goals: 36.0%; BTTS Yes (both teams score): 83.4%; BTTS No (at least one team does not score): 16.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 20.8% | 4.80 |
| Draw | 17.5% | 5.70 |
| Como win | 61.6% | 1.62 |

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
| Over 3.5 | 80.2% |
| Under 3.5 | 19.8% |
| Over 4.5 | 64.0% |
| Under 4.5 | 36.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.22% |
| 2 | 1-3 | 5.05% |
| 3 | 1-4 | 4.81% |
| 4 | 3-3 | 4.79% |
| 5 | 2-3 | 4.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 20.8% | 27.5% | 3.58 | -25.5% |
| Draw | 17.5% | 22.9% | 4.32 | -24.2% |
| Como win | 61.6% | 49.6% | 1.98 | +22.1% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 83.4% |
| P btts no | 16.6% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 295.91 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 36.65 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.88 |
| Fair Over 3.5 odds | 1.25 |
| Fair Under 3.5 odds | 5.05 |
| Fair Over 4.5 odds | 1.56 |
| Fair Under 4.5 odds | 2.78 |
| Unadjusted home-win probability | 14.2% |
| Unadjusted draw probability | 12.2% |
| Unadjusted away-win probability | 73.7% |
| Raw p over 1 5 | 97.5% |
| Raw p under 3 5 | 18.8% |
| Raw p btts yes | 81.8% |
| P home draw | 38.4% |
| P draw away | 79.2% |
| Raw p home draw | 26.3% |
| Raw p draw away | 85.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.30 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.91 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -6.6% |
| Draw probability edge | -5.4% |
| Away probability edge | +12.0% |
| Over 2.5 probability edge | +22.3% |
| Under 2.5 probability edge | -22.3% |
| Raw edge prob home | -0.1329 |
| Raw ev home | -0.4928 |
| Raw edge prob draw | -0.1075 |
| Raw ev draw | -0.4745 |
| Raw edge prob away | 0.2404 |
| Raw ev away | 0.4586 |
| Market p home draw | 50.4% |
| Market home draw odds | 1.92 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.7% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.89 |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 87.8% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T17:00:55Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 53.7% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T17:00:55Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 1.96 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.5% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 3.00 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **71.3%**. Expected goals are 0.28 for LASK and 1.45 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 27.3%. Goal-market probabilities: at least one goal: 86.1%; Over 2.5 goals: 26.5%; Under 3.5 goals: 89.8%; Double Chance 1X: 28.7%; Double Chance X2: 91.3%; Under 4.5 goals: 96.6%; BTTS Yes (both teams score): 17.7%; BTTS No (at least one team does not score): 82.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 8.7% | 11.55 |
| Draw | 20.0% | 4.99 |
| Liverpool win | 71.3% | 1.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.45 |
| Expected total goals | 1.74 |
| Over 0.5 | 86.1% |
| Under 0.5 | 13.9% |
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
| 1 | 0-1 | 27.32% |
| 2 | 0-2 | 19.60% |
| 3 | 0-0 | 13.89% |
| 4 | 0-3 | 9.50% |
| 5 | 1-0 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 8.7% | 10.0% | 9.10 | -21.2% |
| Draw | 20.0% | 15.2% | 6.24 | +25.0% |
| Liverpool win | 71.3% | 74.8% | 1.34 | -4.4% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
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
| Fair Under 0.5 odds | 7.20 |
| Fair Over 1.5 odds | 1.91 |
| Fair Under 1.5 odds | 2.10 |
| Fair Over 2.5 odds | 3.77 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 9.79 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 29.71 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 67.8% |
| Raw p over 1 5 | 51.4% |
| Raw p under 3 5 | 90.1% |
| Raw p btts yes | 18.5% |
| P home draw | 28.7% |
| P draw away | 91.3% |
| Raw p home draw | 32.2% |
| Raw p draw away | 92.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 8.00 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.30 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -1.4% |
| Draw probability edge | +4.9% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -45.1% |
| Under 2.5 probability edge | +45.1% |
| Raw edge prob home | -0.0273 |
| Raw ev home | -0.3368 |
| Raw edge prob draw | 0.0972 |
| Raw ev draw | 0.5529 |
| Raw edge prob away | -0.0698 |
| Raw ev away | -0.0911 |
| Market p home draw | 26.5% |
| Market home draw odds | 3.56 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.1% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.60 |
| Market reference dc draw away odds | 1.07 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 88.7% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T16:48:09Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.1% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T16:48:09Z |
| Market reference under 3 5 odds | 1.80 |
| Market reference under 3 5 opposite odds | 1.87 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.0% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **44.2%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.8%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 69.1%; Under 3.5 goals: 51.9%; Double Chance 1X: 55.8%; Double Chance X2: 65.7%; Under 4.5 goals: 71.1%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 34.3% | 2.91 |
| Draw | 21.5% | 4.65 |
| Paris Saint Germain win | 44.2% | 2.26 |

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
| 1 | 1-1 | 8.76% |
| 2 | 2-1 | 8.28% |
| 3 | 2-2 | 7.21% |
| 4 | 1-2 | 7.19% |
| 5 | 1-0 | 5.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 34.3% | 44.6% | 2.23 | -23.5% |
| Draw | 21.5% | 23.7% | 4.11 | -11.5% |
| Paris Saint Germain win | 44.2% | 31.6% | 3.08 | +36.0% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
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
| Fair Under 0.5 odds | 40.20 |
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
| P home draw | 55.8% |
| P draw away | 65.7% |
| Raw p home draw | 43.3% |
| Raw p draw away | 76.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.10 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.88 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -10.3% |
| Draw probability edge | -2.2% |
| Away probability edge | +12.5% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | -0.2059 |
| Raw ev home | -0.4643 |
| Raw edge prob draw | -0.0444 |
| Raw ev draw | -0.2068 |
| Raw edge prob away | 0.2504 |
| Raw ev away | 0.7457 |
| Market p home draw | 68.4% |
| Market home draw odds | 1.43 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:45Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.1% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:45Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.41 |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 86.9% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T16:50:56Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.6% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T16:50:56Z |
| Market reference under 3 5 odds | 1.74 |
| Market reference under 3 5 opposite odds | 2.15 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.3% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 2.94 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **61.1%**. Expected goals are 3.29 for Real Betis and 1.29 for Porto (4.58 combined). The most likely exact score is 2-2 at 7.1%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 80.9%; Under 3.5 goals: 35.2%; Double Chance 1X: 80.3%; Double Chance X2: 38.9%; Under 4.5 goals: 54.9%; BTTS Yes (both teams score): 72.3%; BTTS No (at least one team does not score): 27.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 61.1% | 1.64 |
| Draw | 19.2% | 5.22 |
| Porto win | 19.7% | 5.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 3.29 |
| Porto expected goals | 1.29 |
| Expected total goals | 4.58 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 93.2% |
| Under 1.5 | 6.8% |
| Over 2.5 | 80.9% |
| Under 2.5 | 19.1% |
| Over 3.5 | 64.8% |
| Under 3.5 | 35.2% |
| Over 4.5 | 45.1% |
| Under 4.5 | 54.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.12% |
| 2 | 1-1 | 6.37% |
| 3 | 3-1 | 6.30% |
| 4 | 2-1 | 5.75% |
| 5 | 4-1 | 5.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 61.1% | 46.1% | 2.16 | +32.0% |
| Draw | 19.2% | 25.9% | 3.76 | -28.0% |
| Porto win | 19.7% | 28.0% | 3.50 | -30.9% |
| Over 2.5 | 80.9% | 56.3% | 1.79 | +44.9% |
| Under 2.5 | 19.1% | 43.7% | 2.19 | -58.2% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
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
| P btts yes | 72.3% |
| P btts no | 27.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 80.53 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.76 |
| Fair Over 2.5 odds | 1.24 |
| Fair Under 2.5 odds | 5.25 |
| Fair Over 3.5 odds | 1.54 |
| Fair Under 3.5 odds | 2.84 |
| Fair Over 4.5 odds | 2.22 |
| Fair Under 4.5 odds | 1.82 |
| Unadjusted home-win probability | 76.1% |
| Unadjusted draw probability | 12.4% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 94.1% |
| Raw p under 3 5 | 32.9% |
| Raw p btts yes | 69.6% |
| P home draw | 80.3% |
| P draw away | 38.9% |
| Raw p home draw | 88.6% |
| Raw p draw away | 23.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.05 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +15.0% |
| Draw probability edge | -6.7% |
| Away probability edge | -8.3% |
| Over 2.5 probability edge | +24.6% |
| Under 2.5 probability edge | -24.6% |
| Raw edge prob home | 0.3002 |
| Raw ev home | 0.6441 |
| Raw edge prob draw | -0.1344 |
| Raw ev draw | -0.5324 |
| Raw edge prob away | -0.1658 |
| Raw ev away | -0.5993 |
| Market p home draw | 72.2% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:45Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.9% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:45Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 80.3% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T17:00:28Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.1% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T17:00:28Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.74 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.6% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.35 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **40.0%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 51.0%; Under 3.5 goals: 70.6%; Double Chance 1X: 66.1%; Double Chance X2: 60.0%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 40.0% | 2.50 |
| Draw | 26.1% | 3.83 |
| AEK Athens win | 33.9% | 2.95 |

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
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.34% |
| 2 | 1-0 | 9.44% |
| 3 | 0-1 | 9.05% |
| 4 | 2-1 | 8.27% |
| 5 | 1-2 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 40.0% | 36.7% | 2.73 | +9.2% |
| Draw | 26.1% | 28.1% | 3.47 | -9.3% |
| AEK Athens win | 33.9% | 35.2% | 2.77 | -6.1% |
| Over 2.5 | 51.0% | 52.2% | 1.95 | -0.6% |
| Under 2.5 | 49.0% | 47.8% | 1.99 | -2.4% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
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
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.81 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.12 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 54.7% |
| P home draw | 66.1% |
| P draw away | 60.0% |
| Raw p home draw | 67.4% |
| Raw p draw away | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.50 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | +3.2% |
| Draw probability edge | -1.9% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -1.2% |
| Under 2.5 probability edge | +1.2% |
| Raw edge prob home | 0.0650 |
| Raw ev home | 0.1804 |
| Raw edge prob draw | -0.0386 |
| Raw ev draw | -0.1604 |
| Raw edge prob away | -0.0264 |
| Raw ev away | -0.0979 |
| Market p home draw | 63.5% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:47Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.4% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:47Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.52 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 77.2% |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.93 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 70.3% |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.10 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.26 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **65.7%**. Expected goals are 1.46 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.6%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 72.5%; Under 3.5 goals: 48.5%; Double Chance 1X: 34.3%; Double Chance X2: 82.9%; Under 4.5 goals: 67.8%; BTTS Yes (both teams score): 67.3%; BTTS No (at least one team does not score): 32.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.1% | 5.85 |
| Draw | 17.2% | 5.81 |
| VfB Stuttgart win | 65.7% | 1.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.46 |
| VfB Stuttgart expected goals | 2.25 |
| Expected total goals | 3.71 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 88.5% |
| Under 1.5 | 11.5% |
| Over 2.5 | 72.5% |
| Under 2.5 | 27.5% |
| Over 3.5 | 51.5% |
| Under 3.5 | 48.5% |
| Over 4.5 | 32.2% |
| Under 4.5 | 67.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.64% |
| 2 | 1-3 | 7.98% |
| 3 | 0-2 | 7.31% |
| 4 | 0-1 | 6.97% |
| 5 | 1-1 | 6.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.1% | 9.4% | 10.00 | +70.9% |
| Draw | 17.2% | 15.2% | 6.48 | +11.5% |
| VfB Stuttgart win | 65.7% | 75.5% | 1.31 | -13.9% |

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
| Market best home last update utc | 2026-10-13T17:02:12Z |
| Market best draw last update utc | 2026-10-13T17:02:12Z |
| Market best away last update utc | 2026-10-13T17:02:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.3% |
| P btts no | 32.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 54.42 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.66 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.64 |
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
| P home draw | 34.3% |
| P draw away | 82.9% |
| Raw p home draw | 44.1% |
| Raw p draw away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 8.50 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.29 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Home probability edge | +7.7% |
| Draw probability edge | +2.0% |
| Away probability edge | -9.8% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.1544 |
| Raw ev home | 1.4815 |
| Raw edge prob draw | 0.0408 |
| Raw ev draw | 0.2477 |
| Raw edge prob away | -0.1952 |
| Raw ev away | -0.2673 |
| Market p home draw | 25.4% |
| Market home draw odds | 3.78 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T17:02:12Z |
| Market reference home draw last update utc | 2026-10-13T17:02:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.0% |
| Market draw away odds | 1.06 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T17:02:12Z |
| Market reference draw away last update utc | 2026-10-13T17:02:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.82 |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 89.5% |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 49.9% |
| Market reference under 3 5 odds | 1.94 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.3% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T17:02:12Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.27 |
| Market btts yes bookmakers | 1 |

</details>


---
