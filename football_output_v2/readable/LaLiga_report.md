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

The model's most likely 1X2 outcome is **Espanyol win** at **42.6%**. Expected goals are 0.57 for Málaga and 1.09 for Espanyol (1.66 combined). The most likely exact score is 0-0 at 18.3%. Goal-market probabilities: at least one goal: 81.7%; Over 2.5 goals: 23.2%; Under 4.5 goals: 97.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 25.8% | 3.88 |
| Draw | 31.6% | 3.16 |
| Espanyol win | 42.6% | 2.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.57 |
| Espanyol expected goals | 1.09 |
| Expected total goals | 1.66 |
| Over 0.5 | 81.7% |
| Under 0.5 | 18.3% |
| Over 1.5 | 48.8% |
| Under 1.5 | 51.2% |
| Over 2.5 | 23.2% |
| Under 2.5 | 76.8% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.33% |
| 2 | 0-1 | 18.31% |
| 3 | 1-0 | 14.53% |
| 4 | 1-1 | 11.42% |
| 5 | 0-2 | 10.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 25.8% | 32.6% | 3.00 | -22.6% |
| Draw | 31.6% | 30.1% | 3.35 | +5.9% |
| Espanyol win | 42.6% | 37.3% | 2.66 | +13.3% |
| Over 2.5 | 23.2% | 45.6% | 2.10 | -51.3% |
| Under 2.5 | 76.8% | 54.4% | 1.89 | +45.2% |

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
| Market best home last update utc | 2026-10-09T14:37:54Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:32:58Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Malaga |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 93/100 |
| P btts yes | 28.8% |
| P btts no | 71.2% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.46 |
| Fair Over 1.5 odds | 2.05 |
| Fair Under 1.5 odds | 1.95 |
| Fair Over 2.5 odds | 4.31 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.83 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.57 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 19.0% |
| Unadjusted draw probability | 33.2% |
| Unadjusted away-win probability | 47.9% |
| Raw p over 1 5 | 49.5% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 29.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.63 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.07 |
| Reference Under 2.5 odds | 1.76 |
| Home probability edge | -6.8% |
| Draw probability edge | +1.5% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | -22.5% |
| Under 2.5 probability edge | +22.5% |
| Raw edge prob home | -0.1364 |
| Raw ev home | -0.4305 |
| Raw edge prob draw | 0.0310 |
| Raw ev draw | 0.1110 |
| Raw edge prob away | 0.1054 |
| Raw ev away | 0.2729 |
| Market p over 1 5 | 73.9% |
| Market over 1 5 odds | 1.33 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T14:37:23Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.55 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 73.4% |
| Market under 3 5 odds | 1.34 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T14:38:10Z |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.50 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 55.5% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T14:37:54Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.16 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-10 — Alavés vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **50.8%**. Expected goals are 0.99 for Alavés and 1.47 for Atlético Madrid (2.46 combined). The most likely exact score is 0-1 at 13.1%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 44.9%; Under 4.5 goals: 89.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 23.1% | 4.32 |
| Draw | 26.0% | 3.84 |
| Atlético Madrid win | 50.8% | 1.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 0.99 |
| Atlético Madrid expected goals | 1.47 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.9% |
| Under 2.5 | 55.1% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.13% |
| 2 | 1-1 | 12.32% |
| 3 | 0-2 | 9.76% |
| 4 | 1-2 | 9.68% |
| 5 | 0-0 | 8.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 23.1% | 20.9% | 4.70 | +8.7% |
| Draw | 26.0% | 25.4% | 3.95 | +2.9% |
| Atlético Madrid win | 50.8% | 53.8% | 1.87 | -5.0% |
| Over 2.5 | 44.9% | 53.7% | 1.92 | -13.9% |
| Under 2.5 | 55.1% | 46.3% | 2.06 | +13.6% |

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
| Market best home last update utc | 2026-10-09T14:37:54Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:38:10Z |
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
| Fair Under 0.5 odds | 11.73 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.57 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 25.4% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 47.9% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 48.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 4.60 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.83 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.04 |
| Home probability edge | +2.3% |
| Draw probability edge | +0.7% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | 0.0455 |
| Raw ev home | 0.1942 |
| Raw edge prob draw | 0.0131 |
| Raw ev draw | 0.0545 |
| Raw edge prob away | -0.0586 |
| Raw ev away | -0.1043 |

</details>


---

## 2026-10-10 — Barcelona vs Getafe

