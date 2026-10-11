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
| Additional event odds calls used before this league | 16.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
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

The model's most likely 1X2 outcome is **Nice win** at **39.8%**. Expected goals are 1.46 for Nice and 1.39 for Strasbourg (2.84 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 54.3%; Under 3.5 goals: 68.2%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 58.0%; BTTS No (at least one team does not score): 42.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nice win | 39.8% | 2.51 |
| Draw | 25.5% | 3.92 |
| Strasbourg win | 34.7% | 2.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nice expected goals | 1.46 |
| Strasbourg expected goals | 1.39 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.3% |
| Under 1.5 | 21.7% |
| Over 2.5 | 54.3% |
| Under 2.5 | 45.7% |
| Over 3.5 | 31.8% |
| Under 3.5 | 68.2% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.03% |
| 2 | 2-1 | 8.87% |
| 3 | 1-0 | 8.15% |
| 4 | 1-2 | 8.01% |
| 5 | 0-1 | 7.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nice win | 39.8% | 41.2% | 2.41 | -4.2% |
| Draw | 25.5% | 24.8% | 3.80 | -3.0% |
| Strasbourg win | 34.7% | 34.0% | 3.05 | +5.8% |
| Over 2.5 | 54.3% | 57.7% | 1.71 | -7.1% |
| Under 2.5 | 45.7% | 42.3% | 2.40 | +9.6% |

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
| Market best home last update utc | 2026-10-11T08:23:10Z |
| Market best draw last update utc | 2026-10-11T08:23:10Z |
| Market best away last update utc | 2026-10-11T08:23:09Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Tipico |
| Matched home-team name | Nice |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.0% |
| P btts no | 42.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.99 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.60 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.14 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.24 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 38.4% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 58.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.75 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | -1.4% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | -0.0279 |
| Raw ev home | -0.0752 |
| Raw edge prob draw | 0.0146 |
| Raw ev draw | -0.0021 |
| Raw edge prob away | 0.0134 |
| Raw ev away | 0.0786 |

</details>


---

## 2026-10-11 — Rennes vs Auxerre

The model's most likely 1X2 outcome is **Rennes win** at **60.7%**. Expected goals are 1.84 for Rennes and 1.14 for Auxerre (2.98 combined). The most likely exact score is 2-1 at 11.2%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 58.8%; Under 3.5 goals: 64.4%; Under 4.5 goals: 81.1%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 60.7% | 1.65 |
| Draw | 20.5% | 4.88 |
| Auxerre win | 18.8% | 5.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.84 |
| Auxerre expected goals | 1.14 |
| Expected total goals | 2.98 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 35.6% |
| Under 3.5 | 64.4% |
| Over 4.5 | 18.9% |
| Under 4.5 | 81.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.21% |
| 2 | 1-0 | 10.02% |
| 3 | 2-0 | 9.80% |
| 4 | 1-1 | 9.60% |
| 5 | 3-1 | 6.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 60.7% | 68.4% | 1.47 | -10.7% |
| Draw | 20.5% | 17.1% | 5.40 | +10.7% |
| Auxerre win | 18.8% | 14.6% | 7.50 | +40.9% |
| Over 2.5 | 58.8% | 66.1% | 1.50 | -11.8% |
| Under 2.5 | 41.2% | 33.9% | 2.72 | +12.1% |

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
| Market best home last update utc | 2026-10-11T08:23:10Z |
| Market best draw last update utc | 2026-10-11T08:23:09Z |
| Market best away last update utc | 2026-10-11T08:22:53Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | LeoVegas (SE) |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Rennes |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.79 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.23 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.28 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 53.1% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 80.4% |
| Raw p under 3 5 | 65.1% |
| Raw p btts yes | 57.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.42 |
| Reference draw odds | 5.10 |
| Reference away odds | 5.90 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.68 |
| Home probability edge | -7.6% |
| Draw probability edge | +3.4% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.1527 |
| Raw ev home | -0.2196 |
| Raw edge prob draw | 0.0685 |
| Raw ev draw | 0.2916 |
| Raw edge prob away | 0.0842 |
| Raw ev away | 0.7245 |

