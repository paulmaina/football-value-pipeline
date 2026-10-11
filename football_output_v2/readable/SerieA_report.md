# Serie A — football model report

Fixtures in this report: **16**.

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
<<<<<<< HEAD
| Live odds matched | 17.00 |
| Additional event odds calls used before this league | 9.00 |
=======
| Live odds matched | 16.00 |
| Additional event odds calls used before this league | 12.00 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 3.00 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
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

## 2026-10-11 — Cagliari vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **58.6%**. Expected goals are 0.80 for Cagliari and 1.48 for Juventus (2.28 combined). The most likely exact score is 0-1 at 16.7%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 40.6%; Under 3.5 goals: 79.9%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 41.9%; BTTS No (at least one team does not score): 58.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 16.5% | 6.08 |
| Draw | 25.0% | 4.01 |
| Juventus win | 58.6% | 1.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 0.80 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 67.0% |
| Under 1.5 | 33.0% |
| Over 2.5 | 40.6% |
| Under 2.5 | 59.4% |
| Over 3.5 | 20.1% |
| Under 3.5 | 79.9% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.67% |
| 2 | 0-2 | 12.32% |
| 3 | 1-1 | 11.43% |
| 4 | 1-2 | 9.81% |
| 5 | 0-0 | 9.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 16.5% | 12.7% | 7.80 | +28.3% |
| Draw | 25.0% | 23.7% | 4.21 | +5.1% |
| Juventus win | 58.6% | 63.6% | 1.58 | -7.4% |
| Over 2.5 | 40.6% | 48.8% | 2.06 | -16.4% |
| Under 2.5 | 59.4% | 51.2% | 1.93 | +14.7% |

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
| Market best home last update utc | 2026-10-11T10:49:19Z |
| Market best draw last update utc | 2026-10-11T10:48:59Z |
| Market best away last update utc | 2026-10-11T10:48:59Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Cagliari |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.9% |
| P btts no | 58.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.35 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.03 |
| Fair Over 2.5 odds | 2.46 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 4.98 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.92 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 53.6% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.3% |
| Raw p btts yes | 42.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
<<<<<<< HEAD
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
| Market p over 1 5 | 73.8% |
| Market over 1 5 odds | 1.35 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:51:09Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.52 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 73.9% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:51:23Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.55 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 46.3% |
| Market btts yes odds | 2.14 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:51:40Z |
| Market reference btts yes odds | 2.14 |
| Market reference btts yes opposite odds | 1.85 |
| Market btts yes bookmakers | 4 |

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
=======
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 7.80 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.57 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | +3.7% |
| Draw probability edge | +1.3% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -8.3% |
| Under 2.5 probability edge | +8.3% |
| Raw edge prob home | 0.0746 |
| Raw ev home | 0.5742 |
| Raw edge prob draw | 0.0256 |
| Raw ev draw | 0.1051 |
| Raw edge prob away | -0.1002 |
| Raw ev away | -0.1536 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-11 — Lazio vs Monza

The model's most likely 1X2 outcome is **Lazio win** at **59.9%**. Expected goals are 2.01 for Lazio and 0.87 for Monza (2.88 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.0%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 59.9% | 1.67 |
| Draw | 22.7% | 4.41 |
| Monza win | 17.4% | 5.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 2.01 |
| Monza expected goals | 0.87 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 53.8% |
| Under 2.5 | 46.2% |
| Over 3.5 | 32.0% |
| Under 3.5 | 68.0% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.77% |
| 2 | 2-0 | 10.64% |
| 3 | 1-0 | 10.63% |
| 4 | 2-1 | 9.21% |
| 5 | 3-0 | 7.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 59.9% | 55.7% | 1.80 | +7.9% |
| Draw | 22.7% | 24.8% | 4.02 | -8.9% |
| Monza win | 17.4% | 19.5% | 5.10 | -11.2% |
| Over 2.5 | 53.8% | 51.9% | 1.83 | -1.5% |
| Under 2.5 | 46.2% | 48.1% | 2.20 | +1.6% |

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
| Market best home last update utc | 2026-10-11T10:49:15Z |
| Market best draw last update utc | 2026-10-11T10:49:14Z |
| Market best away last update utc | 2026-10-11T10:49:19Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Matchbook |
| Best draw bookmaker | GTbets |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | LeoVegas (SE) |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Lazio |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.23 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.13 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.26 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 64.1% |
| Unadjusted draw probability | 20.5% |
| Unadjusted away-win probability | 15.4% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 67.5% |
| Raw p btts yes | 50.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.79 |
| Reference draw odds | 4.00 |
| Reference away odds | 5.10 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | +4.2% |
| Draw probability edge | -2.2% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | 0.0842 |
| Raw ev home | 0.1543 |
| Raw edge prob draw | -0.0433 |
| Raw ev draw | -0.1756 |
| Raw edge prob away | -0.0409 |
| Raw ev away | -0.2164 |

