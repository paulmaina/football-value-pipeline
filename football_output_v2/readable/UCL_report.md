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
| Training data health | {'completed_matches': 18, 'latest_completed_utc': '2026-09-10T19:00:00+00:00', 'latest_completed_date': '2026-09-10', 'next_fixture_utc': '2026-10-13T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-13T11:47:48.867891+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'e5a952fc3addc9a4e23d1d3bd4af8b31b836fd55452464d6ebbce16e4fdab9d0', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'LIVE_REFRESH_FAILED_USING_CACHE', 'download_age_hours': 0.6311165830555555, 'training_end': '2026-09-10', 'cache_hash_verified': True, 'last_refresh_error': 'ValueError'} |
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

The model's most likely 1X2 outcome is **Arsenal win** at **74.8%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.5%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 49.5%; Under 3.5 goals: 73.0%; Double Chance 1X: 91.2%; Double Chance X2: 25.2%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 39.4%; BTTS No (at least one team does not score): 60.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 74.8% | 1.34 |
| Draw | 16.4% | 6.11 |
| Lille win | 8.8% | 11.37 |

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
| 1 | 1-0 | 16.52% |
| 2 | 2-0 | 15.43% |
| 3 | 2-1 | 10.09% |
| 4 | 3-0 | 9.92% |
| 5 | 1-1 | 7.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 74.8% | 81.5% | 1.23 | -8.0% |
| Draw | 16.4% | 13.2% | 7.06 | +15.6% |
| Lille win | 8.8% | 5.4% | 16.00 | +40.7% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| P home draw | 91.2% |
| P draw away | 25.2% |
| Raw p home draw | 87.8% |
| Raw p draw away | 31.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.21 |
| Reference draw odds | 6.60 |
| Reference away odds | 15.25 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -6.7% |
| Draw probability edge | +3.2% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -14.3% |
| Under 2.5 probability edge | +14.3% |
| Raw edge prob home | -0.1331 |
| Raw ev home | -0.1615 |
| Raw edge prob draw | 0.0643 |
| Raw ev draw | 0.3833 |
| Raw edge prob away | 0.0688 |
| Raw ev away | 0.9575 |
| Market p home draw | 93.9% |
| Market home draw odds | 1.03 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:20:38Z |
| Market reference home draw last update utc | 2026-10-13T12:25:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 20.6% |
| Market draw away odds | 4.68 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:20:38Z |
| Market reference draw away last update utc | 2026-10-13T12:25:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.02 |
| Market reference dc draw away odds | 4.65 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 86.4% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:25:26Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.5% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:25:26Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.27 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 44.4% |
| Market btts yes odds | 2.21 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:20:38Z |
| Market reference btts yes odds | 2.24 |
| Market reference btts yes opposite odds | 1.79 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **63.7%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.8%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.8%; Under 3.5 goals: 24.5%; Double Chance 1X: 81.9%; Double Chance X2: 36.3%; Under 4.5 goals: 42.5%; BTTS Yes (both teams score): 78.8%; BTTS No (at least one team does not score): 21.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 63.7% | 1.57 |
| Draw | 18.2% | 5.49 |
| Manchester United win | 18.1% | 5.52 |

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
| Over 4.5 | 57.5% |
| Under 4.5 | 42.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.80% |
| 2 | 3-1 | 5.67% |
| 3 | 4-1 | 5.28% |
| 4 | 2-1 | 4.56% |
| 5 | 1-1 | 4.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 63.7% | 50.3% | 1.98 | +26.1% |
| Draw | 18.2% | 25.0% | 3.90 | -29.0% |
| Manchester United win | 18.1% | 24.7% | 3.94 | -28.6% |
| Over 2.5 | 87.8% | 60.0% | 1.71 | +50.1% |
| Under 2.5 | 12.2% | 40.0% | 2.33 | -71.6% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
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
| Fair Under 0.5 odds | 170.52 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.43 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.19 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.07 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.35 |
| Unadjusted home-win probability | 77.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 23.0% |
| Raw p btts yes | 76.6% |
| P home draw | 81.9% |
| P draw away | 36.3% |
| Raw p home draw | 88.5% |
| Raw p draw away | 22.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.95 |
| Reference draw odds | 3.84 |
| Reference away odds | 3.88 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | +13.4% |
| Draw probability edge | -6.8% |
| Away probability edge | -6.6% |
| Over 2.5 probability edge | +27.8% |
| Under 2.5 probability edge | -27.8% |
| Raw edge prob home | 0.2683 |
| Raw ev home | 0.5263 |
| Raw edge prob draw | -0.1359 |
| Raw ev draw | -0.5549 |
| Raw edge prob away | -0.1324 |
| Raw ev away | -0.5469 |
| Market p home draw | 75.9% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:20:38Z |
| Market reference home draw last update utc | 2026-10-13T12:25:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.3% |
| Market draw away odds | 1.92 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:20:38Z |
| Market reference draw away last update utc | 2026-10-13T12:25:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.28 |
| Market reference dc draw away odds | 1.97 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:19:29Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.1% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:19:29Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.6% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:20:38Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.43 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **67.3%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.6%. Goal-market probabilities: at least one goal: 98.7%; Over 2.5 goals: 77.6%; Under 3.5 goals: 41.8%; Double Chance 1X: 32.7%; Double Chance X2: 83.3%; Under 4.5 goals: 61.2%; BTTS Yes (both teams score): 70.9%; BTTS No (at least one team does not score): 29.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 16.7% | 5.98 |
| Draw | 16.0% | 6.27 |
| Barcelona win | 67.3% | 1.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.53 |
| Barcelona expected goals | 2.51 |
| Expected total goals | 4.04 |
| Over 0.5 | 98.7% |
| Under 0.5 | 1.3% |
| Over 1.5 | 91.1% |
| Under 1.5 | 8.9% |
| Over 2.5 | 77.6% |
| Under 2.5 | 22.4% |
| Over 3.5 | 58.2% |
| Under 3.5 | 41.8% |
| Over 4.5 | 38.8% |
| Under 4.5 | 61.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.63% |
| 2 | 1-3 | 8.05% |
| 3 | 0-2 | 6.27% |
| 4 | 2-3 | 6.18% |
| 5 | 2-2 | 5.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 16.7% | 10.6% | 8.70 | +45.5% |
| Draw | 16.0% | 14.0% | 6.66 | +6.3% |
| Barcelona win | 67.3% | 75.4% | 1.33 | -10.5% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.9% |
| P btts no | 29.1% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 79.26 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.30 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.47 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.39 |
| Fair Over 4.5 odds | 2.57 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.5% |
| Raw p btts yes | 71.7% |
| P home draw | 32.7% |
| P draw away | 83.3% |
| Raw p home draw | 40.8% |
| Raw p draw away | 77.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 8.60 |
| Reference draw odds | 6.55 |
| Reference away odds | 1.31 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.60 |
| Home probability edge | +6.2% |
| Draw probability edge | +1.9% |
| Away probability edge | -8.1% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | 0.1234 |
| Raw ev home | 0.9921 |
| Raw edge prob draw | 0.0386 |
| Raw ev draw | 0.1913 |
| Raw edge prob away | -0.1620 |
| Raw ev away | -0.2125 |
| Market p home draw | 26.2% |
| Market home draw odds | 3.62 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:20:38Z |
| Market reference home draw last update utc | 2026-10-13T12:25:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 88.5% |
| Market draw away odds | 1.09 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:20:38Z |
| Market reference draw away last update utc | 2026-10-13T12:25:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.68 |
| Market reference dc draw away odds | 1.09 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 94.3% |
| Market over 1 5 odds | 1.01 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:16:11Z |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 11.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 36.2% |
| Market under 3 5 odds | 2.42 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:16:11Z |
| Market reference under 3 5 odds | 2.57 |
| Market reference under 3 5 opposite odds | 1.52 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:20:38Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 3.10 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **69.8%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 56.3%; Under 3.5 goals: 66.8%; Double Chance 1X: 87.0%; Double Chance X2: 30.2%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 69.8% | 1.43 |
| Draw | 17.3% | 5.79 |
| Club Brugge win | 13.0% | 7.71 |

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
| Over 2.5 | 56.3% |
| Under 2.5 | 43.7% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.18% |
| 2 | 2-0 | 12.08% |
| 3 | 2-1 | 11.41% |
| 4 | 1-1 | 8.18% |
| 5 | 3-0 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 69.8% | 78.8% | 1.27 | -11.4% |
| Draw | 17.3% | 13.8% | 6.74 | +16.5% |
| Club Brugge win | 13.0% | 7.4% | 12.10 | +56.9% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.15 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.62 |
| Fair Over 2.5 odds | 1.78 |
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
| P home draw | 87.0% |
| P draw away | 30.2% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.25 |
| Reference draw odds | 6.40 |
| Reference away odds | 11.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Home probability edge | -9.1% |
| Draw probability edge | +3.5% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -16.6% |
| Under 2.5 probability edge | +16.6% |
| Raw edge prob home | -0.1811 |
| Raw ev home | -0.2291 |
| Raw edge prob draw | 0.0696 |
| Raw ev draw | 0.3991 |
| Raw edge prob away | 0.1116 |
| Raw ev away | 1.2435 |
| Market p home draw | 91.6% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:20:38Z |
| Market reference home draw last update utc | 2026-10-13T12:25:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 23.2% |
| Market draw away odds | 4.14 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:20:38Z |
| Market reference draw away last update utc | 2026-10-13T12:25:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 4.15 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 89.8% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:24:23Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 48.5% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:24:23Z |
| Market reference under 3 5 odds | 2.00 |
| Market reference under 3 5 opposite odds | 1.89 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.5% |
| Market btts yes odds | 1.73 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:20:38Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.24 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **47.9%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 68.3%; Under 3.5 goals: 53.6%; Double Chance 1X: 68.1%; Double Chance X2: 52.1%; Under 4.5 goals: 72.2%; BTTS Yes (both teams score): 67.7%; BTTS No (at least one team does not score): 32.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 47.9% | 2.09 |
| Draw | 20.2% | 4.95 |
| PSV Eindhoven win | 31.9% | 3.13 |

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
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.8% |
| Under 4.5 | 72.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.33% |
| 2 | 1-1 | 8.28% |
| 3 | 1-0 | 7.34% |
| 4 | 2-2 | 6.71% |
| 5 | 1-2 | 6.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 47.9% | 60.8% | 1.65 | -21.0% |
| Draw | 20.2% | 19.2% | 4.98 | +0.5% |
| PSV Eindhoven win | 31.9% | 20.0% | 4.77 | +52.4% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| Fair Under 0.5 odds | 41.74 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.09 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.15 |
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
| P home draw | 68.1% |
| P draw away | 52.1% |
| Raw p home draw | 56.2% |
| Raw p draw away | 65.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.61 |
| Reference draw odds | 4.85 |
| Reference away odds | 4.65 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Home probability edge | -12.9% |
| Draw probability edge | +1.0% |
| Away probability edge | +11.9% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | -0.2580 |
| Raw ev home | -0.4229 |
| Raw edge prob draw | 0.0200 |
| Raw ev draw | 0.0550 |
| Raw edge prob away | 0.2379 |
| Raw ev away | 1.0911 |
| Market p home draw | 79.9% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:20:38Z |
| Market reference home draw last update utc | 2026-10-13T12:25:42Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.5% |
| Market draw away odds | 2.38 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:20:38Z |
| Market reference draw away last update utc | 2026-10-13T12:25:42Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.47 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 96.7% |
| Market over 1 5 odds | 1.02 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:25:26Z |
| Market reference over 1 5 odds | 1.02 |
| Market reference over 1 5 opposite odds | 7.70 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 42.5% |
| Market under 3 5 odds | 2.22 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:25:26Z |
| Market reference under 3 5 odds | 2.25 |
| Market reference under 3 5 opposite odds | 1.69 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 72.2% |
| Market btts yes odds | 1.32 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:20:38Z |
| Market reference btts yes odds | 1.36 |
| Market reference btts yes opposite odds | 3.36 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **41.2%**. Expected goals are 1.28 for RC Lens and 1.60 for Sporting Lisbon (2.89 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.7%; Under 3.5 goals: 67.4%; Double Chance 1X: 58.8%; Double Chance X2: 65.5%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 34.5% | 2.90 |
| Draw | 24.3% | 4.11 |
| Sporting Lisbon win | 41.2% | 2.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.28 |
| Sporting Lisbon expected goals | 1.60 |
| Expected total goals | 2.89 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 54.7% |
| Under 2.5 | 45.3% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.35% |
| 2 | 0-1 | 8.62% |
| 3 | 1-0 | 8.54% |
| 4 | 1-2 | 8.34% |
| 5 | 2-1 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 34.5% | 37.7% | 2.62 | -9.7% |
| Draw | 24.3% | 25.3% | 3.85 | -6.4% |
| Sporting Lisbon win | 41.2% | 37.0% | 2.67 | +10.1% |
| Over 2.5 | 54.7% | 60.8% | 1.64 | -10.3% |
| Under 2.5 | 45.3% | 39.2% | 2.46 | +11.4% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Sporting Clube de Portugal |
| Home-name matching confidence | 86/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.21 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.09 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.2% |
| P home draw | 58.8% |
| P draw away | 65.5% |
| Raw p home draw | 54.6% |
| Raw p draw away | 68.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.55 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.60 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Home probability edge | -3.3% |
| Draw probability edge | -1.0% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.0653 |
| Raw ev home | -0.1822 |
| Raw edge prob draw | -0.0192 |
| Raw ev draw | -0.1014 |
| Raw edge prob away | 0.0846 |
| Raw ev away | 0.2134 |
| Market p home draw | 63.4% |
| Market home draw odds | 1.53 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:20:38Z |
| Market reference home draw last update utc | 2026-10-13T12:25:42Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.6% |
| Market draw away odds | 1.55 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:20:38Z |
| Market reference draw away last update utc | 2026-10-13T12:25:42Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.53 |
| Market reference dc draw away odds | 1.55 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:20:35Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.4% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:20:35Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.47 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.1% |
| Market btts yes odds | 1.47 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:20:38Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.71 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **54.6%**. Expected goals are 0.38 for Sabah FK and 1.28 for Slavia Praha (1.66 combined). The most likely exact score is 0-1 at 22.5%. Goal-market probabilities: at least one goal: 82.6%; Over 2.5 goals: 22.9%; Under 3.5 goals: 91.7%; Double Chance 1X: 45.4%; Double Chance X2: 81.4%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 22.2%; BTTS No (at least one team does not score): 77.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 18.6% | 5.37 |
| Draw | 26.7% | 3.74 |
| Slavia Praha win | 54.6% | 1.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.38 |
| Slavia Praha expected goals | 1.28 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.6% |
| Under 0.5 | 17.4% |
| Over 1.5 | 47.5% |
| Under 1.5 | 52.5% |
| Over 2.5 | 22.9% |
| Under 2.5 | 77.1% |
| Over 3.5 | 8.3% |
| Under 3.5 | 91.7% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.55% |
| 2 | 0-0 | 17.39% |
| 3 | 0-2 | 14.17% |
| 4 | 1-0 | 12.53% |
| 5 | 1-1 | 8.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 18.6% | 25.8% | 3.78 | -29.6% |
| Draw | 26.7% | 25.0% | 3.90 | +4.3% |
| Slavia Praha win | 54.6% | 49.2% | 2.02 | +10.4% |
| Over 2.5 | 22.9% | 60.5% | 1.65 | -62.2% |
| Under 2.5 | 77.1% | 39.5% | 2.45 | +88.9% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| Fair Under 0.5 odds | 5.75 |
| Fair Over 1.5 odds | 2.10 |
| Fair Under 1.5 odds | 1.91 |
| Fair Over 2.5 odds | 4.37 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 12.05 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 38.29 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.4% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 60.1% |
| Raw p over 1 5 | 49.0% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 22.4% |
| P home draw | 45.4% |
| P draw away | 81.4% |
| Raw p home draw | 39.9% |
| Raw p draw away | 88.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.72 |
| Reference draw odds | 3.84 |
| Reference away odds | 1.99 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -7.2% |
| Draw probability edge | +1.8% |
| Away probability edge | +5.4% |
| Over 2.5 probability edge | -37.6% |
| Under 2.5 probability edge | +37.6% |
| Raw edge prob home | -0.1440 |
| Raw ev home | -0.5683 |
| Raw edge prob draw | 0.0352 |
| Raw ev draw | 0.1119 |
| Raw edge prob away | 0.1087 |
| Raw ev away | 0.2134 |
| Market p home draw | 51.4% |
| Market home draw odds | 1.88 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:20:38Z |
| Market reference home draw last update utc | 2026-10-13T12:25:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.7% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:20:38Z |
| Market reference draw away last update utc | 2026-10-13T12:25:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.88 |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:18:46Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.4% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:18:46Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.47 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.4% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:20:38Z |
| Market reference btts yes odds | 1.59 |
| Market reference btts yes opposite odds | 2.62 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **91.9%**. Expected goals are 0.70 for Viking FK and 4.47 for Bayern Munich (5.17 combined). The most likely exact score is 0-4 at 9.3%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.1%; Under 3.5 goals: 25.1%; Double Chance 1X: 8.1%; Double Chance X2: 97.1%; Under 4.5 goals: 42.3%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 2.9% | 34.36 |
| Draw | 5.2% | 19.21 |
| Bayern Munich win | 91.9% | 1.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.70 |
| Bayern Munich expected goals | 4.47 |
| Expected total goals | 5.17 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.1% |
| Under 1.5 | 3.9% |
| Over 2.5 | 88.1% |
| Under 2.5 | 11.9% |
| Over 3.5 | 74.9% |
| Under 3.5 | 25.1% |
| Over 4.5 | 57.7% |
| Under 4.5 | 42.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.34% |
| 2 | 0-3 | 8.37% |
| 3 | 0-5 | 8.35% |
| 4 | 1-4 | 6.51% |
| 5 | 0-6 | 6.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 2.9% | 3.9% | 21.00 | -38.9% |
| Draw | 5.2% | 6.2% | 13.90 | -27.6% |
| Bayern Munich win | 91.9% | 89.9% | 1.11 | +2.0% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 165.04 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 25.43 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.42 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.98 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.37 |
| Unadjusted home-win probability | 2.0% |
| Unadjusted draw probability | 4.2% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.4% |
| Raw p btts yes | 49.5% |
| P home draw | 8.1% |
| P draw away | 97.1% |
| Raw p home draw | 6.1% |
| Raw p draw away | 98.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 18.50 |
| Reference draw odds | 12.00 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.50 |
| Home probability edge | -0.9% |
| Draw probability edge | -1.0% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +2.7% |
| Under 2.5 probability edge | -2.7% |
| Raw edge prob home | -0.0188 |
| Raw ev home | -0.5862 |
| Raw edge prob draw | -0.0207 |
| Raw ev draw | -0.4203 |
| Raw edge prob away | 0.0395 |
| Raw ev away | 0.0418 |
| Market p home draw | 13.9% |
| Market home draw odds | 7.70 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:20:38Z |
| Market reference home draw last update utc | 2026-10-13T12:25:42Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 94.8% |
| Market draw away odds | 1.02 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:20:38Z |
| Market reference draw away last update utc | 2026-10-13T12:25:42Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 7.00 |
| Market reference dc draw away odds | 1.03 |
| Market reference dc home away odds | 1.07 |
| Market p over 1 5 | 96.4% |
| Market over 1 5 odds | 1.03 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:25:26Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 15.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 31.0% |
| Market under 3 5 odds | 2.76 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:25:26Z |
| Market reference under 3 5 odds | 2.76 |
| Market reference under 3 5 opposite odds | 1.38 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.7% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:20:38Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.34 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **38.8%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.7%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 40.1%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.2%; Double Chance X2: 64.7%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 44.5%; BTTS No (at least one team does not score): 55.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 35.3% | 2.83 |
| Draw | 25.9% | 3.86 |
| Napoli win | 38.8% | 2.57 |

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
| 1 | 1-0 | 13.70% |
| 2 | 1-1 | 11.98% |
| 3 | 0-1 | 11.42% |
| 4 | 0-0 | 9.28% |
| 5 | 2-1 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 35.3% | 46.1% | 2.15 | -24.2% |
| Draw | 25.9% | 26.0% | 3.76 | -2.7% |
| Napoli win | 38.8% | 27.9% | 3.50 | +35.9% |
| Over 2.5 | 40.1% | 57.7% | 1.72 | -31.0% |
| Under 2.5 | 59.9% | 42.3% | 2.30 | +37.7% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| Fair Under 0.5 odds | 10.77 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.10 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 44.3% |
| P home draw | 61.2% |
| P draw away | 64.7% |
| Raw p home draw | 50.2% |
| Raw p draw away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.12 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.45 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -10.8% |
| Draw probability edge | -0.1% |
| Away probability edge | +10.9% |
| Over 2.5 probability edge | -17.6% |
| Under 2.5 probability edge | +17.6% |
| Raw edge prob home | -0.2166 |
| Raw ev home | -0.4743 |
| Raw edge prob draw | -0.0018 |
| Raw ev draw | -0.0301 |
| Raw edge prob away | 0.2184 |
| Raw ev away | 0.7414 |
| Market p home draw | 71.1% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:20:38Z |
| Market reference home draw last update utc | 2026-10-13T12:25:47Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.1% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:20:38Z |
| Market reference draw away last update utc | 2026-10-13T12:25:47Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.1% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:23:13Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.2% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:23:13Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.8% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:20:38Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.46 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **50.4%**. Expected goals are 1.18 for AS Roma and 1.67 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.4%; Under 3.5 goals: 67.9%; Double Chance 1X: 49.6%; Double Chance X2: 73.6%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 55.8%; BTTS No (at least one team does not score): 44.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.4% | 3.79 |
| Draw | 23.2% | 4.31 |
| Real Madrid win | 50.4% | 1.98 |

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
| 1 | 1-1 | 10.89% |
| 2 | 0-1 | 10.40% |
| 3 | 1-2 | 9.70% |
| 4 | 0-2 | 8.22% |
| 5 | 1-0 | 7.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.4% | 25.3% | 3.85 | +1.6% |
| Draw | 23.2% | 23.4% | 4.16 | -3.5% |
| Real Madrid win | 50.4% | 51.3% | 1.94 | -2.2% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| Fair Under 0.5 odds | 19.14 |
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
| P home draw | 49.6% |
| P draw away | 73.6% |
| Raw p home draw | 50.5% |
| Raw p draw away | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.80 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.91 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Home probability edge | +1.1% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -14.6% |
| Under 2.5 probability edge | +14.6% |
| Raw edge prob home | 0.0223 |
| Raw ev home | 0.0591 |
| Raw edge prob draw | -0.0036 |
| Raw ev draw | -0.0424 |
| Raw edge prob away | -0.0187 |
| Raw ev away | -0.0403 |
| Market p home draw | 49.4% |
| Market home draw odds | 1.96 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:25:49Z |
| Market reference home draw last update utc | 2026-10-13T12:25:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.4% |
| Market draw away odds | 1.30 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:25:49Z |
| Market reference draw away last update utc | 2026-10-13T12:25:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.96 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:19:31Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.2% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:19:31Z |
| Market reference under 3 5 odds | 1.71 |
| Market reference under 3 5 opposite odds | 1.98 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.9% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:25:49Z |
| Market reference btts yes odds | 1.39 |
| Market reference btts yes opposite odds | 2.81 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **67.1%**. Expected goals are 2.23 for Aston Villa and 0.61 for Fenerbahce (2.84 combined). The most likely exact score is 2-0 at 13.0%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 51.7%; Under 3.5 goals: 69.8%; Double Chance 1X: 86.5%; Double Chance X2: 32.9%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 41.6%; BTTS No (at least one team does not score): 58.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 67.1% | 1.49 |
| Draw | 19.4% | 5.15 |
| Fenerbahce win | 13.5% | 7.40 |

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
| 1 | 2-0 | 13.03% |
| 2 | 1-0 | 12.03% |
| 3 | 3-0 | 9.70% |
| 4 | 1-1 | 9.08% |
| 5 | 2-1 | 7.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 67.1% | 59.2% | 1.69 | +13.4% |
| Draw | 19.4% | 22.7% | 4.26 | -17.3% |
| Fenerbahce win | 13.5% | 18.0% | 5.33 | -28.0% |
| Over 2.5 | 51.7% | 58.9% | 1.69 | -12.6% |
| Under 2.5 | 48.3% | 41.1% | 2.36 | +13.9% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| Fair Under 0.5 odds | 15.24 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.32 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.74 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.1% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 40.3% |
| P home draw | 86.5% |
| P draw away | 32.9% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.66 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.25 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.29 |
| Home probability edge | +7.8% |
| Draw probability edge | -3.3% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | 0.1566 |
| Raw ev home | 0.2660 |
| Raw edge prob draw | -0.0660 |
| Raw ev draw | -0.3137 |
| Raw edge prob away | -0.0906 |
| Raw ev away | -0.5213 |
| Market p home draw | 81.3% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:25:49Z |
| Market reference home draw last update utc | 2026-10-13T12:25:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 41.9% |
| Market draw away odds | 2.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:25:49Z |
| Market reference draw away last update utc | 2026-10-13T12:25:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.31 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:17:59Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.8% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:17:59Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.37 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.5% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:25:49Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.15 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **45.2%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.0%; Double Chance 1X: 54.8%; Double Chance X2: 67.4%; Under 4.5 goals: 69.6%; BTTS Yes (both teams score): 70.3%; BTTS No (at least one team does not score): 29.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 32.6% | 3.06 |
| Draw | 22.2% | 4.51 |
| Borussia Dortmund win | 45.2% | 2.21 |

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
| Over 4.5 | 30.4% |
| Under 4.5 | 69.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.69% |
| 2 | 1-2 | 8.56% |
| 3 | 2-2 | 7.67% |
| 4 | 2-1 | 6.81% |
| 5 | 0-1 | 5.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 32.6% | 29.8% | 3.29 | +7.4% |
| Draw | 22.2% | 23.6% | 4.11 | -8.9% |
| Borussia Dortmund win | 45.2% | 46.6% | 2.14 | -3.3% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| Fair Under 0.5 odds | 44.00 |
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
| P home draw | 54.8% |
| P draw away | 67.4% |
| Raw p home draw | 56.2% |
| Raw p draw away | 64.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.20 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.08 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +2.9% |
| Draw probability edge | -1.4% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | +1.5% |
| Under 2.5 probability edge | -1.5% |
| Raw edge prob home | 0.0573 |
| Raw ev home | 0.1680 |
| Raw edge prob draw | -0.0285 |
| Raw ev draw | -0.1472 |
| Raw edge prob away | -0.0288 |
| Raw ev away | -0.0637 |
| Market p home draw | 54.3% |
| Market home draw odds | 1.79 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:25:49Z |
| Market reference home draw last update utc | 2026-10-13T12:25:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.9% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:25:49Z |
| Market reference draw away last update utc | 2026-10-13T12:25:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.79 |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 88.7% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.2% |
| Market reference under 3 5 odds | 1.77 |
| Market reference under 3 5 opposite odds | 1.91 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 70.5% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:25:49Z |
| Market reference btts yes odds | 1.36 |
| Market reference btts yes opposite odds | 2.93 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **62.0%**. Expected goals are 1.82 for Feyenoord and 3.81 for Como (5.63 combined). The most likely exact score is 2-2 at 6.1%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.9%; Under 3.5 goals: 19.8%; Double Chance 1X: 38.0%; Double Chance X2: 79.3%; Under 4.5 goals: 35.9%; BTTS Yes (both teams score): 83.3%; BTTS No (at least one team does not score): 16.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 20.7% | 4.83 |
| Draw | 17.3% | 5.79 |
| Como win | 62.0% | 1.61 |

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
| Over 2.5 | 90.9% |
| Under 2.5 | 9.1% |
| Over 3.5 | 80.2% |
| Under 3.5 | 19.8% |
| Over 4.5 | 64.1% |
| Under 4.5 | 35.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.13% |
| 2 | 1-3 | 5.08% |
| 3 | 1-4 | 4.84% |
| 4 | 3-3 | 4.72% |
| 5 | 2-3 | 4.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 20.7% | 27.2% | 3.58 | -25.9% |
| Draw | 17.3% | 22.4% | 4.32 | -25.4% |
| Como win | 62.0% | 50.4% | 1.98 | +22.8% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| Fair Under 0.5 odds | 300.41 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 36.70 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.93 |
| Fair Over 3.5 odds | 1.25 |
| Fair Under 3.5 odds | 5.06 |
| Fair Over 4.5 odds | 1.56 |
| Fair Under 4.5 odds | 2.79 |
| Unadjusted home-win probability | 14.2% |
| Unadjusted draw probability | 12.2% |
| Unadjusted away-win probability | 73.7% |
| Raw p over 1 5 | 97.5% |
| Raw p under 3 5 | 18.8% |
| Raw p btts yes | 81.8% |
| P home draw | 38.0% |
| P draw away | 79.3% |
| Raw p home draw | 26.3% |
| Raw p draw away | 85.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.48 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.93 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -6.5% |
| Draw probability edge | -5.1% |
| Away probability edge | +11.6% |
| Over 2.5 probability edge | +22.3% |
| Under 2.5 probability edge | -22.3% |
| Raw edge prob home | -0.1307 |
| Raw ev home | -0.4928 |
| Raw edge prob draw | -0.1022 |
| Raw ev draw | -0.4745 |
| Raw edge prob away | 0.2330 |
| Raw ev away | 0.4586 |
| Market p home draw | 50.4% |
| Market home draw odds | 1.92 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:20:38Z |
| Market reference home draw last update utc | 2026-10-13T12:25:48Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.7% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:20:38Z |
| Market reference draw away last update utc | 2026-10-13T12:25:48Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.89 |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:18:44Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.6% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:18:44Z |
| Market reference under 3 5 odds | 1.70 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.0% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:20:38Z |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.96 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **71.9%**. Expected goals are 0.28 for LASK and 1.45 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 27.6%. Goal-market probabilities: at least one goal: 86.4%; Over 2.5 goals: 26.7%; Under 3.5 goals: 89.7%; Double Chance 1X: 28.1%; Double Chance X2: 91.6%; Under 4.5 goals: 96.6%; BTTS Yes (both teams score): 17.6%; BTTS No (at least one team does not score): 82.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 8.4% | 11.91 |
| Draw | 19.7% | 5.08 |
| Liverpool win | 71.9% | 1.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.45 |
| Expected total goals | 1.74 |
| Over 0.5 | 86.4% |
| Under 0.5 | 13.6% |
| Over 1.5 | 52.7% |
| Under 1.5 | 47.3% |
| Over 2.5 | 26.7% |
| Under 2.5 | 73.3% |
| Over 3.5 | 10.3% |
| Under 3.5 | 89.7% |
| Over 4.5 | 3.4% |
| Under 4.5 | 96.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 27.56% |
| 2 | 0-2 | 19.76% |
| 3 | 0-0 | 13.65% |
| 4 | 0-3 | 9.58% |
| 5 | 1-0 | 6.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 8.4% | 9.5% | 9.65 | -19.0% |
| Draw | 19.7% | 14.5% | 6.45 | +27.0% |
| Liverpool win | 71.9% | 76.0% | 1.32 | -5.1% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 17.6% |
| P btts no | 82.4% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.33 |
| Fair Over 1.5 odds | 1.90 |
| Fair Under 1.5 odds | 2.11 |
| Fair Over 2.5 odds | 3.75 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 9.73 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 29.50 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 67.8% |
| Raw p over 1 5 | 51.4% |
| Raw p under 3 5 | 90.1% |
| Raw p btts yes | 18.5% |
| P home draw | 28.1% |
| P draw away | 91.6% |
| Raw p home draw | 32.2% |
| Raw p draw away | 92.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 9.50 |
| Reference draw odds | 6.35 |
| Reference away odds | 1.30 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -1.1% |
| Draw probability edge | +5.2% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -44.9% |
| Under 2.5 probability edge | +44.9% |
| Raw edge prob home | -0.0222 |
| Raw ev home | -0.2967 |
| Raw edge prob draw | 0.1040 |
| Raw ev draw | 0.6052 |
| Raw edge prob away | -0.0819 |
| Raw ev away | -0.1047 |
| Market p home draw | 26.2% |
| Market home draw odds | 3.70 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:20:38Z |
| Market reference home draw last update utc | 2026-10-13T12:25:48Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.3% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:20:38Z |
| Market reference draw away last update utc | 2026-10-13T12:25:48Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.64 |
| Market reference dc draw away odds | 1.07 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 88.7% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:22:53Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.1% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:22:53Z |
| Market reference under 3 5 odds | 1.80 |
| Market reference under 3 5 opposite odds | 1.87 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.5% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:20:38Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.14 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **44.3%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.8%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 69.1%; Under 3.5 goals: 51.9%; Double Chance 1X: 55.7%; Double Chance X2: 65.8%; Under 4.5 goals: 71.1%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 34.2% | 2.92 |
| Draw | 21.5% | 4.65 |
| Paris Saint Germain win | 44.3% | 2.26 |

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
| 1 | 1-1 | 8.75% |
| 2 | 2-1 | 8.26% |
| 3 | 2-2 | 7.21% |
| 4 | 1-2 | 7.20% |
| 5 | 1-0 | 5.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 34.2% | 44.4% | 2.23 | -23.7% |
| Draw | 21.5% | 23.7% | 4.11 | -11.6% |
| Paris Saint Germain win | 44.3% | 31.9% | 3.08 | +36.3% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| Fair Under 0.5 odds | 40.23 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.53 |
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
| P home draw | 55.7% |
| P draw away | 65.8% |
| Raw p home draw | 43.3% |
| Raw p draw away | 76.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.20 |
| Reference draw odds | 4.05 |
| Reference away odds | 3.04 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -10.2% |
| Draw probability edge | -2.2% |
| Away probability edge | +12.4% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | -0.2041 |
| Raw ev home | -0.4643 |
| Raw edge prob draw | -0.0441 |
| Raw ev draw | -0.2068 |
| Raw edge prob away | 0.2482 |
| Raw ev away | 0.7457 |
| Market p home draw | 67.9% |
| Market home draw odds | 1.43 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:25:49Z |
| Market reference home draw last update utc | 2026-10-13T12:25:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.2% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:25:49Z |
| Market reference draw away last update utc | 2026-10-13T12:25:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.43 |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:25:03Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.5% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:25:03Z |
| Market reference under 3 5 odds | 1.70 |
| Market reference under 3 5 opposite odds | 1.99 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.0% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:25:49Z |
| Market reference btts yes odds | 1.37 |
| Market reference btts yes opposite odds | 2.89 |
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
| Porto win | 19.7% | 5.08 |

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
| 3 | 3-1 | 6.31% |
| 4 | 2-1 | 5.75% |
| 5 | 4-1 | 5.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 61.1% | 46.2% | 2.16 | +32.1% |
| Draw | 19.2% | 25.9% | 3.76 | -28.0% |
| Porto win | 19.7% | 27.9% | 3.50 | -31.1% |
| Over 2.5 | 80.9% | 55.3% | 1.79 | +44.9% |
| Under 2.5 | 19.1% | 44.7% | 2.19 | -58.3% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| Fair Under 0.5 odds | 80.52 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.77 |
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
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.10 |
| Reference draw odds | 3.66 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | +15.0% |
| Draw probability edge | -6.7% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | +25.7% |
| Under 2.5 probability edge | -25.7% |
| Raw edge prob home | 0.2995 |
| Raw ev home | 0.6441 |
| Raw edge prob draw | -0.1345 |
| Raw ev draw | -0.5324 |
| Raw edge prob away | -0.1650 |
| Raw ev away | -0.5993 |
| Market p home draw | 71.9% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:25:49Z |
| Market reference home draw last update utc | 2026-10-13T12:25:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.5% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:25:49Z |
| Market reference draw away last update utc | 2026-10-13T12:25:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.35 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 80.3% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:23:37Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.8% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:23:37Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.1% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:25:49Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.22 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.7%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 51.0%; Under 3.5 goals: 70.6%; Double Chance 1X: 65.9%; Double Chance X2: 60.3%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.7% | 2.52 |
| Draw | 26.2% | 3.82 |
| AEK Athens win | 34.1% | 2.93 |

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
| 1 | 1-1 | 12.37% |
| 2 | 1-0 | 9.37% |
| 3 | 0-1 | 9.11% |
| 4 | 2-1 | 8.21% |
| 5 | 1-2 | 7.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.7% | 36.1% | 2.73 | +8.3% |
| Draw | 26.2% | 28.2% | 3.47 | -9.2% |
| AEK Athens win | 34.1% | 35.7% | 2.77 | -5.4% |
| Over 2.5 | 51.0% | 50.6% | 1.95 | -0.6% |
| Under 2.5 | 49.0% | 49.4% | 1.99 | -2.4% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
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
| P home draw | 65.9% |
| P draw away | 60.3% |
| Raw p home draw | 67.4% |
| Raw p draw away | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.66 |
| Reference draw odds | 3.38 |
| Reference away odds | 2.69 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.93 |
| Home probability edge | +3.6% |
| Draw probability edge | -2.0% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.0711 |
| Raw ev home | 0.1804 |
| Raw edge prob draw | -0.0396 |
| Raw ev draw | -0.1604 |
| Raw edge prob away | -0.0315 |
| Raw ev away | -0.0979 |
| Market p home draw | 64.1% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:25:49Z |
| Market reference home draw last update utc | 2026-10-13T12:25:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.1% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:25:49Z |
| Market reference draw away last update utc | 2026-10-13T12:25:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.51 |
| Market reference dc draw away odds | 1.51 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 76.7% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:18:25Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:18:25Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.8% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:25:49Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.12 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.2%**. Expected goals are 1.46 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 72.6%; Under 3.5 goals: 48.5%; Double Chance 1X: 33.8%; Double Chance X2: 83.0%; Under 4.5 goals: 67.7%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.0% | 5.89 |
| Draw | 16.9% | 5.93 |
| VfB Stuttgart win | 66.2% | 1.51 |

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
| Over 2.5 | 72.6% |
| Under 2.5 | 27.4% |
| Over 3.5 | 51.5% |
| Under 3.5 | 48.5% |
| Over 4.5 | 32.3% |
| Under 4.5 | 67.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.71% |
| 2 | 1-3 | 8.04% |
| 3 | 0-2 | 7.36% |
| 4 | 0-1 | 7.02% |
| 5 | 1-1 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.0% | 9.1% | 10.00 | +69.7% |
| Draw | 16.9% | 14.5% | 6.48 | +9.4% |
| VfB Stuttgart win | 66.2% | 76.4% | 1.31 | -13.3% |

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
| Market best home last update utc | 2026-10-13T12:20:38Z |
| Market best draw last update utc | 2026-10-13T12:20:38Z |
| Market best away last update utc | 2026-10-13T12:20:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.2% |
| P btts no | 32.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.51 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.66 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.65 |
| Fair Over 3.5 odds | 1.94 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.09 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 24.8% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 55.9% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 68.2% |
| P home draw | 33.8% |
| P draw away | 83.0% |
| Raw p home draw | 44.1% |
| Raw p draw away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 9.60 |
| Reference draw odds | 6.20 |
| Reference away odds | 1.29 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Home probability edge | +7.8% |
| Draw probability edge | +2.4% |
| Away probability edge | -10.2% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.1569 |
| Raw ev home | 1.4815 |
| Raw edge prob draw | 0.0476 |
| Raw ev draw | 0.2477 |
| Raw edge prob away | -0.2044 |
| Raw ev away | -0.2673 |
| Market p home draw | 25.5% |
| Market home draw odds | 3.78 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:25:49Z |
| Market reference home draw last update utc | 2026-10-13T12:25:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.8% |
| Market draw away odds | 1.06 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:25:49Z |
| Market reference draw away last update utc | 2026-10-13T12:25:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.78 |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:24:20Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.5% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:24:20Z |
| Market reference under 3 5 odds | 1.85 |
| Market reference under 3 5 opposite odds | 1.82 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.1% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:25:49Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.13 |
| Market btts yes bookmakers | 1 |

</details>


---
