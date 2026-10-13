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

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.3%**. Expected goals are 2.04 for Deportivo La Coruña and 1.32 for Levante (3.36 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.4%; Under 3.5 goals: 57.0%; Double Chance 1X: 74.5%; Double Chance X2: 49.7%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.3% | 1.99 |
| Draw | 24.2% | 4.13 |
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
| 1 | 1-1 | 10.62% |
| 2 | 2-1 | 8.90% |
| 3 | 2-2 | 7.02% |
| 4 | 2-0 | 6.74% |
| 5 | 1-2 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.3% | 46.7% | 2.17 | +9.1% |
| Draw | 24.2% | 26.7% | 3.62 | -12.3% |
| Levante win | 25.5% | 26.6% | 3.80 | -3.1% |
| Over 2.5 | 64.4% | 50.3% | 1.98 | +27.5% |
| Under 2.5 | 35.6% | 49.7% | 1.97 | -29.8% |

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
| Market best home last update utc | 2026-10-13T11:02:27Z |
| Market best draw last update utc | 2026-10-13T11:02:27Z |
| Market best away last update utc | 2026-10-13T11:02:57Z |
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
| Fair Under 0.5 odds | 24.56 |
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
| P draw away | 49.7% |
| Raw p home draw | 75.6% |
| Raw p draw away | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.09 |
| Reference draw odds | 3.59 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | +3.6% |
| Draw probability edge | -2.5% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +14.1% |
| Under 2.5 probability edge | -14.1% |
| Raw edge prob home | 0.0720 |
| Raw ev home | 0.1693 |
| Raw edge prob draw | -0.0496 |
| Raw ev draw | -0.2133 |
| Raw edge prob away | -0.0224 |
| Raw ev away | -0.0735 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **52.1%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.7%; Under 3.5 goals: 73.2%; Double Chance 1X: 47.9%; Double Chance X2: 77.3%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 22.7% | 4.40 |
| Draw | 25.2% | 3.97 |
| Atlético Madrid win | 52.1% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.02 |
| Atlético Madrid expected goals | 1.59 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.7% |
| Under 2.5 | 51.3% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.98% |
| 2 | 0-1 | 11.86% |
| 3 | 1-2 | 9.84% |
| 4 | 0-2 | 9.60% |
| 5 | 0-0 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 22.7% | 21.2% | 4.70 | +6.8% |
| Draw | 25.2% | 24.7% | 3.90 | -1.9% |
| Atlético Madrid win | 52.1% | 54.1% | 1.91 | -0.5% |
| Over 2.5 | 48.7% | 54.3% | 1.87 | -9.0% |
| Under 2.5 | 51.3% | 45.7% | 2.09 | +7.3% |

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
| Market best home last update utc | 2026-10-13T11:02:58Z |
| Market best draw last update utc | 2026-10-13T11:02:28Z |
| Market best away last update utc | 2026-10-13T11:02:27Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
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
| Fair Under 0.5 odds | 13.41 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.99 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.2% |
| P home draw | 47.9% |
| P draw away | 77.3% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.47 |
| Reference draw odds | 3.85 |
| Reference away odds | 1.81 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | +1.5% |
| Draw probability edge | +0.4% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | 0.0306 |
| Raw ev home | 0.1397 |
| Raw edge prob draw | 0.0085 |
| Raw ev draw | -0.0022 |
| Raw edge prob away | -0.0391 |
| Raw ev away | -0.0418 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **60.9%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.5%; Under 3.5 goals: 54.8%; Double Chance 1X: 39.1%; Double Chance X2: 79.9%; Under 4.5 goals: 73.3%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 20.1% | 4.99 |
| Draw | 19.1% | 5.24 |
| Barcelona win | 60.9% | 1.64 |

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
| 1 | 1-2 | 10.68% |
| 2 | 1-1 | 8.25% |
| 3 | 0-2 | 7.91% |
| 4 | 0-1 | 7.43% |
| 5 | 1-3 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 20.1% | 15.5% | 6.40 | +28.4% |
| Draw | 19.1% | 16.6% | 5.90 | +12.5% |
| Barcelona win | 60.9% | 67.9% | 1.49 | -9.3% |
| Over 2.5 | 67.5% | 78.5% | 1.26 | -15.0% |
| Under 2.5 | 32.5% | 21.5% | 3.99 | +29.7% |

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
| Market best home last update utc | 2026-10-13T11:02:58Z |
| Market best draw last update utc | 2026-10-13T11:02:57Z |
| Market best away last update utc | 2026-10-13T11:02:27Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Matchbook |
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
| Fair Under 0.5 odds | 32.76 |
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
| P home draw | 39.1% |
| P draw away | 79.9% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.96 |
| Reference draw odds | 5.58 |
| Reference away odds | 1.45 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.24 |
| Reference Under 2.5 odds | 3.90 |
| Home probability edge | +4.5% |
| Draw probability edge | +2.5% |
| Away probability edge | -7.0% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0908 |
| Raw ev home | 0.5743 |
| Raw edge prob draw | 0.0490 |
| Raw ev draw | 0.2701 |
| Raw edge prob away | -0.1398 |
| Raw ev away | -0.1973 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **40.5%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.1%; Double Chance 1X: 59.5%; Double Chance X2: 69.2%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.5%; BTTS No (at least one team does not score): 54.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.8% | 3.25 |
| Draw | 28.7% | 3.48 |
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
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.34% |
| 2 | 0-1 | 13.05% |
| 3 | 0-0 | 10.70% |
| 4 | 1-0 | 10.40% |
| 5 | 1-2 | 8.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.8% | 28.5% | 3.65 | +12.4% |
| Draw | 28.7% | 28.2% | 3.58 | +2.9% |
| Athletic Bilbao win | 40.5% | 43.3% | 2.26 | -8.6% |
| Over 2.5 | 39.0% | 46.4% | 2.12 | -17.3% |
| Under 2.5 | 61.0% | 53.6% | 1.86 | +13.4% |

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
| Market best home last update utc | 2026-10-13T11:02:28Z |
| Market best draw last update utc | 2026-10-13T11:02:27Z |
| Market best away last update utc | 2026-10-13T11:02:58Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.5% |
| P btts no | 54.5% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.35 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.29 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.90 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 45.6% |
| P home draw | 59.5% |
| P draw away | 69.2% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.37 |
| Reference draw odds | 3.41 |
| Reference away odds | 2.25 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.09 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +2.3% |
| Draw probability edge | +0.6% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | 0.0454 |
| Raw ev home | 0.2070 |
| Raw edge prob draw | 0.0113 |
| Raw ev draw | 0.0492 |
| Raw edge prob away | -0.0567 |
| Raw ev away | -0.1497 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.8%**. Expected goals are 2.41 for Villarreal and 1.19 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 69.8%; Under 3.5 goals: 51.3%; Double Chance 1X: 84.3%; Double Chance X2: 34.2%; Under 4.5 goals: 70.5%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.8% | 1.52 |
| Draw | 18.5% | 5.40 |
| Elche CF win | 15.7% | 6.38 |

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
| Over 2.5 | 69.8% |
| Under 2.5 | 30.2% |
| Over 3.5 | 48.7% |
| Under 3.5 | 51.3% |
| Over 4.5 | 29.5% |
| Under 4.5 | 70.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.66% |
| 2 | 2-0 | 8.15% |
| 3 | 1-1 | 7.94% |
| 4 | 3-1 | 7.77% |
| 5 | 1-0 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.8% | 67.3% | 1.51 | -0.6% |
| Draw | 18.5% | 18.4% | 5.10 | -5.6% |
| Elche CF win | 15.7% | 14.3% | 6.73 | +5.5% |
| Over 2.5 | 69.8% | 67.0% | 1.45 | +1.3% |
| Under 2.5 | 30.2% | 33.0% | 2.79 | -15.9% |

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
| Market best home last update utc | 2026-10-13T11:02:27Z |
| Market best draw last update utc | 2026-10-13T11:02:58Z |
| Market best away last update utc | 2026-10-13T11:02:27Z |
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
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.77 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.13 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.32 |
| Fair Over 3.5 odds | 2.05 |
| Fair Under 3.5 odds | 1.95 |
| Fair Over 4.5 odds | 3.39 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 63.4% |
| P home draw | 84.3% |
| P draw away | 34.2% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.46 |
| Reference draw odds | 5.03 |
| Reference away odds | 6.41 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -1.5% |
| Draw probability edge | +0.1% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +2.8% |
| Under 2.5 probability edge | -2.8% |
| Raw edge prob home | -0.0294 |
| Raw ev home | -0.0284 |
| Raw edge prob draw | 0.0017 |
| Raw ev draw | -0.0515 |
| Raw edge prob away | 0.0276 |
| Raw ev away | 0.1480 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **55.5%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.33 combined). The most likely exact score is 2-2 at 7.8%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.1%; Under 3.5 goals: 38.0%; Double Chance 1X: 77.4%; Double Chance X2: 44.5%; Under 4.5 goals: 58.1%; BTTS Yes (both teams score): 75.2%; BTTS No (at least one team does not score): 24.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 55.5% | 1.80 |
| Draw | 22.0% | 4.55 |
| Real Racing Club de Santander win | 22.6% | 4.43 |

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
| 1 | 2-2 | 7.81% |
| 2 | 1-1 | 7.41% |
| 3 | 2-1 | 6.93% |
| 4 | 3-1 | 6.41% |
| 5 | 1-2 | 5.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 55.5% | 47.7% | 2.12 | +17.6% |
| Draw | 22.0% | 26.7% | 3.75 | -17.6% |
| Real Racing Club de Santander win | 22.6% | 25.6% | 3.95 | -10.9% |
| Over 2.5 | 79.1% | 59.3% | 1.74 | +37.6% |
| Under 2.5 | 20.9% | 40.7% | 2.32 | -51.5% |

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
| Market best home last update utc | 2026-10-13T11:02:58Z |
| Market best draw last update utc | 2026-10-13T11:02:15Z |
| Market best away last update utc | 2026-10-13T11:02:28Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Osasuna |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 75.2% |
| P btts no | 24.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 54.49 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.90 |
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
| P home draw | 77.4% |
| P draw away | 44.5% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.05 |
| Reference draw odds | 3.59 |
| Reference away odds | 3.75 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | +7.8% |
| Draw probability edge | -4.8% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | +19.7% |
| Under 2.5 probability edge | -19.7% |
| Raw edge prob home | 0.1558 |
| Raw ev home | 0.3411 |
| Raw edge prob draw | -0.0954 |
| Raw ev draw | -0.3547 |
| Raw edge prob away | -0.0604 |
| Raw ev away | -0.2285 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **48.3%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 43.6%; Under 3.5 goals: 77.2%; Double Chance 1X: 76.0%; Double Chance X2: 51.7%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.9%; BTTS No (at least one team does not score): 52.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 48.3% | 2.07 |
| Draw | 27.7% | 3.61 |
| Alavés win | 24.0% | 4.17 |

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
| Over 2.5 | 43.6% |
| Under 2.5 | 56.4% |
| Over 3.5 | 22.8% |
| Under 3.5 | 77.2% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.06% |
| 2 | 1-0 | 12.46% |
| 3 | 2-0 | 9.47% |
| 4 | 0-0 | 9.36% |
| 5 | 2-1 | 8.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 48.3% | 46.9% | 2.08 | +0.5% |
| Draw | 27.7% | 28.7% | 3.58 | -0.8% |
| Alavés win | 24.0% | 24.4% | 4.00 | -4.0% |
| Over 2.5 | 43.6% | 43.1% | 2.28 | -0.7% |
| Under 2.5 | 56.4% | 56.9% | 1.79 | +1.0% |

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
| Market best home last update utc | 2026-10-13T11:03:26Z |
| Market best draw last update utc | 2026-10-13T11:02:27Z |
| Market best away last update utc | 2026-10-13T11:02:15Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 47.9% |
| P btts no | 52.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.69 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.30 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.39 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.09 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 47.6% |
| P home draw | 76.0% |
| P draw away | 51.7% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.34 |
| Reference away odds | 3.92 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.67 |
| Home probability edge | +1.4% |
| Draw probability edge | -1.0% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0281 |
| Raw ev home | 0.0339 |
| Raw edge prob draw | -0.0209 |
| Raw ev draw | -0.0457 |
| Raw edge prob away | -0.0072 |
| Raw ev away | -0.0545 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.2%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.6%. Goal-market probabilities: at least one goal: 85.5%; Over 2.5 goals: 29.5%; Under 3.5 goals: 87.9%; Double Chance 1X: 51.8%; Double Chance X2: 76.7%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.4%; BTTS No (at least one team does not score): 66.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.3% | 4.30 |
| Draw | 28.5% | 3.51 |
| Real Sociedad win | 48.2% | 2.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.5% |
| Under 0.5 | 14.5% |
| Over 1.5 | 56.1% |
| Under 1.5 | 43.9% |
| Over 2.5 | 29.5% |
| Under 2.5 | 70.5% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.60% |
| 2 | 0-0 | 14.54% |
| 3 | 1-0 | 11.81% |
| 4 | 1-1 | 11.54% |
| 5 | 0-2 | 11.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.3% | 28.4% | 3.40 | -20.8% |
| Draw | 28.5% | 26.9% | 3.70 | +5.5% |
| Real Sociedad win | 48.2% | 44.7% | 2.29 | +10.4% |
| Over 2.5 | 29.5% | 54.8% | 1.86 | -45.2% |
| Under 2.5 | 70.5% | 45.2% | 2.12 | +49.5% |

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
| Market best home last update utc | 2026-10-13T11:03:14Z |
| Market best draw last update utc | 2026-10-13T11:02:15Z |
| Market best away last update utc | 2026-10-13T11:02:27Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Malaga |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 33.4% |
| P btts no | 66.6% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.88 |
| Fair Over 1.5 odds | 1.78 |
| Fair Under 1.5 odds | 2.28 |
| Fair Over 2.5 odds | 3.39 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.25 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.26 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 51.8% |
| P draw away | 76.7% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.39 |
| Reference draw odds | 3.57 |
| Reference away odds | 2.18 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | -5.1% |
| Draw probability edge | +1.6% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -25.4% |
| Under 2.5 probability edge | +25.4% |
| Raw edge prob home | -0.1017 |
| Raw ev home | -0.3813 |
| Raw edge prob draw | 0.0324 |
| Raw ev draw | 0.1150 |
| Raw edge prob away | 0.0693 |
| Raw ev away | 0.1832 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **77.8%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.6%; Under 3.5 goals: 56.5%; Double Chance 1X: 91.8%; Double Chance X2: 22.2%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 48.6%; BTTS No (at least one team does not score): 51.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.8% | 1.29 |
| Draw | 14.1% | 7.12 |
| Sevilla win | 8.2% | 12.26 |

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
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.5% |
| Under 3.5 | 56.5% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.94% |
| 2 | 3-0 | 10.45% |
| 3 | 1-0 | 8.96% |
| 4 | 2-1 | 8.86% |
| 5 | 3-1 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.8% | 78.1% | 1.30 | +1.1% |
| Draw | 14.1% | 13.6% | 7.00 | -1.6% |
| Sevilla win | 8.2% | 8.3% | 12.50 | +2.0% |
| Over 2.5 | 65.6% | 70.5% | 1.39 | -8.8% |
| Under 2.5 | 34.4% | 29.5% | 3.07 | +5.7% |

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
| Market best home last update utc | 2026-10-13T11:02:27Z |
| Market best draw last update utc | 2026-10-13T11:02:58Z |
| Market best away last update utc | 2026-10-13T11:02:28Z |
| Odds bookmakers 1x2 | 21.00 |
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
| P btts yes | 48.6% |
| P btts no | 51.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.81 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.72 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.99 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.7% |
| P home draw | 91.8% |
| P draw away | 22.2% |
| Raw p home draw | 91.9% |
| Raw p draw away | 22.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.26 |
| Reference draw odds | 6.48 |
| Reference away odds | 10.33 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -0.3% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0069 |
| Raw ev home | 0.0068 |
| Raw edge prob draw | 0.0090 |
| Raw ev draw | 0.0152 |
| Raw edge prob away | -0.0021 |
| Raw ev away | 0.0064 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **34.7%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.9%. Goal-market probabilities: at least one goal: 81.1%; Over 2.5 goals: 23.0%; Under 3.5 goals: 91.5%; Double Chance 1X: 68.6%; Double Chance X2: 65.3%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 31.1%; BTTS No (at least one team does not score): 68.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 34.7% | 2.88 |
| Draw | 33.9% | 2.95 |
| Rayo Vallecano win | 31.4% | 3.18 |

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
| 1 | 0-0 | 18.91% |
| 2 | 1-0 | 16.10% |
| 3 | 0-1 | 15.90% |
| 4 | 1-1 | 12.71% |
| 5 | 2-0 | 7.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 34.7% | 32.2% | 3.10 | +7.7% |
| Draw | 33.9% | 32.6% | 3.16 | +7.0% |
| Rayo Vallecano win | 31.4% | 35.2% | 2.80 | -12.0% |
| Over 2.5 | 23.0% | 35.9% | 2.61 | -39.9% |
| Under 2.5 | 77.0% | 64.1% | 1.54 | +18.5% |

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
| Market best home last update utc | 2026-10-13T11:02:58Z |
| Market best draw last update utc | 2026-10-13T11:02:27Z |
| Market best away last update utc | 2026-10-13T11:02:15Z |
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
| Fair Under 0.5 odds | 5.29 |
| Fair Over 1.5 odds | 2.04 |
| Fair Under 1.5 odds | 1.96 |
| Fair Over 2.5 odds | 4.34 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.81 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.90 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.1% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.3% |
| P home draw | 68.6% |
| P draw away | 65.3% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.99 |
| Reference draw odds | 2.95 |
| Reference away odds | 2.74 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 2.55 |
| Reference Under 2.5 odds | 1.50 |
| Home probability edge | +2.6% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -12.8% |
| Under 2.5 probability edge | +12.8% |
| Raw edge prob home | 0.0512 |
| Raw ev home | 0.1560 |
| Raw edge prob draw | 0.0247 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0759 |
| Raw ev away | -0.2265 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.1%**. Expected goals are 1.29 for Levante and 1.39 for Athletic Bilbao (2.68 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 49.5%; Under 3.5 goals: 71.8%; Double Chance 1X: 57.9%; Double Chance X2: 70.8%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 29.2% | 3.42 |
| Draw | 28.7% | 3.48 |
| Athletic Bilbao win | 42.1% | 2.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.29 |
| Athletic Bilbao expected goals | 1.39 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.64% |
| 2 | 0-1 | 9.97% |
| 3 | 1-2 | 9.19% |
| 4 | 0-0 | 7.71% |
| 5 | 1-0 | 7.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 29.2% | 24.0% | 3.90 | +14.0% |
| Draw | 28.7% | 31.0% | 3.52 | +1.0% |
| Athletic Bilbao win | 42.1% | 45.0% | 2.24 | -5.7% |
| Over 2.5 | 49.5% | 47.8% | 2.02 | -0.1% |
| Under 2.5 | 50.5% | 52.2% | 1.92 | -3.0% |

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
| Market best home last update utc | 2026-10-13T11:03:26Z |
| Market best draw last update utc | 2026-10-13T11:02:27Z |
| Market best away last update utc | 2026-10-13T11:02:27Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.3% |
| P btts no | 44.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.97 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.58 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 54.7% |
| P home draw | 57.9% |
| P draw away | 70.8% |
| Raw p home draw | 60.8% |
| Raw p draw away | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.90 |
| Reference draw odds | 3.05 |
| Reference away odds | 2.14 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.84 |
| Home probability edge | +5.3% |
| Draw probability edge | -2.3% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | +1.7% |
| Under 2.5 probability edge | -1.7% |
| Raw edge prob home | 0.1051 |
| Raw ev home | 0.3446 |
| Raw edge prob draw | -0.0466 |
| Raw ev draw | -0.0719 |
| Raw edge prob away | -0.0585 |
| Raw ev away | -0.1229 |

</details>


---