</details>


---

## 2026-10-11 — Lecce vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **48.6%**. Expected goals are 0.78 for Lecce and 1.33 for Bologna (2.11 combined). The most likely exact score is 0-1 at 15.8%. Goal-market probabilities: at least one goal: 87.7%; Over 2.5 goals: 35.1%; Under 3.5 goals: 83.7%; Under 4.5 goals: 93.7%; BTTS Yes (both teams score): 40.0%; BTTS No (at least one team does not score): 60.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 22.5% | 4.44 |
| Draw | 28.9% | 3.46 |
| Bologna win | 48.6% | 2.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.78 |
| Bologna expected goals | 1.33 |
| Expected total goals | 2.11 |
| Over 0.5 | 87.7% |
| Under 0.5 | 12.3% |
| Over 1.5 | 62.2% |
| Under 1.5 | 37.8% |
| Over 2.5 | 35.1% |
| Under 2.5 | 64.9% |
| Over 3.5 | 16.3% |
| Under 3.5 | 83.7% |
| Over 4.5 | 6.3% |
| Under 4.5 | 93.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.78% |
| 2 | 1-1 | 12.82% |
| 3 | 0-0 | 12.32% |
| 4 | 0-2 | 10.46% |
| 5 | 1-0 | 9.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 22.5% | 23.0% | 4.30 | -3.2% |
| Draw | 28.9% | 29.6% | 3.38 | -2.3% |
| Bologna win | 48.6% | 47.4% | 2.10 | +2.0% |
| Over 2.5 | 35.1% | 43.3% | 2.26 | -20.6% |
| Under 2.5 | 64.9% | 56.7% | 1.78 | +15.5% |

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
| Market best home last update utc | 2026-10-11T10:49:19Z |
| Market best draw last update utc | 2026-10-11T10:49:14Z |
| Market best away last update utc | 2026-10-11T10:49:19Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | GTbets |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Lecce |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 40.0% |
| P btts no | 60.0% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.12 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.64 |
| Fair Over 2.5 odds | 2.85 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.14 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 15.94 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 22.0% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 62.3% |
| Raw p under 3 5 | 83.6% |
| Raw p btts yes | 39.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 4.30 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.68 |
| Home probability edge | -0.5% |
| Draw probability edge | -0.7% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -8.2% |
| Under 2.5 probability edge | +8.2% |
| Raw edge prob home | -0.0101 |
| Raw ev home | -0.0535 |
| Raw edge prob draw | -0.0139 |
| Raw ev draw | -0.0466 |
| Raw edge prob away | 0.0240 |
| Raw ev away | 0.0454 |
| Market p over 1 5 | 69.1% |
| Market over 1 5 odds | 1.42 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T10:49:14Z |
| Market reference over 1 5 odds | 1.42 |
| Market reference over 1 5 opposite odds | 3.05 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 78.3% |
| Market under 3 5 odds | 1.26 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T10:49:14Z |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 4.25 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 50.4% |
| Market btts yes odds | 1.97 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T10:49:15Z |
| Market reference btts yes odds | 1.97 |
| Market reference btts yes opposite odds | 2.00 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Sassuolo vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **51.5%**. Expected goals are 1.13 for Sassuolo and 1.68 for AC Milan (2.81 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 53.1%; Under 3.5 goals: 68.8%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 23.6% | 4.23 |
| Draw | 24.9% | 4.01 |
| AC Milan win | 51.5% | 1.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.13 |
| AC Milan expected goals | 1.68 |
| Expected total goals | 2.81 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 53.1% |
| Under 2.5 | 46.9% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.79% |
| 2 | 0-1 | 10.38% |
| 3 | 1-2 | 9.81% |
| 4 | 0-2 | 8.69% |
| 5 | 1-0 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 23.6% | 21.6% | 4.60 | +8.6% |
| Draw | 24.9% | 25.9% | 3.94 | -1.8% |
| AC Milan win | 51.5% | 52.5% | 1.90 | -2.2% |
| Over 2.5 | 53.1% | 54.4% | 1.75 | -7.0% |
| Under 2.5 | 46.9% | 45.6% | 2.27 | +6.4% |

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
| Market best home last update utc | 2026-10-11T10:49:19Z |
| Market best draw last update utc | 2026-10-11T10:48:59Z |
| Market best away last update utc | 2026-10-11T10:49:19Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Unibet (SE) |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sassuolo |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.3% |
| P btts no | 44.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.22 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.13 |
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
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 4.60 |
| Reference draw odds | 3.85 |
| Reference away odds | 1.90 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.06 |
| Home probability edge | +2.0% |
| Draw probability edge | -0.9% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -1.3% |
| Under 2.5 probability edge | +1.3% |
| Raw edge prob home | 0.0398 |
| Raw ev home | 0.1778 |
| Raw edge prob draw | -0.0185 |
| Raw ev draw | -0.0541 |
| Raw edge prob away | -0.0213 |
| Raw ev away | -0.0426 |

</details>


---

## 2026-10-12 — Atalanta BC vs Venezia

The model's most likely 1X2 outcome is **Atalanta BC win** at **68.4%**. Expected goals are 2.35 for Atalanta BC and 0.66 for Venezia (3.02 combined). The most likely exact score is 2-0 at 12.4%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 56.0%; Under 3.5 goals: 65.8%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 45.1%; BTTS No (at least one team does not score): 54.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 68.4% | 1.46 |
| Draw | 19.2% | 5.20 |
| Venezia win | 12.3% | 8.12 |

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
| Over 3.5 | 34.2% |
| Under 3.5 | 65.8% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.35% |
| 2 | 1-0 | 10.53% |
| 3 | 3-0 | 9.70% |
| 4 | 1-1 | 9.14% |
| 5 | 2-1 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 68.4% | 61.5% | 1.63 | +11.6% |
| Draw | 19.2% | 22.5% | 4.40 | -15.3% |
| Venezia win | 12.3% | 15.9% | 6.20 | -23.7% |
| Over 2.5 | 56.0% | 62.4% | 1.55 | -13.3% |
| Under 2.5 | 44.0% | 37.6% | 2.48 | +9.2% |

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
| Market best home last update utc | 2026-10-11T10:48:59Z |
| Market best draw last update utc | 2026-10-11T10:48:58Z |
| Market best away last update utc | 2026-10-11T10:49:19Z |
| Odds bookmakers 1x2 | 23.00 |
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
| Fair Under 0.5 odds | 17.07 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.75 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.66 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 75.3% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 8.7% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 64.4% |
| Raw p btts yes | 43.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.62 |
| Reference draw odds | 4.40 |
| Reference away odds | 6.20 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Home probability edge | +6.9% |
| Draw probability edge | -3.3% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.1380 |
| Raw ev home | 0.2280 |
| Raw edge prob draw | -0.0654 |
| Raw ev draw | -0.2971 |
| Raw edge prob away | -0.0726 |
| Raw ev away | -0.4615 |
| Market p over 1 5 | 83.1% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:51:09Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 60.9% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T08:51:09Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.43 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 58.3% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:51:40Z |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.34 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-12 — Torino vs Udinese

The model's most likely 1X2 outcome is **Torino win** at **37.9%**. Expected goals are 1.29 for Torino and 1.35 for Udinese (2.64 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.4%; Under 3.5 goals: 72.8%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 54.2%; BTTS No (at least one team does not score): 45.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 37.9% | 2.64 |
| Draw | 28.2% | 3.55 |
| Udinese win | 33.9% | 2.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.29 |
| Udinese expected goals | 1.35 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.4% |
| Under 2.5 | 51.6% |
| Over 3.5 | 27.2% |
| Under 3.5 | 72.8% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.39% |
| 2 | 1-0 | 9.88% |
| 3 | 0-1 | 8.57% |
| 4 | 2-1 | 8.54% |
| 5 | 0-0 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 37.9% | 40.2% | 2.46 | -6.7% |
| Draw | 28.2% | 30.3% | 3.35 | -5.6% |
| Udinese win | 33.9% | 29.4% | 3.35 | +13.5% |
| Over 2.5 | 48.4% | 44.8% | 2.24 | +8.5% |
| Under 2.5 | 51.6% | 55.2% | 1.79 | -7.7% |

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
| Market best home last update utc | 2026-10-11T10:49:19Z |
| Market best draw last update utc | 2026-10-11T10:48:59Z |
| Market best away last update utc | 2026-10-11T10:48:59Z |
| Odds bookmakers 1x2 | 23.00 |
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
| P btts yes | 54.2% |
| P btts no | 45.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.05 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.68 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.96 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 38.3% |
| Raw p over 1 5 | 73.9% |
| Raw p under 3 5 | 72.7% |
| Raw p btts yes | 53.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.46 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.73 |
| Home probability edge | -2.3% |
| Draw probability edge | -2.2% |
| Away probability edge | +4.4% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Raw edge prob home | -0.0456 |
| Raw ev home | -0.1228 |
| Raw edge prob draw | -0.0433 |
| Raw ev draw | -0.1285 |
| Raw edge prob away | 0.0890 |
| Raw ev away | 0.2839 |

</details>


---

## 2026-10-16 — Frosinone vs Sassuolo

The model's most likely 1X2 outcome is **Frosinone win** at **47.2%**. Expected goals are 1.84 for Frosinone and 1.12 for Sassuolo (2.95 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.4%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 47.2% | 2.12 |
| Draw | 23.8% | 4.20 |
| Sassuolo win | 28.9% | 3.46 |

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
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.17% |
| 2 | 2-1 | 8.56% |
| 3 | 1-0 | 8.40% |
| 4 | 2-0 | 7.66% |
| 5 | 1-2 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 47.2% | 40.2% | 2.53 | +19.5% |
| Draw | 23.8% | 25.0% | 3.80 | -9.4% |
| Sassuolo win | 28.9% | 34.8% | 2.96 | -14.4% |
| Over 2.5 | 55.9% | 59.2% | 1.62 | -9.5% |
| Under 2.5 | 44.1% | 40.8% | 2.61 | +15.2% |

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
| Market best home last update utc | 2026-10-11T10:48:59Z |
| Market best draw last update utc | 2026-10-11T10:49:19Z |
| Market best away last update utc | 2026-10-11T10:48:59Z |
| Odds bookmakers 1x2 | 19.00 |
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
| Fair Under 0.5 odds | 18.45 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.71 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.98 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.80 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.3% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 79.3% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.40 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.76 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +7.0% |
| Draw probability edge | -1.1% |
| Away probability edge | -5.9% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | 0.1401 |
| Raw ev home | 0.3726 |
| Raw edge prob draw | -0.0224 |
| Raw ev draw | -0.1367 |
| Raw edge prob away | -0.1177 |
| Raw ev away | -0.3183 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **71.7%**. Expected goals are 2.01 for AS Roma and 0.66 for Genoa (2.67 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 50.6%; Under 3.5 goals: 71.7%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 41.3%; BTTS No (at least one team does not score): 58.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 71.7% | 1.39 |
| Draw | 18.1% | 5.52 |
| Genoa win | 10.2% | 9.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 2.01 |
| Genoa expected goals | 0.66 |
| Expected total goals | 2.67 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 74.9% |
| Under 1.5 | 25.1% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 28.3% |
| Under 3.5 | 71.7% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.50% |
| 2 | 2-0 | 14.49% |
| 3 | 3-0 | 9.69% |
| 4 | 2-1 | 9.59% |
| 5 | 1-1 | 8.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 71.7% | 74.3% | 1.36 | -2.5% |
| Draw | 18.1% | 16.6% | 5.70 | +3.2% |
| Genoa win | 10.2% | 9.1% | 10.50 | +7.0% |
| Over 2.5 | 50.6% | 58.2% | 1.72 | -12.9% |
| Under 2.5 | 49.4% | 41.8% | 2.31 | +14.1% |

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
| Market best home last update utc | 2026-10-11T10:48:59Z |
| Market best draw last update utc | 2026-10-11T10:49:13Z |
| Market best away last update utc | 2026-10-11T10:49:13Z |
| Odds bookmakers 1x2 | 19.00 |
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
| P btts yes | 41.3% |
| P btts no | 58.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.71 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 3.99 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.53 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.39 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 11.3% |
| Raw p over 1 5 | 74.5% |
| Raw p under 3 5 | 72.1% |
| Raw p btts yes | 41.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.33 |
| Reference draw odds | 5.60 |
| Reference away odds | 10.00 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | -2.6% |
| Draw probability edge | +1.5% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | -0.0520 |
| Raw ev home | -0.0603 |
| Raw edge prob draw | 0.0298 |
| Raw ev draw | 0.1172 |
| Raw edge prob away | 0.0222 |
| Raw ev away | 0.1866 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.0%**. Expected goals are 1.07 for Bologna and 2.13 for Inter Milan (3.21 combined). The most likely exact score is 1-1 at 9.9%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.2%; Under 4.5 goals: 78.2%; BTTS Yes (both teams score): 58.3%; BTTS No (at least one team does not score): 41.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.5% | 5.71 |
| Draw | 21.5% | 4.66 |
| Inter Milan win | 61.0% | 1.64 |

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
| Over 2.5 | 61.7% |
| Under 2.5 | 38.3% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.8% |
| Under 4.5 | 78.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.86% |
| 2 | 1-2 | 9.79% |
| 3 | 0-2 | 9.12% |
| 4 | 0-1 | 8.60% |
| 5 | 1-3 | 6.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.5% | 16.8% | 5.70 | -0.1% |
| Draw | 21.5% | 22.8% | 4.20 | -9.8% |
| Inter Milan win | 61.0% | 60.4% | 1.69 | +3.1% |
| Over 2.5 | 61.7% | 58.7% | 1.72 | +6.1% |
| Under 2.5 | 38.3% | 41.3% | 2.30 | -11.9% |

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
| Market best home last update utc | 2026-10-11T10:49:13Z |
| Market best draw last update utc | 2026-10-11T10:49:13Z |
| Market best away last update utc | 2026-10-11T10:48:59Z |
| Odds bookmakers 1x2 | 19.00 |
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
| P btts yes | 58.3% |
| P btts no | 41.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.38 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.85 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.58 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 61.7% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 57.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 5.50 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.62 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +0.7% |
| Draw probability edge | -1.4% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | +2.9% |
| Under 2.5 probability edge | -2.9% |
| Raw edge prob home | 0.0145 |
| Raw ev home | 0.0399 |
| Raw edge prob draw | -0.0275 |
| Raw ev draw | -0.1562 |
| Raw edge prob away | 0.0130 |
| Raw ev away | 0.0421 |
<<<<<<< HEAD
=======
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T10:48:42Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 64.4% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T10:49:13Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.59 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T10:49:16Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.22 |
| Market btts yes bookmakers | 4 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **64.0%**. Expected goals are 0.67 for Venezia and 2.18 for Napoli (2.85 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 52.1%; Under 3.5 goals: 69.7%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 44.5%; BTTS No (at least one team does not score): 55.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 15.3% | 6.54 |
| Draw | 20.7% | 4.82 |
| Napoli win | 64.0% | 1.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.18 |
| Expected total goals | 2.85 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 76.1% |
| Under 1.5 | 23.9% |
| Over 2.5 | 52.1% |
| Under 2.5 | 47.9% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.20% |
| 2 | 0-1 | 11.26% |
| 3 | 1-1 | 9.80% |
| 4 | 0-3 | 8.85% |
| 5 | 1-2 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 15.3% | 20.5% | 4.90 | -25.1% |
| Draw | 20.7% | 23.7% | 4.22 | -12.5% |
| Napoli win | 64.0% | 55.9% | 1.76 | +12.6% |
| Over 2.5 | 52.1% | 56.0% | 1.75 | -8.8% |
| Under 2.5 | 47.9% | 44.0% | 2.25 | +7.8% |

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
| Market best home last update utc | 2026-10-11T10:49:14Z |
| Market best draw last update utc | 2026-10-11T10:48:59Z |
| Market best away last update utc | 2026-10-11T10:48:59Z |
| Odds bookmakers 1x2 | 19.00 |
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
| P btts yes | 44.5% |
| P btts no | 55.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.91 |
| Fair Over 1.5 odds | 1.31 |
<<<<<<< HEAD
| Fair Under 1.5 odds | 4.22 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.27 |
=======
| Fair Under 1.5 odds | 4.18 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.30 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.68 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 72.1% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 43.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 4.60 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.75 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -5.2% |
| Draw probability edge | -2.9% |
| Away probability edge | +8.1% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.1034 |
| Raw ev home | -0.5043 |
| Raw edge prob draw | -0.0583 |
| Raw ev draw | -0.2477 |
| Raw edge prob away | 0.1617 |
| Raw ev away | 0.2682 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **45.5%**. Expected goals are 1.28 for AC Milan and 1.16 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 44.4%; Under 3.5 goals: 76.9%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 49.3%; BTTS No (at least one team does not score): 50.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 45.5% | 2.20 |
| Draw | 26.5% | 3.77 |
| Atalanta BC win | 28.0% | 3.57 |

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
| 1 | 1-0 | 12.97% |
| 2 | 1-1 | 12.55% |
| 3 | 2-1 | 9.57% |
| 4 | 0-1 | 8.52% |
| 5 | 0-0 | 8.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 45.5% | 51.5% | 1.93 | -12.2% |
| Draw | 26.5% | 25.8% | 3.86 | +2.3% |
| Atalanta BC win | 28.0% | 22.7% | 4.30 | +20.4% |
| Over 2.5 | 44.4% | 55.4% | 1.83 | -18.8% |
| Under 2.5 | 55.6% | 44.6% | 2.13 | +18.5% |

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
| Market best home last update utc | 2026-10-11T10:48:59Z |
| Market best draw last update utc | 2026-10-11T10:48:59Z |
| Market best away last update utc | 2026-10-11T10:49:13Z |
| Odds bookmakers 1x2 | 17.00 |
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
| P btts yes | 49.3% |
| P btts no | 50.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.86 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.81 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 33.3% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.90 |
| Reference draw odds | 3.70 |
| Reference away odds | 4.20 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -6.0% |
| Draw probability edge | +0.7% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | -11.1% |
| Under 2.5 probability edge | +11.1% |
| Raw edge prob home | -0.1200 |
| Raw ev home | -0.2379 |
| Raw edge prob draw | 0.0134 |
| Raw ev draw | 0.0493 |
| Raw edge prob away | 0.1066 |
| Raw ev away | 0.4332 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.6%**. Expected goals are 1.00 for Fiorentina and 1.73 for Como (2.73 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.1%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 52.2%; BTTS No (at least one team does not score): 47.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 25.2% | 3.97 |
| Draw | 24.2% | 4.13 |
| Como win | 50.6% | 1.98 |

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
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.51% |
| 2 | 0-1 | 10.50% |
| 3 | 0-2 | 9.04% |
| 4 | 1-2 | 9.03% |
| 5 | 1-0 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 25.2% | 28.7% | 3.65 | -8.0% |
| Draw | 24.2% | 24.8% | 3.85 | -6.8% |
| Como win | 50.6% | 46.5% | 2.13 | +7.7% |
| Over 2.5 | 50.9% | 56.7% | 1.73 | -11.9% |
| Under 2.5 | 49.1% | 43.3% | 2.29 | +12.3% |

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
| Market best home last update utc | 2026-10-11T10:49:13Z |
| Market best draw last update utc | 2026-10-11T10:49:19Z |
| Market best away last update utc | 2026-10-11T10:48:59Z |
| Odds bookmakers 1x2 | 17.00 |
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
| Fair Under 0.5 odds | 15.09 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.04 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.17 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 21.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 51.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.35 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -3.5% |
| Draw probability edge | -0.6% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0693 |
| Raw ev home | -0.2061 |
| Raw edge prob draw | -0.0126 |
| Raw ev draw | -0.0919 |
| Raw edge prob away | 0.0819 |
| Raw ev away | 0.1643 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **54.1%**. Expected goals are 1.37 for Juventus and 0.85 for Lazio (2.22 combined). The most likely exact score is 1-0 at 16.5%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 38.9%; Under 3.5 goals: 81.3%; Under 4.5 goals: 92.3%; BTTS Yes (both teams score): 42.1%; BTTS No (at least one team does not score): 57.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 54.1% | 1.85 |
| Draw | 26.0% | 3.84 |
| Lazio win | 19.8% | 5.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.85 |
| Expected total goals | 2.22 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 38.9% |
| Under 2.5 | 61.1% |
| Over 3.5 | 18.7% |
| Under 3.5 | 81.3% |
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.51% |
| 2 | 1-1 | 11.88% |
| 3 | 2-0 | 11.24% |
| 4 | 0-0 | 10.21% |
| 5 | 2-1 | 9.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 54.1% | 59.2% | 1.69 | -8.5% |
| Draw | 26.0% | 24.5% | 4.04 | +5.2% |
| Lazio win | 19.8% | 16.3% | 5.80 | +14.9% |
| Over 2.5 | 38.9% | 48.8% | 2.03 | -21.0% |
| Under 2.5 | 61.1% | 51.2% | 1.92 | +17.3% |

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
| Market best home last update utc | 2026-10-11T10:48:59Z |
| Market best draw last update utc | 2026-10-11T10:48:59Z |
| Market best away last update utc | 2026-10-11T10:49:19Z |
| Odds bookmakers 1x2 | 17.00 |
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
| P btts yes | 42.1% |
| P btts no | 57.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.80 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.34 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.05 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 23.4% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 42.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.66 |
| Reference draw odds | 3.90 |
| Reference away odds | 5.80 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | -5.1% |
| Draw probability edge | +1.5% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | -0.1018 |
| Raw ev home | -0.1710 |
| Raw edge prob draw | 0.0308 |
| Raw ev draw | 0.1144 |
| Raw edge prob away | 0.0710 |
| Raw ev away | 0.3549 |
<<<<<<< HEAD
=======
| Market p over 1 5 | 75.5% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T10:49:13Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.30 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 75.5% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T10:49:13Z |
| Market reference under 3 5 odds | 1.27 |
| Market reference under 3 5 opposite odds | 3.30 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 48.2% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T10:48:59Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 1.80 |
| Market btts yes bookmakers | 2 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.8%**. Expected goals are 1.44 for Udinese and 0.82 for Lecce (2.26 combined). The most likely exact score is 1-0 at 15.1%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 39.5%; Under 3.5 goals: 80.7%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.6%; BTTS No (at least one team does not score): 57.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.8% | 1.93 |
| Draw | 26.4% | 3.78 |
| Lecce win | 21.8% | 4.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.44 |
| Lecce expected goals | 0.82 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.5% |
| Under 2.5 | 60.5% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.10% |
| 2 | 1-1 | 12.11% |
| 3 | 2-0 | 10.80% |
| 4 | 0-0 | 10.22% |
| 5 | 2-1 | 8.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.8% | 51.9% | 1.95 | +0.9% |
| Draw | 26.4% | 26.1% | 3.71 | -1.9% |
| Lecce win | 21.8% | 22.0% | 4.40 | -4.1% |
| Over 2.5 | 39.5% | 48.4% | 2.00 | -21.1% |
| Under 2.5 | 60.5% | 51.6% | 1.94 | +17.5% |

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
| Market best home last update utc | 2026-10-11T10:48:59Z |
| Market best draw last update utc | 2026-10-11T10:48:59Z |
| Market best away last update utc | 2026-10-11T10:49:13Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.6% |
| P btts no | 57.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.78 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.19 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.58 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 21.6% |
| Raw p over 1 5 | 65.9% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 42.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.88 |
| Reference draw odds | 3.65 |
| Reference away odds | 4.30 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.94 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | -0.2% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | -0.0033 |
| Raw ev home | 0.0061 |
| Raw edge prob draw | 0.0073 |
| Raw ev draw | -0.0054 |
| Raw edge prob away | -0.0040 |
| Raw ev away | -0.0498 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **38.1%**. Expected goals are 1.13 for Monza and 1.57 for Cagliari (2.70 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.4%; Under 3.5 goals: 72.0%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 34.1% | 2.93 |
| Draw | 27.7% | 3.61 |
| Cagliari win | 38.1% | 2.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.13 |
| Cagliari expected goals | 1.57 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.5% |
| Under 1.5 | 25.5% |
| Over 2.5 | 49.4% |
| Under 2.5 | 50.6% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.17% |
| 2 | 1-0 | 9.55% |
| 3 | 0-1 | 8.52% |
| 4 | 2-1 | 8.38% |
| 5 | 1-2 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 34.1% | 40.9% | 2.40 | -18.1% |
| Draw | 27.7% | 30.5% | 3.30 | -8.5% |
| Cagliari win | 38.1% | 28.6% | 3.65 | +39.2% |
| Over 2.5 | 49.4% | 44.2% | 2.13 | +5.1% |
| Under 2.5 | 50.6% | 55.8% | 1.83 | -7.3% |

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
| Market best home last update utc | 2026-10-11T10:49:19Z |
| Market best draw last update utc | 2026-10-11T10:49:13Z |
| Market best away last update utc | 2026-10-11T10:49:13Z |
| Odds bookmakers 1x2 | 17.00 |
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
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.50 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.92 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.61 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 27.4% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 47.7% |
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 53.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.40 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.71 |
| Home probability edge | -6.8% |
| Draw probability edge | -2.8% |
| Away probability edge | +9.5% |
| Over 2.5 probability edge | +5.2% |
| Under 2.5 probability edge | -5.2% |
| Raw edge prob home | -0.1351 |
| Raw ev home | -0.3430 |
| Raw edge prob draw | -0.0550 |
| Raw ev draw | -0.1759 |
| Raw edge prob away | 0.1901 |
| Raw ev away | 0.7393 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.0%**. Expected goals are 1.02 for Parma and 1.08 for Torino (2.10 combined). The most likely exact score is 0-1 at 13.8%. Goal-market probabilities: at least one goal: 87.6%; Over 2.5 goals: 34.9%; Under 3.5 goals: 83.9%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 42.3%; BTTS No (at least one team does not score): 57.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.7% | 3.15 |
| Draw | 30.3% | 3.30 |
| Torino win | 38.0% | 2.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.02 |
| Torino expected goals | 1.08 |
| Expected total goals | 2.10 |
| Over 0.5 | 87.6% |
| Under 0.5 | 12.4% |
| Over 1.5 | 62.0% |
| Under 1.5 | 38.0% |
| Over 2.5 | 34.9% |
| Under 2.5 | 65.1% |
| Over 3.5 | 16.1% |
| Under 3.5 | 83.9% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.80% |
| 2 | 1-1 | 13.64% |
| 3 | 0-0 | 12.37% |
| 4 | 1-0 | 11.86% |
| 5 | 1-2 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.7% | 29.8% | 3.25 | +3.2% |
| Draw | 30.3% | 30.8% | 3.25 | -1.6% |
| Torino win | 38.0% | 39.5% | 2.54 | -3.5% |
| Over 2.5 | 34.9% | 40.5% | 2.48 | -13.4% |
| Under 2.5 | 65.1% | 59.5% | 1.64 | +6.8% |

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
| Market best home last update utc | 2026-10-11T10:48:59Z |
| Market best draw last update utc | 2026-10-11T10:49:13Z |
| Market best away last update utc | 2026-10-11T10:48:59Z |
| Odds bookmakers 1x2 | 17.00 |
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
| P btts yes | 42.3% |
| P btts no | 57.7% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.08 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.63 |
| Fair Over 2.5 odds | 2.86 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.20 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.17 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 36.5% |
| Raw p over 1 5 | 62.0% |
| Raw p under 3 5 | 83.9% |
| Raw p btts yes | 42.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.20 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.44 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.32 |
| Reference Under 2.5 odds | 1.62 |
| Home probability edge | +2.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | 0.0397 |
| Raw ev home | 0.0964 |
| Raw edge prob draw | -0.0097 |
| Raw ev draw | -0.0317 |
| Raw edge prob away | -0.0301 |
| Raw ev away | -0.0736 |
<<<<<<< HEAD
=======
| Market p over 1 5 | 67.4% |
| Market over 1 5 odds | 1.44 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T10:49:13Z |
| Market reference over 1 5 odds | 1.44 |
| Market reference over 1 5 opposite odds | 2.81 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 80.5% |
| Market under 3 5 odds | 1.20 |
| Best under 3 5 bookmaker | Codere (IT) |
| Market best under 3 5 last update utc | 2026-10-11T10:49:00Z |
| Market reference under 3 5 odds | 1.20 |
| Market reference under 3 5 opposite odds | 3.95 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 47.2% |
| Market btts yes odds | 1.96 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T10:48:59Z |
| Market reference btts yes odds | 1.96 |
| Market reference btts yes opposite odds | 1.77 |
| Market btts yes bookmakers | 2 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---
