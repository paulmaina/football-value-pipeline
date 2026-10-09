# Ligue 1 — football model report

Fixtures in this report: **18**.

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
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 24.00 |
| Additional event odds calls budget | 24.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-09 — RC Lens vs Lyon

The model's most likely 1X2 outcome is **RC Lens win** at **42.6%**. Expected goals are 1.57 for RC Lens and 1.23 for Lyon (2.80 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 53.0%; Under 4.5 goals: 84.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 42.6% | 2.34 |
| Draw | 26.0% | 3.85 |
| Lyon win | 31.4% | 3.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.57 |
| Lyon expected goals | 1.23 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 53.0% |
| Under 2.5 | 47.0% |
| Over 3.5 | 30.7% |
| Under 3.5 | 69.3% |
| Over 4.5 | 15.2% |
| Under 4.5 | 84.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.29% |
| 2 | 2-1 | 8.80% |
| 3 | 1-0 | 8.54% |
| 4 | 1-2 | 7.75% |
| 5 | 0-1 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 42.6% | 40.6% | 2.44 | +4.1% |
| Draw | 26.0% | 25.8% | 3.85 | -0.1% |
| Lyon win | 31.4% | 33.6% | 3.05 | -4.2% |
| Over 2.5 | 53.0% | 63.0% | 1.53 | -18.9% |
| Under 2.5 | 47.0% | 37.0% | 2.56 | +20.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-09T18:45:00+00:00 |
| Fixture id | 17694e68f399fdf9c5030021ec9bb595 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:41:37Z |
| Market best away last update utc | 2026-10-09T07:42:08Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Lens |
| Matched away-team name | Lyon |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.6% |
| P btts no | 43.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.01 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.43 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.26 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.58 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 44.7% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 29.2% |
| Raw p over 1 5 | 77.5% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.40 |
| Reference draw odds | 3.72 |
| Reference away odds | 2.88 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | +2.1% |
| Draw probability edge | +0.1% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | 0.0417 |
| Raw ev home | 0.0914 |
| Raw edge prob draw | 0.0026 |
| Raw ev draw | 0.0040 |
| Raw edge prob away | -0.0442 |
| Raw ev away | -0.1097 |

</details>


---

## 2026-10-10 — AS Monaco vs Toulouse

The model's most likely 1X2 outcome is **AS Monaco win** at **58.5%**. Expected goals are 1.95 for AS Monaco and 1.13 for Toulouse (3.07 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 59.8%; Under 4.5 goals: 80.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 58.5% | 1.71 |
| Draw | 22.0% | 4.55 |
| Toulouse win | 19.6% | 5.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.95 |
| Toulouse expected goals | 1.13 |
| Expected total goals | 3.07 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 81.9% |
| Under 1.5 | 18.1% |
| Over 2.5 | 59.8% |
| Under 2.5 | 40.2% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.32% |
| 2 | 1-1 | 10.22% |
| 3 | 2-0 | 9.17% |
| 4 | 1-0 | 8.87% |
| 5 | 3-1 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 58.5% | 61.0% | 1.65 | -3.5% |
| Draw | 22.0% | 21.0% | 4.60 | +1.1% |
| Toulouse win | 19.6% | 18.0% | 5.60 | +9.5% |
| Over 2.5 | 59.8% | 60.0% | 1.65 | -1.4% |
| Under 2.5 | 40.2% | 40.0% | 2.45 | -1.4% |

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
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:42:07Z |
| Market best away last update utc | 2026-10-09T07:42:07Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monaco |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.26 |
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
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.61 |
| Reference draw odds | 4.49 |
| Reference away odds | 5.21 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -2.5% |
| Draw probability edge | +1.0% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.0502 |
| Raw ev home | -0.0768 |
| Raw edge prob draw | 0.0192 |
| Raw ev draw | 0.0551 |
| Raw edge prob away | 0.0310 |
| Raw ev away | 0.1820 |

</details>


---

## 2026-10-10 — Brest vs Angers

