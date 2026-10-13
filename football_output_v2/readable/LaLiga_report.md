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
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
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

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **49.8%**. Expected goals are 2.04 for Deportivo La Coruña and 1.32 for Levante (3.36 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.0%; Double Chance 1X: 74.2%; Double Chance X2: 50.2%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 49.8% | 2.01 |
| Draw | 24.4% | 4.09 |
| Levante win | 25.8% | 3.88 |

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
| Over 2.5 | 64.3% |
| Under 2.5 | 35.7% |
| Over 3.5 | 43.0% |
| Under 3.5 | 57.0% |
| Over 4.5 | 24.3% |
| Under 4.5 | 75.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.73% |
| 2 | 2-1 | 8.81% |
| 3 | 2-2 | 7.09% |
| 4 | 2-0 | 6.67% |
| 5 | 1-2 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 49.8% | 45.7% | 2.17 | +8.0% |
| Draw | 24.4% | 27.2% | 3.62 | -11.5% |
| Levante win | 25.8% | 27.2% | 3.60 | -7.2% |
| Over 2.5 | 64.3% | 48.3% | 1.98 | +27.3% |
| Under 2.5 | 35.7% | 51.7% | 1.96 | -30.0% |

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
| Market best home last update utc | 2026-10-13T16:57:32Z |
| Market best draw last update utc | 2026-10-13T16:57:32Z |
| Market best away last update utc | 2026-10-13T16:57:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | La Coruna |
| Matched away-team name | Levante |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.32 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.61 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.12 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 53.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 64.0% |
| P home draw | 74.2% |
| P draw away | 50.2% |
| Raw p home draw | 75.6% |
| Raw p draw away | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.05 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | +4.1% |
| Draw probability edge | -2.7% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | +16.0% |
| Under 2.5 probability edge | -16.0% |
| Raw edge prob home | 0.0821 |
| Raw ev home | 0.1693 |
| Raw edge prob draw | -0.0543 |
| Raw ev draw | -0.2133 |
| Raw edge prob away | -0.0278 |
| Raw ev away | -0.1223 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **51.4%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 48.5%; Under 3.5 goals: 73.3%; Double Chance 1X: 48.6%; Double Chance X2: 76.9%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 23.1% | 4.33 |
| Draw | 25.5% | 3.92 |
| Atlético Madrid win | 51.4% | 1.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.02 |
| Atlético Madrid expected goals | 1.59 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 26.7% |
| Under 3.5 | 73.3% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.14% |
| 2 | 0-1 | 11.69% |
| 3 | 1-2 | 9.70% |
| 4 | 0-2 | 9.47% |
| 5 | 0-0 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 23.1% | 22.0% | 4.57 | +5.6% |
| Draw | 25.5% | 25.4% | 3.90 | -0.5% |
| Atlético Madrid win | 51.4% | 52.6% | 1.85 | -4.9% |
| Over 2.5 | 48.5% | 54.3% | 1.86 | -9.7% |
| Under 2.5 | 51.5% | 45.7% | 2.10 | +8.1% |

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
| Market best home last update utc | 2026-10-13T16:57:32Z |
| Market best draw last update utc | 2026-10-13T16:57:32Z |
| Market best away last update utc | 2026-10-13T16:57:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Espanol |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 93/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.23 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.74 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.02 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.2% |
| P home draw | 48.6% |
| P draw away | 76.9% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 4.00 |
| Reference draw odds | 3.50 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | +1.1% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.0228 |
| Raw ev home | 0.1082 |
| Raw edge prob draw | 0.0016 |
| Raw ev draw | -0.0022 |
| Raw edge prob away | -0.0243 |
| Raw ev away | -0.0719 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **60.8%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 67.5%; Under 3.5 goals: 54.8%; Double Chance 1X: 39.2%; Double Chance X2: 79.9%; Under 4.5 goals: 73.3%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 20.1% | 4.97 |
| Draw | 19.0% | 5.25 |
| Barcelona win | 60.8% | 1.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.35 |
| Barcelona expected goals | 2.07 |
| Expected total goals | 3.42 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
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
| 1 | 1-2 | 10.68% |
| 2 | 1-1 | 8.24% |
| 3 | 0-2 | 7.90% |
| 4 | 0-1 | 7.43% |
| 5 | 1-3 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 20.1% | 15.6% | 6.21 | +24.9% |
| Draw | 19.0% | 16.6% | 5.44 | +3.6% |
| Barcelona win | 60.8% | 67.8% | 1.49 | -9.3% |

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
| Market best home last update utc | 2026-10-13T16:57:32Z |
| Market best draw last update utc | 2026-10-13T16:57:32Z |
| Market best away last update utc | 2026-10-13T16:57:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.81 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.18 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.08 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.74 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 24.6% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 55.3% |
| Raw p btts yes | 65.0% |
| P home draw | 39.2% |
| P draw away | 79.9% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 5.00 |
| Reference draw odds | 4.75 |
| Reference away odds | 1.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Home probability edge | +4.5% |
| Draw probability edge | +2.5% |
| Away probability edge | -7.0% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | 0.0899 |
| Raw ev home | 0.5275 |
| Raw edge prob draw | 0.0496 |
| Raw ev draw | 0.1711 |
| Raw edge prob away | -0.1395 |
| Raw ev away | -0.1973 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **40.9%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 39.1%; Under 3.5 goals: 81.1%; Double Chance 1X: 59.1%; Double Chance X2: 69.5%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.5% | 3.28 |
| Draw | 28.6% | 3.49 |
| Athletic Bilbao win | 40.9% | 2.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.07 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
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
| 1 | 1-1 | 13.28% |
| 2 | 0-1 | 13.19% |
| 3 | 0-0 | 10.65% |
| 4 | 1-0 | 10.30% |
| 5 | 1-2 | 8.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.5% | 27.9% | 3.62 | +10.4% |
| Draw | 28.6% | 27.9% | 3.58 | +2.5% |
| Athletic Bilbao win | 40.9% | 44.1% | 2.18 | -10.9% |
| Over 2.5 | 39.1% | 45.7% | 2.10 | -18.0% |
| Under 2.5 | 60.9% | 54.3% | 1.86 | +13.4% |

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
| Market best home last update utc | 2026-10-13T16:57:32Z |
| Market best draw last update utc | 2026-10-13T16:57:32Z |
| Market best away last update utc | 2026-10-13T16:57:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
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
| Fair Under 0.5 odds | 9.39 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.28 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.88 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 45.6% |
| P home draw | 59.1% |
| P draw away | 69.5% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.30 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.75 |
| Home probability edge | +2.6% |
| Draw probability edge | +0.7% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | 0.0514 |
| Raw ev home | 0.1971 |
| Raw edge prob draw | 0.0138 |
| Raw ev draw | 0.0492 |
| Raw edge prob away | -0.0652 |
| Raw ev away | -0.1798 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.6%**. Expected goals are 2.41 for Villarreal and 1.19 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 69.7%; Under 3.5 goals: 51.3%; Double Chance 1X: 84.5%; Double Chance X2: 34.4%; Under 4.5 goals: 70.6%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.6% | 1.52 |
| Draw | 18.9% | 5.30 |
| Elche CF win | 15.5% | 6.45 |

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
| Over 3.5 | 48.7% |
| Under 3.5 | 51.3% |
| Over 4.5 | 29.4% |
| Under 4.5 | 70.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.63% |
| 2 | 2-0 | 8.13% |
| 3 | 1-1 | 8.09% |
| 4 | 3-1 | 7.75% |
| 5 | 1-0 | 6.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.6% | 67.0% | 1.51 | -0.9% |
| Draw | 18.9% | 19.1% | 4.88 | -8.0% |
| Elche CF win | 15.5% | 13.9% | 6.73 | +4.3% |

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
| Market best home last update utc | 2026-10-13T16:57:32Z |
| Market best draw last update utc | 2026-10-13T16:57:32Z |
| Market best away last update utc | 2026-10-13T16:57:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.14 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.13 |
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
| P home draw | 84.5% |
| P draw away | 34.4% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.44 |
| Reference draw odds | 4.50 |
| Reference away odds | 6.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | -1.3% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | -0.0261 |
| Raw ev home | -0.0284 |
| Raw edge prob draw | -0.0052 |
| Raw ev draw | -0.0924 |
| Raw edge prob away | 0.0313 |
| Raw ev away | 0.1480 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **55.3%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.33 combined). The most likely exact score is 2-2 at 7.8%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.1%; Under 3.5 goals: 38.0%; Double Chance 1X: 77.3%; Double Chance X2: 44.7%; Under 4.5 goals: 58.1%; BTTS Yes (both teams score): 75.3%; BTTS No (at least one team does not score): 24.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 55.3% | 1.81 |
| Draw | 22.0% | 4.55 |
| Real Racing Club de Santander win | 22.7% | 4.40 |

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
| Over 2.5 | 79.1% |
| Under 2.5 | 20.9% |
| Over 3.5 | 62.0% |
| Under 3.5 | 38.0% |
| Over 4.5 | 41.9% |
| Under 4.5 | 58.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.80% |
| 2 | 1-1 | 7.41% |
| 3 | 2-1 | 6.91% |
| 4 | 3-1 | 6.40% |
| 5 | 1-2 | 5.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 55.3% | 47.4% | 2.04 | +12.8% |
| Draw | 22.0% | 26.7% | 3.72 | -18.3% |
| Real Racing Club de Santander win | 22.7% | 25.9% | 3.88 | -11.8% |
| Over 2.5 | 79.1% | 55.8% | 1.74 | +37.6% |
| Under 2.5 | 20.9% | 44.2% | 2.27 | -52.5% |

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
| Market best home last update utc | 2026-10-13T16:57:32Z |
| Market best draw last update utc | 2026-10-13T16:57:32Z |
| Market best away last update utc | 2026-10-13T16:57:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Osasuna |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 75.3% |
| P btts no | 24.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 54.51 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.89 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.78 |
| Fair Over 3.5 odds | 1.61 |
| Fair Under 3.5 odds | 2.63 |
| Fair Over 4.5 odds | 2.39 |
| Fair Under 4.5 odds | 1.72 |
| Unadjusted home-win probability | 63.3% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 19.5% |
| Raw p over 1 5 | 93.1% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 73.9% |
| P home draw | 77.3% |
| P draw away | 44.7% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.00 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | +7.9% |
| Draw probability edge | -4.8% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | +23.3% |
| Under 2.5 probability edge | -23.3% |
| Raw edge prob home | 0.1590 |
| Raw ev home | 0.2905 |
| Raw edge prob draw | -0.0952 |
| Raw ev draw | -0.3599 |
| Raw edge prob away | -0.0638 |
| Raw ev away | -0.2422 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **48.0%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 43.7%; Under 3.5 goals: 77.3%; Double Chance 1X: 75.2%; Double Chance X2: 52.0%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 48.0% | 2.08 |
| Draw | 27.2% | 3.68 |
| Alavés win | 24.8% | 4.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.49 |
| Alavés expected goals | 0.94 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 43.7% |
| Under 2.5 | 56.3% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.83% |
| 2 | 1-0 | 12.37% |
| 3 | 2-0 | 9.40% |
| 4 | 0-0 | 9.19% |
| 5 | 2-1 | 8.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 48.0% | 46.2% | 2.16 | +3.6% |
| Draw | 27.2% | 27.7% | 3.48 | -5.4% |
| Alavés win | 24.8% | 26.0% | 3.78 | -6.1% |
| Over 2.5 | 43.7% | 43.1% | 2.30 | +0.5% |
| Under 2.5 | 56.3% | 56.9% | 1.72 | -3.2% |

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
| Market best home last update utc | 2026-10-13T16:57:32Z |
| Market best draw last update utc | 2026-10-13T16:57:32Z |
| Market best away last update utc | 2026-10-13T16:57:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.89 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.29 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.06 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 47.6% |
| P home draw | 75.2% |
| P draw away | 52.0% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.05 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.67 |
| Home probability edge | +1.7% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | 0.0346 |
| Raw ev home | 0.0737 |
| Raw edge prob draw | -0.0107 |
| Raw ev draw | -0.0724 |
| Raw edge prob away | -0.0239 |
| Raw ev away | -0.1065 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **47.6%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.4%. Goal-market probabilities: at least one goal: 85.4%; Over 2.5 goals: 29.4%; Under 3.5 goals: 87.9%; Double Chance 1X: 52.4%; Double Chance X2: 76.3%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.4%; BTTS No (at least one team does not score): 66.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.7% | 4.22 |
| Draw | 28.7% | 3.48 |
| Real Sociedad win | 47.6% | 2.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.4% |
| Under 0.5 | 14.6% |
| Over 1.5 | 56.0% |
| Under 1.5 | 44.0% |
| Over 2.5 | 29.4% |
| Under 2.5 | 70.6% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.37% |
| 2 | 0-0 | 14.64% |
| 3 | 1-0 | 12.02% |
| 4 | 1-1 | 11.62% |
| 5 | 0-2 | 11.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.7% | 29.2% | 3.29 | -22.0% |
| Draw | 28.7% | 27.3% | 3.63 | +4.2% |
| Real Sociedad win | 47.6% | 43.5% | 2.29 | +9.0% |
| Over 2.5 | 29.4% | 52.2% | 1.86 | -45.3% |
| Under 2.5 | 70.6% | 47.8% | 2.10 | +48.3% |

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
| Market best home last update utc | 2026-10-13T16:57:33Z |
| Market best draw last update utc | 2026-10-13T16:57:33Z |
| Market best away last update utc | 2026-10-13T16:57:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 33.4% |
| P btts no | 66.6% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.83 |
| Fair Over 1.5 odds | 1.79 |
| Fair Under 1.5 odds | 2.27 |
| Fair Over 2.5 odds | 3.40 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.28 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.37 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 52.4% |
| P draw away | 76.3% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.10 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | -5.5% |
| Draw probability edge | +1.4% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -22.8% |
| Under 2.5 probability edge | +22.8% |
| Raw edge prob home | -0.1102 |
| Raw ev home | -0.4013 |
| Raw edge prob draw | 0.0284 |
| Raw ev draw | 0.0939 |
| Raw edge prob away | 0.0817 |
| Raw ev away | 0.1832 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **77.7%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.5%; Under 3.5 goals: 56.5%; Double Chance 1X: 91.9%; Double Chance X2: 22.3%; Under 4.5 goals: 75.0%; BTTS Yes (both teams score): 48.6%; BTTS No (at least one team does not score): 51.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.7% | 1.29 |
| Draw | 14.3% | 7.01 |
| Sevilla win | 8.1% | 12.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.63 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 65.5% |
| Under 2.5 | 34.5% |
| Over 3.5 | 43.5% |
| Under 3.5 | 56.5% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.92% |
| 2 | 3-0 | 10.43% |
| 3 | 1-0 | 8.95% |
| 4 | 2-1 | 8.84% |
| 5 | 3-1 | 7.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.7% | 77.9% | 1.30 | +1.0% |
| Draw | 14.3% | 14.0% | 6.61 | -5.8% |
| Sevilla win | 8.1% | 8.1% | 10.70 | -13.8% |

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
| Market best home last update utc | 2026-10-13T16:57:33Z |
| Market best draw last update utc | 2026-10-13T16:57:33Z |
| Market best away last update utc | 2026-10-13T16:57:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.6% |
| P btts no | 51.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.40 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.71 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 4.00 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.7% |
| P home draw | 91.9% |
| P draw away | 22.3% |
| Raw p home draw | 91.9% |
| Raw p draw away | 22.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.25 |
| Reference draw odds | 5.80 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | -0.2% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0047 |
| Raw ev home | 0.0068 |
| Raw edge prob draw | 0.0049 |
| Raw ev draw | -0.0414 |
| Raw edge prob away | -0.0002 |
| Raw ev away | -0.1385 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.1%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.7%. Goal-market probabilities: at least one goal: 81.3%; Over 2.5 goals: 23.1%; Under 3.5 goals: 91.5%; Double Chance 1X: 68.5%; Double Chance X2: 64.9%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 31.0%; BTTS No (at least one team does not score): 69.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.1% | 2.85 |
| Draw | 33.4% | 2.99 |
| Rayo Vallecano win | 31.5% | 3.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.3% |
| Under 0.5 | 18.7% |
| Over 1.5 | 49.1% |
| Under 1.5 | 50.9% |
| Over 2.5 | 23.1% |
| Under 2.5 | 76.9% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.65% |
| 2 | 1-0 | 16.27% |
| 3 | 0-1 | 15.94% |
| 4 | 1-1 | 12.53% |
| 5 | 2-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.1% | 32.9% | 2.99 | +5.0% |
| Draw | 33.4% | 31.7% | 3.16 | +5.5% |
| Rayo Vallecano win | 31.5% | 35.4% | 2.74 | -13.7% |

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
| Market best home last update utc | 2026-10-13T16:57:33Z |
| Market best draw last update utc | 2026-10-13T16:57:33Z |
| Market best away last update utc | 2026-10-13T16:57:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 31.0% |
| P btts no | 69.0% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.36 |
| Fair Over 1.5 odds | 2.04 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.32 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.79 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.68 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.1% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.3% |
| P home draw | 68.5% |
| P draw away | 64.9% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.80 |
| Reference draw odds | 2.90 |
| Reference away odds | 2.62 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.45 |
| Reference Under 2.5 odds | 1.50 |
| Home probability edge | +2.2% |
| Draw probability edge | +1.7% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | -13.4% |
| Under 2.5 probability edge | +13.4% |
| Raw edge prob home | 0.0436 |
| Raw ev home | 0.1149 |
| Raw edge prob draw | 0.0338 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0775 |
| Raw ev away | -0.2431 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.1%**. Expected goals are 1.29 for Levante and 1.39 for Athletic Bilbao (2.68 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.8%; Under 3.5 goals: 71.8%; Double Chance 1X: 58.9%; Double Chance X2: 68.6%; Under 4.5 goals: 86.7%; BTTS Yes (both teams score): 55.0%; BTTS No (at least one team does not score): 45.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 31.4% | 3.19 |
| Draw | 27.6% | 3.63 |
| Athletic Bilbao win | 41.1% | 2.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.29 |
| Athletic Bilbao expected goals | 1.39 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 49.8% |
| Under 2.5 | 50.2% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.3% |
| Under 4.5 | 86.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.10% |
| 2 | 0-1 | 9.72% |
| 3 | 1-2 | 8.97% |
| 4 | 1-0 | 7.81% |
| 5 | 0-0 | 7.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 31.4% | 28.3% | 3.52 | +10.5% |
| Draw | 27.6% | 28.8% | 3.52 | -3.0% |
| Athletic Bilbao win | 41.1% | 43.0% | 2.24 | -8.0% |
| Over 2.5 | 49.8% | 47.8% | 2.02 | +0.7% |
| Under 2.5 | 50.2% | 52.2% | 1.92 | -3.7% |

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
| Market best home last update utc | 2026-10-13T16:57:33Z |
| Market best draw last update utc | 2026-10-13T16:57:33Z |
| Market best away last update utc | 2026-10-13T16:57:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.0% |
| P btts no | 45.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.51 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.51 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 54.7% |
| P home draw | 58.9% |
| P draw away | 68.6% |
| Raw p home draw | 60.8% |
| Raw p draw away | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.25 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.80 |
| Home probability edge | +3.1% |
| Draw probability edge | -1.2% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | 0.0620 |
| Raw ev home | 0.2136 |
| Raw edge prob draw | -0.0239 |
| Raw ev draw | -0.0719 |
| Raw edge prob away | -0.0381 |
| Raw ev away | -0.1229 |

</details>


---
