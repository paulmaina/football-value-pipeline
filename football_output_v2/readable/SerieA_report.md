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
| Additional event odds calls used before this league | 15.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 5.00 |
| Additional event odds calls this league | 5.00 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-10 — Genoa vs Fiorentina

The model's most likely 1X2 outcome is **Fiorentina win** at **40.3%**. Expected goals are 1.17 for Genoa and 1.29 for Fiorentina (2.46 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 44.4%; Under 4.5 goals: 89.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 32.1% | 3.11 |
| Draw | 27.6% | 3.63 |
| Fiorentina win | 40.3% | 2.48 |

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
| 1 | 1-1 | 13.05% |
| 2 | 0-1 | 11.40% |
| 3 | 1-0 | 9.64% |
| 4 | 0-0 | 8.65% |
| 5 | 1-2 | 8.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 32.1% | 30.6% | 3.45 | +10.9% |
| Draw | 27.6% | 28.0% | 3.48 | -4.1% |
| Fiorentina win | 40.3% | 41.4% | 2.39 | -3.7% |
| Over 2.5 | 44.4% | 47.1% | 2.16 | -4.2% |
| Under 2.5 | 55.6% | 52.9% | 1.87 | +4.0% |

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
| Market best home last update utc | 2026-10-09T14:38:11Z |
| Market best draw last update utc | 2026-10-09T14:37:37Z |
| Market best away last update utc | 2026-10-09T14:37:37Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Genoa |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.56 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.37 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.29 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.74 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 49.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 3.10 |
| Reference draw odds | 3.37 |
| Reference away odds | 2.32 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +1.6% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | 0.0315 |
| Raw ev home | 0.1633 |
| Raw edge prob draw | -0.0092 |
| Raw ev draw | -0.0572 |
| Raw edge prob away | -0.0223 |
| Raw ev away | -0.0634 |

</details>


---

## 2026-10-10 — Inter Milan vs Parma

The model's most likely 1X2 outcome is **Inter Milan win** at **81.7%**. Expected goals are 2.47 for Inter Milan and 0.67 for Parma (3.14 combined). The most likely exact score is 2-0 at 14.1%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 62.3%; Under 4.5 goals: 78.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 81.7% | 1.22 |
| Draw | 12.0% | 8.31 |
| Parma win | 6.3% | 15.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.47 |
| Parma expected goals | 0.67 |
| Expected total goals | 3.14 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 62.3% |
| Under 2.5 | 37.7% |
| Over 3.5 | 39.3% |
| Under 3.5 | 60.7% |
| Over 4.5 | 21.6% |
| Under 4.5 | 78.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.06% |
| 2 | 3-0 | 11.56% |
| 3 | 1-0 | 11.44% |
| 4 | 2-1 | 9.40% |
| 5 | 3-1 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 81.7% | 86.5% | 1.17 | -4.4% |
| Draw | 12.0% | 9.1% | 10.50 | +26.4% |
| Parma win | 6.3% | 4.4% | 22.00 | +37.9% |
| Over 2.5 | 62.3% | 71.8% | 1.36 | -15.3% |
| Under 2.5 | 37.7% | 28.2% | 3.20 | +20.7% |

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
| Market best home last update utc | 2026-10-09T14:37:37Z |
| Market best draw last update utc | 2026-10-09T14:38:26Z |
| Market best away last update utc | 2026-10-09T14:38:11Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Inter |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 43.4% |
| P btts no | 56.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.90 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.82 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.65 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.62 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 76.9% |
| Unadjusted draw probability | 15.0% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 61.7% |
| Raw p btts yes | 44.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.14 |
| Reference draw odds | 8.71 |
| Reference away odds | 16.62 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.15 |
| Home probability edge | -4.8% |
| Draw probability edge | +3.0% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | -0.0958 |
| Raw ev home | -0.1003 |
| Raw edge prob draw | 0.0592 |
| Raw ev draw | 0.5748 |
| Raw edge prob away | 0.0367 |
| Raw ev away | 0.7827 |
| Market p over 1 5 | 92.1% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T14:37:37Z |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 6.10 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 49.9% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T14:38:36Z |
| Market reference under 3 5 odds | 1.94 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 43.7% |
| Market btts yes odds | 2.26 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T14:38:26Z |
| Market reference btts yes odds | 2.26 |
| Market reference btts yes opposite odds | 1.76 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-10 — Napoli vs Frosinone

