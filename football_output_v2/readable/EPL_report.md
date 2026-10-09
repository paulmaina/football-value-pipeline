# Premier League — football model report

Fixtures in this report: **19**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,190 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 365 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1333.746 |
| Base scoring parameter | 0.174 |
| Home-advantage parameter | 0.164 |
| Dixon-Coles low-score adjustment | -0.105 |
| Xi per day | 0.0019 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 19.00 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-10 — Arsenal vs Leeds United

The model's most likely 1X2 outcome is **Arsenal win** at **66.3%**. Expected goals are 1.76 for Arsenal and 0.68 for Leeds United (2.44 combined). The most likely exact score is 1-0 at 15.2%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 45.4%; Under 4.5 goals: 89.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 66.3% | 1.51 |
| Draw | 21.7% | 4.60 |
| Leeds United win | 12.0% | 8.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.76 |
| Leeds United expected goals | 0.68 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 71.7% |
| Under 1.5 | 28.3% |
| Over 2.5 | 45.4% |
| Under 2.5 | 54.6% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.18% |
| 2 | 2-0 | 14.38% |
| 3 | 1-1 | 10.06% |
| 4 | 2-1 | 9.76% |
| 5 | 0-0 | 8.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 66.3% | 70.3% | 1.44 | -4.5% |
| Draw | 21.7% | 18.6% | 5.30 | +15.2% |
| Leeds United win | 12.0% | 11.1% | 9.40 | +12.4% |
| Over 2.5 | 45.4% | 51.2% | 1.89 | -14.2% |
| Under 2.5 | 54.6% | 48.8% | 2.05 | +11.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T11:30:00+00:00 |
| Fixture id | b870dcfba5e5920d3f1551a3aa1ea435 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.67 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.26 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.52 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 62.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 12.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.41 |
| Reference draw odds | 5.15 |
| Reference away odds | 8.50 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.98 |
| Home probability edge | -4.0% |
| Draw probability edge | +3.1% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0798 |
| Raw ev home | -0.1028 |
| Raw edge prob draw | 0.0629 |
| Raw ev draw | 0.3191 |
| Raw edge prob away | 0.0169 |
| Raw ev away | 0.2037 |

</details>


---

## 2026-10-10 — Aston Villa vs Brentford

The model's most likely 1X2 outcome is **Aston Villa win** at **38.3%**. Expected goals are 1.59 for Aston Villa and 1.41 for Brentford (3.00 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 57.7%; Under 4.5 goals: 81.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 38.3% | 2.61 |
| Draw | 26.8% | 3.74 |
| Brentford win | 34.9% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.59 |
| Brentford expected goals | 1.41 |
| Expected total goals | 3.00 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 81.3% |
| Under 1.5 | 18.7% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 35.3% |
| Under 3.5 | 64.7% |
| Over 4.5 | 18.5% |
| Under 4.5 | 81.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.43% |
| 2 | 1-2 | 8.38% |
| 3 | 2-1 | 8.35% |
| 4 | 2-2 | 6.33% |
| 5 | 1-0 | 6.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 38.3% | 35.9% | 2.78 | +6.4% |
| Draw | 26.8% | 27.0% | 3.75 | +0.4% |
| Brentford win | 34.9% | 37.0% | 2.67 | -6.7% |
| Over 2.5 | 57.7% | 55.9% | 1.75 | +0.9% |
| Under 2.5 | 42.3% | 44.1% | 2.25 | -4.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T14:00:00+00:00 |
| Fixture id | 02e6c0ccb11bb7ce78989ce49d67110b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.18 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.34 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.83 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.41 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 40.6% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 32.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.73 |
| Reference draw odds | 3.61 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | +2.4% |
| Draw probability edge | -0.3% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | 0.0471 |
| Raw ev home | 0.1300 |
| Raw edge prob draw | -0.0052 |
| Raw ev draw | -0.0059 |
| Raw edge prob away | -0.0420 |
| Raw ev away | -0.1231 |

</details>


---

## 2026-10-10 — Chelsea vs Bournemouth

