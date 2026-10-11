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
| Additional event odds calls used before this league | 15.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 5.00 |
| Additional event odds calls this league | 5.00 |
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

The model's most likely 1X2 outcome is **Juventus win** at **57.6%**. Expected goals are 0.80 for Cagliari and 1.48 for Juventus (2.28 combined). The most likely exact score is 0-1 at 16.4%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 40.5%; Under 3.5 goals: 80.0%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 42.0%; BTTS No (at least one team does not score): 58.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 17.3% | 5.80 |
| Draw | 25.1% | 3.98 |
| Juventus win | 57.6% | 1.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 0.80 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.5% |
| Under 2.5 | 59.5% |
| Over 3.5 | 20.0% |
| Under 3.5 | 80.0% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.40% |
| 2 | 0-2 | 12.12% |
| 3 | 1-1 | 11.49% |
| 4 | 0-0 | 9.71% |
| 5 | 1-2 | 9.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 17.3% | 14.3% | 7.20 | +24.2% |
| Draw | 25.1% | 23.9% | 4.17 | +4.7% |
| Juventus win | 57.6% | 61.7% | 1.61 | -7.2% |
| Over 2.5 | 40.5% | 46.5% | 2.14 | -13.3% |
| Under 2.5 | 59.5% | 53.5% | 1.88 | +11.9% |

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
| Market best home last update utc | 2026-10-11T06:31:55Z |
| Market best draw last update utc | 2026-10-11T06:31:42Z |
| Market best away last update utc | 2026-10-11T06:31:42Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.0% |
| P btts no | 58.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.30 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.47 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.00 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.98 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 53.6% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.3% |
| Raw p btts yes | 42.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.47 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.59 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +2.9% |
| Draw probability edge | +1.2% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | 0.0585 |
| Raw ev home | 0.4531 |
| Raw edge prob draw | 0.0230 |
| Raw ev draw | 0.0946 |
| Raw edge prob away | -0.0815 |
| Raw ev away | -0.1375 |

</details>


---

## 2026-10-11 — Como vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **37.0%**. Expected goals are 1.17 for Como and 1.30 for AS Roma (2.47 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 44.8%; Under 3.5 goals: 76.4%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 35.8% | 2.79 |
| Draw | 27.2% | 3.68 |
| AS Roma win | 37.0% | 2.70 |

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
| Over 2.5 | 44.8% |
| Under 2.5 | 55.2% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.89% |
| 2 | 1-0 | 10.64% |
| 3 | 0-1 | 10.33% |
| 4 | 0-0 | 8.42% |
| 5 | 2-1 | 8.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 35.8% | 38.1% | 2.61 | -6.5% |
| Draw | 27.2% | 27.4% | 3.73 | +1.4% |
| AS Roma win | 37.0% | 34.6% | 2.94 | +8.8% |
| Over 2.5 | 44.8% | 60.5% | 1.68 | -24.7% |
| Under 2.5 | 55.2% | 39.5% | 2.38 | +31.3% |

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
| Market best home last update utc | 2026-10-11T06:31:42Z |
| Market best draw last update utc | 2026-10-11T06:31:42Z |
| Market best away last update utc | 2026-10-11T06:31:55Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
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
| Fair Under 0.5 odds | 11.87 |
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
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.55 |
| Reference draw odds | 3.51 |
| Reference away odds | 2.80 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | -2.3% |
| Draw probability edge | -0.2% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -15.6% |
| Under 2.5 probability edge | +15.6% |
| Raw edge prob home | -0.0451 |
| Raw ev home | -0.1243 |
| Raw edge prob draw | -0.0040 |
| Raw ev draw | 0.0060 |
| Raw edge prob away | 0.0491 |
| Raw ev away | 0.1606 |

</details>


---

## 2026-10-11 — Lazio vs Monza

