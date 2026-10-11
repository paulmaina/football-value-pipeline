# Serie A — football model report

Fixtures in this report: **17**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,190 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 879.078 |
| Base scoring parameter | 0.134 |
| Home-advantage parameter | 0.091 |
| Dixon-Coles low-score adjustment | 0.005 |
| Xi per day | 0.0029 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 17.00 |
| Additional event odds calls used before this league | 12.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-11 — Cagliari vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **57.6%**. Expected goals are 0.80 for Cagliari and 1.48 for Juventus (2.28 combined). The most likely exact score is 0-1 at 16.4%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 40.4%; Under 3.5 goals: 80.0%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 42.1%; BTTS No (at least one team does not score): 57.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 17.1% | 5.86 |
| Draw | 25.4% | 3.94 |
| Juventus win | 57.6% | 1.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 0.80 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.4% |
| Under 2.5 | 59.6% |
| Over 3.5 | 20.0% |
| Under 3.5 | 80.0% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.38% |
| 2 | 0-2 | 12.10% |
| 3 | 1-1 | 11.62% |
| 4 | 0-0 | 9.83% |
| 5 | 1-2 | 9.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 17.1% | 13.9% | 7.60 | +29.6% |
| Draw | 25.4% | 24.5% | 4.30 | +9.2% |
| Juventus win | 57.6% | 61.6% | 1.61 | -7.3% |
| Over 2.5 | 40.4% | 47.2% | 2.07 | -16.4% |
| Under 2.5 | 59.6% | 52.8% | 1.94 | +15.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T18:45:00+00:00 |
| Fixture id | 407f7d03157d1dfad384876e6a6bc910 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:56:10Z |
| Market best away last update utc | 2026-10-11T08:56:56Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Cagliari |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.1% |
| P btts no | 57.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.18 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.00 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.01 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 53.6% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.3% |
| Raw p btts yes | 42.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 6.75 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.84 |
| Home probability edge | +3.1% |
| Draw probability edge | +0.9% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
| Raw edge prob home | 0.0626 |
| Raw ev home | 0.5338 |
| Raw edge prob draw | 0.0172 |
| Raw ev draw | 0.1287 |
| Raw edge prob away | -0.0798 |
| Raw ev away | -0.1375 |

</details>


---

## 2026-10-11 — Como vs AS Roma

The model's most likely 1X2 outcome is **Como win** at **37.0%**. Expected goals are 1.17 for Como and 1.30 for AS Roma (2.47 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 44.9%; Under 3.5 goals: 76.4%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 37.0% | 2.70 |
| Draw | 27.1% | 3.69 |
| AS Roma win | 35.9% | 2.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 1.17 |
| AS Roma expected goals | 1.30 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 70.6% |
| Under 1.5 | 29.4% |
| Over 2.5 | 44.9% |
| Under 2.5 | 55.1% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.84% |
| 2 | 1-0 | 11.00% |
| 3 | 0-1 | 10.02% |
| 4 | 0-0 | 8.39% |
| 5 | 2-1 | 8.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 37.0% | 40.5% | 2.46 | -8.9% |
| Draw | 27.1% | 27.2% | 3.66 | -0.9% |
| AS Roma win | 35.9% | 32.3% | 3.10 | +11.3% |
| Over 2.5 | 44.9% | 59.5% | 1.66 | -25.5% |
| Under 2.5 | 55.1% | 40.5% | 2.42 | +33.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T10:30:00+00:00 |
| Fixture id | 2547c0dbddd26d23fa532228e36348cb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:55Z |
| Market best draw last update utc | 2026-10-11T08:56:56Z |
| Market best away last update utc | 2026-10-11T08:56:39Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Matchbook |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.2% |
| P btts no | 49.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.91 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.40 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.23 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.53 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 27.0% |
| Unadjusted away-win probability | 39.5% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.3% |
| Raw p btts yes | 50.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.41 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.00 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | -3.5% |
| Draw probability edge | -0.1% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -14.7% |
| Under 2.5 probability edge | +14.7% |
| Raw edge prob home | -0.0693 |
| Raw ev home | -0.1746 |
| Raw edge prob draw | -0.0022 |
| Raw ev draw | -0.0129 |
| Raw edge prob away | 0.0715 |
| Raw ev away | 0.2238 |

</details>


---

## 2026-10-11 — Lazio vs Monza

