# Serie A — football model report

Fixtures in this report: **14**.

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
| Live odds matched | 14.00 |
| Additional event odds calls used before this league | 16.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 3.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 3.00 |
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

The model's most likely 1X2 outcome is **Frosinone win** at **42.0%**. Expected goals are 1.64 for Frosinone and 1.29 for Sassuolo (2.94 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 56.2%; Under 3.5 goals: 66.3%; Double Chance 1X: 66.5%; Double Chance X2: 58.0%; Under 4.5 goals: 82.6%; BTTS Yes (both teams score): 58.8%; BTTS No (at least one team does not score): 41.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 42.0% | 2.38 |
| Draw | 24.5% | 4.09 |
| Sassuolo win | 33.5% | 2.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.64 |
| Sassuolo expected goals | 1.29 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 56.2% |
| Under 2.5 | 43.8% |
| Over 3.5 | 33.7% |
| Under 3.5 | 66.3% |
| Over 4.5 | 17.4% |
| Under 4.5 | 82.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.42% |
| 2 | 2-1 | 8.58% |
| 3 | 1-2 | 8.16% |
| 4 | 1-0 | 7.86% |
| 5 | 0-1 | 7.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 42.0% | 38.7% | 2.63 | +10.5% |
| Draw | 24.5% | 24.3% | 3.65 | -10.7% |
| Sassuolo win | 33.5% | 37.1% | 2.77 | -7.2% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.8% |
| P btts no | 41.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.16 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 2.97 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.76 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 45.4% |
| Unadjusted draw probability | 24.7% |
| Unadjusted away-win probability | 30.0% |
| Raw p over 1 5 | 79.3% |
| Raw p under 3 5 | 66.2% |
| Raw p btts yes | 58.8% |
| P home draw | 66.5% |
| P draw away | 58.0% |
| Raw p home draw | 70.0% |
| Raw p draw away | 54.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.45 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.55 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | +3.4% |
| Draw probability edge | +0.2% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | 0.0671 |
| Raw ev home | 0.1934 |
| Raw edge prob draw | 0.0040 |
| Raw ev draw | -0.0995 |
| Raw edge prob away | -0.0711 |
| Raw ev away | -0.1704 |
| Market p home draw | 64.5% |
| Market home draw odds | 1.50 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:12:37Z |
| Market reference home draw last update utc | 2026-10-14T18:12:43Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.8% |
| Market draw away odds | 1.55 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:12:37Z |
| Market reference draw away last update utc | 2026-10-14T18:12:43Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.49 |
| Market reference dc draw away odds | 1.53 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 87.4% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T18:12:51Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 4.95 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.5% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T18:12:51Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.20 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:12:37Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 3.10 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **69.9%**. Expected goals are 1.97 for AS Roma and 0.64 for Genoa (2.61 combined). The most likely exact score is 2-0 at 14.5%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 49.1%; Under 3.5 goals: 73.2%; Double Chance 1X: 88.5%; Double Chance X2: 30.1%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 40.4%; BTTS No (at least one team does not score): 59.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 69.9% | 1.43 |
| Draw | 18.7% | 5.36 |
| Genoa win | 11.5% | 8.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.97 |
| Genoa expected goals | 0.64 |
| Expected total goals | 2.61 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 49.1% |
| Under 2.5 | 50.9% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.51% |
| 2 | 1-0 | 14.50% |
| 3 | 3-0 | 9.55% |
| 4 | 2-1 | 9.27% |
| 5 | 1-1 | 8.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 69.9% | 71.0% | 1.42 | -0.7% |
| Draw | 18.7% | 17.0% | 5.06 | -5.6% |
| Genoa win | 11.5% | 12.0% | 8.75 | +0.2% |
| Over 2.5 | 49.1% | 56.1% | 1.76 | -13.6% |
| Under 2.5 | 50.9% | 43.9% | 2.23 | +13.5% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| P btts yes | 40.4% |
| P btts no | 59.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.48 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.91 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.8% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 10.9% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 40.9% |
| P home draw | 88.5% |
| P draw away | 30.1% |
| Raw p home draw | 89.1% |
| Raw p draw away | 31.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.37 |
| Reference draw odds | 5.10 |
| Reference away odds | 7.00 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.22 |
| Home probability edge | -1.1% |
| Draw probability edge | +1.7% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | -0.0219 |
| Raw ev home | -0.0230 |
| Raw edge prob draw | 0.0334 |
| Raw ev draw | 0.0283 |
| Raw edge prob away | -0.0116 |
| Raw ev away | -0.0486 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.9%**. Expected goals are 1.08 for Bologna and 2.13 for Inter Milan (3.20 combined). The most likely exact score is 1-2 at 10.0%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 62.0%; Under 3.5 goals: 60.1%; Double Chance 1X: 38.1%; Double Chance X2: 82.9%; Under 4.5 goals: 78.0%; BTTS Yes (both teams score): 58.2%; BTTS No (at least one team does not score): 41.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.1% | 5.83 |
| Draw | 20.9% | 4.78 |
| Inter Milan win | 61.9% | 1.61 |

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
| Over 2.5 | 62.0% |
| Under 2.5 | 38.0% |
| Over 3.5 | 39.9% |
| Under 3.5 | 60.1% |
| Over 4.5 | 22.0% |
| Under 4.5 | 78.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.01% |
| 2 | 1-1 | 9.62% |
| 3 | 0-2 | 9.31% |
| 4 | 0-1 | 8.56% |
| 5 | 1-3 | 7.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.1% | 16.1% | 5.82 | -0.2% |
| Draw | 20.9% | 21.2% | 4.22 | -11.7% |
| Inter Milan win | 61.9% | 62.7% | 1.65 | +2.2% |
| Over 2.5 | 62.0% | 59.3% | 1.71 | +6.1% |
| Under 2.5 | 38.0% | 40.7% | 2.33 | -11.5% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| P btts yes | 58.2% |
| P btts no | 41.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.15 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.94 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.55 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.1% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 61.2% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 60.2% |
| Raw p btts yes | 58.2% |
| P home draw | 38.1% |
| P draw away | 82.9% |
| Raw p home draw | 38.8% |
| Raw p draw away | 81.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 5.40 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.54 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | +1.0% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +2.7% |
| Under 2.5 probability edge | -2.7% |
| Raw edge prob home | 0.0201 |
| Raw ev home | 0.0561 |
| Raw edge prob draw | -0.0052 |
| Raw ev draw | -0.1284 |
| Raw edge prob away | -0.0149 |
| Raw ev away | 0.0098 |
| Market p home draw | 41.3% |
| Market home draw odds | 2.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:12:37Z |
| Market reference home draw last update utc | 2026-10-14T18:13:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 82.6% |
| Market draw away odds | 1.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:12:37Z |
| Market reference draw away last update utc | 2026-10-14T18:13:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.30 |
| Market reference dc draw away odds | 1.15 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 81.0% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T18:12:52Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T18:12:52Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:12:37Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.15 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **66.0%**. Expected goals are 0.67 for Venezia and 2.30 for Napoli (2.96 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 54.9%; Under 3.5 goals: 67.2%; Double Chance 1X: 34.0%; Double Chance X2: 85.5%; Under 4.5 goals: 83.2%; BTTS Yes (both teams score): 45.2%; BTTS No (at least one team does not score): 54.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 14.5% | 6.92 |
| Draw | 19.5% | 5.12 |
| Napoli win | 66.0% | 1.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.30 |
| Expected total goals | 2.96 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.9% |
| Under 2.5 | 45.1% |
| Over 3.5 | 32.8% |
| Under 3.5 | 67.2% |
| Over 4.5 | 16.8% |
| Under 4.5 | 83.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.15% |
| 2 | 0-1 | 10.44% |
| 3 | 0-3 | 9.30% |
| 4 | 1-1 | 9.27% |
| 5 | 1-2 | 8.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 14.5% | 19.9% | 5.04 | -27.2% |
| Draw | 19.5% | 22.0% | 4.32 | -15.7% |
| Napoli win | 66.0% | 58.1% | 1.71 | +12.9% |
| Over 2.5 | 54.9% | 56.3% | 1.74 | -4.5% |
| Under 2.5 | 45.1% | 43.7% | 2.27 | +2.4% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| P btts yes | 45.2% |
| P btts no | 54.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.34 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.58 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.05 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.95 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 9.0% |
| Unadjusted draw probability | 17.0% |
| Unadjusted away-win probability | 74.0% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 43.9% |
| P home draw | 34.0% |
| P draw away | 85.5% |
| Raw p home draw | 26.0% |
| Raw p draw away | 91.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.50 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.66 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.26 |
| Home probability edge | -5.5% |
| Draw probability edge | -2.5% |
| Away probability edge | +8.0% |
| Over 2.5 probability edge | -1.4% |
| Under 2.5 probability edge | +1.4% |
| Raw edge prob home | -0.1094 |
| Raw ev home | -0.5472 |
| Raw edge prob draw | -0.0500 |
| Raw ev draw | -0.2649 |
| Raw edge prob away | 0.1594 |
| Raw ev away | 0.2654 |
| Market p home draw | 43.6% |
| Market home draw odds | 2.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:12:37Z |
| Market reference home draw last update utc | 2026-10-14T18:13:26Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 79.5% |
| Market draw away odds | 1.21 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:12:37Z |
| Market reference draw away last update utc | 2026-10-14T18:13:26Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.15 |
| Market reference dc draw away odds | 1.18 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.4% |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 54.7% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:12:37Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.05 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **46.2%**. Expected goals are 1.29 for AC Milan and 1.15 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 12.8%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 44.8%; Under 3.5 goals: 76.9%; Double Chance 1X: 72.1%; Double Chance X2: 53.8%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 49.3%; BTTS No (at least one team does not score): 50.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 46.2% | 2.17 |
| Draw | 26.0% | 3.85 |
| Atalanta BC win | 27.9% | 3.59 |

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
| Over 2.5 | 44.8% |
| Under 2.5 | 55.2% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.83% |
| 2 | 1-1 | 12.31% |
| 3 | 2-1 | 9.75% |
| 4 | 2-0 | 8.49% |
| 5 | 0-0 | 8.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 46.2% | 52.8% | 1.93 | -10.9% |
| Draw | 26.0% | 24.1% | 3.86 | +0.2% |
| Atalanta BC win | 27.9% | 23.1% | 4.22 | +17.6% |
| Over 2.5 | 44.8% | 54.8% | 1.83 | -18.1% |
| Under 2.5 | 55.2% | 45.2% | 2.13 | +17.6% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| Fair Under 0.5 odds | 11.94 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.32 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.69 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.8% |
| P home draw | 72.1% |
| P draw away | 53.8% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.82 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.95 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | -6.6% |
| Draw probability edge | +1.9% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | -0.1328 |
| Raw ev home | -0.2372 |
| Raw edge prob draw | 0.0376 |
| Raw ev draw | 0.0750 |
| Raw edge prob away | 0.0952 |
| Raw ev away | 0.3769 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **51.2%**. Expected goals are 0.96 for Fiorentina and 1.71 for Como (2.67 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 49.5%; Under 3.5 goals: 72.5%; Double Chance 1X: 48.8%; Double Chance X2: 75.9%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.1% | 4.14 |
| Draw | 24.7% | 4.05 |
| Como win | 51.2% | 1.95 |

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
| 1 | 1-1 | 11.76% |
| 2 | 0-1 | 10.88% |
| 3 | 0-2 | 9.47% |
| 4 | 1-2 | 9.08% |
| 5 | 1-0 | 7.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.1% | 27.4% | 3.54 | -14.6% |
| Draw | 24.7% | 25.0% | 3.81 | -5.9% |
| Como win | 51.2% | 47.6% | 2.12 | +8.5% |
| Over 2.5 | 49.5% | 57.4% | 1.73 | -14.4% |
| Under 2.5 | 50.5% | 42.6% | 2.29 | +15.7% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| Fair Under 0.5 odds | 13.73 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.91 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.68 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 50.7% |
| P home draw | 48.8% |
| P draw away | 75.9% |
| Raw p home draw | 45.3% |
| Raw p draw away | 79.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.35 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | -3.3% |
| Draw probability edge | -0.3% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -7.9% |
| Under 2.5 probability edge | +7.9% |
| Raw edge prob home | -0.0654 |
| Raw ev home | -0.2616 |
| Raw edge prob draw | -0.0058 |
| Raw ev draw | -0.0697 |
| Raw edge prob away | 0.0712 |
| Raw ev away | 0.1601 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **53.2%**. Expected goals are 1.37 for Juventus and 0.87 for Lazio (2.23 combined). The most likely exact score is 1-0 at 15.8%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 39.6%; Under 3.5 goals: 80.9%; Double Chance 1X: 78.9%; Double Chance X2: 46.8%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.8%; BTTS No (at least one team does not score): 57.2%.

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
| Over 2.5 | 39.6% | 48.5% | 2.03 | -19.6% |
| Under 2.5 | 60.4% | 51.5% | 1.92 | +15.9% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| Raw p home draw | 76.5% |
| Raw p draw away | 51.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.66 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.89 |
| Home probability edge | -4.9% |
| Draw probability edge | +2.5% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | -0.0984 |
| Raw ev home | -0.1843 |
| Raw edge prob draw | 0.0496 |
| Raw ev draw | 0.1404 |
| Raw edge prob away | 0.0488 |
| Raw ev away | 0.3424 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.8%**. Expected goals are 1.46 for Udinese and 0.83 for Lecce (2.29 combined). The most likely exact score is 1-0 at 14.6%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 40.4%; Under 3.5 goals: 80.1%; Double Chance 1X: 78.1%; Double Chance X2: 48.2%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 43.4%; BTTS No (at least one team does not score): 56.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.8% | 1.93 |
| Draw | 26.3% | 3.81 |
| Lecce win | 21.9% | 4.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.46 |
| Lecce expected goals | 0.83 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.4% |
| Under 2.5 | 59.6% |
| Over 3.5 | 19.9% |
| Under 3.5 | 80.1% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.57% |
| 2 | 1-1 | 12.12% |
| 3 | 2-0 | 10.80% |
| 4 | 0-0 | 10.04% |
| 5 | 2-1 | 8.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.8% | 52.0% | 1.95 | +1.0% |
| Draw | 26.3% | 25.3% | 3.65 | -4.1% |
| Lecce win | 21.9% | 22.6% | 4.38 | -4.0% |
| Over 2.5 | 40.4% | 46.5% | 2.08 | -16.0% |
| Under 2.5 | 59.6% | 53.5% | 1.87 | +11.5% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| P btts yes | 43.4% |
| P btts no | 56.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.96 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.03 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.03 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.02 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 43.6% |
| P home draw | 78.1% |
| P draw away | 48.2% |
| Raw p home draw | 78.8% |
| Raw p draw away | 48.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.84 |
| Reference draw odds | 3.60 |
| Reference away odds | 4.00 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | -0.2% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.0045 |
| Raw ev home | 0.0058 |
| Raw edge prob draw | 0.0187 |
| Raw ev draw | -0.0069 |
| Raw edge prob away | -0.0142 |
| Raw ev away | -0.0709 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.6%**. Expected goals are 1.13 for Monza and 1.62 for Cagliari (2.75 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 51.0%; Under 3.5 goals: 70.9%; Double Chance 1X: 60.4%; Double Chance X2: 66.3%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 33.7% | 2.97 |
| Draw | 26.7% | 3.74 |
| Cagliari win | 39.6% | 2.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.13 |
| Cagliari expected goals | 1.62 |
| Expected total goals | 2.75 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.7% |
| Under 1.5 | 24.3% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.69% |
| 2 | 1-0 | 8.93% |
| 3 | 2-1 | 8.45% |
| 4 | 0-1 | 8.27% |
| 5 | 1-2 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.7% | 40.9% | 2.49 | -16.1% |
| Draw | 26.7% | 28.3% | 3.25 | -13.1% |
| Cagliari win | 39.6% | 30.8% | 3.25 | +28.7% |
| Over 2.5 | 51.0% | 45.9% | 2.15 | +9.6% |
| Under 2.5 | 49.0% | 54.1% | 1.82 | -10.8% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.17 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.43 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.13 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 26.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.3% |
| Raw p btts yes | 54.5% |
| P home draw | 60.4% |
| P draw away | 66.3% |
| Raw p home draw | 51.6% |
| Raw p draw away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.00 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.81 |
| Home probability edge | -7.3% |
| Draw probability edge | -1.5% |
| Away probability edge | +8.8% |
| Over 2.5 probability edge | +5.1% |
| Under 2.5 probability edge | -5.1% |
| Raw edge prob home | -0.1454 |
| Raw ev home | -0.3425 |
| Raw edge prob draw | -0.0307 |
| Raw ev draw | -0.1812 |
| Raw edge prob away | 0.1760 |
| Raw ev away | 0.5730 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.3%**. Expected goals are 1.00 for Parma and 1.10 for Torino (2.11 combined). The most likely exact score is 0-1 at 13.5%. Goal-market probabilities: at least one goal: 87.9%; Over 2.5 goals: 35.5%; Under 3.5 goals: 83.7%; Double Chance 1X: 61.7%; Double Chance X2: 67.9%; Under 4.5 goals: 93.7%; BTTS Yes (both teams score): 42.4%; BTTS No (at least one team does not score): 57.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 32.1% | 3.11 |
| Draw | 29.6% | 3.38 |
| Torino win | 38.3% | 2.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.00 |
| Torino expected goals | 1.10 |
| Expected total goals | 2.11 |
| Over 0.5 | 87.9% |
| Under 0.5 | 12.1% |
| Over 1.5 | 62.5% |
| Under 1.5 | 37.5% |
| Over 2.5 | 35.5% |
| Under 2.5 | 64.5% |
| Over 3.5 | 16.3% |
| Under 3.5 | 83.7% |
| Over 4.5 | 6.3% |
| Under 4.5 | 93.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.46% |
| 2 | 1-1 | 13.39% |
| 3 | 0-0 | 12.12% |
| 4 | 1-0 | 11.88% |
| 5 | 1-2 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 32.1% | 32.0% | 3.25 | +4.4% |
| Draw | 29.6% | 28.8% | 3.17 | -6.1% |
| Torino win | 38.3% | 39.2% | 2.54 | -2.8% |
| Over 2.5 | 35.5% | 39.8% | 2.48 | -12.0% |
| Under 2.5 | 64.5% | 60.2% | 1.63 | +5.2% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| P btts yes | 42.4% |
| P btts no | 57.6% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.25 |
| Fair Over 1.5 odds | 1.60 |
| Fair Under 1.5 odds | 2.67 |
| Fair Over 2.5 odds | 2.82 |
| Fair Under 2.5 odds | 1.55 |
| Fair Over 3.5 odds | 6.14 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 15.79 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.2% |
| Unadjusted draw probability | 30.4% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 62.5% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 42.6% |
| P home draw | 61.7% |
| P draw away | 67.9% |
| Raw p home draw | 62.6% |
| Raw p draw away | 67.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.46 |
| Reference Under 2.5 odds | 1.64 |
| Home probability edge | +0.1% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | 0.0023 |
| Raw ev home | 0.0475 |
| Raw edge prob draw | 0.0161 |
| Raw ev draw | -0.0358 |
| Raw edge prob away | -0.0184 |
| Raw ev away | -0.0513 |

</details>


---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **50.4%**. Expected goals are 1.94 for Torino and 1.18 for Monza (3.12 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 59.5%; Under 3.5 goals: 62.4%; Double Chance 1X: 74.8%; Double Chance X2: 49.6%; Under 4.5 goals: 79.9%; BTTS Yes (both teams score): 60.2%; BTTS No (at least one team does not score): 39.8%.

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
| Over 2.5 | 59.5% | 48.5% | 2.11 | +25.6% |
| Under 2.5 | 40.5% | 51.5% | 1.85 | -25.1% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| Fair Under 0.5 odds | 19.87 |
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
| Raw p home draw | 77.4% |
| Raw p draw away | 45.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.86 |
| Home probability edge | +4.6% |
| Draw probability edge | -2.0% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | +11.0% |
| Under 2.5 probability edge | -11.0% |
| Raw edge prob home | 0.0919 |
| Raw ev home | 0.1825 |
| Raw edge prob draw | -0.0403 |
| Raw ev draw | -0.1892 |
| Raw edge prob away | -0.0515 |
| Raw ev away | -0.1773 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **38.8%**. Expected goals are 1.07 for Cagliari and 1.18 for Bologna (2.25 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.2%; Under 3.5 goals: 80.9%; Double Chance 1X: 61.2%; Double Chance X2: 67.8%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

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
| Over 2.5 | 39.2% | 43.5% | 2.24 | -12.1% |
| Under 2.5 | 60.8% | 56.5% | 1.76 | +7.0% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| Raw p home draw | 62.0% |
| Raw p draw away | 67.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.15 |
| Reference away odds | 2.35 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.17 |
| Reference Under 2.5 odds | 1.70 |
| Home probability edge | +0.6% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | 0.0124 |
| Raw ev home | 0.0982 |
| Raw edge prob draw | 0.0039 |
| Raw ev draw | -0.0851 |
| Raw edge prob away | -0.0163 |
| Raw ev away | -0.0426 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **64.7%**. Expected goals are 1.96 for Como and 0.91 for Sassuolo (2.87 combined). The most likely exact score is 1-0 at 11.5%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 55.5%; Under 3.5 goals: 67.4%; Double Chance 1X: 84.4%; Double Chance X2: 35.3%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 64.7% | 1.54 |
| Draw | 19.7% | 5.08 |
| Sassuolo win | 15.6% | 6.42 |

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
| Over 2.5 | 55.5% |
| Under 2.5 | 44.5% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.48% |
| 2 | 2-0 | 11.45% |
| 3 | 2-1 | 10.41% |
| 4 | 1-1 | 9.36% |
| 5 | 3-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 64.7% | 67.8% | 1.49 | -3.5% |
| Draw | 19.7% | 17.6% | 4.94 | -2.8% |
| Sassuolo win | 15.6% | 14.6% | 7.10 | +10.6% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.70 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.65 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.00 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 61.6% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 16.6% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 51.5% |
| P home draw | 84.4% |
| P draw away | 35.3% |
| Raw p home draw | 83.4% |
| Raw p draw away | 38.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.42 |
| Reference draw odds | 4.80 |
| Reference away odds | 5.70 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.52 |
| Home probability edge | -3.1% |
| Draw probability edge | +2.1% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | -0.0618 |
| Raw ev home | -0.0814 |
| Raw edge prob draw | 0.0414 |
| Raw ev draw | 0.0743 |
| Raw edge prob away | 0.0204 |
| Raw ev away | 0.1789 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **40.1%**. Expected goals are 1.04 for Napoli and 1.19 for AS Roma (2.23 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 38.9%; Under 3.5 goals: 81.3%; Double Chance 1X: 59.9%; Double Chance X2: 68.2%; Under 4.5 goals: 92.3%; BTTS Yes (both teams score): 44.9%; BTTS No (at least one team does not score): 55.1%.

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
| Over 2.5 | 38.9% | 51.4% | 1.93 | -24.9% |
| Under 2.5 | 61.1% | 48.6% | 2.01 | +22.8% |

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
| Market best home last update utc | 2026-10-14T18:12:37Z |
| Market best draw last update utc | 2026-10-14T18:12:37Z |
| Market best away last update utc | 2026-10-14T18:12:37Z |
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
| Fair Under 0.5 odds | 9.47 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.90 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.36 |
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
| Raw p home draw | 61.1% |
| Raw p draw away | 68.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.25 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | -0.1% |
| Draw probability edge | +1.3% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -12.5% |
| Under 2.5 probability edge | +12.5% |
| Raw edge prob home | -0.0019 |
| Raw ev home | -0.0353 |
| Raw edge prob draw | 0.0261 |
| Raw ev draw | 0.0576 |
| Raw edge prob away | -0.0242 |
| Raw ev away | -0.0472 |

</details>


---
