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
| Additional event odds calls used before this league | 19.00 |
| Additional event odds calls budget | 24.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-09 — Málaga vs Espanyol

The model's most likely 1X2 outcome is **Espanyol win** at **42.5%**. Expected goals are 0.57 for Málaga and 1.09 for Espanyol (1.66 combined). The most likely exact score is 0-1 at 18.3%. Goal-market probabilities: at least one goal: 82.1%; Over 2.5 goals: 23.3%; Under 4.5 goals: 97.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 26.5% | 3.77 |
| Draw | 30.9% | 3.23 |
| Espanyol win | 42.5% | 2.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.57 |
| Espanyol expected goals | 1.09 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.1% |
| Under 0.5 | 17.9% |
| Over 1.5 | 48.8% |
| Under 1.5 | 51.2% |
| Over 2.5 | 23.3% |
| Under 2.5 | 76.7% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.28% |
| 2 | 0-0 | 17.93% |
| 3 | 1-0 | 14.95% |
| 4 | 1-1 | 11.17% |
| 5 | 0-2 | 10.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 26.5% | 34.1% | 3.00 | -20.4% |
| Draw | 30.9% | 28.7% | 3.30 | +2.1% |
| Espanyol win | 42.5% | 37.2% | 2.75 | +16.9% |
| Over 2.5 | 23.3% | 46.4% | 2.17 | -49.4% |
| Under 2.5 | 76.7% | 53.6% | 1.85 | +41.9% |

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
| Market best home last update utc | 2026-10-09T08:09:54Z |
| Market best draw last update utc | 2026-10-09T08:10:27Z |
| Market best away last update utc | 2026-10-09T08:07:00Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Malaga |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 93/100 |
| P btts yes | 28.7% |
| P btts no | 71.3% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.58 |
| Fair Over 1.5 odds | 2.05 |
| Fair Under 1.5 odds | 1.95 |
| Fair Over 2.5 odds | 4.29 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.83 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.35 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 19.0% |
| Unadjusted draw probability | 33.2% |
| Unadjusted away-win probability | 47.9% |
| Raw p over 1 5 | 49.5% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 29.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.45 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.09 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | -7.6% |
| Draw probability edge | +2.2% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | -23.1% |
| Under 2.5 probability edge | +23.1% |
| Raw edge prob home | -0.1513 |
| Raw ev home | -0.4305 |
| Raw edge prob draw | 0.0447 |
| Raw ev draw | 0.0944 |
| Raw edge prob away | 0.1065 |
| Raw ev away | 0.3159 |
| Market p over 1 5 | 73.7% |
| Market over 1 5 odds | 1.37 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:09:58Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.48 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 74.8% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:40Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.62 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 54.2% |
| Market btts yes odds | 1.83 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 2.16 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-10 — Alavés vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **50.4%**. Expected goals are 0.99 for Alavés and 1.47 for Atlético Madrid (2.46 combined). The most likely exact score is 0-1 at 13.0%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 44.8%; Under 4.5 goals: 89.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 23.6% | 4.24 |
| Draw | 26.0% | 3.84 |
| Atlético Madrid win | 50.4% | 1.98 |

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
| 1 | 0-1 | 13.02% |
| 2 | 1-1 | 12.31% |
| 3 | 0-2 | 9.68% |
| 4 | 1-2 | 9.60% |
| 5 | 0-0 | 8.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 23.6% | 21.7% | 4.70 | +10.8% |
| Draw | 26.0% | 25.3% | 3.92 | +2.0% |
| Atlético Madrid win | 50.4% | 52.9% | 1.87 | -5.7% |
| Over 2.5 | 44.8% | 50.9% | 1.93 | -13.5% |
| Under 2.5 | 55.2% | 49.1% | 2.05 | +13.1% |

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
| Market best home last update utc | 2026-10-09T08:10:27Z |
| Market best draw last update utc | 2026-10-09T08:07:00Z |
| Market best away last update utc | 2026-10-09T08:09:58Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.74 |
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
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.37 |
| Reference draw odds | 3.77 |
| Reference away odds | 1.85 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.98 |
| Home probability edge | +1.8% |
| Draw probability edge | +0.7% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | 0.0366 |
| Raw ev home | 0.1942 |
| Raw edge prob draw | 0.0136 |
| Raw ev draw | 0.0465 |
| Raw edge prob away | -0.0502 |
| Raw ev away | -0.1043 |
| Market p over 1 5 | 76.6% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:09:58Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 3.83 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 71.3% |
| Market under 3 5 odds | 1.37 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:40Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.20 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 54.0% |
| Market btts yes odds | 1.83 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 2.14 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-10 — Barcelona vs Getafe

