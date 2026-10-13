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

The model's most likely 1X2 outcome is **Frosinone win** at **41.4%**. Expected goals are 1.64 for Frosinone and 1.29 for Sassuolo (2.94 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.4%; Double Chance 1X: 66.8%; Double Chance X2: 58.6%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 41.4% | 2.42 |
| Draw | 25.4% | 3.94 |
| Sassuolo win | 33.2% | 3.01 |

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
| Over 3.5 | 33.6% |
| Under 3.5 | 66.4% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.85% |
| 2 | 2-1 | 8.44% |
| 3 | 1-2 | 8.09% |
| 4 | 1-0 | 7.74% |
| 5 | 0-1 | 7.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 41.4% | 37.4% | 2.66 | +10.0% |
| Draw | 25.4% | 26.1% | 3.80 | -3.5% |
| Sassuolo win | 33.2% | 36.5% | 2.80 | -6.9% |
| Over 2.5 | 55.9% | 65.9% | 1.51 | -15.6% |
| Under 2.5 | 44.1% | 34.1% | 2.71 | +19.6% |

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
| Market best home last update utc | 2026-10-13T11:03:12Z |
| Market best draw last update utc | 2026-10-13T11:02:43Z |
| Market best away last update utc | 2026-10-13T11:02:43Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Unibet (SE) |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.51 |
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
| P home draw | 66.8% |
| P draw away | 58.6% |
| Raw p home draw | 70.0% |
| Raw p draw away | 54.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 2.66 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.72 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Home probability edge | +4.0% |
| Draw probability edge | -0.7% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | 0.0801 |
| Raw ev home | 0.2070 |
| Raw edge prob draw | -0.0143 |
| Raw ev draw | -0.0625 |
| Raw edge prob away | -0.0659 |
| Raw ev away | -0.1614 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **69.5%**. Expected goals are 1.97 for AS Roma and 0.64 for Genoa (2.61 combined). The most likely exact score is 2-0 at 14.4%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 48.9%; Under 3.5 goals: 73.2%; Double Chance 1X: 88.7%; Double Chance X2: 30.5%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 40.6%; BTTS No (at least one team does not score): 59.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 69.5% | 1.44 |
| Draw | 19.2% | 5.22 |
| Genoa win | 11.3% | 8.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.97 |
| Genoa expected goals | 0.64 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 48.9% |
| Under 2.5 | 51.1% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.43% |
| 2 | 1-0 | 14.42% |
| 3 | 3-0 | 9.50% |
| 4 | 2-1 | 9.22% |
| 5 | 1-1 | 8.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 69.5% | 70.2% | 1.41 | -2.0% |
| Draw | 19.2% | 18.0% | 5.30 | +1.5% |
| Genoa win | 11.3% | 11.8% | 9.05 | +2.5% |
| Over 2.5 | 48.9% | 56.1% | 1.74 | -14.9% |
| Under 2.5 | 51.1% | 43.9% | 2.27 | +15.9% |

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
| Market best home last update utc | 2026-10-13T11:03:12Z |
| Market best draw last update utc | 2026-10-13T11:02:43Z |
| Market best away last update utc | 2026-10-13T11:02:13Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 40.6% |
| P btts no | 59.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.10 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.95 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.8% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 10.9% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 40.9% |
| P home draw | 88.7% |
| P draw away | 30.5% |
| Raw p home draw | 89.1% |
| Raw p draw away | 31.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.41 |
| Reference draw odds | 5.30 |
| Reference away odds | 8.00 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | -0.7% |
| Draw probability edge | +1.2% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -7.2% |
| Under 2.5 probability edge | +7.2% |
| Raw edge prob home | -0.0143 |
| Raw ev home | -0.0299 |
| Raw edge prob draw | 0.0233 |
| Raw ev draw | 0.0771 |
| Raw edge prob away | -0.0091 |
| Raw ev away | -0.0160 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.0%**. Expected goals are 1.08 for Bologna and 2.13 for Inter Milan (3.20 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.2%; Double Chance 1X: 39.0%; Double Chance X2: 82.7%; Under 4.5 goals: 78.2%; BTTS Yes (both teams score): 58.5%; BTTS No (at least one team does not score): 41.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.3% | 5.78 |
| Draw | 21.7% | 4.61 |
| Inter Milan win | 61.0% | 1.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.08 |
| Inter Milan expected goals | 2.13 |
| Expected total goals | 3.20 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 61.7% |
| Under 2.5 | 38.3% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.8% |
| Under 4.5 | 78.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.97% |
| 2 | 1-2 | 9.86% |
| 3 | 0-2 | 9.17% |
| 4 | 0-1 | 8.43% |
| 5 | 1-3 | 6.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.3% | 16.5% | 6.15 | +6.4% |
| Draw | 21.7% | 22.7% | 4.30 | -6.8% |
| Inter Milan win | 61.0% | 60.9% | 1.65 | +0.7% |
| Over 2.5 | 61.7% | 58.9% | 1.71 | +5.5% |
| Under 2.5 | 38.3% | 41.1% | 2.33 | -10.8% |

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
| Market best home last update utc | 2026-10-13T11:03:12Z |
| Market best draw last update utc | 2026-10-13T11:02:58Z |
| Market best away last update utc | 2026-10-13T11:02:13Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | BetOnline.ag |
| Best draw bookmaker | Codere (IT) |
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
| Fair Under 0.5 odds | 22.34 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.92 |
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
| P home draw | 39.0% |
| P draw away | 82.7% |
| Raw p home draw | 38.8% |
| Raw p draw away | 81.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 5.90 |
| Reference draw odds | 4.30 |
| Reference away odds | 1.63 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | +0.8% |
| Draw probability edge | -1.0% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | +2.8% |
| Under 2.5 probability edge | -2.8% |
| Raw edge prob home | 0.0169 |
| Raw ev home | 0.1160 |
| Raw edge prob draw | -0.0204 |
| Raw ev draw | -0.1119 |
| Raw edge prob away | 0.0035 |
| Raw ev away | 0.0098 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **66.4%**. Expected goals are 0.67 for Venezia and 2.30 for Napoli (2.96 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.9%; Under 3.5 goals: 67.1%; Double Chance 1X: 33.6%; Double Chance X2: 86.2%; Under 4.5 goals: 83.2%; BTTS Yes (both teams score): 45.2%; BTTS No (at least one team does not score): 54.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 13.8% | 7.26 |
| Draw | 19.8% | 5.05 |
| Napoli win | 66.4% | 1.51 |

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
| Over 3.5 | 32.9% |
| Under 3.5 | 67.1% |
| Over 4.5 | 16.8% |
| Under 4.5 | 83.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.23% |
| 2 | 0-1 | 10.50% |
| 3 | 1-1 | 9.40% |
| 4 | 0-3 | 9.36% |
| 5 | 1-2 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 13.8% | 18.6% | 5.20 | -28.4% |
| Draw | 19.8% | 22.6% | 4.32 | -14.5% |
| Napoli win | 66.4% | 58.9% | 1.74 | +15.6% |
| Over 2.5 | 54.9% | 56.8% | 1.74 | -4.5% |
| Under 2.5 | 45.1% | 43.2% | 2.27 | +2.4% |

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
| Market best home last update utc | 2026-10-13T11:02:28Z |
| Market best draw last update utc | 2026-10-13T11:02:13Z |
| Market best away last update utc | 2026-10-13T11:02:43Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.2% |
| P btts no | 54.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.12 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.60 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.04 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.94 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 9.0% |
| Unadjusted draw probability | 17.0% |
| Unadjusted away-win probability | 74.0% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 43.9% |
| P home draw | 33.6% |
| P draw away | 86.2% |
| Raw p home draw | 26.0% |
| Raw p draw away | 91.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 5.20 |
| Reference draw odds | 4.30 |
| Reference away odds | 1.68 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.26 |
| Home probability edge | -4.8% |
| Draw probability edge | -2.8% |
| Away probability edge | +7.6% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.0959 |
| Raw ev home | -0.5329 |
| Raw edge prob draw | -0.0554 |
| Raw ev draw | -0.2649 |
| Raw edge prob away | 0.1513 |
| Raw ev away | 0.2876 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **45.3%**. Expected goals are 1.29 for AC Milan and 1.15 for Atalanta BC (2.44 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 44.5%; Under 3.5 goals: 76.9%; Double Chance 1X: 71.9%; Double Chance X2: 54.7%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 45.3% | 2.21 |
| Draw | 26.7% | 3.75 |
| Atalanta BC win | 28.1% | 3.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.29 |
| Atalanta BC expected goals | 1.15 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 70.4% |
| Under 1.5 | 29.6% |
| Over 2.5 | 44.5% |
| Under 2.5 | 55.5% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.63% |
| 2 | 1-0 | 12.57% |
| 3 | 2-1 | 9.56% |
| 4 | 0-0 | 8.60% |
| 5 | 0-1 | 8.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 45.3% | 51.0% | 1.93 | -12.7% |
| Draw | 26.7% | 25.5% | 3.95 | +5.3% |
| Atalanta BC win | 28.1% | 23.6% | 4.40 | +23.6% |
| Over 2.5 | 44.5% | 55.1% | 1.83 | -18.5% |
| Under 2.5 | 55.5% | 44.9% | 2.17 | +20.4% |

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
| Market best home last update utc | 2026-10-13T11:02:13Z |
| Market best draw last update utc | 2026-10-13T11:02:43Z |
| Market best away last update utc | 2026-10-13T11:02:43Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.63 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.38 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.76 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.8% |
| P home draw | 71.9% |
| P draw away | 54.7% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.93 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | -5.7% |
| Draw probability edge | +1.2% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | -0.1146 |
| Raw ev home | -0.2372 |
| Raw edge prob draw | 0.0239 |
| Raw ev draw | 0.1000 |
| Raw edge prob away | 0.0907 |
| Raw ev away | 0.4357 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **51.0%**. Expected goals are 0.96 for Fiorentina and 1.71 for Como (2.67 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.5%; Double Chance 1X: 49.0%; Double Chance X2: 76.2%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 23.8% | 4.20 |
| Draw | 25.2% | 3.97 |
| Como win | 51.0% | 1.96 |

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
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 27.5% |
| Under 3.5 | 72.5% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.00% |
| 2 | 0-1 | 10.84% |
| 3 | 0-2 | 9.44% |
| 4 | 1-2 | 9.05% |
| 5 | 0-0 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 23.8% | 26.7% | 3.70 | -12.0% |
| Draw | 25.2% | 26.0% | 3.81 | -4.0% |
| Como win | 51.0% | 47.3% | 2.12 | +8.1% |
| Over 2.5 | 49.3% | 58.0% | 1.73 | -14.7% |
| Under 2.5 | 50.7% | 42.0% | 2.29 | +16.1% |

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
| Market best home last update utc | 2026-10-13T11:03:27Z |
| Market best draw last update utc | 2026-10-13T11:02:13Z |
| Market best away last update utc | 2026-10-13T11:02:13Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Matchbook |
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
| Fair Under 0.5 odds | 13.46 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.91 |
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
| P home draw | 49.0% |
| P draw away | 76.2% |
| Raw p home draw | 45.3% |
| Raw p draw away | 79.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 3.70 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.26 |
| Home probability edge | -2.9% |
| Draw probability edge | -0.8% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.0585 |
| Raw ev home | -0.2282 |
| Raw edge prob draw | -0.0158 |
| Raw ev draw | -0.0697 |
| Raw edge prob away | 0.0743 |
| Raw ev away | 0.1601 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **53.0%**. Expected goals are 1.37 for Juventus and 0.87 for Lazio (2.23 combined). The most likely exact score is 1-0 at 15.8%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 39.4%; Under 3.5 goals: 81.0%; Double Chance 1X: 79.6%; Double Chance X2: 47.0%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 43.0%; BTTS No (at least one team does not score): 57.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 53.0% | 1.89 |
| Draw | 26.6% | 3.76 |
| Lazio win | 20.4% | 4.91 |

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
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.80% |
| 2 | 1-1 | 12.21% |
| 3 | 2-0 | 11.00% |
| 4 | 0-0 | 10.34% |
| 5 | 2-1 | 9.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 53.0% | 57.8% | 1.72 | -8.8% |
| Draw | 26.6% | 25.0% | 4.04 | +7.4% |
| Lazio win | 20.4% | 17.2% | 5.71 | +16.3% |
| Over 2.5 | 39.4% | 48.8% | 2.03 | -20.1% |
| Under 2.5 | 60.6% | 51.2% | 1.92 | +16.4% |

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
| Market best home last update utc | 2026-10-13T11:03:12Z |
| Market best draw last update utc | 2026-10-13T11:02:13Z |
| Market best away last update utc | 2026-10-13T11:02:13Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Juventus |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 43.0% |
| P btts no | 57.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.67 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.54 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.76 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 43.5% |
| P home draw | 79.6% |
| P draw away | 47.0% |
| Raw p home draw | 76.5% |
| Raw p draw away | 51.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.72 |
| Reference draw odds | 3.95 |
| Reference away odds | 5.70 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.98 |
| Reference Under 2.5 odds | 1.89 |
| Home probability edge | -4.8% |
| Draw probability edge | +1.6% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.0955 |
| Raw ev home | -0.1699 |
| Raw edge prob draw | 0.0327 |
| Raw ev draw | 0.1404 |
| Raw edge prob away | 0.0628 |
| Raw ev away | 0.3424 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.7%**. Expected goals are 1.46 for Udinese and 0.83 for Lecce (2.29 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.1%; Double Chance 1X: 78.5%; Double Chance X2: 48.3%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 43.5%; BTTS No (at least one team does not score): 56.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.7% | 1.93 |
| Draw | 26.8% | 3.73 |
| Lecce win | 21.5% | 4.66 |

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
| 1 | 1-0 | 14.54% |
| 2 | 1-1 | 12.38% |
| 3 | 2-0 | 10.78% |
| 4 | 0-0 | 10.25% |
| 5 | 2-1 | 8.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.7% | 51.8% | 1.95 | +0.8% |
| Draw | 26.8% | 26.5% | 3.70 | -0.7% |
| Lecce win | 21.5% | 21.7% | 4.50 | -3.4% |
| Over 2.5 | 40.2% | 47.4% | 2.12 | -14.7% |
| Under 2.5 | 59.8% | 52.6% | 1.87 | +11.8% |

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
| Market best home last update utc | 2026-10-13T11:02:13Z |
| Market best draw last update utc | 2026-10-13T11:03:27Z |
| Market best away last update utc | 2026-10-13T11:03:27Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 43.5% |
| P btts no | 56.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.75 |
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
| P home draw | 78.5% |
| P draw away | 48.3% |
| Raw p home draw | 78.8% |
| Raw p draw away | 48.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.91 |
| Reference draw odds | 3.70 |
| Reference away odds | 4.50 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.86 |
| Home probability edge | -0.1% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | -0.0025 |
| Raw ev home | 0.0058 |
| Raw edge prob draw | 0.0073 |
| Raw ev draw | 0.0067 |
| Raw edge prob away | -0.0049 |
| Raw ev away | -0.0454 |

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
| 1 | 1-1 | 13.10% |
| 2 | 1-0 | 8.81% |
| 3 | 2-1 | 8.34% |
| 4 | 0-1 | 8.19% |
| 5 | 1-2 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.2% | 40.0% | 2.50 | -16.9% |
| Draw | 27.6% | 30.0% | 3.27 | -9.8% |
| Cagliari win | 39.2% | 30.0% | 3.46 | +35.6% |
| Over 2.5 | 50.7% | 46.0% | 2.14 | +8.5% |
| Under 2.5 | 49.3% | 54.0% | 1.83 | -9.8% |

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
| Market best home last update utc | 2026-10-13T11:03:12Z |
| Market best draw last update utc | 2026-10-13T11:02:13Z |
| Market best away last update utc | 2026-10-13T11:02:13Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | LeoVegas (SE) |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.4% |
| P btts no | 44.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.73 |
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
| P home draw | 60.8% |
| P draw away | 66.8% |
| Raw p home draw | 51.6% |
| Raw p draw away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 2.42 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.80 |
| Home probability edge | -6.8% |
| Draw probability edge | -2.4% |
| Away probability edge | +9.2% |
| Over 2.5 probability edge | +4.7% |
| Under 2.5 probability edge | -4.7% |
| Raw edge prob home | -0.1363 |
| Raw ev home | -0.3398 |
| Raw edge prob draw | -0.0479 |
| Raw ev draw | -0.1762 |
| Raw edge prob away | 0.1842 |
| Raw ev away | 0.6746 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **37.8%**. Expected goals are 1.00 for Parma and 1.10 for Torino (2.11 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 87.2%; Over 2.5 goals: 35.0%; Under 3.5 goals: 83.8%; Double Chance 1X: 62.2%; Double Chance X2: 69.0%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 42.8%; BTTS No (at least one team does not score): 57.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.0% | 3.22 |
| Draw | 31.2% | 3.21 |
| Torino win | 37.8% | 2.65 |

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
| 1 | 1-1 | 14.09% |
| 2 | 0-1 | 13.30% |
| 3 | 0-0 | 12.75% |
| 4 | 1-0 | 11.48% |
| 5 | 1-2 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.0% | 29.8% | 3.25 | +0.9% |
| Draw | 31.2% | 31.9% | 3.20 | -0.3% |
| Torino win | 37.8% | 38.3% | 2.55 | -3.6% |
| Over 2.5 | 35.0% | 40.5% | 2.48 | -13.2% |
| Under 2.5 | 65.0% | 59.5% | 1.64 | +6.6% |

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
| Market best home last update utc | 2026-10-13T11:02:13Z |
| Market best draw last update utc | 2026-10-13T11:02:43Z |
| Market best away last update utc | 2026-10-13T11:02:43Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Parma |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.8% |
| P btts no | 57.2% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.84 |
| Fair Over 1.5 odds | 1.60 |
| Fair Under 1.5 odds | 2.66 |
| Fair Over 2.5 odds | 2.86 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.16 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.05 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.2% |
| Unadjusted draw probability | 30.4% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 62.5% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 42.6% |
| P home draw | 62.2% |
| P draw away | 69.0% |
| Raw p home draw | 62.6% |
| Raw p draw away | 67.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 3.20 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.52 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.36 |
| Reference Under 2.5 odds | 1.64 |
| Home probability edge | +1.2% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | 0.0239 |
| Raw ev home | 0.0475 |
| Raw edge prob draw | -0.0149 |
| Raw ev draw | -0.0266 |
| Raw edge prob away | -0.0090 |
| Raw ev away | -0.0475 |

</details>


---
