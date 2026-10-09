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

The model's most likely 1X2 outcome is **RC Lens win** at **41.0%**. Expected goals are 1.57 for RC Lens and 1.23 for Lyon (2.80 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.2%; Under 4.5 goals: 84.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 41.0% | 2.44 |
| Draw | 25.3% | 3.95 |
| Lyon win | 33.7% | 2.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.57 |
| Lyon expected goals | 1.23 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 53.2% |
| Under 2.5 | 46.8% |
| Over 3.5 | 30.7% |
| Under 3.5 | 69.3% |
| Over 4.5 | 15.2% |
| Under 4.5 | 84.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.98% |
| 2 | 2-1 | 8.46% |
| 3 | 1-2 | 8.31% |
| 4 | 1-0 | 8.22% |
| 5 | 0-1 | 7.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 41.0% | 37.3% | 2.70 | +10.8% |
| Draw | 25.3% | 24.5% | 3.80 | -3.9% |
| Lyon win | 33.7% | 38.2% | 2.70 | -9.1% |
| Over 2.5 | 53.2% | 63.1% | 1.54 | -18.1% |
| Under 2.5 | 46.8% | 36.9% | 2.52 | +17.9% |

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
| Market best home last update utc | 2026-10-09T13:49:26Z |
| Market best draw last update utc | 2026-10-09T13:49:26Z |
| Market best away last update utc | 2026-10-09T13:49:26Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Lens |
| Matched away-team name | Lyon |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.40 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.42 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.26 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.56 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 44.7% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 29.2% |
| Raw p over 1 5 | 77.5% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.50 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.45 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.48 |
| Home probability edge | +3.7% |
| Draw probability edge | +0.8% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | 0.0739 |
| Raw ev home | 0.2077 |
| Raw edge prob draw | 0.0158 |
| Raw ev draw | -0.0090 |
| Raw edge prob away | -0.0897 |
| Raw ev away | -0.2118 |

</details>


---

## 2026-10-10 — AS Monaco vs Toulouse

The model's most likely 1X2 outcome is **AS Monaco win** at **59.1%**. Expected goals are 1.95 for AS Monaco and 1.13 for Toulouse (3.07 combined). The most likely exact score is 2-1 at 10.4%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 60.0%; Under 4.5 goals: 79.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 59.1% | 1.69 |
| Draw | 21.3% | 4.70 |
| Toulouse win | 19.7% | 5.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.95 |
| Toulouse expected goals | 1.13 |
| Expected total goals | 3.07 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 81.9% |
| Under 1.5 | 18.1% |
| Over 2.5 | 60.0% |
| Under 2.5 | 40.0% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 20.1% |
| Under 4.5 | 79.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.43% |
| 2 | 1-1 | 9.89% |
| 3 | 2-0 | 9.26% |
| 4 | 1-0 | 8.96% |
| 5 | 3-1 | 6.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 59.1% | 62.2% | 1.65 | -2.5% |
| Draw | 21.3% | 19.6% | 4.70 | -0.1% |
| Toulouse win | 19.7% | 18.2% | 5.80 | +14.1% |
| Over 2.5 | 60.0% | 61.6% | 1.65 | -1.0% |
| Under 2.5 | 40.0% | 38.4% | 2.45 | -2.1% |

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
| Market best home last update utc | 2026-10-09T13:47:15Z |
| Market best draw last update utc | 2026-10-09T13:49:26Z |
| Market best away last update utc | 2026-10-09T13:49:26Z |
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
| P btts yes | 57.9% |
| P btts no | 42.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.94 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.53 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 4.98 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 56.0% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 21.1% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 63.1% |
| Raw p btts yes | 58.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.54 |
| Reference draw odds | 4.40 |
| Reference away odds | 4.70 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -3.1% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | -0.0623 |
| Raw ev home | -0.0768 |
| Raw edge prob draw | 0.0335 |
| Raw ev draw | 0.0781 |
| Raw edge prob away | 0.0289 |
| Raw ev away | 0.2242 |

</details>


---

## 2026-10-10 — Brest vs Angers

