# Bundesliga — football model report

Fixtures in this report: **16**.

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
| Live odds matched | 16.00 |
| Additional event odds calls used before this league | 10.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
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

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **54.4%**. Expected goals are 2.24 for Eintracht Frankfurt and 1.24 for 1. FC Köln (3.48 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 67.2%; Under 3.5 goals: 54.6%; Double Chance 1X: 76.1%; Double Chance X2: 45.6%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 54.4% | 1.84 |
| Draw | 21.6% | 4.62 |
| 1. FC Köln win | 23.9% | 4.18 |

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
| Over 4.5 | 26.8% |
| Under 4.5 | 73.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.45% |
| 2 | 2-1 | 8.81% |
| 3 | 2-0 | 7.09% |
| 4 | 3-1 | 6.58% |
| 5 | 1-2 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 54.4% | 49.7% | 1.99 | +8.3% |
| Draw | 21.6% | 22.0% | 4.36 | -5.7% |
| 1. FC Köln win | 23.9% | 28.3% | 3.52 | -15.8% |

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
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
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
| Fair Under 0.5 odds | 25.85 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.50 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.05 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.74 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 59.2% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 19.6% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.1% |
| Raw p btts yes | 64.3% |
| P home draw | 76.1% |
| P draw away | 45.6% |
| Raw p home draw | 80.4% |
| Raw p draw away | 40.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.92 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.26 |
| Home probability edge | +4.7% |
| Draw probability edge | -0.4% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | 0.0949 |
| Raw ev home | 0.1778 |
| Raw edge prob draw | -0.0082 |
| Raw ev draw | -0.0749 |
| Raw edge prob away | -0.0867 |
| Raw ev away | -0.3103 |
| Market p home draw | 72.0% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:07:17Z |
| Market reference home draw last update utc | 2026-10-14T19:07:17Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.9% |
| Market draw away odds | 1.91 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:07:17Z |
| Market reference draw away last update utc | 2026-10-14T19:07:17Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.91 |
| Market reference dc home draw odds | 1.35 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:06:38Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 48.8% |
| Market under 3 5 odds | 2.00 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:06:38Z |
| Market reference under 3 5 odds | 1.99 |
| Market reference under 3 5 opposite odds | 1.90 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 72.3% |
| Market btts yes odds | 1.33 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:07:17Z |
| Market reference btts yes odds | 1.33 |
| Market reference btts yes opposite odds | 3.10 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **75.3%**. Expected goals are 2.86 for Bayern Munich and 1.24 for RB Leipzig (4.10 combined). The most likely exact score is 2-1 at 9.0%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 78.9%; Under 3.5 goals: 40.7%; Double Chance 1X: 88.4%; Double Chance X2: 24.7%; Under 4.5 goals: 59.8%; BTTS Yes (both teams score): 66.5%; BTTS No (at least one team does not score): 33.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 75.3% | 1.33 |
| Draw | 13.1% | 7.63 |
| RB Leipzig win | 11.6% | 8.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.86 |
| RB Leipzig expected goals | 1.24 |
| Expected total goals | 4.10 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 92.4% |
| Under 1.5 | 7.6% |
| Over 2.5 | 78.9% |
| Under 2.5 | 21.1% |
| Over 3.5 | 59.3% |
| Under 3.5 | 40.7% |
| Over 4.5 | 40.2% |
| Under 4.5 | 59.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.99% |
| 2 | 3-1 | 8.58% |
| 3 | 2-0 | 7.26% |
| 4 | 3-0 | 6.92% |
| 5 | 4-1 | 6.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 75.3% | 80.2% | 1.26 | -5.2% |
| Draw | 13.1% | 9.9% | 7.36 | -3.5% |
| RB Leipzig win | 11.6% | 9.9% | 11.30 | +31.3% |

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
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Bayern Munich |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.5% |
| P btts no | 33.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 57.78 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.09 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.73 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.46 |
| Fair Over 4.5 odds | 2.49 |
| Fair Under 4.5 odds | 1.67 |
| Unadjusted home-win probability | 70.4% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 92.0% |
| Raw p under 3 5 | 41.4% |
| Raw p btts yes | 67.4% |
| P home draw | 88.4% |
| P draw away | 24.7% |
| Raw p home draw | 86.7% |
| Raw p draw away | 29.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.22 |
| Reference draw odds | 8.00 |
| Reference away odds | 8.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.83 |
| Home probability edge | -4.9% |
| Draw probability edge | +3.2% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.0980 |
| Raw ev home | -0.1133 |
| Raw edge prob draw | 0.0639 |
| Raw ev draw | 0.1997 |
| Raw edge prob away | 0.0341 |
| Raw ev away | 0.5059 |
| Market p home draw | 91.6% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:07:17Z |
| Market reference home draw last update utc | 2026-10-14T19:07:17Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.6% |
| Market draw away odds | 4.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:07:17Z |
| Market reference draw away last update utc | 2026-10-14T19:07:17Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.26 |
| Market reference dc home draw odds | 1.05 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 95.8% |
| Market over 1 5 odds | 1.03 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:05:49Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 8.60 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 29.0% |
| Market under 3 5 odds | 2.76 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:05:49Z |
| Market reference under 3 5 odds | 3.12 |
| Market reference under 3 5 opposite odds | 1.37 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.4% |
| Market btts yes odds | 1.38 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:07:17Z |
| Market reference btts yes odds | 1.38 |
| Market reference btts yes opposite odds | 2.85 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **48.4%**. Expected goals are 2.05 for Elversberg and 1.15 for Augsburg (3.20 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 61.5%; Under 3.5 goals: 61.1%; Double Chance 1X: 71.5%; Double Chance X2: 51.6%; Under 4.5 goals: 78.5%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 48.4% | 2.06 |
| Draw | 23.1% | 4.33 |
| Augsburg win | 28.5% | 3.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.05 |
| Augsburg expected goals | 1.15 |
| Expected total goals | 3.20 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.5% |
| Under 4.5 | 78.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.60% |
| 2 | 2-1 | 8.31% |
| 3 | 1-2 | 7.87% |
| 4 | 2-0 | 7.23% |
| 5 | 1-0 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 48.4% | 39.5% | 2.55 | +23.5% |
| Draw | 23.1% | 23.6% | 3.92 | -9.4% |
| Augsburg win | 28.5% | 37.0% | 2.71 | -22.9% |

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
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Elversberg |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.14 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.94 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.66 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 57.4% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 19.9% |
| Raw p over 1 5 | 83.7% |
| Raw p under 3 5 | 60.2% |
| Raw p btts yes | 60.4% |
| P home draw | 71.5% |
| P draw away | 51.6% |
| Raw p home draw | 80.1% |
| Raw p draw away | 42.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.40 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.55 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Home probability edge | +9.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -8.5% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | 0.1797 |
| Raw ev home | 0.4643 |
| Raw edge prob draw | -0.0091 |
| Raw ev draw | -0.1122 |
| Raw edge prob away | -0.1706 |
| Raw ev away | -0.4599 |
| Market p home draw | 63.9% |
| Market home draw odds | 1.52 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:07:17Z |
| Market reference home draw last update utc | 2026-10-14T19:07:17Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.4% |
| Market draw away odds | 1.58 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:07:17Z |
| Market reference draw away last update utc | 2026-10-14T19:07:17Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.58 |
| Market reference dc home draw odds | 1.52 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 91.0% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:07:02Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 5.70 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.4% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:07:02Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.0% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:07:17Z |
| Market reference btts yes odds | 1.37 |
| Market reference btts yes opposite odds | 2.89 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **37.4%**. Expected goals are 0.95 for FC Schalke 04 and 0.92 for FSV Mainz 05 (1.87 combined). The most likely exact score is 0-1 at 15.3%. Goal-market probabilities: at least one goal: 85.8%; Over 2.5 goals: 30.1%; Under 3.5 goals: 87.9%; Double Chance 1X: 62.6%; Double Chance X2: 66.9%; Under 4.5 goals: 95.6%; BTTS Yes (both teams score): 36.9%; BTTS No (at least one team does not score): 63.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 33.1% | 3.02 |
| Draw | 29.5% | 3.39 |
| FSV Mainz 05 win | 37.4% | 2.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.95 |
| FSV Mainz 05 expected goals | 0.92 |
| Expected total goals | 1.87 |
| Over 0.5 | 85.8% |
| Under 0.5 | 14.2% |
| Over 1.5 | 57.1% |
| Under 1.5 | 42.9% |
| Over 2.5 | 30.1% |
| Under 2.5 | 69.9% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.4% |
| Under 4.5 | 95.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.31% |
| 2 | 0-0 | 14.24% |
| 3 | 1-0 | 13.33% |
| 4 | 1-1 | 12.51% |
| 5 | 0-2 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 33.1% | 32.5% | 3.16 | +4.6% |
| Draw | 29.5% | 24.6% | 3.67 | +8.3% |
| FSV Mainz 05 win | 37.4% | 42.9% | 2.34 | -12.5% |
| Over 2.5 | 30.1% | 58.1% | 1.70 | -48.8% |
| Under 2.5 | 69.9% | 41.9% | 2.34 | +63.5% |

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
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Schalke 04 |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 36.9% |
| P btts no | 63.1% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 7.02 |
| Fair Over 1.5 odds | 1.75 |
| Fair Under 1.5 odds | 2.33 |
| Fair Over 2.5 odds | 3.32 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 8.25 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 22.86 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 34.4% |
| Unadjusted away-win probability | 31.9% |
| Raw p over 1 5 | 56.8% |
| Raw p under 3 5 | 88.1% |
| Raw p btts yes | 37.9% |
| P home draw | 62.6% |
| P draw away | 66.9% |
| Raw p home draw | 68.1% |
| Raw p draw away | 66.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.34 |
| Home probability edge | +0.6% |
| Draw probability edge | +4.9% |
| Away probability edge | -5.5% |
| Over 2.5 probability edge | -28.0% |
| Under 2.5 probability edge | +28.0% |
| Raw edge prob home | 0.0117 |
| Raw ev home | 0.0642 |
| Raw edge prob draw | 0.0987 |
| Raw ev draw | 0.2638 |
| Raw edge prob away | -0.1103 |
| Raw ev away | -0.2539 |
| Market p home draw | 58.1% |
| Market home draw odds | 1.67 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:07:17Z |
| Market reference home draw last update utc | 2026-10-14T19:07:17Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.9% |
| Market draw away odds | 1.41 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:07:17Z |
| Market reference draw away last update utc | 2026-10-14T19:07:17Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home draw odds | 1.67 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:06:14Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.4% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:06:14Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.59 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.9% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:07:17Z |
| Market reference btts yes odds | 1.51 |
| Market reference btts yes opposite odds | 2.42 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **54.9%**. Expected goals are 1.17 for Hamburger SV and 2.00 for VfB Stuttgart (3.17 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.9%; Double Chance 1X: 45.1%; Double Chance X2: 77.3%; Under 4.5 goals: 78.5%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 22.7% | 4.40 |
| Draw | 22.4% | 4.47 |
| VfB Stuttgart win | 54.9% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.17 |
| VfB Stuttgart expected goals | 2.00 |
| Expected total goals | 3.17 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 61.7% |
| Under 2.5 | 38.3% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.5% |
| Under 4.5 | 78.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.28% |
| 2 | 1-2 | 9.67% |
| 3 | 0-2 | 8.26% |
| 4 | 0-1 | 7.43% |
| 5 | 1-3 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 22.7% | 24.4% | 4.08 | -7.4% |
| Draw | 22.4% | 21.6% | 4.08 | -8.7% |
| VfB Stuttgart win | 54.9% | 54.0% | 1.90 | +4.4% |

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
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Hamburg |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 88/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.66 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.00 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.64 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 55.8% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 60.5% |
| P home draw | 45.1% |
| P draw away | 77.3% |
| Raw p home draw | 44.2% |
| Raw p draw away | 79.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.75 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.78 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -1.7% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | -0.0334 |
| Raw ev home | -0.1418 |
| Raw edge prob draw | 0.0154 |
| Raw ev draw | -0.0561 |
| Raw edge prob away | 0.0181 |
| Raw ev away | 0.0608 |
| Market p home draw | 48.5% |
| Market home draw odds | 2.00 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:07:17Z |
| Market reference home draw last update utc | 2026-10-14T19:07:17Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.8% |
| Market draw away odds | 1.28 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:07:17Z |
| Market reference draw away last update utc | 2026-10-14T19:07:17Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.28 |
| Market reference dc home draw odds | 2.00 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 88.5% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:05:51Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.0% |
| Market under 3 5 odds | 1.96 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:05:51Z |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 2.02 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 71.1% |
| Market btts yes odds | 1.35 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:07:17Z |
| Market reference btts yes odds | 1.35 |
| Market reference btts yes opposite odds | 2.98 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **60.1%**. Expected goals are 0.94 for Union Berlin and 1.94 for Borussia Dortmund (2.88 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 55.3%; Under 3.5 goals: 67.4%; Double Chance 1X: 39.9%; Double Chance X2: 82.5%; Under 4.5 goals: 83.4%; BTTS Yes (both teams score): 52.8%; BTTS No (at least one team does not score): 47.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.5% | 5.72 |
| Draw | 22.4% | 4.47 |
| Borussia Dortmund win | 60.1% | 1.66 |

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
| 1 | 1-1 | 10.65% |
| 2 | 0-2 | 10.62% |
| 3 | 0-1 | 10.08% |
| 4 | 1-2 | 9.97% |
| 5 | 0-3 | 6.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.5% | 18.2% | 4.98 | -12.9% |
| Draw | 22.4% | 21.4% | 4.52 | +1.1% |
| Borussia Dortmund win | 60.1% | 60.4% | 1.69 | +1.7% |

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
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Union Berlin |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 52.8% |
| P btts no | 47.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.08 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.79 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.02 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 16.8% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 59.9% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 53.0% |
| P home draw | 39.9% |
| P draw away | 82.5% |
| Raw p home draw | 40.1% |
| Raw p draw away | 83.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.90 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Home probability edge | -0.7% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.0137 |
| Raw ev home | -0.1633 |
| Raw edge prob draw | 0.0185 |
| Raw ev draw | 0.0527 |
| Raw edge prob away | -0.0048 |
| Raw ev away | 0.0124 |
| Market p home draw | 41.9% |
| Market home draw odds | 2.31 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:07:17Z |
| Market reference home draw last update utc | 2026-10-14T19:07:17Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.0% |
| Market draw away odds | 1.21 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:07:17Z |
| Market reference draw away last update utc | 2026-10-14T19:07:17Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.21 |
| Market reference dc home draw odds | 2.31 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:05:23Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.4% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:05:23Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.9% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:07:17Z |
| Market reference btts yes odds | 1.51 |
| Market reference btts yes opposite odds | 2.42 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **52.8%**. Expected goals are 1.24 for Werder Bremen and 0.61 for SC Paderborn (1.85 combined). The most likely exact score is 1-0 at 19.3%. Goal-market probabilities: at least one goal: 85.8%; Over 2.5 goals: 29.6%; Under 3.5 goals: 88.2%; Double Chance 1X: 79.9%; Double Chance X2: 47.2%; Under 4.5 goals: 95.8%; BTTS Yes (both teams score): 32.3%; BTTS No (at least one team does not score): 67.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 52.8% | 1.89 |
| Draw | 27.1% | 3.69 |
| SC Paderborn win | 20.1% | 4.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.24 |
| SC Paderborn expected goals | 0.61 |
| Expected total goals | 1.85 |
| Over 0.5 | 85.8% |
| Under 0.5 | 14.2% |
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
| 1 | 1-0 | 19.28% |
| 2 | 0-0 | 14.17% |
| 3 | 2-0 | 12.63% |
| 4 | 1-1 | 10.87% |
| 5 | 0-1 | 10.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 52.8% | 54.7% | 1.84 | -2.8% |
| Draw | 27.1% | 22.2% | 4.26 | +15.4% |
| SC Paderborn win | 20.1% | 23.1% | 4.21 | -15.4% |

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
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.3% |
| P btts no | 67.7% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 7.06 |
| Fair Over 1.5 odds | 1.77 |
| Fair Under 1.5 odds | 2.30 |
| Fair Over 2.5 odds | 3.38 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.44 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 23.74 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 50.9% |
| Unadjusted draw probability | 32.0% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 56.1% |
| Raw p under 3 5 | 88.3% |
| Raw p btts yes | 33.3% |
| P home draw | 79.9% |
| P draw away | 47.2% |
| Raw p home draw | 82.9% |
| Raw p draw away | 49.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.76 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.95 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Home probability edge | -1.9% |
| Draw probability edge | +4.9% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -32.8% |
| Under 2.5 probability edge | +32.8% |
| Raw edge prob home | -0.0381 |
| Raw ev home | -0.0634 |
| Raw edge prob draw | 0.0981 |
| Raw ev draw | 0.3635 |
| Raw edge prob away | -0.0601 |
| Raw ev away | -0.2806 |
| Market p home draw | 76.3% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:07:17Z |
| Market reference home draw last update utc | 2026-10-14T19:07:17Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.8% |
| Market draw away odds | 2.07 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:07:17Z |
| Market reference draw away last update utc | 2026-10-14T19:07:17Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.07 |
| Market reference dc home draw odds | 1.27 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 87.2% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:07:01Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.0% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:07:01Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.38 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.9% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:07:17Z |
| Market reference btts yes odds | 1.51 |
| Market reference btts yes opposite odds | 2.42 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **61.0%**. Expected goals are 2.40 for Bayer Leverkusen and 1.08 for SC Freiburg (3.48 combined). The most likely exact score is 1-1 at 8.9%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 66.9%; Under 3.5 goals: 54.9%; Double Chance 1X: 80.9%; Double Chance X2: 39.0%; Under 4.5 goals: 73.5%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 61.0% | 1.64 |
| Draw | 19.9% | 5.01 |
| SC Freiburg win | 19.1% | 5.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.40 |
| SC Freiburg expected goals | 1.08 |
| Expected total goals | 3.48 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 86.4% |
| Under 1.5 | 13.6% |
| Over 2.5 | 66.9% |
| Under 2.5 | 33.1% |
| Over 3.5 | 45.1% |
| Under 3.5 | 54.9% |
| Over 4.5 | 26.5% |
| Under 4.5 | 73.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.94% |
| 2 | 2-1 | 8.87% |
| 3 | 2-0 | 8.23% |
| 4 | 3-1 | 7.09% |
| 5 | 3-0 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 61.0% | 56.0% | 1.75 | +6.7% |
| Draw | 19.9% | 20.6% | 4.42 | -11.8% |
| SC Freiburg win | 19.1% | 23.4% | 4.62 | -12.0% |

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
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Leverkusen |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.76 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.37 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.03 |
| Fair Over 3.5 odds | 2.22 |
| Fair Under 3.5 odds | 1.82 |
| Fair Over 4.5 odds | 3.77 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 65.9% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 14.7% |
| Raw p over 1 5 | 86.8% |
| Raw p under 3 5 | 54.2% |
| Raw p btts yes | 60.6% |
| P home draw | 80.9% |
| P draw away | 39.0% |
| Raw p home draw | 85.3% |
| Raw p draw away | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.72 |
| Reference draw odds | 4.40 |
| Reference away odds | 3.90 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.69 |
| Home probability edge | +4.9% |
| Draw probability edge | -0.6% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | +1.4% |
| Under 2.5 probability edge | -1.4% |
| Raw edge prob home | 0.0990 |
| Raw ev home | 0.1540 |
| Raw edge prob draw | -0.0124 |
| Raw ev draw | -0.1457 |
| Raw edge prob away | -0.0866 |
| Raw ev away | -0.3196 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **41.4%**. Expected goals are 1.87 for Borussia Monchengladbach and 1.78 for TSG Hoffenheim (3.65 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.5%; Double Chance 1X: 58.6%; Double Chance X2: 64.3%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 71.0%; BTTS No (at least one team does not score): 29.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 35.7% | 2.80 |
| Draw | 22.9% | 4.37 |
| TSG Hoffenheim win | 41.4% | 2.41 |

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
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.25% |
| 2 | 1-2 | 8.72% |
| 3 | 2-1 | 7.19% |
| 4 | 2-2 | 7.09% |
| 5 | 1-3 | 5.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 35.7% | 31.3% | 3.33 | +18.9% |
| Draw | 22.9% | 22.5% | 4.21 | -3.7% |
| TSG Hoffenheim win | 41.4% | 46.2% | 2.10 | -13.0% |

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
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | M'gladbach |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 71.0% |
| P btts no | 29.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.48 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.79 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.41 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 36.6% |
| Raw p over 1 5 | 88.6% |
| Raw p under 3 5 | 50.5% |
| Raw p btts yes | 71.0% |
| P home draw | 58.6% |
| P draw away | 64.3% |
| Raw p home draw | 63.4% |
| Raw p draw away | 59.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.95 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.05 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.99 |
| Home probability edge | +4.5% |
| Draw probability edge | +0.3% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | 0.0891 |
| Raw ev home | 0.3373 |
| Raw edge prob draw | 0.0068 |
| Raw ev draw | -0.0230 |
| Raw edge prob away | -0.0958 |
| Raw ev away | -0.2307 |

</details>


---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **68.5%**. Expected goals are 2.52 for VfB Stuttgart and 1.17 for Borussia Monchengladbach (3.69 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 72.1%; Under 3.5 goals: 49.2%; Double Chance 1X: 85.2%; Double Chance X2: 31.5%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 63.6%; BTTS No (at least one team does not score): 36.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 68.5% | 1.46 |
| Draw | 16.7% | 5.99 |
| Borussia Monchengladbach win | 14.8% | 6.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.52 |
| Borussia Monchengladbach expected goals | 1.17 |
| Expected total goals | 3.69 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 89.1% |
| Under 1.5 | 10.9% |
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 50.8% |
| Under 3.5 | 49.2% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.61% |
| 2 | 2-0 | 8.20% |
| 3 | 3-1 | 8.08% |
| 4 | 1-1 | 7.13% |
| 5 | 3-0 | 6.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 68.5% | 70.9% | 1.43 | -2.1% |
| Draw | 16.7% | 14.7% | 5.80 | -3.1% |
| Borussia Monchengladbach win | 14.8% | 14.4% | 6.98 | +3.5% |

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
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
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
| Fair Under 0.5 odds | 35.98 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.19 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.59 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.16 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 66.0% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 15.3% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 49.6% |
| Raw p btts yes | 64.1% |
| P home draw | 85.2% |
| P draw away | 31.5% |
| Raw p home draw | 84.7% |
| Raw p draw away | 34.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.34 |
| Reference draw odds | 5.10 |
| Reference away odds | 5.20 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.76 |
| Home probability edge | -2.4% |
| Draw probability edge | +2.0% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.0484 |
| Raw ev home | -0.0555 |
| Raw edge prob draw | 0.0395 |
| Raw ev draw | 0.0833 |
| Raw edge prob away | 0.0088 |
| Raw ev away | 0.0662 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **40.6%**. Expected goals are 0.97 for 1. FC Köln and 0.96 for FC Schalke 04 (1.93 combined). The most likely exact score is 1-0 at 15.7%. Goal-market probabilities: at least one goal: 86.9%; Over 2.5 goals: 32.1%; Under 3.5 goals: 86.7%; Double Chance 1X: 69.0%; Double Chance X2: 59.4%; Under 4.5 goals: 95.0%; BTTS Yes (both teams score): 38.3%; BTTS No (at least one team does not score): 61.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 40.6% | 2.46 |
| Draw | 28.4% | 3.52 |
| FC Schalke 04 win | 31.0% | 3.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 0.97 |
| FC Schalke 04 expected goals | 0.96 |
| Expected total goals | 1.93 |
| Over 0.5 | 86.9% |
| Under 0.5 | 13.1% |
| Over 1.5 | 59.0% |
| Under 1.5 | 41.0% |
| Over 2.5 | 32.1% |
| Under 2.5 | 67.9% |
| Over 3.5 | 13.3% |
| Under 3.5 | 86.7% |
| Over 4.5 | 5.0% |
| Under 4.5 | 95.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.73% |
| 2 | 0-0 | 13.15% |
| 3 | 1-1 | 12.31% |
| 4 | 0-1 | 12.09% |
| 5 | 2-0 | 8.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 40.6% | 47.7% | 2.12 | -13.9% |
| Draw | 28.4% | 23.0% | 3.98 | +13.0% |
| FC Schalke 04 win | 31.0% | 29.3% | 3.43 | +6.2% |
| Over 2.5 | 32.1% | 60.2% | 1.64 | -47.4% |
| Under 2.5 | 67.9% | 39.8% | 2.46 | +67.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 983440c6e348b558c6a3e10e2061ba55 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Koln |
| Matched away-team name | Schalke 04 |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 38.3% |
| P btts no | 61.7% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.61 |
| Fair Over 1.5 odds | 1.69 |
| Fair Under 1.5 odds | 2.44 |
| Fair Over 2.5 odds | 3.12 |
| Fair Under 2.5 odds | 1.47 |
| Fair Over 3.5 odds | 7.53 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.17 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 33.8% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 86.9% |
| Raw p btts yes | 39.5% |
| P home draw | 69.0% |
| P draw away | 59.4% |
| Raw p home draw | 67.3% |
| Raw p draw away | 66.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.92 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.95 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Home probability edge | -7.1% |
| Draw probability edge | +5.4% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -28.1% |
| Under 2.5 probability edge | +28.1% |
| Raw edge prob home | -0.1414 |
| Raw ev home | -0.2886 |
| Raw edge prob draw | 0.1078 |
| Raw ev draw | 0.3448 |
| Raw edge prob away | 0.0336 |
| Raw ev away | 0.1200 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **50.5%**. Expected goals are 1.60 for Augsburg and 1.05 for Union Berlin (2.65 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 50.2%; Under 3.5 goals: 72.4%; Double Chance 1X: 75.4%; Double Chance X2: 49.5%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 52.4%; BTTS No (at least one team does not score): 47.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 50.5% | 1.98 |
| Draw | 24.8% | 4.03 |
| Union Berlin win | 24.6% | 4.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.60 |
| Union Berlin expected goals | 1.05 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.2% |
| Under 2.5 | 49.8% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.86% |
| 2 | 1-0 | 10.58% |
| 3 | 2-1 | 9.74% |
| 4 | 2-0 | 9.30% |
| 5 | 0-0 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 50.5% | 51.7% | 1.96 | -1.0% |
| Draw | 24.8% | 22.8% | 4.16 | +3.3% |
| Union Berlin win | 24.6% | 25.5% | 3.77 | -7.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04bb232a2940fcf03abf05b308e27577 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 52.4% |
| P btts no | 47.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.45 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.55 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 49.3% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 23.8% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 52.8% |
| P home draw | 75.4% |
| P draw away | 49.5% |
| Raw p home draw | 76.2% |
| Raw p draw away | 50.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.78 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Home probability edge | -1.2% |
| Draw probability edge | +2.1% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -12.2% |
| Under 2.5 probability edge | +12.2% |
| Raw edge prob home | -0.0239 |
| Raw ev home | -0.0331 |
| Raw edge prob draw | 0.0416 |
| Raw ev draw | 0.1195 |
| Raw edge prob away | -0.0177 |
| Raw ev away | -0.1043 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **65.9%**. Expected goals are 2.43 for Borussia Dortmund and 1.20 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 71.0%; Under 3.5 goals: 50.5%; Double Chance 1X: 83.7%; Double Chance X2: 34.1%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 65.9% | 1.52 |
| Draw | 17.7% | 5.64 |
| Eintracht Frankfurt win | 16.3% | 6.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.43 |
| Eintracht Frankfurt expected goals | 1.20 |
| Expected total goals | 3.64 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 71.0% |
| Under 2.5 | 29.0% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.69% |
| 2 | 2-0 | 8.07% |
| 3 | 3-1 | 7.87% |
| 4 | 1-1 | 7.61% |
| 5 | 3-0 | 6.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 65.9% | 68.0% | 1.48 | -2.4% |
| Draw | 17.7% | 16.0% | 5.39 | -4.4% |
| Eintracht Frankfurt win | 16.3% | 16.0% | 6.42 | +4.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 3ed4d1e775910625c50518a384e9c547 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 81/100 |
| P btts yes | 64.0% |
| P btts no | 36.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.47 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.76 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.45 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.28 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 63.8% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 16.7% |
| Raw p over 1 5 | 88.4% |
| Raw p under 3 5 | 50.8% |
| Raw p btts yes | 64.4% |
| P home draw | 83.7% |
| P draw away | 34.1% |
| Raw p home draw | 83.3% |
| Raw p draw away | 36.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.39 |
| Reference draw odds | 4.80 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.31 |
| Home probability edge | -2.1% |
| Draw probability edge | +1.8% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0420 |
| Raw ev home | -0.0551 |
| Raw edge prob draw | 0.0352 |
| Raw ev draw | 0.0507 |
| Raw edge prob away | 0.0069 |
| Raw ev away | 0.0698 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **53.9%**. Expected goals are 1.66 for FSV Mainz 05 and 1.14 for Werder Bremen (2.80 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 54.3%; Under 3.5 goals: 68.7%; Double Chance 1X: 77.3%; Double Chance X2: 46.1%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 53.9% | 1.86 |
| Draw | 23.4% | 4.27 |
| Werder Bremen win | 22.7% | 4.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.66 |
| Werder Bremen expected goals | 1.14 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.3% |
| Under 2.5 | 45.7% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.12% |
| 2 | 2-1 | 10.59% |
| 3 | 1-0 | 10.10% |
| 4 | 2-0 | 9.29% |
| 5 | 0-0 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 53.9% | 59.1% | 1.73 | -6.8% |
| Draw | 23.4% | 20.6% | 4.41 | +3.3% |
| Werder Bremen win | 22.7% | 20.3% | 4.72 | +7.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 4e5820453145833132980b8d190998c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.3% |
| P btts no | 44.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.93 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.60 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.34 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 25.1% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 56.1% |
| P home draw | 77.3% |
| P draw away | 46.1% |
| Raw p home draw | 74.9% |
| Raw p draw away | 51.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.58 |
| Reference draw odds | 3.95 |
| Reference away odds | 4.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.54 |
| Home probability edge | -5.2% |
| Draw probability edge | +2.8% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.1046 |
| Raw ev home | -0.1587 |
| Raw edge prob draw | 0.0563 |
| Raw ev draw | 0.1566 |
| Raw edge prob away | 0.0484 |
| Raw ev away | 0.1867 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **62.8%**. Expected goals are 1.99 for RB Leipzig and 1.38 for Elversberg (3.37 combined). The most likely exact score is 2-1 at 11.6%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 67.5%; Under 3.5 goals: 55.6%; Double Chance 1X: 81.1%; Double Chance X2: 37.2%; Under 4.5 goals: 73.7%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 62.8% | 1.59 |
| Draw | 18.3% | 5.48 |
| Elversberg win | 18.9% | 5.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.99 |
| Elversberg expected goals | 1.38 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 86.3% |
| Under 1.5 | 13.7% |
| Over 2.5 | 67.5% |
| Under 2.5 | 32.5% |
| Over 3.5 | 44.4% |
| Under 3.5 | 55.6% |
| Over 4.5 | 26.3% |
| Under 4.5 | 73.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.58% |
| 2 | 2-0 | 8.41% |
| 3 | 1-1 | 8.02% |
| 4 | 3-1 | 7.69% |
| 5 | 1-0 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 62.8% | 74.6% | 1.39 | -12.7% |
| Draw | 18.3% | 13.2% | 6.09 | +11.2% |
| Elversberg win | 18.9% | 12.2% | 7.70 | +45.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04dac5e98ab5fc5564980542ca3fc746 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.9% |
| P btts no | 36.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.13 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.30 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.25 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.80 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 51.0% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 25.7% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 56.5% |
| Raw p btts yes | 65.4% |
| P home draw | 81.1% |
| P draw away | 37.2% |
| Raw p home draw | 74.3% |
| Raw p draw away | 49.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.28 |
| Reference draw odds | 5.50 |
| Reference away odds | 5.90 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.85 |
| Home probability edge | -11.8% |
| Draw probability edge | +5.0% |
| Away probability edge | +6.8% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | -0.2361 |
| Raw ev home | -0.2912 |
| Raw edge prob draw | 0.1007 |
| Raw ev draw | 0.4190 |
| Raw edge prob away | 0.1354 |
| Raw ev away | 0.9795 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **35.2%**. Expected goals are 0.78 for SC Paderborn and 0.89 for Hamburger SV (1.67 combined). The most likely exact score is 1-0 at 16.7%. Goal-market probabilities: at least one goal: 83.5%; Over 2.5 goals: 25.1%; Under 3.5 goals: 91.0%; Double Chance 1X: 65.4%; Double Chance X2: 64.8%; Under 4.5 goals: 97.0%; BTTS Yes (both teams score): 31.8%; BTTS No (at least one team does not score): 68.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 35.2% | 2.84 |
| Draw | 30.2% | 3.31 |
| Hamburger SV win | 34.6% | 2.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.78 |
| Hamburger SV expected goals | 0.89 |
| Expected total goals | 1.67 |
| Over 0.5 | 83.5% |
| Under 0.5 | 16.5% |
| Over 1.5 | 51.3% |
| Under 1.5 | 48.7% |
| Over 2.5 | 25.1% |
| Under 2.5 | 74.9% |
| Over 3.5 | 9.0% |
| Under 3.5 | 91.0% |
| Over 4.5 | 3.0% |
| Under 4.5 | 97.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.70% |
| 2 | 0-0 | 16.49% |
| 3 | 0-1 | 15.55% |
| 4 | 1-1 | 11.72% |
| 5 | 0-2 | 7.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 35.2% | 41.7% | 2.40 | -15.5% |
| Draw | 30.2% | 23.9% | 3.92 | +18.5% |
| Hamburger SV win | 34.6% | 34.3% | 2.91 | +0.6% |
| Over 2.5 | 25.1% | 62.6% | 1.64 | -58.8% |
| Under 2.5 | 74.9% | 37.4% | 2.47 | +85.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 7630f897583f3acc0f483fa2d17d1ac5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T19:07:17Z |
| Market best draw last update utc | 2026-10-14T19:07:17Z |
| Market best away last update utc | 2026-10-14T19:07:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paderborn |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 88/100 |
| P btts yes | 31.8% |
| P btts no | 68.2% |
| Fair Over 0.5 odds | 1.20 |
| Fair Under 0.5 odds | 6.06 |
| Fair Over 1.5 odds | 1.95 |
| Fair Under 1.5 odds | 2.05 |
| Fair Over 2.5 odds | 3.98 |
| Fair Under 2.5 odds | 1.34 |
| Fair Over 3.5 odds | 11.06 |
| Fair Under 3.5 odds | 1.10 |
| Fair Over 4.5 odds | 33.50 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 28.6% |
| Unadjusted draw probability | 36.5% |
| Unadjusted away-win probability | 34.8% |
| Raw p over 1 5 | 50.8% |
| Raw p under 3 5 | 91.1% |
| Raw p btts yes | 33.0% |
| P home draw | 65.4% |
| P draw away | 64.8% |
| Raw p home draw | 65.2% |
| Raw p draw away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.55 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -6.5% |
| Draw probability edge | +6.3% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -37.5% |
| Under 2.5 probability edge | +37.5% |
| Raw edge prob home | -0.1308 |
| Raw ev home | -0.3124 |
| Raw edge prob draw | 0.1262 |
| Raw ev draw | 0.4327 |
| Raw edge prob away | 0.0046 |
| Raw ev away | 0.0127 |

</details>


---