The model's most likely 1X2 outcome is **Chelsea win** at **51.2%**. Expected goals are 1.75 for Chelsea and 1.40 for Bournemouth (3.15 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 61.6%; Under 4.5 goals: 78.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 51.2% | 1.95 |
| Draw | 24.0% | 4.17 |
| Bournemouth win | 24.8% | 4.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.75 |
| Bournemouth expected goals | 1.40 |
| Expected total goals | 3.15 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 83.5% |
| Under 1.5 | 16.5% |
| Over 2.5 | 61.6% |
| Under 2.5 | 38.4% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.94% |
| 2 | 2-1 | 10.49% |
| 3 | 2-0 | 7.50% |
| 4 | 1-0 | 7.31% |
| 5 | 1-2 | 6.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 51.2% | 57.5% | 1.74 | -11.0% |
| Draw | 24.0% | 22.6% | 4.40 | +5.6% |
| Bournemouth win | 24.8% | 20.0% | 4.91 | +21.8% |
| Over 2.5 | 61.6% | 65.1% | 1.49 | -8.2% |
| Under 2.5 | 38.4% | 34.9% | 2.66 | +2.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T14:00:00+00:00 |
| Fixture id | 45d4a466e32cd2b4ea535207923ceaf5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Chelsea |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.69 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.07 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.67 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 44.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 29.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.72 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.85 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.66 |
| Home probability edge | -6.3% |
| Draw probability edge | +1.4% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.1262 |
| Raw ev home | -0.2193 |
| Raw edge prob draw | 0.0289 |
| Raw ev draw | 0.1198 |
| Raw edge prob away | 0.0973 |
| Raw ev away | 0.4573 |

</details>


---

## 2026-10-10 — Ipswich Town vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **45.6%**. Expected goals are 1.14 for Ipswich Town and 1.79 for Fulham (2.93 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 55.6%; Under 4.5 goals: 83.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 28.2% | 3.55 |
| Draw | 26.2% | 3.81 |
| Fulham win | 45.6% | 2.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.14 |
| Fulham expected goals | 1.79 |
| Expected total goals | 2.93 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 79.8% |
| Under 1.5 | 20.2% |
| Over 2.5 | 55.6% |
| Under 2.5 | 44.4% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.37% |
| 2 | 1-2 | 8.63% |
| 3 | 2-1 | 7.61% |
| 4 | 0-2 | 7.59% |
| 5 | 0-1 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 28.2% | 33.4% | 2.96 | -16.6% |
| Draw | 26.2% | 26.9% | 3.65 | -4.3% |
| Fulham win | 45.6% | 39.6% | 2.54 | +15.8% |
| Over 2.5 | 55.6% | 54.3% | 1.82 | +1.2% |
| Under 2.5 | 44.4% | 45.7% | 2.18 | -3.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T14:00:00+00:00 |
| Fixture id | 288b4ff00c79daa712c911c564fe1be7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Ipswich |
| Matched away-team name | Fulham |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.00 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.95 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.88 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 51.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.93 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.48 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.11 |
| Home probability edge | -5.3% |
| Draw probability edge | -0.7% |
| Away probability edge | +6.0% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | -0.1051 |
| Raw ev home | -0.3215 |
| Raw edge prob draw | -0.0146 |
| Raw ev draw | -0.0697 |
| Raw edge prob away | 0.1197 |
| Raw ev away | 0.3104 |

</details>


---

## 2026-10-10 — Manchester United vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Manchester United win** at **55.1%**. Expected goals are 1.93 for Manchester United and 1.19 for Tottenham Hotspur (3.12 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.7%; Under 4.5 goals: 79.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 55.1% | 1.82 |
| Draw | 23.4% | 4.28 |
| Tottenham Hotspur win | 21.6% | 4.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.93 |
| Tottenham Hotspur expected goals | 1.19 |
| Expected total goals | 3.12 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 60.7% |
| Under 2.5 | 39.3% |
| Over 3.5 | 38.2% |
| Under 3.5 | 61.8% |
| Over 4.5 | 20.8% |
| Under 4.5 | 79.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.81% |
| 2 | 2-1 | 10.05% |
| 3 | 2-0 | 8.45% |
| 4 | 1-0 | 7.65% |
| 5 | 3-1 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 55.1% | 56.5% | 1.76 | -3.1% |
| Draw | 23.4% | 22.6% | 4.50 | +5.2% |
| Tottenham Hotspur win | 21.6% | 21.0% | 4.80 | +3.5% |
| Over 2.5 | 60.7% | 64.2% | 1.51 | -8.3% |
| Under 2.5 | 39.3% | 35.8% | 2.60 | +2.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T16:30:00+00:00 |
| Fixture id | 22c9b2c43cbe1334381269550dab78e6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Man United |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.95 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.89 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.62 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.82 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 53.6% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 22.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.75 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.62 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.60 |
| Home probability edge | -1.4% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.0285 |
| Raw ev home | -0.0562 |
| Raw edge prob draw | 0.0164 |
| Raw ev draw | 0.0888 |
| Raw edge prob away | 0.0121 |
| Raw ev away | 0.0646 |

