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
| Training data health | {'training_end': '2026-10-11', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
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

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **54.7%**. Expected goals are 2.24 for Eintracht Frankfurt and 1.24 for 1. FC Köln (3.48 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 67.2%; Under 3.5 goals: 54.6%; Double Chance 1X: 76.4%; Double Chance X2: 45.3%; Double Chance 12 (either team wins): 78.3%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 54.7% | 1.83 |
| Draw | 21.7% | 4.61 |
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
| Over 4.5 | 26.8% |
| Under 4.5 | 73.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.49% |
| 2 | 2-1 | 8.85% |
| 3 | 2-0 | 7.13% |
| 4 | 3-1 | 6.61% |
| 5 | 1-2 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 54.7% | 50.2% | 1.99 | +8.8% |
| Draw | 21.7% | 22.2% | 4.36 | -5.4% |
| 1. FC Köln win | 23.6% | 27.6% | 3.52 | -16.9% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
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
| Fair Under 0.5 odds | 25.77 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.51 |
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
| P home draw | 76.4% |
| P draw away | 45.3% |
| P home away | 78.3% |
| Raw p home draw | 80.4% |
| Raw p draw away | 40.8% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.94 |
| Reference draw odds | 4.25 |
| Reference away odds | 3.44 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | +4.5% |
| Draw probability edge | -0.5% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | 0.0901 |
| Raw ev home | 0.1778 |
| Raw edge prob draw | -0.0096 |
| Raw ev draw | -0.0749 |
| Raw edge prob away | -0.0805 |
| Raw ev away | -0.3103 |
| Market p home draw | 72.1% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:15Z |
| Market reference home draw last update utc | 2026-10-15T06:53:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.5% |
| Market draw away odds | 1.91 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:15Z |
| Market reference draw away last update utc | 2026-10-15T06:53:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.4% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:15Z |
| Market reference home away last update utc | 2026-10-15T06:53:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.90 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 48.8% |
| Market under 3 5 odds | 2.00 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference under 3 5 odds | 1.99 |
| Market reference under 3 5 opposite odds | 1.90 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.8% |
| Market btts yes odds | 1.33 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:15Z |
| Market reference btts yes odds | 1.36 |
| Market reference btts yes opposite odds | 3.00 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **74.9%**. Expected goals are 2.86 for Bayern Munich and 1.24 for RB Leipzig (4.10 combined). The most likely exact score is 2-1 at 9.0%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 78.4%; Under 3.5 goals: 40.7%; Double Chance 1X: 89.4%; Double Chance X2: 25.1%; Double Chance 12 (either team wins): 85.6%; Under 4.5 goals: 60.1%; BTTS Yes (both teams score): 66.7%; BTTS No (at least one team does not score): 33.3%.

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
| Draw | 14.4% | 12.6% | 7.36 | +6.2% |
| RB Leipzig win | 10.6% | 7.9% | 11.30 | +20.2% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
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
| P home away | 85.6% |
| Raw p home draw | 86.7% |
| Raw p draw away | 29.6% |
| Raw p home away | 83.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.24 |
| Reference draw odds | 7.00 |
| Reference away odds | 10.75 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.50 |
| Home probability edge | -4.6% |
| Draw probability edge | +1.9% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | -0.0913 |
| Raw ev home | -0.1133 |
| Raw edge prob draw | 0.0375 |
| Raw ev draw | 0.1997 |
| Raw edge prob away | 0.0538 |
| Raw ev away | 0.5059 |
| Market p home draw | 91.2% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:15Z |
| Market reference home draw last update utc | 2026-10-15T06:53:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.5% |
| Market draw away odds | 4.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:15Z |
| Market reference draw away last update utc | 2026-10-15T06:53:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.3% |
| Market home away odds | 1.12 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:15Z |
| Market reference home away last update utc | 2026-10-15T06:53:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.25 |
| Market reference dc home draw odds | 1.05 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 95.6% |
| Market over 1 5 odds | 1.03 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:34Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 15.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 29.0% |
| Market under 3 5 odds | 2.76 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:34Z |
| Market reference under 3 5 odds | 3.12 |
| Market reference under 3 5 opposite odds | 1.37 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.8% |
| Market btts yes odds | 1.38 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:15Z |
| Market reference btts yes odds | 1.36 |
| Market reference btts yes opposite odds | 3.00 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **48.1%**. Expected goals are 2.05 for Elversberg and 1.15 for Augsburg (3.20 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 61.3%; Under 3.5 goals: 61.1%; Double Chance 1X: 71.8%; Double Chance X2: 51.9%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

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
| Draw | 23.7% | 24.8% | 3.92 | -7.1% |
| Augsburg win | 28.2% | 36.4% | 2.71 | -23.7% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
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
| P home away | 76.3% |
| Raw p home draw | 80.1% |
| Raw p draw away | 42.6% |
| Raw p home away | 77.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.48 |
| Reference draw odds | 3.82 |
| Reference away odds | 2.64 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | +9.3% |
| Draw probability edge | -1.1% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | 0.1858 |
| Raw ev home | 0.4643 |
| Raw edge prob draw | -0.0212 |
| Raw ev draw | -0.1122 |
| Raw edge prob away | -0.1646 |
| Raw ev away | -0.4599 |
| Market p home draw | 63.9% |
| Market home draw odds | 1.52 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:15Z |
| Market reference home draw last update utc | 2026-10-15T06:53:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.4% |
| Market draw away odds | 1.58 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:15Z |
| Market reference draw away last update utc | 2026-10-15T06:53:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.7% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:15Z |
| Market reference home away last update utc | 2026-10-15T06:53:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.57 |
| Market reference dc home draw odds | 1.51 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:35Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.4% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:35Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:15Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.80 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **37.2%**. Expected goals are 0.95 for FC Schalke 04 and 0.92 for FSV Mainz 05 (1.87 combined). The most likely exact score is 0-1 at 15.2%. Goal-market probabilities: at least one goal: 85.3%; Over 2.5 goals: 29.8%; Under 3.5 goals: 87.9%; Double Chance 1X: 62.8%; Double Chance X2: 67.6%; Double Chance 12 (either team wins): 69.5%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 37.1%; BTTS No (at least one team does not score): 62.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 32.4% | 3.09 |
| Draw | 30.5% | 3.28 |
| FSV Mainz 05 win | 37.2% | 2.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.95 |
| FSV Mainz 05 expected goals | 0.92 |
| Expected total goals | 1.87 |
| Over 0.5 | 85.3% |
| Under 0.5 | 14.7% |
| Over 1.5 | 57.0% |
| Under 1.5 | 43.0% |
| Over 2.5 | 29.8% |
| Under 2.5 | 70.2% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.21% |
| 2 | 0-0 | 14.71% |
| 3 | 1-0 | 13.04% |
| 4 | 1-1 | 12.92% |
| 5 | 0-2 | 7.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 32.4% | 31.0% | 3.16 | +2.2% |
| Draw | 30.5% | 26.5% | 3.67 | +11.9% |
| FSV Mainz 05 win | 37.2% | 42.4% | 2.34 | -13.1% |
| Over 2.5 | 29.8% | 58.5% | 1.70 | -49.3% |
| Under 2.5 | 70.2% | 41.5% | 2.34 | +64.2% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
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
| P btts yes | 37.1% |
| P btts no | 62.9% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.80 |
| Fair Over 1.5 odds | 1.75 |
| Fair Under 1.5 odds | 2.33 |
| Fair Over 2.5 odds | 3.35 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 8.27 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.12 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 34.4% |
| Unadjusted away-win probability | 31.9% |
| Raw p over 1 5 | 56.8% |
| Raw p under 3 5 | 88.1% |
| Raw p btts yes | 37.9% |
| P home draw | 62.8% |
| P draw away | 67.6% |
| P home away | 69.5% |
| Raw p home draw | 68.1% |
| Raw p draw away | 66.3% |
| Raw p home away | 65.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.08 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.28 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | +1.3% |
| Draw probability edge | +4.0% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | -28.6% |
| Under 2.5 probability edge | +28.6% |
| Raw edge prob home | 0.0265 |
| Raw ev home | 0.0642 |
| Raw edge prob draw | 0.0790 |
| Raw ev draw | 0.2638 |
| Raw edge prob away | -0.1055 |
| Raw ev away | -0.2539 |
| Market p home draw | 58.1% |
| Market home draw odds | 1.67 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:15Z |
| Market reference home draw last update utc | 2026-10-15T06:53:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.9% |
| Market draw away odds | 1.41 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:15Z |
| Market reference draw away last update utc | 2026-10-15T06:53:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.0% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:15Z |
| Market reference home away last update utc | 2026-10-15T06:53:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home draw odds | 1.66 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.4% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.59 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:15Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **54.2%**. Expected goals are 1.17 for Hamburger SV and 2.00 for VfB Stuttgart (3.17 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 61.3%; Under 3.5 goals: 61.0%; Double Chance 1X: 45.8%; Double Chance X2: 77.6%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

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
| Hamburger SV win | 22.4% | 23.7% | 4.08 | -8.8% |
| Draw | 23.4% | 23.7% | 4.08 | -4.5% |
| VfB Stuttgart win | 54.2% | 52.6% | 1.90 | +3.1% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
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
| P home away | 76.6% |
| Raw p home draw | 44.2% |
| Raw p draw away | 79.0% |
| Raw p home away | 76.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.98 |
| Reference draw odds | 3.98 |
| Reference away odds | 1.85 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -1.3% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | -0.0264 |
| Raw ev home | -0.1418 |
| Raw edge prob draw | -0.0054 |
| Raw ev draw | -0.0561 |
| Raw edge prob away | 0.0319 |
| Raw ev away | 0.0608 |
| Market p home draw | 48.2% |
| Market home draw odds | 2.00 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:15Z |
| Market reference home draw last update utc | 2026-10-15T06:53:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.9% |
| Market draw away odds | 1.28 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:15Z |
| Market reference draw away last update utc | 2026-10-15T06:53:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.9% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:15Z |
| Market reference home away last update utc | 2026-10-15T06:53:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.27 |
| Market reference dc home draw odds | 2.00 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:52:21Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.0% |
| Market under 3 5 odds | 1.96 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:52:21Z |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 2.02 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.35 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:15Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.90 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **59.8%**. Expected goals are 0.94 for Union Berlin and 1.94 for Borussia Dortmund (2.88 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 55.3%; Under 3.5 goals: 67.4%; Double Chance 1X: 40.2%; Double Chance X2: 82.0%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 83.4%; BTTS Yes (both teams score): 52.8%; BTTS No (at least one team does not score): 47.2%.

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
| Union Berlin win | 18.0% | 19.2% | 4.98 | -10.4% |
| Draw | 22.3% | 21.2% | 4.52 | +0.6% |
| Borussia Dortmund win | 59.8% | 59.6% | 1.69 | +1.0% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
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
| P home away | 77.7% |
| Raw p home draw | 40.1% |
| Raw p draw away | 83.2% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.85 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.64 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -1.2% |
| Draw probability edge | +1.0% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -8.5% |
| Under 2.5 probability edge | +8.5% |
| Raw edge prob home | -0.0237 |
| Raw ev home | -0.1633 |
| Raw edge prob draw | 0.0206 |
| Raw ev draw | 0.0527 |
| Raw edge prob away | 0.0031 |
| Raw ev away | 0.0124 |
| Market p home draw | 41.5% |
| Market home draw odds | 2.31 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:15Z |
| Market reference home draw last update utc | 2026-10-15T06:53:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.2% |
| Market draw away odds | 1.21 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:15Z |
| Market reference draw away last update utc | 2026-10-15T06:53:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.3% |
| Market home away odds | 1.24 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:15Z |
| Market reference home away last update utc | 2026-10-15T06:53:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.20 |
| Market reference dc home draw odds | 2.32 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 85.4% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.4% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:15Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **52.7%**. Expected goals are 1.24 for Werder Bremen and 0.61 for SC Paderborn (1.85 combined). The most likely exact score is 1-0 at 19.2%. Goal-market probabilities: at least one goal: 85.7%; Over 2.5 goals: 29.6%; Under 3.5 goals: 88.2%; Double Chance 1X: 80.0%; Double Chance X2: 47.3%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 95.8%; BTTS Yes (both teams score): 32.4%; BTTS No (at least one team does not score): 67.6%.

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
| Werder Bremen win | 52.7% | 54.5% | 1.84 | -3.1% |
| Draw | 27.3% | 22.6% | 4.26 | +16.4% |
| SC Paderborn win | 20.0% | 22.9% | 4.21 | -15.8% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
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
| P home away | 72.7% |
| Raw p home draw | 82.9% |
| Raw p draw away | 49.1% |
| Raw p home away | 68.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.79 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -1.8% |
| Draw probability edge | +4.7% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -32.2% |
| Under 2.5 probability edge | +32.2% |
| Raw edge prob home | -0.0355 |
| Raw ev home | -0.0634 |
| Raw edge prob draw | 0.0938 |
| Raw ev draw | 0.3635 |
| Raw edge prob away | -0.0583 |
| Raw ev away | -0.2806 |
| Market p home draw | 76.4% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:15Z |
| Market reference home draw last update utc | 2026-10-15T06:53:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.5% |
| Market draw away odds | 2.07 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:15Z |
| Market reference draw away last update utc | 2026-10-15T06:53:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.0% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:15Z |
| Market reference home away last update utc | 2026-10-15T06:53:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.07 |
| Market reference dc home draw odds | 1.26 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 87.2% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:55Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.5% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:55Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.42 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.2% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:15Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.45 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **61.7%**. Expected goals are 2.40 for Bayer Leverkusen and 1.08 for SC Freiburg (3.48 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 66.8%; Under 3.5 goals: 54.8%; Double Chance 1X: 82.2%; Double Chance X2: 38.3%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 73.5%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

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
| Bayer Leverkusen win | 61.7% | 57.4% | 1.75 | +8.0% |
| Draw | 20.6% | 21.8% | 4.42 | -9.1% |
| SC Freiburg win | 17.8% | 20.8% | 4.62 | -18.0% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
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
| P home away | 79.4% |
| Raw p home draw | 85.3% |
| Raw p draw away | 34.1% |
| Raw p home away | 80.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.70 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | +4.3% |
| Draw probability edge | -1.2% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0850 |
| Raw ev home | 0.1540 |
| Raw edge prob draw | -0.0246 |
| Raw ev draw | -0.1457 |
| Raw edge prob away | -0.0605 |
| Raw ev away | -0.3196 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **42.1%**. Expected goals are 1.87 for Borussia Monchengladbach and 1.78 for TSG Hoffenheim (3.65 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.5%; Double Chance 1X: 57.9%; Double Chance X2: 65.2%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 71.0%; BTTS No (at least one team does not score): 29.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 34.8% | 2.88 |
| Draw | 23.1% | 4.33 |
| TSG Hoffenheim win | 42.1% | 2.37 |

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
| 2 | 1-2 | 8.86% |
| 3 | 2-2 | 7.17% |
| 4 | 2-1 | 7.00% |
| 5 | 1-3 | 5.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 34.8% | 29.4% | 3.33 | +15.8% |
| Draw | 23.1% | 23.0% | 4.21 | -2.7% |
| TSG Hoffenheim win | 42.1% | 47.6% | 2.10 | -11.6% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
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
| Fair Under 0.5 odds | 30.17 |
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
| P home draw | 57.9% |
| P draw away | 65.2% |
| P home away | 76.9% |
| Raw p home draw | 63.4% |
| Raw p draw away | 59.8% |
| Raw p home away | 76.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.24 |
| Reference draw odds | 4.10 |
| Reference away odds | 2.04 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | +5.4% |
| Draw probability edge | +0.1% |
| Away probability edge | -5.5% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | 0.1076 |
| Raw ev home | 0.3373 |
| Raw edge prob draw | 0.0020 |
| Raw ev draw | -0.0230 |
| Raw edge prob away | -0.1096 |
| Raw ev away | -0.2307 |

</details>


---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **68.4%**. Expected goals are 2.52 for VfB Stuttgart and 1.17 for Borussia Monchengladbach (3.69 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 71.9%; Under 3.5 goals: 49.2%; Double Chance 1X: 85.7%; Double Chance X2: 31.6%; Double Chance 12 (either team wins): 82.6%; Under 4.5 goals: 68.4%; BTTS Yes (both teams score): 63.7%; BTTS No (at least one team does not score): 36.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 68.4% | 1.46 |
| Draw | 17.4% | 5.75 |
| Borussia Monchengladbach win | 14.3% | 7.01 |

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
| 1 | 2-1 | 9.60% |
| 2 | 2-0 | 8.19% |
| 3 | 3-1 | 8.06% |
| 4 | 1-1 | 7.43% |
| 5 | 3-0 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 68.4% | 70.7% | 1.43 | -2.3% |
| Draw | 17.4% | 16.1% | 5.80 | +0.9% |
| Borussia Monchengladbach win | 14.3% | 13.2% | 6.98 | -0.5% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.7% |
| P btts no | 36.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.56 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.18 |
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
| P home draw | 85.7% |
| P draw away | 31.6% |
| P home away | 82.6% |
| Raw p home draw | 84.7% |
| Raw p draw away | 34.0% |
| Raw p home away | 81.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.39 |
| Reference draw odds | 5.65 |
| Reference away odds | 6.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Home probability edge | -2.3% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | -0.0461 |
| Raw ev home | -0.0555 |
| Raw edge prob draw | 0.0258 |
| Raw ev draw | 0.0833 |
| Raw edge prob away | 0.0203 |
| Raw ev away | 0.0662 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **40.3%**. Expected goals are 0.97 for 1. FC Köln and 0.96 for FC Schalke 04 (1.93 combined). The most likely exact score is 1-0 at 15.6%. Goal-market probabilities: at least one goal: 86.5%; Over 2.5 goals: 31.9%; Under 3.5 goals: 86.7%; Double Chance 1X: 69.4%; Double Chance X2: 59.7%; Double Chance 12 (either team wins): 70.9%; Under 4.5 goals: 95.1%; BTTS Yes (both teams score): 38.4%; BTTS No (at least one team does not score): 61.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 40.3% | 2.48 |
| Draw | 29.1% | 3.44 |
| FC Schalke 04 win | 30.6% | 3.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 0.97 |
| FC Schalke 04 expected goals | 0.96 |
| Expected total goals | 1.93 |
| Over 0.5 | 86.5% |
| Under 0.5 | 13.5% |
| Over 1.5 | 59.0% |
| Under 1.5 | 41.0% |
| Over 2.5 | 31.9% |
| Under 2.5 | 68.1% |
| Over 3.5 | 13.3% |
| Under 3.5 | 86.7% |
| Over 4.5 | 4.9% |
| Under 4.5 | 95.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.62% |
| 2 | 0-0 | 13.47% |
| 3 | 1-1 | 12.61% |
| 4 | 0-1 | 11.93% |
| 5 | 2-0 | 8.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 40.3% | 47.1% | 2.12 | -14.5% |
| Draw | 29.1% | 24.4% | 3.98 | +15.8% |
| FC Schalke 04 win | 30.6% | 28.5% | 3.43 | +4.9% |
| Over 2.5 | 31.9% | 60.8% | 1.64 | -47.7% |
| Under 2.5 | 68.1% | 39.2% | 2.46 | +67.6% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
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
| P btts yes | 38.4% |
| P btts no | 61.6% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.43 |
| Fair Over 1.5 odds | 1.70 |
| Fair Under 1.5 odds | 2.44 |
| Fair Over 2.5 odds | 3.14 |
| Fair Under 2.5 odds | 1.47 |
| Fair Over 3.5 odds | 7.55 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.33 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 33.8% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 86.9% |
| Raw p btts yes | 39.5% |
| P home draw | 69.4% |
| P draw away | 59.7% |
| P home away | 70.9% |
| Raw p home draw | 67.3% |
| Raw p draw away | 66.4% |
| Raw p home away | 66.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.06 |
| Reference draw odds | 3.88 |
| Reference away odds | 3.34 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Home probability edge | -6.8% |
| Draw probability edge | +4.7% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -28.9% |
| Under 2.5 probability edge | +28.9% |
| Raw edge prob home | -0.1357 |
| Raw ev home | -0.2886 |
| Raw edge prob draw | 0.0941 |
| Raw ev draw | 0.3448 |
| Raw edge prob away | 0.0416 |
| Raw ev away | 0.1200 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **50.1%**. Expected goals are 1.60 for Augsburg and 1.05 for Union Berlin (2.65 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 50.1%; Under 3.5 goals: 72.4%; Double Chance 1X: 75.3%; Double Chance X2: 49.9%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 52.4%; BTTS No (at least one team does not score): 47.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 50.1% | 1.99 |
| Draw | 25.1% | 3.98 |
| Union Berlin win | 24.7% | 4.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.60 |
| Union Berlin expected goals | 1.05 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 50.1% |
| Under 2.5 | 49.9% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.99% |
| 2 | 1-0 | 10.50% |
| 3 | 2-1 | 9.66% |
| 4 | 2-0 | 9.23% |
| 5 | 0-0 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 50.1% | 51.0% | 1.96 | -1.7% |
| Draw | 25.1% | 23.3% | 4.16 | +4.4% |
| Union Berlin win | 24.7% | 25.7% | 3.77 | -6.7% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
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
| Fair Under 0.5 odds | 13.31 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.05 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.58 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 49.3% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 23.8% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 52.8% |
| P home draw | 75.3% |
| P draw away | 49.9% |
| P home away | 74.9% |
| Raw p home draw | 76.2% |
| Raw p draw away | 50.7% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.91 |
| Reference draw odds | 4.05 |
| Reference away odds | 3.68 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -0.8% |
| Draw probability edge | +1.8% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -11.7% |
| Under 2.5 probability edge | +11.7% |
| Raw edge prob home | -0.0164 |
| Raw ev home | -0.0331 |
| Raw edge prob draw | 0.0362 |
| Raw ev draw | 0.1195 |
| Raw edge prob away | -0.0198 |
| Raw ev away | -0.1043 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **66.0%**. Expected goals are 2.43 for Borussia Dortmund and 1.20 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 70.8%; Under 3.5 goals: 50.5%; Double Chance 1X: 84.4%; Double Chance X2: 34.0%; Double Chance 12 (either team wins): 81.5%; Under 4.5 goals: 69.6%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 66.0% | 1.52 |
| Draw | 18.5% | 5.42 |
| Eintracht Frankfurt win | 15.6% | 6.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.43 |
| Eintracht Frankfurt expected goals | 1.20 |
| Expected total goals | 3.64 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 70.8% |
| Under 2.5 | 29.2% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 30.4% |
| Under 4.5 | 69.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.70% |
| 2 | 2-0 | 8.07% |
| 3 | 1-1 | 7.91% |
| 4 | 3-1 | 7.87% |
| 5 | 3-0 | 6.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 66.0% | 68.1% | 1.48 | -2.4% |
| Draw | 18.5% | 17.4% | 5.39 | -0.5% |
| Eintracht Frankfurt win | 15.6% | 14.5% | 6.42 | +0.0% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 81/100 |
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.16 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.75 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.43 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.29 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 63.8% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 16.7% |
| Raw p over 1 5 | 88.4% |
| Raw p under 3 5 | 50.8% |
| Raw p btts yes | 64.4% |
| P home draw | 84.4% |
| P draw away | 34.0% |
| P home away | 81.5% |
| Raw p home draw | 83.3% |
| Raw p draw away | 36.2% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.44 |
| Reference draw odds | 5.25 |
| Reference away odds | 6.25 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Home probability edge | -2.1% |
| Draw probability edge | +1.0% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.0425 |
| Raw ev home | -0.0551 |
| Raw edge prob draw | 0.0208 |
| Raw ev draw | 0.0507 |
| Raw edge prob away | 0.0217 |
| Raw ev away | 0.0698 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **53.2%**. Expected goals are 1.66 for FSV Mainz 05 and 1.14 for Werder Bremen (2.80 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.0%; Under 3.5 goals: 68.8%; Double Chance 1X: 77.3%; Double Chance X2: 46.8%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 53.2% | 1.88 |
| Draw | 24.0% | 4.16 |
| Werder Bremen win | 22.7% | 4.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.66 |
| Werder Bremen expected goals | 1.14 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.0% |
| Under 2.5 | 46.0% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.41% |
| 2 | 2-1 | 10.46% |
| 3 | 1-0 | 9.98% |
| 4 | 2-0 | 9.18% |
| 5 | 0-0 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 53.2% | 57.8% | 1.73 | -7.9% |
| Draw | 24.0% | 21.8% | 4.41 | +6.0% |
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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.4% |
| P btts no | 44.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.53 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.59 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.38 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 25.1% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 56.1% |
| P home draw | 77.3% |
| P draw away | 46.8% |
| P home away | 76.0% |
| Raw p home draw | 74.9% |
| Raw p draw away | 51.4% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.69 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -4.6% |
| Draw probability edge | +2.2% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.0920 |
| Raw ev home | -0.1587 |
| Raw edge prob draw | 0.0440 |
| Raw ev draw | 0.1566 |
| Raw edge prob away | 0.0480 |
| Raw ev away | 0.1867 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **61.9%**. Expected goals are 1.99 for RB Leipzig and 1.38 for Elversberg (3.37 combined). The most likely exact score is 2-1 at 11.4%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 67.1%; Under 3.5 goals: 55.7%; Double Chance 1X: 81.2%; Double Chance X2: 38.1%; Double Chance 12 (either team wins): 80.7%; Under 4.5 goals: 73.9%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 61.9% | 1.62 |
| Draw | 19.3% | 5.18 |
| Elversberg win | 18.8% | 5.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.99 |
| Elversberg expected goals | 1.38 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 86.2% |
| Under 1.5 | 13.8% |
| Over 2.5 | 67.1% |
| Under 2.5 | 32.9% |
| Over 3.5 | 44.3% |
| Under 3.5 | 55.7% |
| Over 4.5 | 26.1% |
| Under 4.5 | 73.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.41% |
| 2 | 1-1 | 8.48% |
| 3 | 2-0 | 8.29% |
| 4 | 3-1 | 7.58% |
| 5 | 1-0 | 7.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 61.9% | 72.8% | 1.39 | -14.0% |
| Draw | 19.3% | 15.3% | 6.09 | +17.6% |
| Elversberg win | 18.8% | 11.9% | 7.70 | +44.7% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.50 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.27 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.04 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.83 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 51.0% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 25.7% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 56.5% |
| Raw p btts yes | 65.4% |
| P home draw | 81.2% |
| P draw away | 38.1% |
| P home away | 80.7% |
| Raw p home draw | 74.3% |
| Raw p draw away | 49.0% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.35 |
| Reference draw odds | 5.90 |
| Reference away odds | 7.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Home probability edge | -10.9% |
| Draw probability edge | +4.0% |
| Away probability edge | +6.9% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | -0.2182 |
| Raw ev home | -0.2912 |
| Raw edge prob draw | 0.0799 |
| Raw ev draw | 0.4190 |
| Raw edge prob away | 0.1383 |
| Raw ev away | 0.9795 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **35.0%**. Expected goals are 0.78 for SC Paderborn and 0.89 for Hamburger SV (1.67 combined). The most likely exact score is 0-0 at 16.7%. Goal-market probabilities: at least one goal: 83.3%; Over 2.5 goals: 25.0%; Under 3.5 goals: 91.0%; Double Chance 1X: 65.7%; Double Chance X2: 65.0%; Double Chance 12 (either team wins): 69.3%; Under 4.5 goals: 97.0%; BTTS Yes (both teams score): 31.9%; BTTS No (at least one team does not score): 68.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 35.0% | 2.86 |
| Draw | 30.7% | 3.26 |
| Hamburger SV win | 34.3% | 2.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.78 |
| Hamburger SV expected goals | 0.89 |
| Expected total goals | 1.67 |
| Over 0.5 | 83.3% |
| Under 0.5 | 16.7% |
| Over 1.5 | 51.2% |
| Under 1.5 | 48.8% |
| Over 2.5 | 25.0% |
| Under 2.5 | 75.0% |
| Over 3.5 | 9.0% |
| Under 3.5 | 91.0% |
| Over 4.5 | 3.0% |
| Under 4.5 | 97.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 16.73% |
| 2 | 1-0 | 16.60% |
| 3 | 0-1 | 15.45% |
| 4 | 1-1 | 11.89% |
| 5 | 0-2 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 35.0% | 41.3% | 2.40 | -16.1% |
| Draw | 30.7% | 24.8% | 3.92 | +20.3% |
| Hamburger SV win | 34.3% | 33.9% | 2.91 | -0.1% |
| Over 2.5 | 25.0% | 60.5% | 1.64 | -59.0% |
| Under 2.5 | 75.0% | 39.5% | 2.47 | +85.3% |

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
| Market best home last update utc | 2026-10-15T06:53:15Z |
| Market best draw last update utc | 2026-10-15T06:53:15Z |
| Market best away last update utc | 2026-10-15T06:53:15Z |
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
| P btts yes | 31.9% |
| P btts no | 68.1% |
| Fair Over 0.5 odds | 1.20 |
| Fair Under 0.5 odds | 5.98 |
| Fair Over 1.5 odds | 1.95 |
| Fair Under 1.5 odds | 2.05 |
| Fair Over 2.5 odds | 4.00 |
| Fair Under 2.5 odds | 1.33 |
| Fair Over 3.5 odds | 11.08 |
| Fair Under 3.5 odds | 1.10 |
| Fair Over 4.5 odds | 33.68 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 28.6% |
| Unadjusted draw probability | 36.5% |
| Unadjusted away-win probability | 34.8% |
| Raw p over 1 5 | 50.8% |
| Raw p under 3 5 | 91.1% |
| Raw p btts yes | 33.0% |
| P home draw | 65.7% |
| P draw away | 65.0% |
| P home away | 69.3% |
| Raw p home draw | 65.2% |
| Raw p draw away | 71.4% |
| Raw p home away | 63.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.34 |
| Reference draw odds | 3.82 |
| Reference away odds | 2.83 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -6.3% |
| Draw probability edge | +5.9% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -35.5% |
| Under 2.5 probability edge | +35.5% |
| Raw edge prob home | -0.1265 |
| Raw ev home | -0.3124 |
| Raw edge prob draw | 0.1174 |
| Raw ev draw | 0.4327 |
| Raw edge prob away | 0.0091 |
| Raw ev away | 0.0127 |

</details>


---
