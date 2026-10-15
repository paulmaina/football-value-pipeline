# Serie A — football model report

Fixtures in this report: **16**.

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
| Live odds matched | 16.00 |
| Additional event odds calls used before this league | 21.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-16 — Frosinone vs Sassuolo

The model's most likely 1X2 outcome is **Frosinone win** at **41.5%**. Expected goals are 1.64 for Frosinone and 1.29 for Sassuolo (2.94 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.3%; Double Chance 1X: 67.0%; Double Chance X2: 58.5%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 41.5% | 2.41 |
| Draw | 25.5% | 3.92 |
| Sassuolo win | 33.0% | 3.03 |

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
| 2 | 2-1 | 8.47% |
| 3 | 1-2 | 8.03% |
| 4 | 1-0 | 7.76% |
| 5 | 0-1 | 7.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 41.5% | 37.6% | 2.62 | +8.8% |
| Draw | 25.5% | 26.3% | 3.67 | -6.4% |
| Sassuolo win | 33.0% | 36.0% | 2.76 | -8.9% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
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
| Fair Under 0.5 odds | 17.43 |
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
| P home draw | 67.0% |
| P draw away | 58.5% |
| P home away | 74.5% |
| Raw p home draw | 70.0% |
| Raw p draw away | 54.6% |
| Raw p home away | 75.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 2.45 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.55 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.60 |
| Home probability edge | +3.9% |
| Draw probability edge | -0.8% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -10.3% |
| Under 2.5 probability edge | +10.3% |
| Raw edge prob home | 0.0774 |
| Raw ev home | 0.1889 |
| Raw edge prob draw | -0.0166 |
| Raw ev draw | -0.0945 |
| Raw edge prob away | -0.0608 |
| Raw ev away | -0.1734 |
| Market p home draw | 64.3% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T13:12:19Z |
| Market reference home draw last update utc | 2026-10-15T13:12:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.7% |
| Market draw away odds | 1.55 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T13:12:19Z |
| Market reference draw away last update utc | 2026-10-15T13:12:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.0% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T13:12:19Z |
| Market reference home away last update utc | 2026-10-15T13:12:19Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.51 |
| Market reference dc draw away odds | 1.55 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 86.0% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 56.0% |
| Market reference under 3 5 odds | 1.74 |
| Market reference under 3 5 opposite odds | 2.19 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 68.4% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T13:12:19Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.77 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **67.8%**. Expected goals are 1.97 for AS Roma and 0.64 for Genoa (2.61 combined). The most likely exact score is 2-0 at 14.1%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 48.4%; Under 3.5 goals: 73.5%; Double Chance 1X: 87.9%; Double Chance X2: 32.2%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 40.9%; BTTS No (at least one team does not score): 59.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 67.8% | 1.47 |
| Draw | 20.1% | 4.98 |
| Genoa win | 12.1% | 8.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.97 |
| Genoa expected goals | 0.64 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 73.5% |
| Under 1.5 | 26.5% |
| Over 2.5 | 48.4% |
| Under 2.5 | 51.6% |
| Over 3.5 | 26.5% |
| Under 3.5 | 73.5% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.08% |
| 2 | 1-0 | 14.07% |
| 3 | 1-1 | 9.33% |
| 4 | 3-0 | 9.27% |
| 5 | 2-1 | 9.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 67.8% | 66.9% | 1.48 | +0.4% |
| Draw | 20.1% | 19.9% | 4.74 | -4.8% |
| Genoa win | 12.1% | 13.3% | 7.70 | -7.1% |
| Over 2.5 | 48.4% | 56.9% | 1.77 | -14.3% |
| Under 2.5 | 51.6% | 43.1% | 2.22 | +14.5% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| P btts yes | 40.9% |
| P btts no | 59.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.45 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.77 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.77 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.07 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.8% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 10.9% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 40.9% |
| P home draw | 87.9% |
| P draw away | 32.2% |
| P home away | 79.9% |
| Raw p home draw | 89.1% |
| Raw p draw away | 31.2% |
| Raw p home away | 79.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 1.44 |
| Reference draw odds | 4.33 |
| Reference away odds | 6.25 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +1.0% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -8.5% |
| Under 2.5 probability edge | +8.5% |
| Raw edge prob home | 0.0192 |
| Raw ev home | 0.0183 |
| Raw edge prob draw | 0.0046 |
| Raw ev draw | -0.0367 |
| Raw edge prob away | -0.0238 |
| Raw ev away | -0.1628 |
| Market p home draw | 85.9% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T13:12:19Z |
| Market reference home draw last update utc | 2026-10-15T13:12:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.7% |
| Market draw away odds | 2.85 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T13:12:19Z |
| Market reference draw away last update utc | 2026-10-15T13:12:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.4% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T13:12:19Z |
| Market reference home away last update utc | 2026-10-15T13:12:19Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.11 |
| Market reference dc draw away odds | 2.75 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 80.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.3% |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.86 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 50.3% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T13:12:19Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 1.87 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.4%**. Expected goals are 1.08 for Bologna and 2.13 for Inter Milan (3.20 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.2%; Double Chance 1X: 38.6%; Double Chance X2: 83.3%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 78.2%; BTTS Yes (both teams score): 58.5%; BTTS No (at least one team does not score): 41.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 16.7% | 6.00 |
| Draw | 21.9% | 4.56 |
| Inter Milan win | 61.4% | 1.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.08 |
| Inter Milan expected goals | 2.13 |
| Expected total goals | 3.20 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 61.7% |
| Under 2.5 | 38.3% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.8% |
| Under 4.5 | 78.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.09% |
| 2 | 1-2 | 9.93% |
| 3 | 0-2 | 9.23% |
| 4 | 0-1 | 8.48% |
| 5 | 1-3 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 16.7% | 15.2% | 5.56 | -7.3% |
| Draw | 21.9% | 23.2% | 4.10 | -10.1% |
| Inter Milan win | 61.4% | 61.6% | 1.69 | +3.8% |
| Over 2.5 | 61.7% | 56.9% | 1.74 | +7.3% |
| Under 2.5 | 38.3% | 43.1% | 2.27 | -13.0% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| P btts yes | 58.5% |
| P btts no | 41.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.09 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.93 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.58 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.1% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 61.2% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 60.2% |
| Raw p btts yes | 58.2% |
| P home draw | 38.6% |
| P draw away | 83.3% |
| P home away | 78.1% |
| Raw p home draw | 38.8% |
| Raw p draw away | 81.9% |
| Raw p home away | 79.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 5.50 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.55 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +1.5% |
| Draw probability edge | -1.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +4.8% |
| Under 2.5 probability edge | -4.8% |
| Raw edge prob home | 0.0295 |
| Raw ev home | 0.0089 |
| Raw edge prob draw | -0.0255 |
| Raw ev draw | -0.1532 |
| Raw edge prob away | -0.0040 |
| Raw ev away | 0.0343 |
| Market p home draw | 40.9% |
| Market home draw odds | 2.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T13:12:19Z |
| Market reference home draw last update utc | 2026-10-15T13:12:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.9% |
| Market draw away odds | 1.18 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T13:12:19Z |
| Market reference draw away last update utc | 2026-10-15T13:12:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.2% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T13:12:19Z |
| Market reference home away last update utc | 2026-10-15T13:12:19Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.32 |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T13:11:47Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.5% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T13:11:47Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.65 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.4% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T13:12:19Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **65.8%**. Expected goals are 0.67 for Venezia and 2.30 for Napoli (2.96 combined). The most likely exact score is 0-2 at 12.1%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.8%; Under 3.5 goals: 67.2%; Double Chance 1X: 34.2%; Double Chance X2: 85.5%; Double Chance 12 (either team wins): 80.3%; Under 4.5 goals: 83.2%; BTTS Yes (both teams score): 45.3%; BTTS No (at least one team does not score): 54.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 14.5% | 6.91 |
| Draw | 19.7% | 5.08 |
| Napoli win | 65.8% | 1.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.30 |
| Expected total goals | 2.96 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 78.1% |
| Under 1.5 | 21.9% |
| Over 2.5 | 54.8% |
| Under 2.5 | 45.2% |
| Over 3.5 | 32.8% |
| Under 3.5 | 67.2% |
| Over 4.5 | 16.8% |
| Under 4.5 | 83.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.12% |
| 2 | 0-1 | 10.41% |
| 3 | 1-1 | 9.36% |
| 4 | 0-3 | 9.27% |
| 5 | 1-2 | 8.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 14.5% | 20.0% | 4.89 | -29.2% |
| Draw | 19.7% | 22.4% | 4.22 | -16.9% |
| Napoli win | 65.8% | 57.7% | 1.74 | +14.5% |
| Over 2.5 | 54.8% | 55.8% | 1.77 | -3.0% |
| Under 2.5 | 45.2% | 44.2% | 2.22 | +0.3% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| P btts yes | 45.3% |
| P btts no | 54.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.18 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.57 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.05 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.96 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 9.0% |
| Unadjusted draw probability | 17.0% |
| Unadjusted away-win probability | 74.0% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 43.9% |
| P home draw | 34.2% |
| P draw away | 85.5% |
| P home away | 80.3% |
| Raw p home draw | 26.0% |
| Raw p draw away | 91.0% |
| Raw p home away | 83.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 4.33 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.65 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -5.5% |
| Draw probability edge | -2.7% |
| Away probability edge | +8.2% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | -0.1097 |
| Raw ev home | -0.5607 |
| Raw edge prob draw | -0.0537 |
| Raw ev draw | -0.2820 |
| Raw edge prob away | 0.1635 |
| Raw ev away | 0.2876 |
| Market p home draw | 45.0% |
| Market home draw odds | 2.21 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T13:12:19Z |
| Market reference home draw last update utc | 2026-10-15T13:12:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 78.8% |
| Market draw away odds | 1.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T13:12:19Z |
| Market reference draw away last update utc | 2026-10-15T13:12:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T13:12:19Z |
| Market reference home away last update utc | 2026-10-15T13:12:19Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.12 |
| Market reference dc draw away odds | 1.21 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 80.4% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.1% |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 56.4% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T13:12:19Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **46.9%**. Expected goals are 1.29 for AC Milan and 1.15 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 44.7%; Under 3.5 goals: 76.9%; Double Chance 1X: 73.2%; Double Chance X2: 53.1%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 46.9% | 2.13 |
| Draw | 26.3% | 3.80 |
| Atalanta BC win | 26.8% | 3.73 |

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
| Over 2.5 | 44.7% |
| Under 2.5 | 55.3% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.04% |
| 2 | 1-1 | 12.47% |
| 3 | 2-1 | 9.91% |
| 4 | 2-0 | 8.63% |
| 5 | 0-0 | 8.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 46.9% | 54.3% | 1.93 | -9.4% |
| Draw | 26.3% | 24.7% | 3.86 | +1.5% |
| Atalanta BC win | 26.8% | 20.9% | 4.22 | +13.0% |
| Over 2.5 | 44.7% | 53.7% | 1.83 | -18.2% |
| Under 2.5 | 55.3% | 46.3% | 2.13 | +17.8% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| Fair Under 0.5 odds | 11.79 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.32 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.71 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.8% |
| P home draw | 73.2% |
| P draw away | 53.1% |
| P home away | 73.7% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.5% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 1.75 |
| Reference draw odds | 3.60 |
| Reference away odds | 4.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.00 |
| Home probability edge | -7.4% |
| Draw probability edge | +1.6% |
| Away probability edge | +5.9% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.1481 |
| Raw ev home | -0.2372 |
| Raw edge prob draw | 0.0310 |
| Raw ev draw | 0.0750 |
| Raw edge prob away | 0.1171 |
| Raw ev away | 0.3769 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.3%**. Expected goals are 0.96 for Fiorentina and 1.71 for Como (2.67 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.6%; Double Chance 1X: 49.7%; Double Chance X2: 75.4%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.6% | 4.06 |
| Draw | 25.1% | 3.99 |
| Como win | 50.3% | 1.99 |

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
| 2 | 0-1 | 10.70% |
| 3 | 0-2 | 9.32% |
| 4 | 1-2 | 8.93% |
| 5 | 1-0 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.6% | 28.3% | 3.54 | -12.9% |
| Draw | 25.1% | 25.7% | 3.81 | -4.5% |
| Como win | 50.3% | 45.9% | 2.12 | +6.7% |
| Over 2.5 | 49.3% | 56.9% | 1.73 | -14.7% |
| Under 2.5 | 50.7% | 43.1% | 2.29 | +16.1% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
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
| Fair Over 3.5 odds | 3.65 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.72 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 50.7% |
| P home draw | 49.7% |
| P draw away | 75.4% |
| P home away | 74.9% |
| Raw p home draw | 45.3% |
| Raw p draw away | 79.1% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 3.20 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.05 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -3.7% |
| Draw probability edge | -0.7% |
| Away probability edge | +4.4% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | -0.0749 |
| Raw ev home | -0.2616 |
| Raw edge prob draw | -0.0131 |
| Raw ev draw | -0.0697 |
| Raw edge prob away | 0.0879 |
| Raw ev away | 0.1601 |
| Market p home draw | 54.5% |
| Market home draw odds | 1.80 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T13:12:19Z |
| Market reference home draw last update utc | 2026-10-15T13:12:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.7% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T13:12:19Z |
| Market reference draw away last update utc | 2026-10-15T13:12:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.9% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T13:12:19Z |
| Market reference home away last update utc | 2026-10-15T13:12:19Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.75 |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T13:12:10Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.0% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T13:12:10Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.69 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.1% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T13:12:19Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.32 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **53.6%**. Expected goals are 1.37 for Juventus and 0.87 for Lazio (2.23 combined). The most likely exact score is 1-0 at 15.9%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 39.5%; Under 3.5 goals: 80.9%; Double Chance 1X: 79.7%; Double Chance X2: 46.4%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.9%; BTTS No (at least one team does not score): 57.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 53.6% | 1.87 |
| Draw | 26.2% | 3.82 |
| Lazio win | 20.3% | 4.93 |

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
| 1 | 1-0 | 15.95% |
| 2 | 1-1 | 12.01% |
| 3 | 2-0 | 11.11% |
| 4 | 0-0 | 10.17% |
| 5 | 2-1 | 9.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 53.6% | 58.8% | 1.69 | -9.5% |
| Draw | 26.2% | 24.1% | 4.04 | +5.7% |
| Lazio win | 20.3% | 17.1% | 5.71 | +15.8% |
| Over 2.5 | 39.5% | 50.0% | 2.03 | -19.8% |
| Under 2.5 | 60.5% | 50.0% | 1.92 | +16.1% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| Fair Under 0.5 odds | 9.83 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.24 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.69 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 43.5% |
| P home draw | 79.7% |
| P draw away | 46.4% |
| P home away | 73.8% |
| Raw p home draw | 76.5% |
| Raw p draw away | 51.7% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 1.62 |
| Reference draw odds | 3.65 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | -5.3% |
| Draw probability edge | +2.1% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | -0.1058 |
| Raw ev home | -0.1843 |
| Raw edge prob draw | 0.0413 |
| Raw ev draw | 0.1404 |
| Raw edge prob away | 0.0646 |
| Raw ev away | 0.3424 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.6%**. Expected goals are 1.46 for Udinese and 0.83 for Lecce (2.29 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.1%; Double Chance 1X: 78.5%; Double Chance X2: 48.4%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 43.5%; BTTS No (at least one team does not score): 56.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.6% | 1.94 |
| Draw | 26.9% | 3.72 |
| Lecce win | 21.5% | 4.64 |

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
| Over 3.5 | 19.9% |
| Under 3.5 | 80.1% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.50% |
| 2 | 1-1 | 12.40% |
| 3 | 2-0 | 10.75% |
| 4 | 0-0 | 10.27% |
| 5 | 2-1 | 8.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.6% | 51.6% | 1.95 | +0.6% |
| Draw | 26.9% | 26.6% | 3.65 | -1.9% |
| Lecce win | 21.5% | 21.9% | 4.38 | -5.6% |
| Over 2.5 | 40.2% | 46.3% | 2.08 | -16.4% |
| Under 2.5 | 59.8% | 53.7% | 1.87 | +11.8% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| Fair Under 0.5 odds | 9.74 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.04 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.09 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 43.6% |
| P home draw | 78.5% |
| P draw away | 48.4% |
| P home away | 73.1% |
| Raw p home draw | 78.8% |
| Raw p draw away | 48.4% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 1.83 |
| Reference draw odds | 3.35 |
| Reference away odds | 4.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.75 |
| Home probability edge | +0.0% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | 0.0002 |
| Raw ev home | 0.0058 |
| Raw edge prob draw | 0.0064 |
| Raw ev draw | -0.0069 |
| Raw edge prob away | -0.0066 |
| Raw ev away | -0.0709 |
| Market p home draw | 77.4% |
| Market home draw odds | 1.25 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T13:12:19Z |
| Market reference home draw last update utc | 2026-10-15T13:12:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.9% |
| Market draw away odds | 1.95 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T13:12:19Z |
| Market reference draw away last update utc | 2026-10-15T13:12:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.7% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T13:12:19Z |
| Market reference home away last update utc | 2026-10-15T13:12:19Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.23 |
| Market reference dc draw away odds | 1.91 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 72.5% |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.35 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 76.1% |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.80 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 50.9% |
| Market btts yes odds | 1.83 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T13:12:19Z |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 1.89 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.1%**. Expected goals are 1.13 for Monza and 1.62 for Cagliari (2.75 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 50.7%; Under 3.5 goals: 70.9%; Double Chance 1X: 60.9%; Double Chance X2: 66.6%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 33.4% | 2.99 |
| Draw | 27.5% | 3.64 |
| Cagliari win | 39.1% | 2.56 |

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
| 1 | 1-1 | 13.05% |
| 2 | 1-0 | 8.86% |
| 3 | 2-1 | 8.39% |
| 4 | 0-1 | 8.16% |
| 5 | 1-2 | 7.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.4% | 40.5% | 2.49 | -16.8% |
| Draw | 27.5% | 29.8% | 3.25 | -10.7% |
| Cagliari win | 39.1% | 29.8% | 3.25 | +27.0% |
| Over 2.5 | 50.7% | 45.7% | 2.15 | +9.0% |
| Under 2.5 | 49.3% | 54.3% | 1.82 | -10.3% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| Fair Under 0.5 odds | 13.78 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.18 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 26.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.3% |
| Raw p btts yes | 54.5% |
| P home draw | 60.9% |
| P draw away | 66.6% |
| P home away | 72.5% |
| Raw p home draw | 51.6% |
| Raw p draw away | 73.6% |
| Raw p home away | 74.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 2.30 |
| Reference draw odds | 3.05 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.75 |
| Home probability edge | -7.0% |
| Draw probability edge | -2.3% |
| Away probability edge | +9.3% |
| Over 2.5 probability edge | +5.0% |
| Under 2.5 probability edge | -5.0% |
| Raw edge prob home | -0.1405 |
| Raw ev home | -0.3425 |
| Raw edge prob draw | -0.0458 |
| Raw ev draw | -0.1812 |
| Raw edge prob away | 0.1863 |
| Raw ev away | 0.5730 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **37.5%**. Expected goals are 1.00 for Parma and 1.10 for Torino (2.11 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 87.2%; Over 2.5 goals: 35.0%; Under 3.5 goals: 83.8%; Double Chance 1X: 62.5%; Double Chance X2: 68.8%; Double Chance 12 (either team wins): 68.8%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 42.8%; BTTS No (at least one team does not score): 57.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.2% | 3.20 |
| Draw | 31.2% | 3.20 |
| Torino win | 37.5% | 2.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.00 |
| Torino expected goals | 1.10 |
| Expected total goals | 2.11 |
| Over 0.5 | 87.2% |
| Under 0.5 | 12.8% |
| Over 1.5 | 62.5% |
| Under 1.5 | 37.5% |
| Over 2.5 | 35.0% |
| Under 2.5 | 65.0% |
| Over 3.5 | 16.2% |
| Under 3.5 | 83.8% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.11% |
| 2 | 0-1 | 13.20% |
| 3 | 0-0 | 12.77% |
| 4 | 1-0 | 11.56% |
| 5 | 1-2 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.2% | 30.3% | 3.25 | +1.6% |
| Draw | 31.2% | 32.0% | 3.17 | -1.1% |
| Torino win | 37.5% | 37.7% | 2.54 | -4.6% |
| Over 2.5 | 35.0% | 39.5% | 2.48 | -13.3% |
| Under 2.5 | 65.0% | 60.5% | 1.63 | +6.0% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| P btts yes | 42.8% |
| P btts no | 57.2% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.83 |
| Fair Over 1.5 odds | 1.60 |
| Fair Under 1.5 odds | 2.66 |
| Fair Over 2.5 odds | 2.86 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.16 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.06 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.2% |
| Unadjusted draw probability | 30.4% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 62.5% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 42.6% |
| P home draw | 62.5% |
| P draw away | 68.8% |
| P home away | 68.8% |
| Raw p home draw | 62.6% |
| Raw p draw away | 67.8% |
| Raw p home away | 69.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 3.00 |
| Reference draw odds | 2.85 |
| Reference away odds | 2.45 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.30 |
| Reference Under 2.5 odds | 1.57 |
| Home probability edge | +1.0% |
| Draw probability edge | -0.8% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | 0.0196 |
| Raw ev home | 0.0475 |
| Raw edge prob draw | -0.0159 |
| Raw ev draw | -0.0358 |
| Raw edge prob away | -0.0038 |
| Raw ev away | -0.0513 |

</details>


---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **50.5%**. Expected goals are 1.94 for Torino and 1.18 for Monza (3.12 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 59.4%; Under 3.5 goals: 62.4%; Double Chance 1X: 75.4%; Double Chance X2: 49.5%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 50.5% | 1.98 |
| Draw | 24.9% | 4.01 |
| Monza win | 24.6% | 4.07 |

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
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.46% |
| 2 | 2-1 | 9.00% |
| 3 | 1-0 | 7.67% |
| 4 | 2-0 | 7.64% |
| 5 | 1-2 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 50.5% | 46.0% | 2.15 | +8.5% |
| Draw | 24.9% | 27.5% | 3.62 | -9.8% |
| Monza win | 24.6% | 26.6% | 3.64 | -10.5% |
| Over 2.5 | 59.4% | 46.3% | 2.11 | +25.2% |
| Under 2.5 | 40.6% | 53.7% | 1.85 | -24.8% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.46 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.49 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.66 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.99 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 55.0% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 82.1% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 59.5% |
| P home draw | 75.4% |
| P draw away | 49.5% |
| P home away | 75.1% |
| Raw p home draw | 77.4% |
| Raw p draw away | 45.0% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.05 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.75 |
| Home probability edge | +4.5% |
| Draw probability edge | -2.5% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +13.1% |
| Under 2.5 probability edge | -13.1% |
| Raw edge prob home | 0.0903 |
| Raw ev home | 0.1825 |
| Raw edge prob draw | -0.0506 |
| Raw ev draw | -0.1892 |
| Raw edge prob away | -0.0398 |
| Raw ev away | -0.1773 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **38.0%**. Expected goals are 1.07 for Cagliari and 1.18 for Bologna (2.25 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 39.0%; Under 3.5 goals: 80.9%; Double Chance 1X: 62.0%; Double Chance X2: 67.8%; Double Chance 12 (either team wins): 70.2%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 46.0%; BTTS No (at least one team does not score): 54.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 32.2% | 3.11 |
| Draw | 29.8% | 3.35 |
| Bologna win | 38.0% | 2.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.07 |
| Bologna expected goals | 1.18 |
| Expected total goals | 2.25 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.87% |
| 2 | 0-1 | 12.10% |
| 3 | 0-0 | 11.01% |
| 4 | 1-0 | 10.81% |
| 5 | 1-2 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 32.2% | 31.6% | 3.35 | +7.8% |
| Draw | 29.8% | 30.5% | 3.13 | -6.6% |
| Bologna win | 38.0% | 37.9% | 2.52 | -4.3% |
| Over 2.5 | 39.0% | 42.2% | 2.24 | -12.7% |
| Under 2.5 | 61.0% | 57.8% | 1.76 | +7.4% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| P btts yes | 46.0% |
| P btts no | 54.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.08 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.23 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.84 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 38.0% |
| Raw p over 1 5 | 66.1% |
| Raw p under 3 5 | 80.9% |
| Raw p btts yes | 45.9% |
| P home draw | 62.0% |
| P draw away | 67.8% |
| P home away | 70.2% |
| Raw p home draw | 62.0% |
| Raw p draw away | 67.2% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.90 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.45 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.65 |
| Home probability edge | +0.6% |
| Draw probability edge | -0.6% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | 0.0118 |
| Raw ev home | 0.0982 |
| Raw edge prob draw | -0.0124 |
| Raw ev draw | -0.0851 |
| Raw edge prob away | 0.0006 |
| Raw ev away | -0.0426 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **65.3%**. Expected goals are 1.96 for Como and 0.91 for Sassuolo (2.87 combined). The most likely exact score is 1-0 at 11.6%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 55.4%; Under 3.5 goals: 67.3%; Double Chance 1X: 85.4%; Double Chance X2: 34.7%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 65.3% | 1.53 |
| Draw | 20.1% | 4.97 |
| Sassuolo win | 14.6% | 6.85 |

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
| Over 2.5 | 55.4% |
| Under 2.5 | 44.6% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.58% |
| 2 | 2-0 | 11.55% |
| 3 | 2-1 | 10.49% |
| 4 | 1-1 | 9.56% |
| 5 | 3-0 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 65.3% | 68.9% | 1.49 | -2.7% |
| Draw | 20.1% | 18.5% | 4.94 | -0.6% |
| Sassuolo win | 14.6% | 12.6% | 7.10 | +3.7% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| Fair Under 0.5 odds | 18.29 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.67 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 6.01 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 61.6% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 16.6% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 51.5% |
| P home draw | 85.4% |
| P draw away | 34.7% |
| P home away | 79.9% |
| Raw p home draw | 83.4% |
| Raw p draw away | 38.4% |
| Raw p home away | 78.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.40 |
| Reference draw odds | 4.60 |
| Reference away odds | 6.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -3.6% |
| Draw probability edge | +1.6% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | -0.0727 |
| Raw ev home | -0.0814 |
| Raw edge prob draw | 0.0327 |
| Raw ev draw | 0.0743 |
| Raw edge prob away | 0.0400 |
| Raw ev away | 0.1789 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **57.8%**. Expected goals are 1.36 for Lazio and 0.66 for Parma (2.02 combined). The most likely exact score is 1-0 at 19.2%. Goal-market probabilities: at least one goal: 87.7%; Over 2.5 goals: 33.9%; Under 3.5 goals: 85.0%; Double Chance 1X: 83.7%; Double Chance X2: 42.2%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 94.3%; BTTS Yes (both teams score): 35.5%; BTTS No (at least one team does not score): 64.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 57.8% | 1.73 |
| Draw | 26.0% | 3.85 |
| Parma win | 16.3% | 6.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.36 |
| Parma expected goals | 0.66 |
| Expected total goals | 2.02 |
| Over 0.5 | 87.7% |
| Under 0.5 | 12.3% |
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
| 1 | 1-0 | 19.20% |
| 2 | 2-0 | 13.24% |
| 3 | 0-0 | 12.26% |
| 4 | 1-1 | 11.03% |
| 5 | 2-1 | 8.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 57.8% | 62.0% | 1.58 | -8.7% |
| Draw | 26.0% | 23.3% | 4.33 | +12.4% |
| Parma win | 16.3% | 14.7% | 6.64 | +8.1% |
| Over 2.5 | 33.9% | 47.8% | 2.06 | -30.2% |
| Under 2.5 | 66.1% | 52.2% | 1.89 | +24.9% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| Fair Under 0.5 odds | 8.16 |
| Fair Over 1.5 odds | 1.64 |
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
| P home draw | 83.7% |
| P draw away | 42.2% |
| P home away | 74.0% |
| Raw p home draw | 82.1% |
| Raw p draw away | 46.5% |
| Raw p home away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.55 |
| Reference draw odds | 3.80 |
| Reference away odds | 5.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.80 |
| Home probability edge | -4.2% |
| Draw probability edge | +2.7% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -13.9% |
| Under 2.5 probability edge | +13.9% |
| Raw edge prob home | -0.0848 |
| Raw ev home | -0.1544 |
| Raw edge prob draw | 0.0532 |
| Raw ev draw | 0.2394 |
| Raw edge prob away | 0.0316 |
| Raw ev away | 0.1856 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **39.6%**. Expected goals are 1.04 for Napoli and 1.19 for AS Roma (2.23 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 38.8%; Under 3.5 goals: 81.3%; Double Chance 1X: 60.4%; Double Chance X2: 67.9%; Double Chance 12 (either team wins): 71.7%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 45.0%; BTTS No (at least one team does not score): 55.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 32.1% | 3.11 |
| Draw | 28.3% | 3.54 |
| AS Roma win | 39.6% | 2.53 |

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
| 1 | 1-1 | 13.09% |
| 2 | 0-1 | 12.72% |
| 3 | 1-0 | 11.09% |
| 4 | 0-0 | 10.64% |
| 5 | 1-2 | 8.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 32.1% | 32.5% | 3.04 | -2.3% |
| Draw | 28.3% | 27.2% | 3.60 | +1.8% |
| AS Roma win | 39.6% | 40.3% | 2.45 | -3.0% |
| Over 2.5 | 38.8% | 50.9% | 1.93 | -25.1% |
| Under 2.5 | 61.2% | 49.1% | 2.01 | +23.0% |

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
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
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
| Fair Under 0.5 odds | 9.40 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.90 |
| Fair Over 2.5 odds | 2.58 |
| Fair Under 2.5 odds | 1.63 |
| Fair Over 3.5 odds | 5.36 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.09 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 31.7% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.4% |
| Raw p btts yes | 45.2% |
| P home draw | 60.4% |
| P draw away | 67.9% |
| P home away | 71.7% |
| Raw p home draw | 61.1% |
| Raw p draw away | 68.3% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.80 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.30 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.91 |
| Home probability edge | -0.4% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -12.0% |
| Under 2.5 probability edge | +12.0% |
| Raw edge prob home | -0.0078 |
| Raw ev home | -0.0353 |
| Raw edge prob draw | 0.0220 |
| Raw ev draw | 0.0576 |
| Raw edge prob away | -0.0141 |
| Raw ev away | -0.0472 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **73.4%**. Expected goals are 2.78 for Inter Milan and 0.94 for Fiorentina (3.72 combined). The most likely exact score is 2-0 at 9.1%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 71.3%; Under 3.5 goals: 49.3%; Double Chance 1X: 89.2%; Double Chance X2: 26.6%; Double Chance 12 (either team wins): 84.2%; Under 4.5 goals: 68.7%; BTTS Yes (both teams score): 57.9%; BTTS No (at least one team does not score): 42.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 73.4% | 1.36 |
| Draw | 15.8% | 6.33 |
| Fiorentina win | 10.8% | 9.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.78 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.72 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 88.5% |
| Under 1.5 | 11.5% |
| Over 2.5 | 71.3% |
| Under 2.5 | 28.7% |
| Over 3.5 | 50.7% |
| Under 3.5 | 49.3% |
| Over 4.5 | 31.3% |
| Under 4.5 | 68.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.08% |
| 2 | 2-1 | 8.57% |
| 3 | 3-0 | 8.41% |
| 4 | 3-1 | 7.93% |
| 5 | 1-1 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 73.4% | 71.3% | 1.41 | +3.4% |
| Draw | 15.8% | 17.0% | 5.56 | -12.1% |
| Fiorentina win | 10.8% | 11.7% | 7.90 | -14.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T11:30:00+00:00 |
| Fixture id | c9b6c7048d8dc33dae618f67f462f67a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T13:11:12Z |
| Market best draw last update utc | 2026-10-15T13:11:12Z |
| Market best away last update utc | 2026-10-15T13:11:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.9% |
| P btts no | 42.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.25 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.70 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.48 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.20 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 75.4% |
| Unadjusted draw probability | 14.6% |
| Unadjusted away-win probability | 9.9% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 48.9% |
| Raw p btts yes | 57.4% |
| P home draw | 89.2% |
| P draw away | 26.6% |
| P home away | 84.2% |
| Raw p home draw | 90.1% |
| Raw p draw away | 24.6% |
| Raw p home away | 85.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.36 |
| Reference draw odds | 5.00 |
| Reference away odds | 7.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | +2.1% |
| Draw probability edge | -1.2% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | 0.0416 |
| Raw ev home | 0.0637 |
| Raw edge prob draw | -0.0238 |
| Raw ev draw | -0.1876 |
| Raw edge prob away | -0.0178 |
| Raw ev away | -0.2142 |

</details>


---
