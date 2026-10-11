# Ligue 1 — football model report

Fixtures in this report: **12**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 963 |
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
| Optimizer objective | 1689.031 |
| Base scoring parameter | 0.211 |
| Home-advantage parameter | 0.193 |
| Dixon-Coles low-score adjustment | -0.052 |
| Xi per day | 0.0009 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 12.00 |
| Additional event odds calls used before this league | 12.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 3.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-11 — Nice vs Strasbourg

The model's most likely 1X2 outcome is **Nice win** at **40.5%**. Expected goals are 1.46 for Nice and 1.39 for Strasbourg (2.84 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.2%; Under 3.5 goals: 68.2%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 58.1%; BTTS No (at least one team does not score): 41.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nice win | 40.5% | 2.47 |
| Draw | 26.0% | 3.84 |
| Strasbourg win | 33.5% | 2.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nice expected goals | 1.46 |
| Strasbourg expected goals | 1.39 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.2% |
| Under 2.5 | 45.8% |
| Over 3.5 | 31.8% |
| Under 3.5 | 68.2% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.26% |
| 2 | 2-1 | 9.03% |
| 3 | 1-0 | 8.30% |
| 4 | 1-2 | 7.73% |
| 5 | 0-1 | 7.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nice win | 40.5% | 42.6% | 2.36 | -4.4% |
| Draw | 26.0% | 25.8% | 3.84 | -0.1% |
| Strasbourg win | 33.5% | 31.6% | 3.15 | +5.5% |
| Over 2.5 | 54.2% | 58.9% | 1.63 | -11.7% |
| Under 2.5 | 45.8% | 41.1% | 2.49 | +14.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | 5d3606630a2d3a218a6340d082c1bdc6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:26:23Z |
| Market best draw last update utc | 2026-10-11T11:25:52Z |
| Market best away last update utc | 2026-10-11T11:26:23Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nice |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.69 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.60 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.27 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 38.4% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 58.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.20 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -2.1% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | -0.0424 |
| Raw ev home | -0.0944 |
| Raw edge prob draw | 0.0048 |
| Raw ev draw | 0.0084 |
| Raw edge prob away | 0.0376 |
| Raw ev away | 0.1140 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T11:26:25Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 60.7% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T11:26:23Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 65.3% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-11T11:26:30Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.74 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-11 — Rennes vs Auxerre

