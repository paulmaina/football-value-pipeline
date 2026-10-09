# Serie A — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,190 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 879.078 |
| Base scoring parameter | 0.134 |
| Home-advantage parameter | 0.091 |
| Dixon-Coles low-score adjustment | 0.005 |
| Xi per day | 0.0029 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 24.00 |
| Additional event odds calls budget | 24.00 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-10 — Genoa vs Fiorentina

The model's most likely 1X2 outcome is **Fiorentina win** at **40.7%**. Expected goals are 1.17 for Genoa and 1.29 for Fiorentina (2.46 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 44.4%; Under 4.5 goals: 89.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 31.9% | 3.13 |
| Draw | 27.3% | 3.66 |
| Fiorentina win | 40.7% | 2.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.17 |
| Fiorentina expected goals | 1.29 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 70.3% |
| Under 1.5 | 29.7% |
| Over 2.5 | 44.4% |
| Under 2.5 | 55.6% |
| Over 3.5 | 23.3% |
| Under 3.5 | 76.7% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.96% |
| 2 | 0-1 | 11.53% |
| 3 | 1-0 | 9.57% |
| 4 | 1-2 | 8.62% |
| 5 | 0-0 | 8.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 31.9% | 30.1% | 3.45 | +10.1% |
| Draw | 27.3% | 27.6% | 3.48 | -4.8% |
| Fiorentina win | 40.7% | 42.3% | 2.39 | -2.7% |
| Over 2.5 | 44.4% | 47.2% | 2.15 | -4.5% |
| Under 2.5 | 55.6% | 52.8% | 1.87 | +3.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T13:00:00+00:00 |
| Fixture id | 2f8e871a0f7f66ae22938028645e1066 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:38Z |
| Market best draw last update utc | 2026-10-09T07:40:53Z |
| Market best away last update utc | 2026-10-09T07:40:53Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | BetAnything |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Genoa |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.65 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.37 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.29 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.72 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 49.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.78 |
| Home probability edge | +1.8% |
| Draw probability edge | -0.3% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | 0.0359 |
| Raw ev home | 0.1633 |
| Raw edge prob draw | -0.0051 |
| Raw ev draw | -0.0572 |
| Raw edge prob away | -0.0308 |
| Raw ev away | -0.0634 |

</details>


---

## 2026-10-10 — Inter Milan vs Parma

The model's most likely 1X2 outcome is **Inter Milan win** at **83.0%**. Expected goals are 2.47 for Inter Milan and 0.67 for Parma (3.14 combined). The most likely exact score is 2-0 at 14.3%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 62.8%; Under 4.5 goals: 78.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 83.0% | 1.20 |
| Draw | 11.0% | 9.10 |
| Parma win | 6.0% | 16.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.47 |
| Parma expected goals | 0.67 |
| Expected total goals | 3.14 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 62.8% |
| Under 2.5 | 37.2% |
| Over 3.5 | 39.6% |
| Under 3.5 | 60.4% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.29% |
| 2 | 3-0 | 11.75% |
| 3 | 1-0 | 11.62% |
| 4 | 2-1 | 9.55% |
| 5 | 3-1 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 83.0% | 89.1% | 1.17 | -2.9% |
| Draw | 11.0% | 7.0% | 10.50 | +15.4% |
| Parma win | 6.0% | 3.9% | 23.00 | +38.3% |
| Over 2.5 | 62.8% | 71.7% | 1.36 | -14.6% |
| Under 2.5 | 37.2% | 28.3% | 3.20 | +19.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T16:00:00+00:00 |
| Fixture id | 1a01b0611dacd334e1558a5097e05023 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:40:53Z |
| Market best draw last update utc | 2026-10-09T07:42:38Z |
| Market best away last update utc | 2026-10-09T07:42:38Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Inter |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 43.1% |
| P btts no | 56.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.65 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.89 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.69 |
| Fair Over 3.5 odds | 2.53 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.57 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 76.9% |
| Unadjusted draw probability | 15.0% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 61.7% |
| Raw p btts yes | 44.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.10 |
| Reference draw odds | 9.00 |
| Reference away odds | 14.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.20 |
| Home probability edge | -6.1% |
| Draw probability edge | +4.0% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | -0.1220 |
| Raw ev home | -0.1003 |
| Raw edge prob draw | 0.0801 |
| Raw ev draw | 0.5748 |
| Raw edge prob away | 0.0418 |
| Raw ev away | 0.8637 |

