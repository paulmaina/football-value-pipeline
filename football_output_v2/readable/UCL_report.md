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
| Optimizer objective | 1560.624 |
| Base scoring parameter | 0.154 |
| Home-advantage parameter | 0.271 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0 |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 20.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'INSUFFICIENT_HISTORY', 'away': 'INSUFFICIENT_HISTORY', 'over_1_5': 'INSUFFICIENT_HISTORY', 'under_3_5': 'INSUFFICIENT_HISTORY', 'btts_yes': 'INSUFFICIENT_HISTORY'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-13 — Arsenal vs Lille

The model's most likely 1X2 outcome is **Arsenal win** at **73.5%**. Expected goals are 2.01 for Arsenal and 0.77 for Lille (2.78 combined). The most likely exact score is 1-0 at 14.2%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 54.4%; Under 3.5 goals: 68.6%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 44.9%; BTTS No (at least one team does not score): 55.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 73.5% | 1.36 |
| Draw | 15.9% | 6.30 |
| Lille win | 10.6% | 9.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 2.01 |
| Lille expected goals | 0.77 |
| Expected total goals | 2.78 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 54.4% |
| Under 2.5 | 45.6% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.20% |
| 2 | 2-0 | 13.76% |
| 3 | 2-1 | 10.61% |
| 4 | 3-0 | 9.23% |
| 5 | 1-1 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 73.5% | 80.2% | 1.29 | -5.2% |
| Draw | 15.9% | 12.5% | 7.40 | +17.5% |
| Lille win | 10.6% | 7.3% | 14.50 | +53.7% |
| Over 2.5 | 54.4% | 61.3% | 1.67 | -9.1% |
| Under 2.5 | 45.6% | 38.7% | 2.50 | +14.0% |

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
| P btts yes | 44.9% |
| P btts no | 55.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.27 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.36 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.35 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 19.2% |
| Unadjusted away-win probability | 13.9% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.21 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -6.6% |
| Draw probability edge | +3.4% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | -0.1327 |
| Raw ev home | -0.1372 |
| Raw edge prob draw | 0.0674 |
| Raw ev draw | 0.4244 |
| Raw edge prob away | 0.0653 |
| Raw ev away | 1.0110 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **63.4%**. Expected goals are 3.87 for Atlético Madrid and 1.70 for Manchester United (5.57 combined). The most likely exact score is 2-2 at 6.3%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 90.2%; Under 3.5 goals: 20.7%; Under 4.5 goals: 37.2%; BTTS Yes (both teams score): 81.8%; BTTS No (at least one team does not score): 18.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 63.4% | 1.58 |
| Draw | 17.3% | 5.78 |
| Manchester United win | 19.3% | 5.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 3.87 |
| Manchester United expected goals | 1.70 |
| Expected total goals | 5.57 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.1% |
| Under 1.5 | 2.9% |
| Over 2.5 | 90.2% |
| Under 2.5 | 9.8% |
| Over 3.5 | 79.3% |
| Under 3.5 | 20.7% |
| Over 4.5 | 62.8% |
| Under 4.5 | 37.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.25% |
| 2 | 3-1 | 5.22% |
| 3 | 4-1 | 5.05% |
| 4 | 3-3 | 4.58% |
| 5 | 3-2 | 4.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 63.4% | 50.7% | 2.07 | +31.3% |
| Draw | 17.3% | 23.2% | 4.10 | -29.0% |
| Manchester United win | 19.3% | 26.2% | 3.75 | -27.7% |
| Over 2.5 | 90.2% | 63.8% | 1.50 | +35.3% |
| Under 2.5 | 9.8% | 36.2% | 2.66 | -74.0% |

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
| P btts yes | 81.8% |
| P btts no | 18.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 258.72 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 34.17 |
| Fair Over 2.5 odds | 1.11 |
| Fair Under 2.5 odds | 10.23 |
| Fair Over 3.5 odds | 1.26 |
| Fair Under 3.5 odds | 4.83 |
| Fair Over 4.5 odds | 1.59 |
| Fair Under 4.5 odds | 2.69 |
| Unadjusted home-win probability | 76.2% |
| Unadjusted draw probability | 11.5% |
| Unadjusted away-win probability | 12.4% |
| Raw p over 1 5 | 97.4% |
| Raw p under 3 5 | 19.4% |
| Raw p btts yes | 80.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.86 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | +12.7% |
| Draw probability edge | -5.9% |
| Away probability edge | -6.9% |
| Over 2.5 probability edge | +26.4% |
| Under 2.5 probability edge | -26.4% |
| Raw edge prob home | 0.2548 |
| Raw ev home | 0.5763 |
| Raw edge prob draw | -0.1171 |
| Raw ev draw | -0.5302 |
| Raw edge prob away | -0.1378 |
| Raw ev away | -0.5354 |
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