The model's most likely 1X2 outcome is **Barcelona win** at **86.5%**. Expected goals are 2.38 for Barcelona and 0.59 for Getafe (2.97 combined). The most likely exact score is 2-0 at 16.3%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 60.3%; Under 4.5 goals: 80.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 86.5% | 1.16 |
| Draw | 9.4% | 10.63 |
| Getafe win | 4.1% | 24.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.38 |
| Getafe expected goals | 0.59 |
| Expected total goals | 2.97 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 81.5% |
| Under 1.5 | 18.5% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 36.5% |
| Under 3.5 | 63.5% |
| Over 4.5 | 19.4% |
| Under 4.5 | 80.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 16.31% |
| 2 | 1-0 | 13.60% |
| 3 | 3-0 | 12.92% |
| 4 | 2-1 | 9.59% |
| 5 | 4-0 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 86.5% | 95.7% | 1.10 | -4.9% |
| Draw | 9.4% | 3.3% | 16.00 | +50.6% |
| Getafe win | 4.1% | 1.0% | 38.00 | +56.5% |
| Over 2.5 | 60.3% | 78.3% | 1.25 | -24.6% |
| Under 2.5 | 39.7% | 21.7% | 4.02 | +59.6% |

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
| Market best home last update utc | 2026-10-09T08:10:27Z |
| Market best draw last update utc | 2026-10-09T08:10:27Z |
| Market best away last update utc | 2026-10-09T08:07:00Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Barcelona |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 38.2% |
| P btts no | 61.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.37 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.42 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.74 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.15 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 77.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 7.3% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.5% |
| Raw p btts yes | 40.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.03 |
| Reference draw odds | 10.00 |
| Reference away odds | 23.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.02 |
| Home probability edge | -9.2% |
| Draw probability edge | +6.1% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -18.0% |
| Under 2.5 probability edge | +18.0% |
| Raw edge prob home | -0.1850 |
| Raw ev home | -0.1506 |
| Raw edge prob draw | 0.1219 |
| Raw ev draw | 1.4810 |
| Raw edge prob away | 0.0631 |
| Raw ev away | 1.7634 |
| Market p over 1 5 | 92.4% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T08:09:55Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 9.00 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 43.0% |
| Market under 3 5 odds | 2.23 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T08:09:58Z |
| Market reference under 3 5 odds | 2.20 |
| Market reference under 3 5 opposite odds | 1.69 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 40.2% |
| Market btts yes odds | 2.46 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 2.46 |
| Market reference btts yes opposite odds | 1.66 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-10 — Rayo Vallecano vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **36.8%**. Expected goals are 1.01 for Rayo Vallecano and 1.05 for Athletic Bilbao (2.06 combined). The most likely exact score is 0-1 at 13.6%. Goal-market probabilities: at least one goal: 87.7%; Over 2.5 goals: 34.5%; Under 4.5 goals: 94.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 34.1% | 2.93 |
| Draw | 29.1% | 3.44 |
| Athletic Bilbao win | 36.8% | 2.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.01 |
| Athletic Bilbao expected goals | 1.05 |
| Expected total goals | 2.06 |
| Over 0.5 | 87.7% |
| Under 0.5 | 12.3% |
| Over 1.5 | 61.3% |
| Under 1.5 | 38.7% |
| Over 2.5 | 34.5% |
| Under 2.5 | 65.5% |
| Over 3.5 | 15.5% |
| Under 3.5 | 84.5% |
| Over 4.5 | 5.9% |
| Under 4.5 | 94.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.58% |
| 2 | 1-1 | 13.00% |
| 3 | 1-0 | 12.86% |
| 4 | 0-0 | 12.25% |
| 5 | 1-2 | 7.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 34.1% | 34.6% | 2.88 | -1.8% |
| Draw | 29.1% | 27.5% | 3.50 | +1.8% |
| Athletic Bilbao win | 36.8% | 37.9% | 2.74 | +0.9% |
| Over 2.5 | 34.5% | 49.7% | 1.99 | -31.4% |
| Under 2.5 | 65.5% | 50.3% | 1.98 | +29.7% |

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
| Market best home last update utc | 2026-10-09T08:07:00Z |
| Market best draw last update utc | 2026-10-09T08:10:27Z |
| Market best away last update utc | 2026-10-09T08:10:27Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Vallecano |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.16 |
| Fair Over 1.5 odds | 1.63 |
| Fair Under 1.5 odds | 2.58 |
| Fair Over 2.5 odds | 2.90 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.46 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 16.84 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 30.7% |
| Unadjusted away-win probability | 35.8% |
| Raw p over 1 5 | 61.2% |
| Raw p under 3 5 | 84.6% |
| Raw p btts yes | 41.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.93 |
| Home probability edge | -0.5% |
| Draw probability edge | +1.6% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -15.3% |
| Under 2.5 probability edge | +15.3% |
| Raw edge prob home | -0.0106 |
| Raw ev home | -0.0331 |
| Raw edge prob draw | 0.0315 |
| Raw ev draw | 0.0732 |
| Raw edge prob away | -0.0209 |
| Raw ev away | -0.0200 |
| Market p over 1 5 | 76.1% |
| Market over 1 5 odds | 1.33 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:09:58Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.79 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 72.5% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:40Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.34 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 56.5% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.26 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-10 — Real Madrid vs Villarreal

