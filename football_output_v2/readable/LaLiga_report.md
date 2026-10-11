# La Liga — football model report

Fixtures in this report: **19**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,209 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 2013.044 |
| Base scoring parameter | 0.081 |
| Home-advantage parameter | 0.279 |
| Dixon-Coles low-score adjustment | -0.014 |
| Xi per day | 0.0009 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 19.00 |
| Additional event odds calls used before this league | 5.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 5.00 |
| Additional event odds calls this league | 5.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-09 — Málaga vs Espanyol

The model's most likely 1X2 outcome is **Espanyol win** at **42.2%**. Expected goals are 0.57 for Málaga and 1.09 for Espanyol (1.66 combined). The most likely exact score is 0-0 at 18.4%. Goal-market probabilities: at least one goal: 81.6%; Over 2.5 goals: 23.1%; Under 3.5 goals: 91.6%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 28.8%; BTTS No (at least one team does not score): 71.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 26.1% | 3.84 |
| Draw | 31.7% | 3.15 |
| Espanyol win | 42.2% | 2.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.57 |
| Espanyol expected goals | 1.09 |
| Expected total goals | 1.66 |
| Over 0.5 | 81.6% |
| Under 0.5 | 18.4% |
| Over 1.5 | 48.8% |
| Under 1.5 | 51.2% |
| Over 2.5 | 23.1% |
| Under 2.5 | 76.9% |
| Over 3.5 | 8.4% |
| Under 3.5 | 91.6% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.39% |
| 2 | 0-1 | 18.16% |
| 3 | 1-0 | 14.67% |
| 4 | 1-1 | 11.45% |
| 5 | 0-2 | 9.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 26.1% | 33.1% | 3.05 | -20.5% |
| Draw | 31.7% | 30.3% | 3.35 | +6.2% |
| Espanyol win | 42.2% | 36.6% | 2.66 | +12.3% |
| Over 2.5 | 23.1% | 48.3% | 2.12 | -51.0% |
| Under 2.5 | 76.9% | 51.7% | 1.88 | +44.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-09T19:00:00+00:00 |
| Fixture id | 4e4c6763037ffc0e1dfe92ed16287b6d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:50Z |
| Market best draw last update utc | 2026-10-09T15:20:50Z |
| Market best away last update utc | 2026-10-09T15:20:00Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 93/100 |
| P btts yes | 28.8% |
| P btts no | 71.2% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.44 |
| Fair Over 1.5 odds | 2.05 |
| Fair Under 1.5 odds | 1.95 |
| Fair Over 2.5 odds | 4.32 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.86 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.68 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 19.0% |
| Unadjusted draw probability | 33.2% |
| Unadjusted away-win probability | 47.9% |
| Raw p over 1 5 | 49.5% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 29.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.93 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.66 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.01 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | -7.1% |
| Draw probability edge | +1.4% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -25.1% |
| Under 2.5 probability edge | +25.1% |
| Raw edge prob home | -0.1415 |
| Raw ev home | -0.4210 |
| Raw edge prob draw | 0.0290 |
| Raw ev draw | 0.1110 |
| Raw edge prob away | 0.1126 |
| Raw ev away | 0.2729 |

</details>


---

## 2026-10-10 — Alavés vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **50.2%**. Expected goals are 0.99 for Alavés and 1.47 for Atlético Madrid (2.46 combined). The most likely exact score is 0-1 at 13.0%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 44.8%; Under 3.5 goals: 76.5%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 23.8% | 4.20 |
| Draw | 26.0% | 3.85 |
| Atlético Madrid win | 50.2% | 1.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 0.99 |
| Atlético Madrid expected goals | 1.47 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 70.7% |
| Under 1.5 | 29.3% |
| Over 2.5 | 44.8% |
| Under 2.5 | 55.2% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.97% |
| 2 | 1-1 | 12.30% |
| 3 | 0-2 | 9.63% |
| 4 | 1-2 | 9.56% |
| 5 | 0-0 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 23.8% | 22.2% | 4.70 | +11.9% |
| Draw | 26.0% | 25.3% | 3.95 | +2.7% |
| Atlético Madrid win | 50.2% | 52.5% | 1.87 | -6.1% |
| Over 2.5 | 44.8% | 50.7% | 1.92 | -13.9% |
| Under 2.5 | 55.2% | 49.3% | 2.06 | +13.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T14:15:00+00:00 |
| Fixture id | 3869391e3dbdcaa74153b11df56a3fe5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:50Z |
| Market best draw last update utc | 2026-10-09T15:20:50Z |
| Market best away last update utc | 2026-10-09T15:20:51Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Alaves |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.75 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.26 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.58 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 25.4% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 47.9% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 48.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 4.31 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.87 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +1.6% |
| Draw probability edge | +0.7% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.0319 |
| Raw ev home | 0.1942 |
| Raw edge prob draw | 0.0140 |
| Raw ev draw | 0.0545 |
| Raw edge prob away | -0.0460 |
| Raw ev away | -0.1043 |

</details>


---

## 2026-10-10 — Barcelona vs Getafe