The model's most likely 1X2 outcome is **Barcelona win** at **84.6%**. Expected goals are 2.38 for Barcelona and 0.59 for Getafe (2.97 combined). The most likely exact score is 2-0 at 15.9%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 59.6%; Under 4.5 goals: 80.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 84.6% | 1.18 |
| Draw | 10.5% | 9.49 |
| Getafe win | 4.9% | 20.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.38 |
| Getafe expected goals | 0.59 |
| Expected total goals | 2.97 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 59.6% |
| Under 2.5 | 40.4% |
| Over 3.5 | 36.1% |
| Under 3.5 | 63.9% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 15.95% |
| 2 | 1-0 | 13.30% |
| 3 | 3-0 | 12.64% |
| 4 | 2-1 | 9.38% |
| 5 | 4-0 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 84.6% | 91.9% | 1.11 | -6.1% |
| Draw | 10.5% | 5.6% | 15.00 | +58.1% |
| Getafe win | 4.9% | 2.5% | 32.00 | +56.5% |
| Over 2.5 | 59.6% | 76.7% | 1.28 | -23.7% |
| Under 2.5 | 40.4% | 23.3% | 3.80 | +53.4% |

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
| Market best home last update utc | 2026-10-09T14:37:54Z |
| Market best draw last update utc | 2026-10-09T14:37:23Z |
| Market best away last update utc | 2026-10-09T14:32:58Z |
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
| P btts yes | 38.7% |
| P btts no | 61.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.01 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.31 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.48 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 77.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 7.3% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.5% |
| Raw p btts yes | 40.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.08 |
| Reference draw odds | 14.00 |
| Reference away odds | 29.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.70 |
| Home probability edge | -7.4% |
| Draw probability edge | +5.0% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -17.0% |
| Under 2.5 probability edge | +17.0% |
| Raw edge prob home | -0.1470 |
| Raw ev home | -0.1428 |
| Raw edge prob draw | 0.0994 |
| Raw ev draw | 1.3259 |
| Raw edge prob away | 0.0476 |
| Raw ev away | 1.3271 |

</details>


---

## 2026-10-10 — Rayo Vallecano vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **36.3%**. Expected goals are 1.01 for Rayo Vallecano and 1.05 for Athletic Bilbao (2.06 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 87.5%; Over 2.5 goals: 34.3%; Under 4.5 goals: 94.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 34.0% | 2.94 |
| Draw | 29.7% | 3.37 |
| Athletic Bilbao win | 36.3% | 2.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.01 |
| Athletic Bilbao expected goals | 1.05 |
| Expected total goals | 2.06 |
| Over 0.5 | 87.5% |
| Under 0.5 | 12.5% |
| Over 1.5 | 61.3% |
| Under 1.5 | 38.7% |
| Over 2.5 | 34.3% |
| Under 2.5 | 65.7% |
| Over 3.5 | 15.4% |
| Under 3.5 | 84.6% |
| Over 4.5 | 5.9% |
| Under 4.5 | 94.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.39% |
| 2 | 1-1 | 13.26% |
| 3 | 1-0 | 12.83% |
| 4 | 0-0 | 12.50% |
| 5 | 1-2 | 7.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 34.0% | 34.5% | 2.88 | -2.0% |
| Draw | 29.7% | 28.7% | 3.50 | +3.8% |
| Athletic Bilbao win | 36.3% | 36.8% | 2.72 | -1.3% |
| Over 2.5 | 34.3% | 50.0% | 1.99 | -31.7% |
| Under 2.5 | 65.7% | 50.0% | 1.98 | +30.1% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:37:54Z |
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
| P btts yes | 41.3% |
| P btts no | 58.7% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.00 |
| Fair Over 1.5 odds | 1.63 |
| Fair Under 1.5 odds | 2.58 |
| Fair Over 2.5 odds | 2.92 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.47 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 16.94 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 30.7% |
| Unadjusted away-win probability | 35.8% |
| Raw p over 1 5 | 61.2% |
| Raw p under 3 5 | 84.6% |
| Raw p btts yes | 41.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.63 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.89 |
| Home probability edge | -0.5% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -15.7% |
| Under 2.5 probability edge | +15.7% |
| Raw edge prob home | -0.0094 |
| Raw ev home | -0.0331 |
| Raw edge prob draw | 0.0199 |
| Raw ev draw | 0.0732 |
| Raw edge prob away | -0.0105 |
| Raw ev away | -0.0272 |

</details>


---

## 2026-10-10 — Real Madrid vs Villarreal

