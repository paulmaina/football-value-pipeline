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
| Additional event odds calls this league | 4.00 |
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

The model's most likely 1X2 outcome is **Elche CF win** at **37.4%**. Expected goals are 1.59 for Elche CF and 1.41 for Celta Vigo (3.00 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 57.0%; Under 3.5 goals: 64.9%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 60.8%; BTTS No (at least one team does not score): 39.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 37.4% | 2.67 |
| Draw | 26.4% | 3.79 |
| Celta Vigo win | 36.2% | 2.76 |

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
| 1 | 1-1 | 12.18% |
| 2 | 1-2 | 8.43% |
| 3 | 2-1 | 7.97% |
| 4 | 0-1 | 7.36% |
| 5 | 1-0 | 6.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 37.4% | 33.2% | 3.06 | +14.5% |
| Draw | 26.4% | 28.2% | 3.40 | -10.4% |
| Celta Vigo win | 36.2% | 38.6% | 2.61 | -5.5% |
| Over 2.5 | 57.0% | 47.5% | 2.07 | +18.0% |
| Under 2.5 | 43.0% | 52.5% | 1.93 | -17.0% |

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
| Market best home last update utc | 2026-10-11T08:22:55Z |
| Market best draw last update utc | 2026-10-11T08:22:37Z |
| Market best away last update utc | 2026-10-11T08:22:24Z |
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
| Fair Under 0.5 odds | 18.08 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.75 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.07 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +4.2% |
| Draw probability edge | -1.8% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | +9.5% |
| Under 2.5 probability edge | -9.5% |
| Raw edge prob home | 0.0834 |
| Raw ev home | 0.2726 |
| Raw edge prob draw | -0.0367 |
| Raw ev draw | -0.1662 |
| Raw edge prob away | -0.0467 |
| Raw ev away | -0.1155 |

</details>


---

## 2026-10-11 — Real Betis vs CA Osasuna

The model's most likely 1X2 outcome is **Real Betis win** at **61.3%**. Expected goals are 1.77 for Real Betis and 0.94 for CA Osasuna (2.71 combined). The most likely exact score is 1-0 at 12.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 51.9%; Under 3.5 goals: 70.7%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 61.3% | 1.63 |
| Draw | 21.3% | 4.70 |
| CA Osasuna win | 17.4% | 5.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.77 |
| CA Osasuna expected goals | 0.94 |
| Expected total goals | 2.71 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 29.3% |
| Under 3.5 | 70.7% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.55% |
| 2 | 2-0 | 11.27% |
| 3 | 2-1 | 10.57% |
| 4 | 1-1 | 10.12% |
| 5 | 3-0 | 6.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 61.3% | 65.8% | 1.57 | -3.7% |
| Draw | 21.3% | 19.0% | 4.62 | -1.7% |
| CA Osasuna win | 17.4% | 15.2% | 7.00 | +21.8% |
| Over 2.5 | 51.9% | 54.6% | 1.81 | -6.1% |
| Under 2.5 | 48.1% | 45.4% | 2.26 | +8.7% |

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
| Market best home last update utc | 2026-10-11T08:22:55Z |
| Market best draw last update utc | 2026-10-11T08:22:55Z |
| Market best away last update utc | 2026-10-11T08:22:37Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Betis |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.27 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.15 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.42 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.00 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 56.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 19.6% |
| Raw p over 1 5 | 75.5% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 50.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.46 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.50 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.17 |
| Home probability edge | -4.5% |
| Draw probability edge | +2.3% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | -0.0898 |
| Raw ev home | -0.1075 |
| Raw edge prob draw | 0.0459 |
| Raw ev draw | 0.0888 |
| Raw edge prob away | 0.0439 |
| Raw ev away | 0.3710 |

</details>


---