</details>


---

## 2026-10-10 — Napoli vs Frosinone

The model's most likely 1X2 outcome is **Napoli win** at **55.9%**. Expected goals are 1.39 for Napoli and 1.08 for Frosinone (2.47 combined). The most likely exact score is 1-0 at 15.0%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 46.6%; Under 4.5 goals: 88.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 55.9% | 1.79 |
| Draw | 22.0% | 4.55 |
| Frosinone win | 22.1% | 4.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.39 |
| Frosinone expected goals | 1.08 |
| Expected total goals | 2.47 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 46.6% |
| Under 2.5 | 53.4% |
| Over 3.5 | 24.1% |
| Under 3.5 | 75.9% |
| Over 4.5 | 11.1% |
| Under 4.5 | 88.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.04% |
| 2 | 2-1 | 11.21% |
| 3 | 1-1 | 10.40% |
| 4 | 2-0 | 10.37% |
| 5 | 0-1 | 6.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 55.9% | 67.9% | 1.49 | -16.7% |
| Draw | 22.0% | 17.3% | 5.10 | +12.0% |
| Frosinone win | 22.1% | 14.9% | 7.20 | +59.1% |
| Over 2.5 | 46.6% | 65.2% | 1.49 | -30.6% |
| Under 2.5 | 53.4% | 34.8% | 2.67 | +42.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T18:45:00+00:00 |
| Fixture id | 40c1bd70fee927f9bfa8901edab02b48 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:40:53Z |
| Market best draw last update utc | 2026-10-09T07:41:55Z |
| Market best away last update utc | 2026-10-09T07:42:38Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Napoli |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.45 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.46 |
| Fair Over 2.5 odds | 2.15 |
| Fair Under 2.5 odds | 1.87 |
| Fair Over 3.5 odds | 4.16 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.04 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 44.0% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 29.3% |
| Raw p over 1 5 | 70.5% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.42 |
| Reference draw odds | 4.90 |
| Reference away odds | 5.60 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.67 |
| Home probability edge | -11.9% |
| Draw probability edge | +4.7% |
| Away probability edge | +7.2% |
| Over 2.5 probability edge | -18.6% |
| Under 2.5 probability edge | +18.6% |
| Raw edge prob home | -0.2386 |
| Raw ev home | -0.3443 |
| Raw edge prob draw | 0.0942 |
| Raw ev draw | 0.3605 |
| Raw edge prob away | 0.1443 |
| Raw ev away | 1.1109 |

</details>


---

## 2026-10-11 — Cagliari vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **58.3%**. Expected goals are 0.80 for Cagliari and 1.48 for Juventus (2.28 combined). The most likely exact score is 0-1 at 16.6%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 40.8%; Under 4.5 goals: 91.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 17.5% | 5.72 |
| Draw | 24.2% | 4.14 |
| Juventus win | 58.3% | 1.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 0.80 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.8% |
| Under 2.5 | 59.2% |
| Over 3.5 | 20.1% |
| Under 3.5 | 79.9% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.60% |
| 2 | 0-2 | 12.27% |
| 3 | 1-1 | 11.07% |
| 4 | 1-2 | 9.77% |
| 5 | 0-0 | 9.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 17.5% | 14.8% | 7.00 | +22.3% |
| Draw | 24.2% | 22.1% | 4.10 | -0.9% |
| Juventus win | 58.3% | 63.1% | 1.62 | -5.5% |
| Over 2.5 | 40.8% | 47.0% | 2.12 | -13.5% |
| Under 2.5 | 59.2% | 53.0% | 1.88 | +11.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T18:45:00+00:00 |
| Fixture id | 407f7d03157d1dfad384876e6a6bc910 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:38Z |
| Market best draw last update utc | 2026-10-09T07:41:55Z |
| Market best away last update utc | 2026-10-09T07:40:53Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.7% |
| P btts no | 58.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.69 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.45 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.99 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.87 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 53.6% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.3% |
| Raw p btts yes | 42.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 5.70 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.52 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +2.7% |
| Draw probability edge | +2.1% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | 0.0541 |
| Raw ev home | 0.4127 |
| Raw edge prob draw | 0.0415 |
| Raw ev draw | 0.0762 |
| Raw edge prob away | -0.0956 |
| Raw ev away | -0.1322 |

