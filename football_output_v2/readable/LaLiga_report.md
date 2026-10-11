# La Liga — football model report

Fixtures in this report: **15**.

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
| Live odds matched | 15.00 |
| Additional event odds calls used before this league | 4.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 3.00 |
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

## 2026-10-11 — Elche CF vs Celta Vigo

The model's most likely 1X2 outcome is **Elche CF win** at **36.9%**. Expected goals are 1.59 for Elche CF and 1.41 for Celta Vigo (3.00 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 56.8%; Under 3.5 goals: 64.9%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 61.0%; BTTS No (at least one team does not score): 39.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 36.9% | 2.71 |
| Draw | 27.0% | 3.70 |
| Celta Vigo win | 36.1% | 2.77 |

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
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.49% |
| 2 | 1-2 | 8.39% |
| 3 | 2-1 | 7.86% |
| 4 | 0-1 | 7.33% |
| 5 | 2-2 | 6.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 36.9% | 32.2% | 3.20 | +18.0% |
| Draw | 27.0% | 29.5% | 3.40 | -8.1% |
| Celta Vigo win | 36.1% | 38.3% | 2.58 | -6.9% |
| Over 2.5 | 56.8% | 47.5% | 2.07 | +17.5% |
| Under 2.5 | 43.2% | 52.5% | 1.96 | -15.3% |

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
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:25:52Z |
| Market best away last update utc | 2026-10-11T11:26:08Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Elche |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 61.0% |
| P btts no | 39.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.63 |
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
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.06 |
| Reference draw odds | 3.33 |
| Reference away odds | 2.58 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.07 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +4.7% |
| Draw probability edge | -2.5% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +9.2% |
| Under 2.5 probability edge | -9.2% |
| Raw edge prob home | 0.0940 |
| Raw ev home | 0.3308 |
| Raw edge prob draw | -0.0502 |
| Raw ev draw | -0.1662 |
| Raw edge prob away | -0.0438 |
| Raw ev away | -0.1256 |
| Market p over 1 5 | 74.7% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T11:26:08Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 72.4% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T11:26:08Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 56.5% |
| Market btts yes odds | 1.77 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:26:08Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.21 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Real Betis vs CA Osasuna

The model's most likely 1X2 outcome is **Real Betis win** at **60.3%**. Expected goals are 1.77 for Real Betis and 0.94 for CA Osasuna (2.71 combined). The most likely exact score is 1-0 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 51.5%; Under 3.5 goals: 70.8%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 60.3% | 1.66 |
| Draw | 22.2% | 4.50 |
| CA Osasuna win | 17.5% | 5.71 |

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
| Over 3.5 | 29.2% |
| Under 3.5 | 70.8% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.33% |
| 2 | 2-0 | 11.07% |
| 3 | 1-1 | 10.58% |
| 4 | 2-1 | 10.39% |
| 5 | 3-0 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 60.3% | 63.7% | 1.56 | -6.0% |
| Draw | 22.2% | 20.9% | 4.70 | +4.5% |
| CA Osasuna win | 17.5% | 15.4% | 7.20 | +26.1% |
| Over 2.5 | 51.5% | 56.8% | 1.74 | -10.3% |
| Under 2.5 | 48.5% | 43.2% | 2.40 | +16.3% |

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
| Market best home last update utc | 2026-10-11T11:26:08Z |
| Market best draw last update utc | 2026-10-11T11:25:53Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Betis |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 50.2% |
| P btts no | 49.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.56 |
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
| Raw p over 1 5 | 75.5% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 50.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.56 |
| Reference draw odds | 4.67 |
| Reference away odds | 6.30 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | -3.4% |
| Draw probability edge | +1.3% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.0682 |
| Raw ev home | -0.1132 |
| Raw edge prob draw | 0.0266 |
| Raw ev draw | 0.1076 |
| Raw edge prob away | 0.0416 |
| Raw ev away | 0.4102 |

</details>


---