The model's most likely 1X2 outcome is **Napoli win** at **55.3%**. Expected goals are 1.39 for Napoli and 1.08 for Frosinone (2.47 combined). The most likely exact score is 1-0 at 14.9%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 46.2%; Under 4.5 goals: 89.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 55.3% | 1.81 |
| Draw | 23.1% | 4.34 |
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
| 2 | 2-1 | 11.07% |
| 3 | 1-1 | 10.92% |
| 4 | 2-0 | 10.25% |
| 5 | 0-0 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 55.3% | 66.5% | 1.49 | -17.6% |
| Draw | 23.1% | 19.4% | 5.20 | +19.9% |
| Frosinone win | 21.7% | 14.0% | 7.20 | +56.0% |
| Over 2.5 | 46.2% | 65.4% | 1.49 | -31.1% |
| Under 2.5 | 53.8% | 34.6% | 2.67 | +43.6% |

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
| Market best home last update utc | 2026-10-09T14:37:37Z |
| Market best draw last update utc | 2026-10-09T14:38:11Z |
| Market best away last update utc | 2026-10-09T14:38:11Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Napoli |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.77 |
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
| Raw p over 1 5 | 70.5% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.47 |
| Reference draw odds | 4.71 |
| Reference away odds | 6.41 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -11.3% |
| Draw probability edge | +3.6% |
| Away probability edge | +7.6% |
| Over 2.5 probability edge | -19.2% |
| Under 2.5 probability edge | +19.2% |
| Raw edge prob home | -0.2254 |
| Raw ev home | -0.3443 |
| Raw edge prob draw | 0.0725 |
| Raw ev draw | 0.3871 |
| Raw edge prob away | 0.1529 |
| Raw ev away | 1.1109 |

</details>


---

## 2026-10-11 — Cagliari vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **57.7%**. Expected goals are 0.80 for Cagliari and 1.48 for Juventus (2.28 combined). The most likely exact score is 0-1 at 16.4%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 40.5%; Under 4.5 goals: 91.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 17.3% | 5.77 |
| Draw | 25.0% | 4.00 |
| Juventus win | 57.7% | 1.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 0.80 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.5% |
| Under 2.5 | 59.5% |
| Over 3.5 | 20.0% |
| Under 3.5 | 80.0% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.40% |
| 2 | 0-2 | 12.12% |
| 3 | 1-1 | 11.45% |
| 4 | 0-0 | 9.68% |
| 5 | 1-2 | 9.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 17.3% | 14.5% | 7.00 | +21.4% |
| Draw | 25.0% | 23.8% | 4.10 | +2.5% |
| Juventus win | 57.7% | 61.7% | 1.62 | -6.6% |
| Over 2.5 | 40.5% | 47.1% | 2.12 | -14.1% |
| Under 2.5 | 59.5% | 52.9% | 1.88 | +11.8% |

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
| Market best home last update utc | 2026-10-09T14:38:11Z |
| Market best draw last update utc | 2026-10-09T14:38:13Z |
| Market best away last update utc | 2026-10-09T14:37:37Z |
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
| P btts yes | 42.0% |
| P btts no | 58.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.33 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.47 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.00 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.97 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 53.6% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.3% |
| Raw p btts yes | 42.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 6.25 |
| Reference draw odds | 3.91 |
| Reference away odds | 1.58 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +2.8% |
| Draw probability edge | +1.2% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | 0.0569 |
| Raw ev home | 0.4127 |
| Raw edge prob draw | 0.0249 |
| Raw ev draw | 0.0762 |
| Raw edge prob away | -0.0818 |
| Raw ev away | -0.1322 |

</details>


---