</details>


---

## 2026-10-11 — Como vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **38.2%**. Expected goals are 1.17 for Como and 1.30 for AS Roma (2.47 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 45.1%; Under 4.5 goals: 89.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 35.6% | 2.81 |
| Draw | 26.2% | 3.81 |
| AS Roma win | 38.2% | 2.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 1.17 |
| AS Roma expected goals | 1.30 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 70.6% |
| Under 1.5 | 29.4% |
| Over 2.5 | 45.1% |
| Under 2.5 | 54.9% |
| Over 3.5 | 23.7% |
| Under 3.5 | 76.3% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.45% |
| 2 | 0-1 | 10.65% |
| 3 | 1-0 | 10.58% |
| 4 | 0-0 | 8.13% |
| 5 | 1-2 | 8.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 35.6% | 37.6% | 2.78 | -1.0% |
| Draw | 26.2% | 25.5% | 3.71 | -2.6% |
| AS Roma win | 38.2% | 36.8% | 2.77 | +5.7% |
| Over 2.5 | 45.1% | 59.1% | 1.69 | -23.7% |
| Under 2.5 | 54.9% | 40.9% | 2.37 | +30.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T10:30:00+00:00 |
| Fixture id | 2547c0dbddd26d23fa532228e36348cb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:38Z |
| Market best draw last update utc | 2026-10-09T07:40:53Z |
| Market best away last update utc | 2026-10-09T07:41:41Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.29 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.41 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.22 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.44 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 27.0% |
| Unadjusted away-win probability | 39.5% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.3% |
| Raw p btts yes | 50.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.45 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -2.0% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -14.0% |
| Under 2.5 probability edge | +14.0% |
| Raw edge prob home | -0.0410 |
| Raw ev home | -0.0672 |
| Raw edge prob draw | 0.0145 |
| Raw ev draw | 0.0006 |
| Raw edge prob away | 0.0265 |
| Raw ev away | 0.0935 |

</details>


---

## 2026-10-11 — Lazio vs Monza

The model's most likely 1X2 outcome is **Lazio win** at **63.2%**. Expected goals are 2.01 for Lazio and 0.87 for Monza (2.88 combined). The most likely exact score is 2-0 at 11.2%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 54.7%; Under 4.5 goals: 83.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 63.2% | 1.58 |
| Draw | 20.9% | 4.78 |
| Monza win | 15.9% | 6.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 2.01 |
| Monza expected goals | 0.87 |
| Expected total goals | 2.88 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 54.7% |
| Under 2.5 | 45.3% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.23% |
| 2 | 1-0 | 11.21% |
| 3 | 1-1 | 9.93% |
| 4 | 2-1 | 9.72% |
| 5 | 3-0 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 63.2% | 62.3% | 1.64 | +3.7% |
| Draw | 20.9% | 21.3% | 4.22 | -11.8% |
| Monza win | 15.9% | 16.4% | 6.40 | +1.7% |
| Over 2.5 | 54.7% | 48.8% | 1.96 | +7.2% |
| Under 2.5 | 45.3% | 51.2% | 2.08 | -5.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | c0f72699f32ec193b64fd54092fe268d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:41:38Z |
| Market best draw last update utc | 2026-10-09T07:42:38Z |
| Market best away last update utc | 2026-10-09T07:42:38Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Lazio |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.61 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.55 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.08 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.11 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 64.1% |
| Unadjusted draw probability | 20.5% |
| Unadjusted away-win probability | 15.4% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 67.5% |
| Raw p btts yes | 50.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.54 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.20 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | +0.9% |
| Draw probability edge | -0.4% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +5.8% |
| Under 2.5 probability edge | -5.8% |
| Raw edge prob home | 0.0183 |
| Raw ev home | 0.0517 |
| Raw edge prob draw | -0.0079 |
| Raw ev draw | -0.1346 |
| Raw edge prob away | -0.0105 |
| Raw ev away | -0.0166 |

</details>


---

