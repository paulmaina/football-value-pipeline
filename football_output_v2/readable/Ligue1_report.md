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

## 2026-10-09 — RC Lens vs Lyon

The model's most likely 1X2 outcome is **RC Lens win** at **40.6%**. Expected goals are 1.57 for RC Lens and 1.23 for Lyon (2.80 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 52.9%; Under 4.5 goals: 84.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 40.6% | 2.46 |
| Draw | 26.3% | 3.81 |
| Lyon win | 33.1% | 3.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.57 |
| Lyon expected goals | 1.23 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 52.9% |
| Under 2.5 | 47.1% |
| Over 3.5 | 30.6% |
| Under 3.5 | 69.4% |
| Over 4.5 | 15.1% |
| Under 4.5 | 84.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.43% |
| 2 | 2-1 | 8.38% |
| 3 | 1-2 | 8.18% |
| 4 | 1-0 | 8.13% |
| 5 | 0-1 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 40.6% | 36.5% | 2.72 | +10.5% |
| Draw | 26.3% | 26.4% | 3.75 | -1.6% |
| Lyon win | 33.1% | 37.1% | 2.69 | -10.9% |
| Over 2.5 | 52.9% | 63.1% | 1.54 | -18.6% |
| Under 2.5 | 47.1% | 36.9% | 2.52 | +18.8% |

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
| Market best home last update utc | 2026-10-09T14:38:42Z |
| Market best draw last update utc | 2026-10-09T14:38:09Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Lens |
| Matched away-team name | Lyon |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.84 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.27 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.61 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 44.7% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 29.2% |
| Raw p over 1 5 | 77.5% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.72 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.68 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.48 |
| Home probability edge | +4.1% |
| Draw probability edge | -0.2% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | -10.3% |
| Under 2.5 probability edge | +10.3% |
| Raw edge prob home | 0.0822 |
| Raw ev home | 0.2167 |
| Raw edge prob draw | -0.0035 |
| Raw ev draw | -0.0220 |
| Raw edge prob away | -0.0787 |
| Raw ev away | -0.2148 |

</details>


---

## 2026-10-10 — AS Monaco vs Toulouse

The model's most likely 1X2 outcome is **AS Monaco win** at **59.2%**. Expected goals are 1.95 for AS Monaco and 1.13 for Toulouse (3.07 combined). The most likely exact score is 2-1 at 10.5%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 59.9%; Under 4.5 goals: 80.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 59.2% | 1.69 |
| Draw | 21.7% | 4.60 |
| Toulouse win | 19.0% | 5.26 |

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
| Over 2.5 | 59.9% |
| Under 2.5 | 40.1% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.46% |
| 2 | 1-1 | 10.11% |
| 3 | 2-0 | 9.29% |
| 4 | 1-0 | 8.98% |
| 5 | 3-1 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 59.2% | 62.5% | 1.65 | -2.2% |
| Draw | 21.7% | 20.5% | 4.70 | +2.1% |
| Toulouse win | 19.0% | 16.9% | 5.80 | +10.3% |
| Over 2.5 | 59.9% | 60.0% | 1.65 | -1.2% |
| Under 2.5 | 40.1% | 40.0% | 2.45 | -1.7% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:38:41Z |
| Market best away last update utc | 2026-10-09T14:38:41Z |
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
| P btts yes | 58.0% |
| P btts no | 42.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.49 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.53 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.68 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 4.99 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 56.0% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 21.1% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 63.1% |
| Raw p btts yes | 58.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 1.53 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -3.3% |
| Draw probability edge | +1.2% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0659 |
| Raw ev home | -0.0768 |
| Raw edge prob draw | 0.0241 |
| Raw ev draw | 0.0781 |
| Raw edge prob away | 0.0418 |
| Raw ev away | 0.2242 |

</details>


---

## 2026-10-10 — Brest vs Angers

