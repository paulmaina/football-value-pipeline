# La Liga — football model report

Fixtures in this report: **17**.

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
| Live odds matched | 17.00 |
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

## 2026-10-10 — Barcelona vs Getafe

The model's most likely 1X2 outcome is **Barcelona win** at **82.5%**. Expected goals are 2.38 for Barcelona and 0.59 for Getafe (2.97 combined). The most likely exact score is 2-0 at 15.6%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 58.8%; Under 3.5 goals: 64.4%; Under 4.5 goals: 81.2%; BTTS Yes (both teams score): 39.2%; BTTS No (at least one team does not score): 60.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 82.5% | 1.21 |
| Draw | 12.0% | 8.31 |
| Getafe win | 5.5% | 18.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.38 |
| Getafe expected goals | 0.59 |
| Expected total goals | 2.97 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 80.7% |
| Under 1.5 | 19.3% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 35.6% |
| Under 3.5 | 64.4% |
| Over 4.5 | 18.8% |
| Under 4.5 | 81.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 15.56% |
| 2 | 1-0 | 12.98% |
| 3 | 3-0 | 12.33% |
| 4 | 2-1 | 9.15% |
| 5 | 4-0 | 7.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 82.5% | 87.8% | 1.14 | -6.0% |
| Draw | 12.0% | 8.6% | 14.00 | +68.4% |
| Getafe win | 5.5% | 3.7% | 27.00 | +47.9% |
| Over 2.5 | 58.8% | 75.7% | 1.29 | -24.1% |
| Under 2.5 | 41.2% | 24.3% | 3.80 | +56.4% |

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
| Market best home last update utc | 2026-10-10T15:46:02Z |
| Market best draw last update utc | 2026-10-10T15:46:18Z |
| Market best away last update utc | 2026-10-10T15:45:41Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | BetOnline.ag |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Barcelona |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 39.2% |
| P btts no | 60.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.54 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.19 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.33 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 77.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 7.3% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.5% |
| Raw p btts yes | 40.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.13 |
| Reference draw odds | 10.00 |
| Reference away odds | 22.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.66 |
| Home probability edge | -5.3% |
| Draw probability edge | +3.5% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -16.9% |
| Under 2.5 probability edge | +16.9% |
| Raw edge prob home | -0.1054 |
| Raw ev home | -0.1197 |
| Raw edge prob draw | 0.0695 |
| Raw ev draw | 1.1709 |
| Raw edge prob away | 0.0359 |
| Raw ev away | 0.9635 |

</details>


---

## 2026-10-10 — Real Madrid vs Villarreal

The model's most likely 1X2 outcome is **Real Madrid win** at **70.4%**. Expected goals are 2.56 for Real Madrid and 1.12 for Villarreal (3.68 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 71.6%; Under 3.5 goals: 49.5%; Under 4.5 goals: 68.7%; BTTS Yes (both teams score): 62.0%; BTTS No (at least one team does not score): 38.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 70.4% | 1.42 |
| Draw | 16.1% | 6.21 |
| Villarreal win | 13.5% | 7.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.56 |
| Villarreal expected goals | 1.12 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 88.5% |
| Under 1.5 | 11.5% |
| Over 2.5 | 71.6% |
| Under 2.5 | 28.4% |
| Over 3.5 | 50.5% |
| Under 3.5 | 49.5% |
| Over 4.5 | 31.3% |
| Under 4.5 | 68.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.56% |
| 2 | 2-0 | 8.50% |
| 3 | 3-1 | 8.15% |
| 4 | 3-0 | 7.25% |
| 5 | 1-1 | 6.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 70.4% | 72.7% | 1.40 | -1.4% |
| Draw | 16.1% | 15.0% | 6.40 | +3.0% |
| Villarreal win | 13.5% | 12.3% | 8.00 | +7.8% |
| Over 2.5 | 71.6% | 76.4% | 1.28 | -8.3% |
| Under 2.5 | 28.4% | 23.6% | 3.76 | +6.7% |

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
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:46:01Z |
| Market best away last update utc | 2026-10-10T15:46:01Z |
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
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.68 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.68 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.52 |
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
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.36 |
| Reference draw odds | 6.20 |
| Reference away odds | 7.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.76 |
| Home probability edge | -2.2% |
| Draw probability edge | +1.1% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | -0.0445 |
| Raw ev home | -0.0452 |
| Raw edge prob draw | 0.0215 |
| Raw ev draw | 0.0992 |
| Raw edge prob away | 0.0230 |
| Raw ev away | 0.1698 |