</details>


---

## 2026-10-11 — Troyes vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **61.2%**. Expected goals are 0.92 for Troyes and 2.68 for Marseille (3.60 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 67.1%; Under 3.5 goals: 54.1%; Under 4.5 goals: 72.8%; BTTS Yes (both teams score): 58.8%; BTTS No (at least one team does not score): 41.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 19.0% | 5.26 |
| Draw | 19.8% | 5.05 |
| Marseille win | 61.2% | 1.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.92 |
| Marseille expected goals | 2.68 |
| Expected total goals | 3.60 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 86.3% |
| Under 1.5 | 13.7% |
| Over 2.5 | 67.1% |
| Under 2.5 | 32.9% |
| Over 3.5 | 45.9% |
| Under 3.5 | 54.1% |
| Over 4.5 | 27.2% |
| Under 4.5 | 72.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.97% |
| 2 | 0-2 | 8.07% |
| 3 | 1-2 | 7.45% |
| 4 | 0-3 | 7.21% |
| 5 | 1-3 | 6.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 19.0% | 27.9% | 3.85 | -26.9% |
| Draw | 19.8% | 24.0% | 3.86 | -23.5% |
| Marseille win | 61.2% | 48.2% | 2.10 | +28.5% |
| Over 2.5 | 67.1% | 59.3% | 1.67 | +12.0% |
| Under 2.5 | 32.9% | 40.7% | 2.41 | -20.7% |

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
| Market best home last update utc | 2026-10-11T08:22:22Z |
| Market best draw last update utc | 2026-10-11T08:23:10Z |
| Market best away last update utc | 2026-10-11T08:23:09Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.8% |
| P btts no | 41.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.70 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.30 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.04 |
| Fair Over 3.5 odds | 2.18 |
| Fair Under 3.5 odds | 1.85 |
| Fair Over 4.5 odds | 3.67 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 15.7% |
| Unadjusted away-win probability | 74.2% |
| Raw p over 1 5 | 87.8% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 56.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.98 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.41 |
| Home probability edge | -8.9% |
| Draw probability edge | -4.2% |
| Away probability edge | +13.0% |
| Over 2.5 probability edge | +7.8% |
| Under 2.5 probability edge | -7.8% |
| Raw edge prob home | -0.1776 |
| Raw ev home | -0.6104 |
| Raw edge prob draw | -0.0830 |
| Raw ev draw | -0.3951 |
| Raw edge prob away | 0.2606 |
| Raw ev away | 0.5584 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:22:54Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 62.3% |
| Market under 3 5 odds | 1.60 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T08:22:54Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.54 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 62.5% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-11T08:22:37Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.40 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-16 — Le Mans FC vs Toulouse

