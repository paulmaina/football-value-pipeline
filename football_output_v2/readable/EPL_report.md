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
| Additional event odds calls used before this league | 0.00 |
| Additional event odds calls budget | 24.00 |
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

The model's most likely 1X2 outcome is **Arsenal win** at **66.5%**. Expected goals are 1.76 for Arsenal and 0.68 for Leeds United (2.44 combined). The most likely exact score is 1-0 at 15.2%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 45.4%; Under 4.5 goals: 89.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 66.5% | 1.50 |
| Draw | 21.8% | 4.59 |
| Leeds United win | 11.7% | 8.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.76 |
| Leeds United expected goals | 0.68 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.4% |
| Under 2.5 | 54.6% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.23% |
| 2 | 2-0 | 14.44% |
| 3 | 1-1 | 10.08% |
| 4 | 2-1 | 9.80% |
| 5 | 0-0 | 8.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 66.5% | 70.8% | 1.44 | -4.2% |
| Draw | 21.8% | 18.7% | 5.30 | +15.5% |
| Leeds United win | 11.7% | 10.5% | 9.40 | +9.6% |
| Over 2.5 | 45.4% | 53.0% | 1.89 | -14.1% |
| Under 2.5 | 54.6% | 47.0% | 2.05 | +11.9% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:09:19Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.0% |
| P btts no | 59.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.64 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.51 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 62.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 12.8% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 41.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.41 |
| Reference draw odds | 5.30 |
| Reference away odds | 9.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.00 |
| Home probability edge | -4.2% |
| Draw probability edge | +3.1% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | -0.0848 |
| Raw ev home | -0.1028 |
| Raw edge prob draw | 0.0619 |
| Raw ev draw | 0.3191 |
| Raw edge prob away | 0.0229 |
| Raw ev away | 0.2037 |
| Market p over 1 5 | 75.7% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-09T08:09:33Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 71.2% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.25 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 44.1% |
| Market btts yes odds | 2.23 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-09T08:10:28Z |
| Market reference btts yes odds | 2.22 |
| Market reference btts yes opposite odds | 1.76 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-10 — Aston Villa vs Brentford

The model's most likely 1X2 outcome is **Aston Villa win** at **38.2%**. Expected goals are 1.59 for Aston Villa and 1.41 for Brentford (3.00 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 57.6%; Under 4.5 goals: 81.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 38.2% | 2.62 |
| Draw | 26.9% | 3.72 |
| Brentford win | 34.9% | 2.87 |

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
| Over 2.5 | 57.6% |
| Under 2.5 | 42.4% |
| Over 3.5 | 35.3% |
| Under 3.5 | 64.7% |
| Over 4.5 | 18.5% |
| Under 4.5 | 81.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.49% |
| 2 | 1-2 | 8.36% |
| 3 | 2-1 | 8.34% |
| 4 | 2-2 | 6.36% |
| 5 | 1-0 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 38.2% | 35.8% | 2.78 | +6.3% |
| Draw | 26.9% | 27.3% | 3.75 | +0.8% |
| Brentford win | 34.9% | 36.9% | 2.70 | -5.8% |
| Over 2.5 | 57.6% | 59.7% | 1.75 | +0.8% |
| Under 2.5 | 42.4% | 40.3% | 2.25 | -4.7% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.5% |
| P btts no | 38.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.10 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.34 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.83 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.41 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 40.6% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 32.8% |
| Raw p over 1 5 | 81.3% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 61.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.78 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | +2.4% |
| Draw probability edge | -0.4% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | 0.0481 |
| Raw ev home | 0.1300 |
| Raw edge prob draw | -0.0076 |
| Raw ev draw | -0.0059 |
| Raw edge prob away | -0.0406 |
| Raw ev away | -0.1132 |
| Market p over 1 5 | 81.0% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 66.5% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:09:33Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.80 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.0% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:37Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-10 — Chelsea vs Bournemouth