The model's most likely 1X2 outcome is **Real Madrid win** at **70.8%**. Expected goals are 2.56 for Real Madrid and 1.12 for Villarreal (3.68 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 71.7%; Under 4.5 goals: 68.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 70.8% | 1.41 |
| Draw | 15.9% | 6.31 |
| Villarreal win | 13.3% | 7.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.56 |
| Villarreal expected goals | 1.12 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 88.5% |
| Under 1.5 | 11.5% |
| Over 2.5 | 71.7% |
| Under 2.5 | 28.3% |
| Over 3.5 | 50.6% |
| Under 3.5 | 49.4% |
| Over 4.5 | 31.4% |
| Under 4.5 | 68.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.62% |
| 2 | 2-0 | 8.55% |
| 3 | 3-1 | 8.20% |
| 4 | 3-0 | 7.29% |
| 5 | 1-1 | 6.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 70.8% | 73.5% | 1.40 | -0.8% |
| Draw | 15.9% | 14.5% | 6.40 | +1.4% |
| Villarreal win | 13.3% | 12.0% | 8.00 | +6.4% |
| Over 2.5 | 71.7% | 75.4% | 1.30 | -6.8% |
| Under 2.5 | 28.3% | 24.6% | 3.60 | +1.8% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:37:23Z |
| Market best away last update utc | 2026-10-09T14:37:23Z |
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
| P btts yes | 61.9% |
| P btts no | 38.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.32 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.70 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.54 |
| Fair Over 3.5 odds | 1.98 |
| Fair Under 3.5 odds | 2.02 |
| Fair Over 4.5 odds | 3.19 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 14.6% |
| Raw p over 1 5 | 88.3% |
| Raw p under 3 5 | 49.8% |
| Raw p btts yes | 62.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.34 |
| Reference draw odds | 6.25 |
| Reference away odds | 7.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.55 |
| Home probability edge | -2.6% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | -0.0528 |
| Raw ev home | -0.0452 |
| Raw edge prob draw | 0.0265 |
| Raw ev draw | 0.0992 |
| Raw edge prob away | 0.0263 |
| Raw ev away | 0.1698 |

</details>


---

## 2026-10-11 — Elche CF vs Celta Vigo

The model's most likely 1X2 outcome is **Elche CF win** at **37.6%**. Expected goals are 1.59 for Elche CF and 1.41 for Celta Vigo (3.00 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 56.8%; Under 4.5 goals: 81.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 37.6% | 2.66 |
| Draw | 27.0% | 3.70 |
| Celta Vigo win | 35.4% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elche CF expected goals | 1.59 |
| Celta Vigo expected goals | 1.41 |
| Expected total goals | 3.00 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
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
| 1 | 1-1 | 12.47% |
| 2 | 1-2 | 8.23% |
| 3 | 2-1 | 8.02% |
| 4 | 0-1 | 7.19% |
| 5 | 1-0 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 37.6% | 33.6% | 2.93 | +10.2% |
| Draw | 27.0% | 29.5% | 3.35 | -9.6% |
| Celta Vigo win | 35.4% | 36.9% | 2.75 | -2.7% |
| Over 2.5 | 56.8% | 46.0% | 2.12 | +20.4% |
| Under 2.5 | 43.2% | 54.0% | 1.93 | -16.6% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:37:56Z |
| Market best away last update utc | 2026-10-09T14:38:10Z |
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
| P btts yes | 61.0% |
| P btts no | 39.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.66 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.03 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 2.85 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.54 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 41.6% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 33.9% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 64.8% |
| Raw p btts yes | 60.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.77 |
| Home probability edge | +4.0% |
| Draw probability edge | -2.5% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | +10.8% |
| Under 2.5 probability edge | -10.8% |
| Raw edge prob home | 0.0795 |
| Raw ev home | 0.2185 |
| Raw edge prob draw | -0.0495 |
| Raw ev draw | -0.1785 |
| Raw edge prob away | -0.0300 |
| Raw ev away | -0.0680 |

</details>


---

## 2026-10-11 — Real Betis vs CA Osasuna

