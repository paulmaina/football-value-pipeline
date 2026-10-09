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

The model's most likely 1X2 outcome is **Espanyol win** at **42.5%**. Expected goals are 0.57 for Málaga and 1.09 for Espanyol (1.66 combined). The most likely exact score is 0-0 at 18.4%. Goal-market probabilities: at least one goal: 81.6%; Over 2.5 goals: 23.2%; Under 4.5 goals: 97.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 25.9% | 3.86 |
| Draw | 31.7% | 3.16 |
| Espanyol win | 42.5% | 2.36 |

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
| Over 2.5 | 23.2% |
| Under 2.5 | 76.8% |
| Over 3.5 | 8.4% |
| Under 3.5 | 91.6% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.36% |
| 2 | 0-1 | 18.25% |
| 3 | 1-0 | 14.57% |
| 4 | 1-1 | 11.43% |
| 5 | 0-2 | 10.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 25.9% | 32.8% | 3.00 | -22.3% |
| Draw | 31.7% | 30.2% | 3.30 | +4.5% |
| Espanyol win | 42.5% | 37.1% | 2.75 | +16.7% |
| Over 2.5 | 23.2% | 46.4% | 2.17 | -49.7% |
| Under 2.5 | 76.8% | 53.6% | 1.86 | +42.9% |

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
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Matchbook |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Malaga |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 93/100 |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.45 |
| Fair Over 1.5 odds | 2.05 |
| Fair Under 1.5 odds | 1.95 |
| Fair Over 2.5 odds | 4.32 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.84 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.61 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 19.0% |
| Unadjusted draw probability | 33.2% |
| Unadjusted away-win probability | 47.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.95 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.62 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.09 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | -6.9% |
| Draw probability edge | +1.5% |
| Away probability edge | +5.4% |
| Over 2.5 probability edge | -23.2% |
| Under 2.5 probability edge | +23.2% |
| Raw edge prob home | -0.1381 |
| Raw ev home | -0.4305 |
| Raw edge prob draw | 0.0301 |
| Raw ev draw | 0.0944 |
| Raw edge prob away | 0.1080 |
| Raw ev away | 0.3159 |

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

</details>


---

## 2026-10-10 — Barcelona vs Getafe

The model's most likely 1X2 outcome is **Barcelona win** at **84.9%**. Expected goals are 2.38 for Barcelona and 0.59 for Getafe (2.97 combined). The most likely exact score is 2-0 at 16.0%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 59.9%; Under 4.5 goals: 80.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 84.9% | 1.18 |
| Draw | 10.0% | 9.99 |
| Getafe win | 5.1% | 19.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.38 |
| Getafe expected goals | 0.59 |
| Expected total goals | 2.97 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 59.9% |
| Under 2.5 | 40.1% |
| Over 3.5 | 36.1% |
| Under 3.5 | 63.9% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 16.02% |
| 2 | 1-0 | 13.36% |
| 3 | 3-0 | 12.70% |
| 4 | 2-1 | 9.42% |
| 5 | 4-0 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 84.9% | 92.7% | 1.10 | -6.6% |
| Draw | 10.0% | 4.5% | 16.00 | +60.1% |
| Getafe win | 5.1% | 2.8% | 38.00 | +92.2% |
| Over 2.5 | 59.9% | 78.3% | 1.25 | -25.2% |
| Under 2.5 | 40.1% | 21.7% | 4.02 | +61.4% |

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
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Barcelona |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.50 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.32 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.21 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 77.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 7.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.07 |
| Reference draw odds | 15.63 |
| Reference away odds | 23.51 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.02 |
| Home probability edge | -7.7% |
| Draw probability edge | +5.5% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -18.4% |
| Under 2.5 probability edge | +18.4% |
| Raw edge prob home | -0.1543 |
| Raw ev home | -0.1506 |
| Raw edge prob draw | 0.1100 |
| Raw ev draw | 1.4810 |
| Raw edge prob away | 0.0443 |
| Raw ev away | 1.7634 |

</details>


---