The model's most likely 1X2 outcome is **Brest win** at **50.9%**. Expected goals are 1.56 for Brest and 0.88 for Angers (2.44 combined). The most likely exact score is 1-0 at 12.6%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 44.1%; Under 4.5 goals: 89.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 50.9% | 1.97 |
| Draw | 26.0% | 3.85 |
| Angers win | 23.1% | 4.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Angers expected goals | 0.88 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 70.4% |
| Under 1.5 | 29.6% |
| Over 2.5 | 44.1% |
| Under 2.5 | 55.9% |
| Over 3.5 | 22.8% |
| Under 3.5 | 77.2% |
| Over 4.5 | 10.1% |
| Under 4.5 | 89.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.56% |
| 2 | 1-1 | 12.24% |
| 3 | 2-0 | 10.25% |
| 4 | 0-0 | 9.10% |
| 5 | 2-1 | 9.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 50.9% | 49.1% | 2.08 | +5.8% |
| Draw | 26.0% | 25.2% | 3.90 | +1.4% |
| Angers win | 23.1% | 25.6% | 3.80 | -12.1% |
| Over 2.5 | 44.1% | 54.0% | 1.83 | -19.3% |
| Under 2.5 | 55.9% | 46.0% | 2.15 | +20.2% |

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
| Market best home last update utc | 2026-10-09T14:38:41Z |
| Market best draw last update utc | 2026-10-09T14:38:09Z |
| Market best away last update utc | 2026-10-09T14:38:09Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Brest |
| Matched away-team name | Angers |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 46.7% |
| P btts no | 53.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.98 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.38 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.39 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 9.95 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 52.6% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 20.6% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 46.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 1.91 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.45 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | +1.8% |
| Draw probability edge | +0.7% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | 0.0353 |
| Raw ev home | 0.0950 |
| Raw edge prob draw | 0.0150 |
| Raw ev draw | 0.0429 |
| Raw edge prob away | -0.0503 |
| Raw ev away | -0.2167 |

</details>


---

## 2026-10-10 — Lille vs Le Havre

The model's most likely 1X2 outcome is **Lille win** at **65.7%**. Expected goals are 1.77 for Lille and 0.68 for Le Havre (2.45 combined). The most likely exact score is 1-0 at 15.4%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 45.3%; Under 4.5 goals: 89.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 65.7% | 1.52 |
| Draw | 21.3% | 4.70 |
| Le Havre win | 13.0% | 7.70 |

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
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.39% |
| 2 | 2-0 | 14.11% |
| 3 | 1-1 | 9.81% |
| 4 | 2-1 | 9.58% |
| 5 | 3-0 | 8.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 65.7% | 68.5% | 1.48 | -2.7% |
| Draw | 21.3% | 18.8% | 5.10 | +8.4% |
| Le Havre win | 13.0% | 12.7% | 8.00 | +3.9% |
| Over 2.5 | 45.3% | 57.4% | 1.72 | -22.1% |
| Under 2.5 | 54.7% | 42.6% | 2.30 | +25.9% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:38:41Z |
| Market best away last update utc | 2026-10-09T14:38:09Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 40.8% |
| P btts no | 59.2% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.13 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.47 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.26 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.52 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 63.0% |
| Unadjusted draw probability | 23.7% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.9% |
| Raw p btts yes | 41.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 1.40 |
| Reference draw odds | 4.40 |
| Reference away odds | 6.25 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -2.7% |
| Draw probability edge | +2.4% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -12.1% |
| Under 2.5 probability edge | +12.1% |
| Raw edge prob home | -0.0542 |
| Raw ev home | -0.0671 |
| Raw edge prob draw | 0.0483 |
| Raw ev draw | 0.2077 |
| Raw edge prob away | 0.0059 |
| Raw ev away | 0.0628 |

</details>


---

## 2026-10-10 — Lorient vs Paris FC