</details>


---

## 2026-10-10 — Sunderland vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **41.6%**. Expected goals are 1.20 for Sunderland and 1.44 for Brighton and Hove Albion (2.65 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 49.5%; Under 4.5 goals: 87.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 30.5% | 3.28 |
| Draw | 27.9% | 3.58 |
| Brighton and Hove Albion win | 41.6% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.20 |
| Brighton and Hove Albion expected goals | 1.44 |
| Expected total goals | 2.65 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 27.5% |
| Under 3.5 | 72.5% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.33% |
| 2 | 0-1 | 9.00% |
| 3 | 1-2 | 8.94% |
| 4 | 0-0 | 8.21% |
| 5 | 2-1 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 30.5% | 30.8% | 3.18 | -3.2% |
| Draw | 27.9% | 27.4% | 3.65 | +1.9% |
| Brighton and Hove Albion win | 41.6% | 41.9% | 2.42 | +0.8% |
| Over 2.5 | 49.5% | 53.6% | 1.88 | -6.9% |
| Under 2.5 | 50.5% | 46.4% | 2.10 | +6.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T14:00:00+00:00 |
| Fixture id | 380b8f24ec5430fb545a7490c1017285 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Sunderland |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.18 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.69 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 41.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.18 |
| Reference draw odds | 3.57 |
| Reference away odds | 2.35 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | -0.3% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | -0.0064 |
| Raw ev home | -0.0418 |
| Raw edge prob draw | 0.0112 |
| Raw ev draw | 0.0392 |
| Raw edge prob away | -0.0048 |
| Raw ev away | 0.0018 |

</details>


---

## 2026-10-11 — Crystal Palace vs Nottingham Forest

The model's most likely 1X2 outcome is **Crystal Palace win** at **35.5%**. Expected goals are 1.25 for Crystal Palace and 1.23 for Nottingham Forest (2.48 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 45.2%; Under 4.5 goals: 89.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 35.5% | 2.82 |
| Draw | 29.3% | 3.42 |
| Nottingham Forest win | 35.3% | 2.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.25 |
| Nottingham Forest expected goals | 1.23 |
| Expected total goals | 2.48 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 72.2% |
| Under 1.5 | 27.8% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.8% |
| Under 3.5 | 76.2% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.95% |
| 2 | 0-0 | 9.56% |
| 3 | 0-1 | 9.13% |
| 4 | 1-0 | 9.13% |
| 5 | 1-2 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 35.5% | 35.5% | 2.78 | -1.4% |
| Draw | 29.3% | 28.7% | 3.48 | +1.8% |
| Nottingham Forest win | 35.3% | 35.8% | 2.80 | -1.3% |
| Over 2.5 | 45.2% | 50.3% | 2.01 | -9.1% |
| Under 2.5 | 54.8% | 49.7% | 2.02 | +10.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | 86effab5c6e7bfd58c8e88b1fb7c6ba9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.46 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.59 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.21 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.40 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 35.4% |
| Unadjusted draw probability | 29.9% |
| Unadjusted away-win probability | 34.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.76 |
| Reference draw odds | 3.41 |
| Reference away odds | 2.74 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.94 |
| Home probability edge | -0.1% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | -0.0011 |
| Raw ev home | -0.0151 |
| Raw edge prob draw | 0.0120 |
| Raw ev draw | 0.0389 |
| Raw edge prob away | -0.0109 |
| Raw ev away | -0.0278 |

</details>


---

## 2026-10-11 — Hull City vs Everton

