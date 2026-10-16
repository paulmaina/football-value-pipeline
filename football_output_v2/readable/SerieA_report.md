# Serie A — football model report

Fixtures in this report: **19**.

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
| Training sha256 | 80621aabc4748832a2597f51e5acf50b59b403a8fcdfc3362297a8635cc0f4ea |
| Optimizer objective | 849.586 |
| Base scoring parameter | 0.127 |
| Home-advantage parameter | 0.111 |
| Dixon-Coles low-score adjustment | -0.021 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 19.00 |
| Additional event odds calls used before this league | 27.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
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

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **65.8%**. Expected goals are 1.97 for AS Roma and 0.64 for Genoa (2.61 combined). The most likely exact score is 2-0 at 13.7%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.0%; Under 3.5 goals: 73.8%; Double Chance 1X: 86.6%; Double Chance X2: 34.2%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 87.8%; BTTS Yes (both teams score): 41.2%; BTTS No (at least one team does not score): 58.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 65.8% | 1.52 |
| Draw | 20.8% | 4.81 |
| Genoa win | 13.4% | 7.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.97 |
| Genoa expected goals | 0.64 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 73.1% |
| Under 1.5 | 26.9% |
| Over 2.5 | 48.0% |
| Under 2.5 | 52.0% |
| Over 3.5 | 26.2% |
| Under 3.5 | 73.8% |
| Over 4.5 | 12.2% |
| Under 4.5 | 87.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.66% |
| 2 | 1-0 | 13.65% |
| 3 | 1-1 | 9.67% |
| 4 | 3-0 | 8.99% |
| 5 | 2-1 | 8.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 65.8% | 62.8% | 1.58 | +4.0% |
| Draw | 20.8% | 21.3% | 4.43 | -7.8% |
| Genoa win | 13.4% | 15.9% | 6.44 | -13.7% |
| Over 2.5 | 48.0% | 51.2% | 1.83 | -12.2% |
| Under 2.5 | 52.0% | 48.8% | 2.14 | +11.4% |

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
| Market best home last update utc | 2026-10-16T22:15:12Z |
| Market best draw last update utc | 2026-10-16T22:15:12Z |
| Market best away last update utc | 2026-10-16T22:15:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.99 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.72 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.82 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.20 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.8% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 10.9% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 40.9% |
| P home draw | 86.6% |
| P draw away | 34.2% |
| P home away | 79.2% |
| Raw p home draw | 89.1% |
| Raw p draw away | 31.2% |
| Raw p home away | 79.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.54 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.50 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:12Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:12Z |
| Home probability edge | +3.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | 0.0602 |
| Raw ev home | 0.0872 |
| Raw edge prob draw | -0.0097 |
| Raw ev draw | -0.0998 |
| Raw edge prob away | -0.0505 |
| Raw ev away | -0.2999 |
| Market p home draw | 84.4% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:15:12Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 38.6% |
| Market draw away odds | 2.56 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:15:12Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.0% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:15:12Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.51 |
| Market reference dc home draw odds | 1.15 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 77.1% |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 4.05 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:13Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 70.3% |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.12 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:37Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 49.4% |
| Market btts yes odds | 1.82 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:15:12Z |
| Market reference btts yes odds | 2.00 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-10-16T22:15:51Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **62.0%**. Expected goals are 1.08 for Bologna and 2.13 for Inter Milan (3.20 combined). The most likely exact score is 1-2 at 10.0%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 62.1%; Under 3.5 goals: 60.1%; Double Chance 1X: 38.0%; Double Chance X2: 82.8%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 78.0%; BTTS Yes (both teams score): 58.2%; BTTS No (at least one team does not score): 41.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.2% | 5.80 |
| Draw | 20.7% | 4.82 |
| Inter Milan win | 62.0% | 1.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.08 |
| Inter Milan expected goals | 2.13 |
| Expected total goals | 3.20 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 39.9% |
| Under 3.5 | 60.1% |
| Over 4.5 | 22.0% |
| Under 4.5 | 78.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.03% |
| 2 | 1-1 | 9.54% |
| 3 | 0-2 | 9.32% |
| 4 | 0-1 | 8.57% |
| 5 | 1-3 | 7.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.2% | 16.3% | 5.99 | +3.2% |
| Draw | 20.7% | 20.8% | 4.21 | -12.7% |
| Inter Milan win | 62.0% | 62.9% | 1.64 | +1.7% |
| Over 2.5 | 62.1% | 57.2% | 1.73 | +7.4% |
| Under 2.5 | 37.9% | 42.8% | 2.28 | -13.5% |

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
| Market best home last update utc | 2026-10-16T22:15:12Z |
| Market best draw last update utc | 2026-10-16T22:15:12Z |
| Market best away last update utc | 2026-10-16T22:15:12Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 58.2% |
| P btts no | 41.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.35 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.95 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.54 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.1% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 61.2% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 60.2% |
| Raw p btts yes | 58.2% |
| P home draw | 38.0% |
| P draw away | 82.8% |
| P home away | 79.3% |
| Raw p home draw | 38.8% |
| Raw p draw away | 81.9% |
| Raw p home away | 79.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 5.40 |
| Reference draw odds | 4.30 |
| Reference away odds | 1.54 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:12Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:12Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | +4.9% |
| Under 2.5 probability edge | -4.9% |
| Raw edge prob home | 0.0184 |
| Raw ev home | 0.0870 |
| Raw edge prob draw | -0.0018 |
| Raw ev draw | -0.1305 |
| Raw edge prob away | -0.0166 |
| Raw ev away | 0.0037 |
| Market p home draw | 38.3% |
| Market home draw odds | 2.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:15:12Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.9% |
| Market draw away odds | 1.16 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:15:12Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.8% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:15:12Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.14 |
| Market reference dc home draw odds | 2.53 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 82.4% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:15:58Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:58Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.3% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:15:58Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.56 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:58Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.0% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:15:12Z |
| Market reference btts yes odds | 1.77 |
| Market reference btts yes opposite odds | 2.24 |
| Market reference btts yes last update utc | 2026-10-16T22:15:51Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **65.6%**. Expected goals are 0.67 for Venezia and 2.30 for Napoli (2.96 combined). The most likely exact score is 0-2 at 12.1%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.8%; Under 3.5 goals: 67.3%; Double Chance 1X: 34.4%; Double Chance X2: 85.4%; Double Chance 12 (either team wins): 80.2%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 45.3%; BTTS No (at least one team does not score): 54.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 14.6% | 6.83 |
| Draw | 19.8% | 5.06 |
| Napoli win | 65.6% | 1.52 |

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
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.07% |
| 2 | 0-1 | 10.37% |
| 3 | 1-1 | 9.38% |
| 4 | 0-3 | 9.24% |
| 5 | 1-2 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 14.6% | 20.3% | 4.89 | -28.4% |
| Draw | 19.8% | 22.5% | 4.22 | -16.6% |
| Napoli win | 65.6% | 57.2% | 1.74 | +14.2% |
| Over 2.5 | 54.8% | 56.9% | 1.77 | -3.1% |
| Under 2.5 | 45.2% | 43.1% | 2.22 | +0.4% |

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
| Market best home last update utc | 2026-10-16T22:15:12Z |
| Market best draw last update utc | 2026-10-16T22:15:12Z |
| Market best away last update utc | 2026-10-16T22:15:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 45.3% |
| P btts no | 54.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.14 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.56 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.05 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.97 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 9.0% |
| Unadjusted draw probability | 17.0% |
| Unadjusted away-win probability | 74.0% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 43.9% |
| P home draw | 34.4% |
| P draw away | 85.4% |
| P home away | 80.2% |
| Raw p home draw | 26.0% |
| Raw p draw away | 91.0% |
| Raw p home away | 83.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.40 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.68 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.17 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:12Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:12Z |
| Home probability edge | -5.7% |
| Draw probability edge | -2.7% |
| Away probability edge | +8.4% |
| Over 2.5 probability edge | -2.2% |
| Under 2.5 probability edge | +2.2% |
| Raw edge prob home | -0.1131 |
| Raw ev home | -0.5606 |
| Raw edge prob draw | -0.0547 |
| Raw ev draw | -0.2819 |
| Raw edge prob away | 0.1679 |
| Raw ev away | 0.2876 |
| Market p home draw | 43.2% |
| Market home draw odds | 2.21 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:15:12Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.0% |
| Market draw away odds | 1.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:15:12Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.8% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:15:12Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.21 |
| Market reference dc home draw odds | 2.24 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 78.9% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 4.35 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:13Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 68.2% |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 2.92 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:37Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 56.1% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:15:12Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.24 |
| Market reference btts yes last update utc | 2026-10-16T22:15:51Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **47.1%**. Expected goals are 1.29 for AC Milan and 1.15 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 44.9%; Under 3.5 goals: 76.8%; Double Chance 1X: 72.6%; Double Chance X2: 52.9%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 47.1% | 2.12 |
| Draw | 25.6% | 3.91 |
| Atalanta BC win | 27.4% | 3.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.29 |
| Atalanta BC expected goals | 1.15 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 70.5% |
| Under 1.5 | 29.5% |
| Over 2.5 | 44.9% |
| Under 2.5 | 55.1% |
| Over 3.5 | 23.2% |
| Under 3.5 | 76.8% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.08% |
| 2 | 1-1 | 12.12% |
| 3 | 2-1 | 9.94% |
| 4 | 2-0 | 8.66% |
| 5 | 0-0 | 8.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 47.1% | 54.6% | 1.86 | -12.5% |
| Draw | 25.6% | 23.3% | 3.93 | +0.5% |
| Atalanta BC win | 27.4% | 22.1% | 4.46 | +22.0% |
| Over 2.5 | 44.9% | 55.6% | 1.81 | -18.7% |
| Under 2.5 | 55.1% | 44.4% | 2.16 | +19.0% |

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
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.12 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.32 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.65 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.8% |
| P home draw | 72.6% |
| P draw away | 52.9% |
| P home away | 74.4% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.5% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.76 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | -7.5% |
| Draw probability edge | +2.3% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | -0.1508 |
| Raw ev home | -0.2648 |
| Raw edge prob draw | 0.0454 |
| Raw ev draw | 0.0945 |
| Raw edge prob away | 0.1054 |
| Raw ev away | 0.4551 |
| Market p home draw | 78.7% |
| Market home draw odds | 1.25 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:15:13Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.3% |
| Market draw away odds | 2.04 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:15:13Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:15:13Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.09 |
| Market reference dc home draw odds | 1.23 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 78.8% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:13Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.7% |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.87 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:37Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.9% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:15:13Z |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.34 |
| Market reference btts yes last update utc | 2026-10-16T22:15:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.7%**. Expected goals are 0.96 for Fiorentina and 1.71 for Como (2.67 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 49.5%; Under 3.5 goals: 72.5%; Double Chance 1X: 49.3%; Double Chance X2: 75.3%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.7% | 4.05 |
| Draw | 24.6% | 4.06 |
| Como win | 50.7% | 1.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 0.96 |
| Como expected goals | 1.71 |
| Expected total goals | 2.67 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 74.4% |
| Under 1.5 | 25.6% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 27.5% |
| Under 3.5 | 72.5% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.73% |
| 2 | 0-1 | 10.77% |
| 3 | 0-2 | 9.38% |
| 4 | 1-2 | 8.99% |
| 5 | 1-0 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.7% | 28.5% | 3.54 | -12.6% |
| Draw | 24.6% | 24.9% | 3.81 | -6.1% |
| Como win | 50.7% | 46.6% | 2.12 | +7.4% |
| Over 2.5 | 49.5% | 58.5% | 1.73 | -14.4% |
| Under 2.5 | 50.5% | 41.5% | 2.29 | +15.7% |

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
| Market best home last update utc | 2026-10-16T22:15:12Z |
| Market best draw last update utc | 2026-10-16T22:15:12Z |
| Market best away last update utc | 2026-10-16T22:15:12Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.77 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.90 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.69 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 50.7% |
| P home draw | 49.3% |
| P draw away | 75.3% |
| P home away | 75.4% |
| Raw p home draw | 45.3% |
| Raw p draw away | 79.1% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.25 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:12Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:12Z |
| Home probability edge | -3.8% |
| Draw probability edge | -0.2% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.0768 |
| Raw ev home | -0.2615 |
| Raw edge prob draw | -0.0045 |
| Raw ev draw | -0.0697 |
| Raw edge prob away | 0.0812 |
| Raw ev away | 0.1601 |
| Market p home draw | 54.2% |
| Market home draw odds | 1.80 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:15:12Z |
| Market reference home draw last update utc | 2026-10-16T22:15:48Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.5% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:15:12Z |
| Market reference draw away last update utc | 2026-10-16T22:15:48Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.3% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:15:12Z |
| Market reference home away last update utc | 2026-10-16T22:15:48Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.35 |
| Market reference dc home draw odds | 1.78 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 82.7% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:15:32Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.25 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.0% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:15:32Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.68 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:37Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.1% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:15:12Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.52 |
| Market reference btts yes last update utc | 2026-10-16T22:15:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **53.2%**. Expected goals are 1.37 for Juventus and 0.87 for Lazio (2.23 combined). The most likely exact score is 1-0 at 15.8%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 39.6%; Under 3.5 goals: 80.9%; Double Chance 1X: 78.9%; Double Chance X2: 46.8%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.8%; BTTS No (at least one team does not score): 57.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 53.2% | 1.88 |
| Draw | 25.7% | 3.88 |
| Lazio win | 21.1% | 4.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.87 |
| Expected total goals | 2.23 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 39.6% |
| Under 2.5 | 60.4% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.84% |
| 2 | 1-1 | 11.82% |
| 3 | 2-0 | 11.03% |
| 4 | 0-0 | 10.01% |
| 5 | 2-1 | 9.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 53.2% | 58.1% | 1.69 | -10.1% |
| Draw | 25.7% | 23.3% | 4.04 | +4.0% |
| Lazio win | 21.1% | 18.6% | 5.71 | +20.3% |
| Over 2.5 | 39.6% | 48.7% | 2.03 | -19.6% |
| Under 2.5 | 60.4% | 51.3% | 1.92 | +15.9% |

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
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 42.8% |
| P btts no | 57.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.99 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.66 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 43.5% |
| P home draw | 78.9% |
| P draw away | 46.8% |
| P home away | 74.3% |
| Raw p home draw | 76.5% |
| Raw p draw away | 51.7% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.66 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.80 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.94 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | -4.9% |
| Draw probability edge | +2.5% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -9.1% |
| Under 2.5 probability edge | +9.1% |
| Raw edge prob home | -0.0984 |
| Raw ev home | -0.1843 |
| Raw edge prob draw | 0.0496 |
| Raw ev draw | 0.1404 |
| Raw edge prob away | 0.0488 |
| Raw ev away | 0.3423 |
| Market p home draw | 81.6% |
| Market home draw odds | 1.18 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:15:13Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.2% |
| Market draw away odds | 2.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:15:13Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.3% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:15:13Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.25 |
| Market reference dc home draw odds | 1.19 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 74.3% |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.56 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:37Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 73.6% |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.44 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:37Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 49.5% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:15:13Z |
| Market reference btts yes odds | 2.00 |
| Market reference btts yes opposite odds | 1.96 |
| Market reference btts yes last update utc | 2026-10-16T22:15:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.5%**. Expected goals are 1.46 for Udinese and 0.83 for Lecce (2.29 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 40.3%; Under 3.5 goals: 80.1%; Double Chance 1X: 78.0%; Double Chance X2: 48.5%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 43.4%; BTTS No (at least one team does not score): 56.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.5% | 1.94 |
| Draw | 26.5% | 3.77 |
| Lecce win | 22.0% | 4.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.46 |
| Lecce expected goals | 0.83 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.3% |
| Under 2.5 | 59.7% |
| Over 3.5 | 19.9% |
| Under 3.5 | 80.1% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.49% |
| 2 | 1-1 | 12.22% |
| 3 | 2-0 | 10.75% |
| 4 | 0-0 | 10.12% |
| 5 | 2-1 | 8.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.5% | 51.5% | 1.95 | +0.5% |
| Draw | 26.5% | 25.8% | 3.65 | -3.3% |
| Lecce win | 22.0% | 22.7% | 4.38 | -3.8% |
| Over 2.5 | 40.3% | 48.3% | 2.08 | -16.1% |
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
| Market best home last update utc | 2026-10-16T22:15:12Z |
| Market best draw last update utc | 2026-10-16T22:15:12Z |
| Market best away last update utc | 2026-10-16T22:15:12Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 43.4% |
| P btts no | 56.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.88 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.04 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.05 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 43.6% |
| P home draw | 78.0% |
| P draw away | 48.5% |
| P home away | 73.5% |
| Raw p home draw | 78.8% |
| Raw p draw away | 48.4% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.86 |
| Reference draw odds | 3.55 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:12Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:12Z |
| Home probability edge | +0.0% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | 0.0008 |
| Raw ev home | 0.0058 |
| Raw edge prob draw | 0.0141 |
| Raw ev draw | -0.0069 |
| Raw edge prob away | -0.0150 |
| Raw ev away | -0.0710 |
| Market p home draw | 77.4% |
| Market home draw odds | 1.25 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:15:12Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.3% |
| Market draw away odds | 1.95 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:15:12Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.3% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:15:12Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.96 |
| Market reference dc home draw odds | 1.25 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 72.5% |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.35 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:37Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 76.5% |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.81 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:37Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 51.0% |
| Market btts yes odds | 1.83 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:15:12Z |
| Market reference btts yes odds | 1.94 |
| Market reference btts yes opposite odds | 2.02 |
| Market reference btts yes last update utc | 2026-10-16T22:15:51Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.8%**. Expected goals are 1.13 for Monza and 1.62 for Cagliari (2.75 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 50.9%; Under 3.5 goals: 70.9%; Double Chance 1X: 60.2%; Double Chance X2: 66.6%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 33.4% | 3.00 |
| Draw | 26.9% | 3.72 |
| Cagliari win | 39.8% | 2.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.13 |
| Cagliari expected goals | 1.62 |
| Expected total goals | 2.75 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.76% |
| 2 | 1-0 | 8.84% |
| 3 | 2-1 | 8.37% |
| 4 | 0-1 | 8.30% |
| 5 | 1-2 | 7.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.4% | 40.3% | 2.49 | -16.9% |
| Draw | 26.9% | 28.6% | 3.25 | -12.6% |
| Cagliari win | 39.8% | 31.1% | 3.25 | +29.2% |
| Over 2.5 | 50.9% | 43.7% | 2.15 | +9.5% |
| Under 2.5 | 49.1% | 56.3% | 1.82 | -10.7% |

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
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.09 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.43 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.14 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 26.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.3% |
| Raw p btts yes | 54.5% |
| P home draw | 60.2% |
| P draw away | 66.6% |
| P home away | 73.1% |
| Raw p home draw | 51.6% |
| Raw p draw away | 73.6% |
| Raw p home away | 74.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.35 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.00 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | -7.0% |
| Draw probability edge | -1.7% |
| Away probability edge | +8.6% |
| Over 2.5 probability edge | +7.3% |
| Under 2.5 probability edge | -7.3% |
| Raw edge prob home | -0.1392 |
| Raw ev home | -0.3424 |
| Raw edge prob draw | -0.0338 |
| Raw ev draw | -0.1812 |
| Raw edge prob away | 0.1729 |
| Raw ev away | 0.5729 |
| Market p home draw | 69.5% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:15:13Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.1% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:15:13Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.5% |
| Market home away odds | 1.39 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:15:13Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.58 |
| Market reference dc home draw odds | 1.39 |
| Market reference dc home away odds | 1.39 |
| Market p over 1 5 | 73.6% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:14:40Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.45 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:37Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.7% |
| Market under 3 5 odds | 1.25 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:14:40Z |
| Market reference under 3 5 odds | 1.30 |
| Market reference under 3 5 opposite odds | 3.80 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:13Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.1% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:15:13Z |
| Market reference btts yes odds | 1.86 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-16T22:15:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **39.2%**. Expected goals are 1.00 for Parma and 1.10 for Torino (2.11 combined). The most likely exact score is 0-1 at 13.8%. Goal-market probabilities: at least one goal: 87.7%; Over 2.5 goals: 35.3%; Under 3.5 goals: 83.7%; Double Chance 1X: 60.8%; Double Chance X2: 69.3%; Double Chance 12 (either team wins): 69.9%; Under 4.5 goals: 93.7%; BTTS Yes (both teams score): 42.5%; BTTS No (at least one team does not score): 57.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 30.7% | 3.25 |
| Draw | 30.1% | 3.32 |
| Torino win | 39.2% | 2.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.00 |
| Torino expected goals | 1.10 |
| Expected total goals | 2.11 |
| Over 0.5 | 87.7% |
| Under 0.5 | 12.3% |
| Over 1.5 | 62.5% |
| Under 1.5 | 37.5% |
| Over 2.5 | 35.3% |
| Under 2.5 | 64.7% |
| Over 3.5 | 16.3% |
| Under 3.5 | 83.7% |
| Over 4.5 | 6.3% |
| Under 4.5 | 93.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.78% |
| 2 | 1-1 | 13.60% |
| 3 | 0-0 | 12.32% |
| 4 | 1-0 | 11.37% |
| 5 | 1-2 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 30.7% | 29.3% | 3.42 | +5.1% |
| Draw | 30.1% | 29.8% | 3.17 | -4.6% |
| Torino win | 39.2% | 41.0% | 2.45 | -4.0% |
| Over 2.5 | 35.3% | 39.8% | 2.48 | -12.4% |
| Under 2.5 | 64.7% | 60.2% | 1.63 | +5.4% |

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
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 42.5% |
| P btts no | 57.5% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.12 |
| Fair Over 1.5 odds | 1.60 |
| Fair Under 1.5 odds | 2.67 |
| Fair Over 2.5 odds | 2.83 |
| Fair Under 2.5 odds | 1.55 |
| Fair Over 3.5 odds | 6.14 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 15.86 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.2% |
| Unadjusted draw probability | 30.4% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 62.5% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 42.6% |
| P home draw | 60.8% |
| P draw away | 69.3% |
| P home away | 69.9% |
| Raw p home draw | 62.6% |
| Raw p draw away | 67.8% |
| Raw p home away | 69.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.15 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.35 |
| Reference Under 2.5 odds | 1.60 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | +1.5% |
| Draw probability edge | +0.3% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | 0.0297 |
| Raw ev home | 0.1023 |
| Raw edge prob draw | 0.0065 |
| Raw ev draw | -0.0358 |
| Raw edge prob away | -0.0363 |
| Raw ev away | -0.0849 |
| Market p home draw | 59.6% |
| Market home draw odds | 1.62 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:15:13Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.0% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:15:13Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 68.4% |
| Market home away odds | 1.41 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:15:13Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.34 |
| Market reference dc home draw odds | 1.62 |
| Market reference dc home away odds | 1.41 |
| Market p over 1 5 | 67.0% |
| Market reference over 1 5 odds | 1.46 |
| Market reference over 1 5 opposite odds | 2.86 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:37Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 80.9% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 4.75 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:13Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 48.7% |
| Market btts yes odds | 1.98 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:15:13Z |
| Market reference btts yes odds | 2.02 |
| Market reference btts yes opposite odds | 1.92 |
| Market reference btts yes last update utc | 2026-10-16T22:15:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **50.4%**. Expected goals are 1.94 for Torino and 1.18 for Monza (3.12 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 59.5%; Under 3.5 goals: 62.4%; Double Chance 1X: 74.8%; Double Chance X2: 49.6%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 79.9%; BTTS Yes (both teams score): 60.2%; BTTS No (at least one team does not score): 39.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 50.4% | 1.98 |
| Draw | 24.4% | 4.10 |
| Monza win | 25.2% | 3.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.94 |
| Monza expected goals | 1.18 |
| Expected total goals | 3.12 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 59.5% |
| Under 2.5 | 40.5% |
| Over 3.5 | 37.6% |
| Under 3.5 | 62.4% |
| Over 4.5 | 20.1% |
| Under 4.5 | 79.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.23% |
| 2 | 2-1 | 8.99% |
| 3 | 1-0 | 7.65% |
| 4 | 2-0 | 7.63% |
| 5 | 1-2 | 6.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 50.4% | 45.8% | 2.15 | +8.4% |
| Draw | 24.4% | 26.4% | 3.62 | -11.6% |
| Monza win | 25.2% | 27.8% | 3.64 | -8.3% |
| Over 2.5 | 59.5% | 44.2% | 2.11 | +25.6% |
| Under 2.5 | 40.5% | 55.8% | 1.85 | -25.1% |

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
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.2% |
| P btts no | 39.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.88 |
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
| P home draw | 74.8% |
| P draw away | 49.6% |
| P home away | 75.6% |
| Raw p home draw | 77.4% |
| Raw p draw away | 45.0% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | +4.6% |
| Draw probability edge | -2.0% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | +15.3% |
| Under 2.5 probability edge | -15.3% |
| Raw edge prob home | 0.0919 |
| Raw ev home | 0.1825 |
| Raw edge prob draw | -0.0403 |
| Raw ev draw | -0.1893 |
| Raw edge prob away | -0.0515 |
| Raw ev away | -0.1773 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **38.8%**. Expected goals are 1.07 for Cagliari and 1.18 for Bologna (2.25 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.2%; Under 3.5 goals: 80.9%; Double Chance 1X: 61.2%; Double Chance X2: 67.8%; Double Chance 12 (either team wins): 71.0%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 32.2% | 3.11 |
| Draw | 29.0% | 3.44 |
| Bologna win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.07 |
| Bologna expected goals | 1.18 |
| Expected total goals | 2.25 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 39.2% |
| Under 2.5 | 60.8% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.50% |
| 2 | 0-1 | 12.36% |
| 3 | 1-0 | 10.80% |
| 4 | 0-0 | 10.71% |
| 5 | 1-2 | 8.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 32.2% | 31.5% | 3.35 | +7.7% |
| Draw | 29.0% | 28.8% | 3.13 | -9.1% |
| Bologna win | 38.8% | 39.6% | 2.52 | -2.2% |
| Over 2.5 | 39.2% | 42.7% | 2.24 | -12.1% |
| Under 2.5 | 60.8% | 57.3% | 1.76 | +7.0% |

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
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.33 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.23 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.73 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 38.0% |
| Raw p over 1 5 | 66.1% |
| Raw p under 3 5 | 80.9% |
| Raw p btts yes | 45.9% |
| P home draw | 61.2% |
| P draw away | 67.8% |
| P home away | 71.0% |
| Raw p home draw | 62.0% |
| Raw p draw away | 67.2% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.15 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.17 |
| Reference Under 2.5 odds | 1.66 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | +0.6% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | 0.0124 |
| Raw ev home | 0.0982 |
| Raw edge prob draw | 0.0039 |
| Raw ev draw | -0.0852 |
| Raw edge prob away | -0.0163 |
| Raw ev away | -0.0427 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **65.1%**. Expected goals are 1.96 for Como and 0.91 for Sassuolo (2.87 combined). The most likely exact score is 1-0 at 11.5%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 55.6%; Under 3.5 goals: 67.3%; Double Chance 1X: 84.6%; Double Chance X2: 34.9%; Double Chance 12 (either team wins): 80.4%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 65.1% | 1.54 |
| Draw | 19.6% | 5.11 |
| Sassuolo win | 15.4% | 6.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 1.96 |
| Sassuolo expected goals | 0.91 |
| Expected total goals | 2.87 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 55.6% |
| Under 2.5 | 44.4% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.54% |
| 2 | 2-0 | 11.51% |
| 3 | 2-1 | 10.46% |
| 4 | 1-1 | 9.30% |
| 5 | 3-0 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 65.1% | 68.5% | 1.49 | -3.0% |
| Draw | 19.6% | 17.4% | 4.94 | -3.4% |
| Sassuolo win | 15.4% | 14.2% | 7.10 | +9.2% |

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
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.82 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.66 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.99 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 61.6% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 16.6% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 51.5% |
| P home draw | 84.6% |
| P draw away | 34.9% |
| P home away | 80.4% |
| Raw p home draw | 83.4% |
| Raw p draw away | 38.4% |
| Raw p home away | 78.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.41 |
| Reference draw odds | 4.90 |
| Reference away odds | 5.90 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.65 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:52Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:52Z |
| Home probability edge | -3.4% |
| Draw probability edge | +2.2% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | -0.0684 |
| Raw ev home | -0.0814 |
| Raw edge prob draw | 0.0438 |
| Raw ev draw | 0.0743 |
| Raw edge prob away | 0.0245 |
| Raw ev away | 0.1789 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **58.8%**. Expected goals are 1.36 for Lazio and 0.66 for Parma (2.02 combined). The most likely exact score is 1-0 at 19.5%. Goal-market probabilities: at least one goal: 88.2%; Over 2.5 goals: 34.2%; Under 3.5 goals: 84.9%; Double Chance 1X: 83.7%; Double Chance X2: 41.2%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 94.3%; BTTS Yes (both teams score): 35.2%; BTTS No (at least one team does not score): 64.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 58.8% | 1.70 |
| Draw | 24.9% | 4.01 |
| Parma win | 16.3% | 6.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.36 |
| Parma expected goals | 0.66 |
| Expected total goals | 2.02 |
| Over 0.5 | 88.2% |
| Under 0.5 | 11.8% |
| Over 1.5 | 60.9% |
| Under 1.5 | 39.1% |
| Over 2.5 | 34.2% |
| Under 2.5 | 65.8% |
| Over 3.5 | 15.1% |
| Under 3.5 | 84.9% |
| Over 4.5 | 5.7% |
| Under 4.5 | 94.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.54% |
| 2 | 2-0 | 13.47% |
| 3 | 0-0 | 11.76% |
| 4 | 1-1 | 10.58% |
| 5 | 2-1 | 8.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 58.8% | 64.0% | 1.58 | -7.1% |
| Draw | 24.9% | 21.2% | 4.33 | +7.9% |
| Parma win | 16.3% | 14.8% | 6.64 | +8.3% |
| Over 2.5 | 34.2% | 49.7% | 2.06 | -29.5% |
| Under 2.5 | 65.8% | 50.3% | 1.89 | +24.3% |

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
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 35.2% |
| P btts no | 64.8% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.50 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.56 |
| Fair Over 2.5 odds | 2.92 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.64 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 17.39 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 53.5% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 17.9% |
| Raw p over 1 5 | 60.2% |
| Raw p under 3 5 | 85.3% |
| Raw p btts yes | 36.2% |
| P home draw | 83.7% |
| P draw away | 41.2% |
| P home away | 75.1% |
| Raw p home draw | 82.1% |
| Raw p draw away | 46.5% |
| Raw p home away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.50 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.70 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | -5.3% |
| Draw probability edge | +3.7% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -15.5% |
| Under 2.5 probability edge | +15.5% |
| Raw edge prob home | -0.1052 |
| Raw ev home | -0.1544 |
| Raw edge prob draw | 0.0742 |
| Raw ev draw | 0.2394 |
| Raw edge prob away | 0.0310 |
| Raw ev away | 0.1857 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **40.1%**. Expected goals are 1.04 for Napoli and 1.19 for AS Roma (2.23 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 38.9%; Under 3.5 goals: 81.3%; Double Chance 1X: 59.9%; Double Chance X2: 68.2%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 92.3%; BTTS Yes (both teams score): 44.9%; BTTS No (at least one team does not score): 55.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 31.8% | 3.14 |
| Draw | 28.1% | 3.56 |
| AS Roma win | 40.1% | 2.49 |

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
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.99% |
| 2 | 0-1 | 12.88% |
| 3 | 1-0 | 10.98% |
| 4 | 0-0 | 10.56% |
| 5 | 1-2 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 31.8% | 31.9% | 3.04 | -3.2% |
| Draw | 28.1% | 26.8% | 3.60 | +1.1% |
| AS Roma win | 40.1% | 41.3% | 2.45 | -1.8% |
| Over 2.5 | 38.9% | 51.5% | 1.93 | -24.9% |
| Under 2.5 | 61.1% | 48.5% | 2.01 | +22.8% |

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
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 44.9% |
| P btts no | 55.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.47 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.90 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.35 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.05 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 31.7% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.4% |
| Raw p btts yes | 45.2% |
| P home draw | 59.9% |
| P draw away | 68.2% |
| P home away | 71.9% |
| Raw p home draw | 61.1% |
| Raw p draw away | 68.3% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | -0.1% |
| Draw probability edge | +1.3% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | -0.0019 |
| Raw ev home | -0.0354 |
| Raw edge prob draw | 0.0261 |
| Raw ev draw | 0.0575 |
| Raw edge prob away | -0.0242 |
| Raw ev away | -0.0471 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **55.5%**. Expected goals are 1.65 for Atalanta BC and 1.06 for Frosinone (2.71 combined). The most likely exact score is 1-0 at 11.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 51.8%; Under 3.5 goals: 70.9%; Double Chance 1X: 78.1%; Double Chance X2: 44.5%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 85.8%; BTTS Yes (both teams score): 52.2%; BTTS No (at least one team does not score): 47.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 55.5% | 1.80 |
| Draw | 22.6% | 4.42 |
| Frosinone win | 21.9% | 4.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 1.65 |
| Frosinone expected goals | 1.06 |
| Expected total goals | 2.71 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 51.8% |
| Under 2.5 | 48.2% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.2% |
| Under 4.5 | 85.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.70% |
| 2 | 1-1 | 10.77% |
| 3 | 2-1 | 10.43% |
| 4 | 2-0 | 9.89% |
| 5 | 0-0 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 55.5% | 59.8% | 1.68 | -6.8% |
| Draw | 22.6% | 20.3% | 4.53 | +2.6% |
| Frosinone win | 21.9% | 19.8% | 5.04 | +10.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 63aa6e3f679ee4c68de5b4bd8d3361bb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.2% |
| P btts no | 47.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.94 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.04 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 51.1% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 75.5% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 52.9% |
| P home draw | 78.1% |
| P draw away | 44.5% |
| P home away | 77.4% |
| Raw p home draw | 76.0% |
| Raw p draw away | 48.9% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.60 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:52Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:52Z |
| Home probability edge | -4.4% |
| Draw probability edge | +2.3% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -14.7% |
| Under 2.5 probability edge | +14.7% |
| Raw edge prob home | -0.0879 |
| Raw ev home | -0.1422 |
| Raw edge prob draw | 0.0463 |
| Raw ev draw | 0.1305 |
| Raw edge prob away | 0.0416 |
| Raw ev away | 0.2088 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **51.7%**. Expected goals are 1.76 for Genoa and 0.89 for Venezia (2.65 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.5%; Under 3.5 goals: 73.2%; Double Chance 1X: 76.6%; Double Chance X2: 48.3%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 51.7% | 1.93 |
| Draw | 24.9% | 4.02 |
| Venezia win | 23.4% | 4.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.76 |
| Venezia expected goals | 0.89 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.84% |
| 2 | 1-0 | 10.97% |
| 3 | 2-0 | 9.81% |
| 4 | 2-1 | 8.74% |
| 5 | 0-0 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 51.7% | 45.8% | 2.25 | +16.3% |
| Draw | 24.9% | 26.0% | 3.44 | -14.3% |
| Venezia win | 23.4% | 28.2% | 3.58 | -16.2% |
| Over 2.5 | 48.5% | 51.5% | 1.97 | -4.4% |
| Under 2.5 | 51.5% | 48.5% | 1.98 | +1.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 95cfaecfe96bb7ced1fb6af974a4110b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.05 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.97 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 57.6% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 74.4% |
| Raw p under 3 5 | 72.6% |
| Raw p btts yes | 49.0% |
| P home draw | 76.6% |
| P draw away | 48.3% |
| P home away | 75.1% |
| Raw p home draw | 81.4% |
| Raw p draw away | 42.4% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | +5.9% |
| Draw probability edge | -1.1% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -2.9% |
| Under 2.5 probability edge | +2.9% |
| Raw edge prob home | 0.1180 |
| Raw ev home | 0.2959 |
| Raw edge prob draw | -0.0218 |
| Raw ev draw | -0.1809 |
| Raw edge prob away | -0.0962 |
| Raw ev away | -0.3343 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **73.2%**. Expected goals are 2.78 for Inter Milan and 0.94 for Fiorentina (3.72 combined). The most likely exact score is 2-0 at 9.1%. Goal-market probabilities: at least one goal: 97.4%; Over 2.5 goals: 71.5%; Under 3.5 goals: 49.4%; Double Chance 1X: 88.3%; Double Chance X2: 26.8%; Double Chance 12 (either team wins): 84.9%; Under 4.5 goals: 68.6%; BTTS Yes (both teams score): 57.8%; BTTS No (at least one team does not score): 42.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 73.2% | 1.37 |
| Draw | 15.1% | 6.63 |
| Fiorentina win | 11.7% | 8.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.78 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.72 |
| Over 0.5 | 97.4% |
| Under 0.5 | 2.6% |
| Over 1.5 | 88.5% |
| Under 1.5 | 11.5% |
| Over 2.5 | 71.5% |
| Under 2.5 | 28.5% |
| Over 3.5 | 50.6% |
| Under 3.5 | 49.4% |
| Over 4.5 | 31.4% |
| Under 4.5 | 68.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.05% |
| 2 | 2-1 | 8.54% |
| 3 | 3-0 | 8.39% |
| 4 | 3-1 | 7.91% |
| 5 | 1-1 | 6.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 73.2% | 70.9% | 1.41 | +3.2% |
| Draw | 15.1% | 15.5% | 5.56 | -16.2% |
| Fiorentina win | 11.7% | 13.5% | 7.90 | -7.3% |

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
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 57.8% |
| P btts no | 42.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 38.01 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.66 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.50 |
| Fair Over 3.5 odds | 1.98 |
| Fair Under 3.5 odds | 2.02 |
| Fair Over 4.5 odds | 3.19 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 75.4% |
| Unadjusted draw probability | 14.6% |
| Unadjusted away-win probability | 9.9% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 48.9% |
| Raw p btts yes | 57.4% |
| P home draw | 88.3% |
| P draw away | 26.8% |
| P home away | 84.9% |
| Raw p home draw | 90.1% |
| Raw p draw away | 24.6% |
| Raw p home away | 85.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.36 |
| Reference draw odds | 5.30 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:52Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:52Z |
| Home probability edge | +2.3% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +4.0% |
| Under 2.5 probability edge | -4.0% |
| Raw edge prob home | 0.0450 |
| Raw ev home | 0.0638 |
| Raw edge prob draw | -0.0092 |
| Raw ev draw | -0.1877 |
| Raw edge prob away | -0.0358 |
| Raw ev away | -0.2143 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **66.3%**. Expected goals are 0.60 for Lecce and 1.65 for Juventus (2.26 combined). The most likely exact score is 0-1 at 18.1%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 40.5%; Under 3.5 goals: 80.4%; Double Chance 1X: 33.7%; Double Chance X2: 87.5%; Double Chance 12 (either team wins): 78.7%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 36.1%; BTTS No (at least one team does not score): 63.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 12.5% | 8.02 |
| Draw | 21.3% | 4.70 |
| Juventus win | 66.3% | 1.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.60 |
| Juventus expected goals | 1.65 |
| Expected total goals | 2.26 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 66.7% |
| Under 1.5 | 33.3% |
| Over 2.5 | 40.5% |
| Under 2.5 | 59.5% |
| Over 3.5 | 19.6% |
| Under 3.5 | 80.4% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.05% |
| 2 | 0-2 | 15.12% |
| 3 | 0-0 | 9.36% |
| 4 | 1-1 | 9.35% |
| 5 | 1-2 | 9.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 12.5% | 11.9% | 7.70 | -4.0% |
| Draw | 21.3% | 18.3% | 4.53 | -3.7% |
| Juventus win | 66.3% | 69.8% | 1.50 | -0.6% |
| Over 2.5 | 40.5% | 50.6% | 1.92 | -22.3% |
| Under 2.5 | 59.5% | 49.4% | 2.02 | +20.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:00:00+00:00 |
| Fixture id | 63af660d4d0d52f8ac7685172ef939c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 36.1% |
| P btts no | 63.9% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.68 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.01 |
| Fair Over 2.5 odds | 2.47 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.10 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.20 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 13.0% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 62.7% |
| Raw p over 1 5 | 66.1% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 36.9% |
| P home draw | 33.7% |
| P draw away | 87.5% |
| P home away | 78.7% |
| Raw p home draw | 37.3% |
| Raw p draw away | 87.0% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 6.75 |
| Reference draw odds | 4.60 |
| Reference away odds | 1.38 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.89 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | +0.6% |
| Draw probability edge | +3.0% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | 0.0112 |
| Raw ev home | 0.0027 |
| Raw edge prob draw | 0.0602 |
| Raw ev draw | 0.0994 |
| Raw edge prob away | -0.0713 |
| Raw ev away | -0.0594 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **51.3%**. Expected goals are 1.04 for Udinese and 1.57 for AC Milan (2.60 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.5%; Under 3.5 goals: 73.4%; Double Chance 1X: 48.7%; Double Chance X2: 76.6%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 23.4% | 4.27 |
| Draw | 25.2% | 3.96 |
| AC Milan win | 51.3% | 1.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.57 |
| Expected total goals | 2.60 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.02% |
| 2 | 0-1 | 11.80% |
| 3 | 1-2 | 9.79% |
| 4 | 0-2 | 9.45% |
| 5 | 0-0 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 23.4% | 22.0% | 4.68 | +9.7% |
| Draw | 25.2% | 24.7% | 3.91 | -1.3% |
| AC Milan win | 51.3% | 53.3% | 1.83 | -6.1% |
| Over 2.5 | 48.5% | 50.0% | 1.97 | -4.5% |
| Under 2.5 | 51.5% | 50.0% | 1.97 | +1.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 3564688383b255192409c9deb8e526ed |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:15:13Z |
| Market best draw last update utc | 2026-10-16T22:15:13Z |
| Market best away last update utc | 2026-10-16T22:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.33 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.06 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.9% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.4% |
| Raw p over 1 5 | 73.6% |
| Raw p under 3 5 | 73.5% |
| Raw p btts yes | 51.3% |
| P home draw | 48.7% |
| P draw away | 76.6% |
| P home away | 74.8% |
| Raw p home draw | 50.6% |
| Raw p draw away | 75.1% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.00 |
| Reference draw odds | 3.60 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:53Z |
| Market reference home last update utc | 2026-10-16T22:15:53Z |
| Market reference draw last update utc | 2026-10-16T22:15:53Z |
| Market reference away last update utc | 2026-10-16T22:15:53Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:53Z |
| Market best over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | +1.4% |
| Draw probability edge | +0.5% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | 0.0284 |
| Raw ev home | 0.1630 |
| Raw edge prob draw | 0.0110 |
| Raw ev draw | 0.0087 |
| Raw edge prob away | -0.0393 |
| Raw ev away | -0.0969 |

</details>


---