The model's most likely 1X2 outcome is **Paris FC win** at **41.2%**. Expected goals are 1.33 for Lorient and 1.43 for Paris FC (2.76 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 51.9%; Under 4.5 goals: 85.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 31.3% | 3.19 |
| Draw | 27.5% | 3.64 |
| Paris FC win | 41.2% | 2.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.33 |
| Paris FC expected goals | 1.43 |
| Expected total goals | 2.76 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
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
| 1 | 1-1 | 13.02% |
| 2 | 1-2 | 9.12% |
| 3 | 0-1 | 8.90% |
| 4 | 2-1 | 7.29% |
| 5 | 0-0 | 7.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 31.3% | 28.2% | 3.50 | +9.6% |
| Draw | 27.5% | 28.2% | 3.50 | -3.9% |
| Paris FC win | 41.2% | 43.5% | 2.36 | -2.7% |
| Over 2.5 | 51.9% | 48.7% | 2.03 | +5.4% |
| Under 2.5 | 48.1% | 51.3% | 1.93 | -7.2% |

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
| Market best home last update utc | 2026-10-09T14:38:42Z |
| Market best draw last update utc | 2026-10-09T14:38:42Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
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
| Fair Under 0.5 odds | 14.02 |
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
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.50 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.28 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.92 |
| Home probability edge | +3.1% |
| Draw probability edge | -0.8% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | +3.2% |
| Under 2.5 probability edge | -3.2% |
| Raw edge prob home | 0.0615 |
| Raw ev home | 0.2035 |
| Raw edge prob draw | -0.0156 |
| Raw ev draw | -0.0662 |
| Raw edge prob away | -0.0459 |
| Raw ev away | -0.0812 |

</details>


---

## 2026-10-10 — Paris Saint Germain vs Le Mans FC

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **83.6%**. Expected goals are 3.17 for Paris Saint Germain and 1.12 for Le Mans FC (4.29 combined). The most likely exact score is 3-1 at 8.8%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 81.5%; Under 4.5 goals: 55.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 83.6% | 1.20 |
| Draw | 9.9% | 10.08 |
| Le Mans FC win | 6.5% | 15.40 |

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
| Over 2.5 | 81.5% |
| Under 2.5 | 18.5% |
| Over 3.5 | 63.2% |
| Under 3.5 | 36.8% |
| Over 4.5 | 44.1% |
| Under 4.5 | 55.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 8.83% |
| 2 | 2-1 | 8.36% |
| 3 | 3-0 | 7.90% |
| 4 | 2-0 | 7.48% |
| 5 | 4-1 | 6.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 83.6% | 90.0% | 1.11 | -7.2% |
| Draw | 9.9% | 6.6% | 14.90 | +47.9% |
| Le Mans FC win | 6.5% | 3.4% | 31.00 | +101.4% |
| Over 2.5 | 81.5% | 81.2% | 1.24 | +1.1% |
| Under 2.5 | 18.5% | 18.8% | 4.33 | -20.0% |

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
| Market best home last update utc | 2026-10-09T14:38:42Z |
| Market best draw last update utc | 2026-10-09T14:38:27Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Paris SG |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.4% |
| P btts no | 36.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 81.64 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.27 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.41 |
| Fair Over 3.5 odds | 1.58 |
| Fair Under 3.5 odds | 2.72 |
| Fair Over 4.5 odds | 2.27 |
| Fair Under 4.5 odds | 1.79 |
| Unadjusted home-win probability | 77.2% |
| Unadjusted draw probability | 13.2% |
| Unadjusted away-win probability | 9.6% |
| Raw p over 1 5 | 93.0% |
| Raw p under 3 5 | 38.0% |
| Raw p btts yes | 64.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.11 |
| Reference draw odds | 14.50 |
| Reference away odds | 28.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.33 |
| Home probability edge | -6.4% |
| Draw probability edge | +3.3% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | -0.1275 |
| Raw ev home | -0.1430 |
| Raw edge prob draw | 0.0657 |
| Raw ev draw | 0.9684 |
| Raw edge prob away | 0.0618 |
| Raw ev away | 1.9713 |
| Market p over 1 5 | 93.4% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T14:38:10Z |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 10.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 40.8% |
| Market under 3 5 odds | 2.39 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T14:38:10Z |
| Market reference under 3 5 odds | 2.28 |
| Market reference under 3 5 opposite odds | 1.62 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 45.5% |
| Market btts yes odds | 2.17 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-09T14:38:05Z |
| Market reference btts yes odds | 2.02 |
| Market reference btts yes opposite odds | 1.72 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-11 — Nice vs Strasbourg

