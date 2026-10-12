# La Liga — football model report

Fixtures in this report: **11**.

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
| Live odds matched | 11.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
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

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.4%**. Expected goals are 1.84 for Deportivo La Coruña and 1.11 for Levante (2.95 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.8%; Under 3.5 goals: 66.1%; Double Chance 1X: 75.4%; Double Chance X2: 49.6%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.4% | 1.98 |
| Draw | 24.9% | 4.01 |
| Levante win | 24.6% | 4.06 |

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
| Over 2.5 | 55.8% |
| Under 2.5 | 44.2% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.71% |
| 2 | 2-1 | 9.13% |
| 3 | 1-0 | 8.79% |
| 4 | 2-0 | 8.23% |
| 5 | 1-2 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.4% | 46.5% | 2.17 | +9.5% |
| Draw | 24.9% | 26.8% | 3.62 | -9.7% |
| Levante win | 24.6% | 26.7% | 3.75 | -7.7% |
| Over 2.5 | 55.8% | 50.3% | 1.98 | +10.5% |
| Under 2.5 | 44.2% | 49.7% | 1.99 | -12.1% |

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
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:23Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | La Coruna |
| Matched away-team name | Levante |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.21 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.79 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.4% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 79.5% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.6% |
| P home draw | 75.4% |
| P draw away | 49.6% |
| Raw p home draw | 77.4% |
| Raw p draw away | 45.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.10 |
| Reference draw odds | 3.58 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | +3.9% |
| Draw probability edge | -1.9% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | +5.5% |
| Under 2.5 probability edge | -5.5% |
| Raw edge prob home | 0.0788 |
| Raw ev home | 0.1801 |
| Raw edge prob draw | -0.0376 |
| Raw ev draw | -0.1650 |
| Raw edge prob away | -0.0412 |
| Raw ev away | -0.1543 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **52.0%**. Expected goals are 1.03 for Espanyol and 1.58 for Atlético Madrid (2.60 combined). The most likely exact score is 0-1 at 12.0%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 48.5%; Under 3.5 goals: 73.4%; Double Chance 1X: 48.0%; Double Chance X2: 77.1%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 22.9% | 4.37 |
| Draw | 25.1% | 3.99 |
| Atlético Madrid win | 52.0% | 1.92 |

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
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 11.97% |
| 2 | 1-1 | 11.92% |
| 3 | 1-2 | 9.84% |
| 4 | 0-2 | 9.58% |
| 5 | 0-0 | 7.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 22.9% | 21.3% | 4.60 | +5.3% |
| Draw | 25.1% | 24.6% | 3.90 | -2.3% |
| Atlético Madrid win | 52.0% | 54.1% | 1.91 | -0.6% |
| Over 2.5 | 48.5% | 54.3% | 1.87 | -9.3% |
| Under 2.5 | 51.5% | 45.7% | 2.09 | +7.6% |

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
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:07Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Espanol |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 93/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.47 |
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
| P home draw | 48.0% |
| P draw away | 77.1% |
| Raw p home draw | 50.0% |
| Raw p draw away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.46 |
| Reference draw odds | 3.88 |
| Reference away odds | 1.81 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | +1.6% |
| Draw probability edge | +0.5% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.0321 |
| Raw ev home | 0.1270 |
| Raw edge prob draw | 0.0094 |
| Raw ev draw | -0.0045 |
| Raw edge prob away | -0.0415 |
| Raw ev away | -0.0455 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **61.8%**. Expected goals are 1.32 for Real Betis and 2.05 for Barcelona (3.37 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 66.7%; Under 3.5 goals: 55.8%; Double Chance 1X: 38.2%; Double Chance X2: 80.3%; Under 4.5 goals: 74.1%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.7% | 5.09 |
| Draw | 18.6% | 5.38 |
| Barcelona win | 61.8% | 1.62 |

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
| 1 | 1-2 | 10.89% |
| 2 | 0-2 | 8.22% |
| 3 | 1-1 | 8.13% |
| 4 | 0-1 | 7.88% |
| 5 | 1-3 | 7.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.7% | 14.9% | 6.40 | +25.8% |
| Draw | 18.6% | 15.6% | 6.00 | +11.6% |
| Barcelona win | 61.8% | 69.5% | 1.49 | -8.0% |
| Over 2.5 | 66.7% | 77.5% | 1.26 | -15.9% |
| Under 2.5 | 33.3% | 22.5% | 3.92 | +30.5% |

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
| Market best home last update utc | 2026-10-12T21:08:23Z |
| Market best draw last update utc | 2026-10-12T21:08:23Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
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
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.58 |
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
| P home draw | 38.2% |
| P draw away | 80.3% |
| Raw p home draw | 46.0% |
| Raw p draw away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 5.00 |
| Reference draw odds | 4.80 |
| Reference away odds | 1.36 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Home probability edge | +4.8% |
| Draw probability edge | +3.0% |
| Away probability edge | -7.7% |
| Over 2.5 probability edge | -10.8% |
| Under 2.5 probability edge | +10.8% |
| Raw edge prob home | 0.0953 |
| Raw ev home | 0.5627 |
| Raw edge prob draw | 0.0595 |
| Raw ev draw | 0.2943 |
| Raw edge prob away | -0.1548 |
| Raw ev away | -0.1952 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.5%**. Expected goals are 1.08 for Valencia and 1.17 for Athletic Bilbao (2.25 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.2%; Under 3.5 goals: 81.0%; Double Chance 1X: 58.5%; Double Chance X2: 70.0%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.5%; BTTS No (at least one team does not score): 54.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.0% | 3.33 |
| Draw | 28.5% | 3.51 |
| Athletic Bilbao win | 41.5% | 2.41 |

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
| 1 | 0-1 | 13.39% |
| 2 | 1-1 | 13.22% |
| 3 | 0-0 | 10.54% |
| 4 | 1-0 | 10.16% |
| 5 | 1-2 | 8.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.0% | 27.0% | 3.68 | +10.5% |
| Draw | 28.5% | 27.8% | 3.58 | +2.0% |
| Athletic Bilbao win | 41.5% | 45.2% | 2.22 | -7.9% |
| Over 2.5 | 39.2% | 45.7% | 2.12 | -16.9% |
| Under 2.5 | 60.8% | 54.3% | 1.86 | +13.1% |

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
| Market best home last update utc | 2026-10-12T21:08:21Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | BetOnline.ag |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.5% |
| P btts no | 54.5% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.49 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.79 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.1% |
| Unadjusted away-win probability | 37.8% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 45.6% |
| P home draw | 58.5% |
| P draw away | 70.0% |
| Raw p home draw | 62.2% |
| Raw p draw away | 66.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.40 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.75 |
| Home probability edge | +3.1% |
| Draw probability edge | +0.6% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | 0.0612 |
| Raw ev home | 0.2177 |
| Raw edge prob draw | 0.0126 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | -0.0738 |
| Raw ev away | -0.1608 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.8%**. Expected goals are 2.51 for Villarreal and 1.25 for Elche CF (3.76 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 72.5%; Under 3.5 goals: 48.0%; Double Chance 1X: 84.1%; Double Chance X2: 34.2%; Under 4.5 goals: 67.5%; BTTS Yes (both teams score): 65.7%; BTTS No (at least one team does not score): 34.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.8% | 1.52 |
| Draw | 18.3% | 5.46 |
| Elche CF win | 15.9% | 6.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.51 |
| Elche CF expected goals | 1.25 |
| Expected total goals | 3.76 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 89.1% |
| Under 1.5 | 10.9% |
| Over 2.5 | 72.5% |
| Under 2.5 | 27.5% |
| Over 3.5 | 52.0% |
| Under 3.5 | 48.0% |
| Over 4.5 | 32.5% |
| Under 4.5 | 67.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.33% |
| 2 | 3-1 | 7.80% |
| 3 | 1-1 | 7.53% |
| 4 | 2-0 | 7.44% |
| 5 | 3-0 | 6.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.8% | 66.9% | 1.51 | -0.7% |
| Draw | 18.3% | 18.6% | 5.10 | -6.5% |
| Elche CF win | 15.9% | 14.5% | 6.73 | +7.1% |
| Over 2.5 | 72.5% | 66.7% | 1.47 | +6.6% |
| Under 2.5 | 27.5% | 33.3% | 2.71 | -25.4% |

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
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:23Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
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
| P btts yes | 65.7% |
| P btts no | 34.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.57 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.20 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.63 |
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
| P home draw | 84.1% |
| P draw away | 34.2% |
| Raw p home draw | 82.6% |
| Raw p draw away | 35.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.47 |
| Reference draw odds | 5.02 |
| Reference away odds | 6.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | -1.2% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +5.7% |
| Under 2.5 probability edge | -5.7% |
| Raw edge prob home | -0.0234 |
| Raw ev home | -0.0247 |
| Raw edge prob draw | -0.0057 |
| Raw ev draw | -0.0798 |
| Raw edge prob away | 0.0291 |
| Raw ev away | 0.1687 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **56.0%**. Expected goals are 2.71 for CA Osasuna and 1.48 for Real Racing Club de Santander (4.19 combined). The most likely exact score is 1-1 at 7.5%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 77.6%; Under 3.5 goals: 40.5%; Double Chance 1X: 77.1%; Double Chance X2: 44.0%; Under 4.5 goals: 60.4%; BTTS Yes (both teams score): 73.4%; BTTS No (at least one team does not score): 26.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 56.0% | 1.79 |
| Draw | 21.2% | 4.72 |
| Real Racing Club de Santander win | 22.9% | 4.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 2.71 |
| Real Racing Club de Santander expected goals | 1.48 |
| Expected total goals | 4.19 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 91.9% |
| Under 1.5 | 8.1% |
| Over 2.5 | 77.6% |
| Under 2.5 | 22.4% |
| Over 3.5 | 59.5% |
| Under 3.5 | 40.5% |
| Over 4.5 | 39.6% |
| Under 4.5 | 60.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.50% |
| 2 | 2-2 | 7.43% |
| 3 | 2-1 | 7.26% |
| 4 | 3-1 | 6.56% |
| 5 | 1-2 | 5.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 56.0% | 48.5% | 2.04 | +14.2% |
| Draw | 21.2% | 25.0% | 3.75 | -20.6% |
| Real Racing Club de Santander win | 22.9% | 26.5% | 4.08 | -6.7% |
| Over 2.5 | 77.6% | 55.8% | 1.74 | +35.0% |
| Under 2.5 | 22.4% | 44.2% | 2.36 | -47.1% |

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
| Market best home last update utc | 2026-10-12T21:08:23Z |
| Market best draw last update utc | 2026-10-12T21:07:39Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
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
| P btts yes | 73.4% |
| P btts no | 26.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 51.38 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.41 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.46 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.47 |
| Fair Over 4.5 odds | 2.53 |
| Fair Under 4.5 odds | 1.65 |
| Unadjusted home-win probability | 63.4% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 19.2% |
| Raw p over 1 5 | 92.2% |
| Raw p under 3 5 | 39.7% |
| Raw p btts yes | 72.2% |
| P home draw | 77.1% |
| P draw away | 44.0% |
| Raw p home draw | 80.8% |
| Raw p draw away | 36.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.95 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | +7.5% |
| Draw probability edge | -3.8% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | +21.8% |
| Under 2.5 probability edge | -21.8% |
| Raw edge prob home | 0.1494 |
| Raw ev home | 0.2941 |
| Raw edge prob draw | -0.0758 |
| Raw ev draw | -0.3483 |
| Raw edge prob away | -0.0736 |
| Raw ev away | -0.2172 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **48.6%**. Expected goals are 1.51 for Celta Vigo and 0.96 for Alavés (2.47 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 44.5%; Under 3.5 goals: 76.5%; Double Chance 1X: 75.7%; Double Chance X2: 51.4%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 48.6% | 2.06 |
| Draw | 27.1% | 3.69 |
| Alavés win | 24.3% | 4.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.51 |
| Alavés expected goals | 0.96 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 70.7% |
| Under 1.5 | 29.3% |
| Over 2.5 | 44.5% |
| Under 2.5 | 55.5% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.80% |
| 2 | 1-0 | 12.31% |
| 3 | 2-0 | 9.40% |
| 4 | 2-1 | 9.05% |
| 5 | 0-0 | 8.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 48.6% | 47.6% | 2.08 | +1.1% |
| Draw | 27.1% | 27.8% | 3.58 | -3.1% |
| Alavés win | 24.3% | 24.6% | 4.00 | -2.8% |
| Over 2.5 | 44.5% | 45.3% | 2.19 | -2.5% |
| Under 2.5 | 55.5% | 54.7% | 1.79 | -0.7% |

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
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:23Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.25 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.63 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 70.8% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.3% |
| P home draw | 75.7% |
| P draw away | 51.4% |
| Raw p home draw | 76.0% |
| Raw p draw away | 50.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.00 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.73 |
| Home probability edge | +1.1% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | 0.0211 |
| Raw ev home | 0.0334 |
| Raw edge prob draw | -0.0149 |
| Raw ev draw | -0.0573 |
| Raw edge prob away | -0.0062 |
| Raw ev away | -0.0405 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.0%**. Expected goals are 0.57 for Málaga and 1.26 for Real Sociedad (1.83 combined). The most likely exact score is 0-1 at 18.1%. Goal-market probabilities: at least one goal: 84.4%; Over 2.5 goals: 27.6%; Under 3.5 goals: 89.0%; Double Chance 1X: 52.0%; Double Chance X2: 76.9%; Under 4.5 goals: 96.2%; BTTS Yes (both teams score): 31.1%; BTTS No (at least one team does not score): 68.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.1% | 4.33 |
| Draw | 28.9% | 3.46 |
| Real Sociedad win | 48.0% | 2.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.57 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.83 |
| Over 0.5 | 84.4% |
| Under 0.5 | 15.6% |
| Over 1.5 | 53.8% |
| Under 1.5 | 46.2% |
| Over 2.5 | 27.6% |
| Under 2.5 | 72.4% |
| Over 3.5 | 11.0% |
| Under 3.5 | 89.0% |
| Over 4.5 | 3.8% |
| Under 4.5 | 96.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.11% |
| 2 | 0-0 | 15.57% |
| 3 | 1-0 | 12.48% |
| 4 | 0-2 | 11.50% |
| 5 | 1-1 | 11.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.1% | 29.6% | 3.31 | -23.6% |
| Draw | 28.9% | 27.6% | 3.70 | +6.9% |
| Real Sociedad win | 48.0% | 42.8% | 2.29 | +9.9% |
| Over 2.5 | 27.6% | 52.2% | 1.86 | -48.7% |
| Under 2.5 | 72.4% | 47.8% | 2.10 | +52.1% |

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
| Market best home last update utc | 2026-10-12T21:08:37Z |
| Market best draw last update utc | 2026-10-12T21:07:39Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Coolbet |
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
| Fair Under 0.5 odds | 6.42 |
| Fair Over 1.5 odds | 1.86 |
| Fair Under 1.5 odds | 2.17 |
| Fair Over 2.5 odds | 3.63 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.12 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 26.56 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 16.6% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 53.2% |
| Raw p over 1 5 | 54.7% |
| Raw p under 3 5 | 88.7% |
| Raw p btts yes | 31.2% |
| P home draw | 52.0% |
| P draw away | 76.9% |
| Raw p home draw | 46.8% |
| Raw p draw away | 83.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.10 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | -6.5% |
| Draw probability edge | +1.2% |
| Away probability edge | +5.2% |
| Over 2.5 probability edge | -24.7% |
| Under 2.5 probability edge | +24.7% |
| Raw edge prob home | -0.1296 |
| Raw ev home | -0.4500 |
| Raw edge prob draw | 0.0249 |
| Raw ev draw | 0.1152 |
| Raw edge prob away | 0.1046 |
| Raw ev away | 0.2193 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **77.6%**. Expected goals are 2.62 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.5%; Under 3.5 goals: 56.5%; Double Chance 1X: 91.9%; Double Chance X2: 22.4%; Under 4.5 goals: 75.0%; BTTS Yes (both teams score): 48.7%; BTTS No (at least one team does not score): 51.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.6% | 1.29 |
| Draw | 14.2% | 7.02 |
| Sevilla win | 8.1% | 12.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.62 |
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
| 1 | 2-0 | 11.91% |
| 2 | 3-0 | 10.41% |
| 3 | 1-0 | 8.99% |
| 4 | 2-1 | 8.86% |
| 5 | 3-1 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.6% | 77.9% | 1.30 | +0.9% |
| Draw | 14.2% | 14.0% | 7.20 | +2.5% |
| Sevilla win | 8.1% | 8.1% | 12.50 | +1.4% |
| Over 2.5 | 65.5% | 70.4% | 1.39 | -9.0% |
| Under 2.5 | 34.5% | 29.6% | 3.07 | +6.0% |

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
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:23Z |
| Market best away last update utc | 2026-10-12T21:08:08Z |
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
| P btts yes | 48.7% |
| P btts no | 51.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.65 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.69 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 4.00 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.8% |
| P home draw | 91.9% |
| P draw away | 22.4% |
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
| Home probability edge | -0.3% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0054 |
| Raw ev home | 0.0059 |
| Raw edge prob draw | 0.0046 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | 0.0008 |
| Raw ev away | 0.0186 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.4%**. Expected goals are 0.92 for Getafe and 0.73 for Rayo Vallecano (1.65 combined). The most likely exact score is 0-0 at 18.5%. Goal-market probabilities: at least one goal: 81.5%; Over 2.5 goals: 23.4%; Under 3.5 goals: 91.4%; Double Chance 1X: 68.6%; Double Chance X2: 64.6%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 31.2%; BTTS No (at least one team does not score): 68.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.4% | 2.83 |
| Draw | 33.2% | 3.01 |
| Rayo Vallecano win | 31.4% | 3.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.92 |
| Rayo Vallecano expected goals | 0.73 |
| Expected total goals | 1.65 |
| Over 0.5 | 81.5% |
| Under 0.5 | 18.5% |
| Over 1.5 | 49.4% |
| Under 1.5 | 50.6% |
| Over 2.5 | 23.4% |
| Under 2.5 | 76.6% |
| Over 3.5 | 8.6% |
| Under 3.5 | 91.4% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.47% |
| 2 | 1-0 | 16.28% |
| 3 | 0-1 | 15.89% |
| 4 | 1-1 | 12.52% |
| 5 | 2-0 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.4% | 32.9% | 3.05 | +7.8% |
| Draw | 33.2% | 31.7% | 3.16 | +5.0% |
| Rayo Vallecano win | 31.4% | 35.4% | 2.87 | -9.9% |
| Over 2.5 | 23.4% | 36.6% | 2.61 | -39.0% |
| Under 2.5 | 76.6% | 63.4% | 1.53 | +17.3% |

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
| Market best home last update utc | 2026-10-12T21:08:23Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:07:39Z |
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
| P btts yes | 31.2% |
| P btts no | 68.8% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.41 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.28 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.60 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 36.93 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.8% |
| Unadjusted draw probability | 34.8% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 49.4% |
| Raw p under 3 5 | 91.4% |
| Raw p btts yes | 31.5% |
| P home draw | 68.6% |
| P draw away | 64.6% |
| Raw p home draw | 72.6% |
| Raw p draw away | 62.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.80 |
| Reference draw odds | 2.90 |
| Reference away odds | 2.62 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.45 |
| Reference Under 2.5 odds | 1.50 |
| Home probability edge | +2.4% |
| Draw probability edge | +1.5% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -13.2% |
| Under 2.5 probability edge | +13.2% |
| Raw edge prob home | 0.0487 |
| Raw ev home | 0.1527 |
| Raw edge prob draw | 0.0307 |
| Raw ev draw | 0.0989 |
| Raw edge prob away | -0.0794 |
| Raw ev away | -0.2127 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.0%**. Expected goals are 1.25 for Levante and 1.36 for Athletic Bilbao (2.61 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 48.0%; Under 3.5 goals: 73.5%; Double Chance 1X: 59.0%; Double Chance X2: 68.8%; Under 4.5 goals: 87.8%; BTTS Yes (both teams score): 53.4%; BTTS No (at least one team does not score): 46.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 31.2% | 3.20 |
| Draw | 27.7% | 3.61 |
| Athletic Bilbao win | 41.0% | 2.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.25 |
| Athletic Bilbao expected goals | 1.36 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 48.0% |
| Under 2.5 | 52.0% |
| Over 3.5 | 26.5% |
| Under 3.5 | 73.5% |
| Over 4.5 | 12.2% |
| Under 4.5 | 87.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.19% |
| 2 | 0-1 | 10.31% |
| 3 | 1-2 | 8.90% |
| 4 | 1-0 | 8.27% |
| 5 | 0-0 | 7.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 31.2% | 28.3% | 3.95 | +23.4% |
| Draw | 27.7% | 28.8% | 3.52 | -2.5% |
| Athletic Bilbao win | 41.0% | 43.0% | 2.25 | -7.7% |
| Over 2.5 | 48.0% | 47.8% | 2.02 | -3.1% |
| Under 2.5 | 52.0% | 52.2% | 1.92 | -0.1% |

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
| Market best home last update utc | 2026-10-12T21:08:23Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 53.4% |
| P btts no | 46.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.73 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.78 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.77 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.17 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 34.2% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 39.1% |
| Raw p over 1 5 | 73.6% |
| Raw p under 3 5 | 73.5% |
| Raw p btts yes | 53.1% |
| P home draw | 59.0% |
| P draw away | 68.8% |
| Raw p home draw | 60.9% |
| Raw p draw away | 65.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.25 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.80 |
| Home probability edge | +3.0% |
| Draw probability edge | -1.0% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0593 |
| Raw ev home | 0.3512 |
| Raw edge prob draw | -0.0209 |
| Raw ev draw | -0.0614 |
| Raw edge prob away | -0.0384 |
| Raw ev away | -0.1197 |

</details>


---
