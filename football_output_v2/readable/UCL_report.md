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
| Training data health | {'completed_matches': 18, 'latest_completed_utc': '2026-09-10T19:00:00+00:00', 'latest_completed_date': '2026-09-10', 'next_fixture_utc': '2026-10-13T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-13T12:43:15.877880+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'e5a952fc3addc9a4e23d1d3bd4af8b31b836fd55452464d6ebbce16e4fdab9d0', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.000614991111111111, 'training_end': '2026-09-10', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
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

The model's most likely 1X2 outcome is **Arsenal win** at **75.9%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.8%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 50.0%; Under 3.5 goals: 72.9%; Double Chance 1X: 90.9%; Double Chance X2: 24.1%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 39.0%; BTTS No (at least one team does not score): 61.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 75.9% | 1.32 |
| Draw | 15.0% | 6.66 |
| Lille win | 9.1% | 11.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.93 |
| Lille expected goals | 0.65 |
| Expected total goals | 2.58 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 50.0% |
| Under 2.5 | 50.0% |
| Over 3.5 | 27.1% |
| Under 3.5 | 72.9% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.76% |
| 2 | 2-0 | 15.65% |
| 3 | 2-1 | 10.24% |
| 4 | 3-0 | 10.07% |
| 5 | 1-1 | 6.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 75.9% | 83.6% | 1.23 | -6.6% |
| Draw | 15.0% | 10.4% | 7.06 | +6.0% |
| Lille win | 9.1% | 5.9% | 16.00 | +45.3% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 39.0% |
| P btts no | 61.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.44 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.68 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.78 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 72.5% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 40.6% |
| P home draw | 90.9% |
| P draw away | 24.1% |
| Raw p home draw | 87.8% |
| Raw p draw away | 31.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.17 |
| Reference draw odds | 7.30 |
| Reference away odds | 12.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.63 |
| Home probability edge | -7.7% |
| Draw probability edge | +4.6% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -14.6% |
| Under 2.5 probability edge | +14.6% |
| Raw edge prob home | -0.1548 |
| Raw ev home | -0.1615 |
| Raw edge prob draw | 0.0917 |
| Raw ev draw | 0.3833 |
| Raw edge prob away | 0.0631 |
| Raw ev away | 0.9575 |
| Market p home draw | 93.9% |
| Market home draw odds | 1.03 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:09Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 19.7% |
| Market draw away odds | 4.68 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:09Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.04 |
| Market reference dc draw away odds | 4.97 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 83.7% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:43:13Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.5% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:43:13Z |
| Market reference under 3 5 odds | 1.64 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 43.7% |
| Market btts yes odds | 2.21 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 2.28 |
| Market reference btts yes opposite odds | 1.77 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **64.1%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.8%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.8%; Under 3.5 goals: 24.5%; Double Chance 1X: 82.2%; Double Chance X2: 35.9%; Under 4.5 goals: 42.4%; BTTS Yes (both teams score): 78.8%; BTTS No (at least one team does not score): 21.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 64.1% | 1.56 |
| Draw | 18.1% | 5.53 |
| Manchester United win | 17.8% | 5.63 |

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
| 1 | 2-2 | 6.76% |
| 2 | 3-1 | 5.71% |
| 3 | 4-1 | 5.32% |
| 4 | 2-1 | 4.60% |
| 5 | 1-1 | 4.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 64.1% | 51.2% | 1.98 | +27.0% |
| Draw | 18.1% | 24.8% | 3.90 | -29.4% |
| Manchester United win | 17.8% | 24.1% | 3.94 | -30.0% |
| Over 2.5 | 87.8% | 58.3% | 1.71 | +50.2% |
| Under 2.5 | 12.2% | 41.7% | 2.33 | -71.7% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| Fair Under 0.5 odds | 171.58 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.56 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.22 |
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
| P home draw | 82.2% |
| P draw away | 35.9% |
| Raw p home draw | 88.5% |
| Raw p draw away | 22.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.85 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.21 |
| Home probability edge | +13.0% |
| Draw probability edge | -6.7% |
| Away probability edge | -6.3% |
| Over 2.5 probability edge | +29.5% |
| Under 2.5 probability edge | -29.5% |
| Raw edge prob home | 0.2592 |
| Raw ev home | 0.5263 |
| Raw edge prob draw | -0.1337 |
| Raw ev draw | -0.5549 |
| Raw edge prob away | -0.1255 |
| Raw ev away | -0.5469 |
| Market p home draw | 75.1% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.4% |
| Market draw away odds | 1.92 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.27 |
| Market reference dc draw away odds | 1.89 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 80.2% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:41:42Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.55 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.3% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:41:42Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.73 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.1% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.42 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **68.8%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 77.9%; Under 3.5 goals: 41.7%; Double Chance 1X: 31.2%; Double Chance X2: 83.8%; Under 4.5 goals: 60.9%; BTTS Yes (both teams score): 70.7%; BTTS No (at least one team does not score): 29.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 16.2% | 6.17 |
| Draw | 15.0% | 6.68 |
| Barcelona win | 68.8% | 1.45 |

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
| Over 2.5 | 77.9% |
| Under 2.5 | 22.1% |
| Over 3.5 | 58.3% |
| Under 3.5 | 41.7% |
| Over 4.5 | 39.1% |
| Under 4.5 | 60.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.84% |
| 2 | 1-3 | 8.23% |
| 3 | 0-2 | 6.41% |
| 4 | 2-3 | 6.32% |
| 5 | 0-1 | 5.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 16.2% | 9.5% | 8.70 | +41.1% |
| Draw | 15.0% | 12.1% | 6.66 | -0.3% |
| Barcelona win | 68.8% | 78.4% | 1.33 | -8.5% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.7% |
| P btts no | 29.3% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 84.50 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.33 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.53 |
| Fair Over 3.5 odds | 1.71 |
| Fair Under 3.5 odds | 2.40 |
| Fair Over 4.5 odds | 2.56 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.5% |
| Raw p btts yes | 71.7% |
| P home draw | 31.2% |
| P draw away | 83.8% |
| Raw p home draw | 40.8% |
| Raw p draw away | 77.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 8.00 |
| Reference draw odds | 6.50 |
| Reference away odds | 1.24 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.64 |
| Home probability edge | +6.7% |
| Draw probability edge | +2.9% |
| Away probability edge | -9.6% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | 0.1337 |
| Raw ev home | 0.9921 |
| Raw edge prob draw | 0.0583 |
| Raw ev draw | 0.1913 |
| Raw edge prob away | -0.1920 |
| Raw ev away | -0.2125 |
| Market p home draw | 26.1% |
| Market home draw odds | 3.62 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:08Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 88.5% |
| Market draw away odds | 1.09 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:08Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.73 |
| Market reference dc draw away odds | 1.10 |
| Market reference dc home away odds | 1.14 |
| Market p over 1 5 | 94.4% |
| Market over 1 5 odds | 1.01 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:39:31Z |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 11.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 35.7% |
| Market under 3 5 odds | 2.42 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:39:31Z |
| Market reference under 3 5 odds | 2.66 |
| Market reference under 3 5 opposite odds | 1.52 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 3.15 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **70.9%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.4%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 56.7%; Under 3.5 goals: 66.7%; Double Chance 1X: 87.2%; Double Chance X2: 29.1%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 50.0%; BTTS No (at least one team does not score): 50.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.9% | 1.41 |
| Draw | 16.3% | 6.14 |
| Club Brugge win | 12.8% | 7.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.92 |
| Club Brugge expected goals | 0.94 |
| Expected total goals | 2.86 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 56.7% |
| Under 2.5 | 43.3% |
| Over 3.5 | 33.3% |
| Under 3.5 | 66.7% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.40% |
| 2 | 2-0 | 12.28% |
| 3 | 2-1 | 11.59% |
| 4 | 3-0 | 7.85% |
| 5 | 1-1 | 7.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.9% | 81.1% | 1.27 | -10.0% |
| Draw | 16.3% | 11.8% | 6.74 | +9.8% |
| Club Brugge win | 12.8% | 7.1% | 12.10 | +55.0% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.55 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.64 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 3.00 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.79 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 51.6% |
| P home draw | 87.2% |
| P draw away | 29.1% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.20 |
| Reference draw odds | 6.40 |
| Reference away odds | 10.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.32 |
| Home probability edge | -10.2% |
| Draw probability edge | +4.5% |
| Away probability edge | +5.7% |
| Over 2.5 probability edge | -16.1% |
| Under 2.5 probability edge | +16.1% |
| Raw edge prob home | -0.2039 |
| Raw ev home | -0.2291 |
| Raw edge prob draw | 0.0893 |
| Raw ev draw | 0.3991 |
| Raw edge prob away | 0.1146 |
| Raw ev away | 1.2435 |
| Market p home draw | 92.1% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 23.0% |
| Market draw away odds | 4.14 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.06 |
| Market reference dc draw away odds | 4.24 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 89.1% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:42:04Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 7.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.3% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:42:04Z |
| Market reference under 3 5 odds | 1.96 |
| Market reference under 3 5 opposite odds | 1.91 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.3% |
| Market btts yes odds | 1.73 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.22 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **48.7%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 10.5%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 68.4%; Under 3.5 goals: 53.7%; Double Chance 1X: 68.4%; Double Chance X2: 51.3%; Under 4.5 goals: 72.2%; BTTS Yes (both teams score): 67.6%; BTTS No (at least one team does not score): 32.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 48.7% | 2.05 |
| Draw | 19.8% | 5.06 |
| PSV Eindhoven win | 31.6% | 3.17 |

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
| 1 | 2-1 | 10.50% |
| 2 | 1-1 | 8.11% |
| 3 | 1-0 | 7.46% |
| 4 | 2-2 | 6.57% |
| 5 | 1-2 | 6.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 48.7% | 62.4% | 1.61 | -21.6% |
| Draw | 19.8% | 18.4% | 5.08 | +0.4% |
| PSV Eindhoven win | 31.6% | 19.3% | 5.03 | +58.8% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| Fair Under 0.5 odds | 42.61 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.08 |
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
| P home draw | 68.4% |
| P draw away | 51.3% |
| Raw p home draw | 56.2% |
| Raw p draw away | 65.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.53 |
| Reference draw odds | 4.60 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.01 |
| Home probability edge | -13.7% |
| Draw probability edge | +1.4% |
| Away probability edge | +12.3% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | -0.2738 |
| Raw ev home | -0.4369 |
| Raw edge prob draw | 0.0283 |
| Raw ev draw | 0.0762 |
| Raw edge prob away | 0.2455 |
| Raw ev away | 1.2051 |
| Market p home draw | 79.9% |
| Market home draw odds | 1.21 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.6% |
| Market draw away odds | 2.46 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.40 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 91.7% |
| Market over 1 5 odds | 1.02 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:42:06Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 9.30 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 42.5% |
| Market under 3 5 odds | 2.28 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:42:06Z |
| Market reference under 3 5 odds | 2.25 |
| Market reference under 3 5 opposite odds | 1.69 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.9% |
| Market btts yes odds | 1.32 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 3.35 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **41.5%**. Expected goals are 1.28 for RC Lens and 1.60 for Sporting Lisbon (2.89 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.8%; Under 3.5 goals: 67.4%; Double Chance 1X: 58.5%; Double Chance X2: 65.6%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 34.4% | 2.91 |
| Draw | 24.2% | 4.14 |
| Sporting Lisbon win | 41.5% | 2.41 |

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
| Over 2.5 | 54.8% |
| Under 2.5 | 45.2% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.29% |
| 2 | 0-1 | 8.68% |
| 3 | 1-0 | 8.51% |
| 4 | 1-2 | 8.39% |
| 5 | 2-1 | 8.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 34.4% | 37.5% | 2.62 | -10.0% |
| Draw | 24.2% | 25.0% | 3.85 | -6.9% |
| Sporting Lisbon win | 41.5% | 37.5% | 2.67 | +10.7% |
| Over 2.5 | 54.8% | 60.6% | 1.64 | -10.2% |
| Under 2.5 | 45.2% | 39.4% | 2.46 | +11.3% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| Fair Under 0.5 odds | 19.31 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.08 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.2% |
| P home draw | 58.5% |
| P draw away | 65.6% |
| Raw p home draw | 54.6% |
| Raw p draw away | 68.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.50 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.34 |
| Home probability edge | -3.1% |
| Draw probability edge | -0.8% |
| Away probability edge | +4.0% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0628 |
| Raw ev home | -0.1822 |
| Raw edge prob draw | -0.0167 |
| Raw ev draw | -0.1014 |
| Raw edge prob away | 0.0795 |
| Raw ev away | 0.2134 |
| Market p home draw | 64.1% |
| Market home draw odds | 1.53 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.4% |
| Market draw away odds | 1.55 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.49 |
| Market reference dc draw away odds | 1.53 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:36:10Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.4% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:36:10Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.47 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.5% |
| Market btts yes odds | 1.47 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.54 |
| Market reference btts yes opposite odds | 2.78 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **55.6%**. Expected goals are 0.38 for Sabah FK and 1.28 for Slavia Praha (1.66 combined). The most likely exact score is 0-1 at 23.0%. Goal-market probabilities: at least one goal: 82.9%; Over 2.5 goals: 23.1%; Under 3.5 goals: 91.6%; Double Chance 1X: 44.4%; Double Chance X2: 81.9%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 22.1%; BTTS No (at least one team does not score): 77.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 18.1% | 5.52 |
| Draw | 26.3% | 3.81 |
| Slavia Praha win | 55.6% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.38 |
| Slavia Praha expected goals | 1.28 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.9% |
| Under 0.5 | 17.1% |
| Over 1.5 | 47.8% |
| Under 1.5 | 52.2% |
| Over 2.5 | 23.1% |
| Under 2.5 | 76.9% |
| Over 3.5 | 8.4% |
| Under 3.5 | 91.6% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.95% |
| 2 | 0-0 | 17.08% |
| 3 | 0-2 | 14.42% |
| 4 | 1-0 | 12.18% |
| 5 | 1-1 | 8.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 18.1% | 24.8% | 3.78 | -31.6% |
| Draw | 26.3% | 24.1% | 3.90 | +2.5% |
| Slavia Praha win | 55.6% | 51.2% | 2.02 | +12.4% |
| Over 2.5 | 23.1% | 60.3% | 1.65 | -61.9% |
| Under 2.5 | 76.9% | 39.7% | 2.45 | +88.5% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| P btts yes | 22.1% |
| P btts no | 77.9% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.85 |
| Fair Over 1.5 odds | 2.09 |
| Fair Under 1.5 odds | 1.92 |
| Fair Over 2.5 odds | 4.33 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.94 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.84 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.4% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 60.1% |
| Raw p over 1 5 | 49.0% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 22.4% |
| P home draw | 44.4% |
| P draw away | 81.9% |
| Raw p home draw | 39.9% |
| Raw p draw away | 88.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.60 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.85 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.31 |
| Home probability edge | -6.7% |
| Draw probability edge | +2.2% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | -37.3% |
| Under 2.5 probability edge | +37.3% |
| Raw edge prob home | -0.1336 |
| Raw ev home | -0.5683 |
| Raw edge prob draw | 0.0446 |
| Raw ev draw | 0.1119 |
| Raw edge prob away | 0.0890 |
| Raw ev away | 0.2134 |
| Market p home draw | 50.0% |
| Market home draw odds | 1.88 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.7% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.94 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:40:59Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.4% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:40:59Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.47 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.4% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.59 |
| Market reference btts yes opposite odds | 2.62 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **91.5%**. Expected goals are 0.70 for Viking FK and 4.47 for Bayern Munich (5.17 combined). The most likely exact score is 0-4 at 9.3%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.0%; Under 3.5 goals: 25.3%; Double Chance 1X: 8.5%; Double Chance X2: 97.0%; Under 4.5 goals: 42.5%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 3.0% | 33.29 |
| Draw | 5.5% | 18.05 |
| Bayern Munich win | 91.5% | 1.09 |

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
| Over 2.5 | 88.0% |
| Under 2.5 | 12.0% |
| Over 3.5 | 74.7% |
| Under 3.5 | 25.3% |
| Over 4.5 | 57.5% |
| Under 4.5 | 42.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.30% |
| 2 | 0-3 | 8.33% |
| 3 | 0-5 | 8.31% |
| 4 | 1-4 | 6.48% |
| 5 | 0-6 | 6.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 3.0% | 4.0% | 21.00 | -36.9% |
| Draw | 5.5% | 6.9% | 13.90 | -23.0% |
| Bayern Munich win | 91.5% | 89.1% | 1.11 | +1.5% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| Fair Under 0.5 odds | 155.11 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 25.11 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.30 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.96 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 2.0% |
| Unadjusted draw probability | 4.2% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.4% |
| Raw p btts yes | 49.5% |
| P home draw | 8.5% |
| P draw away | 97.0% |
| Raw p home draw | 6.1% |
| Raw p draw away | 98.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 14.00 |
| Reference draw odds | 9.00 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.90 |
| Home probability edge | -1.0% |
| Draw probability edge | -1.4% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | -0.0207 |
| Raw ev home | -0.5862 |
| Raw edge prob draw | -0.0274 |
| Raw ev draw | -0.4203 |
| Raw edge prob away | 0.0480 |
| Raw ev away | 0.0418 |
| Market p home draw | 13.0% |
| Market home draw odds | 7.70 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:42:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 94.9% |
| Market draw away odds | 1.02 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:42:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 7.40 |
| Market reference dc draw away odds | 1.01 |
| Market reference dc home away odds | 1.04 |
| Market p over 1 5 | 95.5% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:35:26Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 14.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 31.6% |
| Market under 3 5 odds | 2.76 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:35:26Z |
| Market reference under 3 5 odds | 2.95 |
| Market reference under 3 5 opposite odds | 1.43 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.2% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.38 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **38.8%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.2%; Double Chance X2: 64.4%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 44.4%; BTTS No (at least one team does not score): 55.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 35.6% | 2.81 |
| Draw | 25.6% | 3.91 |
| Napoli win | 38.8% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.90 |
| Napoli expected goals | 1.42 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 65.6% |
| Under 1.5 | 34.4% |
| Over 2.5 | 40.2% |
| Under 2.5 | 59.8% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.82% |
| 2 | 1-1 | 11.83% |
| 3 | 0-1 | 11.42% |
| 4 | 0-0 | 9.16% |
| 5 | 2-1 | 8.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 35.6% | 46.8% | 2.15 | -23.4% |
| Draw | 25.6% | 25.3% | 3.76 | -3.9% |
| Napoli win | 38.8% | 27.9% | 3.50 | +35.9% |
| Over 2.5 | 40.2% | 57.9% | 1.72 | -30.8% |
| Under 2.5 | 59.8% | 42.1% | 2.30 | +37.5% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| P btts yes | 44.4% |
| P btts no | 55.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.91 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.07 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 44.3% |
| P home draw | 61.2% |
| P draw away | 64.4% |
| Raw p home draw | 50.2% |
| Raw p draw away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.19 |
| Home probability edge | -11.2% |
| Draw probability edge | +0.2% |
| Away probability edge | +10.9% |
| Over 2.5 probability edge | -17.7% |
| Under 2.5 probability edge | +17.7% |
| Raw edge prob home | -0.2231 |
| Raw ev home | -0.4743 |
| Raw edge prob draw | 0.0048 |
| Raw ev draw | -0.0301 |
| Raw edge prob away | 0.2183 |
| Raw ev away | 0.7414 |
| Market p home draw | 72.9% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.6% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.81 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 80.6% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:42:26Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.55 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.1% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:42:26Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.8% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.46 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **49.9%**. Expected goals are 1.18 for AS Roma and 1.67 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.4%; Under 3.5 goals: 67.9%; Double Chance 1X: 50.1%; Double Chance X2: 72.9%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 27.1% | 3.69 |
| Draw | 22.9% | 4.36 |
| Real Madrid win | 49.9% | 2.00 |

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
| 1 | 1-1 | 10.78% |
| 2 | 0-1 | 10.30% |
| 3 | 1-2 | 9.61% |
| 4 | 0-2 | 8.14% |
| 5 | 1-0 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 27.1% | 26.7% | 3.85 | +4.4% |
| Draw | 22.9% | 22.9% | 4.16 | -4.5% |
| Real Madrid win | 49.9% | 50.4% | 1.94 | -3.1% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.35 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.40 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.12 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.20 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 27.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 49.5% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.0% |
| Raw p btts yes | 55.7% |
| P home draw | 50.1% |
| P draw away | 72.9% |
| Raw p home draw | 50.5% |
| Raw p draw away | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.86 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Home probability edge | +0.4% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -13.1% |
| Under 2.5 probability edge | +13.1% |
| Raw edge prob home | 0.0077 |
| Raw ev home | 0.0591 |
| Raw edge prob draw | 0.0014 |
| Raw ev draw | -0.0424 |
| Raw edge prob away | -0.0091 |
| Raw ev away | -0.0403 |
| Market p home draw | 50.4% |
| Market home draw odds | 1.96 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.3% |
| Market draw away odds | 1.30 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.92 |
| Market reference dc draw away odds | 1.32 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 86.7% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:42:26Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.2% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:42:26Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.9% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.92 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **67.5%**. Expected goals are 2.23 for Aston Villa and 0.61 for Fenerbahce (2.84 combined). The most likely exact score is 2-0 at 13.1%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 51.9%; Under 3.5 goals: 69.8%; Double Chance 1X: 86.6%; Double Chance X2: 32.5%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 41.5%; BTTS No (at least one team does not score): 58.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 67.5% | 1.48 |
| Draw | 19.1% | 5.25 |
| Fenerbahce win | 13.4% | 7.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.23 |
| Fenerbahce expected goals | 0.61 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.12% |
| 2 | 1-0 | 12.11% |
| 3 | 3-0 | 9.76% |
| 4 | 1-1 | 8.91% |
| 5 | 2-1 | 7.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 67.5% | 60.1% | 1.69 | +14.1% |
| Draw | 19.1% | 22.0% | 4.26 | -18.8% |
| Fenerbahce win | 13.4% | 17.9% | 5.33 | -28.4% |
| Over 2.5 | 51.9% | 57.7% | 1.69 | -12.3% |
| Under 2.5 | 48.1% | 42.3% | 2.36 | +13.5% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| P btts yes | 41.5% |
| P btts no | 58.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.52 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.09 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.71 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.1% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 40.3% |
| P home draw | 86.6% |
| P draw away | 32.5% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.58 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.70 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | +7.4% |
| Draw probability edge | -2.9% |
| Away probability edge | -4.4% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.1479 |
| Raw ev home | 0.2660 |
| Raw edge prob draw | -0.0589 |
| Raw ev draw | -0.3137 |
| Raw edge prob away | -0.0890 |
| Raw ev away | -0.5213 |
| Market p home draw | 80.8% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 41.6% |
| Market draw away odds | 2.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.33 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 81.5% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:31:23Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.85 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.0% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:31:23Z |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.57 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.2% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.28 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **45.8%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-2 at 8.7%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.0%; Double Chance 1X: 54.2%; Double Chance X2: 67.4%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 70.2%; BTTS No (at least one team does not score): 29.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 32.6% | 3.06 |
| Draw | 21.5% | 4.64 |
| Borussia Dortmund win | 45.8% | 2.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 1.73 |
| Borussia Dortmund expected goals | 1.94 |
| Expected total goals | 3.67 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 50.0% |
| Under 3.5 | 50.0% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.68% |
| 2 | 1-1 | 8.44% |
| 3 | 2-2 | 7.44% |
| 4 | 2-1 | 6.81% |
| 5 | 0-1 | 5.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 32.6% | 29.8% | 3.29 | +7.4% |
| Draw | 21.5% | 22.3% | 4.11 | -11.5% |
| Borussia Dortmund win | 45.8% | 47.9% | 2.14 | -1.9% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| Fair Under 0.5 odds | 45.32 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.13 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.42 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.27 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 35.5% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 50.1% |
| Raw p btts yes | 70.0% |
| P home draw | 54.2% |
| P draw away | 67.4% |
| Raw p home draw | 56.2% |
| Raw p draw away | 64.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.95 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.03 |
| Home probability edge | +2.9% |
| Draw probability edge | -0.8% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | 0.0571 |
| Raw ev home | 0.1680 |
| Raw edge prob draw | -0.0156 |
| Raw ev draw | -0.1472 |
| Raw edge prob away | -0.0415 |
| Raw ev away | -0.0637 |
| Market p home draw | 54.1% |
| Market home draw odds | 1.79 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.1% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.79 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 88.2% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:32:50Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.90 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.8% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:32:50Z |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.9% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.42 |
| Market reference btts yes opposite odds | 3.25 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **62.1%**. Expected goals are 1.82 for Feyenoord and 3.81 for Como (5.63 combined). The most likely exact score is 2-2 at 6.2%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.8%; Under 3.5 goals: 19.7%; Double Chance 1X: 37.9%; Double Chance X2: 79.6%; Under 4.5 goals: 35.9%; BTTS Yes (both teams score): 83.3%; BTTS No (at least one team does not score): 16.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 20.4% | 4.90 |
| Draw | 17.5% | 5.72 |
| Como win | 62.1% | 1.61 |

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
| 1 | 2-2 | 6.20% |
| 2 | 1-3 | 5.09% |
| 3 | 1-4 | 4.85% |
| 4 | 3-3 | 4.77% |
| 5 | 2-3 | 4.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 20.4% | 26.6% | 3.58 | -27.0% |
| Draw | 17.5% | 22.8% | 4.32 | -24.5% |
| Como win | 62.1% | 50.6% | 1.98 | +23.0% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| Fair Under 0.5 odds | 297.02 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 36.84 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.91 |
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
| P home draw | 37.9% |
| P draw away | 79.6% |
| Raw p home draw | 26.3% |
| Raw p draw away | 85.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.85 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.87 |
| Home probability edge | -6.2% |
| Draw probability edge | -5.3% |
| Away probability edge | +11.5% |
| Over 2.5 probability edge | +22.9% |
| Under 2.5 probability edge | -22.9% |
| Raw edge prob home | -0.1247 |
| Raw ev home | -0.4928 |
| Raw edge prob draw | -0.1062 |
| Raw ev draw | -0.4745 |
| Raw edge prob away | 0.2309 |
| Raw ev away | 0.4586 |
| Market p home draw | 50.1% |
| Market home draw odds | 1.92 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.6% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.93 |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 86.7% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:35:27Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.1% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:35:27Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.09 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.1% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.98 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **73.3%**. Expected goals are 0.28 for LASK and 1.45 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 28.1%. Goal-market probabilities: at least one goal: 87.0%; Over 2.5 goals: 27.0%; Under 3.5 goals: 89.6%; Double Chance 1X: 26.7%; Double Chance X2: 92.1%; Under 4.5 goals: 96.6%; BTTS Yes (both teams score): 17.5%; BTTS No (at least one team does not score): 82.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 7.9% | 12.66 |
| Draw | 18.8% | 5.32 |
| Liverpool win | 73.3% | 1.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.45 |
| Expected total goals | 1.74 |
| Over 0.5 | 87.0% |
| Under 0.5 | 13.0% |
| Over 1.5 | 53.1% |
| Under 1.5 | 46.9% |
| Over 2.5 | 27.0% |
| Under 2.5 | 73.0% |
| Over 3.5 | 10.4% |
| Under 3.5 | 89.6% |
| Over 4.5 | 3.4% |
| Under 4.5 | 96.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 28.09% |
| 2 | 0-2 | 20.15% |
| 3 | 0-0 | 13.03% |
| 4 | 0-3 | 9.77% |
| 5 | 1-0 | 5.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 7.9% | 8.5% | 9.65 | -23.8% |
| Draw | 18.8% | 12.7% | 6.45 | +21.2% |
| Liverpool win | 73.3% | 78.8% | 1.32 | -3.2% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 17.5% |
| P btts no | 82.5% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.67 |
| Fair Over 1.5 odds | 1.88 |
| Fair Under 1.5 odds | 2.13 |
| Fair Over 2.5 odds | 3.70 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.60 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 29.02 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 67.8% |
| Raw p over 1 5 | 51.4% |
| Raw p under 3 5 | 90.1% |
| Raw p btts yes | 18.5% |
| P home draw | 26.7% |
| P draw away | 92.1% |
| Raw p home draw | 32.2% |
| Raw p draw away | 92.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 8.50 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.23 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.18 |
| Home probability edge | -0.6% |
| Draw probability edge | +6.1% |
| Away probability edge | -5.5% |
| Over 2.5 probability edge | -44.5% |
| Under 2.5 probability edge | +44.5% |
| Raw edge prob home | -0.0122 |
| Raw ev home | -0.2967 |
| Raw edge prob draw | 0.1218 |
| Raw ev draw | 0.6052 |
| Raw edge prob away | -0.1096 |
| Raw ev away | -0.1047 |
| Market p home draw | 24.5% |
| Market home draw odds | 3.70 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.1% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.97 |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home away odds | 1.14 |
| Market p over 1 5 | 88.2% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:39:30Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.90 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:39:30Z |
| Market reference under 3 5 odds | 1.88 |
| Market reference under 3 5 opposite odds | 1.99 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.5% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.14 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **44.8%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.5%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 69.3%; Under 3.5 goals: 51.9%; Double Chance 1X: 55.2%; Double Chance X2: 65.6%; Under 4.5 goals: 70.9%; BTTS Yes (both teams score): 67.7%; BTTS No (at least one team does not score): 32.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 34.4% | 2.90 |
| Draw | 20.8% | 4.80 |
| Paris Saint Germain win | 44.8% | 2.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.40 |
| Paris Saint Germain expected goals | 2.23 |
| Expected total goals | 3.63 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 69.3% |
| Under 2.5 | 30.7% |
| Over 3.5 | 48.1% |
| Under 3.5 | 51.9% |
| Over 4.5 | 29.1% |
| Under 4.5 | 70.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.47% |
| 2 | 2-1 | 8.31% |
| 3 | 1-2 | 7.28% |
| 4 | 2-2 | 6.97% |
| 5 | 1-0 | 5.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 34.4% | 44.8% | 2.23 | -23.2% |
| Draw | 20.8% | 22.3% | 4.11 | -14.5% |
| Paris Saint Germain win | 44.8% | 32.8% | 3.08 | +37.9% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.57 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.52 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.26 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.44 |
| Fair Under 4.5 odds | 1.41 |
| Unadjusted home-win probability | 24.0% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 56.7% |
| Raw p over 1 5 | 87.3% |
| Raw p under 3 5 | 50.8% |
| Raw p btts yes | 66.9% |
| P home draw | 55.2% |
| P draw away | 65.6% |
| Raw p home draw | 43.3% |
| Raw p draw away | 76.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.10 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.80 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -10.4% |
| Draw probability edge | -1.5% |
| Away probability edge | +11.9% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | -0.2081 |
| Raw ev home | -0.4643 |
| Raw edge prob draw | -0.0303 |
| Raw ev draw | -0.2068 |
| Raw edge prob away | 0.2384 |
| Raw ev away | 0.7457 |
| Market p home draw | 67.5% |
| Market home draw odds | 1.43 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.8% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.43 |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 86.6% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:41:42Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.1% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:41:42Z |
| Market reference under 3 5 odds | 1.76 |
| Market reference under 3 5 opposite odds | 2.14 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.4% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.98 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **61.7%**. Expected goals are 3.29 for Real Betis and 1.29 for Porto (4.58 combined). The most likely exact score is 2-2 at 6.9%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 81.1%; Under 3.5 goals: 35.1%; Double Chance 1X: 80.3%; Double Chance X2: 38.3%; Under 4.5 goals: 54.7%; BTTS Yes (both teams score): 72.1%; BTTS No (at least one team does not score): 27.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 61.7% | 1.62 |
| Draw | 18.5% | 5.40 |
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
| Over 2.5 | 81.1% |
| Under 2.5 | 18.9% |
| Over 3.5 | 64.9% |
| Under 3.5 | 35.1% |
| Over 4.5 | 45.3% |
| Under 4.5 | 54.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.89% |
| 2 | 3-1 | 6.37% |
| 3 | 1-1 | 6.16% |
| 4 | 2-1 | 5.81% |
| 5 | 4-1 | 5.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 61.7% | 47.4% | 2.16 | +33.4% |
| Draw | 18.5% | 24.6% | 3.76 | -30.3% |
| Porto win | 19.7% | 28.0% | 3.50 | -30.9% |
| Over 2.5 | 81.1% | 56.4% | 1.79 | +45.2% |
| Under 2.5 | 18.9% | 43.6% | 2.19 | -58.6% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| Fair Under 0.5 odds | 83.25 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.79 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.29 |
| Fair Over 3.5 odds | 1.54 |
| Fair Under 3.5 odds | 2.85 |
| Fair Over 4.5 odds | 2.21 |
| Fair Under 4.5 odds | 1.83 |
| Unadjusted home-win probability | 76.1% |
| Unadjusted draw probability | 12.4% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 94.1% |
| Raw p under 3 5 | 32.9% |
| Raw p btts yes | 69.6% |
| P home draw | 80.3% |
| P draw away | 38.3% |
| Raw p home draw | 88.6% |
| Raw p draw away | 23.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.98 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.19 |
| Home probability edge | +14.4% |
| Draw probability edge | -6.1% |
| Away probability edge | -8.3% |
| Over 2.5 probability edge | +24.8% |
| Under 2.5 probability edge | -24.8% |
| Raw edge prob home | 0.2875 |
| Raw ev home | 0.6441 |
| Raw edge prob draw | -0.1219 |
| Raw ev draw | -0.5324 |
| Raw edge prob away | -0.1656 |
| Raw ev away | -0.5993 |
| Market p home draw | 72.2% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.9% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 80.1% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:41:21Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.6% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:41:21Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.6% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.35 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.5%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 51.1%; Under 3.5 goals: 70.6%; Double Chance 1X: 65.0%; Double Chance X2: 60.5%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.5% | 2.53 |
| Draw | 25.6% | 3.91 |
| AEK Athens win | 35.0% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.49 |
| AEK Athens expected goals | 1.25 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.07% |
| 2 | 0-1 | 9.33% |
| 3 | 1-0 | 9.32% |
| 4 | 2-1 | 8.17% |
| 5 | 1-2 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.5% | 35.7% | 2.73 | +7.8% |
| Draw | 25.6% | 26.9% | 3.47 | -11.3% |
| AEK Athens win | 35.0% | 37.3% | 2.77 | -3.2% |
| Over 2.5 | 51.1% | 51.5% | 1.95 | -0.3% |
| Under 2.5 | 48.9% | 48.5% | 1.99 | -2.7% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
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
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.16 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.41 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.09 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 54.7% |
| P home draw | 65.0% |
| P draw away | 60.5% |
| Raw p home draw | 67.4% |
| Raw p draw away | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.55 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.45 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 2.04 |
| Home probability edge | +3.8% |
| Draw probability edge | -1.4% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.0750 |
| Raw ev home | 0.1804 |
| Raw edge prob draw | -0.0272 |
| Raw ev draw | -0.1604 |
| Raw edge prob away | -0.0478 |
| Raw ev away | -0.0979 |
| Market p home draw | 63.5% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.4% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.52 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 75.6% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:43:13Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:43:13Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.30 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.26 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **67.0%**. Expected goals are 1.46 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 72.9%; Under 3.5 goals: 48.5%; Double Chance 1X: 33.0%; Double Chance X2: 82.9%; Under 4.5 goals: 67.5%; BTTS Yes (both teams score): 67.0%; BTTS No (at least one team does not score): 33.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.1% | 5.84 |
| Draw | 15.9% | 6.30 |
| VfB Stuttgart win | 67.0% | 1.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.46 |
| VfB Stuttgart expected goals | 2.25 |
| Expected total goals | 3.71 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 88.5% |
| Under 1.5 | 11.5% |
| Over 2.5 | 72.9% |
| Under 2.5 | 27.1% |
| Over 3.5 | 51.5% |
| Under 3.5 | 48.5% |
| Over 4.5 | 32.5% |
| Under 4.5 | 67.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.85% |
| 2 | 1-3 | 8.14% |
| 3 | 0-2 | 7.46% |
| 4 | 0-1 | 7.11% |
| 5 | 1-1 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.1% | 9.4% | 10.00 | +71.2% |
| Draw | 15.9% | 12.5% | 6.48 | +2.9% |
| VfB Stuttgart win | 67.0% | 78.1% | 1.31 | -12.2% |

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
| Market best home last update utc | 2026-10-13T12:42:00Z |
| Market best draw last update utc | 2026-10-13T12:42:00Z |
| Market best away last update utc | 2026-10-13T12:42:00Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.0% |
| P btts no | 33.0% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 59.01 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.66 |
| Fair Over 2.5 odds | 1.37 |
| Fair Under 2.5 odds | 3.69 |
| Fair Over 3.5 odds | 1.94 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.07 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 24.8% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 55.9% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 68.2% |
| P home draw | 33.0% |
| P draw away | 82.9% |
| Raw p home draw | 44.1% |
| Raw p draw away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 7.80 |
| Reference draw odds | 6.10 |
| Reference away odds | 1.24 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.32 |
| Home probability edge | +7.7% |
| Draw probability edge | +3.4% |
| Away probability edge | -11.1% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.1540 |
| Raw ev home | 1.4815 |
| Raw edge prob draw | 0.0676 |
| Raw ev draw | 0.2477 |
| Raw edge prob away | -0.2215 |
| Raw ev away | -0.2673 |
| Market p home draw | 25.4% |
| Market home draw odds | 3.78 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T12:42:00Z |
| Market reference home draw last update utc | 2026-10-13T12:43:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.0% |
| Market draw away odds | 1.06 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T12:42:00Z |
| Market reference draw away last update utc | 2026-10-13T12:43:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.82 |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 88.4% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-13T12:34:19Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 7.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 50.0% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T12:34:19Z |
| Market reference under 3 5 odds | 1.93 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.4% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-13T12:42:00Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 1 |

</details>


---