The model's most likely 1X2 outcome is **Barcelona win** at **84.1%**. Expected goals are 2.38 for Barcelona and 0.59 for Getafe (2.97 combined). The most likely exact score is 2-0 at 15.9%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 59.5%; Under 3.5 goals: 64.0%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 38.8%; BTTS No (at least one team does not score): 61.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 84.1% | 1.19 |
| Draw | 10.8% | 9.28 |
| Getafe win | 5.1% | 19.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.38 |
| Getafe expected goals | 0.59 |
| Expected total goals | 2.97 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 81.1% |
| Under 1.5 | 18.9% |
| Over 2.5 | 59.5% |
| Under 2.5 | 40.5% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 15.86% |
| 2 | 1-0 | 13.23% |
| 3 | 3-0 | 12.57% |
| 4 | 2-1 | 9.33% |
| 5 | 4-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 84.1% | 91.0% | 1.11 | -6.6% |
| Draw | 10.8% | 6.0% | 15.00 | +61.6% |
| Getafe win | 5.1% | 3.0% | 32.00 | +63.6% |
| Over 2.5 | 59.5% | 76.7% | 1.28 | -23.9% |
| Under 2.5 | 40.5% | 23.3% | 3.80 | +53.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T16:30:00+00:00 |
| Fixture id | edb80d633a1906e5865ab70cc9b540ea |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:50Z |
| Market best draw last update utc | 2026-10-09T15:19:59Z |
| Market best away last update utc | 2026-10-09T15:20:00Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Barcelona |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 38.8% |
| P btts no | 61.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.39 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.28 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.25 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 77.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 7.3% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.5% |
| Raw p btts yes | 40.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.09 |
| Reference draw odds | 13.00 |
| Reference away odds | 25.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.70 |
| Home probability edge | -6.9% |
| Draw probability edge | +4.7% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -17.2% |
| Under 2.5 probability edge | +17.2% |
| Raw edge prob home | -0.1378 |
| Raw ev home | -0.1428 |
| Raw edge prob draw | 0.0946 |
| Raw ev draw | 1.3259 |
| Raw edge prob away | 0.0432 |
| Raw ev away | 1.3271 |

</details>


---

## 2026-10-10 — Rayo Vallecano vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **35.9%**. Expected goals are 1.01 for Rayo Vallecano and 1.05 for Athletic Bilbao (2.06 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 87.4%; Over 2.5 goals: 34.2%; Under 3.5 goals: 84.6%; Under 4.5 goals: 94.1%; BTTS Yes (both teams score): 41.4%; BTTS No (at least one team does not score): 58.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 34.1% | 2.93 |
| Draw | 30.0% | 3.34 |
| Athletic Bilbao win | 35.9% | 2.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.01 |
| Athletic Bilbao expected goals | 1.05 |
| Expected total goals | 2.06 |
| Over 0.5 | 87.4% |
| Under 0.5 | 12.6% |
| Over 1.5 | 61.3% |
| Under 1.5 | 38.7% |
| Over 2.5 | 34.2% |
| Under 2.5 | 65.8% |
| Over 3.5 | 15.4% |
| Under 3.5 | 84.6% |
| Over 4.5 | 5.9% |
| Under 4.5 | 94.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.40% |
| 2 | 0-1 | 13.24% |
| 3 | 1-0 | 12.87% |
| 4 | 0-0 | 12.63% |
| 5 | 1-2 | 7.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 34.1% | 34.7% | 2.88 | -1.7% |
| Draw | 30.0% | 29.3% | 3.50 | +4.9% |
| Athletic Bilbao win | 35.9% | 36.0% | 2.74 | -1.7% |
| Over 2.5 | 34.2% | 48.8% | 1.99 | -31.9% |
| Under 2.5 | 65.8% | 51.2% | 1.97 | +29.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T12:00:00+00:00 |
| Fixture id | 349c47668fdd909039a9408c14cad8bc |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:50Z |
| Market best away last update utc | 2026-10-09T15:20:50Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Vallecano |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.4% |
| P btts no | 58.6% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 7.92 |
| Fair Over 1.5 odds | 1.63 |
| Fair Under 1.5 odds | 2.58 |
| Fair Over 2.5 odds | 2.92 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.48 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 17.00 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 30.7% |
| Unadjusted away-win probability | 35.8% |
| Raw p over 1 5 | 61.2% |
| Raw p under 3 5 | 84.6% |
| Raw p btts yes | 41.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.80 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.90 |
| Home probability edge | -0.6% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -14.6% |
| Under 2.5 probability edge | +14.6% |
| Raw edge prob home | -0.0112 |
| Raw ev home | -0.0331 |
| Raw edge prob draw | 0.0136 |
| Raw ev draw | 0.0732 |
| Raw edge prob away | -0.0025 |
| Raw ev away | -0.0200 |

</details>


---

## 2026-10-10 — Real Madrid vs Villarreal