## 2026-10-11 — Lecce vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **50.4%**. Expected goals are 0.78 for Lecce and 1.33 for Bologna (2.11 combined). The most likely exact score is 0-1 at 16.4%. Goal-market probabilities: at least one goal: 88.0%; Over 2.5 goals: 35.5%; Under 4.5 goals: 93.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 21.6% | 4.64 |
| Draw | 28.0% | 3.57 |
| Bologna win | 50.4% | 1.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.78 |
| Bologna expected goals | 1.33 |
| Expected total goals | 2.11 |
| Over 0.5 | 88.0% |
| Under 0.5 | 12.0% |
| Over 1.5 | 62.4% |
| Under 1.5 | 37.6% |
| Over 2.5 | 35.5% |
| Under 2.5 | 64.5% |
| Over 3.5 | 16.4% |
| Under 3.5 | 83.6% |
| Over 4.5 | 6.4% |
| Under 4.5 | 93.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.37% |
| 2 | 1-1 | 12.43% |
| 3 | 0-0 | 11.95% |
| 4 | 0-2 | 10.85% |
| 5 | 1-0 | 9.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 21.6% | 21.1% | 4.70 | +1.3% |
| Draw | 28.0% | 27.9% | 3.50 | -1.9% |
| Bologna win | 50.4% | 51.0% | 1.98 | -0.2% |
| Over 2.5 | 35.5% | 45.2% | 2.18 | -22.7% |
| Under 2.5 | 64.5% | 54.8% | 1.81 | +16.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | 946716d7e5e52822f08be8cb95193d9d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:38Z |
| Market best draw last update utc | 2026-10-09T07:41:38Z |
| Market best away last update utc | 2026-10-09T07:40:53Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 39.8% |
| P btts no | 60.2% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.37 |
| Fair Over 1.5 odds | 1.60 |
| Fair Under 1.5 odds | 2.66 |
| Fair Over 2.5 odds | 2.82 |
| Fair Under 2.5 odds | 1.55 |
| Fair Over 3.5 odds | 6.09 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.72 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 22.0% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 62.3% |
| Raw p under 3 5 | 83.6% |
| Raw p btts yes | 39.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.20 |
| Reference draw odds | 3.25 |
| Reference away odds | 1.86 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.74 |
| Home probability edge | +0.5% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | 0.0091 |
| Raw ev home | 0.0346 |
| Raw edge prob draw | 0.0034 |
| Raw ev draw | -0.0127 |
| Raw edge prob away | -0.0125 |
| Raw ev away | -0.0144 |

</details>


---

## 2026-10-11 — Sassuolo vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **52.1%**. Expected goals are 1.13 for Sassuolo and 1.68 for AC Milan (2.81 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 53.5%; Under 4.5 goals: 84.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 23.9% | 4.18 |
| Draw | 23.9% | 4.18 |
| AC Milan win | 52.1% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.13 |
| AC Milan expected goals | 1.68 |
| Expected total goals | 2.81 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 53.5% |
| Under 2.5 | 46.5% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.32% |
| 2 | 0-1 | 10.51% |
| 3 | 1-2 | 9.94% |
| 4 | 0-2 | 8.80% |
| 5 | 1-0 | 6.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 23.9% | 22.2% | 4.45 | +6.5% |
| Draw | 23.9% | 23.9% | 3.95 | -5.4% |
| AC Milan win | 52.1% | 53.9% | 1.89 | -1.5% |
| Over 2.5 | 53.5% | 53.8% | 1.87 | +0.0% |
| Under 2.5 | 46.5% | 46.2% | 2.20 | +2.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T16:00:00+00:00 |
| Fixture id | 1cf64166dda1e0da8b325161deb39662 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:09Z |
| Market best draw last update utc | 2026-10-09T07:42:38Z |
| Market best away last update utc | 2026-10-09T07:42:38Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betsson |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | BetAnything |
| Matched home-team name | Sassuolo |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.0% |
| P btts no | 45.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.88 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.45 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 25.6% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 50.4% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 68.9% |
| Raw p btts yes | 55.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.95 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.76 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.04 |
| Home probability edge | +1.7% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.0336 |
| Raw ev home | 0.1394 |
| Raw edge prob draw | 0.0012 |
| Raw ev draw | -0.0517 |
| Raw edge prob away | -0.0348 |
| Raw ev away | -0.0477 |

</details>


---

## 2026-10-12 — Atalanta BC vs Venezia