The model's most likely 1X2 outcome is **Hull City win** at **34.7%**. Expected goals are 1.09 for Hull City and 0.66 for Everton (1.74 combined). The most likely exact score is 0-0 at 16.9%. Goal-market probabilities: at least one goal: 83.1%; Over 2.5 goals: 26.0%; Under 4.5 goals: 96.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 34.7% | 2.88 |
| Draw | 31.4% | 3.18 |
| Everton win | 33.8% | 2.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.09 |
| Everton expected goals | 0.66 |
| Expected total goals | 1.74 |
| Over 0.5 | 83.1% |
| Under 0.5 | 16.9% |
| Over 1.5 | 52.7% |
| Under 1.5 | 47.3% |
| Over 2.5 | 26.0% |
| Under 2.5 | 74.0% |
| Over 3.5 | 9.7% |
| Under 3.5 | 90.3% |
| Over 4.5 | 3.3% |
| Under 4.5 | 96.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 16.86% |
| 2 | 0-1 | 16.60% |
| 3 | 1-0 | 13.88% |
| 4 | 1-1 | 12.39% |
| 5 | 2-0 | 8.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 34.7% | 25.3% | 3.90 | +35.5% |
| Draw | 31.4% | 27.8% | 3.62 | +13.8% |
| Everton win | 33.8% | 46.9% | 2.16 | -26.9% |
| Over 2.5 | 26.0% | 47.0% | 2.08 | -45.9% |
| Under 2.5 | 74.0% | 53.0% | 1.90 | +40.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | 0bdae4d304810578e47386606bff7106 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Hull |
| Matched away-team name | Everton |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.20 |
| Fair Under 0.5 odds | 5.93 |
| Fair Over 1.5 odds | 1.90 |
| Fair Under 1.5 odds | 2.11 |
| Fair Over 2.5 odds | 3.85 |
| Fair Under 2.5 odds | 1.35 |
| Fair Over 3.5 odds | 10.33 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.69 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 44.2% |
| Unadjusted draw probability | 35.0% |
| Unadjusted away-win probability | 20.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.85 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | +9.5% |
| Draw probability edge | +3.6% |
| Away probability edge | -13.1% |
| Over 2.5 probability edge | -21.0% |
| Under 2.5 probability edge | +21.0% |
| Raw edge prob home | 0.1896 |
| Raw ev home | 0.7246 |
| Raw edge prob draw | 0.0716 |
| Raw ev draw | 0.2671 |
| Raw edge prob away | -0.2612 |
| Raw ev away | -0.5513 |

</details>


---

## 2026-10-11 — Liverpool vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **40.7%**. Expected goals are 1.40 for Liverpool and 1.65 for Manchester City (3.05 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.8%; Under 4.5 goals: 80.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 33.4% | 3.00 |
| Draw | 25.9% | 3.86 |
| Manchester City win | 40.7% | 2.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.40 |
| Manchester City expected goals | 1.65 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 81.9% |
| Under 1.5 | 18.1% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 36.3% |
| Under 3.5 | 63.7% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.97% |
| 2 | 1-2 | 8.66% |
| 3 | 2-1 | 8.13% |
| 4 | 0-1 | 6.41% |
| 5 | 2-2 | 6.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 33.4% | 35.4% | 2.80 | -6.5% |
| Draw | 25.9% | 25.6% | 3.90 | +1.0% |
| Manchester City win | 40.7% | 39.0% | 2.57 | +4.6% |
| Over 2.5 | 58.8% | 62.0% | 1.60 | -5.9% |
| Under 2.5 | 41.2% | 38.0% | 2.46 | +1.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T15:30:00+00:00 |
| Fixture id | 6dbab232dd8d2aed0cb1d6f7978fb7b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Liverpool |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.16 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.53 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.75 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.18 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 31.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 42.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.77 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.52 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.46 |
| Home probability edge | -2.0% |
| Draw probability edge | +0.3% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | -0.0400 |
| Raw ev home | -0.1212 |
| Raw edge prob draw | 0.0052 |
| Raw ev draw | 0.0204 |
| Raw edge prob away | 0.0348 |
| Raw ev away | 0.0910 |

</details>


---