## 2026-10-11 — Como vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **38.0%**. Expected goals are 1.17 for Como and 1.30 for AS Roma (2.47 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 45.0%; Under 4.5 goals: 89.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 35.2% | 2.84 |
| Draw | 26.8% | 3.73 |
| AS Roma win | 38.0% | 2.63 |

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
| 1 | 1-1 | 12.71% |
| 2 | 0-1 | 10.60% |
| 3 | 1-0 | 10.47% |
| 4 | 0-0 | 8.30% |
| 5 | 1-2 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 35.2% | 36.9% | 2.70 | -4.9% |
| Draw | 26.8% | 26.6% | 3.71 | -0.6% |
| AS Roma win | 38.0% | 36.5% | 2.78 | +5.6% |
| Over 2.5 | 45.0% | 57.8% | 1.69 | -24.0% |
| Under 2.5 | 55.0% | 42.2% | 2.37 | +30.4% |

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
| Market best home last update utc | 2026-10-09T14:38:11Z |
| Market best draw last update utc | 2026-10-09T14:37:37Z |
| Market best away last update utc | 2026-10-09T14:38:11Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.04 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.40 |
| Fair Over 2.5 odds | 2.22 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.23 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.49 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 27.0% |
| Unadjusted away-win probability | 39.5% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.3% |
| Raw p btts yes | 50.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.59 |
| Reference draw odds | 3.54 |
| Reference away odds | 2.62 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.24 |
| Home probability edge | -1.7% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -12.8% |
| Under 2.5 probability edge | +12.8% |
| Raw edge prob home | -0.0336 |
| Raw ev home | -0.0941 |
| Raw edge prob draw | 0.0036 |
| Raw ev draw | 0.0006 |
| Raw edge prob away | 0.0300 |
| Raw ev away | 0.0974 |

</details>


---

## 2026-10-11 — Lazio vs Monza

The model's most likely 1X2 outcome is **Lazio win** at **62.9%**. Expected goals are 2.01 for Lazio and 0.87 for Monza (2.88 combined). The most likely exact score is 2-0 at 11.2%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 54.4%; Under 4.5 goals: 83.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 62.9% | 1.59 |
| Draw | 21.8% | 4.59 |
| Monza win | 15.3% | 6.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 2.01 |
| Monza expected goals | 0.87 |
| Expected total goals | 2.88 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 54.4% |
| Under 2.5 | 45.6% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.3% |
| Under 4.5 | 83.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.18% |
| 2 | 1-0 | 11.16% |
| 3 | 1-1 | 10.36% |
| 4 | 2-1 | 9.68% |
| 5 | 3-0 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 62.9% | 61.8% | 1.66 | +4.5% |
| Draw | 21.8% | 23.1% | 4.22 | -8.0% |
| Monza win | 15.3% | 15.2% | 6.20 | -5.4% |
| Over 2.5 | 54.4% | 50.1% | 1.96 | +6.6% |
| Under 2.5 | 45.6% | 49.9% | 2.04 | -7.0% |

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
| Market best home last update utc | 2026-10-09T14:38:11Z |
| Market best draw last update utc | 2026-10-09T14:37:38Z |
| Market best away last update utc | 2026-10-09T14:38:11Z |
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
| P btts yes | 50.5% |
| P btts no | 49.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.88 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.55 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.15 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 64.1% |
| Unadjusted draw probability | 20.5% |
| Unadjusted away-win probability | 15.4% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 67.5% |
| Raw p btts yes | 50.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.58 |
| Reference draw odds | 4.02 |
| Reference away odds | 5.99 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.89 |
| Home probability edge | +1.2% |
| Draw probability edge | -1.3% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +4.2% |
| Under 2.5 probability edge | -4.2% |
| Raw edge prob home | 0.0237 |
| Raw ev home | 0.0645 |
| Raw edge prob draw | -0.0258 |
| Raw ev draw | -0.1346 |
| Raw edge prob away | 0.0020 |
| Raw ev away | -0.0474 |

</details>


---

