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

## 2026-10-11 — Elche CF vs Celta Vigo

The model's most likely 1X2 outcome is **Elche CF win** at **37.3%**. Expected goals are 1.59 for Elche CF and 1.41 for Celta Vigo (3.00 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.9%; Under 3.5 goals: 64.9%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 37.3% | 2.68 |
| Draw | 26.7% | 3.75 |
| Celta Vigo win | 36.1% | 2.77 |

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
| 1 | 1-1 | 12.33% |
| 2 | 1-2 | 8.39% |
| 3 | 2-1 | 7.94% |
| 4 | 0-1 | 7.32% |
| 5 | 1-0 | 6.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 37.3% | 32.9% | 3.10 | +15.5% |
| Draw | 26.7% | 28.9% | 3.40 | -9.3% |
| Celta Vigo win | 36.1% | 38.2% | 2.61 | -5.9% |
| Over 2.5 | 56.9% | 48.3% | 2.07 | +17.8% |
| Under 2.5 | 43.1% | 51.7% | 1.95 | -15.9% |

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
| Market best home last update utc | 2026-10-11T06:31:23Z |
| Market best draw last update utc | 2026-10-11T06:31:23Z |
| Market best away last update utc | 2026-10-11T06:30:54Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
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
| Fair Under 0.5 odds | 17.86 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.03 |
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
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.75 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.01 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +4.3% |
| Draw probability edge | -2.2% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +8.6% |
| Under 2.5 probability edge | -8.6% |
| Raw edge prob home | 0.0867 |
| Raw ev home | 0.2892 |
| Raw edge prob draw | -0.0434 |
| Raw ev draw | -0.1662 |
| Raw edge prob away | -0.0434 |
| Raw ev away | -0.1155 |

</details>


---

## 2026-10-11 — Real Betis vs CA Osasuna

The model's most likely 1X2 outcome is **Real Betis win** at **60.7%**. Expected goals are 1.77 for Real Betis and 0.94 for CA Osasuna (2.71 combined). The most likely exact score is 1-0 at 12.4%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 51.6%; Under 3.5 goals: 70.8%; Under 4.5 goals: 85.8%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 60.7% | 1.65 |
| Draw | 22.1% | 4.52 |
| CA Osasuna win | 17.2% | 5.81 |

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
| Over 2.5 | 51.6% |
| Under 2.5 | 48.4% |
| Over 3.5 | 29.2% |
| Under 3.5 | 70.8% |
| Over 4.5 | 14.2% |
| Under 4.5 | 85.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.42% |
| 2 | 2-0 | 11.15% |
| 3 | 1-1 | 10.52% |
| 4 | 2-1 | 10.46% |
| 5 | 3-0 | 6.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 60.7% | 64.5% | 1.57 | -4.7% |
| Draw | 22.1% | 20.6% | 4.70 | +3.9% |
| CA Osasuna win | 17.2% | 14.9% | 6.80 | +17.1% |
| Over 2.5 | 51.6% | 55.4% | 1.81 | -6.6% |
| Under 2.5 | 48.4% | 44.6% | 2.24 | +8.4% |

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
| Market best home last update utc | 2026-10-11T06:31:38Z |
| Market best draw last update utc | 2026-10-11T06:31:23Z |
| Market best away last update utc | 2026-10-11T06:31:23Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
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
| Fair Under 0.5 odds | 15.66 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.43 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.05 |
| Fair Under 4.5 odds | 1.17 |
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
| Reference draw odds | 4.10 |
| Reference away odds | 5.50 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | -3.8% |
| Draw probability edge | +1.5% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | -0.0766 |
| Raw ev home | -0.1075 |
| Raw edge prob draw | 0.0293 |
| Raw ev draw | 0.1076 |
| Raw edge prob away | 0.0473 |
| Raw ev away | 0.3319 |

</details>


---

