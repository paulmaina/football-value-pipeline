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

The model's most likely 1X2 outcome is **RC Lens win** at **42.5%**. Expected goals are 1.57 for RC Lens and 1.23 for Lyon (2.80 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 53.0%; Under 4.5 goals: 84.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 42.5% | 2.35 |
| Draw | 26.2% | 3.82 |
| Lyon win | 31.3% | 3.19 |

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
| 1 | 1-1 | 12.39% |
| 2 | 2-1 | 8.77% |
| 3 | 1-0 | 8.51% |
| 4 | 1-2 | 7.74% |
| 5 | 0-1 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 42.5% | 40.3% | 2.48 | +5.4% |
| Draw | 26.2% | 26.3% | 3.85 | +0.7% |
| Lyon win | 31.3% | 33.5% | 2.98 | -6.6% |
| Over 2.5 | 53.0% | 63.9% | 1.53 | -19.0% |
| Under 2.5 | 47.0% | 36.1% | 2.56 | +20.4% |

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
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Lens |
| Matched away-team name | Lyon |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.89 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.43 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.26 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.59 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 44.7% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 29.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.48 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.98 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.52 |
| Home probability edge | +2.2% |
| Draw probability edge | -0.1% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0447 |
| Raw ev home | 0.1093 |
| Raw edge prob draw | -0.0017 |
| Raw ev draw | 0.0040 |
| Raw edge prob away | -0.0430 |
| Raw ev away | -0.1301 |

</details>


---

## 2026-10-10 — AS Monaco vs Toulouse

The model's most likely 1X2 outcome is **AS Monaco win** at **58.5%**. Expected goals are 1.95 for AS Monaco and 1.13 for Toulouse (3.07 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 59.7%; Under 4.5 goals: 80.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 58.5% | 1.71 |
| Draw | 22.2% | 4.51 |
| Toulouse win | 19.3% | 5.17 |

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
| Over 4.5 | 19.9% |
| Under 4.5 | 80.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.33% |
| 2 | 1-1 | 10.31% |
| 3 | 2-0 | 9.17% |
| 4 | 1-0 | 8.87% |
| 5 | 3-1 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 58.5% | 61.0% | 1.65 | -3.5% |
| Draw | 22.2% | 21.4% | 4.60 | +2.0% |
| Toulouse win | 19.3% | 17.5% | 5.60 | +8.2% |
| Over 2.5 | 59.7% | 61.6% | 1.65 | -1.5% |
| Under 2.5 | 40.3% | 38.4% | 2.45 | -1.2% |

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
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.08 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.51 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.48 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.01 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 56.0% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 21.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.63 |
| Reference draw odds | 4.60 |
| Reference away odds | 5.60 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -2.5% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | -0.0509 |
| Raw ev home | -0.0768 |
| Raw edge prob draw | 0.0153 |
| Raw ev draw | 0.0551 |
| Raw edge prob away | 0.0356 |
| Raw ev away | 0.1820 |

</details>


---

## 2026-10-10 — Brest vs Angers

The model's most likely 1X2 outcome is **Brest win** at **50.2%**. Expected goals are 1.56 for Brest and 0.88 for Angers (2.44 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 43.9%; Under 4.5 goals: 90.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 50.2% | 1.99 |
| Draw | 26.4% | 3.79 |
| Angers win | 23.3% | 4.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Angers expected goals | 0.88 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 70.3% |
| Under 1.5 | 29.7% |
| Over 2.5 | 43.9% |
| Under 2.5 | 56.1% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.44% |
| 2 | 1-0 | 12.41% |
| 3 | 2-0 | 10.12% |
| 4 | 0-0 | 9.25% |
| 5 | 2-1 | 8.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 50.2% | 47.8% | 2.08 | +4.5% |
| Draw | 26.4% | 26.1% | 3.85 | +1.7% |
| Angers win | 23.3% | 26.1% | 3.85 | -10.1% |
| Over 2.5 | 43.9% | 55.2% | 1.83 | -19.6% |
| Under 2.5 | 56.1% | 44.8% | 2.15 | +20.5% |

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
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.81 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.37 |
| Fair Over 2.5 odds | 2.28 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.00 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 52.6% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 20.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.08 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.80 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | +2.4% |
| Draw probability edge | +0.3% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | 0.0481 |
| Raw ev home | 0.0950 |
| Raw edge prob draw | 0.0066 |
| Raw ev draw | 0.0295 |
| Raw edge prob away | -0.0547 |
| Raw ev away | -0.2064 |