The model's most likely 1X2 outcome is **Brest win** at **50.7%**. Expected goals are 1.56 for Brest and 0.88 for Angers (2.44 combined). The most likely exact score is 1-0 at 12.5%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 44.2%; Under 4.5 goals: 89.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 50.7% | 1.97 |
| Draw | 25.8% | 3.88 |
| Angers win | 23.5% | 4.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Angers expected goals | 0.88 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 70.4% |
| Under 1.5 | 29.6% |
| Over 2.5 | 44.2% |
| Under 2.5 | 55.8% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 10.1% |
| Under 4.5 | 89.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.51% |
| 2 | 1-1 | 12.15% |
| 3 | 2-0 | 10.21% |
| 4 | 0-0 | 9.04% |
| 5 | 2-1 | 8.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 50.7% | 48.7% | 2.08 | +5.4% |
| Draw | 25.8% | 24.9% | 3.90 | +0.6% |
| Angers win | 23.5% | 26.5% | 3.80 | -10.6% |
| Over 2.5 | 44.2% | 54.9% | 1.83 | -19.2% |
| Under 2.5 | 55.8% | 45.1% | 2.15 | +20.1% |

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
| Market best home last update utc | 2026-10-09T13:49:26Z |
| Market best draw last update utc | 2026-10-09T13:49:10Z |
| Market best away last update utc | 2026-10-09T13:49:10Z |
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
| Fair Under 0.5 odds | 11.07 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.38 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 9.94 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 52.6% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 20.6% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 46.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.94 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | +2.0% |
| Draw probability edge | +0.9% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | 0.0397 |
| Raw ev home | 0.0950 |
| Raw edge prob draw | 0.0188 |
| Raw ev draw | 0.0429 |
| Raw edge prob away | -0.0584 |
| Raw ev away | -0.2167 |

</details>


---

## 2026-10-10 — Lille vs Le Havre

The model's most likely 1X2 outcome is **Lille win** at **66.0%**. Expected goals are 1.77 for Lille and 0.68 for Le Havre (2.45 combined). The most likely exact score is 1-0 at 15.5%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 45.5%; Under 4.5 goals: 89.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 66.0% | 1.51 |
| Draw | 20.7% | 4.83 |
| Le Havre win | 13.3% | 7.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.77 |
| Le Havre expected goals | 0.68 |
| Expected total goals | 2.45 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 71.2% |
| Under 1.5 | 28.8% |
| Over 2.5 | 45.5% |
| Under 2.5 | 54.5% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.45% |
| 2 | 2-0 | 14.17% |
| 3 | 2-1 | 9.62% |
| 4 | 1-1 | 9.56% |
| 5 | 3-0 | 8.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 66.0% | 69.0% | 1.48 | -2.3% |
| Draw | 20.7% | 17.7% | 5.00 | +3.5% |
| Le Havre win | 13.3% | 13.3% | 8.00 | +6.2% |
| Over 2.5 | 45.5% | 58.4% | 1.72 | -21.8% |
| Under 2.5 | 54.5% | 41.6% | 2.30 | +25.4% |

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
| Market best home last update utc | 2026-10-09T13:47:15Z |
| Market best draw last update utc | 2026-10-09T13:49:10Z |
| Market best away last update utc | 2026-10-09T13:49:10Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 40.6% |
| P btts no | 59.4% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.45 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.47 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.48 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 63.0% |
| Unadjusted draw probability | 23.7% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.9% |
| Raw p btts yes | 41.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.40 |
| Reference draw odds | 4.80 |
| Reference away odds | 6.25 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.26 |
| Home probability edge | -3.0% |
| Draw probability edge | +3.0% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -12.9% |
| Under 2.5 probability edge | +12.9% |
| Raw edge prob home | -0.0597 |
| Raw ev home | -0.0671 |
| Raw edge prob draw | 0.0594 |
| Raw ev draw | 0.1840 |
| Raw edge prob away | 0.0003 |
| Raw ev away | 0.0628 |

</details>


---

## 2026-10-10 — Lorient vs Paris FC