The model's most likely 1X2 outcome is **Rennes win** at **60.8%**. Expected goals are 1.84 for Rennes and 1.14 for Auxerre (2.98 combined). The most likely exact score is 2-1 at 11.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 58.6%; Under 3.5 goals: 64.4%; Under 4.5 goals: 81.1%; BTTS Yes (both teams score): 56.9%; BTTS No (at least one team does not score): 43.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 60.8% | 1.64 |
| Draw | 21.0% | 4.77 |
| Auxerre win | 18.2% | 5.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.84 |
| Auxerre expected goals | 1.14 |
| Expected total goals | 2.98 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 58.6% |
| Under 2.5 | 41.4% |
| Over 3.5 | 35.6% |
| Under 3.5 | 64.4% |
| Over 4.5 | 18.9% |
| Under 4.5 | 81.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.22% |
| 2 | 1-0 | 10.04% |
| 3 | 1-1 | 9.83% |
| 4 | 2-0 | 9.81% |
| 5 | 3-1 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 60.8% | 68.6% | 1.47 | -10.6% |
| Draw | 21.0% | 18.0% | 5.30 | +11.2% |
| Auxerre win | 18.2% | 13.4% | 7.50 | +36.5% |
| Over 2.5 | 58.6% | 67.0% | 1.47 | -13.8% |
| Under 2.5 | 41.4% | 33.0% | 2.75 | +13.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T15:15:00+00:00 |
| Fixture id | 34f584ab922e220dc4f3b81217959d6d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:26:23Z |
| Market best away last update utc | 2026-10-11T11:26:23Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | LeoVegas (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Rennes |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.9% |
| P btts no | 43.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.30 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.23 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.30 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 53.1% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 80.4% |
| Raw p under 3 5 | 65.1% |
| Raw p btts yes | 57.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.40 |
| Reference draw odds | 4.60 |
| Reference away odds | 6.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -7.7% |
| Draw probability edge | +2.9% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | -0.1547 |
| Raw ev home | -0.2196 |
| Raw edge prob draw | 0.0587 |
| Raw ev draw | 0.2677 |
| Raw edge prob away | 0.0960 |
| Raw ev away | 0.7245 |
| Market p over 1 5 | 86.3% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T11:26:25Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 57.4% |
| Market under 3 5 odds | 1.77 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T11:26:06Z |
| Market reference under 3 5 odds | 1.70 |
| Market reference under 3 5 opposite odds | 2.26 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 58.0% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-11T11:26:29Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.29 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-11 — Troyes vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **60.8%**. Expected goals are 0.92 for Troyes and 2.68 for Marseille (3.60 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 66.7%; Under 3.5 goals: 54.1%; Under 4.5 goals: 73.0%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 18.4% | 5.43 |
| Draw | 20.8% | 4.81 |
| Marseille win | 60.8% | 1.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.92 |
| Marseille expected goals | 2.68 |
| Expected total goals | 3.60 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 86.3% |
| Under 1.5 | 13.7% |
| Over 2.5 | 66.7% |
| Under 2.5 | 33.3% |
| Over 3.5 | 45.9% |
| Under 3.5 | 54.1% |
| Over 4.5 | 27.0% |
| Under 4.5 | 73.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.41% |
| 2 | 0-2 | 8.02% |
| 3 | 1-2 | 7.40% |
| 4 | 0-3 | 7.16% |
| 5 | 1-3 | 6.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 18.4% | 26.7% | 3.65 | -32.8% |
| Draw | 20.8% | 25.9% | 3.90 | -18.9% |
| Marseille win | 60.8% | 47.4% | 2.14 | +30.1% |
| Over 2.5 | 66.7% | 60.5% | 1.67 | +11.4% |
| Under 2.5 | 33.3% | 39.5% | 2.41 | -19.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T18:45:00+00:00 |
| Fixture id | cb7067ac191abf32ad49dad45e46f639 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:26:23Z |
| Market best away last update utc | 2026-10-11T11:26:23Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.50 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.29 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 3.01 |
| Fair Over 3.5 odds | 2.18 |
| Fair Under 3.5 odds | 1.85 |
| Fair Over 4.5 odds | 3.70 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 15.7% |
| Unadjusted away-win probability | 74.2% |
| Raw p over 1 5 | 87.8% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 56.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.40 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -8.3% |
| Draw probability edge | -5.1% |
| Away probability edge | +13.4% |
| Over 2.5 probability edge | +6.3% |
| Under 2.5 probability edge | -6.3% |
| Raw edge prob home | -0.1661 |
| Raw ev home | -0.6306 |
| Raw edge prob draw | -0.1024 |
| Raw ev draw | -0.3888 |
| Raw edge prob away | 0.2685 |
| Raw ev away | 0.5881 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T11:26:25Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T11:26:25Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.56 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 61.2% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-11T11:26:26Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.38 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-16 — Le Mans FC vs Toulouse

The model's most likely 1X2 outcome is **Le Mans FC win** at **38.0%**. Expected goals are 1.87 for Le Mans FC and 1.51 for Toulouse (3.37 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 64.7%; Under 3.5 goals: 56.8%; Under 4.5 goals: 75.4%; BTTS Yes (both teams score): 66.9%; BTTS No (at least one team does not score): 33.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 38.0% | 2.63 |
| Draw | 25.3% | 3.95 |
| Toulouse win | 36.6% | 2.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Mans FC expected goals | 1.87 |
| Toulouse expected goals | 1.51 |
| Expected total goals | 3.37 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 64.7% |
| Under 2.5 | 35.3% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.6% |
| Under 4.5 | 75.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.99% |
| 2 | 1-2 | 8.63% |
| 3 | 2-1 | 7.47% |
| 4 | 2-2 | 7.34% |
| 5 | 0-1 | 5.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 38.0% | 30.3% | 3.25 | +23.5% |
| Draw | 25.3% | 27.3% | 3.75 | -5.0% |
| Toulouse win | 36.6% | 42.4% | 2.34 | -14.3% |
| Over 2.5 | 64.7% | 53.7% | 1.84 | +19.1% |
| Under 2.5 | 35.3% | 46.3% | 2.12 | -25.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-16T18:45:00+00:00 |
| Fixture id | 66c168c030f3faad3983fcadc3060009 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Mans |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.9% |
| P btts no | 33.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.47 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.80 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.83 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.07 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 45.7% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 30.9% |
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 66.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.00 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.00 |
| Home probability edge | +7.7% |
| Draw probability edge | -2.0% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | +11.0% |
| Under 2.5 probability edge | -11.0% |
| Raw edge prob home | 0.1547 |
| Raw ev home | 0.4869 |
| Raw edge prob draw | -0.0391 |
| Raw ev draw | -0.1230 |
| Raw edge prob away | -0.1156 |
| Raw ev away | -0.2778 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **56.6%**. Expected goals are 1.76 for Lille and 0.94 for Brest (2.70 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.3%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 56.6% | 1.77 |
| Draw | 24.0% | 4.17 |
| Brest win | 19.4% | 5.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.76 |
| Brest expected goals | 0.94 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.7% |
| Under 3.5 | 71.3% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.42% |
| 2 | 1-0 | 11.35% |
| 3 | 2-0 | 10.49% |
| 4 | 2-1 | 9.89% |
| 5 | 0-0 | 7.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 56.6% | 57.2% | 1.73 | -2.1% |
| Draw | 24.0% | 23.4% | 4.25 | +1.8% |
| Brest win | 19.4% | 19.4% | 5.25 | +2.0% |
| Over 2.5 | 50.9% | 56.9% | 1.76 | -10.4% |
| Under 2.5 | 49.1% | 43.1% | 2.23 | +9.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | ad25a350c89b64715e15c59cde5653d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:26:23Z |
| Market best away last update utc | 2026-10-11T11:26:23Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | LeoVegas (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.05 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.24 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 56.0% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 19.4% |
| Raw p over 1 5 | 75.7% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 51.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.67 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -0.6% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | -0.0119 |
| Raw ev home | -0.0310 |
| Raw edge prob draw | 0.0119 |
| Raw ev draw | 0.0434 |
| Raw edge prob away | 0.0000 |
| Raw ev away | 0.0205 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **62.9%**. Expected goals are 1.23 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.6%; Under 3.5 goals: 56.8%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 61.8%; BTTS No (at least one team does not score): 38.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.5% | 5.72 |
| Draw | 19.6% | 5.09 |
| Paris Saint Germain win | 62.9% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.23 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.72% |
| 2 | 1-1 | 8.77% |
| 3 | 0-2 | 8.74% |
| 4 | 0-1 | 7.79% |
| 5 | 1-3 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.5% | 13.7% | 7.00 | +22.3% |
| Draw | 19.6% | 17.5% | 5.90 | +15.9% |
| Paris Saint Germain win | 62.9% | 68.8% | 1.46 | -8.2% |
| Over 2.5 | 65.6% | 73.1% | 1.33 | -12.8% |
| Under 2.5 | 34.4% | 26.9% | 3.37 | +15.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T15:15:00+00:00 |
| Fixture id | f3034246520a2ee4ff0ac0d5074966f8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:26:23Z |
| Market best draw last update utc | 2026-10-11T11:24:59Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Betclic (FR) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Strasbourg |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.8% |
| P btts no | 38.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.27 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.82 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.02 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 57.0% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.4% |
| Raw p btts yes | 62.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 6.00 |
| Reference draw odds | 4.80 |
| Reference away odds | 1.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Home probability edge | +3.8% |
| Draw probability edge | +2.1% |
| Away probability edge | -5.9% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | 0.0761 |
| Raw ev home | 0.4895 |
| Raw edge prob draw | 0.0424 |
| Raw ev draw | 0.2837 |
| Raw edge prob away | -0.1185 |
| Raw ev away | -0.1683 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **62.1%**. Expected goals are 0.78 for Troyes and 2.31 for RC Lens (3.09 combined). The most likely exact score is 0-2 at 10.5%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.7%; Under 3.5 goals: 64.4%; Under 4.5 goals: 81.2%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 16.7% | 5.98 |
| Draw | 21.2% | 4.72 |
| RC Lens win | 62.1% | 1.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.78 |
| RC Lens expected goals | 2.31 |
| Expected total goals | 3.09 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 35.6% |
| Under 3.5 | 64.4% |
| Over 4.5 | 18.8% |
| Under 4.5 | 81.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 10.55% |
| 2 | 1-1 | 10.08% |
| 3 | 0-1 | 8.76% |
| 4 | 1-2 | 8.25% |
| 5 | 0-3 | 8.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 16.7% | 22.9% | 4.30 | -28.0% |
| Draw | 21.2% | 24.2% | 4.04 | -14.4% |
| RC Lens win | 62.1% | 52.9% | 1.87 | +16.1% |
| Over 2.5 | 57.7% | 61.3% | 1.64 | -5.4% |
| Under 2.5 | 42.3% | 38.7% | 2.46 | +4.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | b077aa049133c0358bcd643bfee48da3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:25:52Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.25 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.13 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.31 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 10.6% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 71.3% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 49.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.90 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -6.1% |
| Draw probability edge | -3.0% |
| Away probability edge | +9.2% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | -0.1230 |
| Raw ev home | -0.5449 |
| Raw edge prob draw | -0.0609 |
| Raw ev draw | -0.2672 |
| Raw edge prob away | 0.1839 |
| Raw ev away | 0.3329 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **48.3%**. Expected goals are 0.95 for Angers and 1.65 for Marseille (2.59 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 47.6%; Under 3.5 goals: 74.1%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 25.6% | 3.90 |
| Draw | 26.0% | 3.84 |
| Marseille win | 48.3% | 2.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.95 |
| Marseille expected goals | 1.65 |
| Expected total goals | 2.59 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 73.3% |
| Under 1.5 | 26.7% |
| Over 2.5 | 47.6% |
| Under 2.5 | 52.4% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.40% |
| 2 | 0-1 | 10.63% |
| 3 | 0-2 | 9.21% |
| 4 | 1-2 | 8.71% |
| 5 | 0-0 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 25.6% | 30.2% | 3.25 | -16.8% |
| Draw | 26.0% | 26.4% | 4.00 | +4.2% |
| Marseille win | 48.3% | 43.4% | 2.28 | +10.2% |
| Over 2.5 | 47.6% | 58.9% | 1.68 | -20.0% |
| Under 2.5 | 52.4% | 41.1% | 2.40 | +25.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | c7a60aa94470fe959fbf6b0c68060fc1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:26:23Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | LeoVegas (SE) |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Unibet (SE) |
| Matched home-team name | Angers |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.24 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.75 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.35 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 53.2% |
| Raw p over 1 5 | 73.8% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 50.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.00 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -4.6% |
| Draw probability edge | -0.3% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -11.3% |
| Under 2.5 probability edge | +11.3% |
| Raw edge prob home | -0.0919 |
| Raw ev home | -0.3169 |
| Raw edge prob draw | -0.0062 |
| Raw ev draw | 0.0295 |
| Raw edge prob away | 0.0981 |
| Raw ev away | 0.2140 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **36.7%**. Expected goals are 1.16 for Le Havre and 1.19 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.8%; Under 3.5 goals: 79.0%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 36.7% | 2.73 |
| Draw | 28.7% | 3.48 |
| Auxerre win | 34.6% | 2.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.16 |
| Auxerre expected goals | 1.19 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 68.6% |
| Under 1.5 | 31.4% |
| Over 2.5 | 41.8% |
| Under 2.5 | 58.2% |
| Over 3.5 | 21.0% |
| Under 3.5 | 79.0% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.55% |
| 2 | 1-0 | 11.07% |
| 3 | 0-1 | 10.25% |
| 4 | 0-0 | 10.04% |
| 5 | 2-1 | 8.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 36.7% | 38.9% | 2.52 | -7.5% |
| Draw | 28.7% | 28.1% | 3.60 | +3.5% |
| Auxerre win | 34.6% | 33.0% | 3.00 | +3.7% |
| Over 2.5 | 41.8% | 50.9% | 1.94 | -18.9% |
| Under 2.5 | 58.2% | 49.1% | 2.00 | +16.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | d637845b9760bb02b55bbbaa32b5c21e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Havre |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.2% |
| P btts no | 51.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.96 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.39 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.76 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.16 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.0% |
| Raw p btts yes | 48.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.40 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.91 |
| Home probability edge | -2.2% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -9.1% |
| Under 2.5 probability edge | +9.1% |
| Raw edge prob home | -0.0449 |
| Raw ev home | -0.1318 |
| Raw edge prob draw | 0.0132 |
| Raw ev draw | 0.0587 |
| Raw edge prob away | 0.0316 |
| Raw ev away | 0.0843 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **47.7%**. Expected goals are 1.36 for Lorient and 1.84 for AS Monaco (3.21 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.5%; Under 3.5 goals: 60.2%; Under 4.5 goals: 78.3%; BTTS Yes (both teams score): 63.5%; BTTS No (at least one team does not score): 36.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 26.7% | 3.74 |
| Draw | 25.5% | 3.92 |
| AS Monaco win | 47.7% | 2.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.36 |
| AS Monaco expected goals | 1.84 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.7% |
| Under 4.5 | 78.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.50% |
| 2 | 1-2 | 9.26% |
| 3 | 2-2 | 6.86% |
| 4 | 0-1 | 6.86% |
| 5 | 0-2 | 6.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 26.7% | 25.6% | 3.78 | +1.1% |
| Draw | 25.5% | 27.3% | 3.75 | -4.2% |
| AS Monaco win | 47.7% | 47.1% | 2.14 | +2.1% |
| Over 2.5 | 61.5% | 52.2% | 1.90 | +16.9% |
| Under 2.5 | 38.5% | 47.8% | 2.05 | -21.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | 53f5fe7ed0ba0fbf6345c73270e4cd00 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:26:23Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | LeoVegas (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lorient |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 63.5% |
| P btts no | 36.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.31 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.03 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.60 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 27.9% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 83.5% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 63.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.50 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | +1.1% |
| Draw probability edge | -1.8% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | +9.3% |
| Under 2.5 probability edge | -9.3% |
| Raw edge prob home | 0.0225 |
| Raw ev home | 0.0533 |
| Raw edge prob draw | -0.0355 |
| Raw ev draw | -0.1090 |
| Raw edge prob away | 0.0130 |
| Raw ev away | 0.0352 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **55.6%**. Expected goals are 1.78 for Lyon and 1.08 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.7%; Under 3.5 goals: 67.6%; Under 4.5 goals: 83.7%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 55.6% | 1.80 |
| Draw | 24.0% | 4.17 |
| Nice win | 20.3% | 4.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.78 |
| Nice expected goals | 1.08 |
| Expected total goals | 2.86 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 78.6% |
| Under 1.5 | 21.4% |
| Over 2.5 | 54.7% |
| Under 2.5 | 45.3% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.3% |
| Under 4.5 | 83.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.37% |
| 2 | 2-1 | 10.26% |
| 3 | 1-0 | 10.07% |
| 4 | 2-0 | 9.49% |
| 5 | 0-0 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 55.6% | 58.1% | 1.71 | -4.8% |
| Draw | 24.0% | 23.6% | 4.20 | +0.8% |
| Nice win | 20.3% | 18.3% | 5.24 | +6.6% |
| Over 2.5 | 54.7% | 55.8% | 1.78 | -2.6% |
| Under 2.5 | 45.3% | 44.2% | 2.25 | +1.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T18:45:00+00:00 |
| Fixture id | 471f891b1f6516a864ad94c8eb649f5e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:25:52Z |
| Market best draw last update utc | 2026-10-11T11:26:08Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Tipico |
| Matched home-team name | Lyon |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.3% |
| P btts no | 44.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.17 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.68 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.13 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 53.1% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 22.4% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.65 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -2.5% |
| Draw probability edge | +0.4% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | -0.0500 |
| Raw ev home | -0.0912 |
| Raw edge prob draw | 0.0090 |
| Raw ev draw | 0.0272 |
| Raw edge prob away | 0.0410 |
| Raw ev away | 0.1736 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **42.8%**. Expected goals are 1.62 for Paris FC and 1.36 for Rennes (2.98 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 56.8%; Under 3.5 goals: 65.3%; Under 4.5 goals: 82.1%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 42.8% | 2.34 |
| Draw | 26.3% | 3.80 |
| Rennes win | 30.9% | 3.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.62 |
| Rennes expected goals | 1.36 |
| Expected total goals | 2.98 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 80.3% |
| Under 1.5 | 19.7% |
| Over 2.5 | 56.8% |
| Under 2.5 | 43.2% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 17.9% |
| Under 4.5 | 82.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.23% |
| 2 | 2-1 | 9.00% |
| 3 | 1-0 | 7.61% |
| 4 | 1-2 | 7.44% |
| 5 | 2-0 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 42.8% | 42.4% | 2.40 | +2.7% |
| Draw | 26.3% | 27.3% | 3.60 | -5.3% |
| Rennes win | 30.9% | 30.3% | 3.29 | +1.6% |
| Over 2.5 | 56.8% | 57.8% | 1.72 | -2.3% |
| Under 2.5 | 43.2% | 42.2% | 2.30 | -0.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | 27f7222d2abde93fc6e8d17b5b05b272 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T11:26:25Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:25:52Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paris FC |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.97 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.07 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.57 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 31.5% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 60.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.20 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +0.4% |
| Draw probability edge | -1.0% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | 0.0076 |
| Raw ev home | 0.0364 |
| Raw edge prob draw | -0.0196 |
| Raw ev draw | -0.0880 |
| Raw edge prob away | 0.0121 |
| Raw ev away | 0.0359 |

</details>


---
