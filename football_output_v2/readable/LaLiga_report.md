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

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **49.8%**. Expected goals are 2.04 for Deportivo La Coruña and 1.32 for Levante (3.36 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 64.4%; Under 3.5 goals: 57.0%; Double Chance 1X: 73.8%; Double Chance X2: 50.2%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 64.6%; BTTS No (at least one team does not score): 35.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 49.8% | 2.01 |
| Draw | 24.0% | 4.17 |
| Levante win | 26.2% | 3.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 2.04 |
| Levante expected goals | 1.32 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
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
| 1 | 1-1 | 10.53% |
| 2 | 2-1 | 8.81% |
| 3 | 2-2 | 6.96% |
| 4 | 2-0 | 6.67% |
| 5 | 1-2 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 49.8% | 45.7% | 2.17 | +8.0% |
| Draw | 24.0% | 26.3% | 3.62 | -13.1% |
| Levante win | 26.2% | 28.1% | 3.75 | -1.7% |
| Over 2.5 | 64.4% | 49.7% | 1.98 | +27.5% |
| Under 2.5 | 35.6% | 50.3% | 1.97 | -29.9% |

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
| Market best home last update utc | 2026-10-13T11:49:27Z |
| Market best draw last update utc | 2026-10-13T11:49:27Z |
| Market best away last update utc | 2026-10-13T11:51:25Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | La Coruna |
| Matched away-team name | Levante |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.6% |
| P btts no | 35.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.77 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.61 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.11 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 53.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 64.0% |
| P home draw | 73.8% |
| P draw away | 50.2% |
| Raw p home draw | 75.6% |
| Raw p draw away | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.90 |
| Home probability edge | +4.1% |
| Draw probability edge | -2.3% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +14.7% |
| Under 2.5 probability edge | -14.7% |
| Raw edge prob home | 0.0823 |
| Raw ev home | 0.1693 |
| Raw edge prob draw | -0.0454 |
| Raw ev draw | -0.2133 |
| Raw edge prob away | -0.0369 |
| Raw ev away | -0.0857 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **52.7%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 0-1 at 12.0%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 48.9%; Under 3.5 goals: 73.2%; Double Chance 1X: 47.3%; Double Chance X2: 77.2%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 22.8% | 4.38 |
| Draw | 24.4% | 4.09 |
| Atlético Madrid win | 52.7% | 1.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.02 |
| Atlético Madrid expected goals | 1.59 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.9% |
| Under 2.5 | 51.1% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.00% |
| 2 | 1-1 | 11.63% |
| 3 | 1-2 | 9.96% |
| 4 | 0-2 | 9.72% |
| 5 | 0-0 | 7.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 22.8% | 21.4% | 4.80 | +9.6% |
| Draw | 24.4% | 23.3% | 4.00 | -2.3% |
| Atlético Madrid win | 52.7% | 55.3% | 1.85 | -2.4% |
| Over 2.5 | 48.9% | 53.2% | 1.86 | -9.0% |
| Under 2.5 | 51.1% | 46.8% | 2.10 | +7.3% |

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
| Market best home last update utc | 2026-10-13T11:51:25Z |
| Market best draw last update utc | 2026-10-13T11:51:25Z |
| Market best away last update utc | 2026-10-13T11:50:56Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Espanol |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 93/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.81 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.93 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.2% |
| P home draw | 47.3% |
| P draw away | 77.2% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.10 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.72 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.03 |
| Home probability edge | +1.4% |
| Draw probability edge | +1.2% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | 0.0283 |
| Raw ev home | 0.1640 |
| Raw edge prob draw | 0.0231 |
| Raw ev draw | 0.0234 |
| Raw edge prob away | -0.0514 |
| Raw ev away | -0.0719 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **60.9%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 67.6%; Under 3.5 goals: 54.8%; Double Chance 1X: 39.1%; Double Chance X2: 79.5%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 20.5% | 4.89 |
| Draw | 18.6% | 5.38 |
| Barcelona win | 60.9% | 1.64 |

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
| Over 3.5 | 45.2% |
| Under 3.5 | 54.8% |
| Over 4.5 | 26.8% |
| Under 4.5 | 73.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.70% |
| 2 | 1-1 | 8.05% |
| 3 | 0-2 | 7.92% |
| 4 | 0-1 | 7.44% |
| 5 | 1-3 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 20.5% | 16.3% | 6.40 | +31.0% |
| Draw | 18.6% | 15.7% | 5.80 | +7.9% |
| Barcelona win | 60.9% | 68.0% | 1.49 | -9.2% |
| Over 2.5 | 67.6% | 77.6% | 1.26 | -14.8% |
| Under 2.5 | 32.4% | 22.4% | 3.92 | +26.9% |

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
| Market best home last update utc | 2026-10-13T11:51:25Z |
| Market best draw last update utc | 2026-10-13T11:51:25Z |
| Market best away last update utc | 2026-10-13T11:49:27Z |
| Odds bookmakers 1x2 | 20.00 |
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
| P btts yes | 64.0% |
| P btts no | 36.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.61 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.18 |
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
| P home draw | 39.1% |
| P draw away | 79.5% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 5.20 |
| Reference draw odds | 5.40 |
| Reference away odds | 1.42 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.92 |
| Home probability edge | +4.1% |
| Draw probability edge | +2.9% |
| Away probability edge | -7.1% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | 0.0827 |
| Raw ev home | 0.5743 |
| Raw edge prob draw | 0.0587 |
| Raw ev draw | 0.2486 |
| Raw edge prob away | -0.1414 |
| Raw ev away | -0.1973 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.6%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.2%; Under 3.5 goals: 81.1%; Double Chance 1X: 58.4%; Double Chance X2: 69.7%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.3%; BTTS No (at least one team does not score): 54.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.3% | 3.30 |
| Draw | 28.2% | 3.55 |
| Athletic Bilbao win | 41.6% | 2.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.07 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.2% |
| Under 2.5 | 60.8% |
| Over 3.5 | 18.9% |
| Under 3.5 | 81.1% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.41% |
| 2 | 1-1 | 13.06% |
| 3 | 0-0 | 10.48% |
| 4 | 1-0 | 10.22% |
| 5 | 1-2 | 8.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.3% | 27.5% | 3.65 | +10.5% |
| Draw | 28.2% | 27.0% | 3.58 | +0.8% |
| Athletic Bilbao win | 41.6% | 45.5% | 2.26 | -6.0% |
| Over 2.5 | 39.2% | 46.8% | 2.12 | -16.9% |
| Under 2.5 | 60.8% | 53.2% | 1.86 | +13.1% |

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
| Market best home last update utc | 2026-10-13T11:51:10Z |
| Market best draw last update utc | 2026-10-13T11:49:27Z |
| Market best away last update utc | 2026-10-13T11:51:24Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.3% |
| P btts no | 54.7% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.54 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.28 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.82 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 45.6% |
| P home draw | 58.4% |
| P draw away | 69.7% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.25 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.05 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.80 |
| Home probability edge | +2.8% |
| Draw probability edge | +1.1% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | 0.0560 |
| Raw ev home | 0.2070 |
| Raw edge prob draw | 0.0230 |
| Raw ev draw | 0.0492 |
| Raw edge prob away | -0.0790 |
| Raw ev away | -0.1497 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.6%**. Expected goals are 2.41 for Villarreal and 1.19 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 70.0%; Under 3.5 goals: 51.4%; Double Chance 1X: 83.7%; Double Chance X2: 34.4%; Under 4.5 goals: 70.5%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.6% | 1.52 |
| Draw | 18.0% | 5.56 |
| Elche CF win | 16.3% | 6.12 |

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
| Over 3.5 | 48.6% |
| Under 3.5 | 51.4% |
| Over 4.5 | 29.5% |
| Under 4.5 | 70.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.63% |
| 2 | 2-0 | 8.13% |
| 3 | 3-1 | 7.75% |
| 4 | 1-1 | 7.72% |
| 5 | 1-0 | 6.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.6% | 67.0% | 1.51 | -0.9% |
| Draw | 18.0% | 17.4% | 5.10 | -8.2% |
| Elche CF win | 16.3% | 15.6% | 6.73 | +10.0% |
| Over 2.5 | 70.0% | 67.0% | 1.45 | +1.5% |
| Under 2.5 | 30.0% | 33.0% | 2.79 | -16.2% |

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
| Market best home last update utc | 2026-10-13T11:49:27Z |
| Market best draw last update utc | 2026-10-13T11:51:25Z |
| Market best away last update utc | 2026-10-13T11:49:27Z |
| Odds bookmakers 1x2 | 20.00 |
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
| Fair Under 0.5 odds | 35.76 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.11 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.33 |
| Fair Over 3.5 odds | 2.06 |
| Fair Under 3.5 odds | 1.95 |
| Fair Over 4.5 odds | 3.38 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 63.4% |
| P home draw | 83.7% |
| P draw away | 34.4% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.44 |
| Reference draw odds | 4.90 |
| Reference away odds | 5.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.79 |
| Home probability edge | -1.3% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | -0.0261 |
| Raw ev home | -0.0284 |
| Raw edge prob draw | 0.0119 |
| Raw ev draw | -0.0515 |
| Raw edge prob away | 0.0142 |
| Raw ev away | 0.1480 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **55.8%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.33 combined). The most likely exact score is 2-2 at 7.4%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 79.4%; Under 3.5 goals: 38.0%; Double Chance 1X: 76.7%; Double Chance X2: 44.2%; Under 4.5 goals: 57.9%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 55.8% | 1.79 |
| Draw | 20.9% | 4.78 |
| Real Racing Club de Santander win | 23.3% | 4.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 2.78 |
| Real Racing Club de Santander expected goals | 1.55 |
| Expected total goals | 4.33 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 92.8% |
| Under 1.5 | 7.2% |
| Over 2.5 | 79.4% |
| Under 2.5 | 20.6% |
| Over 3.5 | 62.0% |
| Under 3.5 | 38.0% |
| Over 4.5 | 42.1% |
| Under 4.5 | 57.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.44% |
| 2 | 1-1 | 7.06% |
| 3 | 2-1 | 6.97% |
| 4 | 3-1 | 6.45% |
| 5 | 1-2 | 5.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 55.8% | 48.3% | 2.06 | +14.9% |
| Draw | 20.9% | 24.7% | 3.80 | -20.5% |
| Real Racing Club de Santander win | 23.3% | 27.0% | 3.95 | -8.0% |
| Over 2.5 | 79.4% | 57.0% | 1.74 | +38.1% |
| Under 2.5 | 20.6% | 43.0% | 2.27 | -53.1% |

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
| Market best home last update utc | 2026-10-13T11:51:25Z |
| Market best draw last update utc | 2026-10-13T11:51:25Z |
| Market best away last update utc | 2026-10-13T11:51:10Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Osasuna |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 75.1% |
| P btts no | 24.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 57.22 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.90 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.84 |
| Fair Over 3.5 odds | 1.61 |
| Fair Under 3.5 odds | 2.63 |
| Fair Over 4.5 odds | 2.37 |
| Fair Under 4.5 odds | 1.73 |
| Unadjusted home-win probability | 63.3% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 19.5% |
| Raw p over 1 5 | 93.1% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 73.9% |
| P home draw | 76.7% |
| P draw away | 44.2% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.96 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +7.5% |
| Draw probability edge | -3.7% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | +22.3% |
| Under 2.5 probability edge | -22.3% |
| Raw edge prob home | 0.1496 |
| Raw ev home | 0.3032 |
| Raw edge prob draw | -0.0745 |
| Raw ev draw | -0.3461 |
| Raw edge prob away | -0.0752 |
| Raw ev away | -0.2285 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **47.8%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 43.7%; Under 3.5 goals: 77.3%; Double Chance 1X: 75.0%; Double Chance X2: 52.2%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 47.8% | 2.09 |
| Draw | 27.2% | 3.68 |
| Alavés win | 25.0% | 3.99 |

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
| 2 | 1-0 | 12.32% |
| 3 | 2-0 | 9.36% |
| 4 | 0-0 | 9.19% |
| 5 | 2-1 | 8.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 47.8% | 45.8% | 2.24 | +7.0% |
| Draw | 27.2% | 27.8% | 3.58 | -2.6% |
| Alavés win | 25.0% | 26.4% | 4.00 | +0.1% |
| Over 2.5 | 43.7% | 44.7% | 2.26 | -1.3% |
| Under 2.5 | 56.3% | 55.3% | 1.79 | +0.8% |

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
| Market best home last update utc | 2026-10-13T11:51:25Z |
| Market best draw last update utc | 2026-10-13T11:49:27Z |
| Market best away last update utc | 2026-10-13T11:50:56Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.88 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.29 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.07 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 47.6% |
| P home draw | 75.0% |
| P draw away | 52.2% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Home probability edge | +1.9% |
| Draw probability edge | -0.6% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | 0.0389 |
| Raw ev home | 0.1135 |
| Raw edge prob draw | -0.0110 |
| Raw ev draw | -0.0457 |
| Raw edge prob away | -0.0279 |
| Raw ev away | -0.0545 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.2%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.6%. Goal-market probabilities: at least one goal: 85.8%; Over 2.5 goals: 29.6%; Under 3.5 goals: 87.9%; Double Chance 1X: 51.8%; Double Chance X2: 76.0%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.2%; BTTS No (at least one team does not score): 66.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 24.0% | 4.17 |
| Draw | 27.9% | 3.59 |
| Real Sociedad win | 48.2% | 2.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.8% |
| Under 0.5 | 14.2% |
| Over 1.5 | 56.1% |
| Under 1.5 | 43.9% |
| Over 2.5 | 29.6% |
| Under 2.5 | 70.4% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.58% |
| 2 | 0-0 | 14.21% |
| 3 | 1-0 | 12.16% |
| 4 | 1-1 | 11.28% |
| 5 | 0-2 | 11.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 24.0% | 29.7% | 3.40 | -18.5% |
| Draw | 27.9% | 25.6% | 3.70 | +3.1% |
| Real Sociedad win | 48.2% | 44.6% | 2.29 | +10.3% |
| Over 2.5 | 29.6% | 53.2% | 1.86 | -44.9% |
| Under 2.5 | 70.4% | 46.8% | 2.10 | +47.8% |

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
| Market best home last update utc | 2026-10-13T11:50:57Z |
| Market best draw last update utc | 2026-10-13T11:50:56Z |
| Market best away last update utc | 2026-10-13T11:49:27Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 33.2% |
| P btts no | 66.8% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 7.04 |
| Fair Over 1.5 odds | 1.78 |
| Fair Under 1.5 odds | 2.28 |
| Fair Over 2.5 odds | 3.37 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.25 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.15 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 51.8% |
| P draw away | 76.0% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.05 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.03 |
| Home probability edge | -5.8% |
| Draw probability edge | +2.3% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -23.6% |
| Under 2.5 probability edge | +23.6% |
| Raw edge prob home | -0.1155 |
| Raw ev home | -0.3813 |
| Raw edge prob draw | 0.0452 |
| Raw ev draw | 0.1150 |
| Raw edge prob away | 0.0703 |
| Raw ev away | 0.1832 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.9%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.1%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 66.0%; Under 3.5 goals: 56.3%; Double Chance 1X: 92.2%; Double Chance X2: 21.1%; Under 4.5 goals: 74.7%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.9% | 1.27 |
| Draw | 13.3% | 7.50 |
| Sevilla win | 7.8% | 12.85 |

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
| Over 2.5 | 66.0% |
| Under 2.5 | 34.0% |
| Over 3.5 | 43.7% |
| Under 3.5 | 56.3% |
| Over 4.5 | 25.3% |
| Under 4.5 | 74.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.11% |
| 2 | 3-0 | 10.60% |
| 3 | 1-0 | 9.09% |
| 4 | 2-1 | 8.98% |
| 5 | 3-1 | 7.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 78.9% | 80.3% | 1.30 | +2.5% |
| Draw | 13.3% | 12.2% | 7.00 | -6.7% |
| Sevilla win | 7.8% | 7.5% | 12.00 | -6.6% |
| Over 2.5 | 66.0% | 69.5% | 1.40 | -7.7% |
| Under 2.5 | 34.0% | 30.5% | 3.00 | +2.1% |

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
| Market best home last update utc | 2026-10-13T11:50:56Z |
| Market best draw last update utc | 2026-10-13T11:51:25Z |
| Market best away last update utc | 2026-10-13T11:51:10Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.37 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.79 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.94 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.95 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.21 |
| Reference draw odds | 6.25 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -1.4% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.0288 |
| Raw ev home | 0.0068 |
| Raw edge prob draw | 0.0234 |
| Raw ev draw | 0.0152 |
| Raw edge prob away | 0.0054 |
| Raw ev away | -0.0338 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.3%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.1%. Goal-market probabilities: at least one goal: 81.9%; Over 2.5 goals: 23.4%; Under 3.5 goals: 91.5%; Double Chance 1X: 67.7%; Double Chance X2: 64.7%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 30.8%; BTTS No (at least one team does not score): 69.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.3% | 2.83 |
| Draw | 32.4% | 3.08 |
| Rayo Vallecano win | 32.3% | 3.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.9% |
| Under 0.5 | 18.1% |
| Over 1.5 | 49.2% |
| Under 1.5 | 50.8% |
| Over 2.5 | 23.4% |
| Under 2.5 | 76.6% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.11% |
| 2 | 1-0 | 16.36% |
| 3 | 0-1 | 16.33% |
| 4 | 1-1 | 12.17% |
| 5 | 2-0 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.3% | 33.3% | 3.10 | +9.4% |
| Draw | 32.4% | 29.8% | 3.16 | +2.5% |
| Rayo Vallecano win | 32.3% | 36.9% | 2.80 | -9.6% |
| Over 2.5 | 23.4% | 35.8% | 2.61 | -39.0% |
| Under 2.5 | 76.6% | 64.2% | 1.54 | +18.0% |

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
| Market best home last update utc | 2026-10-13T11:51:25Z |
| Market best draw last update utc | 2026-10-13T11:49:27Z |
| Market best away last update utc | 2026-10-13T11:50:56Z |
| Odds bookmakers 1x2 | 19.00 |
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
| P btts yes | 30.8% |
| P btts no | 69.2% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.52 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.28 |
| Fair Under 2.5 odds | 1.31 |
| Fair Over 3.5 odds | 11.76 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.25 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.1% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.3% |
| P home draw | 67.7% |
| P draw away | 64.7% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.75 |
| Reference draw odds | 3.05 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.60 |
| Reference Under 2.5 odds | 1.51 |
| Home probability edge | +2.0% |
| Draw probability edge | +2.7% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -12.4% |
| Under 2.5 probability edge | +12.4% |
| Raw edge prob home | 0.0399 |
| Raw ev home | 0.1560 |
| Raw edge prob draw | 0.0533 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0931 |
| Raw ev away | -0.2265 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.8%**. Expected goals are 1.29 for Levante and 1.39 for Athletic Bilbao (2.68 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 50.1%; Under 3.5 goals: 71.8%; Double Chance 1X: 57.2%; Double Chance X2: 69.5%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 30.5% | 3.28 |
| Draw | 26.7% | 3.75 |
| Athletic Bilbao win | 42.8% | 2.34 |

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
| 1 | 1-1 | 12.68% |
| 2 | 0-1 | 10.14% |
| 3 | 1-2 | 9.35% |
| 4 | 1-0 | 7.59% |
| 5 | 0-2 | 7.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 30.5% | 26.5% | 3.90 | +18.9% |
| Draw | 26.7% | 27.0% | 3.52 | -6.0% |
| Athletic Bilbao win | 42.8% | 46.5% | 2.24 | -4.1% |
| Over 2.5 | 50.1% | 48.6% | 2.02 | +1.3% |
| Under 2.5 | 49.9% | 51.4% | 1.92 | -4.3% |

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
| Market best home last update utc | 2026-10-13T11:51:24Z |
| Market best draw last update utc | 2026-10-13T11:49:27Z |
| Market best away last update utc | 2026-10-13T11:49:27Z |
| Odds bookmakers 1x2 | 14.00 |
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
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.95 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.02 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.44 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 54.7% |
| P home draw | 57.2% |
| P draw away | 69.5% |
| Raw p home draw | 60.8% |
| Raw p draw away | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.15 |
| Reference draw odds | 3.10 |
| Reference away odds | 1.94 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.86 |
| Home probability edge | +4.0% |
| Draw probability edge | -0.3% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | +1.5% |
| Under 2.5 probability edge | -1.5% |
| Raw edge prob home | 0.0796 |
| Raw ev home | 0.3446 |
| Raw edge prob draw | -0.0065 |
| Raw ev draw | -0.0719 |
| Raw edge prob away | -0.0731 |
| Raw ev away | -0.1229 |

</details>


---