The model's most likely 1X2 outcome is **Lazio win** at **61.0%**. Expected goals are 2.01 for Lazio and 0.87 for Monza (2.88 combined). The most likely exact score is 2-0 at 10.8%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 54.0%; Under 3.5 goals: 67.9%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 61.0% | 1.64 |
| Draw | 22.5% | 4.44 |
| Monza win | 16.5% | 6.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 2.01 |
| Monza expected goals | 0.87 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 54.0% |
| Under 2.5 | 46.0% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.83% |
| 2 | 1-0 | 10.81% |
| 3 | 1-1 | 10.70% |
| 4 | 2-1 | 9.37% |
| 5 | 3-0 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 61.0% | 57.8% | 1.78 | +8.5% |
| Draw | 22.5% | 24.5% | 4.02 | -9.5% |
| Monza win | 16.5% | 17.6% | 5.37 | -11.4% |
| Over 2.5 | 54.0% | 52.3% | 1.86 | +0.4% |
| Under 2.5 | 46.0% | 47.7% | 2.16 | -0.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | c0f72699f32ec193b64fd54092fe268d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:56Z |
| Market best draw last update utc | 2026-10-11T08:56:27Z |
| Market best away last update utc | 2026-10-11T08:56:58Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | GTbets |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Lazio |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.34 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.23 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 64.1% |
| Unadjusted draw probability | 20.5% |
| Unadjusted away-win probability | 15.4% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 67.5% |
| Raw p btts yes | 50.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.70 |
| Reference draw odds | 3.90 |
| Reference away odds | 5.37 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 2.03 |
| Home probability edge | +3.2% |
| Draw probability edge | -2.0% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +1.7% |
| Under 2.5 probability edge | -1.7% |
| Raw edge prob home | 0.0630 |
| Raw ev home | 0.1415 |
| Raw edge prob draw | -0.0403 |
| Raw ev draw | -0.1756 |
| Raw edge prob away | -0.0227 |
| Raw ev away | -0.1749 |

</details>


---