## 2026-10-11 — Real Racing Club de Santander vs Valencia

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **40.7%**. Expected goals are 1.92 for Real Racing Club de Santander and 1.95 for Valencia (3.87 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 73.4%; Under 3.5 goals: 46.0%; Under 4.5 goals: 66.1%; BTTS Yes (both teams score): 74.0%; BTTS No (at least one team does not score): 26.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 40.7% | 2.46 |
| Draw | 24.5% | 4.08 |
| Valencia win | 34.8% | 2.87 |

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
| Over 4.5 | 33.9% |
| Under 4.5 | 66.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.11% |
| 2 | 2-2 | 8.42% |
| 3 | 2-1 | 7.84% |
| 4 | 1-2 | 6.65% |
| 5 | 3-1 | 5.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 40.7% | 42.4% | 2.33 | -5.3% |
| Draw | 24.5% | 27.7% | 3.70 | -9.3% |
| Valencia win | 34.8% | 29.9% | 3.30 | +14.9% |
| Over 2.5 | 73.4% | 56.8% | 1.74 | +27.6% |
| Under 2.5 | 26.6% | 43.2% | 2.27 | -39.5% |

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
| Market best home last update utc | 2026-10-11T11:26:08Z |
| Market best draw last update utc | 2026-10-11T11:25:52Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Valencia |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 74.0% |
| P btts no | 26.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.63 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.95 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.75 |
| Fair Over 3.5 odds | 1.85 |
| Fair Under 3.5 odds | 2.18 |
| Fair Over 4.5 odds | 2.95 |
| Fair Under 4.5 odds | 1.51 |
| Unadjusted home-win probability | 38.9% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 39.8% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 45.9% |
| Raw p btts yes | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.33 |
| Reference draw odds | 3.54 |
| Reference away odds | 3.29 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | -1.7% |
| Draw probability edge | -3.2% |
| Away probability edge | +5.0% |
| Over 2.5 probability edge | +16.6% |
| Under 2.5 probability edge | -16.6% |
| Raw edge prob home | -0.0348 |
| Raw ev home | -0.0932 |
| Raw edge prob draw | -0.0644 |
| Raw ev draw | -0.2122 |
| Raw edge prob away | 0.0992 |
| Raw ev away | 0.3131 |
| Market p over 1 5 | 79.7% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T11:26:08Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.55 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 65.6% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T11:26:07Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 62.3% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:26:08Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.53 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Real Sociedad vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Real Sociedad win** at **51.7%**. Expected goals are 1.49 for Real Sociedad and 1.20 for Deportivo La Coruña (2.68 combined). The most likely exact score is 1-0 at 11.8%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.4%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 53.7%; BTTS No (at least one team does not score): 46.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 51.7% | 1.93 |
| Draw | 24.6% | 4.07 |
| Deportivo La Coruña win | 23.7% | 4.22 |

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
| 1 | 1-0 | 11.81% |
| 2 | 1-1 | 11.69% |
| 3 | 2-1 | 10.70% |
| 4 | 2-0 | 8.93% |
| 5 | 0-0 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 51.7% | 59.8% | 1.68 | -13.1% |
| Draw | 24.6% | 23.3% | 4.25 | +4.5% |
| Deportivo La Coruña win | 23.7% | 16.9% | 5.90 | +39.8% |
| Over 2.5 | 50.9% | 54.4% | 1.81 | -7.9% |
| Under 2.5 | 49.1% | 45.6% | 2.24 | +10.0% |

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
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:25:52Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
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
| Fair Under 0.5 odds | 15.07 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.05 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.27 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 54.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.66 |
| Reference draw odds | 4.21 |
| Reference away odds | 5.75 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -8.1% |
| Draw probability edge | +1.3% |
| Away probability edge | +6.7% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.1616 |
| Raw ev home | -0.2669 |
| Raw edge prob draw | 0.0268 |
| Raw ev draw | 0.1023 |
| Raw edge prob away | 0.1348 |
| Raw ev away | 0.7953 |

</details>


---

## 2026-10-12 — Levante vs Sevilla

The model's most likely 1X2 outcome is **Levante win** at **39.9%**. Expected goals are 1.61 for Levante and 1.27 for Sevilla (2.88 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.2%; Under 3.5 goals: 67.7%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 58.3%; BTTS No (at least one team does not score): 41.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 39.9% | 2.51 |
| Draw | 26.7% | 3.74 |
| Sevilla win | 33.4% | 2.99 |

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
| 1 | 1-1 | 12.55% |
| 2 | 2-1 | 8.13% |
| 3 | 1-2 | 8.13% |
| 4 | 1-0 | 7.82% |
| 5 | 0-1 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 39.9% | 34.4% | 2.88 | +14.8% |
| Draw | 26.7% | 28.7% | 3.43 | -8.3% |
| Sevilla win | 33.4% | 37.0% | 2.74 | -8.4% |
| Over 2.5 | 54.2% | 46.9% | 2.12 | +14.9% |
| Under 2.5 | 45.8% | 53.1% | 1.86 | -14.8% |

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
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:26:08Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.3% |
| P btts no | 41.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.05 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.58 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.19 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 45.4% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 29.9% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 57.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.87 |
| Reference draw odds | 3.43 |
| Reference away odds | 2.67 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.86 |
| Home probability edge | +5.5% |
| Draw probability edge | -1.9% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | +7.3% |
| Under 2.5 probability edge | -7.3% |
| Raw edge prob home | 0.1100 |
| Raw ev home | 0.3063 |
| Raw edge prob draw | -0.0390 |
| Raw ev draw | -0.1500 |
| Raw edge prob away | -0.0711 |
| Raw ev away | -0.1818 |
| Market p over 1 5 | 73.4% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T11:26:07Z |
| Market reference over 1 5 odds | 1.34 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 74.1% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T11:26:08Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.60 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 53.5% |
| Market btts yes odds | 1.84 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:26:08Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 1.98 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.0%**. Expected goals are 1.84 for Deportivo La Coruña and 1.11 for Levante (2.95 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.7%; Under 3.5 goals: 66.2%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.0% | 2.00 |
| Draw | 25.1% | 3.98 |
| Levante win | 24.9% | 4.01 |

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
| Over 2.5 | 55.7% |
| Under 2.5 | 44.3% |
| Over 3.5 | 33.8% |
| Under 3.5 | 66.2% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.78% |
| 2 | 2-1 | 9.04% |
| 3 | 1-0 | 8.71% |
| 4 | 2-0 | 8.15% |
| 5 | 1-2 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.0% | 45.6% | 2.17 | +8.5% |
| Draw | 25.1% | 27.1% | 3.62 | -9.1% |
| Levante win | 24.9% | 27.3% | 3.60 | -10.3% |
| Over 2.5 | 55.7% | 49.7% | 1.98 | +10.4% |
| Under 2.5 | 44.3% | 50.3% | 1.96 | -13.2% |

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
| Market best home last update utc | 2026-10-11T11:26:08Z |
| Market best draw last update utc | 2026-10-11T11:26:08Z |
| Market best away last update utc | 2026-10-11T11:26:08Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 12.00 |
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
| Fair Under 0.5 odds | 17.11 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.96 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.80 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.4% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 79.5% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.17 |
| Reference draw odds | 3.62 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.98 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | +4.4% |
| Draw probability edge | -2.0% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | +6.0% |
| Under 2.5 probability edge | -6.0% |
| Raw edge prob home | 0.0880 |
| Raw ev home | 0.1801 |
| Raw edge prob draw | -0.0407 |
| Raw ev draw | -0.1650 |
| Raw edge prob away | -0.0473 |
| Raw ev away | -0.1882 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **50.9%**. Expected goals are 1.03 for Espanyol and 1.58 for Atlético Madrid (2.60 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 48.3%; Under 3.5 goals: 73.4%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 23.6% | 4.24 |
| Draw | 25.5% | 3.92 |
| Atlético Madrid win | 50.9% | 1.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.03 |
| Atlético Madrid expected goals | 1.58 |
| Expected total goals | 2.60 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
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
| 1 | 1-1 | 12.14% |
| 2 | 0-1 | 11.71% |
| 3 | 1-2 | 9.63% |
| 4 | 0-2 | 9.38% |
| 5 | 0-0 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 23.6% | 22.6% | 4.60 | +8.4% |
| Draw | 25.5% | 25.5% | 3.84 | -2.0% |
| Atlético Madrid win | 50.9% | 51.8% | 1.91 | -2.8% |
| Over 2.5 | 48.3% | 52.7% | 1.87 | -9.6% |
| Under 2.5 | 51.7% | 47.3% | 2.08 | +7.5% |

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
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:26:08Z |
| Market best away last update utc | 2026-10-11T11:26:08Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
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
| Fair Under 0.5 odds | 13.23 |
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
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 4.32 |
| Reference draw odds | 3.84 |
| Reference away odds | 1.91 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | +0.9% |
| Draw probability edge | +0.0% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | 0.0186 |
| Raw ev home | 0.1270 |
| Raw edge prob draw | 0.0001 |
| Raw ev draw | -0.0198 |
| Raw edge prob away | -0.0187 |
| Raw ev away | -0.0455 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **60.3%**. Expected goals are 1.32 for Real Betis and 2.05 for Barcelona (3.37 combined). The most likely exact score is 1-2 at 10.6%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 66.3%; Under 3.5 goals: 55.9%; Under 4.5 goals: 74.3%; BTTS Yes (both teams score): 63.4%; BTTS No (at least one team does not score): 36.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 20.0% | 5.00 |
| Draw | 19.7% | 5.08 |
| Barcelona win | 60.3% | 1.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.32 |
| Barcelona expected goals | 2.05 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 66.3% |
| Under 2.5 | 33.7% |
| Over 3.5 | 44.1% |
| Under 3.5 | 55.9% |
| Over 4.5 | 25.7% |
| Under 4.5 | 74.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.64% |
| 2 | 1-1 | 8.61% |
| 3 | 0-2 | 8.03% |
| 4 | 0-1 | 7.70% |
| 5 | 1-3 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 20.0% | 15.6% | 6.50 | +29.9% |
| Draw | 19.7% | 17.8% | 6.00 | +18.2% |
| Barcelona win | 60.3% | 66.6% | 1.49 | -10.1% |
| Over 2.5 | 66.3% | 77.0% | 1.27 | -15.8% |
| Under 2.5 | 33.7% | 23.0% | 3.82 | +28.6% |

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
| Market best home last update utc | 2026-10-11T11:25:37Z |
| Market best draw last update utc | 2026-10-11T11:25:53Z |
| Market best away last update utc | 2026-10-11T11:26:08Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.4% |
| P btts no | 36.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.76 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.87 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.97 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.90 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 54.0% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 64.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 6.21 |
| Reference draw odds | 5.44 |
| Reference away odds | 1.49 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.82 |
| Home probability edge | +4.4% |
| Draw probability edge | +1.9% |
| Away probability edge | -6.3% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | 0.0885 |
| Raw ev home | 0.5871 |
| Raw edge prob draw | 0.0376 |
| Raw ev draw | 0.2943 |
| Raw edge prob away | -0.1261 |
| Raw ev away | -0.1952 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.6%**. Expected goals are 1.08 for Valencia and 1.17 for Athletic Bilbao (2.25 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.2%; Under 3.5 goals: 81.0%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.1% | 3.32 |
| Draw | 28.3% | 3.54 |
| Athletic Bilbao win | 41.6% | 2.40 |

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
| 1 | 0-1 | 13.42% |
| 2 | 1-1 | 13.13% |
| 3 | 0-0 | 10.47% |
| 4 | 1-0 | 10.19% |
| 5 | 1-2 | 8.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.1% | 27.1% | 3.70 | +11.4% |
| Draw | 28.3% | 27.5% | 3.58 | +1.3% |
| Athletic Bilbao win | 41.6% | 45.4% | 2.18 | -9.3% |
| Over 2.5 | 39.2% | 46.9% | 2.10 | -17.6% |
| Under 2.5 | 60.8% | 53.1% | 1.86 | +13.0% |

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
| Market best home last update utc | 2026-10-11T11:25:37Z |
| Market best draw last update utc | 2026-10-11T11:26:08Z |
| Market best away last update utc | 2026-10-11T11:26:08Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Tipico |
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
| Fair Under 0.5 odds | 9.55 |
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
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 45.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.62 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.18 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.86 |
| Home probability edge | +3.0% |
| Draw probability edge | +0.8% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.0594 |
| Raw ev home | 0.2243 |
| Raw edge prob draw | 0.0165 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | -0.0759 |
| Raw ev away | -0.1760 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.2%**. Expected goals are 2.51 for Villarreal and 1.25 for Elche CF (3.76 combined). The most likely exact score is 2-1 at 9.2%. Goal-market probabilities: at least one goal: 97.4%; Over 2.5 goals: 72.3%; Under 3.5 goals: 48.0%; Under 4.5 goals: 67.6%; BTTS Yes (both teams score): 65.9%; BTTS No (at least one team does not score): 34.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.2% | 1.53 |
| Draw | 19.0% | 5.27 |
| Elche CF win | 15.9% | 6.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.51 |
| Elche CF expected goals | 1.25 |
| Expected total goals | 3.76 |
| Over 0.5 | 97.4% |
| Under 0.5 | 2.6% |
| Over 1.5 | 89.1% |
| Under 1.5 | 10.9% |
| Over 2.5 | 72.3% |
| Under 2.5 | 27.7% |
| Over 3.5 | 52.0% |
| Under 3.5 | 48.0% |
| Over 4.5 | 32.4% |
| Under 4.5 | 67.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.25% |
| 2 | 1-1 | 7.80% |
| 3 | 3-1 | 7.73% |
| 4 | 2-0 | 7.37% |
| 5 | 3-0 | 6.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.2% | 65.7% | 1.51 | -1.6% |
| Draw | 19.0% | 19.9% | 5.00 | -5.1% |
| Elche CF win | 15.9% | 14.4% | 6.73 | +6.7% |
| Over 2.5 | 72.3% | 64.6% | 1.50 | +8.4% |
| Under 2.5 | 27.7% | 35.4% | 2.70 | -25.1% |

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
| Market best home last update utc | 2026-10-11T11:26:08Z |
| Market best draw last update utc | 2026-10-11T11:25:52Z |
| Market best away last update utc | 2026-10-11T11:26:08Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.9% |
| P btts no | 34.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.18 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.18 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.61 |
| Fair Over 3.5 odds | 1.92 |
| Fair Under 3.5 odds | 2.08 |
| Fair Over 4.5 odds | 3.09 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 64.6% |
| Unadjusted draw probability | 18.0% |
| Unadjusted away-win probability | 17.4% |
| Raw p over 1 5 | 89.0% |
| Raw p under 3 5 | 48.1% |
| Raw p btts yes | 65.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.51 |
| Reference draw odds | 4.88 |
| Reference away odds | 6.73 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -0.6% |
| Draw probability edge | -0.9% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +7.7% |
| Under 2.5 probability edge | -7.7% |
| Raw edge prob home | -0.0114 |
| Raw ev home | -0.0247 |
| Raw edge prob draw | -0.0187 |
| Raw ev draw | -0.0978 |
| Raw edge prob away | 0.0301 |
| Raw ev away | 0.1687 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **57.1%**. Expected goals are 2.71 for CA Osasuna and 1.48 for Real Racing Club de Santander (4.19 combined). The most likely exact score is 1-1 at 7.8%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 77.4%; Under 3.5 goals: 40.3%; Under 4.5 goals: 60.5%; BTTS Yes (both teams score): 73.5%; BTTS No (at least one team does not score): 26.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 57.1% | 1.75 |
| Draw | 22.0% | 4.55 |
| Real Racing Club de Santander win | 20.9% | 4.78 |

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
| 1 | 1-1 | 7.80% |
| 2 | 2-2 | 7.72% |
| 3 | 2-1 | 7.41% |
| 4 | 3-1 | 6.69% |
| 5 | 2-0 | 5.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 57.1% | 50.7% | 1.95 | +11.3% |
| Draw | 22.0% | 26.6% | 3.68 | -19.0% |
| Real Racing Club de Santander win | 20.9% | 22.6% | 4.32 | -9.7% |
| Over 2.5 | 77.4% | 54.6% | 1.81 | +40.1% |
| Under 2.5 | 22.6% | 45.4% | 2.17 | -51.0% |

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
| Market best home last update utc | 2026-10-11T11:26:08Z |
| Market best draw last update utc | 2026-10-11T11:26:08Z |
| Market best away last update utc | 2026-10-11T11:26:08Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
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
| Fair Under 0.5 odds | 49.43 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.53 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.43 |
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
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.95 |
| Reference draw odds | 3.68 |
| Reference away odds | 4.32 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.17 |
| Home probability edge | +6.3% |
| Draw probability edge | -4.6% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | +22.8% |
| Under 2.5 probability edge | -22.8% |
| Raw edge prob home | 0.1269 |
| Raw ev home | 0.2370 |
| Raw edge prob draw | -0.0925 |
| Raw ev draw | -0.3605 |
| Raw edge prob away | -0.0344 |
| Raw ev away | -0.1712 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **48.6%**. Expected goals are 1.51 for Celta Vigo and 0.96 for Alavés (2.47 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.5%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.4%; BTTS No (at least one team does not score): 51.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 48.6% | 2.06 |
| Draw | 26.9% | 3.72 |
| Alavés win | 24.5% | 4.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.51 |
| Alavés expected goals | 0.96 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
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
| 1 | 1-1 | 12.72% |
| 2 | 1-0 | 12.32% |
| 3 | 2-0 | 9.40% |
| 4 | 2-1 | 9.05% |
| 5 | 0-0 | 8.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 48.6% | 47.6% | 2.08 | +1.2% |
| Draw | 26.9% | 27.5% | 3.58 | -3.7% |
| Alavés win | 24.5% | 24.9% | 3.94 | -3.6% |
| Over 2.5 | 44.6% | 44.9% | 2.19 | -2.3% |
| Under 2.5 | 55.4% | 55.1% | 1.79 | -0.8% |

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
| Market best home last update utc | 2026-10-11T11:26:08Z |
| Market best draw last update utc | 2026-10-11T11:26:08Z |
| Market best away last update utc | 2026-10-11T11:26:08Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.33 |
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
| Raw p over 1 5 | 70.8% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.08 |
| Reference draw odds | 3.58 |
| Reference away odds | 3.94 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.19 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +1.0% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.0207 |
| Raw ev home | 0.0334 |
| Raw edge prob draw | -0.0113 |
| Raw ev draw | -0.0573 |
| Raw edge prob away | -0.0094 |
| Raw ev away | -0.0549 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.2%**. Expected goals are 0.57 for Málaga and 1.26 for Real Sociedad (1.83 combined). The most likely exact score is 0-1 at 18.2%. Goal-market probabilities: at least one goal: 84.6%; Over 2.5 goals: 27.6%; Under 3.5 goals: 89.0%; Under 4.5 goals: 96.2%; BTTS Yes (both teams score): 31.1%; BTTS No (at least one team does not score): 68.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.2% | 4.30 |
| Draw | 28.6% | 3.50 |
| Real Sociedad win | 48.2% | 2.08 |

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
| Over 2.5 | 27.6% |
| Under 2.5 | 72.4% |
| Over 3.5 | 11.0% |
| Under 3.5 | 89.0% |
| Over 4.5 | 3.8% |
| Under 4.5 | 96.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.17% |
| 2 | 0-0 | 15.40% |
| 3 | 1-0 | 12.55% |
| 4 | 0-2 | 11.54% |
| 5 | 1-1 | 11.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.2% | 29.9% | 3.30 | -23.3% |
| Draw | 28.6% | 27.0% | 3.63 | +3.7% |
| Real Sociedad win | 48.2% | 43.1% | 2.29 | +10.3% |
| Over 2.5 | 27.6% | 53.1% | 1.86 | -48.6% |
| Under 2.5 | 72.4% | 46.9% | 2.10 | +52.0% |

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
| Market best home last update utc | 2026-10-11T11:25:37Z |
| Market best draw last update utc | 2026-10-11T11:26:08Z |
| Market best away last update utc | 2026-10-11T11:26:08Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
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
| Fair Under 0.5 odds | 6.50 |
| Fair Over 1.5 odds | 1.86 |
| Fair Under 1.5 odds | 2.17 |
| Fair Over 2.5 odds | 3.62 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.11 |
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
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.29 |
| Reference draw odds | 3.63 |
| Reference away odds | 2.29 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -6.6% |
| Draw probability edge | +1.6% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -25.5% |
| Under 2.5 probability edge | +25.5% |
| Raw edge prob home | -0.1324 |
| Raw ev home | -0.4517 |
| Raw edge prob draw | 0.0312 |
| Raw ev draw | 0.0941 |
| Raw edge prob away | 0.1012 |
| Raw ev away | 0.2193 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **76.9%**. Expected goals are 2.62 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 11.8%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 65.3%; Under 3.5 goals: 56.7%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 48.8%; BTTS No (at least one team does not score): 51.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 76.9% | 1.30 |
| Draw | 14.5% | 6.89 |
| Sevilla win | 8.5% | 11.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.62 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 84.9% |
| Under 1.5 | 15.1% |
| Over 2.5 | 65.3% |
| Under 2.5 | 34.7% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.80% |
| 2 | 3-0 | 10.31% |
| 3 | 1-0 | 8.91% |
| 4 | 2-1 | 8.78% |
| 5 | 3-1 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 76.9% | 76.5% | 1.30 | +0.0% |
| Draw | 14.5% | 14.6% | 7.40 | +7.5% |
| Sevilla win | 8.5% | 8.9% | 12.00 | +2.4% |
| Over 2.5 | 65.3% | 70.7% | 1.38 | -9.9% |
| Under 2.5 | 34.7% | 29.3% | 3.12 | +8.3% |

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
| Market best home last update utc | 2026-10-11T11:26:08Z |
| Market best draw last update utc | 2026-10-11T11:25:52Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.8% |
| P btts no | 51.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.10 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.64 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.88 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.02 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.30 |
| Reference draw odds | 6.61 |
| Reference away odds | 10.70 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.12 |
| Home probability edge | +0.4% |
| Draw probability edge | -0.0% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | 0.0086 |
| Raw ev home | 0.0059 |
| Raw edge prob draw | -0.0009 |
| Raw ev draw | 0.0711 |
| Raw edge prob away | -0.0076 |
| Raw ev away | -0.0221 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.5%**. Expected goals are 0.92 for Getafe and 0.73 for Rayo Vallecano (1.65 combined). The most likely exact score is 0-0 at 18.0%. Goal-market probabilities: at least one goal: 82.0%; Over 2.5 goals: 23.5%; Under 3.5 goals: 91.4%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 31.0%; BTTS No (at least one team does not score): 69.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.5% | 2.82 |
| Draw | 32.5% | 3.08 |
| Rayo Vallecano win | 32.0% | 3.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.92 |
| Rayo Vallecano expected goals | 0.73 |
| Expected total goals | 1.65 |
| Over 0.5 | 82.0% |
| Under 0.5 | 18.0% |
| Over 1.5 | 49.4% |
| Under 1.5 | 50.6% |
| Over 2.5 | 23.5% |
| Under 2.5 | 76.5% |
| Over 3.5 | 8.6% |
| Under 3.5 | 91.4% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.05% |
| 2 | 1-0 | 16.33% |
| 3 | 0-1 | 16.22% |
| 4 | 1-1 | 12.23% |
| 5 | 2-0 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.5% | 33.2% | 2.97 | +5.4% |
| Draw | 32.5% | 30.2% | 3.26 | +5.9% |
| Rayo Vallecano win | 32.0% | 36.7% | 2.80 | -10.3% |
| Over 2.5 | 23.5% | 38.6% | 2.54 | -40.2% |
| Under 2.5 | 76.5% | 61.4% | 1.61 | +23.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T19:00:00+00:00 |
| Fixture id | 4a88bc4de574d43ef34677fd8d78722f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:26:08Z |
| Market best draw last update utc | 2026-10-11T11:26:08Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 31.0% |
| P btts no | 69.0% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.54 |
| Fair Over 1.5 odds | 2.02 |
| Fair Under 1.5 odds | 1.98 |
| Fair Over 2.5 odds | 4.25 |
| Fair Under 2.5 odds | 1.31 |
| Fair Over 3.5 odds | 11.58 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 36.60 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.8% |
| Unadjusted draw probability | 34.8% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 49.4% |
| Raw p under 3 5 | 91.4% |
| Raw p btts yes | 31.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.97 |
| Reference draw odds | 3.26 |
| Reference away odds | 2.69 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.54 |
| Reference Under 2.5 odds | 1.61 |
| Home probability edge | +2.3% |
| Draw probability edge | +2.3% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -15.0% |
| Under 2.5 probability edge | +15.0% |
| Raw edge prob home | 0.0463 |
| Raw ev home | 0.1225 |
| Raw edge prob draw | 0.0460 |
| Raw ev draw | 0.1337 |
| Raw edge prob away | -0.0923 |
| Raw ev away | -0.2319 |

</details>


---