The model's most likely 1X2 outcome is **Paris FC win** at **41.1%**. Expected goals are 1.33 for Lorient and 1.43 for Paris FC (2.76 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 52.0%; Under 4.5 goals: 85.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 31.7% | 3.15 |
| Draw | 27.1% | 3.68 |
| Paris FC win | 41.1% | 2.43 |

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
| Over 2.5 | 52.0% |
| Under 2.5 | 48.0% |
| Over 3.5 | 30.0% |
| Under 3.5 | 70.0% |
| Over 4.5 | 14.6% |
| Under 4.5 | 85.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.87% |
| 2 | 1-2 | 9.10% |
| 3 | 0-1 | 8.88% |
| 4 | 2-1 | 7.39% |
| 5 | 1-0 | 7.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 31.7% | 29.1% | 3.50 | +11.0% |
| Draw | 27.1% | 27.6% | 3.50 | -5.0% |
| Paris FC win | 41.1% | 43.3% | 2.36 | -2.9% |
| Over 2.5 | 52.0% | 50.0% | 2.03 | +5.6% |
| Under 2.5 | 48.0% | 50.0% | 1.93 | -7.4% |

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
| Market best home last update utc | 2026-10-09T13:49:26Z |
| Market best draw last update utc | 2026-10-09T13:49:26Z |
| Market best away last update utc | 2026-10-09T13:47:15Z |
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
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.19 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.33 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.84 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 34.4% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 76.9% |
| Raw p under 3 5 | 70.0% |
| Raw p btts yes | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.90 |
| Home probability edge | +2.7% |
| Draw probability edge | -0.5% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | 0.0533 |
| Raw ev home | 0.2035 |
| Raw edge prob draw | -0.0092 |
| Raw ev draw | -0.0662 |
| Raw edge prob away | -0.0441 |
| Raw ev away | -0.0812 |

</details>


---

## 2026-10-10 — Paris Saint Germain vs Le Mans FC

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **84.5%**. Expected goals are 3.17 for Paris Saint Germain and 1.12 for Le Mans FC (4.29 combined). The most likely exact score is 3-1 at 8.9%. Goal-market probabilities: at least one goal: 98.9%; Over 2.5 goals: 81.9%; Under 4.5 goals: 55.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 84.5% | 1.18 |
| Draw | 9.0% | 11.15 |
| Le Mans FC win | 6.5% | 15.42 |

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
| Over 2.5 | 81.9% |
| Under 2.5 | 18.1% |
| Over 3.5 | 63.4% |
| Under 3.5 | 36.6% |
| Over 4.5 | 44.4% |
| Under 4.5 | 55.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 8.93% |
| 2 | 2-1 | 8.46% |
| 3 | 3-0 | 7.99% |
| 4 | 2-0 | 7.57% |
| 5 | 4-1 | 7.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 84.5% | 91.9% | 1.11 | -6.2% |
| Draw | 9.0% | 4.7% | 14.90 | +33.6% |
| Le Mans FC win | 6.5% | 3.4% | 31.00 | +101.1% |
| Over 2.5 | 81.9% | 79.1% | 1.24 | +1.5% |
| Under 2.5 | 18.1% | 20.9% | 4.33 | -21.6% |

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
| Market best home last update utc | 2026-10-09T13:49:26Z |
| Market best draw last update utc | 2026-10-09T13:47:15Z |
| Market best away last update utc | 2026-10-09T13:47:15Z |
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
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 90.36 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.43 |
| Fair Over 2.5 odds | 1.22 |
| Fair Under 2.5 odds | 5.52 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.07 |
| Reference draw odds | 11.50 |
| Reference away odds | 15.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.24 |
| Reference Under 2.5 odds | 4.19 |
| Home probability edge | -7.3% |
| Draw probability edge | +4.2% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | +2.8% |
| Under 2.5 probability edge | -2.8% |
| Raw edge prob home | -0.1469 |
| Raw ev home | -0.1430 |
| Raw edge prob draw | 0.0849 |
| Raw ev draw | 0.9684 |
| Raw edge prob away | 0.0620 |
| Raw ev away | 1.9713 |
| Market p over 1 5 | 93.4% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T13:48:37Z |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 10.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 40.0% |
| Market under 3 5 odds | 2.39 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T13:48:37Z |
| Market reference under 3 5 odds | 2.32 |
| Market reference under 3 5 opposite odds | 1.60 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 44.2% |
| Market btts yes odds | 2.14 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-09T13:49:24Z |
| Market reference btts yes odds | 2.14 |
| Market reference btts yes opposite odds | 1.72 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-11 — Nice vs Strasbourg

The model's most likely 1X2 outcome is **Nice win** at **39.8%**. Expected goals are 1.46 for Nice and 1.39 for Strasbourg (2.84 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.1%; Under 4.5 goals: 84.1%.

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
| Over 2.5 | 54.1% | 56.2% | 1.77 | -4.3% |
| Under 2.5 | 45.9% | 43.8% | 2.22 | +1.9% |

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
| Market best home last update utc | 2026-10-09T13:49:10Z |
| Market best draw last update utc | 2026-10-09T13:47:15Z |
| Market best away last update utc | 2026-10-09T13:47:15Z |
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
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | -1.4% |
| Draw probability edge | -0.0% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -2.2% |
| Under 2.5 probability edge | +2.2% |
| Raw edge prob home | -0.0287 |
| Raw ev home | -0.0483 |
| Raw edge prob draw | -0.0001 |
| Raw ev draw | -0.0152 |
| Raw edge prob away | 0.0288 |
| Raw ev away | 0.0857 |

