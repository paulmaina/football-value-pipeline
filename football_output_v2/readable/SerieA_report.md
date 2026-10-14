# Serie A — football model report

Fixtures in this report: **11**.

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
| Live odds matched | 11.00 |
| Additional event odds calls used before this league | 2.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
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

The model's most likely 1X2 outcome is **Frosinone win** at **41.8%**. Expected goals are 1.64 for Frosinone and 1.29 for Sassuolo (2.94 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.8%; Under 3.5 goals: 66.3%; Double Chance 1X: 67.5%; Double Chance X2: 58.2%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 59.1%; BTTS No (at least one team does not score): 40.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 41.8% | 2.39 |
| Draw | 25.7% | 3.89 |
| Sassuolo win | 32.5% | 3.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.64 |
| Sassuolo expected goals | 1.29 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.8% |
| Under 2.5 | 44.2% |
| Over 3.5 | 33.7% |
| Under 3.5 | 66.3% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.00% |
| 2 | 2-1 | 8.53% |
| 3 | 1-2 | 7.92% |
| 4 | 1-0 | 7.81% |
| 5 | 0-1 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 41.8% | 38.2% | 2.63 | +9.9% |
| Draw | 25.7% | 26.7% | 3.65 | -6.2% |
| Sassuolo win | 32.5% | 35.1% | 2.77 | -10.0% |

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
| Market best home last update utc | 2026-10-14T11:21:32Z |
| Market best draw last update utc | 2026-10-14T11:21:32Z |
| Market best away last update utc | 2026-10-14T11:21:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.1% |
| P btts no | 40.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.30 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.97 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.82 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 45.4% |
| Unadjusted draw probability | 24.7% |
| Unadjusted away-win probability | 30.0% |
| Raw p over 1 5 | 79.3% |
| Raw p under 3 5 | 66.2% |
| Raw p btts yes | 58.8% |
| P home draw | 67.5% |
| P draw away | 58.2% |
| Raw p home draw | 70.0% |
| Raw p draw away | 54.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.54 |
| Reference draw odds | 3.59 |
| Reference away odds | 2.76 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.72 |
| Home probability edge | +3.6% |
| Draw probability edge | -1.0% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -10.8% |
| Under 2.5 probability edge | +10.8% |
| Raw edge prob home | 0.0717 |
| Raw ev home | 0.1934 |
| Raw edge prob draw | -0.0206 |
| Raw ev draw | -0.0995 |
| Raw edge prob away | -0.0511 |
| Raw ev away | -0.1704 |
| Market p home draw | 64.2% |
| Market home draw odds | 1.50 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T11:21:32Z |
| Market reference home draw last update utc | 2026-10-14T11:22:48Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.7% |
| Market draw away odds | 1.55 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T11:21:32Z |
| Market reference draw away last update utc | 2026-10-14T11:22:48Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.48 |
| Market reference dc draw away odds | 1.54 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 85.4% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 6.10 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 56.0% |
| Market reference under 3 5 odds | 1.74 |
| Market reference under 3 5 opposite odds | 2.19 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 70.4% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T11:21:32Z |
| Market reference btts yes odds | 1.39 |
| Market reference btts yes opposite odds | 3.14 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **69.8%**. Expected goals are 1.97 for AS Roma and 0.64 for Genoa (2.61 combined). The most likely exact score is 2-0 at 14.5%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 49.0%; Under 3.5 goals: 73.2%; Double Chance 1X: 88.9%; Double Chance X2: 30.2%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 40.5%; BTTS No (at least one team does not score): 59.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 69.8% | 1.43 |
| Draw | 19.0% | 5.25 |
| Genoa win | 11.1% | 8.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.97 |
| Genoa expected goals | 0.64 |
| Expected total goals | 2.61 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 49.0% |
| Under 2.5 | 51.0% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.50% |
| 2 | 1-0 | 14.49% |
| 3 | 3-0 | 9.54% |
| 4 | 2-1 | 9.26% |
| 5 | 1-1 | 8.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 69.8% | 70.9% | 1.42 | -0.8% |
| Draw | 19.0% | 17.8% | 5.06 | -3.7% |
| Genoa win | 11.1% | 11.4% | 8.75 | -2.6% |
| Over 2.5 | 49.0% | 56.4% | 1.76 | -13.8% |
| Under 2.5 | 51.0% | 43.6% | 2.23 | +13.7% |

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
| Market best home last update utc | 2026-10-14T11:21:32Z |
| Market best draw last update utc | 2026-10-14T11:21:32Z |
| Market best away last update utc | 2026-10-14T11:21:32Z |
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
| P btts yes | 40.5% |
| P btts no | 59.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.19 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.93 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.8% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 10.9% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 40.9% |
| P home draw | 88.9% |
| P draw away | 30.2% |
| Raw p home draw | 89.1% |
| Raw p draw away | 31.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.39 |
| Reference draw odds | 5.22 |
| Reference away odds | 7.98 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -1.0% |
| Draw probability edge | +1.3% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.0205 |
| Raw ev home | -0.0230 |
| Raw edge prob draw | 0.0257 |
| Raw ev draw | 0.0283 |
| Raw edge prob away | -0.0051 |
| Raw ev away | -0.0486 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.5%**. Expected goals are 1.08 for Bologna and 2.13 for Inter Milan (3.20 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.2%; Double Chance 1X: 38.5%; Double Chance X2: 83.3%; Under 4.5 goals: 78.2%; BTTS Yes (both teams score): 58.5%; BTTS No (at least one team does not score): 41.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 16.7% | 6.00 |
| Draw | 21.8% | 4.58 |
| Inter Milan win | 61.5% | 1.63 |

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
| 1 | 1-1 | 10.04% |
| 2 | 1-2 | 9.94% |
| 3 | 0-2 | 9.24% |
| 4 | 0-1 | 8.50% |
| 5 | 1-3 | 7.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 16.7% | 15.2% | 5.82 | -3.0% |
| Draw | 21.8% | 23.0% | 4.22 | -7.9% |
| Inter Milan win | 61.5% | 61.8% | 1.65 | +1.5% |
| Over 2.5 | 61.7% | 58.6% | 1.71 | +5.5% |
| Under 2.5 | 38.3% | 41.4% | 2.33 | -10.8% |

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
| Market best home last update utc | 2026-10-14T11:21:32Z |
| Market best draw last update utc | 2026-10-14T11:21:32Z |
| Market best away last update utc | 2026-10-14T11:21:32Z |
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
| Fair Under 0.5 odds | 22.20 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.94 |
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
| P home draw | 38.5% |
| P draw away | 83.3% |
| Raw p home draw | 38.8% |
| Raw p draw away | 81.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 6.15 |
| Reference draw odds | 4.13 |
| Reference away odds | 1.59 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.22 |
| Home probability edge | +1.5% |
| Draw probability edge | -1.2% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +3.1% |
| Under 2.5 probability edge | -3.1% |
| Raw edge prob home | 0.0294 |
| Raw ev home | 0.0561 |
| Raw edge prob draw | -0.0232 |
| Raw ev draw | -0.1284 |
| Raw edge prob away | -0.0062 |
| Raw ev away | 0.0098 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **66.2%**. Expected goals are 0.67 for Venezia and 2.30 for Napoli (2.96 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.8%; Under 3.5 goals: 67.1%; Double Chance 1X: 33.8%; Double Chance X2: 85.9%; Under 4.5 goals: 83.2%; BTTS Yes (both teams score): 45.3%; BTTS No (at least one team does not score): 54.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 14.1% | 7.10 |
| Draw | 19.8% | 5.06 |
| Napoli win | 66.2% | 1.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.30 |
| Expected total goals | 2.96 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.8% |
| Under 2.5 | 45.2% |
| Over 3.5 | 32.9% |
| Under 3.5 | 67.1% |
| Over 4.5 | 16.8% |
| Under 4.5 | 83.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.17% |
| 2 | 0-1 | 10.46% |
| 3 | 1-1 | 9.38% |
| 4 | 0-3 | 9.32% |
| 5 | 1-2 | 8.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 14.1% | 19.2% | 5.04 | -29.0% |
| Draw | 19.8% | 22.5% | 4.32 | -14.7% |
| Napoli win | 66.2% | 58.3% | 1.71 | +13.1% |
| Over 2.5 | 54.8% | 56.2% | 1.74 | -4.6% |
| Under 2.5 | 45.2% | 43.8% | 2.27 | +2.5% |

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
| Market best home last update utc | 2026-10-14T11:21:32Z |
| Market best draw last update utc | 2026-10-14T11:21:32Z |
| Market best away last update utc | 2026-10-14T11:21:32Z |
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
| Fair Under 0.5 odds | 16.14 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.59 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.04 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.95 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 9.0% |
| Unadjusted draw probability | 17.0% |
| Unadjusted away-win probability | 74.0% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 43.9% |
| P home draw | 33.8% |
| P draw away | 85.9% |
| Raw p home draw | 26.0% |
| Raw p draw away | 91.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 4.80 |
| Reference draw odds | 4.13 |
| Reference away odds | 1.67 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -5.1% |
| Draw probability edge | -2.7% |
| Away probability edge | +7.8% |
| Over 2.5 probability edge | -1.4% |
| Under 2.5 probability edge | +1.4% |
| Raw edge prob home | -0.1022 |
| Raw ev home | -0.5472 |
| Raw edge prob draw | -0.0548 |
| Raw ev draw | -0.2649 |
| Raw edge prob away | 0.1570 |
| Raw ev away | 0.2654 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **45.9%**. Expected goals are 1.29 for AC Milan and 1.15 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 12.8%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.9%; Double Chance 1X: 72.5%; Double Chance X2: 54.1%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 45.9% | 2.18 |
| Draw | 26.6% | 3.77 |
| Atalanta BC win | 27.5% | 3.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.29 |
| Atalanta BC expected goals | 1.15 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
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
| 1 | 1-0 | 12.77% |
| 2 | 1-1 | 12.59% |
| 3 | 2-1 | 9.71% |
| 4 | 0-0 | 8.57% |
| 5 | 2-0 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 45.9% | 52.4% | 1.93 | -11.3% |
| Draw | 26.6% | 25.3% | 3.86 | +2.5% |
| Atalanta BC win | 27.5% | 22.4% | 4.22 | +16.1% |
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
| Market best home last update utc | 2026-10-14T11:21:32Z |
| Market best draw last update utc | 2026-10-14T11:21:32Z |
| Market best away last update utc | 2026-10-14T11:21:32Z |
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
| Fair Under 0.5 odds | 11.67 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.74 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.8% |
| P home draw | 72.5% |
| P draw away | 54.1% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.85 |
| Reference draw odds | 3.70 |
| Reference away odds | 4.15 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | -6.4% |
| Draw probability edge | +1.3% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | -0.1284 |
| Raw ev home | -0.2372 |
| Raw edge prob draw | 0.0259 |
| Raw ev draw | 0.0750 |
| Raw edge prob away | 0.1024 |
| Raw ev away | 0.3769 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.5%**. Expected goals are 0.96 for Fiorentina and 1.71 for Como (2.67 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.6%; Double Chance 1X: 49.5%; Double Chance X2: 75.4%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.6% | 4.07 |
| Draw | 25.0% | 4.00 |
| Como win | 50.5% | 1.98 |

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
| 1 | 1-1 | 11.89% |
| 2 | 0-1 | 10.73% |
| 3 | 0-2 | 9.35% |
| 4 | 1-2 | 8.96% |
| 5 | 1-0 | 7.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.6% | 28.2% | 3.54 | -13.1% |
| Draw | 25.0% | 25.5% | 3.81 | -4.9% |
| Como win | 50.5% | 46.2% | 2.12 | +7.0% |
| Over 2.5 | 49.3% | 58.6% | 1.73 | -14.6% |
| Under 2.5 | 50.7% | 41.4% | 2.29 | +16.0% |

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
| Market best home last update utc | 2026-10-14T11:21:32Z |
| Market best draw last update utc | 2026-10-14T11:21:32Z |
| Market best away last update utc | 2026-10-14T11:21:32Z |
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
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.59 |
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
| P home draw | 49.5% |
| P draw away | 75.4% |
| Raw p home draw | 45.3% |
| Raw p draw away | 79.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 3.40 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.11 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.22 |
| Home probability edge | -3.7% |
| Draw probability edge | -0.6% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.0738 |
| Raw ev home | -0.2616 |
| Raw edge prob draw | -0.0111 |
| Raw ev draw | -0.0697 |
| Raw edge prob away | 0.0849 |
| Raw ev away | 0.1601 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **53.9%**. Expected goals are 1.37 for Juventus and 0.87 for Lazio (2.23 combined). The most likely exact score is 1-0 at 16.0%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 39.6%; Under 3.5 goals: 80.9%; Double Chance 1X: 79.9%; Double Chance X2: 46.1%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.8%; BTTS No (at least one team does not score): 57.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 53.9% | 1.86 |
| Draw | 26.0% | 3.85 |
| Lazio win | 20.1% | 4.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.87 |
| Expected total goals | 2.23 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
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
| 1 | 1-0 | 16.05% |
| 2 | 1-1 | 11.93% |
| 3 | 2-0 | 11.18% |
| 4 | 0-0 | 10.10% |
| 5 | 2-1 | 9.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 53.9% | 59.5% | 1.69 | -8.9% |
| Draw | 26.0% | 23.8% | 4.04 | +5.0% |
| Lazio win | 20.1% | 16.8% | 5.71 | +15.0% |
| Over 2.5 | 39.6% | 49.1% | 2.03 | -19.6% |
| Under 2.5 | 60.4% | 50.9% | 1.92 | +16.0% |

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
| Market best home last update utc | 2026-10-14T11:21:32Z |
| Market best draw last update utc | 2026-10-14T11:21:32Z |
| Market best away last update utc | 2026-10-14T11:21:32Z |
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
| Fair Under 0.5 odds | 9.90 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.24 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.66 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 43.5% |
| P home draw | 79.9% |
| P draw away | 46.1% |
| Raw p home draw | 76.5% |
| Raw p draw away | 51.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.65 |
| Reference draw odds | 4.00 |
| Reference away odds | 5.60 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.86 |
| Home probability edge | -5.6% |
| Draw probability edge | +2.2% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | -0.1123 |
| Raw ev home | -0.1843 |
| Raw edge prob draw | 0.0448 |
| Raw ev draw | 0.1404 |
| Raw edge prob away | 0.0675 |
| Raw ev away | 0.3424 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.6%**. Expected goals are 1.46 for Udinese and 0.83 for Lecce (2.29 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.1%; Double Chance 1X: 78.4%; Double Chance X2: 48.4%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 43.5%; BTTS No (at least one team does not score): 56.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.6% | 1.94 |
| Draw | 26.8% | 3.73 |
| Lecce win | 21.6% | 4.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.46 |
| Lecce expected goals | 0.83 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
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
| 2 | 1-1 | 12.36% |
| 3 | 2-0 | 10.75% |
| 4 | 0-0 | 10.24% |
| 5 | 2-1 | 8.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.6% | 51.6% | 1.95 | +0.6% |
| Draw | 26.8% | 26.4% | 3.65 | -2.2% |
| Lecce win | 21.6% | 22.0% | 4.38 | -5.3% |
| Over 2.5 | 40.2% | 47.1% | 2.08 | -16.3% |
| Under 2.5 | 59.8% | 52.9% | 1.87 | +11.8% |

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
| Market best home last update utc | 2026-10-14T11:21:32Z |
| Market best draw last update utc | 2026-10-14T11:21:32Z |
| Market best away last update utc | 2026-10-14T11:21:32Z |
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
| Fair Under 0.5 odds | 9.77 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.04 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.08 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 43.6% |
| P home draw | 78.4% |
| P draw away | 48.4% |
| Raw p home draw | 78.8% |
| Raw p draw away | 48.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.88 |
| Reference draw odds | 3.56 |
| Reference away odds | 4.23 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +0.0% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | 0.0001 |
| Raw ev home | 0.0058 |
| Raw edge prob draw | 0.0081 |
| Raw ev draw | -0.0069 |
| Raw edge prob away | -0.0082 |
| Raw ev away | -0.0709 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.1%**. Expected goals are 1.13 for Monza and 1.62 for Cagliari (2.75 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 50.7%; Under 3.5 goals: 70.9%; Double Chance 1X: 60.9%; Double Chance X2: 66.6%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

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
| 1 | 1-1 | 13.06% |
| 2 | 1-0 | 8.86% |
| 3 | 2-1 | 8.39% |
| 4 | 0-1 | 8.16% |
| 5 | 1-2 | 7.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.4% | 40.5% | 2.49 | -16.8% |
| Draw | 27.5% | 29.8% | 3.25 | -10.6% |
| Cagliari win | 39.1% | 29.7% | 3.25 | +26.9% |
| Over 2.5 | 50.7% | 45.8% | 2.15 | +9.0% |
| Under 2.5 | 49.3% | 54.2% | 1.82 | -10.3% |

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
| Market best home last update utc | 2026-10-14T11:21:32Z |
| Market best draw last update utc | 2026-10-14T11:21:32Z |
| Market best away last update utc | 2026-10-14T11:21:32Z |
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
| Fair Under 0.5 odds | 13.77 |
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
| Raw p home draw | 51.6% |
| Raw p draw away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.37 |
| Reference draw odds | 3.17 |
| Reference away odds | 3.18 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.75 |
| Home probability edge | -7.0% |
| Draw probability edge | -2.3% |
| Away probability edge | +9.3% |
| Over 2.5 probability edge | +4.9% |
| Under 2.5 probability edge | -4.9% |
| Raw edge prob home | -0.1405 |
| Raw ev home | -0.3425 |
| Raw edge prob draw | -0.0463 |
| Raw ev draw | -0.1812 |
| Raw edge prob away | 0.1868 |
| Raw ev away | 0.5730 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.0%**. Expected goals are 1.00 for Parma and 1.10 for Torino (2.11 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 87.3%; Over 2.5 goals: 35.0%; Under 3.5 goals: 83.7%; Double Chance 1X: 62.0%; Double Chance X2: 69.0%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 42.7%; BTTS No (at least one team does not score): 57.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.0% | 3.22 |
| Draw | 31.0% | 3.23 |
| Torino win | 38.0% | 2.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.00 |
| Torino expected goals | 1.10 |
| Expected total goals | 2.11 |
| Over 0.5 | 87.3% |
| Under 0.5 | 12.7% |
| Over 1.5 | 62.5% |
| Under 1.5 | 37.5% |
| Over 2.5 | 35.0% |
| Under 2.5 | 65.0% |
| Over 3.5 | 16.3% |
| Under 3.5 | 83.7% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.02% |
| 2 | 0-1 | 13.35% |
| 3 | 0-0 | 12.69% |
| 4 | 1-0 | 11.48% |
| 5 | 1-2 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.0% | 29.8% | 3.25 | +0.8% |
| Draw | 31.0% | 31.6% | 3.17 | -1.7% |
| Torino win | 38.0% | 38.6% | 2.54 | -3.6% |
| Over 2.5 | 35.0% | 38.6% | 2.48 | -13.1% |
| Under 2.5 | 65.0% | 61.4% | 1.63 | +5.9% |

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
| Market best home last update utc | 2026-10-14T11:21:32Z |
| Market best draw last update utc | 2026-10-14T11:21:32Z |
| Market best away last update utc | 2026-10-14T11:21:32Z |
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
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.88 |
| Fair Over 1.5 odds | 1.60 |
| Fair Under 1.5 odds | 2.67 |
| Fair Over 2.5 odds | 2.85 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.15 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.02 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.2% |
| Unadjusted draw probability | 30.4% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 62.5% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 42.6% |
| P home draw | 62.0% |
| P draw away | 69.0% |
| Raw p home draw | 62.6% |
| Raw p draw away | 67.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 3.17 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.48 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.35 |
| Reference Under 2.5 odds | 1.55 |
| Home probability edge | +1.2% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | 0.0241 |
| Raw ev home | 0.0475 |
| Raw edge prob draw | -0.0118 |
| Raw ev draw | -0.0358 |
| Raw edge prob away | -0.0123 |
| Raw ev away | -0.0513 |

</details>


---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **49.8%**. Expected goals are 1.94 for Torino and 1.18 for Monza (3.12 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 59.3%; Under 3.5 goals: 62.4%; Double Chance 1X: 74.7%; Double Chance X2: 50.2%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 49.8% | 2.01 |
| Draw | 24.9% | 4.01 |
| Monza win | 25.3% | 3.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.94 |
| Monza expected goals | 1.18 |
| Expected total goals | 3.12 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 59.3% |
| Under 2.5 | 40.7% |
| Over 3.5 | 37.6% |
| Under 3.5 | 62.4% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.47% |
| 2 | 2-1 | 8.88% |
| 3 | 1-0 | 7.56% |
| 4 | 2-0 | 7.54% |
| 5 | 1-2 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 49.8% | 44.6% | 2.15 | +7.1% |
| Draw | 24.9% | 27.5% | 3.62 | -9.7% |
| Monza win | 25.3% | 27.9% | 3.64 | -8.0% |
| Over 2.5 | 59.3% | 48.5% | 2.11 | +25.1% |
| Under 2.5 | 40.7% | 51.5% | 1.85 | -24.7% |

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
| Market best home last update utc | 2026-10-14T11:21:32Z |
| Market best draw last update utc | 2026-10-14T11:21:32Z |
| Market best away last update utc | 2026-10-14T11:21:32Z |
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
| Fair Under 0.5 odds | 19.45 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.48 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.66 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 5.00 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 55.0% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 82.1% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 59.5% |
| P home draw | 74.7% |
| P draw away | 50.2% |
| Raw p home draw | 77.4% |
| Raw p draw away | 45.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.15 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +5.2% |
| Draw probability edge | -2.5% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | +10.8% |
| Under 2.5 probability edge | -10.8% |
| Raw edge prob home | 0.1041 |
| Raw ev home | 0.1825 |
| Raw edge prob draw | -0.0509 |
| Raw ev draw | -0.1892 |
| Raw edge prob away | -0.0532 |
| Raw ev away | -0.1773 |

</details>


---
