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
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
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

The model's most likely 1X2 outcome is **Frosinone win** at **42.1%**. Expected goals are 1.64 for Frosinone and 1.29 for Sassuolo (2.94 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.3%; Double Chance 1X: 67.6%; Double Chance X2: 57.9%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 42.1% | 2.37 |
| Draw | 25.5% | 3.92 |
| Sassuolo win | 32.4% | 3.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.64 |
| Sassuolo expected goals | 1.29 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.7% |
| Under 3.5 | 66.3% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.90% |
| 2 | 2-1 | 8.60% |
| 3 | 1-2 | 7.88% |
| 4 | 1-0 | 7.88% |
| 5 | 0-1 | 7.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 42.1% | 38.9% | 2.63 | +10.8% |
| Draw | 25.5% | 26.3% | 3.65 | -7.0% |
| Sassuolo win | 32.4% | 34.8% | 2.77 | -10.3% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.44 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.97 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.81 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 45.4% |
| Unadjusted draw probability | 24.7% |
| Unadjusted away-win probability | 30.0% |
| Raw p over 1 5 | 79.3% |
| Raw p under 3 5 | 66.2% |
| Raw p btts yes | 58.8% |
| P home draw | 67.6% |
| P draw away | 57.9% |
| Raw p home draw | 70.0% |
| Raw p draw away | 54.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.35 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.60 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | +3.2% |
| Draw probability edge | -0.8% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | 0.0647 |
| Raw ev home | 0.1934 |
| Raw edge prob draw | -0.0163 |
| Raw ev draw | -0.0995 |
| Raw edge prob away | -0.0484 |
| Raw ev away | -0.1704 |
| Market p home draw | 63.6% |
| Market home draw odds | 1.50 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T21:06:46Z |
| Market reference home draw last update utc | 2026-10-14T21:07:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.9% |
| Market draw away odds | 1.55 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T21:06:46Z |
| Market reference draw away last update utc | 2026-10-14T21:07:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.49 |
| Market reference dc draw away odds | 1.53 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 85.4% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T21:06:48Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 6.10 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.0% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T21:06:48Z |
| Market reference under 3 5 odds | 1.74 |
| Market reference under 3 5 opposite odds | 2.19 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T21:06:46Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 3.10 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **70.6%**. Expected goals are 1.97 for AS Roma and 0.64 for Genoa (2.61 combined). The most likely exact score is 2-0 at 14.7%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 49.1%; Under 3.5 goals: 73.0%; Double Chance 1X: 89.7%; Double Chance X2: 29.4%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 40.5%; BTTS No (at least one team does not score): 59.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 70.6% | 1.42 |
| Draw | 19.1% | 5.23 |
| Genoa win | 10.3% | 9.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.97 |
| Genoa expected goals | 0.64 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 74.0% |
| Under 1.5 | 26.0% |
| Over 2.5 | 49.1% |
| Under 2.5 | 50.9% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.66% |
| 2 | 1-0 | 14.65% |
| 3 | 3-0 | 9.65% |
| 4 | 2-1 | 9.37% |
| 5 | 1-1 | 8.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 70.6% | 72.4% | 1.45 | +2.4% |
| Draw | 19.1% | 17.9% | 4.84 | -7.5% |
| Genoa win | 10.3% | 9.6% | 8.30 | -14.9% |
| Over 2.5 | 49.1% | 55.7% | 1.79 | -12.1% |
| Under 2.5 | 50.9% | 44.3% | 2.19 | +11.5% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 40.5% |
| P btts no | 59.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.13 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.85 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.71 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.90 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.8% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 10.9% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 40.9% |
| P home draw | 89.7% |
| P draw away | 29.4% |
| Raw p home draw | 89.1% |
| Raw p draw away | 31.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.32 |
| Reference draw odds | 4.40 |
| Reference away odds | 7.50 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | -1.8% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -6.7% |
| Under 2.5 probability edge | +6.7% |
| Raw edge prob home | -0.0364 |
| Raw ev home | -0.0023 |
| Raw edge prob draw | 0.0241 |
| Raw ev draw | -0.0164 |
| Raw edge prob away | 0.0123 |
| Raw ev away | -0.0975 |
| Market p home draw | 85.9% |
| Market home draw odds | 1.09 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T21:06:46Z |
| Market reference home draw last update utc | 2026-10-14T21:07:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.7% |
| Market draw away odds | 2.97 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T21:06:46Z |
| Market reference draw away last update utc | 2026-10-14T21:07:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.11 |
| Market reference dc draw away odds | 2.75 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 79.6% |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.2% |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.80 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 49.6% |
| Market btts yes odds | 1.93 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T21:06:46Z |
| Market reference btts yes odds | 1.98 |
| Market reference btts yes opposite odds | 1.95 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.1%**. Expected goals are 1.08 for Bologna and 2.13 for Inter Milan (3.20 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 61.8%; Under 3.5 goals: 60.2%; Double Chance 1X: 38.9%; Double Chance X2: 82.6%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.4% | 5.74 |
| Draw | 21.4% | 4.66 |
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
| 1 | 1-2 | 9.88% |
| 2 | 1-1 | 9.87% |
| 3 | 0-2 | 9.18% |
| 4 | 0-1 | 8.44% |
| 5 | 1-3 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.4% | 16.7% | 5.82 | +1.4% |
| Draw | 21.4% | 22.2% | 4.22 | -9.5% |
| Inter Milan win | 61.1% | 61.1% | 1.65 | +0.9% |
| Over 2.5 | 61.8% | 57.6% | 1.71 | +5.7% |
| Under 2.5 | 38.2% | 42.4% | 2.33 | -11.0% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| Fair Under 0.5 odds | 22.58 |
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
| P draw away | 82.6% |
| Raw p home draw | 38.8% |
| Raw p draw away | 81.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 4.90 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.55 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.02 |
| Home probability edge | +0.7% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +4.2% |
| Under 2.5 probability edge | -4.2% |
| Raw edge prob home | 0.0144 |
| Raw ev home | 0.0561 |
| Raw edge prob draw | -0.0159 |
| Raw ev draw | -0.1284 |
| Raw edge prob away | 0.0015 |
| Raw ev away | 0.0098 |
| Market p home draw | 40.2% |
| Market home draw odds | 2.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T21:06:46Z |
| Market reference home draw last update utc | 2026-10-14T21:07:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 82.6% |
| Market draw away odds | 1.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T21:06:46Z |
| Market reference draw away last update utc | 2026-10-14T21:07:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.36 |
| Market reference dc draw away odds | 1.15 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 81.0% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T21:05:59Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T21:05:59Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.3% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T21:06:46Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.24 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **67.3%**. Expected goals are 0.67 for Venezia and 2.30 for Napoli (2.96 combined). The most likely exact score is 0-2 at 12.4%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 55.1%; Under 3.5 goals: 66.9%; Double Chance 1X: 32.7%; Double Chance X2: 86.6%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 45.1%; BTTS No (at least one team does not score): 54.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 13.4% | 7.44 |
| Draw | 19.3% | 5.19 |
| Napoli win | 67.3% | 1.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.30 |
| Expected total goals | 2.96 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.38% |
| 2 | 0-1 | 10.64% |
| 3 | 0-3 | 9.47% |
| 4 | 1-1 | 9.16% |
| 5 | 1-2 | 8.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 13.4% | 17.9% | 5.04 | -32.3% |
| Draw | 19.3% | 21.5% | 4.32 | -16.7% |
| Napoli win | 67.3% | 60.6% | 1.71 | +15.1% |
| Over 2.5 | 55.1% | 59.0% | 1.74 | -4.0% |
| Under 2.5 | 44.9% | 41.0% | 2.27 | +1.8% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| P btts yes | 45.1% |
| P btts no | 54.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.54 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.63 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.90 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 9.0% |
| Unadjusted draw probability | 17.0% |
| Unadjusted away-win probability | 74.0% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 43.9% |
| P home draw | 32.7% |
| P draw away | 86.6% |
| Raw p home draw | 26.0% |
| Raw p draw away | 91.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 4.60 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.56 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -4.5% |
| Draw probability edge | -2.3% |
| Away probability edge | +6.7% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0890 |
| Raw ev home | -0.5472 |
| Raw edge prob draw | -0.0453 |
| Raw ev draw | -0.2649 |
| Raw edge prob away | 0.1344 |
| Raw ev away | 0.2654 |
| Market p home draw | 43.7% |
| Market home draw odds | 2.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T21:06:46Z |
| Market reference home draw last update utc | 2026-10-14T21:07:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.1% |
| Market draw away odds | 1.21 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T21:06:46Z |
| Market reference draw away last update utc | 2026-10-14T21:07:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.18 |
| Market reference dc draw away odds | 1.19 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.4% |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 55.8% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T21:06:46Z |
| Market reference btts yes odds | 1.77 |
| Market reference btts yes opposite odds | 2.22 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **47.0%**. Expected goals are 1.29 for AC Milan and 1.15 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 44.7%; Under 3.5 goals: 76.9%; Double Chance 1X: 73.1%; Double Chance X2: 53.0%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 49.3%; BTTS No (at least one team does not score): 50.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 47.0% | 2.13 |
| Draw | 26.2% | 3.82 |
| Atalanta BC win | 26.9% | 3.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.29 |
| Atalanta BC expected goals | 1.15 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 70.5% |
| Under 1.5 | 29.5% |
| Over 2.5 | 44.7% |
| Under 2.5 | 55.3% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.05% |
| 2 | 1-1 | 12.41% |
| 3 | 2-1 | 9.92% |
| 4 | 2-0 | 8.64% |
| 5 | 0-0 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 47.0% | 54.4% | 1.93 | -9.4% |
| Draw | 26.2% | 24.5% | 3.86 | +1.0% |
| Atalanta BC win | 26.9% | 21.1% | 4.22 | +13.4% |
| Over 2.5 | 44.7% | 55.9% | 1.83 | -18.2% |
| Under 2.5 | 55.3% | 44.1% | 2.13 | +17.8% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| P btts yes | 49.3% |
| P btts no | 50.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.84 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.32 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.70 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.8% |
| P home draw | 73.1% |
| P draw away | 53.0% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.72 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.00 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | -7.4% |
| Draw probability edge | +1.7% |
| Away probability edge | +5.8% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | -0.1488 |
| Raw ev home | -0.2372 |
| Raw edge prob draw | 0.0334 |
| Raw ev draw | 0.0750 |
| Raw edge prob away | 0.1154 |
| Raw ev away | 0.3769 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **51.8%**. Expected goals are 0.96 for Fiorentina and 1.71 for Como (2.67 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 49.5%; Under 3.5 goals: 72.4%; Double Chance 1X: 48.2%; Double Chance X2: 76.5%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 23.5% | 4.25 |
| Draw | 24.7% | 4.06 |
| Como win | 51.8% | 1.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 0.96 |
| Como expected goals | 1.71 |
| Expected total goals | 2.67 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 74.5% |
| Under 1.5 | 25.5% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.74% |
| 2 | 0-1 | 11.02% |
| 3 | 0-2 | 9.60% |
| 4 | 1-2 | 9.20% |
| 5 | 0-0 | 7.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 23.5% | 26.2% | 3.54 | -16.8% |
| Draw | 24.7% | 24.9% | 3.81 | -6.1% |
| Como win | 51.8% | 48.9% | 2.12 | +9.9% |
| Over 2.5 | 49.5% | 57.9% | 1.73 | -14.3% |
| Under 2.5 | 50.5% | 42.1% | 2.29 | +15.6% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.76 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.92 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.63 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.66 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 50.7% |
| P home draw | 48.2% |
| P draw away | 76.5% |
| Raw p home draw | 45.3% |
| Raw p draw away | 79.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.45 |
| Reference away odds | 1.89 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.04 |
| Home probability edge | -2.7% |
| Draw probability edge | -0.2% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | -8.3% |
| Under 2.5 probability edge | +8.3% |
| Raw edge prob home | -0.0531 |
| Raw ev home | -0.2616 |
| Raw edge prob draw | -0.0048 |
| Raw ev draw | -0.0697 |
| Raw edge prob away | 0.0579 |
| Raw ev away | 0.1601 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **53.5%**. Expected goals are 1.37 for Juventus and 0.87 for Lazio (2.23 combined). The most likely exact score is 1-0 at 15.9%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 39.5%; Under 3.5 goals: 80.9%; Double Chance 1X: 79.8%; Double Chance X2: 46.5%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.9%; BTTS No (at least one team does not score): 57.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 53.5% | 1.87 |
| Draw | 26.2% | 3.81 |
| Lazio win | 20.2% | 4.94 |

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
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.94% |
| 2 | 1-1 | 12.05% |
| 3 | 2-0 | 11.10% |
| 4 | 0-0 | 10.20% |
| 5 | 2-1 | 9.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 53.5% | 58.8% | 1.69 | -9.6% |
| Draw | 26.2% | 24.3% | 4.04 | +6.0% |
| Lazio win | 20.2% | 17.0% | 5.71 | +15.6% |
| Over 2.5 | 39.5% | 48.6% | 2.03 | -19.8% |
| Under 2.5 | 60.5% | 51.4% | 1.92 | +16.2% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| Fair Under 0.5 odds | 9.80 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.24 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.70 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 43.5% |
| P home draw | 79.8% |
| P draw away | 46.5% |
| Raw p home draw | 76.5% |
| Raw p draw away | 51.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.60 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.74 |
| Home probability edge | -5.3% |
| Draw probability edge | +2.0% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | -9.2% |
| Under 2.5 probability edge | +9.2% |
| Raw edge prob home | -0.1051 |
| Raw ev home | -0.1843 |
| Raw edge prob draw | 0.0397 |
| Raw ev draw | 0.1404 |
| Raw edge prob away | 0.0654 |
| Raw ev away | 0.3424 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **52.1%**. Expected goals are 1.46 for Udinese and 0.83 for Lecce (2.29 combined). The most likely exact score is 1-0 at 14.7%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 40.3%; Under 3.5 goals: 80.1%; Double Chance 1X: 78.8%; Double Chance X2: 47.9%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 43.5%; BTTS No (at least one team does not score): 56.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 52.1% | 1.92 |
| Draw | 26.7% | 3.75 |
| Lecce win | 21.2% | 4.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.46 |
| Lecce expected goals | 0.83 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 67.0% |
| Under 1.5 | 33.0% |
| Over 2.5 | 40.3% |
| Under 2.5 | 59.7% |
| Over 3.5 | 19.9% |
| Under 3.5 | 80.1% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.66% |
| 2 | 1-1 | 12.31% |
| 3 | 2-0 | 10.87% |
| 4 | 0-0 | 10.20% |
| 5 | 2-1 | 9.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 52.1% | 52.7% | 1.95 | +1.7% |
| Draw | 26.7% | 26.2% | 3.65 | -2.5% |
| Lecce win | 21.2% | 21.1% | 4.38 | -7.3% |
| Over 2.5 | 40.3% | 48.3% | 2.08 | -16.2% |
| Under 2.5 | 59.7% | 51.7% | 1.87 | +11.6% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| P btts yes | 43.5% |
| P btts no | 56.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.81 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.03 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.03 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.05 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 43.6% |
| P home draw | 78.8% |
| P draw away | 47.9% |
| Raw p home draw | 78.8% |
| Raw p draw away | 48.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.77 |
| Reference draw odds | 3.30 |
| Reference away odds | 4.00 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.73 |
| Home probability edge | -0.6% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | -0.0112 |
| Raw ev home | 0.0058 |
| Raw edge prob draw | 0.0101 |
| Raw ev draw | -0.0069 |
| Raw edge prob away | 0.0010 |
| Raw ev away | -0.0709 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.2%**. Expected goals are 1.13 for Monza and 1.62 for Cagliari (2.75 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 50.7%; Under 3.5 goals: 70.9%; Double Chance 1X: 60.8%; Double Chance X2: 66.8%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 33.2% | 3.01 |
| Draw | 27.6% | 3.62 |
| Cagliari win | 39.2% | 2.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.13 |
| Cagliari expected goals | 1.62 |
| Expected total goals | 2.75 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
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
| 1 | 1-1 | 13.11% |
| 2 | 1-0 | 8.80% |
| 3 | 2-1 | 8.33% |
| 4 | 0-1 | 8.19% |
| 5 | 1-2 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.2% | 40.0% | 2.49 | -17.4% |
| Draw | 27.6% | 30.0% | 3.25 | -10.3% |
| Cagliari win | 39.2% | 30.0% | 3.25 | +27.4% |
| Over 2.5 | 50.7% | 43.3% | 2.15 | +9.0% |
| Under 2.5 | 49.3% | 56.7% | 1.82 | -10.2% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| P btts yes | 55.4% |
| P btts no | 44.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.72 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.19 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 26.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.3% |
| Raw p btts yes | 54.5% |
| P home draw | 60.8% |
| P draw away | 66.8% |
| Raw p home draw | 51.6% |
| Raw p draw away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.28 |
| Reference draw odds | 2.95 |
| Reference away odds | 2.95 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.60 |
| Home probability edge | -6.8% |
| Draw probability edge | -2.4% |
| Away probability edge | +9.2% |
| Over 2.5 probability edge | +7.4% |
| Under 2.5 probability edge | -7.4% |
| Raw edge prob home | -0.1357 |
| Raw ev home | -0.3425 |
| Raw edge prob draw | -0.0482 |
| Raw ev draw | -0.1812 |
| Raw edge prob away | 0.1839 |
| Raw ev away | 0.5730 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.2%**. Expected goals are 1.00 for Parma and 1.10 for Torino (2.11 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 87.5%; Over 2.5 goals: 35.2%; Under 3.5 goals: 83.7%; Double Chance 1X: 61.8%; Double Chance X2: 68.9%; Under 4.5 goals: 93.7%; BTTS Yes (both teams score): 42.7%; BTTS No (at least one team does not score): 57.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.1% | 3.21 |
| Draw | 30.6% | 3.26 |
| Torino win | 38.2% | 2.62 |

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
| 1 | 1-1 | 13.85% |
| 2 | 0-1 | 13.44% |
| 3 | 0-0 | 12.54% |
| 4 | 1-0 | 11.52% |
| 5 | 1-2 | 7.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.1% | 30.1% | 3.25 | +1.2% |
| Draw | 30.6% | 30.9% | 3.17 | -2.9% |
| Torino win | 38.2% | 39.1% | 2.54 | -2.9% |
| Over 2.5 | 35.2% | 38.7% | 2.48 | -12.8% |
| Under 2.5 | 64.8% | 61.3% | 1.63 | +5.7% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| P btts yes | 42.7% |
| P btts no | 57.3% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 7.97 |
| Fair Over 1.5 odds | 1.60 |
| Fair Under 1.5 odds | 2.67 |
| Fair Over 2.5 odds | 2.84 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.15 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 15.96 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.2% |
| Unadjusted draw probability | 30.4% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 62.5% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 42.6% |
| P home draw | 61.8% |
| P draw away | 68.9% |
| Raw p home draw | 62.6% |
| Raw p draw away | 67.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.95 |
| Reference draw odds | 2.88 |
| Reference away odds | 2.33 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.50 |
| Home probability edge | +1.1% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | 0.0217 |
| Raw ev home | 0.0475 |
| Raw edge prob draw | -0.0045 |
| Raw ev draw | -0.0358 |
| Raw edge prob away | -0.0172 |
| Raw ev away | -0.0513 |

</details>


---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **50.3%**. Expected goals are 1.94 for Torino and 1.18 for Monza (3.12 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 59.2%; Under 3.5 goals: 62.4%; Double Chance 1X: 75.6%; Double Chance X2: 49.7%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 50.3% | 1.99 |
| Draw | 25.3% | 3.95 |
| Monza win | 24.4% | 4.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.94 |
| Monza expected goals | 1.18 |
| Expected total goals | 3.12 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 59.2% |
| Under 2.5 | 40.8% |
| Over 3.5 | 37.6% |
| Under 3.5 | 62.4% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.63% |
| 2 | 2-1 | 8.96% |
| 3 | 1-0 | 7.63% |
| 4 | 2-0 | 7.61% |
| 5 | 2-2 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 50.3% | 45.5% | 2.15 | +8.1% |
| Draw | 25.3% | 28.2% | 3.62 | -8.4% |
| Monza win | 24.4% | 26.3% | 3.64 | -11.0% |
| Over 2.5 | 59.2% | 43.5% | 2.11 | +25.0% |
| Under 2.5 | 40.8% | 56.5% | 1.85 | -24.6% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.18 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.49 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.66 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 5.01 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 55.0% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 82.1% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 59.5% |
| P home draw | 75.6% |
| P draw away | 49.7% |
| Raw p home draw | 77.4% |
| Raw p draw away | 45.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.02 |
| Reference draw odds | 3.10 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.61 |
| Home probability edge | +4.7% |
| Draw probability edge | -2.9% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +15.7% |
| Under 2.5 probability edge | -15.7% |
| Raw edge prob home | 0.0947 |
| Raw ev home | 0.1825 |
| Raw edge prob draw | -0.0579 |
| Raw ev draw | -0.1892 |
| Raw edge prob away | -0.0368 |
| Raw ev away | -0.1773 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **39.0%**. Expected goals are 1.07 for Cagliari and 1.18 for Bologna (2.25 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 89.2%; Over 2.5 goals: 39.1%; Under 3.5 goals: 80.9%; Double Chance 1X: 61.0%; Double Chance X2: 68.3%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.9%; BTTS No (at least one team does not score): 54.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 31.7% | 3.16 |
| Draw | 29.3% | 3.41 |
| Bologna win | 39.0% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.07 |
| Bologna expected goals | 1.18 |
| Expected total goals | 2.25 |
| Over 0.5 | 89.2% |
| Under 0.5 | 10.8% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.64% |
| 2 | 0-1 | 12.42% |
| 3 | 0-0 | 10.83% |
| 4 | 1-0 | 10.64% |
| 5 | 1-2 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 31.7% | 30.6% | 3.35 | +6.1% |
| Draw | 29.3% | 29.5% | 3.13 | -8.2% |
| Bologna win | 39.0% | 40.0% | 2.52 | -1.8% |
| Over 2.5 | 39.1% | 41.8% | 2.24 | -12.4% |
| Under 2.5 | 60.9% | 58.2% | 1.76 | +7.1% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| P btts yes | 45.9% |
| P btts no | 54.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.24 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.23 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.77 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 38.0% |
| Raw p over 1 5 | 66.1% |
| Raw p under 3 5 | 80.9% |
| Raw p btts yes | 45.9% |
| P home draw | 61.0% |
| P draw away | 68.3% |
| Raw p home draw | 62.0% |
| Raw p draw away | 67.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.28 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.56 |
| Home probability edge | +1.1% |
| Draw probability edge | -0.1% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -2.6% |
| Under 2.5 probability edge | +2.6% |
| Raw edge prob home | 0.0220 |
| Raw ev home | 0.0982 |
| Raw edge prob draw | -0.0022 |
| Raw ev draw | -0.0851 |
| Raw edge prob away | -0.0198 |
| Raw ev away | -0.0426 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **64.9%**. Expected goals are 1.96 for Como and 0.91 for Sassuolo (2.87 combined). The most likely exact score is 1-0 at 11.5%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 55.3%; Under 3.5 goals: 67.3%; Double Chance 1X: 85.2%; Double Chance X2: 35.1%; Under 4.5 goals: 83.4%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 64.9% | 1.54 |
| Draw | 20.3% | 4.94 |
| Sassuolo win | 14.8% | 6.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 1.96 |
| Sassuolo expected goals | 0.91 |
| Expected total goals | 2.87 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 78.6% |
| Under 1.5 | 21.4% |
| Over 2.5 | 55.3% |
| Under 2.5 | 44.7% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.51% |
| 2 | 2-0 | 11.49% |
| 3 | 2-1 | 10.43% |
| 4 | 1-1 | 9.63% |
| 5 | 3-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 64.9% | 68.2% | 1.49 | -3.3% |
| Draw | 20.3% | 18.8% | 4.94 | +0.1% |
| Sassuolo win | 14.8% | 13.0% | 7.10 | +5.2% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.16 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.66 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 6.02 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 61.6% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 16.6% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 51.5% |
| P home draw | 85.2% |
| P draw away | 35.1% |
| Raw p home draw | 83.4% |
| Raw p draw away | 38.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.40 |
| Reference draw odds | 4.35 |
| Reference away odds | 6.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.56 |
| Home probability edge | -3.3% |
| Draw probability edge | +1.5% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | -0.0655 |
| Raw ev home | -0.0814 |
| Raw edge prob draw | 0.0297 |
| Raw ev draw | 0.0743 |
| Raw edge prob away | 0.0358 |
| Raw ev away | 0.1789 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **57.7%**. Expected goals are 1.36 for Lazio and 0.66 for Parma (2.02 combined). The most likely exact score is 1-0 at 19.2%. Goal-market probabilities: at least one goal: 87.8%; Over 2.5 goals: 33.9%; Under 3.5 goals: 85.0%; Double Chance 1X: 83.5%; Double Chance X2: 42.3%; Under 4.5 goals: 94.3%; BTTS Yes (both teams score): 35.5%; BTTS No (at least one team does not score): 64.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 57.7% | 1.73 |
| Draw | 25.9% | 3.87 |
| Parma win | 16.5% | 6.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.36 |
| Parma expected goals | 0.66 |
| Expected total goals | 2.02 |
| Over 0.5 | 87.8% |
| Under 0.5 | 12.2% |
| Over 1.5 | 60.8% |
| Under 1.5 | 39.2% |
| Over 2.5 | 33.9% |
| Under 2.5 | 66.1% |
| Over 3.5 | 15.0% |
| Under 3.5 | 85.0% |
| Over 4.5 | 5.7% |
| Under 4.5 | 94.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.16% |
| 2 | 2-0 | 13.22% |
| 3 | 0-0 | 12.20% |
| 4 | 1-1 | 10.98% |
| 5 | 2-1 | 8.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 57.7% | 61.8% | 1.58 | -8.9% |
| Draw | 25.9% | 23.1% | 4.33 | +11.9% |
| Parma win | 16.5% | 15.1% | 6.64 | +9.5% |
| Over 2.5 | 33.9% | 48.6% | 2.06 | -30.1% |
| Under 2.5 | 66.1% | 51.4% | 1.89 | +24.9% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| P btts yes | 35.5% |
| P btts no | 64.5% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.19 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.55 |
| Fair Over 2.5 odds | 2.95 |
| Fair Under 2.5 odds | 1.51 |
| Fair Over 3.5 odds | 6.67 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 17.61 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 53.5% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 17.9% |
| Raw p over 1 5 | 60.2% |
| Raw p under 3 5 | 85.3% |
| Raw p btts yes | 36.2% |
| P home draw | 83.5% |
| P draw away | 42.3% |
| Raw p home draw | 82.1% |
| Raw p draw away | 46.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.53 |
| Reference draw odds | 3.65 |
| Reference away odds | 5.30 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.74 |
| Home probability edge | -4.1% |
| Draw probability edge | +2.8% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -14.7% |
| Under 2.5 probability edge | +14.7% |
| Raw edge prob home | -0.0826 |
| Raw ev home | -0.1544 |
| Raw edge prob draw | 0.0554 |
| Raw ev draw | 0.2394 |
| Raw edge prob away | 0.0272 |
| Raw ev away | 0.1856 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **39.4%**. Expected goals are 1.04 for Napoli and 1.19 for AS Roma (2.23 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 38.9%; Under 3.5 goals: 81.3%; Double Chance 1X: 60.6%; Double Chance X2: 67.6%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 44.9%; BTTS No (at least one team does not score): 55.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 32.4% | 3.08 |
| Draw | 28.2% | 3.55 |
| AS Roma win | 39.4% | 2.54 |

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
| Over 2.5 | 38.9% |
| Under 2.5 | 61.1% |
| Over 3.5 | 18.7% |
| Under 3.5 | 81.3% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.03% |
| 2 | 0-1 | 12.66% |
| 3 | 1-0 | 11.19% |
| 4 | 0-0 | 10.60% |
| 5 | 1-2 | 8.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 32.4% | 33.1% | 3.04 | -1.4% |
| Draw | 28.2% | 26.9% | 3.60 | +1.4% |
| AS Roma win | 39.4% | 40.0% | 2.45 | -3.4% |
| Over 2.5 | 38.9% | 52.4% | 1.93 | -25.0% |
| Under 2.5 | 61.1% | 47.6% | 2.01 | +22.9% |

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
| Market best home last update utc | 2026-10-14T21:06:46Z |
| Market best draw last update utc | 2026-10-14T21:06:46Z |
| Market best away last update utc | 2026-10-14T21:06:46Z |
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
| P btts yes | 44.9% |
| P btts no | 55.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.44 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.90 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.36 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.07 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 31.7% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.4% |
| Raw p btts yes | 45.2% |
| P home draw | 60.6% |
| P draw away | 67.6% |
| Raw p home draw | 61.1% |
| Raw p draw away | 68.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.28 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | -0.7% |
| Draw probability edge | +1.2% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -13.5% |
| Under 2.5 probability edge | +13.5% |
| Raw edge prob home | -0.0137 |
| Raw ev home | -0.0353 |
| Raw edge prob draw | 0.0244 |
| Raw ev draw | 0.0576 |
| Raw edge prob away | -0.0107 |
| Raw ev away | -0.0472 |

</details>


---
