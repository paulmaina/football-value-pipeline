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

The model's most likely 1X2 outcome is **Fiorentina win** at **40.3%**. Expected goals are 1.17 for Genoa and 1.29 for Fiorentina (2.46 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 44.3%; Under 4.5 goals: 89.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 32.1% | 3.12 |
| Draw | 27.7% | 3.62 |
| Fiorentina win | 40.3% | 2.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.17 |
| Fiorentina expected goals | 1.29 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 70.3% |
| Under 1.5 | 29.7% |
| Over 2.5 | 44.3% |
| Under 2.5 | 55.7% |
| Over 3.5 | 23.3% |
| Under 3.5 | 76.7% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.11% |
| 2 | 0-1 | 11.39% |
| 3 | 1-0 | 9.62% |
| 4 | 0-0 | 8.68% |
| 5 | 1-2 | 8.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 32.1% | 30.4% | 3.40 | +9.1% |
| Draw | 27.7% | 28.2% | 3.48 | -3.7% |
| Fiorentina win | 40.3% | 41.3% | 2.39 | -3.8% |
| Over 2.5 | 44.3% | 47.3% | 2.15 | -4.7% |
| Under 2.5 | 55.7% | 52.7% | 1.87 | +4.1% |

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
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.52 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.37 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.29 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.75 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 39.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.23 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.39 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.87 |
| Home probability edge | +1.6% |
| Draw probability edge | -0.6% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | 0.0327 |
| Raw ev home | 0.1464 |
| Raw edge prob draw | -0.0114 |
| Raw ev draw | -0.0572 |
| Raw edge prob away | -0.0213 |
| Raw ev away | -0.0634 |

</details>


---

## 2026-10-10 — Inter Milan vs Parma

The model's most likely 1X2 outcome is **Inter Milan win** at **81.0%**. Expected goals are 2.47 for Inter Milan and 0.67 for Parma (3.14 combined). The most likely exact score is 2-0 at 13.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 62.1%; Under 4.5 goals: 78.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 81.0% | 1.24 |
| Draw | 12.3% | 8.12 |
| Parma win | 6.7% | 14.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.47 |
| Parma expected goals | 0.67 |
| Expected total goals | 3.14 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.5% |
| Under 4.5 | 78.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.93% |
| 2 | 3-0 | 11.46% |
| 3 | 1-0 | 11.34% |
| 4 | 2-1 | 9.31% |
| 5 | 3-1 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 81.0% | 85.0% | 1.17 | -5.3% |
| Draw | 12.3% | 9.6% | 10.09 | +24.3% |
| Parma win | 6.7% | 5.3% | 24.00 | +61.3% |
| Over 2.5 | 62.1% | 71.7% | 1.36 | -15.6% |
| Under 2.5 | 37.9% | 28.3% | 3.20 | +21.3% |

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
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Inter |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.23 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.77 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.65 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 76.9% |
| Unadjusted draw probability | 15.0% |
| Unadjusted away-win probability | 8.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.17 |
| Reference draw odds | 9.60 |
| Reference away odds | 17.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.20 |
| Home probability edge | -4.1% |
| Draw probability edge | +2.7% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | -0.0812 |
| Raw ev home | -0.1003 |
| Raw edge prob draw | 0.0535 |
| Raw ev draw | 0.5133 |
| Raw edge prob away | 0.0276 |
| Raw ev away | 0.9447 |

</details>


---

## 2026-10-10 — Napoli vs Frosinone

