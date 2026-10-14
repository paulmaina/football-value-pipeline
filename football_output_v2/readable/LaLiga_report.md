# La Liga — football model report

Fixtures in this report: **12**.

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
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 12.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
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

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.1%**. Expected goals are 2.04 for Deportivo La Coruña and 1.32 for Levante (3.36 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.0%; Double Chance 1X: 74.3%; Double Chance X2: 49.9%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.1% | 2.00 |
| Draw | 24.3% | 4.12 |
| Levante win | 25.7% | 3.89 |

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
| 1 | 1-1 | 10.65% |
| 2 | 2-1 | 8.86% |
| 3 | 2-2 | 7.03% |
| 4 | 2-0 | 6.71% |
| 5 | 1-2 | 6.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.1% | 46.2% | 2.17 | +8.6% |
| Draw | 24.3% | 26.8% | 3.62 | -12.2% |
| Levante win | 25.7% | 27.0% | 3.60 | -7.6% |
| Over 2.5 | 64.3% | 50.7% | 1.98 | +27.4% |
| Under 2.5 | 35.7% | 49.3% | 1.96 | -30.1% |

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
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
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
| Fair Under 0.5 odds | 24.51 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.62 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.11 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 53.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 64.0% |
| P home draw | 74.3% |
| P draw away | 49.9% |
| Raw p home draw | 75.6% |
| Raw p draw away | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.02 |
| Reference draw odds | 3.32 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +3.8% |
| Draw probability edge | -2.5% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | +13.7% |
| Under 2.5 probability edge | -13.7% |
| Raw edge prob home | 0.0766 |
| Raw ev home | 0.1693 |
| Raw edge prob draw | -0.0507 |
| Raw ev draw | -0.2133 |
| Raw edge prob away | -0.0259 |
| Raw ev away | -0.1223 |
| Market p home draw | 72.4% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:22:06Z |
| Market reference home draw last update utc | 2026-10-14T11:22:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.7% |
| Market draw away odds | 1.77 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:22:06Z |
| Market reference draw away last update utc | 2026-10-14T11:22:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.76 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 75.7% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:21:29Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.4% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:21:29Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.30 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.4% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:22:06Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **53.6%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 0-1 at 12.2%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 49.0%; Under 3.5 goals: 73.1%; Double Chance 1X: 46.4%; Double Chance X2: 78.1%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 21.9% | 4.56 |
| Draw | 24.4% | 4.09 |
| Atlético Madrid win | 53.6% | 1.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.02 |
| Atlético Madrid expected goals | 1.59 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 74.0% |
| Under 1.5 | 26.0% |
| Over 2.5 | 49.0% |
| Under 2.5 | 51.0% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.20% |
| 2 | 1-1 | 11.63% |
| 3 | 1-2 | 10.12% |
| 4 | 0-2 | 9.88% |
| 5 | 0-0 | 7.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 21.9% | 19.6% | 4.88 | +7.1% |
| Draw | 24.4% | 23.3% | 3.94 | -3.7% |
| Atlético Madrid win | 53.6% | 57.1% | 1.80 | -3.5% |
| Over 2.5 | 49.0% | 53.8% | 1.87 | -8.4% |
| Under 2.5 | 51.0% | 46.2% | 2.08 | +6.2% |

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
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
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
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.81 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.92 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.2% |
| P home draw | 46.4% |
| P draw away | 78.1% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 4.35 |
| Reference draw odds | 3.73 |
| Reference away odds | 1.66 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.09 |
| Home probability edge | +2.3% |
| Draw probability edge | +1.1% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | 0.0460 |
| Raw ev home | 0.1834 |
| Raw edge prob draw | 0.0229 |
| Raw ev draw | 0.0080 |
| Raw edge prob away | -0.0690 |
| Raw ev away | -0.0970 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **61.5%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 67.6%; Under 3.5 goals: 54.7%; Double Chance 1X: 38.5%; Double Chance X2: 80.2%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.8% | 5.05 |
| Draw | 18.8% | 5.33 |
| Barcelona win | 61.5% | 1.63 |

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
| 1 | 1-2 | 10.79% |
| 2 | 1-1 | 8.11% |
| 3 | 0-2 | 7.98% |
| 4 | 0-1 | 7.50% |
| 5 | 1-3 | 7.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.8% | 15.0% | 6.21 | +22.9% |
| Draw | 18.8% | 16.0% | 5.44 | +2.0% |
| Barcelona win | 61.5% | 69.0% | 1.49 | -8.4% |

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
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
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
| Fair Under 0.5 odds | 33.32 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.19 |
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
| P home draw | 38.5% |
| P draw away | 80.2% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 5.40 |
| Reference draw odds | 5.10 |
| Reference away odds | 1.39 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.99 |
| Home probability edge | +4.8% |
| Draw probability edge | +2.8% |
| Away probability edge | -7.6% |
| Over 2.5 probability edge | -10.2% |
| Under 2.5 probability edge | +10.2% |
| Raw edge prob home | 0.0961 |
| Raw ev home | 0.5275 |
| Raw edge prob draw | 0.0554 |
| Raw ev draw | 0.1711 |
| Raw edge prob away | -0.1516 |
| Raw ev away | -0.1973 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.0%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 0-1 at 13.2%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 39.1%; Under 3.5 goals: 81.1%; Double Chance 1X: 59.0%; Double Chance X2: 69.4%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.6% | 3.27 |
| Draw | 28.5% | 3.51 |
| Athletic Bilbao win | 41.0% | 2.44 |

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
| 1 | 0-1 | 13.22% |
| 2 | 1-1 | 13.20% |
| 3 | 0-0 | 10.59% |
| 4 | 1-0 | 10.33% |
| 5 | 1-2 | 8.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.6% | 28.1% | 3.47 | +6.1% |
| Draw | 28.5% | 27.6% | 3.51 | -0.1% |
| Athletic Bilbao win | 41.0% | 44.3% | 2.26 | -7.4% |
| Over 2.5 | 39.1% | 45.6% | 2.10 | -17.9% |
| Under 2.5 | 60.9% | 54.4% | 1.86 | +13.3% |

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
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
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
| Fair Under 0.5 odds | 9.44 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.28 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.86 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 45.6% |
| P home draw | 59.0% |
| P draw away | 69.4% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.18 |
| Reference draw odds | 3.23 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +2.5% |
| Draw probability edge | +0.8% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | 0.0498 |
| Raw ev home | 0.1475 |
| Raw edge prob draw | 0.0169 |
| Raw ev draw | 0.0287 |
| Raw edge prob away | -0.0667 |
| Raw ev away | -0.1497 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **66.4%**. Expected goals are 2.41 for Villarreal and 1.19 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 70.0%; Under 3.5 goals: 51.3%; Double Chance 1X: 84.4%; Double Chance X2: 33.6%; Under 4.5 goals: 70.4%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 66.4% | 1.50 |
| Draw | 18.0% | 5.56 |
| Elche CF win | 15.6% | 6.43 |

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
| Over 3.5 | 48.7% |
| Under 3.5 | 51.3% |
| Over 4.5 | 29.6% |
| Under 4.5 | 70.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.75% |
| 2 | 2-0 | 8.23% |
| 3 | 3-1 | 7.85% |
| 4 | 1-1 | 7.72% |
| 5 | 1-0 | 6.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 66.4% | 68.6% | 1.51 | +0.3% |
| Draw | 18.0% | 17.4% | 4.88 | -12.2% |
| Elche CF win | 15.6% | 14.0% | 6.73 | +4.7% |

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
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
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
| Fair Under 0.5 odds | 35.76 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.15 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.34 |
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
| P home draw | 84.4% |
| P draw away | 33.6% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.40 |
| Reference draw odds | 4.75 |
| Reference away odds | 5.75 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Home probability edge | -2.1% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +4.1% |
| Under 2.5 probability edge | -4.1% |
| Raw edge prob home | -0.0421 |
| Raw ev home | -0.0284 |
| Raw edge prob draw | 0.0119 |
| Raw ev draw | -0.0924 |
| Raw edge prob away | 0.0301 |
| Raw ev away | 0.1480 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **55.9%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.33 combined). The most likely exact score is 2-2 at 7.5%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.3%; Under 3.5 goals: 38.0%; Double Chance 1X: 77.1%; Double Chance X2: 44.1%; Under 4.5 goals: 57.9%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 55.9% | 1.79 |
| Draw | 21.2% | 4.71 |
| Real Racing Club de Santander win | 22.9% | 4.37 |

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
| Over 2.5 | 79.3% |
| Under 2.5 | 20.7% |
| Over 3.5 | 62.0% |
| Under 3.5 | 38.0% |
| Over 4.5 | 42.1% |
| Under 4.5 | 57.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.54% |
| 2 | 1-1 | 7.16% |
| 3 | 2-1 | 6.98% |
| 4 | 3-1 | 6.46% |
| 5 | 1-2 | 5.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 55.9% | 48.5% | 2.04 | +14.0% |
| Draw | 21.2% | 25.2% | 3.72 | -21.1% |
| Real Racing Club de Santander win | 22.9% | 26.2% | 3.88 | -11.2% |
| Over 2.5 | 79.3% | 57.3% | 1.74 | +38.0% |
| Under 2.5 | 20.7% | 42.7% | 2.27 | -53.0% |

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
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
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
| Fair Under 0.5 odds | 56.43 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.91 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.83 |
| Fair Over 3.5 odds | 1.61 |
| Fair Under 3.5 odds | 2.63 |
| Fair Over 4.5 odds | 2.38 |
| Fair Under 4.5 odds | 1.73 |
| Unadjusted home-win probability | 63.3% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 19.5% |
| Raw p over 1 5 | 93.1% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 73.9% |
| P home draw | 77.1% |
| P draw away | 44.1% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.93 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.38 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Home probability edge | +7.4% |
| Draw probability edge | -4.0% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | +22.0% |
| Under 2.5 probability edge | -22.0% |
| Raw edge prob home | 0.1472 |
| Raw ev home | 0.2905 |
| Raw edge prob draw | -0.0803 |
| Raw ev draw | -0.3599 |
| Raw edge prob away | -0.0669 |
| Raw ev away | -0.2422 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **47.9%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 43.6%; Under 3.5 goals: 77.3%; Double Chance 1X: 75.3%; Double Chance X2: 52.1%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 47.9% | 2.09 |
| Draw | 27.3% | 3.66 |
| Alavés win | 24.7% | 4.05 |

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
| Over 2.5 | 43.6% |
| Under 2.5 | 56.4% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.90% |
| 2 | 1-0 | 12.36% |
| 3 | 2-0 | 9.40% |
| 4 | 0-0 | 9.24% |
| 5 | 2-1 | 8.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 47.9% | 46.2% | 2.16 | +3.5% |
| Draw | 27.3% | 28.0% | 3.48 | -4.8% |
| Alavés win | 24.7% | 25.8% | 3.78 | -6.6% |
| Over 2.5 | 43.6% | 43.0% | 2.30 | +0.4% |
| Under 2.5 | 56.4% | 57.0% | 1.72 | -3.1% |

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
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
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
| Fair Under 0.5 odds | 10.83 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.29 |
| Fair Under 2.5 odds | 1.77 |
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
| P home draw | 75.3% |
| P draw away | 52.1% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.02 |
| Reference draw odds | 3.18 |
| Reference away odds | 3.43 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.24 |
| Reference Under 2.5 odds | 1.71 |
| Home probability edge | +1.8% |
| Draw probability edge | -0.7% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0354 |
| Raw ev home | 0.0737 |
| Raw edge prob draw | -0.0138 |
| Raw ev draw | -0.0724 |
| Raw edge prob away | -0.0216 |
| Raw ev away | -0.1065 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.2%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.6%. Goal-market probabilities: at least one goal: 85.6%; Over 2.5 goals: 29.6%; Under 3.5 goals: 87.9%; Double Chance 1X: 51.8%; Double Chance X2: 76.4%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.3%; BTTS No (at least one team does not score): 66.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.6% | 4.25 |
| Draw | 28.2% | 3.54 |
| Real Sociedad win | 48.2% | 2.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.6% |
| Under 0.5 | 14.4% |
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
| 1 | 0-1 | 17.61% |
| 2 | 0-0 | 14.38% |
| 3 | 1-0 | 11.94% |
| 4 | 1-1 | 11.42% |
| 5 | 0-2 | 11.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.6% | 28.9% | 3.29 | -22.5% |
| Draw | 28.2% | 26.3% | 3.63 | +2.4% |
| Real Sociedad win | 48.2% | 44.8% | 2.29 | +10.4% |
| Over 2.5 | 29.6% | 53.2% | 1.86 | -45.0% |
| Under 2.5 | 70.4% | 46.8% | 2.10 | +47.9% |

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
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
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
| P btts yes | 33.3% |
| P btts no | 66.7% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.95 |
| Fair Over 1.5 odds | 1.78 |
| Fair Under 1.5 odds | 2.28 |
| Fair Over 2.5 odds | 3.38 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.25 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.20 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 51.8% |
| P draw away | 76.4% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.38 |
| Reference away odds | 2.08 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.07 |
| Home probability edge | -5.4% |
| Draw probability edge | +1.9% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -23.7% |
| Under 2.5 probability edge | +23.7% |
| Raw edge prob home | -0.1072 |
| Raw ev home | -0.4013 |
| Raw edge prob draw | 0.0384 |
| Raw ev draw | 0.0939 |
| Raw edge prob away | 0.0688 |
| Raw ev away | 0.1832 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.7%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.1%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 65.9%; Under 3.5 goals: 56.3%; Double Chance 1X: 92.1%; Double Chance X2: 21.3%; Under 4.5 goals: 74.7%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.7% | 1.27 |
| Draw | 13.4% | 7.46 |
| Sevilla win | 7.9% | 12.73 |

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
| 1 | 2-0 | 12.08% |
| 2 | 3-0 | 10.58% |
| 3 | 1-0 | 9.07% |
| 4 | 2-1 | 8.96% |
| 5 | 3-1 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 78.7% | 80.0% | 1.30 | +2.4% |
| Draw | 13.4% | 12.3% | 6.61 | -11.4% |
| Sevilla win | 7.9% | 7.7% | 10.70 | -15.9% |

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
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
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
| Fair Under 0.5 odds | 30.20 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.78 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
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
| P home draw | 92.1% |
| P draw away | 21.3% |
| Raw p home draw | 91.9% |
| Raw p draw away | 22.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.21 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.94 |
| Home probability edge | -1.3% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | -0.0258 |
| Raw ev home | 0.0068 |
| Raw edge prob draw | 0.0219 |
| Raw ev draw | -0.0414 |
| Raw edge prob away | 0.0039 |
| Raw ev away | -0.1385 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.0%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.4%. Goal-market probabilities: at least one goal: 81.6%; Over 2.5 goals: 23.3%; Under 3.5 goals: 91.5%; Double Chance 1X: 67.8%; Double Chance X2: 65.0%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 30.9%; BTTS No (at least one team does not score): 69.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.0% | 2.86 |
| Draw | 32.9% | 3.04 |
| Rayo Vallecano win | 32.2% | 3.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.6% |
| Under 0.5 | 18.4% |
| Over 1.5 | 49.2% |
| Under 1.5 | 50.8% |
| Over 2.5 | 23.3% |
| Under 2.5 | 76.7% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.35% |
| 2 | 0-1 | 16.27% |
| 3 | 1-0 | 16.21% |
| 4 | 1-1 | 12.33% |
| 5 | 2-0 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.0% | 32.7% | 2.99 | +4.6% |
| Draw | 32.9% | 30.6% | 3.16 | +3.8% |
| Rayo Vallecano win | 32.2% | 36.7% | 2.74 | -11.9% |

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
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 30.9% |
| P btts no | 69.1% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.45 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.30 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.78 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.45 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.1% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.3% |
| P home draw | 67.8% |
| P draw away | 65.0% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.78 |
| Reference draw odds | 2.95 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.61 |
| Reference Under 2.5 odds | 1.51 |
| Home probability edge | +2.3% |
| Draw probability edge | +2.2% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -12.5% |
| Under 2.5 probability edge | +12.5% |
| Raw edge prob home | 0.0461 |
| Raw ev home | 0.1149 |
| Raw edge prob draw | 0.0446 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0908 |
| Raw ev away | -0.2431 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.6%**. Expected goals are 1.29 for Levante and 1.39 for Athletic Bilbao (2.68 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 50.1%; Under 3.5 goals: 71.8%; Double Chance 1X: 57.4%; Double Chance X2: 69.4%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 30.6% | 3.26 |
| Draw | 26.8% | 3.73 |
| Athletic Bilbao win | 42.6% | 2.35 |

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
| 1 | 1-1 | 12.74% |
| 2 | 0-1 | 10.08% |
| 3 | 1-2 | 9.29% |
| 4 | 1-0 | 7.62% |
| 5 | 0-2 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 30.6% | 26.8% | 3.52 | +7.8% |
| Draw | 26.8% | 27.2% | 3.52 | -5.7% |
| Athletic Bilbao win | 42.6% | 46.0% | 2.24 | -4.7% |
| Over 2.5 | 50.1% | 49.0% | 2.02 | +1.2% |
| Under 2.5 | 49.9% | 51.0% | 1.92 | -4.2% |

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
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
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
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.89 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.02 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.45 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 54.7% |
| P home draw | 57.4% |
| P draw away | 69.4% |
| Raw p home draw | 60.8% |
| Raw p draw away | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.32 |
| Reference draw odds | 3.27 |
| Reference away odds | 2.03 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +3.8% |
| Draw probability edge | -0.4% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | 0.0769 |
| Raw ev home | 0.2136 |
| Raw edge prob draw | -0.0087 |
| Raw ev draw | -0.0719 |
| Raw edge prob away | -0.0681 |
| Raw ev away | -0.1229 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **56.8%**. Expected goals are 1.38 for Alavés and 0.44 for Málaga (1.82 combined). The most likely exact score is 1-0 at 20.9%. Goal-market probabilities: at least one goal: 84.1%; Over 2.5 goals: 27.2%; Under 3.5 goals: 89.2%; Double Chance 1X: 83.9%; Double Chance X2: 43.2%; Under 4.5 goals: 96.3%; BTTS Yes (both teams score): 26.7%; BTTS No (at least one team does not score): 73.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 56.8% | 1.76 |
| Draw | 27.1% | 3.70 |
| Málaga win | 16.1% | 6.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.38 |
| Málaga expected goals | 0.44 |
| Expected total goals | 1.82 |
| Over 0.5 | 84.1% |
| Under 0.5 | 15.9% |
| Over 1.5 | 53.5% |
| Under 1.5 | 46.5% |
| Over 2.5 | 27.2% |
| Under 2.5 | 72.8% |
| Over 3.5 | 10.8% |
| Under 3.5 | 89.2% |
| Over 4.5 | 3.7% |
| Under 4.5 | 96.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.90% |
| 2 | 0-0 | 15.88% |
| 3 | 2-0 | 14.53% |
| 4 | 0-1 | 9.70% |
| 5 | 1-1 | 9.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 56.8% | 53.2% | 1.89 | +7.4% |
| Draw | 27.1% | 26.1% | 3.73 | +0.9% |
| Málaga win | 16.1% | 20.7% | 4.57 | -26.5% |
| Over 2.5 | 27.2% | 44.4% | 2.07 | -43.8% |
| Under 2.5 | 72.8% | 55.6% | 1.88 | +37.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T19:00:00+00:00 |
| Fixture id | 903eb4941471ffe20d525b02dd3b77aa |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:06Z |
| Market best draw last update utc | 2026-10-14T11:22:06Z |
| Market best away last update utc | 2026-10-14T11:22:06Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 26.7% |
| P btts no | 73.3% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.30 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.68 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.27 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 27.25 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 54.4% |
| Raw p under 3 5 | 88.9% |
| Raw p btts yes | 26.7% |
| P home draw | 83.9% |
| P draw away | 43.2% |
| Raw p home draw | 88.5% |
| Raw p draw away | 39.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.75 |
| Reference draw odds | 3.30 |
| Reference away odds | 4.05 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.13 |
| Reference Under 2.5 odds | 1.73 |
| Home probability edge | +3.6% |
| Draw probability edge | +1.0% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -17.3% |
| Under 2.5 probability edge | +17.3% |
| Raw edge prob home | 0.0721 |
| Raw ev home | 0.1426 |
| Raw edge prob draw | 0.0199 |
| Raw ev draw | 0.0465 |
| Raw edge prob away | -0.0920 |
| Raw ev away | -0.4749 |

</details>


---
