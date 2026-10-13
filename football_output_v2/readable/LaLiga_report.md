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

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.4%**. Expected goals are 2.04 for Deportivo La Coruña and 1.32 for Levante (3.36 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.4%; Under 3.5 goals: 57.0%; Double Chance 1X: 74.5%; Double Chance X2: 49.6%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.4% | 1.99 |
| Draw | 24.2% | 4.14 |
| Levante win | 25.5% | 3.92 |

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
| 1 | 1-1 | 10.60% |
| 2 | 2-1 | 8.91% |
| 3 | 2-2 | 7.00% |
| 4 | 2-0 | 6.75% |
| 5 | 1-2 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.4% | 46.8% | 2.17 | +9.3% |
| Draw | 24.2% | 26.6% | 3.62 | -12.5% |
| Levante win | 25.5% | 26.6% | 3.60 | -8.2% |
| Over 2.5 | 64.4% | 51.5% | 1.98 | +27.5% |
| Under 2.5 | 35.6% | 48.5% | 1.96 | -30.2% |

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
| Market best home last update utc | 2026-10-13T12:25:18Z |
| Market best draw last update utc | 2026-10-13T12:25:18Z |
| Market best away last update utc | 2026-10-13T12:25:18Z |
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
| Fair Under 0.5 odds | 24.61 |
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
| P home draw | 74.5% |
| P draw away | 49.6% |
| Raw p home draw | 75.6% |
| Raw p draw away | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.05 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.93 |
| Home probability edge | +3.5% |
| Draw probability edge | -2.4% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +12.9% |
| Under 2.5 probability edge | -12.9% |
| Raw edge prob home | 0.0707 |
| Raw ev home | 0.1693 |
| Raw edge prob draw | -0.0486 |
| Raw ev draw | -0.2133 |
| Raw edge prob away | -0.0221 |
| Raw ev away | -0.1223 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **53.2%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 0-1 at 12.1%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 48.8%; Under 3.5 goals: 73.1%; Double Chance 1X: 46.8%; Double Chance X2: 78.0%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 22.0% | 4.55 |
| Draw | 24.9% | 4.02 |
| Atlético Madrid win | 53.2% | 1.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.02 |
| Atlético Madrid expected goals | 1.59 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.8% |
| Under 2.5 | 51.2% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.09% |
| 2 | 1-1 | 11.84% |
| 3 | 1-2 | 10.04% |
| 4 | 0-2 | 9.79% |
| 5 | 0-0 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 22.0% | 19.7% | 4.57 | +0.4% |
| Draw | 24.9% | 24.1% | 3.90 | -3.0% |
| Atlético Madrid win | 53.2% | 56.1% | 1.85 | -1.7% |
| Over 2.5 | 48.8% | 54.3% | 1.86 | -9.2% |
| Under 2.5 | 51.2% | 45.7% | 2.10 | +7.5% |

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
| Market best home last update utc | 2026-10-13T12:25:18Z |
| Market best draw last update utc | 2026-10-13T12:25:18Z |
| Market best away last update utc | 2026-10-13T12:25:18Z |
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
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.57 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.95 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.2% |
| P home draw | 46.8% |
| P draw away | 78.0% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 4.60 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.72 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | +2.3% |
| Draw probability edge | +0.7% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | 0.0454 |
| Raw ev home | 0.1082 |
| Raw edge prob draw | 0.0144 |
| Raw ev draw | -0.0022 |
| Raw edge prob away | -0.0598 |
| Raw ev away | -0.0719 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **61.8%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 67.6%; Under 3.5 goals: 54.7%; Double Chance 1X: 38.2%; Double Chance X2: 80.6%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.4% | 5.16 |
| Draw | 18.8% | 5.32 |
| Barcelona win | 61.8% | 1.62 |

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
| Over 2.5 | 67.6% |
| Under 2.5 | 32.4% |
| Over 3.5 | 45.3% |
| Under 3.5 | 54.7% |
| Over 4.5 | 26.8% |
| Under 4.5 | 73.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.85% |
| 2 | 1-1 | 8.14% |
| 3 | 0-2 | 8.03% |
| 4 | 0-1 | 7.54% |
| 5 | 1-3 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.4% | 14.2% | 6.21 | +20.4% |
| Draw | 18.8% | 16.1% | 5.44 | +2.4% |
| Barcelona win | 61.8% | 69.7% | 1.49 | -7.9% |

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
| Market best home last update utc | 2026-10-13T12:25:18Z |
| Market best draw last update utc | 2026-10-13T12:25:18Z |
| Market best away last update utc | 2026-10-13T12:25:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.0% |
| P btts no | 36.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.22 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.20 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.09 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.73 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 24.6% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 55.3% |
| Raw p btts yes | 65.0% |
| P home draw | 38.2% |
| P draw away | 80.6% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 6.20 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Home probability edge | +5.2% |
| Draw probability edge | +2.7% |
| Away probability edge | -7.9% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | 0.1044 |
| Raw ev home | 0.5275 |
| Raw edge prob draw | 0.0543 |
| Raw ev draw | 0.1711 |
| Raw edge prob away | -0.1586 |
| Raw ev away | -0.1973 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **40.5%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.1%; Double Chance 1X: 59.5%; Double Chance X2: 69.3%; Under 4.5 goals: 92.3%; BTTS Yes (both teams score): 45.5%; BTTS No (at least one team does not score): 54.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.7% | 3.26 |
| Draw | 28.8% | 3.47 |
| Athletic Bilbao win | 40.5% | 2.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.07 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 65.8% |
| Under 1.5 | 34.2% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.9% |
| Under 3.5 | 81.1% |
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.36% |
| 2 | 0-1 | 13.08% |
| 3 | 0-0 | 10.71% |
| 4 | 1-0 | 10.36% |
| 5 | 1-2 | 8.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.7% | 28.3% | 3.62 | +11.0% |
| Draw | 28.8% | 28.3% | 3.58 | +3.1% |
| Athletic Bilbao win | 40.5% | 43.4% | 2.18 | -11.6% |
| Over 2.5 | 39.0% | 47.8% | 2.10 | -18.1% |
| Under 2.5 | 61.0% | 52.2% | 1.86 | +13.5% |

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
| Market best home last update utc | 2026-10-13T12:25:18Z |
| Market best draw last update utc | 2026-10-13T12:25:18Z |
| Market best away last update utc | 2026-10-13T12:25:18Z |
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
| P btts yes | 45.5% |
| P btts no | 54.5% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.33 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.29 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.91 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 45.6% |
| P home draw | 59.5% |
| P draw away | 69.3% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.30 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.80 |
| Home probability edge | +2.4% |
| Draw probability edge | +0.5% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | 0.0478 |
| Raw ev home | 0.1971 |
| Raw edge prob draw | 0.0102 |
| Raw ev draw | 0.0492 |
| Raw edge prob away | -0.0581 |
| Raw ev away | -0.1798 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **66.5%**. Expected goals are 2.41 for Villarreal and 1.19 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 70.0%; Under 3.5 goals: 51.2%; Double Chance 1X: 84.7%; Double Chance X2: 33.5%; Under 4.5 goals: 70.4%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 66.5% | 1.50 |
| Draw | 18.2% | 5.49 |
| Elche CF win | 15.3% | 6.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.41 |
| Elche CF expected goals | 1.19 |
| Expected total goals | 3.60 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 70.0% |
| Under 2.5 | 30.0% |
| Over 3.5 | 48.8% |
| Under 3.5 | 51.2% |
| Over 4.5 | 29.6% |
| Under 4.5 | 70.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.76% |
| 2 | 2-0 | 8.24% |
| 3 | 3-1 | 7.86% |
| 4 | 1-1 | 7.81% |
| 5 | 1-0 | 6.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 66.5% | 68.7% | 1.51 | +0.4% |
| Draw | 18.2% | 17.8% | 4.88 | -11.1% |
| Elche CF win | 15.3% | 13.5% | 6.73 | +2.7% |

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
| Market best home last update utc | 2026-10-13T12:25:18Z |
| Market best draw last update utc | 2026-10-13T12:25:18Z |
| Market best away last update utc | 2026-10-13T12:25:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.33 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.16 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.33 |
| Fair Over 3.5 odds | 2.05 |
| Fair Under 3.5 odds | 1.95 |
| Fair Over 4.5 odds | 3.38 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 63.4% |
| P home draw | 84.7% |
| P draw away | 33.5% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.42 |
| Reference draw odds | 5.00 |
| Reference away odds | 6.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | -2.2% |
| Draw probability edge | +0.4% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | +3.2% |
| Under 2.5 probability edge | -3.2% |
| Raw edge prob home | -0.0435 |
| Raw ev home | -0.0284 |
| Raw edge prob draw | 0.0076 |
| Raw ev draw | -0.0924 |
| Raw edge prob away | 0.0359 |
| Raw ev away | 0.1480 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **56.3%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.33 combined). The most likely exact score is 2-2 at 7.6%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.2%; Under 3.5 goals: 37.9%; Double Chance 1X: 77.7%; Double Chance X2: 43.7%; Under 4.5 goals: 57.9%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 56.3% | 1.78 |
| Draw | 21.5% | 4.66 |
| Real Racing Club de Santander win | 22.3% | 4.49 |

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
| 1 | 2-2 | 7.63% |
| 2 | 1-1 | 7.24% |
| 3 | 2-1 | 7.03% |
| 4 | 3-1 | 6.51% |
| 5 | 3-2 | 5.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 56.3% | 49.3% | 2.04 | +14.8% |
| Draw | 21.5% | 25.7% | 3.72 | -20.1% |
| Real Racing Club de Santander win | 22.3% | 25.0% | 3.88 | -13.6% |
| Over 2.5 | 79.2% | 59.3% | 1.74 | +37.9% |
| Under 2.5 | 20.8% | 40.7% | 2.27 | -52.9% |

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
| Market best home last update utc | 2026-10-13T12:25:18Z |
| Market best draw last update utc | 2026-10-13T12:25:18Z |
| Market best away last update utc | 2026-10-13T12:25:18Z |
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
| P btts yes | 75.1% |
| P btts no | 24.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.78 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.95 |
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
| P home draw | 77.7% |
| P draw away | 43.7% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.95 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | +7.0% |
| Draw probability edge | -4.3% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | +19.9% |
| Under 2.5 probability edge | -19.9% |
| Raw edge prob home | 0.1399 |
| Raw ev home | 0.2905 |
| Raw edge prob draw | -0.0852 |
| Raw ev draw | -0.3599 |
| Raw edge prob away | -0.0546 |
| Raw ev away | -0.2422 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **47.7%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 43.4%; Under 3.5 goals: 77.3%; Double Chance 1X: 75.6%; Double Chance X2: 52.3%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.9%; BTTS No (at least one team does not score): 52.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 47.7% | 2.10 |
| Draw | 28.0% | 3.58 |
| Alavés win | 24.4% | 4.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.49 |
| Alavés expected goals | 0.94 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 43.4% |
| Under 2.5 | 56.6% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.18% |
| 2 | 1-0 | 12.30% |
| 3 | 0-0 | 9.44% |
| 4 | 2-0 | 9.35% |
| 5 | 2-1 | 8.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 47.7% | 45.7% | 2.16 | +3.0% |
| Draw | 28.0% | 29.3% | 3.48 | -2.7% |
| Alavés win | 24.4% | 25.1% | 3.78 | -7.9% |
| Over 2.5 | 43.4% | 43.1% | 2.30 | -0.1% |
| Under 2.5 | 56.6% | 56.9% | 1.72 | -2.7% |

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
| Market best home last update utc | 2026-10-13T12:25:18Z |
| Market best draw last update utc | 2026-10-13T12:25:18Z |
| Market best away last update utc | 2026-10-13T12:25:18Z |
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
| P btts yes | 47.9% |
| P btts no | 52.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.59 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.30 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.13 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 47.6% |
| P home draw | 75.6% |
| P draw away | 52.3% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.10 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.67 |
| Home probability edge | +2.0% |
| Draw probability edge | -1.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | 0.0405 |
| Raw ev home | 0.0737 |
| Raw edge prob draw | -0.0260 |
| Raw ev draw | -0.0724 |
| Raw edge prob away | -0.0146 |
| Raw ev away | -0.1065 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.1%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.5%. Goal-market probabilities: at least one goal: 85.1%; Over 2.5 goals: 29.3%; Under 3.5 goals: 87.9%; Double Chance 1X: 51.9%; Double Chance X2: 77.2%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.5%; BTTS No (at least one team does not score): 66.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 22.8% | 4.39 |
| Draw | 29.2% | 3.43 |
| Real Sociedad win | 48.1% | 2.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.1% |
| Under 0.5 | 14.9% |
| Over 1.5 | 56.0% |
| Under 1.5 | 44.0% |
| Over 2.5 | 29.3% |
| Under 2.5 | 70.7% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.54% |
| 2 | 0-0 | 14.87% |
| 3 | 1-1 | 11.81% |
| 4 | 1-0 | 11.55% |
| 5 | 0-2 | 11.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 22.8% | 27.3% | 3.29 | -25.1% |
| Draw | 29.2% | 28.2% | 3.63 | +5.9% |
| Real Sociedad win | 48.1% | 44.4% | 2.29 | +10.0% |
| Over 2.5 | 29.3% | 54.8% | 1.86 | -45.5% |
| Under 2.5 | 70.7% | 45.2% | 2.10 | +48.5% |

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
| Market best home last update utc | 2026-10-13T12:25:18Z |
| Market best draw last update utc | 2026-10-13T12:25:18Z |
| Market best away last update utc | 2026-10-13T12:25:18Z |
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
| P btts yes | 33.5% |
| P btts no | 66.5% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.72 |
| Fair Over 1.5 odds | 1.78 |
| Fair Under 1.5 odds | 2.27 |
| Fair Over 2.5 odds | 3.41 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.26 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.41 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 51.9% |
| P draw away | 77.2% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.40 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | -4.6% |
| Draw probability edge | +1.0% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -25.5% |
| Under 2.5 probability edge | +25.5% |
| Raw edge prob home | -0.0915 |
| Raw ev home | -0.4013 |
| Raw edge prob draw | 0.0191 |
| Raw ev draw | 0.0939 |
| Raw edge prob away | 0.0723 |
| Raw ev away | 0.1832 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.9%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.1%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 65.9%; Under 3.5 goals: 56.3%; Double Chance 1X: 92.2%; Double Chance X2: 21.1%; Under 4.5 goals: 74.7%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.9% | 1.27 |
| Draw | 13.4% | 7.48 |
| Sevilla win | 7.8% | 12.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.63 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.9% |
| Under 2.5 | 34.1% |
| Over 3.5 | 43.7% |
| Under 3.5 | 56.3% |
| Over 4.5 | 25.3% |
| Under 4.5 | 74.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.10% |
| 2 | 3-0 | 10.59% |
| 3 | 1-0 | 9.08% |
| 4 | 2-1 | 8.98% |
| 5 | 3-1 | 7.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 78.9% | 80.3% | 1.30 | +2.5% |
| Draw | 13.4% | 12.2% | 6.61 | -11.6% |
| Sevilla win | 7.8% | 7.5% | 10.70 | -17.0% |

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
| Market best home last update utc | 2026-10-13T12:25:18Z |
| Market best draw last update utc | 2026-10-13T12:25:18Z |
| Market best away last update utc | 2026-10-13T12:25:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.27 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.79 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.94 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.96 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.7% |
| P home draw | 92.2% |
| P draw away | 21.1% |
| Raw p home draw | 91.9% |
| Raw p draw away | 22.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.22 |
| Reference draw odds | 6.70 |
| Reference away odds | 10.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | -1.4% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | -0.0285 |
| Raw ev home | 0.0068 |
| Raw edge prob draw | 0.0225 |
| Raw ev draw | -0.0414 |
| Raw edge prob away | 0.0059 |
| Raw ev away | -0.1385 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **34.9%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.9%. Goal-market probabilities: at least one goal: 81.1%; Over 2.5 goals: 23.0%; Under 3.5 goals: 91.5%; Double Chance 1X: 68.7%; Double Chance X2: 65.1%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 31.1%; BTTS No (at least one team does not score): 68.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 34.9% | 2.87 |
| Draw | 33.8% | 2.96 |
| Rayo Vallecano win | 31.3% | 3.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.1% |
| Under 0.5 | 18.9% |
| Over 1.5 | 49.1% |
| Under 1.5 | 50.9% |
| Over 2.5 | 23.0% |
| Under 2.5 | 77.0% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.87% |
| 2 | 1-0 | 16.17% |
| 3 | 0-1 | 15.85% |
| 4 | 1-1 | 12.68% |
| 5 | 2-0 | 7.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 34.9% | 32.5% | 2.99 | +4.3% |
| Draw | 33.8% | 32.5% | 3.16 | +6.8% |
| Rayo Vallecano win | 31.3% | 35.0% | 2.74 | -14.2% |

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
| Market best home last update utc | 2026-10-13T12:25:18Z |
| Market best draw last update utc | 2026-10-13T12:25:18Z |
| Market best away last update utc | 2026-10-13T12:25:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 31.1% |
| P btts no | 68.9% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.30 |
| Fair Over 1.5 odds | 2.04 |
| Fair Under 1.5 odds | 1.96 |
| Fair Over 2.5 odds | 4.34 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.80 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.86 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.1% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.3% |
| P home draw | 68.7% |
| P draw away | 65.1% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.90 |
| Reference draw odds | 2.90 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 2.55 |
| Reference Under 2.5 odds | 1.50 |
| Home probability edge | +2.4% |
| Draw probability edge | +1.3% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | -12.8% |
| Under 2.5 probability edge | +12.8% |
| Raw edge prob home | 0.0480 |
| Raw ev home | 0.1149 |
| Raw edge prob draw | 0.0260 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0741 |
| Raw ev away | -0.2431 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.4%**. Expected goals are 1.29 for Levante and 1.39 for Athletic Bilbao (2.68 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 49.6%; Under 3.5 goals: 71.8%; Double Chance 1X: 57.6%; Double Chance X2: 70.6%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 29.4% | 3.40 |
| Draw | 28.3% | 3.54 |
| Athletic Bilbao win | 42.4% | 2.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.29 |
| Athletic Bilbao expected goals | 1.39 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.43% |
| 2 | 0-1 | 10.03% |
| 3 | 1-2 | 9.25% |
| 4 | 0-0 | 7.59% |
| 5 | 1-0 | 7.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 29.4% | 24.3% | 3.52 | +3.4% |
| Draw | 28.3% | 30.1% | 3.52 | -0.5% |
| Athletic Bilbao win | 42.4% | 45.6% | 2.24 | -5.1% |
| Over 2.5 | 49.6% | 48.5% | 2.02 | +0.2% |
| Under 2.5 | 50.4% | 51.5% | 1.92 | -3.3% |

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
| Market best home last update utc | 2026-10-13T12:25:18Z |
| Market best draw last update utc | 2026-10-13T12:25:18Z |
| Market best away last update utc | 2026-10-13T12:25:18Z |
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
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.17 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.55 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 54.7% |
| P home draw | 57.6% |
| P draw away | 70.6% |
| Raw p home draw | 60.8% |
| Raw p draw away | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.80 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | +5.1% |
| Draw probability edge | -1.9% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | 0.1018 |
| Raw ev home | 0.2136 |
| Raw edge prob draw | -0.0378 |
| Raw ev draw | -0.0719 |
| Raw edge prob away | -0.0640 |
| Raw ev away | -0.1229 |

</details>


---
