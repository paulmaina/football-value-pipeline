# Premier League — football model report

Fixtures in this report: **14**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,190 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 365 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1333.746 |
| Base scoring parameter | 0.174 |
| Home-advantage parameter | 0.164 |
| Dixon-Coles low-score adjustment | -0.105 |
| Xi per day | 0.0019 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 14.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
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

## 2026-10-11 — Crystal Palace vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **35.9%**. Expected goals are 1.25 for Crystal Palace and 1.23 for Nottingham Forest (2.48 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.2%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 35.1% | 2.85 |
| Draw | 29.0% | 3.45 |
| Nottingham Forest win | 35.9% | 2.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.25 |
| Nottingham Forest expected goals | 1.23 |
| Expected total goals | 2.48 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 72.2% |
| Under 1.5 | 27.8% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 23.8% |
| Under 3.5 | 76.2% |
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.81% |
| 2 | 0-0 | 9.47% |
| 3 | 0-1 | 9.30% |
| 4 | 1-0 | 9.04% |
| 5 | 1-2 | 8.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 35.1% | 34.8% | 2.94 | +3.2% |
| Draw | 29.0% | 28.1% | 3.45 | -0.0% |
| Nottingham Forest win | 35.9% | 37.1% | 2.68 | -3.8% |
| Over 2.5 | 45.3% | 49.4% | 1.96 | -11.1% |
| Under 2.5 | 54.7% | 50.6% | 2.02 | +10.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | 86effab5c6e7bfd58c8e88b1fb7c6ba9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:54Z |
| Market best draw last update utc | 2026-10-11T10:48:54Z |
| Market best away last update utc | 2026-10-11T10:48:54Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.56 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.60 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.20 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.38 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 35.4% |
| Unadjusted draw probability | 29.9% |
| Unadjusted away-win probability | 34.7% |
| Raw p over 1 5 | 72.1% |
| Raw p under 3 5 | 76.3% |
| Raw p btts yes | 51.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.63 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.87 |
| Home probability edge | +0.3% |
| Draw probability edge | +0.9% |
<<<<<<< HEAD
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | 0.0089 |
| Raw ev home | 0.0345 |
| Raw edge prob draw | 0.0178 |
| Raw ev draw | 0.0448 |
| Raw edge prob away | -0.0267 |
| Raw ev away | -0.0625 |
| Market p over 1 5 | 75.3% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:47:23Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 71.1% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:49:14Z |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 2.90 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 56.4% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:49:14Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 5 |
=======
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | 0.0063 |
| Raw ev home | 0.0416 |
| Raw edge prob draw | 0.0176 |
| Raw ev draw | 0.0299 |
| Raw edge prob away | -0.0239 |
| Raw ev away | -0.0695 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-11 — Hull City vs Everton

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Hull City win** at **35.0%**. Expected goals are 1.09 for Hull City and 0.66 for Everton (1.74 combined). The most likely exact score is 0-0 at 16.9%. Goal-market probabilities: at least one goal: 83.1%; Over 2.5 goals: 26.0%; Under 3.5 goals: 90.3%; Under 4.5 goals: 96.7%; BTTS Yes (both teams score): 32.8%; BTTS No (at least one team does not score): 67.2%.
=======
The model's most likely 1X2 outcome is **Hull City win** at **34.7%**. Expected goals are 1.09 for Hull City and 0.66 for Everton (1.74 combined). The most likely exact score is 0-0 at 16.9%. Goal-market probabilities: at least one goal: 83.1%; Over 2.5 goals: 26.0%; Under 3.5 goals: 90.3%; Under 4.5 goals: 96.7%; BTTS Yes (both teams score): 32.9%; BTTS No (at least one team does not score): 67.1%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 34.7% | 2.88 |
| Draw | 31.6% | 3.17 |
| Everton win | 33.8% | 2.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.09 |
| Everton expected goals | 0.66 |
| Expected total goals | 1.74 |
| Over 0.5 | 83.1% |
| Under 0.5 | 16.9% |
| Over 1.5 | 52.6% |
| Under 1.5 | 47.4% |
| Over 2.5 | 26.0% |
| Under 2.5 | 74.0% |
| Over 3.5 | 9.7% |
| Under 3.5 | 90.3% |
| Over 4.5 | 3.3% |
| Under 4.5 | 96.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 0-0 | 16.94% |
| 2 | 0-1 | 16.43% |
| 3 | 1-0 | 13.98% |
=======
| 1 | 0-0 | 16.93% |
| 2 | 0-1 | 16.57% |
| 3 | 1-0 | 13.85% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| 4 | 1-1 | 12.45% |
| 5 | 2-0 | 8.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Hull City win | 35.0% | 25.7% | 3.95 | +38.1% |
| Draw | 31.6% | 28.1% | 3.52 | +11.1% |
| Everton win | 33.5% | 46.2% | 2.18 | -27.1% |
| Over 2.5 | 26.0% | 47.0% | 2.14 | -44.5% |
| Under 2.5 | 74.0% | 53.0% | 1.89 | +39.9% |
=======
| Hull City win | 34.7% | 25.1% | 4.00 | +38.7% |
| Draw | 31.6% | 28.1% | 3.48 | +9.8% |
| Everton win | 33.8% | 46.8% | 2.16 | -27.1% |
| Over 2.5 | 26.0% | 47.1% | 2.20 | -42.9% |
| Under 2.5 | 74.0% | 52.9% | 1.82 | +34.7% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | 0bdae4d304810578e47386606bff7106 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:54Z |
| Market best draw last update utc | 2026-10-11T10:48:21Z |
| Market best away last update utc | 2026-10-11T10:48:21Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Hull |
| Matched away-team name | Everton |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.8% |
| P btts no | 67.2% |
| Fair Over 0.5 odds | 1.20 |
| Fair Under 0.5 odds | 5.91 |
| Fair Over 1.5 odds | 1.90 |
| Fair Under 1.5 odds | 2.11 |
| Fair Over 2.5 odds | 3.85 |
| Fair Under 2.5 odds | 1.35 |
| Fair Over 3.5 odds | 10.33 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.74 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 44.2% |
| Unadjusted draw probability | 35.0% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 53.3% |
| Raw p under 3 5 | 90.0% |
| Raw p btts yes | 33.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 3.85 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.80 |
| Home probability edge | +9.5% |
| Draw probability edge | +3.4% |
<<<<<<< HEAD
| Away probability edge | -12.7% |
| Over 2.5 probability edge | -21.1% |
| Under 2.5 probability edge | +21.1% |
| Raw edge prob home | 0.1852 |
| Raw ev home | 0.7472 |
| Raw edge prob draw | 0.0687 |
| Raw ev draw | 0.2322 |
| Raw edge prob away | -0.2539 |
| Raw ev away | -0.5474 |
| Market p over 1 5 | 74.1% |
=======
| Away probability edge | -13.0% |
| Over 2.5 probability edge | -21.2% |
| Under 2.5 probability edge | +21.2% |
| Raw edge prob home | 0.1909 |
| Raw ev home | 0.7689 |
| Raw edge prob draw | 0.0689 |
| Raw ev draw | 0.2181 |
| Raw edge prob away | -0.2598 |
| Raw ev away | -0.5513 |
| Market p over 1 5 | 72.7% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Market over 1 5 odds | 1.35 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T10:48:54Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 75.1% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T10:48:55Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.70 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 52.1% |
| Market btts yes odds | 1.91 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T10:48:55Z |
| Market reference btts yes odds | 1.91 |
| Market reference btts yes opposite odds | 2.08 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-11 — Liverpool vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **43.2%**. Expected goals are 1.40 for Liverpool and 1.65 for Manchester City (3.05 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.9%; Under 3.5 goals: 63.6%; Under 4.5 goals: 80.6%; BTTS Yes (both teams score): 61.9%; BTTS No (at least one team does not score): 38.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 30.9% | 3.24 |
| Draw | 25.8% | 3.87 |
| Manchester City win | 43.2% | 2.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.40 |
| Manchester City expected goals | 1.65 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 82.0% |
| Under 1.5 | 18.0% |
| Over 2.5 | 58.9% |
| Under 2.5 | 41.1% |
| Over 3.5 | 36.4% |
| Under 3.5 | 63.6% |
| Over 4.5 | 19.4% |
| Under 4.5 | 80.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-1 | 12.00% |
| 2 | 1-2 | 9.16% |
| 3 | 2-1 | 7.55% |
| 4 | 0-1 | 6.78% |
| 5 | 0-2 | 6.56% |
=======
| 1 | 1-1 | 11.94% |
| 2 | 1-2 | 9.20% |
| 3 | 2-1 | 7.53% |
| 4 | 0-1 | 6.81% |
| 5 | 0-2 | 6.59% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 30.9% | 30.4% | 3.40 | +5.1% |
| Draw | 25.8% | 25.5% | 3.90 | +0.8% |
| Manchester City win | 43.2% | 44.0% | 2.29 | -1.0% |
| Over 2.5 | 58.9% | 60.5% | 1.66 | -2.2% |
| Under 2.5 | 41.1% | 39.5% | 2.43 | -0.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T15:30:00+00:00 |
| Fixture id | 6dbab232dd8d2aed0cb1d6f7978fb7b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:54Z |
| Market best draw last update utc | 2026-10-11T10:48:54Z |
| Market best away last update utc | 2026-10-11T10:48:06Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.9% |
| P btts no | 38.1% |
| Fair Over 0.5 odds | 1.06 |
<<<<<<< HEAD
| Fair Under 0.5 odds | 17.10 |
=======
| Fair Under 0.5 odds | 17.19 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.54 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.75 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.17 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 31.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 62.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
<<<<<<< HEAD
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.21 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | +0.4% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | 0.0078 |
| Raw ev home | 0.0197 |
| Raw edge prob draw | 0.0037 |
| Raw ev draw | 0.0073 |
| Raw edge prob away | -0.0115 |
| Raw ev away | -0.0234 |
| Market p over 1 5 | 84.2% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:47:23Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 60.9% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:49:14Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.27 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 63.5% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:49:14Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.72 |
| Market btts yes bookmakers | 5 |
=======
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 3.20 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.23 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | +0.5% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | 0.0095 |
| Raw ev home | 0.0671 |
| Raw edge prob draw | 0.0063 |
| Raw ev draw | 0.0204 |
| Raw edge prob away | -0.0158 |
| Raw ev away | -0.0279 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-12 — Coventry City vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **58.3%**. Expected goals are 0.36 for Coventry City and 1.82 for Newcastle United (2.18 combined). The most likely exact score is 0-1 at 15.9%. Goal-market probabilities: at least one goal: 86.7%; Over 2.5 goals: 34.4%; Under 3.5 goals: 84.5%; Under 4.5 goals: 93.9%; BTTS Yes (both teams score): 27.9%; BTTS No (at least one team does not score): 72.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 17.9% | 5.57 |
| Draw | 23.8% | 4.21 |
| Newcastle United win | 58.3% | 1.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 0.36 |
| Newcastle United expected goals | 1.82 |
| Expected total goals | 2.18 |
| Over 0.5 | 86.7% |
| Under 0.5 | 13.3% |
| Over 1.5 | 60.8% |
| Under 1.5 | 39.2% |
| Over 2.5 | 34.4% |
| Under 2.5 | 65.6% |
| Over 3.5 | 15.5% |
| Under 3.5 | 84.5% |
| Over 4.5 | 6.1% |
| Under 4.5 | 93.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 0-1 | 15.74% |
| 2 | 0-2 | 14.88% |
| 3 | 0-0 | 13.33% |
| 4 | 1-0 | 10.31% |
| 5 | 1-1 | 9.11% |
=======
| 1 | 0-1 | 15.86% |
| 2 | 0-2 | 14.99% |
| 3 | 0-0 | 13.25% |
| 4 | 1-0 | 10.13% |
| 5 | 0-3 | 9.09% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 17.9% | 30.0% | 3.35 | -39.9% |
| Draw | 23.8% | 25.9% | 3.80 | -9.7% |
| Newcastle United win | 58.3% | 44.1% | 2.30 | +34.1% |
| Over 2.5 | 34.4% | 56.0% | 1.75 | -39.8% |
| Under 2.5 | 65.6% | 44.0% | 2.25 | +47.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-12T19:00:00+00:00 |
| Fixture id | acd5bd945dd953ad1e300df5bfe696f9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:55Z |
| Market best draw last update utc | 2026-10-11T10:48:54Z |
| Market best away last update utc | 2026-10-11T10:48:54Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 27.9% |
| P btts no | 72.1% |
| Fair Over 0.5 odds | 1.15 |
<<<<<<< HEAD
| Fair Under 0.5 odds | 7.50 |
=======
| Fair Under 0.5 odds | 7.55 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.55 |
| Fair Over 2.5 odds | 2.90 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.47 |
| Fair Under 3.5 odds | 1.18 |
<<<<<<< HEAD
| Fair Over 4.5 odds | 16.39 |
| Fair Under 4.5 odds | 1.06 |
=======
| Fair Over 4.5 odds | 16.30 |
| Fair Under 4.5 odds | 1.07 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 72.5% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 26.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 3.25 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.23 |
<<<<<<< HEAD
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.13 |
| Home probability edge | -12.4% |
| Draw probability edge | -2.3% |
| Away probability edge | +14.6% |
| Over 2.5 probability edge | -23.6% |
| Under 2.5 probability edge | +23.6% |
| Raw edge prob home | -0.2474 |
| Raw ev home | -0.8033 |
| Raw edge prob draw | -0.0456 |
| Raw ev draw | -0.1784 |
| Raw edge prob away | 0.2930 |
| Raw ev away | 0.6676 |
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:47:23Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T08:47:23Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 61.5% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:49:14Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.45 |
| Market btts yes bookmakers | 4 |
=======
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -12.1% |
| Draw probability edge | -2.1% |
| Away probability edge | +14.2% |
| Over 2.5 probability edge | -21.6% |
| Under 2.5 probability edge | +21.6% |
| Raw edge prob home | -0.2412 |
| Raw ev home | -0.8030 |
| Raw edge prob draw | -0.0429 |
| Raw ev draw | -0.1782 |
| Raw edge prob away | 0.2841 |
| Raw ev away | 0.6673 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **39.6%**. Expected goals are 1.48 for Brentford and 1.63 for Liverpool (3.11 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 60.3%; Under 3.5 goals: 62.2%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 34.7% | 2.88 |
| Draw | 25.7% | 3.90 |
| Liverpool win | 39.6% | 2.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.48 |
| Liverpool expected goals | 1.63 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.73% |
| 2 | 1-2 | 8.63% |
| 3 | 2-1 | 8.19% |
| 4 | 2-2 | 6.42% |
| 5 | 0-1 | 6.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 34.7% | 35.7% | 2.88 | +0.1% |
| Draw | 25.7% | 25.4% | 3.85 | -1.2% |
| Liverpool win | 39.6% | 39.0% | 2.50 | -1.0% |
| Over 2.5 | 60.3% | 61.9% | 1.56 | -6.0% |
| Under 2.5 | 39.7% | 38.1% | 2.45 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | 8f1945e7272bc7e89016439f5ab321c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:21Z |
| Market best draw last update utc | 2026-10-11T10:48:54Z |
| Market best away last update utc | 2026-10-11T10:48:21Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Nordic Bet |
| Matched home-team name | Brentford |
| Matched away-team name | Liverpool |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.17 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.83 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.89 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 40.2% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.48 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -0.9% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | -0.0185 |
| Raw ev home | -0.0260 |
<<<<<<< HEAD
| Raw edge prob draw | 0.0053 |
| Raw ev draw | 0.0001 |
| Raw edge prob away | 0.0036 |
| Raw ev away | 0.0051 |
=======
| Raw edge prob draw | 0.0061 |
| Raw ev draw | 0.0000 |
| Raw edge prob away | 0.0125 |
| Raw ev away | 0.0052 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **39.8%**. Expected goals are 1.28 for Everton and 1.29 for Chelsea (2.57 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 48.3%; Under 3.5 goals: 74.0%; Under 4.5 goals: 87.8%; BTTS Yes (both teams score): 53.2%; BTTS No (at least one team does not score): 46.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 33.3% | 3.00 |
| Draw | 26.9% | 3.72 |
| Chelsea win | 39.8% | 2.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.28 |
| Chelsea expected goals | 1.29 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 48.3% |
| Under 2.5 | 51.7% |
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 12.2% |
| Under 4.5 | 87.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.85% |
| 2 | 0-1 | 9.53% |
| 3 | 1-2 | 9.12% |
| 4 | 0-0 | 8.24% |
| 5 | 1-0 | 8.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 33.3% | 31.4% | 3.45 | +14.9% |
| Draw | 26.9% | 24.6% | 3.88 | +4.4% |
| Chelsea win | 39.8% | 44.0% | 2.23 | -11.3% |
| Over 2.5 | 48.3% | 59.2% | 1.73 | -16.4% |
| Under 2.5 | 51.7% | 40.8% | 2.30 | +18.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T11:30:00+00:00 |
| Fixture id | 764e6513cb3f348881503df70ccb90e0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:54Z |
| Market best draw last update utc | 2026-10-11T10:48:21Z |
| Market best away last update utc | 2026-10-11T10:48:21Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Everton |
| Matched away-team name | Chelsea |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 53.2% |
| P btts no | 46.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.13 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.88 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.23 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 53.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
<<<<<<< HEAD
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.15 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.14 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.13 |
| Home probability edge | +2.6% |
| Draw probability edge | +2.1% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | 0.0526 |
| Raw ev home | 0.1991 |
| Raw edge prob draw | 0.0421 |
| Raw ev draw | 0.1327 |
| Raw edge prob away | -0.0947 |
| Raw ev away | -0.1897 |
=======
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 3.05 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +2.0% |
| Draw probability edge | +2.3% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -10.8% |
| Under 2.5 probability edge | +10.8% |
| Raw edge prob home | 0.0392 |
| Raw ev home | 0.2168 |
| Raw edge prob draw | 0.0459 |
| Raw ev draw | 0.1327 |
| Raw edge prob away | -0.0850 |
| Raw ev away | -0.2076 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.1%**. Expected goals are 0.85 for Fulham and 1.07 for Hull City (1.92 combined). The most likely exact score is 1-0 at 17.2%. Goal-market probabilities: at least one goal: 86.5%; Over 2.5 goals: 31.6%; Under 3.5 goals: 87.2%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 38.0%; BTTS No (at least one team does not score): 62.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.1% | 2.38 |
| Draw | 28.6% | 3.50 |
| Hull City win | 29.3% | 3.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.85 |
| Hull City expected goals | 1.07 |
| Expected total goals | 1.92 |
| Over 0.5 | 86.5% |
| Under 0.5 | 13.5% |
| Over 1.5 | 58.5% |
| Under 1.5 | 41.5% |
| Over 2.5 | 31.6% |
| Under 2.5 | 68.4% |
| Over 3.5 | 12.8% |
| Under 3.5 | 87.2% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-0 | 17.29% |
| 2 | 0-0 | 13.50% |
| 3 | 1-1 | 12.37% |
| 4 | 0-1 | 10.71% |
| 5 | 2-1 | 8.85% |
=======
| 1 | 1-0 | 17.23% |
| 2 | 0-0 | 13.46% |
| 3 | 1-1 | 12.34% |
| 4 | 0-1 | 10.78% |
| 5 | 2-1 | 8.82% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Fulham win | 42.2% | 57.6% | 1.73 | -26.9% |
| Draw | 28.7% | 23.2% | 4.11 | +17.9% |
| Hull City win | 29.1% | 19.2% | 5.18 | +50.7% |
| Over 2.5 | 31.6% | 55.2% | 1.81 | -42.8% |
| Under 2.5 | 68.4% | 44.8% | 2.23 | +52.6% |
=======
| Fulham win | 42.1% | 57.3% | 1.73 | -27.2% |
| Draw | 28.6% | 23.1% | 4.11 | +17.6% |
| Hull City win | 29.3% | 19.6% | 5.18 | +51.7% |
| Over 2.5 | 31.6% | 58.3% | 1.81 | -42.8% |
| Under 2.5 | 68.4% | 41.7% | 2.23 | +52.5% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | 7895f97f2f9577f3b13287a3d086859d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:21Z |
| Market best draw last update utc | 2026-10-11T10:48:21Z |
| Market best away last update utc | 2026-10-11T10:48:21Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | LeoVegas (SE) |
| Matched home-team name | Fulham |
| Matched away-team name | Hull |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 38.0% |
| P btts no | 62.0% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.43 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.41 |
| Fair Over 2.5 odds | 3.17 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.80 |
| Fair Under 3.5 odds | 1.15 |
<<<<<<< HEAD
| Fair Over 4.5 odds | 20.96 |
=======
| Fair Over 4.5 odds | 20.91 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 34.1% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 87.1% |
| Raw p btts yes | 39.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.71 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.80 |
<<<<<<< HEAD
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.02 |
| Home probability edge | -15.3% |
| Draw probability edge | +5.4% |
| Away probability edge | +9.9% |
| Over 2.5 probability edge | -23.7% |
| Under 2.5 probability edge | +23.7% |
| Raw edge prob home | -0.3068 |
| Raw ev home | -0.5349 |
| Raw edge prob draw | 0.1088 |
| Raw ev draw | 0.4025 |
| Raw edge prob away | 0.1980 |
| Raw ev away | 1.0197 |
=======
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -15.2% |
| Draw probability edge | +5.5% |
| Away probability edge | +9.7% |
| Over 2.5 probability edge | -26.7% |
| Under 2.5 probability edge | +26.7% |
| Raw edge prob home | -0.3038 |
| Raw ev home | -0.5345 |
| Raw edge prob draw | 0.1102 |
| Raw ev draw | 0.4023 |
| Raw edge prob away | 0.1936 |
| Raw ev away | 1.0189 |
| Market p over 1 5 | 79.5% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Codere (IT) |
| Market best over 1 5 last update utc | 2026-10-11T10:48:54Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 67.7% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T10:48:54Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 2.65 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 54.9% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T10:48:55Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.12 |
| Market btts yes bookmakers | 4 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Manchester City win** at **82.6%**. Expected goals are 3.46 for Manchester City and 0.70 for Ipswich Town (4.15 combined). The most likely exact score is 3-0 at 10.3%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 77.0%; Under 3.5 goals: 41.9%; Under 4.5 goals: 61.2%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.
=======
The model's most likely 1X2 outcome is **Manchester City win** at **83.8%**. Expected goals are 3.46 for Manchester City and 0.70 for Ipswich Town (4.15 combined). The most likely exact score is 3-0 at 10.4%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 77.2%; Under 3.5 goals: 41.5%; Under 4.5 goals: 60.9%; BTTS Yes (both teams score): 50.0%; BTTS No (at least one team does not score): 50.0%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 83.8% | 1.19 |
| Draw | 11.0% | 9.13 |
| Ipswich Town win | 5.3% | 18.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.46 |
| Ipswich Town expected goals | 0.70 |
| Expected total goals | 4.15 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 91.8% |
| Under 1.5 | 8.2% |
| Over 2.5 | 77.2% |
| Under 2.5 | 22.8% |
| Over 3.5 | 58.5% |
| Under 3.5 | 41.5% |
| Over 4.5 | 39.1% |
| Under 4.5 | 60.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 3-0 | 10.25% |
| 2 | 2-0 | 8.90% |
| 3 | 4-0 | 8.86% |
| 4 | 3-1 | 7.15% |
| 5 | 2-1 | 6.20% |
=======
| 1 | 3-0 | 10.39% |
| 2 | 2-0 | 9.02% |
| 3 | 4-0 | 8.98% |
| 4 | 3-1 | 7.25% |
| 5 | 2-1 | 6.29% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 83.8% | 80.3% | 1.29 | +8.1% |
| Draw | 11.0% | 12.8% | 7.00 | -23.3% |
| Ipswich Town win | 5.3% | 6.9% | 12.50 | -34.0% |
| Over 2.5 | 77.2% | 69.4% | 1.40 | +8.1% |
| Under 2.5 | 22.8% | 30.6% | 3.00 | -31.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | bf2142d1ca76ba2fc9e61afce80f86c0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:21Z |
| Market best draw last update utc | 2026-10-11T10:48:54Z |
| Market best away last update utc | 2026-10-11T10:48:54Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Nordic Bet |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Man City |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.02 |
<<<<<<< HEAD
| Fair Under 0.5 odds | 41.64 |
=======
| Fair Under 0.5 odds | 42.45 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.19 |
| Fair Over 2.5 odds | 1.30 |
<<<<<<< HEAD
| Fair Under 2.5 odds | 4.34 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.39 |
| Fair Over 4.5 odds | 2.58 |
| Fair Under 4.5 odds | 1.63 |
=======
| Fair Under 2.5 odds | 4.39 |
| Fair Over 3.5 odds | 1.71 |
| Fair Under 3.5 odds | 2.41 |
| Fair Over 4.5 odds | 2.56 |
| Fair Under 4.5 odds | 1.64 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Unadjusted home-win probability | 87.2% |
| Unadjusted draw probability | 9.1% |
| Unadjusted away-win probability | 3.7% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.4% |
| Raw p btts yes | 49.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.23 |
| Reference draw odds | 7.00 |
| Reference away odds | 12.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.98 |
| Home probability edge | +3.4% |
| Draw probability edge | -1.8% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | +7.8% |
| Under 2.5 probability edge | -7.8% |
| Raw edge prob home | 0.0687 |
| Raw ev home | 0.1249 |
<<<<<<< HEAD
| Raw edge prob draw | -0.0403 |
| Raw ev draw | -0.3414 |
| Raw edge prob away | -0.0516 |
| Raw ev away | -0.5068 |
=======
| Raw edge prob draw | -0.0361 |
| Raw ev draw | -0.3597 |
| Raw edge prob away | -0.0326 |
| Raw ev away | -0.5433 |
| Market p over 1 5 | 88.7% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T10:48:06Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.92 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T10:48:22Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 1.89 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 54.0% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-11T10:48:47Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 5 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **45.4%**. Expected goals are 1.77 for Newcastle United and 1.44 for Aston Villa (3.21 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 62.4%; Under 3.5 goals: 60.0%; Under 4.5 goals: 77.8%; BTTS Yes (both teams score): 64.2%; BTTS No (at least one team does not score): 35.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 45.4% | 2.20 |
| Draw | 24.7% | 4.05 |
| Aston Villa win | 29.9% | 3.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.77 |
| Aston Villa expected goals | 1.44 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.4% |
| Under 2.5 | 37.6% |
| Over 3.5 | 40.0% |
| Under 3.5 | 60.0% |
| Over 4.5 | 22.2% |
| Under 4.5 | 77.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.12% |
| 2 | 2-1 | 9.31% |
| 3 | 1-2 | 7.30% |
| 4 | 2-0 | 6.47% |
| 5 | 2-2 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 45.4% | 46.4% | 2.17 | -1.5% |
| Draw | 24.7% | 24.1% | 3.95 | -2.6% |
| Aston Villa win | 29.9% | 29.5% | 3.35 | +0.3% |
| Over 2.5 | 62.4% | 60.0% | 1.65 | +2.9% |
| Under 2.5 | 37.6% | 40.0% | 2.45 | -7.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | d1bbbdcd3d430e70091b518369b559cf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:21Z |
| Market best draw last update utc | 2026-10-11T10:48:09Z |
| Market best away last update utc | 2026-10-11T10:48:21Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Newcastle |
| Matched away-team name | Aston Villa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.2% |
| P btts no | 35.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.96 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.29 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.66 |
| Fair Over 3.5 odds | 2.50 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.51 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 44.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 64.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
<<<<<<< HEAD
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.09 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.24 |
| Home probability edge | -0.9% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | -0.0184 |
=======
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | -1.0% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | +2.4% |
| Under 2.5 probability edge | -2.4% |
| Raw edge prob home | -0.0197 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Raw ev home | -0.0364 |
| Raw edge prob draw | 0.0111 |
| Raw ev draw | -0.0036 |
| Raw edge prob away | 0.0086 |
| Raw ev away | 0.0173 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.8%**. Expected goals are 1.53 for Bournemouth and 1.04 for Sunderland (2.57 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 47.9%; Under 3.5 goals: 74.1%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.8% | 2.09 |
| Draw | 27.0% | 3.70 |
| Sunderland win | 25.2% | 3.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.53 |
| Sunderland expected goals | 1.04 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.89% |
| 2 | 1-0 | 10.51% |
| 3 | 2-1 | 9.42% |
| 4 | 2-0 | 9.03% |
| 5 | 0-0 | 8.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.8% | 48.3% | 2.10 | +0.4% |
| Draw | 27.0% | 25.8% | 3.75 | +1.3% |
| Sunderland win | 25.2% | 25.8% | 3.85 | -3.0% |
| Over 2.5 | 47.9% | 52.0% | 1.88 | -9.9% |
| Under 2.5 | 52.1% | 48.0% | 2.07 | +7.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | dfd5d6648be46426e418801584d46a68 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:54Z |
| Market best draw last update utc | 2026-10-11T10:48:22Z |
| Market best away last update utc | 2026-10-11T10:48:22Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bournemouth |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.09 |
<<<<<<< HEAD
| Fair Under 0.5 odds | 11.65 |
=======
| Fair Under 0.5 odds | 11.72 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.32 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 74.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 52.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
<<<<<<< HEAD
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.04 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.55 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 1.94 |
| Home probability edge | -0.1% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | -0.0011 |
| Raw ev home | -0.0074 |
| Raw edge prob draw | 0.0205 |
| Raw ev draw | 0.0563 |
| Raw edge prob away | -0.0194 |
| Raw ev away | -0.0541 |
=======
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.02 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | -0.5% |
| Draw probability edge | +1.2% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | -0.0105 |
| Raw ev home | -0.0073 |
| Raw edge prob draw | 0.0233 |
| Raw ev draw | 0.0562 |
| Raw edge prob away | -0.0127 |
| Raw ev away | -0.0543 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **57.2%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 56.7%; Under 3.5 goals: 66.0%; Under 4.5 goals: 82.4%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 57.2% | 1.75 |
| Draw | 23.5% | 4.26 |
| Crystal Palace win | 19.4% | 5.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 1.85 |
| Crystal Palace expected goals | 1.08 |
| Expected total goals | 2.93 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 80.3% |
| Under 1.5 | 19.7% |
| Over 2.5 | 56.7% |
| Under 2.5 | 43.3% |
| Over 3.5 | 34.0% |
| Under 3.5 | 66.0% |
| Over 4.5 | 17.6% |
| Under 4.5 | 82.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.10% |
| 2 | 2-1 | 10.41% |
| 3 | 2-0 | 9.63% |
| 4 | 1-0 | 9.25% |
| 5 | 3-1 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 57.2% | 60.2% | 1.63 | -6.8% |
| Draw | 23.5% | 22.0% | 4.57 | +7.2% |
| Crystal Palace win | 19.4% | 17.8% | 5.60 | +8.5% |
| Over 2.5 | 56.7% | 61.5% | 1.63 | -7.6% |
| Under 2.5 | 43.3% | 38.5% | 2.49 | +7.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 9fc08b390a49c4434f7cf631a0bb88fb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:22Z |
| Market best draw last update utc | 2026-10-11T10:48:22Z |
| Market best away last update utc | 2026-10-11T10:48:54Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.06 |
<<<<<<< HEAD
| Fair Under 0.5 odds | 16.79 |
=======
| Fair Under 0.5 odds | 16.44 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.09 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 2.94 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.68 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 80.1% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.63 |
| Reference draw odds | 4.30 |
| Reference away odds | 5.25 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -3.0% |
| Draw probability edge | +1.5% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | -0.0602 |
| Raw ev home | -0.1170 |
<<<<<<< HEAD
| Raw edge prob draw | 0.0393 |
| Raw ev draw | 0.1400 |
| Raw edge prob away | 0.0326 |
| Raw ev away | 0.1592 |
=======
| Raw edge prob draw | 0.0298 |
| Raw ev draw | 0.1399 |
| Raw edge prob away | 0.0304 |
| Raw ev away | 0.1696 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

<<<<<<< HEAD
The model's most likely 1X2 outcome is **Leeds United win** at **38.8%**. Expected goals are 1.42 for Leeds United and 1.30 for Manchester United (2.72 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 51.6%; Under 3.5 goals: 70.9%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.
=======
The model's most likely 1X2 outcome is **Leeds United win** at **37.9%**. Expected goals are 1.42 for Leeds United and 1.30 for Manchester United (2.72 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 51.6%; Under 3.5 goals: 70.9%; Under 4.5 goals: 85.8%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 37.9% | 2.64 |
| Draw | 26.9% | 3.72 |
| Manchester United win | 35.2% | 2.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.30 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 51.6% |
| Under 2.5 | 48.4% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.2% |
| Under 4.5 | 85.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.80% |
| 2 | 2-1 | 8.48% |
| 3 | 1-2 | 8.39% |
| 4 | 1-0 | 7.94% |
| 5 | 0-1 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
<<<<<<< HEAD
| Leeds United win | 38.8% | 39.0% | 2.60 | +0.9% |
| Draw | 27.0% | 25.7% | 3.75 | +1.1% |
| Manchester United win | 34.2% | 35.3% | 2.86 | -2.1% |
| Over 2.5 | 51.6% | 58.9% | 1.70 | -12.4% |
| Under 2.5 | 48.4% | 41.1% | 2.34 | +13.4% |
=======
| Leeds United win | 37.9% | 37.2% | 2.60 | -1.4% |
| Draw | 26.9% | 25.5% | 3.75 | +0.7% |
| Manchester United win | 35.2% | 37.2% | 2.85 | +0.4% |
| Over 2.5 | 51.6% | 57.6% | 1.70 | -12.3% |
| Under 2.5 | 48.4% | 42.4% | 2.34 | +13.3% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 676b3b0b609e9cf565da450786618d26 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:55Z |
| Market best draw last update utc | 2026-10-11T10:48:22Z |
| Market best away last update utc | 2026-10-11T10:48:22Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.34 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.07 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.6% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 56.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
<<<<<<< HEAD
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.45 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | -0.2% |
| Draw probability edge | +1.3% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.0046 |
| Raw ev home | 0.0033 |
| Raw edge prob draw | 0.0252 |
| Raw ev draw | 0.0580 |
| Raw edge prob away | -0.0206 |
| Raw ev away | -0.0506 |
=======
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.60 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +0.7% |
| Draw probability edge | +1.4% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | 0.0134 |
| Raw ev home | 0.0032 |
| Raw edge prob draw | 0.0271 |
| Raw ev draw | 0.0580 |
| Raw edge prob away | -0.0405 |
| Raw ev away | -0.0538 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **58.0%**. Expected goals are 0.77 for Nottingham Forest and 1.55 for Arsenal (2.32 combined). The most likely exact score is 0-1 at 14.8%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 42.0%; Under 3.5 goals: 79.1%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 42.9%; BTTS No (at least one team does not score): 57.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.4% | 6.09 |
| Draw | 25.5% | 3.92 |
| Arsenal win | 58.0% | 1.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.77 |
| Arsenal expected goals | 1.55 |
| Expected total goals | 2.32 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 69.1% |
| Under 1.5 | 30.9% |
| Over 2.5 | 42.0% |
| Under 2.5 | 58.0% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.84% |
| 2 | 0-2 | 12.52% |
| 3 | 1-1 | 11.82% |
| 4 | 0-0 | 10.07% |
| 5 | 1-2 | 9.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.4% | 15.5% | 6.80 | +11.7% |
| Draw | 25.5% | 23.1% | 4.10 | +4.7% |
| Arsenal win | 58.0% | 61.4% | 1.66 | -3.7% |
| Over 2.5 | 42.0% | 52.3% | 1.97 | -17.3% |
| Under 2.5 | 58.0% | 47.7% | 1.97 | +14.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | f696a248965373d9071dc0662e5c58a8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:54Z |
| Market best draw last update utc | 2026-10-11T10:48:54Z |
| Market best away last update utc | 2026-10-11T10:48:22Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Codere (IT) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.9% |
| P btts no | 57.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.93 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.23 |
| Fair Over 2.5 odds | 2.38 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.79 |
| Fair Under 3.5 odds | 1.26 |
<<<<<<< HEAD
| Fair Over 4.5 odds | 11.20 |
=======
| Fair Over 4.5 odds | 11.21 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 43.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 6.00 |
| Reference draw odds | 4.10 |
<<<<<<< HEAD
| Reference away odds | 1.59 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +0.8% |
| Draw probability edge | +2.6% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | 0.0151 |
| Raw ev home | 0.1774 |
| Raw edge prob draw | 0.0526 |
| Raw ev draw | 0.1478 |
| Raw edge prob away | -0.0677 |
=======
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +0.9% |
| Draw probability edge | +2.5% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -10.3% |
| Under 2.5 probability edge | +10.3% |
| Raw edge prob home | 0.0177 |
| Raw ev home | 0.1773 |
| Raw edge prob draw | 0.0491 |
| Raw ev draw | 0.1477 |
| Raw edge prob away | -0.0667 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Raw ev away | -0.0921 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **67.9%**. Expected goals are 1.71 for Tottenham Hotspur and 0.34 for Coventry City (2.04 combined). The most likely exact score is 1-0 at 20.5%. Goal-market probabilities: at least one goal: 86.9%; Over 2.5 goals: 33.2%; Under 3.5 goals: 85.4%; Under 4.5 goals: 94.5%; BTTS Yes (both teams score): 24.2%; BTTS No (at least one team does not score): 75.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 67.9% | 1.47 |
| Draw | 22.1% | 4.53 |
| Coventry City win | 10.1% | 9.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.71 |
| Coventry City expected goals | 0.34 |
| Expected total goals | 2.04 |
| Over 0.5 | 86.9% |
| Under 0.5 | 13.1% |
| Over 1.5 | 60.3% |
| Under 1.5 | 39.7% |
| Over 2.5 | 33.2% |
| Under 2.5 | 66.8% |
| Over 3.5 | 14.6% |
| Under 3.5 | 85.4% |
| Over 4.5 | 5.5% |
| Under 4.5 | 94.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
<<<<<<< HEAD
| 1 | 1-0 | 20.67% |
| 2 | 2-0 | 18.26% |
| 3 | 0-0 | 12.60% |
| 4 | 3-0 | 10.38% |
| 5 | 1-1 | 7.51% |
=======
| 1 | 1-0 | 20.45% |
| 2 | 2-0 | 18.08% |
| 3 | 0-0 | 13.15% |
| 4 | 3-0 | 10.28% |
| 5 | 1-1 | 7.84% |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 67.9% | 64.8% | 1.54 | +4.5% |
| Draw | 22.1% | 21.0% | 4.80 | +5.9% |
| Coventry City win | 10.1% | 14.2% | 6.76 | -32.1% |
| Over 2.5 | 33.2% | 60.7% | 1.64 | -45.6% |
| Under 2.5 | 66.8% | 39.3% | 2.46 | +64.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T19:00:00+00:00 |
| Fixture id | 9baaf4e48b041cfef04e70e42532502e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T10:48:22Z |
| Market best draw last update utc | 2026-10-11T10:48:54Z |
| Market best away last update utc | 2026-10-11T10:48:39Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Codere (IT) |
| Best away bookmaker | Betsson |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
<<<<<<< HEAD
| P btts yes | 24.0% |
| P btts no | 76.0% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 7.93 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.53 |
| Fair Over 2.5 odds | 2.99 |
=======
| P btts yes | 24.2% |
| P btts no | 75.8% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.61 |
| Fair Over 1.5 odds | 1.66 |
| Fair Under 1.5 odds | 2.52 |
| Fair Over 2.5 odds | 3.01 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 6.85 |
| Fair Under 3.5 odds | 1.17 |
<<<<<<< HEAD
| Fair Over 4.5 odds | 18.00 |
=======
| Fair Over 4.5 odds | 18.16 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 5.9% |
| Raw p over 1 5 | 61.3% |
| Raw p under 3 5 | 85.0% |
| Raw p btts yes | 24.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
<<<<<<< HEAD
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.48 |
| Reference draw odds | 4.80 |
| Reference away odds | 6.20 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | +2.4% |
| Draw probability edge | +2.0% |
| Away probability edge | -4.4% |
| Over 2.5 probability edge | -27.5% |
| Under 2.5 probability edge | +27.5% |
| Raw edge prob home | 0.0478 |
| Raw ev home | 0.0928 |
| Raw edge prob draw | 0.0394 |
| Raw ev draw | 0.1093 |
| Raw edge prob away | -0.0872 |
| Raw ev away | -0.5994 |
=======
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.51 |
| Reference draw odds | 4.40 |
| Reference away odds | 6.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.33 |
| Home probability edge | +3.1% |
| Draw probability edge | +1.0% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -27.6% |
| Under 2.5 probability edge | +27.6% |
| Raw edge prob home | 0.0615 |
| Raw ev home | 0.0927 |
| Raw edge prob draw | 0.0209 |
| Raw ev draw | 0.1094 |
| Raw edge prob away | -0.0824 |
| Raw ev away | -0.5991 |
| Market p over 1 5 | 85.2% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T10:48:07Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 62.9% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T10:48:54Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.38 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 55.9% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T10:48:22Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.08 |
| Market btts yes bookmakers | 2 |
>>>>>>> 8a4d69b (Include new model training datasets and outputs)

</details>


---