The model's most likely 1X2 outcome is **Real Betis win** at **59.8%**. Expected goals are 1.77 for Real Betis and 0.94 for CA Osasuna (2.71 combined). The most likely exact score is 1-0 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.4%; Under 4.5 goals: 85.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 59.8% | 1.67 |
| Draw | 22.6% | 4.42 |
| CA Osasuna win | 17.5% | 5.70 |

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
| Over 2.5 | 51.4% |
| Under 2.5 | 48.6% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.24% |
| 2 | 2-0 | 10.99% |
| 3 | 1-1 | 10.77% |
| 4 | 2-1 | 10.31% |
| 5 | 0-0 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 59.8% | 62.8% | 1.60 | -4.3% |
| Draw | 22.6% | 21.7% | 4.62 | +4.6% |
| CA Osasuna win | 17.5% | 15.5% | 6.60 | +15.8% |
| Over 2.5 | 51.4% | 56.4% | 1.81 | -7.0% |
| Under 2.5 | 48.6% | 43.6% | 2.18 | +6.0% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:37:54Z |
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
| Fair Under 0.5 odds | 15.29 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.10 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 56.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 19.6% |
| Raw p over 1 5 | 75.5% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 50.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.57 |
| Reference draw odds | 4.40 |
| Reference away odds | 6.10 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | -3.0% |
| Draw probability edge | +0.9% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | -0.0596 |
| Raw ev home | -0.0904 |
| Raw edge prob draw | 0.0187 |
| Raw ev draw | 0.0888 |
| Raw edge prob away | 0.0409 |
| Raw ev away | 0.2927 |

</details>


---

## 2026-10-11 — Real Racing Club de Santander vs Valencia

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **40.5%**. Expected goals are 1.92 for Real Racing Club de Santander and 1.95 for Valencia (3.87 combined). The most likely exact score is 1-1 at 8.9%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 73.5%; Under 4.5 goals: 65.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 40.5% | 2.47 |
| Draw | 23.9% | 4.18 |
| Valencia win | 35.6% | 2.81 |

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
| Over 3.5 | 54.1% |
| Under 3.5 | 45.9% |
| Over 4.5 | 34.1% |
| Under 4.5 | 65.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.89% |
| 2 | 2-2 | 8.21% |
| 3 | 2-1 | 7.81% |
| 4 | 1-2 | 6.79% |
| 5 | 3-1 | 5.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 40.5% | 42.1% | 2.42 | -2.0% |
| Draw | 23.9% | 26.6% | 3.71 | -11.2% |
| Valencia win | 35.6% | 31.4% | 3.10 | +10.3% |
| Over 2.5 | 73.5% | 56.1% | 1.76 | +29.4% |
| Under 2.5 | 26.5% | 43.9% | 2.27 | -39.9% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:32:58Z |
| Market best away last update utc | 2026-10-09T14:37:23Z |
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
| Fair Under 0.5 odds | 40.60 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.95 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.78 |
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
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.33 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -1.6% |
| Draw probability edge | -2.6% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | +17.4% |
| Under 2.5 probability edge | -17.4% |
| Raw edge prob home | -0.0314 |
| Raw ev home | -0.0582 |
| Raw edge prob draw | -0.0526 |
| Raw ev draw | -0.2101 |
| Raw edge prob away | 0.0840 |
| Raw ev away | 0.2335 |
| Market p over 1 5 | 78.9% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T14:38:10Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 4.35 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 66.7% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T14:37:54Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.4% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T14:37:54Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.54 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Real Sociedad vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Real Sociedad win** at **51.5%**. Expected goals are 1.49 for Real Sociedad and 1.20 for Deportivo La Coruña (2.68 combined). The most likely exact score is 1-0 at 11.8%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 50.9%; Under 4.5 goals: 86.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 51.5% | 1.94 |
| Draw | 24.5% | 4.09 |
| Deportivo La Coruña win | 24.0% | 4.16 |

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
| 1 | 1-0 | 11.77% |
| 2 | 1-1 | 11.63% |
| 3 | 2-1 | 10.66% |
| 4 | 2-0 | 8.89% |
| 5 | 0-0 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 51.5% | 59.4% | 1.66 | -14.5% |
| Draw | 24.5% | 23.0% | 4.22 | +3.3% |
| Deportivo La Coruña win | 24.0% | 17.6% | 6.00 | +44.1% |
| Over 2.5 | 50.9% | 54.6% | 1.81 | -7.8% |
| Under 2.5 | 49.1% | 45.4% | 2.24 | +10.0% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:38:10Z |
| Market best away last update utc | 2026-10-09T14:37:54Z |
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
| Fair Under 0.5 odds | 15.15 |
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
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.65 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.30 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | -7.9% |
| Draw probability edge | +1.5% |
| Away probability edge | +6.4% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | -0.1573 |
| Raw ev home | -0.2757 |
| Raw edge prob draw | 0.0292 |
| Raw ev draw | 0.0945 |
| Raw edge prob away | 0.1281 |
| Raw ev away | 0.8257 |