The model's most likely 1X2 outcome is **Brest win** at **50.6%**. Expected goals are 1.56 for Brest and 0.88 for Angers (2.44 combined). The most likely exact score is 1-0 at 12.5%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 44.0%; Under 4.5 goals: 90.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 50.6% | 1.98 |
| Draw | 26.2% | 3.82 |
| Angers win | 23.2% | 4.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Angers expected goals | 0.88 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 70.4% |
| Under 1.5 | 29.6% |
| Over 2.5 | 44.0% |
| Under 2.5 | 56.0% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.50% |
| 2 | 1-1 | 12.34% |
| 3 | 2-0 | 10.20% |
| 4 | 0-0 | 9.17% |
| 5 | 2-1 | 8.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 50.6% | 48.6% | 2.06 | +4.3% |
| Draw | 26.2% | 25.6% | 3.85 | +0.8% |
| Angers win | 23.2% | 25.8% | 3.85 | -10.7% |
| Over 2.5 | 44.0% | 55.8% | 1.83 | -19.4% |
| Under 2.5 | 56.0% | 44.2% | 2.15 | +20.3% |

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
| Market best home last update utc | 2026-10-09T07:42:08Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:41:37Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Brest |
| Matched away-team name | Angers |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 46.8% |
| P btts no | 53.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.90 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.38 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 9.97 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 52.6% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 20.6% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 46.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.01 |
| Reference draw odds | 3.73 |
| Reference away odds | 3.71 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | +2.0% |
| Draw probability edge | +0.6% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -11.7% |
| Under 2.5 probability edge | +11.7% |
| Raw edge prob home | 0.0406 |
| Raw ev home | 0.0845 |
| Raw edge prob draw | 0.0110 |
| Raw ev draw | 0.0295 |
| Raw edge prob away | -0.0517 |
| Raw ev away | -0.2064 |

</details>


---

## 2026-10-10 — Lille vs Le Havre

The model's most likely 1X2 outcome is **Lille win** at **65.4%**. Expected goals are 1.77 for Lille and 0.68 for Le Havre (2.45 combined). The most likely exact score is 1-0 at 15.3%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 45.2%; Under 4.5 goals: 89.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 65.4% | 1.53 |
| Draw | 21.3% | 4.70 |
| Le Havre win | 13.3% | 7.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.77 |
| Le Havre expected goals | 0.68 |
| Expected total goals | 2.45 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.31% |
| 2 | 2-0 | 14.03% |
| 3 | 1-1 | 9.81% |
| 4 | 2-1 | 9.53% |
| 5 | 3-0 | 8.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 65.4% | 67.8% | 1.48 | -3.2% |
| Draw | 21.3% | 18.8% | 5.00 | +6.3% |
| Le Havre win | 13.3% | 13.4% | 7.80 | +4.1% |
| Over 2.5 | 45.2% | 60.9% | 1.72 | -22.2% |
| Under 2.5 | 54.8% | 39.1% | 2.35 | +28.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T15:15:00+00:00 |
| Fixture id | 2c173b3bd3a1491f17fcad1012019c4f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:41:37Z |
| Market best away last update utc | 2026-10-09T07:41:52Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Tipico |
| Matched home-team name | Lille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 40.8% |
| P btts no | 59.2% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.13 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.46 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.27 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.54 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 63.0% |
| Unadjusted draw probability | 23.7% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.9% |
| Raw p btts yes | 41.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.45 |
| Reference draw odds | 4.92 |
| Reference away odds | 6.81 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | -2.4% |
| Draw probability edge | +2.4% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -15.7% |
| Under 2.5 probability edge | +15.7% |
| Raw edge prob home | -0.0472 |
| Raw ev home | -0.0671 |
| Raw edge prob draw | 0.0484 |
| Raw ev draw | 0.1840 |
| Raw edge prob away | -0.0012 |
| Raw ev away | 0.0363 |

</details>


---

## 2026-10-10 — Lorient vs Paris FC