The model's most likely 1X2 outcome is **Napoli win** at **55.3%**. Expected goals are 1.39 for Napoli and 1.08 for Frosinone (2.47 combined). The most likely exact score is 1-0 at 14.9%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 46.2%; Under 4.5 goals: 89.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 55.3% | 1.81 |
| Draw | 23.0% | 4.34 |
| Frosinone win | 21.7% | 4.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.39 |
| Frosinone expected goals | 1.08 |
| Expected total goals | 2.47 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 46.2% |
| Under 2.5 | 53.8% |
| Over 3.5 | 24.0% |
| Under 3.5 | 76.0% |
| Over 4.5 | 11.0% |
| Under 4.5 | 89.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.86% |
| 2 | 2-1 | 11.08% |
| 3 | 1-1 | 10.91% |
| 4 | 2-0 | 10.26% |
| 5 | 0-0 | 7.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 55.3% | 66.6% | 1.49 | -17.6% |
| Draw | 23.0% | 19.4% | 5.10 | +17.4% |
| Frosinone win | 21.7% | 14.0% | 7.20 | +56.1% |
| Over 2.5 | 46.2% | 65.2% | 1.49 | -31.1% |
| Under 2.5 | 53.8% | 34.8% | 2.67 | +43.5% |

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
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.79 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.46 |
| Fair Over 2.5 odds | 2.16 |
| Fair Under 2.5 odds | 1.86 |
| Fair Over 3.5 odds | 4.16 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.12 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 44.0% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 29.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.49 |
| Reference draw odds | 5.00 |
| Reference away odds | 6.85 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.67 |
| Home probability edge | -11.3% |
| Draw probability edge | +3.7% |
| Away probability edge | +7.6% |
| Over 2.5 probability edge | -18.9% |
| Under 2.5 probability edge | +18.9% |
| Raw edge prob home | -0.2258 |
| Raw ev home | -0.3443 |
| Raw edge prob draw | 0.0731 |
| Raw ev draw | 0.3605 |
| Raw edge prob away | 0.1527 |
| Raw ev away | 1.1109 |

</details>


---

## 2026-10-11 — Cagliari vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **57.4%**. Expected goals are 0.80 for Cagliari and 1.48 for Juventus (2.28 combined). The most likely exact score is 0-1 at 16.3%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 40.5%; Under 4.5 goals: 91.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 17.5% | 5.71 |
| Draw | 25.1% | 3.99 |
| Juventus win | 57.4% | 1.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 0.80 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 66.8% |
| Under 1.5 | 33.2% |
| Over 2.5 | 40.5% |
| Under 2.5 | 59.5% |
| Over 3.5 | 20.0% |
| Under 3.5 | 80.0% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.33% |
| 2 | 0-2 | 12.07% |
| 3 | 1-1 | 11.48% |
| 4 | 0-0 | 9.71% |
| 5 | 1-2 | 9.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 17.5% | 14.8% | 7.00 | +22.6% |
| Draw | 25.1% | 23.9% | 4.10 | +2.8% |
| Juventus win | 57.4% | 61.3% | 1.62 | -7.0% |
| Over 2.5 | 40.5% | 47.5% | 2.12 | -14.2% |
| Under 2.5 | 59.5% | 52.5% | 1.88 | +11.9% |

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
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.30 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.47 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.01 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.99 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 53.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 6.54 |
| Reference draw odds | 4.09 |
| Reference away odds | 1.62 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.07 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +2.7% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | 0.0534 |
| Raw ev home | 0.4127 |
| Raw edge prob draw | 0.0234 |
| Raw ev draw | 0.0762 |
| Raw edge prob away | -0.0769 |
| Raw ev away | -0.1322 |

</details>


---

## 2026-10-11 — Como vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **37.7%**. Expected goals are 1.17 for Como and 1.30 for AS Roma (2.47 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 45.0%; Under 4.5 goals: 89.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 35.6% | 2.81 |
| Draw | 26.7% | 3.74 |
| AS Roma win | 37.7% | 2.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 1.17 |
| AS Roma expected goals | 1.30 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 70.6% |
| Under 1.5 | 29.4% |
| Over 2.5 | 45.0% |
| Under 2.5 | 55.0% |
| Over 3.5 | 23.7% |
| Under 3.5 | 76.3% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.67% |
| 2 | 1-0 | 10.58% |
| 3 | 0-1 | 10.51% |
| 4 | 0-0 | 8.28% |
| 5 | 2-1 | 8.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 35.6% | 37.7% | 2.76 | -1.7% |
| Draw | 26.7% | 26.5% | 3.71 | -0.9% |
| AS Roma win | 37.7% | 35.9% | 2.77 | +4.3% |
| Over 2.5 | 45.0% | 58.5% | 1.69 | -24.0% |
| Under 2.5 | 55.0% | 41.5% | 2.37 | +30.4% |

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
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.07 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.40 |
| Fair Over 2.5 odds | 2.22 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.23 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.48 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 27.0% |
| Unadjusted away-win probability | 39.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.62 |
| Reference draw odds | 3.71 |
| Reference away odds | 2.75 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.37 |
| Home probability edge | -2.1% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -13.5% |
| Under 2.5 probability edge | +13.5% |
| Raw edge prob home | -0.0411 |
| Raw ev home | -0.0740 |
| Raw edge prob draw | 0.0050 |
| Raw ev draw | 0.0006 |
| Raw edge prob away | 0.0361 |
| Raw ev away | 0.0935 |

