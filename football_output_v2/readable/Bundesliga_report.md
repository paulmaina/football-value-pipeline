# Bundesliga — football model report

Fixtures in this report: **9**.

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
| Training data health | {'training_end': '2026-10-11', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
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

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **54.5%**. Expected goals are 2.24 for Eintracht Frankfurt and 1.24 for 1. FC Köln (3.48 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 67.2%; Under 3.5 goals: 54.6%; Double Chance 1X: 76.4%; Double Chance X2: 45.5%; Under 4.5 goals: 73.3%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 54.5% | 1.83 |
| Draw | 21.8% | 4.58 |
| 1. FC Köln win | 23.6% | 4.23 |

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
| Over 2.5 | 67.2% |
| Under 2.5 | 32.8% |
| Over 3.5 | 45.4% |
| Under 3.5 | 54.6% |
| Over 4.5 | 26.7% |
| Under 4.5 | 73.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.55% |
| 2 | 2-1 | 8.83% |
| 3 | 2-0 | 7.11% |
| 4 | 3-1 | 6.59% |
| 5 | 1-2 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 54.5% | 49.9% | 2.04 | +11.3% |
| Draw | 21.8% | 22.5% | 4.30 | -6.1% |
| 1. FC Köln win | 23.6% | 27.6% | 3.55 | -16.2% |
| Over 2.5 | 67.2% | 71.1% | 1.37 | -8.0% |
| Under 2.5 | 32.8% | 28.9% | 3.15 | +3.5% |

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
| Market best home last update utc | 2026-10-13T11:51:21Z |
| Market best draw last update utc | 2026-10-13T11:50:07Z |
| Market best away last update utc | 2026-10-13T11:51:21Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 81/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.60 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.50 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.04 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.74 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 59.2% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 19.6% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.1% |
| Raw p btts yes | 64.3% |
| P home draw | 76.4% |
| P draw away | 45.5% |
| Raw p home draw | 80.4% |
| Raw p draw away | 40.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.95 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.44 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.15 |
| Home probability edge | +4.6% |
| Draw probability edge | -0.6% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | 0.0928 |
| Raw ev home | 0.2074 |
| Raw edge prob draw | -0.0124 |
| Raw ev draw | -0.0876 |
| Raw edge prob away | -0.0805 |
| Raw ev away | -0.3044 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **74.9%**. Expected goals are 2.86 for Bayern Munich and 1.24 for RB Leipzig (4.10 combined). The most likely exact score is 2-1 at 9.0%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 78.4%; Under 3.5 goals: 40.7%; Double Chance 1X: 89.4%; Double Chance X2: 25.1%; Under 4.5 goals: 60.1%; BTTS Yes (both teams score): 66.7%; BTTS No (at least one team does not score): 33.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 74.9% | 1.33 |
| Draw | 14.4% | 6.93 |
| RB Leipzig win | 10.6% | 9.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.86 |
| RB Leipzig expected goals | 1.24 |
| Expected total goals | 4.10 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 92.3% |
| Under 1.5 | 7.7% |
| Over 2.5 | 78.4% |
| Under 2.5 | 21.6% |
| Over 3.5 | 59.3% |
| Under 3.5 | 40.7% |
| Over 4.5 | 39.9% |
| Under 4.5 | 60.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.95% |
| 2 | 3-1 | 8.54% |
| 3 | 2-0 | 7.23% |
| 4 | 3-0 | 6.89% |
| 5 | 4-1 | 6.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 74.9% | 79.5% | 1.26 | -5.6% |
| Draw | 14.4% | 12.6% | 8.25 | +19.0% |
| RB Leipzig win | 10.6% | 7.9% | 11.30 | +20.2% |
| Over 2.5 | 78.4% | 86.3% | 1.15 | -9.8% |
| Under 2.5 | 21.6% | 13.7% | 5.83 | +25.7% |

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
| Market best home last update utc | 2026-10-13T11:50:07Z |
| Market best draw last update utc | 2026-10-13T11:50:25Z |
| Market best away last update utc | 2026-10-13T11:50:07Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Bayern Munich |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.7% |
| P btts no | 33.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 52.50 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.02 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.64 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.46 |
| Fair Over 4.5 odds | 2.51 |
| Fair Under 4.5 odds | 1.66 |
| Unadjusted home-win probability | 70.4% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 92.0% |
| Raw p under 3 5 | 41.4% |
| Raw p btts yes | 67.4% |
| P home draw | 89.4% |
| P draw away | 25.1% |
| Raw p home draw | 86.7% |
| Raw p draw away | 29.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.24 |
| Reference draw odds | 7.00 |
| Reference away odds | 10.75 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.83 |
| Home probability edge | -4.6% |
| Draw probability edge | +1.9% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | -0.0913 |
| Raw ev home | -0.1133 |
| Raw edge prob draw | 0.0375 |
| Raw ev draw | 0.3448 |
| Raw edge prob away | 0.0538 |
| Raw ev away | 0.5059 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **48.1%**. Expected goals are 2.05 for Elversberg and 1.15 for Augsburg (3.20 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 61.3%; Under 3.5 goals: 61.1%; Double Chance 1X: 71.8%; Double Chance X2: 51.9%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 48.1% | 2.08 |
| Draw | 23.7% | 4.22 |
| Augsburg win | 28.2% | 3.55 |

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
| Over 2.5 | 61.3% |
| Under 2.5 | 38.7% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.3% |
| Under 4.5 | 78.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.88% |
| 2 | 2-1 | 8.26% |
| 3 | 1-2 | 7.79% |
| 4 | 2-0 | 7.19% |
| 5 | 1-0 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 48.1% | 38.8% | 2.55 | +22.7% |
| Draw | 23.7% | 24.8% | 4.20 | -0.4% |
| Augsburg win | 28.2% | 36.4% | 2.71 | -23.7% |
| Over 2.5 | 61.3% | 67.0% | 1.45 | -11.2% |
| Under 2.5 | 38.7% | 33.0% | 2.79 | +8.1% |

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
| Market best home last update utc | 2026-10-13T11:50:07Z |
| Market best draw last update utc | 2026-10-13T11:51:41Z |
| Market best away last update utc | 2026-10-13T11:50:07Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Elversberg |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.62 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.93 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.68 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 57.4% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 19.9% |
| Raw p over 1 5 | 83.7% |
| Raw p under 3 5 | 60.2% |
| Raw p btts yes | 60.4% |
| P home draw | 71.8% |
| P draw away | 51.9% |
| Raw p home draw | 80.1% |
| Raw p draw away | 42.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.48 |
| Reference draw odds | 3.82 |
| Reference away odds | 2.64 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.79 |
| Home probability edge | +9.3% |
| Draw probability edge | -1.1% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | 0.1858 |
| Raw ev home | 0.4643 |
| Raw edge prob draw | -0.0212 |
| Raw ev draw | -0.0487 |
| Raw edge prob away | -0.1646 |
| Raw ev away | -0.4599 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **36.2%**. Expected goals are 0.95 for FC Schalke 04 and 0.92 for FSV Mainz 05 (1.87 combined). The most likely exact score is 0-1 at 14.8%. Goal-market probabilities: at least one goal: 85.3%; Over 2.5 goals: 29.9%; Under 3.5 goals: 87.9%; Double Chance 1X: 63.8%; Double Chance X2: 66.6%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 37.1%; BTTS No (at least one team does not score): 62.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 33.4% | 3.00 |
| Draw | 30.4% | 3.29 |
| FSV Mainz 05 win | 36.2% | 2.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.95 |
| FSV Mainz 05 expected goals | 0.92 |
| Expected total goals | 1.87 |
| Over 0.5 | 85.3% |
| Under 0.5 | 14.7% |
| Over 1.5 | 57.1% |
| Under 1.5 | 42.9% |
| Over 2.5 | 29.9% |
| Under 2.5 | 70.1% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.83% |
| 2 | 0-0 | 14.67% |
| 3 | 1-0 | 13.44% |
| 4 | 1-1 | 12.89% |
| 5 | 0-2 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 33.4% | 33.0% | 3.10 | +3.4% |
| Draw | 30.4% | 26.4% | 3.80 | +15.6% |
| FSV Mainz 05 win | 36.2% | 40.6% | 2.44 | -11.6% |
| Over 2.5 | 29.9% | 60.0% | 1.66 | -50.4% |
| Under 2.5 | 70.1% | 40.0% | 2.42 | +69.7% |

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
| Market best home last update utc | 2026-10-13T11:50:24Z |
| Market best draw last update utc | 2026-10-13T11:51:40Z |
| Market best away last update utc | 2026-10-13T11:50:07Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Schalke 04 |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 37.1% |
| P btts no | 62.9% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.82 |
| Fair Over 1.5 odds | 1.75 |
| Fair Under 1.5 odds | 2.33 |
| Fair Over 2.5 odds | 3.35 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 8.27 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.09 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 34.4% |
| Unadjusted away-win probability | 31.9% |
| Raw p over 1 5 | 56.8% |
| Raw p under 3 5 | 88.1% |
| Raw p btts yes | 37.9% |
| P home draw | 63.8% |
| P draw away | 66.6% |
| Raw p home draw | 68.1% |
| Raw p draw away | 66.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.90 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.38 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | +0.3% |
| Draw probability edge | +4.0% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -30.1% |
| Under 2.5 probability edge | +30.1% |
| Raw edge prob home | 0.0064 |
| Raw ev home | 0.0440 |
| Raw edge prob draw | 0.0805 |
| Raw ev draw | 0.3086 |
| Raw edge prob away | -0.0869 |
| Raw ev away | -0.2220 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **54.2%**. Expected goals are 1.17 for Hamburger SV and 2.00 for VfB Stuttgart (3.17 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 61.3%; Under 3.5 goals: 61.0%; Double Chance 1X: 45.8%; Double Chance X2: 77.6%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 22.4% | 4.47 |
| Draw | 23.4% | 4.27 |
| VfB Stuttgart win | 54.2% | 1.84 |

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
| Over 3.5 | 39.0% |
| Under 3.5 | 61.0% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.76% |
| 2 | 1-2 | 9.55% |
| 3 | 0-2 | 8.16% |
| 4 | 0-1 | 7.34% |
| 5 | 1-3 | 6.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 22.4% | 23.7% | 4.20 | -6.1% |
| Draw | 23.4% | 23.7% | 4.40 | +3.0% |
| VfB Stuttgart win | 54.2% | 52.6% | 1.90 | +3.1% |
| Over 2.5 | 61.3% | 69.5% | 1.40 | -14.2% |
| Under 2.5 | 38.7% | 30.5% | 3.00 | +16.1% |

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
| Market best home last update utc | 2026-10-13T11:51:40Z |
| Market best draw last update utc | 2026-10-13T11:51:40Z |
| Market best away last update utc | 2026-10-13T11:50:07Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Hamburg |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 88/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.74 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.98 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.68 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 55.8% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 60.5% |
| P home draw | 45.8% |
| P draw away | 77.6% |
| Raw p home draw | 44.2% |
| Raw p draw away | 79.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.98 |
| Reference draw odds | 3.98 |
| Reference away odds | 1.85 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -1.3% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -8.2% |
| Under 2.5 probability edge | +8.2% |
| Raw edge prob home | -0.0264 |
| Raw ev home | -0.1166 |
| Raw edge prob draw | -0.0054 |
| Raw ev draw | 0.0180 |
| Raw edge prob away | 0.0319 |
| Raw ev away | 0.0608 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **59.8%**. Expected goals are 0.94 for Union Berlin and 1.94 for Borussia Dortmund (2.88 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 55.3%; Under 3.5 goals: 67.4%; Double Chance 1X: 40.2%; Double Chance X2: 82.0%; Under 4.5 goals: 83.4%; BTTS Yes (both teams score): 52.8%; BTTS No (at least one team does not score): 47.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 18.0% | 5.56 |
| Draw | 22.3% | 4.49 |
| Borussia Dortmund win | 59.8% | 1.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.94 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.3% |
| Under 2.5 | 44.7% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.60% |
| 2 | 0-2 | 10.55% |
| 3 | 0-1 | 10.01% |
| 4 | 1-2 | 9.90% |
| 5 | 0-3 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 18.0% | 19.2% | 5.40 | -2.9% |
| Draw | 22.3% | 21.2% | 4.52 | +0.6% |
| Borussia Dortmund win | 59.8% | 59.6% | 1.69 | +1.0% |
| Over 2.5 | 55.3% | 64.3% | 1.51 | -16.5% |
| Under 2.5 | 44.7% | 35.7% | 2.61 | +16.7% |

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
| Market best home last update utc | 2026-10-13T11:51:40Z |
| Market best draw last update utc | 2026-10-13T11:50:07Z |
| Market best away last update utc | 2026-10-13T11:50:07Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Union Berlin |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 52.8% |
| P btts no | 47.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.16 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.78 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.03 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 16.8% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 59.9% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 53.0% |
| P home draw | 40.2% |
| P draw away | 82.0% |
| Raw p home draw | 40.1% |
| Raw p draw away | 83.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.85 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.64 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Home probability edge | -1.2% |
| Draw probability edge | +1.0% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.0237 |
| Raw ev home | -0.0927 |
| Raw edge prob draw | 0.0206 |
| Raw ev draw | 0.0527 |
| Raw edge prob away | 0.0031 |
| Raw ev away | 0.0124 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **52.7%**. Expected goals are 1.24 for Werder Bremen and 0.61 for SC Paderborn (1.85 combined). The most likely exact score is 1-0 at 19.2%. Goal-market probabilities: at least one goal: 85.7%; Over 2.5 goals: 29.6%; Under 3.5 goals: 88.2%; Double Chance 1X: 80.0%; Double Chance X2: 47.3%; Under 4.5 goals: 95.8%; BTTS Yes (both teams score): 32.4%; BTTS No (at least one team does not score): 67.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 52.7% | 1.90 |
| Draw | 27.3% | 3.66 |
| SC Paderborn win | 20.0% | 5.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.24 |
| SC Paderborn expected goals | 0.61 |
| Expected total goals | 1.85 |
| Over 0.5 | 85.7% |
| Under 0.5 | 14.3% |
| Over 1.5 | 56.5% |
| Under 1.5 | 43.5% |
| Over 2.5 | 29.6% |
| Under 2.5 | 70.4% |
| Over 3.5 | 11.8% |
| Under 3.5 | 88.2% |
| Over 4.5 | 4.2% |
| Under 4.5 | 95.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.23% |
| 2 | 0-0 | 14.29% |
| 3 | 2-0 | 12.60% |
| 4 | 1-1 | 10.96% |
| 5 | 0-1 | 9.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 52.7% | 54.5% | 1.85 | -2.5% |
| Draw | 27.3% | 22.6% | 4.29 | +17.2% |
| SC Paderborn win | 20.0% | 22.9% | 4.21 | -15.8% |
| Over 2.5 | 29.6% | 63.3% | 1.55 | -54.2% |
| Under 2.5 | 70.4% | 36.7% | 2.54 | +78.9% |

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
| Market best home last update utc | 2026-10-13T11:51:40Z |
| Market best draw last update utc | 2026-10-13T11:51:22Z |
| Market best away last update utc | 2026-10-13T11:50:07Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.4% |
| P btts no | 67.6% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 7.00 |
| Fair Over 1.5 odds | 1.77 |
| Fair Under 1.5 odds | 2.30 |
| Fair Over 2.5 odds | 3.38 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.45 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 23.80 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 50.9% |
| Unadjusted draw probability | 32.0% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 56.1% |
| Raw p under 3 5 | 88.3% |
| Raw p btts yes | 33.3% |
| P home draw | 80.0% |
| P draw away | 47.3% |
| Raw p home draw | 82.9% |
| Raw p draw away | 49.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.79 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.54 |
| Home probability edge | -1.8% |
| Draw probability edge | +4.7% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -33.7% |
| Under 2.5 probability edge | +33.7% |
| Raw edge prob home | -0.0355 |
| Raw ev home | -0.0583 |
| Raw edge prob draw | 0.0938 |
| Raw ev draw | 0.3731 |
| Raw edge prob away | -0.0583 |
| Raw ev away | -0.2806 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **61.7%**. Expected goals are 2.40 for Bayer Leverkusen and 1.08 for SC Freiburg (3.48 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 66.8%; Under 3.5 goals: 54.8%; Double Chance 1X: 82.2%; Double Chance X2: 38.3%; Under 4.5 goals: 73.5%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 61.7% | 1.62 |
| Draw | 20.6% | 4.86 |
| SC Freiburg win | 17.8% | 5.63 |

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
| Over 2.5 | 66.8% |
| Under 2.5 | 33.2% |
| Over 3.5 | 45.2% |
| Under 3.5 | 54.8% |
| Over 4.5 | 26.5% |
| Under 4.5 | 73.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.21% |
| 2 | 2-1 | 8.97% |
| 3 | 2-0 | 8.33% |
| 4 | 3-1 | 7.17% |
| 5 | 3-0 | 6.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 61.7% | 57.4% | 1.76 | +8.6% |
| Draw | 20.6% | 21.8% | 4.42 | -9.1% |
| SC Freiburg win | 17.8% | 20.8% | 4.62 | -18.0% |
| Over 2.5 | 66.8% | 65.6% | 1.48 | -1.2% |
| Under 2.5 | 33.2% | 34.4% | 2.69 | -10.7% |

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
| Market best home last update utc | 2026-10-13T11:51:22Z |
| Market best draw last update utc | 2026-10-13T11:50:07Z |
| Market best away last update utc | 2026-10-13T11:50:07Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Leverkusen |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.99 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.40 |
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
| P home draw | 82.2% |
| P draw away | 38.3% |
| Raw p home draw | 85.3% |
| Raw p draw away | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.70 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.69 |
| Home probability edge | +4.3% |
| Draw probability edge | -1.2% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | 0.0850 |
| Raw ev home | 0.1606 |
| Raw edge prob draw | -0.0246 |
| Raw ev draw | -0.1457 |
| Raw edge prob away | -0.0605 |
| Raw ev away | -0.3196 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **42.6%**. Expected goals are 1.87 for Borussia Monchengladbach and 1.78 for TSG Hoffenheim (3.65 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.5%; Double Chance 1X: 57.4%; Double Chance X2: 65.7%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 71.1%; BTTS No (at least one team does not score): 28.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 34.3% | 2.91 |
| Draw | 23.1% | 4.33 |
| TSG Hoffenheim win | 42.6% | 2.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.87 |
| TSG Hoffenheim expected goals | 1.78 |
| Expected total goals | 3.65 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 70.6% |
| Under 2.5 | 29.4% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.34% |
| 2 | 1-2 | 8.96% |
| 3 | 2-2 | 7.16% |
| 4 | 2-1 | 6.91% |
| 5 | 1-3 | 5.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 34.3% | 28.5% | 3.45 | +18.4% |
| Draw | 23.1% | 23.0% | 4.30 | -0.7% |
| TSG Hoffenheim win | 42.6% | 48.6% | 2.10 | -10.5% |
| Over 2.5 | 70.6% | 69.5% | 1.40 | -1.2% |
| Under 2.5 | 29.4% | 30.5% | 2.99 | -12.1% |

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
| Market best home last update utc | 2026-10-13T11:51:41Z |
| Market best draw last update utc | 2026-10-13T11:50:26Z |
| Market best away last update utc | 2026-10-13T11:51:22Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | M'gladbach |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 71.1% |
| P btts no | 28.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.18 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.78 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.40 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 36.6% |
| Raw p over 1 5 | 88.6% |
| Raw p under 3 5 | 50.5% |
| Raw p btts yes | 71.0% |
| P home draw | 57.4% |
| P draw away | 65.7% |
| Raw p home draw | 63.4% |
| Raw p draw away | 59.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.34 |
| Reference draw odds | 4.10 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.99 |
| Home probability edge | +5.9% |
| Draw probability edge | +0.1% |
| Away probability edge | -6.0% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | 0.1170 |
| Raw ev home | 0.3855 |
| Raw edge prob draw | 0.0022 |
| Raw ev draw | -0.0021 |
| Raw edge prob away | -0.1193 |
| Raw ev away | -0.2307 |

</details>


---
