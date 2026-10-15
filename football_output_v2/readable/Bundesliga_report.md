# Bundesliga — football model report

Fixtures in this report: **17**.

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
| Training sha256 | 47b799f8f0667596e8ecf5ac9e081b9af99c50b3b720b48e2faa78ea69fafc96 |
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
| Live odds matched | 17.00 |
| Additional event odds calls used before this league | 16.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-16 — Eintracht Frankfurt vs 1. FC Köln

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **55.2%**. Expected goals are 2.24 for Eintracht Frankfurt and 1.24 for 1. FC Köln (3.48 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 67.2%; Under 3.5 goals: 54.5%; Double Chance 1X: 77.0%; Double Chance X2: 44.8%; Double Chance 12 (either team wins): 78.3%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 64.6%; BTTS No (at least one team does not score): 35.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 55.2% | 1.81 |
| Draw | 21.7% | 4.61 |
| 1. FC Köln win | 23.0% | 4.34 |

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
| Over 3.5 | 45.5% |
| Under 3.5 | 54.5% |
| Over 4.5 | 26.8% |
| Under 4.5 | 73.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.49% |
| 2 | 2-1 | 8.94% |
| 3 | 2-0 | 7.20% |
| 4 | 3-1 | 6.67% |
| 5 | 1-2 | 6.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 55.2% | 51.3% | 1.99 | +9.9% |
| Draw | 21.7% | 22.2% | 4.36 | -5.3% |
| 1. FC Köln win | 23.0% | 26.5% | 3.53 | -18.6% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 81/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.6% |
| P btts no | 35.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.75 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.52 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.05 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.84 |
| Fair Over 4.5 odds | 3.73 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 59.2% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 19.6% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.1% |
| Raw p btts yes | 64.3% |
| P home draw | 77.0% |
| P draw away | 44.8% |
| P home away | 78.3% |
| Raw p home draw | 80.4% |
| Raw p draw away | 40.8% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.85 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.40 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.12 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:45Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:45Z |
| Home probability edge | +3.9% |
| Draw probability edge | -0.5% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0790 |
| Raw ev home | 0.1778 |
| Raw edge prob draw | -0.0099 |
| Raw ev draw | -0.0749 |
| Raw edge prob away | -0.0690 |
| Raw ev away | -0.3083 |
| Market p home draw | 71.8% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.7% |
| Market draw away odds | 1.91 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.5% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.91 |
| Market reference dc home draw odds | 1.35 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:30:36Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.8% |
| Market under 3 5 odds | 2.00 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:30:36Z |
| Market reference under 3 5 odds | 1.84 |
| Market reference under 3 5 opposite odds | 1.83 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.6% |
| Market btts yes odds | 1.33 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.41 |
| Market reference btts yes opposite odds | 3.35 |
| Market reference btts yes last update utc | 2026-10-15T15:32:17Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **76.6%**. Expected goals are 2.86 for Bayern Munich and 1.24 for RB Leipzig (4.10 combined). The most likely exact score is 2-1 at 9.2%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 79.0%; Under 3.5 goals: 40.5%; Double Chance 1X: 89.5%; Double Chance X2: 23.4%; Double Chance 12 (either team wins): 87.1%; Under 4.5 goals: 59.6%; BTTS Yes (both teams score): 66.3%; BTTS No (at least one team does not score): 33.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 76.6% | 1.30 |
| Draw | 12.9% | 7.77 |
| RB Leipzig win | 10.5% | 9.54 |

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
| Over 2.5 | 79.0% |
| Under 2.5 | 21.0% |
| Over 3.5 | 59.5% |
| Under 3.5 | 40.5% |
| Over 4.5 | 40.4% |
| Under 4.5 | 59.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.15% |
| 2 | 3-1 | 8.73% |
| 3 | 2-0 | 7.39% |
| 4 | 3-0 | 7.05% |
| 5 | 4-1 | 6.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 76.6% | 82.9% | 1.24 | -5.0% |
| Draw | 12.9% | 9.5% | 8.05 | +3.7% |
| RB Leipzig win | 10.5% | 7.6% | 11.40 | +19.5% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Bayern Munich |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 66.3% |
| P btts no | 33.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 58.82 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.23 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.77 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.47 |
| Fair Over 4.5 odds | 2.48 |
| Fair Under 4.5 odds | 1.68 |
| Unadjusted home-win probability | 70.4% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 92.0% |
| Raw p under 3 5 | 41.4% |
| Raw p btts yes | 67.4% |
| P home draw | 89.5% |
| P draw away | 23.4% |
| P home away | 87.1% |
| Raw p home draw | 86.7% |
| Raw p draw away | 29.6% |
| Raw p home away | 83.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.17 |
| Reference draw odds | 7.20 |
| Reference away odds | 8.60 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.83 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:46Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:46Z |
| Home probability edge | -6.3% |
| Draw probability edge | +3.4% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.1252 |
| Raw ev home | -0.1273 |
| Raw edge prob draw | 0.0684 |
| Raw ev draw | 0.3120 |
| Raw edge prob away | 0.0568 |
| Raw ev away | 0.5189 |
| Market p home draw | 91.8% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 21.4% |
| Market draw away odds | 4.50 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.8% |
| Market home away odds | 1.11 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.50 |
| Market reference dc home draw odds | 1.05 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 95.8% |
| Market over 1 5 odds | 1.03 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:30:58Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 8.60 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 30.7% |
| Market under 3 5 odds | 2.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:30:58Z |
| Market reference under 3 5 odds | 2.75 |
| Market reference under 3 5 opposite odds | 1.37 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.7% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 3.10 |
| Market reference btts yes last update utc | 2026-10-15T15:32:17Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **48.8%**. Expected goals are 2.05 for Elversberg and 1.15 for Augsburg (3.20 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 61.5%; Under 3.5 goals: 61.1%; Double Chance 1X: 72.1%; Double Chance X2: 51.2%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 78.5%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 48.8% | 2.05 |
| Draw | 23.3% | 4.30 |
| Augsburg win | 27.9% | 3.58 |

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
| 1 | 1-1 | 10.68% |
| 2 | 2-1 | 8.37% |
| 3 | 1-2 | 7.72% |
| 4 | 2-0 | 7.29% |
| 5 | 1-0 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 48.8% | 40.2% | 2.55 | +24.5% |
| Draw | 23.3% | 23.9% | 3.92 | -8.8% |
| Augsburg win | 27.9% | 35.9% | 2.71 | -24.3% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Elversberg |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.99 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.94 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
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
| P home draw | 72.1% |
| P draw away | 51.2% |
| P home away | 76.7% |
| Raw p home draw | 80.1% |
| Raw p draw away | 42.6% |
| Raw p home away | 77.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.55 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:45Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:45Z |
| Home probability edge | +8.6% |
| Draw probability edge | -0.6% |
| Away probability edge | -8.0% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | 0.1722 |
| Raw ev home | 0.4643 |
| Raw edge prob draw | -0.0125 |
| Raw ev draw | -0.1122 |
| Raw edge prob away | -0.1598 |
| Raw ev away | -0.4599 |
| Market p home draw | 63.9% |
| Market home draw odds | 1.52 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.4% |
| Market draw away odds | 1.58 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.7% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.58 |
| Market reference dc home draw odds | 1.52 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 86.9% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:19Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.2% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:19Z |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.02 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.0% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 3.05 |
| Market reference btts yes last update utc | 2026-10-15T15:32:17Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **36.9%**. Expected goals are 0.95 for FC Schalke 04 and 0.92 for FSV Mainz 05 (1.87 combined). The most likely exact score is 0-1 at 15.1%. Goal-market probabilities: at least one goal: 85.6%; Over 2.5 goals: 30.0%; Under 3.5 goals: 87.9%; Double Chance 1X: 63.1%; Double Chance X2: 66.7%; Double Chance 12 (either team wins): 70.2%; Under 4.5 goals: 95.6%; BTTS Yes (both teams score): 36.9%; BTTS No (at least one team does not score): 63.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 33.3% | 3.01 |
| Draw | 29.8% | 3.35 |
| FSV Mainz 05 win | 36.9% | 2.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.95 |
| FSV Mainz 05 expected goals | 0.92 |
| Expected total goals | 1.87 |
| Over 0.5 | 85.6% |
| Under 0.5 | 14.4% |
| Over 1.5 | 57.1% |
| Under 1.5 | 42.9% |
| Over 2.5 | 30.0% |
| Under 2.5 | 70.0% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.4% |
| Under 4.5 | 95.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.12% |
| 2 | 0-0 | 14.38% |
| 3 | 1-0 | 13.40% |
| 4 | 1-1 | 12.63% |
| 5 | 0-2 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 33.3% | 32.8% | 3.16 | +5.1% |
| Draw | 29.8% | 25.2% | 3.67 | +9.4% |
| FSV Mainz 05 win | 36.9% | 42.0% | 2.34 | -13.6% |
| Over 2.5 | 30.0% | 59.8% | 1.70 | -48.9% |
| Under 2.5 | 70.0% | 40.2% | 2.34 | +63.7% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 36.9% |
| P btts no | 63.1% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.95 |
| Fair Over 1.5 odds | 1.75 |
| Fair Under 1.5 odds | 2.33 |
| Fair Over 2.5 odds | 3.33 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 8.25 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 22.94 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 34.4% |
| Unadjusted away-win probability | 31.9% |
| Raw p over 1 5 | 56.8% |
| Raw p under 3 5 | 88.1% |
| Raw p btts yes | 37.9% |
| P home draw | 63.1% |
| P draw away | 66.7% |
| P home away | 70.2% |
| Raw p home draw | 68.1% |
| Raw p draw away | 66.3% |
| Raw p home away | 65.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.75 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:18Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:18Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:16Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:16Z |
| Home probability edge | +0.4% |
| Draw probability edge | +4.6% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -29.8% |
| Under 2.5 probability edge | +29.8% |
| Raw edge prob home | 0.0084 |
| Raw ev home | 0.0642 |
| Raw edge prob draw | 0.0926 |
| Raw ev draw | 0.2638 |
| Raw edge prob away | -0.1010 |
| Raw ev away | -0.2539 |
| Market p home draw | 58.1% |
| Market home draw odds | 1.67 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.9% |
| Market draw away odds | 1.41 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.0% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home draw odds | 1.67 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:30:36Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:30:36Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.3% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.59 |
| Market reference btts yes opposite odds | 2.60 |
| Market reference btts yes last update utc | 2026-10-15T15:32:17Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **54.3%**. Expected goals are 1.17 for Hamburger SV and 2.00 for VfB Stuttgart (3.17 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.6%; Under 3.5 goals: 61.0%; Double Chance 1X: 45.7%; Double Chance X2: 77.0%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 78.5%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 23.0% | 4.34 |
| Draw | 22.7% | 4.41 |
| VfB Stuttgart win | 54.3% | 1.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.17 |
| VfB Stuttgart expected goals | 2.00 |
| Expected total goals | 3.17 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 61.6% |
| Under 2.5 | 38.4% |
| Over 3.5 | 39.0% |
| Under 3.5 | 61.0% |
| Over 4.5 | 21.5% |
| Under 4.5 | 78.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.41% |
| 2 | 1-2 | 9.56% |
| 3 | 0-2 | 8.17% |
| 4 | 0-1 | 7.35% |
| 5 | 1-3 | 6.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 23.0% | 25.0% | 4.08 | -6.1% |
| Draw | 22.7% | 22.2% | 4.08 | -7.6% |
| VfB Stuttgart win | 54.3% | 52.8% | 1.90 | +3.2% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Hamburg |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 88/100 |
| Away-name matching confidence | 95/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.39 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.98 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.66 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 55.8% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 60.5% |
| P home draw | 45.7% |
| P draw away | 77.0% |
| P home away | 77.3% |
| Raw p home draw | 44.2% |
| Raw p draw away | 79.0% |
| Raw p home away | 76.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:45Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:45Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.5% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -7.9% |
| Under 2.5 probability edge | +7.9% |
| Raw edge prob home | -0.0396 |
| Raw ev home | -0.1418 |
| Raw edge prob draw | 0.0096 |
| Raw ev draw | -0.0561 |
| Raw edge prob away | 0.0300 |
| Raw ev away | 0.0608 |
| Market p home draw | 48.5% |
| Market home draw odds | 2.00 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.8% |
| Market draw away odds | 1.28 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.28 |
| Market reference dc home draw odds | 2.00 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 88.5% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:21Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.5% |
| Market under 3 5 odds | 1.96 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:21Z |
| Market reference under 3 5 odds | 1.76 |
| Market reference under 3 5 opposite odds | 1.92 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.35 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 3.10 |
| Market reference btts yes last update utc | 2026-10-15T15:32:17Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **61.3%**. Expected goals are 0.94 for Union Berlin and 1.94 for Borussia Dortmund (2.88 combined). The most likely exact score is 0-2 at 10.8%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 55.5%; Under 3.5 goals: 67.2%; Double Chance 1X: 38.7%; Double Chance X2: 83.1%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 52.6%; BTTS No (at least one team does not score): 47.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 16.9% | 5.91 |
| Draw | 21.8% | 4.60 |
| Borussia Dortmund win | 61.3% | 1.63 |

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
| Over 2.5 | 55.5% |
| Under 2.5 | 44.5% |
| Over 3.5 | 32.8% |
| Under 3.5 | 67.2% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 10.82% |
| 2 | 1-1 | 10.36% |
| 3 | 0-1 | 10.28% |
| 4 | 1-2 | 10.16% |
| 5 | 0-3 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 16.9% | 17.0% | 5.34 | -9.6% |
| Draw | 21.8% | 20.2% | 4.62 | +0.5% |
| Borussia Dortmund win | 61.3% | 62.7% | 1.63 | -0.0% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Union Berlin |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 52.6% |
| P btts no | 47.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.53 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 3.05 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.97 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 16.8% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 59.9% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 53.0% |
| P home draw | 38.7% |
| P draw away | 83.1% |
| P home away | 78.2% |
| Raw p home draw | 40.1% |
| Raw p draw away | 83.2% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 4.90 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.52 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:46Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:46Z |
| Home probability edge | -0.1% |
| Draw probability edge | +1.5% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.0024 |
| Raw ev home | -0.1028 |
| Raw edge prob draw | 0.0306 |
| Raw ev draw | 0.0760 |
| Raw edge prob away | -0.0283 |
| Raw ev away | -0.0235 |
| Market p home draw | 40.1% |
| Market home draw odds | 2.42 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.6% |
| Market draw away odds | 1.19 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.3% |
| Market home away odds | 1.24 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.19 |
| Market reference dc home draw odds | 2.42 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 89.2% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:32:26Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-10-15T15:32:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.5% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:32:26Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.31 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.9% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.52 |
| Market reference btts yes last update utc | 2026-10-15T15:32:17Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **53.0%**. Expected goals are 1.24 for Werder Bremen and 0.61 for SC Paderborn (1.85 combined). The most likely exact score is 1-0 at 19.4%. Goal-market probabilities: at least one goal: 85.8%; Over 2.5 goals: 29.6%; Under 3.5 goals: 88.1%; Double Chance 1X: 80.2%; Double Chance X2: 47.0%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 95.8%; BTTS Yes (both teams score): 32.3%; BTTS No (at least one team does not score): 67.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 53.0% | 1.89 |
| Draw | 27.2% | 3.67 |
| SC Paderborn win | 19.8% | 5.06 |

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
| Over 3.5 | 11.9% |
| Under 3.5 | 88.1% |
| Over 4.5 | 4.2% |
| Under 4.5 | 95.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.36% |
| 2 | 0-0 | 14.24% |
| 3 | 2-0 | 12.68% |
| 4 | 1-1 | 10.92% |
| 5 | 0-1 | 9.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 53.0% | 55.1% | 1.84 | -2.5% |
| Draw | 27.2% | 22.4% | 4.26 | +16.0% |
| SC Paderborn win | 19.8% | 22.4% | 4.21 | -16.8% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 32.3% |
| P btts no | 67.7% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 7.02 |
| Fair Over 1.5 odds | 1.77 |
| Fair Under 1.5 odds | 2.30 |
| Fair Over 2.5 odds | 3.38 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.43 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 23.74 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 50.9% |
| Unadjusted draw probability | 32.0% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 56.1% |
| Raw p under 3 5 | 88.3% |
| Raw p btts yes | 33.3% |
| P home draw | 80.2% |
| P draw away | 47.0% |
| P home away | 72.8% |
| Raw p home draw | 82.9% |
| Raw p draw away | 49.1% |
| Raw p home away | 68.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.72 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.56 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:45Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:45Z |
| Home probability edge | -2.1% |
| Draw probability edge | +4.8% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | -34.1% |
| Under 2.5 probability edge | +34.1% |
| Raw edge prob home | -0.0422 |
| Raw ev home | -0.0634 |
| Raw edge prob draw | 0.0957 |
| Raw ev draw | 0.3635 |
| Raw edge prob away | -0.0535 |
| Raw ev away | -0.2806 |
| Market p home draw | 76.3% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.8% |
| Market draw away odds | 2.07 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.9% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.07 |
| Market reference dc home draw odds | 1.27 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 84.4% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:42Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.7% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:42Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.21 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.9% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.51 |
| Market reference btts yes opposite odds | 2.42 |
| Market reference btts yes last update utc | 2026-10-15T15:32:16Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **62.1%**. Expected goals are 2.40 for Bayer Leverkusen and 1.08 for SC Freiburg (3.48 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 66.9%; Under 3.5 goals: 54.7%; Double Chance 1X: 82.3%; Double Chance X2: 37.9%; Double Chance 12 (either team wins): 79.8%; Under 4.5 goals: 73.4%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 62.1% | 1.61 |
| Draw | 20.2% | 4.94 |
| SC Freiburg win | 17.7% | 5.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.40 |
| SC Freiburg expected goals | 1.08 |
| Expected total goals | 3.48 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 86.5% |
| Under 1.5 | 13.5% |
| Over 2.5 | 66.9% |
| Under 2.5 | 33.1% |
| Over 3.5 | 45.3% |
| Under 3.5 | 54.7% |
| Over 4.5 | 26.6% |
| Under 4.5 | 73.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.07% |
| 2 | 2-1 | 9.03% |
| 3 | 2-0 | 8.38% |
| 4 | 3-1 | 7.22% |
| 5 | 3-0 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 62.1% | 58.3% | 1.75 | +8.7% |
| Draw | 20.2% | 21.2% | 4.42 | -10.5% |
| SC Freiburg win | 17.7% | 20.6% | 4.62 | -18.4% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Leverkusen |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.38 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.42 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.02 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.77 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 65.9% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 14.7% |
| Raw p over 1 5 | 86.8% |
| Raw p under 3 5 | 54.2% |
| Raw p btts yes | 60.6% |
| P home draw | 82.3% |
| P draw away | 37.9% |
| P home away | 79.8% |
| Raw p home draw | 85.3% |
| Raw p draw away | 34.1% |
| Raw p home away | 80.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.62 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.69 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:46Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:46Z |
| Home probability edge | +3.8% |
| Draw probability edge | -0.9% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | +1.4% |
| Under 2.5 probability edge | -1.4% |
| Raw edge prob home | 0.0770 |
| Raw ev home | 0.1541 |
| Raw edge prob draw | -0.0184 |
| Raw ev draw | -0.1458 |
| Raw edge prob away | -0.0586 |
| Raw ev away | -0.3196 |
| Market p home draw | 78.3% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.0% |
| Market draw away odds | 2.21 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.7% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.21 |
| Market reference dc home draw odds | 1.24 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 85.9% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:42Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.5% |
| Market under 3 5 odds | 1.74 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:42Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.11 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.9% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.62 |
| Market reference btts yes last update utc | 2026-10-15T15:32:17Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **42.2%**. Expected goals are 1.87 for Borussia Monchengladbach and 1.78 for TSG Hoffenheim (3.65 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.5%; Double Chance 1X: 57.8%; Double Chance X2: 65.1%; Double Chance 12 (either team wins): 77.0%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 71.0%; BTTS No (at least one team does not score): 29.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 34.9% | 2.87 |
| Draw | 23.0% | 4.35 |
| TSG Hoffenheim win | 42.2% | 2.37 |

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
| 1 | 1-1 | 9.29% |
| 2 | 1-2 | 8.87% |
| 3 | 2-2 | 7.13% |
| 4 | 2-1 | 7.02% |
| 5 | 1-3 | 5.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 34.9% | 29.6% | 3.33 | +16.1% |
| Draw | 23.0% | 22.8% | 4.21 | -3.3% |
| TSG Hoffenheim win | 42.2% | 47.7% | 2.10 | -11.5% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | M'gladbach |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 71.0% |
| P btts no | 29.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.33 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.79 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.41 |
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
| P home draw | 57.8% |
| P draw away | 65.1% |
| P home away | 77.0% |
| Raw p home draw | 63.4% |
| Raw p draw away | 59.8% |
| Raw p home away | 76.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.95 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.07 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:46Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:46Z |
| Home probability edge | +5.3% |
| Draw probability edge | +0.2% |
| Away probability edge | -5.5% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.1059 |
| Raw ev home | 0.3373 |
| Raw edge prob draw | 0.0046 |
| Raw ev draw | -0.0230 |
| Raw edge prob away | -0.1104 |
| Raw ev away | -0.2307 |
| Market p home draw | 53.3% |
| Market home draw odds | 1.82 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.3% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.4% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home draw odds | 1.82 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 88.5% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:30:38Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.8% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:30:38Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.7% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 3.10 |
| Market reference btts yes last update utc | 2026-10-15T15:32:17Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **69.0%**. Expected goals are 2.52 for VfB Stuttgart and 1.17 for Borussia Monchengladbach (3.69 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 72.1%; Under 3.5 goals: 49.1%; Double Chance 1X: 85.7%; Double Chance X2: 31.0%; Double Chance 12 (either team wins): 83.3%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 63.5%; BTTS No (at least one team does not score): 36.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 69.0% | 1.45 |
| Draw | 16.7% | 5.97 |
| Borussia Monchengladbach win | 14.3% | 6.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.52 |
| Borussia Monchengladbach expected goals | 1.17 |
| Expected total goals | 3.69 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 89.2% |
| Under 1.5 | 10.8% |
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 50.9% |
| Under 3.5 | 49.1% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.68% |
| 2 | 2-0 | 8.26% |
| 3 | 3-1 | 8.13% |
| 4 | 1-1 | 7.15% |
| 5 | 3-0 | 6.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 69.0% | 71.9% | 1.43 | -1.4% |
| Draw | 16.7% | 14.8% | 5.80 | -2.9% |
| Borussia Monchengladbach win | 14.3% | 13.3% | 6.98 | -0.2% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 63.5% |
| P btts no | 36.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.89 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.22 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.59 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 66.0% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 15.3% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 49.6% |
| Raw p btts yes | 64.1% |
| P home draw | 85.7% |
| P draw away | 31.0% |
| P home away | 83.3% |
| Raw p home draw | 84.7% |
| Raw p draw away | 34.0% |
| Raw p home away | 81.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.33 |
| Reference draw odds | 5.20 |
| Reference away odds | 5.70 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.76 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:46Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:46Z |
| Home probability edge | -2.9% |
| Draw probability edge | +1.9% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.0582 |
| Raw ev home | -0.0555 |
| Raw edge prob draw | 0.0386 |
| Raw ev draw | 0.0832 |
| Raw edge prob away | 0.0196 |
| Raw ev away | 0.0662 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **41.1%**. Expected goals are 0.97 for 1. FC Köln and 0.96 for FC Schalke 04 (1.93 combined). The most likely exact score is 1-0 at 15.9%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 32.1%; Under 3.5 goals: 86.7%; Double Chance 1X: 69.6%; Double Chance X2: 58.9%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 95.0%; BTTS Yes (both teams score): 38.3%; BTTS No (at least one team does not score): 61.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 41.1% | 2.43 |
| Draw | 28.4% | 3.52 |
| FC Schalke 04 win | 30.4% | 3.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 0.97 |
| FC Schalke 04 expected goals | 0.96 |
| Expected total goals | 1.93 |
| Over 0.5 | 86.8% |
| Under 0.5 | 13.2% |
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
| 1 | 1-0 | 15.93% |
| 2 | 0-0 | 13.17% |
| 3 | 1-1 | 12.33% |
| 4 | 0-1 | 11.87% |
| 5 | 2-0 | 8.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 41.1% | 48.7% | 2.12 | -12.8% |
| Draw | 28.4% | 23.1% | 3.98 | +13.2% |
| FC Schalke 04 win | 30.4% | 28.2% | 3.43 | +4.3% |
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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 38.3% |
| P btts no | 61.7% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.59 |
| Fair Over 1.5 odds | 1.69 |
| Fair Under 1.5 odds | 2.44 |
| Fair Over 2.5 odds | 3.12 |
| Fair Under 2.5 odds | 1.47 |
| Fair Over 3.5 odds | 7.53 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.18 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 33.8% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 86.9% |
| Raw p btts yes | 39.5% |
| P home draw | 69.6% |
| P draw away | 58.9% |
| P home away | 71.6% |
| Raw p home draw | 67.3% |
| Raw p draw away | 66.4% |
| Raw p home away | 66.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.90 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:16Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:16Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:16Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:16Z |
| Home probability edge | -7.6% |
| Draw probability edge | +5.3% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -28.2% |
| Under 2.5 probability edge | +28.2% |
| Raw edge prob home | -0.1517 |
| Raw ev home | -0.2886 |
| Raw edge prob draw | 0.1069 |
| Raw ev draw | 0.3448 |
| Raw edge prob away | 0.0449 |
| Raw ev away | 0.1200 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **50.9%**. Expected goals are 1.60 for Augsburg and 1.05 for Union Berlin (2.65 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 50.1%; Under 3.5 goals: 72.3%; Double Chance 1X: 75.8%; Double Chance X2: 49.1%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 52.4%; BTTS No (at least one team does not score): 47.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 50.9% | 1.97 |
| Draw | 25.0% | 4.00 |
| Union Berlin win | 24.2% | 4.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.60 |
| Union Berlin expected goals | 1.05 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.1% |
| Under 2.5 | 49.9% |
| Over 3.5 | 27.7% |
| Under 3.5 | 72.3% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.93% |
| 2 | 1-0 | 10.65% |
| 3 | 2-1 | 9.80% |
| 4 | 2-0 | 9.37% |
| 5 | 0-0 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 50.9% | 52.4% | 1.96 | -0.3% |
| Draw | 25.0% | 23.1% | 4.16 | +3.9% |
| Union Berlin win | 24.2% | 24.5% | 3.77 | -8.9% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.4% |
| P btts no | 47.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.37 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.56 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 49.3% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 23.8% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 52.8% |
| P home draw | 75.8% |
| P draw away | 49.1% |
| P home away | 75.0% |
| Raw p home draw | 76.2% |
| Raw p draw away | 50.7% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.78 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.50 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:46Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:46Z |
| Home probability edge | -1.5% |
| Draw probability edge | +1.9% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -12.2% |
| Under 2.5 probability edge | +12.2% |
| Raw edge prob home | -0.0306 |
| Raw ev home | -0.0331 |
| Raw edge prob draw | 0.0385 |
| Raw ev draw | 0.1195 |
| Raw edge prob away | -0.0079 |
| Raw ev away | -0.1043 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **66.0%**. Expected goals are 2.43 for Borussia Dortmund and 1.20 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 70.9%; Under 3.5 goals: 50.5%; Double Chance 1X: 84.1%; Double Chance X2: 34.0%; Double Chance 12 (either team wins): 81.9%; Under 4.5 goals: 69.6%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 66.0% | 1.52 |
| Draw | 18.1% | 5.53 |
| Eintracht Frankfurt win | 15.9% | 6.27 |

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
| Over 2.5 | 70.9% |
| Under 2.5 | 29.1% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 30.4% |
| Under 4.5 | 69.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.70% |
| 2 | 2-0 | 8.07% |
| 3 | 3-1 | 7.87% |
| 4 | 1-1 | 7.76% |
| 5 | 3-0 | 6.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 66.0% | 68.1% | 1.48 | -2.4% |
| Draw | 18.1% | 16.7% | 5.39 | -2.5% |
| Eintracht Frankfurt win | 15.9% | 15.2% | 6.42 | +2.3% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 81/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.0% |
| P btts no | 36.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.82 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.76 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.44 |
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
| P home draw | 84.1% |
| P draw away | 34.0% |
| P home away | 81.9% |
| Raw p home draw | 83.3% |
| Raw p draw away | 36.2% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.40 |
| Reference draw odds | 4.80 |
| Reference away odds | 5.20 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.31 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:46Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:46Z |
| Home probability edge | -2.1% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | -0.0426 |
| Raw ev home | -0.0551 |
| Raw edge prob draw | 0.0281 |
| Raw ev draw | 0.0507 |
| Raw edge prob away | 0.0144 |
| Raw ev away | 0.0697 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **53.8%**. Expected goals are 1.66 for FSV Mainz 05 and 1.14 for Werder Bremen (2.80 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.1%; Under 3.5 goals: 68.7%; Double Chance 1X: 77.6%; Double Chance X2: 46.2%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 53.8% | 1.86 |
| Draw | 23.8% | 4.21 |
| Werder Bremen win | 22.4% | 4.47 |

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
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.29% |
| 2 | 2-1 | 10.58% |
| 3 | 1-0 | 10.10% |
| 4 | 2-0 | 9.29% |
| 5 | 0-0 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 53.8% | 59.1% | 1.73 | -6.8% |
| Draw | 23.8% | 21.3% | 4.41 | +4.9% |
| Werder Bremen win | 22.4% | 19.6% | 4.72 | +5.6% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.4% |
| P btts no | 44.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.69 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.59 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.36 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 25.1% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 56.1% |
| P home draw | 77.6% |
| P draw away | 46.2% |
| P home away | 76.2% |
| Raw p home draw | 74.9% |
| Raw p draw away | 51.4% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.59 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.20 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:46Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:46Z |
| Home probability edge | -5.2% |
| Draw probability edge | +2.4% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -9.1% |
| Under 2.5 probability edge | +9.1% |
| Raw edge prob home | -0.1044 |
| Raw ev home | -0.1587 |
| Raw edge prob draw | 0.0490 |
| Raw ev draw | 0.1566 |
| Raw edge prob away | 0.0554 |
| Raw ev away | 0.1867 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **63.2%**. Expected goals are 1.99 for RB Leipzig and 1.38 for Elversberg (3.37 combined). The most likely exact score is 2-1 at 11.7%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 67.4%; Under 3.5 goals: 55.6%; Double Chance 1X: 81.6%; Double Chance X2: 36.8%; Double Chance 12 (either team wins): 81.6%; Under 4.5 goals: 73.7%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 63.2% | 1.58 |
| Draw | 18.4% | 5.44 |
| Elversberg win | 18.4% | 5.44 |

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
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 44.4% |
| Under 3.5 | 55.6% |
| Over 4.5 | 26.3% |
| Under 4.5 | 73.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.66% |
| 2 | 2-0 | 8.46% |
| 3 | 1-1 | 8.07% |
| 4 | 3-1 | 7.74% |
| 5 | 1-0 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 63.2% | 75.5% | 1.39 | -12.1% |
| Draw | 18.4% | 13.5% | 6.09 | +11.9% |
| Elversberg win | 18.4% | 11.1% | 7.70 | +41.5% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.9% |
| P btts no | 36.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.94 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.31 |
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
| P home draw | 81.6% |
| P draw away | 36.8% |
| P home away | 81.6% |
| Raw p home draw | 74.3% |
| Raw p draw away | 49.0% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.27 |
| Reference draw odds | 5.50 |
| Reference away odds | 6.50 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.82 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:46Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:46Z |
| Home probability edge | -12.2% |
| Draw probability edge | +4.9% |
| Away probability edge | +7.3% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | -0.2449 |
| Raw ev home | -0.2912 |
| Raw edge prob draw | 0.0984 |
| Raw ev draw | 0.4190 |
| Raw edge prob away | 0.1465 |
| Raw ev away | 0.9795 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **35.1%**. Expected goals are 0.78 for SC Paderborn and 0.89 for Hamburger SV (1.67 combined). The most likely exact score is 0-0 at 16.7%. Goal-market probabilities: at least one goal: 83.3%; Over 2.5 goals: 25.0%; Under 3.5 goals: 91.0%; Double Chance 1X: 65.7%; Double Chance X2: 64.9%; Double Chance 12 (either team wins): 69.4%; Under 4.5 goals: 97.0%; BTTS Yes (both teams score): 31.9%; BTTS No (at least one team does not score): 68.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 35.1% | 2.85 |
| Draw | 30.6% | 3.26 |
| Hamburger SV win | 34.3% | 2.92 |

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
| 1 | 0-0 | 16.72% |
| 2 | 1-0 | 16.65% |
| 3 | 0-1 | 15.42% |
| 4 | 1-1 | 11.88% |
| 5 | 0-2 | 7.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 35.1% | 41.5% | 2.40 | -15.8% |
| Draw | 30.6% | 24.7% | 3.92 | +20.1% |
| Hamburger SV win | 34.3% | 33.7% | 2.91 | -0.3% |
| Over 2.5 | 25.0% | 61.5% | 1.64 | -59.0% |
| Under 2.5 | 75.0% | 38.5% | 2.47 | +85.3% |

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
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
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
| Fair Over 4.5 odds | 33.67 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 28.6% |
| Unadjusted draw probability | 36.5% |
| Unadjusted away-win probability | 34.8% |
| Raw p over 1 5 | 50.8% |
| Raw p under 3 5 | 91.1% |
| Raw p btts yes | 33.0% |
| P home draw | 65.7% |
| P draw away | 64.9% |
| P home away | 69.4% |
| Raw p home draw | 65.2% |
| Raw p draw away | 71.4% |
| Raw p home away | 63.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.65 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:18Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:18Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:16Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:16Z |
| Home probability edge | -6.4% |
| Draw probability edge | +5.9% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -36.6% |
| Under 2.5 probability edge | +36.6% |
| Raw edge prob home | -0.1287 |
| Raw ev home | -0.3124 |
| Raw edge prob draw | 0.1181 |
| Raw ev draw | 0.4327 |
| Raw edge prob away | 0.0106 |
| Raw ev away | 0.0127 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **47.6%**. Expected goals are 1.49 for TSG Hoffenheim and 2.29 for Bayer Leverkusen (3.78 combined). The most likely exact score is 1-1 at 8.8%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 72.2%; Under 3.5 goals: 48.4%; Double Chance 1X: 52.4%; Double Chance X2: 69.8%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 67.8%; BTTS Yes (both teams score): 70.8%; BTTS No (at least one team does not score): 29.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 30.2% | 3.31 |
| Draw | 22.1% | 4.52 |
| Bayer Leverkusen win | 47.6% | 2.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.49 |
| Bayer Leverkusen expected goals | 2.29 |
| Expected total goals | 3.78 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 89.5% |
| Under 1.5 | 10.5% |
| Over 2.5 | 72.2% |
| Under 2.5 | 27.8% |
| Over 3.5 | 51.6% |
| Under 3.5 | 48.4% |
| Over 4.5 | 32.2% |
| Under 4.5 | 67.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.84% |
| 2 | 1-2 | 7.74% |
| 3 | 2-1 | 7.35% |
| 4 | 2-2 | 6.94% |
| 5 | 1-3 | 5.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 30.2% | 36.6% | 2.76 | -16.5% |
| Draw | 22.1% | 23.1% | 4.25 | -6.0% |
| Bayer Leverkusen win | 47.6% | 40.3% | 2.39 | +13.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:30:00+00:00 |
| Fixture id | 2fd479cbb110c8f057e363bb06195f2b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T15:32:16Z |
| Market best draw last update utc | 2026-10-15T15:32:16Z |
| Market best away last update utc | 2026-10-15T15:32:16Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Hoffenheim |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 70.8% |
| P btts no | 29.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.47 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.48 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.60 |
| Fair Over 3.5 odds | 1.94 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.10 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 23.9% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 55.0% |
| Raw p over 1 5 | 89.7% |
| Raw p under 3 5 | 47.8% |
| Raw p btts yes | 70.2% |
| P home draw | 52.4% |
| P draw away | 69.8% |
| P home away | 77.9% |
| Raw p home draw | 45.0% |
| Raw p draw away | 76.1% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.45 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:18Z |
| Market reference home last update utc | 2026-10-15T15:32:18Z |
| Market reference draw last update utc | 2026-10-15T15:32:18Z |
| Market reference away last update utc | 2026-10-15T15:32:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.05 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:46Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:46Z |
| Home probability edge | -6.4% |
| Draw probability edge | -1.0% |
| Away probability edge | +7.3% |
| Over 2.5 probability edge | +2.2% |
| Under 2.5 probability edge | -2.2% |
| Raw edge prob home | -0.1276 |
| Raw ev home | -0.3412 |
| Raw edge prob draw | -0.0191 |
| Raw ev draw | -0.1006 |
| Raw edge prob away | 0.1467 |
| Raw ev away | 0.3138 |

</details>


---