The model's most likely 1X2 outcome is **Chelsea win** at **51.2%**. Expected goals are 1.75 for Chelsea and 1.40 for Bournemouth (3.15 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 61.6%; Under 4.5 goals: 78.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 51.2% | 1.95 |
| Draw | 23.8% | 4.20 |
| Bournemouth win | 25.0% | 4.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.75 |
| Bournemouth expected goals | 1.40 |
| Expected total goals | 3.15 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 83.5% |
| Under 1.5 | 16.5% |
| Over 2.5 | 61.6% |
| Under 2.5 | 38.4% |
| Over 3.5 | 39.0% |
| Under 3.5 | 61.0% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.85% |
| 2 | 2-1 | 10.48% |
| 3 | 2-0 | 7.50% |
| 4 | 1-0 | 7.31% |
| 5 | 1-2 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 51.2% | 57.4% | 1.74 | -11.0% |
| Draw | 23.8% | 22.2% | 4.50 | +7.2% |
| Bournemouth win | 25.0% | 20.4% | 4.91 | +22.9% |
| Over 2.5 | 61.6% | 65.1% | 1.49 | -8.1% |
| Under 2.5 | 38.4% | 34.9% | 2.66 | +2.0% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:09:33Z |
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
| P btts yes | 62.8% |
| P btts no | 37.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.84 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.07 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.66 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 44.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 29.7% |
| Raw p over 1 5 | 83.3% |
| Raw p under 3 5 | 61.4% |
| Raw p btts yes | 63.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.74 |
| Reference draw odds | 4.50 |
| Reference away odds | 4.90 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.66 |
| Home probability edge | -6.3% |
| Draw probability edge | +1.6% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.1257 |
| Raw ev home | -0.2193 |
| Raw edge prob draw | 0.0326 |
| Raw ev draw | 0.1452 |
| Raw edge prob away | 0.0931 |
| Raw ev away | 0.4573 |
| Market p over 1 5 | 84.9% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 57.4% |
| Market under 3 5 odds | 1.73 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T08:10:04Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.24 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 63.4% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:37Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.45 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-10 — Ipswich Town vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **45.4%**. Expected goals are 1.14 for Ipswich Town and 1.79 for Fulham (2.93 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 55.6%; Under 4.5 goals: 83.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 28.4% | 3.52 |
| Draw | 26.2% | 3.81 |
| Fulham win | 45.4% | 2.20 |

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
| 1 | 1-1 | 12.38% |
| 2 | 1-2 | 8.58% |
| 3 | 2-1 | 7.66% |
| 4 | 0-2 | 7.55% |
| 5 | 0-1 | 7.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 28.4% | 33.9% | 2.96 | -16.0% |
| Draw | 26.2% | 27.0% | 3.65 | -4.3% |
| Fulham win | 45.4% | 39.2% | 2.56 | +16.2% |
| Over 2.5 | 55.6% | 54.4% | 1.82 | +1.2% |
| Under 2.5 | 44.4% | 45.6% | 2.18 | -3.2% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Ipswich |
| Matched away-team name | Fulham |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.2% |
| P btts no | 41.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.99 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.95 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.89 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 51.6% |
| Raw p over 1 5 | 80.1% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 57.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.75 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.06 |
| Home probability edge | -5.5% |
| Draw probability edge | -0.7% |
| Away probability edge | +6.2% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | -0.1093 |
| Raw ev home | -0.3215 |
| Raw edge prob draw | -0.0149 |
| Raw ev draw | -0.0697 |
| Raw edge prob away | 0.1242 |
| Raw ev away | 0.3208 |
| Market p over 1 5 | 79.6% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 67.7% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:38Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.88 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:37Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.20 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-10 — Manchester United vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Manchester United win** at **55.2%**. Expected goals are 1.93 for Manchester United and 1.19 for Tottenham Hotspur (3.12 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.7%; Under 4.5 goals: 79.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 55.2% | 1.81 |
| Draw | 23.4% | 4.27 |
| Tottenham Hotspur win | 21.4% | 4.66 |

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
| 1 | 1-1 | 10.82% |
| 2 | 2-1 | 10.07% |
| 3 | 2-0 | 8.46% |
| 4 | 1-0 | 7.66% |
| 5 | 3-1 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 55.2% | 56.7% | 1.76 | -2.9% |
| Draw | 23.4% | 22.6% | 4.50 | +5.3% |
| Tottenham Hotspur win | 21.4% | 20.7% | 4.80 | +2.9% |
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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:09:19Z |
| Market best draw last update utc | 2026-10-09T08:10:06Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
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
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.93 |
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
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 60.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.76 |
| Reference draw odds | 4.40 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.60 |
| Home probability edge | -1.5% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.0307 |
| Raw ev home | -0.0562 |
| Raw edge prob draw | 0.0160 |
| Raw ev draw | 0.0888 |
| Raw edge prob away | 0.0147 |
| Raw ev away | 0.0646 |
| Market p over 1 5 | 89.1% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.25 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 57.7% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T08:10:41Z |
| Market reference under 3 5 odds | 1.71 |
| Market reference under 3 5 opposite odds | 2.32 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 63.4% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:37Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.45 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-10 — Sunderland vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **41.2%**. Expected goals are 1.20 for Sunderland and 1.44 for Brighton and Hove Albion (2.65 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 49.5%; Under 4.5 goals: 87.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 30.8% | 3.25 |
| Draw | 28.0% | 3.57 |
| Brighton and Hove Albion win | 41.2% | 2.43 |

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
| Over 3.5 | 27.4% |
| Under 3.5 | 72.6% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.37% |
| 2 | 0-1 | 8.91% |
| 3 | 1-2 | 8.85% |
| 4 | 0-0 | 8.23% |
| 5 | 2-1 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 30.8% | 31.5% | 3.18 | -2.1% |
| Draw | 28.0% | 27.5% | 3.60 | +0.7% |
| Brighton and Hove Albion win | 41.2% | 41.0% | 2.42 | -0.3% |
| Over 2.5 | 49.5% | 52.9% | 1.88 | -6.9% |
| Under 2.5 | 50.5% | 47.1% | 2.10 | +6.1% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:06Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Sunderland |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.6% |
| P btts no | 45.4% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.14 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.70 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 41.4% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 72.6% |
| Raw p btts yes | 54.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.15 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.42 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.00 |
| Home probability edge | -0.7% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | -0.0133 |
| Raw ev home | -0.0418 |
| Raw edge prob draw | 0.0097 |
| Raw ev draw | 0.0249 |
| Raw edge prob away | 0.0036 |
| Raw ev away | 0.0018 |
| Market p over 1 5 | 77.7% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 69.2% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 3.00 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:37Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.15 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-11 — Crystal Palace vs Nottingham Forest

The model's most likely 1X2 outcome is **Crystal Palace win** at **35.4%**. Expected goals are 1.25 for Crystal Palace and 1.23 for Nottingham Forest (2.48 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 45.1%; Under 4.5 goals: 89.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 35.4% | 2.83 |
| Draw | 29.6% | 3.37 |
| Nottingham Forest win | 35.0% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.25 |
| Nottingham Forest expected goals | 1.23 |
| Expected total goals | 2.48 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 72.1% |
| Under 1.5 | 27.9% |
| Over 2.5 | 45.1% |
| Under 2.5 | 54.9% |
| Over 3.5 | 23.8% |
| Under 3.5 | 76.2% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.13% |
| 2 | 0-0 | 9.68% |
| 3 | 1-0 | 9.10% |
| 4 | 0-1 | 9.07% |
| 5 | 2-1 | 8.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 35.4% | 35.3% | 2.78 | -1.7% |
| Draw | 29.6% | 29.4% | 3.48 | +3.1% |
| Nottingham Forest win | 35.0% | 35.3% | 2.80 | -2.0% |
| Over 2.5 | 45.1% | 48.8% | 2.01 | -9.4% |
| Under 2.5 | 54.9% | 51.2% | 2.02 | +10.9% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:09:33Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
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
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.33 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.59 |
| Fair Over 2.5 odds | 2.22 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.21 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.44 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 35.4% |
| Unadjusted draw probability | 29.9% |
| Unadjusted away-win probability | 34.7% |
| Raw p over 1 5 | 72.1% |
| Raw p under 3 5 | 76.3% |
| Raw p btts yes | 51.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.62 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.62 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | +0.1% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | 0.0014 |
| Raw ev home | -0.0151 |
| Raw edge prob draw | 0.0043 |
| Raw ev draw | 0.0389 |
| Raw edge prob away | -0.0057 |
| Raw ev away | -0.0278 |
| Market p over 1 5 | 76.2% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 74.8% |
| Market under 3 5 odds | 1.37 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.24 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 56.4% |
| Market btts yes odds | 1.74 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:37Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-11 — Hull City vs Everton

The model's most likely 1X2 outcome is **Hull City win** at **35.0%**. Expected goals are 1.09 for Hull City and 0.66 for Everton (1.74 combined). The most likely exact score is 0-0 at 17.0%. Goal-market probabilities: at least one goal: 83.0%; Over 2.5 goals: 26.0%; Under 4.5 goals: 96.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 35.0% | 2.86 |
| Draw | 31.6% | 3.16 |
| Everton win | 33.4% | 2.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.09 |
| Everton expected goals | 0.66 |
| Expected total goals | 1.74 |
| Over 0.5 | 83.0% |
| Under 0.5 | 17.0% |
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
| 1 | 0-0 | 16.98% |
| 2 | 0-1 | 16.39% |
| 3 | 1-0 | 13.97% |
| 4 | 1-1 | 12.48% |
| 5 | 2-0 | 8.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 35.0% | 25.7% | 3.85 | +34.6% |
| Draw | 31.6% | 28.3% | 3.62 | +14.6% |
| Everton win | 33.4% | 46.0% | 2.16 | -27.9% |
| Over 2.5 | 26.0% | 46.6% | 2.08 | -46.0% |
| Under 2.5 | 74.0% | 53.4% | 1.90 | +40.7% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:09:19Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
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
| P btts yes | 32.9% |
| P btts no | 67.1% |
| Fair Over 0.5 odds | 1.20 |
| Fair Under 0.5 odds | 5.89 |
| Fair Over 1.5 odds | 1.90 |
| Fair Under 1.5 odds | 2.11 |
| Fair Over 2.5 odds | 3.85 |
| Fair Under 2.5 odds | 1.35 |
| Fair Over 3.5 odds | 10.32 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.73 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 44.2% |
| Unadjusted draw probability | 35.0% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 53.4% |
| Raw p under 3 5 | 90.0% |
| Raw p btts yes | 33.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.85 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.16 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.68 |
| Home probability edge | +9.3% |
| Draw probability edge | +3.4% |
| Away probability edge | -12.6% |
| Over 2.5 probability edge | -20.7% |
| Under 2.5 probability edge | +20.7% |
| Raw edge prob home | 0.1852 |
| Raw ev home | 0.7025 |
| Raw edge prob draw | 0.0671 |
| Raw ev draw | 0.2671 |
| Raw edge prob away | -0.2524 |
| Raw ev away | -0.5513 |
| Market p over 1 5 | 74.2% |
| Market over 1 5 odds | 1.35 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.30 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 74.2% |
| Market under 3 5 odds | 1.32 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference under 3 5 odds | 1.32 |
| Market reference under 3 5 opposite odds | 3.53 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 53.1% |
| Market btts yes odds | 1.86 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:37Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 1.95 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-11 — Liverpool vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **40.6%**. Expected goals are 1.40 for Liverpool and 1.65 for Manchester City (3.05 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 58.8%; Under 4.5 goals: 80.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 33.4% | 3.00 |
| Draw | 26.0% | 3.85 |
| Manchester City win | 40.6% | 2.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.40 |
| Manchester City expected goals | 1.65 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
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
| 1 | 1-1 | 12.01% |
| 2 | 1-2 | 8.65% |
| 3 | 2-1 | 8.12% |
| 4 | 0-1 | 6.40% |
| 5 | 2-2 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 33.4% | 35.3% | 2.80 | -6.6% |
| Draw | 26.0% | 25.8% | 3.90 | +1.4% |
| Manchester City win | 40.6% | 38.8% | 2.58 | +4.9% |
| Over 2.5 | 58.8% | 60.7% | 1.60 | -5.9% |
| Under 2.5 | 41.2% | 39.3% | 2.46 | +1.3% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Liverpool |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 62.0% |
| P btts no | 38.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.09 |
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
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 62.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.62 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.33 |
| Home probability edge | -2.0% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | -0.0394 |
| Raw ev home | -0.1212 |
| Raw edge prob draw | 0.0033 |
| Raw ev draw | 0.0204 |
| Raw edge prob away | 0.0361 |
| Raw ev away | 0.0952 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 60.9% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T08:08:51Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.43 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 65.5% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:37Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-12 — Coventry City vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **59.2%**. Expected goals are 0.36 for Coventry City and 1.82 for Newcastle United (2.18 combined). The most likely exact score is 0-1 at 16.1%. Goal-market probabilities: at least one goal: 86.5%; Over 2.5 goals: 34.5%; Under 4.5 goals: 93.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 16.6% | 6.01 |
| Draw | 24.1% | 4.14 |
| Newcastle United win | 59.2% | 1.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 0.36 |
| Newcastle United expected goals | 1.82 |
| Expected total goals | 2.18 |
| Over 0.5 | 86.5% |
| Under 0.5 | 13.5% |
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
| 1 | 0-1 | 16.11% |
| 2 | 0-2 | 15.23% |
| 3 | 0-0 | 13.46% |
| 4 | 1-0 | 9.40% |
| 5 | 0-3 | 9.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 16.6% | 27.4% | 3.60 | -40.1% |
| Draw | 24.1% | 26.7% | 3.80 | -8.2% |
| Newcastle United win | 59.2% | 45.9% | 2.18 | +29.1% |
| Over 2.5 | 34.5% | 55.8% | 1.72 | -40.7% |
| Under 2.5 | 65.5% | 44.2% | 2.34 | +53.3% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:10:06Z |
| Market best away last update utc | 2026-10-09T08:09:19Z |
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
| P btts yes | 27.8% |
| P btts no | 72.2% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.43 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.57 |
| Fair Over 2.5 odds | 2.90 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.41 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 16.18 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 72.5% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 26.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.60 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.16 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -10.8% |
| Draw probability edge | -2.5% |
| Away probability edge | +13.3% |
| Over 2.5 probability edge | -21.3% |
| Under 2.5 probability edge | +21.3% |
| Raw edge prob home | -0.2153 |
| Raw ev home | -0.7883 |
| Raw edge prob draw | -0.0503 |
| Raw ev draw | -0.1782 |
| Raw edge prob away | 0.2657 |
| Raw ev away | 0.5803 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 64.5% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.64 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 59.3% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T08:10:37Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.25 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **40.0%**. Expected goals are 1.48 for Brentford and 1.63 for Liverpool (3.11 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 60.2%; Under 4.5 goals: 79.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 34.1% | 2.94 |
| Draw | 25.9% | 3.86 |
| Liverpool win | 40.0% | 2.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.48 |
| Liverpool expected goals | 1.63 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 60.2% |
| Under 2.5 | 39.8% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.4% |
| Under 4.5 | 79.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.86% |
| 2 | 1-2 | 8.72% |
| 3 | 2-1 | 8.02% |
| 4 | 2-2 | 6.49% |
| 5 | 0-1 | 6.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 34.1% | 34.3% | 2.88 | -1.9% |
| Draw | 25.9% | 25.9% | 3.80 | -1.4% |
| Liverpool win | 40.0% | 39.8% | 2.50 | +0.0% |
| Over 2.5 | 60.2% | 62.5% | 1.55 | -6.7% |
| Under 2.5 | 39.8% | 37.5% | 2.49 | -0.9% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:09:19Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:09:19Z |
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
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.98 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.83 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.51 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.90 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 40.2% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.82 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.44 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Home probability edge | -0.2% |
| Draw probability edge | +0.0% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | -0.0047 |
| Raw ev home | -0.0260 |
| Raw edge prob draw | 0.0007 |
| Raw ev draw | -0.0130 |
| Raw edge prob away | 0.0039 |
| Raw ev away | 0.0052 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 59.9% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T08:10:06Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.34 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 63.8% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **38.2%**. Expected goals are 1.28 for Everton and 1.29 for Chelsea (2.57 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 48.2%; Under 4.5 goals: 87.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 34.5% | 2.90 |
| Draw | 27.4% | 3.66 |
| Chelsea win | 38.2% | 2.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.28 |
| Chelsea expected goals | 1.29 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 48.2% |
| Under 2.5 | 51.8% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.07% |
| 2 | 0-1 | 9.15% |
| 3 | 1-2 | 8.75% |
| 4 | 0-0 | 8.38% |
| 5 | 1-0 | 8.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 34.5% | 33.6% | 2.95 | +1.7% |
| Draw | 27.4% | 25.5% | 3.86 | +5.6% |
| Chelsea win | 38.2% | 40.8% | 2.45 | -6.4% |
| Over 2.5 | 48.2% | 59.2% | 1.70 | -18.1% |
| Under 2.5 | 51.8% | 40.8% | 2.34 | +21.3% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:09:19Z |
| Market best away last update utc | 2026-10-09T08:09:19Z |
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
| P btts yes | 53.3% |
| P btts no | 46.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.93 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.88 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.26 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 53.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.90 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +0.8% |
| Draw probability edge | +1.8% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0162 |
| Raw ev home | 0.0405 |
| Raw edge prob draw | 0.0367 |
| Raw ev draw | 0.1269 |
| Raw edge prob away | -0.0530 |
| Raw ev away | -0.1294 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 65.3% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.65 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 61.8% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.40 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **41.9%**. Expected goals are 0.85 for Fulham and 1.07 for Hull City (1.92 combined). The most likely exact score is 1-0 at 17.1%. Goal-market probabilities: at least one goal: 86.4%; Over 2.5 goals: 31.5%; Under 4.5 goals: 95.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 41.9% | 2.39 |
| Draw | 28.9% | 3.46 |
| Hull City win | 29.2% | 3.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.85 |
| Hull City expected goals | 1.07 |
| Expected total goals | 1.92 |
| Over 0.5 | 86.4% |
| Under 0.5 | 13.6% |
| Over 1.5 | 58.5% |
| Under 1.5 | 41.5% |
| Over 2.5 | 31.5% |
| Under 2.5 | 68.5% |
| Over 3.5 | 12.8% |
| Under 3.5 | 87.2% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.14% |
| 2 | 0-0 | 13.61% |
| 3 | 1-1 | 12.48% |
| 4 | 0-1 | 10.74% |
| 5 | 2-1 | 8.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 41.9% | 56.9% | 1.74 | -27.1% |
| Draw | 28.9% | 23.7% | 4.11 | +18.9% |
| Hull City win | 29.2% | 19.4% | 5.18 | +51.2% |
| Over 2.5 | 31.5% | 57.6% | 1.81 | -42.9% |
| Under 2.5 | 68.5% | 42.4% | 2.20 | +50.6% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:09:19Z |
| Market best away last update utc | 2026-10-09T08:09:19Z |
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
| P btts yes | 38.1% |
| P btts no | 61.9% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.35 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.41 |
| Fair Over 2.5 odds | 3.17 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.80 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.98 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 34.1% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 87.1% |
| Raw p btts yes | 39.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.74 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | -15.0% |
| Draw probability edge | +5.2% |
| Away probability edge | +9.8% |
| Over 2.5 probability edge | -26.1% |
| Under 2.5 probability edge | +26.1% |
| Raw edge prob home | -0.2996 |
| Raw ev home | -0.5318 |
| Raw edge prob draw | 0.1038 |
| Raw ev draw | 0.4023 |
| Raw edge prob away | 0.1958 |
| Raw ev away | 1.0189 |
| Market p over 1 5 | 81.0% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 68.2% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:38Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.86 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 55.8% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-09T08:09:19Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **84.2%**. Expected goals are 3.46 for Manchester City and 0.70 for Ipswich Town (4.15 combined). The most likely exact score is 3-0 at 10.4%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 77.4%; Under 4.5 goals: 60.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 84.2% | 1.19 |
| Draw | 10.6% | 9.42 |
| Ipswich Town win | 5.1% | 19.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.46 |
| Ipswich Town expected goals | 0.70 |
| Expected total goals | 4.15 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 91.9% |
| Under 1.5 | 8.1% |
| Over 2.5 | 77.4% |
| Under 2.5 | 22.6% |
| Over 3.5 | 58.7% |
| Under 3.5 | 41.3% |
| Over 4.5 | 39.2% |
| Under 4.5 | 60.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.45% |
| 2 | 2-0 | 9.07% |
| 3 | 4-0 | 9.03% |
| 4 | 3-1 | 7.29% |
| 5 | 2-1 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 84.2% | 81.3% | 1.26 | +6.1% |
| Draw | 10.6% | 12.1% | 7.80 | -17.2% |
| Ipswich Town win | 5.1% | 6.6% | 13.50 | -30.5% |
| Over 2.5 | 77.4% | 70.0% | 1.39 | +7.6% |
| Under 2.5 | 22.6% | 30.0% | 3.03 | -31.6% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:09:19Z |
| Market best draw last update utc | 2026-10-09T08:08:31Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
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
| P btts yes | 49.8% |
| P btts no | 50.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.81 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.30 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.43 |
| Fair Over 3.5 odds | 1.70 |
| Fair Under 3.5 odds | 2.42 |
| Fair Over 4.5 odds | 2.55 |
| Fair Under 4.5 odds | 1.65 |
| Unadjusted home-win probability | 87.2% |
| Unadjusted draw probability | 9.1% |
| Unadjusted away-win probability | 3.7% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.4% |
| Raw p btts yes | 49.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.22 |
| Reference draw odds | 7.60 |
| Reference away odds | 13.50 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.03 |
| Home probability edge | +3.0% |
| Draw probability edge | -1.5% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | +7.5% |
| Under 2.5 probability edge | -7.5% |
| Raw edge prob home | 0.0592 |
| Raw ev home | 0.0987 |
| Raw edge prob draw | -0.0293 |
| Raw ev draw | -0.2866 |
| Raw edge prob away | -0.0298 |
| Raw ev away | -0.5067 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 50.8% |
| Market under 3 5 odds | 1.95 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T08:10:04Z |
| Market reference under 3 5 odds | 1.88 |
| Market reference under 3 5 opposite odds | 1.94 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 53.7% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-09T08:09:19Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **45.3%**. Expected goals are 1.77 for Newcastle United and 1.44 for Aston Villa (3.21 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 62.3%; Under 4.5 goals: 77.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 45.3% | 2.21 |
| Draw | 24.9% | 4.02 |
| Aston Villa win | 29.8% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.77 |
| Aston Villa expected goals | 1.44 |
| Expected total goals | 3.21 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.3% |
| Under 2.5 | 37.7% |
| Over 3.5 | 40.0% |
| Under 3.5 | 60.0% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.22% |
| 2 | 2-1 | 9.29% |
| 3 | 1-2 | 7.27% |
| 4 | 2-2 | 6.46% |
| 5 | 2-0 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 45.3% | 46.2% | 2.17 | -1.7% |
| Draw | 24.9% | 24.5% | 3.92 | -2.4% |
| Aston Villa win | 29.8% | 29.3% | 3.35 | -0.1% |
| Over 2.5 | 62.3% | 60.7% | 1.65 | +2.8% |
| Under 2.5 | 37.7% | 39.3% | 2.45 | -7.6% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:09:19Z |
| Market best draw last update utc | 2026-10-09T08:09:19Z |
| Market best away last update utc | 2026-10-09T08:09:19Z |
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
| P btts yes | 64.3% |
| P btts no | 35.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.78 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.29 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.65 |
| Fair Over 3.5 odds | 2.50 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.51 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 44.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 64.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.10 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | -0.9% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | -0.0176 |
| Raw ev home | -0.0364 |
| Raw edge prob draw | 0.0068 |
| Raw ev draw | -0.0112 |
| Raw edge prob away | 0.0108 |
| Raw ev away | 0.0173 |
| Market p over 1 5 | 84.3% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.55 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 62.4% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.35 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 61.8% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.40 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.6%**. Expected goals are 1.53 for Bournemouth and 1.04 for Sunderland (2.57 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 47.9%; Under 4.5 goals: 88.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.6% | 2.10 |
| Draw | 27.1% | 3.69 |
| Sunderland win | 25.3% | 3.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.53 |
| Sunderland expected goals | 1.04 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.93% |
| 2 | 1-0 | 10.48% |
| 3 | 2-1 | 9.39% |
| 4 | 2-0 | 9.00% |
| 5 | 0-0 | 8.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.6% | 48.0% | 2.04 | -2.8% |
| Draw | 27.1% | 26.0% | 3.75 | +1.6% |
| Sunderland win | 25.3% | 26.0% | 3.85 | -2.7% |
| Over 2.5 | 47.9% | 52.4% | 1.88 | -10.0% |
| Under 2.5 | 52.1% | 47.6% | 2.07 | +7.9% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:09:19Z |
| Market best draw last update utc | 2026-10-09T08:09:19Z |
| Market best away last update utc | 2026-10-09T08:09:19Z |
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
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.68 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.33 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 74.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 52.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.04 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | -0.4% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | -0.0073 |
| Raw ev home | -0.0357 |
| Raw edge prob draw | 0.0216 |
| Raw ev draw | 0.0562 |
| Raw edge prob away | -0.0144 |
| Raw ev away | -0.0543 |
| Market p over 1 5 | 77.8% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 69.7% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 2.98 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.15 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **56.7%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 56.7%; Under 4.5 goals: 82.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 56.7% | 1.76 |
| Draw | 23.6% | 4.25 |
| Crystal Palace win | 19.7% | 5.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 1.85 |
| Crystal Palace expected goals | 1.08 |
| Expected total goals | 2.93 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 80.3% |
| Under 1.5 | 19.7% |
| Over 2.5 | 56.7% |
| Under 2.5 | 43.3% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.6% |
| Under 4.5 | 82.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.14% |
| 2 | 2-1 | 10.33% |
| 3 | 2-0 | 9.55% |
| 4 | 1-0 | 9.17% |
| 5 | 3-1 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 56.7% | 59.2% | 1.67 | -5.3% |
| Draw | 23.6% | 22.2% | 4.45 | +4.8% |
| Crystal Palace win | 19.7% | 18.6% | 5.30 | +4.6% |
| Over 2.5 | 56.7% | 62.2% | 1.65 | -6.5% |
| Under 2.5 | 43.3% | 37.8% | 2.45 | +6.2% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:09:19Z |
| Market best draw last update utc | 2026-10-09T08:09:19Z |
| Market best away last update utc | 2026-10-09T08:10:06Z |
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
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.37 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.08 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.69 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 80.1% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.66 |
| Reference draw odds | 4.30 |
| Reference away odds | 5.10 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -2.5% |
| Draw probability edge | +1.4% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | -0.0508 |
| Raw ev home | -0.0953 |
| Raw edge prob draw | 0.0278 |
| Raw ev draw | 0.1100 |
| Raw edge prob away | 0.0230 |
| Raw ev away | 0.1069 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 62.8% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.20 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Manchester United win** at **37.1%**. Expected goals are 1.42 for Leeds United and 1.30 for Manchester United (2.72 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 51.5%; Under 4.5 goals: 85.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 36.0% | 2.77 |
| Draw | 26.9% | 3.72 |
| Manchester United win | 37.1% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.30 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 29.0% |
| Under 3.5 | 71.0% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.82% |
| 2 | 1-2 | 8.83% |
| 3 | 0-1 | 8.16% |
| 4 | 2-1 | 8.06% |
| 5 | 1-0 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 36.0% | 33.5% | 2.95 | +6.3% |
| Draw | 26.9% | 25.6% | 3.80 | +2.2% |
| Manchester United win | 37.1% | 40.9% | 2.44 | -9.6% |
| Over 2.5 | 51.5% | 57.2% | 1.69 | -12.9% |
| Under 2.5 | 48.5% | 42.8% | 2.37 | +14.8% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:22Z |
| Market best draw last update utc | 2026-10-09T08:10:24Z |
| Market best away last update utc | 2026-10-09T08:09:19Z |
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
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.32 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.07 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.6% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 56.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.92 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | +2.5% |
| Draw probability edge | +1.3% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | 0.0509 |
| Raw ev home | 0.1383 |
| Raw edge prob draw | 0.0262 |
| Raw ev draw | 0.0721 |
| Raw edge prob away | -0.0771 |
| Raw ev away | -0.1899 |
| Market p over 1 5 | 81.2% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.49 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 61.6% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.38 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **46.0%**. Expected goals are 0.77 for Nottingham Forest and 1.55 for Arsenal (2.32 combined). The most likely exact score is 1-0 at 13.7%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 44.1%; Under 4.5 goals: 90.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 37.4% | 2.67 |
| Draw | 16.6% | 6.04 |
| Arsenal win | 46.0% | 2.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.77 |
| Arsenal expected goals | 1.55 |
| Expected total goals | 2.32 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 68.0% |
| Under 1.5 | 32.0% |
| Over 2.5 | 44.1% |
| Under 2.5 | 55.9% |
| Over 3.5 | 20.0% |
| Under 3.5 | 80.0% |
| Over 4.5 | 9.1% |
| Under 4.5 | 90.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.67% |
| 2 | 0-1 | 11.78% |
| 3 | 0-2 | 9.94% |
| 4 | 2-1 | 9.75% |
| 5 | 1-1 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 37.4% | 57.5% | 6.20 | +131.8% |
| Draw | 16.6% | 5.1% | 4.10 | -32.1% |
| Arsenal win | 46.0% | 37.4% | 1.66 | -23.6% |
| Over 2.5 | 44.1% | 52.6% | 1.97 | -13.1% |
| Under 2.5 | 55.9% | 47.4% | 1.97 | +10.1% |

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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:08:31Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:09:19Z |
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
| P btts yes | 41.9% |
| P btts no | 58.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.31 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.13 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 5.01 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 10.96 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 43.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.28 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.55 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | -20.1% |
| Draw probability edge | +11.4% |
| Away probability edge | +8.7% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | -0.4015 |
| Raw ev home | 0.0734 |
| Raw edge prob draw | 0.2285 |
| Raw ev draw | 0.1477 |
| Raw edge prob away | 0.1730 |
| Raw ev away | -0.0921 |
| Market p over 1 5 | 75.3% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 71.8% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T08:10:39Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.16 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 49.1% |
| Market btts yes odds | 1.91 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T08:10:39Z |
| Market reference btts yes odds | 1.91 |
| Market reference btts yes opposite odds | 1.85 |
| Market btts yes bookmakers | 2 |

</details>


---