</details>


---

## 2026-10-11 — Rennes vs Auxerre

The model's most likely 1X2 outcome is **Rennes win** at **61.3%**. Expected goals are 1.84 for Rennes and 1.14 for Auxerre (2.98 combined). The most likely exact score is 2-1 at 11.3%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 58.8%; Under 4.5 goals: 81.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 61.3% | 1.63 |
| Draw | 20.5% | 4.88 |
| Auxerre win | 18.1% | 5.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.84 |
| Auxerre expected goals | 1.14 |
| Expected total goals | 2.98 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 35.6% |
| Under 3.5 | 64.4% |
| Over 4.5 | 19.0% |
| Under 4.5 | 81.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.32% |
| 2 | 1-0 | 10.12% |
| 3 | 2-0 | 9.90% |
| 4 | 1-1 | 9.61% |
| 5 | 3-1 | 6.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 61.3% | 69.6% | 1.48 | -9.2% |
| Draw | 20.5% | 17.1% | 5.30 | +8.7% |
| Auxerre win | 18.1% | 13.3% | 7.50 | +36.1% |
| Over 2.5 | 58.8% | 64.6% | 1.51 | -11.2% |
| Under 2.5 | 41.2% | 35.4% | 2.61 | +7.5% |

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
| Market best home last update utc | 2026-10-09T13:47:15Z |
| Market best draw last update utc | 2026-10-09T13:49:26Z |
| Market best away last update utc | 2026-10-09T13:48:53Z |
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
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.77 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.27 |
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
| Reference home odds | 1.38 |
| Reference draw odds | 4.80 |
| Reference away odds | 6.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Home probability edge | -8.3% |
| Draw probability edge | +3.4% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.1650 |
| Raw ev home | -0.2143 |
| Raw edge prob draw | 0.0681 |
| Raw ev draw | 0.2677 |
| Raw edge prob away | 0.0969 |
| Raw ev away | 0.7245 |

</details>


---

## 2026-10-11 — Troyes vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **62.8%**. Expected goals are 0.92 for Troyes and 2.68 for Marseille (3.60 combined). The most likely exact score is 1-1 at 8.8%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 67.4%; Under 4.5 goals: 72.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 17.7% | 5.66 |
| Draw | 19.5% | 5.12 |
| Marseille win | 62.8% | 1.59 |

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
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.5% |
| Under 4.5 | 72.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.83% |
| 2 | 0-2 | 8.29% |
| 3 | 1-2 | 7.65% |
| 4 | 0-3 | 7.40% |
| 5 | 1-3 | 6.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 17.7% | 25.2% | 4.03 | -28.8% |
| Draw | 19.5% | 23.4% | 4.05 | -21.0% |
| Marseille win | 62.8% | 51.4% | 2.00 | +25.6% |
| Over 2.5 | 67.4% | 61.2% | 1.65 | +11.1% |
| Under 2.5 | 32.6% | 38.8% | 2.45 | -20.0% |

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
| Market best home last update utc | 2026-10-09T13:47:15Z |
| Market best draw last update utc | 2026-10-09T13:47:15Z |
| Market best away last update utc | 2026-10-09T13:49:26Z |
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
| P btts yes | 58.5% |
| P btts no | 41.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.10 |
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
| Reference home odds | 3.50 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.83 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.41 |
| Home probability edge | -7.5% |
| Draw probability edge | -3.8% |
| Away probability edge | +11.4% |
| Over 2.5 probability edge | +6.2% |
| Under 2.5 probability edge | -6.2% |
| Raw edge prob home | -0.1508 |
| Raw ev home | -0.5922 |
| Raw edge prob draw | -0.0769 |
| Raw ev draw | -0.3653 |
| Raw edge prob away | 0.2277 |
| Raw ev away | 0.4842 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T13:48:37Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 62.1% |
| Market under 3 5 odds | 1.57 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T13:49:09Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 62.7% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T13:49:10Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.53 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-16 — Le Mans FC vs Toulouse