</details>


---

## 2026-10-10 — Lille vs Le Havre

The model's most likely 1X2 outcome is **Lille win** at **65.6%**. Expected goals are 1.77 for Lille and 0.68 for Le Havre (2.45 combined). The most likely exact score is 1-0 at 15.3%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 45.2%; Under 4.5 goals: 89.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 65.6% | 1.53 |
| Draw | 21.6% | 4.63 |
| Le Havre win | 12.8% | 7.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.77 |
| Le Havre expected goals | 0.68 |
| Expected total goals | 2.45 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.35% |
| 2 | 2-0 | 14.07% |
| 3 | 1-1 | 9.96% |
| 4 | 2-1 | 9.56% |
| 5 | 0-0 | 8.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 65.6% | 68.1% | 1.48 | -3.0% |
| Draw | 21.6% | 19.5% | 5.00 | +8.0% |
| Le Havre win | 12.8% | 12.4% | 7.80 | +0.2% |
| Over 2.5 | 45.2% | 58.6% | 1.72 | -22.3% |
| Under 2.5 | 54.8% | 41.4% | 2.35 | +28.9% |

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
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.94 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.46 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.26 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.55 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 63.0% |
| Unadjusted draw probability | 23.7% |
| Unadjusted away-win probability | 13.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.46 |
| Reference draw odds | 5.00 |
| Reference away odds | 7.80 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.22 |
| Home probability edge | -2.5% |
| Draw probability edge | +2.1% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -13.5% |
| Under 2.5 probability edge | +13.5% |
| Raw edge prob home | -0.0505 |
| Raw ev home | -0.0671 |
| Raw edge prob draw | 0.0418 |
| Raw ev draw | 0.1840 |
| Raw edge prob away | 0.0087 |
| Raw ev away | 0.0363 |

</details>


---

## 2026-10-10 — Lorient vs Paris FC

The model's most likely 1X2 outcome is **Paris FC win** at **40.8%**. Expected goals are 1.33 for Lorient and 1.43 for Paris FC (2.76 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 51.9%; Under 4.5 goals: 85.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 31.5% | 3.17 |
| Draw | 27.7% | 3.62 |
| Paris FC win | 40.8% | 2.45 |

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
| 1 | 1-1 | 13.11% |
| 2 | 1-2 | 9.03% |
| 3 | 0-1 | 8.82% |
| 4 | 2-1 | 7.34% |
| 5 | 0-0 | 7.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 31.5% | 28.6% | 3.45 | +8.7% |
| Draw | 27.7% | 28.6% | 3.50 | -3.2% |
| Paris FC win | 40.8% | 42.7% | 2.36 | -3.6% |
| Over 2.5 | 51.9% | 49.3% | 2.03 | +5.3% |
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
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.93 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.32 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.34 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.87 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 34.4% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 38.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.45 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.32 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | +2.9% |
| Draw probability edge | -1.0% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +2.6% |
| Under 2.5 probability edge | -2.6% |
| Raw edge prob home | 0.0576 |
| Raw ev home | 0.1863 |
| Raw edge prob draw | -0.0195 |
| Raw ev draw | -0.0662 |
| Raw edge prob away | -0.0381 |
| Raw ev away | -0.0812 |

</details>


---