## 2026-10-10 — Rayo Vallecano vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **36.2%**. Expected goals are 1.01 for Rayo Vallecano and 1.05 for Athletic Bilbao (2.06 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 87.6%; Over 2.5 goals: 34.3%; Under 4.5 goals: 94.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 34.3% | 2.92 |
| Draw | 29.5% | 3.39 |
| Athletic Bilbao win | 36.2% | 2.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.01 |
| Athletic Bilbao expected goals | 1.05 |
| Expected total goals | 2.06 |
| Over 0.5 | 87.6% |
| Under 0.5 | 12.4% |
| Over 1.5 | 61.3% |
| Under 1.5 | 38.7% |
| Over 2.5 | 34.3% |
| Under 2.5 | 65.7% |
| Over 3.5 | 15.5% |
| Under 3.5 | 84.5% |
| Over 4.5 | 5.9% |
| Under 4.5 | 94.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.36% |
| 2 | 1-1 | 13.19% |
| 3 | 1-0 | 12.93% |
| 4 | 0-0 | 12.43% |
| 5 | 1-2 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 34.3% | 35.0% | 2.88 | -1.2% |
| Draw | 29.5% | 28.3% | 3.50 | +3.3% |
| Athletic Bilbao win | 36.2% | 36.6% | 2.72 | -1.5% |
| Over 2.5 | 34.3% | 49.7% | 1.99 | -31.6% |
| Under 2.5 | 65.7% | 50.3% | 1.98 | +30.0% |

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
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.05 |
| Fair Over 1.5 odds | 1.63 |
| Fair Under 1.5 odds | 2.58 |
| Fair Over 2.5 odds | 2.91 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.47 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 16.92 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 30.7% |
| Unadjusted away-win probability | 35.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.77 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.93 |
| Home probability edge | -0.7% |
| Draw probability edge | +1.2% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -15.4% |
| Under 2.5 probability edge | +15.4% |
| Raw edge prob home | -0.0144 |
| Raw ev home | -0.0331 |
| Raw edge prob draw | 0.0232 |
| Raw ev draw | 0.0732 |
| Raw edge prob away | -0.0088 |
| Raw ev away | -0.0272 |

</details>


---

## 2026-10-10 — Real Madrid vs Villarreal

The model's most likely 1X2 outcome is **Real Madrid win** at **69.8%**. Expected goals are 2.56 for Real Madrid and 1.12 for Villarreal (3.68 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 71.5%; Under 4.5 goals: 68.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 69.8% | 1.43 |
| Draw | 16.3% | 6.13 |
| Villarreal win | 13.9% | 7.20 |

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
| Over 2.5 | 71.5% |
| Under 2.5 | 28.5% |
| Over 3.5 | 50.4% |
| Under 3.5 | 49.6% |
| Over 4.5 | 31.2% |
| Under 4.5 | 68.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.48% |
| 2 | 2-0 | 8.43% |
| 3 | 3-1 | 8.08% |
| 4 | 3-0 | 7.18% |
| 5 | 1-1 | 6.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 69.8% | 71.4% | 1.40 | -2.3% |
| Draw | 16.3% | 15.5% | 6.20 | +1.1% |
| Villarreal win | 13.9% | 13.2% | 8.00 | +11.1% |
| Over 2.5 | 71.5% | 75.2% | 1.30 | -7.0% |
| Under 2.5 | 28.5% | 24.8% | 3.60 | +2.6% |

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
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.15 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.64 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.51 |
| Fair Over 3.5 odds | 1.98 |
| Fair Under 3.5 odds | 2.02 |
| Fair Over 4.5 odds | 3.21 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 14.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.38 |
| Reference draw odds | 5.96 |
| Reference away odds | 6.95 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.60 |
| Home probability edge | -1.6% |
| Draw probability edge | +0.9% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | -0.0319 |
| Raw ev home | -0.0452 |
| Raw edge prob draw | 0.0172 |
| Raw ev draw | 0.0649 |
| Raw edge prob away | 0.0147 |
| Raw ev away | 0.1698 |

