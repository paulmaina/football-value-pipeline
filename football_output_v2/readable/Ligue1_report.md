# Ligue 1 — football model report

Fixtures in this report: **12**.

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
| Training data health | {'training_end': '2026-10-11', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 12.00 |
| Additional event odds calls used before this league | 21.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-16 — Le Mans FC vs Toulouse

The model's most likely 1X2 outcome is **Le Mans FC win** at **38.9%**. Expected goals are 1.86 for Le Mans FC and 1.48 for Toulouse (3.34 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 64.1%; Under 3.5 goals: 57.5%; Double Chance 1X: 64.1%; Double Chance X2: 61.1%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 76.0%; BTTS Yes (both teams score): 66.2%; BTTS No (at least one team does not score): 33.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 38.9% | 2.57 |
| Draw | 25.2% | 3.97 |
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
| Over 2.5 | 64.1% |
| Under 2.5 | 35.9% |
| Over 3.5 | 42.5% |
| Under 3.5 | 57.5% |
| Over 4.5 | 24.0% |
| Under 4.5 | 76.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.00% |
| 2 | 1-2 | 8.52% |
| 3 | 2-1 | 7.64% |
| 4 | 2-2 | 7.24% |
| 5 | 0-1 | 5.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 38.9% | 31.6% | 3.11 | +21.0% |
| Draw | 25.2% | 27.0% | 3.60 | -9.4% |
| Toulouse win | 35.9% | 41.4% | 2.40 | -13.8% |
| Over 2.5 | 64.1% | 56.1% | 1.76 | +12.8% |
| Under 2.5 | 35.9% | 43.9% | 2.23 | -19.9% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.31 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.58 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.78 |
| Fair Over 3.5 odds | 2.36 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.17 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 46.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 30.5% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.2% |
| Raw p btts yes | 65.6% |
| P home draw | 64.1% |
| P draw away | 61.1% |
| P home away | 74.8% |
| Raw p home draw | 69.5% |
| Raw p draw away | 53.8% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.05 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.35 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +7.3% |
| Draw probability edge | -1.8% |
| Away probability edge | -5.4% |
| Over 2.5 probability edge | +7.9% |
| Under 2.5 probability edge | -7.9% |
| Raw edge prob home | 0.1459 |
| Raw ev home | 0.4367 |
| Raw edge prob draw | -0.0370 |
| Raw ev draw | -0.1604 |
| Raw edge prob away | -0.1089 |
| Raw ev away | -0.2685 |
| Market p home draw | 59.0% |
| Market home draw odds | 1.64 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:51:13Z |
| Market reference home draw last update utc | 2026-10-15T09:51:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.9% |
| Market draw away odds | 1.42 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:51:13Z |
| Market reference draw away last update utc | 2026-10-15T09:51:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.1% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:51:13Z |
| Market reference home away last update utc | 2026-10-15T09:51:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.61 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 80.4% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T09:49:53Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.0% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T09:49:53Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.69 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.4% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:51:13Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.52 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **54.6%**. Expected goals are 1.75 for Lille and 0.96 for Brest (2.72 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 51.1%; Under 3.5 goals: 71.1%; Double Chance 1X: 78.8%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 54.6% | 1.83 |
| Draw | 24.2% | 4.13 |
| Brest win | 21.2% | 4.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.75 |
| Brest expected goals | 0.96 |
| Expected total goals | 2.72 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.54% |
| 2 | 1-0 | 10.93% |
| 3 | 2-0 | 10.00% |
| 4 | 2-1 | 9.63% |
| 5 | 0-0 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 54.6% | 53.7% | 1.86 | +1.6% |
| Draw | 24.2% | 24.0% | 4.04 | -2.1% |
| Brest win | 21.2% | 22.3% | 4.36 | -7.7% |
| Over 2.5 | 51.1% | 56.1% | 1.75 | -10.7% |
| Under 2.5 | 48.9% | 43.9% | 2.25 | +10.1% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| Fair Under 0.5 odds | 14.22 |
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
| P home draw | 78.8% |
| P draw away | 45.4% |
| P home away | 75.8% |
| Raw p home draw | 79.9% |
| Raw p draw away | 44.5% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.83 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.30 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +0.9% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | 0.0182 |
| Raw ev home | 0.0326 |
| Raw edge prob draw | 0.0042 |
| Raw ev draw | -0.0131 |
| Raw edge prob away | -0.0224 |
| Raw ev away | -0.1256 |
| Market p home draw | 76.6% |
| Market home draw odds | 1.26 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:51:13Z |
| Market reference home draw last update utc | 2026-10-15T09:51:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.1% |
| Market draw away odds | 2.05 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:51:13Z |
| Market reference draw away last update utc | 2026-10-15T09:51:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:51:13Z |
| Market reference home away last update utc | 2026-10-15T09:51:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.25 |
| Market reference dc draw away odds | 1.99 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 80.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.8% |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.82 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 55.8% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:51:13Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **63.4%**. Expected goals are 1.22 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 65.6%; Under 3.5 goals: 56.8%; Double Chance 1X: 36.6%; Double Chance X2: 82.7%; Double Chance 12 (either team wins): 80.7%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 61.6%; BTTS No (at least one team does not score): 38.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.3% | 5.78 |
| Draw | 19.3% | 5.17 |
| Paris Saint Germain win | 63.4% | 1.58 |

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
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.77% |
| 2 | 0-2 | 8.80% |
| 3 | 1-1 | 8.64% |
| 4 | 0-1 | 7.93% |
| 5 | 1-3 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.3% | 13.3% | 6.73 | +16.4% |
| Draw | 19.3% | 17.1% | 5.50 | +6.4% |
| Paris Saint Germain win | 63.4% | 69.6% | 1.46 | -7.5% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| Fair Under 0.5 odds | 27.94 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.78 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
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
| P home draw | 36.6% |
| P draw away | 82.7% |
| P home away | 80.7% |
| Raw p home draw | 42.8% |
| Raw p draw away | 78.7% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 7.00 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.42 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Home probability edge | +4.0% |
| Draw probability edge | +2.2% |
| Away probability edge | -6.2% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | 0.0793 |
| Raw ev home | 0.4309 |
| Raw edge prob draw | 0.0447 |
| Raw ev draw | 0.1872 |
| Raw edge prob away | -0.1240 |
| Raw ev away | -0.1656 |
| Market p home draw | 33.3% |
| Market home draw odds | 2.94 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:51:13Z |
| Market reference home draw last update utc | 2026-10-15T09:51:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.4% |
| Market draw away odds | 1.12 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:51:13Z |
| Market reference draw away last update utc | 2026-10-15T09:51:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.2% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:51:13Z |
| Market reference home away last update utc | 2026-10-15T09:51:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.84 |
| Market reference dc draw away odds | 1.12 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 90.4% |
| Market over 1 5 odds | 1.03 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T09:50:38Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.3% |
| Market under 3 5 odds | 2.06 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T09:50:38Z |
| Market reference under 3 5 odds | 1.95 |
| Market reference under 3 5 opposite odds | 1.90 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.5% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:51:13Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.60 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **62.6%**. Expected goals are 0.64 for Troyes and 2.21 for RC Lens (2.84 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 51.8%; Under 3.5 goals: 70.3%; Double Chance 1X: 37.4%; Double Chance X2: 83.1%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 43.7%; BTTS No (at least one team does not score): 56.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 16.9% | 5.91 |
| Draw | 20.5% | 4.89 |
| RC Lens win | 62.6% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.64 |
| RC Lens expected goals | 2.21 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 51.8% |
| Under 2.5 | 48.2% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.17% |
| 2 | 0-1 | 10.73% |
| 3 | 1-1 | 9.66% |
| 4 | 0-3 | 8.95% |
| 5 | 1-2 | 7.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 16.9% | 25.0% | 4.30 | -27.2% |
| Draw | 20.5% | 22.8% | 4.04 | -17.4% |
| RC Lens win | 62.6% | 52.2% | 1.87 | +17.1% |
| Over 2.5 | 51.8% | 61.6% | 1.64 | -15.1% |
| Under 2.5 | 48.2% | 38.4% | 2.46 | +18.6% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 43.7% |
| P btts no | 56.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.28 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.80 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 8.9% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 73.0% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 42.2% |
| P home draw | 37.4% |
| P draw away | 83.1% |
| P home away | 79.5% |
| Raw p home draw | 27.0% |
| Raw p draw away | 91.1% |
| Raw p home away | 81.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.85 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.88 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -8.0% |
| Draw probability edge | -2.4% |
| Away probability edge | +10.4% |
| Over 2.5 probability edge | -9.8% |
| Under 2.5 probability edge | +9.8% |
| Raw edge prob home | -0.1608 |
| Raw ev home | -0.6179 |
| Raw edge prob draw | -0.0474 |
| Raw ev draw | -0.2694 |
| Raw edge prob away | 0.2082 |
| Raw ev away | 0.3656 |
| Market p home draw | 48.3% |
| Market home draw odds | 2.04 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:51:13Z |
| Market reference home draw last update utc | 2026-10-15T09:51:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.9% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:51:13Z |
| Market reference draw away last update utc | 2026-10-15T09:51:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.9% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:51:13Z |
| Market reference home away last update utc | 2026-10-15T09:51:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.98 |
| Market reference dc draw away odds | 1.26 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T09:49:53Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.0% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T09:49:53Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.49 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:51:13Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **50.3%**. Expected goals are 0.95 for Angers and 1.71 for Marseille (2.66 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 49.2%; Under 3.5 goals: 72.8%; Double Chance 1X: 49.7%; Double Chance X2: 75.3%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 24.7% | 4.05 |
| Draw | 25.0% | 3.99 |
| Marseille win | 50.3% | 1.99 |

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
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.93% |
| 2 | 0-1 | 10.54% |
| 3 | 0-2 | 9.41% |
| 4 | 1-2 | 8.89% |
| 5 | 0-0 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 24.7% | 29.2% | 3.37 | -16.8% |
| Draw | 25.0% | 25.2% | 3.79 | -5.1% |
| Marseille win | 50.3% | 45.6% | 2.20 | +10.6% |
| Over 2.5 | 49.2% | 60.9% | 1.67 | -17.8% |
| Under 2.5 | 50.8% | 39.1% | 2.40 | +21.9% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| Fair Under 0.5 odds | 13.22 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.90 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.68 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.78 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 54.9% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.4% |
| Raw p btts yes | 50.6% |
| P home draw | 49.7% |
| P draw away | 75.3% |
| P home away | 75.0% |
| Raw p home draw | 45.1% |
| Raw p draw away | 79.8% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.30 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.14 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | -4.5% |
| Draw probability edge | -0.2% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -11.7% |
| Under 2.5 probability edge | +11.7% |
| Raw edge prob home | -0.0894 |
| Raw ev home | -0.3182 |
| Raw edge prob draw | -0.0035 |
| Raw ev draw | -0.0576 |
| Raw edge prob away | 0.0929 |
| Raw ev away | 0.2079 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **38.1%**. Expected goals are 1.17 for Le Havre and 1.17 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.6%; Under 3.5 goals: 79.1%; Double Chance 1X: 66.8%; Double Chance X2: 61.9%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 38.1% | 2.63 |
| Draw | 28.8% | 3.48 |
| Auxerre win | 33.2% | 3.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.17 |
| Auxerre expected goals | 1.17 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 68.4% |
| Under 1.5 | 31.6% |
| Over 2.5 | 41.6% |
| Under 2.5 | 58.4% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.54% |
| 2 | 1-0 | 11.48% |
| 3 | 0-1 | 10.04% |
| 4 | 0-0 | 10.03% |
| 5 | 2-1 | 8.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 38.1% | 40.5% | 2.42 | -7.9% |
| Draw | 28.8% | 28.3% | 3.51 | +1.0% |
| Auxerre win | 33.2% | 31.1% | 3.14 | +4.2% |
| Over 2.5 | 41.6% | 51.2% | 1.95 | -18.8% |
| Under 2.5 | 58.4% | 48.8% | 1.99 | +16.1% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| Fair Under 0.5 odds | 9.97 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.40 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.78 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.23 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 35.6% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 68.4% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 48.2% |
| P home draw | 66.8% |
| P draw away | 61.9% |
| P home away | 71.2% |
| Raw p home draw | 64.8% |
| Raw p draw away | 64.4% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.40 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.99 |
| Home probability edge | -2.5% |
| Draw probability edge | +0.5% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | -0.0498 |
| Raw ev home | -0.1394 |
| Raw edge prob draw | 0.0090 |
| Raw ev draw | 0.0254 |
| Raw edge prob away | 0.0408 |
| Raw ev away | 0.1060 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **47.4%**. Expected goals are 1.37 for Lorient and 1.80 for AS Monaco (3.17 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.8%; Under 3.5 goals: 60.9%; Double Chance 1X: 52.6%; Double Chance X2: 73.3%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 78.8%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 26.7% | 3.74 |
| Draw | 25.9% | 3.87 |
| AS Monaco win | 47.4% | 2.11 |

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
| Over 2.5 | 60.8% |
| Under 2.5 | 39.2% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.2% |
| Under 4.5 | 78.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.69% |
| 2 | 1-2 | 9.36% |
| 3 | 0-1 | 7.12% |
| 4 | 2-2 | 6.92% |
| 5 | 0-2 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 26.7% | 24.5% | 3.87 | +3.4% |
| Draw | 25.9% | 27.8% | 3.58 | -7.4% |
| AS Monaco win | 47.4% | 47.6% | 2.10 | -0.4% |
| Over 2.5 | 60.8% | 50.0% | 1.97 | +19.8% |
| Under 2.5 | 39.2% | 50.0% | 1.97 | -22.8% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| Fair Under 0.5 odds | 19.94 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.72 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 28.9% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 47.2% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 62.8% |
| P home draw | 52.6% |
| P draw away | 73.3% |
| P home away | 74.1% |
| Raw p home draw | 52.8% |
| Raw p draw away | 71.1% |
| Raw p home away | 76.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.90 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.05 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.91 |
| Home probability edge | +2.2% |
| Draw probability edge | -2.0% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +10.8% |
| Under 2.5 probability edge | -10.8% |
| Raw edge prob home | 0.0439 |
| Raw ev home | 0.1190 |
| Raw edge prob draw | -0.0396 |
| Raw ev draw | -0.1454 |
| Raw edge prob away | -0.0043 |
| Raw ev away | -0.0085 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **55.5%**. Expected goals are 1.77 for Lyon and 1.09 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 54.8%; Under 3.5 goals: 67.7%; Double Chance 1X: 79.1%; Double Chance X2: 44.5%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 83.7%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 55.5% | 1.80 |
| Draw | 23.6% | 4.23 |
| Nice win | 20.9% | 4.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.77 |
| Nice expected goals | 1.09 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 54.8% |
| Under 2.5 | 45.2% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.3% |
| Under 4.5 | 83.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.18% |
| 2 | 2-1 | 10.25% |
| 3 | 1-0 | 10.15% |
| 4 | 2-0 | 9.43% |
| 5 | 3-1 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 55.5% | 58.0% | 1.71 | -5.2% |
| Draw | 23.6% | 22.9% | 4.21 | -0.6% |
| Nice win | 20.9% | 19.1% | 5.18 | +8.4% |
| Over 2.5 | 54.8% | 59.3% | 1.72 | -5.8% |
| Under 2.5 | 45.2% | 40.7% | 2.31 | +4.5% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| Fair Under 0.5 odds | 16.57 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.65 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.10 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.13 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 52.9% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| P home draw | 79.1% |
| P draw away | 44.5% |
| P home away | 76.4% |
| Raw p home draw | 77.3% |
| Raw p draw away | 47.1% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.70 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -2.5% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.0505 |
| Raw ev home | -0.0949 |
| Raw edge prob draw | 0.0145 |
| Raw ev draw | 0.0248 |
| Raw edge prob away | 0.0359 |
| Raw ev away | 0.1774 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **41.5%**. Expected goals are 1.57 for Paris FC and 1.37 for Rennes (2.94 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 55.7%; Under 3.5 goals: 66.1%; Double Chance 1X: 68.6%; Double Chance X2: 58.5%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 59.9%; BTTS No (at least one team does not score): 40.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 41.5% | 2.41 |
| Draw | 27.1% | 3.69 |
| Rennes win | 31.4% | 3.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.57 |
| Rennes expected goals | 1.37 |
| Expected total goals | 2.94 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 55.7% |
| Under 2.5 | 44.3% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.64% |
| 2 | 2-1 | 8.86% |
| 3 | 1-0 | 7.75% |
| 4 | 1-2 | 7.46% |
| 5 | 2-2 | 6.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 41.5% | 41.1% | 2.37 | -1.7% |
| Draw | 27.1% | 28.8% | 3.45 | -6.5% |
| Rennes win | 31.4% | 30.2% | 3.29 | +3.4% |
| Over 2.5 | 55.7% | 58.5% | 1.72 | -4.1% |
| Under 2.5 | 44.3% | 41.5% | 2.30 | +1.8% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| Fair Under 0.5 odds | 16.23 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.80 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 41.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.1% |
| Raw p btts yes | 59.5% |
| P home draw | 68.6% |
| P draw away | 58.5% |
| P home away | 72.9% |
| Raw p home draw | 67.3% |
| Raw p draw away | 58.1% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.37 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | +0.4% |
| Draw probability edge | -1.7% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | 0.0080 |
| Raw ev home | -0.0072 |
| Raw edge prob draw | -0.0334 |
| Raw ev draw | -0.1229 |
| Raw edge prob away | 0.0254 |
| Raw ev away | 0.0754 |

</details>


---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **43.1%**. Expected goals are 1.56 for Brest and 1.28 for Nice (2.84 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.4%; Double Chance 1X: 69.1%; Double Chance X2: 56.9%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 43.1% | 2.32 |
| Draw | 26.1% | 3.84 |
| Nice win | 30.9% | 3.24 |

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
| Over 2.5 | 53.8% |
| Under 2.5 | 46.2% |
| Over 3.5 | 31.6% |
| Under 3.5 | 68.4% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.29% |
| 2 | 2-1 | 9.03% |
| 3 | 1-0 | 8.57% |
| 4 | 1-2 | 7.49% |
| 5 | 2-0 | 7.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 43.1% | 42.7% | 2.31 | -0.5% |
| Draw | 26.1% | 26.3% | 3.49 | -9.0% |
| Nice win | 30.9% | 31.0% | 3.37 | +4.1% |
| Over 2.5 | 53.8% | 57.4% | 1.76 | -5.3% |
| Under 2.5 | 46.2% | 42.6% | 2.23 | +3.0% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| Fair Under 0.5 odds | 15.56 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.17 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.34 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.5% |
| P home draw | 69.1% |
| P draw away | 56.9% |
| P home away | 73.9% |
| Raw p home draw | 69.2% |
| Raw p draw away | 56.6% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | +0.3% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | 0.0068 |
| Raw ev home | 0.0025 |
| Raw edge prob draw | -0.0046 |
| Raw ev draw | -0.0986 |
| Raw edge prob away | -0.0022 |
| Raw ev away | 0.0370 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **48.7%**. Expected goals are 1.59 for RC Lens and 1.00 for Paris FC (2.58 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 47.9%; Under 3.5 goals: 74.1%; Double Chance 1X: 74.0%; Double Chance X2: 51.3%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 48.7% | 2.05 |
| Draw | 25.4% | 3.94 |
| Paris FC win | 26.0% | 3.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.59 |
| Paris FC expected goals | 1.00 |
| Expected total goals | 2.58 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 73.3% |
| Under 1.5 | 26.7% |
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.08% |
| 2 | 1-0 | 11.03% |
| 3 | 2-0 | 9.14% |
| 4 | 2-1 | 9.13% |
| 5 | 0-1 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 48.7% | 46.8% | 2.09 | +1.7% |
| Draw | 25.4% | 24.5% | 3.90 | -1.1% |
| Paris FC win | 26.0% | 28.6% | 3.58 | -7.0% |
| Over 2.5 | 47.9% | 60.7% | 1.68 | -19.5% |
| Under 2.5 | 52.1% | 39.3% | 2.38 | +23.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | fc6c50376190b578cfeb38c029db8487 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.80 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.75 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.29 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 50.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.3% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.9% |
| Raw p btts yes | 50.7% |
| P home draw | 74.0% |
| P draw away | 51.3% |
| P home away | 74.6% |
| Raw p home draw | 76.7% |
| Raw p draw away | 49.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | +1.8% |
| Draw probability edge | +0.8% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -12.7% |
| Under 2.5 probability edge | +12.7% |
| Raw edge prob home | 0.0367 |
| Raw ev home | 0.0555 |
| Raw edge prob draw | 0.0163 |
| Raw ev draw | 0.0209 |
| Raw edge prob away | -0.0530 |
| Raw ev away | -0.1651 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **66.1%**. Expected goals are 2.29 for Toulouse and 0.62 for Troyes (2.91 combined). The most likely exact score is 2-0 at 12.6%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 53.6%; Under 3.5 goals: 68.4%; Double Chance 1X: 85.8%; Double Chance X2: 33.9%; Double Chance 12 (either team wins): 80.3%; Under 4.5 goals: 84.1%; BTTS Yes (both teams score): 43.5%; BTTS No (at least one team does not score): 56.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 66.1% | 1.51 |
| Draw | 19.7% | 5.06 |
| Troyes win | 14.2% | 7.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 2.29 |
| Troyes expected goals | 0.62 |
| Expected total goals | 2.91 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.6% |
| Under 3.5 | 68.4% |
| Over 4.5 | 15.9% |
| Under 4.5 | 84.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.57% |
| 2 | 1-0 | 10.68% |
| 3 | 3-0 | 9.60% |
| 4 | 1-1 | 9.34% |
| 5 | 2-1 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 66.1% | 57.4% | 1.75 | +15.7% |
| Draw | 19.7% | 22.4% | 4.21 | -16.9% |
| Troyes win | 14.2% | 20.2% | 4.88 | -30.9% |
| Over 2.5 | 53.6% | 59.6% | 1.69 | -9.4% |
| Under 2.5 | 46.4% | 40.4% | 2.36 | +9.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T15:15:00+00:00 |
| Fixture id | 0bbce95e5764e706e6c428bb52dc5536 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 43.5% |
| P btts no | 56.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.04 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.42 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.17 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.27 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 74.8% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 66.6% |
| Raw p btts yes | 42.1% |
| P home draw | 85.8% |
| P draw away | 33.9% |
| P home away | 80.3% |
| Raw p home draw | 91.9% |
| Raw p draw away | 25.2% |
| Raw p home away | 82.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.71 |
| Reference draw odds | 4.25 |
| Reference away odds | 4.70 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +8.7% |
| Draw probability edge | -2.6% |
| Away probability edge | -6.0% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | 0.1734 |
| Raw ev home | 0.3083 |
| Raw edge prob draw | -0.0530 |
| Raw ev draw | -0.2801 |
| Raw edge prob away | -0.1204 |
| Raw ev away | -0.6028 |

</details>


---