</details>


---

## 2026-10-11 — Elche CF vs Celta Vigo

The model's most likely 1X2 outcome is **Elche CF win** at **37.8%**. Expected goals are 1.59 for Elche CF and 1.41 for Celta Vigo (3.00 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.8%; Under 3.5 goals: 64.9%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 37.8% | 2.64 |
| Draw | 26.9% | 3.72 |
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
| 2 | 1-2 | 8.21% |
| 3 | 2-1 | 8.06% |
| 4 | 0-1 | 7.17% |
| 5 | 1-0 | 7.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 37.8% | 34.0% | 3.00 | +13.4% |
| Draw | 26.9% | 29.3% | 3.35 | -9.9% |
| Celta Vigo win | 35.3% | 36.7% | 2.68 | -5.4% |
| Over 2.5 | 56.8% | 46.9% | 2.12 | +20.5% |
| Under 2.5 | 43.2% | 53.1% | 1.92 | -17.1% |

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
| Market best home last update utc | 2026-10-10T15:46:02Z |
| Market best draw last update utc | 2026-10-10T15:45:43Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Elche |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.72 |
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
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.85 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | +3.8% |
| Draw probability edge | -2.4% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | +9.9% |
| Under 2.5 probability edge | -9.9% |
| Raw edge prob home | 0.0755 |
| Raw ev home | 0.2476 |
| Raw edge prob draw | -0.0475 |
| Raw ev draw | -0.1785 |
| Raw edge prob away | -0.0280 |
| Raw ev away | -0.0917 |

</details>


---

## 2026-10-11 — Real Betis vs CA Osasuna

The model's most likely 1X2 outcome is **Real Betis win** at **60.2%**. Expected goals are 1.77 for Real Betis and 0.94 for CA Osasuna (2.71 combined). The most likely exact score is 1-0 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 51.5%; Under 3.5 goals: 70.9%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 60.2% | 1.66 |
| Draw | 22.2% | 4.50 |
| CA Osasuna win | 17.6% | 5.69 |

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
| 1 | 1-0 | 12.32% |
| 2 | 2-0 | 11.06% |
| 3 | 1-1 | 10.58% |
| 4 | 2-1 | 10.38% |
| 5 | 3-0 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 60.2% | 63.6% | 1.57 | -5.5% |
| Draw | 22.2% | 20.9% | 4.60 | +2.2% |
| CA Osasuna win | 17.6% | 15.6% | 6.60 | +16.0% |
| Over 2.5 | 51.5% | 54.4% | 1.81 | -6.7% |
| Under 2.5 | 48.5% | 45.6% | 2.18 | +5.7% |

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
| Market best home last update utc | 2026-10-10T15:46:02Z |
| Market best draw last update utc | 2026-10-10T15:45:43Z |
| Market best away last update utc | 2026-10-10T15:46:02Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
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
| Raw p over 1 5 | 75.5% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 50.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.55 |
| Reference draw odds | 4.55 |
| Reference away odds | 6.05 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -3.4% |
| Draw probability edge | +1.3% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -2.9% |
| Under 2.5 probability edge | +2.9% |
| Raw edge prob home | -0.0672 |
| Raw ev home | -0.1075 |
| Raw edge prob draw | 0.0269 |
| Raw ev draw | 0.0841 |
| Raw edge prob away | 0.0403 |
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
| Valencia win | 35.5% | 31.3% | 3.15 | +11.9% |
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
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:46:18Z |
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
| Raw ev away | 0.2534 |
| Market p over 1 5 | 78.9% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-10T15:46:20Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 4.35 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 66.7% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-10T15:46:16Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 61.3% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-10T15:46:17Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.52 |
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
| Draw | 24.5% | 23.1% | 4.30 | +5.4% |
| Deportivo La Coruña win | 23.8% | 17.3% | 6.20 | +47.8% |
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
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:46:02Z |
| Market best away last update utc | 2026-10-10T15:46:02Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
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
| Raw ev draw | 0.1153 |
| Raw edge prob away | 0.1317 |
| Raw ev away | 0.8866 |

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
| Levante win | 40.0% | 34.7% | 2.88 | +15.3% |
| Draw | 27.0% | 29.3% | 3.43 | -7.3% |
| Sevilla win | 32.9% | 36.0% | 2.75 | -9.4% |
| Over 2.5 | 54.1% | 46.9% | 2.12 | +14.7% |
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
| Market best home last update utc | 2026-10-10T15:46:02Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:46:18Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | Matchbook |
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
| Raw ev home | 0.3063 |
| Raw edge prob draw | -0.0452 |
| Raw ev draw | -0.1500 |
| Raw edge prob away | -0.0615 |
| Raw ev away | -0.1788 |