The model's most likely 1X2 outcome is **Paris FC win** at **40.9%**. Expected goals are 1.33 for Lorient and 1.43 for Paris FC (2.76 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 51.9%; Under 4.5 goals: 85.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 31.5% | 3.17 |
| Draw | 27.6% | 3.63 |
| Paris FC win | 40.9% | 2.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.33 |
| Paris FC expected goals | 1.43 |
| Expected total goals | 2.76 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 76.9% |
| Under 1.5 | 23.1% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 30.0% |
| Under 3.5 | 70.0% |
| Over 4.5 | 14.6% |
| Under 4.5 | 85.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.06% |
| 2 | 1-2 | 9.05% |
| 3 | 0-1 | 8.83% |
| 4 | 2-1 | 7.35% |
| 5 | 0-0 | 7.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 31.5% | 28.7% | 3.45 | +8.8% |
| Draw | 27.6% | 28.4% | 3.50 | -3.6% |
| Paris FC win | 40.9% | 42.9% | 2.36 | -3.5% |
| Over 2.5 | 51.9% | 49.3% | 2.03 | +5.4% |
| Under 2.5 | 48.1% | 50.7% | 1.92 | -7.6% |

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
| Market best home last update utc | 2026-10-09T07:42:08Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Coolbet |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lorient |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.98 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.33 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.86 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 34.4% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 76.9% |
| Raw p under 3 5 | 70.0% |
| Raw p btts yes | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.35 |
| Reference draw odds | 3.38 |
| Reference away odds | 2.27 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.92 |
| Home probability edge | +2.8% |
| Draw probability edge | -0.9% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +2.6% |
| Under 2.5 probability edge | -2.6% |
| Raw edge prob home | 0.0570 |
| Raw ev home | 0.1863 |
| Raw edge prob draw | -0.0175 |
| Raw ev draw | -0.0662 |
| Raw edge prob away | -0.0395 |
| Raw ev away | -0.0812 |

</details>


---

## 2026-10-10 — Paris Saint Germain vs Le Mans FC

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **84.5%**. Expected goals are 3.17 for Paris Saint Germain and 1.12 for Le Mans FC (4.29 combined). The most likely exact score is 3-1 at 8.9%. Goal-market probabilities: at least one goal: 98.9%; Over 2.5 goals: 81.8%; Under 4.5 goals: 55.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 84.5% | 1.18 |
| Draw | 9.3% | 10.81 |
| Le Mans FC win | 6.3% | 15.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 3.17 |
| Le Mans FC expected goals | 1.12 |
| Expected total goals | 4.29 |
| Over 0.5 | 98.9% |
| Under 0.5 | 1.1% |
| Over 1.5 | 93.5% |
| Under 1.5 | 6.5% |
| Over 2.5 | 81.8% |
| Under 2.5 | 18.2% |
| Over 3.5 | 63.4% |
| Under 3.5 | 36.6% |
| Over 4.5 | 44.4% |
| Under 4.5 | 55.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 8.93% |
| 2 | 2-1 | 8.45% |
| 3 | 3-0 | 7.99% |
| 4 | 2-0 | 7.56% |
| 5 | 4-1 | 7.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 84.5% | 91.8% | 1.10 | -7.1% |
| Draw | 9.3% | 5.3% | 16.50 | +52.7% |
| Le Mans FC win | 6.3% | 2.9% | 34.00 | +113.0% |
| Over 2.5 | 81.8% | 81.7% | 1.22 | -0.2% |
| Under 2.5 | 18.2% | 18.3% | 4.60 | -16.3% |

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
| Market best home last update utc | 2026-10-09T07:41:37Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Paris SG |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 87.57 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.43 |
| Fair Over 2.5 odds | 1.22 |
| Fair Under 2.5 odds | 5.49 |
| Fair Over 3.5 odds | 1.58 |
| Fair Under 3.5 odds | 2.73 |
| Fair Over 4.5 odds | 2.25 |
| Fair Under 4.5 odds | 1.80 |
| Unadjusted home-win probability | 77.2% |
| Unadjusted draw probability | 13.2% |
| Unadjusted away-win probability | 9.6% |
| Raw p over 1 5 | 93.0% |
| Raw p under 3 5 | 38.0% |
| Raw p btts yes | 64.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.08 |
| Reference draw odds | 13.87 |
| Reference away odds | 23.43 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.60 |
| Home probability edge | -7.3% |
| Draw probability edge | +4.0% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.1456 |
| Raw ev home | -0.1508 |
| Raw edge prob draw | 0.0792 |
| Raw ev draw | 1.1798 |
| Raw edge prob away | 0.0664 |
| Raw ev away | 2.2589 |

