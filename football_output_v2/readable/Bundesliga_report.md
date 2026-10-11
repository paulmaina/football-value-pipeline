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
| Additional event odds calls used before this league | 7.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 2.00 |
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

The model's most likely 1X2 outcome is **1. FC Köln win** at **41.6%**. Expected goals are 1.43 for 1. FC Köln and 1.55 for Borussia Monchengladbach (2.97 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.4%; Under 3.5 goals: 65.3%; Under 4.5 goals: 81.8%; BTTS Yes (both teams score): 60.8%; BTTS No (at least one team does not score): 39.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 41.6% | 2.41 |
| Draw | 25.7% | 3.90 |
| Borussia Monchengladbach win | 32.8% | 3.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.43 |
| Borussia Monchengladbach expected goals | 1.55 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 57.4% |
| Under 2.5 | 42.6% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.2% |
| Under 4.5 | 81.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.96% |
| 2 | 2-1 | 9.85% |
| 3 | 1-0 | 7.48% |
| 4 | 1-2 | 7.27% |
| 5 | 2-0 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 41.6% | 49.2% | 2.06 | -14.4% |
| Draw | 25.7% | 24.6% | 4.10 | +5.2% |
| Borussia Monchengladbach win | 32.8% | 26.2% | 3.80 | +24.5% |
| Over 2.5 | 57.4% | 62.5% | 1.55 | -11.0% |
| Under 2.5 | 42.6% | 37.5% | 2.50 | +6.4% |

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
| Market best home last update utc | 2026-10-11T11:25:51Z |
| Market best draw last update utc | 2026-10-11T11:25:38Z |
| Market best away last update utc | 2026-10-11T11:25:51Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Nordic Bet |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | FC Koln |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.57 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.23 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.51 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 33.9% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 39.4% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 61.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.91 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Home probability edge | -7.7% |
| Draw probability edge | +1.1% |
| Away probability edge | +6.6% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | -0.1531 |
| Raw ev home | -0.3013 |
| Raw edge prob draw | 0.0213 |
| Raw ev draw | 0.0957 |
| Raw edge prob away | 0.1318 |
| Raw ev away | 0.4956 |
| Market p over 1 5 | 84.2% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T11:25:17Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 60.0% |
| Market under 3 5 odds | 1.68 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T11:25:31Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.38 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 64.0% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:26:20Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.72 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — SC Freiburg vs FC Schalke 04