The model's most likely 1X2 outcome is **Atalanta BC win** at **69.6%**. Expected goals are 2.35 for Atalanta BC and 0.66 for Venezia (3.02 combined). The most likely exact score is 2-0 at 12.6%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.4%; Under 4.5 goals: 82.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 69.6% | 1.44 |
| Draw | 18.5% | 5.41 |
| Venezia win | 11.9% | 8.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.35 |
| Venezia expected goals | 0.66 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 56.4% |
| Under 2.5 | 43.6% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 17.9% |
| Under 4.5 | 82.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.56% |
| 2 | 1-0 | 10.71% |
| 3 | 3-0 | 9.86% |
| 4 | 1-1 | 8.77% |
| 5 | 2-1 | 8.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 69.6% | 63.8% | 1.66 | +15.5% |
| Draw | 18.5% | 21.0% | 4.40 | -18.7% |
| Venezia win | 11.9% | 15.2% | 6.20 | -26.1% |
| Over 2.5 | 56.4% | 62.1% | 1.56 | -12.1% |
| Under 2.5 | 43.6% | 37.9% | 2.47 | +7.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-12T16:30:00+00:00 |
| Fixture id | 0f2e7ff90b994f31d5cd48a9680943e1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:40:54Z |
| Market best draw last update utc | 2026-10-09T07:41:38Z |
| Market best away last update utc | 2026-10-09T07:42:38Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Atalanta |
| Matched away-team name | Venezia |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 44.8% |
| P btts no | 55.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.77 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.80 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.59 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 75.3% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 8.7% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 64.4% |
| Raw p btts yes | 43.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.50 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.47 |
| Home probability edge | +5.7% |
| Draw probability edge | -2.5% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | 0.1149 |
| Raw ev home | 0.2506 |
| Raw edge prob draw | -0.0501 |
| Raw ev draw | -0.2971 |
| Raw edge prob away | -0.0648 |
| Raw ev away | -0.4615 |

</details>


---

## 2026-10-12 — Torino vs Udinese

The model's most likely 1X2 outcome is **Torino win** at **38.6%**. Expected goals are 1.29 for Torino and 1.35 for Udinese (2.64 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.6%; Under 4.5 goals: 87.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 38.6% | 2.59 |
| Draw | 27.5% | 3.64 |
| Udinese win | 33.9% | 2.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.29 |
| Udinese expected goals | 1.35 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.6% |
| Under 2.5 | 51.4% |
| Over 3.5 | 27.2% |
| Under 3.5 | 72.8% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.06% |
| 2 | 1-0 | 10.06% |
| 3 | 2-1 | 8.69% |
| 4 | 0-1 | 8.57% |
| 5 | 0-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 38.6% | 41.6% | 2.44 | -5.7% |
| Draw | 27.5% | 28.9% | 3.35 | -8.0% |
| Udinese win | 33.9% | 29.4% | 3.35 | +13.5% |
| Over 2.5 | 48.6% | 44.6% | 2.24 | +9.0% |
| Under 2.5 | 51.4% | 55.4% | 1.79 | -8.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-12T18:45:00+00:00 |
| Fixture id | f4a28510bb0c835280a2aca709c19d50 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:38Z |
| Market best draw last update utc | 2026-10-09T07:40:54Z |
| Market best away last update utc | 2026-10-09T07:40:54Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Torino |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.0% |
| P btts no | 46.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.38 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.68 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.91 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 38.3% |
| Raw p over 1 5 | 73.9% |
| Raw p under 3 5 | 72.7% |
| Raw p btts yes | 53.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.25 |
| Reference draw odds | 3.15 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.72 |
| Home probability edge | -3.0% |
| Draw probability edge | -1.5% |
| Away probability edge | +4.4% |
| Over 2.5 probability edge | +4.1% |
| Under 2.5 probability edge | -4.1% |
| Raw edge prob home | -0.0597 |
| Raw ev home | -0.1299 |
| Raw edge prob draw | -0.0292 |
| Raw ev draw | -0.1285 |
| Raw edge prob away | 0.0889 |
| Raw ev away | 0.2839 |

</details>


---

## 2026-10-16 — Frosinone vs Sassuolo