</details>


---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.3%**. Expected goals are 1.84 for Deportivo La Coruña and 1.11 for Levante (2.95 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 55.7%; Under 3.5 goals: 66.1%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.3% | 1.99 |
| Draw | 25.3% | 3.95 |
| Levante win | 24.4% | 4.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 1.84 |
| Levante expected goals | 1.11 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.7% |
| Under 2.5 | 44.3% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.87% |
| 2 | 2-1 | 9.10% |
| 3 | 1-0 | 8.76% |
| 4 | 2-0 | 8.20% |
| 5 | 1-2 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.3% | 46.2% | 2.17 | +9.1% |
| Draw | 25.3% | 27.5% | 3.62 | -8.5% |
| Levante win | 24.4% | 26.3% | 3.65 | -10.9% |
| Over 2.5 | 55.7% | 50.0% | 1.98 | +10.3% |
| Under 2.5 | 44.3% | 50.0% | 1.96 | -13.2% |

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
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:46:02Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | La Coruna |
| Matched away-team name | Levante |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.98 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.95 |
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
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.08 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.55 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.91 |
| Home probability edge | +4.1% |
| Draw probability edge | -2.2% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +5.7% |
| Under 2.5 probability edge | -5.7% |
| Raw edge prob home | 0.0819 |
| Raw ev home | 0.1801 |
| Raw edge prob draw | -0.0445 |
| Raw ev draw | -0.1650 |
| Raw edge prob away | -0.0374 |
| Raw ev away | -0.1769 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **51.5%**. Expected goals are 1.03 for Espanyol and 1.58 for Atlético Madrid (2.60 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.4%; Under 3.5 goals: 73.4%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 23.0% | 4.34 |
| Draw | 25.4% | 3.93 |
| Atlético Madrid win | 51.5% | 1.94 |

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
| 1 | 1-1 | 12.11% |
| 2 | 0-1 | 11.85% |
| 3 | 1-2 | 9.74% |
| 4 | 0-2 | 9.48% |
| 5 | 0-0 | 7.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 23.0% | 21.6% | 4.32 | -0.4% |
| Draw | 25.4% | 25.4% | 3.90 | -0.7% |
| Atlético Madrid win | 51.5% | 53.0% | 1.91 | -1.6% |
| Over 2.5 | 48.4% | 53.9% | 1.87 | -9.5% |
| Under 2.5 | 51.6% | 46.1% | 2.08 | +7.4% |

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
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:46:01Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
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
| Fair Under 0.5 odds | 13.27 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.08 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 50.0% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.5% |
| Raw p btts yes | 51.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 4.25 |
| Reference draw odds | 3.65 |
| Reference away odds | 1.82 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.06 |
| Home probability edge | +1.5% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | 0.0290 |
| Raw ev home | 0.0584 |
| Raw edge prob draw | 0.0015 |
| Raw ev draw | -0.0045 |
| Raw edge prob away | -0.0305 |
| Raw ev away | -0.0455 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **61.9%**. Expected goals are 1.32 for Real Betis and 2.05 for Barcelona (3.37 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 66.7%; Under 3.5 goals: 55.8%; Under 4.5 goals: 74.1%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.4% | 5.15 |
| Draw | 18.7% | 5.35 |
| Barcelona win | 61.9% | 1.62 |

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
| 1 | 1-2 | 10.92% |
| 2 | 0-2 | 8.24% |
| 3 | 1-1 | 8.18% |
| 4 | 0-1 | 7.90% |
| 5 | 1-3 | 7.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.4% | 14.4% | 7.00 | +36.0% |
| Draw | 18.7% | 15.8% | 6.20 | +15.9% |
| Barcelona win | 61.9% | 69.8% | 1.49 | -7.8% |
| Over 2.5 | 66.7% | 77.6% | 1.26 | -16.0% |
| Under 2.5 | 33.3% | 22.4% | 3.92 | +30.6% |

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
| Market best home last update utc | 2026-10-10T15:46:01Z |
| Market best draw last update utc | 2026-10-10T15:46:01Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.41 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.90 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 3.00 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.86 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 54.0% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 64.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 6.10 |
| Reference draw odds | 5.60 |
| Reference away odds | 1.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.92 |
| Home probability edge | +5.0% |
| Draw probability edge | +2.9% |
| Away probability edge | -7.9% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | 0.0999 |
| Raw ev home | 0.7092 |
| Raw edge prob draw | 0.0576 |
| Raw ev draw | 0.3375 |
| Raw edge prob away | -0.1574 |
| Raw ev away | -0.1952 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.0%**. Expected goals are 1.08 for Valencia and 1.17 for Athletic Bilbao (2.25 combined). The most likely exact score is 0-1 at 13.6%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.2%; Under 3.5 goals: 81.0%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.7% | 3.37 |
| Draw | 28.3% | 3.53 |
| Athletic Bilbao win | 42.0% | 2.38 |

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
| 1 | 0-1 | 13.55% |
| 2 | 1-1 | 13.14% |
| 3 | 0-0 | 10.48% |
| 4 | 1-0 | 10.05% |
| 5 | 1-2 | 8.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.7% | 26.3% | 3.71 | +10.2% |
| Draw | 28.3% | 27.5% | 3.58 | +1.4% |
| Athletic Bilbao win | 42.0% | 46.2% | 2.18 | -8.4% |
| Over 2.5 | 39.2% | 47.5% | 2.10 | -17.6% |
| Under 2.5 | 60.8% | 52.5% | 1.86 | +13.0% |

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
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
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
| P btts yes | 45.4% |
| P btts no | 54.6% |
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
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 45.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 3.55 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.08 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +3.4% |
| Draw probability edge | +0.8% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -8.2% |
| Under 2.5 probability edge | +8.2% |
| Raw edge prob home | 0.0680 |
| Raw ev home | 0.2277 |
| Raw edge prob draw | 0.0159 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | -0.0840 |
| Raw ev away | -0.1760 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.3%**. Expected goals are 2.51 for Villarreal and 1.25 for Elche CF (3.76 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 97.4%; Over 2.5 goals: 72.2%; Under 3.5 goals: 48.0%; Under 4.5 goals: 67.6%; BTTS Yes (both teams score): 65.9%; BTTS No (at least one team does not score): 34.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.3% | 1.53 |
| Draw | 19.1% | 5.23 |
| Elche CF win | 15.6% | 6.40 |

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
| Over 2.5 | 72.2% |
| Under 2.5 | 27.8% |
| Over 3.5 | 52.0% |
| Under 3.5 | 48.0% |
| Over 4.5 | 32.4% |
| Under 4.5 | 67.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.26% |
| 2 | 1-1 | 7.85% |
| 3 | 3-1 | 7.74% |
| 4 | 2-0 | 7.38% |
| 5 | 3-0 | 6.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.3% | 65.9% | 1.51 | -1.5% |
| Draw | 19.1% | 20.2% | 5.20 | -0.6% |
| Elche CF win | 15.6% | 13.9% | 6.73 | +5.2% |
| Over 2.5 | 72.2% | 64.6% | 1.50 | +8.4% |
| Under 2.5 | 27.8% | 35.4% | 2.70 | -25.0% |

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
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:42:14Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
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
| P btts yes | 65.9% |
| P btts no | 34.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 38.89 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.19 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.60 |
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
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.48 |
| Reference draw odds | 4.50 |
| Reference away odds | 6.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -0.7% |
| Draw probability edge | -1.1% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | +7.6% |
| Under 2.5 probability edge | -7.6% |
| Raw edge prob home | -0.0132 |
| Raw ev home | -0.0247 |
| Raw edge prob draw | -0.0216 |
| Raw ev draw | -0.0617 |
| Raw edge prob away | 0.0348 |
| Raw ev away | 0.1687 |
| Market p over 1 5 | 90.1% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Codere (IT) |
| Market best over 1 5 last update utc | 2026-10-10T15:45:58Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 5.45 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 56.4% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-10T15:46:22Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.25 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 60.6% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-10T15:46:17Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.40 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **57.1%**. Expected goals are 2.71 for CA Osasuna and 1.48 for Real Racing Club de Santander (4.19 combined). The most likely exact score is 1-1 at 7.7%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 77.5%; Under 3.5 goals: 40.3%; Under 4.5 goals: 60.5%; BTTS Yes (both teams score): 73.4%; BTTS No (at least one team does not score): 26.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 57.1% | 1.75 |
| Draw | 21.8% | 4.59 |
| Real Racing Club de Santander win | 21.1% | 4.73 |

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
| Over 2.5 | 77.5% |
| Under 2.5 | 22.5% |
| Over 3.5 | 59.7% |
| Under 3.5 | 40.3% |
| Over 4.5 | 39.5% |
| Under 4.5 | 60.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.72% |
| 2 | 2-2 | 7.64% |
| 3 | 2-1 | 7.40% |
| 4 | 3-1 | 6.69% |
| 5 | 2-0 | 5.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 57.1% | 50.7% | 1.95 | +11.3% |
| Draw | 21.8% | 26.2% | 3.68 | -19.8% |
| Real Racing Club de Santander win | 21.1% | 23.1% | 4.32 | -8.7% |
| Over 2.5 | 77.5% | 54.6% | 1.81 | +40.2% |
| Under 2.5 | 22.5% | 45.4% | 2.17 | -51.1% |

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
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
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
| P btts yes | 73.4% |
| P btts no | 26.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 49.92 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.52 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.44 |
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
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.90 |
| Reference draw odds | 3.55 |
| Reference away odds | 4.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.09 |
| Home probability edge | +6.4% |
| Draw probability edge | -4.4% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +22.9% |
| Under 2.5 probability edge | -22.9% |
| Raw edge prob home | 0.1271 |
| Raw ev home | 0.2370 |
| Raw edge prob draw | -0.0881 |
| Raw ev draw | -0.3605 |
| Raw edge prob away | -0.0390 |
| Raw ev away | -0.1712 |
| Market p over 1 5 | 79.8% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-10T15:45:43Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.84 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 67.3% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-10T15:46:16Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.64 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-10T15:45:43Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.15 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **48.9%**. Expected goals are 1.51 for Celta Vigo and 0.96 for Alavés (2.47 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.5%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 48.9% | 2.04 |
| Draw | 27.0% | 3.71 |
| Alavés win | 24.1% | 4.15 |

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
| 1 | 1-1 | 12.75% |
| 2 | 1-0 | 12.39% |
| 3 | 2-0 | 9.46% |
| 4 | 2-1 | 9.11% |
| 5 | 0-0 | 8.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 48.9% | 48.2% | 2.08 | +1.8% |
| Draw | 27.0% | 27.6% | 3.58 | -3.5% |
| Alavés win | 24.1% | 24.2% | 3.94 | -5.1% |
| Over 2.5 | 44.6% | 45.1% | 2.19 | -2.3% |
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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
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
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.30 |
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
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.00 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.85 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.75 |
| Home probability edge | +0.7% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0147 |
| Raw ev home | 0.0334 |
| Raw edge prob draw | -0.0125 |
| Raw ev draw | -0.0573 |
| Raw edge prob away | -0.0021 |
| Raw ev away | -0.0549 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.4%**. Expected goals are 0.57 for Málaga and 1.26 for Real Sociedad (1.83 combined). The most likely exact score is 0-1 at 18.3%. Goal-market probabilities: at least one goal: 84.7%; Over 2.5 goals: 27.7%; Under 3.5 goals: 89.0%; Under 4.5 goals: 96.2%; BTTS Yes (both teams score): 31.0%; BTTS No (at least one team does not score): 69.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.2% | 4.31 |
| Draw | 28.4% | 3.52 |
| Real Sociedad win | 48.4% | 2.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.57 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.83 |
| Over 0.5 | 84.7% |
| Under 0.5 | 15.3% |
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
| 1 | 0-1 | 18.25% |
| 2 | 0-0 | 15.30% |
| 3 | 1-0 | 12.54% |
| 4 | 0-2 | 11.58% |
| 5 | 1-1 | 11.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.2% | 29.8% | 3.30 | -23.4% |
| Draw | 28.4% | 26.7% | 3.63 | +3.1% |
| Real Sociedad win | 48.4% | 43.5% | 2.29 | +10.8% |
| Over 2.5 | 27.7% | 53.9% | 1.86 | -48.5% |
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
| Market best home last update utc | 2026-10-10T15:42:14Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
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
| Fair Under 0.5 odds | 6.53 |
| Fair Over 1.5 odds | 1.85 |
| Fair Under 1.5 odds | 2.17 |
| Fair Over 2.5 odds | 3.61 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.10 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 26.40 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 16.6% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 53.2% |
| Raw p over 1 5 | 54.7% |
| Raw p under 3 5 | 88.7% |
| Raw p btts yes | 31.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 3.15 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.06 |
| Home probability edge | -6.6% |
| Draw probability edge | +1.7% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -26.2% |
| Under 2.5 probability edge | +26.2% |
| Raw edge prob home | -0.1319 |
| Raw ev home | -0.4517 |
| Raw edge prob draw | 0.0347 |
| Raw ev draw | 0.0941 |
| Raw edge prob away | 0.0972 |
| Raw ev away | 0.2193 |
| Market p over 1 5 | 77.8% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-10T15:45:43Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 68.7% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-10T15:46:33Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.90 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 58.9% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-10T15:45:43Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.25 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **77.2%**. Expected goals are 2.62 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 11.8%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.2%; Under 3.5 goals: 56.6%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 48.9%; BTTS No (at least one team does not score): 51.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.2% | 1.29 |
| Draw | 15.0% | 6.67 |
| Sevilla win | 7.8% | 12.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.62 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 65.2% |
| Under 2.5 | 34.8% |
| Over 3.5 | 43.4% |
| Under 3.5 | 56.6% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.85% |
| 2 | 3-0 | 10.35% |
| 3 | 1-0 | 8.94% |
| 4 | 2-1 | 8.82% |
| 5 | 3-1 | 7.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.2% | 77.1% | 1.30 | +0.4% |
| Draw | 15.0% | 15.5% | 7.00 | +5.0% |
| Sevilla win | 7.8% | 7.4% | 11.50 | -10.7% |
| Over 2.5 | 65.2% | 70.0% | 1.39 | -9.4% |
| Under 2.5 | 34.8% | 30.0% | 3.05 | +6.2% |

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
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:45:43Z |
| Market best away last update utc | 2026-10-10T15:46:02Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.9% |
| P btts no | 51.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.21 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.68 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.87 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
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
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.27 |
| Reference draw odds | 5.55 |
| Reference away odds | 11.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | +0.1% |
| Draw probability edge | -0.5% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | 0.0026 |
| Raw ev home | 0.0059 |
| Raw edge prob draw | -0.0104 |
| Raw ev draw | 0.0132 |
| Raw edge prob away | 0.0078 |
| Raw ev away | -0.0629 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.6%**. Expected goals are 0.92 for Getafe and 0.73 for Rayo Vallecano (1.65 combined). The most likely exact score is 0-0 at 18.1%. Goal-market probabilities: at least one goal: 81.9%; Over 2.5 goals: 23.5%; Under 3.5 goals: 91.4%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 31.0%; BTTS No (at least one team does not score): 69.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.6% | 2.81 |
| Draw | 32.5% | 3.07 |
| Rayo Vallecano win | 31.8% | 3.14 |

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
| 1 | 0-0 | 18.08% |
| 2 | 1-0 | 16.41% |
| 3 | 0-1 | 16.10% |
| 4 | 1-1 | 12.26% |
| 5 | 2-0 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.6% | 33.5% | 2.97 | +5.9% |
| Draw | 32.5% | 30.3% | 3.26 | +6.1% |
| Rayo Vallecano win | 31.8% | 36.2% | 2.80 | -10.9% |
| Over 2.5 | 23.5% | 37.6% | 2.54 | -40.2% |
| Under 2.5 | 76.5% | 62.4% | 1.61 | +23.1% |

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
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:46:16Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 9.00 |
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
| Fair Under 0.5 odds | 5.53 |
| Fair Over 1.5 odds | 2.02 |
| Fair Under 1.5 odds | 1.98 |
| Fair Over 2.5 odds | 4.25 |
| Fair Under 2.5 odds | 1.31 |
| Fair Over 3.5 odds | 11.58 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 36.62 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.8% |
| Unadjusted draw probability | 34.8% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 49.4% |
| Raw p under 3 5 | 91.4% |
| Raw p btts yes | 31.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.82 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.62 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.48 |
| Reference Under 2.5 odds | 1.55 |
| Home probability edge | +2.1% |
| Draw probability edge | +2.2% |
| Away probability edge | -4.4% |
| Over 2.5 probability edge | -14.1% |
| Under 2.5 probability edge | +14.1% |
| Raw edge prob home | 0.0430 |
| Raw ev home | 0.1225 |
| Raw edge prob draw | 0.0447 |
| Raw ev draw | 0.1337 |
| Raw edge prob away | -0.0877 |
| Raw ev away | -0.2319 |
| Market p over 1 5 | 66.0% |
| Market over 1 5 odds | 1.50 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-10T15:45:43Z |
| Market reference over 1 5 odds | 1.42 |
| Market reference over 1 5 opposite odds | 2.48 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 83.6% |
| Market under 3 5 odds | 1.16 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-10T15:45:17Z |
| Market reference under 3 5 odds | 1.16 |
| Market reference under 3 5 opposite odds | 4.50 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 45.7% |
| Market btts yes odds | 2.05 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-10T15:45:43Z |
| Market reference btts yes odds | 2.05 |
| Market reference btts yes opposite odds | 1.75 |
| Market btts yes bookmakers | 2 |

</details>


---
