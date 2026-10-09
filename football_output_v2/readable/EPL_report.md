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
| Additional event odds league quota | 5.00 |
| Additional event odds calls this league | 5.00 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

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
| Draw | 21.7% | 4.60 |
| Leeds United win | 11.7% | 8.53 |

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
| 3 | 1-1 | 10.05% |
| 4 | 2-1 | 9.80% |
| 5 | 0-0 | 8.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 66.5% | 70.8% | 1.44 | -4.2% |
| Draw | 21.7% | 18.6% | 5.30 | +15.2% |
| Leeds United win | 11.7% | 10.6% | 9.20 | +7.9% |
| Over 2.5 | 45.4% | 51.4% | 1.89 | -14.1% |
| Under 2.5 | 54.6% | 48.6% | 2.05 | +11.8% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
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
| Fair Under 0.5 odds | 11.67 |
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
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.40 |
| Reference draw odds | 5.15 |
| Reference away odds | 8.85 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.98 |
| Home probability edge | -4.2% |
| Draw probability edge | +3.2% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0847 |
| Raw ev home | -0.1028 |
| Raw edge prob draw | 0.0632 |
| Raw ev draw | 0.3191 |
| Raw edge prob away | 0.0216 |
| Raw ev away | 0.1781 |

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
| Aston Villa win | 38.3% | 35.9% | 2.76 | +5.7% |
| Draw | 26.8% | 27.0% | 3.75 | +0.4% |
| Brentford win | 34.9% | 37.0% | 2.68 | -6.4% |
| Over 2.5 | 57.7% | 58.7% | 1.75 | +0.9% |
| Under 2.5 | 42.3% | 41.3% | 2.25 | -4.8% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:18Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 12.00 |
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
| Raw p over 1 5 | 81.3% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 61.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.73 |
| Reference draw odds | 3.61 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | +2.4% |
| Draw probability edge | -0.3% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | 0.0471 |
| Raw ev home | 0.1219 |
| Raw edge prob draw | -0.0052 |
| Raw ev draw | -0.0059 |
| Raw edge prob away | -0.0420 |
| Raw ev away | -0.1198 |

</details>


---

## 2026-10-10 — Chelsea vs Bournemouth

The model's most likely 1X2 outcome is **Chelsea win** at **51.0%**. Expected goals are 1.75 for Chelsea and 1.40 for Bournemouth (3.15 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 61.6%; Under 4.5 goals: 78.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 51.0% | 1.96 |
| Draw | 23.9% | 4.18 |
| Bournemouth win | 25.1% | 3.99 |

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
| 1 | 1-1 | 10.90% |
| 2 | 2-1 | 10.45% |
| 3 | 2-0 | 7.48% |
| 4 | 1-0 | 7.28% |
| 5 | 1-2 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 51.0% | 57.1% | 1.75 | -10.8% |
| Draw | 23.9% | 22.4% | 4.40 | +5.3% |
| Bournemouth win | 25.1% | 20.5% | 4.83 | +21.1% |
| Over 2.5 | 61.6% | 65.5% | 1.51 | -7.0% |
| Under 2.5 | 38.4% | 34.5% | 2.60 | -0.2% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Chelsea |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.75 |
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
| Raw p over 1 5 | 83.3% |
| Raw p under 3 5 | 61.4% |
| Raw p btts yes | 63.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.73 |
| Reference draw odds | 4.32 |
| Reference away odds | 4.72 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -6.1% |
| Draw probability edge | +1.5% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.1224 |
| Raw ev home | -0.2148 |
| Raw edge prob draw | 0.0304 |
| Raw ev draw | 0.1198 |
| Raw edge prob away | 0.0921 |
| Raw ev away | 0.4336 |

</details>


---