</details>


---

## 2026-10-11 — Elche CF vs Celta Vigo

The model's most likely 1X2 outcome is **Elche CF win** at **37.9%**. Expected goals are 1.59 for Elche CF and 1.41 for Celta Vigo (3.00 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.9%; Under 4.5 goals: 81.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 37.9% | 2.64 |
| Draw | 26.7% | 3.74 |
| Celta Vigo win | 35.3% | 2.83 |

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
| Over 2.5 | 56.9% |
| Under 2.5 | 43.1% |
| Over 3.5 | 35.1% |
| Under 3.5 | 64.9% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.35% |
| 2 | 1-2 | 8.22% |
| 3 | 2-1 | 8.08% |
| 4 | 0-1 | 7.18% |
| 5 | 1-0 | 7.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 37.9% | 34.2% | 2.93 | +11.1% |
| Draw | 26.7% | 29.0% | 3.40 | -9.1% |
| Celta Vigo win | 35.3% | 36.8% | 2.75 | -2.8% |
| Over 2.5 | 56.9% | 47.7% | 2.12 | +20.6% |
| Under 2.5 | 43.1% | 52.3% | 1.92 | -17.2% |

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
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.82 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.83 |
| Reference draw odds | 3.33 |
| Reference away odds | 2.64 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.86 |
| Home probability edge | +3.7% |
| Draw probability edge | -2.2% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | +9.2% |
| Under 2.5 probability edge | -9.2% |
| Raw edge prob home | 0.0734 |
| Raw ev home | 0.2185 |
| Raw edge prob draw | -0.0444 |
| Raw ev draw | -0.1662 |
| Raw edge prob away | -0.0290 |
| Raw ev away | -0.0680 |

</details>


---

## 2026-10-11 — Real Betis vs CA Osasuna

The model's most likely 1X2 outcome is **Real Betis win** at **60.1%**. Expected goals are 1.77 for Real Betis and 0.94 for CA Osasuna (2.71 combined). The most likely exact score is 1-0 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 51.5%; Under 4.5 goals: 85.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 60.1% | 1.66 |
| Draw | 22.2% | 4.50 |
| CA Osasuna win | 17.7% | 5.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.77 |
| CA Osasuna expected goals | 0.94 |
| Expected total goals | 2.71 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.30% |
| 2 | 2-0 | 11.04% |
| 3 | 1-1 | 10.58% |
| 4 | 2-1 | 10.36% |
| 5 | 3-0 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 60.1% | 63.4% | 1.61 | -3.2% |
| Draw | 22.2% | 20.9% | 4.58 | +1.8% |
| CA Osasuna win | 17.7% | 15.8% | 6.40 | +13.1% |
| Over 2.5 | 51.5% | 53.9% | 1.82 | -6.2% |
| Under 2.5 | 48.5% | 46.1% | 2.16 | +4.7% |

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
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.57 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.43 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.07 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 56.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 19.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.55 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.89 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.06 |
| Home probability edge | -3.3% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | -0.0651 |
| Raw ev home | -0.0848 |
| Raw edge prob draw | 0.0269 |
| Raw ev draw | 0.0794 |
| Raw edge prob away | 0.0381 |
| Raw ev away | 0.2535 |

</details>


---

