# Ligue 1 — football model report

Fixtures in this report: **16**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 963 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1689.031 |
| Base scoring parameter | 0.211 |
| Home-advantage parameter | 0.193 |
| Dixon-Coles low-score adjustment | -0.052 |
| Xi per day | 0.0009 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 16.00 |
| Additional event odds calls used before this league | 20.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-10 — AS Monaco vs Toulouse

The model's most likely 1X2 outcome is **AS Monaco win** at **58.4%**. Expected goals are 1.95 for AS Monaco and 1.13 for Toulouse (3.07 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 59.7%; Under 3.5 goals: 62.8%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 58.1%; BTTS No (at least one team does not score): 41.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 58.4% | 1.71 |
| Draw | 22.1% | 4.53 |
| Toulouse win | 19.5% | 5.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.95 |
| Toulouse expected goals | 1.13 |
| Expected total goals | 3.07 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 81.9% |
| Under 1.5 | 18.1% |
| Over 2.5 | 59.7% |
| Under 2.5 | 40.3% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.32% |
| 2 | 1-1 | 10.27% |
| 3 | 2-0 | 9.16% |
| 4 | 1-0 | 8.86% |
| 5 | 3-1 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 58.4% | 60.9% | 1.69 | -1.2% |
| Draw | 22.1% | 21.2% | 4.41 | -2.6% |
| Toulouse win | 19.5% | 17.8% | 5.60 | +9.1% |
| Over 2.5 | 59.7% | 59.8% | 1.65 | -1.5% |
| Under 2.5 | 40.3% | 40.2% | 2.45 | -1.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T18:45:00+00:00 |
| Fixture id | c2c64ebfc5810226f807c1920d580392 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:46:34Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:46:16Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | LeoVegas (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monaco |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.17 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.51 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.48 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.01 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 56.0% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 21.1% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 63.1% |
| Raw p btts yes | 58.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.57 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -2.5% |
| Draw probability edge | +0.9% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0497 |
| Raw ev home | -0.0544 |
| Raw edge prob draw | 0.0171 |
| Raw ev draw | 0.0116 |
| Raw edge prob away | 0.0326 |
| Raw ev away | 0.1820 |

</details>


---

## 2026-10-10 — Brest vs Angers

The model's most likely 1X2 outcome is **Brest win** at **51.7%**. Expected goals are 1.56 for Brest and 0.88 for Angers (2.44 combined). The most likely exact score is 1-0 at 12.8%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 44.3%; Under 3.5 goals: 77.2%; Under 4.5 goals: 89.9%; BTTS Yes (both teams score): 46.6%; BTTS No (at least one team does not score): 53.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 51.7% | 1.93 |
| Draw | 25.7% | 3.89 |
| Angers win | 22.6% | 4.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Angers expected goals | 0.88 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 70.5% |
| Under 1.5 | 29.5% |
| Over 2.5 | 44.3% |
| Under 2.5 | 55.7% |
| Over 3.5 | 22.8% |
| Under 3.5 | 77.2% |
| Over 4.5 | 10.1% |
| Under 4.5 | 89.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.76% |
| 2 | 1-1 | 12.10% |
| 3 | 2-0 | 10.41% |
| 4 | 2-1 | 9.16% |
| 5 | 0-0 | 9.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 51.7% | 50.7% | 2.00 | +3.4% |
| Draw | 25.7% | 24.6% | 3.95 | +1.5% |
| Angers win | 22.6% | 24.6% | 4.10 | -7.2% |
| Over 2.5 | 44.3% | 56.9% | 1.74 | -23.0% |
| Under 2.5 | 55.7% | 43.1% | 2.27 | +26.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T18:45:00+00:00 |
| Fixture id | 007dc2ff845c33e3e18f2bd2bc126304 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:46:16Z |
| Market best away last update utc | 2026-10-10T15:46:34Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brest |
| Matched away-team name | Angers |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 46.6% |
| P btts no | 53.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.11 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.38 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.90 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 52.6% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 20.6% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 46.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.86 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +1.0% |
| Draw probability edge | +1.1% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | 0.0192 |
| Raw ev home | 0.0529 |
| Raw edge prob draw | 0.0210 |
| Raw ev draw | 0.0563 |
| Raw edge prob away | -0.0402 |
| Raw ev away | -0.1548 |

</details>


---

## 2026-10-10 — Lorient vs Paris FC

The model's most likely 1X2 outcome is **Paris FC win** at **42.9%**. Expected goals are 1.33 for Lorient and 1.43 for Paris FC (2.76 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 52.2%; Under 3.5 goals: 70.0%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 56.7%; BTTS No (at least one team does not score): 43.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 30.3% | 3.30 |
| Draw | 26.9% | 3.72 |
| Paris FC win | 42.9% | 2.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.33 |
| Paris FC expected goals | 1.43 |
| Expected total goals | 2.76 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 76.9% |
| Under 1.5 | 23.1% |
| Over 2.5 | 52.2% |
| Under 2.5 | 47.8% |
| Over 3.5 | 30.0% |
| Under 3.5 | 70.0% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.73% |
| 2 | 1-2 | 9.48% |
| 3 | 0-1 | 9.25% |
| 4 | 0-2 | 7.12% |
| 5 | 2-1 | 7.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 30.3% | 26.2% | 3.81 | +15.4% |
| Draw | 26.9% | 27.0% | 3.50 | -6.0% |
| Paris FC win | 42.9% | 46.8% | 2.20 | -5.7% |
| Over 2.5 | 52.2% | 48.6% | 2.03 | +5.9% |
| Under 2.5 | 47.8% | 51.4% | 1.91 | -8.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T18:45:00+00:00 |
| Fixture id | 3aa72885e0aa107c62843749f7930a9a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:46:48Z |
| Market best draw last update utc | 2026-10-10T15:46:34Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lorient |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.34 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.33 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.82 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 34.4% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 76.9% |
| Raw p under 3 5 | 70.0% |
| Raw p btts yes | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.40 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | +4.1% |
| Draw probability edge | -0.2% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Raw edge prob home | 0.0822 |
| Raw ev home | 0.3101 |
| Raw edge prob draw | -0.0036 |
| Raw ev draw | -0.0662 |
| Raw edge prob away | -0.0786 |
| Raw ev away | -0.1435 |

</details>


---

## 2026-10-10 — Paris Saint Germain vs Le Mans FC

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **83.3%**. Expected goals are 3.17 for Paris Saint Germain and 1.12 for Le Mans FC (4.29 combined). The most likely exact score is 3-1 at 8.8%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 81.6%; Under 3.5 goals: 36.9%; Under 4.5 goals: 55.8%; BTTS Yes (both teams score): 63.4%; BTTS No (at least one team does not score): 36.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 83.3% | 1.20 |
| Draw | 9.5% | 10.49 |
| Le Mans FC win | 7.2% | 13.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 3.17 |
| Le Mans FC expected goals | 1.12 |
| Expected total goals | 4.29 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 93.4% |
| Under 1.5 | 6.6% |
| Over 2.5 | 81.6% |
| Under 2.5 | 18.4% |
| Over 3.5 | 63.1% |
| Under 3.5 | 36.9% |
| Over 4.5 | 44.2% |
| Under 4.5 | 55.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 8.80% |
| 2 | 2-1 | 8.33% |
| 3 | 3-0 | 7.87% |
| 4 | 2-0 | 7.45% |
| 5 | 4-1 | 6.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 83.3% | 89.3% | 1.15 | -4.2% |
| Draw | 9.5% | 5.9% | 11.50 | +9.6% |
| Le Mans FC win | 7.2% | 4.8% | 23.00 | +65.5% |
| Over 2.5 | 81.6% | 78.0% | 1.29 | +5.3% |
| Under 2.5 | 18.4% | 22.0% | 3.90 | -28.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T18:45:00+00:00 |
| Fixture id | 2849460eb4d15adbb20ec15927a0fd4a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:46:34Z |
| Market best draw last update utc | 2026-10-10T15:46:34Z |
| Market best away last update utc | 2026-10-10T15:46:33Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betsson |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Paris SG |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.4% |
| P btts no | 36.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 84.98 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.20 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.44 |
| Fair Over 3.5 odds | 1.58 |
| Fair Under 3.5 odds | 2.71 |
| Fair Over 4.5 odds | 2.26 |
| Fair Under 4.5 odds | 1.79 |
| Unadjusted home-win probability | 77.2% |
| Unadjusted draw probability | 13.2% |
| Unadjusted away-win probability | 9.6% |
| Raw p over 1 5 | 93.0% |
| Raw p under 3 5 | 38.0% |
| Raw p btts yes | 64.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.10 |
| Reference draw odds | 11.00 |
| Reference away odds | 13.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.90 |
| Home probability edge | -6.1% |
| Draw probability edge | +3.7% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Raw edge prob home | -0.1213 |
| Raw ev home | -0.1122 |
| Raw edge prob draw | 0.0735 |
| Raw ev draw | 0.5192 |
| Raw edge prob away | 0.0478 |
| Raw ev away | 1.2045 |
| Market p over 1 5 | 92.2% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-10T15:46:16Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 8.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 44.9% |
| Market under 3 5 odds | 2.25 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-10T15:45:14Z |
| Market reference under 3 5 odds | 2.12 |
| Market reference under 3 5 opposite odds | 1.75 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 48.3% |
| Market btts yes odds | 2.05 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-10T15:46:44Z |
| Market reference btts yes odds | 1.95 |
| Market reference btts yes opposite odds | 1.83 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-11 — Nice vs Strasbourg

The model's most likely 1X2 outcome is **Nice win** at **39.8%**. Expected goals are 1.46 for Nice and 1.39 for Strasbourg (2.84 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.1%; Under 3.5 goals: 68.2%; Under 4.5 goals: 84.1%; BTTS Yes (both teams score): 58.1%; BTTS No (at least one team does not score): 41.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nice win | 39.8% | 2.51 |
| Draw | 26.3% | 3.81 |
| Strasbourg win | 33.9% | 2.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nice expected goals | 1.46 |
| Strasbourg expected goals | 1.39 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 31.8% |
| Under 3.5 | 68.2% |
| Over 4.5 | 15.9% |
| Under 4.5 | 84.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.38% |
| 2 | 2-1 | 8.88% |
| 3 | 1-0 | 8.16% |
| 4 | 1-2 | 7.83% |
| 5 | 0-1 | 7.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nice win | 39.8% | 41.2% | 2.48 | -1.3% |
| Draw | 26.3% | 26.3% | 3.75 | -1.5% |
| Strasbourg win | 33.9% | 32.5% | 3.07 | +4.1% |
| Over 2.5 | 54.1% | 56.9% | 1.77 | -4.3% |
| Under 2.5 | 45.9% | 43.1% | 2.25 | +3.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | 5d3606630a2d3a218a6340d082c1bdc6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Tipico |
| Matched home-team name | Nice |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.54 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.59 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.28 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 38.4% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 58.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.25 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -1.4% |
| Draw probability edge | -0.0% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | -0.0287 |
| Raw ev home | -0.0483 |
| Raw edge prob draw | -0.0001 |
| Raw ev draw | -0.0152 |
| Raw edge prob away | 0.0288 |
| Raw ev away | 0.0857 |

</details>


---

## 2026-10-11 — Rennes vs Auxerre

The model's most likely 1X2 outcome is **Rennes win** at **61.0%**. Expected goals are 1.84 for Rennes and 1.14 for Auxerre (2.98 combined). The most likely exact score is 2-1 at 11.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 58.7%; Under 3.5 goals: 64.4%; Under 4.5 goals: 81.1%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 61.0% | 1.64 |
| Draw | 20.7% | 4.83 |
| Auxerre win | 18.3% | 5.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.84 |
| Auxerre expected goals | 1.14 |
| Expected total goals | 2.98 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 58.7% |
| Under 2.5 | 41.3% |
| Over 3.5 | 35.6% |
| Under 3.5 | 64.4% |
| Over 4.5 | 18.9% |
| Under 4.5 | 81.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.25% |
| 2 | 1-0 | 10.06% |
| 3 | 2-0 | 9.83% |
| 4 | 1-1 | 9.70% |
| 5 | 3-1 | 6.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 61.0% | 68.8% | 1.48 | -9.8% |
| Draw | 20.7% | 17.5% | 5.20 | +7.7% |
| Auxerre win | 18.3% | 13.7% | 7.50 | +37.5% |
| Over 2.5 | 58.7% | 63.8% | 1.51 | -11.3% |
| Under 2.5 | 41.3% | 36.2% | 2.61 | +7.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T15:15:00+00:00 |
| Fixture id | 34f584ab922e220dc4f3b81217959d6d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:37:39Z |
| Market best away last update utc | 2026-10-10T15:46:16Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | LeoVegas (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Rennes |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.56 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.29 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 53.1% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 80.4% |
| Raw p under 3 5 | 65.1% |
| Raw p btts yes | 57.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.40 |
| Reference draw odds | 4.80 |
| Reference away odds | 6.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -7.9% |
| Draw probability edge | +3.2% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.1573 |
| Raw ev home | -0.2143 |
| Raw edge prob draw | 0.0641 |
| Raw ev draw | 0.2438 |
| Raw edge prob away | 0.0932 |
| Raw ev away | 0.7245 |

</details>


---

## 2026-10-11 — Troyes vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **62.9%**. Expected goals are 0.92 for Troyes and 2.68 for Marseille (3.60 combined). The most likely exact score is 1-1 at 8.9%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 67.3%; Under 3.5 goals: 53.7%; Under 4.5 goals: 72.5%; BTTS Yes (both teams score): 58.5%; BTTS No (at least one team does not score): 41.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 17.5% | 5.71 |
| Draw | 19.6% | 5.11 |
| Marseille win | 62.9% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.92 |
| Marseille expected goals | 2.68 |
| Expected total goals | 3.60 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 86.5% |
| Under 1.5 | 13.5% |
| Over 2.5 | 67.3% |
| Under 2.5 | 32.7% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.5% |
| Under 4.5 | 72.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.86% |
| 2 | 0-2 | 8.30% |
| 3 | 1-2 | 7.66% |
| 4 | 0-3 | 7.41% |
| 5 | 1-3 | 6.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 17.5% | 24.9% | 4.04 | -29.2% |
| Draw | 19.6% | 23.5% | 4.04 | -20.9% |
| Marseille win | 62.9% | 51.6% | 2.02 | +27.1% |
| Over 2.5 | 67.3% | 60.5% | 1.65 | +11.1% |
| Under 2.5 | 32.7% | 39.5% | 2.45 | -20.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T18:45:00+00:00 |
| Fixture id | cb7067ac191abf32ad49dad45e46f639 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:46:34Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.5% |
| P btts no | 41.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.02 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.41 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.06 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.64 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 15.7% |
| Unadjusted away-win probability | 74.2% |
| Raw p over 1 5 | 87.8% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 56.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.60 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.84 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -7.4% |
| Draw probability edge | -3.9% |
| Away probability edge | +11.3% |
| Over 2.5 probability edge | +6.9% |
| Under 2.5 probability edge | -6.9% |
| Raw edge prob home | -0.1479 |
| Raw ev home | -0.5912 |
| Raw edge prob draw | -0.0782 |
| Raw ev draw | -0.3669 |
| Raw edge prob away | 0.2261 |
| Raw ev away | 0.4990 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-10T15:46:17Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 61.3% |
| Market under 3 5 odds | 1.60 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-10T15:46:17Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 61.2% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-10T15:46:49Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.38 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-16 — Le Mans FC vs Toulouse

The model's most likely 1X2 outcome is **Le Mans FC win** at **38.0%**. Expected goals are 1.87 for Le Mans FC and 1.51 for Toulouse (3.37 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 64.7%; Under 3.5 goals: 56.8%; Under 4.5 goals: 75.4%; BTTS Yes (both teams score): 66.9%; BTTS No (at least one team does not score): 33.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 38.0% | 2.63 |
| Draw | 25.3% | 3.95 |
| Toulouse win | 36.6% | 2.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Mans FC expected goals | 1.87 |
| Toulouse expected goals | 1.51 |
| Expected total goals | 3.37 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 64.7% |
| Under 2.5 | 35.3% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.6% |
| Under 4.5 | 75.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.99% |
| 2 | 1-2 | 8.63% |
| 3 | 2-1 | 7.47% |
| 4 | 2-2 | 7.34% |
| 5 | 0-1 | 5.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 38.0% | 30.3% | 3.30 | +25.4% |
| Draw | 25.3% | 27.3% | 3.57 | -9.5% |
| Toulouse win | 36.6% | 42.4% | 2.34 | -14.3% |
| Over 2.5 | 64.7% | 53.7% | 1.84 | +19.1% |
| Under 2.5 | 35.3% | 46.3% | 2.12 | -25.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-16T18:45:00+00:00 |
| Fixture id | 66c168c030f3faad3983fcadc3060009 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 17.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | LeoVegas (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Mans |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.9% |
| P btts no | 33.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.47 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.80 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.83 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.07 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 45.7% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 30.9% |
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 66.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.00 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.00 |
| Home probability edge | +7.7% |
| Draw probability edge | -2.0% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | +11.0% |
| Under 2.5 probability edge | -11.0% |
| Raw edge prob home | 0.1547 |
| Raw ev home | 0.5097 |
| Raw edge prob draw | -0.0391 |
| Raw ev draw | -0.1651 |
| Raw edge prob away | -0.1156 |
| Raw ev away | -0.2778 |
| Market p over 1 5 | 78.0% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-10T15:46:49Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 68.2% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-10T15:46:48Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.86 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 59.8% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-10T15:46:49Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **57.6%**. Expected goals are 1.76 for Lille and 0.94 for Brest (2.70 combined). The most likely exact score is 1-0 at 11.5%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 51.1%; Under 3.5 goals: 71.2%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 57.6% | 1.74 |
| Draw | 23.6% | 4.23 |
| Brest win | 18.8% | 5.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.76 |
| Brest expected goals | 0.94 |
| Expected total goals | 2.70 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.55% |
| 2 | 1-1 | 11.27% |
| 3 | 2-0 | 10.67% |
| 4 | 2-1 | 10.06% |
| 5 | 0-0 | 7.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 57.6% | 59.1% | 1.66 | -4.4% |
| Draw | 23.6% | 22.7% | 4.37 | +3.3% |
| Brest win | 18.8% | 18.1% | 5.50 | +3.3% |
| Over 2.5 | 51.1% | 56.9% | 1.74 | -11.2% |
| Under 2.5 | 48.9% | 43.1% | 2.27 | +11.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | ad25a350c89b64715e15c59cde5653d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:46:16Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | LeoVegas (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.24 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.48 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.21 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 56.0% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 19.4% |
| Raw p over 1 5 | 75.7% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 51.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.62 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | -1.6% |
| Draw probability edge | +0.9% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0313 |
| Raw ev home | -0.0702 |
| Raw edge prob draw | 0.0182 |
| Raw ev draw | 0.0728 |
| Raw edge prob away | 0.0131 |
| Raw ev away | 0.0691 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **62.9%**. Expected goals are 1.23 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.6%; Under 3.5 goals: 56.8%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 61.8%; BTTS No (at least one team does not score): 38.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.5% | 5.72 |
| Draw | 19.6% | 5.09 |
| Paris Saint Germain win | 62.9% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.23 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.72% |
| 2 | 1-1 | 8.77% |
| 3 | 0-2 | 8.74% |
| 4 | 0-1 | 7.79% |
| 5 | 1-3 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.5% | 13.7% | 6.73 | +17.6% |
| Draw | 19.6% | 17.5% | 5.75 | +12.9% |
| Paris Saint Germain win | 62.9% | 68.8% | 1.46 | -8.2% |
| Over 2.5 | 65.6% | 73.1% | 1.33 | -12.8% |
| Under 2.5 | 34.4% | 26.9% | 3.42 | +17.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T15:15:00+00:00 |
| Fixture id | f3034246520a2ee4ff0ac0d5074966f8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:44:27Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betclic (FR) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Strasbourg |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.8% |
| P btts no | 38.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.27 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.82 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.02 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 57.0% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.4% |
| Raw p btts yes | 62.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 6.00 |
| Reference draw odds | 4.80 |
| Reference away odds | 1.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Home probability edge | +3.8% |
| Draw probability edge | +2.1% |
| Away probability edge | -5.9% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | 0.0761 |
| Raw ev home | 0.4321 |
| Raw edge prob draw | 0.0424 |
| Raw ev draw | 0.2511 |
| Raw edge prob away | -0.1185 |
| Raw ev away | -0.1683 |
| Market p over 1 5 | 91.2% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-10T15:46:49Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 7.50 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 46.7% |
| Market under 3 5 odds | 2.06 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-10T15:42:55Z |
| Market reference under 3 5 odds | 2.04 |
| Market reference under 3 5 opposite odds | 1.80 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 64.5% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-10T15:46:49Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.60 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **62.1%**. Expected goals are 0.78 for Troyes and 2.31 for RC Lens (3.09 combined). The most likely exact score is 0-2 at 10.5%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.7%; Under 3.5 goals: 64.4%; Under 4.5 goals: 81.2%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 16.7% | 5.98 |
| Draw | 21.2% | 4.72 |
| RC Lens win | 62.1% | 1.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.78 |
| RC Lens expected goals | 2.31 |
| Expected total goals | 3.09 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 35.6% |
| Under 3.5 | 64.4% |
| Over 4.5 | 18.8% |
| Under 4.5 | 81.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 10.55% |
| 2 | 1-1 | 10.08% |
| 3 | 0-1 | 8.76% |
| 4 | 1-2 | 8.25% |
| 5 | 0-3 | 8.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 16.7% | 22.9% | 4.30 | -28.0% |
| Draw | 21.2% | 24.2% | 4.10 | -13.2% |
| RC Lens win | 62.1% | 52.9% | 1.87 | +16.1% |
| Over 2.5 | 57.7% | 61.3% | 1.64 | -5.4% |
| Under 2.5 | 42.3% | 38.7% | 2.46 | +4.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | b077aa049133c0358bcd643bfee48da3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:46:16Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.25 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.13 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.31 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 10.6% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 71.3% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 49.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.90 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -6.1% |
| Draw probability edge | -3.0% |
| Away probability edge | +9.2% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | -0.1230 |
| Raw ev home | -0.5449 |
| Raw edge prob draw | -0.0609 |
| Raw ev draw | -0.2563 |
| Raw edge prob away | 0.1839 |
| Raw ev away | 0.3329 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **48.3%**. Expected goals are 0.95 for Angers and 1.65 for Marseille (2.59 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 47.6%; Under 3.5 goals: 74.1%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 25.6% | 3.90 |
| Draw | 26.0% | 3.84 |
| Marseille win | 48.3% | 2.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.95 |
| Marseille expected goals | 1.65 |
| Expected total goals | 2.59 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 73.3% |
| Under 1.5 | 26.7% |
| Over 2.5 | 47.6% |
| Under 2.5 | 52.4% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.40% |
| 2 | 0-1 | 10.63% |
| 3 | 0-2 | 9.21% |
| 4 | 1-2 | 8.71% |
| 5 | 0-0 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 25.6% | 30.2% | 3.25 | -16.8% |
| Draw | 26.0% | 26.4% | 3.80 | -1.0% |
| Marseille win | 48.3% | 43.4% | 2.28 | +10.2% |
| Over 2.5 | 47.6% | 58.9% | 1.68 | -20.0% |
| Under 2.5 | 52.4% | 41.1% | 2.40 | +25.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | c7a60aa94470fe959fbf6b0c68060fc1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:46:16Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | LeoVegas (SE) |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Unibet (SE) |
| Matched home-team name | Angers |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.24 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.75 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.35 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 53.2% |
| Raw p over 1 5 | 73.8% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 50.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.00 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -4.6% |
| Draw probability edge | -0.3% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -11.3% |
| Under 2.5 probability edge | +11.3% |
| Raw edge prob home | -0.0919 |
| Raw ev home | -0.3169 |
| Raw edge prob draw | -0.0062 |
| Raw ev draw | -0.0220 |
| Raw edge prob away | 0.0981 |
| Raw ev away | 0.2140 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **37.3%**. Expected goals are 1.16 for Le Havre and 1.19 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 42.0%; Under 3.5 goals: 79.0%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 37.3% | 2.68 |
| Draw | 28.2% | 3.55 |
| Auxerre win | 34.5% | 2.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.16 |
| Auxerre expected goals | 1.19 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 68.7% |
| Under 1.5 | 31.3% |
| Over 2.5 | 42.0% |
| Under 2.5 | 58.0% |
| Over 3.5 | 21.0% |
| Under 3.5 | 79.0% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.28% |
| 2 | 1-0 | 11.24% |
| 3 | 0-1 | 10.25% |
| 4 | 0-0 | 9.85% |
| 5 | 2-1 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 37.3% | 40.1% | 2.52 | -6.1% |
| Draw | 28.2% | 27.0% | 3.55 | +0.1% |
| Auxerre win | 34.5% | 32.9% | 3.00 | +3.6% |
| Over 2.5 | 42.0% | 50.9% | 1.94 | -18.6% |
| Under 2.5 | 58.0% | 49.1% | 2.00 | +16.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | d637845b9760bb02b55bbbaa32b5c21e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:46:16Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 12.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Havre |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.16 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.38 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.76 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.10 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.0% |
| Raw p btts yes | 48.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.75 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.91 |
| Home probability edge | -2.8% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | -0.0563 |
| Raw ev home | -0.1318 |
| Raw edge prob draw | 0.0244 |
| Raw ev draw | 0.0440 |
| Raw edge prob away | 0.0320 |
| Raw ev away | 0.0843 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **46.1%**. Expected goals are 1.36 for Lorient and 1.84 for AS Monaco (3.21 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 61.3%; Under 3.5 goals: 60.3%; Under 4.5 goals: 78.4%; BTTS Yes (both teams score): 63.7%; BTTS No (at least one team does not score): 36.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 28.0% | 3.57 |
| Draw | 25.9% | 3.86 |
| AS Monaco win | 46.1% | 2.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.36 |
| AS Monaco expected goals | 1.84 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 61.3% |
| Under 2.5 | 38.7% |
| Over 3.5 | 39.7% |
| Under 3.5 | 60.3% |
| Over 4.5 | 21.6% |
| Under 4.5 | 78.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.68% |
| 2 | 1-2 | 8.95% |
| 3 | 2-2 | 6.97% |
| 4 | 2-1 | 6.95% |
| 5 | 0-1 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 28.0% | 28.1% | 3.60 | +0.7% |
| Draw | 25.9% | 28.1% | 3.56 | -7.7% |
| AS Monaco win | 46.1% | 43.8% | 2.24 | +3.3% |
| Over 2.5 | 61.3% | 52.2% | 1.93 | +18.4% |
| Under 2.5 | 38.7% | 47.8% | 2.01 | -22.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | 53f5fe7ed0ba0fbf6345c73270e4cd00 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:45:24Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | LeoVegas (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lorient |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 63.7% |
| P btts no | 36.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.01 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.01 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.52 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.62 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 27.9% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 83.5% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 63.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.25 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | -0.1% |
| Draw probability edge | -2.2% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | +9.1% |
| Under 2.5 probability edge | -9.1% |
| Raw edge prob home | -0.0022 |
| Raw ev home | 0.0032 |
| Raw edge prob draw | -0.0432 |
| Raw ev draw | -0.1541 |
| Raw edge prob away | 0.0454 |
| Raw ev away | 0.0836 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **56.5%**. Expected goals are 1.78 for Lyon and 1.08 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 55.0%; Under 3.5 goals: 67.6%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 56.5% | 1.77 |
| Draw | 23.4% | 4.28 |
| Nice win | 20.2% | 4.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.78 |
| Nice expected goals | 1.08 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.7% |
| Under 1.5 | 21.3% |
| Over 2.5 | 55.0% |
| Under 2.5 | 45.0% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.07% |
| 2 | 2-1 | 10.41% |
| 3 | 1-0 | 10.22% |
| 4 | 2-0 | 9.63% |
| 5 | 3-1 | 6.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 56.5% | 59.8% | 1.71 | -3.5% |
| Draw | 23.4% | 22.3% | 4.20 | -1.9% |
| Nice win | 20.2% | 18.0% | 5.24 | +5.7% |
| Over 2.5 | 55.0% | 55.8% | 1.78 | -2.1% |
| Under 2.5 | 45.0% | 44.2% | 2.25 | +1.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T18:45:00+00:00 |
| Fixture id | 471f891b1f6516a864ad94c8eb649f5e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:37:39Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Tipico |
| Matched home-team name | Lyon |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.62 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.69 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.08 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.09 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 53.1% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 22.4% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.58 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -3.3% |
| Draw probability edge | +1.1% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.0662 |
| Raw ev home | -0.0912 |
| Raw edge prob draw | 0.0219 |
| Raw ev draw | 0.0272 |
| Raw edge prob away | 0.0444 |
| Raw ev away | 0.1736 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **43.1%**. Expected goals are 1.62 for Paris FC and 1.36 for Rennes (2.98 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.1%; Under 3.5 goals: 65.2%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 60.2%; BTTS No (at least one team does not score): 39.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 43.1% | 2.32 |
| Draw | 25.7% | 3.90 |
| Rennes win | 31.2% | 3.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.62 |
| Rennes expected goals | 1.36 |
| Expected total goals | 2.98 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 80.3% |
| Under 1.5 | 19.7% |
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.8% |
| Under 3.5 | 65.2% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.93% |
| 2 | 2-1 | 9.06% |
| 3 | 1-0 | 7.67% |
| 4 | 1-2 | 7.53% |
| 5 | 2-0 | 6.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 43.1% | 43.0% | 2.37 | +2.2% |
| Draw | 25.7% | 26.0% | 3.55 | -8.9% |
| Rennes win | 31.2% | 31.0% | 3.29 | +2.7% |
| Over 2.5 | 57.1% | 57.8% | 1.72 | -1.9% |
| Under 2.5 | 42.9% | 42.2% | 2.30 | -1.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | 27f7222d2abde93fc6e8d17b5b05b272 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:24Z |
| Market best draw last update utc | 2026-10-10T15:46:16Z |
| Market best away last update utc | 2026-10-10T15:45:24Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paris FC |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.2% |
| P btts no | 39.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.40 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.08 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.54 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 31.5% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 60.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +0.1% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | 0.0013 |
| Raw ev home | 0.0234 |
| Raw edge prob draw | -0.0066 |
| Raw ev draw | -0.1007 |
| Raw edge prob away | 0.0052 |
| Raw ev away | 0.0359 |

</details>


---
