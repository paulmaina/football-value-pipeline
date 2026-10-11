# UEFA Champions League — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 521 |
| Training data through | 2026-09-10 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1537.063 |
| Base scoring parameter | 0.142 |
| Home-advantage parameter | 0.278 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0 |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 15.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |
| Data mode | offline_replay_of_committed_provider_responses |
| Provider response source commit | 1cd7e6bed154f42a64d727330bff7e94e7913210 |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-13 — Arsenal vs Lille

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Arsenal win** at **74.2%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.4%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 49.5%; Under 3.5 goals: 73.1%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 39.4%; BTTS No (at least one team does not score): 60.6%.
=======
The model's most likely 1X2 outcome is **Arsenal win** at **72.5%**. Expected goals are 2.01 for Arsenal and 0.77 for Lille (2.78 combined). The most likely exact score is 1-0 at 14.0%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 53.9%; Under 3.5 goals: 68.7%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 45.3%; BTTS No (at least one team does not score): 54.7%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Arsenal win | 74.2% | 1.35 |
| Draw | 16.1% | 6.23 |
| Lille win | 9.8% | 10.22 |
=======
| Arsenal win | 72.5% | 1.38 |
| Draw | 17.4% | 5.76 |
| Lille win | 10.1% | 9.89 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
<<<<<<< HEAD
| Arsenal expected goals | 1.93 |
| Lille expected goals | 0.65 |
| Expected total goals | 2.58 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 73.5% |
| Under 1.5 | 26.5% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |
=======
| Arsenal expected goals | 2.01 |
| Lille expected goals | 0.77 |
| Expected total goals | 2.78 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 77.0% |
| Under 1.5 | 23.0% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-0 | 16.37% |
| 2 | 2-0 | 15.29% |
| 3 | 2-1 | 10.00% |
| 4 | 3-0 | 9.83% |
| 5 | 1-1 | 7.42% |
=======
| 1 | 1-0 | 14.01% |
| 2 | 2-0 | 13.57% |
| 3 | 2-1 | 10.47% |
| 4 | 3-0 | 9.10% |
| 5 | 1-1 | 8.22% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Arsenal win | 74.2% | 80.2% | 1.29 | -4.3% |
| Draw | 16.1% | 12.5% | 7.40 | +18.8% |
| Lille win | 9.8% | 7.3% | 14.50 | +41.9% |
| Over 2.5 | 49.5% | 61.3% | 1.67 | -17.3% |
| Under 2.5 | 50.5% | 38.7% | 2.50 | +26.3% |
=======
| Arsenal win | 72.5% | 78.2% | 1.29 | -6.4% |
| Draw | 17.4% | 15.5% | 7.20 | +25.0% |
| Lille win | 10.1% | 6.4% | 14.50 | +46.6% |
| Over 2.5 | 53.9% | 62.4% | 1.67 | -10.0% |
| Under 2.5 | 46.1% | 37.6% | 2.48 | +14.3% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 93177465a42a0fb7802f1c8b06d6ee3a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:41Z |
| Market best draw last update utc | 2026-10-11T10:49:30Z |
| Market best away last update utc | 2026-10-11T10:49:29Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
<<<<<<< HEAD
| P btts yes | 39.4% |
| P btts no | 60.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.25 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.77 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.90 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 72.5% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 40.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.21 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -6.0% |
| Draw probability edge | +3.5% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -11.8% |
| Under 2.5 probability edge | +11.8% |
| Raw edge prob home | -0.1200 |
| Raw ev home | -0.1207 |
| Raw edge prob draw | 0.0709 |
| Raw ev draw | 0.4503 |
| Raw edge prob away | 0.0490 |
| Raw ev away | 0.7750 |
=======
| P btts yes | 45.3% |
| P btts no | 54.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.44 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.35 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 19.2% |
| Unadjusted away-win probability | 13.9% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.26 |
| Reference draw odds | 5.75 |
| Reference away odds | 13.25 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -5.6% |
| Draw probability edge | +1.9% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -8.5% |
| Under 2.5 probability edge | +8.5% |
| Raw edge prob home | -0.1127 |
| Raw ev home | -0.1372 |
| Raw edge prob draw | 0.0376 |
| Raw ev draw | 0.3859 |
| Raw edge prob away | 0.0751 |
| Raw ev away | 1.0110 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Atlético Madrid win** at **63.9%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.5%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.9%; Under 3.5 goals: 24.6%; Under 4.5 goals: 42.3%; BTTS Yes (both teams score): 78.7%; BTTS No (at least one team does not score): 21.3%.
=======
The model's most likely 1X2 outcome is **Atlético Madrid win** at **62.1%**. Expected goals are 3.87 for Atlético Madrid and 1.70 for Manchester United (5.57 combined). The most likely exact score is 2-2 at 6.4%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 90.1%; Under 3.5 goals: 20.8%; Under 4.5 goals: 37.5%; BTTS Yes (both teams score): 82.0%; BTTS No (at least one team does not score): 18.0%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Atlético Madrid win | 63.9% | 1.57 |
| Draw | 17.3% | 5.78 |
| Manchester United win | 18.8% | 5.31 |
=======
| Atlético Madrid win | 62.1% | 1.61 |
| Draw | 17.8% | 5.62 |
| Manchester United win | 20.1% | 4.98 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
<<<<<<< HEAD
| Atlético Madrid expected goals | 3.73 |
| Manchester United expected goals | 1.54 |
| Expected total goals | 5.27 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 87.9% |
| Under 2.5 | 12.1% |
| Over 3.5 | 75.4% |
| Under 3.5 | 24.6% |
| Over 4.5 | 57.7% |
| Under 4.5 | 42.3% |
=======
| Atlético Madrid expected goals | 3.87 |
| Manchester United expected goals | 1.70 |
| Expected total goals | 5.57 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.0% |
| Under 1.5 | 3.0% |
| Over 2.5 | 90.1% |
| Under 2.5 | 9.9% |
| Over 3.5 | 79.2% |
| Under 3.5 | 20.8% |
| Over 4.5 | 62.5% |
| Under 4.5 | 37.5% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 2-2 | 6.46% |
| 2 | 3-1 | 5.68% |
| 3 | 4-1 | 5.30% |
| 4 | 2-1 | 4.58% |
| 5 | 3-2 | 4.39% |
=======
| 1 | 2-2 | 6.43% |
| 2 | 3-1 | 5.11% |
| 3 | 4-1 | 4.94% |
| 4 | 3-3 | 4.70% |
| 5 | 3-2 | 4.35% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Atlético Madrid win | 63.9% | 50.7% | 2.07 | +32.2% |
| Draw | 17.3% | 23.2% | 4.10 | -29.1% |
| Manchester United win | 18.8% | 26.2% | 3.75 | -29.4% |
| Over 2.5 | 87.9% | 63.8% | 1.50 | +31.9% |
| Under 2.5 | 12.1% | 36.2% | 2.66 | -67.9% |
=======
| Atlético Madrid win | 62.1% | 48.1% | 2.07 | +28.6% |
| Draw | 17.8% | 24.1% | 4.10 | -27.1% |
| Manchester United win | 20.1% | 27.8% | 3.75 | -24.7% |
| Over 2.5 | 90.1% | 65.3% | 1.50 | +35.2% |
| Under 2.5 | 9.9% | 34.7% | 2.66 | -73.7% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | a9c22e08b395ee5753c8a65bc0eb97cf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:41Z |
| Market best draw last update utc | 2026-10-11T10:49:30Z |
| Market best away last update utc | 2026-10-11T10:49:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
<<<<<<< HEAD
| P btts yes | 78.7% |
| P btts no | 21.3% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 179.78 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.21 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.30 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.07 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.37 |
| Unadjusted home-win probability | 77.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 23.0% |
| Raw p btts yes | 76.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.86 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | +13.2% |
| Draw probability edge | -5.9% |
| Away probability edge | -7.3% |
| Over 2.5 probability edge | +24.2% |
| Under 2.5 probability edge | -24.2% |
| Raw edge prob home | 0.2642 |
| Raw ev home | 0.5957 |
| Raw edge prob draw | -0.1175 |
| Raw ev draw | -0.5321 |
| Raw edge prob away | -0.1467 |
| Raw ev away | -0.5687 |
=======
| P btts yes | 82.0% |
| P btts no | 18.0% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 251.81 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 33.77 |
| Fair Over 2.5 odds | 1.11 |
| Fair Under 2.5 odds | 10.11 |
| Fair Over 3.5 odds | 1.26 |
| Fair Under 3.5 odds | 4.80 |
| Fair Over 4.5 odds | 1.60 |
| Fair Under 4.5 odds | 2.67 |
| Unadjusted home-win probability | 76.2% |
| Unadjusted draw probability | 11.5% |
| Unadjusted away-win probability | 12.4% |
| Raw p over 1 5 | 97.4% |
| Raw p under 3 5 | 19.4% |
| Raw p btts yes | 80.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.02 |
| Reference draw odds | 3.92 |
| Reference away odds | 3.42 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.65 |
| Home probability edge | +14.0% |
| Draw probability edge | -6.3% |
| Away probability edge | -7.7% |
| Over 2.5 probability edge | +24.8% |
| Under 2.5 probability edge | -24.8% |
| Raw edge prob home | 0.2806 |
| Raw ev home | 0.5763 |
| Raw edge prob draw | -0.1266 |
| Raw ev draw | -0.5302 |
| Raw edge prob away | -0.1540 |
| Raw ev away | -0.5354 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Market p over 1 5 | 85.4% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T10:49:13Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 57.3% |
| Market under 3 5 odds | 1.69 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T10:49:14Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.23 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 66.8% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T10:49:29Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 2.82 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Barcelona win** at **69.3%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 78.0%; Under 3.5 goals: 41.7%; Under 4.5 goals: 60.8%; BTTS Yes (both teams score): 70.6%; BTTS No (at least one team does not score): 29.4%.
=======
The model's most likely 1X2 outcome is **Barcelona win** at **66.0%**. Expected goals are 1.61 for Galatasaray and 2.47 for Barcelona (4.09 combined). The most likely exact score is 1-2 at 9.6%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 78.2%; Under 3.5 goals: 40.9%; Under 4.5 goals: 60.3%; BTTS Yes (both teams score): 72.3%; BTTS No (at least one team does not score): 27.7%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Galatasaray win | 16.1% | 6.23 |
| Draw | 14.6% | 6.83 |
| Barcelona win | 69.3% | 1.44 |
=======
| Galatasaray win | 17.7% | 5.66 |
| Draw | 16.3% | 6.12 |
| Barcelona win | 66.0% | 1.52 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
<<<<<<< HEAD
| Galatasaray expected goals | 1.53 |
| Barcelona expected goals | 2.51 |
| Expected total goals | 4.04 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 78.0% |
| Under 2.5 | 22.0% |
| Over 3.5 | 58.3% |
| Under 3.5 | 41.7% |
| Over 4.5 | 39.2% |
| Under 4.5 | 60.8% |
=======
| Galatasaray expected goals | 1.61 |
| Barcelona expected goals | 2.47 |
| Expected total goals | 4.09 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 91.4% |
| Under 1.5 | 8.6% |
| Over 2.5 | 78.2% |
| Under 2.5 | 21.8% |
| Over 3.5 | 59.1% |
| Under 3.5 | 40.9% |
| Over 4.5 | 39.7% |
| Under 4.5 | 60.3% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-2 | 9.91% |
| 2 | 1-3 | 8.29% |
| 3 | 0-2 | 6.46% |
| 4 | 2-3 | 6.36% |
| 5 | 0-1 | 5.54% |
=======
| 1 | 1-2 | 9.60% |
| 2 | 1-3 | 7.92% |
| 3 | 2-3 | 6.40% |
| 4 | 2-2 | 5.99% |
| 5 | 0-2 | 5.95% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Galatasaray win | 16.1% | 9.2% | 10.00 | +60.6% |
| Draw | 14.6% | 11.4% | 7.40 | +8.3% |
| Barcelona win | 69.3% | 79.4% | 1.34 | -7.1% |
| Over 2.5 | 78.0% | 81.3% | 1.21 | -5.6% |
| Under 2.5 | 22.0% | 18.7% | 4.50 | -1.1% |
=======
| Galatasaray win | 17.7% | 10.5% | 10.00 | +76.6% |
| Draw | 16.3% | 14.4% | 7.40 | +20.9% |
| Barcelona win | 66.0% | 75.1% | 1.34 | -11.6% |
| Over 2.5 | 78.2% | 80.9% | 1.21 | -5.3% |
| Under 2.5 | 21.8% | 19.1% | 4.50 | -2.1% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | dd431688ed5c8f383b6434fd4f01e883 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:41Z |
| Market best draw last update utc | 2026-10-11T10:49:30Z |
| Market best away last update utc | 2026-10-11T10:48:41Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
<<<<<<< HEAD
| P btts yes | 70.6% |
| P btts no | 29.4% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 86.40 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.34 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.55 |
| Fair Over 3.5 odds | 1.71 |
| Fair Under 3.5 odds | 2.40 |
| Fair Over 4.5 odds | 2.55 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.5% |
| Raw p btts yes | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 7.80 |
| Reference draw odds | 6.50 |
| Reference away odds | 1.22 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.40 |
| Home probability edge | +6.8% |
| Draw probability edge | +3.2% |
| Away probability edge | -10.1% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | 0.1368 |
| Raw ev home | 1.2902 |
| Raw edge prob draw | 0.0650 |
| Raw ev draw | 0.3238 |
| Raw edge prob away | -0.2018 |
| Raw ev away | -0.2066 |
| Market p over 1 5 | 93.5% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:43:45Z |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 10.50 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 37.7% |
| Market under 3 5 odds | 2.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:43:30Z |
| Market reference under 3 5 odds | 2.47 |
| Market reference under 3 5 opposite odds | 1.55 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 68.0% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:43:30Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 2.88 |
| Market btts yes bookmakers | 4 |
=======
| P btts yes | 72.3% |
| P btts no | 27.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 83.24 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.69 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.60 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.44 |
| Fair Over 4.5 odds | 2.52 |
| Fair Under 4.5 odds | 1.66 |
| Unadjusted home-win probability | 24.9% |
| Unadjusted draw probability | 18.2% |
| Unadjusted away-win probability | 56.9% |
| Raw p over 1 5 | 91.1% |
| Raw p under 3 5 | 41.6% |
| Raw p btts yes | 73.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 8.40 |
| Reference draw odds | 6.20 |
| Reference away odds | 1.31 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.21 |
| Reference Under 2.5 odds | 4.45 |
| Home probability edge | +7.2% |
| Draw probability edge | +1.9% |
| Away probability edge | -9.1% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | 0.1439 |
| Raw ev home | 1.4854 |
| Raw edge prob draw | 0.0379 |
| Raw ev draw | 0.3490 |
| Raw edge prob away | -0.1818 |
| Raw ev away | -0.2373 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Inter Milan win** at **70.4%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 56.6%; Under 3.5 goals: 66.7%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.
=======
The model's most likely 1X2 outcome is **Inter Milan win** at **68.7%**. Expected goals are 1.98 for Inter Milan and 1.01 for Club Brugge (2.99 combined). The most likely exact score is 1-0 at 11.9%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 58.8%; Under 3.5 goals: 64.1%; Under 4.5 goals: 81.0%; BTTS Yes (both teams score): 53.1%; BTTS No (at least one team does not score): 46.9%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Inter Milan win | 70.4% | 1.42 |
| Draw | 16.6% | 6.01 |
| Club Brugge win | 12.9% | 7.73 |
=======
| Inter Milan win | 68.7% | 1.46 |
| Draw | 17.7% | 5.64 |
| Club Brugge win | 13.5% | 7.38 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
<<<<<<< HEAD
| Inter Milan expected goals | 1.92 |
| Club Brugge expected goals | 0.94 |
| Expected total goals | 2.86 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 56.6% |
| Under 2.5 | 43.4% |
| Over 3.5 | 33.3% |
| Under 3.5 | 66.7% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |
=======
| Inter Milan expected goals | 1.98 |
| Club Brugge expected goals | 1.01 |
| Expected total goals | 2.99 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 80.2% |
| Under 1.5 | 19.8% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 35.9% |
| Under 3.5 | 64.1% |
| Over 4.5 | 19.0% |
| Under 4.5 | 81.0% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-0 | 13.31% |
| 2 | 2-0 | 12.20% |
| 3 | 2-1 | 11.52% |
| 4 | 1-1 | 7.87% |
| 5 | 3-0 | 7.80% |
=======
| 1 | 1-0 | 11.93% |
| 2 | 2-1 | 11.30% |
| 3 | 2-0 | 11.24% |
| 4 | 1-1 | 8.32% |
| 5 | 3-1 | 7.46% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Inter Milan win | 70.4% | 80.2% | 1.31 | -7.7% |
| Draw | 16.6% | 12.5% | 6.60 | +9.8% |
| Club Brugge win | 12.9% | 7.3% | 12.00 | +55.3% |
| Over 2.5 | 56.6% | 67.0% | 1.44 | -18.5% |
| Under 2.5 | 43.4% | 33.0% | 2.83 | +22.9% |
=======
| Inter Milan win | 68.7% | 76.9% | 1.31 | -10.0% |
| Draw | 17.7% | 15.1% | 6.50 | +15.3% |
| Club Brugge win | 13.5% | 8.0% | 12.00 | +62.5% |
| Over 2.5 | 58.8% | 67.4% | 1.44 | -15.4% |
| Under 2.5 | 41.2% | 32.6% | 2.83 | +16.7% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | ca3f4b075d835413f9cb7bd3c439fdd0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:41Z |
| Market best draw last update utc | 2026-10-11T10:49:20Z |
| Market best away last update utc | 2026-10-11T10:49:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
<<<<<<< HEAD
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.05 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.63 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
| Fair Over 3.5 odds | 3.00 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.81 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 51.6% |
=======
| P btts yes | 53.1% |
| P btts no | 46.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.23 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.04 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.26 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 65.0% |
| Raw p btts yes | 54.1% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.28 |
| Reference draw odds | 5.90 |
| Reference away odds | 10.75 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
<<<<<<< HEAD
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -9.7% |
| Draw probability edge | +4.1% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | -0.1946 |
| Raw ev home | -0.2048 |
| Raw edge prob draw | 0.0825 |
| Raw ev draw | 0.3701 |
| Raw edge prob away | 0.1120 |
| Raw ev away | 1.2249 |
=======
| Reference Under 2.5 odds | 2.82 |
| Home probability edge | -8.2% |
| Draw probability edge | +2.6% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -8.6% |
| Under 2.5 probability edge | +8.6% |
| Raw edge prob home | -0.1636 |
| Raw ev home | -0.2070 |
| Raw edge prob draw | 0.0524 |
| Raw ev draw | 0.3234 |
| Raw edge prob away | 0.1112 |
| Raw ev away | 1.2926 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