</details>


---

## 2026-10-11 — Nice vs Strasbourg

The model's most likely 1X2 outcome is **Nice win** at **39.9%**. Expected goals are 1.46 for Nice and 1.39 for Strasbourg (2.84 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.1%; Under 4.5 goals: 84.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nice win | 39.9% | 2.51 |
| Draw | 26.1% | 3.83 |
| Strasbourg win | 34.0% | 2.95 |

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
| 1 | 1-1 | 12.32% |
| 2 | 2-1 | 8.90% |
| 3 | 1-0 | 8.18% |
| 4 | 1-2 | 7.84% |
| 5 | 0-1 | 7.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nice win | 39.9% | 41.4% | 2.48 | -1.0% |
| Draw | 26.1% | 26.0% | 3.75 | -2.0% |
| Strasbourg win | 34.0% | 32.5% | 3.10 | +5.3% |
| Over 2.5 | 54.1% | 57.8% | 1.77 | -4.2% |
| Under 2.5 | 45.9% | 42.2% | 2.22 | +1.8% |

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
| Market best home last update utc | 2026-10-09T07:41:37Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:08Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nice |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.62 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.60 |
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
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.35 |
| Reference draw odds | 3.69 |
| Reference away odds | 2.97 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | -1.5% |
| Draw probability edge | +0.1% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | -0.0306 |
| Raw ev home | -0.0483 |
| Raw edge prob draw | 0.0024 |
| Raw ev draw | -0.0152 |
| Raw edge prob away | 0.0282 |
| Raw ev away | 0.0963 |

</details>


---

## 2026-10-11 — Rennes vs Auxerre

The model's most likely 1X2 outcome is **Rennes win** at **60.7%**. Expected goals are 1.84 for Rennes and 1.14 for Auxerre (2.98 combined). The most likely exact score is 2-1 at 11.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 58.6%; Under 4.5 goals: 81.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 60.7% | 1.65 |
| Draw | 20.9% | 4.77 |
| Auxerre win | 18.4% | 5.44 |

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
| Over 2.5 | 58.6% |
| Under 2.5 | 41.4% |
| Over 3.5 | 35.6% |
| Under 3.5 | 64.4% |
| Over 4.5 | 18.9% |
| Under 4.5 | 81.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.20% |
| 2 | 1-0 | 10.01% |
| 3 | 1-1 | 9.81% |
| 4 | 2-0 | 9.79% |
| 5 | 3-1 | 6.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 60.7% | 68.3% | 1.48 | -10.2% |
| Draw | 20.9% | 18.0% | 5.20 | +8.9% |
| Auxerre win | 18.4% | 13.8% | 7.50 | +37.8% |
| Over 2.5 | 58.6% | 63.8% | 1.51 | -11.5% |
| Under 2.5 | 41.4% | 36.2% | 2.61 | +8.0% |

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
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:42:37Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
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
| P btts yes | 56.9% |
| P btts no | 43.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.34 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.23 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.30 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 53.1% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 80.4% |
| Raw p under 3 5 | 65.1% |
| Raw p btts yes | 57.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.44 |
| Reference draw odds | 5.15 |
| Reference away odds | 6.65 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -7.6% |
| Draw probability edge | +3.0% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.1518 |
| Raw ev home | -0.2143 |
| Raw edge prob draw | 0.0594 |
| Raw ev draw | 0.2438 |
| Raw edge prob away | 0.0924 |
| Raw ev away | 0.7245 |

</details>


---