</details>


---

## 2026-10-11 — Lazio vs Monza

The model's most likely 1X2 outcome is **Lazio win** at **62.5%**. Expected goals are 2.01 for Lazio and 0.87 for Monza (2.88 combined). The most likely exact score is 2-0 at 11.1%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 54.3%; Under 4.5 goals: 83.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 62.5% | 1.60 |
| Draw | 22.0% | 4.55 |
| Monza win | 15.5% | 6.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 2.01 |
| Monza expected goals | 0.87 |
| Expected total goals | 2.88 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 54.3% |
| Under 2.5 | 45.7% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.10% |
| 2 | 1-0 | 11.08% |
| 3 | 1-1 | 10.44% |
| 4 | 2-1 | 9.61% |
| 5 | 3-0 | 7.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 62.5% | 60.9% | 1.64 | +2.5% |
| Draw | 22.0% | 23.4% | 4.22 | -7.3% |
| Monza win | 15.5% | 15.7% | 6.20 | -3.7% |
| Over 2.5 | 54.3% | 50.4% | 1.96 | +6.4% |
| Under 2.5 | 45.7% | 49.6% | 2.08 | -4.9% |

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
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.75 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.17 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 64.1% |
| Unadjusted draw probability | 20.5% |
| Unadjusted away-win probability | 15.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.63 |
| Reference draw odds | 4.17 |
| Reference away odds | 6.18 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.99 |
| Home probability edge | +1.6% |
| Draw probability edge | -1.5% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +3.9% |
| Under 2.5 probability edge | -3.9% |
| Raw edge prob home | 0.0326 |
| Raw ev home | 0.0517 |
| Raw edge prob draw | -0.0292 |
| Raw ev draw | -0.1346 |
| Raw edge prob away | -0.0034 |
| Raw ev away | -0.0474 |

</details>


---

## 2026-10-11 — Lecce vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **49.9%**. Expected goals are 0.78 for Lecce and 1.33 for Bologna (2.11 combined). The most likely exact score is 0-1 at 16.2%. Goal-market probabilities: at least one goal: 87.9%; Over 2.5 goals: 35.3%; Under 4.5 goals: 93.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 21.7% | 4.61 |
| Draw | 28.4% | 3.52 |
| Bologna win | 49.9% | 2.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.78 |
| Bologna expected goals | 1.33 |
| Expected total goals | 2.11 |
| Over 0.5 | 87.9% |
| Under 0.5 | 12.1% |
| Over 1.5 | 62.3% |
| Under 1.5 | 37.7% |
| Over 2.5 | 35.3% |
| Under 2.5 | 64.7% |
| Over 3.5 | 16.4% |
| Under 3.5 | 83.6% |
| Over 4.5 | 6.3% |
| Under 4.5 | 93.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.21% |
| 2 | 1-1 | 12.59% |
| 3 | 0-0 | 12.10% |
| 4 | 0-2 | 10.74% |
| 5 | 1-0 | 9.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 21.7% | 21.4% | 4.68 | +1.5% |
| Draw | 28.4% | 28.6% | 3.50 | -0.6% |
| Bologna win | 49.9% | 50.0% | 1.98 | -1.2% |
| Over 2.5 | 35.3% | 45.5% | 2.18 | -23.0% |
| Under 2.5 | 64.7% | 54.5% | 1.81 | +17.0% |

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
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.26 |
| Fair Over 1.5 odds | 1.60 |
| Fair Under 1.5 odds | 2.65 |
| Fair Over 2.5 odds | 2.83 |
| Fair Under 2.5 odds | 1.55 |
| Fair Over 3.5 odds | 6.10 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.80 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 22.0% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 49.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 4.58 |
| Reference draw odds | 3.44 |
| Reference away odds | 1.98 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.16 |
| Reference Under 2.5 odds | 1.81 |
| Home probability edge | +0.3% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -10.2% |
| Under 2.5 probability edge | +10.2% |
| Raw edge prob home | 0.0063 |
| Raw ev home | 0.0302 |
| Raw edge prob draw | -0.0037 |
| Raw ev draw | -0.0127 |
| Raw edge prob away | -0.0025 |
| Raw ev away | -0.0144 |