The model's most likely 1X2 outcome is **Nice win** at **39.7%**. Expected goals are 1.46 for Nice and 1.39 for Strasbourg (2.84 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.1%; Under 4.5 goals: 84.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nice win | 39.7% | 2.52 |
| Draw | 26.2% | 3.82 |
| Strasbourg win | 34.1% | 2.94 |

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
| 1 | 1-1 | 12.34% |
| 2 | 2-1 | 8.86% |
| 3 | 1-0 | 8.14% |
| 4 | 1-2 | 7.87% |
| 5 | 0-1 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nice win | 39.7% | 41.1% | 2.48 | -1.4% |
| Draw | 26.2% | 26.1% | 3.75 | -1.8% |
| Strasbourg win | 34.1% | 32.8% | 3.07 | +4.6% |
| Over 2.5 | 54.1% | 55.8% | 1.77 | -4.2% |
| Under 2.5 | 45.9% | 44.2% | 2.22 | +1.9% |

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
| Market best home last update utc | 2026-10-09T14:38:09Z |
| Market best draw last update utc | 2026-10-09T14:38:27Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nice |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.58 |
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
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.40 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.00 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Home probability edge | -1.4% |
| Draw probability edge | +0.1% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0273 |
| Raw ev home | -0.0483 |
| Raw edge prob draw | 0.0014 |
| Raw ev draw | -0.0152 |
| Raw edge prob away | 0.0259 |
| Raw ev away | 0.0857 |

</details>


---

## 2026-10-11 — Rennes vs Auxerre

The model's most likely 1X2 outcome is **Rennes win** at **60.9%**. Expected goals are 1.84 for Rennes and 1.14 for Auxerre (2.98 combined). The most likely exact score is 2-1 at 11.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 58.7%; Under 4.5 goals: 81.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 60.9% | 1.64 |
| Draw | 20.8% | 4.81 |
| Auxerre win | 18.3% | 5.47 |

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
| 1 | 2-1 | 11.24% |
| 2 | 1-0 | 10.05% |
| 3 | 2-0 | 9.83% |
| 4 | 1-1 | 9.73% |
| 5 | 3-1 | 6.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 60.9% | 68.8% | 1.48 | -9.8% |
| Draw | 20.8% | 17.6% | 5.30 | +10.1% |
| Auxerre win | 18.3% | 13.6% | 7.50 | +37.2% |
| Over 2.5 | 58.7% | 63.8% | 1.51 | -11.4% |
| Under 2.5 | 41.3% | 36.2% | 2.61 | +7.8% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:38:41Z |
| Market best away last update utc | 2026-10-09T14:37:54Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
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
| Fair Under 0.5 odds | 20.50 |
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
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 1.40 |
| Reference draw odds | 4.75 |
| Reference away odds | 6.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -7.8% |
| Draw probability edge | +3.1% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.1567 |
| Raw ev home | -0.2143 |
| Raw edge prob draw | 0.0628 |
| Raw ev draw | 0.2677 |
| Raw edge prob away | 0.0939 |
| Raw ev away | 0.7245 |

</details>


---