The model's most likely 1X2 outcome is **Real Madrid win** at **69.9%**. Expected goals are 2.56 for Real Madrid and 1.12 for Villarreal (3.68 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 71.4%; Under 3.5 goals: 49.6%; Under 4.5 goals: 68.8%; BTTS Yes (both teams score): 62.1%; BTTS No (at least one team does not score): 37.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 69.9% | 1.43 |
| Draw | 16.6% | 6.02 |
| Villarreal win | 13.5% | 7.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.56 |
| Villarreal expected goals | 1.12 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 71.4% |
| Under 2.5 | 28.6% |
| Over 3.5 | 50.4% |
| Under 3.5 | 49.6% |
| Over 4.5 | 31.2% |
| Under 4.5 | 68.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.49% |
| 2 | 2-0 | 8.44% |
| 3 | 3-1 | 8.08% |
| 4 | 3-0 | 7.19% |
| 5 | 1-1 | 7.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 69.9% | 71.5% | 1.40 | -2.2% |
| Draw | 16.6% | 16.0% | 6.40 | +6.3% |
| Villarreal win | 13.5% | 12.4% | 8.00 | +8.3% |
| Over 2.5 | 71.4% | 75.4% | 1.30 | -7.1% |
| Under 2.5 | 28.6% | 24.6% | 3.60 | +2.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T19:00:00+00:00 |
| Fixture id | 551f242223b1625f458d1a2ea212a0c3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:19:59Z |
| Market best away last update utc | 2026-10-09T15:19:59Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Real Madrid |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 62.1% |
| P btts no | 37.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.43 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.65 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.50 |
| Fair Over 3.5 odds | 1.98 |
| Fair Under 3.5 odds | 2.02 |
| Fair Over 4.5 odds | 3.21 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 14.6% |
| Raw p over 1 5 | 88.3% |
| Raw p under 3 5 | 49.8% |
| Raw p btts yes | 62.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.38 |
| Reference draw odds | 5.80 |
| Reference away odds | 7.40 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.55 |
| Home probability edge | -1.7% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | -0.0331 |
| Raw ev home | -0.0452 |
| Raw edge prob draw | 0.0113 |
| Raw ev draw | 0.0992 |
| Raw edge prob away | 0.0217 |
| Raw ev away | 0.1698 |

</details>


---

## 2026-10-11 — Elche CF vs Celta Vigo

The model's most likely 1X2 outcome is **Elche CF win** at **38.5%**. Expected goals are 1.59 for Elche CF and 1.41 for Celta Vigo (3.00 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.8%; Under 3.5 goals: 64.9%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 38.5% | 2.60 |
| Draw | 26.9% | 3.72 |
| Celta Vigo win | 34.6% | 2.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elche CF expected goals | 1.59 |
| Celta Vigo expected goals | 1.41 |
| Expected total goals | 3.00 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 56.8% |
| Under 2.5 | 43.2% |
| Over 3.5 | 35.1% |
| Under 3.5 | 64.9% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.43% |
| 2 | 2-1 | 8.20% |
| 3 | 1-2 | 8.05% |
| 4 | 1-0 | 7.17% |
| 5 | 0-1 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 38.5% | 35.3% | 2.93 | +12.7% |
| Draw | 26.9% | 29.3% | 3.35 | -9.8% |
| Celta Vigo win | 34.6% | 35.3% | 2.75 | -4.8% |
| Over 2.5 | 56.8% | 48.5% | 2.12 | +20.5% |
| Under 2.5 | 43.2% | 51.5% | 1.92 | -17.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T12:00:00+00:00 |
| Fixture id | 7daf7edaf572eba3ac86196c663d67d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:02Z |
| Market best away last update utc | 2026-10-09T15:20:51Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Elche |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.71 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.04 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.85 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.53 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 41.6% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 33.9% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 64.8% |
| Raw p btts yes | 60.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.75 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.75 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.89 |
| Home probability edge | +3.1% |
| Draw probability edge | -2.4% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +8.3% |
| Under 2.5 probability edge | -8.3% |
| Raw edge prob home | 0.0624 |
| Raw ev home | 0.2185 |
| Raw edge prob draw | -0.0478 |
| Raw ev draw | -0.1785 |
| Raw edge prob away | -0.0146 |
| Raw ev away | -0.0680 |

</details>


---

## 2026-10-11 — Real Betis vs CA Osasuna

The model's most likely 1X2 outcome is **Real Betis win** at **59.6%**. Expected goals are 1.77 for Real Betis and 0.94 for CA Osasuna (2.71 combined). The most likely exact score is 1-0 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.5%; Under 3.5 goals: 70.9%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 59.6% | 1.68 |
| Draw | 22.3% | 4.47 |
| CA Osasuna win | 18.1% | 5.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.77 |
| CA Osasuna expected goals | 0.94 |
| Expected total goals | 2.71 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 75.7% |
| Under 1.5 | 24.3% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.19% |
| 2 | 2-0 | 10.95% |
| 3 | 1-1 | 10.64% |
| 4 | 2-1 | 10.27% |
| 5 | 3-0 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 59.6% | 62.3% | 1.60 | -4.7% |
| Draw | 22.3% | 21.1% | 4.62 | +3.2% |
| CA Osasuna win | 18.1% | 16.5% | 6.60 | +19.2% |
| Over 2.5 | 51.5% | 54.4% | 1.81 | -6.9% |
| Under 2.5 | 48.5% | 45.6% | 2.18 | +5.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T16:30:00+00:00 |
| Fixture id | 984691837d31fd0c59c088f377f55f75 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:47Z |
| Market best away last update utc | 2026-10-09T15:20:35Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Betis |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.49 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.09 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 56.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 19.6% |
| Raw p over 1 5 | 75.5% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 50.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.58 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.70 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -2.7% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | -0.0548 |
| Raw ev home | -0.0904 |
| Raw edge prob draw | 0.0244 |
| Raw ev draw | 0.0888 |
| Raw edge prob away | 0.0304 |
| Raw ev away | 0.2927 |