The model's most likely 1X2 outcome is **Real Madrid win** at **70.1%**. Expected goals are 2.56 for Real Madrid and 1.12 for Villarreal (3.68 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 71.6%; Under 4.5 goals: 68.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 70.1% | 1.43 |
| Draw | 15.9% | 6.27 |
| Villarreal win | 13.9% | 7.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.56 |
| Villarreal expected goals | 1.12 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 71.6% |
| Under 2.5 | 28.4% |
| Over 3.5 | 50.4% |
| Under 3.5 | 49.6% |
| Over 4.5 | 31.3% |
| Under 4.5 | 68.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.52% |
| 2 | 2-0 | 8.47% |
| 3 | 3-1 | 8.11% |
| 4 | 3-0 | 7.22% |
| 5 | 1-1 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 70.1% | 72.0% | 1.40 | -1.8% |
| Draw | 15.9% | 14.7% | 6.20 | -1.2% |
| Villarreal win | 13.9% | 13.3% | 7.80 | +8.7% |
| Over 2.5 | 71.6% | 75.2% | 1.30 | -6.9% |
| Under 2.5 | 28.4% | 24.8% | 3.60 | +2.1% |

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
| Market best home last update utc | 2026-10-09T08:07:00Z |
| Market best draw last update utc | 2026-10-09T08:10:27Z |
| Market best away last update utc | 2026-10-09T08:10:27Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Real Madrid |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 62.0% |
| P btts no | 38.0% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.09 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.65 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.53 |
| Fair Over 3.5 odds | 1.98 |
| Fair Under 3.5 odds | 2.02 |
| Fair Over 4.5 odds | 3.20 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 14.6% |
| Raw p over 1 5 | 88.3% |
| Raw p under 3 5 | 49.8% |
| Raw p btts yes | 62.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.33 |
| Reference draw odds | 5.30 |
| Reference away odds | 5.80 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.60 |
| Home probability edge | -1.9% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.0384 |
| Raw ev home | -0.0452 |
| Raw edge prob draw | 0.0248 |
| Raw ev draw | 0.0649 |
| Raw edge prob away | 0.0137 |
| Raw ev away | 0.1405 |
| Market p over 1 5 | 91.0% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:09:58Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 9.10 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 44.3% |
| Market under 3 5 odds | 2.19 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T08:00:44Z |
| Market reference under 3 5 odds | 2.16 |
| Market reference under 3 5 opposite odds | 1.74 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 65.0% |
| Market btts yes odds | 1.52 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.78 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Elche CF vs Celta Vigo

The model's most likely 1X2 outcome is **Elche CF win** at **37.6%**. Expected goals are 1.59 for Elche CF and 1.41 for Celta Vigo (3.00 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 57.0%; Under 4.5 goals: 81.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 37.6% | 2.66 |
| Draw | 26.3% | 3.80 |
| Celta Vigo win | 36.1% | 2.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elche CF expected goals | 1.59 |
| Celta Vigo expected goals | 1.41 |
| Expected total goals | 3.00 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 57.0% |
| Under 2.5 | 43.0% |
| Over 3.5 | 35.1% |
| Under 3.5 | 64.9% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.16% |
| 2 | 1-2 | 8.40% |
| 3 | 2-1 | 8.00% |
| 4 | 0-1 | 7.34% |
| 5 | 1-0 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 37.6% | 33.5% | 2.93 | +10.0% |
| Draw | 26.3% | 28.1% | 3.40 | -10.5% |
| Celta Vigo win | 36.1% | 38.4% | 2.75 | -0.7% |
| Over 2.5 | 57.0% | 47.7% | 2.12 | +20.9% |
| Under 2.5 | 43.0% | 52.3% | 1.92 | -17.5% |

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
| Market best home last update utc | 2026-10-09T08:07:00Z |
| Market best draw last update utc | 2026-10-09T08:10:27Z |
| Market best away last update utc | 2026-10-09T08:09:58Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Elche |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.11 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.03 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.85 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.51 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 41.6% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 33.9% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 64.8% |
| Raw p btts yes | 60.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.35 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.86 |
| Home probability edge | +4.0% |
| Draw probability edge | -1.8% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +9.3% |
| Under 2.5 probability edge | -9.3% |
| Raw edge prob home | 0.0806 |
| Raw ev home | 0.2185 |
| Raw edge prob draw | -0.0359 |
| Raw ev draw | -0.1662 |
| Raw edge prob away | -0.0447 |
| Raw ev away | -0.0680 |