The model's most likely 1X2 outcome is **Lazio win** at **60.7%**. Expected goals are 2.01 for Lazio and 0.87 for Monza (2.88 combined). The most likely exact score is 2-0 at 10.8%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 54.0%; Under 3.5 goals: 67.9%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 60.7% | 1.65 |
| Draw | 22.3% | 4.48 |
| Monza win | 17.0% | 5.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 2.01 |
| Monza expected goals | 0.87 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 54.0% |
| Under 2.5 | 46.0% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.78% |
| 2 | 1-0 | 10.76% |
| 3 | 1-1 | 10.60% |
| 4 | 2-1 | 9.33% |
| 5 | 3-0 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 60.7% | 57.2% | 1.75 | +6.2% |
| Draw | 22.3% | 24.1% | 4.10 | -8.6% |
| Monza win | 17.0% | 18.7% | 5.50 | -6.4% |
| Over 2.5 | 54.0% | 53.4% | 1.86 | +0.5% |
| Under 2.5 | 46.0% | 46.6% | 2.14 | -1.6% |

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
| Market best home last update utc | 2026-10-11T06:31:55Z |
| Market best draw last update utc | 2026-10-11T06:31:40Z |
| Market best away last update utc | 2026-10-11T06:31:40Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Lazio |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.50 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.12 |
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
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.71 |
| Reference draw odds | 3.93 |
| Reference away odds | 5.02 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +3.4% |
| Draw probability edge | -1.8% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | 0.0689 |
| Raw ev home | 0.1222 |
| Raw edge prob draw | -0.0358 |
| Raw ev draw | -0.1592 |
| Raw edge prob away | -0.0331 |
| Raw ev away | -0.1549 |

</details>


---

