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

The model's most likely 1X2 outcome is **Arsenal win** at **72.8%**. Expected goals are 2.01 for Arsenal and 0.77 for Lille (2.78 combined). The most likely exact score is 1-0 at 14.1%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 54.1%; Under 4.5 goals: 84.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 72.8% | 1.37 |
| Draw | 16.5% | 6.05 |
| Lille win | 10.6% | 9.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 2.01 |
| Lille expected goals | 0.77 |
| Expected total goals | 2.78 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 77.0% |
| Under 1.5 | 23.0% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.07% |
| 2 | 2-0 | 13.63% |
| 3 | 2-1 | 10.51% |
| 4 | 3-0 | 9.14% |
| 5 | 1-1 | 7.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 72.8% | 78.8% | 1.30 | -5.3% |
| Draw | 16.5% | 13.8% | 6.80 | +12.5% |
| Lille win | 10.6% | 7.4% | 15.00 | +59.4% |
| Over 2.5 | 54.1% | 60.3% | 1.67 | -9.6% |
| Under 2.5 | 45.9% | 39.7% | 2.44 | +11.9% |

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
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.41 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.35 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.39 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 19.2% |
| Unadjusted away-win probability | 13.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.26 |
| Reference draw odds | 6.80 |
| Reference away odds | 12.50 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.44 |
| Home probability edge | -6.0% |
| Draw probability edge | +2.7% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.1190 |
| Raw ev home | -0.1305 |
| Raw edge prob draw | 0.0541 |
| Raw ev draw | 0.3089 |
| Raw edge prob away | 0.0649 |
| Raw ev away | 1.0803 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **60.8%**. Expected goals are 3.87 for Atlético Madrid and 1.70 for Manchester United (5.57 combined). The most likely exact score is 2-2 at 6.7%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 90.0%; Under 4.5 goals: 37.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 60.8% | 1.64 |
| Draw | 18.5% | 5.40 |
| Manchester United win | 20.7% | 4.83 |

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
| Over 3.5 | 79.0% |
| Under 3.5 | 21.0% |
| Over 4.5 | 62.3% |
| Under 4.5 | 37.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.69% |
| 2 | 3-1 | 5.00% |
| 3 | 3-3 | 4.89% |
| 4 | 4-1 | 4.84% |
| 5 | 3-2 | 4.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 60.8% | 45.4% | 2.24 | +36.2% |
| Draw | 18.5% | 25.6% | 4.20 | -22.3% |
| Manchester United win | 20.7% | 29.0% | 3.40 | -29.7% |
| Over 2.5 | 90.0% | 63.8% | 1.50 | +34.9% |
| Under 2.5 | 10.0% | 36.2% | 2.63 | -73.6% |

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
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 241.96 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 33.48 |
| Fair Over 2.5 odds | 1.11 |
| Fair Under 2.5 odds | 9.95 |
| Fair Over 3.5 odds | 1.27 |
| Fair Under 3.5 odds | 4.77 |
| Fair Over 4.5 odds | 1.61 |
| Fair Under 4.5 odds | 2.65 |
| Unadjusted home-win probability | 76.2% |
| Unadjusted draw probability | 11.5% |
| Unadjusted away-win probability | 12.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.18 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | +15.4% |
| Draw probability edge | -7.1% |
| Away probability edge | -8.3% |
| Over 2.5 probability edge | +26.2% |
| Under 2.5 probability edge | -26.2% |
| Raw edge prob home | 0.3070 |
| Raw ev home | 0.7058 |
| Raw edge prob draw | -0.1410 |
| Raw ev draw | -0.5188 |
| Raw edge prob away | -0.1660 |
| Raw ev away | -0.5787 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **67.2%**. Expected goals are 1.61 for Galatasaray and 2.47 for Barcelona (4.09 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 98.9%; Over 2.5 goals: 78.5%; Under 4.5 goals: 60.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 17.4% | 5.76 |
| Draw | 15.4% | 6.48 |
| Barcelona win | 67.2% | 1.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.61 |
| Barcelona expected goals | 2.47 |
| Expected total goals | 4.09 |
| Over 0.5 | 98.9% |
| Under 0.5 | 1.1% |
| Over 1.5 | 91.5% |
| Under 1.5 | 8.5% |
| Over 2.5 | 78.5% |
| Under 2.5 | 21.5% |
| Over 3.5 | 59.1% |
| Under 3.5 | 40.9% |
| Over 4.5 | 39.9% |
| Under 4.5 | 60.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.78% |
| 2 | 1-3 | 8.07% |
| 3 | 2-3 | 6.51% |
| 4 | 0-2 | 6.06% |
| 5 | 2-2 | 5.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 17.4% | 9.9% | 9.50 | +65.0% |
| Draw | 15.4% | 12.6% | 7.40 | +14.2% |
| Barcelona win | 67.2% | 77.5% | 1.34 | -10.0% |
| Over 2.5 | 78.5% | 81.3% | 1.21 | -5.0% |
| Under 2.5 | 21.5% | 18.7% | 4.50 | -3.2% |

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
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 88.09 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.70 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.65 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.45 |
| Fair Over 4.5 odds | 2.50 |
| Fair Under 4.5 odds | 1.66 |
| Unadjusted home-win probability | 24.9% |
| Unadjusted draw probability | 18.2% |
| Unadjusted away-win probability | 56.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 9.40 |
| Reference draw odds | 7.40 |
| Reference away odds | 1.28 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.40 |
| Home probability edge | +7.5% |
| Draw probability edge | +2.8% |
| Away probability edge | -10.3% |
| Over 2.5 probability edge | -2.9% |
| Under 2.5 probability edge | +2.9% |
| Raw edge prob home | 0.1498 |
| Raw ev home | 1.3611 |
| Raw edge prob draw | 0.0559 |
| Raw ev draw | 0.3490 |
| Raw edge prob away | -0.2057 |
| Raw ev away | -0.2373 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **68.9%**. Expected goals are 1.98 for Inter Milan and 1.01 for Club Brugge (2.99 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 58.9%; Under 4.5 goals: 80.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 68.9% | 1.45 |
| Draw | 17.4% | 5.74 |
| Club Brugge win | 13.7% | 7.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.98 |
| Club Brugge expected goals | 1.01 |
| Expected total goals | 2.99 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 80.2% |
| Under 1.5 | 19.8% |
| Over 2.5 | 58.9% |
| Under 2.5 | 41.1% |
| Over 3.5 | 35.9% |
| Under 3.5 | 64.1% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.96% |
| 2 | 2-1 | 11.34% |
| 3 | 2-0 | 11.28% |
| 4 | 1-1 | 8.17% |
| 5 | 3-1 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 68.9% | 77.3% | 1.31 | -9.7% |
| Draw | 17.4% | 14.5% | 6.40 | +11.4% |
| Club Brugge win | 13.7% | 8.2% | 11.50 | +57.1% |
| Over 2.5 | 58.9% | 64.5% | 1.50 | -11.7% |
| Under 2.5 | 41.1% | 35.5% | 2.66 | +9.4% |

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
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.71 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.04 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.25 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 19.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.28 |
| Reference draw odds | 6.40 |
| Reference away odds | 11.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.60 |
| Home probability edge | -8.4% |
| Draw probability edge | +3.0% |
| Away probability edge | +5.4% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | -0.1679 |
| Raw ev home | -0.2070 |
| Raw edge prob draw | 0.0590 |
| Raw ev draw | 0.3030 |
| Raw edge prob away | 0.1088 |
| Raw ev away | 1.1970 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **41.4%**. Expected goals are 1.58 for RB Leipzig and 1.78 for PSV Eindhoven (3.36 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 64.9%; Under 4.5 goals: 75.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 41.4% | 2.41 |
| Draw | 22.5% | 4.44 |
| PSV Eindhoven win | 36.1% | 2.77 |

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
| 1 | 1-1 | 9.63% |
| 2 | 2-1 | 9.15% |
| 3 | 1-2 | 7.23% |
| 4 | 2-2 | 7.12% |
| 5 | 1-0 | 7.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 41.4% | 47.9% | 2.08 | -13.9% |
| Draw | 22.5% | 23.3% | 4.30 | -3.2% |
| PSV Eindhoven win | 36.1% | 28.7% | 3.50 | +26.3% |
| Over 2.5 | 64.9% | 70.8% | 1.38 | -10.4% |
| Under 2.5 | 35.1% | 29.2% | 3.08 | +8.1% |

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
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.26 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.35 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.85 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.06 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 34.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 43.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.04 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -6.5% |
| Draw probability edge | -0.8% |
| Away probability edge | +7.3% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.1305 |
| Raw ev home | -0.2744 |
| Raw edge prob draw | -0.0163 |
| Raw ev draw | -0.0669 |
| Raw edge prob away | 0.1468 |
| Raw ev away | 0.5195 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **42.5%**. Expected goals are 1.25 for RC Lens and 1.66 for Sporting Lisbon (2.91 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 55.2%; Under 4.5 goals: 83.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 33.5% | 2.98 |
| Draw | 23.9% | 4.18 |
| Sporting Lisbon win | 42.5% | 2.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.25 |
| Sporting Lisbon expected goals | 1.66 |
| Expected total goals | 2.91 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 16.8% |
| Under 4.5 | 83.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.15% |
| 2 | 0-1 | 8.59% |
| 3 | 1-2 | 8.40% |
| 4 | 1-0 | 8.39% |
| 5 | 2-1 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 33.5% | 37.6% | 2.63 | -11.8% |
| Draw | 23.9% | 24.8% | 3.90 | -6.7% |
| Sporting Lisbon win | 42.5% | 37.6% | 2.70 | +14.8% |
| Over 2.5 | 55.2% | 60.7% | 1.64 | -9.4% |
| Under 2.5 | 44.8% | 39.3% | 2.46 | +10.1% |

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
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.75 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.03 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.96 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 47.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.60 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.60 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.33 |
| Home probability edge | -4.0% |
| Draw probability edge | -0.9% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | -0.0810 |
| Raw ev home | -0.2244 |
| Raw edge prob draw | -0.0179 |
| Raw ev draw | -0.1018 |
| Raw edge prob away | 0.0989 |
| Raw ev away | 0.2819 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **54.0%**. Expected goals are 0.37 for Sabah FK and 1.26 for Slavia Praha (1.63 combined). The most likely exact score is 0-1 at 22.7%. Goal-market probabilities: at least one goal: 82.2%; Over 2.5 goals: 22.1%; Under 4.5 goals: 97.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 19.1% | 5.24 |
| Draw | 27.0% | 3.71 |
| Slavia Praha win | 54.0% | 1.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.37 |
| Slavia Praha expected goals | 1.26 |
| Expected total goals | 1.63 |
| Over 0.5 | 82.2% |
| Under 0.5 | 17.8% |
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
| 1 | 0-1 | 22.73% |
| 2 | 0-0 | 17.78% |
| 3 | 0-2 | 14.01% |
| 4 | 1-0 | 12.96% |
| 5 | 1-1 | 8.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 19.1% | 26.7% | 3.74 | -28.6% |
| Draw | 27.0% | 24.9% | 4.00 | +7.8% |
| Slavia Praha win | 54.0% | 48.4% | 2.04 | +10.1% |
| Over 2.5 | 22.1% | 58.3% | 1.71 | -62.2% |
| Under 2.5 | 77.9% | 41.7% | 2.32 | +80.7% |

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
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.63 |
| Fair Over 1.5 odds | 2.15 |
| Fair Under 1.5 odds | 1.87 |
| Fair Over 2.5 odds | 4.52 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 12.72 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 41.06 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 11.5% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 59.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.60 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.02 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -7.6% |
| Draw probability edge | +2.1% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | -36.2% |
| Under 2.5 probability edge | +36.2% |
| Raw edge prob home | -0.1521 |
| Raw ev home | -0.5708 |
| Raw edge prob draw | 0.0413 |
| Raw ev draw | 0.1611 |
| Raw edge prob away | 0.1107 |
| Raw ev away | 0.2137 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **92.0%**. Expected goals are 0.69 for Viking FK and 4.47 for Bayern Munich (5.16 combined). The most likely exact score is 0-4 at 9.4%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.1%; Under 4.5 goals: 42.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 3.2% | 30.88 |
| Draw | 4.8% | 20.89 |
| Bayern Munich win | 92.0% | 1.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.69 |
| Bayern Munich expected goals | 4.47 |
| Expected total goals | 5.16 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.0% |
| Under 1.5 | 4.0% |
| Over 2.5 | 88.1% |
| Under 2.5 | 11.9% |
| Over 3.5 | 74.7% |
| Under 3.5 | 25.3% |
| Over 4.5 | 57.6% |
| Under 4.5 | 42.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.42% |
| 2 | 0-3 | 8.44% |
| 3 | 0-5 | 8.42% |
| 4 | 1-4 | 6.49% |
| 5 | 0-6 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 3.2% | 4.5% | 27.00 | -12.6% |
| Draw | 4.8% | 5.4% | 15.50 | -25.8% |
| Bayern Munich win | 92.0% | 90.0% | 1.11 | +2.1% |
| Over 2.5 | 88.1% | 85.5% | 1.15 | +1.4% |
| Under 2.5 | 11.9% | 14.5% | 5.60 | -33.5% |

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
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 176.06 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 24.95 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.43 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.95 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 1.9% |
| Unadjusted draw probability | 4.1% |
| Unadjusted away-win probability | 93.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 16.50 |
| Reference draw odds | 14.00 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.60 |
| Home probability edge | -1.3% |
| Draw probability edge | -0.7% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +2.6% |
| Under 2.5 probability edge | -2.6% |
| Raw edge prob home | -0.0260 |
| Raw ev home | -0.4769 |
| Raw edge prob draw | -0.0131 |
| Raw ev draw | -0.3593 |
| Raw edge prob away | 0.0391 |
| Raw ev away | 0.0426 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **40.7%**. Expected goals are 0.87 for Villarreal and 1.43 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 39.9%; Under 4.5 goals: 91.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 33.4% | 2.99 |
| Draw | 25.9% | 3.87 |
| Napoli win | 40.7% | 2.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.87 |
| Napoli expected goals | 1.43 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 39.9% |
| Under 2.5 | 60.1% |
| Over 3.5 | 19.5% |
| Under 3.5 | 80.5% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.22% |
| 2 | 0-1 | 11.95% |
| 3 | 1-1 | 11.93% |
| 4 | 0-0 | 9.40% |
| 5 | 0-2 | 8.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 33.4% | 43.2% | 2.33 | -22.1% |
| Draw | 25.9% | 26.0% | 3.85 | -0.4% |
| Napoli win | 40.7% | 30.7% | 3.25 | +32.4% |
| Over 2.5 | 39.9% | 56.0% | 1.77 | -29.4% |
| Under 2.5 | 60.1% | 44.0% | 2.22 | +33.4% |

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
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.64 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.51 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.12 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.24 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 23.6% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 50.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.26 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -9.8% |
| Draw probability edge | -0.2% |
| Away probability edge | +10.0% |
| Over 2.5 probability edge | -16.1% |
| Under 2.5 probability edge | +16.1% |
| Raw edge prob home | -0.1964 |
| Raw ev home | -0.4502 |
| Raw edge prob draw | -0.0036 |
| Raw ev draw | -0.0113 |
| Raw edge prob away | 0.2000 |
| Raw ev away | 0.6485 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **51.6%**. Expected goals are 1.26 for AS Roma and 1.83 for Real Madrid (3.09 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 59.6%; Under 4.5 goals: 80.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.0% | 3.85 |
| Draw | 22.4% | 4.46 |
| Real Madrid win | 51.6% | 1.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.26 |
| Real Madrid expected goals | 1.83 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 59.6% |
| Under 2.5 | 40.4% |
| Over 3.5 | 37.4% |
| Under 3.5 | 62.6% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.23% |
| 2 | 1-2 | 9.65% |
| 3 | 0-1 | 8.87% |
| 4 | 0-2 | 7.65% |
| 5 | 2-1 | 6.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.0% | 25.1% | 4.10 | +6.5% |
| Draw | 22.4% | 23.0% | 4.30 | -3.6% |
| Real Madrid win | 51.6% | 51.9% | 1.94 | +0.1% |
| Over 2.5 | 59.6% | 67.0% | 1.44 | -14.2% |
| Under 2.5 | 40.4% | 33.0% | 2.95 | +19.2% |

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
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.28 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.26 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.48 |
| Fair Over 3.5 odds | 2.67 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 5.00 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 51.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.95 |
| Reference draw odds | 4.30 |
| Reference away odds | 1.92 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | +0.9% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | 0.0175 |
| Raw ev home | 0.1008 |
| Raw edge prob draw | -0.0123 |
| Raw ev draw | -0.0620 |
| Raw edge prob away | -0.0053 |
| Raw ev away | -0.0040 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **66.3%**. Expected goals are 2.22 for Aston Villa and 0.60 for Fenerbahce (2.83 combined). The most likely exact score is 2-0 at 13.0%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 51.1%; Under 4.5 goals: 85.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 66.3% | 1.51 |
| Draw | 20.1% | 4.98 |
| Fenerbahce win | 13.6% | 7.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.22 |
| Fenerbahce expected goals | 0.60 |
| Expected total goals | 2.83 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.97% |
| 2 | 1-0 | 12.02% |
| 3 | 3-0 | 9.61% |
| 4 | 1-1 | 9.38% |
| 5 | 2-1 | 7.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 66.3% | 57.8% | 1.77 | +17.4% |
| Draw | 20.1% | 24.0% | 4.25 | -14.6% |
| Fenerbahce win | 13.6% | 18.2% | 5.40 | -26.7% |
| Over 2.5 | 51.1% | 59.2% | 1.74 | -11.1% |
| Under 2.5 | 48.9% | 40.8% | 2.28 | +11.5% |

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
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.55 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.36 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.90 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.2% |
| Unadjusted away-win probability | 9.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.72 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.40 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +8.5% |
| Draw probability edge | -3.9% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | 0.1707 |
| Raw ev home | 0.3252 |
| Raw edge prob draw | -0.0785 |
| Raw ev draw | -0.3129 |
| Raw edge prob away | -0.0922 |
| Raw ev away | -0.5162 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **47.4%**. Expected goals are 1.67 for Bodø/Glimt and 2.04 for Borussia Dortmund (3.70 combined). The most likely exact score is 1-2 at 8.6%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 71.2%; Under 4.5 goals: 68.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 30.9% | 3.23 |
| Draw | 21.7% | 4.61 |
| Borussia Dortmund win | 47.4% | 2.11 |

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
| 1 | 1-2 | 8.56% |
| 2 | 1-1 | 8.44% |
| 3 | 2-2 | 7.54% |
| 4 | 2-1 | 6.65% |
| 5 | 1-3 | 5.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 30.9% | 29.4% | 3.30 | +2.1% |
| Draw | 21.7% | 23.0% | 4.30 | -6.7% |
| Borussia Dortmund win | 47.4% | 47.7% | 2.14 | +1.4% |
| Over 2.5 | 71.2% | 69.0% | 1.40 | -0.3% |
| Under 2.5 | 28.8% | 31.0% | 3.03 | -12.8% |

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
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.05 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.30 |
| Reference draw odds | 4.20 |
| Reference away odds | 2.06 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +1.6% |
| Draw probability edge | -1.3% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +2.2% |
| Under 2.5 probability edge | -2.2% |
| Raw edge prob home | 0.0310 |
| Raw ev home | 0.0723 |
| Raw edge prob draw | -0.0253 |
| Raw ev draw | -0.1217 |
| Raw edge prob away | -0.0057 |
| Raw ev away | 0.0075 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **62.6%**. Expected goals are 1.84 for Feyenoord and 3.93 for Como (5.77 combined). The most likely exact score is 2-2 at 6.0%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 91.6%; Under 4.5 goals: 34.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 20.0% | 4.99 |
| Draw | 17.4% | 5.76 |
| Como win | 62.6% | 1.60 |

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
| Over 3.5 | 81.6% |
| Under 3.5 | 18.4% |
| Over 4.5 | 66.0% |
| Under 4.5 | 34.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.05% |
| 2 | 1-3 | 4.88% |
| 3 | 3-3 | 4.86% |
| 4 | 1-4 | 4.79% |
| 5 | 2-3 | 4.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 20.0% | 26.5% | 3.85 | -22.9% |
| Draw | 17.4% | 23.0% | 4.33 | -24.8% |
| Como win | 62.6% | 50.5% | 1.95 | +22.1% |
| Over 2.5 | 91.6% | 68.5% | 1.43 | +30.9% |
| Under 2.5 | 8.4% | 31.5% | 2.87 | -75.8% |

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
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 337.72 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 40.95 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 11.86 |
| Fair Over 3.5 odds | 1.23 |
| Fair Under 3.5 odds | 5.44 |
| Fair Over 4.5 odds | 1.52 |
| Fair Under 4.5 odds | 2.94 |
| Unadjusted home-win probability | 13.5% |
| Unadjusted draw probability | 11.7% |
| Unadjusted away-win probability | 74.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.65 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.95 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -6.5% |
| Draw probability edge | -5.6% |
| Away probability edge | +12.2% |
| Over 2.5 probability edge | +23.0% |
| Under 2.5 probability edge | -23.0% |
| Raw edge prob home | -0.1303 |
| Raw ev home | -0.4795 |
| Raw edge prob draw | -0.1127 |
| Raw ev draw | -0.4924 |
| Raw edge prob away | 0.2430 |
| Raw ev away | 0.4578 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **73.3%**. Expected goals are 0.33 for LASK and 1.48 for Liverpool (1.80 combined). The most likely exact score is 0-1 at 27.0%. Goal-market probabilities: at least one goal: 87.7%; Over 2.5 goals: 29.0%; Under 4.5 goals: 96.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 7.9% | 12.68 |
| Draw | 18.8% | 5.31 |
| Liverpool win | 73.3% | 1.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.33 |
| Liverpool expected goals | 1.48 |
| Expected total goals | 1.80 |
| Over 0.5 | 87.7% |
| Under 0.5 | 12.3% |
| Over 1.5 | 55.2% |
| Under 1.5 | 44.8% |
| Over 2.5 | 29.0% |
| Under 2.5 | 71.0% |
| Over 3.5 | 11.6% |
| Under 3.5 | 88.4% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 27.03% |
| 2 | 0-2 | 19.64% |
| 3 | 0-0 | 12.28% |
| 4 | 0-3 | 9.67% |
| 5 | 1-2 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 7.9% | 7.4% | 13.00 | +2.5% |
| Draw | 18.8% | 13.0% | 7.25 | +36.5% |
| Liverpool win | 73.3% | 79.5% | 1.29 | -5.5% |
| Over 2.5 | 29.0% | 71.6% | 1.38 | -60.0% |
| Under 2.5 | 71.0% | 28.4% | 3.10 | +120.2% |

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
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.14 |
| Fair Over 1.5 odds | 1.81 |
| Fair Under 1.5 odds | 2.23 |
| Fair Over 2.5 odds | 3.45 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.64 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 25.17 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 8.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 67.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 11.50 |
| Reference draw odds | 6.80 |
| Reference away odds | 1.24 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | +0.4% |
| Draw probability edge | +5.8% |
| Away probability edge | -6.3% |
| Over 2.5 probability edge | -42.6% |
| Under 2.5 probability edge | +42.6% |
| Raw edge prob home | 0.0089 |
| Raw ev home | 0.0827 |
| Raw edge prob draw | 0.1162 |
| Raw ev draw | 0.7856 |
| Raw edge prob away | -0.1250 |
| Raw ev away | -0.1352 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **46.9%**. Expected goals are 1.53 for Manchester City and 2.51 for Paris Saint Germain (4.04 combined). The most likely exact score is 2-1 at 7.4%. Goal-market probabilities: at least one goal: 98.4%; Over 2.5 goals: 75.6%; Under 4.5 goals: 63.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 32.8% | 3.05 |
| Draw | 20.4% | 4.91 |
| Paris Saint Germain win | 46.9% | 2.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.53 |
| Paris Saint Germain expected goals | 2.51 |
| Expected total goals | 4.04 |
| Over 0.5 | 98.4% |
| Under 0.5 | 1.6% |
| Over 1.5 | 90.3% |
| Under 1.5 | 9.7% |
| Over 2.5 | 75.6% |
| Under 2.5 | 24.4% |
| Over 3.5 | 56.3% |
| Under 3.5 | 43.7% |
| Over 4.5 | 36.6% |
| Under 4.5 | 63.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 7.42% |
| 2 | 2-2 | 7.39% |
| 3 | 1-1 | 7.32% |
| 4 | 1-2 | 6.71% |
| 5 | 1-3 | 5.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 32.8% | 42.7% | 2.34 | -23.3% |
| Draw | 20.4% | 22.8% | 4.30 | -12.4% |
| Paris Saint Germain win | 46.9% | 34.5% | 2.97 | +39.1% |
| Over 2.5 | 75.6% | 67.0% | 1.44 | +8.9% |
| Under 2.5 | 24.4% | 33.0% | 2.87 | -30.0% |

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
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 61.72 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.27 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.10 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.29 |
| Fair Over 4.5 odds | 2.73 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.32 |
| Reference draw odds | 4.30 |
| Reference away odds | 2.86 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -9.9% |
| Draw probability edge | -2.5% |
| Away probability edge | +12.3% |
| Over 2.5 probability edge | +8.6% |
| Under 2.5 probability edge | -8.6% |
| Raw edge prob home | -0.1975 |
| Raw ev home | -0.4641 |
| Raw edge prob draw | -0.0493 |
| Raw ev draw | -0.2301 |
| Raw edge prob away | 0.2468 |
| Raw ev away | 0.7580 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **64.8%**. Expected goals are 4.51 for Real Betis and 1.48 for Porto (5.98 combined). The most likely exact score is 2-2 at 6.1%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 91.2%; Under 4.5 goals: 33.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 64.8% | 1.54 |
| Draw | 17.0% | 5.89 |
| Porto win | 18.2% | 5.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 4.51 |
| Porto expected goals | 1.48 |
| Expected total goals | 5.98 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.4% |
| Under 1.5 | 2.6% |
| Over 2.5 | 91.2% |
| Under 2.5 | 8.8% |
| Over 3.5 | 81.6% |
| Under 3.5 | 18.4% |
| Over 4.5 | 66.1% |
| Under 4.5 | 33.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.11% |
| 2 | 4-1 | 4.88% |
| 3 | 3-3 | 4.51% |
| 4 | 5-1 | 4.40% |
| 5 | 3-1 | 4.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 64.8% | 44.1% | 2.27 | +47.1% |
| Draw | 17.0% | 26.1% | 3.80 | -35.5% |
| Porto win | 18.2% | 29.8% | 3.30 | -39.9% |
| Over 2.5 | 91.2% | 56.2% | 1.78 | +62.4% |
| Under 2.5 | 8.8% | 43.8% | 2.21 | -80.6% |

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
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 270.77 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 39.14 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 11.42 |
| Fair Over 3.5 odds | 1.22 |
| Fair Under 3.5 odds | 5.45 |
| Fair Over 4.5 odds | 1.51 |
| Fair Under 4.5 odds | 2.95 |
| Unadjusted home-win probability | 85.5% |
| Unadjusted draw probability | 7.8% |
| Unadjusted away-win probability | 6.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.24 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | +20.7% |
| Draw probability edge | -9.2% |
| Away probability edge | -11.5% |
| Over 2.5 probability edge | +35.0% |
| Under 2.5 probability edge | -35.0% |
| Raw edge prob home | 0.4143 |
| Raw ev home | 0.9415 |
| Raw edge prob draw | -0.1834 |
| Raw ev draw | -0.7037 |
| Raw edge prob away | -0.2308 |
| Raw ev away | -0.7797 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.1%**. Expected goals are 1.45 for Shakhtar Donetsk and 1.25 for AEK Athens (2.71 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 50.5%; Under 4.5 goals: 86.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.1% | 2.56 |
| Draw | 25.4% | 3.94 |
| AEK Athens win | 35.5% | 2.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.45 |
| AEK Athens expected goals | 1.25 |
| Expected total goals | 2.71 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.7% |
| Under 3.5 | 71.3% |
| Over 4.5 | 13.7% |
| Under 4.5 | 86.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.00% |
| 2 | 0-1 | 9.60% |
| 3 | 1-0 | 9.50% |
| 4 | 1-2 | 8.16% |
| 5 | 2-1 | 8.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.1% | 35.8% | 2.81 | +9.8% |
| Draw | 25.4% | 26.3% | 3.65 | -7.4% |
| AEK Athens win | 35.5% | 37.9% | 2.65 | -5.8% |
| Over 2.5 | 50.5% | 52.3% | 1.91 | -3.6% |
| Under 2.5 | 49.5% | 47.7% | 2.03 | +0.5% |

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
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.87 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.31 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 42.4% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 33.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.68 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.54 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +3.3% |
| Draw probability edge | -1.0% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | 0.0655 |
| Raw ev home | 0.1903 |
| Raw edge prob draw | -0.0192 |
| Raw ev draw | -0.1089 |
| Raw edge prob away | -0.0464 |
| Raw ev away | -0.1195 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **65.6%**. Expected goals are 1.40 for ŠK Slovan Bratislava and 2.20 for VfB Stuttgart (3.60 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 70.7%; Under 4.5 goals: 69.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.1% | 5.85 |
| Draw | 17.3% | 5.79 |
| VfB Stuttgart win | 65.6% | 1.52 |

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
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 49.2% |
| Under 3.5 | 50.8% |
| Over 4.5 | 30.1% |
| Under 4.5 | 69.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.84% |
| 2 | 1-3 | 7.94% |
| 3 | 0-2 | 7.75% |
| 4 | 0-1 | 7.55% |
| 5 | 1-1 | 7.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.1% | 9.8% | 9.90 | +69.3% |
| Draw | 17.3% | 15.0% | 6.25 | +7.9% |
| VfB Stuttgart win | 65.6% | 75.2% | 1.35 | -11.4% |
| Over 2.5 | 70.7% | 70.8% | 1.38 | -2.5% |
| Under 2.5 | 29.3% | 29.2% | 3.08 | -9.7% |

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
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 48.60 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.94 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.41 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.97 |
| Fair Over 4.5 odds | 3.32 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 56.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 9.00 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.31 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +7.3% |
| Draw probability edge | +2.2% |
| Away probability edge | -9.5% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.1461 |
| Raw ev home | 1.4158 |
| Raw edge prob draw | 0.0446 |
| Raw ev draw | 0.2189 |
| Raw edge prob away | -0.1907 |
| Raw ev away | -0.2427 |

</details>


---