</details>


---

## 2026-10-11 — Real Racing Club de Santander vs Valencia

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **40.2%**. Expected goals are 1.92 for Real Racing Club de Santander and 1.95 for Valencia (3.87 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 73.4%; Under 3.5 goals: 46.0%; Under 4.5 goals: 66.0%; BTTS Yes (both teams score): 73.9%; BTTS No (at least one team does not score): 26.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 40.2% | 2.49 |
| Draw | 24.2% | 4.13 |
| Valencia win | 35.5% | 2.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.92 |
| Valencia expected goals | 1.95 |
| Expected total goals | 3.87 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 90.0% |
| Under 1.5 | 10.0% |
| Over 2.5 | 73.4% |
| Under 2.5 | 26.6% |
| Over 3.5 | 54.0% |
| Under 3.5 | 46.0% |
| Over 4.5 | 34.0% |
| Under 4.5 | 66.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.01% |
| 2 | 2-2 | 8.32% |
| 3 | 2-1 | 7.76% |
| 4 | 1-2 | 6.78% |
| 5 | 3-1 | 4.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 40.2% | 41.6% | 2.42 | -2.6% |
| Draw | 24.2% | 27.2% | 3.71 | -10.1% |
| Valencia win | 35.5% | 31.3% | 3.10 | +10.1% |
| Over 2.5 | 73.4% | 55.4% | 1.76 | +29.2% |
| Under 2.5 | 26.6% | 44.6% | 2.27 | -39.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T19:00:00+00:00 |
| Fixture id | 66a4f4201806b928c9007116727fdd61 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:00Z |
| Market best away last update utc | 2026-10-09T15:19:59Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Valencia |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 73.9% |
| P btts no | 26.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.07 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.95 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.76 |
| Fair Over 3.5 odds | 1.85 |
| Fair Under 3.5 odds | 2.18 |
| Fair Over 4.5 odds | 2.94 |
| Fair Under 4.5 odds | 1.52 |
| Unadjusted home-win probability | 38.9% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 39.8% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 45.9% |
| Raw p btts yes | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.35 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.17 |
| Home probability edge | -1.3% |
| Draw probability edge | -3.0% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | +18.0% |
| Under 2.5 probability edge | -18.0% |
| Raw edge prob home | -0.0263 |
| Raw ev home | -0.0582 |
| Raw edge prob draw | -0.0590 |
| Raw ev draw | -0.2101 |
| Raw edge prob away | 0.0853 |
| Raw ev away | 0.2335 |
| Market p over 1 5 | 78.9% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T15:20:51Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 4.35 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 66.7% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T15:20:47Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 62.0% |
| Market btts yes odds | 1.59 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T15:20:35Z |
| Market reference btts yes odds | 1.59 |
| Market reference btts yes opposite odds | 2.56 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Real Sociedad vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Real Sociedad win** at **51.7%**. Expected goals are 1.49 for Real Sociedad and 1.20 for Deportivo La Coruña (2.68 combined). The most likely exact score is 1-0 at 11.8%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.4%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 53.7%; BTTS No (at least one team does not score): 46.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 51.7% | 1.94 |
| Draw | 24.5% | 4.08 |
| Deportivo La Coruña win | 23.8% | 4.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.49 |
| Deportivo La Coruña expected goals | 1.20 |
| Expected total goals | 2.68 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.6% |
| Under 3.5 | 71.4% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.80% |
| 2 | 1-1 | 11.65% |
| 3 | 2-1 | 10.69% |
| 4 | 2-0 | 8.92% |
| 5 | 0-0 | 6.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 51.7% | 59.7% | 1.66 | -14.2% |
| Draw | 24.5% | 23.1% | 4.22 | +3.4% |
| Deportivo La Coruña win | 23.8% | 17.3% | 6.00 | +43.0% |
| Over 2.5 | 50.9% | 56.4% | 1.81 | -7.9% |
| Under 2.5 | 49.1% | 43.6% | 2.24 | +10.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T14:15:00+00:00 |
| Fixture id | 2997b68cc93f62d8a1dee9f06bedbefd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:48Z |
| Market best away last update utc | 2026-10-09T15:20:50Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Sociedad |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 53.7% |
| P btts no | 46.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.13 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.05 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.26 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 54.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.65 |
| Reference draw odds | 4.15 |
| Reference away odds | 5.50 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.21 |
| Home probability edge | -8.0% |
| Draw probability edge | +1.4% |
| Away probability edge | +6.6% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | -0.1605 |
| Raw ev home | -0.2757 |
| Raw edge prob draw | 0.0287 |
| Raw ev draw | 0.0945 |
| Raw edge prob away | 0.1317 |
| Raw ev away | 0.8257 |

</details>


---

## 2026-10-12 — Levante vs Sevilla

The model's most likely 1X2 outcome is **Levante win** at **40.0%**. Expected goals are 1.61 for Levante and 1.27 for Sevilla (2.88 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 54.1%; Under 3.5 goals: 67.7%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 58.3%; BTTS No (at least one team does not score): 41.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 40.0% | 2.50 |
| Draw | 27.0% | 3.70 |
| Sevilla win | 32.9% | 3.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.61 |
| Sevilla expected goals | 1.27 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.69% |
| 2 | 2-1 | 8.17% |
| 3 | 1-2 | 8.01% |
| 4 | 1-0 | 7.85% |
| 5 | 0-1 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 40.0% | 34.7% | 2.92 | +16.9% |
| Draw | 27.0% | 29.3% | 3.43 | -7.3% |
| Sevilla win | 32.9% | 36.0% | 2.75 | -9.4% |
| Over 2.5 | 54.1% | 46.9% | 2.10 | +13.6% |
| Under 2.5 | 45.9% | 53.1% | 1.86 | -14.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-12T19:00:00+00:00 |
| Fixture id | 529fc26c7774d5b469932e275c668921 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:35Z |
| Market best draw last update utc | 2026-10-09T15:20:00Z |
| Market best away last update utc | 2026-10-09T15:19:59Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Matchbook |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.3% |
| P btts no | 41.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.87 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.58 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.21 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 45.4% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 29.9% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 57.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.80 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | +5.3% |
| Draw probability edge | -2.3% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | +7.2% |
| Under 2.5 probability edge | -7.2% |
| Raw edge prob home | 0.1067 |
| Raw ev home | 0.3245 |
| Raw edge prob draw | -0.0452 |
| Raw ev draw | -0.1500 |
| Raw edge prob away | -0.0615 |
| Raw ev away | -0.1788 |

</details>


---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.7%**. Expected goals are 1.84 for Deportivo La Coruña and 1.11 for Levante (2.95 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.1%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.7% | 1.97 |
| Draw | 24.8% | 4.04 |
| Levante win | 24.5% | 4.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 1.84 |
| Levante expected goals | 1.11 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 79.3% |
| Under 1.5 | 20.7% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.63% |
| 2 | 2-1 | 9.17% |
| 3 | 1-0 | 8.83% |
| 4 | 2-0 | 8.27% |
| 5 | 1-2 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.7% | 47.0% | 2.17 | +10.0% |
| Draw | 24.8% | 26.5% | 3.62 | -10.3% |
| Levante win | 24.5% | 26.5% | 3.60 | -11.7% |
| Over 2.5 | 55.9% | 51.2% | 1.98 | +10.6% |
| Under 2.5 | 44.1% | 48.8% | 1.96 | -13.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-16T19:00:00+00:00 |
| Fixture id | 19ee731602634e5c9e3106630e087464 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:00Z |
| Market best away last update utc | 2026-10-09T15:20:00Z |
| Odds bookmakers 1x2 | 12.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | La Coruna |
| Matched away-team name | Levante |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.33 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.77 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.4% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 79.5% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.97 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.93 |
| Home probability edge | +3.7% |
| Draw probability edge | -1.7% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +4.7% |
| Under 2.5 probability edge | -4.7% |
| Raw edge prob home | 0.0736 |
| Raw ev home | 0.1801 |
| Raw edge prob draw | -0.0342 |
| Raw ev draw | -0.1650 |
| Raw edge prob away | -0.0394 |
| Raw ev away | -0.1882 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **52.2%**. Expected goals are 1.03 for Espanyol and 1.58 for Atlético Madrid (2.60 combined). The most likely exact score is 0-1 at 12.0%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 48.7%; Under 3.5 goals: 73.3%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 23.2% | 4.30 |
| Draw | 24.5% | 4.08 |
| Atlético Madrid win | 52.2% | 1.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.03 |
| Atlético Madrid expected goals | 1.58 |
| Expected total goals | 2.60 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.7% |
| Under 2.5 | 51.3% |
| Over 3.5 | 26.7% |
| Under 3.5 | 73.3% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.02% |
| 2 | 1-1 | 11.66% |
| 3 | 1-2 | 9.88% |
| 4 | 0-2 | 9.62% |
| 5 | 0-0 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 23.2% | 22.0% | 4.32 | +0.4% |
| Draw | 24.5% | 23.5% | 3.84 | -5.9% |
| Atlético Madrid win | 52.2% | 54.5% | 1.91 | -0.2% |
| Over 2.5 | 48.7% | 53.8% | 1.87 | -8.9% |
| Under 2.5 | 51.3% | 46.2% | 2.08 | +6.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T12:00:00+00:00 |
| Fixture id | 6436925dd15916d7041ba32b60000d48 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:00Z |
| Market best away last update utc | 2026-10-09T15:20:00Z |
| Odds bookmakers 1x2 | 12.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Espanol |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 93/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.78 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.75 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.01 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 50.0% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.5% |
| Raw p btts yes | 51.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.65 |
| Reference draw odds | 3.45 |
| Reference away odds | 1.68 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.04 |
| Home probability edge | +1.3% |
| Draw probability edge | +1.0% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | 0.0250 |
| Raw ev home | 0.0584 |
| Raw edge prob draw | 0.0203 |
| Raw ev draw | -0.0198 |
| Raw edge prob away | -0.0453 |
| Raw ev away | -0.0455 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **61.0%**. Expected goals are 1.32 for Real Betis and 2.05 for Barcelona (3.37 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 66.6%; Under 3.5 goals: 55.9%; Under 4.5 goals: 74.2%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 20.2% | 4.94 |
| Draw | 18.8% | 5.32 |
| Barcelona win | 61.0% | 1.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.32 |
| Barcelona expected goals | 2.05 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 66.6% |
| Under 2.5 | 33.4% |
| Over 3.5 | 44.1% |
| Under 3.5 | 55.9% |
| Over 4.5 | 25.8% |
| Under 4.5 | 74.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.76% |
| 2 | 1-1 | 8.22% |
| 3 | 0-2 | 8.12% |
| 4 | 0-1 | 7.78% |
| 5 | 1-3 | 7.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 20.2% | 16.0% | 6.21 | +25.6% |
| Draw | 18.8% | 16.0% | 6.00 | +12.8% |
| Barcelona win | 61.0% | 67.9% | 1.49 | -9.2% |
| Over 2.5 | 66.6% | 76.7% | 1.28 | -14.7% |
| Under 2.5 | 33.4% | 23.3% | 3.76 | +25.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | 846e496fc232b2fc20214754836727d0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:50Z |
| Market best away last update utc | 2026-10-09T15:20:00Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.22 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.88 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 3.00 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.87 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 54.0% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 64.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 6.00 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.46 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.70 |
| Home probability edge | +4.2% |
| Draw probability edge | +2.8% |
| Away probability edge | -7.0% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | 0.0838 |
| Raw ev home | 0.5163 |
| Raw edge prob draw | 0.0554 |
| Raw ev draw | 0.2943 |
| Raw edge prob away | -0.1392 |
| Raw ev away | -0.1952 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.3%**. Expected goals are 1.08 for Valencia and 1.17 for Athletic Bilbao (2.25 combined). The most likely exact score is 0-1 at 13.6%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 39.3%; Under 3.5 goals: 81.0%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.6% | 3.37 |
| Draw | 28.1% | 3.56 |
| Athletic Bilbao win | 42.3% | 2.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.08 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.25 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.3% |
| Under 2.5 | 60.7% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.64% |
| 2 | 1-1 | 13.04% |
| 3 | 0-0 | 10.40% |
| 4 | 1-0 | 10.03% |
| 5 | 1-2 | 8.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.6% | 26.2% | 3.71 | +9.9% |
| Draw | 28.1% | 27.1% | 3.58 | +0.6% |
| Athletic Bilbao win | 42.3% | 46.7% | 2.18 | -7.9% |
| Over 2.5 | 39.3% | 46.6% | 2.10 | -17.5% |
| Under 2.5 | 60.7% | 53.4% | 1.86 | +12.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T19:00:00+00:00 |
| Fixture id | f00cd1ea41fa39149729d14ebc07aa6c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:47Z |
| Market best draw last update utc | 2026-10-09T15:20:00Z |
| Market best away last update utc | 2026-10-09T15:20:00Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.4% |
| P btts no | 54.6% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.61 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.54 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.74 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.1% |
| Unadjusted away-win probability | 37.8% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 45.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.20 |
| Reference away odds | 1.97 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.78 |
| Home probability edge | +3.5% |
| Draw probability edge | +1.0% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | 0.0691 |
| Raw ev home | 0.2277 |
| Raw edge prob draw | 0.0201 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | -0.0892 |
| Raw ev away | -0.1760 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **66.1%**. Expected goals are 2.51 for Villarreal and 1.25 for Elche CF (3.76 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 72.6%; Under 3.5 goals: 47.9%; Under 4.5 goals: 67.4%; BTTS Yes (both teams score): 65.6%; BTTS No (at least one team does not score): 34.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 66.1% | 1.51 |
| Draw | 18.0% | 5.56 |
| Elche CF win | 16.0% | 6.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.51 |
| Elche CF expected goals | 1.25 |
| Expected total goals | 3.76 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 89.1% |
| Under 1.5 | 10.9% |
| Over 2.5 | 72.6% |
| Under 2.5 | 27.4% |
| Over 3.5 | 52.1% |
| Under 3.5 | 47.9% |
| Over 4.5 | 32.6% |
| Under 4.5 | 67.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.37% |
| 2 | 3-1 | 7.84% |
| 3 | 2-0 | 7.47% |
| 4 | 1-1 | 7.39% |
| 5 | 3-0 | 6.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 66.1% | 67.5% | 1.51 | -0.3% |
| Draw | 18.0% | 17.9% | 5.00 | -10.1% |
| Elche CF win | 16.0% | 14.6% | 6.73 | +7.4% |
| Over 2.5 | 72.6% | 64.6% | 1.51 | +9.6% |
| Under 2.5 | 27.4% | 35.4% | 2.70 | -26.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:15:00+00:00 |
| Fixture id | aef660734585649651415961a9d177c6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:48Z |
| Market best away last update utc | 2026-10-09T15:20:00Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.6% |
| P btts no | 34.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.35 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.21 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.65 |
| Fair Over 3.5 odds | 1.92 |
| Fair Under 3.5 odds | 2.09 |
| Fair Over 4.5 odds | 3.07 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 64.6% |
| Unadjusted draw probability | 18.0% |
| Unadjusted away-win probability | 17.4% |
| Raw p over 1 5 | 89.0% |
| Raw p under 3 5 | 48.1% |
| Raw p btts yes | 65.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.41 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.40 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Home probability edge | -1.5% |
| Draw probability edge | +0.1% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +8.0% |
| Under 2.5 probability edge | -8.0% |
| Raw edge prob home | -0.0293 |
| Raw ev home | -0.0247 |
| Raw edge prob draw | 0.0012 |
| Raw ev draw | -0.0978 |
| Raw edge prob away | 0.0281 |
| Raw ev away | 0.1687 |
| Market p over 1 5 | 87.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T15:20:01Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 57.4% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T15:18:46Z |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.22 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-09T15:20:00Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **57.9%**. Expected goals are 2.71 for CA Osasuna and 1.48 for Real Racing Club de Santander (4.19 combined). The most likely exact score is 2-1 at 7.5%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 77.7%; Under 3.5 goals: 40.2%; Under 4.5 goals: 60.3%; BTTS Yes (both teams score): 73.2%; BTTS No (at least one team does not score): 26.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 57.9% | 1.73 |
| Draw | 21.0% | 4.77 |
| Real Racing Club de Santander win | 21.1% | 4.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 2.71 |
| Real Racing Club de Santander expected goals | 1.48 |
| Expected total goals | 4.19 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 77.7% |
| Under 2.5 | 22.3% |
| Over 3.5 | 59.8% |
| Under 3.5 | 40.2% |
| Over 4.5 | 39.7% |
| Under 4.5 | 60.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 7.51% |
| 2 | 1-1 | 7.43% |
| 3 | 2-2 | 7.35% |
| 4 | 3-1 | 6.78% |
| 5 | 2-0 | 5.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 57.9% | 52.4% | 1.95 | +12.9% |
| Draw | 21.0% | 24.5% | 3.68 | -22.9% |
| Real Racing Club de Santander win | 21.1% | 23.1% | 4.32 | -8.7% |
| Over 2.5 | 77.7% | 54.4% | 1.81 | +40.7% |
| Under 2.5 | 22.3% | 45.6% | 2.17 | -51.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T12:00:00+00:00 |
| Fixture id | 1f566f17c50fe5162724ec2863d2207b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:00Z |
| Market best away last update utc | 2026-10-09T15:20:00Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Osasuna |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 73.2% |
| P btts no | 26.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 51.88 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.56 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.49 |
| Fair Over 3.5 odds | 1.67 |
| Fair Under 3.5 odds | 2.49 |
| Fair Over 4.5 odds | 2.52 |
| Fair Under 4.5 odds | 1.66 |
| Unadjusted home-win probability | 63.4% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 19.2% |
| Raw p over 1 5 | 92.2% |
| Raw p under 3 5 | 39.7% |
| Raw p btts yes | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.78 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.06 |
| Home probability edge | +5.5% |
| Draw probability edge | -3.6% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +23.3% |
| Under 2.5 probability edge | -23.3% |
| Raw edge prob home | 0.1105 |
| Raw ev home | 0.2370 |
| Raw edge prob draw | -0.0717 |
| Raw ev draw | -0.3605 |
| Raw edge prob away | -0.0388 |
| Raw ev away | -0.1712 |
| Market p over 1 5 | 80.0% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T15:20:01Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 68.6% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T15:20:47Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.87 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T15:20:01Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.15 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **49.1%**. Expected goals are 1.51 for Celta Vigo and 0.96 for Alavés (2.47 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.7%; Under 3.5 goals: 76.5%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.4%; BTTS No (at least one team does not score): 51.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 49.1% | 2.04 |
| Draw | 26.7% | 3.75 |
| Alavés win | 24.2% | 4.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.51 |
| Alavés expected goals | 0.96 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.7% |
| Under 2.5 | 55.3% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.61% |
| 2 | 1-0 | 12.44% |
| 3 | 2-0 | 9.50% |
| 4 | 2-1 | 9.14% |
| 5 | 0-0 | 8.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 49.1% | 48.6% | 2.08 | +2.2% |
| Draw | 26.7% | 27.0% | 3.58 | -4.5% |
| Alavés win | 24.2% | 24.4% | 3.95 | -4.4% |
| Over 2.5 | 44.7% | 43.8% | 2.19 | -2.1% |
| Under 2.5 | 55.3% | 56.2% | 1.79 | -1.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T14:15:00+00:00 |
| Fixture id | aabe899ecc4c19a1fafe5440151b62e4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:00Z |
| Market best away last update utc | 2026-10-09T15:20:48Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.42 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.59 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 70.8% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.90 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.14 |
| Reference Under 2.5 odds | 1.70 |
| Home probability edge | +0.6% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.0112 |
| Raw ev home | 0.0334 |
| Raw edge prob draw | -0.0068 |
| Raw ev draw | -0.0573 |
| Raw edge prob away | -0.0043 |
| Raw ev away | -0.0525 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.5%**. Expected goals are 0.57 for Málaga and 1.26 for Real Sociedad (1.83 combined). The most likely exact score is 0-1 at 18.3%. Goal-market probabilities: at least one goal: 84.8%; Over 2.5 goals: 27.7%; Under 3.5 goals: 89.0%; Under 4.5 goals: 96.2%; BTTS Yes (both teams score): 31.0%; BTTS No (at least one team does not score): 69.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.3% | 4.30 |
| Draw | 28.3% | 3.54 |
| Real Sociedad win | 48.5% | 2.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.57 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.83 |
| Over 0.5 | 84.8% |
| Under 0.5 | 15.2% |
| Over 1.5 | 53.9% |
| Under 1.5 | 46.1% |
| Over 2.5 | 27.7% |
| Under 2.5 | 72.3% |
| Over 3.5 | 11.0% |
| Under 3.5 | 89.0% |
| Over 4.5 | 3.8% |
| Under 4.5 | 96.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.28% |
| 2 | 0-0 | 15.23% |
| 3 | 1-0 | 12.57% |
| 4 | 0-2 | 11.61% |
| 5 | 1-1 | 10.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.3% | 29.9% | 3.30 | -23.2% |
| Draw | 28.3% | 26.4% | 3.63 | +2.6% |
| Real Sociedad win | 48.5% | 43.7% | 2.29 | +11.0% |
| Over 2.5 | 27.7% | 54.1% | 1.86 | -48.4% |
| Under 2.5 | 72.3% | 45.9% | 2.10 | +51.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T16:30:00+00:00 |
| Fixture id | 1051298b4aca6f07113309bff598a5c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:16Z |
| Market best draw last update utc | 2026-10-09T15:20:00Z |
| Market best away last update utc | 2026-10-09T15:20:00Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 31.0% |
| P btts no | 69.0% |
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.57 |
| Fair Over 1.5 odds | 1.85 |
| Fair Under 1.5 odds | 2.17 |
| Fair Over 2.5 odds | 3.61 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.09 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 26.36 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 16.6% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 53.2% |
| Raw p over 1 5 | 54.7% |
| Raw p under 3 5 | 88.7% |
| Raw p btts yes | 31.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | -6.6% |
| Draw probability edge | +1.9% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -26.4% |
| Under 2.5 probability edge | +26.4% |
| Raw edge prob home | -0.1329 |
| Raw ev home | -0.4517 |
| Raw edge prob draw | 0.0375 |
| Raw ev draw | 0.0941 |
| Raw edge prob away | 0.0954 |
| Raw ev away | 0.2193 |
| Market p over 1 5 | 77.8% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T15:20:01Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 68.8% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T15:20:47Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.91 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 58.9% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T15:20:01Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.25 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.1%**. Expected goals are 2.62 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 65.7%; Under 3.5 goals: 56.4%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.1% | 1.28 |
| Draw | 13.8% | 7.25 |
| Sevilla win | 8.1% | 12.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.62 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 65.7% |
| Under 2.5 | 34.3% |
| Over 3.5 | 43.6% |
| Under 3.5 | 56.4% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.98% |
| 2 | 3-0 | 10.47% |
| 3 | 1-0 | 9.04% |
| 4 | 2-1 | 8.91% |
| 5 | 3-1 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 78.1% | 78.8% | 1.30 | +1.5% |
| Draw | 13.8% | 13.1% | 7.20 | -0.8% |
| Sevilla win | 8.1% | 8.1% | 11.50 | -6.7% |
| Over 2.5 | 65.7% | 69.6% | 1.40 | -8.1% |
| Under 2.5 | 34.3% | 30.4% | 3.00 | +3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T19:00:00+00:00 |
| Fixture id | eccd63bf768e2f2a358b871d3f33a63d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T15:20:00Z |
| Market best draw last update utc | 2026-10-09T15:20:50Z |
| Market best away last update utc | 2026-10-09T15:20:35Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.60 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.72 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.98 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.26 |
| Reference draw odds | 7.20 |
| Reference away odds | 11.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | -0.7% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0144 |
| Raw ev home | 0.0059 |
| Raw edge prob draw | 0.0138 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | 0.0006 |
| Raw ev away | -0.0629 |

</details>


---