## 2026-10-11 — Lecce vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **49.8%**. Expected goals are 0.78 for Lecce and 1.33 for Bologna (2.11 combined). The most likely exact score is 0-1 at 16.2%. Goal-market probabilities: at least one goal: 87.9%; Over 2.5 goals: 35.4%; Under 4.5 goals: 93.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 21.9% | 4.56 |
| Draw | 28.3% | 3.54 |
| Bologna win | 49.8% | 2.01 |

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
| Over 2.5 | 35.4% |
| Under 2.5 | 64.6% |
| Over 3.5 | 16.4% |
| Under 3.5 | 83.6% |
| Over 4.5 | 6.3% |
| Under 4.5 | 93.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.17% |
| 2 | 1-1 | 12.54% |
| 3 | 0-0 | 12.05% |
| 4 | 0-2 | 10.72% |
| 5 | 1-0 | 9.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 21.9% | 21.9% | 4.70 | +3.1% |
| Draw | 28.3% | 28.3% | 3.50 | -1.1% |
| Bologna win | 49.8% | 49.8% | 1.98 | -1.4% |
| Over 2.5 | 35.4% | 45.3% | 2.18 | -22.9% |
| Under 2.5 | 64.6% | 54.7% | 1.81 | +17.0% |

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
| Market best home last update utc | 2026-10-09T14:38:13Z |
| Market best draw last update utc | 2026-10-09T14:38:11Z |
| Market best away last update utc | 2026-10-09T14:37:37Z |
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
| P btts yes | 39.8% |
| P btts no | 60.2% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.30 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.65 |
| Fair Over 2.5 odds | 2.83 |
| Fair Under 2.5 odds | 1.55 |
| Fair Over 3.5 odds | 6.11 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.79 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 22.0% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 62.3% |
| Raw p under 3 5 | 83.6% |
| Raw p btts yes | 39.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 4.34 |
| Reference draw odds | 3.38 |
| Reference away odds | 1.96 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.73 |
| Home probability edge | +0.1% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | 0.0015 |
| Raw ev home | 0.0346 |
| Raw edge prob draw | -0.0012 |
| Raw ev draw | -0.0127 |
| Raw edge prob away | -0.0003 |
| Raw ev away | -0.0144 |
| Market p over 1 5 | 71.9% |
| Market over 1 5 odds | 1.40 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T14:38:11Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 3.26 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 77.1% |
| Market under 3 5 odds | 1.28 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T14:38:11Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 4.05 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 50.0% |
| Market btts yes odds | 1.97 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T14:38:26Z |
| Market reference btts yes odds | 1.97 |
| Market reference btts yes opposite odds | 1.97 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Sassuolo vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **51.7%**. Expected goals are 1.13 for Sassuolo and 1.68 for AC Milan (2.81 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 53.3%; Under 4.5 goals: 84.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 23.7% | 4.22 |
| Draw | 24.6% | 4.07 |
| AC Milan win | 51.7% | 1.93 |

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
| 1 | 1-1 | 11.62% |
| 2 | 0-1 | 10.43% |
| 3 | 1-2 | 9.86% |
| 4 | 0-2 | 8.73% |
| 5 | 1-0 | 6.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 23.7% | 21.8% | 4.50 | +6.7% |
| Draw | 24.6% | 25.2% | 3.91 | -3.9% |
| AC Milan win | 51.7% | 53.0% | 1.89 | -2.3% |
| Over 2.5 | 53.3% | 52.9% | 1.87 | -0.4% |
| Under 2.5 | 46.7% | 47.1% | 2.20 | +2.8% |

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
| Market best home last update utc | 2026-10-09T14:38:11Z |
| Market best draw last update utc | 2026-10-09T14:37:37Z |
| Market best away last update utc | 2026-10-09T14:38:11Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | BetAnything |
| Matched home-team name | Sassuolo |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.45 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.48 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 25.6% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 50.4% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 68.9% |
| Raw p btts yes | 55.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 4.26 |
| Reference draw odds | 3.72 |
| Reference away odds | 1.83 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 1.99 |
| Home probability edge | +1.9% |
| Draw probability edge | -0.6% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.0378 |
| Raw ev home | 0.1522 |
| Raw edge prob draw | -0.0116 |
| Raw ev draw | -0.0613 |
| Raw edge prob away | -0.0262 |
| Raw ev away | -0.0477 |

</details>


---

## 2026-10-12 — Atalanta BC vs Venezia

The model's most likely 1X2 outcome is **Atalanta BC win** at **67.9%**. Expected goals are 2.35 for Atalanta BC and 0.66 for Venezia (3.02 combined). The most likely exact score is 2-0 at 12.3%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.9%; Under 4.5 goals: 82.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 67.9% | 1.47 |
| Draw | 19.2% | 5.20 |
| Venezia win | 12.9% | 7.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.35 |
| Venezia expected goals | 0.66 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 78.8% |
| Under 1.5 | 21.2% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 34.1% |
| Under 3.5 | 65.9% |
| Over 4.5 | 17.6% |
| Under 4.5 | 82.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.26% |
| 2 | 1-0 | 10.45% |
| 3 | 3-0 | 9.62% |
| 4 | 1-1 | 9.12% |
| 5 | 2-1 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 67.9% | 60.5% | 1.66 | +12.8% |
| Draw | 19.2% | 22.5% | 4.40 | -15.5% |
| Venezia win | 12.9% | 17.0% | 6.20 | -20.2% |
| Over 2.5 | 55.9% | 62.7% | 1.56 | -12.8% |
| Under 2.5 | 44.1% | 37.3% | 2.47 | +9.0% |

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
| Market best home last update utc | 2026-10-09T14:37:37Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:38:11Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Codere (IT) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Atalanta |
| Matched away-team name | Venezia |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 45.1% |
| P btts no | 54.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.10 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.73 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.93 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.67 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 75.3% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 8.7% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 64.4% |
| Raw p btts yes | 43.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.61 |
| Reference draw odds | 4.12 |
| Reference away odds | 5.35 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | +7.4% |
| Draw probability edge | -3.2% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
| Raw edge prob home | 0.1483 |
| Raw ev home | 0.2506 |
| Raw edge prob draw | -0.0648 |
| Raw ev draw | -0.2971 |
| Raw edge prob away | -0.0836 |
| Raw ev away | -0.4615 |

</details>


---

## 2026-10-12 — Torino vs Udinese

The model's most likely 1X2 outcome is **Torino win** at **38.4%**. Expected goals are 1.29 for Torino and 1.35 for Udinese (2.64 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 48.7%; Under 4.5 goals: 87.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 38.4% | 2.61 |
| Draw | 27.2% | 3.67 |
| Udinese win | 34.4% | 2.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.29 |
| Udinese expected goals | 1.35 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.7% |
| Under 2.5 | 51.3% |
| Over 3.5 | 27.2% |
| Under 3.5 | 72.8% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.95% |
| 2 | 1-0 | 9.99% |
| 3 | 0-1 | 8.70% |
| 4 | 2-1 | 8.63% |
| 5 | 1-2 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 38.4% | 41.1% | 2.44 | -6.4% |
| Draw | 27.2% | 28.5% | 3.35 | -8.7% |
| Udinese win | 34.4% | 30.5% | 3.45 | +18.7% |
| Over 2.5 | 48.7% | 45.3% | 2.22 | +8.2% |
| Under 2.5 | 51.3% | 54.7% | 1.79 | -8.2% |

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
| Market best home last update utc | 2026-10-09T14:38:11Z |
| Market best draw last update utc | 2026-10-09T14:37:39Z |
| Market best away last update utc | 2026-10-09T14:38:26Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Torino |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.50 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.68 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.89 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 38.3% |
| Raw p over 1 5 | 73.9% |
| Raw p under 3 5 | 72.7% |
| Raw p btts yes | 53.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.34 |
| Reference draw odds | 3.32 |
| Reference away odds | 3.11 |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.76 |
| Home probability edge | -2.7% |
| Draw probability edge | -1.2% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | +3.4% |
| Under 2.5 probability edge | -3.4% |
| Raw edge prob home | -0.0540 |
| Raw ev home | -0.1299 |
| Raw edge prob draw | -0.0245 |
| Raw ev draw | -0.1285 |
| Raw edge prob away | 0.0785 |
| Raw ev away | 0.3222 |

</details>


---

## 2026-10-16 — Frosinone vs Sassuolo

The model's most likely 1X2 outcome is **Frosinone win** at **46.2%**. Expected goals are 1.84 for Frosinone and 1.12 for Sassuolo (2.95 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.5%; Under 4.5 goals: 82.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 46.2% | 2.17 |
| Draw | 25.0% | 4.00 |
| Sassuolo win | 28.8% | 3.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.84 |
| Sassuolo expected goals | 1.12 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 78.7% |
| Under 1.5 | 21.3% |
| Over 2.5 | 55.5% |
| Under 2.5 | 44.5% |
| Over 3.5 | 33.5% |
| Under 3.5 | 66.5% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.72% |
| 2 | 2-1 | 8.36% |
| 3 | 1-0 | 8.21% |
| 4 | 2-0 | 7.49% |
| 5 | 1-2 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 46.2% | 38.1% | 2.55 | +17.7% |
| Draw | 25.0% | 27.3% | 3.55 | -11.2% |
| Sassuolo win | 28.8% | 34.6% | 2.96 | -14.6% |
| Over 2.5 | 55.5% | 59.4% | 1.61 | -10.7% |
| Under 2.5 | 44.5% | 40.6% | 2.47 | +10.0% |

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
| Market best home last update utc | 2026-10-09T14:38:11Z |
| Market best draw last update utc | 2026-10-09T14:38:13Z |
| Market best away last update utc | 2026-10-09T14:37:37Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Unibet (SE) |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.59 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.70 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 2.98 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.3% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 79.3% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.43 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +8.1% |
| Draw probability edge | -2.3% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | 0.1618 |
| Raw ev home | 0.3834 |
| Raw edge prob draw | -0.0457 |
| Raw ev draw | -0.1935 |
| Raw edge prob away | -0.1161 |
| Raw ev away | -0.3183 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **72.4%**. Expected goals are 2.01 for AS Roma and 0.66 for Genoa (2.67 combined). The most likely exact score is 1-0 at 14.6%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 50.8%; Under 4.5 goals: 86.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 72.4% | 1.38 |
| Draw | 17.8% | 5.63 |
| Genoa win | 9.8% | 10.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 2.01 |
| Genoa expected goals | 0.66 |
| Expected total goals | 2.67 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 50.8% |
| Under 2.5 | 49.2% |
| Over 3.5 | 28.4% |
| Under 3.5 | 71.6% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.64% |
| 2 | 2-0 | 14.63% |
| 3 | 3-0 | 9.79% |
| 4 | 2-1 | 9.68% |
| 5 | 1-1 | 8.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 72.4% | 75.7% | 1.36 | -1.5% |
| Draw | 17.8% | 15.9% | 5.53 | -1.8% |
| Genoa win | 9.8% | 8.4% | 10.50 | +3.4% |
| Over 2.5 | 50.8% | 59.2% | 1.72 | -12.6% |
| Under 2.5 | 49.2% | 40.8% | 2.31 | +13.6% |

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
| Market best home last update utc | 2026-10-09T14:37:37Z |
| Market best draw last update utc | 2026-10-09T14:37:37Z |
| Market best away last update utc | 2026-10-09T14:37:39Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.02 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.52 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.34 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 11.3% |
| Raw p over 1 5 | 74.5% |
| Raw p under 3 5 | 72.1% |
| Raw p btts yes | 41.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.28 |
| Reference draw odds | 5.10 |
| Reference away odds | 9.00 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | -3.3% |
| Draw probability edge | +1.8% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | -0.0660 |
| Raw ev home | -0.0603 |
| Raw edge prob draw | 0.0368 |
| Raw ev draw | 0.0839 |
| Raw edge prob away | 0.0291 |
| Raw ev away | 0.1866 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.2%**. Expected goals are 1.07 for Bologna and 2.13 for Inter Milan (3.21 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 61.8%; Under 4.5 goals: 78.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.6% | 5.69 |
| Draw | 21.2% | 4.72 |
| Inter Milan win | 61.2% | 1.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.07 |
| Inter Milan expected goals | 2.13 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 61.8% |
| Under 2.5 | 38.2% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.82% |
| 2 | 1-1 | 9.72% |
| 3 | 0-2 | 9.16% |
| 4 | 0-1 | 8.63% |
| 5 | 1-3 | 6.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.6% | 16.9% | 5.70 | +0.3% |
| Draw | 21.2% | 22.3% | 4.20 | -11.0% |
| Inter Milan win | 61.2% | 60.8% | 1.69 | +3.5% |
| Over 2.5 | 61.8% | 56.2% | 1.72 | +6.3% |
| Under 2.5 | 38.2% | 43.8% | 2.30 | -12.1% |

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
| Market best home last update utc | 2026-10-09T14:37:57Z |
| Market best draw last update utc | 2026-10-09T14:37:39Z |
| Market best away last update utc | 2026-10-09T14:37:37Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bologna |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.2% |
| P btts no | 41.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.69 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.85 |
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
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 5.00 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.57 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | +0.7% |
| Draw probability edge | -1.1% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | +5.6% |
| Under 2.5 probability edge | -5.6% |
| Raw edge prob home | 0.0131 |
| Raw ev home | 0.0399 |
| Raw edge prob draw | -0.0218 |
| Raw ev draw | -0.1562 |
| Raw edge prob away | 0.0087 |
| Raw ev away | 0.0421 |
| Market p over 1 5 | 83.4% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T14:37:37Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 64.3% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T14:38:41Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.58 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 56.8% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T14:37:37Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.12 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **64.1%**. Expected goals are 0.67 for Venezia and 2.18 for Napoli (2.85 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 52.1%; Under 4.5 goals: 85.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 15.0% | 6.67 |
| Draw | 20.9% | 4.78 |
| Napoli win | 64.1% | 1.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.18 |
| Expected total goals | 2.85 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 76.1% |
| Under 1.5 | 23.9% |
| Over 2.5 | 52.1% |
| Under 2.5 | 47.9% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.22% |
| 2 | 0-1 | 11.28% |
| 3 | 1-1 | 9.89% |
| 4 | 0-3 | 8.86% |
| 5 | 1-2 | 8.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 15.0% | 19.9% | 4.74 | -28.9% |
| Draw | 20.9% | 24.0% | 4.22 | -11.7% |
| Napoli win | 64.1% | 56.1% | 1.76 | +12.8% |
| Over 2.5 | 52.1% | 56.0% | 1.75 | -8.9% |
| Under 2.5 | 47.9% | 44.0% | 2.25 | +7.9% |

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
| Market best home last update utc | 2026-10-09T14:37:37Z |
| Market best draw last update utc | 2026-10-09T14:37:37Z |
| Market best away last update utc | 2026-10-09T14:37:37Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 44.6% |
| P btts no | 55.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.78 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.19 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.68 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 72.1% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 43.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 4.40 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.70 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -4.9% |
| Draw probability edge | -3.1% |
| Away probability edge | +8.0% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0978 |
| Raw ev home | -0.5205 |
| Raw edge prob draw | -0.0620 |
| Raw ev draw | -0.2477 |
| Raw edge prob away | 0.1597 |
| Raw ev away | 0.2682 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **46.7%**. Expected goals are 1.28 for AC Milan and 1.16 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 44.5%; Under 4.5 goals: 89.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 46.7% | 2.14 |
| Draw | 25.9% | 3.86 |
| Atalanta BC win | 27.4% | 3.65 |

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
| Over 2.5 | 44.5% |
| Under 2.5 | 55.5% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.32% |
| 2 | 1-1 | 12.27% |
| 3 | 2-1 | 9.82% |
| 4 | 2-0 | 8.50% |
| 5 | 0-1 | 8.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 46.7% | 53.9% | 1.93 | -9.9% |
| Draw | 25.9% | 24.7% | 3.86 | +0.1% |
| Atalanta BC win | 27.4% | 21.4% | 4.30 | +17.7% |
| Over 2.5 | 44.5% | 55.4% | 1.83 | -18.5% |
| Under 2.5 | 55.5% | 44.6% | 2.13 | +18.1% |

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
| Market best home last update utc | 2026-10-09T14:37:37Z |
| Market best draw last update utc | 2026-10-09T14:37:37Z |
| Market best away last update utc | 2026-10-09T14:37:39Z |
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
| Fair Under 0.5 odds | 12.13 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.75 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 33.3% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.76 |
| Reference draw odds | 3.60 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -7.2% |
| Draw probability edge | +1.3% |
| Away probability edge | +6.0% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | -0.1444 |
| Raw ev home | -0.2379 |
| Raw edge prob draw | 0.0251 |
| Raw ev draw | 0.0493 |
| Raw edge prob away | 0.1192 |
| Raw ev away | 0.4332 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **51.6%**. Expected goals are 1.00 for Fiorentina and 1.73 for Como (2.73 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 50.9%; Under 4.5 goals: 86.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 23.8% | 4.20 |
| Draw | 24.6% | 4.07 |
| Como win | 51.6% | 1.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.00 |
| Como expected goals | 1.73 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 29.0% |
| Under 3.5 | 71.0% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.67% |
| 2 | 0-1 | 10.71% |
| 3 | 0-2 | 9.23% |
| 4 | 1-2 | 9.22% |
| 5 | 1-0 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 23.8% | 25.9% | 3.65 | -13.0% |
| Draw | 24.6% | 25.5% | 3.81 | -6.5% |
| Como win | 51.6% | 48.6% | 2.13 | +9.9% |
| Over 2.5 | 50.9% | 56.7% | 1.73 | -11.9% |
| Under 2.5 | 49.1% | 43.3% | 2.29 | +12.4% |

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
| Market best home last update utc | 2026-10-09T14:37:39Z |
| Market best draw last update utc | 2026-10-09T14:37:37Z |
| Market best away last update utc | 2026-10-09T14:37:37Z |
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
| P btts yes | 52.3% |
| P btts no | 47.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.88 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.45 |
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
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.45 |
| Reference draw odds | 3.50 |
| Reference away odds | 1.94 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -2.1% |
| Draw probability edge | -1.0% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0417 |
| Raw ev home | -0.2061 |
| Raw edge prob draw | -0.0193 |
| Raw ev draw | -0.1014 |
| Raw edge prob away | 0.0611 |
| Raw ev away | 0.1643 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **53.8%**. Expected goals are 1.37 for Juventus and 0.85 for Lazio (2.22 combined). The most likely exact score is 1-0 at 16.4%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 38.9%; Under 4.5 goals: 92.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 53.8% | 1.86 |
| Draw | 25.9% | 3.86 |
| Lazio win | 20.3% | 4.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.85 |
| Expected total goals | 2.22 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 38.9% |
| Under 2.5 | 61.1% |
| Over 3.5 | 18.7% |
| Under 3.5 | 81.3% |
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.41% |
| 2 | 1-1 | 11.82% |
| 3 | 2-0 | 11.18% |
| 4 | 0-0 | 10.16% |
| 5 | 2-1 | 9.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 53.8% | 58.6% | 1.69 | -9.0% |
| Draw | 25.9% | 24.2% | 4.04 | +4.7% |
| Lazio win | 20.3% | 17.2% | 5.71 | +15.7% |
| Over 2.5 | 38.9% | 48.8% | 2.03 | -20.9% |
| Under 2.5 | 61.1% | 51.2% | 1.92 | +17.2% |

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
| Market best home last update utc | 2026-10-09T14:37:37Z |
| Market best draw last update utc | 2026-10-09T14:37:37Z |
| Market best away last update utc | 2026-10-09T14:37:37Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Juventus |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.1% |
| P btts no | 57.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.85 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.34 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.05 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 23.4% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 42.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.63 |
| Reference draw odds | 3.65 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | -4.8% |
| Draw probability edge | +1.7% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | -0.0953 |
| Raw ev home | -0.1710 |
| Raw edge prob draw | 0.0334 |
| Raw ev draw | 0.1144 |
| Raw edge prob away | 0.0618 |
| Raw ev away | 0.3339 |
| Market p over 1 5 | 74.3% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-09T14:38:41Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.44 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 74.2% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T14:38:41Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 48.2% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-09T14:37:37Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 1.80 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **52.0%**. Expected goals are 1.44 for Udinese and 0.82 for Lecce (2.26 combined). The most likely exact score is 1-0 at 15.2%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 39.5%; Under 4.5 goals: 92.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 52.0% | 1.92 |
| Draw | 26.4% | 3.79 |
| Lecce win | 21.6% | 4.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.44 |
| Lecce expected goals | 0.82 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 66.0% |
| Under 1.5 | 34.0% |
| Over 2.5 | 39.5% |
| Under 2.5 | 60.5% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.18% |
| 2 | 1-1 | 12.09% |
| 3 | 2-0 | 10.86% |
| 4 | 0-0 | 10.21% |
| 5 | 2-1 | 8.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 52.0% | 52.4% | 1.95 | +1.4% |
| Draw | 26.4% | 26.0% | 3.71 | -2.0% |
| Lecce win | 21.6% | 21.6% | 4.35 | -6.2% |
| Over 2.5 | 39.5% | 48.4% | 2.00 | -21.0% |
| Under 2.5 | 60.5% | 51.6% | 1.94 | +17.4% |

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
| Market best home last update utc | 2026-10-09T14:37:37Z |
| Market best draw last update utc | 2026-10-09T14:37:37Z |
| Market best away last update utc | 2026-10-09T14:37:39Z |
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
| P btts yes | 42.6% |
| P btts no | 57.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.80 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.57 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 21.6% |
| Raw p over 1 5 | 65.9% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 42.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.81 |
| Reference draw odds | 3.45 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.94 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | -0.4% |
| Draw probability edge | +0.4% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | -0.0085 |
| Raw ev home | 0.0061 |
| Raw edge prob draw | 0.0081 |
| Raw ev draw | -0.0054 |
| Raw edge prob away | 0.0005 |
| Raw ev away | -0.0606 |
| Market p over 1 5 | 74.9% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-09T14:38:41Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 74.3% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T14:38:41Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.45 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 52.5% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-09T14:38:43Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 1.95 |
| Market btts yes bookmakers | 2 |

</details>


---