## 2026-10-11 — Real Racing Club de Santander vs Valencia

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **41.1%**. Expected goals are 1.92 for Real Racing Club de Santander and 1.95 for Valencia (3.87 combined). The most likely exact score is 1-1 at 8.8%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 73.6%; Under 3.5 goals: 45.9%; Under 4.5 goals: 65.9%; BTTS Yes (both teams score): 73.8%; BTTS No (at least one team does not score): 26.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 41.1% | 2.43 |
| Draw | 23.7% | 4.21 |
| Valencia win | 35.2% | 2.84 |

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
| Over 2.5 | 73.6% |
| Under 2.5 | 26.4% |
| Over 3.5 | 54.1% |
| Under 3.5 | 45.9% |
| Over 4.5 | 34.1% |
| Under 4.5 | 65.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.82% |
| 2 | 2-2 | 8.15% |
| 3 | 2-1 | 7.93% |
| 4 | 1-2 | 6.72% |
| 5 | 3-1 | 5.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 41.1% | 43.2% | 2.34 | -3.9% |
| Draw | 23.7% | 26.2% | 3.70 | -12.2% |
| Valencia win | 35.2% | 30.6% | 3.30 | +16.1% |
| Over 2.5 | 73.6% | 55.4% | 1.74 | +28.0% |
| Under 2.5 | 26.4% | 44.6% | 2.27 | -40.0% |

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
| Market best home last update utc | 2026-10-11T06:31:38Z |
| Market best draw last update utc | 2026-10-11T06:31:23Z |
| Market best away last update utc | 2026-10-11T06:31:08Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Tipico |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Valencia |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 73.8% |
| P btts no | 26.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.92 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.96 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.78 |
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
| Reference away odds | 2.95 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | -2.2% |
| Draw probability edge | -2.4% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | +18.2% |
| Under 2.5 probability edge | -18.2% |
| Raw edge prob home | -0.0432 |
| Raw ev home | -0.0893 |
| Raw edge prob draw | -0.0489 |
| Raw ev draw | -0.2122 |
| Raw edge prob away | 0.0921 |
| Raw ev away | 0.3131 |
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T06:30:54Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T06:31:39Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.2% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T06:31:54Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.54 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Real Sociedad vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Real Sociedad win** at **52.3%**. Expected goals are 1.49 for Real Sociedad and 1.20 for Deportivo La Coruña (2.68 combined). The most likely exact score is 1-0 at 11.9%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.4%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 53.7%; BTTS No (at least one team does not score): 46.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 52.3% | 1.91 |
| Draw | 24.2% | 4.13 |
| Deportivo La Coruña win | 23.5% | 4.25 |

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
| 2 | 1-1 | 11.52% |
| 3 | 2-1 | 10.81% |
| 4 | 2-0 | 9.02% |
| 5 | 0-0 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 52.3% | 60.9% | 1.68 | -12.2% |
| Draw | 24.2% | 22.5% | 4.35 | +5.4% |
| Deportivo La Coruña win | 23.5% | 16.6% | 5.90 | +38.7% |
| Over 2.5 | 51.0% | 55.8% | 1.81 | -7.7% |
| Under 2.5 | 49.0% | 44.2% | 2.22 | +8.8% |

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
| Market best home last update utc | 2026-10-11T06:31:23Z |
| Market best draw last update utc | 2026-10-11T06:31:24Z |
| Market best away last update utc | 2026-10-11T06:31:23Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 12.00 |
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
| Fair Under 0.5 odds | 15.30 |
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
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 54.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 3.80 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -8.6% |
| Draw probability edge | +1.7% |
| Away probability edge | +6.9% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | -0.1724 |
| Raw ev home | -0.2669 |
| Raw edge prob draw | 0.0340 |
| Raw ev draw | 0.1282 |
| Raw edge prob away | 0.1384 |
| Raw ev away | 0.7953 |

</details>


---

## 2026-10-12 — Levante vs Sevilla