</details>


---

## 2026-10-11 — Real Betis vs CA Osasuna

The model's most likely 1X2 outcome is **Real Betis win** at **60.4%**. Expected goals are 1.77 for Real Betis and 0.94 for CA Osasuna (2.71 combined). The most likely exact score is 1-0 at 12.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.5%; Under 4.5 goals: 85.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 60.4% | 1.66 |
| Draw | 22.4% | 4.47 |
| CA Osasuna win | 17.2% | 5.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.77 |
| CA Osasuna expected goals | 0.94 |
| Expected total goals | 2.71 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 29.2% |
| Under 3.5 | 70.8% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.36% |
| 2 | 2-0 | 11.09% |
| 3 | 1-1 | 10.64% |
| 4 | 2-1 | 10.41% |
| 5 | 3-0 | 6.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 60.4% | 63.9% | 1.61 | -2.8% |
| Draw | 22.4% | 21.2% | 4.58 | +2.4% |
| CA Osasuna win | 17.2% | 14.9% | 6.40 | +10.4% |
| Over 2.5 | 51.5% | 54.3% | 1.82 | -6.3% |
| Under 2.5 | 48.5% | 45.7% | 2.16 | +4.8% |

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
| Market best home last update utc | 2026-10-09T08:09:54Z |
| Market best draw last update utc | 2026-10-09T08:09:52Z |
| Market best away last update utc | 2026-10-09T08:10:27Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Betis |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 50.2% |
| P btts no | 49.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.48 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.43 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.07 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 56.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 19.6% |
| Raw p over 1 5 | 75.5% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 50.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.48 |
| Reference draw odds | 3.90 |
| Reference away odds | 5.30 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | -3.5% |
| Draw probability edge | +1.2% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | -0.0708 |
| Raw ev home | -0.0848 |
| Raw edge prob draw | 0.0241 |
| Raw ev draw | 0.0794 |
| Raw edge prob away | 0.0468 |
| Raw ev away | 0.2535 |

</details>


---