The model's most likely 1X2 outcome is **Le Mans FC win** at **39.2%**. Expected goals are 1.87 for Le Mans FC and 1.51 for Toulouse (3.37 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 65.0%; Under 4.5 goals: 75.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 39.2% | 2.55 |
| Draw | 24.6% | 4.07 |
| Toulouse win | 36.3% | 2.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Mans FC expected goals | 1.87 |
| Toulouse expected goals | 1.51 |
| Expected total goals | 3.37 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.0% |
| Under 2.5 | 35.0% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.65% |
| 2 | 1-2 | 8.54% |
| 3 | 2-1 | 7.70% |
| 4 | 2-2 | 7.12% |
| 5 | 0-1 | 5.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 39.2% | 32.6% | 3.30 | +29.2% |
| Draw | 24.6% | 25.7% | 3.60 | -11.6% |
| Toulouse win | 36.3% | 41.7% | 2.34 | -15.1% |
| Over 2.5 | 65.0% | 55.2% | 1.84 | +19.6% |
| Under 2.5 | 35.0% | 44.8% | 2.12 | -25.8% |

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
| Market best home last update utc | 2026-10-09T13:48:53Z |
| Market best draw last update utc | 2026-10-09T13:48:53Z |
| Market best away last update utc | 2026-10-09T13:47:15Z |
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
| P btts yes | 66.7% |
| P btts no | 33.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.22 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.82 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.05 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 45.7% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 30.9% |
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 66.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.75 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | +6.6% |
| Draw probability edge | -1.2% |
| Away probability edge | -5.4% |
| Over 2.5 probability edge | +9.8% |
| Under 2.5 probability edge | -9.8% |
| Raw edge prob home | 0.1319 |
| Raw ev home | 0.5097 |
| Raw edge prob draw | -0.0235 |
| Raw ev draw | -0.1580 |
| Raw edge prob away | -0.1084 |
| Raw ev away | -0.2778 |
| Market p over 1 5 | 78.0% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T13:49:10Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 68.2% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T13:49:09Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.86 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 59.8% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T13:49:10Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **58.5%**. Expected goals are 1.76 for Lille and 0.94 for Brest (2.70 combined). The most likely exact score is 1-0 at 11.7%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 51.3%; Under 4.5 goals: 86.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 58.5% | 1.71 |
| Draw | 23.0% | 4.34 |
| Brest win | 18.4% | 5.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.76 |
| Brest expected goals | 0.94 |
| Expected total goals | 2.70 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
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
| 1 | 1-0 | 11.73% |
| 2 | 1-1 | 10.99% |
| 3 | 2-0 | 10.84% |
| 4 | 2-1 | 10.22% |
| 5 | 0-0 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 58.5% | 61.0% | 1.66 | -2.9% |
| Draw | 23.0% | 21.5% | 4.37 | +0.7% |
| Brest win | 18.4% | 17.5% | 5.50 | +1.5% |
| Over 2.5 | 51.3% | 57.6% | 1.74 | -10.7% |
| Under 2.5 | 48.7% | 42.4% | 2.27 | +10.5% |

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
| Market best home last update utc | 2026-10-09T13:47:15Z |
| Market best draw last update utc | 2026-10-09T13:47:15Z |
| Market best away last update utc | 2026-10-09T13:48:53Z |
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
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.61 |
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
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.55 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.70 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | -2.5% |
| Draw probability edge | +1.5% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.0499 |
| Raw ev home | -0.0702 |
| Raw edge prob draw | 0.0300 |
| Raw ev draw | 0.0728 |
| Raw edge prob away | 0.0198 |
| Raw ev away | 0.0691 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **63.7%**. Expected goals are 1.23 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.9%; Under 4.5 goals: 74.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.5% | 5.72 |
| Draw | 18.8% | 5.31 |
| Paris Saint Germain win | 63.7% | 1.57 |

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
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.86% |
| 2 | 0-2 | 8.85% |
| 3 | 1-1 | 8.42% |
| 4 | 0-1 | 7.88% |
| 5 | 1-3 | 7.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.5% | 13.7% | 6.73 | +17.7% |
| Draw | 18.8% | 15.9% | 5.70 | +7.4% |
| Paris Saint Germain win | 63.7% | 70.4% | 1.46 | -7.0% |
| Over 2.5 | 65.9% | 74.0% | 1.33 | -12.4% |
| Under 2.5 | 34.1% | 26.0% | 3.42 | +16.6% |

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
| Market best home last update utc | 2026-10-09T13:47:15Z |
| Market best draw last update utc | 2026-10-09T13:48:52Z |
| Market best away last update utc | 2026-10-09T13:47:15Z |
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
| P btts yes | 61.6% |
| P btts no | 38.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.43 |
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
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 5.70 |
| Reference draw odds | 5.00 |
| Reference away odds | 1.36 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.31 |
| Reference Under 2.5 odds | 3.35 |
| Home probability edge | +3.8% |
| Draw probability edge | +2.9% |
| Away probability edge | -6.7% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | 0.0758 |
| Raw ev home | 0.4321 |
| Raw edge prob draw | 0.0585 |
| Raw ev draw | 0.2402 |
| Raw edge prob away | -0.1342 |
| Raw ev away | -0.1683 |
| Market p over 1 5 | 95.5% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T13:49:10Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 7.20 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 47.8% |
| Market under 3 5 odds | 2.06 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T13:49:35Z |
| Market reference under 3 5 odds | 2.06 |
| Market reference under 3 5 opposite odds | 1.89 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 64.5% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T13:49:10Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.60 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **62.4%**. Expected goals are 0.78 for Troyes and 2.31 for RC Lens (3.09 combined). The most likely exact score is 0-2 at 10.6%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.9%; Under 4.5 goals: 81.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 16.9% | 5.92 |
| Draw | 20.7% | 4.84 |
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
| 2 | 1-1 | 9.84% |
| 3 | 0-1 | 8.81% |
| 4 | 1-2 | 8.30% |
| 5 | 0-3 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 16.9% | 23.2% | 4.30 | -27.3% |
| Draw | 20.7% | 23.2% | 4.10 | -15.2% |
| RC Lens win | 62.4% | 53.6% | 1.87 | +16.7% |
| Over 2.5 | 57.9% | 61.6% | 1.64 | -5.1% |
| Under 2.5 | 42.1% | 38.4% | 2.48 | +4.5% |

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
| Market best home last update utc | 2026-10-09T13:47:15Z |
| Market best draw last update utc | 2026-10-09T13:48:53Z |
| Market best away last update utc | 2026-10-09T13:47:15Z |
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
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.67 |
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
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.70 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.75 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -6.3% |
| Draw probability edge | -2.5% |
| Away probability edge | +8.9% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | -0.1264 |
| Raw ev home | -0.5449 |
| Raw edge prob draw | -0.0508 |
| Raw ev draw | -0.2563 |
| Raw edge prob away | 0.1772 |
| Raw ev away | 0.3329 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **49.2%**. Expected goals are 0.95 for Angers and 1.65 for Marseille (2.59 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 47.9%; Under 4.5 goals: 87.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 25.4% | 3.94 |
| Draw | 25.4% | 3.94 |
| Marseille win | 49.2% | 2.03 |

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
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.09% |
| 2 | 0-1 | 10.83% |
| 3 | 0-2 | 9.38% |
| 4 | 1-2 | 8.88% |
| 5 | 0-0 | 7.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 25.4% | 29.7% | 3.30 | -16.3% |
| Draw | 25.4% | 25.1% | 3.80 | -3.5% |
| Marseille win | 49.2% | 45.2% | 2.28 | +12.3% |
| Over 2.5 | 47.9% | 60.4% | 1.68 | -19.5% |
| Under 2.5 | 52.1% | 39.6% | 2.40 | +25.0% |

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
| Market best home last update utc | 2026-10-09T13:48:52Z |
| Market best draw last update utc | 2026-10-09T13:48:53Z |
| Market best away last update utc | 2026-10-09T13:47:15Z |
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
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.05 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | -4.3% |
| Draw probability edge | +0.3% |
| Away probability edge | +4.0% |
| Over 2.5 probability edge | -12.5% |
| Under 2.5 probability edge | +12.5% |
| Raw edge prob home | -0.0869 |
| Raw ev home | -0.3064 |
| Raw edge prob draw | 0.0068 |
| Raw ev draw | -0.0220 |
| Raw edge prob away | 0.0800 |
| Raw ev away | 0.2140 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **37.3%**. Expected goals are 1.16 for Le Havre and 1.19 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 42.0%; Under 4.5 goals: 91.0%.

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
| Over 2.5 | 42.0% | 50.7% | 1.94 | -18.6% |
| Under 2.5 | 58.0% | 49.3% | 2.00 | +16.0% |

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
| Market best home last update utc | 2026-10-09T13:47:15Z |
| Market best draw last update utc | 2026-10-09T13:48:53Z |
| Market best away last update utc | 2026-10-09T13:47:15Z |
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
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.90 |
| Home probability edge | -2.8% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | -0.0563 |
| Raw ev home | -0.1318 |
| Raw edge prob draw | 0.0244 |
| Raw ev draw | 0.0440 |
| Raw edge prob away | 0.0320 |
| Raw ev away | 0.0843 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **47.4%**. Expected goals are 1.36 for Lorient and 1.84 for AS Monaco (3.21 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 61.7%; Under 4.5 goals: 78.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 27.8% | 3.60 |
| Draw | 24.8% | 4.03 |
| AS Monaco win | 47.4% | 2.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.36 |
| AS Monaco expected goals | 1.84 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 61.7% |
| Under 2.5 | 38.3% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.8% |
| Under 4.5 | 78.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.18% |
| 2 | 1-2 | 9.20% |
| 3 | 2-1 | 6.90% |
| 4 | 0-1 | 6.82% |
| 5 | 0-2 | 6.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 27.8% | 27.7% | 3.65 | +1.3% |
| Draw | 24.8% | 25.9% | 3.60 | -10.7% |
| AS Monaco win | 47.4% | 46.5% | 2.17 | +2.9% |
| Over 2.5 | 61.7% | 51.9% | 1.92 | +18.6% |
| Under 2.5 | 38.3% | 48.1% | 2.02 | -22.7% |

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
| Market best home last update utc | 2026-10-09T13:48:53Z |
| Market best draw last update utc | 2026-10-09T13:48:53Z |
| Market best away last update utc | 2026-10-09T13:47:15Z |
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
| P btts yes | 63.4% |
| P btts no | 36.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.90 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.03 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.58 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 27.9% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 48.4% |
| Raw p over 1 5 | 83.5% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 63.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.20 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | +0.1% |
| Draw probability edge | -1.1% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | +9.9% |
| Under 2.5 probability edge | -9.9% |
| Raw edge prob home | 0.0021 |
| Raw ev home | 0.0171 |
| Raw edge prob draw | -0.0210 |
| Raw ev draw | -0.1446 |
| Raw edge prob away | 0.0189 |
| Raw ev away | 0.0497 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **56.5%**. Expected goals are 1.78 for Lyon and 1.08 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 55.0%; Under 4.5 goals: 83.6%.

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
| Over 2.5 | 55.0% | 57.6% | 1.78 | -2.1% |
| Under 2.5 | 45.0% | 42.4% | 2.25 | +1.3% |

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
| Market best home last update utc | 2026-10-09T13:47:15Z |
| Market best draw last update utc | 2026-10-09T13:48:52Z |
| Market best away last update utc | 2026-10-09T13:47:15Z |
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
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | -3.3% |
| Draw probability edge | +1.1% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -2.6% |
| Under 2.5 probability edge | +2.6% |
| Raw edge prob home | -0.0662 |
| Raw ev home | -0.0912 |
| Raw edge prob draw | 0.0219 |
| Raw ev draw | 0.0272 |
| Raw edge prob away | 0.0444 |
| Raw ev away | 0.1736 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **43.1%**. Expected goals are 1.62 for Paris FC and 1.36 for Rennes (2.98 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.1%; Under 4.5 goals: 82.0%.

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
| Paris FC win | 43.1% | 43.0% | 2.38 | +2.6% |
| Draw | 25.7% | 26.0% | 3.50 | -10.2% |
| Rennes win | 31.2% | 31.0% | 3.29 | +2.7% |
| Over 2.5 | 57.1% | 58.6% | 1.72 | -1.9% |
| Under 2.5 | 42.9% | 41.4% | 2.30 | -1.2% |

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
| Market best home last update utc | 2026-10-09T13:49:26Z |
| Market best draw last update utc | 2026-10-09T13:49:25Z |
| Market best away last update utc | 2026-10-09T13:47:15Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 888sport |
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
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.22 |
| Home probability edge | +0.1% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | 0.0013 |
| Raw ev home | 0.0277 |
| Raw edge prob draw | -0.0066 |
| Raw ev draw | -0.1134 |
| Raw edge prob away | 0.0052 |
| Raw ev away | 0.0359 |

</details>


---