## 2026-10-11 — Real Racing Club de Santander vs Valencia

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **41.2%**. Expected goals are 1.92 for Real Racing Club de Santander and 1.95 for Valencia (3.87 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 73.6%; Under 3.5 goals: 45.9%; Under 4.5 goals: 65.8%; BTTS Yes (both teams score): 73.8%; BTTS No (at least one team does not score): 26.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 41.2% | 2.43 |
| Draw | 23.5% | 4.26 |
| Valencia win | 35.3% | 2.83 |

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
| Over 4.5 | 34.2% |
| Under 4.5 | 65.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.72% |
| 2 | 2-2 | 8.05% |
| 3 | 2-1 | 7.95% |
| 4 | 1-2 | 6.74% |
| 5 | 3-1 | 5.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 41.2% | 43.5% | 2.34 | -3.5% |
| Draw | 23.5% | 25.6% | 3.67 | -13.9% |
| Valencia win | 35.3% | 30.9% | 3.30 | +16.6% |
| Over 2.5 | 73.6% | 56.8% | 1.74 | +28.2% |
| Under 2.5 | 26.4% | 43.2% | 2.27 | -40.2% |

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
| Market best home last update utc | 2026-10-11T08:22:55Z |
| Market best draw last update utc | 2026-10-11T08:22:55Z |
| Market best away last update utc | 2026-10-11T08:22:53Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Valencia |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 73.8% |
| P btts no | 26.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.41 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.96 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.79 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.95 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | -2.3% |
| Draw probability edge | -2.2% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | +16.9% |
| Under 2.5 probability edge | -16.9% |
| Raw edge prob home | -0.0460 |
| Raw ev home | -0.0893 |
| Raw edge prob draw | -0.0433 |
| Raw ev draw | -0.2186 |
| Raw edge prob away | 0.0893 |
| Raw ev away | 0.3131 |
| Market p over 1 5 | 79.7% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:22:24Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.55 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:22:53Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.67 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 62.3% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:22:38Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Real Sociedad vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Real Sociedad win** at **52.1%**. Expected goals are 1.49 for Real Sociedad and 1.20 for Deportivo La Coruña (2.68 combined). The most likely exact score is 1-0 at 11.9%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.1%; Under 3.5 goals: 71.4%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 53.6%; BTTS No (at least one team does not score): 46.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 52.1% | 1.92 |
| Draw | 23.9% | 4.18 |
| Deportivo La Coruña win | 24.0% | 4.17 |

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
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 28.6% |
| Under 3.5 | 71.4% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.90% |
| 2 | 1-1 | 11.37% |
| 3 | 2-1 | 10.78% |
| 4 | 2-0 | 8.99% |
| 5 | 0-0 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 52.1% | 60.6% | 1.67 | -13.0% |
| Draw | 23.9% | 21.9% | 4.21 | +0.7% |
| Deportivo La Coruña win | 24.0% | 17.5% | 5.90 | +41.5% |
| Over 2.5 | 51.1% | 54.4% | 1.81 | -7.5% |
| Under 2.5 | 48.9% | 45.6% | 2.22 | +8.5% |

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
| Market best home last update utc | 2026-10-11T08:22:37Z |
| Market best draw last update utc | 2026-10-11T08:22:55Z |
| Market best away last update utc | 2026-10-11T08:22:37Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
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
| Fair Under 0.5 odds | 15.50 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.05 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.23 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 54.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.90 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -8.5% |
| Draw probability edge | +2.0% |
| Away probability edge | +6.5% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | -0.1694 |
| Raw ev home | -0.2713 |
| Raw edge prob draw | 0.0404 |
| Raw ev draw | 0.0919 |
| Raw edge prob away | 0.1290 |
| Raw ev away | 0.7953 |

</details>


---

## 2026-10-12 — Levante vs Sevilla

The model's most likely 1X2 outcome is **Levante win** at **40.4%**. Expected goals are 1.61 for Levante and 1.27 for Sevilla (2.88 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 54.3%; Under 3.5 goals: 67.6%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 58.1%; BTTS No (at least one team does not score): 41.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 40.4% | 2.48 |
| Draw | 26.3% | 3.81 |
| Sevilla win | 33.4% | 3.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.61 |
| Sevilla expected goals | 1.27 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.3% |
| Under 2.5 | 45.7% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.33% |
| 2 | 2-1 | 8.24% |
| 3 | 1-2 | 8.12% |
| 4 | 1-0 | 7.92% |
| 5 | 0-1 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 40.4% | 35.4% | 2.87 | +15.8% |
| Draw | 26.3% | 27.7% | 3.43 | -9.9% |
| Sevilla win | 33.4% | 36.9% | 2.74 | -8.5% |
| Over 2.5 | 54.3% | 46.9% | 2.12 | +15.2% |
| Under 2.5 | 45.7% | 53.1% | 1.86 | -15.1% |

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
| Market best home last update utc | 2026-10-11T08:22:55Z |
| Market best draw last update utc | 2026-10-11T08:22:55Z |
| Market best away last update utc | 2026-10-11T08:22:37Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.34 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.59 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.17 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 45.4% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 29.9% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 57.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.86 |
| Home probability edge | +5.0% |
| Draw probability edge | -1.5% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | +7.4% |
| Under 2.5 probability edge | -7.4% |
| Raw edge prob home | 0.1000 |
| Raw ev home | 0.3018 |
| Raw edge prob draw | -0.0296 |
| Raw ev draw | -0.1500 |
| Raw edge prob away | -0.0704 |
| Raw ev away | -0.1818 |

</details>


---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.2%**. Expected goals are 1.84 for Deportivo La Coruña and 1.11 for Levante (2.95 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.2%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.2% | 1.99 |
| Draw | 24.7% | 4.06 |
| Levante win | 25.1% | 3.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 1.84 |
| Levante expected goals | 1.11 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.8% |
| Under 3.5 | 66.2% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.57% |
| 2 | 2-1 | 9.09% |
| 3 | 1-0 | 8.75% |
| 4 | 2-0 | 8.19% |
| 5 | 1-2 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.2% | 46.1% | 2.17 | +9.0% |
| Draw | 24.7% | 26.2% | 3.62 | -10.7% |
| Levante win | 25.1% | 27.7% | 3.60 | -9.6% |
| Over 2.5 | 55.9% | 49.7% | 1.98 | +10.7% |
| Under 2.5 | 44.1% | 50.3% | 1.96 | -13.5% |

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
| Market best home last update utc | 2026-10-11T08:22:55Z |
| Market best draw last update utc | 2026-10-11T08:22:55Z |
| Market best away last update utc | 2026-10-11T08:22:55Z |
| Odds bookmakers 1x2 | 15.00 |
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
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.42 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.98 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.98 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | +4.2% |
| Draw probability edge | -1.6% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | +6.1% |
| Under 2.5 probability edge | -6.1% |
| Raw edge prob home | 0.0832 |
| Raw ev home | 0.1801 |
| Raw edge prob draw | -0.0318 |
| Raw ev draw | -0.1650 |
| Raw edge prob away | -0.0514 |
| Raw ev away | -0.1882 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **52.3%**. Expected goals are 1.03 for Espanyol and 1.58 for Atlético Madrid (2.60 combined). The most likely exact score is 0-1 at 12.0%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 48.7%; Under 3.5 goals: 73.3%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 23.1% | 4.32 |
| Draw | 24.6% | 4.07 |
| Atlético Madrid win | 52.3% | 1.91 |

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
| 1 | 0-1 | 12.03% |
| 2 | 1-1 | 11.69% |
| 3 | 1-2 | 9.89% |
| 4 | 0-2 | 9.63% |
| 5 | 0-0 | 7.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 23.1% | 21.8% | 4.60 | +6.4% |
| Draw | 24.6% | 23.6% | 3.84 | -5.7% |
| Atlético Madrid win | 52.3% | 54.6% | 1.91 | -0.1% |
| Over 2.5 | 48.7% | 52.7% | 1.87 | -9.0% |
| Under 2.5 | 51.3% | 47.3% | 2.08 | +6.7% |

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
| Market best home last update utc | 2026-10-11T08:22:37Z |
| Market best draw last update utc | 2026-10-11T08:22:55Z |
| Market best away last update utc | 2026-10-11T08:22:55Z |
| Odds bookmakers 1x2 | 15.00 |
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
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.74 |
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
| Reference home odds | 3.70 |
| Reference draw odds | 3.45 |
| Reference away odds | 1.68 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | +1.4% |
| Draw probability edge | +1.0% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | 0.0274 |
| Raw ev home | 0.1270 |
| Raw edge prob draw | 0.0191 |
| Raw ev draw | -0.0198 |
| Raw edge prob away | -0.0465 |
| Raw ev away | -0.0455 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **62.2%**. Expected goals are 1.32 for Real Betis and 2.05 for Barcelona (3.37 combined). The most likely exact score is 1-2 at 11.0%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 67.1%; Under 3.5 goals: 55.8%; Under 4.5 goals: 73.9%; BTTS Yes (both teams score): 62.8%; BTTS No (at least one team does not score): 37.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 20.4% | 4.90 |
| Draw | 17.4% | 5.75 |
| Barcelona win | 62.2% | 1.61 |

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
| Over 3.5 | 44.2% |
| Under 3.5 | 55.8% |
| Over 4.5 | 26.1% |
| Under 4.5 | 73.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.97% |
| 2 | 0-2 | 8.28% |
| 3 | 0-1 | 7.94% |
| 4 | 1-1 | 7.61% |
| 5 | 1-3 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 20.4% | 16.4% | 6.50 | +32.8% |
| Draw | 17.4% | 13.2% | 6.20 | +7.8% |
| Barcelona win | 62.2% | 70.4% | 1.49 | -7.3% |
| Over 2.5 | 67.1% | 77.0% | 1.27 | -14.8% |
| Under 2.5 | 32.9% | 23.0% | 3.82 | +25.7% |

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
| Market best home last update utc | 2026-10-11T08:22:22Z |
| Market best draw last update utc | 2026-10-11T08:22:37Z |
| Market best away last update utc | 2026-10-11T08:22:55Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 62.8% |
| P btts no | 37.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.84 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.90 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.50 |
| Reference draw odds | 5.40 |
| Reference away odds | 1.34 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.82 |
| Home probability edge | +4.0% |
| Draw probability edge | +4.2% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | 0.0799 |
| Raw ev home | 0.5871 |
| Raw edge prob draw | 0.0837 |
| Raw ev draw | 0.3375 |
| Raw edge prob away | -0.1636 |
| Raw ev away | -0.1952 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.4%**. Expected goals are 1.08 for Valencia and 1.17 for Athletic Bilbao (2.25 combined). The most likely exact score is 0-1 at 13.7%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 39.5%; Under 3.5 goals: 80.9%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 45.2%; BTTS No (at least one team does not score): 54.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.0% | 3.33 |
| Draw | 27.6% | 3.63 |
| Athletic Bilbao win | 42.4% | 2.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.08 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.25 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 66.0% |
| Under 1.5 | 34.0% |
| Over 2.5 | 39.5% |
| Under 2.5 | 60.5% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.68% |
| 2 | 1-1 | 12.79% |
| 3 | 0-0 | 10.20% |
| 4 | 1-0 | 10.17% |
| 5 | 1-2 | 8.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.0% | 27.0% | 3.75 | +12.7% |
| Draw | 27.6% | 26.0% | 3.58 | -1.3% |
| Athletic Bilbao win | 42.4% | 47.0% | 2.18 | -7.6% |
| Over 2.5 | 39.5% | 46.9% | 2.10 | -17.1% |
| Under 2.5 | 60.5% | 53.1% | 1.86 | +12.6% |

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
| Market best home last update utc | 2026-10-11T08:22:37Z |
| Market best draw last update utc | 2026-10-11T08:22:55Z |
| Market best away last update utc | 2026-10-11T08:22:55Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.2% |
| P btts no | 54.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.80 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.67 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.1% |
| Unadjusted away-win probability | 37.8% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 45.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.20 |
| Reference away odds | 1.92 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.86 |
| Home probability edge | +3.1% |
| Draw probability edge | +1.5% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | 0.0610 |
| Raw ev home | 0.2409 |
| Raw edge prob draw | 0.0309 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | -0.0919 |
| Raw ev away | -0.1760 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.8%**. Expected goals are 2.51 for Villarreal and 1.25 for Elche CF (3.76 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 72.6%; Under 3.5 goals: 48.0%; Under 4.5 goals: 67.4%; BTTS Yes (both teams score): 65.6%; BTTS No (at least one team does not score): 34.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.8% | 1.52 |
| Draw | 17.8% | 5.61 |
| Elche CF win | 16.4% | 6.10 |

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
| Over 3.5 | 52.0% |
| Under 3.5 | 48.0% |
| Over 4.5 | 32.6% |
| Under 4.5 | 67.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.33% |
| 2 | 3-1 | 7.80% |
| 3 | 2-0 | 7.44% |
| 4 | 1-1 | 7.32% |
| 5 | 3-0 | 6.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.8% | 67.0% | 1.51 | -0.7% |
| Draw | 17.8% | 17.6% | 5.20 | -7.3% |
| Elche CF win | 16.4% | 15.4% | 6.73 | +10.4% |
| Over 2.5 | 72.6% | 64.6% | 1.50 | +8.9% |
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
| Market best home last update utc | 2026-10-11T08:22:55Z |
| Market best draw last update utc | 2026-10-11T08:22:22Z |
| Market best away last update utc | 2026-10-11T08:22:55Z |
| Odds bookmakers 1x2 | 16.00 |
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
| Fair Under 0.5 odds | 41.73 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.19 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.65 |
| Fair Over 3.5 odds | 1.92 |
| Fair Under 3.5 odds | 2.08 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.40 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -1.2% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +8.0% |
| Under 2.5 probability edge | -8.0% |
| Raw edge prob home | -0.0238 |
| Raw ev home | -0.0247 |
| Raw edge prob draw | 0.0045 |
| Raw ev draw | -0.0617 |
| Raw edge prob away | 0.0193 |
| Raw ev away | 0.1687 |
| Market p over 1 5 | 90.1% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:22:06Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 5.45 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 56.4% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T08:23:03Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.25 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 59.9% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:22:39Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.26 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **57.6%**. Expected goals are 2.71 for CA Osasuna and 1.48 for Real Racing Club de Santander (4.19 combined). The most likely exact score is 2-1 at 7.5%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 77.7%; Under 3.5 goals: 40.3%; Under 4.5 goals: 60.3%; BTTS Yes (both teams score): 73.2%; BTTS No (at least one team does not score): 26.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 57.6% | 1.74 |
| Draw | 20.9% | 4.79 |
| Real Racing Club de Santander win | 21.6% | 4.64 |

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
| Over 3.5 | 59.7% |
| Under 3.5 | 40.3% |
| Over 4.5 | 39.7% |
| Under 4.5 | 60.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 7.47% |
| 2 | 1-1 | 7.40% |
| 3 | 2-2 | 7.32% |
| 4 | 3-1 | 6.74% |
| 5 | 1-2 | 5.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 57.6% | 51.7% | 1.95 | +12.2% |
| Draw | 20.9% | 24.4% | 3.68 | -23.2% |
| Real Racing Club de Santander win | 21.6% | 24.0% | 4.32 | -6.8% |
| Over 2.5 | 77.7% | 54.6% | 1.81 | +40.7% |
| Under 2.5 | 22.3% | 45.4% | 2.17 | -51.6% |

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
| Market best home last update utc | 2026-10-11T08:22:55Z |
| Market best draw last update utc | 2026-10-11T08:22:55Z |
| Market best away last update utc | 2026-10-11T08:22:55Z |
| Odds bookmakers 1x2 | 15.00 |
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
| P btts yes | 73.2% |
| P btts no | 26.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 52.10 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.53 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.49 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.76 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.17 |
| Home probability edge | +5.9% |
| Draw probability edge | -3.5% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | +23.1% |
| Under 2.5 probability edge | -23.1% |
| Raw edge prob home | 0.1176 |
| Raw ev home | 0.2370 |
| Raw edge prob draw | -0.0699 |
| Raw ev draw | -0.3605 |
| Raw edge prob away | -0.0477 |
| Raw ev away | -0.1712 |
| Market p over 1 5 | 79.7% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:22:06Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 68.6% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:22:53Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.87 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 57.5% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-11T08:22:06Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.15 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **49.0%**. Expected goals are 1.51 for Celta Vigo and 0.96 for Alavés (2.47 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 44.7%; Under 3.5 goals: 76.5%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 49.0% | 2.04 |
| Draw | 26.5% | 3.78 |
| Alavés win | 24.6% | 4.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.51 |
| Alavés expected goals | 0.96 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 70.7% |
| Under 1.5 | 29.3% |
| Over 2.5 | 44.7% |
| Under 2.5 | 55.3% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.51% |
| 2 | 1-0 | 12.40% |
| 3 | 2-0 | 9.46% |
| 4 | 2-1 | 9.11% |
| 5 | 0-0 | 8.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 49.0% | 48.2% | 2.08 | +1.8% |
| Draw | 26.5% | 26.6% | 3.58 | -5.3% |
| Alavés win | 24.6% | 25.2% | 3.94 | -3.1% |
| Over 2.5 | 44.7% | 44.9% | 2.19 | -2.0% |
| Under 2.5 | 55.3% | 55.1% | 1.79 | -1.1% |

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
| Market best home last update utc | 2026-10-11T08:22:55Z |
| Market best draw last update utc | 2026-10-11T08:22:55Z |
| Market best away last update utc | 2026-10-11T08:22:55Z |
| Odds bookmakers 1x2 | 15.00 |
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
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.52 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.58 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 70.8% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.15 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.19 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +0.7% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0144 |
| Raw ev home | 0.0334 |
| Raw edge prob draw | -0.0025 |
| Raw ev draw | -0.0573 |
| Raw edge prob away | -0.0120 |
| Raw ev away | -0.0549 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.9%**. Expected goals are 0.57 for Málaga and 1.26 for Real Sociedad (1.83 combined). The most likely exact score is 0-1 at 18.4%. Goal-market probabilities: at least one goal: 85.1%; Over 2.5 goals: 27.9%; Under 3.5 goals: 89.0%; Under 4.5 goals: 96.2%; BTTS Yes (both teams score): 30.9%; BTTS No (at least one team does not score): 69.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.4% | 4.28 |
| Draw | 27.7% | 3.61 |
| Real Sociedad win | 48.9% | 2.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.57 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.83 |
| Over 0.5 | 85.1% |
| Under 0.5 | 14.9% |
| Over 1.5 | 54.0% |
| Under 1.5 | 46.0% |
| Over 2.5 | 27.9% |
| Under 2.5 | 72.1% |
| Over 3.5 | 11.0% |
| Under 3.5 | 89.0% |
| Over 4.5 | 3.8% |
| Under 4.5 | 96.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.45% |
| 2 | 0-0 | 14.94% |
| 3 | 1-0 | 12.62% |
| 4 | 0-2 | 11.71% |
| 5 | 1-1 | 10.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.4% | 30.1% | 3.30 | -22.9% |
| Draw | 27.7% | 25.3% | 3.63 | +0.6% |
| Real Sociedad win | 48.9% | 44.6% | 2.29 | +12.0% |
| Over 2.5 | 27.9% | 53.1% | 1.86 | -48.1% |
| Under 2.5 | 72.1% | 46.9% | 2.10 | +51.4% |

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
| Market best home last update utc | 2026-10-11T08:22:22Z |
| Market best draw last update utc | 2026-10-11T08:22:55Z |
| Market best away last update utc | 2026-10-11T08:22:55Z |
| Odds bookmakers 1x2 | 15.00 |
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
| P btts yes | 30.9% |
| P btts no | 69.1% |
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.70 |
| Fair Over 1.5 odds | 1.85 |
| Fair Under 1.5 odds | 2.17 |
| Fair Over 2.5 odds | 3.59 |
| Fair Under 2.5 odds | 1.39 |
| Fair Over 3.5 odds | 9.07 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 26.18 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 16.6% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 53.2% |
| Raw p over 1 5 | 54.7% |
| Raw p under 3 5 | 88.7% |
| Raw p btts yes | 31.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -6.7% |
| Draw probability edge | +2.4% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -25.2% |
| Under 2.5 probability edge | +25.2% |
| Raw edge prob home | -0.1350 |
| Raw ev home | -0.4517 |
| Raw edge prob draw | 0.0483 |
| Raw ev draw | 0.0941 |
| Raw edge prob away | 0.0867 |
| Raw ev away | 0.2193 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **80.0%**. Expected goals are 2.62 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.3%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 66.4%; Under 3.5 goals: 56.0%; Under 4.5 goals: 74.5%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 80.0% | 1.25 |
| Draw | 12.4% | 8.07 |
| Sevilla win | 7.6% | 13.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.62 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 66.4% |
| Under 2.5 | 33.6% |
| Over 3.5 | 44.0% |
| Under 3.5 | 56.0% |
| Over 4.5 | 25.5% |
| Under 4.5 | 74.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.27% |
| 2 | 3-0 | 10.73% |
| 3 | 1-0 | 9.27% |
| 4 | 2-1 | 9.14% |
| 5 | 3-1 | 7.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 80.0% | 82.7% | 1.30 | +4.0% |
| Draw | 12.4% | 10.3% | 7.20 | -10.8% |
| Sevilla win | 7.6% | 7.0% | 12.00 | -9.2% |
| Over 2.5 | 66.4% | 70.1% | 1.39 | -7.7% |
| Under 2.5 | 33.6% | 29.9% | 3.07 | +3.2% |

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
| Market best home last update utc | 2026-10-11T08:22:55Z |
| Market best draw last update utc | 2026-10-11T08:22:37Z |
| Market best away last update utc | 2026-10-11T08:22:06Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.92 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.85 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.97 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.92 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.16 |
| Reference draw odds | 5.90 |
| Reference away odds | 8.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.07 |
| Home probability edge | -2.7% |
| Draw probability edge | +2.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | -0.0532 |
| Raw ev home | 0.0059 |
| Raw edge prob draw | 0.0416 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | 0.0116 |
| Raw ev away | -0.0221 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.8%**. Expected goals are 0.92 for Getafe and 0.73 for Rayo Vallecano (1.65 combined). The most likely exact score is 0-0 at 17.9%. Goal-market probabilities: at least one goal: 82.1%; Over 2.5 goals: 23.6%; Under 3.5 goals: 91.4%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 31.0%; BTTS No (at least one team does not score): 69.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.8% | 2.79 |
| Draw | 32.3% | 3.10 |
| Rayo Vallecano win | 31.9% | 3.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.92 |
| Rayo Vallecano expected goals | 0.73 |
| Expected total goals | 1.65 |
| Over 0.5 | 82.1% |
| Under 0.5 | 17.9% |
| Over 1.5 | 49.4% |
| Under 1.5 | 50.6% |
| Over 2.5 | 23.6% |
| Under 2.5 | 76.4% |
| Over 3.5 | 8.6% |
| Under 3.5 | 91.4% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 17.94% |
| 2 | 1-0 | 16.50% |
| 3 | 0-1 | 16.14% |
| 4 | 1-1 | 12.16% |
| 5 | 2-0 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.8% | 33.9% | 2.98 | +6.8% |
| Draw | 32.3% | 29.8% | 3.26 | +5.2% |
| Rayo Vallecano win | 31.9% | 36.3% | 2.80 | -10.7% |
| Over 2.5 | 23.6% | 38.6% | 2.54 | -40.1% |
| Under 2.5 | 76.4% | 61.4% | 1.61 | +23.0% |

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
| Market best home last update utc | 2026-10-11T08:22:37Z |
| Market best draw last update utc | 2026-10-11T08:22:55Z |
| Market best away last update utc | 2026-10-11T08:22:54Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 10.00 |
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
| Fair Under 0.5 odds | 5.57 |
| Fair Over 1.5 odds | 2.02 |
| Fair Under 1.5 odds | 1.98 |
| Fair Over 2.5 odds | 4.24 |
| Fair Under 2.5 odds | 1.31 |
| Fair Over 3.5 odds | 11.57 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 36.50 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.8% |
| Unadjusted draw probability | 34.8% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 49.4% |
| Raw p under 3 5 | 91.4% |
| Raw p btts yes | 31.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.55 |
| Reference draw odds | 2.85 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.54 |
| Reference Under 2.5 odds | 1.61 |
| Home probability edge | +2.0% |
| Draw probability edge | +2.5% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -14.9% |
| Under 2.5 probability edge | +14.9% |
| Raw edge prob home | 0.0392 |
| Raw ev home | 0.1262 |
| Raw edge prob draw | 0.0499 |
| Raw ev draw | 0.1337 |
| Raw edge prob away | -0.0891 |
| Raw ev away | -0.2319 |
| Market p over 1 5 | 65.9% |
| Market over 1 5 odds | 1.50 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:22:06Z |
| Market reference over 1 5 odds | 1.47 |
| Market reference over 1 5 opposite odds | 2.70 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 83.6% |
| Market under 3 5 odds | 1.17 |
| Best under 3 5 bookmaker | Codere (IT) |
| Market best under 3 5 last update utc | 2026-10-11T08:22:21Z |
| Market reference under 3 5 odds | 1.16 |
| Market reference under 3 5 opposite odds | 4.50 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 46.1% |
| Market btts yes odds | 2.05 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-11T08:22:06Z |
| Market reference btts yes odds | 2.00 |
| Market reference btts yes opposite odds | 1.74 |
| Market btts yes bookmakers | 2 |

</details>


---