The model's most likely 1X2 outcome is **SC Freiburg win** at **45.8%**. Expected goals are 0.90 for SC Freiburg and 0.80 for FC Schalke 04 (1.70 combined). The most likely exact score is 1-0 at 20.0%. Goal-market probabilities: at least one goal: 83.9%; Over 2.5 goals: 26.2%; Under 3.5 goals: 90.3%; Under 4.5 goals: 96.7%; BTTS Yes (both teams score): 32.8%; BTTS No (at least one team does not score): 67.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 45.8% | 2.18 |
| Draw | 30.1% | 3.32 |
| FC Schalke 04 win | 24.1% | 4.15 |

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
| Over 4.5 | 3.3% |
| Under 4.5 | 96.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.04% |
| 2 | 0-0 | 16.08% |
| 3 | 1-1 | 11.93% |
| 4 | 0-1 | 11.02% |
| 5 | 2-0 | 9.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 45.8% | 57.4% | 1.74 | -20.3% |
| Draw | 30.1% | 23.5% | 4.10 | +23.5% |
| FC Schalke 04 win | 24.1% | 19.1% | 5.50 | +32.5% |
| Over 2.5 | 26.2% | 57.9% | 1.72 | -54.9% |
| Under 2.5 | 73.8% | 42.1% | 2.31 | +70.4% |

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
| Market best home last update utc | 2026-10-11T11:25:01Z |
| Market best draw last update utc | 2026-10-11T11:26:05Z |
| Market best away last update utc | 2026-10-11T11:26:05Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Freiburg |
| Matched away-team name | Schalke 04 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.8% |
| P btts no | 67.2% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.22 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.12 |
| Fair Over 2.5 odds | 3.81 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 10.34 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.77 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 34.2% |
| Unadjusted draw probability | 36.7% |
| Unadjusted away-win probability | 29.1% |
| Raw p over 1 5 | 52.1% |
| Raw p under 3 5 | 90.6% |
| Raw p btts yes | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.67 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.60 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -11.6% |
| Draw probability edge | +6.6% |
| Away probability edge | +5.0% |
| Over 2.5 probability edge | -31.7% |
| Under 2.5 probability edge | +31.7% |
| Raw edge prob home | -0.2312 |
| Raw ev home | -0.4044 |
| Raw edge prob draw | 0.1319 |
| Raw ev draw | 0.5053 |
| Raw edge prob away | 0.0993 |
| Raw ev away | 0.5979 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T11:25:35Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 63.7% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T11:25:35Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:26:05Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.38 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-16 — Eintracht Frankfurt vs 1. FC Köln

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **56.0%**. Expected goals are 2.20 for Eintracht Frankfurt and 1.06 for 1. FC Köln (3.26 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 62.6%; Under 3.5 goals: 59.8%; Under 4.5 goals: 77.6%; BTTS Yes (both teams score): 59.7%; BTTS No (at least one team does not score): 40.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 56.0% | 1.79 |
| Draw | 22.2% | 4.51 |
| 1. FC Köln win | 21.8% | 4.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 2.20 |
| 1. FC Köln expected goals | 1.06 |
| Expected total goals | 3.26 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.6% |
| Under 2.5 | 37.4% |
| Over 3.5 | 40.2% |
| Under 3.5 | 59.8% |
| Over 4.5 | 22.4% |
| Under 4.5 | 77.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.23% |
| 2 | 2-1 | 8.85% |
| 3 | 2-0 | 8.36% |
| 4 | 1-0 | 6.76% |
| 5 | 3-1 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 56.0% | 49.6% | 2.00 | +12.0% |
| Draw | 22.2% | 22.9% | 4.30 | -4.6% |
| 1. FC Köln win | 21.8% | 27.5% | 3.70 | -19.2% |
| Over 2.5 | 62.6% | 70.1% | 1.40 | -12.4% |
| Under 2.5 | 37.4% | 29.9% | 3.07 | +14.9% |

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
| Market best home last update utc | 2026-10-11T11:25:01Z |
| Market best draw last update utc | 2026-10-11T11:25:01Z |
| Market best away last update utc | 2026-10-11T11:25:35Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Tipico |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 81/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 59.7% |
| P btts no | 40.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.22 |
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
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.91 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.07 |
| Home probability edge | +6.3% |
| Draw probability edge | -0.7% |
| Away probability edge | -5.6% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | 0.1270 |
| Raw ev home | 0.2465 |
| Raw edge prob draw | -0.0146 |
| Raw ev draw | -0.0776 |
| Raw edge prob away | -0.1123 |
| Raw ev away | -0.3997 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **73.6%**. Expected goals are 2.79 for Bayern Munich and 1.24 for RB Leipzig (4.02 combined). The most likely exact score is 2-1 at 9.2%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 77.3%; Under 3.5 goals: 42.2%; Under 4.5 goals: 61.7%; BTTS Yes (both teams score): 66.5%; BTTS No (at least one team does not score): 33.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 73.6% | 1.36 |
| Draw | 15.4% | 6.49 |
| RB Leipzig win | 11.0% | 9.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.79 |
| RB Leipzig expected goals | 1.24 |
| Expected total goals | 4.02 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 91.9% |
| Under 1.5 | 8.1% |
| Over 2.5 | 77.3% |
| Under 2.5 | 22.7% |
| Over 3.5 | 57.8% |
| Under 3.5 | 42.2% |
| Over 4.5 | 38.3% |
| Under 4.5 | 61.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.15% |
| 2 | 3-1 | 8.50% |
| 3 | 2-0 | 7.41% |
| 4 | 3-0 | 6.88% |
| 5 | 1-1 | 6.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 73.6% | 78.1% | 1.27 | -6.5% |
| Draw | 15.4% | 13.7% | 8.00 | +23.2% |
| RB Leipzig win | 11.0% | 8.2% | 11.20 | +23.3% |
| Over 2.5 | 77.3% | 83.9% | 1.17 | -9.6% |
| Under 2.5 | 22.7% | 16.1% | 5.14 | +16.7% |

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
| Market best home last update utc | 2026-10-11T11:25:01Z |
| Market best draw last update utc | 2026-10-11T11:25:39Z |
| Market best away last update utc | 2026-10-11T11:25:01Z |
| Odds bookmakers 1x2 | 19.00 |
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
| P btts yes | 66.5% |
| P btts no | 33.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.58 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.38 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.40 |
| Fair Over 3.5 odds | 1.73 |
| Fair Under 3.5 odds | 2.37 |
| Fair Over 4.5 odds | 2.61 |
| Fair Under 4.5 odds | 1.62 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 13.8% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 42.9% |
| Raw p btts yes | 67.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.25 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.17 |
| Reference Under 2.5 odds | 5.14 |
| Home probability edge | -4.5% |
| Draw probability edge | +1.7% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | -0.0896 |
| Raw ev home | -0.1222 |
| Raw edge prob draw | 0.0339 |
| Raw ev draw | 0.3676 |
| Raw edge prob away | 0.0556 |
| Raw ev away | 0.5445 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **56.1%**. Expected goals are 2.96 for Elversberg and 1.17 for Augsburg (4.13 combined). The most likely exact score is 1-1 at 8.1%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 75.4%; Under 3.5 goals: 43.9%; Under 4.5 goals: 63.3%; BTTS Yes (both teams score): 68.8%; BTTS No (at least one team does not score): 31.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 56.1% | 1.78 |
| Draw | 20.3% | 4.92 |
| Augsburg win | 23.6% | 4.24 |

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
| Over 2.5 | 75.4% |
| Under 2.5 | 24.6% |
| Over 3.5 | 56.1% |
| Under 3.5 | 43.9% |
| Over 4.5 | 36.7% |
| Under 4.5 | 63.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.09% |
| 2 | 1-2 | 6.74% |
| 3 | 2-2 | 6.33% |
| 4 | 2-1 | 6.32% |
| 5 | 3-1 | 6.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 56.1% | 39.0% | 2.55 | +43.0% |
| Draw | 20.3% | 25.2% | 4.00 | -18.6% |
| Augsburg win | 23.6% | 35.8% | 2.75 | -35.2% |
| Over 2.5 | 75.4% | 66.5% | 1.46 | +10.1% |
| Under 2.5 | 24.6% | 33.5% | 2.76 | -32.2% |

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
| Market best home last update utc | 2026-10-11T11:25:01Z |
| Market best draw last update utc | 2026-10-11T11:26:05Z |
| Market best away last update utc | 2026-10-11T11:26:05Z |
| Odds bookmakers 1x2 | 20.00 |
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
| Fair Under 0.5 odds | 34.67 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.37 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 4.07 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.28 |
| Fair Over 4.5 odds | 2.72 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 73.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.9% |
| Raw p btts yes | 65.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.40 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.60 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.76 |
| Home probability edge | +17.1% |
| Draw probability edge | -4.9% |
| Away probability edge | -12.2% |
| Over 2.5 probability edge | +8.9% |
| Under 2.5 probability edge | -8.9% |
| Raw edge prob home | 0.3415 |
| Raw ev home | 0.8655 |
| Raw edge prob draw | -0.0975 |
| Raw ev draw | -0.3813 |
| Raw edge prob away | -0.2441 |
| Raw ev away | -0.6871 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FC Schalke 04 win** at **34.6%**. Expected goals are 0.87 for FC Schalke 04 and 0.69 for FSV Mainz 05 (1.56 combined). The most likely exact score is 0-0 at 18.9%. Goal-market probabilities: at least one goal: 81.1%; Over 2.5 goals: 22.0%; Under 3.5 goals: 92.5%; Under 4.5 goals: 97.7%; BTTS Yes (both teams score): 29.2%; BTTS No (at least one team does not score): 70.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 34.6% | 2.89 |
| Draw | 32.4% | 3.08 |
| FSV Mainz 05 win | 33.0% | 3.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| FSV Mainz 05 expected goals | 0.69 |
| Expected total goals | 1.56 |
| Over 0.5 | 81.1% |
| Under 0.5 | 18.9% |
| Over 1.5 | 47.8% |
| Under 1.5 | 52.2% |
| Over 2.5 | 22.0% |
| Under 2.5 | 78.0% |
| Over 3.5 | 7.5% |
| Under 3.5 | 92.5% |
| Over 4.5 | 2.3% |
| Under 4.5 | 97.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.92% |
| 2 | 0-1 | 17.00% |
| 3 | 1-0 | 16.23% |
| 4 | 1-1 | 11.79% |
| 5 | 2-0 | 7.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 34.6% | 32.8% | 3.05 | +5.4% |
| Draw | 32.4% | 26.6% | 3.85 | +24.8% |
| FSV Mainz 05 win | 33.0% | 40.6% | 2.44 | -19.4% |
| Over 2.5 | 22.0% | 60.1% | 1.66 | -63.5% |
| Under 2.5 | 78.0% | 39.9% | 2.42 | +88.8% |

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
| Market best home last update utc | 2026-10-11T11:26:05Z |
| Market best draw last update utc | 2026-10-11T11:25:35Z |
| Market best away last update utc | 2026-10-11T11:25:01Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Coolbet |
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
| Fair Under 0.5 odds | 5.28 |
| Fair Over 1.5 odds | 2.09 |
| Fair Under 1.5 odds | 1.92 |
| Fair Over 2.5 odds | 4.55 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 13.42 |
| Fair Under 3.5 odds | 1.08 |
| Fair Over 4.5 odds | 43.42 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 36.3% |
| Unadjusted draw probability | 38.3% |
| Unadjusted away-win probability | 25.4% |
| Raw p over 1 5 | 47.5% |
| Raw p under 3 5 | 92.7% |
| Raw p btts yes | 30.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.80 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.30 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.33 |
| Home probability edge | +1.7% |
| Draw probability edge | +5.8% |
| Away probability edge | -7.6% |
| Over 2.5 probability edge | -38.1% |
| Under 2.5 probability edge | +38.1% |
| Raw edge prob home | 0.0348 |
| Raw ev home | 0.1070 |
| Raw edge prob draw | 0.1167 |
| Raw ev draw | 0.4730 |
| Raw edge prob away | -0.1515 |
| Raw ev away | -0.3791 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **54.7%**. Expected goals are 1.11 for Hamburger SV and 2.02 for VfB Stuttgart (3.13 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 60.3%; Under 3.5 goals: 62.1%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 59.4%; BTTS No (at least one team does not score): 40.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 21.7% | 4.62 |
| Draw | 23.6% | 4.23 |
| VfB Stuttgart win | 54.7% | 1.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.11 |
| VfB Stuttgart expected goals | 2.02 |
| Expected total goals | 3.13 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.99% |
| 2 | 1-2 | 9.44% |
| 3 | 0-2 | 8.50% |
| 4 | 0-1 | 7.45% |
| 5 | 1-3 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 21.7% | 24.0% | 4.30 | -6.8% |
| Draw | 23.6% | 24.0% | 4.40 | +4.0% |
| VfB Stuttgart win | 54.7% | 52.1% | 1.90 | +3.9% |
| Over 2.5 | 60.3% | 70.1% | 1.39 | -16.2% |
| Under 2.5 | 39.7% | 29.9% | 3.07 | +22.0% |

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
| Market best home last update utc | 2026-10-11T11:26:05Z |
| Market best draw last update utc | 2026-10-11T11:26:05Z |
| Market best away last update utc | 2026-10-11T11:25:01Z |
| Odds bookmakers 1x2 | 20.00 |
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
| Fair Under 0.5 odds | 18.26 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.81 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.88 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 19.4% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 57.3% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 61.8% |
| Raw p btts yes | 59.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 3.75 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.83 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.07 |
| Home probability edge | -2.3% |
| Draw probability edge | -0.3% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | -0.0462 |
| Raw ev home | -0.1675 |
| Raw edge prob draw | -0.0066 |
| Raw ev draw | 0.0257 |
| Raw edge prob away | 0.0528 |
| Raw ev away | 0.0893 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **58.3%**. Expected goals are 0.94 for Union Berlin and 1.92 for Borussia Dortmund (2.87 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 54.8%; Under 3.5 goals: 67.8%; Under 4.5 goals: 83.7%; BTTS Yes (both teams score): 53.1%; BTTS No (at least one team does not score): 46.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 18.6% | 5.37 |
| Draw | 23.1% | 4.34 |
| Borussia Dortmund win | 58.3% | 1.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.92 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 79.0% |
| Under 1.5 | 21.0% |
| Over 2.5 | 54.8% |
| Under 2.5 | 45.2% |
| Over 3.5 | 32.2% |
| Under 3.5 | 67.8% |
| Over 4.5 | 16.3% |
| Under 4.5 | 83.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.00% |
| 2 | 0-2 | 10.37% |
| 3 | 1-2 | 9.76% |
| 4 | 0-1 | 9.72% |
| 5 | 0-3 | 6.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 18.6% | 20.4% | 5.40 | +0.5% |
| Draw | 23.1% | 22.2% | 4.50 | +3.8% |
| Borussia Dortmund win | 58.3% | 57.3% | 1.73 | +0.9% |
| Over 2.5 | 54.8% | 64.3% | 1.51 | -17.2% |
| Under 2.5 | 45.2% | 35.7% | 2.61 | +17.9% |

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
| Market best home last update utc | 2026-10-11T11:26:05Z |
| Market best draw last update utc | 2026-10-11T11:25:51Z |
| Market best away last update utc | 2026-10-11T11:25:01Z |
| Odds bookmakers 1x2 | 20.00 |
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
| P btts yes | 53.1% |
| P btts no | 46.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.29 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.76 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.13 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 16.8% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 59.3% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 53.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 4.33 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.67 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Home probability edge | -1.8% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.0359 |
| Raw ev home | -0.0916 |
| Raw edge prob draw | 0.0165 |
| Raw ev draw | 0.0751 |
| Raw edge prob away | 0.0194 |
| Raw ev away | 0.0257 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **49.5%**. Expected goals are 1.16 for Werder Bremen and 0.74 for SC Paderborn (1.91 combined). The most likely exact score is 1-0 at 17.8%. Goal-market probabilities: at least one goal: 86.4%; Over 2.5 goals: 31.5%; Under 3.5 goals: 87.0%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 36.2%; BTTS No (at least one team does not score): 63.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 49.5% | 2.02 |
| Draw | 28.1% | 3.56 |
| SC Paderborn win | 22.4% | 4.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.16 |
| SC Paderborn expected goals | 0.74 |
| Expected total goals | 1.91 |
| Over 0.5 | 86.4% |
| Under 0.5 | 13.6% |
| Over 1.5 | 58.8% |
| Under 1.5 | 41.2% |
| Over 2.5 | 31.5% |
| Under 2.5 | 68.5% |
| Over 3.5 | 13.0% |
| Under 3.5 | 87.0% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.76% |
| 2 | 0-0 | 13.63% |
| 3 | 1-1 | 11.92% |
| 4 | 2-0 | 11.21% |
| 5 | 0-1 | 9.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 49.5% | 54.4% | 1.85 | -8.5% |
| Draw | 28.1% | 22.8% | 4.26 | +19.7% |
| SC Paderborn win | 22.4% | 22.8% | 4.21 | -5.6% |
| Over 2.5 | 31.5% | 62.4% | 1.55 | -51.2% |
| Under 2.5 | 68.5% | 37.6% | 2.48 | +69.9% |

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
| Market best home last update utc | 2026-10-11T11:25:35Z |
| Market best draw last update utc | 2026-10-11T11:25:01Z |
| Market best away last update utc | 2026-10-11T11:25:01Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 36.2% |
| P btts no | 63.8% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.34 |
| Fair Over 1.5 odds | 1.70 |
| Fair Under 1.5 odds | 2.43 |
| Fair Over 2.5 odds | 3.17 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.71 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.98 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 44.5% |
| Unadjusted draw probability | 33.4% |
| Unadjusted away-win probability | 22.1% |
| Raw p over 1 5 | 58.1% |
| Raw p under 3 5 | 87.4% |
| Raw p btts yes | 37.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.75 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.90 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Home probability edge | -5.0% |
| Draw probability edge | +5.3% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -30.9% |
| Under 2.5 probability edge | +30.9% |
| Raw edge prob home | -0.0993 |
| Raw ev home | -0.1767 |
| Raw edge prob draw | 0.1065 |
| Raw ev draw | 0.4242 |
| Raw edge prob away | -0.0072 |
| Raw ev away | -0.0710 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **64.2%**. Expected goals are 2.44 for Bayer Leverkusen and 0.96 for SC Freiburg (3.41 combined). The most likely exact score is 2-0 at 9.2%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 65.4%; Under 3.5 goals: 56.5%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 58.0%; BTTS No (at least one team does not score): 42.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 64.2% | 1.56 |
| Draw | 19.8% | 5.06 |
| SC Freiburg win | 16.0% | 6.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.44 |
| SC Freiburg expected goals | 0.96 |
| Expected total goals | 3.41 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 85.7% |
| Under 1.5 | 14.3% |
| Over 2.5 | 65.4% |
| Under 2.5 | 34.6% |
| Over 3.5 | 43.5% |
| Under 3.5 | 56.5% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.21% |
| 2 | 1-1 | 9.10% |
| 3 | 2-1 | 8.87% |
| 4 | 3-0 | 7.50% |
| 5 | 3-1 | 7.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 64.2% | 59.4% | 1.72 | +10.5% |
| Draw | 19.8% | 20.8% | 4.60 | -9.0% |
| SC Freiburg win | 16.0% | 19.8% | 4.83 | -22.8% |
| Over 2.5 | 65.4% | 65.6% | 1.48 | -3.2% |
| Under 2.5 | 34.6% | 34.4% | 2.69 | -6.9% |

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
| Market best home last update utc | 2026-10-11T11:26:05Z |
| Market best draw last update utc | 2026-10-11T11:25:35Z |
| Market best away last update utc | 2026-10-11T11:25:01Z |
| Odds bookmakers 1x2 | 18.00 |
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
| P btts yes | 58.0% |
| P btts no | 42.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.92 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.01 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.89 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.99 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.7% |
| Raw p btts yes | 57.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.61 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.69 |
| Home probability edge | +4.8% |
| Draw probability edge | -1.0% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0967 |
| Raw ev home | 0.1881 |
| Raw edge prob draw | -0.0208 |
| Raw ev draw | -0.1381 |
| Raw edge prob away | -0.0760 |
| Raw ev away | -0.4114 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **42.1%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 71.9%; Under 3.5 goals: 49.0%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 72.2%; BTTS No (at least one team does not score): 27.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 34.7% | 2.88 |
| Draw | 23.2% | 4.32 |
| TSG Hoffenheim win | 42.1% | 2.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.94 |
| TSG Hoffenheim expected goals | 1.79 |
| Expected total goals | 3.73 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 89.5% |
| Under 1.5 | 10.5% |
| Over 2.5 | 71.9% |
| Under 2.5 | 28.1% |
| Over 3.5 | 51.0% |
| Under 3.5 | 49.0% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.20% |
| 2 | 1-2 | 8.87% |
| 3 | 2-2 | 7.22% |
| 4 | 2-1 | 6.79% |
| 5 | 1-3 | 5.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 34.7% | 28.1% | 3.58 | +24.3% |
| Draw | 23.2% | 23.1% | 4.30 | -0.4% |
| TSG Hoffenheim win | 42.1% | 48.7% | 2.00 | -15.8% |
| Over 2.5 | 71.9% | 70.0% | 1.40 | +0.6% |
| Under 2.5 | 28.1% | 30.0% | 3.05 | -14.2% |

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
| Market best home last update utc | 2026-10-11T11:25:01Z |
| Market best draw last update utc | 2026-10-11T11:25:35Z |
| Market best away last update utc | 2026-10-11T11:26:05Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
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
| Fair Under 0.5 odds | 30.54 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.48 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.56 |
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
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 3.25 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.95 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | +6.6% |
| Draw probability edge | +0.0% |
| Away probability edge | -6.6% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | 0.1315 |
| Raw ev home | 0.4780 |
| Raw edge prob draw | 0.0009 |
| Raw ev draw | -0.0018 |
| Raw edge prob away | -0.1324 |
| Raw ev away | -0.2899 |

</details>


---