## 2026-10-10 — Ipswich Town vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **45.2%**. Expected goals are 1.14 for Ipswich Town and 1.79 for Fulham (2.93 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 55.6%; Under 4.5 goals: 83.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 28.5% | 3.51 |
| Draw | 26.3% | 3.80 |
| Fulham win | 45.2% | 2.21 |

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
| 1 | 1-1 | 12.40% |
| 2 | 1-2 | 8.55% |
| 3 | 2-1 | 7.70% |
| 4 | 0-2 | 7.52% |
| 5 | 0-1 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 28.5% | 34.1% | 2.90 | -17.3% |
| Draw | 26.3% | 27.1% | 3.65 | -4.1% |
| Fulham win | 45.2% | 38.8% | 2.62 | +18.4% |
| Over 2.5 | 55.6% | 54.3% | 1.83 | +1.7% |
| Under 2.5 | 44.4% | 45.7% | 2.18 | -3.1% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Ipswich |
| Matched away-team name | Fulham |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.2% |
| P btts no | 41.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.96 |
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
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.87 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.53 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.11 |
| Home probability edge | -5.6% |
| Draw probability edge | -0.8% |
| Away probability edge | +6.4% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | -0.1120 |
| Raw ev home | -0.3353 |
| Raw edge prob draw | -0.0159 |
| Raw ev draw | -0.0697 |
| Raw edge prob away | 0.1279 |
| Raw ev away | 0.3517 |

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
| Manchester United win | 55.1% | 56.5% | 1.78 | -2.0% |
| Draw | 23.4% | 22.6% | 4.40 | +2.9% |
| Tottenham Hotspur win | 21.6% | 21.0% | 4.80 | +3.5% |
| Over 2.5 | 60.7% | 63.8% | 1.51 | -8.3% |
| Under 2.5 | 39.3% | 36.2% | 2.60 | +2.1% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Man United |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
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
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 60.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.75 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.62 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -1.4% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | -0.0285 |
| Raw ev home | -0.0455 |
| Raw edge prob draw | 0.0164 |
| Raw ev draw | 0.0646 |
| Raw edge prob away | 0.0121 |
| Raw ev away | 0.0646 |

</details>


---

## 2026-10-10 — Sunderland vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **41.5%**. Expected goals are 1.20 for Sunderland and 1.44 for Brighton and Hove Albion (2.65 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 49.5%; Under 4.5 goals: 87.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 30.5% | 3.27 |
| Draw | 27.9% | 3.58 |
| Brighton and Hove Albion win | 41.5% | 2.41 |

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
| 2 | 0-1 | 8.98% |
| 3 | 1-2 | 8.92% |
| 4 | 0-0 | 8.21% |
| 5 | 2-1 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 30.5% | 31.0% | 3.20 | -2.2% |
| Draw | 27.9% | 27.3% | 3.70 | +3.3% |
| Brighton and Hove Albion win | 41.5% | 41.7% | 2.42 | +0.5% |
| Over 2.5 | 49.5% | 53.4% | 1.88 | -6.9% |
| Under 2.5 | 50.5% | 46.6% | 2.10 | +6.0% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
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
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 72.6% |
| Raw p btts yes | 54.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.16 |
| Reference draw odds | 3.57 |
| Reference away odds | 2.36 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.07 |
| Home probability edge | -0.4% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | -0.0083 |
| Raw ev home | -0.0357 |
| Raw edge prob draw | 0.0112 |
| Raw ev draw | 0.0534 |
| Raw edge prob away | -0.0029 |
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
| Crystal Palace win | 35.5% | 35.5% | 2.82 | +0.1% |
| Draw | 29.3% | 28.7% | 3.50 | +2.4% |
| Nottingham Forest win | 35.3% | 35.8% | 2.78 | -2.0% |
| Over 2.5 | 45.2% | 50.3% | 1.97 | -10.9% |
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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:18Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
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
| Raw p over 1 5 | 72.1% |
| Raw p under 3 5 | 76.3% |
| Raw p btts yes | 51.8% |
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
| Raw ev home | -0.0010 |
| Raw edge prob draw | 0.0120 |
| Raw ev draw | 0.0448 |
| Raw edge prob away | -0.0109 |
| Raw ev away | -0.0348 |

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
| Everton win | 33.8% | 46.9% | 2.14 | -27.6% |
| Over 2.5 | 26.0% | 47.4% | 2.07 | -46.2% |
| Under 2.5 | 74.0% | 52.6% | 1.91 | +41.3% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Hull |
| Matched away-team name | Everton |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.8% |
| P btts no | 67.2% |
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
| Raw p over 1 5 | 53.4% |
| Raw p under 3 5 | 90.0% |
| Raw p btts yes | 33.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.85 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.84 |
| Home probability edge | +9.5% |
| Draw probability edge | +3.6% |
| Away probability edge | -13.1% |
| Over 2.5 probability edge | -21.4% |
| Under 2.5 probability edge | +21.4% |
| Raw edge prob home | 0.1896 |
| Raw ev home | 0.7246 |
| Raw edge prob draw | 0.0716 |
| Raw ev draw | 0.2671 |
| Raw edge prob away | -0.2612 |
| Raw ev away | -0.5554 |
| Market p over 1 5 | 73.2% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T13:48:54Z |
| Market reference over 1 5 odds | 1.34 |
| Market reference over 1 5 opposite odds | 3.45 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 74.4% |
| Market under 3 5 odds | 1.32 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T13:48:34Z |
| Market reference under 3 5 odds | 1.32 |
| Market reference under 3 5 opposite odds | 3.60 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 53.7% |
| Market btts yes odds | 1.86 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T13:48:37Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.07 |
| Market btts yes bookmakers | 5 |

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
| Liverpool win | 33.4% | 35.4% | 2.96 | -1.2% |
| Draw | 25.9% | 25.6% | 3.90 | +1.0% |
| Manchester City win | 40.7% | 39.0% | 2.52 | +2.6% |
| Over 2.5 | 58.8% | 61.4% | 1.65 | -2.9% |
| Under 2.5 | 41.2% | 38.6% | 2.56 | +5.4% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:54Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Liverpool |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 62.0% |
| P btts no | 38.0% |
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
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 62.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.77 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.52 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -2.0% |
| Draw probability edge | +0.3% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0400 |
| Raw ev home | -0.0710 |
| Raw edge prob draw | 0.0052 |
| Raw ev draw | 0.0204 |
| Raw edge prob away | 0.0348 |
| Raw ev away | 0.0698 |