</details>


---

## 2026-10-12 — Levante vs Sevilla

The model's most likely 1X2 outcome is **Levante win** at **40.4%**. Expected goals are 1.61 for Levante and 1.27 for Sevilla (2.88 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 54.1%; Under 4.5 goals: 83.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 40.4% | 2.47 |
| Draw | 26.9% | 3.72 |
| Sevilla win | 32.7% | 3.06 |

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
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.62% |
| 2 | 2-1 | 8.25% |
| 3 | 1-2 | 7.95% |
| 4 | 1-0 | 7.93% |
| 5 | 0-1 | 7.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 40.4% | 35.5% | 2.92 | +18.1% |
| Draw | 26.9% | 29.0% | 3.43 | -7.8% |
| Sevilla win | 32.7% | 35.5% | 2.75 | -10.1% |
| Over 2.5 | 54.1% | 44.8% | 2.10 | +13.7% |
| Under 2.5 | 45.9% | 55.2% | 1.86 | -14.7% |

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
| Market best home last update utc | 2026-10-09T14:37:54Z |
| Market best draw last update utc | 2026-10-09T14:32:58Z |
| Market best away last update utc | 2026-10-09T14:37:23Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
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
| Fair Under 0.5 odds | 15.96 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.59 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.20 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 45.4% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 29.9% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 57.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.75 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.75 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.73 |
| Home probability edge | +4.9% |
| Draw probability edge | -2.1% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | +9.4% |
| Under 2.5 probability edge | -9.4% |
| Raw edge prob home | 0.0986 |
| Raw ev home | 0.3245 |
| Raw edge prob draw | -0.0422 |
| Raw ev draw | -0.1500 |
| Raw edge prob away | -0.0564 |
| Raw ev away | -0.1788 |

</details>