The model's most likely 1X2 outcome is **Le Mans FC win** at **38.7%**. Expected goals are 1.87 for Le Mans FC and 1.51 for Toulouse (3.37 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 65.1%; Under 3.5 goals: 56.7%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 66.6%; BTTS No (at least one team does not score): 33.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 38.7% | 2.58 |
| Draw | 24.3% | 4.11 |
| Toulouse win | 37.0% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Mans FC expected goals | 1.87 |
| Toulouse expected goals | 1.51 |
| Expected total goals | 3.37 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.1% |
| Under 2.5 | 34.9% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.55% |
| 2 | 1-2 | 8.71% |
| 3 | 2-1 | 7.61% |
| 4 | 2-2 | 7.05% |
| 5 | 0-1 | 5.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 38.7% | 31.6% | 3.25 | +25.8% |
| Draw | 24.3% | 25.2% | 3.57 | -13.2% |
| Toulouse win | 37.0% | 43.1% | 2.34 | -13.4% |
| Over 2.5 | 65.1% | 53.6% | 1.84 | +19.7% |
| Under 2.5 | 34.9% | 46.4% | 2.12 | -25.9% |

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
| Market best home last update utc | 2026-10-11T08:23:10Z |
| Market best draw last update utc | 2026-10-11T08:23:10Z |
| Market best away last update utc | 2026-10-11T08:23:10Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Mans |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.6% |
| P btts no | 33.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.47 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.81 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.04 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 45.7% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 30.9% |
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 66.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | +7.1% |
| Draw probability edge | -0.9% |
| Away probability edge | -6.1% |
| Over 2.5 probability edge | +11.4% |
| Under 2.5 probability edge | -11.4% |
| Raw edge prob home | 0.1411 |
| Raw ev home | 0.4869 |
| Raw edge prob draw | -0.0186 |
| Raw ev draw | -0.1651 |
| Raw edge prob away | -0.1226 |
| Raw ev away | -0.2778 |
| Market p over 1 5 | 78.0% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:22:37Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 68.2% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:23:10Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.86 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 59.1% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-11T08:22:37Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.22 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **56.5%**. Expected goals are 1.76 for Lille and 0.94 for Brest (2.70 combined). The most likely exact score is 1-0 at 11.3%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 51.1%; Under 3.5 goals: 71.3%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 56.5% | 1.77 |
| Draw | 23.3% | 4.29 |
| Brest win | 20.2% | 4.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.76 |
| Brest expected goals | 0.94 |
| Expected total goals | 2.70 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 28.7% |
| Under 3.5 | 71.3% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.33% |
| 2 | 1-1 | 11.12% |
| 3 | 2-0 | 10.47% |
| 4 | 2-1 | 9.87% |
| 5 | 0-0 | 6.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 56.5% | 57.0% | 1.73 | -2.2% |
| Draw | 23.3% | 22.1% | 4.35 | +1.5% |
| Brest win | 20.2% | 20.9% | 5.50 | +10.9% |
| Over 2.5 | 51.1% | 56.0% | 1.76 | -10.1% |
| Under 2.5 | 48.9% | 44.0% | 2.25 | +10.1% |

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
| Market best home last update utc | 2026-10-11T08:23:10Z |
| Market best draw last update utc | 2026-10-11T08:22:53Z |
| Market best away last update utc | 2026-10-11T08:22:53Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | LeoVegas (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Unibet (SE) |
| Matched home-team name | Lille |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.43 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.21 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 56.0% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 19.4% |
| Raw p over 1 5 | 75.7% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 51.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.66 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -0.5% |
| Draw probability edge | +1.2% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0098 |
| Raw ev home | -0.0310 |
| Raw edge prob draw | 0.0245 |
| Raw ev draw | 0.0679 |
| Raw edge prob away | -0.0147 |
| Raw ev away | 0.0691 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **63.5%**. Expected goals are 1.23 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 66.0%; Under 3.5 goals: 56.7%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 61.5%; BTTS No (at least one team does not score): 38.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 18.0% | 5.57 |
| Draw | 18.5% | 5.40 |
| Paris Saint Germain win | 63.5% | 1.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.23 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 66.0% |
| Under 2.5 | 34.0% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.83% |
| 2 | 0-2 | 8.83% |
| 3 | 1-1 | 8.27% |
| 4 | 0-1 | 7.87% |
| 5 | 1-3 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 18.0% | 14.6% | 6.73 | +20.8% |
| Draw | 18.5% | 15.3% | 5.90 | +9.2% |
| Paris Saint Germain win | 63.5% | 70.1% | 1.46 | -7.2% |
| Over 2.5 | 66.0% | 74.0% | 1.33 | -12.2% |
| Under 2.5 | 34.0% | 26.0% | 3.42 | +16.3% |

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
| Market best home last update utc | 2026-10-11T08:23:10Z |
| Market best draw last update utc | 2026-10-11T08:22:50Z |
| Market best away last update utc | 2026-10-11T08:23:10Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betclic (FR) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Strasbourg |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.5% |
| P btts no | 38.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.94 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.84 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.94 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 3.98 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 57.0% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.4% |
| Raw p btts yes | 62.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 5.50 |
| Reference draw odds | 5.30 |
| Reference away odds | 1.37 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.31 |
| Reference Under 2.5 odds | 3.35 |
| Home probability edge | +3.3% |
| Draw probability edge | +3.3% |
| Away probability edge | -6.6% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | 0.0665 |
| Raw ev home | 0.4321 |
| Raw edge prob draw | 0.0651 |
| Raw ev draw | 0.2837 |
| Raw edge prob away | -0.1316 |
| Raw ev away | -0.1683 |
| Market p over 1 5 | 95.5% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:22:37Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 7.20 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 47.8% |
| Market under 3 5 odds | 2.06 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T08:23:21Z |
| Market reference under 3 5 odds | 2.06 |
| Market reference under 3 5 opposite odds | 1.89 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 65.8% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-11T08:22:37Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 2.59 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **62.2%**. Expected goals are 0.78 for Troyes and 2.31 for RC Lens (3.09 combined). The most likely exact score is 0-2 at 10.6%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 57.9%; Under 3.5 goals: 64.3%; Under 4.5 goals: 81.1%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 17.4% | 5.76 |
| Draw | 20.5% | 4.89 |
| RC Lens win | 62.2% | 1.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.78 |
| RC Lens expected goals | 2.31 |
| Expected total goals | 3.09 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.9% |
| Under 2.5 | 42.1% |
| Over 3.5 | 35.7% |
| Under 3.5 | 64.3% |
| Over 4.5 | 18.9% |
| Under 4.5 | 81.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 10.57% |
| 2 | 1-1 | 9.73% |
| 3 | 0-1 | 8.78% |
| 4 | 1-2 | 8.27% |
| 5 | 0-3 | 8.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 17.4% | 24.1% | 4.30 | -25.3% |
| Draw | 20.5% | 22.8% | 4.04 | -17.4% |
| RC Lens win | 62.2% | 53.1% | 1.87 | +16.3% |
| Over 2.5 | 57.9% | 60.2% | 1.64 | -5.0% |
| Under 2.5 | 42.1% | 39.8% | 2.46 | +3.5% |

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
| Market best home last update utc | 2026-10-11T08:23:10Z |
| Market best draw last update utc | 2026-10-11T08:23:10Z |
| Market best away last update utc | 2026-10-11T08:23:10Z |
| Odds bookmakers 1x2 | 16.00 |
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
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.86 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.13 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.38 |
| Fair Over 3.5 odds | 2.80 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.29 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 10.6% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 71.3% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 49.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.65 |
| Reference draw odds | 3.85 |
| Reference away odds | 1.78 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Home probability edge | -6.8% |
| Draw probability edge | -2.3% |
| Away probability edge | +9.1% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | -0.1355 |
| Raw ev home | -0.5449 |
| Raw edge prob draw | -0.0463 |
| Raw ev draw | -0.2672 |
| Raw edge prob away | 0.1818 |
| Raw ev away | 0.3329 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **49.3%**. Expected goals are 0.95 for Angers and 1.65 for Marseille (2.59 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 48.1%; Under 3.5 goals: 74.0%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 50.0%; BTTS No (at least one team does not score): 50.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 25.7% | 3.89 |
| Draw | 24.9% | 4.01 |
| Marseille win | 49.3% | 2.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.95 |
| Marseille expected goals | 1.65 |
| Expected total goals | 2.59 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 73.4% |
| Under 1.5 | 26.6% |
| Over 2.5 | 48.1% |
| Under 2.5 | 51.9% |
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.86% |
| 2 | 0-1 | 10.85% |
| 3 | 0-2 | 9.40% |
| 4 | 1-2 | 8.90% |
| 5 | 1-0 | 7.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 25.7% | 30.5% | 3.25 | -16.3% |
| Draw | 24.9% | 24.1% | 3.85 | -4.1% |
| Marseille win | 49.3% | 45.4% | 2.28 | +12.5% |
| Over 2.5 | 48.1% | 58.8% | 1.68 | -19.3% |
| Under 2.5 | 51.9% | 41.2% | 2.40 | +24.7% |

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
| Market best home last update utc | 2026-10-11T08:22:53Z |
| Market best draw last update utc | 2026-10-11T08:23:09Z |
| Market best away last update utc | 2026-10-11T08:23:10Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | LeoVegas (SE) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Unibet (SE) |
| Matched home-team name | Angers |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.79 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.76 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.26 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 53.2% |
| Raw p over 1 5 | 73.8% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 50.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.05 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -4.7% |
| Draw probability edge | +0.8% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | -10.8% |
| Under 2.5 probability edge | +10.8% |
| Raw edge prob home | -0.0944 |
| Raw ev home | -0.3169 |
| Raw edge prob draw | 0.0163 |
| Raw ev draw | -0.0091 |
| Raw edge prob away | 0.0781 |
| Raw ev away | 0.2140 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **36.8%**. Expected goals are 1.16 for Le Havre and 1.19 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 42.1%; Under 3.5 goals: 79.0%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 36.8% | 2.72 |
| Draw | 28.0% | 3.58 |
| Auxerre win | 35.2% | 2.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.16 |
| Auxerre expected goals | 1.19 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 68.7% |
| Under 1.5 | 31.3% |
| Over 2.5 | 42.1% |
| Under 2.5 | 57.9% |
| Over 3.5 | 21.0% |
| Under 3.5 | 79.0% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.18% |
| 2 | 1-0 | 11.10% |
| 3 | 0-1 | 10.45% |
| 4 | 0-0 | 9.77% |
| 5 | 2-1 | 8.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 36.8% | 39.2% | 2.52 | -7.3% |
| Draw | 28.0% | 26.5% | 3.55 | -0.7% |
| Auxerre win | 35.2% | 34.3% | 3.00 | +5.7% |
| Over 2.5 | 42.1% | 51.0% | 1.94 | -18.4% |
| Under 2.5 | 57.9% | 49.0% | 2.00 | +15.9% |

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
| Market best home last update utc | 2026-10-11T08:23:10Z |
| Market best draw last update utc | 2026-10-11T08:22:53Z |
| Market best away last update utc | 2026-10-11T08:23:10Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Havre |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.24 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.38 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.75 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.07 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.0% |
| Raw p btts yes | 48.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.35 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | -2.4% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | -0.0470 |
| Raw ev home | -0.1318 |
| Raw edge prob draw | 0.0288 |
| Raw ev draw | 0.0440 |
| Raw edge prob away | 0.0183 |
| Raw ev away | 0.0843 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **48.1%**. Expected goals are 1.36 for Lorient and 1.84 for AS Monaco (3.21 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 61.9%; Under 3.5 goals: 60.2%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 27.4% | 3.65 |
| Draw | 24.5% | 4.08 |
| AS Monaco win | 48.1% | 2.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.36 |
| AS Monaco expected goals | 1.84 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 83.5% |
| Under 1.5 | 16.5% |
| Over 2.5 | 61.9% |
| Under 2.5 | 38.1% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.04% |
| 2 | 1-2 | 9.33% |
| 3 | 0-1 | 6.91% |
| 4 | 0-2 | 6.86% |
| 5 | 2-1 | 6.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 27.4% | 27.0% | 3.78 | +3.6% |
| Draw | 24.5% | 25.3% | 3.65 | -10.5% |
| AS Monaco win | 48.1% | 47.8% | 2.14 | +2.9% |
| Over 2.5 | 61.9% | 51.0% | 1.90 | +17.5% |
| Under 2.5 | 38.1% | 49.0% | 2.05 | -21.8% |

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
| Market best home last update utc | 2026-10-11T08:23:10Z |
| Market best draw last update utc | 2026-10-11T08:23:10Z |
| Market best away last update utc | 2026-10-11T08:22:53Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | LeoVegas (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lorient |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.15 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.04 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.62 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.56 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 27.9% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 83.5% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 63.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.50 |
| Reference away odds | 1.96 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | +0.5% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +10.9% |
| Under 2.5 probability edge | -10.9% |
| Raw edge prob home | 0.0091 |
| Raw ev home | 0.0533 |
| Raw edge prob draw | -0.0151 |
| Raw ev draw | -0.1328 |
| Raw edge prob away | 0.0061 |
| Raw ev away | 0.0352 |
| Market p over 1 5 | 79.0% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Codere (IT) |
| Market best over 1 5 last update utc | 2026-10-11T08:22:37Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 3.72 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:23:10Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 2.96 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 56.5% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-11T08:22:37Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.11 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **56.2%**. Expected goals are 1.78 for Lyon and 1.08 for Nice (2.86 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 55.1%; Under 3.5 goals: 67.6%; Under 4.5 goals: 83.5%; BTTS Yes (both teams score): 55.0%; BTTS No (at least one team does not score): 45.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 56.2% | 1.78 |
| Draw | 22.9% | 4.36 |
| Nice win | 20.8% | 4.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.78 |
| Nice expected goals | 1.08 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 78.7% |
| Under 1.5 | 21.3% |
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.5% |
| Under 4.5 | 83.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.87% |
| 2 | 2-1 | 10.36% |
| 3 | 1-0 | 10.18% |
| 4 | 2-0 | 9.59% |
| 5 | 3-1 | 6.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 56.2% | 59.3% | 1.71 | -3.8% |
| Draw | 22.9% | 21.4% | 4.20 | -3.7% |
| Nice win | 20.8% | 19.3% | 5.24 | +9.2% |
| Over 2.5 | 55.1% | 55.5% | 1.78 | -1.9% |
| Under 2.5 | 44.9% | 44.5% | 2.25 | +1.0% |

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
| Market best home last update utc | 2026-10-11T08:23:10Z |
| Market best draw last update utc | 2026-10-11T08:22:24Z |
| Market best away last update utc | 2026-10-11T08:23:10Z |
| Odds bookmakers 1x2 | 16.00 |
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
| P btts yes | 55.0% |
| P btts no | 45.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.93 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.69 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.07 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 53.1% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 22.4% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.60 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.21 |
| Home probability edge | -3.1% |
| Draw probability edge | +1.5% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.0616 |
| Raw ev home | -0.0912 |
| Raw edge prob draw | 0.0304 |
| Raw ev draw | 0.0272 |
| Raw edge prob away | 0.0313 |
| Raw ev away | 0.1736 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **43.2%**. Expected goals are 1.62 for Paris FC and 1.36 for Rennes (2.98 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.2%; Under 3.5 goals: 65.2%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 60.1%; BTTS No (at least one team does not score): 39.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 43.2% | 2.32 |
| Draw | 25.3% | 3.95 |
| Rennes win | 31.6% | 3.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.62 |
| Rennes expected goals | 1.36 |
| Expected total goals | 2.98 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 80.3% |
| Under 1.5 | 19.7% |
| Over 2.5 | 57.2% |
| Under 2.5 | 42.8% |
| Over 3.5 | 34.8% |
| Under 3.5 | 65.2% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.76% |
| 2 | 2-1 | 9.07% |
| 3 | 1-0 | 7.67% |
| 4 | 1-2 | 7.61% |
| 5 | 2-0 | 6.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 43.2% | 43.1% | 2.38 | +2.7% |
| Draw | 25.3% | 25.2% | 3.55 | -10.2% |
| Rennes win | 31.6% | 31.6% | 3.29 | +3.8% |
| Over 2.5 | 57.2% | 57.4% | 1.72 | -1.6% |
| Under 2.5 | 42.8% | 42.6% | 2.30 | -1.5% |

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
| Market best home last update utc | 2026-10-11T08:23:09Z |
| Market best draw last update utc | 2026-10-11T08:22:53Z |
| Market best away last update utc | 2026-10-11T08:23:10Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paris FC |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.1% |
| P btts no | 39.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.66 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.08 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.53 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 31.5% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 60.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.85 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +0.0% |
| Draw probability edge | +0.0% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.0006 |
| Raw ev home | 0.0277 |
| Raw edge prob draw | 0.0009 |
| Raw ev draw | -0.1007 |
| Raw edge prob away | -0.0015 |
| Raw ev away | 0.0359 |

</details>


---