</details>


---

## 2026-10-12 — Coventry City vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **59.5%**. Expected goals are 0.36 for Coventry City and 1.82 for Newcastle United (2.18 combined). The most likely exact score is 0-1 at 16.2%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 34.6%; Under 4.5 goals: 93.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 16.5% | 6.07 |
| Draw | 24.0% | 4.16 |
| Newcastle United win | 59.5% | 1.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 0.36 |
| Newcastle United expected goals | 1.82 |
| Expected total goals | 2.18 |
| Over 0.5 | 86.6% |
| Under 0.5 | 13.4% |
| Over 1.5 | 61.1% |
| Under 1.5 | 38.9% |
| Over 2.5 | 34.6% |
| Under 2.5 | 65.4% |
| Over 3.5 | 15.7% |
| Under 3.5 | 84.3% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.18% |
| 2 | 0-2 | 15.30% |
| 3 | 0-0 | 13.40% |
| 4 | 1-0 | 9.31% |
| 5 | 0-3 | 9.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 16.5% | 27.1% | 3.60 | -40.7% |
| Draw | 24.0% | 26.5% | 3.80 | -8.6% |
| Newcastle United win | 59.5% | 46.5% | 2.20 | +30.8% |
| Over 2.5 | 34.6% | 55.8% | 1.72 | -40.6% |
| Under 2.5 | 65.4% | 44.2% | 2.30 | +50.5% |

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
| Market best home last update utc | 2026-10-09T13:48:54Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 27.8% |
| P btts no | 72.2% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.46 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.57 |
| Fair Over 2.5 odds | 2.89 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.39 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.13 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 72.5% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 26.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.60 |
| Reference draw odds | 3.68 |
| Reference away odds | 2.12 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -10.6% |
| Draw probability edge | -2.4% |
| Away probability edge | +13.0% |
| Over 2.5 probability edge | -21.3% |
| Under 2.5 probability edge | +21.3% |
| Raw edge prob home | -0.2119 |
| Raw ev home | -0.7883 |
| Raw edge prob draw | -0.0484 |
| Raw ev draw | -0.1782 |
| Raw edge prob away | 0.2603 |
| Raw ev away | 0.5948 |
| Market p over 1 5 | 80.8% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T13:48:54Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.65 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T13:48:54Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.67 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.5% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T13:48:37Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.45 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **40.8%**. Expected goals are 1.48 for Brentford and 1.63 for Liverpool (3.11 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 60.5%; Under 4.5 goals: 79.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 34.2% | 2.92 |
| Draw | 25.0% | 4.00 |
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
| Over 2.5 | 60.5% |
| Under 2.5 | 39.5% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.43% |
| 2 | 1-2 | 8.89% |
| 3 | 2-1 | 8.06% |
| 4 | 2-2 | 6.26% |
| 5 | 0-1 | 6.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 34.2% | 34.6% | 2.88 | -1.5% |
| Draw | 25.0% | 24.1% | 3.80 | -4.9% |
| Liverpool win | 40.8% | 41.3% | 2.50 | +1.9% |
| Over 2.5 | 60.5% | 61.0% | 1.55 | -6.2% |
| Under 2.5 | 39.5% | 39.0% | 2.49 | -1.7% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:18Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
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
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.64 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.85 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.53 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 40.2% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.25 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -0.4% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.0078 |
| Raw ev home | -0.0260 |
| Raw edge prob draw | 0.0192 |
| Raw ev draw | -0.0130 |
| Raw edge prob away | -0.0114 |
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
| Draw | 26.8% | 3.73 |
| Chelsea win | 39.0% | 2.57 |

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
| 1 | 1-1 | 12.81% |
| 2 | 0-1 | 9.33% |
| 3 | 1-2 | 8.93% |
| 4 | 1-0 | 8.22% |
| 5 | 0-0 | 8.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 34.2% | 33.2% | 2.95 | +1.0% |
| Draw | 26.8% | 24.4% | 3.86 | +3.5% |
| Chelsea win | 39.0% | 42.4% | 2.45 | -4.6% |
| Over 2.5 | 48.4% | 59.0% | 1.70 | -17.8% |
| Under 2.5 | 51.6% | 41.0% | 2.34 | +20.8% |

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
| Market best home last update utc | 2026-10-09T13:48:18Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
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
| P btts yes | 53.2% |
| P btts no | 46.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.17 |
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
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 53.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.75 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +1.0% |
| Draw probability edge | +2.4% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | 0.0205 |
| Raw ev home | 0.0405 |
| Raw edge prob draw | 0.0479 |
| Raw ev draw | 0.1269 |
| Raw edge prob away | -0.0683 |
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
| Over 2.5 | 31.8% | 58.1% | 1.81 | -42.4% |
| Under 2.5 | 68.2% | 41.9% | 2.23 | +52.1% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
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
| P btts yes | 37.9% |
| P btts no | 62.1% |
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
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 87.1% |
| Raw p btts yes | 39.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.64 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -15.7% |
| Draw probability edge | +6.1% |
| Away probability edge | +9.6% |
| Over 2.5 probability edge | -26.3% |
| Under 2.5 probability edge | +26.3% |
| Raw edge prob home | -0.3132 |
| Raw ev home | -0.5318 |
| Raw edge prob draw | 0.1215 |
| Raw ev draw | 0.4023 |
| Raw edge prob away | 0.1918 |
| Raw ev away | 1.0189 |
| Market p over 1 5 | 80.5% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T13:48:19Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.94 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 68.4% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T13:48:34Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 2.72 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 54.5% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-09T13:48:50Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.02 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **83.1%**. Expected goals are 3.46 for Manchester City and 0.70 for Ipswich Town (4.15 combined). The most likely exact score is 3-0 at 10.3%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 77.3%; Under 4.5 goals: 61.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 83.1% | 1.20 |
| Draw | 10.5% | 9.56 |
| Ipswich Town win | 6.5% | 15.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.46 |
| Ipswich Town expected goals | 0.70 |
| Expected total goals | 4.15 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 91.7% |
| Under 1.5 | 8.3% |
| Over 2.5 | 77.3% |
| Under 2.5 | 22.7% |
| Over 3.5 | 58.3% |
| Under 3.5 | 41.7% |
| Over 4.5 | 39.0% |
| Under 4.5 | 61.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.30% |
| 2 | 2-0 | 8.94% |
| 3 | 4-0 | 8.91% |
| 4 | 3-1 | 7.19% |
| 5 | 2-1 | 6.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 83.1% | 78.9% | 1.29 | +7.2% |
| Draw | 10.5% | 11.8% | 7.20 | -24.7% |
| Ipswich Town win | 6.5% | 9.3% | 12.50 | -19.1% |
| Over 2.5 | 77.3% | 71.2% | 1.38 | +6.7% |
| Under 2.5 | 22.7% | 28.8% | 3.08 | -30.1% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:02Z |
| Market best away last update utc | 2026-10-09T13:48:18Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | Nordic Bet |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Man City |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.44 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.07 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.41 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.40 |
| Fair Over 4.5 odds | 2.56 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 87.2% |
| Unadjusted draw probability | 9.1% |
| Unadjusted away-win probability | 3.7% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.4% |
| Raw p btts yes | 49.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.23 |
| Reference draw odds | 6.50 |
| Reference away odds | 8.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +4.1% |
| Draw probability edge | -1.3% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | +6.1% |
| Under 2.5 probability edge | -6.1% |
| Raw edge prob home | 0.0827 |
| Raw ev home | 0.1249 |
| Raw edge prob draw | -0.0263 |
| Raw ev draw | -0.3414 |
| Raw edge prob away | -0.0564 |
| Raw ev away | -0.5433 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T13:48:19Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 51.8% |
| Market under 3 5 odds | 1.92 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T13:47:25Z |
| Market reference under 3 5 odds | 1.85 |
| Market reference under 3 5 opposite odds | 1.98 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 54.3% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T13:48:19Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.02 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **45.8%**. Expected goals are 1.77 for Newcastle United and 1.44 for Aston Villa (3.21 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 62.4%; Under 4.5 goals: 77.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 45.8% | 2.19 |
| Draw | 24.7% | 4.05 |
| Aston Villa win | 29.6% | 3.38 |

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
| 1 | 1-1 | 11.13% |
| 2 | 2-1 | 9.38% |
| 3 | 1-2 | 7.21% |
| 4 | 2-0 | 6.52% |
| 5 | 2-2 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 45.8% | 47.1% | 2.17 | -0.7% |
| Draw | 24.7% | 24.1% | 3.95 | -2.5% |
| Aston Villa win | 29.6% | 28.8% | 3.35 | -1.0% |
| Over 2.5 | 62.4% | 60.0% | 1.65 | +2.9% |
| Under 2.5 | 37.6% | 40.0% | 2.45 | -7.8% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Newcastle |
| Matched away-team name | Aston Villa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.2% |
| P btts no | 35.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.95 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.29 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.66 |
| Fair Over 3.5 odds | 2.50 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.51 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 44.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 64.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | -1.3% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +2.4% |
| Under 2.5 probability edge | -2.4% |
| Raw edge prob home | -0.0269 |
| Raw ev home | -0.0364 |
| Raw edge prob draw | 0.0108 |
| Raw ev draw | -0.0036 |
| Raw edge prob away | 0.0161 |
| Raw ev away | 0.0173 |
| Market p over 1 5 | 82.7% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T13:48:19Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 62.8% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T13:48:34Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 63.4% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T13:48:19Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.45 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.7%**. Expected goals are 1.53 for Bournemouth and 1.04 for Sunderland (2.57 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 48.0%; Under 4.5 goals: 88.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.7% | 2.10 |
| Draw | 26.7% | 3.74 |
| Sunderland win | 25.5% | 3.92 |

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
| Over 2.5 | 48.0% |
| Under 2.5 | 52.0% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.77% |
| 2 | 1-0 | 10.50% |
| 3 | 2-1 | 9.41% |
| 4 | 2-0 | 9.02% |
| 5 | 0-0 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.7% | 48.2% | 2.04 | -2.6% |
| Draw | 26.7% | 25.3% | 3.75 | +0.2% |
| Sunderland win | 25.5% | 26.5% | 3.85 | -1.7% |
| Over 2.5 | 48.0% | 52.0% | 1.88 | -9.7% |
| Under 2.5 | 52.0% | 48.0% | 2.07 | +7.6% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
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
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.83 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.30 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 74.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 52.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.96 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | -0.5% |
| Draw probability edge | +1.4% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | -0.0092 |
| Raw ev home | -0.0357 |
| Raw edge prob draw | 0.0287 |
| Raw ev draw | 0.0562 |
| Raw edge prob away | -0.0195 |
| Raw ev away | -0.0543 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **57.3%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 57.0%; Under 4.5 goals: 82.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 57.3% | 1.75 |
| Draw | 22.7% | 4.40 |
| Crystal Palace win | 20.0% | 5.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 1.85 |
| Crystal Palace expected goals | 1.08 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 57.0% |
| Under 2.5 | 43.0% |
| Over 3.5 | 34.0% |
| Under 3.5 | 66.0% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.76% |
| 2 | 2-1 | 10.43% |
| 3 | 2-0 | 9.65% |
| 4 | 1-0 | 9.27% |
| 5 | 3-1 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 57.3% | 60.4% | 1.67 | -4.3% |
| Draw | 22.7% | 20.6% | 4.45 | +1.2% |
| Crystal Palace win | 20.0% | 19.0% | 5.20 | +3.8% |
| Over 2.5 | 57.0% | 61.5% | 1.65 | -6.0% |
| Under 2.5 | 43.0% | 38.5% | 2.45 | +5.4% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:50Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
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
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.95 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.10 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.94 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.65 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 80.1% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.50 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -3.1% |
| Draw probability edge | +2.2% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.0622 |
| Raw ev home | -0.0953 |
| Raw edge prob draw | 0.0439 |
| Raw ev draw | 0.1100 |
| Raw edge prob away | 0.0184 |
| Raw ev away | 0.0860 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **37.1%**. Expected goals are 1.42 for Leeds United and 1.30 for Manchester United (2.72 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 51.9%; Under 4.5 goals: 85.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 37.1% | 2.69 |
| Draw | 25.9% | 3.86 |
| Manchester United win | 36.9% | 2.71 |

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
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.36% |
| 2 | 1-2 | 8.80% |
| 3 | 2-1 | 8.30% |
| 4 | 0-1 | 8.13% |
| 5 | 1-0 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 37.1% | 35.6% | 2.94 | +9.1% |
| Draw | 25.9% | 23.7% | 3.80 | -1.4% |
| Manchester United win | 36.9% | 40.7% | 2.44 | -9.9% |
| Over 2.5 | 51.9% | 57.6% | 1.69 | -12.3% |
| Under 2.5 | 48.1% | 42.4% | 2.37 | +14.0% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:48:53Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.82 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.32 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.01 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 38.6% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 56.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.30 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +1.5% |
| Draw probability edge | +2.3% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | 0.0294 |
| Raw ev home | 0.1344 |
| Raw edge prob draw | 0.0455 |
| Raw ev draw | 0.0721 |
| Raw edge prob away | -0.0749 |
| Raw ev away | -0.1899 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **58.0%**. Expected goals are 0.77 for Nottingham Forest and 1.55 for Arsenal (2.32 combined). The most likely exact score is 0-1 at 14.8%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 42.2%; Under 4.5 goals: 91.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 17.2% | 5.83 |
| Draw | 24.9% | 4.02 |
| Arsenal win | 58.0% | 1.72 |

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
| 1 | 0-1 | 14.83% |
| 2 | 0-2 | 12.51% |
| 3 | 1-1 | 11.50% |
| 4 | 0-0 | 9.80% |
| 5 | 1-2 | 9.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 17.2% | 17.0% | 6.20 | +6.3% |
| Draw | 24.9% | 21.7% | 4.10 | +1.9% |
| Arsenal win | 58.0% | 61.3% | 1.66 | -3.7% |
| Over 2.5 | 42.2% | 52.3% | 1.97 | -16.9% |
| Under 2.5 | 57.8% | 47.7% | 1.97 | +13.9% |

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
| Market best home last update utc | 2026-10-09T13:48:03Z |
| Market best draw last update utc | 2026-10-09T13:48:18Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
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
| P btts yes | 42.8% |
| P btts no | 57.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.20 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.24 |
| Fair Over 2.5 odds | 2.37 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.79 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.15 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 43.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 5.00 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.56 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +0.2% |
| Draw probability edge | +3.1% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | 0.0032 |
| Raw ev home | 0.0734 |
| Raw edge prob draw | 0.0627 |
| Raw ev draw | 0.1477 |
| Raw edge prob away | -0.0659 |
| Raw ev away | -0.0921 |

</details>


---