## 2026-10-11 — Real Racing Club de Santander vs Valencia

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **40.0%**. Expected goals are 1.92 for Real Racing Club de Santander and 1.95 for Valencia (3.87 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 73.5%; Under 4.5 goals: 66.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 40.0% | 2.50 |
| Draw | 24.2% | 4.14 |
| Valencia win | 35.9% | 2.79 |

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
| Over 2.5 | 73.5% |
| Under 2.5 | 26.5% |
| Over 3.5 | 54.0% |
| Under 3.5 | 46.0% |
| Over 4.5 | 34.0% |
| Under 4.5 | 66.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.98% |
| 2 | 2-2 | 8.30% |
| 3 | 2-1 | 7.71% |
| 4 | 1-2 | 6.85% |
| 5 | 3-1 | 4.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 40.0% | 41.0% | 2.44 | -2.5% |
| Draw | 24.2% | 27.0% | 3.71 | -10.4% |
| Valencia win | 35.9% | 31.9% | 3.10 | +11.2% |
| Over 2.5 | 73.5% | 58.4% | 1.76 | +29.3% |
| Under 2.5 | 26.5% | 41.6% | 2.27 | -39.7% |

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
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Valencia |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.20 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.95 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.77 |
| Fair Over 3.5 odds | 1.85 |
| Fair Under 3.5 odds | 2.18 |
| Fair Over 4.5 odds | 2.94 |
| Fair Under 4.5 odds | 1.52 |
| Unadjusted home-win probability | 38.9% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 39.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.37 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.02 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.26 |
| Home probability edge | -1.1% |
| Draw probability edge | -2.9% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | +15.1% |
| Under 2.5 probability edge | -15.1% |
| Raw edge prob home | -0.0211 |
| Raw ev home | -0.0504 |
| Raw edge prob draw | -0.0574 |
| Raw ev draw | -0.2101 |
| Raw edge prob away | 0.0785 |
| Raw ev away | 0.2335 |

</details>


---

## 2026-10-11 — Real Sociedad vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Real Sociedad win** at **52.3%**. Expected goals are 1.49 for Real Sociedad and 1.20 for Deportivo La Coruña (2.68 combined). The most likely exact score is 1-0 at 11.9%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.0%; Under 4.5 goals: 86.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 52.3% | 1.91 |
| Draw | 24.3% | 4.12 |
| Deportivo La Coruña win | 23.5% | 4.26 |

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
| 1 | 1-0 | 11.94% |
| 2 | 1-1 | 11.53% |
| 3 | 2-1 | 10.82% |
| 4 | 2-0 | 9.02% |
| 5 | 0-0 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 52.3% | 60.9% | 1.69 | -11.7% |
| Draw | 24.3% | 22.6% | 4.30 | +4.3% |
| Deportivo La Coruña win | 23.5% | 16.5% | 5.90 | +38.5% |
| Over 2.5 | 51.0% | 54.9% | 1.84 | -6.2% |
| Under 2.5 | 49.0% | 45.1% | 2.16 | +5.8% |

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
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Sociedad |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.29 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.05 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.24 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 30.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.61 |
| Reference draw odds | 4.18 |
| Reference away odds | 5.64 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -8.6% |
| Draw probability edge | +1.7% |
| Away probability edge | +7.0% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.1728 |
| Raw ev home | -0.2626 |
| Raw edge prob draw | 0.0337 |
| Raw ev draw | 0.1153 |
| Raw edge prob away | 0.1391 |
| Raw ev away | 0.7953 |

</details>


---

## 2026-10-12 — Levante vs Sevilla

The model's most likely 1X2 outcome is **Levante win** at **39.9%**. Expected goals are 1.61 for Levante and 1.27 for Sevilla (2.88 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.2%; Under 4.5 goals: 83.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 39.9% | 2.51 |
| Draw | 26.8% | 3.74 |
| Sevilla win | 33.4% | 3.00 |

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
| Over 2.5 | 54.2% |
| Under 2.5 | 45.8% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.56% |
| 2 | 2-1 | 8.13% |
| 3 | 1-2 | 8.12% |
| 4 | 1-0 | 7.82% |
| 5 | 0-1 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 39.9% | 34.3% | 2.88 | +14.8% |
| Draw | 26.8% | 28.8% | 3.41 | -8.7% |
| Sevilla win | 33.4% | 36.9% | 2.85 | -4.9% |
| Over 2.5 | 54.2% | 46.8% | 2.11 | +14.3% |
| Under 2.5 | 45.8% | 53.2% | 1.84 | -15.7% |

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
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.03 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.58 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.20 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 45.4% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 29.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.82 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.63 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.07 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | +5.5% |
| Draw probability edge | -2.0% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | +7.4% |
| Under 2.5 probability edge | -7.4% |
| Raw edge prob home | 0.1102 |
| Raw ev home | 0.3063 |
| Raw edge prob draw | -0.0397 |
| Raw ev draw | -0.1550 |
| Raw edge prob away | -0.0704 |
| Raw ev away | -0.1490 |

</details>


---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.4%**. Expected goals are 1.84 for Deportivo La Coruña and 1.11 for Levante (2.95 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.8%; Under 4.5 goals: 82.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.4% | 1.98 |
| Draw | 25.1% | 3.99 |
| Levante win | 24.6% | 4.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 1.84 |
| Levante expected goals | 1.11 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.8% |
| Under 2.5 | 44.2% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.76% |
| 2 | 2-1 | 9.12% |
| 3 | 1-0 | 8.78% |
| 4 | 2-0 | 8.22% |
| 5 | 1-2 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.4% | 46.4% | 2.17 | +9.3% |
| Draw | 25.1% | 27.0% | 3.62 | -9.3% |
| Levante win | 24.6% | 26.6% | 3.65 | -10.4% |
| Over 2.5 | 55.8% | 50.0% | 1.98 | +10.4% |
| Under 2.5 | 44.2% | 50.0% | 1.96 | -13.3% |

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
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | La Coruna |
| Matched away-team name | Levante |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.14 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.79 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.4% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 22.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.48 |
| Reference away odds | 3.54 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.92 |
| Home probability edge | +4.0% |
| Draw probability edge | -2.0% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +5.8% |
| Under 2.5 probability edge | -5.8% |
| Raw edge prob home | 0.0799 |
| Raw ev home | 0.1801 |
| Raw edge prob draw | -0.0398 |
| Raw ev draw | -0.1650 |
| Raw edge prob away | -0.0401 |
| Raw ev away | -0.1769 |

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

The model's most likely 1X2 outcome is **Barcelona win** at **61.7%**. Expected goals are 1.32 for Real Betis and 2.05 for Barcelona (3.37 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 66.7%; Under 4.5 goals: 74.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.7% | 5.07 |
| Draw | 18.6% | 5.38 |
| Barcelona win | 61.7% | 1.62 |

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
| Over 2.5 | 66.7% |
| Under 2.5 | 33.3% |
| Over 3.5 | 44.2% |
| Under 3.5 | 55.8% |
| Over 4.5 | 25.9% |
| Under 4.5 | 74.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.88% |
| 2 | 0-2 | 8.21% |
| 3 | 1-1 | 8.14% |
| 4 | 0-1 | 7.87% |
| 5 | 1-3 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.7% | 15.1% | 6.21 | +22.6% |
| Draw | 18.6% | 15.6% | 6.00 | +11.6% |
| Barcelona win | 61.7% | 69.3% | 1.49 | -8.1% |
| Over 2.5 | 66.7% | 76.4% | 1.28 | -14.6% |
| Under 2.5 | 33.3% | 23.6% | 3.76 | +25.2% |

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
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.57 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.89 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 3.00 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.86 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 54.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 5.90 |
| Reference draw odds | 5.70 |
| Reference away odds | 1.41 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.76 |
| Home probability edge | +4.7% |
| Draw probability edge | +3.0% |
| Away probability edge | -7.7% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | 0.0936 |
| Raw ev home | 0.5163 |
| Raw edge prob draw | 0.0595 |
| Raw ev draw | 0.2943 |
| Raw edge prob away | -0.1531 |
| Raw ev away | -0.1952 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.1%**. Expected goals are 1.08 for Valencia and 1.17 for Athletic Bilbao (2.25 combined). The most likely exact score is 0-1 at 13.6%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.2%; Under 4.5 goals: 92.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.6% | 3.38 |
| Draw | 28.3% | 3.53 |
| Athletic Bilbao win | 42.1% | 2.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.08 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.25 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.2% |
| Under 2.5 | 60.8% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.58% |
| 2 | 1-1 | 13.14% |
| 3 | 0-0 | 10.48% |
| 4 | 1-0 | 10.01% |
| 5 | 1-2 | 8.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.6% | 26.1% | 3.70 | +9.5% |
| Draw | 28.3% | 27.5% | 3.58 | +1.4% |
| Athletic Bilbao win | 42.1% | 46.4% | 2.18 | -8.2% |
| Over 2.5 | 39.2% | 47.1% | 2.10 | -17.6% |
| Under 2.5 | 60.8% | 52.9% | 1.86 | +13.0% |

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
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.54 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.77 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.1% |
| Unadjusted away-win probability | 37.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.60 |
| Reference draw odds | 3.42 |
| Reference away odds | 2.08 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +3.5% |
| Draw probability edge | +0.8% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -7.9% |
| Under 2.5 probability edge | +7.9% |
| Raw edge prob home | 0.0700 |
| Raw ev home | 0.2243 |
| Raw edge prob draw | 0.0158 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | -0.0858 |
| Raw ev away | -0.1760 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.7%**. Expected goals are 2.51 for Villarreal and 1.25 for Elche CF (3.76 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 72.5%; Under 4.5 goals: 67.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.7% | 1.52 |
| Draw | 18.3% | 5.46 |
| Elche CF win | 16.0% | 6.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.51 |
| Elche CF expected goals | 1.25 |
| Expected total goals | 3.76 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 89.1% |
| Under 1.5 | 10.9% |
| Over 2.5 | 72.5% |
| Under 2.5 | 27.5% |
| Over 3.5 | 52.0% |
| Under 3.5 | 48.0% |
| Over 4.5 | 32.5% |
| Under 4.5 | 67.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.32% |
| 2 | 3-1 | 7.79% |
| 3 | 1-1 | 7.52% |
| 4 | 2-0 | 7.43% |
| 5 | 3-0 | 6.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.7% | 66.8% | 1.51 | -0.8% |
| Draw | 18.3% | 18.6% | 5.20 | -4.8% |
| Elche CF win | 16.0% | 14.7% | 6.73 | +7.8% |
| Over 2.5 | 72.5% | 64.3% | 1.51 | +9.5% |
| Under 2.5 | 27.5% | 35.7% | 2.70 | -25.7% |

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
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.61 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.20 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.63 |
| Fair Over 3.5 odds | 1.92 |
| Fair Under 3.5 odds | 2.08 |
| Fair Over 4.5 odds | 3.07 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 64.6% |
| Unadjusted draw probability | 18.0% |
| Unadjusted away-win probability | 17.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.46 |
| Reference draw odds | 4.84 |
| Reference away odds | 6.04 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Home probability edge | -1.1% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +8.2% |
| Under 2.5 probability edge | -8.2% |
| Raw edge prob home | -0.0217 |
| Raw ev home | -0.0247 |
| Raw edge prob draw | -0.0053 |
| Raw ev draw | -0.0617 |
| Raw edge prob away | 0.0270 |
| Raw ev away | 0.1687 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **57.0%**. Expected goals are 2.71 for CA Osasuna and 1.48 for Real Racing Club de Santander (4.19 combined). The most likely exact score is 1-1 at 8.0%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 77.3%; Under 4.5 goals: 60.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 57.0% | 1.75 |
| Draw | 22.5% | 4.45 |
| Real Racing Club de Santander win | 20.5% | 4.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 2.71 |
| Real Racing Club de Santander expected goals | 1.48 |
| Expected total goals | 4.19 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 77.3% |
| Under 2.5 | 22.7% |
| Over 3.5 | 59.7% |
| Under 3.5 | 40.3% |
| Over 4.5 | 39.4% |
| Under 4.5 | 60.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.97% |
| 2 | 2-2 | 7.89% |
| 3 | 2-1 | 7.40% |
| 4 | 3-1 | 6.68% |
| 5 | 2-0 | 4.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 57.0% | 50.6% | 1.95 | +11.2% |
| Draw | 22.5% | 27.6% | 3.68 | -17.2% |
| Real Racing Club de Santander win | 20.5% | 21.8% | 4.32 | -11.5% |
| Over 2.5 | 77.3% | 54.9% | 1.81 | +39.9% |
| Under 2.5 | 22.7% | 45.1% | 2.17 | -50.7% |

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
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 48.36 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.54 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.40 |
| Fair Over 3.5 odds | 1.67 |
| Fair Under 3.5 odds | 2.48 |
| Fair Over 4.5 odds | 2.54 |
| Fair Under 4.5 odds | 1.65 |
| Unadjusted home-win probability | 63.4% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 19.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.91 |
| Reference draw odds | 3.40 |
| Reference away odds | 4.26 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | +6.4% |
| Draw probability edge | -5.1% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | +22.4% |
| Under 2.5 probability edge | -22.4% |
| Raw edge prob home | 0.1281 |
| Raw ev home | 0.2370 |
| Raw edge prob draw | -0.1022 |
| Raw ev draw | -0.3605 |
| Raw edge prob away | -0.0259 |
| Raw ev away | -0.1712 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **49.0%**. Expected goals are 1.51 for Celta Vigo and 0.96 for Alavés (2.47 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 44.6%; Under 4.5 goals: 89.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 49.0% | 2.04 |
| Draw | 27.0% | 3.71 |
| Alavés win | 24.1% | 4.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.51 |
| Alavés expected goals | 0.96 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 70.7% |
| Under 1.5 | 29.3% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.76% |
| 2 | 1-0 | 12.40% |
| 3 | 2-0 | 9.47% |
| 4 | 2-1 | 9.11% |
| 5 | 0-0 | 8.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 49.0% | 48.3% | 2.08 | +1.9% |
| Draw | 27.0% | 27.6% | 3.58 | -3.4% |
| Alavés win | 24.1% | 24.1% | 3.95 | -5.0% |
| Over 2.5 | 44.6% | 45.1% | 2.19 | -2.4% |
| Under 2.5 | 55.4% | 54.9% | 1.79 | -0.8% |

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
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.29 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.62 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 24.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.00 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.87 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.75 |
| Home probability edge | +0.7% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0142 |
| Raw ev home | 0.0334 |
| Raw edge prob draw | -0.0130 |
| Raw ev draw | -0.0573 |
| Raw edge prob away | -0.0013 |
| Raw ev away | -0.0525 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.5%**. Expected goals are 0.57 for Málaga and 1.26 for Real Sociedad (1.83 combined). The most likely exact score is 0-1 at 18.3%. Goal-market probabilities: at least one goal: 84.6%; Over 2.5 goals: 27.7%; Under 4.5 goals: 96.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 22.9% | 4.36 |
| Draw | 28.6% | 3.50 |
| Real Sociedad win | 48.5% | 2.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.57 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.83 |
| Over 0.5 | 84.6% |
| Under 0.5 | 15.4% |
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
| 1 | 0-1 | 18.29% |
| 2 | 0-0 | 15.39% |
| 3 | 1-0 | 12.39% |
| 4 | 0-2 | 11.61% |
| 5 | 1-1 | 11.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 22.9% | 29.3% | 3.30 | -24.3% |
| Draw | 28.6% | 27.0% | 3.63 | +3.7% |
| Real Sociedad win | 48.5% | 43.8% | 2.29 | +11.1% |
| Over 2.5 | 27.7% | 53.9% | 1.86 | -48.5% |
| Under 2.5 | 72.3% | 46.1% | 2.10 | +51.9% |

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
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.50 |
| Fair Over 1.5 odds | 1.85 |
| Fair Under 1.5 odds | 2.17 |
| Fair Over 2.5 odds | 3.61 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.09 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 26.42 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 16.6% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 53.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.23 |
| Reference draw odds | 3.49 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.06 |
| Home probability edge | -6.3% |
| Draw probability edge | +1.6% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -26.2% |
| Under 2.5 probability edge | +26.2% |
| Raw edge prob home | -0.1264 |
| Raw ev home | -0.4517 |
| Raw edge prob draw | 0.0316 |
| Raw ev draw | 0.0941 |
| Raw edge prob away | 0.0948 |
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
