# UEFA Champions League — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 521 |
| Training data through | 2026-09-10 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1560.624 |
| Base scoring parameter | 0.154 |
| Home-advantage parameter | 0.271 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0 |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 24.00 |
| Additional event odds calls budget | 24.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-13 — Arsenal vs Lille

The model's most likely 1X2 outcome is **Arsenal win** at **71.7%**. Expected goals are 2.01 for Arsenal and 0.77 for Lille (2.78 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 53.6%; Under 4.5 goals: 84.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 71.7% | 1.39 |
| Draw | 17.9% | 5.58 |
| Lille win | 10.4% | 9.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 2.01 |
| Lille expected goals | 0.77 |
| Expected total goals | 2.78 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 76.9% |
| Under 1.5 | 23.1% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.85% |
| 2 | 2-0 | 13.41% |
| 3 | 2-1 | 10.35% |
| 4 | 3-0 | 9.00% |
| 5 | 1-1 | 8.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 71.7% | 76.5% | 1.30 | -6.8% |
| Draw | 17.9% | 16.6% | 6.80 | +21.9% |
| Lille win | 10.4% | 6.9% | 15.00 | +55.6% |
| Over 2.5 | 53.6% | 59.2% | 1.67 | -10.4% |
| Under 2.5 | 46.4% | 40.8% | 2.44 | +13.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 93177465a42a0fb7802f1c8b06d6ee3a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:37Z |
| Market best draw last update utc | 2026-10-09T07:42:09Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 45.5% |
| P btts no | 54.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.83 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.33 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.47 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 19.2% |
| Unadjusted away-win probability | 13.9% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.30 |
| Reference draw odds | 5.81 |
| Reference away odds | 13.80 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -4.8% |
| Draw probability edge | +1.3% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | -0.0963 |
| Raw ev home | -0.1305 |
| Raw edge prob draw | 0.0264 |
| Raw ev draw | 0.3089 |
| Raw edge prob away | 0.0700 |
| Raw ev away | 1.0803 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **60.1%**. Expected goals are 3.87 for Atlético Madrid and 1.70 for Manchester United (5.57 combined). The most likely exact score is 2-2 at 6.6%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 90.0%; Under 4.5 goals: 37.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 60.1% | 1.66 |
| Draw | 18.2% | 5.51 |
| Manchester United win | 21.7% | 4.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 3.87 |
| Manchester United expected goals | 1.70 |
| Expected total goals | 5.57 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.0% |
| Under 1.5 | 3.0% |
| Over 2.5 | 90.0% |
| Under 2.5 | 10.0% |
| Over 3.5 | 78.9% |
| Under 3.5 | 21.1% |
| Over 4.5 | 62.2% |
| Under 4.5 | 37.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.56% |
| 2 | 3-1 | 4.95% |
| 3 | 3-3 | 4.80% |
| 4 | 4-1 | 4.78% |
| 5 | 3-2 | 4.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 60.1% | 44.1% | 2.24 | +34.7% |
| Draw | 18.2% | 24.9% | 4.20 | -23.7% |
| Manchester United win | 21.7% | 31.0% | 3.40 | -26.2% |
| Over 2.5 | 90.0% | 64.7% | 1.50 | +34.9% |
| Under 2.5 | 10.0% | 35.3% | 2.63 | -73.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | a9c22e08b395ee5753c8a65bc0eb97cf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:37Z |
| Market best draw last update utc | 2026-10-09T07:42:23Z |
| Market best away last update utc | 2026-10-09T07:42:09Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 82.2% |
| P btts no | 17.8% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 246.56 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 33.02 |
| Fair Over 2.5 odds | 1.11 |
| Fair Under 2.5 odds | 9.96 |
| Fair Over 3.5 odds | 1.27 |
| Fair Under 3.5 odds | 4.74 |
| Fair Over 4.5 odds | 1.61 |
| Fair Under 4.5 odds | 2.65 |
| Unadjusted home-win probability | 76.2% |
| Unadjusted draw probability | 11.5% |
| Unadjusted away-win probability | 12.4% |
| Raw p over 1 5 | 97.4% |
| Raw p under 3 5 | 19.4% |
| Raw p btts yes | 80.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.24 |
| Reference draw odds | 3.94 |
| Reference away odds | 3.17 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.63 |
| Home probability edge | +16.0% |
| Draw probability edge | -6.7% |
| Away probability edge | -9.3% |
| Over 2.5 probability edge | +25.3% |
| Under 2.5 probability edge | -25.3% |
| Raw edge prob home | 0.3204 |
| Raw ev home | 0.7058 |
| Raw edge prob draw | -0.1341 |
| Raw ev draw | -0.5188 |
| Raw edge prob away | -0.1862 |
| Raw ev away | -0.5787 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **65.5%**. Expected goals are 1.61 for Galatasaray and 2.47 for Barcelona (4.09 combined). The most likely exact score is 1-2 at 9.5%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 78.2%; Under 4.5 goals: 60.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 17.9% | 5.59 |
| Draw | 16.6% | 6.04 |
| Barcelona win | 65.5% | 1.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.61 |
| Barcelona expected goals | 2.47 |
| Expected total goals | 4.09 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 91.4% |
| Under 1.5 | 8.6% |
| Over 2.5 | 78.2% |
| Under 2.5 | 21.8% |
| Over 3.5 | 59.0% |
| Under 3.5 | 41.0% |
| Over 4.5 | 39.6% |
| Under 4.5 | 60.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.54% |
| 2 | 1-3 | 7.86% |
| 3 | 2-3 | 6.35% |
| 4 | 2-2 | 6.08% |
| 5 | 0-2 | 5.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 17.9% | 11.0% | 9.50 | +70.1% |
| Draw | 16.6% | 14.9% | 7.40 | +22.6% |
| Barcelona win | 65.5% | 74.1% | 1.34 | -12.2% |
| Over 2.5 | 78.2% | 81.0% | 1.21 | -5.4% |
| Under 2.5 | 21.8% | 19.0% | 4.50 | -1.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | dd431688ed5c8f383b6434fd4f01e883 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:37Z |
| Market best draw last update utc | 2026-10-09T07:42:09Z |
| Market best away last update utc | 2026-10-09T07:42:37Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 72.3% |
| P btts no | 27.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 82.09 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.67 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.58 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.44 |
| Fair Over 4.5 odds | 2.52 |
| Fair Under 4.5 odds | 1.66 |
| Unadjusted home-win probability | 24.9% |
| Unadjusted draw probability | 18.2% |
| Unadjusted away-win probability | 56.9% |
| Raw p over 1 5 | 91.1% |
| Raw p under 3 5 | 41.6% |
| Raw p btts yes | 73.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 8.70 |
| Reference draw odds | 6.44 |
| Reference away odds | 1.34 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.21 |
| Reference Under 2.5 odds | 4.50 |
| Home probability edge | +6.9% |
| Draw probability edge | +1.7% |
| Away probability edge | -8.6% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | 0.1390 |
| Raw ev home | 1.3611 |
| Raw edge prob draw | 0.0333 |
| Raw ev draw | 0.3490 |
| Raw edge prob away | -0.1723 |
| Raw ev away | -0.2373 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **68.2%**. Expected goals are 1.98 for Inter Milan and 1.01 for Club Brugge (2.99 combined). The most likely exact score is 1-0 at 11.8%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 58.6%; Under 4.5 goals: 81.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 68.2% | 1.47 |
| Draw | 18.2% | 5.51 |
| Club Brugge win | 13.7% | 7.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.98 |
| Club Brugge expected goals | 1.01 |
| Expected total goals | 2.99 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 58.6% |
| Under 2.5 | 41.4% |
| Over 3.5 | 35.8% |
| Under 3.5 | 64.2% |
| Over 4.5 | 18.9% |
| Under 4.5 | 81.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.83% |
| 2 | 2-1 | 11.21% |
| 3 | 2-0 | 11.16% |
| 4 | 1-1 | 8.52% |
| 5 | 3-1 | 7.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 68.2% | 75.8% | 1.31 | -10.7% |
| Draw | 18.2% | 15.9% | 6.40 | +16.2% |
| Club Brugge win | 13.7% | 8.2% | 11.50 | +57.2% |
| Over 2.5 | 58.6% | 65.1% | 1.50 | -12.1% |
| Under 2.5 | 41.4% | 34.9% | 2.66 | +10.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | ca3f4b075d835413f9cb7bd3c439fdd0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:37Z |
| Market best draw last update utc | 2026-10-09T07:42:09Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 53.2% |
| P btts no | 46.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.66 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.03 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.28 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 65.0% |
| Raw p btts yes | 54.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.31 |
| Reference draw odds | 5.99 |
| Reference away odds | 11.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.66 |
| Home probability edge | -7.6% |
| Draw probability edge | +2.2% |
| Away probability edge | +5.4% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.1528 |
| Raw ev home | -0.2070 |
| Raw edge prob draw | 0.0441 |
| Raw ev draw | 0.3030 |
| Raw edge prob away | 0.1086 |
| Raw ev away | 1.1970 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **41.2%**. Expected goals are 1.58 for RB Leipzig and 1.78 for PSV Eindhoven (3.36 combined). The most likely exact score is 1-1 at 9.7%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 64.9%; Under 4.5 goals: 75.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 41.2% | 2.43 |
| Draw | 22.6% | 4.43 |
| PSV Eindhoven win | 36.2% | 2.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.58 |
| PSV Eindhoven expected goals | 1.78 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 84.3% |
| Under 1.5 | 15.7% |
| Over 2.5 | 64.9% |
| Under 2.5 | 35.1% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.6% |
| Under 4.5 | 75.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.66% |
| 2 | 2-1 | 9.10% |
| 3 | 1-2 | 7.26% |
| 4 | 2-2 | 7.15% |
| 5 | 1-0 | 7.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 41.2% | 47.5% | 2.08 | -14.3% |
| Draw | 22.6% | 23.5% | 4.30 | -2.8% |
| PSV Eindhoven win | 36.2% | 29.0% | 3.50 | +26.7% |
| Over 2.5 | 64.9% | 70.0% | 1.39 | -9.8% |
| Under 2.5 | 35.1% | 30.0% | 3.03 | +6.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | da9e9e9eb9a238ed97827c4a8fbe6044 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:37Z |
| Market best draw last update utc | 2026-10-09T07:42:23Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.8% |
| P btts no | 34.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.15 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.36 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.85 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.07 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 34.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 43.4% |
| Raw p over 1 5 | 84.4% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.08 |
| Reference draw odds | 4.16 |
| Reference away odds | 3.38 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.03 |
| Home probability edge | -6.3% |
| Draw probability edge | -0.9% |
| Away probability edge | +7.2% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.1262 |
| Raw ev home | -0.2744 |
| Raw edge prob draw | -0.0179 |
| Raw ev draw | -0.0669 |
| Raw edge prob away | 0.1441 |
| Raw ev away | 0.5195 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **42.2%**. Expected goals are 1.25 for RC Lens and 1.66 for Sporting Lisbon (2.91 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 55.1%; Under 4.5 goals: 83.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 33.6% | 2.98 |
| Draw | 24.2% | 4.12 |
| Sporting Lisbon win | 42.2% | 2.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.25 |
| Sporting Lisbon expected goals | 1.66 |
| Expected total goals | 2.91 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 77.9% |
| Under 1.5 | 22.1% |
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 33.0% |
| Under 3.5 | 67.0% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.30% |
| 2 | 0-1 | 8.52% |
| 3 | 1-0 | 8.40% |
| 4 | 1-2 | 8.33% |
| 5 | 2-1 | 8.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 33.6% | 37.6% | 2.63 | -11.7% |
| Draw | 24.2% | 25.5% | 3.90 | -5.4% |
| Sporting Lisbon win | 42.2% | 36.9% | 2.70 | +13.9% |
| Over 2.5 | 55.1% | 60.2% | 1.64 | -9.6% |
| Under 2.5 | 44.9% | 39.8% | 2.46 | +10.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T16:45:00+00:00 |
| Fixture id | 2b0a946cac613732fcbf57ce931490a1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:22Z |
| Market best draw last update utc | 2026-10-09T07:42:09Z |
| Market best away last update utc | 2026-10-09T07:42:23Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Sporting Clube de Portugal |
| Home-name matching confidence | 86/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.49 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.03 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.98 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 47.5% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 66.7% |
| Raw p btts yes | 57.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.62 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.67 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Home probability edge | -4.1% |
| Draw probability edge | -1.2% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.0814 |
| Raw ev home | -0.2244 |
| Raw edge prob draw | -0.0243 |
| Raw ev draw | -0.1018 |
| Raw edge prob away | 0.1057 |
| Raw ev away | 0.2819 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **54.0%**. Expected goals are 0.37 for Sabah FK and 1.26 for Slavia Praha (1.63 combined). The most likely exact score is 0-1 at 22.7%. Goal-market probabilities: at least one goal: 82.1%; Over 2.5 goals: 22.1%; Under 4.5 goals: 97.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 18.8% | 5.31 |
| Draw | 27.2% | 3.68 |
| Slavia Praha win | 54.0% | 1.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.37 |
| Slavia Praha expected goals | 1.26 |
| Expected total goals | 1.63 |
| Over 0.5 | 82.1% |
| Under 0.5 | 17.9% |
| Over 1.5 | 46.5% |
| Under 1.5 | 53.5% |
| Over 2.5 | 22.1% |
| Under 2.5 | 77.9% |
| Over 3.5 | 7.9% |
| Under 3.5 | 92.1% |
| Over 4.5 | 2.4% |
| Under 4.5 | 97.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.74% |
| 2 | 0-0 | 17.93% |
| 3 | 0-2 | 14.01% |
| 4 | 1-0 | 12.79% |
| 5 | 1-1 | 8.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 18.8% | 26.2% | 3.74 | -29.6% |
| Draw | 27.2% | 25.4% | 4.00 | +8.8% |
| Slavia Praha win | 54.0% | 48.5% | 2.04 | +10.1% |
| Over 2.5 | 22.1% | 57.7% | 1.71 | -62.2% |
| Under 2.5 | 77.9% | 42.3% | 2.32 | +80.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T16:45:00+00:00 |
| Fixture id | 46f726554e6876fb828c767bfbfdfdad |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:37Z |
| Market best draw last update utc | 2026-10-09T07:42:23Z |
| Market best away last update utc | 2026-10-09T07:42:09Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 21.7% |
| P btts no | 78.3% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.58 |
| Fair Over 1.5 odds | 2.15 |
| Fair Under 1.5 odds | 1.87 |
| Fair Over 2.5 odds | 4.53 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 12.72 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 41.10 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 11.5% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 59.5% |
| Raw p over 1 5 | 48.0% |
| Raw p under 3 5 | 91.7% |
| Raw p btts yes | 21.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.74 |
| Reference draw odds | 3.86 |
| Reference away odds | 2.04 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | -7.4% |
| Draw probability edge | +1.8% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | -35.7% |
| Under 2.5 probability edge | +35.7% |
| Raw edge prob home | -0.1470 |
| Raw ev home | -0.5708 |
| Raw edge prob draw | 0.0367 |
| Raw ev draw | 0.1611 |
| Raw edge prob away | 0.1103 |
| Raw ev away | 0.2137 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **92.3%**. Expected goals are 0.69 for Viking FK and 4.47 for Bayern Munich (5.16 combined). The most likely exact score is 0-4 at 9.5%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.2%; Under 4.5 goals: 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 2.7% | 36.38 |
| Draw | 5.0% | 20.05 |
| Bayern Munich win | 92.3% | 1.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.69 |
| Bayern Munich expected goals | 4.47 |
| Expected total goals | 5.16 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.1% |
| Under 1.5 | 3.9% |
| Over 2.5 | 88.2% |
| Under 2.5 | 11.8% |
| Over 3.5 | 74.9% |
| Under 3.5 | 25.1% |
| Over 4.5 | 57.7% |
| Under 4.5 | 42.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.45% |
| 2 | 0-3 | 8.46% |
| 3 | 0-5 | 8.44% |
| 4 | 1-4 | 6.51% |
| 5 | 0-6 | 6.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 2.7% | 3.6% | 27.00 | -25.8% |
| Draw | 5.0% | 5.8% | 15.50 | -22.7% |
| Bayern Munich win | 92.3% | 90.6% | 1.11 | +2.4% |
| Over 2.5 | 88.2% | 85.4% | 1.15 | +1.4% |
| Under 2.5 | 11.8% | 14.6% | 5.70 | -32.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 8a9d20b23417357011c10585a99335e9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:40:53Z |
| Market best draw last update utc | 2026-10-09T07:42:37Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 49.6% |
| P btts no | 50.4% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 168.96 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 25.53 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.44 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.98 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 1.9% |
| Unadjusted draw probability | 4.1% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.3% |
| Raw p under 3 5 | 24.5% |
| Raw p btts yes | 49.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 25.00 |
| Reference draw odds | 15.50 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.54 |
| Home probability edge | -0.8% |
| Draw probability edge | -0.9% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | +2.7% |
| Under 2.5 probability edge | -2.7% |
| Raw edge prob home | -0.0162 |
| Raw ev home | -0.4769 |
| Raw edge prob draw | -0.0171 |
| Raw ev draw | -0.3593 |
| Raw edge prob away | 0.0333 |
| Raw ev away | 0.0426 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **40.6%**. Expected goals are 0.87 for Villarreal and 1.43 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 39.8%; Under 4.5 goals: 91.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 33.2% | 3.01 |
| Draw | 26.2% | 3.81 |
| Napoli win | 40.6% | 2.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.87 |
| Napoli expected goals | 1.43 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 39.8% |
| Under 2.5 | 60.2% |
| Over 3.5 | 19.5% |
| Under 3.5 | 80.5% |
| Over 4.5 | 8.1% |
| Under 4.5 | 91.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.12% |
| 2 | 1-1 | 12.11% |
| 3 | 0-1 | 11.91% |
| 4 | 0-0 | 9.54% |
| 5 | 0-2 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 33.2% | 42.8% | 2.33 | -22.7% |
| Draw | 26.2% | 26.8% | 3.85 | +1.0% |
| Napoli win | 40.6% | 30.4% | 3.25 | +31.9% |
| Over 2.5 | 39.8% | 55.8% | 1.77 | -29.6% |
| Under 2.5 | 60.2% | 44.2% | 2.22 | +33.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 09e41b63d1d59bd4d971c54ffce154d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:09Z |
| Market best draw last update utc | 2026-10-09T07:42:23Z |
| Market best away last update utc | 2026-10-09T07:42:22Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.1% |
| P btts no | 55.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.48 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.51 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.12 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.29 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 23.6% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 50.7% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 79.8% |
| Raw p btts yes | 43.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.31 |
| Reference draw odds | 3.66 |
| Reference away odds | 3.23 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Home probability edge | -9.6% |
| Draw probability edge | -0.6% |
| Away probability edge | +10.1% |
| Over 2.5 probability edge | -16.0% |
| Under 2.5 probability edge | +16.0% |
| Raw edge prob home | -0.1916 |
| Raw ev home | -0.4502 |
| Raw edge prob draw | -0.0113 |
| Raw ev draw | -0.0113 |
| Raw edge prob away | 0.2029 |
| Raw ev away | 0.6485 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **52.3%**. Expected goals are 1.26 for AS Roma and 1.83 for Real Madrid (3.09 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 59.5%; Under 4.5 goals: 80.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 24.9% | 4.02 |
| Draw | 22.8% | 4.38 |
| Real Madrid win | 52.3% | 1.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.26 |
| Real Madrid expected goals | 1.83 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 59.5% |
| Under 2.5 | 40.5% |
| Over 3.5 | 37.5% |
| Under 3.5 | 62.5% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.42% |
| 2 | 1-2 | 9.78% |
| 3 | 0-1 | 8.99% |
| 4 | 0-2 | 7.75% |
| 5 | 2-2 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 24.9% | 22.9% | 4.10 | +2.0% |
| Draw | 22.8% | 23.9% | 4.30 | -1.8% |
| Real Madrid win | 52.3% | 53.2% | 1.94 | +1.4% |
| Over 2.5 | 59.5% | 69.0% | 1.44 | -14.3% |
| Under 2.5 | 40.5% | 31.0% | 2.95 | +19.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | d4ef112438afa4c2cdbbfc9376a009c9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:40:53Z |
| Market best draw last update utc | 2026-10-09T07:42:09Z |
| Market best away last update utc | 2026-10-09T07:42:37Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.9% |
| P btts no | 40.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.84 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.27 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.67 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 5.00 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 51.3% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 62.6% |
| Raw p btts yes | 59.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 4.05 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.82 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | +2.0% |
| Draw probability edge | -1.0% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | 0.0392 |
| Raw ev home | 0.1008 |
| Raw edge prob draw | -0.0204 |
| Raw ev draw | -0.0620 |
| Raw edge prob away | -0.0189 |
| Raw ev away | -0.0040 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **66.4%**. Expected goals are 2.22 for Aston Villa and 0.60 for Fenerbahce (2.83 combined). The most likely exact score is 2-0 at 13.0%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 51.2%; Under 4.5 goals: 85.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 66.4% | 1.51 |
| Draw | 19.7% | 5.07 |
| Fenerbahce win | 13.9% | 7.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.22 |
| Fenerbahce expected goals | 0.60 |
| Expected total goals | 2.83 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 51.2% |
| Under 2.5 | 48.8% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.98% |
| 2 | 1-0 | 12.03% |
| 3 | 3-0 | 9.62% |
| 4 | 1-1 | 9.20% |
| 5 | 2-1 | 7.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 66.4% | 57.9% | 1.77 | +17.5% |
| Draw | 19.7% | 23.3% | 4.25 | -16.2% |
| Fenerbahce win | 13.9% | 18.8% | 5.40 | -25.1% |
| Over 2.5 | 51.2% | 58.1% | 1.74 | -10.9% |
| Under 2.5 | 48.8% | 41.9% | 2.28 | +11.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 3f3cb74e560dfcc3e795b667ed9ebdef |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:09Z |
| Market best draw last update utc | 2026-10-09T07:42:37Z |
| Market best away last update utc | 2026-10-09T07:42:09Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Unibet (NL) |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 41.4% |
| P btts no | 58.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.83 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.36 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.88 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.2% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 76.9% |
| Raw p under 3 5 | 68.6% |
| Raw p btts yes | 40.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.68 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.90 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | +8.5% |
| Draw probability edge | -3.5% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | 0.1693 |
| Raw ev home | 0.3252 |
| Raw edge prob draw | -0.0710 |
| Raw ev draw | -0.3129 |
| Raw edge prob away | -0.0983 |
| Raw ev away | -0.5162 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **47.5%**. Expected goals are 1.67 for Bodø/Glimt and 2.04 for Borussia Dortmund (3.70 combined). The most likely exact score is 1-2 at 8.6%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 71.2%; Under 4.5 goals: 68.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 30.8% | 3.25 |
| Draw | 21.8% | 4.60 |
| Borussia Dortmund win | 47.5% | 2.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 1.67 |
| Borussia Dortmund expected goals | 2.04 |
| Expected total goals | 3.70 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 88.1% |
| Under 1.5 | 11.9% |
| Over 2.5 | 71.2% |
| Under 2.5 | 28.8% |
| Over 3.5 | 50.7% |
| Under 3.5 | 49.3% |
| Over 4.5 | 31.1% |
| Under 4.5 | 68.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.58% |
| 2 | 1-1 | 8.46% |
| 3 | 2-2 | 7.56% |
| 4 | 2-1 | 6.61% |
| 5 | 1-3 | 5.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 30.8% | 29.1% | 3.30 | +1.6% |
| Draw | 21.8% | 23.1% | 4.30 | -6.5% |
| Borussia Dortmund win | 47.5% | 47.9% | 2.14 | +1.6% |
| Over 2.5 | 71.2% | 70.0% | 1.40 | -0.3% |
| Under 2.5 | 28.8% | 30.0% | 3.03 | -12.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | ca87a3874b0eae31b4173ae4a9324957 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:09Z |
| Market best draw last update utc | 2026-10-09T07:42:24Z |
| Market best away last update utc | 2026-10-09T07:42:37Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.4% |
| P btts no | 29.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.91 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.37 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.47 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.21 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 32.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 47.1% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 70.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 3.25 |
| Reference draw odds | 4.05 |
| Reference away odds | 2.02 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.03 |
| Home probability edge | +1.7% |
| Draw probability edge | -1.3% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | 0.0343 |
| Raw ev home | 0.0723 |
| Raw edge prob draw | -0.0265 |
| Raw ev draw | -0.1217 |
| Raw edge prob away | -0.0077 |
| Raw ev away | 0.0075 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **63.0%**. Expected goals are 1.84 for Feyenoord and 3.93 for Como (5.77 combined). The most likely exact score is 2-2 at 6.0%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 91.6%; Under 4.5 goals: 33.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 19.8% | 5.06 |
| Draw | 17.2% | 5.81 |
| Como win | 63.0% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 1.84 |
| Como expected goals | 3.93 |
| Expected total goals | 5.77 |
| Over 0.5 | 99.7% |
| Under 0.5 | 0.3% |
| Over 1.5 | 97.6% |
| Under 1.5 | 2.4% |
| Over 2.5 | 91.6% |
| Under 2.5 | 8.4% |
| Over 3.5 | 81.7% |
| Under 3.5 | 18.3% |
| Over 4.5 | 66.1% |
| Under 4.5 | 33.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.00% |
| 2 | 1-3 | 4.91% |
| 3 | 1-4 | 4.83% |
| 4 | 3-3 | 4.81% |
| 5 | 2-3 | 4.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 19.8% | 26.0% | 3.85 | -23.9% |
| Draw | 17.2% | 22.7% | 4.33 | -25.5% |
| Como win | 63.0% | 51.3% | 1.95 | +22.9% |
| Over 2.5 | 91.6% | 68.0% | 1.43 | +31.0% |
| Under 2.5 | 8.4% | 32.0% | 2.87 | -75.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T16:45:00+00:00 |
| Fixture id | 5d6f9accd6f79ae4216dfd29ccc342b2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:23Z |
| Market best draw last update utc | 2026-10-09T07:42:07Z |
| Market best away last update utc | 2026-10-09T07:42:09Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 83.9% |
| P btts no | 16.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 340.64 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 41.10 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 11.91 |
| Fair Over 3.5 odds | 1.22 |
| Fair Under 3.5 odds | 5.45 |
| Fair Over 4.5 odds | 1.51 |
| Fair Under 4.5 odds | 2.95 |
| Unadjusted home-win probability | 13.5% |
| Unadjusted draw probability | 11.7% |
| Unadjusted away-win probability | 74.8% |
| Raw p over 1 5 | 97.8% |
| Raw p under 3 5 | 17.3% |
| Raw p btts yes | 82.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.77 |
| Reference draw odds | 4.31 |
| Reference away odds | 1.93 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.87 |
| Home probability edge | -6.2% |
| Draw probability edge | -5.5% |
| Away probability edge | +11.7% |
| Over 2.5 probability edge | +23.6% |
| Under 2.5 probability edge | -23.6% |
| Raw edge prob home | -0.1248 |
| Raw ev home | -0.4795 |
| Raw edge prob draw | -0.1097 |
| Raw ev draw | -0.4924 |
| Raw edge prob away | 0.2345 |
| Raw ev away | 0.4578 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **72.8%**. Expected goals are 0.33 for LASK and 1.48 for Liverpool (1.80 combined). The most likely exact score is 0-1 at 26.9%. Goal-market probabilities: at least one goal: 87.1%; Over 2.5 goals: 28.8%; Under 4.5 goals: 96.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 7.5% | 13.41 |
| Draw | 19.7% | 5.07 |
| Liverpool win | 72.8% | 1.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.33 |
| Liverpool expected goals | 1.48 |
| Expected total goals | 1.80 |
| Over 0.5 | 87.1% |
| Under 0.5 | 12.9% |
| Over 1.5 | 55.1% |
| Under 1.5 | 44.9% |
| Over 2.5 | 28.8% |
| Under 2.5 | 71.2% |
| Over 3.5 | 11.5% |
| Under 3.5 | 88.5% |
| Over 4.5 | 3.9% |
| Under 4.5 | 96.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 26.86% |
| 2 | 0-2 | 19.52% |
| 3 | 0-0 | 12.86% |
| 4 | 0-3 | 9.61% |
| 5 | 1-2 | 6.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 7.5% | 6.6% | 13.00 | -3.1% |
| Draw | 19.7% | 14.8% | 7.25 | +42.9% |
| Liverpool win | 72.8% | 78.6% | 1.29 | -6.0% |
| Over 2.5 | 28.8% | 70.5% | 1.38 | -60.3% |
| Under 2.5 | 71.2% | 29.5% | 3.10 | +120.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T16:45:00+00:00 |
| Fixture id | 2903ee092f7e08c549b130a3d394ac3c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:40:53Z |
| Market best draw last update utc | 2026-10-09T07:42:11Z |
| Market best away last update utc | 2026-10-09T07:42:37Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 20.2% |
| P btts no | 79.8% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.78 |
| Fair Over 1.5 odds | 1.81 |
| Fair Under 1.5 odds | 2.23 |
| Fair Over 2.5 odds | 3.48 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.67 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 25.35 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 8.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 67.0% |
| Raw p over 1 5 | 53.4% |
| Raw p under 3 5 | 89.1% |
| Raw p btts yes | 21.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 12.50 |
| Reference draw odds | 5.90 |
| Reference away odds | 1.25 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.08 |
| Home probability edge | +0.9% |
| Draw probability edge | +4.9% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -41.7% |
| Under 2.5 probability edge | +41.7% |
| Raw edge prob home | 0.0174 |
| Raw ev home | 0.0827 |
| Raw edge prob draw | 0.0985 |
| Raw ev draw | 0.7856 |
| Raw edge prob away | -0.1159 |
| Raw ev away | -0.1352 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **46.6%**. Expected goals are 1.53 for Manchester City and 2.51 for Paris Saint Germain (4.04 combined). The most likely exact score is 2-2 at 7.6%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 75.5%; Under 4.5 goals: 63.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 32.5% | 3.08 |
| Draw | 20.9% | 4.78 |
| Paris Saint Germain win | 46.6% | 2.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.53 |
| Paris Saint Germain expected goals | 2.51 |
| Expected total goals | 4.04 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 90.3% |
| Under 1.5 | 9.7% |
| Over 2.5 | 75.5% |
| Under 2.5 | 24.5% |
| Over 3.5 | 56.3% |
| Under 3.5 | 43.7% |
| Over 4.5 | 36.5% |
| Under 4.5 | 63.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.60% |
| 2 | 1-1 | 7.52% |
| 3 | 2-1 | 7.36% |
| 4 | 1-2 | 6.67% |
| 5 | 1-3 | 5.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 32.5% | 42.1% | 2.34 | -23.9% |
| Draw | 20.9% | 24.0% | 4.30 | -10.0% |
| Paris Saint Germain win | 46.6% | 33.9% | 2.97 | +38.3% |
| Over 2.5 | 75.5% | 68.0% | 1.44 | +8.7% |
| Under 2.5 | 24.5% | 32.0% | 2.87 | -29.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 5a1a6a04c5561897741105e30d5d7ec4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:37Z |
| Market best draw last update utc | 2026-10-09T07:42:09Z |
| Market best away last update utc | 2026-10-09T07:42:37Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 72.9% |
| P btts no | 27.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 60.05 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.29 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 4.08 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.29 |
| Fair Over 4.5 odds | 2.74 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.6% |
| Raw p btts yes | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.28 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.80 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.87 |
| Home probability edge | -9.6% |
| Draw probability edge | -3.0% |
| Away probability edge | +12.6% |
| Over 2.5 probability edge | +7.5% |
| Under 2.5 probability edge | -7.5% |
| Raw edge prob home | -0.1920 |
| Raw ev home | -0.4641 |
| Raw edge prob draw | -0.0606 |
| Raw ev draw | -0.2301 |
| Raw edge prob away | 0.2526 |
| Raw ev away | 0.7580 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **65.2%**. Expected goals are 4.51 for Real Betis and 1.48 for Porto (5.98 combined). The most likely exact score is 2-2 at 6.1%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 91.3%; Under 4.5 goals: 33.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 65.2% | 1.53 |
| Draw | 17.0% | 5.90 |
| Porto win | 17.9% | 5.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 4.51 |
| Porto expected goals | 1.48 |
| Expected total goals | 5.98 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.5% |
| Under 1.5 | 2.5% |
| Over 2.5 | 91.3% |
| Under 2.5 | 8.7% |
| Over 3.5 | 81.7% |
| Under 3.5 | 18.3% |
| Over 4.5 | 66.1% |
| Under 4.5 | 33.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.11% |
| 2 | 4-1 | 4.91% |
| 3 | 3-3 | 4.51% |
| 4 | 5-1 | 4.43% |
| 5 | 3-1 | 4.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 65.2% | 44.8% | 2.27 | +47.9% |
| Draw | 17.0% | 26.1% | 3.80 | -35.6% |
| Porto win | 17.9% | 29.1% | 3.30 | -41.0% |
| Over 2.5 | 91.3% | 55.6% | 1.78 | +62.5% |
| Under 2.5 | 8.7% | 44.4% | 2.21 | -80.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 4c7f87780ae5ab8bec9e83d6d6ec9909 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:37Z |
| Market best draw last update utc | 2026-10-09T07:42:37Z |
| Market best away last update utc | 2026-10-09T07:42:09Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 79.8% |
| P btts no | 20.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 270.99 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 39.43 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 11.45 |
| Fair Over 3.5 odds | 1.22 |
| Fair Under 3.5 odds | 5.47 |
| Fair Over 4.5 odds | 1.51 |
| Fair Under 4.5 odds | 2.95 |
| Unadjusted home-win probability | 85.5% |
| Unadjusted draw probability | 7.8% |
| Unadjusted away-win probability | 6.7% |
| Raw p over 1 5 | 98.1% |
| Raw p under 3 5 | 15.4% |
| Raw p btts yes | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.15 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Home probability edge | +20.4% |
| Draw probability edge | -9.2% |
| Away probability edge | -11.2% |
| Over 2.5 probability edge | +35.7% |
| Under 2.5 probability edge | -35.7% |
| Raw edge prob home | 0.4070 |
| Raw ev home | 0.9415 |
| Raw edge prob draw | -0.1831 |
| Raw ev draw | -0.7037 |
| Raw edge prob away | -0.2239 |
| Raw ev away | -0.7797 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.4%**. Expected goals are 1.45 for Shakhtar Donetsk and 1.25 for AEK Athens (2.71 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 50.4%; Under 4.5 goals: 86.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.4% | 2.54 |
| Draw | 25.8% | 3.87 |
| AEK Athens win | 34.8% | 2.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.45 |
| AEK Athens expected goals | 1.25 |
| Expected total goals | 2.71 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.7% |
| Under 3.5 | 71.3% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.22% |
| 2 | 1-0 | 9.57% |
| 3 | 0-1 | 9.40% |
| 4 | 2-1 | 8.21% |
| 5 | 1-2 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.4% | 36.4% | 2.81 | +10.6% |
| Draw | 25.8% | 27.2% | 3.65 | -5.7% |
| AEK Athens win | 34.8% | 36.4% | 2.65 | -7.8% |
| Over 2.5 | 50.4% | 51.8% | 1.91 | -3.8% |
| Under 2.5 | 49.6% | 48.2% | 2.03 | +0.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 0f961390e790ad2c80ecb3f302cad4a6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:42:37Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:40:53Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 67/100 |
| P btts yes | 54.6% |
| P btts no | 45.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.59 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.33 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 42.4% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 54.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.62 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.62 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.98 |
| Home probability edge | +3.0% |
| Draw probability edge | -1.4% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | 0.0598 |
| Raw ev home | 0.1903 |
| Raw edge prob draw | -0.0284 |
| Raw ev draw | -0.1089 |
| Raw edge prob away | -0.0315 |
| Raw ev away | -0.1195 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **65.5%**. Expected goals are 1.40 for ŠK Slovan Bratislava and 2.20 for VfB Stuttgart (3.60 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 70.5%; Under 4.5 goals: 70.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 16.6% | 6.04 |
| Draw | 18.0% | 5.56 |
| VfB Stuttgart win | 65.5% | 1.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.40 |
| VfB Stuttgart expected goals | 2.20 |
| Expected total goals | 3.60 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 70.5% |
| Under 2.5 | 29.5% |
| Over 3.5 | 49.2% |
| Under 3.5 | 50.8% |
| Over 4.5 | 30.0% |
| Under 4.5 | 70.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.81% |
| 2 | 1-3 | 7.92% |
| 3 | 0-2 | 7.73% |
| 4 | 0-1 | 7.53% |
| 5 | 1-1 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 16.6% | 8.7% | 9.90 | +63.9% |
| Draw | 18.0% | 16.5% | 6.25 | +12.5% |
| VfB Stuttgart win | 65.5% | 74.8% | 1.35 | -11.6% |
| Over 2.5 | 70.5% | 70.5% | 1.38 | -2.7% |
| Under 2.5 | 29.5% | 29.5% | 3.08 | -9.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | d7576351b8cb2396e32cc3de0446f3de |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T07:40:53Z |
| Market best draw last update utc | 2026-10-09T07:42:11Z |
| Market best away last update utc | 2026-10-09T07:42:37Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.8% |
| P btts no | 34.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.64 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.96 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.39 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.97 |
| Fair Over 4.5 odds | 3.33 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 56.1% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 51.6% |
| Raw p btts yes | 66.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 9.70 |
| Reference draw odds | 5.35 |
| Reference away odds | 1.31 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.08 |
| Home probability edge | +7.9% |
| Draw probability edge | +1.5% |
| Away probability edge | -9.4% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.1570 |
| Raw ev home | 1.4158 |
| Raw edge prob draw | 0.0301 |
| Raw ev draw | 0.2189 |
| Raw edge prob away | -0.1871 |
| Raw ev away | -0.2427 |

</details>


---
