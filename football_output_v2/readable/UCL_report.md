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
| Training data health | {'completed_matches': 18, 'latest_completed_utc': '2026-09-10T19:00:00+00:00', 'latest_completed_date': '2026-09-10', 'next_fixture_utc': '2026-10-13T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-13T11:47:48.867891+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'e5a952fc3addc9a4e23d1d3bd4af8b31b836fd55452464d6ebbce16e4fdab9d0', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'LIVE_REFRESH_FAILED_USING_CACHE', 'download_age_hours': 0.06971773972222223, 'training_end': '2026-09-10', 'cache_hash_verified': True, 'last_refresh_error': 'ValueError'} |
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

The model's most likely 1X2 outcome is **Arsenal win** at **74.8%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.5%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 49.5%; Under 3.5 goals: 73.0%; Double Chance 1X: 91.0%; Double Chance X2: 25.2%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 39.4%; BTTS No (at least one team does not score): 60.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 74.8% | 1.34 |
| Draw | 16.2% | 6.16 |
| Lille win | 9.0% | 11.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.93 |
| Lille expected goals | 0.65 |
| Expected total goals | 2.58 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
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
| 2 | 2-0 | 15.41% |
| 3 | 2-1 | 10.08% |
| 4 | 3-0 | 9.91% |
| 5 | 1-1 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 74.8% | 81.3% | 1.23 | -8.1% |
| Draw | 16.2% | 12.9% | 7.80 | +26.6% |
| Lille win | 9.0% | 5.8% | 16.00 | +44.2% |
| Over 2.5 | 49.5% | 64.7% | 1.50 | -25.7% |
| Under 2.5 | 50.5% | 35.3% | 2.63 | +32.7% |

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
| Market best home last update utc | 2026-10-13T11:51:41Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:41Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 39.4% |
| P btts no | 60.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.05 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
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
| P home draw | 91.0% |
| P draw away | 25.2% |
| Raw p home draw | 87.8% |
| Raw p draw away | 31.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.21 |
| Reference draw odds | 6.63 |
| Reference away odds | 13.86 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.63 |
| Home probability edge | -6.6% |
| Draw probability edge | +3.4% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -15.1% |
| Under 2.5 probability edge | +15.1% |
| Raw edge prob home | -0.1316 |
| Raw ev home | -0.1615 |
| Raw edge prob draw | 0.0672 |
| Raw ev draw | 0.5283 |
| Raw edge prob away | 0.0644 |
| Raw ev away | 0.9575 |
| Market p home draw | 93.9% |
| Market home draw odds | 1.04 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:51:58Z |
| Market reference home draw last update utc | 2026-10-13T11:51:58Z |
| Market home draw bookmakers | 4 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 19.7% |
| Market draw away odds | 4.97 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:51:58Z |
| Market reference draw away last update utc | 2026-10-13T11:51:58Z |
| Market draw away bookmakers | 4 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.04 |
| Market reference dc draw away odds | 4.97 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 84.9% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 58.5% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:50:59Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.27 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 42.7% |
| Market btts yes odds | 2.23 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:58Z |
| Market reference btts yes odds | 2.23 |
| Market reference btts yes opposite odds | 1.69 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **63.7%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.8%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.8%; Under 3.5 goals: 24.6%; Double Chance 1X: 81.8%; Double Chance X2: 36.3%; Under 4.5 goals: 42.5%; BTTS Yes (both teams score): 78.8%; BTTS No (at least one team does not score): 21.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 63.7% | 1.57 |
| Draw | 18.1% | 5.53 |
| Manchester United win | 18.2% | 5.48 |

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
| Over 3.5 | 75.4% |
| Under 3.5 | 24.6% |
| Over 4.5 | 57.5% |
| Under 4.5 | 42.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.76% |
| 2 | 3-1 | 5.67% |
| 3 | 4-1 | 5.28% |
| 4 | 2-1 | 4.56% |
| 5 | 1-1 | 4.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 63.7% | 50.2% | 1.98 | +26.0% |
| Draw | 18.1% | 24.8% | 3.95 | -28.5% |
| Manchester United win | 18.2% | 25.0% | 4.10 | -25.2% |
| Over 2.5 | 87.8% | 58.3% | 1.71 | +50.2% |
| Under 2.5 | 12.2% | 41.7% | 2.33 | -71.6% |

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
| Market best home last update utc | 2026-10-13T11:51:41Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:56Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
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
| Fair Under 1.5 odds | 26.38 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.20 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.07 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 77.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 23.0% |
| Raw p btts yes | 76.6% |
| P home draw | 81.8% |
| P draw away | 36.3% |
| Raw p home draw | 88.5% |
| Raw p draw away | 22.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.93 |
| Reference draw odds | 3.79 |
| Reference away odds | 3.76 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.21 |
| Home probability edge | +13.4% |
| Draw probability edge | -6.7% |
| Away probability edge | -6.7% |
| Over 2.5 probability edge | +29.5% |
| Under 2.5 probability edge | -29.5% |
| Raw edge prob home | 0.2686 |
| Raw ev home | 0.5263 |
| Raw edge prob draw | -0.1337 |
| Raw ev draw | -0.5492 |
| Raw edge prob away | -0.1349 |
| Raw ev away | -0.5285 |
| Market p home draw | 74.7% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:51:41Z |
| Market reference home draw last update utc | 2026-10-13T11:51:41Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.6% |
| Market draw away odds | 1.93 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:51:35Z |
| Market reference draw away last update utc | 2026-10-13T11:51:41Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.30 |
| Market reference dc draw away odds | 1.92 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 63.2% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.56 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 60.7% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:35Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **66.8%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.6%. Goal-market probabilities: at least one goal: 98.7%; Over 2.5 goals: 77.6%; Under 3.5 goals: 41.8%; Double Chance 1X: 33.2%; Double Chance X2: 82.9%; Under 4.5 goals: 61.2%; BTTS Yes (both teams score): 71.0%; BTTS No (at least one team does not score): 29.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 17.1% | 5.84 |
| Draw | 16.1% | 6.22 |
| Barcelona win | 66.8% | 1.50 |

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
| 1 | 1-2 | 9.55% |
| 2 | 1-3 | 7.99% |
| 3 | 0-2 | 6.22% |
| 4 | 2-3 | 6.13% |
| 5 | 2-2 | 5.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 17.1% | 11.4% | 9.60 | +64.5% |
| Draw | 16.1% | 14.3% | 7.60 | +22.2% |
| Barcelona win | 66.8% | 74.4% | 1.33 | -11.2% |
| Over 2.5 | 77.6% | 82.4% | 1.20 | -6.9% |
| Under 2.5 | 22.4% | 17.6% | 4.79 | +7.3% |

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
| Market best home last update utc | 2026-10-13T11:51:56Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:41Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 71.0% |
| P btts no | 29.0% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 78.66 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.27 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.46 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.39 |
| Fair Over 4.5 odds | 2.58 |
| Fair Under 4.5 odds | 1.63 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.5% |
| Raw p btts yes | 71.7% |
| P home draw | 33.2% |
| P draw away | 82.9% |
| Raw p home draw | 40.8% |
| Raw p draw away | 77.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 8.10 |
| Reference draw odds | 6.51 |
| Reference away odds | 1.33 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.19 |
| Reference Under 2.5 odds | 4.79 |
| Home probability edge | +5.8% |
| Draw probability edge | +1.8% |
| Away probability edge | -7.6% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | 0.1152 |
| Raw ev home | 1.1982 |
| Raw edge prob draw | 0.0361 |
| Raw ev draw | 0.3595 |
| Raw edge prob away | -0.1514 |
| Raw ev away | -0.2125 |
| Market p home draw | 25.2% |
| Market home draw odds | 3.87 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:51:58Z |
| Market reference home draw last update utc | 2026-10-13T11:51:58Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.4% |
| Market draw away odds | 1.09 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T11:51:41Z |
| Market reference draw away last update utc | 2026-10-13T11:51:58Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.87 |
| Market reference dc draw away odds | 1.09 |
| Market reference dc home away odds | 1.14 |
| Market p over 1 5 | 94.5% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-13T11:51:41Z |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 12.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 36.2% |
| Market under 3 5 odds | 2.66 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference under 3 5 odds | 2.58 |
| Market reference under 3 5 opposite odds | 1.52 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 68.8% |
| Market btts yes odds | 1.42 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:58Z |
| Market reference btts yes odds | 1.42 |
| Market reference btts yes opposite odds | 2.99 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **69.9%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 56.4%; Under 3.5 goals: 66.8%; Double Chance 1X: 87.1%; Double Chance X2: 30.1%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 69.9% | 1.43 |
| Draw | 17.2% | 5.83 |
| Club Brugge win | 12.9% | 7.75 |

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
| 4 | 1-1 | 8.12% |
| 5 | 3-0 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 69.9% | 79.2% | 1.27 | -11.2% |
| Draw | 17.2% | 13.6% | 7.00 | +20.1% |
| Club Brugge win | 12.9% | 7.3% | 13.50 | +74.1% |
| Over 2.5 | 56.4% | 72.8% | 1.34 | -24.4% |
| Under 2.5 | 43.6% | 27.2% | 3.32 | +44.8% |

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
| Market best home last update utc | 2026-10-13T11:51:41Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:56Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.31 |
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
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.24 |
| Reference draw odds | 6.30 |
| Reference away odds | 11.22 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.32 |
| Home probability edge | -9.2% |
| Draw probability edge | +3.6% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -16.4% |
| Under 2.5 probability edge | +16.4% |
| Raw edge prob home | -0.1848 |
| Raw ev home | -0.2291 |
| Raw edge prob draw | 0.0719 |
| Raw ev draw | 0.4531 |
| Raw edge prob away | 0.1129 |
| Raw ev away | 1.5031 |
| Market p home draw | 92.1% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:51:58Z |
| Market reference home draw last update utc | 2026-10-13T11:51:58Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 23.0% |
| Market draw away odds | 4.24 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:51:58Z |
| Market reference draw away last update utc | 2026-10-13T11:51:58Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.06 |
| Market reference dc draw away odds | 4.24 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 48.7% |
| Market under 3 5 odds | 1.99 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T11:51:41Z |
| Market reference under 3 5 odds | 1.99 |
| Market reference under 3 5 opposite odds | 1.89 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 55.0% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:58Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.13 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **47.2%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 68.2%; Under 3.5 goals: 53.6%; Double Chance 1X: 67.9%; Double Chance X2: 52.8%; Under 4.5 goals: 72.3%; BTTS Yes (both teams score): 67.8%; BTTS No (at least one team does not score): 32.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 47.2% | 2.12 |
| Draw | 20.6% | 4.85 |
| PSV Eindhoven win | 32.1% | 3.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.65 |
| PSV Eindhoven expected goals | 1.87 |
| Expected total goals | 3.52 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 85.9% |
| Under 1.5 | 14.1% |
| Over 2.5 | 68.2% |
| Under 2.5 | 31.8% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.7% |
| Under 4.5 | 72.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.19% |
| 2 | 1-1 | 8.47% |
| 3 | 1-0 | 7.24% |
| 4 | 2-2 | 6.86% |
| 5 | 1-2 | 6.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 47.2% | 59.5% | 1.65 | -22.1% |
| Draw | 20.6% | 20.1% | 5.20 | +7.3% |
| PSV Eindhoven win | 32.1% | 20.4% | 4.95 | +59.0% |
| Over 2.5 | 68.2% | 77.6% | 1.26 | -14.1% |
| Under 2.5 | 31.8% | 22.4% | 3.91 | +24.4% |

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
| Market best home last update utc | 2026-10-13T11:51:41Z |
| Market best draw last update utc | 2026-10-13T11:51:10Z |
| Market best away last update utc | 2026-10-13T11:51:25Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.8% |
| P btts no | 32.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.81 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.10 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.14 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.61 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 35.0% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 67.8% |
| P home draw | 67.9% |
| P draw away | 52.8% |
| Raw p home draw | 56.2% |
| Raw p draw away | 65.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.65 |
| Reference draw odds | 4.70 |
| Reference away odds | 4.63 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.91 |
| Home probability edge | -12.3% |
| Draw probability edge | +0.5% |
| Away probability edge | +11.7% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.2452 |
| Raw ev home | -0.4229 |
| Raw edge prob draw | 0.0109 |
| Raw ev draw | 0.1016 |
| Raw edge prob away | 0.2343 |
| Raw ev away | 1.1700 |
| Market p home draw | 78.9% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:51:41Z |
| Market reference home draw last update utc | 2026-10-13T11:51:41Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.8% |
| Market draw away odds | 2.47 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:51:35Z |
| Market reference draw away last update utc | 2026-10-13T11:51:41Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.23 |
| Market reference dc draw away odds | 2.38 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 96.7% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.02 |
| Market reference over 1 5 opposite odds | 7.70 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 44.2% |
| Market under 3 5 odds | 2.25 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T11:51:41Z |
| Market reference under 3 5 odds | 2.22 |
| Market reference under 3 5 opposite odds | 1.77 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 72.9% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:35Z |
| Market reference btts yes odds | 1.32 |
| Market reference btts yes opposite odds | 3.15 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **41.1%**. Expected goals are 1.28 for RC Lens and 1.60 for Sporting Lisbon (2.89 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.7%; Under 3.5 goals: 67.4%; Double Chance 1X: 58.9%; Double Chance X2: 65.4%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 34.6% | 2.89 |
| Draw | 24.3% | 4.12 |
| Sporting Lisbon win | 41.1% | 2.44 |

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
| 2 | 0-1 | 8.59% |
| 3 | 1-0 | 8.58% |
| 4 | 1-2 | 8.31% |
| 5 | 2-1 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 34.6% | 38.1% | 2.66 | -7.9% |
| Draw | 24.3% | 25.3% | 3.85 | -6.4% |
| Sporting Lisbon win | 41.1% | 36.7% | 2.72 | +11.7% |
| Over 2.5 | 54.7% | 60.6% | 1.64 | -10.3% |
| Under 2.5 | 45.3% | 39.4% | 2.46 | +11.4% |

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
| Market best home last update utc | 2026-10-13T11:51:56Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:56Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
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
| P home draw | 58.9% |
| P draw away | 65.4% |
| Raw p home draw | 54.6% |
| Raw p draw away | 68.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.52 |
| Reference draw odds | 3.73 |
| Reference away odds | 2.61 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.34 |
| Home probability edge | -3.4% |
| Draw probability edge | -1.0% |
| Away probability edge | +4.4% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0684 |
| Raw ev home | -0.1697 |
| Raw edge prob draw | -0.0192 |
| Raw ev draw | -0.1014 |
| Raw edge prob away | 0.0876 |
| Raw ev away | 0.2361 |
| Market p home draw | 63.2% |
| Market home draw odds | 1.53 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:51:41Z |
| Market reference home draw last update utc | 2026-10-13T11:51:41Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.4% |
| Market draw away odds | 1.55 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T11:51:41Z |
| Market reference draw away last update utc | 2026-10-13T11:51:41Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.53 |
| Market reference dc draw away odds | 1.55 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 61.4% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T11:51:41Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.47 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 64.8% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-13T11:51:41Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.53 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **54.3%**. Expected goals are 0.38 for Sabah FK and 1.28 for Slavia Praha (1.66 combined). The most likely exact score is 0-1 at 22.4%. Goal-market probabilities: at least one goal: 82.4%; Over 2.5 goals: 22.8%; Under 3.5 goals: 91.7%; Double Chance 1X: 45.7%; Double Chance X2: 81.3%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 22.3%; BTTS No (at least one team does not score): 77.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 18.7% | 5.36 |
| Draw | 27.0% | 3.70 |
| Slavia Praha win | 54.3% | 1.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.38 |
| Slavia Praha expected goals | 1.28 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.4% |
| Under 0.5 | 17.6% |
| Over 1.5 | 47.5% |
| Under 1.5 | 52.5% |
| Over 2.5 | 22.8% |
| Under 2.5 | 77.2% |
| Over 3.5 | 8.3% |
| Under 3.5 | 91.7% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.42% |
| 2 | 0-0 | 17.55% |
| 3 | 0-2 | 14.09% |
| 4 | 1-0 | 12.57% |
| 5 | 1-1 | 8.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 18.7% | 25.9% | 4.00 | -25.3% |
| Draw | 27.0% | 25.5% | 4.00 | +8.0% |
| Slavia Praha win | 54.3% | 48.6% | 2.02 | +9.7% |
| Over 2.5 | 22.8% | 60.3% | 1.65 | -62.4% |
| Under 2.5 | 77.2% | 39.7% | 2.45 | +89.1% |

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
| Market best home last update utc | 2026-10-13T11:51:56Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:41Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 22.3% |
| P btts no | 77.7% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.70 |
| Fair Over 1.5 odds | 2.11 |
| Fair Under 1.5 odds | 1.90 |
| Fair Over 2.5 odds | 4.38 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 12.09 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 38.46 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.4% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 60.1% |
| Raw p over 1 5 | 49.0% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 22.4% |
| P home draw | 45.7% |
| P draw away | 81.3% |
| Raw p home draw | 39.9% |
| Raw p draw away | 88.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 3.69 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.01 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.31 |
| Home probability edge | -7.3% |
| Draw probability edge | +1.5% |
| Away probability edge | +5.7% |
| Over 2.5 probability edge | -37.5% |
| Under 2.5 probability edge | +37.5% |
| Raw edge prob home | -0.1450 |
| Raw ev home | -0.5432 |
| Raw edge prob draw | 0.0302 |
| Raw ev draw | 0.1404 |
| Raw edge prob away | 0.1149 |
| Raw ev away | 0.2134 |
| Market p home draw | 49.5% |
| Market home draw odds | 1.96 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:51:58Z |
| Market reference home draw last update utc | 2026-10-13T11:51:58Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.2% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | Marathon Bet |
| Market best draw away last update utc | 2026-10-13T11:51:14Z |
| Market reference draw away last update utc | 2026-10-13T11:51:58Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.96 |
| Market reference dc draw away odds | 1.29 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 61.3% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T11:51:41Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:58Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.57 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **91.4%**. Expected goals are 0.70 for Viking FK and 4.47 for Bayern Munich (5.17 combined). The most likely exact score is 0-4 at 9.3%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.0%; Under 3.5 goals: 25.3%; Double Chance 1X: 8.6%; Double Chance X2: 96.8%; Under 4.5 goals: 42.4%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 3.2% | 31.18 |
| Draw | 5.3% | 18.71 |
| Bayern Munich win | 91.4% | 1.09 |

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
| Over 4.5 | 57.6% |
| Under 4.5 | 42.4% |

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
| Viking FK win | 3.2% | 4.4% | 24.00 | -23.0% |
| Draw | 5.3% | 6.5% | 14.00 | -25.2% |
| Bayern Munich win | 91.4% | 89.0% | 1.13 | +3.3% |
| Over 2.5 | 88.0% | 86.3% | 1.15 | +1.2% |
| Under 2.5 | 12.0% | 13.7% | 5.90 | -29.2% |

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
| Market best home last update utc | 2026-10-13T11:51:25Z |
| Market best draw last update utc | 2026-10-13T11:50:33Z |
| Market best away last update utc | 2026-10-13T11:51:56Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.2% |
| P btts no | 49.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 160.79 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 24.94 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.33 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.95 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 2.0% |
| Unadjusted draw probability | 4.2% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.4% |
| Raw p btts yes | 49.5% |
| P home draw | 8.6% |
| P draw away | 96.8% |
| Raw p home draw | 6.1% |
| Raw p draw away | 98.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 16.42 |
| Reference draw odds | 11.64 |
| Reference away odds | 1.11 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.90 |
| Home probability edge | -1.2% |
| Draw probability edge | -1.2% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | +1.7% |
| Under 2.5 probability edge | -1.7% |
| Raw edge prob home | -0.0247 |
| Raw ev home | -0.5270 |
| Raw edge prob draw | -0.0235 |
| Raw ev draw | -0.4162 |
| Raw edge prob away | 0.0482 |
| Raw ev away | 0.0606 |
| Market p home draw | 12.6% |
| Market home draw odds | 8.00 |
| Best home draw bookmaker | William Hill |
| Market best home draw last update utc | 2026-10-13T11:51:41Z |
| Market reference home draw last update utc | 2026-10-13T11:51:41Z |
| Market home draw bookmakers | 4 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 95.1% |
| Market draw away odds | 1.03 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:51:35Z |
| Market reference draw away last update utc | 2026-10-13T11:51:41Z |
| Market draw away bookmakers | 4 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 7.70 |
| Market reference dc draw away odds | 1.02 |
| Market reference dc home away odds | 1.05 |
| Market p over 1 5 | 96.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 15.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 31.7% |
| Market under 3 5 odds | 2.95 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference under 3 5 odds | 2.70 |
| Market reference under 3 5 opposite odds | 1.39 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 57.9% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-13T11:51:41Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.17 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **39.0%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.7%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.0%; Double Chance X2: 64.7%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 44.4%; BTTS No (at least one team does not score): 55.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 35.3% | 2.83 |
| Draw | 25.7% | 3.90 |
| Napoli win | 39.0% | 2.56 |

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
| 1 | 1-0 | 13.71% |
| 2 | 1-1 | 11.87% |
| 3 | 0-1 | 11.48% |
| 4 | 0-0 | 9.20% |
| 5 | 2-1 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 35.3% | 46.2% | 2.16 | -23.7% |
| Draw | 25.7% | 25.5% | 3.80 | -2.5% |
| Napoli win | 39.0% | 28.3% | 3.60 | +40.5% |
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
| Market best home last update utc | 2026-10-13T11:51:56Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:56Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.4% |
| P btts no | 55.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.87 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.07 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 44.3% |
| P home draw | 61.0% |
| P draw away | 64.7% |
| Raw p home draw | 50.2% |
| Raw p draw away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.09 |
| Reference draw odds | 3.68 |
| Reference away odds | 3.33 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.19 |
| Home probability edge | -10.9% |
| Draw probability edge | +0.1% |
| Away probability edge | +10.7% |
| Over 2.5 probability edge | -17.7% |
| Under 2.5 probability edge | +17.7% |
| Raw edge prob home | -0.2171 |
| Raw ev home | -0.4719 |
| Raw edge prob draw | 0.0029 |
| Raw ev draw | -0.0198 |
| Raw edge prob away | 0.2143 |
| Raw ev away | 0.7911 |
| Market p home draw | 72.9% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:51:41Z |
| Market reference home draw last update utc | 2026-10-13T11:51:58Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.6% |
| Market draw away odds | 1.81 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:51:58Z |
| Market reference draw away last update utc | 2026-10-13T11:51:58Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.81 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 82.5% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.45 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 65.8% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.59 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 60.3% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:58Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.41 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **50.1%**. Expected goals are 1.18 for AS Roma and 1.67 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 54.2%; Under 3.5 goals: 67.9%; Double Chance 1X: 49.9%; Double Chance X2: 73.7%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.3% | 3.80 |
| Draw | 23.6% | 4.24 |
| Real Madrid win | 50.1% | 2.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.18 |
| Real Madrid expected goals | 1.67 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 54.2% |
| Under 2.5 | 45.8% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.07% |
| 2 | 0-1 | 10.34% |
| 3 | 1-2 | 9.65% |
| 4 | 0-2 | 8.17% |
| 5 | 1-0 | 7.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.3% | 25.1% | 3.90 | +2.6% |
| Draw | 23.6% | 24.1% | 4.16 | -2.0% |
| Real Madrid win | 50.1% | 50.8% | 2.02 | +1.2% |
| Over 2.5 | 54.2% | 67.5% | 1.44 | -21.9% |
| Under 2.5 | 45.8% | 32.5% | 2.88 | +31.8% |

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
| Market best home last update utc | 2026-10-13T11:51:25Z |
| Market best draw last update utc | 2026-10-13T11:51:41Z |
| Market best away last update utc | 2026-10-13T11:51:56Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.84 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.12 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.23 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 27.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 49.5% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.0% |
| Raw p btts yes | 55.7% |
| P home draw | 49.9% |
| P draw away | 73.7% |
| Raw p home draw | 50.5% |
| Raw p draw away | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 3.78 |
| Reference draw odds | 3.93 |
| Reference away odds | 1.92 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Home probability edge | +1.2% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -13.2% |
| Under 2.5 probability edge | +13.2% |
| Raw edge prob home | 0.0240 |
| Raw ev home | 0.0729 |
| Raw edge prob draw | -0.0110 |
| Raw ev draw | -0.0424 |
| Raw edge prob away | -0.0130 |
| Raw ev away | -0.0007 |
| Market p home draw | 49.4% |
| Market home draw odds | 1.96 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:51:41Z |
| Market reference home draw last update utc | 2026-10-13T11:51:41Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.4% |
| Market draw away odds | 1.32 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:51:35Z |
| Market reference draw away last update utc | 2026-10-13T11:51:41Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.96 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 54.4% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:49:27Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 68.9% |
| Market btts yes odds | 1.44 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:35Z |
| Market reference btts yes odds | 1.39 |
| Market reference btts yes opposite odds | 2.81 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **66.6%**. Expected goals are 2.23 for Aston Villa and 0.61 for Fenerbahce (2.84 combined). The most likely exact score is 2-0 at 12.9%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 51.6%; Under 3.5 goals: 69.9%; Double Chance 1X: 86.4%; Double Chance X2: 33.4%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 41.7%; BTTS No (at least one team does not score): 58.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 66.6% | 1.50 |
| Draw | 19.7% | 5.06 |
| Fenerbahce win | 13.6% | 7.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.23 |
| Fenerbahce expected goals | 0.61 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 51.6% |
| Under 2.5 | 48.4% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.95% |
| 2 | 1-0 | 11.95% |
| 3 | 3-0 | 9.63% |
| 4 | 1-1 | 9.23% |
| 5 | 2-1 | 7.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 66.6% | 58.4% | 1.69 | +12.6% |
| Draw | 19.7% | 23.4% | 4.30 | -15.1% |
| Fenerbahce win | 13.6% | 18.3% | 5.60 | -23.7% |
| Over 2.5 | 51.6% | 57.7% | 1.69 | -12.8% |
| Under 2.5 | 48.4% | 42.3% | 2.36 | +14.3% |

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
| Market best home last update utc | 2026-10-13T11:51:41Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:56Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 41.7% |
| P btts no | 58.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.98 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.32 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.78 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.1% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 40.3% |
| P home draw | 86.4% |
| P draw away | 33.4% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.67 |
| Reference draw odds | 3.99 |
| Reference away odds | 5.05 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | +8.3% |
| Draw probability edge | -3.6% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | 0.1655 |
| Raw ev home | 0.2660 |
| Raw edge prob draw | -0.0727 |
| Raw ev draw | -0.3073 |
| Raw edge prob away | -0.0928 |
| Raw ev away | -0.4970 |
| Market p home draw | 80.8% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:51:59Z |
| Market reference home draw last update utc | 2026-10-13T11:51:59Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 41.6% |
| Market draw away odds | 2.33 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:51:59Z |
| Market reference draw away last update utc | 2026-10-13T11:51:59Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.33 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.9% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 63.1% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 58.2% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:59Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.28 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **45.5%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.0%; Double Chance 1X: 54.5%; Double Chance X2: 67.7%; Under 4.5 goals: 69.6%; BTTS Yes (both teams score): 70.3%; BTTS No (at least one team does not score): 29.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 32.3% | 3.09 |
| Draw | 22.1% | 4.52 |
| Borussia Dortmund win | 45.5% | 2.20 |

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
| 1 | 1-1 | 8.67% |
| 2 | 1-2 | 8.63% |
| 3 | 2-2 | 7.65% |
| 4 | 2-1 | 6.75% |
| 5 | 0-1 | 5.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 32.3% | 29.2% | 3.30 | +6.7% |
| Draw | 22.1% | 23.5% | 4.20 | -7.1% |
| Borussia Dortmund win | 45.5% | 47.3% | 2.16 | -1.6% |
| Over 2.5 | 70.6% | 70.0% | 1.40 | -1.2% |
| Under 2.5 | 29.4% | 30.0% | 3.03 | -10.8% |

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
| Market best home last update utc | 2026-10-13T11:51:56Z |
| Market best draw last update utc | 2026-10-13T11:51:10Z |
| Market best away last update utc | 2026-10-13T11:51:56Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.3% |
| P btts no | 29.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.11 |
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
| P home draw | 54.5% |
| P draw away | 67.7% |
| Raw p home draw | 56.2% |
| Raw p draw away | 64.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 3.18 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.02 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.03 |
| Home probability edge | +3.2% |
| Draw probability edge | -1.4% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | 0.0631 |
| Raw ev home | 0.1715 |
| Raw edge prob draw | -0.0274 |
| Raw ev draw | -0.1285 |
| Raw edge prob away | -0.0357 |
| Raw ev away | -0.0550 |
| Market p home draw | 53.5% |
| Market home draw odds | 1.81 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:51:59Z |
| Market reference home draw last update utc | 2026-10-13T11:51:59Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.7% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T11:51:41Z |
| Market reference draw away last update utc | 2026-10-13T11:51:59Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.81 |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:48:19Z |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 1.98 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 70.9% |
| Market btts yes odds | 1.38 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:59Z |
| Market reference btts yes odds | 1.38 |
| Market reference btts yes opposite odds | 3.17 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **61.9%**. Expected goals are 1.82 for Feyenoord and 3.81 for Como (5.63 combined). The most likely exact score is 2-2 at 6.4%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.8%; Under 3.5 goals: 19.7%; Double Chance 1X: 38.1%; Double Chance X2: 79.9%; Under 4.5 goals: 36.0%; BTTS Yes (both teams score): 83.4%; BTTS No (at least one team does not score): 16.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 20.1% | 4.97 |
| Draw | 18.0% | 5.56 |
| Como win | 61.9% | 1.61 |

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
| Over 4.5 | 64.0% |
| Under 4.5 | 36.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.37% |
| 2 | 1-3 | 5.07% |
| 3 | 3-3 | 4.91% |
| 4 | 1-4 | 4.83% |
| 5 | 2-3 | 4.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 20.1% | 26.0% | 3.75 | -24.6% |
| Draw | 18.0% | 23.8% | 4.32 | -22.4% |
| Como win | 61.9% | 50.2% | 1.98 | +22.6% |
| Over 2.5 | 90.8% | 68.0% | 1.43 | +29.8% |
| Under 2.5 | 9.2% | 32.0% | 2.87 | -73.5% |

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
| Market best home last update utc | 2026-10-13T11:51:10Z |
| Market best draw last update utc | 2026-10-13T11:51:41Z |
| Market best away last update utc | 2026-10-13T11:51:41Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 83.4% |
| P btts no | 16.6% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 288.82 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 36.99 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.83 |
| Fair Over 3.5 odds | 1.25 |
| Fair Under 3.5 odds | 5.07 |
| Fair Over 4.5 odds | 1.56 |
| Fair Under 4.5 odds | 2.78 |
| Unadjusted home-win probability | 14.2% |
| Unadjusted draw probability | 12.2% |
| Unadjusted away-win probability | 73.7% |
| Raw p over 1 5 | 97.5% |
| Raw p under 3 5 | 18.8% |
| Raw p btts yes | 81.8% |
| P home draw | 38.1% |
| P draw away | 79.9% |
| Raw p home draw | 26.3% |
| Raw p draw away | 85.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 3.68 |
| Reference draw odds | 4.02 |
| Reference away odds | 1.95 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.87 |
| Home probability edge | -5.9% |
| Draw probability edge | -5.8% |
| Away probability edge | +11.7% |
| Over 2.5 probability edge | +22.8% |
| Under 2.5 probability edge | -22.8% |
| Raw edge prob home | -0.1188 |
| Raw ev home | -0.4687 |
| Raw edge prob draw | -0.1161 |
| Raw ev draw | -0.4745 |
| Raw edge prob away | 0.2349 |
| Raw ev away | 0.4586 |
| Market p home draw | 50.1% |
| Market home draw odds | 1.93 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:51:58Z |
| Market reference home draw last update utc | 2026-10-13T11:51:58Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.6% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T11:51:41Z |
| Market reference draw away last update utc | 2026-10-13T11:51:58Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.93 |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 54.5% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:46:29Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.11 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 67.9% |
| Market btts yes odds | 1.44 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:58Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.91 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **72.7%**. Expected goals are 0.28 for LASK and 1.45 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 27.8%. Goal-market probabilities: at least one goal: 86.5%; Over 2.5 goals: 26.8%; Under 3.5 goals: 89.6%; Double Chance 1X: 27.3%; Double Chance X2: 92.1%; Under 4.5 goals: 96.6%; BTTS Yes (both teams score): 17.6%; BTTS No (at least one team does not score): 82.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 7.9% | 12.66 |
| Draw | 19.4% | 5.14 |
| Liverpool win | 72.7% | 1.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.45 |
| Expected total goals | 1.74 |
| Over 0.5 | 86.5% |
| Under 0.5 | 13.5% |
| Over 1.5 | 52.9% |
| Under 1.5 | 47.1% |
| Over 2.5 | 26.8% |
| Under 2.5 | 73.2% |
| Over 3.5 | 10.4% |
| Under 3.5 | 89.6% |
| Over 4.5 | 3.4% |
| Under 4.5 | 96.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 27.84% |
| 2 | 0-2 | 19.97% |
| 3 | 0-0 | 13.49% |
| 4 | 0-3 | 9.68% |
| 5 | 1-0 | 5.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 7.9% | 8.5% | 10.50 | -17.1% |
| Draw | 19.4% | 14.0% | 6.75 | +31.3% |
| Liverpool win | 72.7% | 77.5% | 1.32 | -4.1% |
| Over 2.5 | 26.8% | 71.6% | 1.36 | -63.5% |
| Under 2.5 | 73.2% | 28.4% | 3.18 | +132.7% |

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
| Market best home last update utc | 2026-10-13T11:51:56Z |
| Market best draw last update utc | 2026-10-13T11:51:28Z |
| Market best away last update utc | 2026-10-13T11:51:41Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 17.6% |
| P btts no | 82.4% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.42 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.12 |
| Fair Over 2.5 odds | 3.73 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.66 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 29.27 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 67.8% |
| Raw p over 1 5 | 51.4% |
| Raw p under 3 5 | 90.1% |
| Raw p btts yes | 18.5% |
| P home draw | 27.3% |
| P draw away | 92.1% |
| Raw p home draw | 32.2% |
| Raw p draw away | 92.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 9.32 |
| Reference draw odds | 5.93 |
| Reference away odds | 1.26 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.18 |
| Home probability edge | -0.6% |
| Draw probability edge | +5.4% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -44.8% |
| Under 2.5 probability edge | +44.8% |
| Raw edge prob home | -0.0122 |
| Raw ev home | -0.2348 |
| Raw edge prob draw | 0.1087 |
| Raw ev draw | 0.6798 |
| Raw edge prob away | -0.0965 |
| Raw ev away | -0.1047 |
| Market p home draw | 26.1% |
| Market home draw odds | 3.97 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:51:35Z |
| Market reference home draw last update utc | 2026-10-13T11:51:41Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.1% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:51:35Z |
| Market reference draw away last update utc | 2026-10-13T11:51:41Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.70 |
| Market reference dc draw away odds | 1.07 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 51.0% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:46:49Z |
| Market reference under 3 5 odds | 1.90 |
| Market reference under 3 5 opposite odds | 1.97 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 56.4% |
| Market btts yes odds | 1.74 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:35Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **44.4%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 69.1%; Under 3.5 goals: 51.9%; Double Chance 1X: 55.6%; Double Chance X2: 65.8%; Under 4.5 goals: 71.0%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 34.2% | 2.92 |
| Draw | 21.4% | 4.67 |
| Paris Saint Germain win | 44.4% | 2.25 |

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
| Over 4.5 | 29.0% |
| Under 4.5 | 71.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.71% |
| 2 | 2-1 | 8.26% |
| 3 | 1-2 | 7.22% |
| 4 | 2-2 | 7.17% |
| 5 | 1-0 | 5.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 34.2% | 44.4% | 2.23 | -23.7% |
| Draw | 21.4% | 23.5% | 4.20 | -10.1% |
| Paris Saint Germain win | 44.4% | 32.1% | 3.10 | +37.6% |
| Over 2.5 | 69.1% | 67.0% | 1.45 | +0.3% |
| Under 2.5 | 30.9% | 33.0% | 2.80 | -13.6% |

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
| Market best home last update utc | 2026-10-13T11:51:41Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:56Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.9% |
| P btts no | 32.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.41 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.53 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.24 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.45 |
| Fair Under 4.5 odds | 1.41 |
| Unadjusted home-win probability | 24.0% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 56.7% |
| Raw p over 1 5 | 87.3% |
| Raw p under 3 5 | 50.8% |
| Raw p btts yes | 66.9% |
| P home draw | 55.6% |
| P draw away | 65.8% |
| Raw p home draw | 43.3% |
| Raw p draw away | 76.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.17 |
| Reference draw odds | 3.98 |
| Reference away odds | 2.96 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -10.2% |
| Draw probability edge | -2.1% |
| Away probability edge | +12.3% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | -0.2038 |
| Raw ev home | -0.4643 |
| Raw edge prob draw | -0.0422 |
| Raw ev draw | -0.1895 |
| Raw edge prob away | 0.2460 |
| Raw ev away | 0.7571 |
| Market p home draw | 67.5% |
| Market home draw odds | 1.43 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:51:41Z |
| Market reference home draw last update utc | 2026-10-13T11:51:58Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.8% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T11:51:41Z |
| Market reference draw away last update utc | 2026-10-13T11:51:58Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.43 |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 55.3% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:51:19Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.14 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 68.3% |
| Market btts yes odds | 1.43 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:58Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 2.94 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **60.9%**. Expected goals are 3.29 for Real Betis and 1.29 for Porto (4.58 combined). The most likely exact score is 2-2 at 7.1%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 80.9%; Under 3.5 goals: 35.2%; Double Chance 1X: 79.9%; Double Chance X2: 39.1%; Under 4.5 goals: 54.9%; BTTS Yes (both teams score): 72.3%; BTTS No (at least one team does not score): 27.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 60.9% | 1.64 |
| Draw | 19.0% | 5.26 |
| Porto win | 20.1% | 4.97 |

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
| 1 | 2-2 | 7.06% |
| 2 | 1-1 | 6.31% |
| 3 | 3-1 | 6.28% |
| 4 | 2-1 | 5.73% |
| 5 | 4-1 | 5.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 60.9% | 45.7% | 2.16 | +31.5% |
| Draw | 19.0% | 25.6% | 3.90 | -25.9% |
| Porto win | 20.1% | 28.8% | 3.70 | -25.6% |
| Over 2.5 | 80.9% | 55.8% | 1.79 | +44.9% |
| Under 2.5 | 19.1% | 44.2% | 2.19 | -58.3% |

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
| Market best home last update utc | 2026-10-13T11:51:41Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:56Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 72.3% |
| P btts no | 27.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 81.20 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.70 |
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
| P home draw | 79.9% |
| P draw away | 39.1% |
| Raw p home draw | 88.6% |
| Raw p draw away | 23.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.11 |
| Reference draw odds | 3.67 |
| Reference away odds | 3.28 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | +15.2% |
| Draw probability edge | -6.6% |
| Away probability edge | -8.7% |
| Over 2.5 probability edge | +25.1% |
| Under 2.5 probability edge | -25.1% |
| Raw edge prob home | 0.3043 |
| Raw ev home | 0.6441 |
| Raw edge prob draw | -0.1312 |
| Raw ev draw | -0.5150 |
| Raw edge prob away | -0.1731 |
| Raw ev away | -0.5764 |
| Market p home draw | 71.9% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:51:41Z |
| Market reference home draw last update utc | 2026-10-13T11:51:41Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.5% |
| Market draw away odds | 1.83 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:51:36Z |
| Market reference draw away last update utc | 2026-10-13T11:51:41Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.35 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 81.2% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 66.1% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.74 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 59.1% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:36Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.22 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.9%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 51.1%; Under 3.5 goals: 70.6%; Double Chance 1X: 65.5%; Double Chance X2: 60.1%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.9% | 2.50 |
| Draw | 25.6% | 3.91 |
| AEK Athens win | 34.5% | 2.90 |

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
| 1 | 1-1 | 12.09% |
| 2 | 1-0 | 9.43% |
| 3 | 0-1 | 9.20% |
| 4 | 2-1 | 8.26% |
| 5 | 1-2 | 7.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.9% | 36.7% | 2.76 | +10.3% |
| Draw | 25.6% | 27.0% | 3.55 | -9.2% |
| AEK Athens win | 34.5% | 36.4% | 2.77 | -4.5% |
| Over 2.5 | 51.1% | 52.2% | 1.95 | -0.3% |
| Under 2.5 | 48.9% | 47.8% | 2.01 | -1.8% |

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
| Market best home last update utc | 2026-10-13T11:51:56Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:41Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 67/100 |
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.15 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.09 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 54.7% |
| P home draw | 65.5% |
| P draw away | 60.1% |
| Raw p home draw | 67.4% |
| Raw p draw away | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.61 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.63 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | +3.3% |
| Draw probability edge | -1.4% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | 0.0658 |
| Raw ev home | 0.1934 |
| Raw edge prob draw | -0.0277 |
| Raw ev draw | -0.1410 |
| Raw edge prob away | -0.0380 |
| Raw ev away | -0.0979 |
| Market p home draw | 64.1% |
| Market home draw odds | 1.52 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:51:35Z |
| Market reference home draw last update utc | 2026-10-13T11:51:41Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.1% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T11:51:41Z |
| Market reference draw away last update utc | 2026-10-13T11:51:41Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.51 |
| Market reference dc draw away odds | 1.51 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 77.2% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.93 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 70.3% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T11:51:41Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.10 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 56.8% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:51:35Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.12 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.3%**. Expected goals are 1.46 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 72.7%; Under 3.5 goals: 48.5%; Double Chance 1X: 33.7%; Double Chance X2: 83.0%; Under 4.5 goals: 67.6%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.0% | 5.90 |
| Draw | 16.7% | 5.97 |
| VfB Stuttgart win | 66.3% | 1.51 |

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
| Over 2.5 | 72.7% |
| Under 2.5 | 27.3% |
| Over 3.5 | 51.5% |
| Under 3.5 | 48.5% |
| Over 4.5 | 32.4% |
| Under 4.5 | 67.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.74% |
| 2 | 1-3 | 8.06% |
| 3 | 0-2 | 7.38% |
| 4 | 0-1 | 7.04% |
| 5 | 1-1 | 6.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.0% | 9.1% | 11.00 | +86.5% |
| Draw | 16.7% | 14.2% | 6.60 | +10.5% |
| VfB Stuttgart win | 66.3% | 76.7% | 1.31 | -13.1% |
| Over 2.5 | 72.7% | 72.8% | 1.34 | -2.6% |
| Under 2.5 | 27.3% | 27.2% | 3.32 | -9.2% |

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
| Market best home last update utc | 2026-10-13T11:50:33Z |
| Market best draw last update utc | 2026-10-13T11:51:56Z |
| Market best away last update utc | 2026-10-13T11:51:41Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.2% |
| P btts no | 32.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.96 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.66 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.66 |
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
| P home draw | 33.7% |
| P draw away | 83.0% |
| Raw p home draw | 44.1% |
| Raw p draw away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 9.29 |
| Reference draw odds | 6.13 |
| Reference away odds | 1.28 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.32 |
| Home probability edge | +7.9% |
| Draw probability edge | +2.5% |
| Away probability edge | -10.4% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.1572 |
| Raw ev home | 1.7297 |
| Raw edge prob draw | 0.0503 |
| Raw ev draw | 0.2708 |
| Raw edge prob away | -0.2075 |
| Raw ev away | -0.2673 |
| Market p home draw | 25.4% |
| Market home draw odds | 3.82 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:52:00Z |
| Market reference home draw last update utc | 2026-10-13T11:52:00Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.0% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:52:00Z |
| Market reference draw away last update utc | 2026-10-13T11:52:00Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.82 |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:50:33Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 49.9% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:49:28Z |
| Market reference under 3 5 odds | 1.94 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 58.1% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:52:00Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.34 |
| Market btts yes bookmakers | 3 |

</details>


---