## 2026-10-10 — Paris Saint Germain vs Le Mans FC

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **83.9%**. Expected goals are 3.17 for Paris Saint Germain and 1.12 for Le Mans FC (4.29 combined). The most likely exact score is 3-1 at 8.9%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 81.6%; Under 4.5 goals: 55.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 83.9% | 1.19 |
| Draw | 9.8% | 10.22 |
| Le Mans FC win | 6.3% | 15.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 3.17 |
| Le Mans FC expected goals | 1.12 |
| Expected total goals | 4.29 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 93.5% |
| Under 1.5 | 6.5% |
| Over 2.5 | 81.6% |
| Under 2.5 | 18.4% |
| Over 3.5 | 63.3% |
| Under 3.5 | 36.7% |
| Over 4.5 | 44.2% |
| Under 4.5 | 55.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 8.87% |
| 2 | 2-1 | 8.40% |
| 3 | 3-0 | 7.93% |
| 4 | 2-0 | 7.51% |
| 5 | 4-1 | 7.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 83.9% | 90.6% | 1.10 | -7.7% |
| Draw | 9.8% | 6.4% | 16.50 | +61.4% |
| Le Mans FC win | 6.3% | 3.0% | 34.00 | +114.0% |
| Over 2.5 | 81.6% | 80.6% | 1.22 | -0.4% |
| Under 2.5 | 18.4% | 19.4% | 4.60 | -15.4% |

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
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 82.83 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.33 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.43 |
| Fair Over 3.5 odds | 1.58 |
| Fair Under 3.5 odds | 2.72 |
| Fair Over 4.5 odds | 2.26 |
| Fair Under 4.5 odds | 1.79 |
| Unadjusted home-win probability | 77.2% |
| Unadjusted draw probability | 13.2% |
| Unadjusted away-win probability | 9.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.10 |
| Reference draw odds | 14.50 |
| Reference away odds | 30.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.21 |
| Reference Under 2.5 odds | 4.25 |
| Home probability edge | -6.7% |
| Draw probability edge | +3.4% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | -0.1344 |
| Raw ev home | -0.1508 |
| Raw edge prob draw | 0.0686 |
| Raw ev draw | 1.1798 |
| Raw edge prob away | 0.0658 |
| Raw ev away | 2.2589 |

</details>


---

## 2026-10-11 — Nice vs Strasbourg

The model's most likely 1X2 outcome is **Nice win** at **39.9%**. Expected goals are 1.46 for Nice and 1.39 for Strasbourg (2.84 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 54.0%; Under 4.5 goals: 84.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nice win | 39.9% | 2.50 |
| Draw | 26.4% | 3.79 |
| Strasbourg win | 33.7% | 2.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nice expected goals | 1.46 |
| Strasbourg expected goals | 1.39 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.0% |
| Under 2.5 | 46.0% |
| Over 3.5 | 31.8% |
| Under 3.5 | 68.2% |
| Over 4.5 | 15.9% |
| Under 4.5 | 84.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.42% |
| 2 | 2-1 | 8.90% |
| 3 | 1-0 | 8.18% |
| 4 | 1-2 | 7.78% |
| 5 | 0-1 | 7.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nice win | 39.9% | 41.5% | 2.48 | -1.0% |
| Draw | 26.4% | 26.5% | 3.75 | -1.1% |
| Strasbourg win | 33.7% | 32.1% | 3.10 | +4.5% |
| Over 2.5 | 54.0% | 56.4% | 1.77 | -4.3% |
| Under 2.5 | 46.0% | 43.6% | 2.22 | +2.0% |

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
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.48 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.59 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.29 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 38.4% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 35.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.40 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -1.5% |
| Draw probability edge | -0.1% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | -0.0309 |
| Raw ev home | -0.0483 |
| Raw edge prob draw | -0.0021 |
| Raw ev draw | -0.0152 |
| Raw edge prob away | 0.0331 |
| Raw ev away | 0.0963 |

</details>


---

## 2026-10-11 — Rennes vs Auxerre

The model's most likely 1X2 outcome is **Rennes win** at **60.6%**. Expected goals are 1.84 for Rennes and 1.14 for Auxerre (2.98 combined). The most likely exact score is 2-1 at 11.2%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 58.5%; Under 4.5 goals: 81.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 60.6% | 1.65 |
| Draw | 21.3% | 4.69 |
| Auxerre win | 18.0% | 5.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.84 |
| Auxerre expected goals | 1.14 |
| Expected total goals | 2.98 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 58.5% |
| Under 2.5 | 41.5% |
| Over 3.5 | 35.5% |
| Under 3.5 | 64.5% |
| Over 4.5 | 18.8% |
| Under 4.5 | 81.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.19% |
| 2 | 1-0 | 10.01% |
| 3 | 1-1 | 9.98% |
| 4 | 2-0 | 9.78% |
| 5 | 3-1 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 60.6% | 68.2% | 1.48 | -10.2% |
| Draw | 21.3% | 18.7% | 5.20 | +10.8% |
| Auxerre win | 18.0% | 13.1% | 7.50 | +35.4% |
| Over 2.5 | 58.5% | 64.6% | 1.51 | -11.6% |
| Under 2.5 | 41.5% | 35.4% | 2.61 | +8.3% |

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
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.00 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.23 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.31 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 53.1% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 23.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.45 |
| Reference draw odds | 5.10 |
| Reference away odds | 7.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Home probability edge | -7.6% |
| Draw probability edge | +2.6% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.1512 |
| Raw ev home | -0.2143 |
| Raw edge prob draw | 0.0523 |
| Raw ev draw | 0.2438 |
| Raw edge prob away | 0.0989 |
| Raw ev away | 0.7245 |