</details>


---

## 2026-10-11 — Sassuolo vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **51.7%**. Expected goals are 1.13 for Sassuolo and 1.68 for AC Milan (2.81 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 53.3%; Under 4.5 goals: 84.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 23.8% | 4.19 |
| Draw | 24.5% | 4.08 |
| AC Milan win | 51.7% | 1.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.13 |
| AC Milan expected goals | 1.68 |
| Expected total goals | 2.81 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 53.3% |
| Under 2.5 | 46.7% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.58% |
| 2 | 0-1 | 10.42% |
| 3 | 1-2 | 9.85% |
| 4 | 0-2 | 8.72% |
| 5 | 1-0 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 23.8% | 22.1% | 4.45 | +6.1% |
| Draw | 24.5% | 25.0% | 3.95 | -3.2% |
| AC Milan win | 51.7% | 52.9% | 1.89 | -2.4% |
| Over 2.5 | 53.3% | 52.7% | 1.87 | -0.4% |
| Under 2.5 | 46.7% | 47.3% | 2.20 | +2.8% |

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
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.50 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.48 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 25.6% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 50.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 4.42 |
| Reference draw odds | 3.91 |
| Reference away odds | 1.87 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | +1.8% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | 0.0353 |
| Raw ev home | 0.1394 |
| Raw edge prob draw | -0.0100 |
| Raw ev draw | -0.0517 |
| Raw edge prob away | -0.0254 |
| Raw ev away | -0.0477 |

</details>


---

## 2026-10-12 — Atalanta BC vs Venezia

The model's most likely 1X2 outcome is **Atalanta BC win** at **67.5%**. Expected goals are 2.35 for Atalanta BC and 0.66 for Venezia (3.02 combined). The most likely exact score is 2-0 at 12.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 55.7%; Under 4.5 goals: 82.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 67.5% | 1.48 |
| Draw | 19.7% | 5.08 |
| Venezia win | 12.8% | 7.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.35 |
| Venezia expected goals | 0.66 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.8% |
| Under 1.5 | 21.2% |
| Over 2.5 | 55.7% |
| Under 2.5 | 44.3% |
| Over 3.5 | 34.0% |
| Under 3.5 | 66.0% |
| Over 4.5 | 17.5% |
| Under 4.5 | 82.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.19% |
| 2 | 1-0 | 10.39% |
| 3 | 3-0 | 9.57% |
| 4 | 1-1 | 9.34% |
| 5 | 2-1 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 67.5% | 59.7% | 1.66 | +12.1% |
| Draw | 19.7% | 23.4% | 4.40 | -13.4% |
| Venezia win | 12.8% | 16.9% | 6.20 | -20.6% |
| Over 2.5 | 55.7% | 62.1% | 1.56 | -13.1% |
| Under 2.5 | 44.3% | 37.9% | 2.47 | +9.5% |

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
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.70 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.71 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.94 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.70 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 75.3% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 8.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.66 |
| Reference draw odds | 4.17 |
| Reference away odds | 5.72 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.47 |
| Home probability edge | +7.8% |
| Draw probability edge | -3.7% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.1565 |
| Raw ev home | 0.2506 |
| Raw edge prob draw | -0.0739 |
| Raw ev draw | -0.2971 |
| Raw edge prob away | -0.0825 |
| Raw ev away | -0.4615 |

</details>


---

## 2026-10-12 — Torino vs Udinese

The model's most likely 1X2 outcome is **Torino win** at **38.5%**. Expected goals are 1.29 for Torino and 1.35 for Udinese (2.64 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.6%; Under 4.5 goals: 87.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 38.5% | 2.60 |
| Draw | 27.7% | 3.61 |
| Udinese win | 33.8% | 2.96 |

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
| 1 | 1-1 | 13.15% |
| 2 | 1-0 | 10.03% |
| 3 | 2-1 | 8.66% |
| 4 | 0-1 | 8.56% |
| 5 | 0-0 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 38.5% | 41.3% | 2.44 | -6.1% |
| Draw | 27.7% | 29.3% | 3.35 | -7.3% |
| Udinese win | 33.8% | 29.3% | 3.35 | +13.3% |
| Over 2.5 | 48.6% | 44.5% | 2.24 | +8.8% |
| Under 2.5 | 51.4% | 55.5% | 1.79 | -8.0% |

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
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.28 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.68 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.93 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 38.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.39 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.21 |
| Reference Under 2.5 odds | 1.78 |
| Home probability edge | -2.8% |
| Draw probability edge | -1.7% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | +4.1% |
| Under 2.5 probability edge | -4.1% |
| Raw edge prob home | -0.0566 |
| Raw ev home | -0.1299 |
| Raw edge prob draw | -0.0332 |
| Raw ev draw | -0.1285 |
| Raw edge prob away | 0.0899 |
| Raw ev away | 0.2839 |