The model's most likely 1X2 outcome is **Barcelona win** at **68.2%**. Expected goals are 1.61 for Galatasaray and 2.47 for Barcelona (4.09 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 98.9%; Over 2.5 goals: 78.7%; Under 3.5 goals: 40.8%; Under 4.5 goals: 59.9%; BTTS Yes (both teams score): 71.8%; BTTS No (at least one team does not score): 28.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 17.0% | 5.87 |
| Draw | 14.8% | 6.75 |
| Barcelona win | 68.2% | 1.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.61 |
| Barcelona expected goals | 2.47 |
| Expected total goals | 4.09 |
| Over 0.5 | 98.9% |
| Under 0.5 | 1.1% |
| Over 1.5 | 91.5% |
| Under 1.5 | 8.5% |
| Over 2.5 | 78.7% |
| Under 2.5 | 21.3% |
| Over 3.5 | 59.2% |
| Under 3.5 | 40.8% |
| Over 4.5 | 40.1% |
| Under 4.5 | 59.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.92% |
| 2 | 1-3 | 8.18% |
| 3 | 2-3 | 6.60% |
| 4 | 0-2 | 6.14% |
| 5 | 2-2 | 5.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 17.0% | 9.2% | 10.00 | +70.4% |
| Draw | 14.8% | 11.4% | 7.40 | +9.6% |
| Barcelona win | 68.2% | 79.4% | 1.34 | -8.7% |
| Over 2.5 | 78.7% | 81.3% | 1.21 | -4.8% |
| Under 2.5 | 21.3% | 18.7% | 4.50 | -4.0% |

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
| P btts yes | 71.8% |
| P btts no | 28.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 91.81 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.71 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.69 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.45 |
| Fair Over 4.5 odds | 2.49 |
| Fair Under 4.5 odds | 1.67 |
| Unadjusted home-win probability | 24.9% |
| Unadjusted draw probability | 18.2% |
| Unadjusted away-win probability | 56.9% |
| Raw p over 1 5 | 91.1% |
| Raw p under 3 5 | 41.6% |
| Raw p btts yes | 73.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 7.80 |
| Reference draw odds | 6.50 |
| Reference away odds | 1.22 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.40 |
| Home probability edge | +7.8% |
| Draw probability edge | +3.4% |
| Away probability edge | -11.2% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | 0.1564 |
| Raw ev home | 1.4854 |
| Raw edge prob draw | 0.0684 |
| Raw ev draw | 0.3490 |
| Raw edge prob away | -0.2248 |
| Raw ev away | -0.2373 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **70.3%**. Expected goals are 1.98 for Inter Milan and 1.01 for Club Brugge (2.99 combined). The most likely exact score is 1-0 at 12.2%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 59.3%; Under 3.5 goals: 64.0%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 52.7%; BTTS No (at least one team does not score): 47.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.3% | 1.42 |
| Draw | 16.4% | 6.09 |
| Club Brugge win | 13.2% | 7.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.98 |
| Club Brugge expected goals | 1.01 |
| Expected total goals | 2.99 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 80.3% |
| Under 1.5 | 19.7% |
| Over 2.5 | 59.3% |
| Under 2.5 | 40.7% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.21% |
| 2 | 2-1 | 11.57% |
| 3 | 2-0 | 11.51% |
| 4 | 1-1 | 7.71% |
| 5 | 3-1 | 7.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.3% | 80.2% | 1.31 | -7.8% |
| Draw | 16.4% | 12.5% | 6.60 | +8.5% |
| Club Brugge win | 13.2% | 7.3% | 12.00 | +58.7% |
| Over 2.5 | 59.3% | 67.0% | 1.44 | -14.6% |
| Under 2.5 | 40.7% | 33.0% | 2.83 | +15.3% |

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
| P btts yes | 52.7% |
| P btts no | 47.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.24 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.07 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.19 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 65.0% |
| Raw p btts yes | 54.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.21 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -9.8% |
| Draw probability edge | +3.9% |
| Away probability edge | +5.9% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | -0.1962 |
| Raw ev home | -0.2070 |
| Raw edge prob draw | 0.0785 |
| Raw ev draw | 0.3438 |
| Raw edge prob away | 0.1177 |
| Raw ev away | 1.2926 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **44.9%**. Expected goals are 1.58 for RB Leipzig and 1.78 for PSV Eindhoven (3.36 combined). The most likely exact score is 2-1 at 9.9%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 65.2%; Under 3.5 goals: 57.0%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 65.5%; BTTS No (at least one team does not score): 34.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 44.9% | 2.23 |
| Draw | 21.3% | 4.69 |
| PSV Eindhoven win | 33.8% | 2.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.58 |
| PSV Eindhoven expected goals | 1.78 |
| Expected total goals | 3.36 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 84.2% |
| Under 1.5 | 15.8% |
| Over 2.5 | 65.2% |
| Under 2.5 | 34.8% |
| Over 3.5 | 43.0% |
| Under 3.5 | 57.0% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.91% |
| 2 | 1-1 | 9.12% |
| 3 | 1-0 | 7.68% |
| 4 | 1-2 | 6.78% |
| 5 | 2-2 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 44.9% | 54.8% | 1.90 | -14.8% |
| Draw | 21.3% | 21.0% | 4.80 | +2.4% |
| PSV Eindhoven win | 33.8% | 24.2% | 3.95 | +33.5% |
| Over 2.5 | 65.2% | 71.6% | 1.35 | -12.0% |
| Under 2.5 | 34.8% | 28.4% | 3.26 | +13.4% |

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
| P btts yes | 65.5% |
| P btts no | 34.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.06 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.32 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.87 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.04 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 34.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 43.4% |
| Raw p over 1 5 | 84.4% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.72 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -10.0% |
| Draw probability edge | +0.4% |
| Away probability edge | +9.6% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | -0.1996 |
| Raw ev home | -0.3372 |
| Raw edge prob draw | 0.0075 |
| Raw ev draw | 0.0417 |
| Raw edge prob away | 0.1921 |
| Raw ev away | 0.7149 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **42.0%**. Expected goals are 1.25 for RC Lens and 1.66 for Sporting Lisbon (2.91 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 55.2%; Under 3.5 goals: 67.0%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 33.9% | 2.95 |
| Draw | 24.1% | 4.14 |
| Sporting Lisbon win | 42.0% | 2.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.25 |
| Sporting Lisbon expected goals | 1.66 |
| Expected total goals | 2.91 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 77.9% |
| Under 1.5 | 22.1% |
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 33.0% |
| Under 3.5 | 67.0% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.25% |
| 2 | 0-1 | 8.48% |
| 3 | 1-0 | 8.47% |
| 4 | 1-2 | 8.29% |
| 5 | 2-1 | 8.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 33.9% | 38.2% | 2.62 | -11.3% |
| Draw | 24.1% | 25.2% | 3.91 | -5.6% |
| Sporting Lisbon win | 42.0% | 36.5% | 2.78 | +16.8% |
| Over 2.5 | 55.2% | 59.8% | 1.64 | -9.5% |
| Under 2.5 | 44.8% | 40.2% | 2.46 | +10.3% |

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
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.57 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.53 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.03 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.97 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 47.5% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 66.7% |
| Raw p btts yes | 57.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.40 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -4.4% |
| Draw probability edge | -1.1% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.0872 |
| Raw ev home | -0.2273 |
| Raw edge prob draw | -0.0221 |
| Raw ev draw | -0.0995 |
| Raw edge prob away | 0.1094 |
| Raw ev away | 0.3199 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **54.1%**. Expected goals are 0.37 for Sabah FK and 1.26 for Slavia Praha (1.63 combined). The most likely exact score is 0-1 at 22.8%. Goal-market probabilities: at least one goal: 82.4%; Over 2.5 goals: 22.2%; Under 3.5 goals: 92.1%; Under 4.5 goals: 97.6%; BTTS Yes (both teams score): 21.6%; BTTS No (at least one team does not score): 78.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 19.2% | 5.22 |
| Draw | 26.7% | 3.74 |
| Slavia Praha win | 54.1% | 1.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.37 |
| Slavia Praha expected goals | 1.26 |
| Expected total goals | 1.63 |
| Over 0.5 | 82.4% |
| Under 0.5 | 17.6% |
| Over 1.5 | 46.6% |
| Under 1.5 | 53.4% |
| Over 2.5 | 22.2% |
| Under 2.5 | 77.8% |
| Over 3.5 | 7.9% |
| Under 3.5 | 92.1% |
| Over 4.5 | 2.4% |
| Under 4.5 | 97.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.80% |
| 2 | 0-0 | 17.61% |
| 3 | 0-2 | 14.05% |
| 4 | 1-0 | 13.02% |
| 5 | 1-1 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 19.2% | 26.9% | 3.74 | -28.3% |
| Draw | 26.7% | 24.4% | 4.00 | +6.9% |
| Slavia Praha win | 54.1% | 48.8% | 2.12 | +14.7% |
| Over 2.5 | 22.2% | 57.8% | 1.71 | -62.1% |
| Under 2.5 | 77.8% | 42.2% | 2.32 | +80.6% |

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
| P btts yes | 21.6% |
| P btts no | 78.4% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.68 |
| Fair Over 1.5 odds | 2.15 |
| Fair Under 1.5 odds | 1.87 |
| Fair Over 2.5 odds | 4.51 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 12.71 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 40.94 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.5% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 59.5% |
| Raw p over 1 5 | 48.0% |
| Raw p under 3 5 | 91.7% |
| Raw p btts yes | 21.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.60 |
| Reference away odds | 1.92 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | -7.7% |
| Draw probability edge | +2.3% |
| Away probability edge | +5.4% |
| Over 2.5 probability edge | -35.6% |
| Under 2.5 probability edge | +35.6% |
| Raw edge prob home | -0.1537 |
| Raw ev home | -0.5708 |
| Raw edge prob draw | 0.0463 |
| Raw ev draw | 0.1611 |
| Raw edge prob away | 0.1074 |
| Raw ev away | 0.2613 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **92.8%**. Expected goals are 0.69 for Viking FK and 4.47 for Bayern Munich (5.16 combined). The most likely exact score is 0-4 at 9.5%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.3%; Under 3.5 goals: 24.9%; Under 4.5 goals: 42.1%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 2.5% | 40.59 |
| Draw | 4.8% | 20.97 |
| Bayern Munich win | 92.8% | 1.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.69 |
| Bayern Munich expected goals | 4.47 |
| Expected total goals | 5.16 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 88.3% |
| Under 2.5 | 11.7% |
| Over 3.5 | 75.1% |
| Under 3.5 | 24.9% |
| Over 4.5 | 57.9% |
| Under 4.5 | 42.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.50% |
| 2 | 0-3 | 8.51% |
| 3 | 0-5 | 8.49% |
| 4 | 1-4 | 6.55% |
| 5 | 0-6 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 2.5% | 3.0% | 27.00 | -33.5% |
| Draw | 4.8% | 5.4% | 15.50 | -26.1% |
| Bayern Munich win | 92.8% | 91.6% | 1.11 | +3.0% |
| Over 2.5 | 88.3% | 85.4% | 1.15 | +1.6% |
| Under 2.5 | 11.7% | 14.6% | 5.90 | -31.1% |

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
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 176.72 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.09 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.56 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.01 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.38 |
| Unadjusted home-win probability | 1.9% |
| Unadjusted draw probability | 4.1% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.3% |
| Raw p under 3 5 | 24.5% |
| Raw p btts yes | 49.1% |
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
| Away probability edge | +1.2% |
| Over 2.5 probability edge | +2.9% |
| Under 2.5 probability edge | -2.9% |
| Raw edge prob home | -0.0105 |
| Raw ev home | -0.4769 |
| Raw edge prob draw | -0.0127 |
| Raw ev draw | -0.3593 |
| Raw edge prob away | 0.0232 |
| Raw ev away | 0.0426 |
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

The model's most likely 1X2 outcome is **Napoli win** at **40.6%**. Expected goals are 0.87 for Villarreal and 1.43 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.4%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 40.0%; Under 3.5 goals: 80.5%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 33.9% | 2.95 |
| Draw | 25.5% | 3.93 |
| Napoli win | 40.6% | 2.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.87 |
| Napoli expected goals | 1.43 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 40.0% |
| Under 2.5 | 60.0% |
| Over 3.5 | 19.5% |
| Under 3.5 | 80.5% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.42% |
| 2 | 0-1 | 11.92% |
| 3 | 1-1 | 11.75% |
| 4 | 0-0 | 9.26% |
| 5 | 0-2 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 33.9% | 44.3% | 2.33 | -20.9% |
| Draw | 25.5% | 25.3% | 3.90 | -0.7% |
| Napoli win | 40.6% | 30.5% | 3.30 | +34.0% |
| Over 2.5 | 40.0% | 58.9% | 1.71 | -31.6% |
| Under 2.5 | 60.0% | 41.1% | 2.44 | +46.4% |

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
| P btts yes | 43.9% |
| P btts no | 56.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.80 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.13 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.21 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 23.6% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 50.7% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 79.8% |
| Raw p btts yes | 43.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.95 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -10.3% |
| Draw probability edge | +0.2% |
| Away probability edge | +10.1% |
| Over 2.5 probability edge | -18.9% |
| Under 2.5 probability edge | +18.9% |
| Raw edge prob home | -0.2067 |
| Raw ev home | -0.4502 |
| Raw edge prob draw | 0.0042 |
| Raw ev draw | 0.0015 |
| Raw edge prob away | 0.2025 |
| Raw ev away | 0.6738 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **51.8%**. Expected goals are 1.26 for AS Roma and 1.83 for Real Madrid (3.09 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 59.6%; Under 3.5 goals: 62.6%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 25.9% | 3.86 |
| Draw | 22.3% | 4.48 |
| Real Madrid win | 51.8% | 1.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.26 |
| Real Madrid expected goals | 1.83 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 59.6% |
| Under 2.5 | 40.4% |
| Over 3.5 | 37.4% |
| Under 3.5 | 62.6% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.18% |
| 2 | 1-2 | 9.68% |
| 3 | 0-1 | 8.90% |
| 4 | 0-2 | 7.67% |
| 5 | 2-1 | 6.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 25.9% | 25.0% | 4.20 | +8.9% |
| Draw | 22.3% | 22.8% | 4.30 | -4.0% |
| Real Madrid win | 51.8% | 52.2% | 1.95 | +0.9% |
| Over 2.5 | 59.6% | 68.9% | 1.42 | -15.3% |
| Under 2.5 | 40.4% | 31.1% | 2.90 | +17.0% |

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
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.39 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.26 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.48 |
| Fair Over 3.5 odds | 2.67 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.99 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 51.3% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 62.6% |
| Raw p btts yes | 59.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Home probability edge | +0.9% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | 0.0185 |
| Raw ev home | 0.1276 |
| Raw edge prob draw | -0.0101 |
| Raw ev draw | -0.0620 |
| Raw edge prob away | -0.0084 |
| Raw ev away | 0.0011 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **66.9%**. Expected goals are 2.22 for Aston Villa and 0.60 for Fenerbahce (2.83 combined). The most likely exact score is 2-0 at 13.1%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 51.4%; Under 3.5 goals: 70.2%; Under 4.5 goals: 85.4%; BTTS Yes (both teams score): 41.3%; BTTS No (at least one team does not score): 58.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 66.9% | 1.49 |
| Draw | 19.4% | 5.14 |
| Fenerbahce win | 13.7% | 7.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.22 |
| Fenerbahce expected goals | 0.60 |
| Expected total goals | 2.83 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 51.4% |
| Under 2.5 | 48.6% |
| Over 3.5 | 29.8% |
| Under 3.5 | 70.2% |
| Over 4.5 | 14.6% |
| Under 4.5 | 85.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.08% |
| 2 | 1-0 | 12.12% |
| 3 | 3-0 | 9.69% |
| 4 | 1-1 | 9.07% |
| 5 | 2-1 | 7.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 66.9% | 58.9% | 1.74 | +16.4% |
| Draw | 19.4% | 22.7% | 4.35 | -15.4% |
| Fenerbahce win | 13.7% | 18.4% | 5.40 | -26.2% |
| Over 2.5 | 51.4% | 56.9% | 1.74 | -10.6% |
| Under 2.5 | 48.6% | 43.1% | 2.32 | +12.8% |

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
| P btts yes | 41.3% |
| P btts no | 58.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.05 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.35 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.85 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.2% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 76.9% |
| Raw p under 3 5 | 68.6% |
| Raw p btts yes | 40.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.61 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +8.0% |
| Draw probability edge | -3.3% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | 0.1594 |
| Raw ev home | 0.3028 |
| Raw edge prob draw | -0.0654 |
| Raw ev draw | -0.2967 |
| Raw edge prob away | -0.0941 |
| Raw ev away | -0.5162 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **47.1%**. Expected goals are 1.67 for Bodø/Glimt and 2.04 for Borussia Dortmund (3.70 combined). The most likely exact score is 1-2 at 8.5%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 71.2%; Under 3.5 goals: 49.3%; Under 4.5 goals: 68.9%; BTTS Yes (both teams score): 70.4%; BTTS No (at least one team does not score): 29.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 31.2% | 3.21 |
| Draw | 21.7% | 4.60 |
| Borussia Dortmund win | 47.1% | 2.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 1.67 |
| Borussia Dortmund expected goals | 2.04 |
| Expected total goals | 3.70 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 88.0% |
| Under 1.5 | 12.0% |
| Over 2.5 | 71.2% |
| Under 2.5 | 28.8% |
| Over 3.5 | 50.7% |
| Under 3.5 | 49.3% |
| Over 4.5 | 31.1% |
| Under 4.5 | 68.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.52% |
| 2 | 1-1 | 8.45% |
| 3 | 2-2 | 7.55% |
| 4 | 2-1 | 6.69% |
| 5 | 1-3 | 5.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 31.2% | 29.8% | 3.30 | +2.9% |
| Draw | 21.7% | 23.0% | 4.30 | -6.6% |
| Borussia Dortmund win | 47.1% | 47.1% | 2.14 | +0.8% |
| Over 2.5 | 71.2% | 69.0% | 1.40 | -0.3% |
| Under 2.5 | 28.8% | 31.0% | 3.03 | -12.7% |

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
| P btts yes | 70.4% |
| P btts no | 29.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.99 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.37 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.47 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.21 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 32.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 47.1% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 70.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.98 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +1.3% |
| Draw probability edge | -1.3% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | +2.2% |
| Under 2.5 probability edge | -2.2% |
| Raw edge prob home | 0.0265 |
| Raw ev home | 0.0723 |
| Raw edge prob draw | -0.0258 |
| Raw ev draw | -0.1217 |
| Raw edge prob away | -0.0007 |
| Raw ev away | 0.0075 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **63.4%**. Expected goals are 1.84 for Feyenoord and 3.93 for Como (5.77 combined). The most likely exact score is 2-2 at 5.9%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 91.6%; Under 3.5 goals: 18.3%; Under 4.5 goals: 33.9%; BTTS Yes (both teams score): 83.8%; BTTS No (at least one team does not score): 16.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 19.6% | 5.09 |
| Draw | 16.9% | 5.91 |
| Como win | 63.4% | 1.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 1.84 |
| Como expected goals | 3.93 |
| Expected total goals | 5.77 |
| Over 0.5 | 99.7% |
| Under 0.5 | 0.3% |
| Over 1.5 | 97.6% |
| Under 1.5 | 2.4% |
| Over 2.5 | 91.6% |
| Under 2.5 | 8.4% |
| Over 3.5 | 81.7% |
| Under 3.5 | 18.3% |
| Over 4.5 | 66.1% |
| Under 4.5 | 33.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 5.90% |
| 2 | 1-3 | 4.94% |
| 3 | 1-4 | 4.86% |
| 4 | 3-3 | 4.73% |
| 5 | 2-3 | 4.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 19.6% | 25.8% | 3.85 | -24.4% |
| Draw | 16.9% | 22.1% | 4.42 | -25.2% |
| Como win | 63.4% | 52.1% | 1.96 | +24.3% |
| Over 2.5 | 91.6% | 68.5% | 1.44 | +32.0% |
| Under 2.5 | 8.4% | 31.5% | 2.84 | -76.3% |

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
| P btts yes | 83.8% |
| P btts no | 16.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 346.43 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 41.17 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 11.97 |
| Fair Over 3.5 odds | 1.22 |
| Fair Under 3.5 odds | 5.46 |
| Fair Over 4.5 odds | 1.51 |
| Fair Under 4.5 odds | 2.95 |
| Unadjusted home-win probability | 13.5% |
| Unadjusted draw probability | 11.7% |
| Unadjusted away-win probability | 74.8% |
| Raw p over 1 5 | 97.8% |
| Raw p under 3 5 | 17.3% |
| Raw p btts yes | 82.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.40 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -6.1% |
| Draw probability edge | -5.2% |
| Away probability edge | +11.3% |
| Over 2.5 probability edge | +23.1% |
| Under 2.5 probability edge | -23.1% |
| Raw edge prob home | -0.1224 |
| Raw ev home | -0.4795 |
| Raw edge prob draw | -0.1040 |
| Raw ev draw | -0.4818 |
| Raw edge prob away | 0.2263 |
| Raw ev away | 0.4652 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:56:24Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 54.5% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T08:56:10Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.11 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 68.9% |
| Market btts yes odds | 1.47 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:57:12Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.88 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **73.9%**. Expected goals are 0.33 for LASK and 1.48 for Liverpool (1.80 combined). The most likely exact score is 0-1 at 27.3%. Goal-market probabilities: at least one goal: 88.1%; Over 2.5 goals: 29.2%; Under 3.5 goals: 88.4%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 19.9%; BTTS No (at least one team does not score): 80.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 7.8% | 12.85 |
| Draw | 18.3% | 5.47 |
| Liverpool win | 73.9% | 1.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.33 |
| Liverpool expected goals | 1.48 |
| Expected total goals | 1.80 |
| Over 0.5 | 88.1% |
| Under 0.5 | 11.9% |
| Over 1.5 | 55.4% |
| Under 1.5 | 44.6% |
| Over 2.5 | 29.2% |
| Under 2.5 | 70.8% |
| Over 3.5 | 11.6% |
| Under 3.5 | 88.4% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 27.27% |
| 2 | 0-2 | 19.82% |
| 3 | 0-0 | 11.92% |
| 4 | 0-3 | 9.76% |
| 5 | 1-2 | 6.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 7.8% | 7.2% | 12.00 | -6.6% |
| Draw | 18.3% | 11.9% | 7.11 | +29.9% |
| Liverpool win | 73.9% | 80.8% | 1.29 | -4.6% |
| Over 2.5 | 29.2% | 71.6% | 1.37 | -60.0% |
| Under 2.5 | 70.8% | 28.4% | 3.13 | +121.7% |

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
| P btts yes | 19.9% |
| P btts no | 80.1% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.39 |
| Fair Over 1.5 odds | 1.80 |
| Fair Under 1.5 odds | 2.24 |
| Fair Over 2.5 odds | 3.43 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.59 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.97 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 8.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 67.0% |
| Raw p over 1 5 | 53.4% |
| Raw p under 3 5 | 89.1% |
| Raw p btts yes | 21.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 9.50 |
| Reference draw odds | 6.20 |
| Reference away odds | 1.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | +0.5% |
| Draw probability edge | +6.4% |
| Away probability edge | -6.9% |
| Over 2.5 probability edge | -42.4% |
| Under 2.5 probability edge | +42.4% |
| Raw edge prob home | 0.0109 |
| Raw ev home | -0.0006 |
| Raw edge prob draw | 0.1272 |
| Raw ev draw | 0.7512 |
| Raw edge prob away | -0.1380 |
| Raw ev away | -0.1352 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **46.8%**. Expected goals are 1.53 for Manchester City and 2.51 for Paris Saint Germain (4.04 combined). The most likely exact score is 2-1 at 7.5%. Goal-market probabilities: at least one goal: 98.4%; Over 2.5 goals: 75.6%; Under 3.5 goals: 43.7%; Under 4.5 goals: 63.3%; BTTS Yes (both teams score): 72.7%; BTTS No (at least one team does not score): 27.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 33.0% | 3.03 |
| Draw | 20.2% | 4.95 |
| Paris Saint Germain win | 46.8% | 2.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.53 |
| Paris Saint Germain expected goals | 2.51 |
| Expected total goals | 4.04 |
| Over 0.5 | 98.4% |
| Under 0.5 | 1.6% |
| Over 1.5 | 90.3% |
| Under 1.5 | 9.7% |
| Over 2.5 | 75.6% |
| Under 2.5 | 24.4% |
| Over 3.5 | 56.3% |
| Under 3.5 | 43.7% |
| Over 4.5 | 36.7% |
| Under 4.5 | 63.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 7.48% |
| 2 | 2-2 | 7.33% |
| 3 | 1-1 | 7.25% |
| 4 | 1-2 | 6.70% |
| 5 | 1-3 | 5.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 33.0% | 43.2% | 2.35 | -22.3% |
| Draw | 20.2% | 22.5% | 4.30 | -13.2% |
| Paris Saint Germain win | 46.8% | 34.3% | 2.94 | +37.5% |
| Over 2.5 | 75.6% | 67.0% | 1.44 | +8.9% |
| Under 2.5 | 24.4% | 33.0% | 2.87 | -30.1% |

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
| P btts yes | 72.7% |
| P btts no | 27.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 62.27 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.26 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.11 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.29 |
| Fair Over 4.5 odds | 2.73 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.6% |
| Raw p btts yes | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -10.1% |
| Draw probability edge | -2.3% |
| Away probability edge | +12.4% |
| Over 2.5 probability edge | +8.6% |
| Under 2.5 probability edge | -8.6% |
| Raw edge prob home | -0.2028 |
| Raw ev home | -0.4618 |
| Raw edge prob draw | -0.0457 |
| Raw ev draw | -0.2301 |
| Raw edge prob away | 0.2485 |
| Raw ev away | 0.7402 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **65.0%**. Expected goals are 4.51 for Real Betis and 1.48 for Porto (5.98 combined). The most likely exact score is 2-2 at 6.0%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 91.3%; Under 3.5 goals: 18.4%; Under 4.5 goals: 33.8%; BTTS Yes (both teams score): 79.8%; BTTS No (at least one team does not score): 20.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 65.0% | 1.54 |
| Draw | 16.6% | 6.02 |
| Porto win | 18.4% | 5.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 4.51 |
| Porto expected goals | 1.48 |
| Expected total goals | 5.98 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.4% |
| Under 1.5 | 2.6% |
| Over 2.5 | 91.3% |
| Under 2.5 | 8.7% |
| Over 3.5 | 81.6% |
| Under 3.5 | 18.4% |
| Over 4.5 | 66.2% |
| Under 4.5 | 33.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 5.99% |
| 2 | 4-1 | 4.90% |
| 3 | 3-3 | 4.42% |
| 4 | 5-1 | 4.41% |
| 5 | 3-1 | 4.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 65.0% | 44.5% | 2.27 | +47.5% |
| Draw | 16.6% | 25.4% | 3.75 | -37.7% |
| Porto win | 18.4% | 30.1% | 3.30 | -39.3% |
| Over 2.5 | 91.3% | 56.3% | 1.78 | +62.5% |
| Under 2.5 | 8.7% | 43.7% | 2.21 | -80.8% |

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
| P btts yes | 79.8% |
| P btts no | 20.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 276.47 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 39.03 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 11.49 |
| Fair Over 3.5 odds | 1.22 |
| Fair Under 3.5 odds | 5.45 |
| Fair Over 4.5 odds | 1.51 |
| Fair Under 4.5 odds | 2.96 |
| Unadjusted home-win probability | 85.5% |
| Unadjusted draw probability | 7.8% |
| Unadjusted away-win probability | 6.7% |
| Raw p over 1 5 | 98.1% |
| Raw p under 3 5 | 15.4% |
| Raw p btts yes | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +20.5% |
| Draw probability edge | -8.8% |
| Away probability edge | -11.7% |
| Over 2.5 probability edge | +35.0% |
| Under 2.5 probability edge | -35.0% |
| Raw edge prob home | 0.4107 |
| Raw ev home | 0.9415 |
| Raw edge prob draw | -0.1764 |
| Raw ev draw | -0.7076 |
| Raw edge prob away | -0.2343 |
| Raw ev away | -0.7797 |
| Market p over 1 5 | 81.2% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:56:24Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 66.7% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:57:12Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.79 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 59.6% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-11T08:57:13Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.35 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.0%**. Expected goals are 1.45 for Shakhtar Donetsk and 1.25 for AEK Athens (2.71 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.3%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.0% | 2.56 |
| Draw | 25.7% | 3.90 |
| AEK Athens win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.45 |
| AEK Athens expected goals | 1.25 |
| Expected total goals | 2.71 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.7% |
| Under 3.5 | 71.3% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.14% |
| 2 | 0-1 | 9.53% |
| 3 | 1-0 | 9.49% |
| 4 | 2-1 | 8.14% |
| 5 | 1-2 | 8.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.0% | 35.7% | 2.81 | +9.7% |
| Draw | 25.7% | 26.9% | 3.65 | -6.3% |
| AEK Athens win | 35.3% | 37.3% | 2.70 | -4.7% |
| Over 2.5 | 50.4% | 52.2% | 1.92 | -3.2% |
| Under 2.5 | 49.6% | 47.8% | 2.03 | +0.7% |

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
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.69 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.33 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 42.4% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 54.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.55 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.45 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | +3.3% |
| Draw probability edge | -1.3% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | 0.0662 |
| Raw ev home | 0.1903 |
| Raw edge prob draw | -0.0251 |
| Raw ev draw | -0.1089 |
| Raw edge prob away | -0.0412 |
| Raw ev away | -0.1029 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.1%**. Expected goals are 1.40 for ŠK Slovan Bratislava and 2.20 for VfB Stuttgart (3.60 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 70.8%; Under 3.5 goals: 50.8%; Under 4.5 goals: 69.8%; BTTS Yes (both teams score): 65.5%; BTTS No (at least one team does not score): 34.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.0% | 5.87 |
| Draw | 16.9% | 5.93 |
| VfB Stuttgart win | 66.1% | 1.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.40 |
| VfB Stuttgart expected goals | 2.20 |
| Expected total goals | 3.60 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 70.8% |
| Under 2.5 | 29.2% |
| Over 3.5 | 49.2% |
| Under 3.5 | 50.8% |
| Over 4.5 | 30.2% |
| Under 4.5 | 69.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.92% |
| 2 | 1-3 | 8.00% |
| 3 | 0-2 | 7.81% |
| 4 | 0-1 | 7.60% |
| 5 | 1-1 | 6.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.0% | 9.7% | 10.00 | +70.4% |
| Draw | 16.9% | 14.2% | 6.48 | +9.3% |
| VfB Stuttgart win | 66.1% | 76.1% | 1.35 | -10.8% |
| Over 2.5 | 70.8% | 70.8% | 1.37 | -3.0% |
| Under 2.5 | 29.2% | 29.2% | 3.13 | -8.6% |

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
| P btts yes | 65.5% |
| P btts no | 34.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 49.76 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.94 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.42 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.97 |
| Fair Over 4.5 odds | 3.31 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 56.1% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 51.6% |
| Raw p btts yes | 66.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 7.70 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.27 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +7.4% |
| Draw probability edge | +2.6% |
| Away probability edge | -10.0% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.1472 |
| Raw ev home | 1.4402 |
| Raw edge prob draw | 0.0527 |
| Raw ev draw | 0.2637 |
| Raw edge prob away | -0.1999 |
| Raw ev away | -0.2427 |

</details>


---