---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.6%**. Expected goals are 1.84 for Deportivo La Coruña and 1.11 for Levante (2.95 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.8%; Under 4.5 goals: 82.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.6% | 1.98 |
| Draw | 24.9% | 4.01 |
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
| Over 2.5 | 55.8% |
| Under 2.5 | 44.2% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.71% |
| 2 | 2-1 | 9.15% |
| 3 | 1-0 | 8.81% |
| 4 | 2-0 | 8.25% |
| 5 | 1-2 | 6.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.6% | 46.7% | 2.17 | +9.7% |
| Draw | 24.9% | 26.8% | 3.62 | -9.7% |
| Levante win | 24.5% | 26.4% | 3.60 | -11.8% |
| Over 2.5 | 55.8% | 51.2% | 1.98 | +10.5% |
| Under 2.5 | 44.2% | 48.8% | 1.96 | -13.4% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:32:58Z |
| Market best away last update utc | 2026-10-09T14:32:58Z |
| Odds bookmakers 1x2 | 13.00 |
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
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.21 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.78 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.4% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 79.5% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.08 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.93 |
| Home probability edge | +3.8% |
| Draw probability edge | -1.9% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +4.7% |
| Under 2.5 probability edge | -4.7% |
| Raw edge prob home | 0.0765 |
| Raw ev home | 0.1801 |
| Raw edge prob draw | -0.0376 |
| Raw ev draw | -0.1650 |
| Raw edge prob away | -0.0389 |
| Raw ev away | -0.1882 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **51.0%**. Expected goals are 1.03 for Espanyol and 1.58 for Atlético Madrid (2.60 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.3%; Under 4.5 goals: 87.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 23.5% | 4.25 |
| Draw | 25.5% | 3.93 |
| Atlético Madrid win | 51.0% | 1.96 |

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
| Over 2.5 | 48.3% |
| Under 2.5 | 51.7% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.12% |
| 2 | 0-1 | 11.73% |
| 3 | 1-2 | 9.64% |
| 4 | 0-2 | 9.39% |
| 5 | 0-0 | 7.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 23.5% | 22.6% | 4.40 | +3.6% |
| Draw | 25.5% | 25.4% | 3.85 | -1.9% |
| Atlético Madrid win | 51.0% | 52.0% | 1.91 | -2.6% |
| Over 2.5 | 48.3% | 53.8% | 1.87 | -9.6% |
| Under 2.5 | 51.7% | 46.2% | 2.08 | +7.4% |

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
| Market best home last update utc | 2026-10-09T14:37:36Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:32:58Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Espanol |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 93/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.26 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.09 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 50.0% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.5% |
| Raw p btts yes | 51.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 4.20 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.88 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.04 |
| Home probability edge | +0.9% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | 0.0190 |
| Raw ev home | 0.0780 |
| Raw edge prob draw | 0.0011 |
| Raw ev draw | -0.0173 |
| Raw edge prob away | -0.0201 |
| Raw ev away | -0.0455 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **60.8%**. Expected goals are 1.32 for Real Betis and 2.05 for Barcelona (3.37 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 66.5%; Under 4.5 goals: 74.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 20.1% | 4.98 |
| Draw | 19.1% | 5.23 |
| Barcelona win | 60.8% | 1.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.32 |
| Barcelona expected goals | 2.05 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 66.5% |
| Under 2.5 | 33.5% |
| Over 3.5 | 44.1% |
| Under 3.5 | 55.9% |
| Over 4.5 | 25.8% |
| Under 4.5 | 74.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.73% |
| 2 | 1-1 | 8.36% |
| 3 | 0-2 | 8.10% |
| 4 | 0-1 | 7.76% |
| 5 | 1-3 | 7.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 20.1% | 15.7% | 6.21 | +24.6% |
| Draw | 19.1% | 16.6% | 5.90 | +12.7% |
| Barcelona win | 60.8% | 67.6% | 1.49 | -9.4% |
| Over 2.5 | 66.5% | 76.7% | 1.28 | -14.8% |
| Under 2.5 | 33.5% | 23.3% | 3.76 | +25.9% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:37:56Z |
| Market best away last update utc | 2026-10-09T14:32:58Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
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
| Fair Under 0.5 odds | 31.71 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.88 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 2.99 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.88 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 54.0% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 64.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 5.80 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.45 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.70 |
| Home probability edge | +4.3% |
| Draw probability edge | +2.5% |
| Away probability edge | -6.8% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | 0.0869 |
| Raw ev home | 0.5163 |
| Raw edge prob draw | 0.0494 |
| Raw ev draw | 0.2728 |
| Raw edge prob away | -0.1363 |
| Raw ev away | -0.1952 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.5%**. Expected goals are 1.08 for Valencia and 1.17 for Athletic Bilbao (2.25 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 39.1%; Under 4.5 goals: 92.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.8% | 3.35 |
| Draw | 28.6% | 3.49 |
| Athletic Bilbao win | 41.5% | 2.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.08 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.25 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.40% |
| 2 | 1-1 | 13.29% |
| 3 | 0-0 | 10.60% |
| 4 | 1-0 | 10.09% |
| 5 | 1-2 | 8.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.8% | 26.6% | 3.71 | +10.6% |
| Draw | 28.6% | 28.2% | 3.58 | +2.5% |
| Athletic Bilbao win | 41.5% | 45.3% | 2.18 | -9.4% |
| Over 2.5 | 39.1% | 46.6% | 2.10 | -17.8% |
| Under 2.5 | 60.9% | 53.4% | 1.86 | +13.2% |

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
| Market best home last update utc | 2026-10-09T14:37:54Z |
| Market best draw last update utc | 2026-10-09T14:32:58Z |
| Market best away last update utc | 2026-10-09T14:32:58Z |
| Odds bookmakers 1x2 | 14.00 |
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
| P btts yes | 45.5% |
| P btts no | 54.5% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.43 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.26 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.81 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.1% |
| Unadjusted away-win probability | 37.8% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 45.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.60 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.78 |
| Home probability edge | +3.3% |
| Draw probability edge | +0.5% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | 0.0654 |
| Raw ev home | 0.2277 |
| Raw edge prob draw | 0.0094 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | -0.0747 |
| Raw ev away | -0.1760 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.8%**. Expected goals are 2.51 for Villarreal and 1.25 for Elche CF (3.76 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 72.5%; Under 4.5 goals: 67.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.8% | 1.52 |
| Draw | 18.4% | 5.45 |
| Elche CF win | 15.9% | 6.29 |

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
| 1 | 2-1 | 9.33% |
| 2 | 3-1 | 7.80% |
| 3 | 1-1 | 7.54% |
| 4 | 2-0 | 7.44% |
| 5 | 3-0 | 6.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.8% | 66.9% | 1.51 | -0.7% |
| Draw | 18.4% | 18.7% | 5.00 | -8.2% |
| Elche CF win | 15.9% | 14.4% | 6.73 | +7.0% |
| Over 2.5 | 72.5% | 64.6% | 1.51 | +9.4% |
| Under 2.5 | 27.5% | 35.4% | 2.70 | -25.7% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:38:13Z |
| Market best away last update utc | 2026-10-09T14:32:58Z |
| Odds bookmakers 1x2 | 14.00 |
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
| P btts yes | 65.7% |
| P btts no | 34.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.52 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.20 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.63 |
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
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.47 |
| Reference draw odds | 5.00 |
| Reference away odds | 6.40 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Home probability edge | -1.2% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +7.9% |
| Under 2.5 probability edge | -7.9% |
| Raw edge prob home | -0.0232 |
| Raw ev home | -0.0247 |
| Raw edge prob draw | -0.0062 |
| Raw ev draw | -0.0978 |
| Raw edge prob away | 0.0294 |
| Raw ev away | 0.1687 |
| Market p over 1 5 | 90.1% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T14:37:23Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 5.45 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 57.4% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T14:37:52Z |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.22 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-09T14:32:58Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **56.9%**. Expected goals are 2.71 for CA Osasuna and 1.48 for Real Racing Club de Santander (4.19 combined). The most likely exact score is 1-1 at 7.8%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 77.4%; Under 4.5 goals: 60.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 56.9% | 1.76 |
| Draw | 22.0% | 4.54 |
| Real Racing Club de Santander win | 21.1% | 4.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 2.71 |
| Real Racing Club de Santander expected goals | 1.48 |
| Expected total goals | 4.19 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 77.4% |
| Under 2.5 | 22.6% |
| Over 3.5 | 59.7% |
| Under 3.5 | 40.3% |
| Over 4.5 | 39.5% |
| Under 4.5 | 60.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.81% |
| 2 | 2-2 | 7.73% |
| 3 | 2-1 | 7.38% |
| 4 | 3-1 | 6.67% |
| 5 | 2-0 | 4.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 56.9% | 50.4% | 1.95 | +11.0% |
| Draw | 22.0% | 26.7% | 3.68 | -18.9% |
| Real Racing Club de Santander win | 21.1% | 23.0% | 4.32 | -9.0% |
| Over 2.5 | 77.4% | 54.4% | 1.81 | +40.1% |
| Under 2.5 | 22.6% | 45.6% | 2.17 | -51.0% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:32:58Z |
| Market best away last update utc | 2026-10-09T14:32:58Z |
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
| P btts yes | 73.5% |
| P btts no | 26.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 49.37 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.51 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.42 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.48 |
| Fair Over 4.5 odds | 2.53 |
| Fair Under 4.5 odds | 1.65 |
| Unadjusted home-win probability | 63.4% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 19.2% |
| Raw p over 1 5 | 92.2% |
| Raw p under 3 5 | 39.7% |
| Raw p btts yes | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.93 |
| Reference draw odds | 3.55 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.06 |
| Home probability edge | +6.5% |
| Draw probability edge | -4.6% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +23.0% |
| Under 2.5 probability edge | -23.0% |
| Raw edge prob home | 0.1307 |
| Raw ev home | 0.2370 |
| Raw edge prob draw | -0.0930 |
| Raw ev draw | -0.3605 |
| Raw edge prob away | -0.0377 |
| Raw ev away | -0.1712 |
| Market p over 1 5 | 79.8% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T14:37:23Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.84 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 67.3% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T14:37:54Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.64 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T14:37:23Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.15 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **48.7%**. Expected goals are 1.51 for Celta Vigo and 0.96 for Alavés (2.47 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 44.5%; Under 4.5 goals: 89.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 48.7% | 2.05 |
| Draw | 27.2% | 3.67 |
| Alavés win | 24.0% | 4.16 |

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
| Over 2.5 | 44.5% |
| Under 2.5 | 55.5% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.88% |
| 2 | 1-0 | 12.34% |
| 3 | 2-0 | 9.42% |
| 4 | 2-1 | 9.07% |
| 5 | 0-0 | 8.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 48.7% | 47.8% | 2.08 | +1.4% |
| Draw | 27.2% | 28.1% | 3.58 | -2.5% |
| Alavés win | 24.0% | 24.1% | 3.95 | -5.0% |
| Over 2.5 | 44.5% | 43.8% | 2.19 | -2.6% |
| Under 2.5 | 55.5% | 56.2% | 1.79 | -0.6% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:32:58Z |
| Market best away last update utc | 2026-10-09T14:38:13Z |
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
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.19 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.64 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 70.8% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.04 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.95 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.14 |
| Reference Under 2.5 odds | 1.70 |
| Home probability edge | +1.0% |
| Draw probability edge | -0.9% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0191 |
| Raw ev home | 0.0334 |
| Raw edge prob draw | -0.0181 |
| Raw ev draw | -0.0573 |
| Raw edge prob away | -0.0010 |
| Raw ev away | -0.0525 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.4%**. Expected goals are 0.57 for Málaga and 1.26 for Real Sociedad (1.83 combined). The most likely exact score is 0-1 at 18.3%. Goal-market probabilities: at least one goal: 84.5%; Over 2.5 goals: 27.6%; Under 4.5 goals: 96.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 22.8% | 4.38 |
| Draw | 28.7% | 3.48 |
| Real Sociedad win | 48.4% | 2.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.57 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.83 |
| Over 0.5 | 84.5% |
| Under 0.5 | 15.5% |
| Over 1.5 | 53.9% |
| Under 1.5 | 46.1% |
| Over 2.5 | 27.6% |
| Under 2.5 | 72.4% |
| Over 3.5 | 11.0% |
| Under 3.5 | 89.0% |
| Over 4.5 | 3.8% |
| Under 4.5 | 96.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.26% |
| 2 | 0-0 | 15.48% |
| 3 | 1-0 | 12.34% |
| 4 | 0-2 | 11.59% |
| 5 | 1-1 | 11.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 22.8% | 29.1% | 3.30 | -24.6% |
| Draw | 28.7% | 27.3% | 3.63 | +4.3% |
| Real Sociedad win | 48.4% | 43.6% | 2.29 | +10.9% |
| Over 2.5 | 27.6% | 54.1% | 1.86 | -48.6% |
| Under 2.5 | 72.4% | 45.9% | 2.10 | +52.0% |

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
| Market best home last update utc | 2026-10-09T14:37:36Z |
| Market best draw last update utc | 2026-10-09T14:32:58Z |
| Market best away last update utc | 2026-10-09T14:32:58Z |
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
| P btts yes | 31.1% |
| P btts no | 68.9% |
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.46 |
| Fair Over 1.5 odds | 1.85 |
| Fair Under 1.5 odds | 2.17 |
| Fair Over 2.5 odds | 3.62 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.10 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 26.47 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 16.6% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 53.2% |
| Raw p over 1 5 | 54.7% |
| Raw p under 3 5 | 88.7% |
| Raw p btts yes | 31.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.23 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | -6.2% |
| Draw probability edge | +1.4% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -26.5% |
| Under 2.5 probability edge | +26.5% |
| Raw edge prob home | -0.1244 |
| Raw ev home | -0.4517 |
| Raw edge prob draw | 0.0280 |
| Raw ev draw | 0.0941 |
| Raw edge prob away | 0.0965 |
| Raw ev away | 0.2193 |
| Market p over 1 5 | 77.8% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T14:37:23Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 68.8% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T14:38:25Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.91 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 58.9% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T14:37:23Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.25 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.5%**. Expected goals are 2.62 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 65.8%; Under 4.5 goals: 74.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.5% | 1.27 |
| Draw | 13.6% | 7.34 |
| Sevilla win | 7.9% | 12.73 |

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
| Over 2.5 | 65.8% |
| Under 2.5 | 34.2% |
| Over 3.5 | 43.7% |
| Under 3.5 | 56.3% |
| Over 4.5 | 25.2% |
| Under 4.5 | 74.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.04% |
| 2 | 3-0 | 10.52% |
| 3 | 1-0 | 9.09% |
| 4 | 2-1 | 8.96% |
| 5 | 3-1 | 7.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 78.5% | 79.7% | 1.30 | +2.1% |
| Draw | 13.6% | 12.8% | 7.20 | -1.9% |
| Sevilla win | 7.9% | 7.6% | 11.50 | -9.7% |
| Over 2.5 | 65.8% | 69.6% | 1.40 | -7.9% |
| Under 2.5 | 34.2% | 30.4% | 3.00 | +2.6% |

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
| Market best home last update utc | 2026-10-09T14:32:58Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:37:54Z |
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
| Fair Under 0.5 odds | 29.94 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.75 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.92 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.97 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.24 |
| Reference draw odds | 7.00 |
| Reference away odds | 11.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | -1.1% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | -0.0228 |
| Raw ev home | 0.0059 |
| Raw edge prob draw | 0.0169 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | 0.0059 |
| Raw ev away | -0.0629 |

</details>


---
