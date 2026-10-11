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
| Crystal Palace win | 35.1% | 34.8% | 2.92 | +2.5% |
| Draw | 29.0% | 28.1% | 3.45 | -0.0% |
| Nottingham Forest win | 35.9% | 37.1% | 2.72 | -2.3% |
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
| Market best home last update utc | 2026-10-11T11:25:49Z |
| Market best draw last update utc | 2026-10-11T11:25:49Z |
| Market best away last update utc | 2026-10-11T11:25:49Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | 1xBet |
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
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.63 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.87 |
| Home probability edge | +0.3% |
| Draw probability edge | +0.9% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | 0.0063 |
| Raw ev home | 0.0345 |
| Raw edge prob draw | 0.0176 |
| Raw ev draw | 0.0299 |
| Raw edge prob away | -0.0239 |
| Raw ev away | -0.0556 |
| Market p over 1 5 | 75.3% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T11:25:34Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T11:26:04Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 56.3% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:26:05Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.11 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-11 — Hull City vs Everton

The model's most likely 1X2 outcome is **Hull City win** at **34.7%**. Expected goals are 1.09 for Hull City and 0.66 for Everton (1.74 combined). The most likely exact score is 0-0 at 16.9%. Goal-market probabilities: at least one goal: 83.1%; Over 2.5 goals: 26.0%; Under 3.5 goals: 90.3%; Under 4.5 goals: 96.7%; BTTS Yes (both teams score): 32.9%; BTTS No (at least one team does not score): 67.1%.

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
| 1 | 0-0 | 16.93% |
| 2 | 0-1 | 16.57% |
| 3 | 1-0 | 13.85% |
| 4 | 1-1 | 12.45% |
| 5 | 2-0 | 8.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 34.7% | 25.1% | 3.90 | +35.2% |
| Draw | 31.6% | 28.1% | 3.48 | +9.8% |
| Everton win | 33.8% | 46.8% | 2.20 | -25.7% |
| Over 2.5 | 26.0% | 47.1% | 2.18 | -43.4% |
| Under 2.5 | 74.0% | 52.9% | 1.83 | +35.5% |

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
| Market best home last update utc | 2026-10-11T11:25:49Z |
| Market best draw last update utc | 2026-10-11T11:25:49Z |
| Market best away last update utc | 2026-10-11T11:25:49Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Hull |
| Matched away-team name | Everton |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.9% |
| P btts no | 67.1% |
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
| Raw p over 1 5 | 53.4% |
| Raw p under 3 5 | 90.0% |
| Raw p btts yes | 33.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.85 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.80 |
| Home probability edge | +9.5% |
| Draw probability edge | +3.4% |
| Away probability edge | -13.0% |
| Over 2.5 probability edge | -21.2% |
| Under 2.5 probability edge | +21.2% |
| Raw edge prob home | 0.1909 |
| Raw ev home | 0.7246 |
| Raw edge prob draw | 0.0689 |
| Raw ev draw | 0.2181 |
| Raw edge prob away | -0.2598 |
| Raw ev away | -0.5429 |
| Market p over 1 5 | 72.6% |
| Market over 1 5 odds | 1.35 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T11:25:47Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.36 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 74.9% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T11:25:34Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.65 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 50.9% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:25:49Z |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 1.89 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-11 — Liverpool vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **43.9%**. Expected goals are 1.40 for Liverpool and 1.65 for Manchester City (3.05 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.9%; Under 3.5 goals: 63.6%; Under 4.5 goals: 80.6%; BTTS Yes (both teams score): 61.9%; BTTS No (at least one team does not score): 38.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 30.3% | 3.31 |
| Draw | 25.9% | 3.87 |
| Manchester City win | 43.9% | 2.28 |

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
| 1 | 1-1 | 11.95% |
| 2 | 1-2 | 9.34% |
| 3 | 2-1 | 7.37% |
| 4 | 0-1 | 6.91% |
| 5 | 0-2 | 6.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 30.3% | 29.1% | 3.40 | +2.9% |
| Draw | 25.9% | 25.6% | 3.90 | +0.9% |
| Manchester City win | 43.9% | 45.3% | 2.23 | -2.1% |
| Over 2.5 | 58.9% | 60.9% | 1.60 | -5.8% |
| Under 2.5 | 41.1% | 39.1% | 2.40 | -1.3% |

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
| Market best home last update utc | 2026-10-11T11:25:49Z |
| Market best draw last update utc | 2026-10-11T11:25:49Z |
| Market best away last update utc | 2026-10-11T11:25:16Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 6.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Liverpool |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.9% |
| P btts no | 38.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.18 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.55 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.75 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.16 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 31.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 62.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.37 |
| Reference draw odds | 3.83 |
| Reference away odds | 2.18 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | +1.1% |
| Draw probability edge | +0.3% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | 0.0227 |
| Raw ev home | 0.0671 |
| Raw edge prob draw | 0.0060 |
| Raw ev draw | 0.0204 |
| Raw edge prob away | -0.0287 |
| Raw ev away | -0.0533 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T11:25:34Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 61.8% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T11:25:48Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.31 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 63.4% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:26:05Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.70 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-12 — Coventry City vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **58.0%**. Expected goals are 0.36 for Coventry City and 1.82 for Newcastle United (2.18 combined). The most likely exact score is 0-1 at 15.8%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 34.3%; Under 3.5 goals: 84.6%; Under 4.5 goals: 93.9%; BTTS Yes (both teams score): 27.9%; BTTS No (at least one team does not score): 72.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 17.9% | 5.59 |
| Draw | 24.1% | 4.15 |
| Newcastle United win | 58.0% | 1.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 0.36 |
| Newcastle United expected goals | 1.82 |
| Expected total goals | 2.18 |
| Over 0.5 | 86.6% |
| Under 0.5 | 13.4% |
| Over 1.5 | 60.7% |
| Under 1.5 | 39.3% |
| Over 2.5 | 34.3% |
| Under 2.5 | 65.7% |
| Over 3.5 | 15.4% |
| Under 3.5 | 84.6% |
| Over 4.5 | 6.1% |
| Under 4.5 | 93.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.78% |
| 2 | 0-2 | 14.92% |
| 3 | 0-0 | 13.44% |
| 4 | 1-0 | 10.10% |
| 5 | 1-1 | 9.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 17.9% | 29.9% | 3.35 | -40.1% |
| Draw | 24.1% | 26.6% | 3.80 | -8.4% |
| Newcastle United win | 58.0% | 43.5% | 2.30 | +33.4% |
| Over 2.5 | 34.3% | 56.4% | 1.75 | -40.0% |
| Under 2.5 | 65.7% | 43.6% | 2.25 | +47.8% |

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
| Market best home last update utc | 2026-10-11T11:25:34Z |
| Market best draw last update utc | 2026-10-11T11:25:49Z |
| Market best away last update utc | 2026-10-11T11:25:49Z |
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
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.44 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.54 |
| Fair Over 2.5 odds | 2.92 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.49 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 16.37 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 72.5% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 26.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.29 |
| Reference draw odds | 3.69 |
| Reference away odds | 2.27 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -12.0% |
| Draw probability edge | -2.5% |
| Away probability edge | +14.5% |
| Over 2.5 probability edge | -22.1% |
| Under 2.5 probability edge | +22.1% |
| Raw edge prob home | -0.2400 |
| Raw ev home | -0.8030 |
| Raw edge prob draw | -0.0496 |
| Raw ev draw | -0.1782 |
| Raw edge prob away | 0.2896 |
| Raw ev away | 0.6673 |
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T11:25:34Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T11:25:34Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 60.7% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:26:05Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **39.9%**. Expected goals are 1.48 for Brentford and 1.63 for Liverpool (3.11 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 60.1%; Under 3.5 goals: 62.2%; Under 4.5 goals: 79.6%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 34.0% | 2.94 |
| Draw | 26.1% | 3.83 |
| Liverpool win | 39.9% | 2.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.48 |
| Liverpool expected goals | 1.63 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 60.1% |
| Under 2.5 | 39.9% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.4% |
| Under 4.5 | 79.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.94% |
| 2 | 1-2 | 8.69% |
| 3 | 2-1 | 8.02% |
| 4 | 2-2 | 6.53% |
| 5 | 0-1 | 6.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 34.0% | 34.2% | 2.88 | -2.0% |
| Draw | 26.1% | 26.3% | 3.85 | +0.6% |
| Liverpool win | 39.9% | 39.5% | 2.50 | -0.4% |
| Over 2.5 | 60.1% | 62.2% | 1.56 | -6.2% |
| Under 2.5 | 39.9% | 37.8% | 2.45 | -2.3% |

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
| Market best home last update utc | 2026-10-11T11:25:50Z |
| Market best draw last update utc | 2026-10-11T11:25:49Z |
| Market best away last update utc | 2026-10-11T11:25:50Z |
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
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.86 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.83 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.51 |
| Fair Over 3.5 odds | 2.65 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.90 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 40.2% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.88 |
| Reference draw odds | 3.74 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -0.2% |
| Draw probability edge | -0.1% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.0041 |
| Raw ev home | -0.0260 |
| Raw edge prob draw | -0.0029 |
| Raw ev draw | 0.0000 |
| Raw edge prob away | 0.0070 |
| Raw ev away | 0.0052 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **39.9%**. Expected goals are 1.28 for Everton and 1.29 for Chelsea (2.57 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 48.2%; Under 3.5 goals: 74.1%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 53.3%; BTTS No (at least one team does not score): 46.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 32.8% | 3.04 |
| Draw | 27.2% | 3.67 |
| Chelsea win | 39.9% | 2.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.28 |
| Chelsea expected goals | 1.29 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 48.2% |
| Under 2.5 | 51.8% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.01% |
| 2 | 0-1 | 9.56% |
| 3 | 1-2 | 9.15% |
| 4 | 0-0 | 8.34% |
| 5 | 1-0 | 7.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 32.8% | 30.4% | 3.45 | +13.3% |
| Draw | 27.2% | 25.3% | 3.88 | +5.6% |
| Chelsea win | 39.9% | 44.3% | 2.23 | -11.0% |
| Over 2.5 | 48.2% | 57.0% | 1.73 | -16.6% |
| Under 2.5 | 51.8% | 43.0% | 2.28 | +18.1% |

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
| Market best home last update utc | 2026-10-11T11:25:49Z |
| Market best draw last update utc | 2026-10-11T11:25:50Z |
| Market best away last update utc | 2026-10-11T11:25:50Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Everton |
| Matched away-team name | Chelsea |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 53.3% |
| P btts no | 46.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.98 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.88 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.25 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 53.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.23 |
| Reference draw odds | 3.88 |
| Reference away odds | 2.23 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +2.4% |
| Draw probability edge | +2.0% |
| Away probability edge | -4.4% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | 0.0484 |
| Raw ev home | 0.2168 |
| Raw edge prob draw | 0.0393 |
| Raw ev draw | 0.1327 |
| Raw edge prob away | -0.0878 |
| Raw ev away | -0.2076 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.1%**. Expected goals are 0.85 for Fulham and 1.07 for Hull City (1.92 combined). The most likely exact score is 1-0 at 17.2%. Goal-market probabilities: at least one goal: 86.4%; Over 2.5 goals: 31.5%; Under 3.5 goals: 87.2%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 38.1%; BTTS No (at least one team does not score): 61.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.1% | 2.37 |
| Draw | 29.0% | 3.45 |
| Hull City win | 28.9% | 3.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.85 |
| Hull City expected goals | 1.07 |
| Expected total goals | 1.92 |
| Over 0.5 | 86.4% |
| Under 0.5 | 13.6% |
| Over 1.5 | 58.5% |
| Under 1.5 | 41.5% |
| Over 2.5 | 31.5% |
| Under 2.5 | 68.5% |
| Over 3.5 | 12.8% |
| Under 3.5 | 87.2% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.24% |
| 2 | 0-0 | 13.63% |
| 3 | 1-1 | 12.50% |
| 4 | 0-1 | 10.64% |
| 5 | 2-1 | 8.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 42.1% | 57.3% | 1.73 | -27.1% |
| Draw | 29.0% | 23.8% | 4.11 | +19.1% |
| Hull City win | 28.9% | 18.8% | 5.18 | +49.7% |
| Over 2.5 | 31.5% | 54.4% | 1.81 | -43.0% |
| Under 2.5 | 68.5% | 45.6% | 2.23 | +52.7% |

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
| Market best home last update utc | 2026-10-11T11:25:50Z |
| Market best draw last update utc | 2026-10-11T11:25:50Z |
| Market best away last update utc | 2026-10-11T11:25:50Z |
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
| P btts yes | 38.1% |
| P btts no | 61.9% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.34 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.41 |
| Fair Over 2.5 odds | 3.17 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.80 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 21.00 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 34.1% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 87.1% |
| Raw p btts yes | 39.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.73 |
| Reference draw odds | 4.11 |
| Reference away odds | 5.18 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -15.2% |
| Draw probability edge | +5.1% |
| Away probability edge | +10.1% |
| Over 2.5 probability edge | -22.9% |
| Under 2.5 probability edge | +22.9% |
| Raw edge prob home | -0.3043 |
| Raw ev home | -0.5345 |
| Raw edge prob draw | 0.1029 |
| Raw ev draw | 0.4023 |
| Raw edge prob away | 0.2014 |
| Raw ev away | 1.0189 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **82.2%**. Expected goals are 3.46 for Manchester City and 0.70 for Ipswich Town (4.15 combined). The most likely exact score is 3-0 at 10.2%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 76.8%; Under 3.5 goals: 42.0%; Under 4.5 goals: 61.4%; BTTS Yes (both teams score): 50.4%; BTTS No (at least one team does not score): 49.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 82.2% | 1.22 |
| Draw | 11.5% | 8.66 |
| Ipswich Town win | 6.3% | 15.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.46 |
| Ipswich Town expected goals | 0.70 |
| Expected total goals | 4.15 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 91.6% |
| Under 1.5 | 8.4% |
| Over 2.5 | 76.8% |
| Under 2.5 | 23.2% |
| Over 3.5 | 58.0% |
| Under 3.5 | 42.0% |
| Over 4.5 | 38.6% |
| Under 4.5 | 61.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.19% |
| 2 | 2-0 | 8.84% |
| 3 | 4-0 | 8.81% |
| 4 | 3-1 | 7.11% |
| 5 | 2-1 | 6.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 82.2% | 77.1% | 1.29 | +6.0% |
| Draw | 11.5% | 13.9% | 7.00 | -19.2% |
| Ipswich Town win | 6.3% | 8.9% | 12.50 | -21.4% |
| Over 2.5 | 76.8% | 69.3% | 1.40 | +7.5% |
| Under 2.5 | 23.2% | 30.7% | 3.00 | -30.4% |

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
| Market best home last update utc | 2026-10-11T11:25:50Z |
| Market best draw last update utc | 2026-10-11T11:25:49Z |
| Market best away last update utc | 2026-10-11T11:25:49Z |
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
| P btts yes | 50.4% |
| P btts no | 49.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.28 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.86 |
| Fair Over 2.5 odds | 1.30 |
| Fair Under 2.5 odds | 4.31 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.38 |
| Fair Over 4.5 odds | 2.59 |
| Fair Under 4.5 odds | 1.63 |
| Unadjusted home-win probability | 87.2% |
| Unadjusted draw probability | 9.1% |
| Unadjusted away-win probability | 3.7% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.4% |
| Raw p btts yes | 49.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.29 |
| Reference draw odds | 6.91 |
| Reference away odds | 10.70 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | +5.0% |
| Draw probability edge | -2.4% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | +7.5% |
| Under 2.5 probability edge | -7.5% |
| Raw edge prob home | 0.1006 |
| Raw ev home | 0.1249 |
| Raw edge prob draw | -0.0479 |
| Raw ev draw | -0.3597 |
| Raw edge prob away | -0.0527 |
| Raw ev away | -0.5433 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **45.0%**. Expected goals are 1.77 for Newcastle United and 1.44 for Aston Villa (3.21 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 62.2%; Under 3.5 goals: 60.1%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 64.3%; BTTS No (at least one team does not score): 35.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 45.0% | 2.22 |
| Draw | 25.1% | 3.98 |
| Aston Villa win | 29.9% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.77 |
| Aston Villa expected goals | 1.44 |
| Expected total goals | 3.21 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.2% |
| Under 2.5 | 37.8% |
| Over 3.5 | 39.9% |
| Under 3.5 | 60.1% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.33% |
| 2 | 2-1 | 9.23% |
| 3 | 1-2 | 7.28% |
| 4 | 2-2 | 6.53% |
| 5 | 2-0 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 45.0% | 45.6% | 2.17 | -2.3% |
| Draw | 25.1% | 25.0% | 3.95 | -0.7% |
| Aston Villa win | 29.9% | 29.4% | 3.35 | +0.0% |
| Over 2.5 | 62.2% | 60.0% | 1.65 | +2.7% |
| Under 2.5 | 37.8% | 40.0% | 2.45 | -7.4% |

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
| Market best home last update utc | 2026-10-11T11:25:50Z |
| Market best draw last update utc | 2026-10-11T11:25:50Z |
| Market best away last update utc | 2026-10-11T11:25:50Z |
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
| P btts yes | 64.3% |
| P btts no | 35.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.59 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.28 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.65 |
| Fair Over 3.5 odds | 2.50 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.52 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 44.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 64.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.17 |
| Reference draw odds | 3.92 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -0.6% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | -0.0119 |
| Raw ev home | -0.0364 |
| Raw edge prob draw | 0.0019 |
| Raw ev draw | -0.0036 |
| Raw edge prob away | 0.0101 |
| Raw ev away | 0.0173 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.9%**. Expected goals are 1.53 for Bournemouth and 1.04 for Sunderland (2.57 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 47.9%; Under 3.5 goals: 74.1%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.9% | 2.09 |
| Draw | 27.1% | 3.68 |
| Sunderland win | 25.0% | 4.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.53 |
| Sunderland expected goals | 1.04 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
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
| 1 | 1-1 | 12.96% |
| 2 | 1-0 | 10.53% |
| 3 | 2-1 | 9.43% |
| 4 | 2-0 | 9.04% |
| 5 | 0-0 | 8.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.9% | 48.5% | 2.10 | +0.5% |
| Draw | 27.1% | 26.1% | 3.75 | +1.8% |
| Sunderland win | 25.0% | 25.4% | 3.85 | -3.8% |
| Over 2.5 | 47.9% | 52.5% | 1.88 | -10.0% |
| Under 2.5 | 52.1% | 47.5% | 2.07 | +7.9% |

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
| Market best home last update utc | 2026-10-11T11:25:49Z |
| Market best draw last update utc | 2026-10-11T11:25:50Z |
| Market best away last update utc | 2026-10-11T11:25:50Z |
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
| Fair Under 0.5 odds | 11.66 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.33 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 74.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 52.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.04 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.85 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 2.07 |
| Home probability edge | -0.6% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.0120 |
| Raw ev home | -0.0073 |
| Raw edge prob draw | 0.0205 |
| Raw ev draw | 0.0562 |
| Raw edge prob away | -0.0086 |
| Raw ev away | -0.0543 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **57.5%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 56.8%; Under 3.5 goals: 66.0%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 57.5% | 1.74 |
| Draw | 23.1% | 4.32 |
| Crystal Palace win | 19.4% | 5.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 1.85 |
| Crystal Palace expected goals | 1.08 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 56.8% |
| Under 2.5 | 43.2% |
| Over 3.5 | 34.0% |
| Under 3.5 | 66.0% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.94% |
| 2 | 2-1 | 10.47% |
| 3 | 2-0 | 9.69% |
| 4 | 1-0 | 9.30% |
| 5 | 3-1 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 57.5% | 60.8% | 1.63 | -6.3% |
| Draw | 23.1% | 21.3% | 4.57 | +5.7% |
| Crystal Palace win | 19.4% | 17.9% | 5.60 | +8.5% |
| Over 2.5 | 56.8% | 60.7% | 1.63 | -7.3% |
| Under 2.5 | 43.2% | 39.3% | 2.49 | +7.4% |

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
| Market best home last update utc | 2026-10-11T11:25:50Z |
| Market best draw last update utc | 2026-10-11T11:25:50Z |
| Market best away last update utc | 2026-10-11T11:25:49Z |
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
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.67 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.10 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.94 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.66 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 80.1% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.63 |
| Reference draw odds | 4.57 |
| Reference away odds | 5.44 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.49 |
| Home probability edge | -3.3% |
| Draw probability edge | +1.8% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | -0.0666 |
| Raw ev home | -0.1170 |
| Raw edge prob draw | 0.0363 |
| Raw ev draw | 0.1399 |
| Raw edge prob away | 0.0303 |
| Raw ev away | 0.1696 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **38.9%**. Expected goals are 1.42 for Leeds United and 1.30 for Manchester United (2.72 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 51.5%; Under 3.5 goals: 70.9%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 38.9% | 2.57 |
| Draw | 27.2% | 3.68 |
| Manchester United win | 33.9% | 2.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.30 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.96% |
| 2 | 2-1 | 8.69% |
| 3 | 1-0 | 8.15% |
| 4 | 1-2 | 8.08% |
| 5 | 0-0 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 38.9% | 39.2% | 2.60 | +1.1% |
| Draw | 27.2% | 26.2% | 3.75 | +2.0% |
| Manchester United win | 33.9% | 34.6% | 2.85 | -3.4% |
| Over 2.5 | 51.5% | 58.1% | 1.70 | -12.5% |
| Under 2.5 | 48.5% | 41.9% | 2.34 | +13.6% |

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
| Market best home last update utc | 2026-10-11T11:25:16Z |
| Market best draw last update utc | 2026-10-11T11:25:50Z |
| Market best away last update utc | 2026-10-11T11:25:50Z |
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
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.17 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.09 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.6% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 56.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.52 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.85 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.34 |
| Home probability edge | -0.3% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | -0.0061 |
| Raw ev home | 0.0032 |
| Raw edge prob draw | 0.0201 |
| Raw ev draw | 0.0580 |
| Raw edge prob away | -0.0140 |
| Raw ev away | -0.0538 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **57.2%**. Expected goals are 0.77 for Nottingham Forest and 1.55 for Arsenal (2.32 combined). The most likely exact score is 0-1 at 14.6%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 41.7%; Under 3.5 goals: 79.2%; Under 4.5 goals: 91.2%; BTTS Yes (both teams score): 43.1%; BTTS No (at least one team does not score): 56.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.6% | 6.03 |
| Draw | 26.2% | 3.81 |
| Arsenal win | 57.2% | 1.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.77 |
| Arsenal expected goals | 1.55 |
| Expected total goals | 2.32 |
| Over 0.5 | 89.7% |
| Under 0.5 | 10.3% |
| Over 1.5 | 69.0% |
| Under 1.5 | 31.0% |
| Over 2.5 | 41.7% |
| Under 2.5 | 58.3% |
| Over 3.5 | 20.8% |
| Under 3.5 | 79.2% |
| Over 4.5 | 8.8% |
| Under 4.5 | 91.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.62% |
| 2 | 0-2 | 12.34% |
| 3 | 1-1 | 12.14% |
| 4 | 0-0 | 10.34% |
| 5 | 1-2 | 9.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.6% | 15.8% | 6.80 | +12.7% |
| Draw | 26.2% | 24.5% | 4.10 | +7.6% |
| Arsenal win | 57.2% | 59.7% | 1.66 | -5.1% |
| Over 2.5 | 41.7% | 50.0% | 1.97 | -17.8% |
| Under 2.5 | 58.3% | 50.0% | 1.97 | +14.8% |

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
| Market best home last update utc | 2026-10-11T11:25:49Z |
| Market best draw last update utc | 2026-10-11T11:25:16Z |
| Market best away last update utc | 2026-10-11T11:25:50Z |
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
| P btts yes | 43.1% |
| P btts no | 56.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.67 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.22 |
| Fair Over 2.5 odds | 2.40 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.81 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.31 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 43.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 6.11 |
| Reference draw odds | 3.98 |
| Reference away odds | 1.66 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +0.7% |
| Draw probability edge | +1.8% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -8.3% |
| Under 2.5 probability edge | +8.3% |
| Raw edge prob home | 0.0148 |
| Raw ev home | 0.1773 |
| Raw edge prob draw | 0.0350 |
| Raw ev draw | 0.1477 |
| Raw edge prob away | -0.0499 |
| Raw ev away | -0.0921 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **67.7%**. Expected goals are 1.71 for Tottenham Hotspur and 0.34 for Coventry City (2.04 combined). The most likely exact score is 1-0 at 20.4%. Goal-market probabilities: at least one goal: 87.0%; Over 2.5 goals: 33.2%; Under 3.5 goals: 85.4%; Under 4.5 goals: 94.5%; BTTS Yes (both teams score): 24.1%; BTTS No (at least one team does not score): 75.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 67.7% | 1.48 |
| Draw | 21.9% | 4.57 |
| Coventry City win | 10.4% | 9.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.71 |
| Coventry City expected goals | 0.34 |
| Expected total goals | 2.04 |
| Over 0.5 | 87.0% |
| Under 0.5 | 13.0% |
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
| 1 | 1-0 | 20.40% |
| 2 | 2-0 | 18.03% |
| 3 | 0-0 | 13.03% |
| 4 | 3-0 | 10.25% |
| 5 | 1-1 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 67.7% | 64.4% | 1.54 | +4.3% |
| Draw | 21.9% | 20.6% | 4.80 | +4.9% |
| Coventry City win | 10.4% | 15.0% | 6.76 | -29.4% |
| Over 2.5 | 33.2% | 60.2% | 1.64 | -45.6% |
| Under 2.5 | 66.8% | 39.8% | 2.46 | +64.3% |

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
| Market best home last update utc | 2026-10-11T11:25:50Z |
| Market best draw last update utc | 2026-10-11T11:25:16Z |
| Market best away last update utc | 2026-10-11T11:25:34Z |
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
| P btts yes | 24.1% |
| P btts no | 75.9% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.68 |
| Fair Over 1.5 odds | 1.66 |
| Fair Under 1.5 odds | 2.52 |
| Fair Over 2.5 odds | 3.01 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 6.86 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.18 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 5.9% |
| Raw p over 1 5 | 61.3% |
| Raw p under 3 5 | 85.0% |
| Raw p btts yes | 24.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.54 |
| Reference draw odds | 4.72 |
| Reference away odds | 6.47 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Home probability edge | +3.3% |
| Draw probability edge | +1.3% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -27.0% |
| Under 2.5 probability edge | +27.0% |
| Raw edge prob home | 0.0652 |
| Raw ev home | 0.0927 |
| Raw edge prob draw | 0.0250 |
| Raw ev draw | 0.1094 |
| Raw edge prob away | -0.0902 |
| Raw ev away | -0.5991 |

</details>


---
