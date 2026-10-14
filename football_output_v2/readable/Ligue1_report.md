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

The model's most likely 1X2 outcome is **Le Mans FC win** at **38.8%**. Expected goals are 1.86 for Le Mans FC and 1.48 for Toulouse (3.34 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 64.0%; Under 3.5 goals: 57.6%; Double Chance 1X: 64.1%; Double Chance X2: 61.2%; Under 4.5 goals: 76.1%; BTTS Yes (both teams score): 66.2%; BTTS No (at least one team does not score): 33.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 38.8% | 2.58 |
| Draw | 25.3% | 3.95 |
| Toulouse win | 35.9% | 2.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Mans FC expected goals | 1.86 |
| Toulouse expected goals | 1.48 |
| Expected total goals | 3.34 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 64.0% |
| Under 2.5 | 36.0% |
| Over 3.5 | 42.4% |
| Under 3.5 | 57.6% |
| Over 4.5 | 23.9% |
| Under 4.5 | 76.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.05% |
| 2 | 1-2 | 8.52% |
| 3 | 2-1 | 7.61% |
| 4 | 2-2 | 7.28% |
| 5 | 0-1 | 5.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 38.8% | 31.4% | 3.12 | +21.0% |
| Draw | 25.3% | 27.3% | 3.61 | -8.7% |
| Toulouse win | 35.9% | 41.4% | 2.39 | -14.1% |
| Over 2.5 | 64.0% | 53.7% | 1.76 | +12.7% |
| Under 2.5 | 36.0% | 46.3% | 2.23 | -19.8% |

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
| Market best home last update utc | 2026-10-14T11:22:48Z |
| Market best draw last update utc | 2026-10-14T11:22:48Z |
| Market best away last update utc | 2026-10-14T11:22:48Z |
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
| P btts yes | 66.2% |
| P btts no | 33.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.20 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.58 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.78 |
| Fair Over 3.5 odds | 2.36 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.18 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 46.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 30.5% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.2% |
| Raw p btts yes | 65.6% |
| P home draw | 64.1% |
| P draw away | 61.2% |
| Raw p home draw | 69.5% |
| Raw p draw away | 53.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.90 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.25 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.00 |
| Home probability edge | +7.4% |
| Draw probability edge | -2.0% |
| Away probability edge | -5.4% |
| Over 2.5 probability edge | +10.3% |
| Under 2.5 probability edge | -10.3% |
| Raw edge prob home | 0.1482 |
| Raw ev home | 0.4413 |
| Raw edge prob draw | -0.0394 |
| Raw ev draw | -0.1580 |
| Raw edge prob away | -0.1088 |
| Raw ev away | -0.2715 |
| Market p home draw | 60.1% |
| Market home draw odds | 1.65 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:22:48Z |
| Market reference home draw last update utc | 2026-10-14T11:22:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.4% |
| Market draw away odds | 1.42 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:22:48Z |
| Market reference draw away last update utc | 2026-10-14T11:22:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.57 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 80.0% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T11:18:34Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.4% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T11:18:34Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.81 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.8% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:22:48Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **54.9%**. Expected goals are 1.75 for Lille and 0.96 for Brest (2.72 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 51.1%; Under 3.5 goals: 71.1%; Double Chance 1X: 79.0%; Double Chance X2: 45.1%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 54.9% | 1.82 |
| Draw | 24.2% | 4.14 |
| Brest win | 21.0% | 4.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.75 |
| Brest expected goals | 0.96 |
| Expected total goals | 2.72 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.51% |
| 2 | 1-0 | 10.98% |
| 3 | 2-0 | 10.05% |
| 4 | 2-1 | 9.67% |
| 5 | 0-0 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 54.9% | 54.2% | 1.86 | +2.0% |
| Draw | 24.2% | 23.9% | 4.04 | -2.4% |
| Brest win | 21.0% | 21.9% | 4.36 | -8.5% |
| Over 2.5 | 51.1% | 56.9% | 1.75 | -10.6% |
| Under 2.5 | 48.9% | 43.1% | 2.25 | +10.0% |

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
| Market best home last update utc | 2026-10-14T11:22:48Z |
| Market best draw last update utc | 2026-10-14T11:22:48Z |
| Market best away last update utc | 2026-10-14T11:22:48Z |
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
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.26 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.17 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 55.5% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 20.1% |
| Raw p over 1 5 | 75.9% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 51.6% |
| P home draw | 79.0% |
| P draw away | 45.1% |
| Raw p home draw | 79.9% |
| Raw p draw away | 44.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.75 |
| Reference draw odds | 3.70 |
| Reference away odds | 4.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +0.7% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.0132 |
| Raw ev home | 0.0326 |
| Raw edge prob draw | 0.0055 |
| Raw ev draw | -0.0131 |
| Raw edge prob away | -0.0187 |
| Raw ev away | -0.1256 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **63.0%**. Expected goals are 1.22 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 65.5%; Under 3.5 goals: 56.9%; Double Chance 1X: 37.0%; Double Chance X2: 82.5%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 61.6%; BTTS No (at least one team does not score): 38.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.5% | 5.73 |
| Draw | 19.5% | 5.12 |
| Paris Saint Germain win | 63.0% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.22 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 65.5% |
| Under 2.5 | 34.5% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.71% |
| 2 | 0-2 | 8.75% |
| 3 | 1-1 | 8.73% |
| 4 | 0-1 | 7.88% |
| 5 | 1-3 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.5% | 13.7% | 6.73 | +17.5% |
| Draw | 19.5% | 17.5% | 5.50 | +7.5% |
| Paris Saint Germain win | 63.0% | 68.8% | 1.46 | -8.0% |

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
| Market best home last update utc | 2026-10-14T11:22:48Z |
| Market best draw last update utc | 2026-10-14T11:22:48Z |
| Market best away last update utc | 2026-10-14T11:22:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Strasbourg |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.6% |
| P btts no | 38.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.65 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.02 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 57.2% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.4% |
| P home draw | 37.0% |
| P draw away | 82.5% |
| Raw p home draw | 42.8% |
| Raw p draw away | 78.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 6.00 |
| Reference draw odds | 4.80 |
| Reference away odds | 1.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Home probability edge | +3.8% |
| Draw probability edge | +2.0% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | 0.0759 |
| Raw ev home | 0.4309 |
| Raw edge prob draw | 0.0407 |
| Raw ev draw | 0.1872 |
| Raw edge prob away | -0.1166 |
| Raw ev away | -0.1656 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **63.0%**. Expected goals are 0.64 for Troyes and 2.21 for RC Lens (2.84 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 51.6%; Under 3.5 goals: 70.2%; Double Chance 1X: 37.0%; Double Chance X2: 84.1%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 43.8%; BTTS No (at least one team does not score): 56.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 15.9% | 6.30 |
| Draw | 21.2% | 4.73 |
| RC Lens win | 63.0% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.64 |
| RC Lens expected goals | 2.21 |
| Expected total goals | 2.84 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 51.6% |
| Under 2.5 | 48.4% |
| Over 3.5 | 29.8% |
| Under 3.5 | 70.2% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.24% |
| 2 | 0-1 | 10.79% |
| 3 | 1-1 | 9.99% |
| 4 | 0-3 | 9.00% |
| 5 | 1-2 | 7.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 15.9% | 22.9% | 4.30 | -31.7% |
| Draw | 21.2% | 24.2% | 4.04 | -14.5% |
| RC Lens win | 63.0% | 52.9% | 1.87 | +17.7% |
| Over 2.5 | 51.6% | 61.3% | 1.64 | -15.3% |
| Under 2.5 | 48.4% | 38.7% | 2.46 | +19.0% |

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
| Market best home last update utc | 2026-10-14T11:22:49Z |
| Market best draw last update utc | 2026-10-14T11:22:49Z |
| Market best away last update utc | 2026-10-14T11:22:49Z |
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
| P btts yes | 43.8% |
| P btts no | 56.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.81 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.16 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.36 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.81 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 8.9% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 73.0% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 42.2% |
| P home draw | 37.0% |
| P draw away | 84.1% |
| Raw p home draw | 27.0% |
| Raw p draw away | 91.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.90 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -7.0% |
| Draw probability edge | -3.1% |
| Away probability edge | +10.1% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.1400 |
| Raw ev home | -0.6179 |
| Raw edge prob draw | -0.0614 |
| Raw ev draw | -0.2694 |
| Raw edge prob away | 0.2014 |
| Raw ev away | 0.3656 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **50.4%**. Expected goals are 0.95 for Angers and 1.71 for Marseille (2.66 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 49.2%; Under 3.5 goals: 72.8%; Double Chance 1X: 49.6%; Double Chance X2: 75.7%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 24.3% | 4.12 |
| Draw | 25.3% | 3.95 |
| Marseille win | 50.4% | 1.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.95 |
| Marseille expected goals | 1.71 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 74.4% |
| Under 1.5 | 25.6% |
| Over 2.5 | 49.2% |
| Under 2.5 | 50.8% |
| Over 3.5 | 27.2% |
| Under 3.5 | 72.8% |
| Over 4.5 | 12.8% |
| Under 4.5 | 87.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.05% |
| 2 | 0-1 | 10.58% |
| 3 | 0-2 | 9.44% |
| 4 | 1-2 | 8.92% |
| 5 | 0-0 | 7.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 24.3% | 28.3% | 3.37 | -18.1% |
| Draw | 25.3% | 25.7% | 3.79 | -4.1% |
| Marseille win | 50.4% | 45.9% | 2.20 | +10.9% |
| Over 2.5 | 49.2% | 58.9% | 1.67 | -17.9% |
| Under 2.5 | 50.8% | 41.1% | 2.40 | +22.0% |

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
| Market best home last update utc | 2026-10-14T11:22:49Z |
| Market best draw last update utc | 2026-10-14T11:22:49Z |
| Market best away last update utc | 2026-10-14T11:22:49Z |
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
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.09 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.91 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.67 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.79 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 54.9% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.4% |
| Raw p btts yes | 50.6% |
| P home draw | 49.6% |
| P draw away | 75.7% |
| Raw p home draw | 45.1% |
| Raw p draw away | 79.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.20 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.05 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -4.1% |
| Draw probability edge | -0.4% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | -9.8% |
| Under 2.5 probability edge | +9.8% |
| Raw edge prob home | -0.0812 |
| Raw ev home | -0.3182 |
| Raw edge prob draw | -0.0086 |
| Raw ev draw | -0.0576 |
| Raw edge prob away | 0.0897 |
| Raw ev away | 0.2079 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **38.2%**. Expected goals are 1.17 for Le Havre and 1.17 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.7%; Under 3.5 goals: 79.1%; Double Chance 1X: 66.7%; Double Chance X2: 61.8%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 38.2% | 2.62 |
| Draw | 28.6% | 3.50 |
| Auxerre win | 33.3% | 3.01 |

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
| 1 | 1-1 | 13.46% |
| 2 | 1-0 | 11.51% |
| 3 | 0-1 | 10.06% |
| 4 | 0-0 | 9.97% |
| 5 | 2-1 | 8.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 38.2% | 40.8% | 2.42 | -7.6% |
| Draw | 28.6% | 27.9% | 3.51 | +0.3% |
| Auxerre win | 33.3% | 31.3% | 3.14 | +4.4% |
| Over 2.5 | 41.7% | 50.5% | 1.95 | -18.7% |
| Under 2.5 | 58.3% | 49.5% | 1.99 | +16.0% |

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
| Market best home last update utc | 2026-10-14T11:22:49Z |
| Market best draw last update utc | 2026-10-14T11:22:49Z |
| Market best away last update utc | 2026-10-14T11:22:49Z |
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
| Fair Under 0.5 odds | 10.03 |
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
| P home draw | 66.7% |
| P draw away | 61.8% |
| Raw p home draw | 64.8% |
| Raw p draw away | 64.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.42 |
| Reference draw odds | 3.51 |
| Reference away odds | 3.14 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.99 |
| Home probability edge | -2.6% |
| Draw probability edge | +0.6% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | -0.0520 |
| Raw ev home | -0.1394 |
| Raw edge prob draw | 0.0127 |
| Raw ev draw | 0.0254 |
| Raw edge prob away | 0.0393 |
| Raw ev away | 0.1060 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **47.1%**. Expected goals are 1.37 for Lorient and 1.80 for AS Monaco (3.17 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.9%; Under 3.5 goals: 60.9%; Double Chance 1X: 52.9%; Double Chance X2: 72.7%; Under 4.5 goals: 78.8%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 27.3% | 3.67 |
| Draw | 25.6% | 3.91 |
| AS Monaco win | 47.1% | 2.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.37 |
| AS Monaco expected goals | 1.80 |
| Expected total goals | 3.17 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 60.9% |
| Under 2.5 | 39.1% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.2% |
| Under 4.5 | 78.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.57% |
| 2 | 1-2 | 9.30% |
| 3 | 0-1 | 7.08% |
| 4 | 2-2 | 6.85% |
| 5 | 0-2 | 6.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 27.3% | 25.6% | 3.87 | +5.5% |
| Draw | 25.6% | 27.3% | 3.58 | -8.4% |
| AS Monaco win | 47.1% | 47.1% | 2.10 | -1.0% |
| Over 2.5 | 60.9% | 50.0% | 1.97 | +20.0% |
| Under 2.5 | 39.1% | 50.0% | 1.97 | -23.0% |

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
| Market best home last update utc | 2026-10-14T11:22:49Z |
| Market best draw last update utc | 2026-10-14T11:22:49Z |
| Market best away last update utc | 2026-10-14T11:22:49Z |
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
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.14 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.71 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 28.9% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 47.2% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 62.8% |
| P home draw | 52.9% |
| P draw away | 72.7% |
| Raw p home draw | 52.8% |
| Raw p draw away | 71.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.50 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | +1.6% |
| Draw probability edge | -1.7% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +10.9% |
| Under 2.5 probability edge | -10.9% |
| Raw edge prob home | 0.0330 |
| Raw ev home | 0.1190 |
| Raw edge prob draw | -0.0344 |
| Raw ev draw | -0.1454 |
| Raw edge prob away | 0.0014 |
| Raw ev away | -0.0085 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **55.5%**. Expected goals are 1.77 for Lyon and 1.09 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 54.7%; Under 3.5 goals: 67.7%; Double Chance 1X: 79.2%; Double Chance X2: 44.5%; Under 4.5 goals: 83.7%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 55.5% | 1.80 |
| Draw | 23.8% | 4.21 |
| Nice win | 20.8% | 4.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.77 |
| Nice expected goals | 1.09 |
| Expected total goals | 2.86 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 54.7% |
| Under 2.5 | 45.3% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.3% |
| Under 4.5 | 83.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.26% |
| 2 | 2-1 | 10.25% |
| 3 | 1-0 | 10.15% |
| 4 | 2-0 | 9.43% |
| 5 | 0-0 | 6.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 55.5% | 58.0% | 1.71 | -5.2% |
| Draw | 23.8% | 23.2% | 4.21 | +0.1% |
| Nice win | 20.8% | 18.8% | 5.18 | +7.6% |
| Over 2.5 | 54.7% | 57.5% | 1.72 | -5.9% |
| Under 2.5 | 45.3% | 42.5% | 2.31 | +4.6% |

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
| Market best home last update utc | 2026-10-14T11:22:49Z |
| Market best draw last update utc | 2026-10-14T11:22:49Z |
| Market best away last update utc | 2026-10-14T11:22:49Z |
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
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.46 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.65 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.10 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.13 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 52.9% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| P home draw | 79.2% |
| P draw away | 44.5% |
| Raw p home draw | 77.3% |
| Raw p draw away | 47.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.71 |
| Reference draw odds | 4.21 |
| Reference away odds | 5.18 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.31 |
| Home probability edge | -2.5% |
| Draw probability edge | +0.6% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | -0.0505 |
| Raw ev home | -0.0949 |
| Raw edge prob draw | 0.0113 |
| Raw ev draw | 0.0248 |
| Raw edge prob away | 0.0392 |
| Raw ev away | 0.1774 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **41.8%**. Expected goals are 1.57 for Paris FC and 1.37 for Rennes (2.94 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 55.8%; Under 3.5 goals: 66.1%; Double Chance 1X: 68.7%; Double Chance X2: 58.2%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 59.9%; BTTS No (at least one team does not score): 40.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 41.8% | 2.39 |
| Draw | 26.9% | 3.71 |
| Rennes win | 31.3% | 3.20 |

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
| Over 2.5 | 55.8% |
| Under 2.5 | 44.2% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.57% |
| 2 | 2-1 | 8.92% |
| 3 | 1-0 | 7.81% |
| 4 | 1-2 | 7.43% |
| 5 | 2-0 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 41.8% | 41.7% | 2.37 | -1.0% |
| Draw | 26.9% | 28.5% | 3.45 | -7.0% |
| Rennes win | 31.3% | 29.9% | 3.29 | +2.9% |
| Over 2.5 | 55.8% | 57.4% | 1.72 | -4.0% |
| Under 2.5 | 44.2% | 42.6% | 2.30 | +1.7% |

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
| Market best home last update utc | 2026-10-14T11:22:49Z |
| Market best draw last update utc | 2026-10-14T11:22:49Z |
| Market best away last update utc | 2026-10-14T11:22:49Z |
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
| P btts yes | 59.9% |
| P btts no | 40.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.32 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.79 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 41.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.1% |
| Raw p btts yes | 59.5% |
| P home draw | 68.7% |
| P draw away | 58.2% |
| Raw p home draw | 67.3% |
| Raw p draw away | 58.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.37 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.29 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +0.1% |
| Draw probability edge | -1.5% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | 0.0023 |
| Raw ev home | -0.0072 |
| Raw edge prob draw | -0.0304 |
| Raw ev draw | -0.1229 |
| Raw edge prob away | 0.0282 |
| Raw ev away | 0.0754 |

</details>


---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **43.0%**. Expected goals are 1.56 for Brest and 1.28 for Nice (2.84 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.9%; Under 3.5 goals: 68.4%; Double Chance 1X: 68.8%; Double Chance X2: 57.0%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 43.0% | 2.33 |
| Draw | 25.8% | 3.87 |
| Nice win | 31.2% | 3.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Nice expected goals | 1.28 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 31.6% |
| Under 3.5 | 68.4% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.17% |
| 2 | 2-1 | 9.02% |
| 3 | 1-0 | 8.56% |
| 4 | 1-2 | 7.56% |
| 5 | 0-1 | 7.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 43.0% | 42.6% | 2.31 | -0.7% |
| Draw | 25.8% | 25.8% | 3.49 | -9.9% |
| Nice win | 31.2% | 31.6% | 3.37 | +5.1% |
| Over 2.5 | 53.9% | 54.3% | 1.76 | -5.1% |
| Under 2.5 | 46.1% | 45.7% | 2.23 | +2.8% |

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
| Market best home last update utc | 2026-10-14T11:22:49Z |
| Market best draw last update utc | 2026-10-14T11:22:49Z |
| Market best away last update utc | 2026-10-14T11:22:49Z |
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
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.71 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.16 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.33 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.5% |
| P home draw | 68.8% |
| P draw away | 57.0% |
| Raw p home draw | 69.2% |
| Raw p draw away | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.20 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | +0.4% |
| Draw probability edge | +0.0% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.0079 |
| Raw ev home | 0.0025 |
| Raw edge prob draw | 0.0004 |
| Raw ev draw | -0.0986 |
| Raw edge prob away | -0.0083 |
| Raw ev away | 0.0370 |

</details>


---