## 2026-10-11 — Lecce vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **49.4%**. Expected goals are 0.78 for Lecce and 1.33 for Bologna (2.11 combined). The most likely exact score is 0-1 at 16.1%. Goal-market probabilities: at least one goal: 87.9%; Over 2.5 goals: 35.3%; Under 3.5 goals: 83.6%; Under 4.5 goals: 93.7%; BTTS Yes (both teams score): 39.9%; BTTS No (at least one team does not score): 60.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 22.1% | 4.52 |
| Draw | 28.5% | 3.51 |
| Bologna win | 49.4% | 2.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.78 |
| Bologna expected goals | 1.33 |
| Expected total goals | 2.11 |
| Over 0.5 | 87.9% |
| Under 0.5 | 12.1% |
| Over 1.5 | 62.3% |
| Under 1.5 | 37.7% |
| Over 2.5 | 35.3% |
| Under 2.5 | 64.7% |
| Over 3.5 | 16.4% |
| Under 3.5 | 83.6% |
| Over 4.5 | 6.3% |
| Under 4.5 | 93.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.05% |
| 2 | 1-1 | 12.62% |
| 3 | 0-0 | 12.13% |
| 4 | 0-2 | 10.64% |
| 5 | 1-0 | 9.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 22.1% | 22.2% | 4.58 | +1.3% |
| Draw | 28.5% | 28.7% | 3.44 | -2.1% |
| Bologna win | 49.4% | 49.1% | 2.06 | +1.8% |
| Over 2.5 | 35.3% | 43.5% | 2.18 | -23.1% |
| Under 2.5 | 64.7% | 56.5% | 1.81 | +17.1% |

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
| Market best home last update utc | 2026-10-11T06:31:42Z |
| Market best draw last update utc | 2026-10-11T06:31:42Z |
| Market best away last update utc | 2026-10-11T06:31:55Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 39.9% |
| P btts no | 60.1% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.24 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.65 |
| Fair Over 2.5 odds | 2.83 |
| Fair Under 2.5 odds | 1.55 |
| Fair Over 3.5 odds | 6.12 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.83 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 22.0% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 62.3% |
| Raw p under 3 5 | 83.6% |
| Raw p btts yes | 39.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.28 |
| Reference draw odds | 3.34 |
| Reference away odds | 1.99 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.61 |
| Home probability edge | -0.1% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -8.2% |
| Under 2.5 probability edge | +8.2% |
| Raw edge prob home | -0.0020 |
| Raw ev home | 0.0082 |
| Raw edge prob draw | -0.0051 |
| Raw ev draw | -0.0296 |
| Raw edge prob away | 0.0071 |
| Raw ev away | 0.0255 |
| Market p over 1 5 | 70.9% |
| Market over 1 5 odds | 1.40 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T06:31:55Z |
| Market reference over 1 5 odds | 1.38 |
| Market reference over 1 5 opposite odds | 3.17 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 77.1% |
| Market under 3 5 odds | 1.28 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T06:31:55Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 4.05 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 49.0% |
| Market btts yes odds | 1.97 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T06:31:39Z |
| Market reference btts yes odds | 1.96 |
| Market reference btts yes opposite odds | 1.89 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Sassuolo vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **51.3%**. Expected goals are 1.13 for Sassuolo and 1.68 for AC Milan (2.81 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 53.2%; Under 3.5 goals: 68.8%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 24.0% | 4.16 |
| Draw | 24.6% | 4.06 |
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
| 1 | 1-1 | 11.64% |
| 2 | 0-1 | 10.36% |
| 3 | 1-2 | 9.79% |
| 4 | 0-2 | 8.67% |
| 5 | 1-0 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 24.0% | 22.5% | 4.60 | +10.6% |
| Draw | 24.6% | 25.2% | 3.90 | -4.0% |
| AC Milan win | 51.3% | 52.3% | 1.91 | -1.9% |
| Over 2.5 | 53.2% | 53.4% | 1.81 | -3.6% |
| Under 2.5 | 46.8% | 46.6% | 2.25 | +5.2% |

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
| Market best home last update utc | 2026-10-11T06:31:39Z |
| Market best draw last update utc | 2026-10-11T06:31:42Z |
| Market best away last update utc | 2026-10-11T06:31:42Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Matchbook |
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
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.42 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.37 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.49 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 25.6% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 50.4% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 68.9% |
| Raw p btts yes | 55.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.23 |
| Reference draw odds | 3.78 |
| Reference away odds | 1.87 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +1.6% |
| Draw probability edge | -0.6% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.0314 |
| Raw ev home | 0.1778 |
| Raw edge prob draw | -0.0123 |
| Raw ev draw | -0.0637 |
| Raw edge prob away | -0.0191 |
| Raw ev away | -0.0376 |

</details>


---

## 2026-10-12 — Atalanta BC vs Venezia

The model's most likely 1X2 outcome is **Atalanta BC win** at **68.9%**. Expected goals are 2.35 for Atalanta BC and 0.66 for Venezia (3.02 combined). The most likely exact score is 2-0 at 12.4%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 56.1%; Under 3.5 goals: 65.7%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 45.0%; BTTS No (at least one team does not score): 55.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 68.9% | 1.45 |
| Draw | 19.2% | 5.21 |
| Venezia win | 11.9% | 8.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.35 |
| Venezia expected goals | 0.66 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 56.1% |
| Under 2.5 | 43.9% |
| Over 3.5 | 34.3% |
| Under 3.5 | 65.7% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.44% |
| 2 | 1-0 | 10.60% |
| 3 | 3-0 | 9.76% |
| 4 | 1-1 | 9.11% |
| 5 | 2-1 | 8.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 68.9% | 62.5% | 1.63 | +12.3% |
| Draw | 19.2% | 22.4% | 4.40 | -15.5% |
| Venezia win | 11.9% | 15.1% | 6.20 | -26.4% |
| Over 2.5 | 56.1% | 61.8% | 1.55 | -13.1% |
| Under 2.5 | 43.9% | 38.2% | 2.45 | +7.7% |

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
| Market best home last update utc | 2026-10-11T06:31:42Z |
| Market best draw last update utc | 2026-10-11T06:31:55Z |
| Market best away last update utc | 2026-10-11T06:31:55Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Nordic Bet |
| Matched home-team name | Atalanta |
| Matched away-team name | Venezia |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.0% |
| P btts no | 55.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.11 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.78 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 2.91 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.64 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 75.3% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 8.7% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 64.4% |
| Raw p btts yes | 43.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.57 |
| Reference draw odds | 4.20 |
| Reference away odds | 6.15 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | +6.4% |
| Draw probability edge | -3.2% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | 0.1283 |
| Raw ev home | 0.2280 |
| Raw edge prob draw | -0.0645 |
| Raw ev draw | -0.2971 |
| Raw edge prob away | -0.0639 |
| Raw ev away | -0.4615 |

</details>


---

## 2026-10-12 — Torino vs Udinese

The model's most likely 1X2 outcome is **Torino win** at **38.5%**. Expected goals are 1.29 for Torino and 1.35 for Udinese (2.64 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 48.5%; Under 3.5 goals: 72.8%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 54.1%; BTTS No (at least one team does not score): 45.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 38.5% | 2.60 |
| Draw | 27.9% | 3.58 |
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
| 1 | 1-1 | 13.28% |
| 2 | 1-0 | 10.02% |
| 3 | 2-1 | 8.66% |
| 4 | 0-1 | 8.50% |
| 5 | 0-0 | 7.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 38.5% | 41.3% | 2.46 | -5.4% |
| Draw | 27.9% | 29.9% | 3.35 | -6.4% |
| Udinese win | 33.6% | 28.9% | 3.40 | +14.2% |
| Over 2.5 | 48.5% | 44.3% | 2.26 | +9.6% |
| Under 2.5 | 51.5% | 55.7% | 1.79 | -7.8% |

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
| Market best home last update utc | 2026-10-11T06:31:55Z |
| Market best draw last update utc | 2026-10-11T06:31:42Z |
| Market best away last update utc | 2026-10-11T06:31:55Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Torino |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.1% |
| P btts no | 45.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.16 |
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
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.36 |
| Reference draw odds | 3.23 |
| Reference away odds | 3.34 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.62 |
| Home probability edge | -2.8% |
| Draw probability edge | -1.9% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | +4.2% |
| Under 2.5 probability edge | -4.2% |
| Raw edge prob home | -0.0562 |
| Raw ev home | -0.1228 |
| Raw edge prob draw | -0.0385 |
| Raw ev draw | -0.1285 |
| Raw edge prob away | 0.0947 |
| Raw ev away | 0.3031 |

</details>


---

## 2026-10-16 — Frosinone vs Sassuolo

The model's most likely 1X2 outcome is **Frosinone win** at **46.9%**. Expected goals are 1.84 for Frosinone and 1.12 for Sassuolo (2.95 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.5%; Under 3.5 goals: 66.4%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 46.9% | 2.13 |
| Draw | 25.2% | 3.98 |
| Sassuolo win | 27.9% | 3.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.84 |
| Sassuolo expected goals | 1.12 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 78.8% |
| Under 1.5 | 21.2% |
| Over 2.5 | 55.5% |
| Under 2.5 | 44.5% |
| Over 3.5 | 33.6% |
| Under 3.5 | 66.4% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.79% |
| 2 | 2-1 | 8.50% |
| 3 | 1-0 | 8.35% |
| 4 | 2-0 | 7.61% |
| 5 | 1-2 | 7.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 46.9% | 39.6% | 2.53 | +18.8% |
| Draw | 25.2% | 27.6% | 3.70 | -6.9% |
| Sassuolo win | 27.9% | 32.8% | 2.96 | -17.4% |
| Over 2.5 | 55.5% | 60.5% | 1.62 | -10.2% |
| Under 2.5 | 44.5% | 39.5% | 2.42 | +7.8% |

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
| Market best home last update utc | 2026-10-11T06:31:42Z |
| Market best draw last update utc | 2026-10-11T06:31:55Z |
| Market best away last update utc | 2026-10-11T06:31:42Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 6.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Unibet (SE) |
| Best under 2 5 bookmaker | Nordic Bet |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.49 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.72 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 2.98 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.3% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 79.3% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.42 |
| Reference draw odds | 3.42 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | +7.3% |
| Draw probability edge | -2.4% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | 0.1462 |
| Raw ev home | 0.3726 |
| Raw edge prob draw | -0.0487 |
| Raw ev draw | -0.1594 |
| Raw edge prob away | -0.0976 |
| Raw ev away | -0.3183 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **71.3%**. Expected goals are 2.01 for AS Roma and 0.66 for Genoa (2.67 combined). The most likely exact score is 1-0 at 14.4%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 50.6%; Under 3.5 goals: 71.8%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 41.3%; BTTS No (at least one team does not score): 58.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 71.3% | 1.40 |
| Draw | 18.0% | 5.56 |
| Genoa win | 10.7% | 9.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 2.01 |
| Genoa expected goals | 0.66 |
| Expected total goals | 2.67 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 74.9% |
| Under 1.5 | 25.1% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.43% |
| 2 | 2-0 | 14.42% |
| 3 | 3-0 | 9.64% |
| 4 | 2-1 | 9.54% |
| 5 | 1-1 | 8.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 71.3% | 73.6% | 1.36 | -3.0% |
| Draw | 18.0% | 16.4% | 5.70 | +2.6% |
| Genoa win | 10.7% | 10.0% | 10.50 | +11.9% |
| Over 2.5 | 50.6% | 59.5% | 1.72 | -13.0% |
| Under 2.5 | 49.4% | 40.5% | 2.31 | +14.1% |

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
| Market best home last update utc | 2026-10-11T06:31:42Z |
| Market best draw last update utc | 2026-10-11T06:31:55Z |
| Market best away last update utc | 2026-10-11T06:31:55Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.3% |
| P btts no | 58.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.81 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.98 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.40 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 11.3% |
| Raw p over 1 5 | 74.5% |
| Raw p under 3 5 | 72.1% |
| Raw p btts yes | 41.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.33 |
| Reference draw odds | 5.38 |
| Reference away odds | 8.51 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -2.3% |
| Draw probability edge | +1.6% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | -0.0450 |
| Raw ev home | -0.0603 |
| Raw edge prob draw | 0.0321 |
| Raw ev draw | 0.1172 |
| Raw edge prob away | 0.0129 |
| Raw ev away | 0.1866 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **60.8%**. Expected goals are 1.07 for Bologna and 2.13 for Inter Milan (3.21 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 61.6%; Under 3.5 goals: 60.2%; Under 4.5 goals: 78.2%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.4% | 5.75 |
| Draw | 21.8% | 4.58 |
| Inter Milan win | 60.8% | 1.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.07 |
| Inter Milan expected goals | 2.13 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 61.6% |
| Under 2.5 | 38.4% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.8% |
| Under 4.5 | 78.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.02% |
| 2 | 1-2 | 9.75% |
| 3 | 0-2 | 9.09% |
| 4 | 0-1 | 8.57% |
| 5 | 1-3 | 6.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.4% | 16.5% | 5.70 | -0.9% |
| Draw | 21.8% | 23.6% | 4.20 | -8.3% |
| Inter Milan win | 60.8% | 59.9% | 1.69 | +2.7% |
| Over 2.5 | 61.6% | 56.9% | 1.72 | +5.9% |
| Under 2.5 | 38.4% | 43.1% | 2.30 | -11.6% |

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
| Market best home last update utc | 2026-10-11T06:31:55Z |
| Market best draw last update utc | 2026-10-11T06:31:23Z |
| Market best away last update utc | 2026-10-11T06:31:42Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bologna |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.99 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.84 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.60 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 61.7% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 57.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.45 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.62 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.02 |
| Home probability edge | +0.9% |
| Draw probability edge | -1.7% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | +4.6% |
| Under 2.5 probability edge | -4.6% |
| Raw edge prob home | 0.0172 |
| Raw ev home | 0.0399 |
| Raw edge prob draw | -0.0348 |
| Raw ev draw | -0.1562 |
| Raw edge prob away | 0.0175 |
| Raw ev away | 0.0421 |
| Market p over 1 5 | 83.4% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T06:31:23Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 64.4% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T06:32:11Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.59 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T06:31:39Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.22 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **64.5%**. Expected goals are 0.67 for Venezia and 2.18 for Napoli (2.85 combined). The most likely exact score is 0-2 at 12.3%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 52.4%; Under 3.5 goals: 69.6%; Under 4.5 goals: 84.9%; BTTS Yes (both teams score): 44.3%; BTTS No (at least one team does not score): 55.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 15.4% | 6.50 |
| Draw | 20.1% | 4.98 |
| Napoli win | 64.5% | 1.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.18 |
| Expected total goals | 2.85 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 76.2% |
| Under 1.5 | 23.8% |
| Over 2.5 | 52.4% |
| Under 2.5 | 47.6% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 15.1% |
| Under 4.5 | 84.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.31% |
| 2 | 0-1 | 11.36% |
| 3 | 1-1 | 9.48% |
| 4 | 0-3 | 8.93% |
| 5 | 1-2 | 8.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 15.4% | 20.7% | 4.85 | -25.4% |
| Draw | 20.1% | 22.3% | 4.22 | -15.3% |
| Napoli win | 64.5% | 57.0% | 1.76 | +13.6% |
| Over 2.5 | 52.4% | 56.7% | 1.75 | -8.4% |
| Under 2.5 | 47.6% | 43.3% | 2.25 | +7.2% |

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
| Market best home last update utc | 2026-10-11T06:29:37Z |
| Market best draw last update utc | 2026-10-11T06:31:42Z |
| Market best away last update utc | 2026-10-11T06:31:42Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Nordic Bet |
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
| Fair Under 0.5 odds | 15.41 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.19 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.64 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 72.1% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 43.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.44 |
| Reference draw odds | 4.13 |
| Reference away odds | 1.70 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.00 |
| Home probability edge | -5.3% |
| Draw probability edge | -2.2% |
| Away probability edge | +7.5% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.1054 |
| Raw ev home | -0.5094 |
| Raw edge prob draw | -0.0447 |
| Raw ev draw | -0.2477 |
| Raw edge prob away | 0.1502 |
| Raw ev away | 0.2682 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **45.9%**. Expected goals are 1.28 for AC Milan and 1.16 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 44.4%; Under 3.5 goals: 76.9%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 45.9% | 2.18 |
| Draw | 26.3% | 3.81 |
| Atalanta BC win | 27.8% | 3.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.28 |
| Atalanta BC expected goals | 1.16 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.4% |
| Under 2.5 | 55.6% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.10% |
| 2 | 1-1 | 12.43% |
| 3 | 2-1 | 9.66% |
| 4 | 0-1 | 8.47% |
| 5 | 2-0 | 8.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 45.9% | 52.4% | 1.93 | -11.4% |
| Draw | 26.3% | 25.3% | 3.86 | +1.3% |
| Atalanta BC win | 27.8% | 22.3% | 4.30 | +19.7% |
| Over 2.5 | 44.4% | 56.1% | 1.83 | -18.7% |
| Under 2.5 | 55.6% | 43.9% | 2.13 | +18.3% |

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
| Market best home last update utc | 2026-10-11T06:31:43Z |
| Market best draw last update utc | 2026-10-11T06:31:43Z |
| Market best away last update utc | 2026-10-11T06:31:23Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.98 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.78 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 33.3% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.85 |
| Reference draw odds | 3.69 |
| Reference away odds | 4.16 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | -6.4% |
| Draw probability edge | +0.9% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | -11.7% |
| Under 2.5 probability edge | +11.7% |
| Raw edge prob home | -0.1287 |
| Raw ev home | -0.2379 |
| Raw edge prob draw | 0.0186 |
| Raw ev draw | 0.0493 |
| Raw edge prob away | 0.1101 |
| Raw ev away | 0.4332 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.4%**. Expected goals are 1.00 for Fiorentina and 1.73 for Como (2.73 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.1%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 52.3%; BTTS No (at least one team does not score): 47.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 25.2% | 3.97 |
| Draw | 24.4% | 4.10 |
| Como win | 50.4% | 1.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.00 |
| Como expected goals | 1.73 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.60% |
| 2 | 0-1 | 10.46% |
| 3 | 0-2 | 9.01% |
| 4 | 1-2 | 9.00% |
| 5 | 1-0 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 25.2% | 28.6% | 3.65 | -8.0% |
| Draw | 24.4% | 25.2% | 3.85 | -6.0% |
| Como win | 50.4% | 46.1% | 2.13 | +7.3% |
| Over 2.5 | 50.9% | 57.6% | 1.73 | -12.0% |
| Under 2.5 | 49.1% | 42.4% | 2.29 | +12.5% |

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
| Market best home last update utc | 2026-10-11T06:31:23Z |
| Market best draw last update utc | 2026-10-11T06:31:55Z |
| Market best away last update utc | 2026-10-11T06:31:43Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 52.3% |
| P btts no | 47.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.97 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.04 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.19 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 21.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 51.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.29 |
| Reference draw odds | 3.71 |
| Reference away odds | 2.09 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.02 |
| Home probability edge | -3.4% |
| Draw probability edge | -0.8% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
| Raw edge prob home | -0.0689 |
| Raw ev home | -0.2061 |
| Raw edge prob draw | -0.0166 |
| Raw ev draw | -0.0919 |
| Raw edge prob away | 0.0855 |
| Raw ev away | 0.1643 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **54.1%**. Expected goals are 1.37 for Juventus and 0.85 for Lazio (2.22 combined). The most likely exact score is 1-0 at 16.5%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.3%; Under 4.5 goals: 92.3%; BTTS Yes (both teams score): 42.1%; BTTS No (at least one team does not score): 57.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 54.1% | 1.85 |
| Draw | 25.7% | 3.89 |
| Lazio win | 20.2% | 4.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.85 |
| Expected total goals | 2.22 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.7% |
| Under 3.5 | 81.3% |
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.50% |
| 2 | 1-1 | 11.73% |
| 3 | 2-0 | 11.24% |
| 4 | 0-0 | 10.08% |
| 5 | 2-1 | 9.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 54.1% | 59.2% | 1.69 | -8.5% |
| Draw | 25.7% | 23.8% | 4.04 | +3.9% |
| Lazio win | 20.2% | 17.0% | 5.80 | +16.9% |
| Over 2.5 | 39.0% | 48.1% | 2.03 | -20.8% |
| Under 2.5 | 61.0% | 51.9% | 1.92 | +17.1% |

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
| Market best home last update utc | 2026-10-11T06:31:43Z |
| Market best draw last update utc | 2026-10-11T06:31:43Z |
| Market best away last update utc | 2026-10-11T06:31:55Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Juventus |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.1% |
| P btts no | 57.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.92 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.34 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.02 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 23.4% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 42.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.64 |
| Reference draw odds | 3.87 |
| Reference away odds | 5.34 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | -5.1% |
| Draw probability edge | +1.9% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.1015 |
| Raw ev home | -0.1710 |
| Raw edge prob draw | 0.0374 |
| Raw ev draw | 0.1144 |
| Raw edge prob away | 0.0641 |
| Raw ev away | 0.3549 |
| Market p over 1 5 | 74.3% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T06:32:11Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.44 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 74.2% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T06:32:11Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 48.2% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T06:31:43Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 1.80 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **52.0%**. Expected goals are 1.44 for Udinese and 0.82 for Lecce (2.26 combined). The most likely exact score is 1-0 at 15.2%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 39.5%; Under 3.5 goals: 80.7%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 42.6%; BTTS No (at least one team does not score): 57.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 52.0% | 1.92 |
| Draw | 26.2% | 3.81 |
| Lecce win | 21.8% | 4.58 |

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
| Over 2.5 | 39.5% |
| Under 2.5 | 60.5% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.16% |
| 2 | 1-1 | 12.01% |
| 3 | 2-0 | 10.84% |
| 4 | 0-0 | 10.14% |
| 5 | 2-1 | 8.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 52.0% | 52.3% | 1.95 | +1.3% |
| Draw | 26.2% | 25.6% | 3.71 | -2.7% |
| Lecce win | 21.8% | 22.1% | 4.40 | -4.0% |
| Over 2.5 | 39.5% | 49.0% | 2.00 | -20.9% |
| Under 2.5 | 60.5% | 51.0% | 1.94 | +17.3% |

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
| Market best home last update utc | 2026-10-11T06:31:43Z |
| Market best draw last update utc | 2026-10-11T06:31:43Z |
| Market best away last update utc | 2026-10-11T06:31:55Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Tipico |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.6% |
| P btts no | 57.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.86 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.55 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 21.6% |
| Raw p over 1 5 | 65.9% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 42.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.85 |
| Reference draw odds | 3.64 |
| Reference away odds | 4.20 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | -0.4% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | -0.0071 |
| Raw ev home | 0.0061 |
| Raw edge prob draw | 0.0117 |
| Raw ev draw | -0.0054 |
| Raw edge prob away | -0.0046 |
| Raw ev away | -0.0498 |
| Market p over 1 5 | 74.9% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T06:38:24Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 74.3% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T06:38:24Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.45 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 53.7% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T06:37:54Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **37.6%**. Expected goals are 1.13 for Monza and 1.57 for Cagliari (2.70 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 49.5%; Under 3.5 goals: 72.0%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 54.3%; BTTS No (at least one team does not score): 45.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 35.2% | 2.84 |
| Draw | 27.3% | 3.67 |
| Cagliari win | 37.6% | 2.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.13 |
| Cagliari expected goals | 1.57 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 74.5% |
| Under 1.5 | 25.5% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.95% |
| 2 | 1-0 | 9.84% |
| 3 | 2-1 | 8.63% |
| 4 | 0-1 | 8.39% |
| 5 | 1-2 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 35.2% | 43.0% | 2.40 | -15.6% |
| Draw | 27.3% | 29.6% | 3.30 | -10.0% |
| Cagliari win | 37.6% | 27.5% | 3.65 | +37.1% |
| Over 2.5 | 49.5% | 43.5% | 2.13 | +5.4% |
| Under 2.5 | 50.5% | 56.5% | 1.83 | -7.6% |

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
| Market best home last update utc | 2026-10-11T06:31:55Z |
| Market best draw last update utc | 2026-10-11T06:31:55Z |
| Market best away last update utc | 2026-10-11T06:31:23Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Tipico |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.3% |
| P btts no | 45.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.72 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.92 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.59 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 27.4% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 47.7% |
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 53.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.24 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.43 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.61 |
| Home probability edge | -7.8% |
| Draw probability edge | -2.3% |
| Away probability edge | +10.1% |
| Over 2.5 probability edge | +6.0% |
| Under 2.5 probability edge | -6.0% |
| Raw edge prob home | -0.1558 |
| Raw ev home | -0.3430 |
| Raw edge prob draw | -0.0459 |
| Raw ev draw | -0.1759 |
| Raw edge prob away | 0.2017 |
| Raw ev away | 0.7393 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **37.6%**. Expected goals are 1.02 for Parma and 1.08 for Torino (2.10 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 87.5%; Over 2.5 goals: 34.8%; Under 3.5 goals: 83.9%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 42.4%; BTTS No (at least one team does not score): 57.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.8% | 3.15 |
| Draw | 30.7% | 3.26 |
| Torino win | 37.6% | 2.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.02 |
| Torino expected goals | 1.08 |
| Expected total goals | 2.10 |
| Over 0.5 | 87.5% |
| Under 0.5 | 12.5% |
| Over 1.5 | 61.9% |
| Under 1.5 | 38.1% |
| Over 2.5 | 34.8% |
| Under 2.5 | 65.2% |
| Over 3.5 | 16.1% |
| Under 3.5 | 83.9% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.82% |
| 2 | 0-1 | 13.65% |
| 3 | 0-0 | 12.53% |
| 4 | 1-0 | 11.87% |
| 5 | 1-2 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.8% | 29.8% | 3.25 | +3.2% |
| Draw | 30.7% | 31.6% | 3.25 | -0.3% |
| Torino win | 37.6% | 38.6% | 2.54 | -4.6% |
| Over 2.5 | 34.8% | 40.5% | 2.48 | -13.7% |
| Under 2.5 | 65.2% | 59.5% | 1.64 | +7.0% |

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
| Market best home last update utc | 2026-10-11T06:31:43Z |
| Market best draw last update utc | 2026-10-11T06:31:23Z |
| Market best away last update utc | 2026-10-11T06:31:43Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | LeoVegas (SE) |
| Matched home-team name | Parma |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.4% |
| P btts no | 57.6% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 7.98 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.63 |
| Fair Over 2.5 odds | 2.87 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.20 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.24 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 36.5% |
| Raw p over 1 5 | 62.0% |
| Raw p under 3 5 | 83.9% |
| Raw p btts yes | 42.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.18 |
| Reference draw odds | 3.01 |
| Reference away odds | 2.48 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.54 |
| Home probability edge | +2.0% |
| Draw probability edge | -0.9% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | 0.0394 |
| Raw ev home | 0.0964 |
| Raw edge prob draw | -0.0176 |
| Raw ev draw | -0.0317 |
| Raw edge prob away | -0.0218 |
| Raw ev away | -0.0736 |
| Market p over 1 5 | 67.4% |
| Market over 1 5 odds | 1.44 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T06:38:24Z |
| Market reference over 1 5 odds | 1.44 |
| Market reference over 1 5 opposite odds | 2.81 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 80.5% |
| Market under 3 5 odds | 1.20 |
| Best under 3 5 bookmaker | Codere (IT) |
| Market best under 3 5 last update utc | 2026-10-11T06:37:38Z |
| Market reference under 3 5 odds | 1.20 |
| Market reference under 3 5 opposite odds | 3.95 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 49.1% |
| Market btts yes odds | 1.96 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T06:37:54Z |
| Market reference btts yes odds | 1.91 |
| Market reference btts yes opposite odds | 1.85 |
| Market btts yes bookmakers | 2 |

</details>


---