</details>


---

## 2026-10-11 — Troyes vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **61.9%**. Expected goals are 0.92 for Troyes and 2.68 for Marseille (3.60 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 67.0%; Under 4.5 goals: 72.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 17.8% | 5.61 |
| Draw | 20.3% | 4.93 |
| Marseille win | 61.9% | 1.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.92 |
| Marseille expected goals | 2.68 |
| Expected total goals | 3.60 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 86.4% |
| Under 1.5 | 13.6% |
| Over 2.5 | 67.0% |
| Under 2.5 | 33.0% |
| Over 3.5 | 46.1% |
| Under 3.5 | 53.9% |
| Over 4.5 | 27.2% |
| Under 4.5 | 72.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.17% |
| 2 | 0-2 | 8.17% |
| 3 | 1-2 | 7.53% |
| 4 | 0-3 | 7.29% |
| 5 | 1-3 | 6.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 17.8% | 25.5% | 4.03 | -28.1% |
| Draw | 20.3% | 24.9% | 4.05 | -17.9% |
| Marseille win | 61.9% | 49.6% | 2.00 | +23.8% |
| Over 2.5 | 67.0% | 61.6% | 1.65 | +10.6% |
| Under 2.5 | 33.0% | 38.4% | 2.45 | -19.2% |

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
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.12 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.35 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.03 |
| Fair Over 3.5 odds | 2.17 |
| Fair Under 3.5 odds | 1.85 |
| Fair Over 4.5 odds | 3.67 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 15.7% |
| Unadjusted away-win probability | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.85 |
| Reference draw odds | 3.95 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -7.7% |
| Draw probability edge | -4.6% |
| Away probability edge | +12.3% |
| Over 2.5 probability edge | +5.4% |
| Under 2.5 probability edge | -5.4% |
| Raw edge prob home | -0.1542 |
| Raw ev home | -0.5922 |
| Raw edge prob draw | -0.0922 |
| Raw ev draw | -0.3653 |
| Raw edge prob away | 0.2464 |
| Raw ev away | 0.4842 |

</details>


---

## 2026-10-16 — Le Mans FC vs Toulouse

