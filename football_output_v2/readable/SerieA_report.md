# Serie A — football model report

Fixtures in this report: **10**.

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
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 10.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
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

The model's most likely 1X2 outcome is **Frosinone win** at **42.0%**. Expected goals are 1.64 for Frosinone and 1.29 for Sassuolo (2.94 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.8%; Under 3.5 goals: 66.3%; Double Chance 1X: 67.6%; Double Chance X2: 58.0%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 42.0% | 2.38 |
| Draw | 25.6% | 3.91 |
| Sassuolo win | 32.4% | 3.09 |

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
| 1 | 1-1 | 11.95% |
| 2 | 2-1 | 8.58% |
| 3 | 1-2 | 7.88% |
| 4 | 1-0 | 7.86% |
| 5 | 0-1 | 7.16% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 7.00 |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.36 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
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
| P draw away | 58.0% |
| Raw p home draw | 70.0% |
| Raw p draw away | 54.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.40 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | +3.3% |
| Draw probability edge | -0.9% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.0667 |
| Raw edge prob draw | -0.0186 |
| Raw edge prob away | -0.0481 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **70.2%**. Expected goals are 1.97 for AS Roma and 0.64 for Genoa (2.61 combined). The most likely exact score is 2-0 at 14.6%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 48.9%; Under 3.5 goals: 73.1%; Double Chance 1X: 89.7%; Double Chance X2: 29.8%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 40.6%; BTTS No (at least one team does not score): 59.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 70.2% | 1.43 |
| Draw | 19.5% | 5.13 |
| Genoa win | 10.3% | 9.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.97 |
| Genoa expected goals | 0.64 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 74.0% |
| Under 1.5 | 26.0% |
| Over 2.5 | 48.9% |
| Under 2.5 | 51.1% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.57% |
| 2 | 1-0 | 14.56% |
| 3 | 3-0 | 9.59% |
| 4 | 2-1 | 9.31% |
| 5 | 1-1 | 9.05% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 11.00 |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 40.6% |
| P btts no | 59.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.86 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.93 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.8% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 10.9% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 40.9% |
| P home draw | 89.7% |
| P draw away | 29.8% |
| Raw p home draw | 89.1% |
| Raw p draw away | 31.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.35 |
| Reference draw odds | 4.50 |
| Reference away odds | 8.00 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -1.4% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.0273 |
| Raw edge prob draw | 0.0167 |
| Raw edge prob away | 0.0106 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.3%**. Expected goals are 1.08 for Bologna and 2.13 for Inter Milan (3.20 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 61.8%; Under 3.5 goals: 60.2%; Double Chance 1X: 38.7%; Double Chance X2: 82.8%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.2% | 5.80 |
| Draw | 21.5% | 4.65 |
| Inter Milan win | 61.3% | 1.63 |

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
| 1 | 1-2 | 9.90% |
| 2 | 1-1 | 9.90% |
| 3 | 0-2 | 9.20% |
| 4 | 0-1 | 8.46% |
| 5 | 1-3 | 7.02% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 12.00 |
| Matched home-team name | Bologna |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.51 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.93 |
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
| P home draw | 38.7% |
| P draw away | 82.8% |
| Raw p home draw | 38.8% |
| Raw p draw away | 81.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 5.20 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.56 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | +0.9% |
| Draw probability edge | -0.9% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | +5.4% |
| Under 2.5 probability edge | -5.4% |
| Raw edge prob home | 0.0184 |
| Raw edge prob draw | -0.0172 |
| Raw edge prob away | -0.0011 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **66.8%**. Expected goals are 0.67 for Venezia and 2.30 for Napoli (2.96 combined). The most likely exact score is 0-2 at 12.3%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.9%; Under 3.5 goals: 67.0%; Double Chance 1X: 33.2%; Double Chance X2: 86.6%; Under 4.5 goals: 83.1%; BTTS Yes (both teams score): 45.2%; BTTS No (at least one team does not score): 54.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 13.4% | 7.45 |
| Draw | 19.7% | 5.07 |
| Napoli win | 66.8% | 1.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.30 |
| Expected total goals | 2.96 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 78.3% |
| Under 1.5 | 21.7% |
| Over 2.5 | 54.9% |
| Under 2.5 | 45.1% |
| Over 3.5 | 33.0% |
| Under 3.5 | 67.0% |
| Over 4.5 | 16.9% |
| Under 4.5 | 83.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.30% |
| 2 | 0-1 | 10.57% |
| 3 | 0-3 | 9.41% |
| 4 | 1-1 | 9.37% |
| 5 | 1-2 | 8.21% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 14.00 |
| Matched home-team name | Venezia |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.2% |
| P btts no | 54.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.16 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.62 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.03 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.93 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 9.0% |
| Unadjusted draw probability | 17.0% |
| Unadjusted away-win probability | 74.0% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 43.9% |
| P home draw | 33.2% |
| P draw away | 86.6% |
| Raw p home draw | 26.0% |
| Raw p draw away | 91.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 4.80 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -4.4% |
| Draw probability edge | -2.7% |
| Away probability edge | +7.2% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | -0.0888 |
| Raw edge prob draw | -0.0543 |
| Raw edge prob away | 0.1431 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **46.8%**. Expected goals are 1.29 for AC Milan and 1.15 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 44.7%; Under 3.5 goals: 76.9%; Double Chance 1X: 72.9%; Double Chance X2: 53.2%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 49.3%; BTTS No (at least one team does not score): 50.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 46.8% | 2.14 |
| Draw | 26.1% | 3.83 |
| Atalanta BC win | 27.1% | 3.69 |

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
| 1 | 1-0 | 13.00% |
| 2 | 1-1 | 12.39% |
| 3 | 2-1 | 9.88% |
| 4 | 2-0 | 8.61% |
| 5 | 0-0 | 8.43% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 15.00 |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 49.3% |
| P btts no | 50.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.86 |
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
| P home draw | 72.9% |
| P draw away | 53.2% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.76 |
| Reference draw odds | 3.65 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -7.3% |
| Draw probability edge | +1.7% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | -0.1452 |
| Raw edge prob draw | 0.0342 |
| Raw edge prob away | 0.1110 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **51.5%**. Expected goals are 0.96 for Fiorentina and 1.71 for Como (2.67 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.4%; Under 3.5 goals: 72.5%; Double Chance 1X: 48.5%; Double Chance X2: 76.4%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 23.6% | 4.24 |
| Draw | 24.9% | 4.01 |
| Como win | 51.5% | 1.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 0.96 |
| Como expected goals | 1.71 |
| Expected total goals | 2.67 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.4% |
| Under 1.5 | 25.6% |
| Over 2.5 | 49.4% |
| Under 2.5 | 50.6% |
| Over 3.5 | 27.5% |
| Under 3.5 | 72.5% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.87% |
| 2 | 0-1 | 10.94% |
| 3 | 0-2 | 9.53% |
| 4 | 1-2 | 9.14% |
| 5 | 0-0 | 7.35% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 12.00 |
| Matched home-team name | Fiorentina |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.60 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.91 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.63 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.68 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 50.7% |
| P home draw | 48.5% |
| P draw away | 76.4% |
| Raw p home draw | 45.3% |
| Raw p draw away | 79.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.40 |
| Reference draw odds | 3.50 |
| Reference away odds | 1.95 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -2.7% |
| Draw probability edge | -0.5% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | -0.0543 |
| Raw edge prob draw | -0.0106 |
| Raw edge prob away | 0.0649 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **53.2%**. Expected goals are 1.37 for Juventus and 0.87 for Lazio (2.23 combined). The most likely exact score is 1-0 at 15.9%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 39.4%; Under 3.5 goals: 80.9%; Double Chance 1X: 79.7%; Double Chance X2: 46.8%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.9%; BTTS No (at least one team does not score): 57.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 53.2% | 1.88 |
| Draw | 26.4% | 3.78 |
| Lazio win | 20.3% | 4.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.87 |
| Expected total goals | 2.23 |
| Over 0.5 | 89.7% |
| Under 0.5 | 10.3% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 39.4% |
| Under 2.5 | 60.6% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.85% |
| 2 | 1-1 | 12.13% |
| 3 | 2-0 | 11.04% |
| 4 | 0-0 | 10.27% |
| 5 | 2-1 | 9.57% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 16.00 |
| Matched home-team name | Juventus |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.9% |
| P btts no | 57.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.74 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.54 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.73 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 43.5% |
| P home draw | 79.7% |
| P draw away | 46.8% |
| Raw p home draw | 76.5% |
| Raw p draw away | 51.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.64 |
| Reference draw odds | 3.60 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | -5.0% |
| Draw probability edge | +1.8% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.0993 |
| Raw edge prob draw | 0.0361 |
| Raw edge prob away | 0.0632 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.9%**. Expected goals are 1.46 for Udinese and 0.83 for Lecce (2.29 combined). The most likely exact score is 1-0 at 14.6%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 40.3%; Under 3.5 goals: 80.1%; Double Chance 1X: 78.7%; Double Chance X2: 48.1%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 43.5%; BTTS No (at least one team does not score): 56.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.9% | 1.93 |
| Draw | 26.7% | 3.74 |
| Lecce win | 21.3% | 4.69 |

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
| 1 | 1-0 | 14.61% |
| 2 | 1-1 | 12.33% |
| 3 | 2-0 | 10.83% |
| 4 | 0-0 | 10.21% |
| 5 | 2-1 | 9.02% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 16.00 |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 43.5% |
| P btts no | 56.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.79 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.03 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.03 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.06 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 43.6% |
| P home draw | 78.7% |
| P draw away | 48.1% |
| Raw p home draw | 78.8% |
| Raw p draw away | 48.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.81 |
| Reference draw odds | 3.40 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | -0.4% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | -0.0073 |
| Raw edge prob draw | 0.0093 |
| Raw edge prob away | -0.0020 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.2%**. Expected goals are 1.13 for Monza and 1.62 for Cagliari (2.75 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 50.6%; Under 3.5 goals: 70.9%; Double Chance 1X: 60.8%; Double Chance X2: 67.0%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 33.0% | 3.03 |
| Draw | 27.8% | 3.59 |
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
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.21% |
| 2 | 1-0 | 8.75% |
| 3 | 2-1 | 8.29% |
| 4 | 0-1 | 8.18% |
| 5 | 1-2 | 7.66% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 14.00 |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.4% |
| P btts no | 44.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.61 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.20 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 26.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.3% |
| Raw p btts yes | 54.5% |
| P home draw | 60.8% |
| P draw away | 67.0% |
| Raw p home draw | 51.6% |
| Raw p draw away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.35 |
| Reference draw odds | 3.00 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.14 |
| Reference Under 2.5 odds | 1.71 |
| Home probability edge | -6.6% |
| Draw probability edge | -2.6% |
| Away probability edge | +9.2% |
| Over 2.5 probability edge | +6.6% |
| Under 2.5 probability edge | -6.6% |
| Raw edge prob home | -0.1325 |
| Raw edge prob draw | -0.0525 |
| Raw edge prob away | 0.1850 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.0%**. Expected goals are 1.00 for Parma and 1.10 for Torino (2.11 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 87.4%; Over 2.5 goals: 35.1%; Under 3.5 goals: 83.7%; Double Chance 1X: 62.0%; Double Chance X2: 68.7%; Under 4.5 goals: 93.7%; BTTS Yes (both teams score): 42.7%; BTTS No (at least one team does not score): 57.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.3% | 3.19 |
| Draw | 30.7% | 3.26 |
| Torino win | 38.0% | 2.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.00 |
| Torino expected goals | 1.10 |
| Expected total goals | 2.11 |
| Over 0.5 | 87.4% |
| Under 0.5 | 12.6% |
| Over 1.5 | 62.5% |
| Under 1.5 | 37.5% |
| Over 2.5 | 35.1% |
| Under 2.5 | 64.9% |
| Over 3.5 | 16.3% |
| Under 3.5 | 83.7% |
| Over 4.5 | 6.3% |
| Under 4.5 | 93.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.87% |
| 2 | 0-1 | 13.37% |
| 3 | 0-0 | 12.55% |
| 4 | 1-0 | 11.58% |
| 5 | 1-2 | 7.56% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 12.00 |
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
| Fair Over 2.5 odds | 2.85 |
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
| P home draw | 62.0% |
| P draw away | 68.7% |
| Raw p home draw | 62.6% |
| Raw p draw away | 67.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.00 |
| Reference draw odds | 2.95 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.35 |
| Reference Under 2.5 odds | 1.60 |
| Home probability edge | +0.9% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | 0.0186 |
| Raw edge prob draw | -0.0052 |
| Raw edge prob away | -0.0134 |

</details>


---