The model's most likely 1X2 outcome is **Levante win** at **40.1%**. Expected goals are 1.61 for Levante and 1.27 for Sevilla (2.88 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.2%; Under 3.5 goals: 67.7%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 58.3%; BTTS No (at least one team does not score): 41.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 40.1% | 2.49 |
| Draw | 26.8% | 3.74 |
| Sevilla win | 33.1% | 3.02 |

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
| 2 | 2-1 | 8.19% |
| 3 | 1-2 | 8.06% |
| 4 | 1-0 | 7.87% |
| 5 | 0-1 | 7.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 40.1% | 34.9% | 2.90 | +16.3% |
| Draw | 26.8% | 28.7% | 3.43 | -8.2% |
| Sevilla win | 33.1% | 36.4% | 2.74 | -9.2% |
| Over 2.5 | 54.2% | 44.6% | 2.12 | +14.9% |
| Under 2.5 | 45.8% | 55.4% | 1.86 | -14.8% |

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
| Market best home last update utc | 2026-10-11T06:31:23Z |
| Market best draw last update utc | 2026-10-11T06:31:38Z |
| Market best away last update utc | 2026-10-11T06:31:23Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
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
| Fair Under 0.5 odds | 16.04 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.59 |
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
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.63 |
| Home probability edge | +5.2% |
| Draw probability edge | -2.0% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | +9.6% |
| Under 2.5 probability edge | -9.6% |
| Raw edge prob home | 0.1049 |
| Raw ev home | 0.3154 |
| Raw edge prob draw | -0.0394 |
| Raw ev draw | -0.1500 |
| Raw edge prob away | -0.0655 |
| Raw ev away | -0.1818 |

</details>