## 2026-10-11 — Real Racing Club de Santander vs Valencia

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **40.8%**. Expected goals are 1.92 for Real Racing Club de Santander and 1.95 for Valencia (3.87 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 73.7%; Under 4.5 goals: 65.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 40.8% | 2.45 |
| Draw | 23.4% | 4.27 |
| Valencia win | 35.8% | 2.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.92 |
| Valencia expected goals | 1.95 |
| Expected total goals | 3.87 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 90.0% |
| Under 1.5 | 10.0% |
| Over 2.5 | 73.7% |
| Under 2.5 | 26.3% |
| Over 3.5 | 54.1% |
| Under 3.5 | 45.9% |
| Over 4.5 | 34.2% |
| Under 4.5 | 65.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.71% |
| 2 | 2-2 | 8.05% |
| 3 | 2-1 | 7.87% |
| 4 | 1-2 | 6.83% |
| 5 | 3-1 | 5.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 40.8% | 42.6% | 2.42 | -1.3% |
| Draw | 23.4% | 25.6% | 3.71 | -13.0% |
| Valencia win | 35.8% | 31.8% | 3.10 | +10.9% |
| Over 2.5 | 73.7% | 58.4% | 1.76 | +29.6% |
| Under 2.5 | 26.3% | 41.6% | 2.27 | -40.2% |

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
| Market best home last update utc | 2026-10-09T08:07:00Z |
| Market best draw last update utc | 2026-10-09T08:07:00Z |
| Market best away last update utc | 2026-10-09T08:09:56Z |
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
| P btts yes | 73.8% |
| P btts no | 26.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.43 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.96 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.80 |
| Fair Over 3.5 odds | 1.85 |
| Fair Under 3.5 odds | 2.18 |
| Fair Over 4.5 odds | 2.93 |
| Fair Under 4.5 odds | 1.52 |
| Unadjusted home-win probability | 38.9% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 39.8% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 45.9% |
| Raw p btts yes | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.80 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.26 |
| Home probability edge | -1.9% |
| Draw probability edge | -2.2% |
| Away probability edge | +4.0% |
| Over 2.5 probability edge | +15.3% |
| Under 2.5 probability edge | -15.3% |
| Raw edge prob home | -0.0372 |
| Raw ev home | -0.0582 |
| Raw edge prob draw | -0.0430 |
| Raw ev draw | -0.2101 |
| Raw edge prob away | 0.0802 |
| Raw ev away | 0.2335 |

</details>


---

## 2026-10-11 — Real Sociedad vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Real Sociedad win** at **52.4%**. Expected goals are 1.49 for Real Sociedad and 1.20 for Deportivo La Coruña (2.68 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.0%; Under 4.5 goals: 86.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 52.4% | 1.91 |
| Draw | 24.2% | 4.13 |
| Deportivo La Coruña win | 23.4% | 4.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.49 |
| Deportivo La Coruña expected goals | 1.20 |
| Expected total goals | 2.68 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 28.6% |
| Under 3.5 | 71.4% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.97% |
| 2 | 1-1 | 11.51% |
| 3 | 2-1 | 10.84% |
| 4 | 2-0 | 9.04% |
| 5 | 0-0 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 52.4% | 61.1% | 1.69 | -11.5% |
| Draw | 24.2% | 22.5% | 4.22 | +2.2% |
| Deportivo La Coruña win | 23.4% | 16.3% | 5.90 | +38.0% |
| Over 2.5 | 51.0% | 54.5% | 1.84 | -6.1% |
| Under 2.5 | 49.0% | 45.5% | 2.16 | +5.8% |

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
| Market best home last update utc | 2026-10-09T08:07:00Z |
| Market best draw last update utc | 2026-10-09T08:09:52Z |
| Market best away last update utc | 2026-10-09T08:10:27Z |
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
| P btts yes | 53.6% |
| P btts no | 46.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.30 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.24 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 54.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.54 |
| Reference draw odds | 3.70 |
| Reference away odds | 4.90 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | -8.8% |
| Draw probability edge | +1.7% |
| Away probability edge | +7.0% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.1750 |
| Raw ev home | -0.2626 |
| Raw edge prob draw | 0.0342 |
| Raw ev draw | 0.0945 |
| Raw edge prob away | 0.1408 |
| Raw ev away | 0.7953 |

</details>


---

## 2026-10-12 — Levante vs Sevilla

The model's most likely 1X2 outcome is **Levante win** at **39.8%**. Expected goals are 1.61 for Levante and 1.27 for Sevilla (2.88 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.3%; Under 4.5 goals: 83.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 39.8% | 2.51 |
| Draw | 26.5% | 3.78 |
| Sevilla win | 33.7% | 2.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.61 |
| Sevilla expected goals | 1.27 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.3% |
| Under 2.5 | 45.7% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.43% |
| 2 | 1-2 | 8.19% |
| 3 | 2-1 | 8.13% |
| 4 | 0-1 | 7.84% |
| 5 | 1-0 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 39.8% | 34.3% | 2.90 | +15.5% |
| Draw | 26.5% | 28.2% | 3.41 | -9.7% |
| Sevilla win | 33.7% | 37.5% | 2.79 | -6.0% |
| Over 2.5 | 54.3% | 46.8% | 2.12 | +15.0% |
| Under 2.5 | 45.7% | 53.2% | 1.84 | -15.8% |

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
| Market best home last update utc | 2026-10-09T08:10:27Z |
| Market best draw last update utc | 2026-10-09T08:07:00Z |
| Market best away last update utc | 2026-10-09T08:07:00Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.2% |
| P btts no | 41.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.21 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.58 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.18 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 45.4% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 29.9% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 57.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.07 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | +5.5% |
| Draw probability edge | -1.7% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | +7.5% |
| Under 2.5 probability edge | -7.5% |
| Raw edge prob home | 0.1105 |
| Raw ev home | 0.3154 |
| Raw edge prob draw | -0.0339 |
| Raw ev draw | -0.1550 |
| Raw edge prob away | -0.0766 |
| Raw ev away | -0.1669 |

</details>


---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.7%**. Expected goals are 1.84 for Deportivo La Coruña and 1.11 for Levante (2.95 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.9%; Under 4.5 goals: 82.7%.

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
| Over 2.5 | 55.9% | 50.0% | 1.98 | +10.6% |
| Under 2.5 | 44.1% | 50.0% | 1.96 | -13.5% |

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
| Market best home last update utc | 2026-10-09T08:07:00Z |
| Market best draw last update utc | 2026-10-09T08:07:00Z |
| Market best away last update utc | 2026-10-09T08:09:57Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Tipico |
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
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.92 |
| Home probability edge | +3.7% |
| Draw probability edge | -1.7% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +5.9% |
| Under 2.5 probability edge | -5.9% |
| Raw edge prob home | 0.0736 |
| Raw ev home | 0.1801 |
| Raw edge prob draw | -0.0342 |
| Raw ev draw | -0.1650 |
| Raw edge prob away | -0.0394 |
| Raw ev away | -0.1882 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **51.6%**. Expected goals are 1.03 for Espanyol and 1.58 for Atlético Madrid (2.60 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.4%; Under 4.5 goals: 87.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 23.2% | 4.32 |
| Draw | 25.2% | 3.96 |
| Atlético Madrid win | 51.6% | 1.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.03 |
| Atlético Madrid expected goals | 1.58 |
| Expected total goals | 2.60 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 48.4% |
| Under 2.5 | 51.6% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.00% |
| 2 | 0-1 | 11.87% |
| 3 | 1-2 | 9.76% |
| 4 | 0-2 | 9.50% |
| 5 | 0-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 23.2% | 21.8% | 4.50 | +4.3% |
| Draw | 25.2% | 24.9% | 3.85 | -2.9% |
| Atlético Madrid win | 51.6% | 53.2% | 1.91 | -1.4% |
| Over 2.5 | 48.4% | 52.4% | 1.87 | -9.4% |
| Under 2.5 | 51.6% | 47.6% | 2.08 | +7.2% |

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
| Market best home last update utc | 2026-10-09T08:10:27Z |
| Market best draw last update utc | 2026-10-09T08:10:27Z |
| Market best away last update utc | 2026-10-09T08:07:00Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Espanol |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 93/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.38 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.06 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 50.0% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.5% |
| Raw p btts yes | 51.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.24 |
| Reference draw odds | 3.74 |
| Reference away odds | 1.82 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.00 |
| Home probability edge | +1.3% |
| Draw probability edge | +0.3% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | 0.0266 |
| Raw ev home | 0.1025 |
| Raw edge prob draw | 0.0060 |
| Raw ev draw | -0.0173 |
| Raw edge prob away | -0.0325 |
| Raw ev away | -0.0455 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **62.4%**. Expected goals are 1.32 for Real Betis and 2.05 for Barcelona (3.37 combined). The most likely exact score is 1-2 at 11.0%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 67.0%; Under 4.5 goals: 74.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.7% | 5.07 |
| Draw | 17.8% | 5.61 |
| Barcelona win | 62.4% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.32 |
| Barcelona expected goals | 2.05 |
| Expected total goals | 3.37 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 67.0% |
| Under 2.5 | 33.0% |
| Over 3.5 | 44.2% |
| Under 3.5 | 55.8% |
| Over 4.5 | 26.0% |
| Under 4.5 | 74.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.01% |
| 2 | 0-2 | 8.31% |
| 3 | 0-1 | 7.97% |
| 4 | 1-1 | 7.80% |
| 5 | 1-3 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.7% | 15.0% | 6.21 | +22.5% |
| Draw | 17.8% | 14.1% | 6.00 | +7.0% |
| Barcelona win | 62.4% | 70.8% | 1.49 | -7.0% |
| Over 2.5 | 67.0% | 76.4% | 1.28 | -14.3% |
| Under 2.5 | 33.0% | 23.6% | 3.76 | +24.2% |

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
| Market best home last update utc | 2026-10-09T08:07:00Z |
| Market best draw last update utc | 2026-10-09T08:10:27Z |
| Market best away last update utc | 2026-10-09T08:07:00Z |
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
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.96 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.91 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.03 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.84 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 54.0% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 64.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 5.20 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.35 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.76 |
| Home probability edge | +4.7% |
| Draw probability edge | +3.7% |
| Away probability edge | -8.4% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | 0.0937 |
| Raw ev home | 0.5163 |
| Raw edge prob draw | 0.0746 |
| Raw ev draw | 0.2943 |
| Raw edge prob away | -0.1683 |
| Raw ev away | -0.1952 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.4%**. Expected goals are 1.08 for Valencia and 1.17 for Athletic Bilbao (2.25 combined). The most likely exact score is 0-1 at 13.7%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 39.4%; Under 4.5 goals: 92.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.8% | 3.36 |
| Draw | 27.8% | 3.60 |
| Athletic Bilbao win | 42.4% | 2.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.08 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.25 |
| Over 0.5 | 89.7% |
| Under 0.5 | 10.3% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.4% |
| Under 2.5 | 60.6% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.69% |
| 2 | 1-1 | 12.90% |
| 3 | 0-0 | 10.29% |
| 4 | 1-0 | 10.08% |
| 5 | 1-2 | 8.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.8% | 26.5% | 3.70 | +10.2% |
| Draw | 27.8% | 26.5% | 3.58 | -0.5% |
| Athletic Bilbao win | 42.4% | 47.0% | 2.18 | -7.5% |
| Over 2.5 | 39.4% | 47.1% | 2.10 | -17.3% |
| Under 2.5 | 60.6% | 52.9% | 1.86 | +12.7% |

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
| Market best home last update utc | 2026-10-09T08:10:27Z |
| Market best draw last update utc | 2026-10-09T08:07:00Z |
| Market best away last update utc | 2026-10-09T08:07:00Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.3% |
| P btts no | 54.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.72 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.54 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.70 |
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
| Reference draw odds | 3.30 |
| Reference away odds | 1.97 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +3.3% |
| Draw probability edge | +1.3% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.0660 |
| Raw ev home | 0.2243 |
| Raw edge prob draw | 0.0262 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | -0.0923 |
| Raw ev away | -0.1760 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **66.2%**. Expected goals are 2.51 for Villarreal and 1.25 for Elche CF (3.76 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 72.6%; Under 4.5 goals: 67.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 66.2% | 1.51 |
| Draw | 17.9% | 5.59 |
| Elche CF win | 15.9% | 6.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.51 |
| Elche CF expected goals | 1.25 |
| Expected total goals | 3.76 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 89.2% |
| Under 1.5 | 10.8% |
| Over 2.5 | 72.6% |
| Under 2.5 | 27.4% |
| Over 3.5 | 52.1% |
| Under 3.5 | 47.9% |
| Over 4.5 | 32.6% |
| Under 4.5 | 67.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.40% |
| 2 | 3-1 | 7.86% |
| 3 | 2-0 | 7.49% |
| 4 | 1-1 | 7.35% |
| 5 | 3-0 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 66.2% | 67.9% | 1.51 | +0.0% |
| Draw | 17.9% | 17.7% | 5.20 | -7.0% |
| Elche CF win | 15.9% | 14.4% | 6.73 | +6.8% |
| Over 2.5 | 72.6% | 64.3% | 1.51 | +9.7% |
| Under 2.5 | 27.4% | 35.7% | 2.70 | -26.1% |

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
| Market best home last update utc | 2026-10-09T08:07:00Z |
| Market best draw last update utc | 2026-10-09T08:09:57Z |
| Market best away last update utc | 2026-10-09T08:07:00Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
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
| Fair Under 0.5 odds | 41.58 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.22 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.66 |
| Fair Over 3.5 odds | 1.92 |
| Fair Under 3.5 odds | 2.09 |
| Fair Over 4.5 odds | 3.06 |
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
| Reference home odds | 1.40 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Home probability edge | -1.7% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +8.4% |
| Under 2.5 probability edge | -8.4% |
| Raw edge prob home | -0.0331 |
| Raw ev home | -0.0247 |
| Raw edge prob draw | 0.0032 |
| Raw ev draw | -0.0617 |
| Raw edge prob away | 0.0299 |
| Raw ev away | 0.1687 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **57.9%**. Expected goals are 2.71 for CA Osasuna and 1.48 for Real Racing Club de Santander (4.19 combined). The most likely exact score is 2-1 at 7.5%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 77.7%; Under 4.5 goals: 60.3%.

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
| Over 2.5 | 77.7% | 54.9% | 1.81 | +40.7% |
| Under 2.5 | 22.3% | 45.1% | 2.17 | -51.6% |

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
| Market best home last update utc | 2026-10-09T08:07:00Z |
| Market best draw last update utc | 2026-10-09T08:07:00Z |
| Market best away last update utc | 2026-10-09T08:07:00Z |
| Odds bookmakers 1x2 | 14.00 |
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
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | +5.5% |
| Draw probability edge | -3.6% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +22.8% |
| Under 2.5 probability edge | -22.8% |
| Raw edge prob home | 0.1105 |
| Raw ev home | 0.2370 |
| Raw edge prob draw | -0.0717 |
| Raw ev draw | -0.3605 |
| Raw edge prob away | -0.0388 |
| Raw ev away | -0.1712 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **49.3%**. Expected goals are 1.51 for Celta Vigo and 0.96 for Alavés (2.47 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.7%; Under 4.5 goals: 89.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 49.3% | 2.03 |
| Draw | 26.8% | 3.73 |
| Alavés win | 23.9% | 4.18 |

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
| 1 | 1-1 | 12.67% |
| 2 | 1-0 | 12.47% |
| 3 | 2-0 | 9.52% |
| 4 | 2-1 | 9.17% |
| 5 | 0-0 | 8.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 49.3% | 48.8% | 2.08 | +2.4% |
| Draw | 26.8% | 27.3% | 3.58 | -4.1% |
| Alavés win | 23.9% | 23.9% | 3.95 | -5.4% |
| Over 2.5 | 44.7% | 45.1% | 2.19 | -2.2% |
| Under 2.5 | 55.3% | 54.9% | 1.79 | -0.9% |

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
| Market best home last update utc | 2026-10-09T08:07:00Z |
| Market best draw last update utc | 2026-10-09T08:07:00Z |
| Market best away last update utc | 2026-10-09T08:09:54Z |
| Odds bookmakers 1x2 | 14.00 |
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
| Fair Under 0.5 odds | 11.37 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.60 |
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
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.75 |
| Home probability edge | +0.4% |
| Draw probability edge | -0.5% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0086 |
| Raw ev home | 0.0334 |
| Raw edge prob draw | -0.0094 |
| Raw ev draw | -0.0573 |
| Raw edge prob away | 0.0008 |
| Raw ev away | -0.0525 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.5%**. Expected goals are 0.57 for Málaga and 1.26 for Real Sociedad (1.83 combined). The most likely exact score is 0-1 at 18.3%. Goal-market probabilities: at least one goal: 84.8%; Over 2.5 goals: 27.7%; Under 4.5 goals: 96.2%.

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
| Over 2.5 | 27.7% | 53.9% | 1.86 | -48.4% |
| Under 2.5 | 72.3% | 46.1% | 2.10 | +51.8% |

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
| Market best home last update utc | 2026-10-09T08:09:57Z |
| Market best draw last update utc | 2026-10-09T08:07:00Z |
| Market best away last update utc | 2026-10-09T08:07:00Z |
| Odds bookmakers 1x2 | 14.00 |
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
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.06 |
| Home probability edge | -6.6% |
| Draw probability edge | +1.9% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -26.2% |
| Under 2.5 probability edge | +26.2% |
| Raw edge prob home | -0.1329 |
| Raw ev home | -0.4517 |
| Raw edge prob draw | 0.0375 |
| Raw ev draw | 0.0941 |
| Raw edge prob away | 0.0954 |
| Raw ev away | 0.2193 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.9%**. Expected goals are 2.62 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.1%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 65.9%; Under 4.5 goals: 74.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.9% | 1.27 |
| Draw | 13.3% | 7.52 |
| Sevilla win | 7.8% | 12.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.62 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 65.9% |
| Under 2.5 | 34.1% |
| Over 3.5 | 43.7% |
| Under 3.5 | 56.3% |
| Over 4.5 | 25.3% |
| Under 4.5 | 74.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.09% |
| 2 | 3-0 | 10.57% |
| 3 | 1-0 | 9.13% |
| 4 | 2-1 | 9.00% |
| 5 | 3-1 | 7.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 78.9% | 80.3% | 1.30 | +2.5% |
| Draw | 13.3% | 12.1% | 7.80 | +3.7% |
| Sevilla win | 7.8% | 7.5% | 11.50 | -9.7% |
| Over 2.5 | 65.9% | 69.5% | 1.40 | -7.7% |
| Under 2.5 | 34.1% | 30.5% | 3.00 | +2.2% |

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
| Market best home last update utc | 2026-10-09T08:07:00Z |
| Market best draw last update utc | 2026-10-09T08:10:27Z |
| Market best away last update utc | 2026-10-09T08:09:13Z |
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
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.69 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.94 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.96 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.20 |
| Reference draw odds | 5.80 |
| Reference away odds | 8.60 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -1.5% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | -0.0296 |
| Raw ev home | 0.0059 |
| Raw edge prob draw | 0.0236 |
| Raw ev draw | 0.1290 |
| Raw edge prob away | 0.0060 |
| Raw ev away | -0.0629 |

</details>


---
