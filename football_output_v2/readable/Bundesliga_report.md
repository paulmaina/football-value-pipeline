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

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **54.6%**. Expected goals are 2.24 for Eintracht Frankfurt and 1.24 for 1. FC Köln (3.48 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 67.3%; Under 3.5 goals: 54.6%; Double Chance 1X: 76.1%; Double Chance X2: 45.4%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 54.6% | 1.83 |
| Draw | 21.5% | 4.65 |
| 1. FC Köln win | 23.9% | 4.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 2.24 |
| 1. FC Köln expected goals | 1.24 |
| Expected total goals | 3.48 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 67.3% |
| Under 2.5 | 32.7% |
| Over 3.5 | 45.4% |
| Under 3.5 | 54.6% |
| Over 4.5 | 26.8% |
| Under 4.5 | 73.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.39% |
| 2 | 2-1 | 8.83% |
| 3 | 2-0 | 7.11% |
| 4 | 3-1 | 6.59% |
| 5 | 1-2 | 6.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 54.6% | 49.9% | 1.99 | +8.6% |
| Draw | 21.5% | 21.8% | 4.36 | -6.3% |
| 1. FC Köln win | 23.9% | 28.3% | 3.52 | -15.7% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 26.02 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.51 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.06 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.73 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 59.2% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 19.6% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.1% |
| Raw p btts yes | 64.3% |
| P home draw | 76.1% |
| P draw away | 45.4% |
| Raw p home draw | 80.4% |
| Raw p draw away | 40.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.88 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.26 |
| Home probability edge | +4.6% |
| Draw probability edge | -0.3% |
| Away probability edge | -4.4% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | 0.0925 |
| Raw ev home | 0.1778 |
| Raw edge prob draw | -0.0054 |
| Raw ev draw | -0.0749 |
| Raw edge prob away | -0.0871 |
| Raw ev away | -0.3103 |
| Market p home draw | 72.4% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T21:06:59Z |
| Market reference home draw last update utc | 2026-10-14T21:07:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.3% |
| Market draw away odds | 1.91 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T21:06:59Z |
| Market reference draw away last update utc | 2026-10-14T21:07:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.80 |
| Market reference dc home draw odds | 1.30 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 88.7% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T21:05:58Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.70 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.6% |
| Market under 3 5 odds | 2.00 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T21:05:58Z |
| Market reference under 3 5 odds | 1.92 |
| Market reference under 3 5 opposite odds | 1.89 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 72.5% |
| Market btts yes odds | 1.33 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T21:06:59Z |
| Market reference btts yes odds | 1.35 |
| Market reference btts yes opposite odds | 3.33 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **75.9%**. Expected goals are 2.86 for Bayern Munich and 1.24 for RB Leipzig (4.10 combined). The most likely exact score is 2-1 at 9.1%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 78.9%; Under 3.5 goals: 40.6%; Double Chance 1X: 89.0%; Double Chance X2: 24.1%; Under 4.5 goals: 59.8%; BTTS Yes (both teams score): 66.4%; BTTS No (at least one team does not score): 33.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 75.9% | 1.32 |
| Draw | 13.0% | 7.67 |
| RB Leipzig win | 11.0% | 9.08 |

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
| Over 3.5 | 59.4% |
| Under 3.5 | 40.6% |
| Over 4.5 | 40.2% |
| Under 4.5 | 59.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.07% |
| 2 | 3-1 | 8.65% |
| 3 | 2-0 | 7.33% |
| 4 | 3-0 | 6.99% |
| 5 | 4-1 | 6.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 75.9% | 81.5% | 1.26 | -4.3% |
| Draw | 13.0% | 9.8% | 7.36 | -4.1% |
| RB Leipzig win | 11.0% | 8.7% | 11.30 | +24.5% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 58.10 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.16 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.75 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.46 |
| Fair Over 4.5 odds | 2.49 |
| Fair Under 4.5 odds | 1.67 |
| Unadjusted home-win probability | 70.4% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 92.0% |
| Raw p under 3 5 | 41.4% |
| Raw p btts yes | 67.4% |
| P home draw | 89.0% |
| P draw away | 24.1% |
| Raw p home draw | 86.7% |
| Raw p draw away | 29.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.19 |
| Reference draw odds | 7.25 |
| Reference away odds | 8.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.83 |
| Home probability edge | -5.6% |
| Draw probability edge | +3.3% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.1115 |
| Raw ev home | -0.1133 |
| Raw edge prob draw | 0.0653 |
| Raw ev draw | 0.1997 |
| Raw edge prob away | 0.0462 |
| Raw ev away | 0.5059 |
| Market p home draw | 89.6% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T21:06:59Z |
| Market reference home draw last update utc | 2026-10-14T21:07:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.5% |
| Market draw away odds | 4.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T21:06:59Z |
| Market reference draw away last update utc | 2026-10-14T21:07:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.22 |
| Market reference dc home draw odds | 1.06 |
| Market reference dc home away odds | 1.08 |
| Market p over 1 5 | 95.8% |
| Market over 1 5 odds | 1.03 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T21:06:08Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 8.60 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 30.7% |
| Market under 3 5 odds | 2.76 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T21:06:08Z |
| Market reference under 3 5 odds | 2.75 |
| Market reference under 3 5 opposite odds | 1.37 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.38 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T21:06:59Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 3.15 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **48.7%**. Expected goals are 2.05 for Elversberg and 1.15 for Augsburg (3.20 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.5%; Under 3.5 goals: 61.1%; Double Chance 1X: 71.8%; Double Chance X2: 51.3%; Under 4.5 goals: 78.5%; BTTS Yes (both teams score): 61.0%; BTTS No (at least one team does not score): 39.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 48.7% | 2.05 |
| Draw | 23.0% | 4.34 |
| Augsburg win | 28.2% | 3.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.05 |
| Augsburg expected goals | 1.15 |
| Expected total goals | 3.20 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
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
| 1 | 1-1 | 10.57% |
| 2 | 2-1 | 8.36% |
| 3 | 1-2 | 7.81% |
| 4 | 2-0 | 7.28% |
| 5 | 1-0 | 6.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 48.7% | 40.0% | 2.55 | +24.3% |
| Draw | 23.0% | 23.4% | 3.92 | -9.7% |
| Augsburg win | 28.2% | 36.5% | 2.71 | -23.5% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Elversberg |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.0% |
| P btts no | 39.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.20 |
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
| P home draw | 71.8% |
| P draw away | 51.3% |
| Raw p home draw | 80.1% |
| Raw p draw away | 42.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Home probability edge | +8.7% |
| Draw probability edge | -0.4% |
| Away probability edge | -8.3% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | 0.1737 |
| Raw ev home | 0.4643 |
| Raw edge prob draw | -0.0076 |
| Raw ev draw | -0.1122 |
| Raw edge prob away | -0.1661 |
| Raw ev away | -0.4599 |
| Market p home draw | 63.3% |
| Market home draw odds | 1.52 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T21:06:59Z |
| Market reference home draw last update utc | 2026-10-14T21:07:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.3% |
| Market draw away odds | 1.58 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T21:06:59Z |
| Market reference draw away last update utc | 2026-10-14T21:07:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.55 |
| Market reference dc home draw odds | 1.50 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 86.9% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T21:06:25Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.2% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T21:06:25Z |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.02 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.7% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T21:06:59Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 3.05 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **37.5%**. Expected goals are 0.95 for FC Schalke 04 and 0.92 for FSV Mainz 05 (1.87 combined). The most likely exact score is 0-1 at 15.4%. Goal-market probabilities: at least one goal: 85.8%; Over 2.5 goals: 30.1%; Under 3.5 goals: 87.9%; Double Chance 1X: 62.5%; Double Chance X2: 67.0%; Under 4.5 goals: 95.6%; BTTS Yes (both teams score): 36.9%; BTTS No (at least one team does not score): 63.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 33.0% | 3.03 |
| Draw | 29.5% | 3.39 |
| FSV Mainz 05 win | 37.5% | 2.66 |

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
| 1 | 0-1 | 15.36% |
| 2 | 0-0 | 14.22% |
| 3 | 1-0 | 13.29% |
| 4 | 1-1 | 12.49% |
| 5 | 0-2 | 7.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 33.0% | 32.3% | 3.16 | +4.3% |
| Draw | 29.5% | 24.5% | 3.67 | +8.2% |
| FSV Mainz 05 win | 37.5% | 43.2% | 2.34 | -12.2% |
| Over 2.5 | 30.1% | 59.3% | 1.70 | -48.8% |
| Under 2.5 | 69.9% | 40.7% | 2.34 | +63.5% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 7.03 |
| Fair Over 1.5 odds | 1.75 |
| Fair Under 1.5 odds | 2.33 |
| Fair Over 2.5 odds | 3.32 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 8.25 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 22.85 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 34.4% |
| Unadjusted away-win probability | 31.9% |
| Raw p over 1 5 | 56.8% |
| Raw p under 3 5 | 88.1% |
| Raw p btts yes | 37.9% |
| P home draw | 62.5% |
| P draw away | 67.0% |
| Raw p home draw | 68.1% |
| Raw p draw away | 66.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | +0.7% |
| Draw probability edge | +5.0% |
| Away probability edge | -5.6% |
| Over 2.5 probability edge | -29.2% |
| Under 2.5 probability edge | +29.2% |
| Raw edge prob home | 0.0137 |
| Raw ev home | 0.0642 |
| Raw edge prob draw | 0.0992 |
| Raw ev draw | 0.2638 |
| Raw edge prob away | -0.1129 |
| Raw ev away | -0.2539 |
| Market p home draw | 58.3% |
| Market home draw odds | 1.67 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T21:06:59Z |
| Market reference home draw last update utc | 2026-10-14T21:07:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.9% |
| Market draw away odds | 1.41 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T21:06:59Z |
| Market reference draw away last update utc | 2026-10-14T21:07:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home draw odds | 1.63 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T21:06:26Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T21:06:26Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.7% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T21:06:59Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.60 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **55.0%**. Expected goals are 1.17 for Hamburger SV and 2.00 for VfB Stuttgart (3.17 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.9%; Double Chance 1X: 45.0%; Double Chance X2: 77.4%; Under 4.5 goals: 78.4%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 22.6% | 4.42 |
| Draw | 22.4% | 4.47 |
| VfB Stuttgart win | 55.0% | 1.82 |

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
| Over 4.5 | 21.6% |
| Under 4.5 | 78.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.28% |
| 2 | 1-2 | 9.68% |
| 3 | 0-2 | 8.27% |
| 4 | 0-1 | 7.45% |
| 5 | 1-3 | 6.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 22.6% | 24.2% | 4.08 | -7.6% |
| Draw | 22.4% | 21.6% | 4.08 | -8.8% |
| VfB Stuttgart win | 55.0% | 54.2% | 1.90 | +4.5% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 20.67 |
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
| P home draw | 45.0% |
| P draw away | 77.4% |
| Raw p home draw | 44.2% |
| Raw p draw away | 79.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.60 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.74 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -1.6% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | -0.0321 |
| Raw ev home | -0.1418 |
| Raw edge prob draw | 0.0156 |
| Raw ev draw | -0.0561 |
| Raw edge prob away | 0.0164 |
| Raw ev away | 0.0608 |
| Market p home draw | 47.6% |
| Market home draw odds | 2.00 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T21:06:59Z |
| Market reference home draw last update utc | 2026-10-14T21:07:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.6% |
| Market draw away odds | 1.28 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T21:06:59Z |
| Market reference draw away last update utc | 2026-10-14T21:07:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.26 |
| Market reference dc home draw odds | 2.00 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 88.5% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T21:06:47Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.3% |
| Market under 3 5 odds | 1.96 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T21:06:47Z |
| Market reference under 3 5 odds | 1.76 |
| Market reference under 3 5 opposite odds | 1.91 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.35 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T21:06:59Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 3.10 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **60.5%**. Expected goals are 0.94 for Union Berlin and 1.94 for Borussia Dortmund (2.88 combined). The most likely exact score is 0-2 at 10.7%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 55.4%; Under 3.5 goals: 67.3%; Double Chance 1X: 39.5%; Double Chance X2: 82.6%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 52.7%; BTTS No (at least one team does not score): 47.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.4% | 5.75 |
| Draw | 22.1% | 4.52 |
| Borussia Dortmund win | 60.5% | 1.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.94 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.4% |
| Under 2.5 | 44.6% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 10.68% |
| 2 | 1-1 | 10.53% |
| 3 | 0-1 | 10.14% |
| 4 | 1-2 | 10.03% |
| 5 | 0-3 | 6.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.4% | 18.0% | 4.98 | -13.4% |
| Draw | 22.1% | 20.9% | 4.52 | -0.1% |
| Borussia Dortmund win | 60.5% | 61.1% | 1.69 | +2.2% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 16.27 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.79 |
| Fair Over 2.5 odds | 1.81 |
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
| P home draw | 39.5% |
| P draw away | 82.6% |
| Raw p home draw | 40.1% |
| Raw p draw away | 83.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.70 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.56 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Home probability edge | -0.6% |
| Draw probability edge | +1.2% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | -0.0119 |
| Raw ev home | -0.1633 |
| Raw edge prob draw | 0.0236 |
| Raw ev draw | 0.0527 |
| Raw edge prob away | -0.0118 |
| Raw ev away | 0.0124 |
| Market p home draw | 41.9% |
| Market home draw odds | 2.31 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T21:06:59Z |
| Market reference home draw last update utc | 2026-10-14T21:07:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.0% |
| Market draw away odds | 1.21 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T21:06:59Z |
| Market reference draw away last update utc | 2026-10-14T21:07:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.19 |
| Market reference dc home draw odds | 2.27 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T21:03:31Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.7% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T21:03:31Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.16 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.2% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T21:06:59Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.54 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **53.0%**. Expected goals are 1.24 for Werder Bremen and 0.61 for SC Paderborn (1.85 combined). The most likely exact score is 1-0 at 19.3%. Goal-market probabilities: at least one goal: 85.9%; Over 2.5 goals: 29.7%; Under 3.5 goals: 88.1%; Double Chance 1X: 80.0%; Double Chance X2: 47.0%; Under 4.5 goals: 95.8%; BTTS Yes (both teams score): 32.3%; BTTS No (at least one team does not score): 67.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 53.0% | 1.89 |
| Draw | 27.0% | 3.70 |
| SC Paderborn win | 20.0% | 4.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.24 |
| SC Paderborn expected goals | 0.61 |
| Expected total goals | 1.85 |
| Over 0.5 | 85.9% |
| Under 0.5 | 14.1% |
| Over 1.5 | 56.5% |
| Under 1.5 | 43.5% |
| Over 2.5 | 29.7% |
| Under 2.5 | 70.3% |
| Over 3.5 | 11.9% |
| Under 3.5 | 88.1% |
| Over 4.5 | 4.2% |
| Under 4.5 | 95.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.33% |
| 2 | 0-0 | 14.13% |
| 3 | 2-0 | 12.67% |
| 4 | 1-1 | 10.84% |
| 5 | 0-1 | 10.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 53.0% | 55.0% | 1.84 | -2.6% |
| Draw | 27.0% | 22.0% | 4.26 | +15.1% |
| SC Paderborn win | 20.0% | 23.0% | 4.21 | -15.7% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.08 |
| Fair Over 1.5 odds | 1.77 |
| Fair Under 1.5 odds | 2.30 |
| Fair Over 2.5 odds | 3.37 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.43 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 23.71 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 50.9% |
| Unadjusted draw probability | 32.0% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 56.1% |
| Raw p under 3 5 | 88.3% |
| Raw p btts yes | 33.3% |
| P home draw | 80.0% |
| P draw away | 47.0% |
| Raw p home draw | 82.9% |
| Raw p draw away | 49.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.72 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.80 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Home probability edge | -2.1% |
| Draw probability edge | +5.0% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -32.8% |
| Under 2.5 probability edge | +32.8% |
| Raw edge prob home | -0.0411 |
| Raw ev home | -0.0634 |
| Raw edge prob draw | 0.0999 |
| Raw ev draw | 0.3635 |
| Raw edge prob away | -0.0588 |
| Raw ev away | -0.2806 |
| Market p home draw | 76.8% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T21:06:59Z |
| Market reference home draw last update utc | 2026-10-14T21:07:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.1% |
| Market draw away odds | 2.07 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T21:06:59Z |
| Market reference draw away last update utc | 2026-10-14T21:07:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.02 |
| Market reference dc home draw odds | 1.24 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 84.2% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T21:05:57Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.1% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T21:05:57Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.23 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.0% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T21:06:59Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.49 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **61.1%**. Expected goals are 2.40 for Bayer Leverkusen and 1.08 for SC Freiburg (3.48 combined). The most likely exact score is 1-1 at 8.9%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 67.0%; Under 3.5 goals: 54.9%; Double Chance 1X: 81.0%; Double Chance X2: 38.9%; Under 4.5 goals: 73.5%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 61.1% | 1.64 |
| Draw | 19.9% | 5.03 |
| SC Freiburg win | 19.0% | 5.27 |

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
| Over 2.5 | 67.0% |
| Under 2.5 | 33.0% |
| Over 3.5 | 45.1% |
| Under 3.5 | 54.9% |
| Over 4.5 | 26.5% |
| Under 4.5 | 73.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.91% |
| 2 | 2-1 | 8.89% |
| 3 | 2-0 | 8.26% |
| 4 | 3-1 | 7.11% |
| 5 | 3-0 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 61.1% | 56.3% | 1.75 | +7.0% |
| Draw | 19.9% | 20.5% | 4.42 | -12.1% |
| SC Freiburg win | 19.0% | 23.2% | 4.62 | -12.4% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 25.82 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.38 |
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
| P home draw | 81.0% |
| P draw away | 38.9% |
| Raw p home draw | 85.3% |
| Raw p draw away | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.68 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.75 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.69 |
| Home probability edge | +4.8% |
| Draw probability edge | -0.6% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | +1.4% |
| Under 2.5 probability edge | -1.4% |
| Raw edge prob home | 0.0960 |
| Raw ev home | 0.1540 |
| Raw edge prob draw | -0.0113 |
| Raw ev draw | -0.1457 |
| Raw edge prob away | -0.0846 |
| Raw ev away | -0.3196 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **41.5%**. Expected goals are 1.87 for Borussia Monchengladbach and 1.78 for TSG Hoffenheim (3.65 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.5%; Double Chance 1X: 58.5%; Double Chance X2: 64.2%; Under 4.5 goals: 69.6%; BTTS Yes (both teams score): 71.0%; BTTS No (at least one team does not score): 29.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 35.8% | 2.80 |
| Draw | 22.7% | 4.41 |
| TSG Hoffenheim win | 41.5% | 2.41 |

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
| Over 4.5 | 30.4% |
| Under 4.5 | 69.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.18% |
| 2 | 1-2 | 8.74% |
| 3 | 2-1 | 7.20% |
| 4 | 2-2 | 7.04% |
| 5 | 1-3 | 5.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 35.8% | 31.4% | 3.33 | +19.1% |
| Draw | 22.7% | 22.2% | 4.21 | -4.5% |
| TSG Hoffenheim win | 41.5% | 46.4% | 2.10 | -12.8% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 30.72 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.80 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.42 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.29 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 36.6% |
| Raw p over 1 5 | 88.6% |
| Raw p under 3 5 | 50.5% |
| Raw p btts yes | 71.0% |
| P home draw | 58.5% |
| P draw away | 64.2% |
| Raw p home draw | 63.4% |
| Raw p draw away | 59.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.99 |
| Home probability edge | +4.4% |
| Draw probability edge | +0.5% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | 0.0878 |
| Raw ev home | 0.3373 |
| Raw edge prob draw | 0.0103 |
| Raw ev draw | -0.0230 |
| Raw edge prob away | -0.0980 |
| Raw ev away | -0.2307 |

</details>


---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **68.8%**. Expected goals are 2.52 for VfB Stuttgart and 1.17 for Borussia Monchengladbach (3.69 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.3%; Over 2.5 goals: 72.2%; Under 3.5 goals: 49.2%; Double Chance 1X: 85.2%; Double Chance X2: 31.2%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 63.5%; BTTS No (at least one team does not score): 36.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 68.8% | 1.45 |
| Draw | 16.5% | 6.07 |
| Borussia Monchengladbach win | 14.8% | 6.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.52 |
| Borussia Monchengladbach expected goals | 1.17 |
| Expected total goals | 3.69 |
| Over 0.5 | 97.3% |
| Under 0.5 | 2.7% |
| Over 1.5 | 89.1% |
| Under 1.5 | 10.9% |
| Over 2.5 | 72.2% |
| Under 2.5 | 27.8% |
| Over 3.5 | 50.8% |
| Under 3.5 | 49.2% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.65% |
| 2 | 2-0 | 8.24% |
| 3 | 3-1 | 8.11% |
| 4 | 1-1 | 7.03% |
| 5 | 3-0 | 6.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 68.8% | 71.5% | 1.43 | -1.7% |
| Draw | 16.5% | 14.3% | 5.80 | -4.5% |
| Borussia Monchengladbach win | 14.8% | 14.3% | 6.98 | +3.1% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.5% |
| P btts no | 36.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.48 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.21 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.60 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 66.0% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 15.3% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 49.6% |
| Raw p btts yes | 64.1% |
| P home draw | 85.2% |
| P draw away | 31.2% |
| Raw p home draw | 84.7% |
| Raw p draw away | 34.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.32 |
| Reference draw odds | 5.00 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.76 |
| Home probability edge | -2.7% |
| Draw probability edge | +2.2% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | -0.0542 |
| Raw ev home | -0.0555 |
| Raw edge prob draw | 0.0441 |
| Raw ev draw | 0.0833 |
| Raw edge prob away | 0.0101 |
| Raw ev away | 0.0662 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **40.8%**. Expected goals are 0.97 for 1. FC Köln and 0.96 for FC Schalke 04 (1.93 combined). The most likely exact score is 1-0 at 15.8%. Goal-market probabilities: at least one goal: 86.9%; Over 2.5 goals: 32.1%; Under 3.5 goals: 86.7%; Double Chance 1X: 69.2%; Double Chance X2: 59.2%; Under 4.5 goals: 95.0%; BTTS Yes (both teams score): 38.3%; BTTS No (at least one team does not score): 61.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 40.8% | 2.45 |
| Draw | 28.4% | 3.53 |
| FC Schalke 04 win | 30.8% | 3.24 |

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
| 1 | 1-0 | 15.79% |
| 2 | 0-0 | 13.14% |
| 3 | 1-1 | 12.30% |
| 4 | 0-1 | 12.04% |
| 5 | 2-0 | 8.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 40.8% | 48.0% | 2.12 | -13.5% |
| Draw | 28.4% | 22.9% | 3.98 | +12.9% |
| FC Schalke 04 win | 30.8% | 29.0% | 3.43 | +5.8% |
| Over 2.5 | 32.1% | 61.2% | 1.64 | -47.4% |
| Under 2.5 | 67.9% | 38.8% | 2.46 | +67.0% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| P home draw | 69.2% |
| P draw away | 59.2% |
| Raw p home draw | 67.3% |
| Raw p draw away | 66.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.41 |
| Home probability edge | -7.2% |
| Draw probability edge | +5.4% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -29.1% |
| Under 2.5 probability edge | +29.1% |
| Raw edge prob home | -0.1447 |
| Raw ev home | -0.2886 |
| Raw edge prob draw | 0.1084 |
| Raw ev draw | 0.3448 |
| Raw edge prob away | 0.0363 |
| Raw ev away | 0.1200 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **50.6%**. Expected goals are 1.60 for Augsburg and 1.05 for Union Berlin (2.65 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 50.2%; Under 3.5 goals: 72.4%; Double Chance 1X: 75.4%; Double Chance X2: 49.4%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 52.4%; BTTS No (at least one team does not score): 47.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 50.6% | 1.98 |
| Draw | 24.9% | 4.02 |
| Union Berlin win | 24.6% | 4.07 |

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
| Over 2.5 | 50.2% |
| Under 2.5 | 49.8% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.88% |
| 2 | 1-0 | 10.59% |
| 3 | 2-1 | 9.74% |
| 4 | 2-0 | 9.31% |
| 5 | 0-0 | 7.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 50.6% | 51.8% | 1.96 | -0.9% |
| Draw | 24.9% | 22.9% | 4.16 | +3.6% |
| Union Berlin win | 24.6% | 25.4% | 3.77 | -7.4% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 13.42 |
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
| P home draw | 75.4% |
| P draw away | 49.4% |
| Raw p home draw | 76.2% |
| Raw p draw away | 50.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.76 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Home probability edge | -1.2% |
| Draw probability edge | +2.0% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -12.2% |
| Under 2.5 probability edge | +12.2% |
| Raw edge prob home | -0.0245 |
| Raw ev home | -0.0331 |
| Raw edge prob draw | 0.0404 |
| Raw ev draw | 0.1195 |
| Raw edge prob away | -0.0159 |
| Raw ev away | -0.1043 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **66.0%**. Expected goals are 2.43 for Borussia Dortmund and 1.20 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 71.0%; Under 3.5 goals: 50.5%; Double Chance 1X: 83.8%; Double Chance X2: 34.0%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 66.0% | 1.52 |
| Draw | 17.8% | 5.61 |
| Eintracht Frankfurt win | 16.2% | 6.17 |

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
| 1 | 2-1 | 9.70% |
| 2 | 2-0 | 8.07% |
| 3 | 3-1 | 7.87% |
| 4 | 1-1 | 7.65% |
| 5 | 3-0 | 6.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 66.0% | 68.1% | 1.48 | -2.4% |
| Draw | 17.8% | 16.2% | 5.39 | -3.9% |
| Eintracht Frankfurt win | 16.2% | 15.8% | 6.42 | +4.1% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 33.29 |
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
| P home draw | 83.8% |
| P draw away | 34.0% |
| Raw p home draw | 83.3% |
| Raw p draw away | 36.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.38 |
| Reference draw odds | 4.60 |
| Reference away odds | 4.70 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.31 |
| Home probability edge | -2.1% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0423 |
| Raw ev home | -0.0551 |
| Raw edge prob draw | 0.0333 |
| Raw ev draw | 0.0507 |
| Raw edge prob away | 0.0091 |
| Raw ev away | 0.0698 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **54.0%**. Expected goals are 1.66 for FSV Mainz 05 and 1.14 for Werder Bremen (2.80 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 54.3%; Under 3.5 goals: 68.7%; Double Chance 1X: 77.3%; Double Chance X2: 46.0%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 54.0% | 1.85 |
| Draw | 23.4% | 4.28 |
| Werder Bremen win | 22.7% | 4.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.66 |
| Werder Bremen expected goals | 1.14 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.3% |
| Under 1.5 | 21.7% |
| Over 2.5 | 54.3% |
| Under 2.5 | 45.7% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.10% |
| 2 | 2-1 | 10.61% |
| 3 | 1-0 | 10.12% |
| 4 | 2-0 | 9.31% |
| 5 | 0-0 | 6.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 54.0% | 59.3% | 1.73 | -6.6% |
| Draw | 23.4% | 20.5% | 4.41 | +3.0% |
| Werder Bremen win | 22.7% | 20.2% | 4.72 | +7.0% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 15.97 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.60 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.34 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 25.1% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 56.1% |
| P home draw | 77.3% |
| P draw away | 46.0% |
| Raw p home draw | 74.9% |
| Raw p draw away | 51.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.90 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.54 |
| Home probability edge | -5.3% |
| Draw probability edge | +2.9% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.1066 |
| Raw ev home | -0.1587 |
| Raw edge prob draw | 0.0572 |
| Raw ev draw | 0.1566 |
| Raw edge prob away | 0.0494 |
| Raw ev away | 0.1867 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **63.1%**. Expected goals are 1.99 for RB Leipzig and 1.38 for Elversberg (3.37 combined). The most likely exact score is 2-1 at 11.6%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 67.5%; Under 3.5 goals: 55.6%; Double Chance 1X: 81.2%; Double Chance X2: 36.9%; Under 4.5 goals: 73.7%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 63.1% | 1.58 |
| Draw | 18.1% | 5.52 |
| Elversberg win | 18.8% | 5.33 |

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
| 1 | 2-1 | 11.64% |
| 2 | 2-0 | 8.45% |
| 3 | 1-1 | 7.95% |
| 4 | 3-1 | 7.73% |
| 5 | 1-0 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 63.1% | 75.3% | 1.39 | -12.2% |
| Draw | 18.1% | 12.9% | 6.09 | +10.2% |
| Elversberg win | 18.8% | 11.8% | 7.70 | +44.4% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 30.40 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.31 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.08 |
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
| P home draw | 81.2% |
| P draw away | 36.9% |
| Raw p home draw | 74.3% |
| Raw p draw away | 49.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.26 |
| Reference draw odds | 5.30 |
| Reference away odds | 5.70 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.85 |
| Home probability edge | -12.2% |
| Draw probability edge | +5.2% |
| Away probability edge | +7.0% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | -0.2430 |
| Raw ev home | -0.2912 |
| Raw edge prob draw | 0.1040 |
| Raw ev draw | 0.4190 |
| Raw edge prob away | 0.1391 |
| Raw ev away | 0.9795 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **34.9%**. Expected goals are 0.78 for SC Paderborn and 0.89 for Hamburger SV (1.67 combined). The most likely exact score is 0-0 at 16.6%. Goal-market probabilities: at least one goal: 83.4%; Over 2.5 goals: 25.1%; Under 3.5 goals: 91.0%; Double Chance 1X: 65.3%; Double Chance X2: 65.1%; Under 4.5 goals: 97.0%; BTTS Yes (both teams score): 31.8%; BTTS No (at least one team does not score): 68.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 34.9% | 2.86 |
| Draw | 30.4% | 3.29 |
| Hamburger SV win | 34.7% | 2.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.78 |
| Hamburger SV expected goals | 0.89 |
| Expected total goals | 1.67 |
| Over 0.5 | 83.4% |
| Under 0.5 | 16.6% |
| Over 1.5 | 51.2% |
| Under 1.5 | 48.8% |
| Over 2.5 | 25.1% |
| Under 2.5 | 74.9% |
| Over 3.5 | 9.0% |
| Under 3.5 | 91.0% |
| Over 4.5 | 3.0% |
| Under 4.5 | 97.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 16.57% |
| 2 | 1-0 | 16.57% |
| 3 | 0-1 | 15.61% |
| 4 | 1-1 | 11.78% |
| 5 | 0-2 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 34.9% | 41.2% | 2.40 | -16.2% |
| Draw | 30.4% | 24.2% | 3.92 | +19.1% |
| Hamburger SV win | 34.7% | 34.6% | 2.91 | +1.0% |
| Over 2.5 | 25.1% | 61.8% | 1.64 | -58.9% |
| Under 2.5 | 74.9% | 38.2% | 2.47 | +85.1% |

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
| Market best home last update utc | 2026-10-14T21:06:59Z |
| Market best draw last update utc | 2026-10-14T21:06:59Z |
| Market best away last update utc | 2026-10-14T21:06:59Z |
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
| Fair Under 0.5 odds | 6.03 |
| Fair Over 1.5 odds | 1.95 |
| Fair Under 1.5 odds | 2.05 |
| Fair Over 2.5 odds | 3.99 |
| Fair Under 2.5 odds | 1.33 |
| Fair Over 3.5 odds | 11.06 |
| Fair Under 3.5 odds | 1.10 |
| Fair Over 4.5 odds | 33.55 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 28.6% |
| Unadjusted draw probability | 36.5% |
| Unadjusted away-win probability | 34.8% |
| Raw p over 1 5 | 50.8% |
| Raw p under 3 5 | 91.1% |
| Raw p btts yes | 33.0% |
| P home draw | 65.3% |
| P draw away | 65.1% |
| Raw p home draw | 65.2% |
| Raw p draw away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -6.3% |
| Draw probability edge | +6.2% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -36.7% |
| Under 2.5 probability edge | +36.7% |
| Raw edge prob home | -0.1254 |
| Raw ev home | -0.3124 |
| Raw edge prob draw | 0.1233 |
| Raw ev draw | 0.4327 |
| Raw edge prob away | 0.0021 |
| Raw ev away | 0.0127 |

</details>


---
