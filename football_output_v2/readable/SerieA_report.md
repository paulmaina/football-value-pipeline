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

The model's most likely 1X2 outcome is **Frosinone win** at **41.6%**. Expected goals are 1.64 for Frosinone and 1.29 for Sassuolo (2.94 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.8%; Under 3.5 goals: 66.3%; Double Chance 1X: 67.3%; Double Chance X2: 58.4%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 59.1%; BTTS No (at least one team does not score): 40.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 41.6% | 2.40 |
| Draw | 25.6% | 3.90 |
| Sassuolo win | 32.7% | 3.05 |

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
| 1 | 1-1 | 11.96% |
| 2 | 2-1 | 8.50% |
| 3 | 1-2 | 7.97% |
| 4 | 1-0 | 7.79% |
| 5 | 0-1 | 7.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 41.6% | 37.9% | 2.68 | +11.6% |
| Draw | 25.6% | 26.6% | 3.80 | -2.6% |
| Sassuolo win | 32.7% | 35.5% | 2.80 | -8.3% |
| Over 2.5 | 55.8% | 65.9% | 1.51 | -15.7% |
| Under 2.5 | 44.2% | 34.1% | 2.71 | +19.7% |

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
| Market best home last update utc | 2026-10-13T07:42:43Z |
| Market best draw last update utc | 2026-10-13T07:42:43Z |
| Market best away last update utc | 2026-10-13T07:42:44Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Matchbook |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Unibet (SE) |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.1% |
| P btts no | 40.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.35 |
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
| P home draw | 67.3% |
| P draw away | 58.4% |
| Raw p home draw | 70.0% |
| Raw p draw away | 54.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.45 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.60 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Home probability edge | +3.7% |
| Draw probability edge | -1.0% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | 0.0748 |
| Raw ev home | 0.2161 |
| Raw edge prob draw | -0.0190 |
| Raw ev draw | -0.0625 |
| Raw edge prob away | -0.0558 |
| Raw ev away | -0.1614 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **70.1%**. Expected goals are 1.97 for AS Roma and 0.64 for Genoa (2.61 combined). The most likely exact score is 2-0 at 14.6%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 49.0%; Under 3.5 goals: 73.1%; Double Chance 1X: 89.3%; Double Chance X2: 29.9%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 40.5%; BTTS No (at least one team does not score): 59.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 70.1% | 1.43 |
| Draw | 19.2% | 5.21 |
| Genoa win | 10.7% | 9.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.97 |
| Genoa expected goals | 0.64 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 49.0% |
| Under 2.5 | 51.0% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.55% |
| 2 | 1-0 | 14.54% |
| 3 | 3-0 | 9.58% |
| 4 | 2-1 | 9.30% |
| 5 | 1-1 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 70.1% | 71.4% | 1.40 | -1.9% |
| Draw | 19.2% | 18.1% | 5.30 | +1.7% |
| Genoa win | 10.7% | 10.5% | 10.00 | +7.0% |
| Over 2.5 | 49.0% | 56.6% | 1.74 | -14.8% |
| Under 2.5 | 51.0% | 43.4% | 2.27 | +15.8% |

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
| Market best home last update utc | 2026-10-13T07:41:45Z |
| Market best draw last update utc | 2026-10-13T07:42:21Z |
| Market best away last update utc | 2026-10-13T07:41:46Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 40.5% |
| P btts no | 59.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.07 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.92 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.8% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 10.9% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 40.9% |
| P home draw | 89.3% |
| P draw away | 29.9% |
| Raw p home draw | 89.1% |
| Raw p draw away | 31.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.37 |
| Reference draw odds | 4.95 |
| Reference away odds | 8.20 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | -1.3% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | -0.0260 |
| Raw ev home | -0.0367 |
| Raw edge prob draw | 0.0226 |
| Raw ev draw | 0.0771 |
| Raw edge prob away | 0.0034 |
| Raw ev away | 0.0873 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.4%**. Expected goals are 1.08 for Bologna and 2.13 for Inter Milan (3.20 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.8%; Under 3.5 goals: 60.2%; Double Chance 1X: 38.6%; Double Chance X2: 83.0%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.0% | 5.88 |
| Draw | 21.6% | 4.62 |
| Inter Milan win | 61.4% | 1.63 |

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
| Over 2.5 | 61.8% |
| Under 2.5 | 38.2% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.95% |
| 2 | 1-2 | 9.92% |
| 3 | 0-2 | 9.22% |
| 4 | 0-1 | 8.47% |
| 5 | 1-3 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.0% | 15.9% | 6.15 | +4.6% |
| Draw | 21.6% | 22.6% | 4.30 | -7.0% |
| Inter Milan win | 61.4% | 61.5% | 1.65 | +1.2% |
| Over 2.5 | 61.8% | 58.4% | 1.71 | +5.6% |
| Under 2.5 | 38.2% | 41.6% | 2.33 | -10.9% |

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
| Market best home last update utc | 2026-10-13T07:41:30Z |
| Market best draw last update utc | 2026-10-13T07:42:13Z |
| Market best away last update utc | 2026-10-13T07:41:45Z |
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
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.38 |
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
| P draw away | 83.0% |
| Raw p home draw | 38.8% |
| Raw p draw away | 81.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 5.65 |
| Reference draw odds | 4.05 |
| Reference away odds | 1.58 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.26 |
| Home probability edge | +1.1% |
| Draw probability edge | -1.0% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +3.4% |
| Under 2.5 probability edge | -3.4% |
| Raw edge prob home | 0.0227 |
| Raw ev home | 0.1160 |
| Raw edge prob draw | -0.0197 |
| Raw ev draw | -0.1119 |
| Raw edge prob away | -0.0030 |
| Raw ev away | 0.0098 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **66.5%**. Expected goals are 0.67 for Venezia and 2.30 for Napoli (2.96 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.9%; Under 3.5 goals: 67.1%; Double Chance 1X: 33.5%; Double Chance X2: 86.2%; Under 4.5 goals: 83.2%; BTTS Yes (both teams score): 45.2%; BTTS No (at least one team does not score): 54.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 13.8% | 7.25 |
| Draw | 19.7% | 5.08 |
| Napoli win | 66.5% | 1.50 |

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
| 1 | 0-2 | 12.24% |
| 2 | 0-1 | 10.52% |
| 3 | 0-3 | 9.37% |
| 4 | 1-1 | 9.35% |
| 5 | 1-2 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 13.8% | 18.6% | 5.20 | -28.3% |
| Draw | 19.7% | 22.4% | 4.32 | -14.9% |
| Napoli win | 66.5% | 59.0% | 1.74 | +15.7% |
| Over 2.5 | 54.9% | 57.4% | 1.74 | -4.5% |
| Under 2.5 | 45.1% | 42.6% | 2.27 | +2.4% |

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
| Market best home last update utc | 2026-10-13T07:42:28Z |
| Market best draw last update utc | 2026-10-13T07:41:45Z |
| Market best away last update utc | 2026-10-13T07:42:28Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
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
| Fair Under 0.5 odds | 16.19 |
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
| P home draw | 33.5% |
| P draw away | 86.2% |
| Raw p home draw | 26.0% |
| Raw p draw away | 91.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 4.95 |
| Reference draw odds | 4.15 |
| Reference away odds | 1.65 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.22 |
| Home probability edge | -4.8% |
| Draw probability edge | -2.7% |
| Away probability edge | +7.5% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0960 |
| Raw ev home | -0.5329 |
| Raw edge prob draw | -0.0536 |
| Raw ev draw | -0.2649 |
| Raw edge prob away | 0.1496 |
| Raw ev away | 0.2876 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **45.6%**. Expected goals are 1.29 for AC Milan and 1.15 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 12.7%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.9%; Double Chance 1X: 72.2%; Double Chance X2: 54.4%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 45.6% | 2.20 |
| Draw | 26.6% | 3.76 |
| Atalanta BC win | 27.8% | 3.59 |

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
| 1 | 1-0 | 12.66% |
| 2 | 1-1 | 12.61% |
| 3 | 2-1 | 9.62% |
| 4 | 0-0 | 8.58% |
| 5 | 2-0 | 8.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 45.6% | 51.6% | 1.93 | -12.1% |
| Draw | 26.6% | 25.4% | 3.90 | +3.8% |
| Atalanta BC win | 27.8% | 23.1% | 4.30 | +19.7% |
| Over 2.5 | 44.6% | 54.9% | 1.83 | -18.5% |
| Under 2.5 | 55.4% | 45.1% | 2.17 | +20.3% |

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
| Market best home last update utc | 2026-10-13T07:41:45Z |
| Market best draw last update utc | 2026-10-13T07:41:46Z |
| Market best away last update utc | 2026-10-13T07:41:46Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.65 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.38 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.75 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.8% |
| P home draw | 72.2% |
| P draw away | 54.4% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.88 |
| Reference draw odds | 3.70 |
| Reference away odds | 4.05 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -6.0% |
| Draw probability edge | +1.2% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -10.3% |
| Under 2.5 probability edge | +10.3% |
| Raw edge prob home | -0.1206 |
| Raw ev home | -0.2372 |
| Raw edge prob draw | 0.0249 |
| Raw ev draw | 0.0861 |
| Raw edge prob away | 0.0957 |
| Raw ev away | 0.4030 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **51.0%**. Expected goals are 0.96 for Fiorentina and 1.71 for Como (2.67 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 49.4%; Under 3.5 goals: 72.5%; Double Chance 1X: 49.0%; Double Chance X2: 75.9%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.1% | 4.15 |
| Draw | 24.9% | 4.01 |
| Como win | 51.0% | 1.96 |

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
| 2 | 0-1 | 10.83% |
| 3 | 0-2 | 9.43% |
| 4 | 1-2 | 9.05% |
| 5 | 1-0 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.1% | 27.4% | 3.70 | -10.8% |
| Draw | 24.9% | 25.4% | 3.85 | -4.0% |
| Como win | 51.0% | 47.2% | 2.12 | +8.0% |
| Over 2.5 | 49.4% | 58.4% | 1.73 | -14.6% |
| Under 2.5 | 50.6% | 41.6% | 2.29 | +15.9% |

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
| Market best home last update utc | 2026-10-13T07:42:28Z |
| Market best draw last update utc | 2026-10-13T07:42:43Z |
| Market best away last update utc | 2026-10-13T07:41:45Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Matchbook |
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
| Fair Under 0.5 odds | 13.61 |
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
| P home draw | 49.0% |
| P draw away | 75.9% |
| Raw p home draw | 45.3% |
| Raw p draw away | 79.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 3.45 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.05 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.26 |
| Home probability edge | -3.3% |
| Draw probability edge | -0.5% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.0651 |
| Raw ev home | -0.2282 |
| Raw edge prob draw | -0.0102 |
| Raw ev draw | -0.0600 |
| Raw edge prob away | 0.0754 |
| Raw ev away | 0.1601 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **54.1%**. Expected goals are 1.37 for Juventus and 0.87 for Lazio (2.23 combined). The most likely exact score is 1-0 at 16.1%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 39.6%; Under 3.5 goals: 80.9%; Double Chance 1X: 79.9%; Double Chance X2: 45.9%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.8%; BTTS No (at least one team does not score): 57.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 54.1% | 1.85 |
| Draw | 25.9% | 3.87 |
| Lazio win | 20.1% | 4.98 |

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
| 1 | 1-0 | 16.10% |
| 2 | 1-1 | 11.88% |
| 3 | 2-0 | 11.21% |
| 4 | 0-0 | 10.06% |
| 5 | 2-1 | 9.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 54.1% | 59.9% | 1.72 | -7.0% |
| Draw | 25.9% | 23.5% | 4.04 | +4.5% |
| Lazio win | 20.1% | 16.6% | 5.71 | +14.6% |
| Over 2.5 | 39.6% | 49.4% | 2.03 | -19.6% |
| Under 2.5 | 60.4% | 50.6% | 1.92 | +15.9% |

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
| Market best home last update utc | 2026-10-13T07:42:28Z |
| Market best draw last update utc | 2026-10-13T07:41:45Z |
| Market best away last update utc | 2026-10-13T07:41:45Z |
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
| P btts yes | 42.8% |
| P btts no | 57.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.94 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.23 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.64 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 43.5% |
| P home draw | 79.9% |
| P draw away | 45.9% |
| Raw p home draw | 76.5% |
| Raw p draw away | 51.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.62 |
| Reference draw odds | 3.90 |
| Reference away odds | 5.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.89 |
| Home probability edge | -5.8% |
| Draw probability edge | +2.4% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -9.8% |
| Under 2.5 probability edge | +9.8% |
| Raw edge prob home | -0.1159 |
| Raw ev home | -0.1699 |
| Raw edge prob draw | 0.0472 |
| Raw ev draw | 0.1404 |
| Raw edge prob away | 0.0688 |
| Raw ev away | 0.3424 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.6%**. Expected goals are 1.46 for Udinese and 0.83 for Lecce (2.29 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.1%; Double Chance 1X: 78.4%; Double Chance X2: 48.4%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 43.5%; BTTS No (at least one team does not score): 56.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.6% | 1.94 |
| Draw | 26.8% | 3.72 |
| Lecce win | 21.6% | 4.64 |

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
| 2 | 1-1 | 12.38% |
| 3 | 2-0 | 10.75% |
| 4 | 0-0 | 10.25% |
| 5 | 2-1 | 8.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.6% | 51.6% | 1.95 | +0.6% |
| Draw | 26.8% | 26.5% | 3.70 | -0.7% |
| Lecce win | 21.6% | 21.9% | 4.50 | -2.9% |
| Over 2.5 | 40.2% | 47.5% | 2.08 | -16.3% |
| Under 2.5 | 59.8% | 52.5% | 1.87 | +11.8% |

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
| Market best home last update utc | 2026-10-13T07:41:45Z |
| Market best draw last update utc | 2026-10-13T07:42:43Z |
| Market best away last update utc | 2026-10-13T07:42:43Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
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
| P home draw | 78.4% |
| P draw away | 48.4% |
| Raw p home draw | 78.8% |
| Raw p draw away | 48.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.88 |
| Reference draw odds | 3.55 |
| Reference away odds | 4.25 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | -0.0% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -7.2% |
| Under 2.5 probability edge | +7.2% |
| Raw edge prob home | -0.0000 |
| Raw ev home | 0.0058 |
| Raw edge prob draw | 0.0072 |
| Raw ev draw | 0.0067 |
| Raw edge prob away | -0.0072 |
| Raw ev away | -0.0454 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.7%**. Expected goals are 1.13 for Monza and 1.62 for Cagliari (2.75 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 50.9%; Under 3.5 goals: 70.9%; Double Chance 1X: 60.3%; Double Chance X2: 66.8%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 33.2% | 3.01 |
| Draw | 27.0% | 3.70 |
| Cagliari win | 39.7% | 2.52 |

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
| 1 | 1-1 | 12.83% |
| 2 | 1-0 | 8.81% |
| 3 | 2-1 | 8.34% |
| 4 | 0-1 | 8.30% |
| 5 | 1-2 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.2% | 40.1% | 2.48 | -17.6% |
| Draw | 27.0% | 28.9% | 3.27 | -11.6% |
| Cagliari win | 39.7% | 31.1% | 3.46 | +37.5% |
| Over 2.5 | 50.9% | 46.9% | 2.14 | +8.9% |
| Under 2.5 | 49.1% | 53.1% | 1.83 | -10.1% |

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
| Market best home last update utc | 2026-10-13T07:42:28Z |
| Market best draw last update utc | 2026-10-13T07:41:45Z |
| Market best away last update utc | 2026-10-13T07:41:45Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | LeoVegas (SE) |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.01 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.43 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.15 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 26.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.3% |
| Raw p btts yes | 54.5% |
| P home draw | 60.3% |
| P draw away | 66.8% |
| Raw p home draw | 51.6% |
| Raw p draw away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.30 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.81 |
| Home probability edge | -6.8% |
| Draw probability edge | -1.8% |
| Away probability edge | +8.7% |
| Over 2.5 probability edge | +3.9% |
| Under 2.5 probability edge | -3.9% |
| Raw edge prob home | -0.1366 |
| Raw ev home | -0.3451 |
| Raw edge prob draw | -0.0368 |
| Raw ev draw | -0.1762 |
| Raw edge prob away | 0.1734 |
| Raw ev away | 0.6746 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.1%**. Expected goals are 1.00 for Parma and 1.10 for Torino (2.11 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 87.5%; Over 2.5 goals: 35.2%; Under 3.5 goals: 83.7%; Double Chance 1X: 61.9%; Double Chance X2: 68.6%; Under 4.5 goals: 93.7%; BTTS Yes (both teams score): 42.6%; BTTS No (at least one team does not score): 57.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.4% | 3.19 |
| Draw | 30.5% | 3.28 |
| Torino win | 38.1% | 2.62 |

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
| 1 | 1-1 | 13.78% |
| 2 | 0-1 | 13.41% |
| 3 | 0-0 | 12.48% |
| 4 | 1-0 | 11.61% |
| 5 | 1-2 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.4% | 30.6% | 3.25 | +2.0% |
| Draw | 30.5% | 30.6% | 3.25 | -0.9% |
| Torino win | 38.1% | 38.9% | 2.55 | -2.8% |
| Over 2.5 | 35.2% | 40.5% | 2.48 | -12.7% |
| Under 2.5 | 64.8% | 59.5% | 1.64 | +6.3% |

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
| Market best home last update utc | 2026-10-13T07:41:45Z |
| Market best draw last update utc | 2026-10-13T07:41:46Z |
| Market best away last update utc | 2026-10-13T07:42:28Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
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
| Fair Over 4.5 odds | 15.93 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.2% |
| Unadjusted draw probability | 30.4% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 62.5% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 42.6% |
| P home draw | 61.9% |
| P draw away | 68.6% |
| Raw p home draw | 62.6% |
| Raw p draw away | 67.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 3.00 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.32 |
| Reference Under 2.5 odds | 1.62 |
| Home probability edge | +0.8% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | 0.0167 |
| Raw ev home | 0.0475 |
| Raw edge prob draw | -0.0014 |
| Raw ev draw | -0.0114 |
| Raw edge prob away | -0.0153 |
| Raw ev away | -0.0475 |

</details>


---
