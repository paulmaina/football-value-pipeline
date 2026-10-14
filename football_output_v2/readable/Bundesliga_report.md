# Bundesliga — football model report

Fixtures in this report: **10**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 963 |
| Training data through | 2026-10-11 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1719.052 |
| Base scoring parameter | 0.238 |
| Home-advantage parameter | 0.200 |
| Dixon-Coles low-score adjustment | -0.084 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-11', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 10.00 |
| Additional event odds calls used before this league | 1.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-16 — Eintracht Frankfurt vs 1. FC Köln

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **54.6%**. Expected goals are 2.24 for Eintracht Frankfurt and 1.24 for 1. FC Köln (3.48 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 67.1%; Under 3.5 goals: 54.6%; Double Chance 1X: 76.6%; Double Chance X2: 45.4%; Under 4.5 goals: 73.3%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 54.6% | 1.83 |
| Draw | 22.0% | 4.54 |
| 1. FC Köln win | 23.4% | 4.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 2.24 |
| 1. FC Köln expected goals | 1.24 |
| Expected total goals | 3.48 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 67.1% |
| Under 2.5 | 32.9% |
| Over 3.5 | 45.4% |
| Under 3.5 | 54.6% |
| Over 4.5 | 26.7% |
| Under 4.5 | 73.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.64% |
| 2 | 2-1 | 8.83% |
| 3 | 2-0 | 7.11% |
| 4 | 3-1 | 6.59% |
| 5 | 1-2 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 54.6% | 49.9% | 1.99 | +8.6% |
| Draw | 22.0% | 22.9% | 4.36 | -3.9% |
| 1. FC Köln win | 23.4% | 27.2% | 3.52 | -17.7% |

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
| Market best home last update utc | 2026-10-14T11:21:29Z |
| Market best draw last update utc | 2026-10-14T11:21:29Z |
| Market best away last update utc | 2026-10-14T11:21:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 81/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.37 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.50 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.04 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.75 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 59.2% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 19.6% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.1% |
| Raw p btts yes | 64.3% |
| P home draw | 76.6% |
| P draw away | 45.4% |
| Raw p home draw | 80.4% |
| Raw p draw away | 40.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.92 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.26 |
| Home probability edge | +4.6% |
| Draw probability edge | -0.8% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | 0.0924 |
| Raw ev home | 0.1778 |
| Raw edge prob draw | -0.0165 |
| Raw ev draw | -0.0749 |
| Raw edge prob away | -0.0759 |
| Raw ev away | -0.3103 |
| Market p home draw | 72.4% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:21:29Z |
| Market reference home draw last update utc | 2026-10-14T11:21:59Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.3% |
| Market draw away odds | 1.91 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:21:29Z |
| Market reference draw away last update utc | 2026-10-14T11:21:59Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.80 |
| Market reference dc home draw odds | 1.30 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 88.7% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:20:46Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.70 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 48.8% |
| Market under 3 5 odds | 2.00 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:20:46Z |
| Market reference under 3 5 odds | 1.99 |
| Market reference under 3 5 opposite odds | 1.90 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.4% |
| Market btts yes odds | 1.33 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:21:29Z |
| Market reference btts yes odds | 1.41 |
| Market reference btts yes opposite odds | 3.30 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **76.1%**. Expected goals are 2.86 for Bayern Munich and 1.24 for RB Leipzig (4.10 combined). The most likely exact score is 2-1 at 9.1%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 78.8%; Under 3.5 goals: 40.6%; Double Chance 1X: 89.6%; Double Chance X2: 23.9%; Under 4.5 goals: 59.8%; BTTS Yes (both teams score): 66.4%; BTTS No (at least one team does not score): 33.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 76.1% | 1.31 |
| Draw | 13.5% | 7.38 |
| RB Leipzig win | 10.4% | 9.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.86 |
| RB Leipzig expected goals | 1.24 |
| Expected total goals | 4.10 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 92.4% |
| Under 1.5 | 7.6% |
| Over 2.5 | 78.8% |
| Under 2.5 | 21.2% |
| Over 3.5 | 59.4% |
| Under 3.5 | 40.6% |
| Over 4.5 | 40.2% |
| Under 4.5 | 59.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.09% |
| 2 | 3-1 | 8.67% |
| 3 | 2-0 | 7.34% |
| 4 | 3-0 | 7.00% |
| 5 | 4-1 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 76.1% | 81.8% | 1.26 | -4.2% |
| Draw | 13.5% | 10.8% | 7.36 | -0.3% |
| RB Leipzig win | 10.4% | 7.4% | 11.30 | +17.4% |

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
| Market best home last update utc | 2026-10-14T11:21:29Z |
| Market best draw last update utc | 2026-10-14T11:21:29Z |
| Market best away last update utc | 2026-10-14T11:21:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Bayern Munich |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.4% |
| P btts no | 33.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.90 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.16 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.71 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.47 |
| Fair Over 4.5 odds | 2.49 |
| Fair Under 4.5 odds | 1.67 |
| Unadjusted home-win probability | 70.4% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 92.0% |
| Raw p under 3 5 | 41.4% |
| Raw p btts yes | 67.4% |
| P home draw | 89.6% |
| P draw away | 23.9% |
| Raw p home draw | 86.7% |
| Raw p draw away | 29.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.20 |
| Reference draw odds | 7.50 |
| Reference away odds | 10.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.83 |
| Home probability edge | -5.7% |
| Draw probability edge | +2.8% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | -0.1138 |
| Raw ev home | -0.1133 |
| Raw edge prob draw | 0.0550 |
| Raw ev draw | 0.1997 |
| Raw edge prob away | 0.0588 |
| Raw ev away | 0.5059 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **48.3%**. Expected goals are 2.05 for Elversberg and 1.15 for Augsburg (3.20 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 61.2%; Under 3.5 goals: 61.1%; Double Chance 1X: 72.2%; Double Chance X2: 51.7%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 48.3% | 2.07 |
| Draw | 23.9% | 4.19 |
| Augsburg win | 27.8% | 3.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.05 |
| Augsburg expected goals | 1.15 |
| Expected total goals | 3.20 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 61.2% |
| Under 2.5 | 38.8% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.3% |
| Under 4.5 | 78.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.95% |
| 2 | 2-1 | 8.29% |
| 3 | 1-2 | 7.69% |
| 4 | 2-0 | 7.22% |
| 5 | 1-0 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 48.3% | 39.3% | 2.55 | +23.3% |
| Draw | 23.9% | 25.1% | 3.92 | -6.5% |
| Augsburg win | 27.8% | 35.7% | 2.71 | -24.7% |

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
| Market best home last update utc | 2026-10-14T11:21:29Z |
| Market best draw last update utc | 2026-10-14T11:21:29Z |
| Market best away last update utc | 2026-10-14T11:21:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Elversberg |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.50 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.93 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.69 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 57.4% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 19.9% |
| Raw p over 1 5 | 83.7% |
| Raw p under 3 5 | 60.2% |
| Raw p btts yes | 60.4% |
| P home draw | 72.2% |
| P draw away | 51.7% |
| Raw p home draw | 80.1% |
| Raw p draw away | 42.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.42 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Home probability edge | +9.1% |
| Draw probability edge | -1.2% |
| Away probability edge | -7.9% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | 0.1815 |
| Raw ev home | 0.4643 |
| Raw edge prob draw | -0.0241 |
| Raw ev draw | -0.1122 |
| Raw edge prob away | -0.1574 |
| Raw ev away | -0.4599 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **37.4%**. Expected goals are 0.95 for FC Schalke 04 and 0.92 for FSV Mainz 05 (1.87 combined). The most likely exact score is 0-1 at 15.3%. Goal-market probabilities: at least one goal: 85.5%; Over 2.5 goals: 30.0%; Under 3.5 goals: 87.9%; Double Chance 1X: 62.6%; Double Chance X2: 67.5%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 37.0%; BTTS No (at least one team does not score): 63.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 32.5% | 3.08 |
| Draw | 30.1% | 3.32 |
| FSV Mainz 05 win | 37.4% | 2.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.95 |
| FSV Mainz 05 expected goals | 0.92 |
| Expected total goals | 1.87 |
| Over 0.5 | 85.5% |
| Under 0.5 | 14.5% |
| Over 1.5 | 57.1% |
| Under 1.5 | 42.9% |
| Over 2.5 | 30.0% |
| Under 2.5 | 70.0% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.33% |
| 2 | 0-0 | 14.52% |
| 3 | 1-0 | 13.08% |
| 4 | 1-1 | 12.76% |
| 5 | 0-2 | 7.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 32.5% | 31.3% | 3.16 | +2.6% |
| Draw | 30.1% | 25.8% | 3.67 | +10.5% |
| FSV Mainz 05 win | 37.4% | 43.0% | 2.34 | -12.4% |
| Over 2.5 | 30.0% | 59.5% | 1.70 | -49.1% |
| Under 2.5 | 70.0% | 40.5% | 2.34 | +63.9% |

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
| Market best home last update utc | 2026-10-14T11:21:29Z |
| Market best draw last update utc | 2026-10-14T11:21:29Z |
| Market best away last update utc | 2026-10-14T11:21:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Schalke 04 |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 37.0% |
| P btts no | 63.0% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.89 |
| Fair Over 1.5 odds | 1.75 |
| Fair Under 1.5 odds | 2.33 |
| Fair Over 2.5 odds | 3.34 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 8.26 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.02 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 34.4% |
| Unadjusted away-win probability | 31.9% |
| Raw p over 1 5 | 56.8% |
| Raw p under 3 5 | 88.1% |
| Raw p btts yes | 37.9% |
| P home draw | 62.6% |
| P draw away | 67.5% |
| Raw p home draw | 68.1% |
| Raw p draw away | 66.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 3.00 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.22 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | +1.2% |
| Draw probability edge | +4.3% |
| Away probability edge | -5.5% |
| Over 2.5 probability edge | -29.6% |
| Under 2.5 probability edge | +29.6% |
| Raw edge prob home | 0.0243 |
| Raw ev home | 0.0642 |
| Raw edge prob draw | 0.0867 |
| Raw ev draw | 0.2638 |
| Raw edge prob away | -0.1110 |
| Raw ev away | -0.2539 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **54.7%**. Expected goals are 1.17 for Hamburger SV and 2.00 for VfB Stuttgart (3.17 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 61.3%; Under 3.5 goals: 60.9%; Double Chance 1X: 45.3%; Double Chance X2: 78.0%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 60.6%; BTTS No (at least one team does not score): 39.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 22.0% | 4.55 |
| Draw | 23.3% | 4.28 |
| VfB Stuttgart win | 54.7% | 1.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.17 |
| VfB Stuttgart expected goals | 2.00 |
| Expected total goals | 3.17 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 61.3% |
| Under 2.5 | 38.7% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.73% |
| 2 | 1-2 | 9.63% |
| 3 | 0-2 | 8.22% |
| 4 | 0-1 | 7.40% |
| 5 | 1-3 | 6.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 22.0% | 22.9% | 4.08 | -10.3% |
| Draw | 23.3% | 23.5% | 4.08 | -4.8% |
| VfB Stuttgart win | 54.7% | 53.5% | 1.90 | +3.9% |

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
| Market best home last update utc | 2026-10-14T11:21:29Z |
| Market best draw last update utc | 2026-10-14T11:21:29Z |
| Market best away last update utc | 2026-10-14T11:21:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Hamburg |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 88/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.80 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.98 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.67 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 55.8% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 60.5% |
| P home draw | 45.3% |
| P draw away | 78.0% |
| Raw p home draw | 44.2% |
| Raw p draw away | 79.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 4.00 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.99 |
| Home probability edge | -0.9% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | -0.0188 |
| Raw ev home | -0.1418 |
| Raw edge prob draw | -0.0041 |
| Raw ev draw | -0.0561 |
| Raw edge prob away | 0.0229 |
| Raw ev away | 0.0608 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **60.6%**. Expected goals are 0.94 for Union Berlin and 1.94 for Borussia Dortmund (2.88 combined). The most likely exact score is 0-2 at 10.7%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 55.4%; Under 3.5 goals: 67.3%; Double Chance 1X: 39.4%; Double Chance X2: 82.6%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 52.7%; BTTS No (at least one team does not score): 47.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.4% | 5.76 |
| Draw | 22.0% | 4.54 |
| Borussia Dortmund win | 60.6% | 1.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.94 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.4% |
| Under 2.5 | 44.6% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 10.70% |
| 2 | 1-1 | 10.49% |
| 3 | 0-1 | 10.16% |
| 4 | 1-2 | 10.05% |
| 5 | 0-3 | 6.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.4% | 17.9% | 4.98 | -13.6% |
| Draw | 22.0% | 20.8% | 4.52 | -0.4% |
| Borussia Dortmund win | 60.6% | 61.3% | 1.69 | +2.4% |

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
| Market best home last update utc | 2026-10-14T11:21:29Z |
| Market best draw last update utc | 2026-10-14T11:21:29Z |
| Market best away last update utc | 2026-10-14T11:21:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Union Berlin |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 52.7% |
| P btts no | 47.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.32 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.80 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 6.00 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 16.8% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 59.9% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 53.0% |
| P home draw | 39.4% |
| P draw away | 82.6% |
| Raw p home draw | 40.1% |
| Raw p draw away | 83.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 5.00 |
| Reference draw odds | 4.35 |
| Reference away odds | 1.58 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Home probability edge | -0.5% |
| Draw probability edge | +1.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | -0.0110 |
| Raw ev home | -0.1633 |
| Raw edge prob draw | 0.0252 |
| Raw ev draw | 0.0527 |
| Raw edge prob away | -0.0142 |
| Raw ev away | 0.0124 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **53.0%**. Expected goals are 1.24 for Werder Bremen and 0.61 for SC Paderborn (1.85 combined). The most likely exact score is 1-0 at 19.3%. Goal-market probabilities: at least one goal: 85.6%; Over 2.5 goals: 29.5%; Under 3.5 goals: 88.1%; Double Chance 1X: 80.5%; Double Chance X2: 47.0%; Under 4.5 goals: 95.8%; BTTS Yes (both teams score): 32.4%; BTTS No (at least one team does not score): 67.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 53.0% | 1.89 |
| Draw | 27.5% | 3.63 |
| SC Paderborn win | 19.5% | 5.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.24 |
| SC Paderborn expected goals | 0.61 |
| Expected total goals | 1.85 |
| Over 0.5 | 85.6% |
| Under 0.5 | 14.4% |
| Over 1.5 | 56.5% |
| Under 1.5 | 43.5% |
| Over 2.5 | 29.5% |
| Under 2.5 | 70.5% |
| Over 3.5 | 11.9% |
| Under 3.5 | 88.1% |
| Over 4.5 | 4.2% |
| Under 4.5 | 95.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.34% |
| 2 | 0-0 | 14.41% |
| 3 | 2-0 | 12.67% |
| 4 | 1-1 | 11.05% |
| 5 | 0-1 | 9.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 53.0% | 55.0% | 1.84 | -2.5% |
| Draw | 27.5% | 23.1% | 4.26 | +17.3% |
| SC Paderborn win | 19.5% | 21.9% | 4.21 | -17.9% |

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
| Market best home last update utc | 2026-10-14T11:21:29Z |
| Market best draw last update utc | 2026-10-14T11:21:29Z |
| Market best away last update utc | 2026-10-14T11:21:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.4% |
| P btts no | 67.6% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.94 |
| Fair Over 1.5 odds | 1.77 |
| Fair Under 1.5 odds | 2.30 |
| Fair Over 2.5 odds | 3.39 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.44 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 23.81 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 50.9% |
| Unadjusted draw probability | 32.0% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 56.1% |
| Raw p under 3 5 | 88.3% |
| Raw p btts yes | 33.3% |
| P home draw | 80.5% |
| P draw away | 47.0% |
| Raw p home draw | 82.9% |
| Raw p draw away | 49.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.75 |
| Reference draw odds | 3.95 |
| Reference away odds | 4.15 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Home probability edge | -2.1% |
| Draw probability edge | +4.5% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -32.9% |
| Under 2.5 probability edge | +32.9% |
| Raw edge prob home | -0.0412 |
| Raw ev home | -0.0634 |
| Raw edge prob draw | 0.0893 |
| Raw ev draw | 0.3635 |
| Raw edge prob away | -0.0481 |
| Raw ev away | -0.2806 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **61.4%**. Expected goals are 2.40 for Bayer Leverkusen and 1.08 for SC Freiburg (3.48 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 66.7%; Under 3.5 goals: 54.8%; Double Chance 1X: 82.1%; Double Chance X2: 38.6%; Under 4.5 goals: 73.6%; BTTS Yes (both teams score): 61.3%; BTTS No (at least one team does not score): 38.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 61.4% | 1.63 |
| Draw | 20.7% | 4.84 |
| SC Freiburg win | 17.9% | 5.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.40 |
| SC Freiburg expected goals | 1.08 |
| Expected total goals | 3.48 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 86.5% |
| Under 1.5 | 13.5% |
| Over 2.5 | 66.7% |
| Under 2.5 | 33.3% |
| Over 3.5 | 45.2% |
| Under 3.5 | 54.8% |
| Over 4.5 | 26.4% |
| Under 4.5 | 73.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.25% |
| 2 | 2-1 | 8.92% |
| 3 | 2-0 | 8.29% |
| 4 | 3-1 | 7.14% |
| 5 | 3-0 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 61.4% | 56.8% | 1.75 | +7.4% |
| Draw | 20.7% | 22.0% | 4.42 | -8.7% |
| SC Freiburg win | 17.9% | 21.2% | 4.62 | -17.1% |

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
| Market best home last update utc | 2026-10-14T11:21:29Z |
| Market best draw last update utc | 2026-10-14T11:21:29Z |
| Market best away last update utc | 2026-10-14T11:21:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Leverkusen |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.3% |
| P btts no | 38.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.87 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.38 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 3.01 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.82 |
| Fair Over 4.5 odds | 3.78 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 65.9% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 14.7% |
| Raw p over 1 5 | 86.8% |
| Raw p under 3 5 | 54.2% |
| Raw p btts yes | 60.6% |
| P home draw | 82.1% |
| P draw away | 38.6% |
| Raw p home draw | 85.3% |
| Raw p draw away | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.70 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.30 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.69 |
| Home probability edge | +4.5% |
| Draw probability edge | -1.3% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | 0.0910 |
| Raw ev home | 0.1540 |
| Raw edge prob draw | -0.0266 |
| Raw ev draw | -0.1457 |
| Raw edge prob away | -0.0644 |
| Raw ev away | -0.3196 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **40.8%**. Expected goals are 1.87 for Borussia Monchengladbach and 1.78 for TSG Hoffenheim (3.65 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 70.5%; Under 3.5 goals: 50.5%; Double Chance 1X: 59.2%; Double Chance X2: 64.2%; Under 4.5 goals: 69.8%; BTTS Yes (both teams score): 71.1%; BTTS No (at least one team does not score): 28.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 35.8% | 2.80 |
| Draw | 23.4% | 4.27 |
| TSG Hoffenheim win | 40.8% | 2.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.87 |
| TSG Hoffenheim expected goals | 1.78 |
| Expected total goals | 3.65 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 70.5% |
| Under 2.5 | 29.5% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 30.2% |
| Under 4.5 | 69.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.46% |
| 2 | 1-2 | 8.59% |
| 3 | 2-2 | 7.26% |
| 4 | 2-1 | 7.20% |
| 5 | 1-3 | 5.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 35.8% | 31.4% | 3.33 | +19.1% |
| Draw | 23.4% | 23.6% | 4.21 | -1.5% |
| TSG Hoffenheim win | 40.8% | 45.0% | 2.10 | -14.2% |

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
| Market best home last update utc | 2026-10-14T11:21:29Z |
| Market best draw last update utc | 2026-10-14T11:21:29Z |
| Market best away last update utc | 2026-10-14T11:21:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | M'gladbach |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 71.1% |
| P btts no | 28.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.79 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.78 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.39 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.31 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 36.6% |
| Raw p over 1 5 | 88.6% |
| Raw p under 3 5 | 50.5% |
| Raw p btts yes | 71.0% |
| P home draw | 59.2% |
| P draw away | 64.2% |
| Raw p home draw | 63.4% |
| Raw p draw away | 59.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.98 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.12 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.99 |
| Home probability edge | +4.4% |
| Draw probability edge | -0.2% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | 0.0878 |
| Raw ev home | 0.3373 |
| Raw edge prob draw | -0.0038 |
| Raw ev draw | -0.0230 |
| Raw edge prob away | -0.0840 |
| Raw ev away | -0.2307 |

</details>


---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **68.6%**. Expected goals are 2.52 for VfB Stuttgart and 1.17 for Borussia Monchengladbach (3.69 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 71.9%; Under 3.5 goals: 49.2%; Double Chance 1X: 86.0%; Double Chance X2: 31.4%; Under 4.5 goals: 68.4%; BTTS Yes (both teams score): 63.6%; BTTS No (at least one team does not score): 36.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 68.6% | 1.46 |
| Draw | 17.3% | 5.77 |
| Borussia Monchengladbach win | 14.0% | 7.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.52 |
| Borussia Monchengladbach expected goals | 1.17 |
| Expected total goals | 3.69 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 89.1% |
| Under 1.5 | 10.9% |
| Over 2.5 | 71.9% |
| Under 2.5 | 28.1% |
| Over 3.5 | 50.8% |
| Under 3.5 | 49.2% |
| Over 4.5 | 31.6% |
| Under 4.5 | 68.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.63% |
| 2 | 2-0 | 8.22% |
| 3 | 3-1 | 8.09% |
| 4 | 1-1 | 7.41% |
| 5 | 3-0 | 6.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 68.6% | 71.2% | 1.43 | -1.9% |
| Draw | 17.3% | 16.0% | 5.80 | +0.6% |
| Borussia Monchengladbach win | 14.0% | 12.8% | 6.98 | -2.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:30:00+00:00 |
| Fixture id | d4d56a31d8ccd432e3a6183180e093f3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:21:29Z |
| Market best draw last update utc | 2026-10-14T11:21:29Z |
| Market best away last update utc | 2026-10-14T11:21:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.6% |
| P btts no | 36.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.64 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.19 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.56 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.17 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 66.0% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 15.3% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 49.6% |
| Raw p btts yes | 64.1% |
| P home draw | 86.0% |
| P draw away | 31.4% |
| Raw p home draw | 84.7% |
| Raw p draw away | 34.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.37 |
| Reference draw odds | 5.45 |
| Reference away odds | 6.70 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.76 |
| Home probability edge | -2.6% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | -0.0512 |
| Raw ev home | -0.0555 |
| Raw edge prob draw | 0.0266 |
| Raw ev draw | 0.0833 |
| Raw edge prob away | 0.0246 |
| Raw ev away | 0.0662 |

</details>


---
