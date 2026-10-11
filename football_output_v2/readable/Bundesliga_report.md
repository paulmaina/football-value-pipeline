# Bundesliga — football model report

Fixtures in this report: **11**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 954 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 2887.213 |
| Base scoring parameter | 0.239 |
| Home-advantage parameter | 0.190 |
| Dixon-Coles low-score adjustment | -0.104 |
| Xi per day | 0 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 11.00 |
| Additional event odds calls used before this league | 8.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-11 — 1. FC Köln vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **1. FC Köln win** at **41.0%**. Expected goals are 1.43 for 1. FC Köln and 1.55 for Borussia Monchengladbach (2.97 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 57.4%; Under 3.5 goals: 65.3%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 41.0% | 2.44 |
| Draw | 25.9% | 3.86 |
| Borussia Monchengladbach win | 33.2% | 3.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.43 |
| Borussia Monchengladbach expected goals | 1.55 |
| Expected total goals | 2.97 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 57.4% |
| Under 2.5 | 42.6% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.06% |
| 2 | 2-1 | 9.71% |
| 3 | 1-0 | 7.37% |
| 4 | 1-2 | 7.36% |
| 5 | 2-0 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 41.0% | 48.0% | 2.04 | -16.4% |
| Draw | 25.9% | 25.0% | 4.10 | +6.1% |
| Borussia Monchengladbach win | 33.2% | 27.0% | 3.80 | +26.0% |
| Over 2.5 | 57.4% | 63.7% | 1.52 | -12.8% |
| Under 2.5 | 42.6% | 36.3% | 2.56 | +9.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:30:00+00:00 |
| Fixture id | a8801462cb97a43570956e4b3ef4aedf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:51Z |
| Market best draw last update utc | 2026-10-11T08:23:07Z |
| Market best away last update utc | 2026-10-11T08:22:51Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Koln |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.43 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.23 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.52 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 33.9% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 39.4% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 61.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.00 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.45 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.56 |
| Home probability edge | -7.0% |
| Draw probability edge | +0.8% |
| Away probability edge | +6.2% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.1409 |
| Raw ev home | -0.3081 |
| Raw edge prob draw | 0.0169 |
| Raw ev draw | 0.0957 |
| Raw edge prob away | 0.1240 |
| Raw ev away | 0.4956 |

</details>


---

## 2026-10-11 — SC Freiburg vs FC Schalke 04

The model's most likely 1X2 outcome is **SC Freiburg win** at **46.4%**. Expected goals are 0.90 for SC Freiburg and 0.80 for FC Schalke 04 (1.70 combined). The most likely exact score is 1-0 at 20.3%. Goal-market probabilities: at least one goal: 83.9%; Over 2.5 goals: 26.2%; Under 3.5 goals: 90.3%; Under 4.5 goals: 96.8%; BTTS Yes (both teams score): 32.8%; BTTS No (at least one team does not score): 67.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 46.4% | 2.16 |
| Draw | 30.2% | 3.31 |
| FC Schalke 04 win | 23.4% | 4.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 0.90 |
| FC Schalke 04 expected goals | 0.80 |
| Expected total goals | 1.70 |
| Over 0.5 | 83.9% |
| Under 0.5 | 16.1% |
| Over 1.5 | 52.9% |
| Under 1.5 | 47.1% |
| Over 2.5 | 26.2% |
| Under 2.5 | 73.8% |
| Over 3.5 | 9.7% |
| Under 3.5 | 90.3% |
| Over 4.5 | 3.2% |
| Under 4.5 | 96.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.31% |
| 2 | 0-0 | 16.12% |
| 3 | 1-1 | 11.96% |
| 4 | 0-1 | 10.70% |
| 5 | 2-0 | 9.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 46.4% | 58.6% | 1.74 | -19.3% |
| Draw | 30.2% | 23.7% | 4.12 | +24.4% |
| FC Schalke 04 win | 23.4% | 17.7% | 5.50 | +28.7% |
| Over 2.5 | 26.2% | 58.4% | 1.70 | -55.5% |
| Under 2.5 | 73.8% | 41.6% | 2.40 | +77.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T15:30:00+00:00 |
| Fixture id | eaf509fb37413b7d055cd394667792b3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:51Z |
| Market best draw last update utc | 2026-10-11T08:22:51Z |
| Market best away last update utc | 2026-10-11T08:22:19Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Freiburg |
| Matched away-team name | Schalke 04 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.8% |
| P btts no | 67.2% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.20 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.12 |
| Fair Over 2.5 odds | 3.82 |
| Fair Under 2.5 odds | 1.35 |
| Fair Over 3.5 odds | 10.34 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.78 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 34.2% |
| Unadjusted draw probability | 36.7% |
| Unadjusted away-win probability | 29.1% |
| Raw p over 1 5 | 52.1% |
| Raw p under 3 5 | 90.6% |
| Raw p btts yes | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.65 |
| Reference draw odds | 3.85 |
| Reference away odds | 5.05 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.26 |
| Home probability edge | -12.2% |
| Draw probability edge | +6.5% |
| Away probability edge | +5.7% |
| Over 2.5 probability edge | -32.2% |
| Under 2.5 probability edge | +32.2% |
| Raw edge prob home | -0.2434 |
| Raw ev home | -0.4044 |
| Raw edge prob draw | 0.1302 |
| Raw ev draw | 0.5127 |
| Raw edge prob away | 0.1132 |
| Raw ev away | 0.5979 |
| Market p over 1 5 | 83.3% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:23:07Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.25 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 62.8% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T08:23:07Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.51 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 57.9% |
| Market btts yes odds | 1.71 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:22:51Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.27 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-16 — Eintracht Frankfurt vs 1. FC Köln

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **56.2%**. Expected goals are 2.20 for Eintracht Frankfurt and 1.06 for 1. FC Köln (3.26 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 62.5%; Under 3.5 goals: 59.8%; Under 4.5 goals: 77.6%; BTTS Yes (both teams score): 59.7%; BTTS No (at least one team does not score): 40.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 56.2% | 1.78 |
| Draw | 22.3% | 4.48 |
| 1. FC Köln win | 21.5% | 4.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 2.20 |
| 1. FC Köln expected goals | 1.06 |
| Expected total goals | 3.26 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.5% |
| Under 2.5 | 37.5% |
| Over 3.5 | 40.2% |
| Under 3.5 | 59.8% |
| Over 4.5 | 22.4% |
| Under 4.5 | 77.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.30% |
| 2 | 2-1 | 8.87% |
| 3 | 2-0 | 8.38% |
| 4 | 1-0 | 6.78% |
| 5 | 3-1 | 6.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 56.2% | 50.0% | 2.00 | +12.3% |
| Draw | 22.3% | 23.2% | 4.30 | -4.0% |
| 1. FC Köln win | 21.5% | 26.8% | 3.65 | -21.5% |
| Over 2.5 | 62.5% | 70.1% | 1.40 | -12.5% |
| Under 2.5 | 37.5% | 29.9% | 3.07 | +15.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-16T18:30:00+00:00 |
| Fixture id | 947bd5d924835af090d9cdc7bbdf10f6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:51Z |
| Market best draw last update utc | 2026-10-11T08:22:51Z |
| Market best away last update utc | 2026-10-11T08:22:19Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 81/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 59.7% |
| P btts no | 40.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.08 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.28 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.49 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.46 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 62.3% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 16.2% |
| Raw p over 1 5 | 84.6% |
| Raw p under 3 5 | 59.0% |
| Raw p btts yes | 59.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.92 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.45 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.07 |
| Home probability edge | +6.2% |
| Draw probability edge | -0.9% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | 0.1234 |
| Raw ev home | 0.2465 |
| Raw edge prob draw | -0.0176 |
| Raw ev draw | -0.0776 |
| Raw edge prob away | -0.1058 |
| Raw ev away | -0.4078 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **74.3%**. Expected goals are 2.79 for Bayern Munich and 1.24 for RB Leipzig (4.02 combined). The most likely exact score is 2-1 at 9.2%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 77.4%; Under 3.5 goals: 42.1%; Under 4.5 goals: 61.6%; BTTS Yes (both teams score): 66.4%; BTTS No (at least one team does not score): 33.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 74.3% | 1.35 |
| Draw | 15.2% | 6.57 |
| RB Leipzig win | 10.4% | 9.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.79 |
| RB Leipzig expected goals | 1.24 |
| Expected total goals | 4.02 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 77.4% |
| Under 2.5 | 22.6% |
| Over 3.5 | 57.9% |
| Under 3.5 | 42.1% |
| Over 4.5 | 38.4% |
| Under 4.5 | 61.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.25% |
| 2 | 3-1 | 8.59% |
| 3 | 2-0 | 7.48% |
| 4 | 3-0 | 6.95% |
| 5 | 1-1 | 6.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 74.3% | 79.6% | 1.27 | -5.6% |
| Draw | 15.2% | 13.3% | 8.00 | +21.8% |
| RB Leipzig win | 10.4% | 7.1% | 11.20 | +16.9% |
| Over 2.5 | 77.4% | 83.9% | 1.17 | -9.5% |
| Under 2.5 | 22.6% | 16.1% | 5.14 | +16.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | 9a64448205fdc4b95f45641bb946706c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:51Z |
| Market best draw last update utc | 2026-10-11T08:23:07Z |
| Market best away last update utc | 2026-10-11T08:22:51Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Bayern Munich |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.4% |
| P btts no | 33.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.12 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.45 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.42 |
| Fair Over 3.5 odds | 1.73 |
| Fair Under 3.5 odds | 2.37 |
| Fair Over 4.5 odds | 2.60 |
| Fair Under 4.5 odds | 1.62 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 13.8% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 42.9% |
| Raw p btts yes | 67.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.23 |
| Reference draw odds | 6.20 |
| Reference away odds | 11.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.17 |
| Reference Under 2.5 odds | 5.14 |
| Home probability edge | -5.2% |
| Draw probability edge | +1.9% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.1045 |
| Raw ev home | -0.1222 |
| Raw edge prob draw | 0.0375 |
| Raw ev draw | 0.3676 |
| Raw edge prob away | 0.0670 |
| Raw ev away | 0.5445 |
| Market p over 1 5 | 95.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-11T08:22:31Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 13.00 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 30.6% |
| Market under 3 5 odds | 2.77 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:22:50Z |
| Market reference under 3 5 odds | 2.77 |
| Market reference under 3 5 opposite odds | 1.37 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 70.9% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:22:51Z |
| Market reference btts yes odds | 1.35 |
| Market reference btts yes opposite odds | 2.94 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **55.9%**. Expected goals are 2.96 for Elversberg and 1.17 for Augsburg (4.13 combined). The most likely exact score is 1-1 at 8.2%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 75.3%; Under 3.5 goals: 43.9%; Under 4.5 goals: 63.3%; BTTS Yes (both teams score): 68.8%; BTTS No (at least one team does not score): 31.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 55.9% | 1.79 |
| Draw | 20.6% | 4.86 |
| Augsburg win | 23.5% | 4.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.96 |
| Augsburg expected goals | 1.17 |
| Expected total goals | 4.13 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 75.3% |
| Under 2.5 | 24.7% |
| Over 3.5 | 56.1% |
| Under 3.5 | 43.9% |
| Over 4.5 | 36.7% |
| Under 4.5 | 63.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.19% |
| 2 | 1-2 | 6.71% |
| 3 | 2-2 | 6.41% |
| 4 | 2-1 | 6.30% |
| 5 | 3-1 | 6.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 55.9% | 38.7% | 2.55 | +42.6% |
| Draw | 20.6% | 25.7% | 4.00 | -17.6% |
| Augsburg win | 23.5% | 35.6% | 2.75 | -35.4% |
| Over 2.5 | 75.3% | 66.5% | 1.46 | +10.0% |
| Under 2.5 | 24.7% | 33.5% | 2.76 | -31.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 0bf757f3bd903496ce2fa27bd0481869 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:51Z |
| Market best draw last update utc | 2026-10-11T08:22:19Z |
| Market best away last update utc | 2026-10-11T08:22:19Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Elversberg |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 68.8% |
| P btts no | 31.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.24 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.35 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 4.05 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.28 |
| Fair Over 4.5 odds | 2.73 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 73.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.9% |
| Raw p btts yes | 65.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.45 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.76 |
| Home probability edge | +17.2% |
| Draw probability edge | -5.1% |
| Away probability edge | -12.1% |
| Over 2.5 probability edge | +8.8% |
| Under 2.5 probability edge | -8.8% |
| Raw edge prob home | 0.3447 |
| Raw ev home | 0.8655 |
| Raw edge prob draw | -0.1026 |
| Raw ev draw | -0.3813 |
| Raw edge prob away | -0.2422 |
| Raw ev away | -0.6871 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:22:52Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 55.3% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T08:21:08Z |
| Market reference under 3 5 odds | 1.74 |
| Market reference under 3 5 opposite odds | 2.12 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:22:51Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.80 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FC Schalke 04 win** at **34.8%**. Expected goals are 0.87 for FC Schalke 04 and 0.69 for FSV Mainz 05 (1.56 combined). The most likely exact score is 0-0 at 18.9%. Goal-market probabilities: at least one goal: 81.1%; Over 2.5 goals: 22.0%; Under 3.5 goals: 92.5%; Under 4.5 goals: 97.7%; BTTS Yes (both teams score): 29.2%; BTTS No (at least one team does not score): 70.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 34.8% | 2.88 |
| Draw | 32.3% | 3.09 |
| FSV Mainz 05 win | 32.9% | 3.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| FSV Mainz 05 expected goals | 0.69 |
| Expected total goals | 1.56 |
| Over 0.5 | 81.1% |
| Under 0.5 | 18.9% |
| Over 1.5 | 47.9% |
| Under 1.5 | 52.1% |
| Over 2.5 | 22.0% |
| Under 2.5 | 78.0% |
| Over 3.5 | 7.5% |
| Under 3.5 | 92.5% |
| Over 4.5 | 2.3% |
| Under 4.5 | 97.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.87% |
| 2 | 0-1 | 16.93% |
| 3 | 1-0 | 16.33% |
| 4 | 1-1 | 11.76% |
| 5 | 2-0 | 7.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 34.8% | 33.2% | 3.05 | +6.0% |
| Draw | 32.3% | 26.4% | 3.80 | +22.9% |
| FSV Mainz 05 win | 32.9% | 40.3% | 2.44 | -19.7% |
| Over 2.5 | 22.0% | 60.3% | 1.66 | -63.4% |
| Under 2.5 | 78.0% | 39.7% | 2.42 | +88.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 606d65d57a9a6d8f9b53faee1ad10009 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:19Z |
| Market best draw last update utc | 2026-10-11T08:22:51Z |
| Market best away last update utc | 2026-10-11T08:22:51Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Schalke 04 |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 29.2% |
| P btts no | 70.8% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.30 |
| Fair Over 1.5 odds | 2.09 |
| Fair Under 1.5 odds | 1.92 |
| Fair Over 2.5 odds | 4.54 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 13.41 |
| Fair Under 3.5 odds | 1.08 |
| Fair Over 4.5 odds | 43.36 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 36.3% |
| Unadjusted draw probability | 38.3% |
| Unadjusted away-win probability | 25.4% |
| Raw p over 1 5 | 47.5% |
| Raw p under 3 5 | 92.7% |
| Raw p btts yes | 30.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.82 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.35 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.36 |
| Home probability edge | +1.5% |
| Draw probability edge | +5.9% |
| Away probability edge | -7.4% |
| Over 2.5 probability edge | -38.3% |
| Under 2.5 probability edge | +38.3% |
| Raw edge prob home | 0.0306 |
| Raw ev home | 0.1070 |
| Raw edge prob draw | 0.1184 |
| Raw ev draw | 0.4539 |
| Raw edge prob away | -0.1490 |
| Raw ev away | -0.3791 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:22:52Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 61.8% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:22:50Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.43 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:22:51Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **54.7%**. Expected goals are 1.11 for Hamburger SV and 2.02 for VfB Stuttgart (3.13 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 60.4%; Under 3.5 goals: 62.1%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 59.4%; BTTS No (at least one team does not score): 40.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 21.9% | 4.56 |
| Draw | 23.4% | 4.27 |
| VfB Stuttgart win | 54.7% | 1.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.11 |
| VfB Stuttgart expected goals | 2.02 |
| Expected total goals | 3.13 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 60.4% |
| Under 2.5 | 39.6% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.88% |
| 2 | 1-2 | 9.44% |
| 3 | 0-2 | 8.50% |
| 4 | 0-1 | 7.44% |
| 5 | 1-3 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 21.9% | 24.5% | 4.30 | -5.7% |
| Draw | 23.4% | 23.5% | 4.40 | +3.0% |
| VfB Stuttgart win | 54.7% | 52.0% | 1.90 | +3.8% |
| Over 2.5 | 60.4% | 70.1% | 1.39 | -16.1% |
| Under 2.5 | 39.6% | 29.9% | 3.07 | +21.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 221916b8b36706ec52aa655a64e5f1d2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:19Z |
| Market best draw last update utc | 2026-10-11T08:22:19Z |
| Market best away last update utc | 2026-10-11T08:22:51Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Hamburg |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 88/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 59.4% |
| P btts no | 40.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.44 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.81 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.87 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 19.4% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 57.3% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 61.8% |
| Raw p btts yes | 59.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 3.75 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.85 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.07 |
| Home probability edge | -2.6% |
| Draw probability edge | -0.1% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | -9.8% |
| Under 2.5 probability edge | +9.8% |
| Raw edge prob home | -0.0515 |
| Raw ev home | -0.1675 |
| Raw edge prob draw | -0.0020 |
| Raw ev draw | 0.0257 |
| Raw edge prob away | 0.0535 |
| Raw ev away | 0.0893 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **59.5%**. Expected goals are 0.94 for Union Berlin and 1.92 for Borussia Dortmund (2.87 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 54.9%; Under 3.5 goals: 67.7%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 53.0%; BTTS No (at least one team does not score): 47.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.4% | 5.74 |
| Draw | 23.1% | 4.33 |
| Borussia Dortmund win | 59.5% | 1.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.92 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 54.9% |
| Under 2.5 | 45.1% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.02% |
| 2 | 0-2 | 10.58% |
| 3 | 1-2 | 9.95% |
| 4 | 0-1 | 9.91% |
| 5 | 0-3 | 6.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.4% | 18.0% | 5.40 | -5.9% |
| Draw | 23.1% | 22.3% | 4.50 | +4.0% |
| Borussia Dortmund win | 59.5% | 59.6% | 1.73 | +2.9% |
| Over 2.5 | 54.9% | 64.3% | 1.51 | -17.1% |
| Under 2.5 | 45.1% | 35.7% | 2.61 | +17.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | d8eac776adb07b0e7f01d8736d097291 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:19Z |
| Market best draw last update utc | 2026-10-11T08:22:51Z |
| Market best away last update utc | 2026-10-11T08:22:51Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Union Berlin |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 53.0% |
| P btts no | 47.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.26 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.78 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.10 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.11 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 16.8% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 59.3% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 53.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 4.95 |
| Reference draw odds | 4.05 |
| Reference away odds | 1.62 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Home probability edge | -0.6% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.0120 |
| Raw ev home | -0.0916 |
| Raw edge prob draw | 0.0155 |
| Raw ev draw | 0.0751 |
| Raw edge prob away | -0.0035 |
| Raw ev away | 0.0257 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **49.3%**. Expected goals are 1.16 for Werder Bremen and 0.74 for SC Paderborn (1.91 combined). The most likely exact score is 1-0 at 17.7%. Goal-market probabilities: at least one goal: 86.0%; Over 2.5 goals: 31.3%; Under 3.5 goals: 87.0%; Under 4.5 goals: 95.3%; BTTS Yes (both teams score): 36.3%; BTTS No (at least one team does not score): 63.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 49.3% | 2.03 |
| Draw | 28.8% | 3.47 |
| SC Paderborn win | 21.9% | 4.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.16 |
| SC Paderborn expected goals | 0.74 |
| Expected total goals | 1.91 |
| Over 0.5 | 86.0% |
| Under 0.5 | 14.0% |
| Over 1.5 | 58.7% |
| Under 1.5 | 41.3% |
| Over 2.5 | 31.3% |
| Under 2.5 | 68.7% |
| Over 3.5 | 13.0% |
| Under 3.5 | 87.0% |
| Over 4.5 | 4.7% |
| Under 4.5 | 95.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.71% |
| 2 | 0-0 | 13.96% |
| 3 | 1-1 | 12.21% |
| 4 | 2-0 | 11.18% |
| 5 | 0-1 | 9.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 49.3% | 54.1% | 1.84 | -9.3% |
| Draw | 28.8% | 24.2% | 4.30 | +23.8% |
| SC Paderborn win | 21.9% | 21.7% | 4.21 | -7.8% |
| Over 2.5 | 31.3% | 62.4% | 1.55 | -51.5% |
| Under 2.5 | 68.7% | 37.6% | 2.48 | +70.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 9a422e1aad1053828eaf629a58d901de |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:51Z |
| Market best draw last update utc | 2026-10-11T08:22:51Z |
| Market best away last update utc | 2026-10-11T08:22:51Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 36.3% |
| P btts no | 63.7% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.16 |
| Fair Over 1.5 odds | 1.70 |
| Fair Under 1.5 odds | 2.42 |
| Fair Over 2.5 odds | 3.20 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.72 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 21.12 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 44.5% |
| Unadjusted draw probability | 33.4% |
| Unadjusted away-win probability | 22.1% |
| Raw p over 1 5 | 58.1% |
| Raw p under 3 5 | 87.4% |
| Raw p btts yes | 37.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.78 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.20 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Home probability edge | -4.8% |
| Draw probability edge | +4.6% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -31.1% |
| Under 2.5 probability edge | +31.1% |
| Raw edge prob home | -0.0964 |
| Raw ev home | -0.1812 |
| Raw edge prob draw | 0.0928 |
| Raw ev draw | 0.4376 |
| Raw edge prob away | 0.0036 |
| Raw ev away | -0.0710 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **63.8%**. Expected goals are 2.44 for Bayer Leverkusen and 0.96 for SC Freiburg (3.41 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 65.1%; Under 3.5 goals: 56.6%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 58.2%; BTTS No (at least one team does not score): 41.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 63.8% | 1.57 |
| Draw | 20.6% | 4.85 |
| SC Freiburg win | 15.6% | 6.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.44 |
| SC Freiburg expected goals | 0.96 |
| Expected total goals | 3.41 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 85.7% |
| Under 1.5 | 14.3% |
| Over 2.5 | 65.1% |
| Under 2.5 | 34.9% |
| Over 3.5 | 43.4% |
| Under 3.5 | 56.6% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.48% |
| 2 | 2-0 | 9.15% |
| 3 | 2-1 | 8.81% |
| 4 | 3-0 | 7.45% |
| 5 | 3-1 | 7.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 63.8% | 58.6% | 1.72 | +9.8% |
| Draw | 20.6% | 22.5% | 4.60 | -5.2% |
| SC Freiburg win | 15.6% | 18.9% | 4.83 | -24.8% |
| Over 2.5 | 65.1% | 65.6% | 1.48 | -3.7% |
| Under 2.5 | 34.9% | 34.4% | 2.69 | -6.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:30:00+00:00 |
| Fixture id | 096d800bcc95c547ef592cbef624d080 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:19Z |
| Market best draw last update utc | 2026-10-11T08:22:19Z |
| Market best away last update utc | 2026-10-11T08:22:51Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Tipico |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Leverkusen |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.2% |
| P btts no | 41.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.00 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.98 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 4.01 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.7% |
| Raw p btts yes | 57.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.65 |
| Reference draw odds | 4.05 |
| Reference away odds | 4.75 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.69 |
| Home probability edge | +5.2% |
| Draw probability edge | -1.9% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.1049 |
| Raw ev home | 0.1881 |
| Raw edge prob draw | -0.0373 |
| Raw ev draw | -0.1381 |
| Raw edge prob away | -0.0676 |
| Raw ev away | -0.4114 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **42.4%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 71.8%; Under 3.5 goals: 49.0%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 72.2%; BTTS No (at least one team does not score): 27.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 34.3% | 2.91 |
| Draw | 23.3% | 4.30 |
| TSG Hoffenheim win | 42.4% | 2.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.94 |
| TSG Hoffenheim expected goals | 1.79 |
| Expected total goals | 3.73 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 71.8% |
| Under 2.5 | 28.2% |
| Over 3.5 | 51.0% |
| Under 3.5 | 49.0% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.25% |
| 2 | 1-2 | 8.93% |
| 3 | 2-2 | 7.25% |
| 4 | 2-1 | 6.72% |
| 5 | 1-3 | 5.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 34.3% | 27.4% | 3.58 | +22.9% |
| Draw | 23.3% | 23.3% | 4.26 | -0.8% |
| TSG Hoffenheim win | 42.4% | 49.3% | 2.00 | -15.2% |
| Over 2.5 | 71.8% | 70.0% | 1.40 | +0.6% |
| Under 2.5 | 28.2% | 30.0% | 3.05 | -14.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | fd9b8c185737a15615aa0c9daaa3dfbf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:51Z |
| Market best draw last update utc | 2026-10-11T08:22:51Z |
| Market best away last update utc | 2026-10-11T08:22:19Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | M'gladbach |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 72.2% |
| P btts no | 27.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.39 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.47 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.55 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 41.3% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.9% |
| Raw p btts yes | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 3.40 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.95 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | +7.0% |
| Draw probability edge | -0.1% |
| Away probability edge | -6.9% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | 0.1392 |
| Raw ev home | 0.4780 |
| Raw edge prob draw | -0.0013 |
| Raw ev draw | -0.0111 |
| Raw edge prob away | -0.1379 |
| Raw ev away | -0.2899 |

</details>


---
