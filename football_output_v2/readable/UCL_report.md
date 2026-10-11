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
| Base scoring parameter | 0.142 |
| Home-advantage parameter | 0.278 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0 |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 15.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |
| Data mode | offline_replay_of_committed_provider_responses |
| Provider response source commit | 1cd7e6bed154f42a64d727330bff7e94e7913210 |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-13 — Arsenal vs Lille

The model's most likely 1X2 outcome is **Arsenal win** at **74.2%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.4%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 49.5%; Under 3.5 goals: 73.1%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 39.4%; BTTS No (at least one team does not score): 60.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 74.2% | 1.35 |
| Draw | 16.1% | 6.23 |
| Lille win | 9.8% | 10.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.93 |
| Lille expected goals | 0.65 |
| Expected total goals | 2.58 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 73.5% |
| Under 1.5 | 26.5% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.37% |
| 2 | 2-0 | 15.29% |
| 3 | 2-1 | 10.00% |
| 4 | 3-0 | 9.83% |
| 5 | 1-1 | 7.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 74.2% | 80.2% | 1.29 | -4.3% |
| Draw | 16.1% | 12.5% | 7.40 | +18.8% |
| Lille win | 9.8% | 7.3% | 14.50 | +41.9% |
| Over 2.5 | 49.5% | 61.3% | 1.67 | -17.3% |
| Under 2.5 | 50.5% | 38.7% | 2.50 | +26.3% |

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
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:57:12Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 39.4% |
| P btts no | 60.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.25 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.77 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.90 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 72.5% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 40.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.21 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -6.0% |
| Draw probability edge | +3.5% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -11.8% |
| Under 2.5 probability edge | +11.8% |
| Raw edge prob home | -0.1200 |
| Raw ev home | -0.1207 |
| Raw edge prob draw | 0.0709 |
| Raw ev draw | 0.4503 |
| Raw edge prob away | 0.0490 |
| Raw ev away | 0.7750 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **63.9%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.5%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.9%; Under 3.5 goals: 24.6%; Under 4.5 goals: 42.3%; BTTS Yes (both teams score): 78.7%; BTTS No (at least one team does not score): 21.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 63.9% | 1.57 |
| Draw | 17.3% | 5.78 |
| Manchester United win | 18.8% | 5.31 |

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
| Over 2.5 | 87.9% |
| Under 2.5 | 12.1% |
| Over 3.5 | 75.4% |
| Under 3.5 | 24.6% |
| Over 4.5 | 57.7% |
| Under 4.5 | 42.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.46% |
| 2 | 3-1 | 5.68% |
| 3 | 4-1 | 5.30% |
| 4 | 2-1 | 4.58% |
| 5 | 3-2 | 4.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 63.9% | 50.7% | 2.07 | +32.2% |
| Draw | 17.3% | 23.2% | 4.10 | -29.1% |
| Manchester United win | 18.8% | 26.2% | 3.75 | -29.4% |
| Over 2.5 | 87.9% | 63.8% | 1.50 | +31.9% |
| Under 2.5 | 12.1% | 36.2% | 2.66 | -67.9% |

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
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:57:12Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 78.7% |
| P btts no | 21.3% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 179.78 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.21 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.30 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.07 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.37 |
| Unadjusted home-win probability | 77.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 23.0% |
| Raw p btts yes | 76.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.86 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | +13.2% |
| Draw probability edge | -5.9% |
| Away probability edge | -7.3% |
| Over 2.5 probability edge | +24.2% |
| Under 2.5 probability edge | -24.2% |
| Raw edge prob home | 0.2642 |
| Raw ev home | 0.5957 |
| Raw edge prob draw | -0.1175 |
| Raw ev draw | -0.5321 |
| Raw edge prob away | -0.1467 |
| Raw ev away | -0.5687 |
| Market p over 1 5 | 85.4% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:57:13Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 57.3% |
| Market under 3 5 odds | 1.73 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T08:43:52Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.23 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 66.7% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:57:12Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.70 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **69.3%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 78.0%; Under 3.5 goals: 41.7%; Under 4.5 goals: 60.8%; BTTS Yes (both teams score): 70.6%; BTTS No (at least one team does not score): 29.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 16.1% | 6.23 |
| Draw | 14.6% | 6.83 |
| Barcelona win | 69.3% | 1.44 |

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
| Over 2.5 | 78.0% |
| Under 2.5 | 22.0% |
| Over 3.5 | 58.3% |
| Under 3.5 | 41.7% |
| Over 4.5 | 39.2% |
| Under 4.5 | 60.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.91% |
| 2 | 1-3 | 8.29% |
| 3 | 0-2 | 6.46% |
| 4 | 2-3 | 6.36% |
| 5 | 0-1 | 5.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 16.1% | 9.2% | 10.00 | +60.6% |
| Draw | 14.6% | 11.4% | 7.40 | +8.3% |
| Barcelona win | 69.3% | 79.4% | 1.34 | -7.1% |
| Over 2.5 | 78.0% | 81.3% | 1.21 | -5.6% |
| Under 2.5 | 22.0% | 18.7% | 4.50 | -1.1% |

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
| Market best home last update utc | 2026-10-11T08:57:12Z |
| Market best draw last update utc | 2026-10-11T08:56:55Z |
| Market best away last update utc | 2026-10-11T08:56:39Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.6% |
| P btts no | 29.4% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 86.40 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.34 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.55 |
| Fair Over 3.5 odds | 1.71 |
| Fair Under 3.5 odds | 2.40 |
| Fair Over 4.5 odds | 2.55 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.5% |
| Raw p btts yes | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 7.80 |
| Reference draw odds | 6.50 |
| Reference away odds | 1.22 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.40 |
| Home probability edge | +6.8% |
| Draw probability edge | +3.2% |
| Away probability edge | -10.1% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | 0.1368 |
| Raw ev home | 1.2902 |
| Raw edge prob draw | 0.0650 |
| Raw ev draw | 0.3238 |
| Raw edge prob away | -0.2018 |
| Raw ev away | -0.2066 |
| Market p over 1 5 | 93.5% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:43:45Z |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 10.50 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 37.7% |
| Market under 3 5 odds | 2.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:43:30Z |
| Market reference under 3 5 odds | 2.47 |
| Market reference under 3 5 opposite odds | 1.55 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 68.0% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:43:30Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 2.88 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **70.4%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 56.6%; Under 3.5 goals: 66.7%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.4% | 1.42 |
| Draw | 16.6% | 6.01 |
| Club Brugge win | 12.9% | 7.73 |

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
| Over 2.5 | 56.6% |
| Under 2.5 | 43.4% |
| Over 3.5 | 33.3% |
| Under 3.5 | 66.7% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.31% |
| 2 | 2-0 | 12.20% |
| 3 | 2-1 | 11.52% |
| 4 | 1-1 | 7.87% |
| 5 | 3-0 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.4% | 80.2% | 1.31 | -7.7% |
| Draw | 16.6% | 12.5% | 6.60 | +9.8% |
| Club Brugge win | 12.9% | 7.3% | 12.00 | +55.3% |
| Over 2.5 | 56.6% | 67.0% | 1.44 | -18.5% |
| Under 2.5 | 43.4% | 33.0% | 2.83 | +22.9% |

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
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:57:12Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.05 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.63 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
| Fair Over 3.5 odds | 3.00 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.81 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 51.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.21 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -9.7% |
| Draw probability edge | +4.1% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | -0.1946 |
| Raw ev home | -0.2048 |
| Raw edge prob draw | 0.0825 |
| Raw ev draw | 0.3701 |
| Raw edge prob away | 0.1120 |
| Raw ev away | 1.2249 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **44.9%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 68.1%; Under 3.5 goals: 53.6%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 44.9% | 2.23 |
| Draw | 21.1% | 4.75 |
| PSV Eindhoven win | 34.0% | 2.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.65 |
| PSV Eindhoven expected goals | 1.87 |
| Expected total goals | 3.52 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 86.0% |
| Under 1.5 | 14.0% |
| Over 2.5 | 68.1% |
| Under 2.5 | 31.9% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.69% |
| 2 | 1-1 | 8.65% |
| 3 | 2-2 | 7.00% |
| 4 | 1-0 | 6.88% |
| 5 | 1-2 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 44.9% | 54.8% | 1.90 | -14.7% |
| Draw | 21.1% | 21.0% | 4.80 | +1.1% |
| PSV Eindhoven win | 34.0% | 24.2% | 3.95 | +34.4% |
| Over 2.5 | 68.1% | 71.6% | 1.35 | -8.1% |
| Under 2.5 | 31.9% | 28.4% | 3.26 | +4.0% |

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
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:56:55Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.9% |
| P btts no | 32.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.97 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.12 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.13 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.62 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 35.0% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 67.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.72 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -9.9% |
| Draw probability edge | +0.1% |
| Away probability edge | +9.8% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.1986 |
| Raw ev home | -0.3354 |
| Raw edge prob draw | 0.0023 |
| Raw ev draw | 0.0169 |
| Raw edge prob away | 0.1963 |
| Raw ev away | 0.7314 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **41.0%**. Expected goals are 1.28 for RC Lens and 1.60 for Sporting Lisbon (2.89 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.7%; Under 3.5 goals: 67.4%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 34.7% | 2.88 |
| Draw | 24.3% | 4.12 |
| Sporting Lisbon win | 41.0% | 2.44 |

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
| 1 | 1-1 | 11.34% |
| 2 | 1-0 | 8.60% |
| 3 | 0-1 | 8.58% |
| 4 | 1-2 | 8.30% |
| 5 | 2-1 | 8.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 34.7% | 38.2% | 2.62 | -9.1% |
| Draw | 24.3% | 25.2% | 3.91 | -5.0% |
| Sporting Lisbon win | 41.0% | 36.5% | 2.78 | +14.0% |
| Over 2.5 | 54.7% | 59.8% | 1.64 | -10.3% |
| Under 2.5 | 45.3% | 40.2% | 2.46 | +11.4% |

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
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:57:12Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
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
| Fair Under 0.5 odds | 19.22 |
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
| Unadjusted away-win probability | 45.5% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.40 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -3.5% |
| Draw probability edge | -1.0% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.0701 |
| Raw ev home | -0.1823 |
| Raw edge prob draw | -0.0191 |
| Raw ev draw | -0.0874 |
| Raw edge prob away | 0.0891 |
| Raw ev away | 0.2635 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **54.4%**. Expected goals are 0.38 for Sabah FK and 1.28 for Slavia Praha (1.66 combined). The most likely exact score is 0-1 at 22.5%. Goal-market probabilities: at least one goal: 82.7%; Over 2.5 goals: 22.8%; Under 3.5 goals: 91.8%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 22.0%; BTTS No (at least one team does not score): 78.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 19.1% | 5.24 |
| Draw | 26.5% | 3.78 |
| Slavia Praha win | 54.4% | 1.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.38 |
| Slavia Praha expected goals | 1.28 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.7% |
| Under 0.5 | 17.3% |
| Over 1.5 | 47.3% |
| Under 1.5 | 52.7% |
| Over 2.5 | 22.8% |
| Under 2.5 | 77.2% |
| Over 3.5 | 8.2% |
| Under 3.5 | 91.8% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.53% |
| 2 | 0-0 | 17.28% |
| 3 | 0-2 | 14.14% |
| 4 | 1-0 | 12.90% |
| 5 | 1-1 | 8.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 19.1% | 26.9% | 3.74 | -28.6% |
| Draw | 26.5% | 24.4% | 4.00 | +5.9% |
| Slavia Praha win | 54.4% | 48.8% | 2.12 | +15.4% |
| Over 2.5 | 22.8% | 57.8% | 1.71 | -61.1% |
| Under 2.5 | 77.2% | 42.2% | 2.32 | +79.2% |

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
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:56:24Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 22.0% |
| P btts no | 78.0% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.79 |
| Fair Over 1.5 odds | 2.11 |
| Fair Under 1.5 odds | 1.90 |
| Fair Over 2.5 odds | 4.39 |
| Fair Under 2.5 odds | 1.29 |
| Fair Over 3.5 odds | 12.20 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 38.79 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.3% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 60.1% |
| Raw p over 1 5 | 48.8% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 22.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.60 |
| Reference away odds | 1.92 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | -7.8% |
| Draw probability edge | +2.1% |
| Away probability edge | +5.7% |
| Over 2.5 probability edge | -35.0% |
| Under 2.5 probability edge | +35.0% |
| Raw edge prob home | -0.1552 |
| Raw ev home | -0.5761 |
| Raw edge prob draw | 0.0415 |
| Raw ev draw | 0.1420 |
| Raw edge prob away | 0.1136 |
| Raw ev away | 0.2744 |
| Market p over 1 5 | 81.0% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:43:48Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 64.5% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:43:30Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.61 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.1% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:43:30Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.32 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **92.7%**. Expected goals are 0.70 for Viking FK and 4.46 for Bayern Munich (5.16 combined). The most likely exact score is 0-4 at 9.4%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.4%; Under 3.5 goals: 24.9%; Under 4.5 goals: 42.0%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 2.5% | 40.25 |
| Draw | 4.8% | 20.85 |
| Bayern Munich win | 92.7% | 1.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.70 |
| Bayern Munich expected goals | 4.46 |
| Expected total goals | 5.16 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 88.4% |
| Under 2.5 | 11.6% |
| Over 3.5 | 75.1% |
| Under 3.5 | 24.9% |
| Over 4.5 | 58.0% |
| Under 4.5 | 42.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.44% |
| 2 | 0-3 | 8.46% |
| 3 | 0-5 | 8.42% |
| 4 | 1-4 | 6.58% |
| 5 | 0-6 | 6.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 2.5% | 3.0% | 27.00 | -32.9% |
| Draw | 4.8% | 5.4% | 15.50 | -25.7% |
| Bayern Munich win | 92.7% | 91.6% | 1.11 | +2.9% |
| Over 2.5 | 88.4% | 85.4% | 1.15 | +1.6% |
| Under 2.5 | 11.6% | 14.6% | 5.90 | -31.3% |

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
| Market best home last update utc | 2026-10-11T08:56:55Z |
| Market best draw last update utc | 2026-10-11T08:56:39Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 178.68 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.19 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.59 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.02 |
| Fair Over 4.5 odds | 1.72 |
| Fair Under 4.5 odds | 2.38 |
| Unadjusted home-win probability | 2.0% |
| Unadjusted draw probability | 4.2% |
| Unadjusted away-win probability | 93.8% |
| Raw p over 1 5 | 96.3% |
| Raw p under 3 5 | 24.5% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 15.00 |
| Reference draw odds | 9.50 |
| Reference away odds | 1.07 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.50 |
| Home probability edge | -0.5% |
| Draw probability edge | -0.6% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | -0.0101 |
| Raw ev home | -0.4657 |
| Raw edge prob draw | -0.0122 |
| Raw ev draw | -0.3512 |
| Raw edge prob away | 0.0223 |
| Raw ev away | 0.0416 |
| Market p over 1 5 | 95.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-11T08:56:25Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 13.00 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 32.7% |
| Market under 3 5 odds | 2.93 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T08:56:24Z |
| Market reference under 3 5 odds | 2.64 |
| Market reference under 3 5 opposite odds | 1.41 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 53.9% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-11T08:57:16Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 2.06 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **40.1%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 40.3%; Under 3.5 goals: 80.2%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 44.4%; BTTS No (at least one team does not score): 55.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 34.4% | 2.91 |
| Draw | 25.5% | 3.92 |
| Napoli win | 40.1% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.90 |
| Napoli expected goals | 1.42 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 65.7% |
| Under 1.5 | 34.3% |
| Over 2.5 | 40.3% |
| Under 2.5 | 59.7% |
| Over 3.5 | 19.8% |
| Under 3.5 | 80.2% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.34% |
| 2 | 1-1 | 11.81% |
| 3 | 0-1 | 11.80% |
| 4 | 0-0 | 9.15% |
| 5 | 0-2 | 8.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 34.4% | 44.3% | 2.33 | -19.9% |
| Draw | 25.5% | 25.3% | 3.90 | -0.4% |
| Napoli win | 40.1% | 30.5% | 3.30 | +32.4% |
| Over 2.5 | 40.3% | 58.9% | 1.71 | -31.1% |
| Under 2.5 | 59.7% | 41.1% | 2.44 | +45.6% |

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
| Market best home last update utc | 2026-10-11T08:56:56Z |
| Market best draw last update utc | 2026-10-11T08:56:55Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.4% |
| P btts no | 55.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.92 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.92 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.06 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.02 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 44.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.95 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -9.9% |
| Draw probability edge | +0.3% |
| Away probability edge | +9.6% |
| Over 2.5 probability edge | -18.6% |
| Under 2.5 probability edge | +18.6% |
| Raw edge prob home | -0.1982 |
| Raw ev home | -0.4304 |
| Raw edge prob draw | 0.0054 |
| Raw ev draw | 0.0060 |
| Raw edge prob away | 0.1928 |
| Raw ev away | 0.6420 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **51.0%**. Expected goals are 1.18 for AS Roma and 1.68 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.5%; Under 3.5 goals: 67.8%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.1% | 3.82 |
| Draw | 22.9% | 4.37 |
| Real Madrid win | 51.0% | 1.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.18 |
| Real Madrid expected goals | 1.68 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 54.5% |
| Under 2.5 | 45.5% |
| Over 3.5 | 32.2% |
| Under 3.5 | 67.8% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.75% |
| 2 | 0-1 | 10.46% |
| 3 | 1-2 | 9.78% |
| 4 | 0-2 | 8.31% |
| 5 | 1-0 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.1% | 25.0% | 4.20 | +9.8% |
| Draw | 22.9% | 22.8% | 4.30 | -1.5% |
| Real Madrid win | 51.0% | 52.2% | 1.95 | -0.6% |
| Over 2.5 | 54.5% | 68.9% | 1.42 | -22.6% |
| Under 2.5 | 45.5% | 31.1% | 2.90 | +31.9% |

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
| Market best home last update utc | 2026-10-11T08:56:55Z |
| Market best draw last update utc | 2026-10-11T08:56:24Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.41 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.42 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.17 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 27.3% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 49.7% |
| Raw p over 1 5 | 77.3% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Home probability edge | +1.1% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -14.4% |
| Under 2.5 probability edge | +14.4% |
| Raw edge prob home | 0.0230 |
| Raw ev home | 0.1463 |
| Raw edge prob draw | 0.0015 |
| Raw ev draw | -0.0123 |
| Raw edge prob away | -0.0244 |
| Raw ev away | -0.0301 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **67.0%**. Expected goals are 2.24 for Aston Villa and 0.61 for Fenerbahce (2.85 combined). The most likely exact score is 2-0 at 13.0%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.8%; Under 3.5 goals: 69.8%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 41.6%; BTTS No (at least one team does not score): 58.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 67.0% | 1.49 |
| Draw | 19.4% | 5.16 |
| Fenerbahce win | 13.6% | 7.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.24 |
| Fenerbahce expected goals | 0.61 |
| Expected total goals | 2.85 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 51.8% |
| Under 2.5 | 48.2% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.00% |
| 2 | 1-0 | 11.95% |
| 3 | 3-0 | 9.71% |
| 4 | 1-1 | 9.05% |
| 5 | 2-1 | 7.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 67.0% | 58.9% | 1.74 | +16.6% |
| Draw | 19.4% | 22.7% | 4.35 | -15.8% |
| Fenerbahce win | 13.6% | 18.4% | 5.40 | -26.4% |
| Over 2.5 | 51.8% | 56.9% | 1.74 | -9.8% |
| Under 2.5 | 48.2% | 43.1% | 2.32 | +11.8% |

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
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:57:12Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 41.6% |
| P btts no | 58.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.29 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.71 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 75.1% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 8.9% |
| Raw p over 1 5 | 77.3% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 40.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.61 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +8.1% |
| Draw probability edge | -3.3% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | 0.1616 |
| Raw ev home | 0.3065 |
| Raw edge prob draw | -0.0669 |
| Raw ev draw | -0.3033 |
| Raw edge prob away | -0.0947 |
| Raw ev away | -0.5196 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **45.5%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-2 at 8.6%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.0%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 70.2%; BTTS No (at least one team does not score): 29.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 32.7% | 3.06 |
| Draw | 21.9% | 4.57 |
| Borussia Dortmund win | 45.5% | 2.20 |

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
| Over 2.5 | 70.6% |
| Under 2.5 | 29.4% |
| Over 3.5 | 50.0% |
| Under 3.5 | 50.0% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.61% |
| 2 | 1-1 | 8.58% |
| 3 | 2-2 | 7.56% |
| 4 | 2-1 | 6.82% |
| 5 | 0-1 | 5.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 32.7% | 29.8% | 3.30 | +7.8% |
| Draw | 21.9% | 23.0% | 4.30 | -5.9% |
| Borussia Dortmund win | 45.5% | 47.1% | 2.14 | -2.7% |
| Over 2.5 | 70.6% | 69.0% | 1.40 | -1.1% |
| Under 2.5 | 29.4% | 31.0% | 3.03 | -11.0% |

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
| Market best home last update utc | 2026-10-11T08:56:55Z |
| Market best draw last update utc | 2026-10-11T08:56:24Z |
| Market best away last update utc | 2026-10-11T08:56:39Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.2% |
| P btts no | 29.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.60 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.41 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.98 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +2.8% |
| Draw probability edge | -1.1% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | 0.0565 |
| Raw ev home | 0.1713 |
| Raw edge prob draw | -0.0226 |
| Raw ev draw | -0.1078 |
| Raw edge prob away | -0.0339 |
| Raw ev away | -0.0636 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **62.9%**. Expected goals are 1.82 for Feyenoord and 3.82 for Como (5.63 combined). The most likely exact score is 2-2 at 6.1%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.9%; Under 3.5 goals: 19.7%; Under 4.5 goals: 35.7%; BTTS Yes (both teams score): 83.2%; BTTS No (at least one team does not score): 16.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 20.0% | 5.01 |
| Draw | 17.1% | 5.83 |
| Como win | 62.9% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 1.82 |
| Como expected goals | 3.82 |
| Expected total goals | 5.63 |
| Over 0.5 | 99.7% |
| Under 0.5 | 0.3% |
| Over 1.5 | 97.3% |
| Under 1.5 | 2.7% |
| Over 2.5 | 90.9% |
| Under 2.5 | 9.1% |
| Over 3.5 | 80.3% |
| Under 3.5 | 19.7% |
| Over 4.5 | 64.3% |
| Under 4.5 | 35.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.08% |
| 2 | 1-3 | 5.15% |
| 3 | 1-4 | 4.91% |
| 4 | 3-3 | 4.68% |
| 5 | 2-3 | 4.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 20.0% | 25.8% | 3.85 | -23.2% |
| Draw | 17.1% | 22.1% | 4.42 | -24.2% |
| Como win | 62.9% | 52.1% | 1.96 | +23.3% |
| Over 2.5 | 90.9% | 68.5% | 1.44 | +30.9% |
| Under 2.5 | 9.1% | 31.5% | 2.84 | -74.2% |

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
| Market best home last update utc | 2026-10-11T08:57:12Z |
| Market best draw last update utc | 2026-10-11T08:57:12Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 83.2% |
| P btts no | 16.8% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 303.17 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 37.09 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 11.01 |
| Fair Over 3.5 odds | 1.24 |
| Fair Under 3.5 odds | 5.09 |
| Fair Over 4.5 odds | 1.56 |
| Fair Under 4.5 odds | 2.80 |
| Unadjusted home-win probability | 14.2% |
| Unadjusted draw probability | 12.2% |
| Unadjusted away-win probability | 73.7% |
| Raw p over 1 5 | 97.5% |
| Raw p under 3 5 | 18.7% |
| Raw p btts yes | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.40 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -5.8% |
| Draw probability edge | -5.0% |
| Away probability edge | +10.8% |
| Over 2.5 probability edge | +22.4% |
| Under 2.5 probability edge | -22.4% |
| Raw edge prob home | -0.1160 |
| Raw ev home | -0.4551 |
| Raw edge prob draw | -0.0996 |
| Raw ev draw | -0.4627 |
| Raw edge prob away | 0.2156 |
| Raw ev away | 0.4443 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **74.4%**. Expected goals are 0.28 for LASK and 1.46 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 28.4%. Goal-market probabilities: at least one goal: 87.3%; Over 2.5 goals: 27.5%; Under 3.5 goals: 89.4%; Under 4.5 goals: 96.5%; BTTS Yes (both teams score): 17.5%; BTTS No (at least one team does not score): 82.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 7.3% | 13.77 |
| Draw | 18.3% | 5.45 |
| Liverpool win | 74.4% | 1.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.46 |
| Expected total goals | 1.74 |
| Over 0.5 | 87.3% |
| Under 0.5 | 12.7% |
| Over 1.5 | 53.7% |
| Under 1.5 | 46.3% |
| Over 2.5 | 27.5% |
| Under 2.5 | 72.5% |
| Over 3.5 | 10.6% |
| Under 3.5 | 89.4% |
| Over 4.5 | 3.5% |
| Under 4.5 | 96.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 28.36% |
| 2 | 0-2 | 20.43% |
| 3 | 0-0 | 12.68% |
| 4 | 0-3 | 9.95% |
| 5 | 1-2 | 5.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 7.3% | 7.2% | 12.00 | -12.8% |
| Draw | 18.3% | 11.9% | 7.11 | +30.4% |
| Liverpool win | 74.4% | 80.8% | 1.29 | -4.0% |
| Over 2.5 | 27.5% | 71.6% | 1.37 | -62.4% |
| Under 2.5 | 72.5% | 28.4% | 3.13 | +127.1% |

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
| Market best home last update utc | 2026-10-11T08:56:55Z |
| Market best draw last update utc | 2026-10-11T08:57:12Z |
| Market best away last update utc | 2026-10-11T08:56:39Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 17.5% |
| P btts no | 82.5% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.89 |
| Fair Over 1.5 odds | 1.86 |
| Fair Under 1.5 odds | 2.16 |
| Fair Over 2.5 odds | 3.64 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.40 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 28.27 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 67.9% |
| Raw p over 1 5 | 51.7% |
| Raw p under 3 5 | 90.0% |
| Raw p btts yes | 18.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 9.50 |
| Reference draw odds | 6.20 |
| Reference away odds | 1.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | +0.0% |
| Draw probability edge | +6.4% |
| Away probability edge | -6.5% |
| Over 2.5 probability edge | -44.2% |
| Under 2.5 probability edge | +44.2% |
| Raw edge prob home | 0.0004 |
| Raw ev home | -0.1257 |
| Raw edge prob draw | 0.1286 |
| Raw ev draw | 0.7612 |
| Raw edge prob away | -0.1290 |
| Raw ev away | -0.1235 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **45.5%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.5%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 69.3%; Under 3.5 goals: 51.8%; Under 4.5 goals: 70.9%; BTTS Yes (both teams score): 67.7%; BTTS No (at least one team does not score): 32.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 33.6% | 2.98 |
| Draw | 20.9% | 4.79 |
| Paris Saint Germain win | 45.5% | 2.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.40 |
| Paris Saint Germain expected goals | 2.23 |
| Expected total goals | 3.63 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 86.8% |
| Under 1.5 | 13.2% |
| Over 2.5 | 69.3% |
| Under 2.5 | 30.7% |
| Over 3.5 | 48.2% |
| Under 3.5 | 51.8% |
| Over 4.5 | 29.1% |
| Under 4.5 | 70.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.50% |
| 2 | 2-1 | 8.11% |
| 3 | 1-2 | 7.41% |
| 4 | 2-2 | 7.00% |
| 5 | 1-0 | 5.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 33.6% | 43.2% | 2.35 | -21.0% |
| Draw | 20.9% | 22.5% | 4.30 | -10.2% |
| Paris Saint Germain win | 45.5% | 34.3% | 2.94 | +33.8% |
| Over 2.5 | 69.3% | 67.0% | 1.44 | -0.2% |
| Under 2.5 | 30.7% | 33.0% | 2.87 | -12.0% |

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
| Market best home last update utc | 2026-10-11T08:56:24Z |
| Market best draw last update utc | 2026-10-11T08:56:55Z |
| Market best away last update utc | 2026-10-11T08:56:39Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.7% |
| P btts no | 32.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.41 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.55 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -9.6% |
| Draw probability edge | -1.6% |
| Away probability edge | +11.2% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | -0.1916 |
| Raw ev home | -0.4354 |
| Raw edge prob draw | -0.0317 |
| Raw ev draw | -0.1701 |
| Raw edge prob away | 0.2234 |
| Raw ev away | 0.6662 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **60.3%**. Expected goals are 3.29 for Real Betis and 1.29 for Porto (4.58 combined). The most likely exact score is 2-2 at 7.0%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 80.9%; Under 3.5 goals: 35.4%; Under 4.5 goals: 55.0%; BTTS Yes (both teams score): 72.3%; BTTS No (at least one team does not score): 27.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 60.3% | 1.66 |
| Draw | 18.9% | 5.28 |
| Porto win | 20.8% | 4.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 3.29 |
| Porto expected goals | 1.29 |
| Expected total goals | 4.58 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 93.1% |
| Under 1.5 | 6.9% |
| Over 2.5 | 80.9% |
| Under 2.5 | 19.1% |
| Over 3.5 | 64.6% |
| Under 3.5 | 35.4% |
| Over 4.5 | 45.0% |
| Under 4.5 | 55.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.04% |
| 2 | 1-1 | 6.30% |
| 3 | 3-1 | 6.22% |
| 4 | 2-1 | 5.67% |
| 5 | 4-1 | 5.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 60.3% | 44.5% | 2.27 | +36.9% |
| Draw | 18.9% | 25.4% | 3.75 | -29.0% |
| Porto win | 20.8% | 30.1% | 3.30 | -31.5% |
| Over 2.5 | 80.9% | 56.3% | 1.78 | +44.0% |
| Under 2.5 | 19.1% | 43.7% | 2.21 | -57.8% |

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
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:56:55Z |
| Market best away last update utc | 2026-10-11T08:57:12Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 72.3% |
| P btts no | 27.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 81.32 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.55 |
| Fair Over 2.5 odds | 1.24 |
| Fair Under 2.5 odds | 5.23 |
| Fair Over 3.5 odds | 1.55 |
| Fair Under 3.5 odds | 2.83 |
| Fair Over 4.5 odds | 2.22 |
| Fair Under 4.5 odds | 1.82 |
| Unadjusted home-win probability | 76.1% |
| Unadjusted draw probability | 12.4% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 94.1% |
| Raw p under 3 5 | 32.9% |
| Raw p btts yes | 69.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +15.8% |
| Draw probability edge | -6.5% |
| Away probability edge | -9.3% |
| Over 2.5 probability edge | +24.6% |
| Under 2.5 probability edge | -24.6% |
| Raw edge prob home | 0.3168 |
| Raw ev home | 0.7283 |
| Raw edge prob draw | -0.1301 |
| Raw ev draw | -0.5339 |
| Raw edge prob away | -0.1867 |
| Raw ev away | -0.6227 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.5%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 51.1%; Under 3.5 goals: 70.6%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.5% | 2.53 |
| Draw | 25.6% | 3.91 |
| AEK Athens win | 34.9% | 2.86 |

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
| Shakhtar Donetsk win | 39.5% | 35.7% | 2.81 | +11.0% |
| Draw | 25.6% | 26.9% | 3.65 | -6.7% |
| AEK Athens win | 34.9% | 37.3% | 2.70 | -5.6% |
| Over 2.5 | 51.1% | 52.2% | 1.92 | -1.8% |
| Under 2.5 | 48.9% | 47.8% | 2.03 | -0.8% |

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
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:57:12Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Pinnacle |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.55 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.45 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | +3.8% |
| Draw probability edge | -1.4% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | 0.0751 |
| Raw ev home | 0.2153 |
| Raw edge prob draw | -0.0272 |
| Raw ev draw | -0.1168 |
| Raw edge prob away | -0.0479 |
| Raw ev away | -0.1210 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.0%**. Expected goals are 1.45 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 72.6%; Under 3.5 goals: 48.5%; Under 4.5 goals: 67.7%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.2% | 5.80 |
| Draw | 16.7% | 5.97 |
| VfB Stuttgart win | 66.0% | 1.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.45 |
| VfB Stuttgart expected goals | 2.25 |
| Expected total goals | 3.71 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 72.6% |
| Under 2.5 | 27.4% |
| Over 3.5 | 51.5% |
| Under 3.5 | 48.5% |
| Over 4.5 | 32.3% |
| Under 4.5 | 67.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.69% |
| 2 | 1-3 | 8.02% |
| 3 | 0-2 | 7.35% |
| 4 | 0-1 | 7.01% |
| 5 | 1-1 | 6.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.2% | 9.7% | 10.00 | +72.4% |
| Draw | 16.7% | 14.2% | 6.48 | +8.5% |
| VfB Stuttgart win | 66.0% | 76.1% | 1.35 | -10.9% |
| Over 2.5 | 72.6% | 70.8% | 1.37 | -0.5% |
| Under 2.5 | 27.4% | 29.2% | 3.13 | -14.3% |

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
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:56:39Z |
| Market best away last update utc | 2026-10-11T08:56:56Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.2% |
| P btts no | 32.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.89 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.65 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.65 |
| Fair Over 3.5 odds | 1.94 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.09 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 24.8% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 56.0% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 68.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 7.70 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.27 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +7.5% |
| Draw probability edge | +2.5% |
| Away probability edge | -10.1% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | 0.1510 |
| Raw ev home | 1.4784 |
| Raw edge prob draw | 0.0502 |
| Raw ev draw | 0.2474 |
| Raw edge prob away | -0.2012 |
| Raw ev away | -0.2445 |

</details>


---