The model's most likely 1X2 outcome is **Le Mans FC win** at **36.2%**. Expected goals are 1.87 for Le Mans FC and 1.51 for Toulouse (3.37 combined). The most likely exact score is 1-1 at 15.2%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 61.5%; Under 4.5 goals: 77.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 36.2% | 2.76 |
| Draw | 35.0% | 2.85 |
| Toulouse win | 28.8% | 3.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Mans FC expected goals | 1.87 |
| Toulouse expected goals | 1.51 |
| Expected total goals | 3.37 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 42.9% |
| Under 3.5 | 57.1% |
| Over 4.5 | 22.8% |
| Under 4.5 | 77.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 15.20% |
| 2 | 2-2 | 10.15% |
| 3 | 2-1 | 7.12% |
| 4 | 1-2 | 6.77% |
| 5 | 0-0 | 5.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 36.2% | 26.7% | 3.30 | +19.5% |
| Draw | 35.0% | 46.7% | 3.57 | +25.1% |
| Toulouse win | 28.8% | 26.7% | 2.34 | -32.7% |
| Over 2.5 | 61.5% | 55.2% | 1.84 | +13.2% |
| Under 2.5 | 38.5% | 44.8% | 2.12 | -18.4% |

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
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.98 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.71 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.38 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 45.7% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 30.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.18 |
| Reference draw odds | 1.10 |
| Reference away odds | 1.18 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | +9.5% |
| Draw probability edge | -11.7% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +6.3% |
| Under 2.5 probability edge | -6.3% |
| Raw edge prob home | 0.1910 |
| Raw ev home | 0.5097 |
| Raw edge prob draw | -0.2331 |
| Raw ev draw | -0.1651 |
| Raw edge prob away | 0.0421 |
| Raw ev away | -0.2778 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **52.6%**. Expected goals are 1.76 for Lille and 0.94 for Brest (2.70 combined). The most likely exact score is 1-0 at 10.5%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 54.1%; Under 4.5 goals: 85.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 52.6% | 1.90 |
| Draw | 13.2% | 7.60 |
| Brest win | 34.3% | 2.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.76 |
| Brest expected goals | 0.94 |
| Expected total goals | 2.70 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 28.3% |
| Under 3.5 | 71.7% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 10.54% |
| 2 | 0-1 | 10.14% |
| 3 | 2-0 | 9.74% |
| 4 | 1-2 | 9.25% |
| 5 | 2-1 | 9.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 52.6% | 49.1% | 1.66 | -12.7% |
| Draw | 13.2% | 1.8% | 4.37 | -42.5% |
| Brest win | 34.3% | 49.1% | 5.42 | +85.8% |
| Over 2.5 | 54.1% | 57.6% | 1.74 | -5.8% |
| Under 2.5 | 45.9% | 42.4% | 2.27 | +4.1% |

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
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.57 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.53 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 6.81 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 56.0% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 19.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.14 |
| Reference draw odds | 2.10 |
| Reference away odds | 1.14 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | +3.5% |
| Draw probability edge | +11.4% |
| Away probability edge | -14.8% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | 0.0690 |
| Raw ev home | -0.0702 |
| Raw edge prob draw | 0.2277 |
| Raw ev draw | 0.0728 |
| Raw edge prob away | -0.2967 |
| Raw ev away | 0.0535 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **63.2%**. Expected goals are 1.23 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 65.8%; Under 4.5 goals: 75.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.7% | 5.67 |
| Draw | 19.1% | 5.23 |
| Paris Saint Germain win | 63.2% | 1.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.23 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 65.8% |
| Under 2.5 | 34.2% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.78% |
| 2 | 0-2 | 8.79% |
| 3 | 1-1 | 8.54% |
| 4 | 0-1 | 7.83% |
| 5 | 1-3 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.7% | 14.0% | 6.75 | +19.1% |
| Draw | 19.1% | 16.5% | 5.70 | +8.9% |
| Paris Saint Germain win | 63.2% | 69.5% | 1.46 | -7.7% |
| Over 2.5 | 65.8% | 74.0% | 1.33 | -12.5% |
| Under 2.5 | 34.2% | 26.0% | 3.42 | +17.0% |

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
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.02 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.83 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.92 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.00 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 57.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 6.40 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.41 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.31 |
| Reference Under 2.5 odds | 3.35 |
| Home probability edge | +3.6% |
| Draw probability edge | +2.6% |
| Away probability edge | -6.3% |
| Over 2.5 probability edge | -8.2% |
| Under 2.5 probability edge | +8.2% |
| Raw edge prob home | 0.0726 |
| Raw ev home | 0.4363 |
| Raw edge prob draw | 0.0530 |
| Raw ev draw | 0.2402 |
| Raw edge prob away | -0.1255 |
| Raw ev away | -0.1683 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **72.6%**. Expected goals are 0.78 for Troyes and 2.31 for RC Lens (3.09 combined). The most likely exact score is 0-2 at 12.3%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 60.7%; Under 4.5 goals: 79.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 11.9% | 8.41 |
| Draw | 15.5% | 6.45 |
| RC Lens win | 72.6% | 1.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.78 |
| RC Lens expected goals | 2.31 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 82.0% |
| Under 1.5 | 18.0% |
| Over 2.5 | 60.7% |
| Under 2.5 | 39.3% |
| Over 3.5 | 37.6% |
| Under 3.5 | 62.4% |
| Over 4.5 | 20.4% |
| Under 4.5 | 79.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.34% |
| 2 | 0-1 | 10.25% |
| 3 | 1-2 | 9.65% |
| 4 | 0-3 | 9.50% |
| 5 | 1-3 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 11.9% | 13.2% | 4.30 | -48.9% |
| Draw | 15.5% | 12.9% | 4.04 | -37.4% |
| RC Lens win | 72.6% | 73.9% | 1.87 | +35.8% |
| Over 2.5 | 60.7% | 61.6% | 1.64 | -0.4% |
| Under 2.5 | 39.3% | 38.4% | 2.48 | -2.6% |

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
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.57 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.55 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.66 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.89 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 10.6% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.14 |
| Reference draw odds | 2.16 |
| Reference away odds | 1.12 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -1.3% |
| Draw probability edge | +2.6% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0260 |
| Raw ev home | -0.5449 |
| Raw edge prob draw | 0.0527 |
| Raw ev draw | -0.2672 |
| Raw edge prob away | -0.0267 |
| Raw ev away | 0.3329 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **43.3%**. Expected goals are 0.95 for Angers and 1.65 for Marseille (2.59 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 46.2%; Under 4.5 goals: 88.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 27.2% | 3.68 |
| Draw | 29.5% | 3.39 |
| Marseille win | 43.3% | 2.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.95 |
| Marseille expected goals | 1.65 |
| Expected total goals | 2.59 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 72.9% |
| Under 1.5 | 27.1% |
| Over 2.5 | 46.2% |
| Under 2.5 | 53.8% |
| Over 3.5 | 25.4% |
| Under 3.5 | 74.6% |
| Over 4.5 | 11.5% |
| Under 4.5 | 88.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.06% |
| 2 | 0-1 | 9.52% |
| 3 | 0-0 | 9.26% |
| 4 | 1-0 | 8.36% |
| 5 | 0-2 | 8.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 27.2% | 33.3% | 3.30 | -10.3% |
| Draw | 29.5% | 33.3% | 3.85 | +13.7% |
| Marseille win | 43.3% | 33.3% | 2.28 | -1.3% |
| Over 2.5 | 46.2% | 60.4% | 1.68 | -22.3% |
| Under 2.5 | 53.8% | 39.6% | 2.40 | +29.1% |

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
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.79 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.68 |
| Fair Over 2.5 odds | 2.16 |
| Fair Under 2.5 odds | 1.86 |
| Fair Over 3.5 odds | 3.94 |
| Fair Under 3.5 odds | 1.34 |
| Fair Over 4.5 odds | 8.72 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 53.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.10 |
| Reference draw odds | 1.10 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | -6.2% |
| Draw probability edge | -3.8% |
| Away probability edge | +10.0% |
| Over 2.5 probability edge | -14.2% |
| Under 2.5 probability edge | +14.2% |
| Raw edge prob home | -0.1231 |
| Raw ev home | -0.3064 |
| Raw edge prob draw | -0.0760 |
| Raw ev draw | -0.0091 |
| Raw edge prob away | 0.1991 |
| Raw ev away | 0.2140 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Auxerre win** at **34.7%**. Expected goals are 1.16 for Le Havre and 1.19 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 14.8%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 40.9%; Under 4.5 goals: 91.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 33.9% | 2.95 |
| Draw | 31.4% | 3.19 |
| Auxerre win | 34.7% | 2.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.16 |
| Auxerre expected goals | 1.19 |
| Expected total goals | 2.34 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 68.5% |
| Under 1.5 | 31.5% |
| Over 2.5 | 40.9% |
| Under 2.5 | 59.1% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.78% |
| 2 | 0-0 | 10.96% |
| 3 | 0-1 | 10.31% |
| 4 | 1-0 | 10.22% |
| 5 | 1-2 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 33.9% | 33.3% | 2.52 | -14.6% |
| Draw | 31.4% | 33.3% | 3.51 | +10.1% |
| Auxerre win | 34.7% | 33.3% | 3.00 | +4.2% |
| Over 2.5 | 40.9% | 50.7% | 1.94 | -20.6% |
| Under 2.5 | 59.1% | 49.3% | 2.00 | +18.2% |

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
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.13 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.18 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.79 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.46 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 36.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.10 |
| Reference draw odds | 1.10 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.90 |
| Home probability edge | +0.6% |
| Draw probability edge | -2.0% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -9.8% |
| Under 2.5 probability edge | +9.8% |
| Raw edge prob home | 0.0112 |
| Raw ev home | -0.1318 |
| Raw edge prob draw | -0.0393 |
| Raw ev draw | 0.0322 |
| Raw edge prob away | 0.0281 |
| Raw ev away | 0.0843 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **46.8%**. Expected goals are 1.36 for Lorient and 1.84 for AS Monaco (3.21 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.6%; Under 4.5 goals: 78.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 28.1% | 3.56 |
| Draw | 25.2% | 3.97 |
| AS Monaco win | 46.8% | 2.14 |

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
| Over 2.5 | 61.6% |
| Under 2.5 | 38.4% |
| Over 3.5 | 39.7% |
| Under 3.5 | 60.3% |
| Over 4.5 | 21.8% |
| Under 4.5 | 78.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.34% |
| 2 | 1-2 | 9.07% |
| 3 | 2-1 | 6.97% |
| 4 | 2-2 | 6.77% |
| 5 | 0-1 | 6.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 28.1% | 28.3% | 3.75 | +5.2% |
| Draw | 25.2% | 26.6% | 3.58 | -9.9% |
| AS Monaco win | 46.8% | 45.1% | 2.17 | +1.5% |
| Over 2.5 | 61.6% | 51.9% | 1.92 | +18.3% |
| Under 2.5 | 38.4% | 48.1% | 2.02 | -22.5% |

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
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.60 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.02 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.52 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.59 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 27.9% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 48.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.35 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.14 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | -0.2% |
| Draw probability edge | -1.4% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | +9.7% |
| Under 2.5 probability edge | -9.7% |
| Raw edge prob home | -0.0039 |
| Raw ev home | 0.0450 |
| Raw edge prob draw | -0.0284 |
| Raw ev draw | -0.1494 |
| Raw edge prob away | 0.0323 |
| Raw ev away | 0.0497 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **43.2%**. Expected goals are 1.78 for Lyon and 1.08 for Nice (2.86 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 52.6%; Under 4.5 goals: 84.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 43.2% | 2.32 |
| Draw | 28.7% | 3.48 |
| Nice win | 28.1% | 3.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.78 |
| Nice expected goals | 1.08 |
| Expected total goals | 2.86 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.3% |
| Under 4.5 | 84.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.59% |
| 2 | 2-1 | 7.96% |
| 3 | 1-0 | 7.82% |
| 4 | 1-2 | 7.47% |
| 5 | 0-0 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 43.2% | 33.2% | 1.71 | -26.1% |
| Draw | 28.7% | 32.9% | 4.20 | +20.5% |
| Nice win | 28.1% | 33.8% | 5.24 | +47.3% |
| Over 2.5 | 52.6% | 57.6% | 1.78 | -6.4% |
| Under 2.5 | 47.4% | 42.4% | 2.25 | +6.7% |

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
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.53 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.54 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 53.1% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 22.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.12 |
| Reference draw odds | 1.13 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | +10.0% |
| Draw probability edge | -4.2% |
| Away probability edge | -5.7% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | 0.1992 |
| Raw ev home | -0.0912 |
| Raw edge prob draw | -0.0848 |
| Raw ev draw | 0.0272 |
| Raw edge prob away | -0.1144 |
| Raw ev away | 0.1736 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **42.6%**. Expected goals are 1.62 for Paris FC and 1.36 for Rennes (2.98 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 56.9%; Under 4.5 goals: 82.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 42.6% | 2.34 |
| Draw | 26.1% | 3.83 |
| Rennes win | 31.3% | 3.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.62 |
| Rennes expected goals | 1.36 |
| Expected total goals | 2.98 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.3% |
| Under 1.5 | 19.7% |
| Over 2.5 | 56.9% |
| Under 2.5 | 43.1% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.13% |
| 2 | 2-1 | 8.97% |
| 3 | 1-0 | 7.58% |
| 4 | 1-2 | 7.54% |
| 5 | 2-0 | 6.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 42.6% | 42.1% | 2.37 | +1.1% |
| Draw | 26.1% | 26.9% | 3.60 | -6.1% |
| Rennes win | 31.3% | 31.0% | 3.29 | +2.8% |
| Over 2.5 | 56.9% | 58.6% | 1.72 | -2.1% |
| Under 2.5 | 43.1% | 41.4% | 2.30 | -0.9% |

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
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.11 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.07 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.56 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 31.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.28 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.22 |
| Home probability edge | +0.5% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | 0.0107 |
| Raw ev home | 0.0234 |
| Raw edge prob draw | -0.0153 |
| Raw ev draw | -0.0880 |
| Raw edge prob away | 0.0045 |
| Raw ev away | 0.0359 |

</details>


---