---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.6%**. Expected goals are 1.84 for Deportivo La Coruña and 1.11 for Levante (2.95 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.1%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.6% | 1.98 |
| Draw | 24.6% | 4.06 |
| Levante win | 24.8% | 4.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 1.84 |
| Levante expected goals | 1.11 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
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
| 1 | 1-1 | 11.56% |
| 2 | 2-1 | 9.14% |
| 3 | 1-0 | 8.81% |
| 4 | 2-0 | 8.24% |
| 5 | 1-2 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.6% | 46.7% | 2.17 | +9.7% |
| Draw | 24.6% | 26.2% | 3.62 | -10.9% |
| Levante win | 24.8% | 27.1% | 3.60 | -10.6% |
| Over 2.5 | 55.9% | 49.7% | 1.98 | +10.7% |
| Under 2.5 | 44.1% | 50.3% | 1.96 | -13.6% |

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
| Market best home last update utc | 2026-10-11T06:31:38Z |
| Market best draw last update utc | 2026-10-11T06:31:38Z |
| Market best away last update utc | 2026-10-11T06:31:38Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 11.00 |
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
| Fair Under 0.5 odds | 17.44 |
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
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.91 |
| Home probability edge | +3.8% |
| Draw probability edge | -1.6% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | +6.2% |
| Under 2.5 probability edge | -6.2% |
| Raw edge prob home | 0.0767 |
| Raw ev home | 0.1801 |
| Raw edge prob draw | -0.0312 |
| Raw ev draw | -0.1650 |
| Raw edge prob away | -0.0455 |
| Raw ev away | -0.1882 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **52.2%**. Expected goals are 1.03 for Espanyol and 1.58 for Atlético Madrid (2.60 combined). The most likely exact score is 0-1 at 12.0%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 48.6%; Under 3.5 goals: 73.3%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 22.8% | 4.38 |
| Draw | 25.0% | 4.00 |
| Atlético Madrid win | 52.2% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.03 |
| Atlético Madrid expected goals | 1.58 |
| Expected total goals | 2.60 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.6% |
| Under 2.5 | 51.4% |
| Over 3.5 | 26.7% |
| Under 3.5 | 73.3% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.01% |
| 2 | 1-1 | 11.89% |
| 3 | 1-2 | 9.87% |
| 4 | 0-2 | 9.61% |
| 5 | 0-0 | 7.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 22.8% | 21.1% | 4.60 | +5.0% |
| Draw | 25.0% | 24.4% | 3.84 | -4.1% |
| Atlético Madrid win | 52.2% | 54.4% | 1.91 | -0.3% |
| Over 2.5 | 48.6% | 54.4% | 1.87 | -9.2% |
| Under 2.5 | 51.4% | 45.6% | 2.08 | +7.0% |

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
| Market best home last update utc | 2026-10-11T06:31:23Z |
| Market best draw last update utc | 2026-10-11T06:31:38Z |
| Market best away last update utc | 2026-10-11T06:31:38Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Espanol |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 93/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.51 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.75 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.04 |
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
| Reference home odds | 4.36 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.78 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 1.92 |
| Home probability edge | +1.7% |
| Draw probability edge | +0.5% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.0336 |
| Raw ev home | 0.1270 |
| Raw edge prob draw | 0.0108 |
| Raw ev draw | -0.0198 |
| Raw edge prob away | -0.0444 |
| Raw ev away | -0.0455 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **62.9%**. Expected goals are 1.32 for Real Betis and 2.05 for Barcelona (3.37 combined). The most likely exact score is 1-2 at 11.1%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 67.1%; Under 3.5 goals: 55.7%; Under 4.5 goals: 73.9%; BTTS Yes (both teams score): 62.8%; BTTS No (at least one team does not score): 37.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.5% | 5.14 |
| Draw | 17.6% | 5.68 |
| Barcelona win | 62.9% | 1.59 |

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
| Over 2.5 | 67.1% |
| Under 2.5 | 32.9% |
| Over 3.5 | 44.3% |
| Under 3.5 | 55.7% |
| Over 4.5 | 26.1% |
| Under 4.5 | 73.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.10% |
| 2 | 0-2 | 8.38% |
| 3 | 0-1 | 8.03% |
| 4 | 1-1 | 7.70% |
| 5 | 1-3 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.5% | 14.5% | 6.50 | +26.5% |
| Draw | 17.6% | 13.6% | 6.20 | +9.1% |
| Barcelona win | 62.9% | 71.9% | 1.49 | -6.2% |
| Over 2.5 | 67.1% | 77.2% | 1.26 | -15.5% |
| Under 2.5 | 32.9% | 22.8% | 3.75 | +23.5% |

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
| Market best home last update utc | 2026-10-11T06:31:08Z |
| Market best draw last update utc | 2026-10-11T06:31:23Z |
| Market best away last update utc | 2026-10-11T06:31:38Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Nordic Bet |
| Best under 2 5 bookmaker | Nordic Bet |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 62.8% |
| P btts no | 37.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.44 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.92 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.04 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.83 |
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
| Reference home odds | 5.30 |
| Reference draw odds | 5.60 |
| Reference away odds | 1.33 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.75 |
| Home probability edge | +5.0% |
| Draw probability edge | +4.0% |
| Away probability edge | -8.9% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | 0.0991 |
| Raw ev home | 0.5871 |
| Raw edge prob draw | 0.0796 |
| Raw ev draw | 0.3375 |
| Raw edge prob away | -0.1787 |
| Raw ev away | -0.1952 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.3%**. Expected goals are 1.08 for Valencia and 1.17 for Athletic Bilbao (2.25 combined). The most likely exact score is 0-1 at 13.7%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 39.3%; Under 3.5 goals: 80.9%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.6% | 3.38 |
| Draw | 28.1% | 3.56 |
| Athletic Bilbao win | 42.3% | 2.36 |

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
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.66% |
| 2 | 1-1 | 13.02% |
| 3 | 0-0 | 10.38% |
| 4 | 1-0 | 10.01% |
| 5 | 1-2 | 8.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.6% | 26.1% | 3.85 | +13.9% |
| Draw | 28.1% | 27.0% | 3.58 | +0.5% |
| Athletic Bilbao win | 42.3% | 46.9% | 2.18 | -7.7% |
| Over 2.5 | 39.3% | 47.1% | 2.10 | -17.4% |
| Under 2.5 | 60.7% | 52.9% | 1.86 | +12.9% |

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
| Market best home last update utc | 2026-10-11T06:31:23Z |
| Market best draw last update utc | 2026-10-11T06:31:39Z |
| Market best away last update utc | 2026-10-11T06:31:39Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
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
| Fair Under 0.5 odds | 9.63 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.54 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.73 |
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
| Reference away odds | 1.96 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +3.5% |
| Draw probability edge | +1.0% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | 0.0700 |
| Raw ev home | 0.2740 |
| Raw edge prob draw | 0.0210 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | -0.0909 |
| Raw ev away | -0.1760 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **66.0%**. Expected goals are 2.51 for Villarreal and 1.25 for Elche CF (3.76 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 72.6%; Under 3.5 goals: 47.9%; Under 4.5 goals: 67.4%; BTTS Yes (both teams score): 65.6%; BTTS No (at least one team does not score): 34.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 66.0% | 1.51 |
| Draw | 17.9% | 5.58 |
| Elche CF win | 16.1% | 6.23 |

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
| 2 | 3-1 | 7.83% |
| 3 | 2-0 | 7.47% |
| 4 | 1-1 | 7.36% |
| 5 | 3-0 | 6.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 66.0% | 67.4% | 1.51 | -0.3% |
| Draw | 17.9% | 17.8% | 5.00 | -10.4% |
| Elche CF win | 16.1% | 14.8% | 6.73 | +8.1% |
| Over 2.5 | 72.6% | 64.6% | 1.49 | +8.2% |
| Under 2.5 | 27.4% | 35.4% | 2.70 | -26.1% |

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
| Market best home last update utc | 2026-10-11T06:31:38Z |
| Market best draw last update utc | 2026-10-11T06:31:23Z |
| Market best away last update utc | 2026-10-11T06:31:38Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Nordic Bet |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.6% |
| P btts no | 34.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.48 |
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
| Reference away odds | 5.30 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Home probability edge | -1.4% |
| Draw probability edge | +0.1% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | +8.0% |
| Under 2.5 probability edge | -8.0% |
| Raw edge prob home | -0.0283 |
| Raw ev home | -0.0247 |
| Raw edge prob draw | 0.0023 |
| Raw ev draw | -0.0978 |
| Raw edge prob away | 0.0260 |
| Raw ev away | 0.1687 |
| Market p over 1 5 | 86.7% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T06:31:24Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 56.3% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T06:30:19Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.06 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 58.7% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T06:31:54Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.34 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **57.6%**. Expected goals are 2.71 for CA Osasuna and 1.48 for Real Racing Club de Santander (4.19 combined). The most likely exact score is 1-1 at 7.6%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 77.6%; Under 3.5 goals: 40.3%; Under 4.5 goals: 60.4%; BTTS Yes (both teams score): 73.3%; BTTS No (at least one team does not score): 26.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 57.6% | 1.74 |
| Draw | 21.3% | 4.69 |
| Real Racing Club de Santander win | 21.1% | 4.74 |

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
| Over 2.5 | 77.6% |
| Under 2.5 | 22.4% |
| Over 3.5 | 59.7% |
| Under 3.5 | 40.3% |
| Over 4.5 | 39.6% |
| Under 4.5 | 60.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.56% |
| 2 | 2-2 | 7.49% |
| 3 | 2-1 | 7.47% |
| 4 | 3-1 | 6.74% |
| 5 | 2-0 | 5.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 57.6% | 51.7% | 1.95 | +12.2% |
| Draw | 21.3% | 25.3% | 3.70 | -21.0% |
| Real Racing Club de Santander win | 21.1% | 23.0% | 4.32 | -8.9% |
| Over 2.5 | 77.6% | 54.6% | 1.81 | +40.5% |
| Under 2.5 | 22.4% | 45.4% | 2.17 | -51.4% |

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
| Market best home last update utc | 2026-10-11T06:31:39Z |
| Market best draw last update utc | 2026-10-11T06:31:23Z |
| Market best away last update utc | 2026-10-11T06:31:39Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Osasuna |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 73.3% |
| P btts no | 26.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 50.96 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.54 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.46 |
| Fair Over 3.5 odds | 1.67 |
| Fair Under 3.5 odds | 2.48 |
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
| Reference home odds | 1.80 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.17 |
| Home probability edge | +5.9% |
| Draw probability edge | -4.0% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +23.0% |
| Under 2.5 probability edge | -23.0% |
| Raw edge prob home | 0.1175 |
| Raw ev home | 0.2370 |
| Raw edge prob draw | -0.0793 |
| Raw ev draw | -0.3570 |
| Raw edge prob away | -0.0383 |
| Raw ev away | -0.1712 |
| Market p over 1 5 | 79.7% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T06:31:24Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 67.7% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T06:31:39Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 2.65 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 57.5% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-11T06:31:24Z |
| Market reference btts yes odds | 1.64 |
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
| Alavés win | 24.2% | 24.4% | 3.94 | -4.6% |
| Over 2.5 | 44.7% | 44.9% | 2.19 | -2.1% |
| Under 2.5 | 55.3% | 55.1% | 1.79 | -1.0% |

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
| Market best home last update utc | 2026-10-11T06:31:39Z |
| Market best draw last update utc | 2026-10-11T06:31:39Z |
| Market best away last update utc | 2026-10-11T06:31:39Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 9.00 |
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
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.19 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +0.6% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.0112 |
| Raw ev home | 0.0334 |
| Raw edge prob draw | -0.0068 |
| Raw ev draw | -0.0573 |
| Raw edge prob away | -0.0043 |
| Raw ev away | -0.0549 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.9%**. Expected goals are 0.57 for Málaga and 1.26 for Real Sociedad (1.83 combined). The most likely exact score is 0-1 at 18.4%. Goal-market probabilities: at least one goal: 84.9%; Over 2.5 goals: 27.8%; Under 3.5 goals: 89.0%; Under 4.5 goals: 96.2%; BTTS Yes (both teams score): 30.9%; BTTS No (at least one team does not score): 69.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.1% | 4.34 |
| Draw | 28.1% | 3.56 |
| Real Sociedad win | 48.9% | 2.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.57 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.83 |
| Over 0.5 | 84.9% |
| Under 0.5 | 15.1% |
| Over 1.5 | 54.0% |
| Under 1.5 | 46.0% |
| Over 2.5 | 27.8% |
| Under 2.5 | 72.2% |
| Over 3.5 | 11.0% |
| Under 3.5 | 89.0% |
| Over 4.5 | 3.8% |
| Under 4.5 | 96.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.43% |
| 2 | 0-0 | 15.12% |
| 3 | 1-0 | 12.46% |
| 4 | 0-2 | 11.70% |
| 5 | 1-1 | 10.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.1% | 29.5% | 3.30 | -23.9% |
| Draw | 28.1% | 26.0% | 3.63 | +1.9% |
| Real Sociedad win | 48.9% | 44.5% | 2.29 | +11.9% |
| Over 2.5 | 27.8% | 53.1% | 1.86 | -48.3% |
| Under 2.5 | 72.2% | 46.9% | 2.10 | +51.6% |

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
| Market best home last update utc | 2026-10-11T06:31:08Z |
| Market best draw last update utc | 2026-10-11T06:31:39Z |
| Market best away last update utc | 2026-10-11T06:31:39Z |
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
| P btts yes | 30.9% |
| P btts no | 69.1% |
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.61 |
| Fair Over 1.5 odds | 1.85 |
| Fair Under 1.5 odds | 2.17 |
| Fair Over 2.5 odds | 3.60 |
| Fair Under 2.5 odds | 1.39 |
| Fair Over 3.5 odds | 9.07 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 26.26 |
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
| Reference away odds | 2.05 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -6.4% |
| Draw probability edge | +2.1% |
| Away probability edge | +4.4% |
| Over 2.5 probability edge | -25.3% |
| Under 2.5 probability edge | +25.3% |
| Raw edge prob home | -0.1289 |
| Raw ev home | -0.4517 |
| Raw edge prob draw | 0.0414 |
| Raw ev draw | 0.0941 |
| Raw edge prob away | 0.0875 |
| Raw ev away | 0.2193 |
| Market p over 1 5 | 78.3% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T06:31:24Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 3.65 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 69.3% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T06:31:39Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 58.3% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-11T06:31:24Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.19 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.8%**. Expected goals are 2.62 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.1%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 65.9%; Under 3.5 goals: 56.3%; Under 4.5 goals: 74.7%; BTTS Yes (both teams score): 48.4%; BTTS No (at least one team does not score): 51.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.8% | 1.27 |
| Draw | 13.3% | 7.53 |
| Sevilla win | 7.9% | 12.68 |

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
| Real Madrid win | 78.8% | 80.3% | 1.30 | +2.5% |
| Draw | 13.3% | 12.1% | 7.20 | -4.4% |
| Sevilla win | 7.9% | 7.6% | 11.50 | -9.3% |
| Over 2.5 | 65.9% | 70.5% | 1.37 | -9.7% |
| Under 2.5 | 34.1% | 29.5% | 3.00 | +2.2% |

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
| Market best home last update utc | 2026-10-11T06:31:39Z |
| Market best draw last update utc | 2026-10-11T06:31:23Z |
| Market best away last update utc | 2026-10-11T06:31:25Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | Nordic Bet |
| Best under 2 5 bookmaker | Nordic Bet |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.74 |
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
| Reference away odds | 8.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -1.5% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | -0.0293 |
| Raw ev home | 0.0059 |
| Raw edge prob draw | 0.0240 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | 0.0053 |
| Raw ev away | -0.0629 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.4%**. Expected goals are 0.92 for Getafe and 0.73 for Rayo Vallecano (1.65 combined). The most likely exact score is 0-0 at 18.1%. Goal-market probabilities: at least one goal: 81.9%; Over 2.5 goals: 23.5%; Under 3.5 goals: 91.4%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 31.0%; BTTS No (at least one team does not score): 69.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.4% | 2.83 |
| Draw | 32.6% | 3.07 |
| Rayo Vallecano win | 32.1% | 3.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.92 |
| Rayo Vallecano expected goals | 0.73 |
| Expected total goals | 1.65 |
| Over 0.5 | 81.9% |
| Under 0.5 | 18.1% |
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
| 1 | 0-0 | 18.11% |
| 2 | 1-0 | 16.28% |
| 3 | 0-1 | 16.23% |
| 4 | 1-1 | 12.27% |
| 5 | 2-0 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.4% | 32.9% | 3.00 | +6.1% |
| Draw | 32.6% | 30.4% | 3.26 | +6.2% |
| Rayo Vallecano win | 32.1% | 36.7% | 2.80 | -10.2% |
| Over 2.5 | 23.5% | 38.6% | 2.54 | -40.3% |
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
| Market best home last update utc | 2026-10-11T06:31:23Z |
| Market best draw last update utc | 2026-10-11T06:31:39Z |
| Market best away last update utc | 2026-10-11T06:31:08Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Betfair |
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
| Fair Under 0.5 odds | 5.52 |
| Fair Over 1.5 odds | 2.02 |
| Fair Under 1.5 odds | 1.98 |
| Fair Over 2.5 odds | 4.25 |
| Fair Under 2.5 odds | 1.31 |
| Fair Over 3.5 odds | 11.59 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 36.65 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.8% |
| Unadjusted draw probability | 34.8% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 49.4% |
| Raw p under 3 5 | 91.4% |
| Raw p btts yes | 31.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.70 |
| Reference draw odds | 2.90 |
| Reference away odds | 2.45 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.54 |
| Reference Under 2.5 odds | 1.61 |
| Home probability edge | +2.4% |
| Draw probability edge | +2.2% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -15.0% |
| Under 2.5 probability edge | +15.0% |
| Raw edge prob home | 0.0488 |
| Raw ev home | 0.1338 |
| Raw edge prob draw | 0.0439 |
| Raw ev draw | 0.1337 |
| Raw edge prob away | -0.0927 |
| Raw ev away | -0.2319 |
| Market p over 1 5 | 65.9% |
| Market over 1 5 odds | 1.50 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T06:38:24Z |
| Market reference over 1 5 odds | 1.47 |
| Market reference over 1 5 opposite odds | 2.70 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 82.8% |
| Market under 3 5 odds | 1.17 |
| Best under 3 5 bookmaker | Codere (IT) |
| Market best under 3 5 last update utc | 2026-10-11T06:38:09Z |
| Market reference under 3 5 odds | 1.17 |
| Market reference under 3 5 opposite odds | 4.30 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 45.7% |
| Market btts yes odds | 2.05 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-11T06:38:24Z |
| Market reference btts yes odds | 2.05 |
| Market reference btts yes opposite odds | 1.75 |
| Market btts yes bookmakers | 2 |

</details>


---
