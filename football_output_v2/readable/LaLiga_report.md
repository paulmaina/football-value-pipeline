# La Liga — football model report

Fixtures in this report: **11**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,218 |
| Training data through | 2026-10-12 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1999.336 |
| Base scoring parameter | 0.091 |
| Home-advantage parameter | 0.282 |
| Dixon-Coles low-score adjustment | -0.020 |
| Xi per day | 0.0009 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 11.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.2%**. Expected goals are 2.04 for Deportivo La Coruña and 1.32 for Levante (3.36 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.4%; Under 3.5 goals: 57.0%; Double Chance 1X: 74.4%; Double Chance X2: 49.8%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.2% | 1.99 |
| Draw | 24.2% | 4.13 |
| Levante win | 25.6% | 3.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 2.04 |
| Levante expected goals | 1.32 |
| Expected total goals | 3.36 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 84.9% |
| Under 1.5 | 15.1% |
| Over 2.5 | 64.4% |
| Under 2.5 | 35.6% |
| Over 3.5 | 43.0% |
| Under 3.5 | 57.0% |
| Over 4.5 | 24.3% |
| Under 4.5 | 75.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.63% |
| 2 | 2-1 | 8.89% |
| 3 | 2-2 | 7.02% |
| 4 | 2-0 | 6.73% |
| 5 | 1-2 | 6.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.2% | 46.6% | 2.17 | +9.0% |
| Draw | 24.2% | 26.7% | 3.62 | -12.3% |
| Levante win | 25.6% | 26.7% | 3.80 | -2.9% |
| Over 2.5 | 64.4% | 50.7% | 1.98 | +27.4% |
| Under 2.5 | 35.6% | 49.3% | 1.97 | -29.8% |

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
| Market best home last update utc | 2026-10-13T07:40:15Z |
| Market best draw last update utc | 2026-10-13T07:40:15Z |
| Market best away last update utc | 2026-10-13T07:42:28Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | La Coruna |
| Matched away-team name | Levante |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.55 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.62 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.11 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 53.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 64.0% |
| P home draw | 74.4% |
| P draw away | 49.8% |
| Raw p home draw | 75.6% |
| Raw p draw away | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.10 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +3.7% |
| Draw probability edge | -2.5% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +13.7% |
| Under 2.5 probability edge | -13.7% |
| Raw edge prob home | 0.0733 |
| Raw ev home | 0.1693 |
| Raw edge prob draw | -0.0499 |
| Raw ev draw | -0.2133 |
| Raw edge prob away | -0.0234 |
| Raw ev away | -0.0735 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **51.6%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.6%; Under 3.5 goals: 73.3%; Double Chance 1X: 48.4%; Double Chance X2: 77.0%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 23.0% | 4.35 |
| Draw | 25.4% | 3.93 |
| Atlético Madrid win | 51.6% | 1.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.02 |
| Atlético Madrid expected goals | 1.59 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 48.6% |
| Under 2.5 | 51.4% |
| Over 3.5 | 26.7% |
| Under 3.5 | 73.3% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.10% |
| 2 | 0-1 | 11.74% |
| 3 | 1-2 | 9.74% |
| 4 | 0-2 | 9.51% |
| 5 | 0-0 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 23.0% | 21.7% | 4.70 | +8.0% |
| Draw | 25.4% | 25.3% | 3.90 | -0.9% |
| Atlético Madrid win | 51.6% | 53.0% | 1.91 | -1.4% |
| Over 2.5 | 48.6% | 53.8% | 1.87 | -9.2% |
| Under 2.5 | 51.4% | 46.2% | 2.09 | +7.5% |

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
| Market best home last update utc | 2026-10-13T07:42:16Z |
| Market best draw last update utc | 2026-10-13T07:42:16Z |
| Market best away last update utc | 2026-10-13T07:40:15Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Espanol |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 93/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.28 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.74 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.01 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.2% |
| P home draw | 48.4% |
| P draw away | 77.0% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 4.40 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.85 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.09 |
| Home probability edge | +1.3% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | 0.0254 |
| Raw ev home | 0.1397 |
| Raw edge prob draw | 0.0033 |
| Raw ev draw | -0.0022 |
| Raw edge prob away | -0.0287 |
| Raw ev away | -0.0418 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **61.0%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.5%; Under 3.5 goals: 54.8%; Double Chance 1X: 39.0%; Double Chance X2: 80.1%; Under 4.5 goals: 73.3%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.9% | 5.03 |
| Draw | 19.2% | 5.22 |
| Barcelona win | 61.0% | 1.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.35 |
| Barcelona expected goals | 2.07 |
| Expected total goals | 3.42 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 67.5% |
| Under 2.5 | 32.5% |
| Over 3.5 | 45.2% |
| Under 3.5 | 54.8% |
| Over 4.5 | 26.7% |
| Under 4.5 | 73.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.70% |
| 2 | 1-1 | 8.29% |
| 3 | 0-2 | 7.92% |
| 4 | 0-1 | 7.44% |
| 5 | 1-3 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.9% | 15.1% | 6.40 | +27.1% |
| Draw | 19.2% | 16.8% | 6.00 | +15.0% |
| Barcelona win | 61.0% | 68.1% | 1.49 | -9.2% |
| Over 2.5 | 67.5% | 77.6% | 1.26 | -15.0% |
| Under 2.5 | 32.5% | 22.4% | 3.92 | +27.6% |

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
| Market best home last update utc | 2026-10-13T07:42:16Z |
| Market best draw last update utc | 2026-10-13T07:42:16Z |
| Market best away last update utc | 2026-10-13T07:40:15Z |
| Odds bookmakers 1x2 | 21.00 |
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
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.61 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.18 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.75 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 24.6% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 55.3% |
| Raw p btts yes | 65.0% |
| P home draw | 39.0% |
| P draw away | 80.1% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 6.20 |
| Reference draw odds | 5.60 |
| Reference away odds | 1.45 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.92 |
| Home probability edge | +4.7% |
| Draw probability edge | +2.4% |
| Away probability edge | -7.1% |
| Over 2.5 probability edge | -10.2% |
| Under 2.5 probability edge | +10.2% |
| Raw edge prob home | 0.0947 |
| Raw ev home | 0.5743 |
| Raw edge prob draw | 0.0472 |
| Raw ev draw | 0.2917 |
| Raw edge prob away | -0.1419 |
| Raw ev away | -0.1973 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.0%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.1%; Under 3.5 goals: 81.1%; Double Chance 1X: 59.0%; Double Chance X2: 69.7%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.3% | 3.30 |
| Draw | 28.6% | 3.49 |
| Athletic Bilbao win | 41.0% | 2.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.07 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 18.9% |
| Under 3.5 | 81.1% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.29% |
| 2 | 0-1 | 13.24% |
| 3 | 0-0 | 10.66% |
| 4 | 1-0 | 10.24% |
| 5 | 1-2 | 8.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.3% | 27.6% | 3.68 | +11.6% |
| Draw | 28.6% | 28.0% | 3.58 | +2.5% |
| Athletic Bilbao win | 41.0% | 44.4% | 2.20 | -9.7% |
| Over 2.5 | 39.1% | 45.6% | 2.12 | -17.2% |
| Under 2.5 | 60.9% | 54.4% | 1.86 | +13.4% |

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
| Market best home last update utc | 2026-10-13T07:41:44Z |
| Market best draw last update utc | 2026-10-13T07:40:15Z |
| Market best away last update utc | 2026-10-13T07:42:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | BetOnline.ag |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.4% |
| P btts no | 54.6% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.38 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.28 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.89 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 45.6% |
| P home draw | 59.0% |
| P draw away | 69.7% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.50 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +2.7% |
| Draw probability edge | +0.7% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | 0.0550 |
| Raw ev home | 0.2169 |
| Raw edge prob draw | 0.0132 |
| Raw ev draw | 0.0492 |
| Raw edge prob away | -0.0682 |
| Raw ev away | -0.1722 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.5%**. Expected goals are 2.41 for Villarreal and 1.19 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 69.7%; Under 3.5 goals: 51.4%; Double Chance 1X: 84.3%; Double Chance X2: 34.5%; Under 4.5 goals: 70.6%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.5% | 1.53 |
| Draw | 18.9% | 5.30 |
| Elche CF win | 15.7% | 6.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.41 |
| Elche CF expected goals | 1.19 |
| Expected total goals | 3.60 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 69.7% |
| Under 2.5 | 30.3% |
| Over 3.5 | 48.6% |
| Under 3.5 | 51.4% |
| Over 4.5 | 29.4% |
| Under 4.5 | 70.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.61% |
| 2 | 2-0 | 8.11% |
| 3 | 1-1 | 8.09% |
| 4 | 3-1 | 7.74% |
| 5 | 1-0 | 6.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.5% | 66.6% | 1.51 | -1.1% |
| Draw | 18.9% | 19.1% | 5.10 | -3.9% |
| Elche CF win | 15.7% | 14.3% | 6.73 | +5.4% |
| Over 2.5 | 69.7% | 65.9% | 1.47 | +2.5% |
| Under 2.5 | 30.3% | 34.1% | 2.71 | -18.0% |

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
| Market best home last update utc | 2026-10-13T07:40:15Z |
| Market best draw last update utc | 2026-10-13T07:42:16Z |
| Market best away last update utc | 2026-10-13T07:40:15Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.15 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.12 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.30 |
| Fair Over 3.5 odds | 2.06 |
| Fair Under 3.5 odds | 1.95 |
| Fair Over 4.5 odds | 3.40 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 63.4% |
| P home draw | 84.3% |
| P draw away | 34.5% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.48 |
| Reference draw odds | 4.95 |
| Reference away odds | 6.57 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Home probability edge | -1.2% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +3.8% |
| Under 2.5 probability edge | -3.8% |
| Raw edge prob home | -0.0230 |
| Raw ev home | -0.0284 |
| Raw edge prob draw | -0.0050 |
| Raw ev draw | -0.0515 |
| Raw edge prob away | 0.0281 |
| Raw ev away | 0.1480 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **56.1%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.33 combined). The most likely exact score is 2-2 at 7.6%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.2%; Under 3.5 goals: 37.9%; Double Chance 1X: 77.6%; Double Chance X2: 43.9%; Under 4.5 goals: 57.9%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 56.1% | 1.78 |
| Draw | 21.4% | 4.66 |
| Real Racing Club de Santander win | 22.4% | 4.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 2.78 |
| Real Racing Club de Santander expected goals | 1.55 |
| Expected total goals | 4.33 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 92.8% |
| Under 1.5 | 7.2% |
| Over 2.5 | 79.2% |
| Under 2.5 | 20.8% |
| Over 3.5 | 62.1% |
| Under 3.5 | 37.9% |
| Over 4.5 | 42.1% |
| Under 4.5 | 57.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.62% |
| 2 | 1-1 | 7.23% |
| 3 | 2-1 | 7.01% |
| 4 | 3-1 | 6.49% |
| 5 | 1-2 | 5.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 56.1% | 49.0% | 2.06 | +15.6% |
| Draw | 21.4% | 25.7% | 3.75 | -19.6% |
| Real Racing Club de Santander win | 22.4% | 25.3% | 4.08 | -8.5% |
| Over 2.5 | 79.2% | 57.3% | 1.74 | +37.9% |
| Under 2.5 | 20.8% | 42.7% | 2.34 | -51.4% |

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
| Market best home last update utc | 2026-10-13T07:42:16Z |
| Market best draw last update utc | 2026-10-13T07:42:30Z |
| Market best away last update utc | 2026-10-13T07:40:15Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Osasuna |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 75.1% |
| P btts no | 24.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.86 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.94 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.82 |
| Fair Over 3.5 odds | 1.61 |
| Fair Under 3.5 odds | 2.64 |
| Fair Over 4.5 odds | 2.38 |
| Fair Under 4.5 odds | 1.73 |
| Unadjusted home-win probability | 63.3% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 19.5% |
| Raw p over 1 5 | 93.1% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 73.9% |
| P home draw | 77.6% |
| P draw away | 43.9% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.00 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.80 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Home probability edge | +7.1% |
| Draw probability edge | -4.2% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | +21.9% |
| Under 2.5 probability edge | -21.9% |
| Raw edge prob home | 0.1425 |
| Raw ev home | 0.3032 |
| Raw edge prob draw | -0.0846 |
| Raw ev draw | -0.3547 |
| Raw edge prob away | -0.0579 |
| Raw ev away | -0.2031 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **49.0%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 43.7%; Under 3.5 goals: 77.2%; Double Chance 1X: 76.2%; Double Chance X2: 51.0%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 47.7%; BTTS No (at least one team does not score): 52.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 49.0% | 2.04 |
| Draw | 27.2% | 3.68 |
| Alavés win | 23.8% | 4.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.49 |
| Alavés expected goals | 0.94 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 43.7% |
| Under 2.5 | 56.3% |
| Over 3.5 | 22.8% |
| Under 3.5 | 77.2% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.82% |
| 2 | 1-0 | 12.63% |
| 3 | 2-0 | 9.60% |
| 4 | 0-0 | 9.18% |
| 5 | 2-1 | 9.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 49.0% | 48.3% | 2.08 | +1.9% |
| Draw | 27.2% | 27.7% | 3.58 | -2.7% |
| Alavés win | 23.8% | 24.0% | 4.00 | -4.7% |
| Over 2.5 | 43.7% | 45.6% | 2.19 | -4.2% |
| Under 2.5 | 56.3% | 54.4% | 1.79 | +0.7% |

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
| Market best home last update utc | 2026-10-13T07:40:15Z |
| Market best draw last update utc | 2026-10-13T07:40:15Z |
| Market best away last update utc | 2026-10-13T07:42:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 47.7% |
| P btts no | 52.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.89 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.29 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.38 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 10.03 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 47.6% |
| P home draw | 76.2% |
| P draw away | 51.0% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.03 |
| Reference draw odds | 3.48 |
| Reference away odds | 4.00 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +0.7% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | 0.0144 |
| Raw ev home | 0.0339 |
| Raw edge prob draw | -0.0106 |
| Raw ev draw | -0.0457 |
| Raw edge prob away | -0.0038 |
| Raw ev away | -0.0545 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.0%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.5%. Goal-market probabilities: at least one goal: 85.7%; Over 2.5 goals: 29.6%; Under 3.5 goals: 87.9%; Double Chance 1X: 52.0%; Double Chance X2: 76.1%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.3%; BTTS No (at least one team does not score): 66.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.9% | 4.18 |
| Draw | 28.0% | 3.57 |
| Real Sociedad win | 48.0% | 2.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.7% |
| Under 0.5 | 14.3% |
| Over 1.5 | 56.0% |
| Under 1.5 | 44.0% |
| Over 2.5 | 29.6% |
| Under 2.5 | 70.4% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.53% |
| 2 | 0-0 | 14.30% |
| 3 | 1-0 | 12.14% |
| 4 | 1-1 | 11.35% |
| 5 | 0-2 | 11.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.9% | 29.7% | 3.35 | -19.8% |
| Draw | 28.0% | 26.0% | 3.70 | +3.8% |
| Real Sociedad win | 48.0% | 44.4% | 2.29 | +10.0% |
| Over 2.5 | 29.6% | 53.2% | 1.86 | -45.0% |
| Under 2.5 | 70.4% | 46.8% | 2.12 | +49.3% |

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
| Market best home last update utc | 2026-10-13T07:41:30Z |
| Market best draw last update utc | 2026-10-13T07:42:30Z |
| Market best away last update utc | 2026-10-13T07:40:15Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Malaga |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 33.3% |
| P btts no | 66.7% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.99 |
| Fair Over 1.5 odds | 1.78 |
| Fair Under 1.5 odds | 2.27 |
| Fair Over 2.5 odds | 3.38 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.26 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.19 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 52.0% |
| P draw away | 76.1% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.25 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.07 |
| Home probability edge | -5.7% |
| Draw probability edge | +2.1% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -23.6% |
| Under 2.5 probability edge | +23.6% |
| Raw edge prob home | -0.1148 |
| Raw ev home | -0.3904 |
| Raw edge prob draw | 0.0417 |
| Raw ev draw | 0.1150 |
| Raw edge prob away | 0.0730 |
| Raw ev away | 0.1832 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **77.3%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 65.4%; Under 3.5 goals: 56.6%; Double Chance 1X: 91.9%; Double Chance X2: 22.7%; Under 4.5 goals: 75.0%; BTTS Yes (both teams score): 48.7%; BTTS No (at least one team does not score): 51.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.3% | 1.29 |
| Draw | 14.5% | 6.87 |
| Sevilla win | 8.1% | 12.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.63 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 65.4% |
| Under 2.5 | 34.6% |
| Over 3.5 | 43.4% |
| Under 3.5 | 56.6% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.87% |
| 2 | 3-0 | 10.39% |
| 3 | 1-0 | 8.91% |
| 4 | 2-1 | 8.81% |
| 5 | 3-1 | 7.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.3% | 77.3% | 1.30 | +0.6% |
| Draw | 14.5% | 14.6% | 7.00 | +1.8% |
| Sevilla win | 8.1% | 8.2% | 12.50 | +1.3% |
| Over 2.5 | 65.4% | 70.7% | 1.38 | -9.8% |
| Under 2.5 | 34.6% | 29.3% | 3.12 | +8.1% |

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
| Market best home last update utc | 2026-10-13T07:40:15Z |
| Market best draw last update utc | 2026-10-13T07:41:48Z |
| Market best away last update utc | 2026-10-13T07:41:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.7% |
| P btts no | 51.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.83 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.69 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.89 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 4.01 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.7% |
| P home draw | 91.9% |
| P draw away | 22.7% |
| Raw p home draw | 91.9% |
| Raw p draw away | 22.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.28 |
| Reference draw odds | 6.30 |
| Reference away odds | 11.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.12 |
| Home probability edge | +0.1% |
| Draw probability edge | -0.0% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | 0.0019 |
| Raw ev home | 0.0068 |
| Raw edge prob draw | -0.0009 |
| Raw ev draw | 0.0152 |
| Raw edge prob away | -0.0010 |
| Raw ev away | 0.0064 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.6%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.8%. Goal-market probabilities: at least one goal: 81.2%; Over 2.5 goals: 23.1%; Under 3.5 goals: 91.5%; Double Chance 1X: 69.3%; Double Chance X2: 64.4%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 31.1%; BTTS No (at least one team does not score): 68.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.6% | 2.81 |
| Draw | 33.7% | 2.97 |
| Rayo Vallecano win | 30.7% | 3.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.2% |
| Under 0.5 | 18.8% |
| Over 1.5 | 49.1% |
| Under 1.5 | 50.9% |
| Over 2.5 | 23.1% |
| Under 2.5 | 76.9% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.83% |
| 2 | 1-0 | 16.48% |
| 3 | 0-1 | 15.55% |
| 4 | 1-1 | 12.65% |
| 5 | 2-0 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.6% | 33.8% | 3.05 | +8.5% |
| Draw | 33.7% | 32.3% | 3.16 | +6.5% |
| Rayo Vallecano win | 30.7% | 33.8% | 2.87 | -11.8% |
| Over 2.5 | 23.1% | 35.7% | 2.61 | -39.8% |
| Under 2.5 | 76.9% | 64.3% | 1.53 | +17.7% |

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
| Market best home last update utc | 2026-10-13T07:42:16Z |
| Market best draw last update utc | 2026-10-13T07:40:15Z |
| Market best away last update utc | 2026-10-13T07:42:30Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Unibet (SE) |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 31.1% |
| P btts no | 68.9% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.31 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.33 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.79 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.78 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.1% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.3% |
| P home draw | 69.3% |
| P draw away | 64.4% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.87 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.87 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.61 |
| Reference Under 2.5 odds | 1.51 |
| Home probability edge | +1.7% |
| Draw probability edge | +1.4% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -12.7% |
| Under 2.5 probability edge | +12.7% |
| Raw edge prob home | 0.0345 |
| Raw ev home | 0.1373 |
| Raw edge prob draw | 0.0276 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0621 |
| Raw ev away | -0.2072 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.7%**. Expected goals are 1.29 for Levante and 1.39 for Athletic Bilbao (2.68 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 50.1%; Under 3.5 goals: 71.8%; Double Chance 1X: 57.3%; Double Chance X2: 69.5%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 30.5% | 3.28 |
| Draw | 26.9% | 3.72 |
| Athletic Bilbao win | 42.7% | 2.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.29 |
| Athletic Bilbao expected goals | 1.39 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 50.1% |
| Under 2.5 | 49.9% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.77% |
| 2 | 0-1 | 10.11% |
| 3 | 1-2 | 9.32% |
| 4 | 1-0 | 7.58% |
| 5 | 0-2 | 7.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 30.5% | 26.4% | 3.90 | +18.8% |
| Draw | 26.9% | 27.4% | 3.52 | -5.4% |
| Athletic Bilbao win | 42.7% | 46.2% | 2.25 | -4.0% |
| Over 2.5 | 50.1% | 48.0% | 2.02 | +1.2% |
| Under 2.5 | 49.9% | 52.0% | 1.92 | -4.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T18:00:00+00:00 |
| Fixture id | a362cccad837f1ffae61ff43a3536688 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-13T07:42:18Z |
| Market best draw last update utc | 2026-10-13T07:40:15Z |
| Market best away last update utc | 2026-10-13T07:42:28Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.86 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.02 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.46 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 54.7% |
| P home draw | 57.3% |
| P draw away | 69.5% |
| Raw p home draw | 60.8% |
| Raw p draw away | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.81 |
| Home probability edge | +4.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | 0.0804 |
| Raw ev home | 0.3446 |
| Raw edge prob draw | -0.0100 |
| Raw ev draw | -0.0719 |
| Raw edge prob away | -0.0704 |
| Raw ev away | -0.1190 |

</details>


---