## 2026-10-12 — Coventry City vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **59.3%**. Expected goals are 0.36 for Coventry City and 1.82 for Newcastle United (2.18 combined). The most likely exact score is 0-1 at 16.1%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 34.5%; Under 4.5 goals: 93.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 16.7% | 6.00 |
| Draw | 24.1% | 4.16 |
| Newcastle United win | 59.3% | 1.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 0.36 |
| Newcastle United expected goals | 1.82 |
| Expected total goals | 2.18 |
| Over 0.5 | 86.6% |
| Under 0.5 | 13.4% |
| Over 1.5 | 61.0% |
| Under 1.5 | 39.0% |
| Over 2.5 | 34.5% |
| Under 2.5 | 65.5% |
| Over 3.5 | 15.6% |
| Under 3.5 | 84.4% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.12% |
| 2 | 0-2 | 15.24% |
| 3 | 0-0 | 13.41% |
| 4 | 1-0 | 9.42% |
| 5 | 0-3 | 9.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 16.7% | 27.5% | 3.60 | -40.0% |
| Draw | 24.1% | 26.5% | 3.80 | -8.6% |
| Newcastle United win | 59.3% | 46.0% | 2.18 | +29.2% |
| Over 2.5 | 34.5% | 57.9% | 1.72 | -40.6% |
| Under 2.5 | 65.5% | 42.1% | 2.34 | +53.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-12T19:00:00+00:00 |
| Fixture id | acd5bd945dd953ad1e300df5bfe696f9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Coventry |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.46 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.57 |
| Fair Over 2.5 odds | 2.90 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.40 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.16 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.55 |
| Reference draw odds | 3.68 |
| Reference away odds | 2.14 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.34 |
| Home probability edge | -10.8% |
| Draw probability edge | -2.4% |
| Away probability edge | +13.2% |
| Over 2.5 probability edge | -23.4% |
| Under 2.5 probability edge | +23.4% |
| Raw edge prob home | -0.2160 |
| Raw ev home | -0.7883 |
| Raw edge prob draw | -0.0486 |
| Raw ev draw | -0.1782 |
| Raw edge prob away | 0.2646 |
| Raw ev away | 0.5803 |

</details>