## 2026-10-11 — Troyes vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **62.4%**. Expected goals are 0.92 for Troyes and 2.68 for Marseille (3.60 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 67.2%; Under 4.5 goals: 72.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 17.7% | 5.66 |
| Draw | 19.9% | 5.03 |
| Marseille win | 62.4% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.92 |
| Marseille expected goals | 2.68 |
| Expected total goals | 3.60 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 86.5% |
| Under 1.5 | 13.5% |
| Over 2.5 | 67.2% |
| Under 2.5 | 32.8% |
| Over 3.5 | 46.2% |
| Under 3.5 | 53.8% |
| Over 4.5 | 27.4% |
| Under 4.5 | 72.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.00% |
| 2 | 0-2 | 8.24% |
| 3 | 1-2 | 7.60% |
| 4 | 0-3 | 7.36% |
| 5 | 1-3 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 17.7% | 25.2% | 4.03 | -28.7% |
| Draw | 19.9% | 24.1% | 4.05 | -19.4% |
| Marseille win | 62.4% | 50.6% | 2.02 | +26.1% |
| Over 2.5 | 67.2% | 61.8% | 1.65 | +10.9% |
| Under 2.5 | 32.8% | 38.2% | 2.45 | -19.6% |

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
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:08Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.6% |
| P btts no | 41.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.60 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.38 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.05 |
| Fair Over 3.5 odds | 2.17 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.65 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 15.7% |
| Unadjusted away-win probability | 74.2% |
| Raw p over 1 5 | 87.8% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 56.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.78 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.93 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -7.6% |
| Draw probability edge | -4.2% |
| Away probability edge | +11.8% |
| Over 2.5 probability edge | +5.4% |
| Under 2.5 probability edge | -5.4% |
| Raw edge prob home | -0.1513 |
| Raw ev home | -0.5922 |
| Raw edge prob draw | -0.0845 |
| Raw ev draw | -0.3653 |
| Raw edge prob away | 0.2358 |
| Raw ev away | 0.4990 |

</details>


---

## 2026-10-16 — Le Mans FC vs Toulouse

