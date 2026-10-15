# Serie A — football model report

Fixtures in this report: **15**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,200 |
| Training data through | 2026-10-12 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 849.586 |
| Base scoring parameter | 0.127 |
| Home-advantage parameter | 0.111 |
| Dixon-Coles low-score adjustment | -0.021 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 15.00 |
| Additional event odds calls used before this league | 17.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-16 — Frosinone vs Sassuolo

The model's most likely 1X2 outcome is **Frosinone win** at **41.8%**. Expected goals are 1.64 for Frosinone and 1.29 for Sassuolo (2.94 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.1%; Under 3.5 goals: 66.3%; Double Chance 1X: 66.7%; Double Chance X2: 58.2%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 58.9%; BTTS No (at least one team does not score): 41.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 41.8% | 2.39 |
| Draw | 24.8% | 4.03 |
| Sassuolo win | 33.3% | 3.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.64 |
| Sassuolo expected goals | 1.29 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 56.1% |
| Under 2.5 | 43.9% |
| Over 3.5 | 33.7% |
| Under 3.5 | 66.3% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.60% |
| 2 | 2-1 | 8.54% |
| 3 | 1-2 | 8.12% |
| 4 | 1-0 | 7.82% |
| 5 | 0-1 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 41.8% | 38.3% | 2.63 | +10.0% |
| Draw | 24.8% | 25.0% | 3.65 | -9.3% |
| Sassuolo win | 33.3% | 36.7% | 2.77 | -7.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-16T18:45:00+00:00 |
| Fixture id | 7d3160040958fe21778fd5ee485666c3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.9% |
| P btts no | 41.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.90 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 2.97 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.78 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 45.4% |
| Unadjusted draw probability | 24.7% |
| Unadjusted away-win probability | 30.0% |
| Raw p over 1 5 | 79.3% |
| Raw p under 3 5 | 66.2% |
| Raw p btts yes | 58.8% |
| P home draw | 66.7% |
| P draw away | 58.2% |
| P home away | 75.2% |
| Raw p home draw | 70.0% |
| Raw p draw away | 54.6% |
| Raw p home away | 75.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.50 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.60 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Home probability edge | +3.6% |
| Draw probability edge | -0.2% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | 0.0711 |
| Raw ev home | 0.1934 |
| Raw edge prob draw | -0.0034 |
| Raw ev draw | -0.0995 |
| Raw edge prob away | -0.0677 |
| Raw ev away | -0.1704 |
| Market p home draw | 63.4% |
| Market home draw odds | 1.50 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:17Z |
| Market reference home draw last update utc | 2026-10-15T06:53:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.7% |
| Market draw away odds | 1.55 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:17Z |
| Market reference draw away last update utc | 2026-10-15T06:53:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.9% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:17Z |
| Market reference home away last update utc | 2026-10-15T06:53:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.50 |
| Market reference dc draw away odds | 1.54 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 87.4% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:57Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 4.95 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.1% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:57Z |
| Market reference under 3 5 odds | 1.76 |
| Market reference under 3 5 opposite odds | 2.24 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.2% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:17Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 3.05 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **68.6%**. Expected goals are 1.97 for AS Roma and 0.64 for Genoa (2.61 combined). The most likely exact score is 2-0 at 14.2%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 48.7%; Under 3.5 goals: 73.4%; Double Chance 1X: 88.2%; Double Chance X2: 31.4%; Double Chance 12 (either team wins): 80.4%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 40.7%; BTTS No (at least one team does not score): 59.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 68.6% | 1.46 |
| Draw | 19.6% | 5.10 |
| Genoa win | 11.8% | 8.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.97 |
| Genoa expected goals | 0.64 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 48.7% |
| Under 2.5 | 51.3% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.24% |
| 2 | 1-0 | 14.23% |
| 3 | 3-0 | 9.37% |
| 4 | 1-1 | 9.11% |
| 5 | 2-1 | 9.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 68.6% | 68.4% | 1.45 | -0.5% |
| Draw | 19.6% | 18.9% | 4.84 | -5.0% |
| Genoa win | 11.8% | 12.7% | 8.30 | -2.3% |
| Over 2.5 | 48.7% | 56.4% | 1.79 | -12.9% |
| Under 2.5 | 51.3% | 43.6% | 2.19 | +12.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | 18d478f469da3bcc654dd4555b85c7e3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 40.7% |
| P btts no | 59.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.77 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.75 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.01 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.8% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 10.9% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 40.9% |
| P home draw | 88.2% |
| P draw away | 31.4% |
| P home away | 80.4% |
| Raw p home draw | 89.1% |
| Raw p draw away | 31.2% |
| Raw p home away | 79.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.43 |
| Reference draw odds | 4.80 |
| Reference away odds | 7.00 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.07 |
| Home probability edge | +0.2% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | 0.0040 |
| Raw ev home | -0.0023 |
| Raw edge prob draw | 0.0141 |
| Raw ev draw | -0.0164 |
| Raw edge prob away | -0.0180 |
| Raw ev away | -0.0975 |
| Market p home draw | 86.6% |
| Market home draw odds | 1.09 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:17Z |
| Market reference home draw last update utc | 2026-10-15T06:53:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.4% |
| Market draw away odds | 2.97 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:17Z |
| Market reference draw away last update utc | 2026-10-15T06:53:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.0% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:17Z |
| Market reference home away last update utc | 2026-10-15T06:53:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.10 |
| Market reference dc draw away odds | 2.85 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 80.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.3% |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.77 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 49.7% |
| Market btts yes odds | 1.93 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:17Z |
| Market reference btts yes odds | 1.99 |
| Market reference btts yes opposite odds | 1.97 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.1%**. Expected goals are 1.08 for Bologna and 2.13 for Inter Milan (3.20 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 61.8%; Under 3.5 goals: 60.2%; Double Chance 1X: 38.9%; Double Chance X2: 82.5%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.5% | 5.70 |
| Draw | 21.4% | 4.68 |
| Inter Milan win | 61.1% | 1.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.08 |
| Inter Milan expected goals | 2.13 |
| Expected total goals | 3.20 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 61.8% |
| Under 2.5 | 38.2% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.87% |
| 2 | 1-1 | 9.83% |
| 3 | 0-2 | 9.18% |
| 4 | 0-1 | 8.44% |
| 5 | 1-3 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.5% | 16.9% | 5.82 | +2.1% |
| Draw | 21.4% | 22.1% | 4.22 | -9.8% |
| Inter Milan win | 61.1% | 61.0% | 1.65 | +0.8% |
| Over 2.5 | 61.8% | 58.9% | 1.71 | +5.7% |
| Under 2.5 | 38.2% | 41.1% | 2.33 | -11.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:00:00+00:00 |
| Fixture id | bfefc309177723410230fee52f650315 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bologna |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.67 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.92 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.62 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.57 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.1% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 61.2% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 60.2% |
| Raw p btts yes | 58.2% |
| P home draw | 38.9% |
| P draw away | 82.5% |
| P home away | 78.6% |
| Raw p home draw | 38.8% |
| Raw p draw away | 81.9% |
| Raw p home away | 79.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 5.40 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | +0.6% |
| Draw probability edge | -0.7% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +2.9% |
| Under 2.5 probability edge | -2.9% |
| Raw edge prob home | 0.0120 |
| Raw ev home | 0.0561 |
| Raw edge prob draw | -0.0143 |
| Raw ev draw | -0.1284 |
| Raw edge prob away | 0.0023 |
| Raw ev away | 0.0098 |
| Market p home draw | 40.4% |
| Market home draw odds | 2.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:17Z |
| Market reference home draw last update utc | 2026-10-15T06:53:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 82.1% |
| Market draw away odds | 1.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:17Z |
| Market reference draw away last update utc | 2026-10-15T06:53:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.5% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:17Z |
| Market reference home away last update utc | 2026-10-15T06:53:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.36 |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 82.0% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.8% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.42 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.8% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:17Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.28 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **65.8%**. Expected goals are 0.67 for Venezia and 2.30 for Napoli (2.96 combined). The most likely exact score is 0-2 at 12.1%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 54.7%; Under 3.5 goals: 67.2%; Double Chance 1X: 34.2%; Double Chance X2: 85.9%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 14.1% | 7.10 |
| Draw | 20.1% | 4.97 |
| Napoli win | 65.8% | 1.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.30 |
| Expected total goals | 2.96 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.1% |
| Under 1.5 | 21.9% |
| Over 2.5 | 54.7% |
| Under 2.5 | 45.3% |
| Over 3.5 | 32.8% |
| Under 3.5 | 67.2% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.11% |
| 2 | 0-1 | 10.40% |
| 3 | 1-1 | 9.56% |
| 4 | 0-3 | 9.26% |
| 5 | 1-2 | 8.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 14.1% | 19.2% | 5.04 | -29.0% |
| Draw | 20.1% | 23.2% | 4.32 | -13.0% |
| Napoli win | 65.8% | 57.6% | 1.71 | +12.5% |
| Over 2.5 | 54.7% | 56.3% | 1.74 | -4.9% |
| Under 2.5 | 45.3% | 43.7% | 2.27 | +2.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:00:00+00:00 |
| Fixture id | 907639dade64cca45d1ab639195d201e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.4% |
| P btts no | 54.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.84 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.57 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.05 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.98 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 9.0% |
| Unadjusted draw probability | 17.0% |
| Unadjusted away-win probability | 74.0% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 43.9% |
| P home draw | 34.2% |
| P draw away | 85.9% |
| P home away | 79.9% |
| Raw p home draw | 26.0% |
| Raw p draw away | 91.0% |
| Raw p home away | 83.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 4.80 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.69 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.06 |
| Home probability edge | -5.1% |
| Draw probability edge | -3.1% |
| Away probability edge | +8.2% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.1020 |
| Raw ev home | -0.5472 |
| Raw edge prob draw | -0.0623 |
| Raw ev draw | -0.2649 |
| Raw edge prob away | 0.1644 |
| Raw ev away | 0.2654 |
| Market p home draw | 43.7% |
| Market home draw odds | 2.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:17Z |
| Market reference home draw last update utc | 2026-10-15T06:53:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.1% |
| Market draw away odds | 1.21 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:17Z |
| Market reference draw away last update utc | 2026-10-15T06:53:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.2% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:17Z |
| Market reference home away last update utc | 2026-10-15T06:53:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.18 |
| Market reference dc draw away odds | 1.19 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 80.4% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.8% |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 55.8% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:17Z |
| Market reference btts yes odds | 1.77 |
| Market reference btts yes opposite odds | 2.22 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **45.9%**. Expected goals are 1.29 for AC Milan and 1.15 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 12.7%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.9%; Double Chance 1X: 72.3%; Double Chance X2: 54.1%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 45.9% | 2.18 |
| Draw | 26.4% | 3.78 |
| Atalanta BC win | 27.7% | 3.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.29 |
| Atalanta BC expected goals | 1.15 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 70.5% |
| Under 1.5 | 29.5% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.74% |
| 2 | 1-1 | 12.53% |
| 3 | 2-1 | 9.69% |
| 4 | 0-0 | 8.53% |
| 5 | 2-0 | 8.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 45.9% | 52.2% | 1.93 | -11.5% |
| Draw | 26.4% | 25.0% | 3.86 | +2.0% |
| Atalanta BC win | 27.7% | 22.8% | 4.22 | +16.9% |
| Over 2.5 | 44.6% | 54.5% | 1.83 | -18.4% |
| Under 2.5 | 55.4% | 45.5% | 2.13 | +18.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T16:00:00+00:00 |
| Fixture id | f9403dd597edbfaa73abdc974e55344c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.72 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.32 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.73 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.8% |
| P home draw | 72.3% |
| P draw away | 54.1% |
| P home away | 73.6% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.5% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.86 |
| Reference draw odds | 3.75 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 1.99 |
| Home probability edge | -6.3% |
| Draw probability edge | +1.4% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | -0.1266 |
| Raw ev home | -0.2372 |
| Raw edge prob draw | 0.0282 |
| Raw ev draw | 0.0750 |
| Raw edge prob away | 0.0984 |
| Raw ev away | 0.3769 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.4%**. Expected goals are 0.96 for Fiorentina and 1.71 for Como (2.67 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.6%; Double Chance 1X: 49.6%; Double Chance X2: 75.5%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.5% | 4.08 |
| Draw | 25.1% | 3.99 |
| Como win | 50.4% | 1.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 0.96 |
| Como expected goals | 1.71 |
| Expected total goals | 2.67 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.3% |
| Under 1.5 | 25.7% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 27.4% |
| Under 3.5 | 72.6% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.93% |
| 2 | 0-1 | 10.72% |
| 3 | 0-2 | 9.34% |
| 4 | 1-2 | 8.95% |
| 5 | 1-0 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.5% | 28.1% | 3.54 | -13.3% |
| Draw | 25.1% | 25.7% | 3.81 | -4.5% |
| Como win | 50.4% | 46.2% | 2.12 | +6.9% |
| Over 2.5 | 49.3% | 57.9% | 1.73 | -14.7% |
| Under 2.5 | 50.7% | 42.1% | 2.29 | +16.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 3ea32a0aa44a5f0ef7fd088155430087 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.53 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.90 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.71 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 50.7% |
| P home draw | 49.6% |
| P draw away | 75.5% |
| P home away | 74.9% |
| Raw p home draw | 45.3% |
| Raw p draw away | 79.1% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.35 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.09 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.13 |
| Home probability edge | -3.6% |
| Draw probability edge | -0.6% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -8.6% |
| Under 2.5 probability edge | +8.6% |
| Raw edge prob home | -0.0728 |
| Raw ev home | -0.2616 |
| Raw edge prob draw | -0.0130 |
| Raw ev draw | -0.0697 |
| Raw edge prob away | 0.0857 |
| Raw ev away | 0.1601 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **53.0%**. Expected goals are 1.37 for Juventus and 0.87 for Lazio (2.23 combined). The most likely exact score is 1-0 at 15.8%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 39.5%; Under 3.5 goals: 81.0%; Double Chance 1X: 79.1%; Double Chance X2: 47.0%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.9%; BTTS No (at least one team does not score): 57.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 53.0% | 1.89 |
| Draw | 26.1% | 3.83 |
| Lazio win | 20.9% | 4.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.87 |
| Expected total goals | 2.23 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 39.5% |
| Under 2.5 | 60.5% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.79% |
| 2 | 1-1 | 11.99% |
| 3 | 2-0 | 11.00% |
| 4 | 0-0 | 10.16% |
| 5 | 2-1 | 9.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 53.0% | 57.8% | 1.69 | -10.4% |
| Draw | 26.1% | 24.0% | 4.04 | +5.5% |
| Lazio win | 20.9% | 18.2% | 5.71 | +19.1% |
| Over 2.5 | 39.5% | 49.5% | 2.03 | -19.8% |
| Under 2.5 | 60.5% | 50.5% | 1.92 | +16.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T18:45:00+00:00 |
| Fixture id | 4c4026e2782f09d6f0ff2bde2a390513 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Juventus |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.9% |
| P btts no | 57.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.85 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.71 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 43.5% |
| P home draw | 79.1% |
| P draw away | 47.0% |
| P home away | 73.9% |
| Raw p home draw | 76.5% |
| Raw p draw away | 51.7% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.68 |
| Reference draw odds | 3.85 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | -4.7% |
| Draw probability edge | +2.1% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | -0.0950 |
| Raw ev home | -0.1843 |
| Raw edge prob draw | 0.0421 |
| Raw ev draw | 0.1404 |
| Raw edge prob away | 0.0529 |
| Raw ev away | 0.3424 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.4%**. Expected goals are 1.46 for Udinese and 0.83 for Lecce (2.29 combined). The most likely exact score is 1-0 at 14.4%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.2%; Double Chance 1X: 78.4%; Double Chance X2: 48.6%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 43.6%; BTTS No (at least one team does not score): 56.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.4% | 1.95 |
| Draw | 27.0% | 3.71 |
| Lecce win | 21.6% | 4.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.46 |
| Lecce expected goals | 0.83 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.7% |
| Under 0.5 | 10.3% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.2% |
| Under 2.5 | 59.8% |
| Over 3.5 | 19.8% |
| Under 3.5 | 80.2% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.45% |
| 2 | 1-1 | 12.44% |
| 3 | 2-0 | 10.71% |
| 4 | 0-0 | 10.30% |
| 5 | 2-1 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.4% | 51.2% | 1.95 | +0.2% |
| Draw | 27.0% | 26.8% | 3.65 | -1.5% |
| Lecce win | 21.6% | 22.1% | 4.38 | -5.2% |
| Over 2.5 | 40.2% | 46.9% | 2.08 | -16.4% |
| Under 2.5 | 59.8% | 53.1% | 1.87 | +11.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T10:30:00+00:00 |
| Fixture id | 367da93aa21a1e13eeafb94fd2263c75 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 43.6% |
| P btts no | 56.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.70 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.04 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.11 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 43.6% |
| P home draw | 78.4% |
| P draw away | 48.6% |
| P home away | 73.0% |
| Raw p home draw | 78.8% |
| Raw p draw away | 48.4% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.89 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.20 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.94 |
| Reference Under 2.5 odds | 1.74 |
| Home probability edge | +0.2% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -6.7% |
| Under 2.5 probability edge | +6.7% |
| Raw edge prob home | 0.0041 |
| Raw ev home | 0.0058 |
| Raw edge prob draw | 0.0046 |
| Raw ev draw | -0.0069 |
| Raw edge prob away | -0.0087 |
| Raw ev away | -0.0709 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.3%**. Expected goals are 1.13 for Monza and 1.62 for Cagliari (2.75 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 50.7%; Under 3.5 goals: 70.9%; Double Chance 1X: 60.7%; Double Chance X2: 66.7%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 33.3% | 3.00 |
| Draw | 27.4% | 3.65 |
| Cagliari win | 39.3% | 2.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.13 |
| Cagliari expected goals | 1.62 |
| Expected total goals | 2.75 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 75.7% |
| Under 1.5 | 24.3% |
| Over 2.5 | 50.7% |
| Under 2.5 | 49.3% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.02% |
| 2 | 1-0 | 8.83% |
| 3 | 2-1 | 8.36% |
| 4 | 0-1 | 8.20% |
| 5 | 1-2 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.3% | 40.2% | 2.49 | -17.0% |
| Draw | 27.4% | 29.6% | 3.25 | -10.9% |
| Cagliari win | 39.3% | 30.1% | 3.25 | +27.6% |
| Over 2.5 | 50.7% | 45.1% | 2.15 | +9.1% |
| Under 2.5 | 49.3% | 54.9% | 1.82 | -10.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T16:30:00+00:00 |
| Fixture id | ce94aca384a20f6af459366da6e1dd21 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.3% |
| P btts no | 44.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.81 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.17 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 26.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.3% |
| Raw p btts yes | 54.5% |
| P home draw | 60.7% |
| P draw away | 66.7% |
| P home away | 72.6% |
| Raw p home draw | 51.6% |
| Raw p draw away | 73.6% |
| Raw p home away | 74.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.39 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 2.01 |
| Reference Under 2.5 odds | 1.69 |
| Home probability edge | -6.9% |
| Draw probability edge | -2.2% |
| Away probability edge | +9.1% |
| Over 2.5 probability edge | +5.7% |
| Under 2.5 probability edge | -5.7% |
| Raw edge prob home | -0.1381 |
| Raw ev home | -0.3425 |
| Raw edge prob draw | -0.0445 |
| Raw ev draw | -0.1812 |
| Raw edge prob away | 0.1826 |
| Raw ev away | 0.5730 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **37.8%**. Expected goals are 1.00 for Parma and 1.10 for Torino (2.11 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 87.5%; Over 2.5 goals: 35.2%; Under 3.5 goals: 83.7%; Double Chance 1X: 62.2%; Double Chance X2: 68.3%; Double Chance 12 (either team wins): 69.5%; Under 4.5 goals: 93.7%; BTTS Yes (both teams score): 42.6%; BTTS No (at least one team does not score): 57.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.7% | 3.16 |
| Draw | 30.5% | 3.28 |
| Torino win | 37.8% | 2.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.00 |
| Torino expected goals | 1.10 |
| Expected total goals | 2.11 |
| Over 0.5 | 87.5% |
| Under 0.5 | 12.5% |
| Over 1.5 | 62.5% |
| Under 1.5 | 37.5% |
| Over 2.5 | 35.2% |
| Under 2.5 | 64.8% |
| Over 3.5 | 16.3% |
| Under 3.5 | 83.7% |
| Over 4.5 | 6.3% |
| Under 4.5 | 93.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.79% |
| 2 | 0-1 | 13.31% |
| 3 | 0-0 | 12.48% |
| 4 | 1-0 | 11.71% |
| 5 | 1-2 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.7% | 31.1% | 3.25 | +2.9% |
| Draw | 30.5% | 30.6% | 3.17 | -3.3% |
| Torino win | 37.8% | 38.3% | 2.54 | -3.9% |
| Over 2.5 | 35.2% | 39.1% | 2.48 | -12.7% |
| Under 2.5 | 64.8% | 60.9% | 1.63 | +5.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T18:45:00+00:00 |
| Fixture id | 07014d9adc65ca39710bd9f0c7c0d3f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.6% |
| P btts no | 57.4% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.01 |
| Fair Over 1.5 odds | 1.60 |
| Fair Under 1.5 odds | 2.67 |
| Fair Over 2.5 odds | 2.84 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.15 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 15.94 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.2% |
| Unadjusted draw probability | 30.4% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 62.5% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 42.6% |
| P home draw | 62.2% |
| P draw away | 68.3% |
| P home away | 69.5% |
| Raw p home draw | 62.6% |
| Raw p draw away | 67.8% |
| Raw p home away | 69.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.05 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 2.27 |
| Reference Under 2.5 odds | 1.54 |
| Home probability edge | +0.6% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | 0.0112 |
| Raw ev home | 0.0475 |
| Raw edge prob draw | -0.0017 |
| Raw ev draw | -0.0358 |
| Raw edge prob away | -0.0096 |
| Raw ev away | -0.0513 |

</details>


---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **50.7%**. Expected goals are 1.94 for Torino and 1.18 for Monza (3.12 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 59.4%; Under 3.5 goals: 62.4%; Double Chance 1X: 75.3%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 79.9%; BTTS Yes (both teams score): 60.2%; BTTS No (at least one team does not score): 39.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 50.7% | 1.97 |
| Draw | 24.7% | 4.06 |
| Monza win | 24.7% | 4.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.94 |
| Monza expected goals | 1.18 |
| Expected total goals | 3.12 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 37.6% |
| Under 3.5 | 62.4% |
| Over 4.5 | 20.1% |
| Under 4.5 | 79.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.34% |
| 2 | 2-1 | 9.04% |
| 3 | 1-0 | 7.69% |
| 4 | 2-0 | 7.67% |
| 5 | 1-2 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 50.7% | 46.3% | 2.15 | +8.9% |
| Draw | 24.7% | 26.9% | 3.62 | -10.8% |
| Monza win | 24.7% | 26.7% | 3.64 | -10.2% |
| Over 2.5 | 59.4% | 46.5% | 2.11 | +25.4% |
| Under 2.5 | 40.6% | 53.5% | 1.85 | -25.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 124c70f8f3248a845bdb983a54e74720 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.2% |
| P btts no | 39.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.68 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.49 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.66 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.98 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 55.0% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 82.1% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 59.5% |
| P home draw | 75.3% |
| P draw away | 49.3% |
| P home away | 75.3% |
| Raw p home draw | 77.4% |
| Raw p draw away | 45.0% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.09 |
| Reference draw odds | 3.52 |
| Reference away odds | 3.54 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +4.3% |
| Draw probability edge | -2.3% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | +13.0% |
| Under 2.5 probability edge | -13.0% |
| Raw edge prob home | 0.0865 |
| Raw ev home | 0.1825 |
| Raw edge prob draw | -0.0451 |
| Raw ev draw | -0.1892 |
| Raw edge prob away | -0.0414 |
| Raw ev away | -0.1773 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **38.7%**. Expected goals are 1.07 for Cagliari and 1.18 for Bologna (2.25 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 38.8%; Under 3.5 goals: 80.9%; Double Chance 1X: 61.3%; Double Chance X2: 69.0%; Double Chance 12 (either team wins): 69.7%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 46.1%; BTTS No (at least one team does not score): 53.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 31.0% | 3.23 |
| Draw | 30.3% | 3.30 |
| Bologna win | 38.7% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.07 |
| Bologna expected goals | 1.18 |
| Expected total goals | 2.25 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 38.8% |
| Under 2.5 | 61.2% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.08% |
| 2 | 0-1 | 12.33% |
| 3 | 0-0 | 11.18% |
| 4 | 1-0 | 10.41% |
| 5 | 1-2 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 31.0% | 29.2% | 3.35 | +3.9% |
| Draw | 30.3% | 31.3% | 3.13 | -5.2% |
| Bologna win | 38.7% | 39.4% | 2.52 | -2.5% |
| Over 2.5 | 38.8% | 43.5% | 2.24 | -13.0% |
| Under 2.5 | 61.2% | 56.5% | 1.76 | +7.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | b7f0880e3da978f9481f7cb5697e2aa5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 46.1% |
| P btts no | 53.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.95 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.58 |
| Fair Under 2.5 odds | 1.63 |
| Fair Over 3.5 odds | 5.24 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.89 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 38.0% |
| Raw p over 1 5 | 66.1% |
| Raw p under 3 5 | 80.9% |
| Raw p btts yes | 45.9% |
| P home draw | 61.3% |
| P draw away | 69.0% |
| P home away | 69.7% |
| Raw p home draw | 62.0% |
| Raw p draw away | 67.2% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.25 |
| Reference draw odds | 3.04 |
| Reference away odds | 2.44 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.17 |
| Reference Under 2.5 odds | 1.70 |
| Home probability edge | +1.8% |
| Draw probability edge | -1.1% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | 0.0355 |
| Raw ev home | 0.0982 |
| Raw edge prob draw | -0.0211 |
| Raw ev draw | -0.0851 |
| Raw edge prob away | -0.0143 |
| Raw ev away | -0.0426 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **64.8%**. Expected goals are 1.96 for Como and 0.91 for Sassuolo (2.87 combined). The most likely exact score is 1-0 at 11.5%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 55.3%; Under 3.5 goals: 67.3%; Double Chance 1X: 85.2%; Double Chance X2: 35.2%; Double Chance 12 (either team wins): 79.6%; Under 4.5 goals: 83.4%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 64.8% | 1.54 |
| Draw | 20.4% | 4.90 |
| Sassuolo win | 14.8% | 6.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 1.96 |
| Sassuolo expected goals | 0.91 |
| Expected total goals | 2.87 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 55.3% |
| Under 2.5 | 44.7% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.50% |
| 2 | 2-0 | 11.47% |
| 3 | 2-1 | 10.42% |
| 4 | 1-1 | 9.70% |
| 5 | 3-0 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 64.8% | 68.0% | 1.49 | -3.4% |
| Draw | 20.4% | 19.0% | 4.94 | +0.7% |
| Sassuolo win | 14.8% | 13.0% | 7.10 | +5.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | 08ffd99b2249c81d8a7410598f32b9b0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.05 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.66 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.03 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 61.6% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 16.6% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 51.5% |
| P home draw | 85.2% |
| P draw away | 35.2% |
| P home away | 79.6% |
| Raw p home draw | 83.4% |
| Raw p draw away | 38.4% |
| Raw p home away | 78.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.44 |
| Reference draw odds | 4.80 |
| Reference away odds | 6.90 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.65 |
| Home probability edge | -3.2% |
| Draw probability edge | +1.4% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -9.8% |
| Under 2.5 probability edge | +9.8% |
| Raw edge prob home | -0.0635 |
| Raw ev home | -0.0814 |
| Raw edge prob draw | 0.0271 |
| Raw ev draw | 0.0743 |
| Raw edge prob away | 0.0364 |
| Raw ev away | 0.1789 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **58.7%**. Expected goals are 1.36 for Lazio and 0.66 for Parma (2.02 combined). The most likely exact score is 1-0 at 19.5%. Goal-market probabilities: at least one goal: 88.0%; Over 2.5 goals: 34.1%; Under 3.5 goals: 84.9%; Double Chance 1X: 84.1%; Double Chance X2: 41.3%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 94.3%; BTTS Yes (both teams score): 35.3%; BTTS No (at least one team does not score): 64.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 58.7% | 1.70 |
| Draw | 25.3% | 3.95 |
| Parma win | 15.9% | 6.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.36 |
| Parma expected goals | 0.66 |
| Expected total goals | 2.02 |
| Over 0.5 | 88.0% |
| Under 0.5 | 12.0% |
| Over 1.5 | 60.9% |
| Under 1.5 | 39.1% |
| Over 2.5 | 34.1% |
| Under 2.5 | 65.9% |
| Over 3.5 | 15.1% |
| Under 3.5 | 84.9% |
| Over 4.5 | 5.7% |
| Under 4.5 | 94.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.51% |
| 2 | 2-0 | 13.46% |
| 3 | 0-0 | 11.96% |
| 4 | 1-1 | 10.76% |
| 5 | 2-1 | 8.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 58.7% | 63.9% | 1.58 | -7.2% |
| Draw | 25.3% | 22.1% | 4.33 | +9.7% |
| Parma win | 15.9% | 14.0% | 6.64 | +5.9% |
| Over 2.5 | 34.1% | 47.8% | 2.06 | -29.7% |
| Under 2.5 | 65.9% | 52.2% | 1.89 | +24.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | b27cb3ea731fa3f18d05e6a627bdf984 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 35.3% |
| P btts no | 64.7% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.36 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.56 |
| Fair Over 2.5 odds | 2.93 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.64 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 17.45 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 53.5% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 17.9% |
| Raw p over 1 5 | 60.2% |
| Raw p under 3 5 | 85.3% |
| Raw p btts yes | 36.2% |
| P home draw | 84.1% |
| P draw away | 41.3% |
| P home away | 74.7% |
| Raw p home draw | 82.1% |
| Raw p draw away | 46.5% |
| Raw p home away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.53 |
| Reference draw odds | 4.20 |
| Reference away odds | 6.45 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | -5.2% |
| Draw probability edge | +3.3% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -13.6% |
| Under 2.5 probability edge | +13.6% |
| Raw edge prob home | -0.1038 |
| Raw ev home | -0.1544 |
| Raw edge prob draw | 0.0656 |
| Raw ev draw | 0.2394 |
| Raw edge prob away | 0.0381 |
| Raw ev away | 0.1856 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **39.7%**. Expected goals are 1.04 for Napoli and 1.19 for AS Roma (2.23 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 38.8%; Under 3.5 goals: 81.3%; Double Chance 1X: 60.3%; Double Chance X2: 67.9%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 45.0%; BTTS No (at least one team does not score): 55.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 32.1% | 3.12 |
| Draw | 28.2% | 3.54 |
| AS Roma win | 39.7% | 2.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.04 |
| AS Roma expected goals | 1.19 |
| Expected total goals | 2.23 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 65.6% |
| Under 1.5 | 34.4% |
| Over 2.5 | 38.8% |
| Under 2.5 | 61.2% |
| Over 3.5 | 18.7% |
| Under 3.5 | 81.3% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.07% |
| 2 | 0-1 | 12.75% |
| 3 | 1-0 | 11.06% |
| 4 | 0-0 | 10.63% |
| 5 | 1-2 | 8.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 32.1% | 32.4% | 3.04 | -2.5% |
| Draw | 28.2% | 27.1% | 3.60 | +1.7% |
| AS Roma win | 39.7% | 40.5% | 2.45 | -2.7% |
| Over 2.5 | 38.8% | 51.0% | 1.93 | -25.0% |
| Under 2.5 | 61.2% | 49.0% | 2.01 | +22.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:00:00+00:00 |
| Fixture id | 0b4894e9fb123ef3045269f97e339eba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:17Z |
| Market best draw last update utc | 2026-10-15T06:53:17Z |
| Market best away last update utc | 2026-10-15T06:53:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 45.0% |
| P btts no | 55.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.41 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.90 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.36 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.08 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 31.7% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.4% |
| Raw p btts yes | 45.2% |
| P home draw | 60.3% |
| P draw away | 67.9% |
| P home away | 71.8% |
| Raw p home draw | 61.1% |
| Raw p draw away | 68.3% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.95 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.38 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.94 |
| Home probability edge | -0.3% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -12.1% |
| Under 2.5 probability edge | +12.1% |
| Raw edge prob home | -0.0065 |
| Raw ev home | -0.0353 |
| Raw edge prob draw | 0.0227 |
| Raw ev draw | 0.0576 |
| Raw edge prob away | -0.0162 |
| Raw ev away | -0.0472 |

</details>


---