## 2026-10-11 — Lecce vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **49.1%**. Expected goals are 0.78 for Lecce and 1.33 for Bologna (2.11 combined). The most likely exact score is 0-1 at 16.0%. Goal-market probabilities: at least one goal: 87.9%; Over 2.5 goals: 35.3%; Under 3.5 goals: 83.7%; Under 4.5 goals: 93.7%; BTTS Yes (both teams score): 39.9%; BTTS No (at least one team does not score): 60.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 22.4% | 4.46 |
| Draw | 28.5% | 3.51 |
| Bologna win | 49.1% | 2.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.78 |
| Bologna expected goals | 1.33 |
| Expected total goals | 2.11 |
| Over 0.5 | 87.9% |
| Under 0.5 | 12.1% |
| Over 1.5 | 62.2% |
| Under 1.5 | 37.8% |
| Over 2.5 | 35.3% |
| Under 2.5 | 64.7% |
| Over 3.5 | 16.3% |
| Under 3.5 | 83.7% |
| Over 4.5 | 6.3% |
| Under 4.5 | 93.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.95% |
| 2 | 1-1 | 12.63% |
| 3 | 0-0 | 12.14% |
| 4 | 0-2 | 10.57% |
| 5 | 1-0 | 9.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 22.4% | 22.8% | 4.35 | -2.6% |
| Draw | 28.5% | 28.8% | 3.40 | -3.1% |
| Bologna win | 49.1% | 48.4% | 2.10 | +3.1% |
| Over 2.5 | 35.3% | 42.6% | 2.26 | -20.3% |
| Under 2.5 | 64.7% | 57.4% | 1.79 | +15.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | 946716d7e5e52822f08be8cb95193d9d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:24Z |
| Market best draw last update utc | 2026-10-11T08:56:24Z |
| Market best away last update utc | 2026-10-11T08:56:39Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Lecce |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 39.9% |
| P btts no | 60.1% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.23 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.65 |
| Fair Over 2.5 odds | 2.84 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.12 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.85 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 22.0% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 62.3% |
| Raw p under 3 5 | 83.6% |
| Raw p btts yes | 39.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 4.20 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.02 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.26 |
| Reference Under 2.5 odds | 1.70 |
| Home probability edge | -0.4% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.0077 |
| Raw ev home | -0.0425 |
| Raw edge prob draw | -0.0056 |
| Raw ev draw | -0.0409 |
| Raw edge prob away | 0.0133 |
| Raw ev away | 0.0454 |
| Market p over 1 5 | 69.1% |
| Market over 1 5 odds | 1.42 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:56:58Z |
| Market reference over 1 5 odds | 1.42 |
| Market reference over 1 5 opposite odds | 3.05 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 78.3% |
| Market under 3 5 odds | 1.26 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T08:56:58Z |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 4.25 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 49.0% |
| Market btts yes odds | 1.97 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-11T08:57:03Z |
| Market reference btts yes odds | 1.97 |
| Market reference btts yes opposite odds | 1.90 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Sassuolo vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **51.3%**. Expected goals are 1.13 for Sassuolo and 1.68 for AC Milan (2.81 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 53.2%; Under 3.5 goals: 68.8%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 23.9% | 4.18 |
| Draw | 24.8% | 4.03 |
| AC Milan win | 51.3% | 1.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.13 |
| AC Milan expected goals | 1.68 |
| Expected total goals | 2.81 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 53.2% |
| Under 2.5 | 46.8% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.73% |
| 2 | 0-1 | 10.34% |
| 3 | 1-2 | 9.78% |
| 4 | 0-2 | 8.66% |
| 5 | 1-0 | 6.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 23.9% | 22.2% | 4.50 | +7.6% |
| Draw | 24.8% | 25.6% | 3.90 | -3.3% |
| AC Milan win | 51.3% | 52.2% | 1.91 | -2.1% |
| Over 2.5 | 53.2% | 56.1% | 1.81 | -3.7% |
| Under 2.5 | 46.8% | 43.9% | 2.25 | +5.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T16:00:00+00:00 |
| Fixture id | 1cf64166dda1e0da8b325161deb39662 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:56:56Z |
| Market best away last update utc | 2026-10-11T08:56:56Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | BetAnything |
| Matched home-team name | Sassuolo |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.30 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.37 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.50 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 25.6% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 50.4% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 68.9% |
| Raw p btts yes | 55.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 4.30 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.88 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +1.7% |
| Draw probability edge | -0.8% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -2.9% |
| Under 2.5 probability edge | +2.9% |
| Raw edge prob home | 0.0337 |
| Raw ev home | 0.1522 |
| Raw edge prob draw | -0.0159 |
| Raw ev draw | -0.0637 |
| Raw edge prob away | -0.0178 |
| Raw ev away | -0.0376 |

</details>


---

## 2026-10-12 — Atalanta BC vs Venezia

The model's most likely 1X2 outcome is **Atalanta BC win** at **68.7%**. Expected goals are 2.35 for Atalanta BC and 0.66 for Venezia (3.02 combined). The most likely exact score is 2-0 at 12.4%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 56.0%; Under 3.5 goals: 65.7%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 45.1%; BTTS No (at least one team does not score): 54.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 68.7% | 1.46 |
| Draw | 19.3% | 5.17 |
| Venezia win | 11.9% | 8.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.35 |
| Venezia expected goals | 0.66 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 79.0% |
| Under 1.5 | 21.0% |
| Over 2.5 | 56.0% |
| Under 2.5 | 44.0% |
| Over 3.5 | 34.3% |
| Under 3.5 | 65.7% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.40% |
| 2 | 1-0 | 10.57% |
| 3 | 3-0 | 9.74% |
| 4 | 1-1 | 9.18% |
| 5 | 2-1 | 8.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 68.7% | 62.1% | 1.63 | +12.0% |
| Draw | 19.3% | 22.7% | 4.40 | -14.9% |
| Venezia win | 11.9% | 15.2% | 6.20 | -26.0% |
| Over 2.5 | 56.0% | 62.2% | 1.55 | -13.2% |
| Under 2.5 | 44.0% | 37.8% | 2.48 | +9.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-12T16:30:00+00:00 |
| Fixture id | 0f2e7ff90b994f31d5cd48a9680943e1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:56Z |
| Market best draw last update utc | 2026-10-11T08:56:24Z |
| Market best away last update utc | 2026-10-11T08:56:39Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Atalanta |
| Matched away-team name | Venezia |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.1% |
| P btts no | 54.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.99 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.77 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.65 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 75.3% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 8.7% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 64.4% |
| Raw p btts yes | 43.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.57 |
| Reference draw odds | 4.07 |
| Reference away odds | 5.95 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | +6.6% |
| Draw probability edge | -3.4% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | 0.1324 |
| Raw ev home | 0.2280 |
| Raw edge prob draw | -0.0673 |
| Raw ev draw | -0.2971 |
| Raw edge prob away | -0.0652 |
| Raw ev away | -0.4615 |

</details>


---

## 2026-10-12 — Torino vs Udinese

The model's most likely 1X2 outcome is **Torino win** at **38.6%**. Expected goals are 1.29 for Torino and 1.35 for Udinese (2.64 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 48.5%; Under 3.5 goals: 72.8%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 54.1%; BTTS No (at least one team does not score): 45.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 38.6% | 2.59 |
| Draw | 27.9% | 3.59 |
| Udinese win | 33.6% | 2.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.29 |
| Udinese expected goals | 1.35 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 27.2% |
| Under 3.5 | 72.8% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.24% |
| 2 | 1-0 | 10.05% |
| 3 | 2-1 | 8.68% |
| 4 | 0-1 | 8.49% |
| 5 | 0-0 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 38.6% | 41.5% | 2.46 | -5.1% |
| Draw | 27.9% | 29.7% | 3.35 | -6.7% |
| Udinese win | 33.6% | 28.8% | 3.35 | +12.4% |
| Over 2.5 | 48.5% | 45.6% | 2.24 | +8.7% |
| Under 2.5 | 51.5% | 54.4% | 1.79 | -7.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-12T18:45:00+00:00 |
| Fixture id | f4a28510bb0c835280a2aca709c19d50 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:56:56Z |
| Market best away last update utc | 2026-10-11T08:56:56Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Torino |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.1% |
| P btts no | 45.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.20 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.68 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.94 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 38.3% |
| Raw p over 1 5 | 73.9% |
| Raw p under 3 5 | 72.7% |
| Raw p btts yes | 53.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.35 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | -2.9% |
| Draw probability edge | -1.8% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | +2.9% |
| Under 2.5 probability edge | -2.9% |
| Raw edge prob home | -0.0583 |
| Raw ev home | -0.1228 |
| Raw edge prob draw | -0.0370 |
| Raw ev draw | -0.1285 |
| Raw edge prob away | 0.0953 |
| Raw ev away | 0.2839 |

</details>


---

## 2026-10-16 — Frosinone vs Sassuolo

The model's most likely 1X2 outcome is **Frosinone win** at **47.4%**. Expected goals are 1.84 for Frosinone and 1.12 for Sassuolo (2.95 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.4%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 47.4% | 2.11 |
| Draw | 23.6% | 4.23 |
| Sassuolo win | 29.0% | 3.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.84 |
| Sassuolo expected goals | 1.12 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 78.8% |
| Under 1.5 | 21.2% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.6% |
| Under 3.5 | 66.4% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.08% |
| 2 | 2-1 | 8.58% |
| 3 | 1-0 | 8.42% |
| 4 | 2-0 | 7.68% |
| 5 | 1-2 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 47.4% | 40.5% | 2.53 | +19.8% |
| Draw | 23.6% | 24.6% | 3.80 | -10.2% |
| Sassuolo win | 29.0% | 35.0% | 2.96 | -14.2% |
| Over 2.5 | 55.9% | 64.6% | 1.62 | -9.4% |
| Under 2.5 | 44.1% | 35.4% | 2.61 | +15.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-16T18:45:00+00:00 |
| Fixture id | 7d3160040958fe21778fd5ee485666c3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:56Z |
| Market best draw last update utc | 2026-10-11T08:56:39Z |
| Market best away last update utc | 2026-10-11T08:56:56Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Unibet (SE) |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.60 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.71 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.98 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.79 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.3% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 79.3% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Home probability edge | +6.9% |
| Draw probability edge | -0.9% |
| Away probability edge | -6.0% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | 0.1378 |
| Raw ev home | 0.3726 |
| Raw edge prob draw | -0.0185 |
| Raw ev draw | -0.1367 |
| Raw edge prob away | -0.1193 |
| Raw ev away | -0.3183 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **72.2%**. Expected goals are 2.01 for AS Roma and 0.66 for Genoa (2.67 combined). The most likely exact score is 1-0 at 14.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.6%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 41.1%; BTTS No (at least one team does not score): 58.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 72.2% | 1.39 |
| Draw | 17.4% | 5.74 |
| Genoa win | 10.4% | 9.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 2.01 |
| Genoa expected goals | 0.66 |
| Expected total goals | 2.67 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 75.0% |
| Under 1.5 | 25.0% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.4% |
| Under 3.5 | 71.6% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.59% |
| 2 | 2-0 | 14.59% |
| 3 | 3-0 | 9.75% |
| 4 | 2-1 | 9.65% |
| 5 | 1-1 | 8.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 72.2% | 75.2% | 1.36 | -1.9% |
| Draw | 17.4% | 15.3% | 5.70 | -0.6% |
| Genoa win | 10.4% | 9.5% | 10.50 | +9.3% |
| Over 2.5 | 50.9% | 57.5% | 1.72 | -12.5% |
| Under 2.5 | 49.1% | 42.5% | 2.31 | +13.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | 18d478f469da3bcc654dd4555b85c7e3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:56Z |
| Market best draw last update utc | 2026-10-11T08:56:10Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.1% |
| P btts no | 58.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.32 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.00 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.53 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.34 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 11.3% |
| Raw p over 1 5 | 74.5% |
| Raw p under 3 5 | 72.1% |
| Raw p btts yes | 41.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.26 |
| Reference draw odds | 4.60 |
| Reference away odds | 6.75 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.31 |
| Home probability edge | -3.1% |
| Draw probability edge | +2.2% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | -0.0613 |
| Raw ev home | -0.0603 |
| Raw edge prob draw | 0.0434 |
| Raw ev draw | 0.1172 |
| Raw edge prob away | 0.0179 |
| Raw ev away | 0.1866 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.4%**. Expected goals are 1.07 for Bologna and 2.13 for Inter Milan (3.21 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 62.0%; Under 3.5 goals: 60.2%; Under 4.5 goals: 78.0%; BTTS Yes (both teams score): 58.1%; BTTS No (at least one team does not score): 41.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 18.1% | 5.53 |
| Draw | 20.6% | 4.86 |
| Inter Milan win | 61.4% | 1.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.07 |
| Inter Milan expected goals | 2.13 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 62.0% |
| Under 2.5 | 38.0% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 22.0% |
| Under 4.5 | 78.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.84% |
| 2 | 1-1 | 9.44% |
| 3 | 0-2 | 9.17% |
| 4 | 0-1 | 8.65% |
| 5 | 1-3 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 18.1% | 17.9% | 5.70 | +3.0% |
| Draw | 20.6% | 21.0% | 4.20 | -13.6% |
| Inter Milan win | 61.4% | 61.0% | 1.69 | +3.7% |
| Over 2.5 | 62.0% | 57.4% | 1.72 | +6.6% |
| Under 2.5 | 38.0% | 42.6% | 2.30 | -12.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:00:00+00:00 |
| Fixture id | bfefc309177723410230fee52f650315 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:10Z |
| Market best draw last update utc | 2026-10-11T08:56:55Z |
| Market best away last update utc | 2026-10-11T08:56:56Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bologna |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.40 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.85 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.55 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 61.7% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 57.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.30 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.52 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +0.2% |
| Draw probability edge | -0.5% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +4.6% |
| Under 2.5 probability edge | -4.6% |
| Raw edge prob home | 0.0033 |
| Raw ev home | 0.0399 |
| Raw edge prob draw | -0.0096 |
| Raw ev draw | -0.1562 |
| Raw edge prob away | 0.0062 |
| Raw ev away | 0.0421 |
| Market p over 1 5 | 83.4% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:56:09Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 64.4% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:56:55Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.59 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 56.8% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:56:55Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.12 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **65.2%**. Expected goals are 0.67 for Venezia and 2.18 for Napoli (2.85 combined). The most likely exact score is 0-2 at 12.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 52.5%; Under 3.5 goals: 69.5%; Under 4.5 goals: 84.9%; BTTS Yes (both teams score): 44.3%; BTTS No (at least one team does not score): 55.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 14.8% | 6.74 |
| Draw | 20.0% | 5.01 |
| Napoli win | 65.2% | 1.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.18 |
| Expected total goals | 2.85 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 76.3% |
| Under 1.5 | 23.7% |
| Over 2.5 | 52.5% |
| Under 2.5 | 47.5% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.1% |
| Under 4.5 | 84.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.44% |
| 2 | 0-1 | 11.48% |
| 3 | 1-1 | 9.44% |
| 4 | 0-3 | 9.02% |
| 5 | 1-2 | 8.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 14.8% | 19.5% | 4.90 | -27.4% |
| Draw | 20.0% | 22.1% | 4.22 | -15.7% |
| Napoli win | 65.2% | 58.3% | 1.76 | +14.8% |
| Over 2.5 | 52.5% | 56.4% | 1.75 | -8.1% |
| Under 2.5 | 47.5% | 43.6% | 2.25 | +6.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:00:00+00:00 |
| Fixture id | 907639dade64cca45d1ab639195d201e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:24Z |
| Market best draw last update utc | 2026-10-11T08:56:56Z |
| Market best away last update utc | 2026-10-11T08:56:56Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betsson |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 44.3% |
| P btts no | 55.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.48 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.22 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.27 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.61 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 72.1% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 43.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.00 |
| Reference draw odds | 3.60 |
| Reference away odds | 1.58 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -4.7% |
| Draw probability edge | -2.1% |
| Away probability edge | +6.9% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0942 |
| Raw ev home | -0.5043 |
| Raw edge prob draw | -0.0429 |
| Raw ev draw | -0.2477 |
| Raw edge prob away | 0.1371 |
| Raw ev away | 0.2682 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **45.6%**. Expected goals are 1.28 for AC Milan and 1.16 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.9%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 49.1%; BTTS No (at least one team does not score): 50.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 45.6% | 2.19 |
| Draw | 25.8% | 3.87 |
| Atalanta BC win | 28.5% | 3.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.28 |
| Atalanta BC expected goals | 1.16 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.02% |
| 2 | 1-1 | 12.23% |
| 3 | 2-1 | 9.60% |
| 4 | 0-1 | 8.68% |
| 5 | 2-0 | 8.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 45.6% | 51.8% | 1.93 | -11.9% |
| Draw | 25.8% | 24.5% | 3.86 | -0.2% |
| Atalanta BC win | 28.5% | 23.7% | 4.30 | +22.6% |
| Over 2.5 | 44.6% | 53.9% | 1.83 | -18.5% |
| Under 2.5 | 55.4% | 46.1% | 2.13 | +18.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T16:00:00+00:00 |
| Fixture id | f9403dd597edbfaa73abdc974e55344c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:56Z |
| Market best draw last update utc | 2026-10-11T08:56:56Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 49.1% |
| P btts no | 50.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.16 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.75 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 33.3% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.76 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.45 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.13 |
| Home probability edge | -6.2% |
| Draw probability edge | +1.3% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.1233 |
| Raw ev home | -0.2379 |
| Raw edge prob draw | 0.0268 |
| Raw ev draw | 0.0493 |
| Raw edge prob away | 0.0965 |
| Raw ev away | 0.4332 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.9%**. Expected goals are 1.00 for Fiorentina and 1.73 for Como (2.73 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.1%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 52.2%; BTTS No (at least one team does not score): 47.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.9% | 4.01 |
| Draw | 24.2% | 4.14 |
| Como win | 50.9% | 1.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.00 |
| Como expected goals | 1.73 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.49% |
| 2 | 0-1 | 10.56% |
| 3 | 0-2 | 9.10% |
| 4 | 1-2 | 9.09% |
| 5 | 1-0 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.9% | 28.1% | 3.65 | -9.0% |
| Draw | 24.2% | 24.8% | 3.85 | -6.9% |
| Como win | 50.9% | 47.1% | 2.13 | +8.4% |
| Over 2.5 | 51.0% | 57.1% | 1.73 | -11.8% |
| Under 2.5 | 49.0% | 42.9% | 2.29 | +12.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 3ea32a0aa44a5f0ef7fd088155430087 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:55Z |
| Market best draw last update utc | 2026-10-11T08:56:39Z |
| Market best away last update utc | 2026-10-11T08:56:56Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 52.2% |
| P btts no | 47.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.11 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.05 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.16 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 21.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 51.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.35 |
| Reference away odds | 1.92 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.29 |
| Home probability edge | -3.2% |
| Draw probability edge | -0.6% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.0638 |
| Raw ev home | -0.2061 |
| Raw edge prob draw | -0.0118 |
| Raw ev draw | -0.0919 |
| Raw edge prob away | 0.0757 |
| Raw ev away | 0.1643 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **54.6%**. Expected goals are 1.37 for Juventus and 0.85 for Lazio (2.22 combined). The most likely exact score is 1-0 at 16.6%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 39.2%; Under 3.5 goals: 81.2%; Under 4.5 goals: 92.3%; BTTS Yes (both teams score): 41.9%; BTTS No (at least one team does not score): 58.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 54.6% | 1.83 |
| Draw | 25.0% | 4.00 |
| Lazio win | 20.4% | 4.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.85 |
| Expected total goals | 2.22 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 39.2% |
| Under 2.5 | 60.8% |
| Over 3.5 | 18.8% |
| Under 3.5 | 81.2% |
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.64% |
| 2 | 1-1 | 11.41% |
| 3 | 2-0 | 11.33% |
| 4 | 0-0 | 9.81% |
| 5 | 2-1 | 9.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 54.6% | 60.1% | 1.69 | -7.8% |
| Draw | 25.0% | 22.5% | 4.04 | +1.1% |
| Lazio win | 20.4% | 17.4% | 5.80 | +18.3% |
| Over 2.5 | 39.2% | 48.6% | 2.03 | -20.3% |
| Under 2.5 | 60.8% | 51.4% | 1.92 | +16.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T18:45:00+00:00 |
| Fixture id | 4c4026e2782f09d6f0ff2bde2a390513 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:56Z |
| Market best draw last update utc | 2026-10-11T08:56:56Z |
| Market best away last update utc | 2026-10-11T08:56:39Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Juventus |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.9% |
| P btts no | 58.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.20 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.33 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.93 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 23.4% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 42.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.54 |
| Reference draw odds | 3.55 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.92 |
| Home probability edge | -5.5% |
| Draw probability edge | +2.6% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.1105 |
| Raw ev home | -0.1710 |
| Raw edge prob draw | 0.0513 |
| Raw ev draw | 0.1144 |
| Raw edge prob away | 0.0592 |
| Raw ev away | 0.3549 |
| Market p over 1 5 | 74.3% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T08:56:55Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.44 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 74.2% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:56:55Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 48.2% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T08:56:56Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 1.80 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **52.0%**. Expected goals are 1.44 for Udinese and 0.82 for Lecce (2.26 combined). The most likely exact score is 1-0 at 15.2%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 39.6%; Under 3.5 goals: 80.7%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 42.5%; BTTS No (at least one team does not score): 57.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 52.0% | 1.92 |
| Draw | 26.0% | 3.84 |
| Lecce win | 22.0% | 4.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.44 |
| Lecce expected goals | 0.82 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 66.0% |
| Under 1.5 | 34.0% |
| Over 2.5 | 39.6% |
| Under 2.5 | 60.4% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.17% |
| 2 | 1-1 | 11.92% |
| 3 | 2-0 | 10.85% |
| 4 | 0-0 | 10.06% |
| 5 | 2-1 | 8.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 52.0% | 52.4% | 1.95 | +1.4% |
| Draw | 26.0% | 25.2% | 3.71 | -3.5% |
| Lecce win | 22.0% | 22.4% | 4.40 | -3.2% |
| Over 2.5 | 39.6% | 49.2% | 2.00 | -20.8% |
| Under 2.5 | 60.4% | 50.8% | 1.94 | +17.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T10:30:00+00:00 |
| Fixture id | 367da93aa21a1e13eeafb94fd2263c75 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:56Z |
| Market best draw last update utc | 2026-10-11T08:56:56Z |
| Market best away last update utc | 2026-10-11T08:56:10Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Tipico |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.5% |
| P btts no | 57.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.94 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.53 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 21.6% |
| Raw p over 1 5 | 65.9% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 42.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.74 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.94 |
| Home probability edge | -0.4% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | -0.0077 |
| Raw ev home | 0.0061 |
| Raw edge prob draw | 0.0157 |
| Raw ev draw | -0.0054 |
| Raw edge prob away | -0.0080 |
| Raw ev away | -0.0498 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **38.3%**. Expected goals are 1.13 for Monza and 1.57 for Cagliari (2.70 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 49.8%; Under 3.5 goals: 72.0%; Under 4.5 goals: 86.7%; BTTS Yes (both teams score): 54.1%; BTTS No (at least one team does not score): 45.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 35.3% | 2.83 |
| Draw | 26.4% | 3.79 |
| Cagliari win | 38.3% | 2.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.13 |
| Cagliari expected goals | 1.57 |
| Expected total goals | 2.70 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 74.5% |
| Under 1.5 | 25.5% |
| Over 2.5 | 49.8% |
| Under 2.5 | 50.2% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.3% |
| Under 4.5 | 86.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.53% |
| 2 | 1-0 | 9.89% |
| 3 | 2-1 | 8.68% |
| 4 | 0-1 | 8.55% |
| 5 | 1-2 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 35.3% | 43.3% | 2.40 | -15.2% |
| Draw | 26.4% | 27.8% | 3.30 | -13.0% |
| Cagliari win | 38.3% | 28.9% | 3.65 | +39.7% |
| Over 2.5 | 49.8% | 46.1% | 2.13 | +6.0% |
| Under 2.5 | 50.2% | 53.9% | 1.83 | -8.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T16:30:00+00:00 |
| Fixture id | ce94aca384a20f6af459366da6e1dd21 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:39Z |
| Market best draw last update utc | 2026-10-11T08:56:10Z |
| Market best away last update utc | 2026-10-11T08:56:55Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Tipico |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.1% |
| P btts no | 45.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.18 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.92 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.52 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 27.4% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 47.7% |
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 53.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.13 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | -8.0% |
| Draw probability edge | -1.4% |
| Away probability edge | +9.4% |
| Over 2.5 probability edge | +3.7% |
| Under 2.5 probability edge | -3.7% |
| Raw edge prob home | -0.1593 |
| Raw ev home | -0.3430 |
| Raw edge prob draw | -0.0281 |
| Raw ev draw | -0.1759 |
| Raw edge prob away | 0.1875 |
| Raw ev away | 0.7393 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.2%**. Expected goals are 1.02 for Parma and 1.08 for Torino (2.10 combined). The most likely exact score is 0-1 at 13.9%. Goal-market probabilities: at least one goal: 88.1%; Over 2.5 goals: 35.2%; Under 3.5 goals: 83.8%; Under 4.5 goals: 93.7%; BTTS Yes (both teams score): 42.0%; BTTS No (at least one team does not score): 58.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 32.6% | 3.06 |
| Draw | 29.1% | 3.43 |
| Torino win | 38.2% | 2.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.02 |
| Torino expected goals | 1.08 |
| Expected total goals | 2.10 |
| Over 0.5 | 88.1% |
| Under 0.5 | 11.9% |
| Over 1.5 | 62.0% |
| Under 1.5 | 38.0% |
| Over 2.5 | 35.2% |
| Under 2.5 | 64.8% |
| Over 3.5 | 16.2% |
| Under 3.5 | 83.8% |
| Over 4.5 | 6.3% |
| Under 4.5 | 93.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.90% |
| 2 | 1-1 | 13.12% |
| 3 | 1-0 | 12.19% |
| 4 | 0-0 | 11.90% |
| 5 | 1-2 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 32.6% | 31.5% | 3.25 | +6.1% |
| Draw | 29.1% | 28.5% | 3.25 | -5.3% |
| Torino win | 38.2% | 40.0% | 2.54 | -2.9% |
| Over 2.5 | 35.2% | 39.4% | 2.48 | -12.6% |
| Under 2.5 | 64.8% | 60.6% | 1.64 | +6.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T18:45:00+00:00 |
| Fixture id | 07014d9adc65ca39710bd9f0c7c0d3f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:56:56Z |
| Market best draw last update utc | 2026-10-11T08:56:55Z |
| Market best away last update utc | 2026-10-11T08:56:56Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | LeoVegas (SE) |
| Matched home-team name | Parma |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.0% |
| P btts no | 58.0% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.41 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.63 |
| Fair Over 2.5 odds | 2.84 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.19 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 15.97 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 36.5% |
| Raw p over 1 5 | 62.0% |
| Raw p under 3 5 | 83.9% |
| Raw p btts yes | 42.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.70 |
| Reference draw odds | 2.95 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.48 |
| Reference Under 2.5 odds | 1.63 |
| Home probability edge | +1.1% |
| Draw probability edge | +0.7% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | 0.0220 |
| Raw ev home | 0.0964 |
| Raw edge prob draw | 0.0134 |
| Raw ev draw | -0.0317 |
| Raw edge prob away | -0.0354 |
| Raw ev away | -0.0736 |
| Market p over 1 5 | 67.4% |
| Market over 1 5 odds | 1.44 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T08:56:55Z |
| Market reference over 1 5 odds | 1.44 |
| Market reference over 1 5 opposite odds | 2.81 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 80.5% |
| Market under 3 5 odds | 1.20 |
| Best under 3 5 bookmaker | Codere (IT) |
| Market best under 3 5 last update utc | 2026-10-11T08:56:11Z |
| Market reference under 3 5 odds | 1.20 |
| Market reference under 3 5 opposite odds | 3.95 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 47.2% |
| Market btts yes odds | 1.96 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T08:56:56Z |
| Market reference btts yes odds | 1.96 |
| Market reference btts yes opposite odds | 1.77 |
| Market btts yes bookmakers | 2 |

</details>


---