The model's most likely 1X2 outcome is **Le Mans FC win** at **38.1%**. Expected goals are 1.87 for Le Mans FC and 1.51 for Toulouse (3.37 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 64.7%; Under 4.5 goals: 75.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 38.1% | 2.63 |
| Draw | 25.4% | 3.94 |
| Toulouse win | 36.5% | 2.74 |

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
| 1 | 1-1 | 11.02% |
| 2 | 1-2 | 8.60% |
| 3 | 2-1 | 7.48% |
| 4 | 2-2 | 7.36% |
| 5 | 0-1 | 5.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 38.1% | 30.4% | 3.30 | +25.6% |
| Draw | 25.4% | 27.4% | 3.57 | -9.3% |
| Toulouse win | 36.5% | 42.2% | 2.34 | -14.5% |
| Over 2.5 | 64.7% | 55.8% | 1.84 | +19.0% |
| Under 2.5 | 35.3% | 44.2% | 2.12 | -25.1% |

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
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
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
| Fair Under 0.5 odds | 23.41 |
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
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.12 |
| Reference draw odds | 3.44 |
| Reference away odds | 2.28 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | +7.7% |
| Draw probability edge | -2.0% |
| Away probability edge | -5.7% |
| Over 2.5 probability edge | +8.9% |
| Under 2.5 probability edge | -8.9% |
| Raw edge prob home | 0.1537 |
| Raw ev home | 0.5097 |
| Raw edge prob draw | -0.0404 |
| Raw ev draw | -0.1651 |
| Raw edge prob away | -0.1133 |
| Raw ev away | -0.2778 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **58.8%**. Expected goals are 1.76 for Lille and 0.94 for Brest (2.70 combined). The most likely exact score is 1-0 at 11.8%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 51.3%; Under 4.5 goals: 86.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 58.8% | 1.70 |
| Draw | 23.2% | 4.32 |
| Brest win | 18.0% | 5.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.76 |
| Brest expected goals | 0.94 |
| Expected total goals | 2.70 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 51.3% |
| Under 2.5 | 48.7% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.79% |
| 2 | 1-1 | 11.04% |
| 3 | 2-0 | 10.90% |
| 4 | 2-1 | 10.27% |
| 5 | 0-0 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 58.8% | 61.6% | 1.66 | -2.4% |
| Draw | 23.2% | 21.8% | 4.37 | +1.2% |
| Brest win | 18.0% | 16.7% | 5.42 | -2.2% |
| Over 2.5 | 51.3% | 57.8% | 1.74 | -10.8% |
| Under 2.5 | 48.7% | 42.2% | 2.27 | +10.6% |

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
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:41Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.53 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.16 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.15 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 56.0% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 19.4% |
| Raw p over 1 5 | 75.7% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 51.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.58 |
| Reference draw odds | 4.21 |
| Reference away odds | 5.42 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | -2.8% |
| Draw probability edge | +1.4% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.0555 |
| Raw ev home | -0.0702 |
| Raw edge prob draw | 0.0277 |
| Raw ev draw | 0.0728 |
| Raw edge prob away | 0.0278 |
| Raw ev away | 0.0535 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **63.6%**. Expected goals are 1.23 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.9%; Under 4.5 goals: 75.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.4% | 5.73 |
| Draw | 19.0% | 5.27 |
| Paris Saint Germain win | 63.6% | 1.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.23 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 65.9% |
| Under 2.5 | 34.1% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.84% |
| 2 | 0-2 | 8.83% |
| 3 | 1-1 | 8.47% |
| 4 | 0-1 | 7.87% |
| 5 | 1-3 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.4% | 13.6% | 6.75 | +17.7% |
| Draw | 19.0% | 16.2% | 5.70 | +8.1% |
| Paris Saint Germain win | 63.6% | 70.2% | 1.46 | -7.2% |
| Over 2.5 | 65.9% | 73.1% | 1.33 | -12.4% |
| Under 2.5 | 34.1% | 26.9% | 3.42 | +16.8% |

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
| Market best home last update utc | 2026-10-09T07:41:37Z |
| Market best draw last update utc | 2026-10-09T07:42:37Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Tipico |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Strasbourg |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.6% |
| P btts no | 38.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.24 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.84 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 3.99 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 57.0% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.4% |
| Raw p btts yes | 62.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.41 |
| Reference draw odds | 5.46 |
| Reference away odds | 1.39 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Home probability edge | +3.8% |
| Draw probability edge | +2.8% |
| Away probability edge | -6.6% |
| Over 2.5 probability edge | -7.2% |
| Under 2.5 probability edge | +7.2% |
| Raw edge prob home | 0.0767 |
| Raw ev home | 0.4363 |
| Raw edge prob draw | 0.0559 |
| Raw ev draw | 0.2402 |
| Raw edge prob away | -0.1326 |
| Raw ev away | -0.1683 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **62.4%**. Expected goals are 0.78 for Troyes and 2.31 for RC Lens (3.09 combined). The most likely exact score is 0-2 at 10.6%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.9%; Under 4.5 goals: 81.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 16.9% | 5.92 |
| Draw | 20.7% | 4.83 |
| RC Lens win | 62.4% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.78 |
| RC Lens expected goals | 2.31 |
| Expected total goals | 3.09 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.9% |
| Under 2.5 | 42.1% |
| Over 3.5 | 35.7% |
| Under 3.5 | 64.3% |
| Over 4.5 | 18.9% |
| Under 4.5 | 81.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 10.60% |
| 2 | 1-1 | 9.86% |
| 3 | 0-1 | 8.81% |
| 4 | 1-2 | 8.29% |
| 5 | 0-3 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 16.9% | 23.2% | 4.30 | -27.4% |
| Draw | 20.7% | 23.3% | 4.04 | -16.3% |
| RC Lens win | 62.4% | 53.5% | 1.87 | +16.7% |
| Over 2.5 | 57.9% | 61.8% | 1.64 | -5.1% |
| Under 2.5 | 42.1% | 38.2% | 2.48 | +4.5% |

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
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Unibet (SE) |
| Matched home-team name | Troyes |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.63 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.14 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.80 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.29 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 10.6% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 71.3% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 49.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.00 |
| Reference draw odds | 3.98 |
| Reference away odds | 1.81 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -6.3% |
| Draw probability edge | -2.6% |
| Away probability edge | +8.9% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.1261 |
| Raw ev home | -0.5449 |
| Raw edge prob draw | -0.0517 |
| Raw ev draw | -0.2672 |
| Raw edge prob away | 0.1778 |
| Raw ev away | 0.3329 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **49.4%**. Expected goals are 0.95 for Angers and 1.65 for Marseille (2.59 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 47.9%; Under 4.5 goals: 87.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 25.2% | 3.96 |
| Draw | 25.4% | 3.94 |
| Marseille win | 49.4% | 2.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.95 |
| Marseille expected goals | 1.65 |
| Expected total goals | 2.59 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 73.4% |
| Under 1.5 | 26.6% |
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.10% |
| 2 | 0-1 | 10.85% |
| 3 | 0-2 | 9.40% |
| 4 | 1-2 | 8.90% |
| 5 | 0-0 | 7.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 25.2% | 29.4% | 3.30 | -16.7% |
| Draw | 25.4% | 25.1% | 3.85 | -2.2% |
| Marseille win | 49.4% | 45.5% | 2.28 | +12.5% |
| Over 2.5 | 47.9% | 60.9% | 1.68 | -19.5% |
| Under 2.5 | 52.1% | 39.1% | 2.40 | +25.0% |

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
| Market best home last update utc | 2026-10-09T07:42:37Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Unibet (SE) |
| Matched home-team name | Angers |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.55 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.76 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.29 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 53.2% |
| Raw p over 1 5 | 73.8% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 50.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.21 |
| Reference draw odds | 3.74 |
| Reference away odds | 2.12 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | -4.2% |
| Draw probability edge | +0.3% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | -13.0% |
| Under 2.5 probability edge | +13.0% |
| Raw edge prob home | -0.0842 |
| Raw ev home | -0.3064 |
| Raw edge prob draw | 0.0066 |
| Raw ev draw | -0.0091 |
| Raw edge prob away | 0.0776 |
| Raw ev away | 0.2140 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **37.0%**. Expected goals are 1.16 for Le Havre and 1.19 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.8%; Under 4.5 goals: 91.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 37.0% | 2.71 |
| Draw | 28.6% | 3.50 |
| Auxerre win | 34.5% | 2.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.16 |
| Auxerre expected goals | 1.19 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 68.6% |
| Under 1.5 | 31.4% |
| Over 2.5 | 41.8% |
| Under 2.5 | 58.2% |
| Over 3.5 | 21.0% |
| Under 3.5 | 79.0% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.47% |
| 2 | 1-0 | 11.15% |
| 3 | 0-1 | 10.23% |
| 4 | 0-0 | 9.98% |
| 5 | 2-1 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 37.0% | 39.5% | 2.52 | -6.9% |
| Draw | 28.6% | 27.8% | 3.51 | +0.3% |
| Auxerre win | 34.5% | 32.8% | 3.00 | +3.4% |
| Over 2.5 | 41.8% | 51.1% | 1.94 | -18.8% |
| Under 2.5 | 58.2% | 48.9% | 2.00 | +16.3% |

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
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Havre |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.02 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.39 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.76 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.14 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.0% |
| Raw p btts yes | 48.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.43 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | -2.5% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.0501 |
| Raw ev home | -0.1318 |
| Raw edge prob draw | 0.0165 |
| Raw ev draw | 0.0322 |
| Raw edge prob away | 0.0335 |
| Raw ev away | 0.0843 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **46.6%**. Expected goals are 1.36 for Lorient and 1.84 for AS Monaco (3.21 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.5%; Under 4.5 goals: 78.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 27.8% | 3.60 |
| Draw | 25.6% | 3.90 |
| AS Monaco win | 46.6% | 2.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.36 |
| AS Monaco expected goals | 1.84 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 39.7% |
| Under 3.5 | 60.3% |
| Over 4.5 | 21.7% |
| Under 4.5 | 78.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.54% |
| 2 | 1-2 | 9.04% |
| 3 | 2-1 | 6.90% |
| 4 | 2-2 | 6.88% |
| 5 | 0-1 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 27.8% | 27.7% | 3.75 | +4.2% |
| Draw | 25.6% | 27.5% | 3.58 | -8.3% |
| AS Monaco win | 46.6% | 44.8% | 2.17 | +1.1% |
| Over 2.5 | 61.5% | 51.8% | 1.92 | +18.0% |
| Under 2.5 | 38.5% | 48.2% | 2.02 | -22.2% |

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
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
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
| P btts yes | 63.6% |
| P btts no | 36.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.25 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.02 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.52 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.61 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 27.9% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 83.5% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 63.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.40 |
| Reference draw odds | 3.43 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.98 |
| Home probability edge | +0.1% |
| Draw probability edge | -1.9% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | +9.6% |
| Under 2.5 probability edge | -9.6% |
| Raw edge prob home | 0.0015 |
| Raw ev home | 0.0450 |
| Raw edge prob draw | -0.0370 |
| Raw ev draw | -0.1494 |
| Raw edge prob away | 0.0356 |
| Raw ev away | 0.0497 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **56.2%**. Expected goals are 1.78 for Lyon and 1.08 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 55.0%; Under 4.5 goals: 83.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 56.2% | 1.78 |
| Draw | 23.3% | 4.29 |
| Nice win | 20.5% | 4.87 |

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
| 1 | 1-1 | 11.05% |
| 2 | 2-1 | 10.35% |
| 3 | 1-0 | 10.17% |
| 4 | 2-0 | 9.58% |
| 5 | 3-1 | 6.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 56.2% | 59.2% | 1.71 | -4.0% |
| Draw | 23.3% | 22.2% | 4.20 | -2.1% |
| Nice win | 20.5% | 18.6% | 5.24 | +7.5% |
| Over 2.5 | 55.0% | 58.9% | 1.78 | -2.1% |
| Under 2.5 | 45.0% | 41.1% | 2.25 | +1.3% |

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
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:42:37Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 15.00 |
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
| Fair Under 0.5 odds | 16.65 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.69 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.09 |
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
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.64 |
| Reference draw odds | 4.14 |
| Reference away odds | 4.88 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -3.0% |
| Draw probability edge | +1.1% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0604 |
| Raw ev home | -0.0912 |
| Raw edge prob draw | 0.0228 |
| Raw ev draw | 0.0272 |
| Raw edge prob away | 0.0377 |
| Raw ev away | 0.1736 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **42.1%**. Expected goals are 1.62 for Paris FC and 1.36 for Rennes (2.98 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 56.5%; Under 4.5 goals: 82.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 42.1% | 2.38 |
| Draw | 27.3% | 3.66 |
| Rennes win | 30.6% | 3.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.62 |
| Rennes expected goals | 1.36 |
| Expected total goals | 2.98 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 80.2% |
| Under 1.5 | 19.8% |
| Over 2.5 | 56.5% |
| Under 2.5 | 43.5% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 17.8% |
| Under 4.5 | 82.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.71% |
| 2 | 2-1 | 8.84% |
| 3 | 1-0 | 7.48% |
| 4 | 1-2 | 7.38% |
| 5 | 2-2 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 42.1% | 40.9% | 2.37 | -0.3% |
| Draw | 27.3% | 29.3% | 3.60 | -1.6% |
| Rennes win | 30.6% | 29.7% | 3.29 | +0.7% |
| Over 2.5 | 56.5% | 58.9% | 1.72 | -2.9% |
| Under 2.5 | 43.5% | 41.1% | 2.30 | +0.1% |

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
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
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
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.33 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.06 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.62 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 31.5% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 60.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.35 |
| Reference draw odds | 3.23 |
| Reference away odds | 3.19 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | +1.1% |
| Draw probability edge | -2.0% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | 0.0226 |
| Raw ev home | 0.0234 |
| Raw edge prob draw | -0.0401 |
| Raw ev draw | -0.0880 |
| Raw edge prob away | 0.0175 |
| Raw ev away | 0.0359 |

</details>


---