## 2026-10-11 — Troyes vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **61.7%**. Expected goals are 0.92 for Troyes and 2.68 for Marseille (3.60 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 67.0%; Under 4.5 goals: 72.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 17.9% | 5.58 |
| Draw | 20.4% | 4.91 |
| Marseille win | 61.7% | 1.62 |

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
| Over 3.5 | 46.0% |
| Under 3.5 | 54.0% |
| Over 4.5 | 27.2% |
| Under 4.5 | 72.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.21% |
| 2 | 0-2 | 8.14% |
| 3 | 1-2 | 7.51% |
| 4 | 0-3 | 7.27% |
| 5 | 1-3 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 17.9% | 25.7% | 4.03 | -27.8% |
| Draw | 20.4% | 25.1% | 4.05 | -17.5% |
| Marseille win | 61.7% | 49.2% | 2.02 | +24.7% |
| Over 2.5 | 67.0% | 60.0% | 1.65 | +10.5% |
| Under 2.5 | 33.0% | 40.0% | 2.45 | -19.1% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:38:27Z |
| Market best away last update utc | 2026-10-09T14:38:42Z |
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
| P btts yes | 58.8% |
| P btts no | 41.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.02 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.34 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.03 |
| Fair Over 3.5 odds | 2.17 |
| Fair Under 3.5 odds | 1.85 |
| Fair Over 4.5 odds | 3.67 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 15.7% |
| Unadjusted away-win probability | 74.2% |
| Raw p over 1 5 | 87.8% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 56.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.85 |
| Reference draw odds | 3.95 |
| Reference away odds | 2.02 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -7.8% |
| Draw probability edge | -4.7% |
| Away probability edge | +12.5% |
| Over 2.5 probability edge | +7.0% |
| Under 2.5 probability edge | -7.0% |
| Raw edge prob home | -0.1559 |
| Raw ev home | -0.5922 |
| Raw edge prob draw | -0.0938 |
| Raw ev draw | -0.3653 |
| Raw edge prob away | 0.2497 |
| Raw ev away | 0.4990 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T14:38:10Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 62.1% |
| Market under 3 5 odds | 1.57 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T14:38:26Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 62.0% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T14:38:26Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.36 |
| Market btts yes bookmakers | 3 |

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
| Draw | 35.0% | 46.7% | 3.60 | +26.2% |
| Toulouse win | 28.8% | 26.7% | 2.34 | -32.7% |
| Over 2.5 | 61.5% | 53.6% | 1.84 | +13.2% |
| Under 2.5 | 38.5% | 46.4% | 2.12 | -18.4% |

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
| Market best home last update utc | 2026-10-09T14:37:54Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | LeoVegas (SE) |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Mans |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 68.9% |
| P btts no | 31.1% |
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
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 66.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.18 |
| Reference draw odds | 1.10 |
| Reference away odds | 1.18 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | +9.5% |
| Draw probability edge | -11.7% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +7.9% |
| Under 2.5 probability edge | -7.9% |
| Raw edge prob home | 0.1910 |
| Raw ev home | 0.5097 |
| Raw edge prob draw | -0.2331 |
| Raw ev draw | -0.1580 |
| Raw edge prob away | 0.0421 |
| Raw ev away | -0.2778 |
| Market p over 1 5 | 78.0% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T14:38:26Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 68.2% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T14:38:26Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.86 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 59.1% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T14:38:26Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.22 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **51.4%**. Expected goals are 1.76 for Lille and 0.94 for Brest (2.70 combined). The most likely exact score is 0-1 at 10.5%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 54.1%; Under 4.5 goals: 85.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 51.4% | 1.95 |
| Draw | 13.0% | 7.72 |
| Brest win | 35.6% | 2.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.76 |
| Brest expected goals | 0.94 |
| Expected total goals | 2.70 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 10.55% |
| 2 | 1-0 | 10.31% |
| 3 | 1-2 | 9.62% |
| 4 | 2-0 | 9.53% |
| 5 | 2-1 | 8.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 51.4% | 46.8% | 1.66 | -14.7% |
| Draw | 13.0% | 1.4% | 4.37 | -43.4% |
| Brest win | 35.6% | 51.8% | 5.50 | +96.0% |
| Over 2.5 | 54.1% | 56.8% | 1.74 | -5.8% |
| Under 2.5 | 45.9% | 43.2% | 2.27 | +4.1% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:38:27Z |
| Market best away last update utc | 2026-10-09T14:37:54Z |
| Odds bookmakers 1x2 | 15.00 |
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
| P btts yes | 48.9% |
| P btts no | 51.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.99 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.05 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 6.82 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 56.0% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 19.4% |
| Raw p over 1 5 | 75.7% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 51.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.14 |
| Reference draw odds | 2.10 |
| Reference away odds | 1.12 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | +4.6% |
| Draw probability edge | +11.6% |
| Away probability edge | -16.2% |
| Over 2.5 probability edge | -2.6% |
| Under 2.5 probability edge | +2.6% |
| Raw edge prob home | 0.0922 |
| Raw ev home | -0.0702 |
| Raw edge prob draw | 0.2319 |
| Raw ev draw | 0.0728 |
| Raw edge prob away | -0.3241 |
| Raw ev away | 0.0691 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **69.4%**. Expected goals are 1.23 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 11.8%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 67.3%; Under 4.5 goals: 74.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 15.2% | 6.58 |
| Draw | 15.4% | 6.47 |
| Paris Saint Germain win | 69.4% | 1.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.23 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 85.7% |
| Under 1.5 | 14.3% |
| Over 2.5 | 67.3% |
| Under 2.5 | 32.7% |
| Over 3.5 | 43.9% |
| Under 3.5 | 56.1% |
| Over 4.5 | 25.9% |
| Under 4.5 | 74.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.82% |
| 2 | 0-2 | 9.63% |
| 3 | 0-1 | 8.59% |
| 4 | 1-3 | 8.28% |
| 5 | 1-1 | 6.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 15.2% | 9.1% | 6.73 | +2.3% |
| Draw | 15.4% | 9.1% | 5.70 | -12.0% |
| Paris Saint Germain win | 69.4% | 81.7% | 1.46 | +1.3% |
| Over 2.5 | 67.3% | 73.1% | 1.33 | -10.5% |
| Under 2.5 | 32.7% | 26.9% | 3.42 | +12.0% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Strasbourg |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.68 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.01 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.05 |
| Fair Over 3.5 odds | 2.28 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.86 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 57.0% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.4% |
| Raw p btts yes | 62.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.10 |
| Reference draw odds | 3.10 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Home probability edge | +6.1% |
| Draw probability edge | +6.3% |
| Away probability edge | -12.4% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.1215 |
| Raw ev home | 0.4321 |
| Raw edge prob draw | 0.1263 |
| Raw ev draw | 0.2402 |
| Raw edge prob away | -0.2478 |
| Raw ev away | -0.1683 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T14:38:26Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 46.5% |
| Market under 3 5 odds | 2.06 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T14:36:56Z |
| Market reference under 3 5 odds | 2.04 |
| Market reference under 3 5 opposite odds | 1.79 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 65.8% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T14:38:26Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 2.59 |
| Market btts yes bookmakers | 2 |

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
| Draw | 15.5% | 12.9% | 4.10 | -36.4% |
| RC Lens win | 72.6% | 73.9% | 1.87 | +35.8% |
| Over 2.5 | 60.7% | 60.2% | 1.64 | -0.4% |
| Under 2.5 | 39.3% | 39.8% | 2.48 | -2.6% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Unibet (SE) |
| Matched home-team name | Troyes |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 48.7% |
| P btts no | 51.3% |
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
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 49.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.14 |
| Reference draw odds | 2.16 |
| Reference away odds | 1.12 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Home probability edge | -1.3% |
| Draw probability edge | +2.6% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | -0.0260 |
| Raw ev home | -0.5449 |
| Raw edge prob draw | 0.0527 |
| Raw ev draw | -0.2563 |
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
| Draw | 29.5% | 33.3% | 3.80 | +12.2% |
| Marseille win | 43.3% | 33.3% | 2.28 | -1.3% |
| Over 2.5 | 46.2% | 58.8% | 1.68 | -22.3% |
| Under 2.5 | 53.8% | 41.2% | 2.40 | +29.1% |

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
| Market best home last update utc | 2026-10-09T14:37:54Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
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
| P btts yes | 51.3% |
| P btts no | 48.7% |
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
| Raw p over 1 5 | 73.8% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 50.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.10 |
| Reference draw odds | 1.10 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -6.2% |
| Draw probability edge | -3.8% |
| Away probability edge | +10.0% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | -0.1231 |
| Raw ev home | -0.3064 |
| Raw edge prob draw | -0.0760 |
| Raw ev draw | -0.0220 |
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
| Draw | 31.4% | 33.3% | 3.55 | +11.4% |
| Auxerre win | 34.7% | 33.3% | 3.00 | +4.2% |
| Over 2.5 | 40.9% | 50.8% | 1.94 | -20.6% |
| Under 2.5 | 59.1% | 49.2% | 2.00 | +18.2% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Havre |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.8% |
| P btts no | 51.2% |
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
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.0% |
| Raw p btts yes | 48.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.10 |
| Reference draw odds | 1.10 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.94 |
| Reference Under 2.5 odds | 2.00 |
| Home probability edge | +0.6% |
| Draw probability edge | -2.0% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | 0.0112 |
| Raw ev home | -0.1318 |
| Raw edge prob draw | -0.0393 |
| Raw ev draw | 0.0440 |
| Raw edge prob away | 0.0281 |
| Raw ev away | 0.0843 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **40.9%**. Expected goals are 1.36 for Lorient and 1.84 for AS Monaco (3.21 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 60.3%; Under 4.5 goals: 78.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 30.6% | 3.27 |
| Draw | 28.5% | 3.50 |
| AS Monaco win | 40.9% | 2.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.36 |
| AS Monaco expected goals | 1.84 |
| Expected total goals | 3.21 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 39.4% |
| Under 3.5 | 60.6% |
| Over 4.5 | 21.1% |
| Under 4.5 | 78.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.86% |
| 2 | 1-2 | 7.93% |
| 3 | 2-2 | 7.67% |
| 4 | 2-1 | 7.60% |
| 5 | 0-1 | 5.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 30.6% | 33.3% | 3.65 | +11.7% |
| Draw | 28.5% | 33.3% | 3.60 | +2.8% |
| AS Monaco win | 40.9% | 33.3% | 2.24 | -8.5% |
| Over 2.5 | 60.3% | 51.0% | 1.93 | +16.5% |
| Under 2.5 | 39.7% | 49.0% | 2.01 | -20.3% |

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
| Market best home last update utc | 2026-10-09T14:37:54Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | LeoVegas (SE) |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lorient |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 64.4% |
| P btts no | 35.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.17 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.93 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.74 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 27.9% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 83.5% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 63.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.10 |
| Reference draw odds | 1.10 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 2.01 |
| Home probability edge | -2.7% |
| Draw probability edge | -4.8% |
| Away probability edge | +7.5% |
| Over 2.5 probability edge | +9.3% |
| Under 2.5 probability edge | -9.3% |
| Raw edge prob home | -0.0547 |
| Raw ev home | 0.0171 |
| Raw edge prob draw | -0.0957 |
| Raw ev draw | -0.1446 |
| Raw edge prob away | 0.1504 |
| Raw ev away | 0.0836 |

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
| Over 2.5 | 52.6% | 55.5% | 1.78 | -6.4% |
| Under 2.5 | 47.4% | 44.5% | 2.25 | +6.7% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:37:54Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
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
| P btts yes | 56.9% |
| P btts no | 43.1% |
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
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.12 |
| Reference draw odds | 1.13 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.21 |
| Home probability edge | +10.0% |
| Draw probability edge | -4.2% |
| Away probability edge | -5.7% |
| Over 2.5 probability edge | -2.9% |
| Under 2.5 probability edge | +2.9% |
| Raw edge prob home | 0.1992 |
| Raw ev home | -0.0912 |
| Raw edge prob draw | -0.0848 |
| Raw ev draw | 0.0272 |
| Raw edge prob away | -0.1144 |
| Raw ev away | 0.1736 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **38.2%**. Expected goals are 1.62 for Paris FC and 1.36 for Rennes (2.98 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 55.7%; Under 4.5 goals: 82.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 38.2% | 2.62 |
| Draw | 29.5% | 3.39 |
| Rennes win | 32.3% | 3.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.62 |
| Rennes expected goals | 1.36 |
| Expected total goals | 2.98 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 55.7% |
| Under 2.5 | 44.3% |
| Over 3.5 | 34.5% |
| Under 3.5 | 65.5% |
| Over 4.5 | 17.4% |
| Under 4.5 | 82.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.73% |
| 2 | 2-1 | 8.02% |
| 3 | 1-2 | 7.79% |
| 4 | 2-2 | 7.17% |
| 5 | 1-0 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 38.2% | 33.1% | 2.37 | -9.6% |
| Draw | 29.5% | 33.7% | 3.50 | +3.4% |
| Rennes win | 32.3% | 33.1% | 3.29 | +6.3% |
| Over 2.5 | 55.7% | 57.4% | 1.72 | -4.3% |
| Under 2.5 | 44.3% | 42.6% | 2.30 | +2.0% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:38:25Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 888sport |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paris FC |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.12 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.03 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.74 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 31.5% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 60.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.12 |
| Reference draw odds | 1.10 |
| Reference away odds | 1.12 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +5.0% |
| Draw probability edge | -4.2% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | 0.1005 |
| Raw ev home | 0.0234 |
| Raw edge prob draw | -0.0840 |
| Raw ev draw | -0.1134 |
| Raw edge prob away | -0.0165 |
| Raw ev away | 0.0359 |

</details>


---