---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **40.8%**. Expected goals are 1.48 for Brentford and 1.63 for Liverpool (3.11 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 60.6%; Under 4.5 goals: 79.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 34.3% | 2.92 |
| Draw | 25.0% | 4.01 |
| Liverpool win | 40.8% | 2.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.48 |
| Liverpool expected goals | 1.63 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 60.6% |
| Under 2.5 | 39.4% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.41% |
| 2 | 1-2 | 8.88% |
| 3 | 2-1 | 8.07% |
| 4 | 2-2 | 6.24% |
| 5 | 0-1 | 6.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 34.3% | 34.7% | 2.88 | -1.3% |
| Draw | 25.0% | 23.9% | 3.80 | -5.2% |
| Liverpool win | 40.8% | 41.3% | 2.50 | +1.9% |
| Over 2.5 | 60.6% | 62.5% | 1.55 | -6.1% |
| Under 2.5 | 39.4% | 37.5% | 2.49 | -1.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | 8f1945e7272bc7e89016439f5ab321c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Brentford |
| Matched away-team name | Liverpool |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.69 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.85 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 40.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.50 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Home probability edge | -0.5% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | -0.0091 |
| Raw ev home | -0.0260 |
| Raw edge prob draw | 0.0203 |
| Raw ev draw | -0.0130 |
| Raw edge prob away | -0.0112 |
| Raw ev away | 0.0052 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **39.0%**. Expected goals are 1.28 for Everton and 1.29 for Chelsea (2.57 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 48.4%; Under 4.5 goals: 87.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 34.2% | 2.92 |
| Draw | 26.8% | 3.74 |
| Chelsea win | 39.0% | 2.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.28 |
| Chelsea expected goals | 1.29 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 48.4% |
| Under 2.5 | 51.6% |
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 12.2% |
| Under 4.5 | 87.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.79% |
| 2 | 0-1 | 9.34% |
| 3 | 1-2 | 8.94% |
| 4 | 1-0 | 8.22% |
| 5 | 0-0 | 8.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 34.2% | 33.2% | 2.95 | +1.0% |
| Draw | 26.8% | 24.3% | 3.86 | +3.3% |
| Chelsea win | 39.0% | 42.5% | 2.45 | -4.4% |
| Over 2.5 | 48.4% | 57.7% | 1.70 | -17.7% |
| Under 2.5 | 51.6% | 42.3% | 2.34 | +20.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T11:30:00+00:00 |
| Fixture id | 764e6513cb3f348881503df70ccb90e0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Everton |
| Matched away-team name | Chelsea |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.19 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.88 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.22 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | +1.0% |
| Draw probability edge | +2.4% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | 0.0208 |
| Raw ev home | 0.0405 |
| Raw edge prob draw | 0.0484 |
| Raw ev draw | 0.1269 |
| Raw edge prob away | -0.0693 |
| Raw ev away | -0.1294 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.6%**. Expected goals are 0.85 for Fulham and 1.07 for Hull City (1.92 combined). The most likely exact score is 1-0 at 17.4%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 31.8%; Under 4.5 goals: 95.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.6% | 2.35 |
| Draw | 28.0% | 3.57 |
| Hull City win | 29.4% | 3.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.85 |
| Hull City expected goals | 1.07 |
| Expected total goals | 1.92 |
| Over 0.5 | 86.8% |
| Under 0.5 | 13.2% |
| Over 1.5 | 58.6% |
| Under 1.5 | 41.4% |
| Over 2.5 | 31.8% |
| Under 2.5 | 68.2% |
| Over 3.5 | 12.9% |
| Under 3.5 | 87.1% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.42% |
| 2 | 0-0 | 13.19% |
| 3 | 1-1 | 12.10% |
| 4 | 0-1 | 10.81% |
| 5 | 2-1 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 42.6% | 58.2% | 1.74 | -25.9% |
| Draw | 28.0% | 22.0% | 4.11 | +15.3% |
| Hull City win | 29.4% | 19.8% | 5.18 | +52.2% |
| Over 2.5 | 31.8% | 55.3% | 1.81 | -42.4% |
| Under 2.5 | 68.2% | 44.7% | 2.20 | +50.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | 7895f97f2f9577f3b13287a3d086859d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | LeoVegas (SE) |
| Matched home-team name | Fulham |
| Matched away-team name | Hull |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.58 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.41 |
| Fair Over 2.5 odds | 3.14 |
| Fair Under 2.5 odds | 1.47 |
| Fair Over 3.5 odds | 7.78 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.78 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 34.1% |
| Unadjusted away-win probability | 39.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.64 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -15.7% |
| Draw probability edge | +6.1% |
| Away probability edge | +9.6% |
| Over 2.5 probability edge | -23.5% |
| Under 2.5 probability edge | +23.5% |
| Raw edge prob home | -0.3132 |
| Raw ev home | -0.5318 |
| Raw edge prob draw | 0.1215 |
| Raw ev draw | 0.4023 |
| Raw edge prob away | 0.1918 |
| Raw ev away | 1.0189 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **84.9%**. Expected goals are 3.46 for Manchester City and 0.70 for Ipswich Town (4.15 combined). The most likely exact score is 3-0 at 10.5%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 77.9%; Under 4.5 goals: 60.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 84.9% | 1.18 |
| Draw | 9.7% | 10.34 |
| Ipswich Town win | 5.4% | 18.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.46 |
| Ipswich Town expected goals | 0.70 |
| Expected total goals | 4.15 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 77.9% |
| Under 2.5 | 22.1% |
| Over 3.5 | 58.9% |
| Under 3.5 | 41.1% |
| Over 4.5 | 39.5% |
| Under 4.5 | 60.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.53% |
| 2 | 2-0 | 9.14% |
| 3 | 4-0 | 9.10% |
| 4 | 3-1 | 7.35% |
| 5 | 2-1 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 84.9% | 82.6% | 1.26 | +7.0% |
| Draw | 9.7% | 10.2% | 7.80 | -24.6% |
| Ipswich Town win | 5.4% | 7.2% | 13.50 | -26.9% |
| Over 2.5 | 77.9% | 70.0% | 1.39 | +8.2% |
| Under 2.5 | 22.1% | 30.0% | 3.03 | -32.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | bf2142d1ca76ba2fc9e61afce80f86c0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Nordic Bet |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Man City |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 48.07 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.47 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.52 |
| Fair Over 3.5 odds | 1.70 |
| Fair Under 3.5 odds | 2.43 |
| Fair Over 4.5 odds | 2.53 |
| Fair Under 4.5 odds | 1.65 |
| Unadjusted home-win probability | 87.2% |
| Unadjusted draw probability | 9.1% |
| Unadjusted away-win probability | 3.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.16 |
| Reference draw odds | 5.90 |
| Reference away odds | 7.75 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.03 |
| Home probability edge | +2.3% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +7.9% |
| Under 2.5 probability edge | -7.9% |
| Raw edge prob home | 0.0458 |
| Raw ev home | 0.0987 |
| Raw edge prob draw | -0.0105 |
| Raw ev draw | -0.2866 |
| Raw edge prob away | -0.0353 |
| Raw ev away | -0.5067 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **46.0%**. Expected goals are 1.77 for Newcastle United and 1.44 for Aston Villa (3.21 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 62.4%; Under 4.5 goals: 77.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 46.0% | 2.17 |
| Draw | 24.5% | 4.08 |
| Aston Villa win | 29.5% | 3.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.77 |
| Aston Villa expected goals | 1.44 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.4% |
| Under 2.5 | 37.6% |
| Over 3.5 | 40.0% |
| Under 3.5 | 60.0% |
| Over 4.5 | 22.2% |
| Under 4.5 | 77.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.06% |
| 2 | 2-1 | 9.43% |
| 3 | 1-2 | 7.19% |
| 4 | 2-0 | 6.55% |
| 5 | 2-2 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 46.0% | 47.6% | 2.17 | -0.2% |
| Draw | 24.5% | 23.8% | 3.92 | -3.8% |
| Aston Villa win | 29.5% | 28.6% | 3.35 | -1.3% |
| Over 2.5 | 62.4% | 60.4% | 1.65 | +3.0% |
| Under 2.5 | 37.6% | 39.6% | 2.45 | -8.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | d1bbbdcd3d430e70091b518369b559cf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Newcastle |
| Matched away-team name | Aston Villa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.07 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.30 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.66 |
| Fair Over 3.5 odds | 2.50 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.50 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 44.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 30.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.90 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.95 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.37 |
| Home probability edge | -1.6% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | -0.0316 |
| Raw ev home | -0.0364 |
| Raw edge prob draw | 0.0138 |
| Raw ev draw | -0.0112 |
| Raw edge prob away | 0.0178 |
| Raw ev away | 0.0173 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **48.0%**. Expected goals are 1.53 for Bournemouth and 1.04 for Sunderland (2.57 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 48.1%; Under 4.5 goals: 87.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 48.0% | 2.09 |
| Draw | 26.6% | 3.76 |
| Sunderland win | 25.5% | 3.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.53 |
| Sunderland expected goals | 1.04 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 48.1% |
| Under 2.5 | 51.9% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.69% |
| 2 | 1-0 | 10.55% |
| 3 | 2-1 | 9.45% |
| 4 | 2-0 | 9.06% |
| 5 | 0-0 | 8.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 48.0% | 48.6% | 2.04 | -2.2% |
| Draw | 26.6% | 25.0% | 3.75 | -0.3% |
| Sunderland win | 25.5% | 26.4% | 3.85 | -1.9% |
| Over 2.5 | 48.1% | 52.6% | 1.88 | -9.6% |
| Under 2.5 | 51.9% | 47.4% | 2.07 | +7.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | dfd5d6648be46426e418801584d46a68 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bournemouth |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.90 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.29 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 24.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.86 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.02 |
| Home probability edge | -0.7% |
| Draw probability edge | +1.6% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.0137 |
| Raw ev home | -0.0357 |
| Raw edge prob draw | 0.0318 |
| Raw ev draw | 0.0562 |
| Raw edge prob away | -0.0181 |
| Raw ev away | -0.0543 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **57.6%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.1%; Under 4.5 goals: 82.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 57.6% | 1.74 |
| Draw | 22.5% | 4.44 |
| Crystal Palace win | 19.9% | 5.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 1.85 |
| Crystal Palace expected goals | 1.08 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.0% |
| Under 3.5 | 66.0% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.65% |
| 2 | 2-1 | 10.49% |
| 3 | 2-0 | 9.70% |
| 4 | 1-0 | 9.32% |
| 5 | 3-1 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 57.6% | 61.0% | 1.67 | -3.8% |
| Draw | 22.5% | 20.1% | 4.45 | +0.2% |
| Crystal Palace win | 19.9% | 18.9% | 5.30 | +5.5% |
| Over 2.5 | 57.1% | 60.8% | 1.65 | -5.8% |
| Under 2.5 | 42.9% | 39.2% | 2.45 | +5.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 9fc08b390a49c4434f7cf631a0bb88fb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.14 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.10 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.94 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.64 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 54.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 20.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.52 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Home probability edge | -3.4% |
| Draw probability edge | +2.4% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | -0.0684 |
| Raw ev home | -0.0953 |
| Raw edge prob draw | 0.0488 |
| Raw ev draw | 0.1100 |
| Raw edge prob away | 0.0197 |
| Raw ev away | 0.1069 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **37.3%**. Expected goals are 1.42 for Leeds United and 1.30 for Manchester United (2.72 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 52.0%; Under 4.5 goals: 85.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 37.3% | 2.68 |
| Draw | 25.7% | 3.89 |
| Manchester United win | 37.0% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.30 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 76.9% |
| Under 1.5 | 23.1% |
| Over 2.5 | 52.0% |
| Under 2.5 | 48.0% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.23% |
| 2 | 1-2 | 8.83% |
| 3 | 2-1 | 8.33% |
| 4 | 0-1 | 8.15% |
| 5 | 1-0 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 37.3% | 36.0% | 2.95 | +10.0% |
| Draw | 25.7% | 23.1% | 3.80 | -2.4% |
| Manchester United win | 37.0% | 40.9% | 2.44 | -9.6% |
| Over 2.5 | 52.0% | 60.4% | 1.69 | -12.1% |
| Under 2.5 | 48.0% | 39.6% | 2.37 | +13.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 676b3b0b609e9cf565da450786618d26 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | LeoVegas (SE) |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.96 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.32 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.43 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 6.99 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 38.6% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 33.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.40 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.37 |
| Home probability edge | +1.3% |
| Draw probability edge | +2.5% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | 0.0262 |
| Raw ev home | 0.1383 |
| Raw edge prob draw | 0.0507 |
| Raw ev draw | 0.0721 |
| Raw edge prob away | -0.0769 |
| Raw ev away | -0.1899 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **58.3%**. Expected goals are 0.77 for Nottingham Forest and 1.55 for Arsenal (2.32 combined). The most likely exact score is 0-1 at 14.9%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 42.2%; Under 4.5 goals: 91.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.9% | 5.92 |
| Draw | 24.8% | 4.03 |
| Arsenal win | 58.3% | 1.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.77 |
| Arsenal expected goals | 1.55 |
| Expected total goals | 2.32 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 69.1% |
| Under 1.5 | 30.9% |
| Over 2.5 | 42.2% |
| Under 2.5 | 57.8% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.91% |
| 2 | 0-2 | 12.58% |
| 3 | 1-1 | 11.48% |
| 4 | 0-0 | 9.78% |
| 5 | 1-2 | 9.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.9% | 16.5% | 6.20 | +4.7% |
| Draw | 24.8% | 21.6% | 4.10 | +1.7% |
| Arsenal win | 58.3% | 61.9% | 1.66 | -3.2% |
| Over 2.5 | 42.2% | 49.7% | 1.97 | -16.8% |
| Under 2.5 | 57.8% | 50.3% | 1.97 | +13.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | f696a248965373d9071dc0662e5c58a8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.22 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.24 |
| Fair Over 2.5 odds | 2.37 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.79 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.14 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 54.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.60 |
| Reference draw odds | 3.65 |
| Reference away odds | 1.50 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.91 |
| Home probability edge | +0.4% |
| Draw probability edge | +3.2% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | 0.0086 |
| Raw ev home | 0.0734 |
| Raw edge prob draw | 0.0636 |
| Raw ev draw | 0.1477 |
| Raw edge prob away | -0.0722 |
| Raw ev away | -0.0921 |

</details>


---
