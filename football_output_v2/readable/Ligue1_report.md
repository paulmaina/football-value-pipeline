# Ligue 1 — football model report

Fixtures in this report: **10**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 972 |
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
| Optimizer objective | 1681.020 |
| Base scoring parameter | 0.195 |
| Home-advantage parameter | 0.201 |
| Dixon-Coles low-score adjustment | -0.043 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-11', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 10.00 |
| Additional event odds calls used before this league | 3.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-16 — Le Mans FC vs Toulouse

The model's most likely 1X2 outcome is **Le Mans FC win** at **38.1%**. Expected goals are 1.86 for Le Mans FC and 1.48 for Toulouse (3.34 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 63.9%; Under 3.5 goals: 57.6%; Double Chance 1X: 63.7%; Double Chance X2: 61.9%; Under 4.5 goals: 76.1%; BTTS Yes (both teams score): 66.3%; BTTS No (at least one team does not score): 33.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 38.1% | 2.63 |
| Draw | 25.7% | 3.90 |
| Toulouse win | 36.3% | 2.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Mans FC expected goals | 1.86 |
| Toulouse expected goals | 1.48 |
| Expected total goals | 3.34 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 63.9% |
| Under 2.5 | 36.1% |
| Over 3.5 | 42.4% |
| Under 3.5 | 57.6% |
| Over 4.5 | 23.9% |
| Under 4.5 | 76.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.21% |
| 2 | 1-2 | 8.61% |
| 3 | 2-1 | 7.47% |
| 4 | 2-2 | 7.38% |
| 5 | 0-1 | 5.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 38.1% | 29.9% | 3.12 | +18.7% |
| Draw | 25.7% | 28.0% | 3.61 | -7.4% |
| Toulouse win | 36.3% | 42.1% | 2.39 | -13.3% |
| Over 2.5 | 63.9% | 57.8% | 1.76 | +12.5% |
| Under 2.5 | 36.1% | 42.2% | 2.23 | -19.5% |

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
| Market best home last update utc | 2026-10-14T09:45:57Z |
| Market best draw last update utc | 2026-10-14T09:45:57Z |
| Market best away last update utc | 2026-10-14T09:45:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Mans |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.3% |
| P btts no | 33.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.87 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.57 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.77 |
| Fair Over 3.5 odds | 2.36 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.19 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 46.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 30.5% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.2% |
| Raw p btts yes | 65.6% |
| P home draw | 63.7% |
| P draw away | 61.9% |
| Raw p home draw | 69.5% |
| Raw p draw away | 53.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.10 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.25 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +8.1% |
| Draw probability edge | -2.3% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | +6.1% |
| Under 2.5 probability edge | -6.1% |
| Raw edge prob home | 0.1628 |
| Raw ev home | 0.4413 |
| Raw edge prob draw | -0.0466 |
| Raw ev draw | -0.1580 |
| Raw edge prob away | -0.1162 |
| Raw ev away | -0.2715 |
| Market p home draw | 58.8% |
| Market home draw odds | 1.65 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T09:45:57Z |
| Market reference home draw last update utc | 2026-10-14T09:45:57Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.3% |
| Market draw away odds | 1.42 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T09:45:57Z |
| Market reference draw away last update utc | 2026-10-14T09:45:57Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.65 |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 80.0% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T09:45:46Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.3% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T09:45:46Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.77 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.5% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T09:45:57Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.46 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **54.9%**. Expected goals are 1.75 for Lille and 0.96 for Brest (2.72 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 51.2%; Under 3.5 goals: 71.1%; Double Chance 1X: 78.7%; Double Chance X2: 45.1%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 54.9% | 1.82 |
| Draw | 23.8% | 4.20 |
| Brest win | 21.3% | 4.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.75 |
| Brest expected goals | 0.96 |
| Expected total goals | 2.72 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 51.2% |
| Under 2.5 | 48.8% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.35% |
| 2 | 1-0 | 10.98% |
| 3 | 2-0 | 10.05% |
| 4 | 2-1 | 9.67% |
| 5 | 0-0 | 6.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 54.9% | 54.2% | 1.86 | +2.0% |
| Draw | 23.8% | 23.2% | 4.04 | -3.8% |
| Brest win | 21.3% | 22.6% | 4.36 | -7.0% |
| Over 2.5 | 51.2% | 57.8% | 1.75 | -10.4% |
| Under 2.5 | 48.8% | 42.2% | 2.25 | +9.8% |

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
| Market best home last update utc | 2026-10-14T09:45:57Z |
| Market best draw last update utc | 2026-10-14T09:45:57Z |
| Market best away last update utc | 2026-10-14T09:45:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.46 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.15 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 55.5% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 20.1% |
| Raw p over 1 5 | 75.9% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 51.6% |
| P home draw | 78.7% |
| P draw away | 45.1% |
| Raw p home draw | 79.9% |
| Raw p draw away | 44.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.77 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.00 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +0.7% |
| Draw probability edge | +0.6% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | 0.0133 |
| Raw ev home | 0.0326 |
| Raw edge prob draw | 0.0121 |
| Raw ev draw | -0.0131 |
| Raw edge prob away | -0.0254 |
| Raw ev away | -0.1256 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **64.0%**. Expected goals are 1.22 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.8%; Under 3.5 goals: 56.8%; Double Chance 1X: 36.0%; Double Chance X2: 82.9%; Under 4.5 goals: 75.0%; BTTS Yes (both teams score): 61.4%; BTTS No (at least one team does not score): 38.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.1% | 5.85 |
| Draw | 18.9% | 5.30 |
| Paris Saint Germain win | 64.0% | 1.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.22 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.8% |
| Under 2.5 | 34.2% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.89% |
| 2 | 0-2 | 8.90% |
| 3 | 1-1 | 8.43% |
| 4 | 0-1 | 8.01% |
| 5 | 1-3 | 7.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.1% | 12.9% | 6.73 | +15.1% |
| Draw | 18.9% | 16.2% | 5.50 | +3.8% |
| Paris Saint Germain win | 64.0% | 70.9% | 1.46 | -6.5% |

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
| Market best home last update utc | 2026-10-14T09:45:57Z |
| Market best draw last update utc | 2026-10-14T09:45:57Z |
| Market best away last update utc | 2026-10-14T09:45:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Strasbourg |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.4% |
| P btts no | 38.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.64 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.79 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.92 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.00 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 57.2% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.4% |
| P home draw | 36.0% |
| P draw away | 82.9% |
| Raw p home draw | 42.8% |
| Raw p draw away | 78.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 6.50 |
| Reference draw odds | 5.30 |
| Reference away odds | 1.37 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Home probability edge | +4.2% |
| Draw probability edge | +2.7% |
| Away probability edge | -6.9% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | 0.0833 |
| Raw ev home | 0.4309 |
| Raw edge prob draw | 0.0542 |
| Raw ev draw | 0.1872 |
| Raw edge prob away | -0.1374 |
| Raw ev away | -0.1656 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **63.6%**. Expected goals are 0.64 for Troyes and 2.21 for RC Lens (2.84 combined). The most likely exact score is 0-2 at 12.4%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 51.9%; Under 3.5 goals: 70.1%; Double Chance 1X: 36.4%; Double Chance X2: 84.3%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 43.6%; BTTS No (at least one team does not score): 56.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 15.7% | 6.35 |
| Draw | 20.7% | 4.84 |
| RC Lens win | 63.6% | 1.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.64 |
| RC Lens expected goals | 2.21 |
| Expected total goals | 2.84 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 76.1% |
| Under 1.5 | 23.9% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 29.9% |
| Under 3.5 | 70.1% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.36% |
| 2 | 0-1 | 10.90% |
| 3 | 1-1 | 9.75% |
| 4 | 0-3 | 9.09% |
| 5 | 1-2 | 7.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 15.7% | 22.6% | 4.30 | -32.3% |
| Draw | 20.7% | 23.2% | 4.04 | -16.6% |
| RC Lens win | 63.6% | 54.2% | 1.87 | +18.9% |
| Over 2.5 | 51.9% | 61.8% | 1.64 | -14.9% |
| Under 2.5 | 48.1% | 38.2% | 2.46 | +18.4% |

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
| Market best home last update utc | 2026-10-14T09:45:57Z |
| Market best draw last update utc | 2026-10-14T09:45:57Z |
| Market best away last update utc | 2026-10-14T09:45:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 43.6% |
| P btts no | 56.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.14 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.18 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.35 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.77 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 8.9% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 73.0% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 42.2% |
| P home draw | 36.4% |
| P draw away | 84.3% |
| Raw p home draw | 27.0% |
| Raw p draw away | 91.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 4.00 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.77 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -6.9% |
| Draw probability edge | -2.6% |
| Away probability edge | +9.4% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | -0.1371 |
| Raw ev home | -0.6179 |
| Raw edge prob draw | -0.0513 |
| Raw ev draw | -0.2694 |
| Raw edge prob away | 0.1884 |
| Raw ev away | 0.3656 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **51.3%**. Expected goals are 0.95 for Angers and 1.71 for Marseille (2.66 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.7%; Double Chance 1X: 48.7%; Double Chance X2: 76.4%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 23.6% | 4.24 |
| Draw | 25.1% | 3.98 |
| Marseille win | 51.3% | 1.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.95 |
| Marseille expected goals | 1.71 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 74.5% |
| Under 1.5 | 25.5% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 27.3% |
| Under 3.5 | 72.7% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.97% |
| 2 | 0-1 | 10.75% |
| 3 | 0-2 | 9.59% |
| 4 | 1-2 | 9.07% |
| 5 | 0-0 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 23.6% | 27.0% | 3.37 | -20.4% |
| Draw | 25.1% | 25.4% | 3.79 | -4.8% |
| Marseille win | 51.3% | 47.6% | 2.20 | +12.8% |
| Over 2.5 | 49.3% | 60.9% | 1.67 | -17.7% |
| Under 2.5 | 50.7% | 39.1% | 2.40 | +21.8% |

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
| Market best home last update utc | 2026-10-14T09:45:57Z |
| Market best draw last update utc | 2026-10-14T09:45:57Z |
| Market best away last update utc | 2026-10-14T09:45:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.17 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.92 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.66 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.76 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 54.9% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.4% |
| Raw p btts yes | 50.6% |
| P home draw | 48.7% |
| P draw away | 76.4% |
| Raw p home draw | 45.1% |
| Raw p draw away | 79.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.40 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | -3.4% |
| Draw probability edge | -0.3% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -11.6% |
| Under 2.5 probability edge | +11.6% |
| Raw edge prob home | -0.0676 |
| Raw ev home | -0.3182 |
| Raw edge prob draw | -0.0052 |
| Raw ev draw | -0.0576 |
| Raw edge prob away | 0.0728 |
| Raw ev away | 0.2079 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **38.8%**. Expected goals are 1.17 for Le Havre and 1.17 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.7%; Under 3.5 goals: 79.1%; Double Chance 1X: 67.4%; Double Chance X2: 61.2%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 38.8% | 2.58 |
| Draw | 28.6% | 3.50 |
| Auxerre win | 32.6% | 3.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.17 |
| Auxerre expected goals | 1.17 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 68.5% |
| Under 1.5 | 31.5% |
| Over 2.5 | 41.7% |
| Under 2.5 | 58.3% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.47% |
| 2 | 1-0 | 11.71% |
| 3 | 0-0 | 9.98% |
| 4 | 0-1 | 9.85% |
| 5 | 2-1 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 38.8% | 42.1% | 2.42 | -6.0% |
| Draw | 28.6% | 28.0% | 3.51 | +0.4% |
| Auxerre win | 32.6% | 29.9% | 3.14 | +2.3% |
| Over 2.5 | 41.7% | 52.2% | 1.95 | -18.7% |
| Under 2.5 | 58.3% | 47.8% | 1.99 | +16.0% |

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
| Market best home last update utc | 2026-10-14T09:45:57Z |
| Market best draw last update utc | 2026-10-14T09:45:57Z |
| Market best away last update utc | 2026-10-14T09:45:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
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
| Fair Under 0.5 odds | 10.02 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.40 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.78 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.21 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 35.6% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 68.4% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 48.2% |
| P home draw | 67.4% |
| P draw away | 61.2% |
| Raw p home draw | 64.8% |
| Raw p draw away | 64.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.25 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | -3.3% |
| Draw probability edge | +0.6% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | -0.0654 |
| Raw ev home | -0.1394 |
| Raw edge prob draw | 0.0123 |
| Raw ev draw | 0.0254 |
| Raw edge prob away | 0.0531 |
| Raw ev away | 0.1060 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **48.1%**. Expected goals are 1.37 for Lorient and 1.80 for AS Monaco (3.17 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.0%; Under 3.5 goals: 60.8%; Double Chance 1X: 51.9%; Double Chance X2: 73.5%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 26.5% | 3.78 |
| Draw | 25.5% | 3.93 |
| AS Monaco win | 48.1% | 2.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.37 |
| AS Monaco expected goals | 1.80 |
| Expected total goals | 3.17 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.0% |
| Under 2.5 | 39.0% |
| Over 3.5 | 39.2% |
| Under 3.5 | 60.8% |
| Over 4.5 | 21.3% |
| Under 4.5 | 78.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.50% |
| 2 | 1-2 | 9.49% |
| 3 | 0-1 | 7.22% |
| 4 | 0-2 | 6.92% |
| 5 | 2-2 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 26.5% | 24.0% | 3.87 | +2.4% |
| Draw | 25.5% | 27.0% | 3.58 | -8.9% |
| AS Monaco win | 48.1% | 49.0% | 2.10 | +1.0% |
| Over 2.5 | 61.0% | 50.0% | 1.97 | +20.1% |
| Under 2.5 | 39.0% | 50.0% | 1.97 | -23.1% |

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
| Market best home last update utc | 2026-10-14T09:45:57Z |
| Market best draw last update utc | 2026-10-14T09:45:57Z |
| Market best away last update utc | 2026-10-14T09:45:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lorient |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.26 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.88 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.70 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 28.9% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 47.2% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 62.8% |
| P home draw | 51.9% |
| P draw away | 73.5% |
| Raw p home draw | 52.8% |
| Raw p draw away | 71.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.80 |
| Reference draw odds | 3.40 |
| Reference away odds | 1.95 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.87 |
| Home probability edge | +2.5% |
| Draw probability edge | -1.6% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +11.0% |
| Under 2.5 probability edge | -11.0% |
| Raw edge prob home | 0.0492 |
| Raw ev home | 0.1190 |
| Raw edge prob draw | -0.0316 |
| Raw ev draw | -0.1454 |
| Raw edge prob away | -0.0176 |
| Raw ev away | -0.0085 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **56.3%**. Expected goals are 1.77 for Lyon and 1.09 for Nice (2.86 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.1%; Under 3.5 goals: 67.6%; Double Chance 1X: 79.1%; Double Chance X2: 43.7%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 55.0%; BTTS No (at least one team does not score): 45.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 56.3% | 1.78 |
| Draw | 22.9% | 4.37 |
| Nice win | 20.9% | 4.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.77 |
| Nice expected goals | 1.09 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 78.6% |
| Under 1.5 | 21.4% |
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.84% |
| 2 | 2-1 | 10.40% |
| 3 | 1-0 | 10.30% |
| 4 | 2-0 | 9.57% |
| 5 | 3-1 | 6.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 56.3% | 59.6% | 1.71 | -3.8% |
| Draw | 22.9% | 21.4% | 4.21 | -3.7% |
| Nice win | 20.9% | 19.0% | 5.18 | +8.1% |
| Over 2.5 | 55.1% | 59.3% | 1.72 | -5.3% |
| Under 2.5 | 44.9% | 40.7% | 2.31 | +3.8% |

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
| Market best home last update utc | 2026-10-14T09:45:57Z |
| Market best draw last update utc | 2026-10-14T09:45:57Z |
| Market best away last update utc | 2026-10-14T09:45:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lyon |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.0% |
| P btts no | 45.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.10 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.67 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.08 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 52.9% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| P home draw | 79.1% |
| P draw away | 43.7% |
| Raw p home draw | 77.3% |
| Raw p draw away | 47.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.62 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.70 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -3.3% |
| Draw probability edge | +1.5% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.0665 |
| Raw ev home | -0.0949 |
| Raw edge prob draw | 0.0291 |
| Raw ev draw | 0.0248 |
| Raw edge prob away | 0.0374 |
| Raw ev away | 0.1774 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **42.5%**. Expected goals are 1.57 for Paris FC and 1.37 for Rennes (2.94 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.1%; Double Chance 1X: 69.2%; Double Chance X2: 57.5%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 42.5% | 2.35 |
| Draw | 26.7% | 3.75 |
| Rennes win | 30.8% | 3.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.57 |
| Rennes expected goals | 1.37 |
| Expected total goals | 2.94 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.46% |
| 2 | 2-1 | 9.08% |
| 3 | 1-0 | 7.94% |
| 4 | 1-2 | 7.32% |
| 5 | 2-0 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 42.5% | 43.1% | 2.37 | +0.7% |
| Draw | 26.7% | 28.0% | 3.45 | -7.9% |
| Rennes win | 30.8% | 28.9% | 3.29 | +1.3% |
| Over 2.5 | 55.9% | 59.3% | 1.72 | -3.9% |
| Under 2.5 | 44.1% | 40.7% | 2.30 | +1.4% |

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
| Market best home last update utc | 2026-10-14T09:45:57Z |
| Market best draw last update utc | 2026-10-14T09:45:57Z |
| Market best away last update utc | 2026-10-14T09:45:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paris FC |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.47 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.78 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 41.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.1% |
| Raw p btts yes | 59.5% |
| P home draw | 69.2% |
| P draw away | 57.5% |
| Raw p home draw | 67.3% |
| Raw p draw away | 58.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.20 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -0.6% |
| Draw probability edge | -1.3% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.0123 |
| Raw ev home | -0.0072 |
| Raw edge prob draw | -0.0255 |
| Raw ev draw | -0.1229 |
| Raw edge prob away | 0.0378 |
| Raw ev away | 0.0754 |

</details>


---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **43.3%**. Expected goals are 1.56 for Brest and 1.28 for Nice (2.84 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 53.5%; Under 3.5 goals: 68.4%; Double Chance 1X: 70.2%; Double Chance X2: 56.7%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 43.3% | 2.31 |
| Draw | 26.9% | 3.72 |
| Nice win | 29.8% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Nice expected goals | 1.28 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.5% |
| Under 2.5 | 46.5% |
| Over 3.5 | 31.6% |
| Under 3.5 | 68.4% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.69% |
| 2 | 2-1 | 9.07% |
| 3 | 1-0 | 8.61% |
| 4 | 1-2 | 7.23% |
| 5 | 2-0 | 7.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 43.3% | 43.1% | 2.31 | -0.1% |
| Draw | 26.9% | 28.0% | 3.49 | -6.1% |
| Nice win | 29.8% | 28.9% | 3.37 | +0.6% |
| Over 2.5 | 53.5% | 58.9% | 1.76 | -5.8% |
| Under 2.5 | 46.5% | 41.1% | 2.23 | +3.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 8aa36b30d655d6c81ed98bf9ec1b4039 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T09:45:57Z |
| Market best draw last update utc | 2026-10-14T09:45:57Z |
| Market best away last update utc | 2026-10-14T09:45:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brest |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.07 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.17 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.39 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.5% |
| P home draw | 70.2% |
| P draw away | 56.7% |
| Raw p home draw | 69.2% |
| Raw p draw away | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.20 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | +0.1% |
| Draw probability edge | -1.1% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | 0.0028 |
| Raw ev home | 0.0025 |
| Raw edge prob draw | -0.0215 |
| Raw ev draw | -0.0986 |
| Raw edge prob away | 0.0186 |
| Raw ev away | 0.0370 |

</details>


---