The model's most likely 1X2 outcome is **Frosinone win** at **47.1%**. Expected goals are 1.84 for Frosinone and 1.12 for Sassuolo (2.95 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 55.9%; Under 4.5 goals: 82.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 47.1% | 2.12 |
| Draw | 23.8% | 4.20 |
| Sassuolo win | 29.1% | 3.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.84 |
| Sassuolo expected goals | 1.12 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 78.8% |
| Under 1.5 | 21.2% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.6% |
| Under 3.5 | 66.4% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.15% |
| 2 | 2-1 | 8.53% |
| 3 | 1-0 | 8.37% |
| 4 | 2-0 | 7.64% |
| 5 | 1-2 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 47.1% | 39.9% | 2.55 | +20.1% |
| Draw | 23.8% | 24.9% | 3.70 | -11.9% |
| Sassuolo win | 29.1% | 35.2% | 2.96 | -13.8% |
| Over 2.5 | 55.9% | 59.6% | 1.61 | -10.1% |
| Under 2.5 | 44.1% | 40.4% | 2.47 | +9.0% |

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
| Market best home last update utc | 2026-10-09T07:41:38Z |
| Market best draw last update utc | 2026-10-09T07:42:38Z |
| Market best away last update utc | 2026-10-09T07:40:54Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Unibet (SE) |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.48 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.71 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.98 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.80 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.3% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 79.3% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.45 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +7.2% |
| Draw probability edge | -1.1% |
| Away probability edge | -6.1% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | 0.1434 |
| Raw ev home | 0.3834 |
| Raw edge prob draw | -0.0217 |
| Raw ev draw | -0.1594 |
| Raw edge prob away | -0.1218 |
| Raw ev away | -0.3183 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **71.9%**. Expected goals are 2.01 for AS Roma and 0.66 for Genoa (2.67 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 50.9%; Under 4.5 goals: 86.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 71.9% | 1.39 |
| Draw | 17.4% | 5.76 |
| Genoa win | 10.7% | 9.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 2.01 |
| Genoa expected goals | 0.66 |
| Expected total goals | 2.67 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 74.9% |
| Under 1.5 | 25.1% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.3% |
| Under 3.5 | 71.7% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.54% |
| 2 | 2-0 | 14.53% |
| 3 | 3-0 | 9.72% |
| 4 | 2-1 | 9.62% |
| 5 | 1-1 | 8.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 71.9% | 74.7% | 1.36 | -2.2% |
| Draw | 17.4% | 15.1% | 5.70 | -1.0% |
| Genoa win | 10.7% | 10.2% | 10.50 | +12.8% |
| Over 2.5 | 50.9% | 58.7% | 1.72 | -12.5% |
| Under 2.5 | 49.1% | 41.3% | 2.31 | +13.5% |

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
| Market best home last update utc | 2026-10-09T07:40:54Z |
| Market best draw last update utc | 2026-10-09T07:42:38Z |
| Market best away last update utc | 2026-10-09T07:42:38Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.1% |
| P btts no | 58.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.39 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 3.99 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.53 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.35 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 11.3% |
| Raw p over 1 5 | 74.5% |
| Raw p under 3 5 | 72.1% |
| Raw p btts yes | 41.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.27 |
| Reference draw odds | 4.70 |
| Reference away odds | 6.50 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -2.8% |
| Draw probability edge | +2.2% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -7.9% |
| Under 2.5 probability edge | +7.9% |
| Raw edge prob home | -0.0560 |
| Raw ev home | -0.0603 |
| Raw edge prob draw | 0.0448 |
| Raw ev draw | 0.1172 |
| Raw edge prob away | 0.0112 |
| Raw ev away | 0.1866 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **60.9%**. Expected goals are 1.07 for Bologna and 2.13 for Inter Milan (3.21 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 61.9%; Under 4.5 goals: 78.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 18.3% | 5.45 |
| Draw | 20.8% | 4.82 |
| Inter Milan win | 60.9% | 1.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.07 |
| Inter Milan expected goals | 2.13 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 61.9% |
| Under 2.5 | 38.1% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.77% |
| 2 | 1-1 | 9.53% |
| 3 | 0-2 | 9.11% |
| 4 | 0-1 | 8.59% |
| 5 | 1-3 | 6.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 18.3% | 18.4% | 5.70 | +4.6% |
| Draw | 20.8% | 21.4% | 4.12 | -14.5% |
| Inter Milan win | 60.9% | 60.1% | 1.69 | +2.9% |
| Over 2.5 | 61.9% | 56.0% | 1.72 | +6.4% |
| Under 2.5 | 38.1% | 44.0% | 2.30 | -12.3% |

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
| Market best home last update utc | 2026-10-09T07:41:40Z |
| Market best draw last update utc | 2026-10-09T07:40:54Z |
| Market best away last update utc | 2026-10-09T07:40:54Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bologna |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.18 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.83 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.62 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.57 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 61.7% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 57.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.20 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.54 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -0.1% |
| Draw probability edge | -0.7% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +5.9% |
| Under 2.5 probability edge | -5.9% |
| Raw edge prob home | -0.0020 |
| Raw ev home | 0.0399 |
| Raw edge prob draw | -0.0133 |
| Raw ev draw | -0.1722 |
| Raw edge prob away | 0.0153 |
| Raw ev away | 0.0421 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **65.2%**. Expected goals are 0.67 for Venezia and 2.18 for Napoli (2.85 combined). The most likely exact score is 0-2 at 12.4%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 52.5%; Under 4.5 goals: 84.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 15.0% | 6.67 |
| Draw | 19.8% | 5.05 |
| Napoli win | 65.2% | 1.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.18 |
| Expected total goals | 2.85 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 76.3% |
| Under 1.5 | 23.7% |
| Over 2.5 | 52.5% |
| Under 2.5 | 47.5% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.2% |
| Under 4.5 | 84.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.44% |
| 2 | 0-1 | 11.48% |
| 3 | 1-1 | 9.36% |
| 4 | 0-3 | 9.02% |
| 5 | 1-2 | 8.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 15.0% | 19.8% | 4.80 | -28.1% |
| Draw | 19.8% | 21.8% | 4.22 | -16.4% |
| Napoli win | 65.2% | 58.4% | 1.76 | +14.8% |
| Over 2.5 | 52.5% | 57.0% | 1.75 | -8.1% |
| Under 2.5 | 47.5% | 43.0% | 2.25 | +6.8% |

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
| Market best home last update utc | 2026-10-09T07:42:38Z |
| Market best draw last update utc | 2026-10-09T07:40:54Z |
| Market best away last update utc | 2026-10-09T07:40:54Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 44.2% |
| P btts no | 55.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.61 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.22 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.27 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.60 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 72.1% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 43.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.95 |
| Reference draw odds | 3.65 |
| Reference away odds | 1.58 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | -4.9% |
| Draw probability edge | -2.0% |
| Away probability edge | +6.8% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | -0.0973 |
| Raw ev home | -0.5144 |
| Raw edge prob draw | -0.0396 |
| Raw ev draw | -0.2477 |
| Raw edge prob away | 0.1369 |
| Raw ev away | 0.2682 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **45.6%**. Expected goals are 1.28 for AC Milan and 1.16 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 44.6%; Under 4.5 goals: 89.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 45.6% | 2.19 |
| Draw | 25.8% | 3.88 |
| Atalanta BC win | 28.6% | 3.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.28 |
| Atalanta BC expected goals | 1.16 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.00% |
| 2 | 1-1 | 12.20% |
| 3 | 2-1 | 9.59% |
| 4 | 0-1 | 8.72% |
| 5 | 2-0 | 8.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 45.6% | 51.7% | 1.93 | -12.0% |
| Draw | 25.8% | 24.4% | 3.86 | -0.5% |
| Atalanta BC win | 28.6% | 24.0% | 4.30 | +23.2% |
| Over 2.5 | 44.6% | 55.6% | 1.83 | -18.4% |
| Under 2.5 | 55.4% | 44.4% | 2.13 | +18.0% |

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
| Market best home last update utc | 2026-10-09T07:40:54Z |
| Market best draw last update utc | 2026-10-09T07:40:54Z |
| Market best away last update utc | 2026-10-09T07:42:38Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 49.1% |
| P btts no | 50.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.20 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.74 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 33.3% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.76 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -6.1% |
| Draw probability edge | +1.4% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | -0.1219 |
| Raw ev home | -0.2379 |
| Raw edge prob draw | 0.0281 |
| Raw ev draw | 0.0493 |
| Raw edge prob away | 0.0938 |
| Raw ev away | 0.4332 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.6%**. Expected goals are 1.00 for Fiorentina and 1.73 for Como (2.73 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 51.0%; Under 4.5 goals: 86.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 25.2% | 3.97 |
| Draw | 24.2% | 4.14 |
| Como win | 50.6% | 1.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.00 |
| Como expected goals | 1.73 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.49% |
| 2 | 0-1 | 10.50% |
| 3 | 0-2 | 9.05% |
| 4 | 1-2 | 9.04% |
| 5 | 1-0 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 25.2% | 28.7% | 3.65 | -7.9% |
| Draw | 24.2% | 24.8% | 3.81 | -7.9% |
| Como win | 50.6% | 46.5% | 2.13 | +7.8% |
| Over 2.5 | 51.0% | 56.8% | 1.73 | -11.9% |
| Under 2.5 | 49.0% | 43.2% | 2.29 | +12.3% |

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
| Market best home last update utc | 2026-10-09T07:42:38Z |
| Market best draw last update utc | 2026-10-09T07:40:54Z |
| Market best away last update utc | 2026-10-09T07:40:54Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 52.2% |
| P btts no | 47.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.11 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.04 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.17 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 21.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 51.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.35 |
| Reference away odds | 1.94 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | -3.5% |
| Draw probability edge | -0.6% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0694 |
| Raw ev home | -0.2061 |
| Raw edge prob draw | -0.0119 |
| Raw ev draw | -0.1014 |
| Raw edge prob away | 0.0812 |
| Raw ev away | 0.1643 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **54.2%**. Expected goals are 1.37 for Juventus and 0.85 for Lazio (2.22 combined). The most likely exact score is 1-0 at 16.5%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 39.1%; Under 4.5 goals: 92.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 54.2% | 1.84 |
| Draw | 25.3% | 3.95 |
| Lazio win | 20.5% | 4.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.85 |
| Expected total goals | 2.22 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 18.7% |
| Under 3.5 | 81.3% |
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.53% |
| 2 | 1-1 | 11.54% |
| 3 | 2-0 | 11.26% |
| 4 | 0-0 | 9.92% |
| 5 | 2-1 | 9.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 54.2% | 59.4% | 1.68 | -8.9% |
| Draw | 25.3% | 23.0% | 4.12 | +4.2% |
| Lazio win | 20.5% | 17.6% | 5.80 | +18.8% |
| Over 2.5 | 39.1% | 48.8% | 1.99 | -22.1% |
| Under 2.5 | 60.9% | 51.2% | 1.98 | +20.5% |

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
| Market best home last update utc | 2026-10-09T07:42:09Z |
| Market best draw last update utc | 2026-10-09T07:40:54Z |
| Market best away last update utc | 2026-10-09T07:42:38Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Betsson |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Juventus |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.0% |
| P btts no | 58.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.08 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.33 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.97 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 23.4% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 42.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | -5.2% |
| Draw probability edge | +2.3% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.1032 |
| Raw ev home | -0.1759 |
| Raw edge prob draw | 0.0456 |
| Raw ev draw | 0.1365 |
| Raw edge prob away | 0.0575 |
| Raw ev away | 0.3549 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **52.0%**. Expected goals are 1.44 for Udinese and 0.82 for Lecce (2.26 combined). The most likely exact score is 1-0 at 15.2%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 39.6%; Under 4.5 goals: 92.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 52.0% | 1.92 |
| Draw | 26.1% | 3.83 |
| Lecce win | 21.9% | 4.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.44 |
| Lecce expected goals | 0.82 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 66.0% |
| Under 1.5 | 34.0% |
| Over 2.5 | 39.6% |
| Under 2.5 | 60.4% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.18% |
| 2 | 1-1 | 11.94% |
| 3 | 2-0 | 10.86% |
| 4 | 0-0 | 10.08% |
| 5 | 2-1 | 8.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 52.0% | 52.5% | 1.95 | +1.5% |
| Draw | 26.1% | 25.4% | 3.71 | -3.2% |
| Lecce win | 21.9% | 22.2% | 4.35 | -4.8% |
| Over 2.5 | 39.6% | 48.5% | 2.00 | -20.8% |
| Under 2.5 | 60.4% | 51.5% | 1.94 | +17.2% |

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
| Market best home last update utc | 2026-10-09T07:40:54Z |
| Market best draw last update utc | 2026-10-09T07:40:54Z |
| Market best away last update utc | 2026-10-09T07:42:38Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.5% |
| P btts no | 57.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.92 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.54 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 21.6% |
| Raw p over 1 5 | 65.9% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 42.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.74 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.65 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | -0.4% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.0089 |
| Raw ev home | 0.0061 |
| Raw edge prob draw | 0.0145 |
| Raw ev draw | -0.0054 |
| Raw edge prob away | -0.0056 |
| Raw ev away | -0.0606 |

</details>


---