</details>


---

## 2026-10-16 — Frosinone vs Sassuolo

The model's most likely 1X2 outcome is **Frosinone win** at **46.6%**. Expected goals are 1.84 for Frosinone and 1.12 for Sassuolo (2.95 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.4%; Under 4.5 goals: 83.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 46.6% | 2.14 |
| Draw | 25.2% | 3.96 |
| Sassuolo win | 28.1% | 3.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.84 |
| Sassuolo expected goals | 1.12 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 78.8% |
| Under 1.5 | 21.2% |
| Over 2.5 | 55.4% |
| Under 2.5 | 44.6% |
| Over 3.5 | 33.6% |
| Under 3.5 | 66.4% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.82% |
| 2 | 2-1 | 8.44% |
| 3 | 1-0 | 8.29% |
| 4 | 2-0 | 7.56% |
| 5 | 1-2 | 7.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 46.6% | 39.0% | 2.55 | +18.9% |
| Draw | 25.2% | 27.7% | 3.70 | -6.7% |
| Sassuolo win | 28.1% | 33.3% | 2.96 | -16.7% |
| Over 2.5 | 55.4% | 62.1% | 1.61 | -10.8% |
| Under 2.5 | 44.6% | 37.9% | 2.47 | +10.1% |

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
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.43 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.71 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 2.98 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.87 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.3% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 23.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.53 |
| Reference draw odds | 3.54 |
| Reference away odds | 2.96 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.47 |
| Home probability edge | +7.6% |
| Draw probability edge | -2.5% |
| Away probability edge | -5.1% |
| Over 2.5 probability edge | -6.7% |
| Under 2.5 probability edge | +6.7% |
| Raw edge prob home | 0.1525 |
| Raw ev home | 0.3834 |
| Raw edge prob draw | -0.0502 |
| Raw ev draw | -0.1594 |
| Raw edge prob away | -0.1023 |
| Raw ev away | -0.3183 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **71.1%**. Expected goals are 2.01 for AS Roma and 0.66 for Genoa (2.67 combined). The most likely exact score is 1-0 at 14.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 50.4%; Under 4.5 goals: 86.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 71.1% | 1.41 |
| Draw | 18.5% | 5.41 |
| Genoa win | 10.4% | 9.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 2.01 |
| Genoa expected goals | 0.66 |
| Expected total goals | 2.67 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.37% |
| 2 | 2-0 | 14.36% |
| 3 | 3-0 | 9.60% |
| 4 | 2-1 | 9.50% |
| 5 | 1-1 | 8.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 71.1% | 73.0% | 1.36 | -3.4% |
| Draw | 18.5% | 17.4% | 5.70 | +5.4% |
| Genoa win | 10.4% | 9.6% | 10.50 | +9.7% |
| Over 2.5 | 50.4% | 57.5% | 1.72 | -13.3% |
| Under 2.5 | 49.6% | 42.5% | 2.31 | +14.5% |

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
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.38 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.97 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.43 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 11.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.36 |
| Reference draw odds | 5.53 |
| Reference away odds | 9.90 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.31 |
| Home probability edge | -2.0% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | -0.0392 |
| Raw ev home | -0.0603 |
| Raw edge prob draw | 0.0221 |
| Raw ev draw | 0.1172 |
| Raw edge prob away | 0.0171 |
| Raw ev away | 0.1866 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **60.2%**. Expected goals are 1.07 for Bologna and 2.13 for Inter Milan (3.21 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 61.5%; Under 4.5 goals: 78.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.9% | 5.59 |
| Draw | 21.9% | 4.56 |
| Inter Milan win | 60.2% | 1.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.07 |
| Inter Milan expected goals | 2.13 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 39.7% |
| Under 3.5 | 60.3% |
| Over 4.5 | 21.7% |
| Under 4.5 | 78.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.06% |
| 2 | 1-2 | 9.65% |
| 3 | 0-2 | 9.00% |
| 4 | 0-1 | 8.49% |
| 5 | 1-3 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.9% | 17.6% | 5.70 | +2.0% |
| Draw | 21.9% | 23.8% | 4.12 | -9.7% |
| Inter Milan win | 60.2% | 58.7% | 1.69 | +1.7% |
| Over 2.5 | 61.5% | 57.4% | 1.72 | +5.7% |
| Under 2.5 | 38.5% | 42.6% | 2.30 | -11.4% |

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
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.90 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.82 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.52 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.61 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 61.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 5.55 |
| Reference draw odds | 4.12 |
| Reference away odds | 1.69 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +0.3% |
| Draw probability edge | -1.8% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +4.1% |
| Under 2.5 probability edge | -4.1% |
| Raw edge prob home | 0.0069 |
| Raw ev home | 0.0399 |
| Raw edge prob draw | -0.0366 |
| Raw ev draw | -0.1722 |
| Raw edge prob away | 0.0297 |
| Raw ev away | 0.0421 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **64.2%**. Expected goals are 0.67 for Venezia and 2.18 for Napoli (2.85 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 52.2%; Under 4.5 goals: 85.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 15.3% | 6.52 |
| Draw | 20.5% | 4.88 |
| Napoli win | 64.2% | 1.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.18 |
| Expected total goals | 2.85 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 76.1% |
| Under 1.5 | 23.9% |
| Over 2.5 | 52.2% |
| Under 2.5 | 47.8% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.24% |
| 2 | 0-1 | 11.30% |
| 3 | 1-1 | 9.68% |
| 4 | 0-3 | 8.88% |
| 5 | 1-2 | 8.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 15.3% | 20.6% | 4.80 | -26.4% |
| Draw | 20.5% | 23.1% | 4.22 | -13.6% |
| Napoli win | 64.2% | 56.3% | 1.76 | +12.9% |
| Over 2.5 | 52.2% | 56.4% | 1.75 | -8.7% |
| Under 2.5 | 47.8% | 43.6% | 2.25 | +7.6% |

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
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.10 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.18 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.67 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 4.74 |
| Reference draw odds | 4.22 |
| Reference away odds | 1.76 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -5.2% |
| Draw probability edge | -2.7% |
| Away probability edge | +7.9% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | -0.1045 |
| Raw ev home | -0.5144 |
| Raw edge prob draw | -0.0531 |
| Raw ev draw | -0.2477 |
| Raw edge prob away | 0.1576 |
| Raw ev away | 0.2682 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **45.4%**. Expected goals are 1.28 for AC Milan and 1.16 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 44.4%; Under 4.5 goals: 89.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 45.4% | 2.20 |
| Draw | 26.3% | 3.80 |
| Atalanta BC win | 28.3% | 3.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.28 |
| Atalanta BC expected goals | 1.16 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.4% |
| Under 2.5 | 55.6% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.95% |
| 2 | 1-1 | 12.45% |
| 3 | 2-1 | 9.55% |
| 4 | 0-1 | 8.61% |
| 5 | 0-0 | 8.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 45.4% | 51.3% | 1.93 | -12.3% |
| Draw | 26.3% | 25.4% | 3.86 | +1.5% |
| Atalanta BC win | 28.3% | 23.2% | 4.30 | +21.6% |
| Over 2.5 | 44.4% | 53.9% | 1.83 | -18.7% |
| Under 2.5 | 55.6% | 46.1% | 2.13 | +18.4% |

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
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.95 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.79 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 33.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.93 |
| Reference draw odds | 3.86 |
| Reference away odds | 4.22 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.13 |
| Home probability edge | -5.9% |
| Draw probability edge | +0.9% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | -0.1186 |
| Raw ev home | -0.2379 |
| Raw edge prob draw | 0.0176 |
| Raw ev draw | 0.0493 |
| Raw edge prob away | 0.1010 |
| Raw ev away | 0.4332 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.5%**. Expected goals are 1.00 for Fiorentina and 1.73 for Como (2.73 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 50.8%; Under 4.5 goals: 86.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.8% | 4.03 |
| Draw | 24.7% | 4.06 |
| Como win | 50.5% | 1.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.00 |
| Como expected goals | 1.73 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 50.8% |
| Under 2.5 | 49.2% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.72% |
| 2 | 0-1 | 10.49% |
| 3 | 0-2 | 9.04% |
| 4 | 1-2 | 9.03% |
| 5 | 1-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.8% | 27.9% | 3.65 | -9.4% |
| Draw | 24.7% | 25.7% | 3.81 | -6.1% |
| Como win | 50.5% | 46.4% | 2.13 | +7.6% |
| Over 2.5 | 50.8% | 57.1% | 1.73 | -12.1% |
| Under 2.5 | 49.2% | 42.9% | 2.29 | +12.6% |

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
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.82 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.04 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.20 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 21.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 54.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.52 |
| Reference draw odds | 3.81 |
| Reference away odds | 2.13 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.29 |
| Home probability edge | -3.1% |
| Draw probability edge | -1.1% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.0612 |
| Raw ev home | -0.2061 |
| Raw edge prob draw | -0.0213 |
| Raw ev draw | -0.1014 |
| Raw edge prob away | 0.0825 |
| Raw ev away | 0.1643 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **54.1%**. Expected goals are 1.37 for Juventus and 0.85 for Lazio (2.22 combined). The most likely exact score is 1-0 at 16.5%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 39.0%; Under 4.5 goals: 92.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 54.1% | 1.85 |
| Draw | 25.7% | 3.90 |
| Lazio win | 20.3% | 4.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.85 |
| Expected total goals | 2.22 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.7% |
| Under 3.5 | 81.3% |
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.48% |
| 2 | 1-1 | 11.71% |
| 3 | 2-0 | 11.22% |
| 4 | 0-0 | 10.06% |
| 5 | 2-1 | 9.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 54.1% | 59.0% | 1.68 | -9.2% |
| Draw | 25.7% | 23.7% | 4.12 | +5.7% |
| Lazio win | 20.3% | 17.2% | 5.80 | +17.6% |
| Over 2.5 | 39.0% | 50.1% | 1.99 | -22.3% |
| Under 2.5 | 61.0% | 49.9% | 1.98 | +20.7% |

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
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.94 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.34 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.01 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 23.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.68 |
| Reference draw odds | 4.12 |
| Reference away odds | 5.66 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.98 |
| Home probability edge | -5.0% |
| Draw probability edge | +1.9% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -11.1% |
| Under 2.5 probability edge | +11.1% |
| Raw edge prob home | -0.0999 |
| Raw ev home | -0.1759 |
| Raw edge prob draw | 0.0384 |
| Raw ev draw | 0.1365 |
| Raw edge prob away | 0.0616 |
| Raw ev away | 0.3549 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.2%**. Expected goals are 1.44 for Udinese and 0.82 for Lecce (2.26 combined). The most likely exact score is 1-0 at 14.9%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 39.4%; Under 4.5 goals: 92.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.2% | 1.95 |
| Draw | 26.6% | 3.75 |
| Lecce win | 22.1% | 4.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.44 |
| Lecce expected goals | 0.82 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.7% |
| Under 0.5 | 10.3% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.4% |
| Under 2.5 | 60.6% |
| Over 3.5 | 19.2% |
| Under 3.5 | 80.8% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.94% |
| 2 | 1-1 | 12.20% |
| 3 | 2-0 | 10.69% |
| 4 | 0-0 | 10.30% |
| 5 | 0-1 | 8.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.2% | 50.8% | 1.95 | -0.1% |
| Draw | 26.6% | 26.5% | 3.71 | -1.1% |
| Lecce win | 22.1% | 22.7% | 4.40 | -2.6% |
| Over 2.5 | 39.4% | 49.2% | 2.00 | -21.3% |
| Under 2.5 | 60.6% | 50.8% | 1.94 | +17.6% |

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
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.71 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.54 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.20 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.63 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 21.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.95 |
| Reference draw odds | 3.71 |
| Reference away odds | 4.32 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.94 |
| Home probability edge | +0.4% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | 0.0077 |
| Raw ev home | 0.0061 |
| Raw edge prob draw | 0.0033 |
| Raw ev draw | -0.0054 |
| Raw edge prob away | -0.0110 |
| Raw ev away | -0.0498 |

</details>


---