<<<<<<< HEAD
The model's most likely 1X2 outcome is **RB Leipzig win** at **44.9%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 68.1%; Under 3.5 goals: 53.6%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.
=======
The model's most likely 1X2 outcome is **RB Leipzig win** at **43.8%**. Expected goals are 1.58 for RB Leipzig and 1.78 for PSV Eindhoven (3.36 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 65.1%; Under 3.5 goals: 56.9%; Under 4.5 goals: 75.3%; BTTS Yes (both teams score): 65.6%; BTTS No (at least one team does not score): 34.4%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| RB Leipzig win | 44.9% | 2.23 |
| Draw | 21.1% | 4.75 |
| PSV Eindhoven win | 34.0% | 2.94 |
=======
| RB Leipzig win | 43.8% | 2.28 |
| Draw | 21.8% | 4.59 |
| PSV Eindhoven win | 34.4% | 2.90 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
<<<<<<< HEAD
| RB Leipzig expected goals | 1.65 |
| PSV Eindhoven expected goals | 1.87 |
| Expected total goals | 3.52 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 86.0% |
| Under 1.5 | 14.0% |
| Over 2.5 | 68.1% |
| Under 2.5 | 31.9% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |
=======
| RB Leipzig expected goals | 1.58 |
| PSV Eindhoven expected goals | 1.78 |
| Expected total goals | 3.36 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 84.2% |
| Under 1.5 | 15.8% |
| Over 2.5 | 65.1% |
| Under 2.5 | 34.9% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 2-1 | 9.69% |
| 2 | 1-1 | 8.65% |
| 3 | 2-2 | 7.00% |
| 4 | 1-0 | 6.88% |
| 5 | 1-2 | 6.63% |
=======
| 1 | 2-1 | 9.67% |
| 2 | 1-1 | 9.32% |
| 3 | 1-0 | 7.49% |
| 4 | 1-2 | 6.90% |
| 5 | 2-2 | 6.89% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| RB Leipzig win | 44.9% | 54.8% | 1.90 | -14.7% |
| Draw | 21.1% | 21.0% | 4.80 | +1.1% |
| PSV Eindhoven win | 34.0% | 24.2% | 3.95 | +34.4% |
| Over 2.5 | 68.1% | 71.6% | 1.35 | -8.1% |
| Under 2.5 | 31.9% | 28.4% | 3.26 | +4.0% |
=======
| RB Leipzig win | 43.8% | 52.7% | 1.90 | -16.8% |
| Draw | 21.8% | 21.9% | 4.80 | +4.6% |
| PSV Eindhoven win | 34.4% | 25.4% | 3.95 | +36.0% |
| Over 2.5 | 65.1% | 72.5% | 1.35 | -12.1% |
| Under 2.5 | 34.9% | 27.5% | 3.26 | +13.8% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | da9e9e9eb9a238ed97827c4a8fbe6044 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:41Z |
| Market best draw last update utc | 2026-10-11T10:49:30Z |
| Market best away last update utc | 2026-10-11T10:49:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
<<<<<<< HEAD
| P btts yes | 67.9% |
| P btts no | 32.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.97 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.12 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.13 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.62 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 35.0% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 67.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.72 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -9.9% |
| Draw probability edge | +0.1% |
| Away probability edge | +9.8% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.1986 |
| Raw ev home | -0.3354 |
| Raw edge prob draw | 0.0023 |
| Raw ev draw | 0.0169 |
| Raw edge prob away | 0.1963 |
| Raw ev away | 0.7314 |
=======
| P btts yes | 65.6% |
| P btts no | 34.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.34 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.33 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.05 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 34.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 43.4% |
| Raw p over 1 5 | 84.4% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.85 |
| Reference draw odds | 4.30 |
| Reference away odds | 3.72 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.25 |
| Home probability edge | -8.9% |
| Draw probability edge | -0.1% |
| Away probability edge | +9.0% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | -0.1780 |
| Raw ev home | -0.3372 |
| Raw edge prob draw | -0.0018 |
| Raw ev draw | 0.0417 |
| Raw edge prob away | 0.1797 |
| Raw ev away | 0.7149 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Sporting Lisbon win** at **41.0%**. Expected goals are 1.28 for RC Lens and 1.60 for Sporting Lisbon (2.89 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.7%; Under 3.5 goals: 67.4%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.
=======
The model's most likely 1X2 outcome is **Sporting Lisbon win** at **42.2%**. Expected goals are 1.25 for RC Lens and 1.66 for Sporting Lisbon (2.91 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 55.2%; Under 3.5 goals: 67.0%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| RC Lens win | 34.7% | 2.88 |
| Draw | 24.3% | 4.12 |
| Sporting Lisbon win | 41.0% | 2.44 |
=======
| RC Lens win | 33.6% | 2.97 |
| Draw | 24.1% | 4.14 |
| Sporting Lisbon win | 42.2% | 2.37 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.28 |
| Sporting Lisbon expected goals | 1.60 |
| Expected total goals | 2.89 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 54.7% |
| Under 2.5 | 45.3% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-1 | 11.34% |
| 2 | 1-0 | 8.60% |
| 3 | 0-1 | 8.58% |
| 4 | 1-2 | 8.30% |
| 5 | 2-1 | 8.19% |
=======
| 1 | 1-1 | 11.26% |
| 2 | 0-1 | 8.53% |
| 3 | 1-0 | 8.41% |
| 4 | 1-2 | 8.34% |
| 5 | 2-1 | 8.07% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| RC Lens win | 34.7% | 38.2% | 2.62 | -9.1% |
| Draw | 24.3% | 25.2% | 3.91 | -5.0% |
| Sporting Lisbon win | 41.0% | 36.5% | 2.78 | +14.0% |
| Over 2.5 | 54.7% | 59.8% | 1.64 | -10.3% |
| Under 2.5 | 45.3% | 40.2% | 2.46 | +11.4% |
=======
| RC Lens win | 33.6% | 37.7% | 2.62 | -11.9% |
| Draw | 24.1% | 25.3% | 3.91 | -5.6% |
| Sporting Lisbon win | 42.2% | 37.0% | 2.76 | +16.6% |
| Over 2.5 | 55.2% | 60.8% | 1.64 | -9.5% |
| Under 2.5 | 44.8% | 39.2% | 2.46 | +10.3% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T16:45:00+00:00 |
| Fixture id | 2b0a946cac613732fcbf57ce931490a1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:41Z |
| Market best draw last update utc | 2026-10-11T10:49:13Z |
| Market best away last update utc | 2026-10-11T10:49:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Sporting Clube de Portugal |
| Home-name matching confidence | 86/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.22 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.09 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 45.5% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
<<<<<<< HEAD
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.40 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -3.5% |
| Draw probability edge | -1.0% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.0701 |
| Raw ev home | -0.1823 |
| Raw edge prob draw | -0.0191 |
| Raw ev draw | -0.0874 |
| Raw edge prob away | 0.0891 |
| Raw ev away | 0.2635 |
=======
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.55 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.60 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Home probability edge | -4.1% |
| Draw probability edge | -1.1% |
| Away probability edge | +5.2% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | -0.0825 |
| Raw ev home | -0.2273 |
| Raw edge prob draw | -0.0223 |
| Raw ev draw | -0.0995 |
| Raw edge prob away | 0.1049 |
| Raw ev away | 0.3104 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Slavia Praha win** at **54.4%**. Expected goals are 0.38 for Sabah FK and 1.28 for Slavia Praha (1.66 combined). The most likely exact score is 0-1 at 22.5%. Goal-market probabilities: at least one goal: 82.7%; Over 2.5 goals: 22.8%; Under 3.5 goals: 91.8%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 22.0%; BTTS No (at least one team does not score): 78.0%.
=======
The model's most likely 1X2 outcome is **Slavia Praha win** at **54.2%**. Expected goals are 0.37 for Sabah FK and 1.26 for Slavia Praha (1.63 combined). The most likely exact score is 0-1 at 22.8%. Goal-market probabilities: at least one goal: 82.1%; Over 2.5 goals: 22.1%; Under 3.5 goals: 92.1%; Under 4.5 goals: 97.6%; BTTS Yes (both teams score): 21.7%; BTTS No (at least one team does not score): 78.3%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Sabah FK win | 19.1% | 5.24 |
| Draw | 26.5% | 3.78 |
| Slavia Praha win | 54.4% | 1.84 |
=======
| Sabah FK win | 18.7% | 5.33 |
| Draw | 27.1% | 3.69 |
| Slavia Praha win | 54.2% | 1.85 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
<<<<<<< HEAD
| Sabah FK expected goals | 0.38 |
| Slavia Praha expected goals | 1.28 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.7% |
| Under 0.5 | 17.3% |
| Over 1.5 | 47.3% |
| Under 1.5 | 52.7% |
| Over 2.5 | 22.8% |
| Under 2.5 | 77.2% |
| Over 3.5 | 8.2% |
| Under 3.5 | 91.8% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |
=======
| Sabah FK expected goals | 0.37 |
| Slavia Praha expected goals | 1.26 |
| Expected total goals | 1.63 |
| Over 0.5 | 82.1% |
| Under 0.5 | 17.9% |
| Over 1.5 | 46.6% |
| Under 1.5 | 53.4% |
| Over 2.5 | 22.1% |
| Under 2.5 | 77.9% |
| Over 3.5 | 7.9% |
| Under 3.5 | 92.1% |
| Over 4.5 | 2.4% |
| Under 4.5 | 97.6% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 0-1 | 22.53% |
| 2 | 0-0 | 17.28% |
| 3 | 0-2 | 14.14% |
| 4 | 1-0 | 12.90% |
| 5 | 1-1 | 8.11% |
=======
| 1 | 0-1 | 22.81% |
| 2 | 0-0 | 17.86% |
| 3 | 0-2 | 14.06% |
| 4 | 1-0 | 12.74% |
| 5 | 1-1 | 8.17% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Sabah FK win | 19.1% | 26.9% | 3.74 | -28.6% |
| Draw | 26.5% | 24.4% | 4.00 | +5.9% |
| Slavia Praha win | 54.4% | 48.8% | 2.12 | +15.4% |
| Over 2.5 | 22.8% | 57.8% | 1.71 | -61.1% |
| Under 2.5 | 77.2% | 42.2% | 2.32 | +79.2% |
=======
| Sabah FK win | 18.7% | 26.0% | 3.74 | -29.9% |
| Draw | 27.1% | 25.2% | 4.00 | +8.4% |
| Slavia Praha win | 54.2% | 48.8% | 2.10 | +13.7% |
| Over 2.5 | 22.1% | 58.1% | 1.71 | -62.2% |
| Under 2.5 | 77.9% | 41.9% | 2.32 | +80.7% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T16:45:00+00:00 |
| Fixture id | 46f726554e6876fb828c767bfbfdfdad |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:41Z |
| Market best draw last update utc | 2026-10-11T10:48:57Z |
| Market best away last update utc | 2026-10-11T10:49:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
<<<<<<< HEAD
| P btts yes | 22.0% |
| P btts no | 78.0% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.79 |
| Fair Over 1.5 odds | 2.11 |
| Fair Under 1.5 odds | 1.90 |
| Fair Over 2.5 odds | 4.39 |
| Fair Under 2.5 odds | 1.29 |
| Fair Over 3.5 odds | 12.20 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 38.79 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.3% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 60.1% |
| Raw p over 1 5 | 48.8% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 22.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.60 |
| Reference away odds | 1.92 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | -7.8% |
| Draw probability edge | +2.1% |
| Away probability edge | +5.7% |
| Over 2.5 probability edge | -35.0% |
| Under 2.5 probability edge | +35.0% |
| Raw edge prob home | -0.1552 |
| Raw ev home | -0.5761 |
| Raw edge prob draw | 0.0415 |
| Raw ev draw | 0.1420 |
| Raw edge prob away | 0.1136 |
| Raw ev away | 0.2744 |
| Market p over 1 5 | 81.0% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:43:48Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 64.5% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:43:30Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.61 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.1% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:43:30Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.32 |
| Market btts yes bookmakers | 4 |
=======
| P btts yes | 21.7% |
| P btts no | 78.3% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.60 |
| Fair Over 1.5 odds | 2.15 |
| Fair Under 1.5 odds | 1.87 |
| Fair Over 2.5 odds | 4.52 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 12.70 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 41.01 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 11.5% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 59.5% |
| Raw p over 1 5 | 48.0% |
| Raw p under 3 5 | 91.7% |
| Raw p btts yes | 21.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.64 |
| Reference draw odds | 3.76 |
| Reference away odds | 1.99 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -7.3% |
| Draw probability edge | +1.9% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | -36.0% |
| Under 2.5 probability edge | +36.0% |
| Raw edge prob home | -0.1455 |
| Raw ev home | -0.5708 |
| Raw edge prob draw | 0.0387 |
| Raw ev draw | 0.1611 |
| Raw edge prob away | 0.1068 |
| Raw ev away | 0.2494 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Bayern Munich win** at **92.7%**. Expected goals are 0.70 for Viking FK and 4.46 for Bayern Munich (5.16 combined). The most likely exact score is 0-4 at 9.4%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.4%; Under 3.5 goals: 24.9%; Under 4.5 goals: 42.0%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.
=======
The model's most likely 1X2 outcome is **Bayern Munich win** at **92.4%**. Expected goals are 0.69 for Viking FK and 4.47 for Bayern Munich (5.16 combined). The most likely exact score is 0-4 at 9.5%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.2%; Under 3.5 goals: 25.1%; Under 4.5 goals: 42.2%; BTTS Yes (both teams score): 49.6%; BTTS No (at least one team does not score): 50.4%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Viking FK win | 2.5% | 40.25 |
| Draw | 4.8% | 20.85 |
| Bayern Munich win | 92.7% | 1.08 |
=======
| Viking FK win | 2.7% | 37.61 |
| Draw | 4.9% | 20.21 |
| Bayern Munich win | 92.4% | 1.08 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.70 |
| Bayern Munich expected goals | 4.46 |
| Expected total goals | 5.16 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
<<<<<<< HEAD
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 88.4% |
| Under 2.5 | 11.6% |
| Over 3.5 | 75.1% |
| Under 3.5 | 24.9% |
| Over 4.5 | 58.0% |
| Under 4.5 | 42.0% |
=======
| Over 1.5 | 96.1% |
| Under 1.5 | 3.9% |
| Over 2.5 | 88.2% |
| Under 2.5 | 11.8% |
| Over 3.5 | 74.9% |
| Under 3.5 | 25.1% |
| Over 4.5 | 57.8% |
| Under 4.5 | 42.2% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 0-4 | 9.44% |
| 2 | 0-3 | 8.46% |
| 3 | 0-5 | 8.42% |
| 4 | 1-4 | 6.58% |
| 5 | 0-6 | 6.26% |
=======
| 1 | 0-4 | 9.46% |
| 2 | 0-3 | 8.47% |
| 3 | 0-5 | 8.46% |
| 4 | 1-4 | 6.52% |
| 5 | 0-6 | 6.30% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Viking FK win | 2.5% | 3.0% | 27.00 | -32.9% |
| Draw | 4.8% | 5.4% | 15.50 | -25.7% |
| Bayern Munich win | 92.7% | 91.6% | 1.11 | +2.9% |
| Over 2.5 | 88.4% | 85.4% | 1.15 | +1.6% |
| Under 2.5 | 11.6% | 14.6% | 5.90 | -31.3% |
=======
| Viking FK win | 2.7% | 3.4% | 27.00 | -28.2% |
| Draw | 4.9% | 5.8% | 15.50 | -23.3% |
| Bayern Munich win | 92.4% | 90.9% | 1.11 | +2.6% |
| Over 2.5 | 88.2% | 86.8% | 1.15 | +1.4% |
| Under 2.5 | 11.8% | 13.2% | 5.90 | -30.4% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 8a9d20b23417357011c10585a99335e9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:49:29Z |
| Market best draw last update utc | 2026-10-11T10:48:41Z |
| Market best away last update utc | 2026-10-11T10:49:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
<<<<<<< HEAD
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 178.68 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.19 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.59 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.02 |
| Fair Over 4.5 odds | 1.72 |
| Fair Under 4.5 odds | 2.38 |
| Unadjusted home-win probability | 2.0% |
| Unadjusted draw probability | 4.2% |
| Unadjusted away-win probability | 93.8% |
=======
| P btts yes | 49.6% |
| P btts no | 50.4% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 170.33 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 25.69 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.47 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 3.99 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.37 |
| Unadjusted home-win probability | 1.9% |
| Unadjusted draw probability | 4.1% |
| Unadjusted away-win probability | 93.9% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Raw p over 1 5 | 96.3% |
| Raw p under 3 5 | 24.5% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
<<<<<<< HEAD
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 15.00 |
| Reference draw odds | 9.50 |
| Reference away odds | 1.07 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.50 |
| Home probability edge | -0.5% |
| Draw probability edge | -0.6% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | -0.0101 |
| Raw ev home | -0.4657 |
| Raw edge prob draw | -0.0122 |
| Raw ev draw | -0.3512 |
| Raw edge prob away | 0.0223 |
| Raw ev away | 0.0416 |
| Market p over 1 5 | 95.4% |
=======
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 21.00 |
| Reference draw odds | 13.00 |
| Reference away odds | 1.09 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.13 |
| Reference Under 2.5 odds | 5.80 |
| Home probability edge | -0.7% |
| Draw probability edge | -0.8% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +1.4% |
| Under 2.5 probability edge | -1.4% |
| Raw edge prob home | -0.0144 |
| Raw ev home | -0.4769 |
| Raw edge prob draw | -0.0163 |
| Raw ev draw | -0.3593 |
| Raw edge prob away | 0.0307 |
| Raw ev away | 0.0426 |
| Market p over 1 5 | 95.5% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-11T10:49:23Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 14.00 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 32.7% |
| Market under 3 5 odds | 2.93 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T10:48:57Z |
| Market reference under 3 5 odds | 2.64 |
| Market reference under 3 5 opposite odds | 1.41 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 55.7% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-11T10:49:19Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.18 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Napoli win** at **40.1%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 40.3%; Under 3.5 goals: 80.2%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 44.4%; BTTS No (at least one team does not score): 55.6%.
=======
The model's most likely 1X2 outcome is **Napoli win** at **40.6%**. Expected goals are 0.87 for Villarreal and 1.43 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 39.9%; Under 3.5 goals: 80.5%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 44.0%; BTTS No (at least one team does not score): 56.0%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Villarreal win | 34.4% | 2.91 |
| Draw | 25.5% | 3.92 |
| Napoli win | 40.1% | 2.49 |
=======
| Villarreal win | 33.5% | 2.99 |
| Draw | 25.9% | 3.85 |
| Napoli win | 40.6% | 2.47 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.90 |
| Napoli expected goals | 1.42 |
| Expected total goals | 2.31 |
<<<<<<< HEAD
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 65.7% |
| Under 1.5 | 34.3% |
| Over 2.5 | 40.3% |
| Under 2.5 | 59.7% |
| Over 3.5 | 19.8% |
| Under 3.5 | 80.2% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |
=======
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 39.9% |
| Under 2.5 | 60.1% |
| Over 3.5 | 19.5% |
| Under 3.5 | 80.5% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-0 | 13.34% |
| 2 | 1-1 | 11.81% |
| 3 | 0-1 | 11.80% |
| 4 | 0-0 | 9.15% |
| 5 | 0-2 | 8.00% |
=======
| 1 | 1-0 | 13.25% |
| 2 | 1-1 | 11.97% |
| 3 | 0-1 | 11.90% |
| 4 | 0-0 | 9.43% |
| 5 | 0-2 | 8.17% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Villarreal win | 34.4% | 44.3% | 2.33 | -19.9% |
| Draw | 25.5% | 25.3% | 3.90 | -0.4% |
| Napoli win | 40.1% | 30.5% | 3.30 | +32.4% |
| Over 2.5 | 40.3% | 58.9% | 1.71 | -31.1% |
| Under 2.5 | 59.7% | 41.1% | 2.44 | +45.6% |
=======
| Villarreal win | 33.5% | 43.4% | 2.33 | -22.0% |
| Draw | 25.9% | 26.2% | 3.90 | +1.2% |
| Napoli win | 40.6% | 30.4% | 3.35 | +35.9% |
| Over 2.5 | 39.9% | 58.1% | 1.71 | -31.8% |
| Under 2.5 | 60.1% | 41.9% | 2.46 | +47.9% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 09e41b63d1d59bd4d971c54ffce154d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:49:14Z |
| Market best draw last update utc | 2026-10-11T10:49:30Z |
| Market best away last update utc | 2026-10-11T10:49:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
<<<<<<< HEAD
| P btts yes | 44.4% |
| P btts no | 55.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.92 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.92 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.06 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.02 |
=======
| P btts yes | 44.0% |
| P btts no | 56.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.60 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.51 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.13 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.26 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 44.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.23 |
| Reference draw odds | 3.62 |
| Reference away odds | 3.14 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -9.9% |
<<<<<<< HEAD
| Draw probability edge | +0.3% |
| Away probability edge | +9.6% |
| Over 2.5 probability edge | -18.6% |
| Under 2.5 probability edge | +18.6% |
| Raw edge prob home | -0.1982 |
| Raw ev home | -0.4304 |
| Raw edge prob draw | 0.0054 |
| Raw ev draw | 0.0060 |
| Raw edge prob away | 0.1928 |
| Raw ev away | 0.6420 |
=======
| Draw probability edge | -0.3% |
| Away probability edge | +10.2% |
| Over 2.5 probability edge | -18.2% |
| Under 2.5 probability edge | +18.2% |
| Raw edge prob home | -0.1980 |
| Raw ev home | -0.4502 |
| Raw edge prob draw | -0.0053 |
| Raw ev draw | 0.0015 |
| Raw edge prob away | 0.2033 |
| Raw ev away | 0.6992 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Real Madrid win** at **51.0%**. Expected goals are 1.18 for AS Roma and 1.68 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.5%; Under 3.5 goals: 67.8%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.
=======
The model's most likely 1X2 outcome is **Real Madrid win** at **51.4%**. Expected goals are 1.26 for AS Roma and 1.83 for Real Madrid (3.09 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 59.5%; Under 3.5 goals: 62.6%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 59.9%; BTTS No (at least one team does not score): 40.1%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| AS Roma win | 26.1% | 3.82 |
| Draw | 22.9% | 4.37 |
| Real Madrid win | 51.0% | 1.96 |
=======
| AS Roma win | 25.9% | 3.86 |
| Draw | 22.7% | 4.41 |
| Real Madrid win | 51.4% | 1.95 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
<<<<<<< HEAD
| AS Roma expected goals | 1.18 |
| Real Madrid expected goals | 1.68 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 54.5% |
| Under 2.5 | 45.5% |
| Over 3.5 | 32.2% |
| Under 3.5 | 67.8% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |
=======
| AS Roma expected goals | 1.26 |
| Real Madrid expected goals | 1.83 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 59.5% |
| Under 2.5 | 40.5% |
| Over 3.5 | 37.4% |
| Under 3.5 | 62.6% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-1 | 10.75% |
| 2 | 0-1 | 10.46% |
| 3 | 1-2 | 9.78% |
| 4 | 0-2 | 8.31% |
| 5 | 1-0 | 7.01% |
=======
| 1 | 1-1 | 10.35% |
| 2 | 1-2 | 9.61% |
| 3 | 0-1 | 8.84% |
| 4 | 0-2 | 7.62% |
| 5 | 2-1 | 6.38% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| AS Roma win | 26.1% | 25.0% | 4.20 | +9.8% |
| Draw | 22.9% | 22.8% | 4.30 | -1.5% |
| Real Madrid win | 51.0% | 52.2% | 1.95 | -0.6% |
| Over 2.5 | 54.5% | 68.9% | 1.42 | -22.6% |
| Under 2.5 | 45.5% | 31.1% | 2.90 | +31.9% |
=======
| AS Roma win | 25.9% | 25.0% | 4.20 | +8.8% |
| Draw | 22.7% | 23.5% | 4.30 | -2.5% |
| Real Madrid win | 51.4% | 51.5% | 1.95 | +0.2% |
| Over 2.5 | 59.5% | 68.7% | 1.42 | -15.5% |
| Under 2.5 | 40.5% | 31.3% | 2.91 | +17.8% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | d4ef112438afa4c2cdbbfc9376a009c9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:49:29Z |
| Market best draw last update utc | 2026-10-11T10:48:57Z |
| Market best away last update utc | 2026-10-11T10:48:57Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
<<<<<<< HEAD
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.41 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.42 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.17 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 27.3% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 49.7% |
| Raw p over 1 5 | 77.3% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Home probability edge | +1.1% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -14.4% |
| Under 2.5 probability edge | +14.4% |
| Raw edge prob home | 0.0230 |
| Raw ev home | 0.1463 |
| Raw edge prob draw | 0.0015 |
| Raw ev draw | -0.0123 |
| Raw edge prob away | -0.0244 |
| Raw ev away | -0.0301 |
=======
| P btts yes | 59.9% |
| P btts no | 40.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.01 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.26 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.67 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 5.01 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 51.3% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 62.6% |
| Raw p btts yes | 59.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.78 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.89 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +0.9% |
| Draw probability edge | -0.9% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -9.2% |
| Under 2.5 probability edge | +9.2% |
| Raw edge prob home | 0.0187 |
| Raw ev home | 0.1276 |
| Raw edge prob draw | -0.0173 |
| Raw ev draw | -0.0620 |
| Raw edge prob away | -0.0014 |
| Raw ev away | 0.0011 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Aston Villa win** at **67.0%**. Expected goals are 2.24 for Aston Villa and 0.61 for Fenerbahce (2.85 combined). The most likely exact score is 2-0 at 13.0%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.8%; Under 3.5 goals: 69.8%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 41.6%; BTTS No (at least one team does not score): 58.4%.
=======
The model's most likely 1X2 outcome is **Aston Villa win** at **66.3%**. Expected goals are 2.22 for Aston Villa and 0.60 for Fenerbahce (2.83 combined). The most likely exact score is 2-0 at 13.0%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 51.1%; Under 3.5 goals: 70.3%; Under 4.5 goals: 85.5%; BTTS Yes (both teams score): 41.5%; BTTS No (at least one team does not score): 58.5%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Aston Villa win | 67.0% | 1.49 |
| Draw | 19.4% | 5.16 |
| Fenerbahce win | 13.6% | 7.34 |
=======
| Aston Villa win | 66.3% | 1.51 |
| Draw | 20.0% | 5.00 |
| Fenerbahce win | 13.7% | 7.31 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
<<<<<<< HEAD
| Aston Villa expected goals | 2.24 |
| Fenerbahce expected goals | 0.61 |
| Expected total goals | 2.85 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 51.8% |
| Under 2.5 | 48.2% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |
=======
| Aston Villa expected goals | 2.22 |
| Fenerbahce expected goals | 0.60 |
| Expected total goals | 2.83 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 2-0 | 13.00% |
| 2 | 1-0 | 11.95% |
| 3 | 3-0 | 9.71% |
| 4 | 1-1 | 9.05% |
| 5 | 2-1 | 7.88% |
=======
| 1 | 2-0 | 12.97% |
| 2 | 1-0 | 12.02% |
| 3 | 3-0 | 9.61% |
| 4 | 1-1 | 9.33% |
| 5 | 2-1 | 7.82% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Aston Villa win | 67.0% | 58.9% | 1.74 | +16.6% |
| Draw | 19.4% | 22.7% | 4.35 | -15.8% |
| Fenerbahce win | 13.6% | 18.4% | 5.40 | -26.4% |
| Over 2.5 | 51.8% | 56.9% | 1.74 | -9.8% |
| Under 2.5 | 48.2% | 43.1% | 2.32 | +11.8% |
=======
| Aston Villa win | 66.3% | 57.8% | 1.74 | +15.4% |
| Draw | 20.0% | 23.8% | 4.35 | -13.1% |
| Fenerbahce win | 13.7% | 18.4% | 5.40 | -26.1% |
| Over 2.5 | 51.1% | 57.0% | 1.74 | -11.0% |
| Under 2.5 | 48.9% | 43.0% | 2.32 | +13.4% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 3f3cb74e560dfcc3e795b667ed9ebdef |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:41Z |
| Market best draw last update utc | 2026-10-11T10:48:42Z |
| Market best away last update utc | 2026-10-11T10:49:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
<<<<<<< HEAD
| P btts yes | 41.6% |
| P btts no | 58.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.29 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.71 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 75.1% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 8.9% |
| Raw p over 1 5 | 77.3% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 40.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.61 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +8.1% |
| Draw probability edge | -3.3% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | 0.1616 |
| Raw ev home | 0.3065 |
| Raw edge prob draw | -0.0669 |
| Raw ev draw | -0.3033 |
| Raw edge prob away | -0.0947 |
| Raw ev away | -0.5196 |
=======
| P btts yes | 41.5% |
| P btts no | 58.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.63 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.36 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.89 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.2% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 76.9% |
| Raw p under 3 5 | 68.6% |
| Raw p btts yes | 40.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.69 |
| Reference draw odds | 3.95 |
| Reference away odds | 5.05 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +8.5% |
| Draw probability edge | -3.8% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | 0.1708 |
| Raw ev home | 0.3028 |
| Raw edge prob draw | -0.0763 |
| Raw ev draw | -0.2967 |
| Raw edge prob away | -0.0945 |
| Raw ev away | -0.5162 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Borussia Dortmund win** at **45.5%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-2 at 8.6%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.0%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 70.2%; BTTS No (at least one team does not score): 29.8%.
=======
The model's most likely 1X2 outcome is **Borussia Dortmund win** at **46.9%**. Expected goals are 1.67 for Bodø/Glimt and 2.04 for Borussia Dortmund (3.70 combined). The most likely exact score is 1-1 at 8.6%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 71.1%; Under 3.5 goals: 49.3%; Under 4.5 goals: 68.9%; BTTS Yes (both teams score): 70.5%; BTTS No (at least one team does not score): 29.5%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Bodø/Glimt win | 32.7% | 3.06 |
| Draw | 21.9% | 4.57 |
| Borussia Dortmund win | 45.5% | 2.20 |
=======
| Bodø/Glimt win | 31.1% | 3.21 |
| Draw | 22.0% | 4.54 |
| Borussia Dortmund win | 46.9% | 2.13 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 1.73 |
| Borussia Dortmund expected goals | 1.94 |
| Expected total goals | 3.67 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
<<<<<<< HEAD
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 70.6% |
| Under 2.5 | 29.4% |
| Over 3.5 | 50.0% |
| Under 3.5 | 50.0% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |
=======
| Over 1.5 | 88.1% |
| Under 1.5 | 11.9% |
| Over 2.5 | 71.1% |
| Under 2.5 | 28.9% |
| Over 3.5 | 50.7% |
| Under 3.5 | 49.3% |
| Over 4.5 | 31.1% |
| Under 4.5 | 68.9% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-2 | 8.61% |
| 2 | 1-1 | 8.58% |
| 3 | 2-2 | 7.56% |
| 4 | 2-1 | 6.82% |
| 5 | 0-1 | 5.58% |
=======
| 1 | 1-1 | 8.56% |
| 2 | 1-2 | 8.47% |
| 3 | 2-2 | 7.65% |
| 4 | 2-1 | 6.69% |
| 5 | 1-3 | 5.75% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Bodø/Glimt win | 32.7% | 29.8% | 3.30 | +7.8% |
| Draw | 21.9% | 23.0% | 4.30 | -5.9% |
| Borussia Dortmund win | 45.5% | 47.1% | 2.14 | -2.7% |
| Over 2.5 | 70.6% | 69.0% | 1.40 | -1.1% |
| Under 2.5 | 29.4% | 31.0% | 3.03 | -11.0% |
=======
| Bodø/Glimt win | 31.1% | 29.8% | 3.30 | +2.7% |
| Draw | 22.0% | 23.6% | 4.30 | -5.4% |
| Borussia Dortmund win | 46.9% | 46.6% | 2.14 | +0.3% |
| Over 2.5 | 71.1% | 69.8% | 1.40 | -0.4% |
| Under 2.5 | 28.9% | 30.2% | 3.03 | -12.5% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | ca87a3874b0eae31b4173ae4a9324957 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:49:31Z |
| Market best draw last update utc | 2026-10-11T10:48:57Z |
| Market best away last update utc | 2026-10-11T10:48:41Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
<<<<<<< HEAD
| P btts yes | 70.2% |
| P btts no | 29.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.60 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.41 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.28 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 35.5% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 50.1% |
| Raw p btts yes | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.98 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +2.8% |
| Draw probability edge | -1.1% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | 0.0565 |
| Raw ev home | 0.1713 |
| Raw edge prob draw | -0.0226 |
| Raw ev draw | -0.1078 |
| Raw edge prob away | -0.0339 |
| Raw ev away | -0.0636 |
=======
| P btts yes | 70.5% |
| P btts no | 29.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.37 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.37 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.46 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.22 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 32.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 47.1% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 70.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.20 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.08 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +1.4% |
| Draw probability edge | -1.6% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | 0.0272 |
| Raw ev home | 0.0723 |
| Raw edge prob draw | -0.0317 |
| Raw ev draw | -0.1217 |
| Raw edge prob away | 0.0045 |
| Raw ev away | 0.0075 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-14 — Feyenoord vs Como

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Como win** at **62.9%**. Expected goals are 1.82 for Feyenoord and 3.82 for Como (5.63 combined). The most likely exact score is 2-2 at 6.1%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.9%; Under 3.5 goals: 19.7%; Under 4.5 goals: 35.7%; BTTS Yes (both teams score): 83.2%; BTTS No (at least one team does not score): 16.8%.
=======
The model's most likely 1X2 outcome is **Como win** at **63.3%**. Expected goals are 1.84 for Feyenoord and 3.93 for Como (5.77 combined). The most likely exact score is 2-2 at 6.0%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 91.6%; Under 3.5 goals: 18.3%; Under 4.5 goals: 33.9%; BTTS Yes (both teams score): 83.8%; BTTS No (at least one team does not score): 16.2%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Feyenoord win | 20.0% | 5.01 |
| Draw | 17.1% | 5.83 |
| Como win | 62.9% | 1.59 |
=======
| Feyenoord win | 19.6% | 5.09 |
| Draw | 17.1% | 5.86 |
| Como win | 63.3% | 1.58 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 1.82 |
| Como expected goals | 3.82 |
| Expected total goals | 5.63 |
| Over 0.5 | 99.7% |
| Under 0.5 | 0.3% |
| Over 1.5 | 97.3% |
| Under 1.5 | 2.7% |
| Over 2.5 | 90.9% |
| Under 2.5 | 9.1% |
| Over 3.5 | 80.3% |
| Under 3.5 | 19.7% |
| Over 4.5 | 64.3% |
| Under 4.5 | 35.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 2-2 | 6.08% |
| 2 | 1-3 | 5.15% |
| 3 | 1-4 | 4.91% |
| 4 | 3-3 | 4.68% |
| 5 | 2-3 | 4.68% |
=======
| 1 | 2-2 | 5.95% |
| 2 | 1-3 | 4.93% |
| 3 | 1-4 | 4.85% |
| 4 | 3-3 | 4.78% |
| 5 | 2-3 | 4.53% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Feyenoord win | 20.0% | 25.8% | 3.85 | -23.2% |
| Draw | 17.1% | 22.1% | 4.42 | -24.2% |
| Como win | 62.9% | 52.1% | 1.96 | +23.3% |
| Over 2.5 | 90.9% | 68.5% | 1.44 | +30.9% |
| Under 2.5 | 9.1% | 31.5% | 2.84 | -74.2% |
=======
| Feyenoord win | 19.6% | 25.7% | 3.85 | -24.4% |
| Draw | 17.1% | 22.4% | 4.42 | -24.5% |
| Como win | 63.3% | 51.8% | 1.95 | +23.4% |
| Over 2.5 | 91.6% | 67.7% | 1.44 | +31.9% |
| Under 2.5 | 8.4% | 32.3% | 2.84 | -76.2% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T16:45:00+00:00 |
| Fixture id | 5d6f9accd6f79ae4216dfd29ccc342b2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:42Z |
| Market best draw last update utc | 2026-10-11T10:49:13Z |
| Market best away last update utc | 2026-10-11T10:49:30Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 83.2% |
| P btts no | 16.8% |
| Fair Over 0.5 odds | 1.00 |
<<<<<<< HEAD
| Fair Under 0.5 odds | 303.17 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 37.09 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 11.01 |
| Fair Over 3.5 odds | 1.24 |
| Fair Under 3.5 odds | 5.09 |
| Fair Over 4.5 odds | 1.56 |
| Fair Under 4.5 odds | 2.80 |
| Unadjusted home-win probability | 14.2% |
| Unadjusted draw probability | 12.2% |
| Unadjusted away-win probability | 73.7% |
| Raw p over 1 5 | 97.5% |
| Raw p under 3 5 | 18.7% |
| Raw p btts yes | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.40 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -5.8% |
| Draw probability edge | -5.0% |
| Away probability edge | +10.8% |
| Over 2.5 probability edge | +22.4% |
| Under 2.5 probability edge | -22.4% |
| Raw edge prob home | -0.1160 |
| Raw ev home | -0.4551 |
| Raw edge prob draw | -0.0996 |
| Raw ev draw | -0.4627 |
| Raw edge prob away | 0.2156 |
| Raw ev away | 0.4443 |
=======
| Fair Under 0.5 odds | 343.25 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 41.17 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 11.94 |
| Fair Over 3.5 odds | 1.22 |
| Fair Under 3.5 odds | 5.46 |
| Fair Over 4.5 odds | 1.51 |
| Fair Under 4.5 odds | 2.95 |
| Unadjusted home-win probability | 13.5% |
| Unadjusted draw probability | 11.7% |
| Unadjusted away-win probability | 74.8% |
| Raw p over 1 5 | 97.8% |
| Raw p under 3 5 | 17.3% |
| Raw p btts yes | 82.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.68 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.88 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.82 |
| Home probability edge | -6.1% |
| Draw probability edge | -5.4% |
| Away probability edge | +11.5% |
| Over 2.5 probability edge | +23.9% |
| Under 2.5 probability edge | -23.9% |
| Raw edge prob home | -0.1223 |
| Raw ev home | -0.4795 |
| Raw edge prob draw | -0.1071 |
| Raw ev draw | -0.4818 |
| Raw edge prob away | 0.2294 |
| Raw ev away | 0.4578 |
| Market p over 1 5 | 89.2% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T10:48:57Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.35 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 54.6% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T10:49:37Z |
| Market reference under 3 5 odds | 1.81 |
| Market reference under 3 5 opposite odds | 2.17 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 66.0% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T10:49:29Z |
| Market reference btts yes odds | 1.49 |
| Market reference btts yes opposite odds | 2.82 |
| Market btts yes bookmakers | 4 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-14 — LASK vs Liverpool

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Liverpool win** at **74.4%**. Expected goals are 0.28 for LASK and 1.46 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 28.4%. Goal-market probabilities: at least one goal: 87.3%; Over 2.5 goals: 27.5%; Under 3.5 goals: 89.4%; Under 4.5 goals: 96.5%; BTTS Yes (both teams score): 17.5%; BTTS No (at least one team does not score): 82.5%.
=======
The model's most likely 1X2 outcome is **Liverpool win** at **72.6%**. Expected goals are 0.33 for LASK and 1.48 for Liverpool (1.80 combined). The most likely exact score is 0-1 at 26.8%. Goal-market probabilities: at least one goal: 87.5%; Over 2.5 goals: 28.8%; Under 3.5 goals: 88.5%; Under 4.5 goals: 96.1%; BTTS Yes (both teams score): 20.1%; BTTS No (at least one team does not score): 79.9%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| LASK win | 7.3% | 13.77 |
| Draw | 18.3% | 5.45 |
| Liverpool win | 74.4% | 1.34 |
=======
| LASK win | 8.3% | 12.11 |
| Draw | 19.1% | 5.23 |
| Liverpool win | 72.6% | 1.38 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
<<<<<<< HEAD
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.46 |
| Expected total goals | 1.74 |
| Over 0.5 | 87.3% |
| Under 0.5 | 12.7% |
| Over 1.5 | 53.7% |
| Under 1.5 | 46.3% |
| Over 2.5 | 27.5% |
| Under 2.5 | 72.5% |
| Over 3.5 | 10.6% |
| Under 3.5 | 89.4% |
| Over 4.5 | 3.5% |
| Under 4.5 | 96.5% |
=======
| LASK expected goals | 0.33 |
| Liverpool expected goals | 1.48 |
| Expected total goals | 1.80 |
| Over 0.5 | 87.5% |
| Under 0.5 | 12.5% |
| Over 1.5 | 55.0% |
| Under 1.5 | 45.0% |
| Over 2.5 | 28.8% |
| Under 2.5 | 71.2% |
| Over 3.5 | 11.5% |
| Under 3.5 | 88.5% |
| Over 4.5 | 3.9% |
| Under 4.5 | 96.1% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 0-1 | 28.36% |
| 2 | 0-2 | 20.43% |
| 3 | 0-0 | 12.68% |
| 4 | 0-3 | 9.95% |
| 5 | 1-2 | 5.78% |
=======
| 1 | 0-1 | 26.78% |
| 2 | 0-2 | 19.46% |
| 3 | 0-0 | 12.48% |
| 4 | 0-3 | 9.58% |
| 5 | 1-2 | 6.36% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| LASK win | 7.3% | 7.2% | 12.00 | -12.8% |
| Draw | 18.3% | 11.9% | 7.11 | +30.4% |
| Liverpool win | 74.4% | 80.8% | 1.29 | -4.0% |
| Over 2.5 | 27.5% | 71.6% | 1.37 | -62.4% |
| Under 2.5 | 72.5% | 28.4% | 3.13 | +127.1% |
=======
| LASK win | 8.3% | 8.2% | 12.00 | -0.9% |
| Draw | 19.1% | 13.6% | 7.11 | +36.0% |
| Liverpool win | 72.6% | 78.2% | 1.29 | -6.3% |
| Over 2.5 | 28.8% | 70.9% | 1.37 | -60.5% |
| Under 2.5 | 71.2% | 29.1% | 3.13 | +122.8% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T16:45:00+00:00 |
| Fixture id | 2903ee092f7e08c549b130a3d394ac3c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:49:29Z |
| Market best draw last update utc | 2026-10-11T10:49:14Z |
| Market best away last update utc | 2026-10-11T10:48:41Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
<<<<<<< HEAD
| P btts yes | 17.5% |
| P btts no | 82.5% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.89 |
| Fair Over 1.5 odds | 1.86 |
| Fair Under 1.5 odds | 2.16 |
| Fair Over 2.5 odds | 3.64 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.40 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 28.27 |
=======
| P btts yes | 20.1% |
| P btts no | 79.9% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.01 |
| Fair Over 1.5 odds | 1.82 |
| Fair Under 1.5 odds | 2.22 |
| Fair Over 2.5 odds | 3.47 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.69 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 25.35 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 67.9% |
| Raw p over 1 5 | 51.7% |
| Raw p under 3 5 | 90.0% |
| Raw p btts yes | 18.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 10.50 |
| Reference draw odds | 6.50 |
| Reference away odds | 1.26 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.10 |
<<<<<<< HEAD
| Home probability edge | +0.0% |
| Draw probability edge | +6.4% |
| Away probability edge | -6.5% |
| Over 2.5 probability edge | -44.2% |
| Under 2.5 probability edge | +44.2% |
| Raw edge prob home | 0.0004 |
| Raw ev home | -0.1257 |
| Raw edge prob draw | 0.1286 |
| Raw ev draw | 0.7612 |
| Raw edge prob away | -0.1290 |
| Raw ev away | -0.1235 |
=======
| Home probability edge | +0.1% |
| Draw probability edge | +5.5% |
| Away probability edge | -5.6% |
| Over 2.5 probability edge | -42.1% |
| Under 2.5 probability edge | +42.1% |
| Raw edge prob home | 0.0015 |
| Raw ev home | -0.0006 |
| Raw edge prob draw | 0.1100 |
| Raw ev draw | 0.7512 |
| Raw edge prob away | -0.1115 |
| Raw ev away | -0.1352 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Paris Saint Germain win** at **45.5%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.5%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 69.3%; Under 3.5 goals: 51.8%; Under 4.5 goals: 70.9%; BTTS Yes (both teams score): 67.7%; BTTS No (at least one team does not score): 32.3%.
=======
The model's most likely 1X2 outcome is **Paris Saint Germain win** at **46.3%**. Expected goals are 1.53 for Manchester City and 2.51 for Paris Saint Germain (4.04 combined). The most likely exact score is 2-2 at 7.6%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 75.5%; Under 3.5 goals: 43.7%; Under 4.5 goals: 63.5%; BTTS Yes (both teams score): 72.9%; BTTS No (at least one team does not score): 27.1%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Manchester City win | 33.6% | 2.98 |
| Draw | 20.9% | 4.79 |
| Paris Saint Germain win | 45.5% | 2.20 |
=======
| Manchester City win | 32.8% | 3.04 |
| Draw | 20.8% | 4.80 |
| Paris Saint Germain win | 46.3% | 2.16 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
<<<<<<< HEAD
| Manchester City expected goals | 1.40 |
| Paris Saint Germain expected goals | 2.23 |
| Expected total goals | 3.63 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 86.8% |
| Under 1.5 | 13.2% |
| Over 2.5 | 69.3% |
| Under 2.5 | 30.7% |
| Over 3.5 | 48.2% |
| Under 3.5 | 51.8% |
| Over 4.5 | 29.1% |
| Under 4.5 | 70.9% |
=======
| Manchester City expected goals | 1.53 |
| Paris Saint Germain expected goals | 2.51 |
| Expected total goals | 4.04 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 90.3% |
| Under 1.5 | 9.7% |
| Over 2.5 | 75.5% |
| Under 2.5 | 24.5% |
| Over 3.5 | 56.3% |
| Under 3.5 | 43.7% |
| Over 4.5 | 36.5% |
| Under 4.5 | 63.5% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-1 | 8.50% |
| 2 | 2-1 | 8.11% |
| 3 | 1-2 | 7.41% |
| 4 | 2-2 | 7.00% |
| 5 | 1-0 | 5.76% |
=======
| 1 | 2-2 | 7.56% |
| 2 | 1-1 | 7.48% |
| 3 | 2-1 | 7.44% |
| 4 | 1-2 | 6.64% |
| 5 | 1-3 | 5.55% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Manchester City win | 33.6% | 43.2% | 2.35 | -21.0% |
| Draw | 20.9% | 22.5% | 4.30 | -10.2% |
| Paris Saint Germain win | 45.5% | 34.3% | 2.94 | +33.8% |
| Over 2.5 | 69.3% | 67.0% | 1.44 | -0.2% |
| Under 2.5 | 30.7% | 33.0% | 2.87 | -12.0% |
=======
| Manchester City win | 32.8% | 42.8% | 2.35 | -22.8% |
| Draw | 20.8% | 23.7% | 4.30 | -10.5% |
| Paris Saint Germain win | 46.3% | 33.5% | 2.94 | +36.2% |
| Over 2.5 | 75.5% | 67.9% | 1.44 | +8.7% |
| Under 2.5 | 24.5% | 32.1% | 2.87 | -29.6% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 5a1a6a04c5561897741105e30d5d7ec4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:57Z |
| Market best draw last update utc | 2026-10-11T10:49:31Z |
| Market best away last update utc | 2026-10-11T10:48:41Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
<<<<<<< HEAD
| P btts yes | 67.7% |
| P btts no | 32.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.41 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.55 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.26 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.44 |
| Fair Under 4.5 odds | 1.41 |
| Unadjusted home-win probability | 24.0% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 56.7% |
| Raw p over 1 5 | 87.3% |
| Raw p under 3 5 | 50.8% |
| Raw p btts yes | 66.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -9.6% |
| Draw probability edge | -1.6% |
| Away probability edge | +11.2% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | -0.1916 |
| Raw ev home | -0.4354 |
| Raw edge prob draw | -0.0317 |
| Raw ev draw | -0.1701 |
| Raw edge prob away | 0.2234 |
| Raw ev away | 0.6662 |
=======
| P btts yes | 72.9% |
| P btts no | 27.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 60.39 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.27 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.08 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.29 |
| Fair Over 4.5 odds | 2.74 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.6% |
| Raw p btts yes | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.26 |
| Reference draw odds | 3.98 |
| Reference away odds | 2.86 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.85 |
| Home probability edge | -9.9% |
| Draw probability edge | -2.9% |
| Away probability edge | +12.9% |
| Over 2.5 probability edge | +7.6% |
| Under 2.5 probability edge | -7.6% |
| Raw edge prob home | -0.1988 |
| Raw ev home | -0.4618 |
| Raw edge prob draw | -0.0583 |
| Raw ev draw | -0.2301 |
| Raw edge prob away | 0.2571 |
| Raw ev away | 0.7402 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-14 — Real Betis vs Porto

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Real Betis win** at **60.3%**. Expected goals are 3.29 for Real Betis and 1.29 for Porto (4.58 combined). The most likely exact score is 2-2 at 7.0%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 80.9%; Under 3.5 goals: 35.4%; Under 4.5 goals: 55.0%; BTTS Yes (both teams score): 72.3%; BTTS No (at least one team does not score): 27.7%.
=======
The model's most likely 1X2 outcome is **Real Betis win** at **64.7%**. Expected goals are 4.51 for Real Betis and 1.48 for Porto (5.98 combined). The most likely exact score is 2-2 at 6.1%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 91.2%; Under 3.5 goals: 18.4%; Under 4.5 goals: 33.9%; BTTS Yes (both teams score): 79.9%; BTTS No (at least one team does not score): 20.1%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Real Betis win | 60.3% | 1.66 |
| Draw | 18.9% | 5.28 |
| Porto win | 20.8% | 4.81 |
=======
| Real Betis win | 64.7% | 1.55 |
| Draw | 17.0% | 5.88 |
| Porto win | 18.3% | 5.45 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
<<<<<<< HEAD
| Real Betis expected goals | 3.29 |
| Porto expected goals | 1.29 |
| Expected total goals | 4.58 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 93.1% |
| Under 1.5 | 6.9% |
| Over 2.5 | 80.9% |
| Under 2.5 | 19.1% |
| Over 3.5 | 64.6% |
| Under 3.5 | 35.4% |
| Over 4.5 | 45.0% |
| Under 4.5 | 55.0% |
=======
| Real Betis expected goals | 4.51 |
| Porto expected goals | 1.48 |
| Expected total goals | 5.98 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.4% |
| Under 1.5 | 2.6% |
| Over 2.5 | 91.2% |
| Under 2.5 | 8.8% |
| Over 3.5 | 81.6% |
| Under 3.5 | 18.4% |
| Over 4.5 | 66.1% |
| Under 4.5 | 33.9% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 2-2 | 7.04% |
| 2 | 1-1 | 6.30% |
| 3 | 3-1 | 6.22% |
| 4 | 2-1 | 5.67% |
| 5 | 4-1 | 5.12% |
=======
| 1 | 2-2 | 6.12% |
| 2 | 4-1 | 4.87% |
| 3 | 3-3 | 4.52% |
| 4 | 5-1 | 4.39% |
| 5 | 3-1 | 4.32% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Real Betis win | 60.3% | 44.5% | 2.27 | +36.9% |
| Draw | 18.9% | 25.4% | 3.75 | -29.0% |
| Porto win | 20.8% | 30.1% | 3.30 | -31.5% |
| Over 2.5 | 80.9% | 56.3% | 1.78 | +44.0% |
| Under 2.5 | 19.1% | 43.7% | 2.21 | -57.8% |
=======
| Real Betis win | 64.7% | 43.8% | 2.27 | +46.8% |
| Draw | 17.0% | 26.2% | 3.75 | -36.2% |
| Porto win | 18.3% | 30.0% | 3.35 | -38.6% |
| Over 2.5 | 91.2% | 55.7% | 1.78 | +62.4% |
| Under 2.5 | 8.8% | 44.3% | 2.21 | -80.6% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 4c7f87780ae5ab8bec9e83d6d6ec9909 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:41Z |
| Market best draw last update utc | 2026-10-11T10:49:30Z |
| Market best away last update utc | 2026-10-11T10:49:29Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
<<<<<<< HEAD
| P btts yes | 72.3% |
| P btts no | 27.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 81.32 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.55 |
| Fair Over 2.5 odds | 1.24 |
| Fair Under 2.5 odds | 5.23 |
| Fair Over 3.5 odds | 1.55 |
| Fair Under 3.5 odds | 2.83 |
| Fair Over 4.5 odds | 2.22 |
| Fair Under 4.5 odds | 1.82 |
| Unadjusted home-win probability | 76.1% |
| Unadjusted draw probability | 12.4% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 94.1% |
| Raw p under 3 5 | 32.9% |
| Raw p btts yes | 69.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +15.8% |
| Draw probability edge | -6.5% |
| Away probability edge | -9.3% |
| Over 2.5 probability edge | +24.6% |
| Under 2.5 probability edge | -24.6% |
| Raw edge prob home | 0.3168 |
| Raw ev home | 0.7283 |
| Raw edge prob draw | -0.1301 |
| Raw ev draw | -0.5339 |
| Raw edge prob away | -0.1867 |
| Raw ev away | -0.6227 |
=======
| P btts yes | 79.9% |
| P btts no | 20.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 270.23 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 39.04 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 11.40 |
| Fair Over 3.5 odds | 1.23 |
| Fair Under 3.5 odds | 5.44 |
| Fair Over 4.5 odds | 1.51 |
| Fair Under 4.5 odds | 2.95 |
| Unadjusted home-win probability | 85.5% |
| Unadjusted draw probability | 7.8% |
| Unadjusted away-win probability | 6.7% |
| Raw p over 1 5 | 98.1% |
| Raw p under 3 5 | 15.4% |
| Raw p btts yes | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.21 |
| Reference draw odds | 3.62 |
| Reference away odds | 3.18 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | +20.9% |
| Draw probability edge | -9.2% |
| Away probability edge | -11.7% |
| Over 2.5 probability edge | +35.6% |
| Under 2.5 probability edge | -35.6% |
| Raw edge prob home | 0.4173 |
| Raw ev home | 0.9415 |
| Raw edge prob draw | -0.1841 |
| Raw ev draw | -0.7076 |
| Raw edge prob away | -0.2332 |
| Raw ev away | -0.7764 |
| Market p over 1 5 | 81.2% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T10:48:57Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 66.7% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T10:49:13Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.79 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 59.6% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-11T10:49:30Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.35 |
| Market btts yes bookmakers | 4 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.5%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 51.1%; Under 3.5 goals: 70.6%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.
=======
The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **38.7%**. Expected goals are 1.45 for Shakhtar Donetsk and 1.25 for AEK Athens (2.71 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 50.3%; Under 3.5 goals: 71.3%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 54.6%; BTTS No (at least one team does not score): 45.4%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| Shakhtar Donetsk win | 39.5% | 2.53 |
| Draw | 25.6% | 3.91 |
| AEK Athens win | 34.9% | 2.86 |
=======
| Shakhtar Donetsk win | 38.7% | 2.58 |
| Draw | 25.9% | 3.87 |
| AEK Athens win | 35.4% | 2.82 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.49 |
| AEK Athens expected goals | 1.25 |
<<<<<<< HEAD
| Expected total goals | 2.74 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |
=======
| Expected total goals | 2.71 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 50.3% |
| Under 2.5 | 49.7% |
| Over 3.5 | 28.7% |
| Under 3.5 | 71.3% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-1 | 12.07% |
| 2 | 0-1 | 9.33% |
| 3 | 1-0 | 9.32% |
| 4 | 2-1 | 8.17% |
| 5 | 1-2 | 8.09% |
=======
| 1 | 1-1 | 12.24% |
| 2 | 0-1 | 9.57% |
| 3 | 1-0 | 9.41% |
| 4 | 1-2 | 8.13% |
| 5 | 2-1 | 8.07% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Shakhtar Donetsk win | 39.5% | 35.7% | 2.81 | +11.0% |
| Draw | 25.6% | 26.9% | 3.65 | -6.7% |
| AEK Athens win | 34.9% | 37.3% | 2.70 | -5.6% |
| Over 2.5 | 51.1% | 52.2% | 1.92 | -1.8% |
| Under 2.5 | 48.9% | 47.8% | 2.03 | -0.8% |
=======
| Shakhtar Donetsk win | 38.7% | 35.0% | 2.81 | +8.8% |
| Draw | 25.9% | 27.3% | 3.65 | -5.6% |
| AEK Athens win | 35.4% | 37.6% | 2.69 | -4.7% |
| Over 2.5 | 50.3% | 51.7% | 1.92 | -3.4% |
| Under 2.5 | 49.7% | 48.3% | 2.03 | +0.8% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 0f961390e790ad2c80ecb3f302cad4a6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:41Z |
| Market best draw last update utc | 2026-10-11T10:48:42Z |
| Market best away last update utc | 2026-10-11T10:49:13Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 67/100 |
<<<<<<< HEAD
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.16 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.41 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.09 |
=======
| P btts yes | 54.6% |
| P btts no | 45.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.57 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.34 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 54.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
<<<<<<< HEAD
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.55 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.45 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | +3.8% |
| Draw probability edge | -1.4% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | 0.0751 |
| Raw ev home | 0.2153 |
| Raw edge prob draw | -0.0272 |
| Raw ev draw | -0.1168 |
| Raw edge prob away | -0.0479 |
| Raw ev away | -0.1210 |
=======
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.74 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.56 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +3.7% |
| Draw probability edge | -1.5% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -1.4% |
| Under 2.5 probability edge | +1.4% |
| Raw edge prob home | 0.0731 |
| Raw ev home | 0.1903 |
| Raw edge prob draw | -0.0292 |
| Raw ev draw | -0.1089 |
| Raw edge prob away | -0.0439 |
| Raw ev away | -0.1062 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

<<<<<<< HEAD
The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.0%**. Expected goals are 1.45 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 72.6%; Under 3.5 goals: 48.5%; Under 4.5 goals: 67.7%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.
=======
The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.2%**. Expected goals are 1.40 for ŠK Slovan Bratislava and 2.20 for VfB Stuttgart (3.60 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 70.8%; Under 3.5 goals: 50.8%; Under 4.5 goals: 69.8%; BTTS Yes (both teams score): 65.5%; BTTS No (at least one team does not score): 34.5%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
<<<<<<< HEAD
| ŠK Slovan Bratislava win | 17.2% | 5.80 |
| Draw | 16.7% | 5.97 |
| VfB Stuttgart win | 66.0% | 1.51 |
=======
| ŠK Slovan Bratislava win | 16.8% | 5.96 |
| Draw | 17.0% | 5.88 |
| VfB Stuttgart win | 66.2% | 1.51 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.45 |
| VfB Stuttgart expected goals | 2.25 |
| Expected total goals | 3.71 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 72.6% |
| Under 2.5 | 27.4% |
| Over 3.5 | 51.5% |
| Under 3.5 | 48.5% |
| Over 4.5 | 32.3% |
| Under 4.5 | 67.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-2 | 10.69% |
| 2 | 1-3 | 8.02% |
| 3 | 0-2 | 7.35% |
| 4 | 0-1 | 7.01% |
| 5 | 1-1 | 6.65% |
=======
| 1 | 1-2 | 10.94% |
| 2 | 1-3 | 8.01% |
| 3 | 0-2 | 7.83% |
| 4 | 0-1 | 7.62% |
| 5 | 1-1 | 6.98% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| ŠK Slovan Bratislava win | 17.2% | 9.7% | 10.00 | +72.4% |
| Draw | 16.7% | 14.2% | 6.48 | +8.5% |
| VfB Stuttgart win | 66.0% | 76.1% | 1.35 | -10.9% |
| Over 2.5 | 72.6% | 70.8% | 1.37 | -0.5% |
| Under 2.5 | 27.4% | 29.2% | 3.13 | -14.3% |
=======
| ŠK Slovan Bratislava win | 16.8% | 9.1% | 10.00 | +67.6% |
| Draw | 17.0% | 14.5% | 6.48 | +10.2% |
| VfB Stuttgart win | 66.2% | 76.4% | 1.35 | -10.6% |
| Over 2.5 | 70.8% | 70.9% | 1.37 | -3.0% |
| Under 2.5 | 29.2% | 29.1% | 3.13 | -8.5% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | d7576351b8cb2396e32cc3de0446f3de |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:41Z |
| Market best draw last update utc | 2026-10-11T10:48:41Z |
| Market best away last update utc | 2026-10-11T10:49:14Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.2% |
| P btts no | 32.8% |
| Fair Over 0.5 odds | 1.02 |
<<<<<<< HEAD
| Fair Under 0.5 odds | 55.89 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.65 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.65 |
| Fair Over 3.5 odds | 1.94 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.09 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 24.8% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 56.0% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 68.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 7.70 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.27 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +7.5% |
| Draw probability edge | +2.5% |
| Away probability edge | -10.1% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | 0.1510 |
| Raw ev home | 1.4784 |
| Raw edge prob draw | 0.0502 |
| Raw ev draw | 0.2474 |
| Raw edge prob away | -0.2012 |
| Raw ev away | -0.2445 |
=======
| Fair Under 0.5 odds | 49.37 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.95 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.42 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.97 |
| Fair Over 4.5 odds | 3.31 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 56.1% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 51.6% |
| Raw p btts yes | 66.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 9.60 |
| Reference draw odds | 6.20 |
| Reference away odds | 1.29 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | +7.6% |
| Draw probability edge | +2.5% |
| Away probability edge | -10.1% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.1528 |
| Raw ev home | 1.4402 |
| Raw edge prob draw | 0.0500 |
| Raw ev draw | 0.2637 |
| Raw edge prob away | -0.2028 |
| Raw ev away | -0.2427 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---
