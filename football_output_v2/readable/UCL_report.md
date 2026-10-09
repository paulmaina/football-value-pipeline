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
| Additional event odds league quota | 0.00 |
| Additional event odds calls this league | 0.00 |
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

The model's most likely 1X2 outcome is **Arsenal win** at **72.8%**. Expected goals are 2.01 for Arsenal and 0.77 for Lille (2.78 combined). The most likely exact score is 1-0 at 14.1%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 54.0%; Under 4.5 goals: 84.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 72.8% | 1.37 |
| Draw | 17.1% | 5.86 |
| Lille win | 10.2% | 9.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 2.01 |
| Lille expected goals | 0.77 |
| Expected total goals | 2.78 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 77.0% |
| Under 1.5 | 23.0% |
| Over 2.5 | 54.0% |
| Under 2.5 | 46.0% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.05% |
| 2 | 2-0 | 13.61% |
| 3 | 2-1 | 10.50% |
| 4 | 3-0 | 9.13% |
| 5 | 1-1 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 72.8% | 78.7% | 1.30 | -5.4% |
| Draw | 17.1% | 14.9% | 7.40 | +26.3% |
| Lille win | 10.2% | 6.4% | 14.00 | +42.2% |
| Over 2.5 | 54.0% | 61.4% | 1.67 | -9.8% |
| Under 2.5 | 46.0% | 38.6% | 2.42 | +11.3% |

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
| Market best home last update utc | 2026-10-09T14:38:09Z |
| Market best draw last update utc | 2026-10-09T14:38:41Z |
| Market best away last update utc | 2026-10-09T14:38:52Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 45.2% |
| P btts no | 54.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.78 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.36 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.41 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 19.2% |
| Unadjusted away-win probability | 13.9% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.26 |
| Reference draw odds | 6.25 |
| Reference away odds | 14.00 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -5.9% |
| Draw probability edge | +2.2% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.1177 |
| Raw ev home | -0.1305 |
| Raw edge prob draw | 0.0435 |
| Raw ev draw | 0.4244 |
| Raw edge prob away | 0.0742 |
| Raw ev away | 0.9416 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **60.7%**. Expected goals are 3.87 for Atlético Madrid and 1.70 for Manchester United (5.57 combined). The most likely exact score is 2-2 at 6.3%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 90.1%; Under 4.5 goals: 37.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 60.7% | 1.65 |
| Draw | 17.5% | 5.72 |
| Manchester United win | 21.9% | 4.58 |

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
| Over 2.5 | 90.1% |
| Under 2.5 | 9.9% |
| Over 3.5 | 78.9% |
| Under 3.5 | 21.1% |
| Over 4.5 | 62.4% |
| Under 4.5 | 37.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.32% |
| 2 | 3-1 | 4.99% |
| 3 | 4-1 | 4.83% |
| 4 | 3-3 | 4.62% |
| 5 | 3-2 | 4.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 60.7% | 45.2% | 2.18 | +32.2% |
| Draw | 17.5% | 23.5% | 4.20 | -26.6% |
| Manchester United win | 21.9% | 31.3% | 3.45 | -24.6% |
| Over 2.5 | 90.1% | 63.8% | 1.50 | +35.1% |
| Under 2.5 | 9.9% | 36.2% | 2.63 | -73.9% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:38:26Z |
| Market best away last update utc | 2026-10-09T14:38:44Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 82.1% |
| P btts no | 17.9% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 256.15 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 32.96 |
| Fair Over 2.5 odds | 1.11 |
| Fair Under 2.5 odds | 10.07 |
| Fair Over 3.5 odds | 1.27 |
| Fair Under 3.5 odds | 4.75 |
| Fair Over 4.5 odds | 1.60 |
| Fair Under 4.5 odds | 2.66 |
| Unadjusted home-win probability | 76.2% |
| Unadjusted draw probability | 11.5% |
| Unadjusted away-win probability | 12.4% |
| Raw p over 1 5 | 97.4% |
| Raw p under 3 5 | 19.4% |
| Raw p btts yes | 80.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.17 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | +15.5% |
| Draw probability edge | -6.0% |
| Away probability edge | -9.5% |
| Over 2.5 probability edge | +26.3% |
| Under 2.5 probability edge | -26.3% |
| Raw edge prob home | 0.3099 |
| Raw ev home | 0.6601 |
| Raw edge prob draw | -0.1205 |
| Raw ev draw | -0.5188 |
| Raw edge prob away | -0.1893 |
| Raw ev away | -0.5725 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **66.6%**. Expected goals are 1.61 for Galatasaray and 2.47 for Barcelona (4.09 combined). The most likely exact score is 1-2 at 9.7%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 78.3%; Under 4.5 goals: 60.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 17.1% | 5.86 |
| Draw | 16.3% | 6.12 |
| Barcelona win | 66.6% | 1.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.61 |
| Barcelona expected goals | 2.47 |
| Expected total goals | 4.09 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 91.5% |
| Under 1.5 | 8.5% |
| Over 2.5 | 78.3% |
| Under 2.5 | 21.7% |
| Over 3.5 | 59.1% |
| Under 3.5 | 40.9% |
| Over 4.5 | 39.7% |
| Under 4.5 | 60.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.69% |
| 2 | 1-3 | 7.99% |
| 3 | 2-3 | 6.45% |
| 4 | 0-2 | 6.00% |
| 5 | 2-2 | 6.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 17.1% | 9.3% | 10.00 | +70.6% |
| Draw | 16.3% | 14.5% | 7.40 | +21.0% |
| Barcelona win | 66.6% | 76.3% | 1.34 | -10.8% |
| Over 2.5 | 78.3% | 81.3% | 1.21 | -5.3% |
| Under 2.5 | 21.7% | 18.7% | 4.50 | -2.2% |

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
| Market best home last update utc | 2026-10-09T14:38:10Z |
| Market best draw last update utc | 2026-10-09T14:38:41Z |
| Market best away last update utc | 2026-10-09T14:38:09Z |
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
| P btts yes | 72.2% |
| P btts no | 27.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 83.18 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.72 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.60 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.45 |
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
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 10.00 |
| Reference draw odds | 6.50 |
| Reference away odds | 1.30 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.40 |
| Home probability edge | +7.8% |
| Draw probability edge | +1.9% |
| Away probability edge | -9.7% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | 0.1558 |
| Raw ev home | 1.4854 |
| Raw edge prob draw | 0.0376 |
| Raw ev draw | 0.3490 |
| Raw edge prob away | -0.1935 |
| Raw ev away | -0.2373 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **68.7%**. Expected goals are 1.98 for Inter Milan and 1.01 for Club Brugge (2.99 combined). The most likely exact score is 1-0 at 11.9%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 58.7%; Under 4.5 goals: 81.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 68.7% | 1.46 |
| Draw | 18.0% | 5.56 |
| Club Brugge win | 13.4% | 7.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.98 |
| Club Brugge expected goals | 1.01 |
| Expected total goals | 2.99 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 80.2% |
| Under 1.5 | 19.8% |
| Over 2.5 | 58.7% |
| Under 2.5 | 41.3% |
| Over 3.5 | 35.9% |
| Under 3.5 | 64.1% |
| Over 4.5 | 19.0% |
| Under 4.5 | 81.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.92% |
| 2 | 2-1 | 11.29% |
| 3 | 2-0 | 11.24% |
| 4 | 1-1 | 8.44% |
| 5 | 3-1 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 68.7% | 76.8% | 1.31 | -10.0% |
| Draw | 18.0% | 15.6% | 6.25 | +12.4% |
| Club Brugge win | 13.4% | 7.6% | 12.00 | +60.3% |
| Over 2.5 | 58.7% | 64.5% | 1.50 | -11.9% |
| Under 2.5 | 41.3% | 35.5% | 2.72 | +12.3% |

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
| Market best home last update utc | 2026-10-09T14:38:09Z |
| Market best draw last update utc | 2026-10-09T14:38:29Z |
| Market best away last update utc | 2026-10-09T14:38:52Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
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
| Fair Under 0.5 odds | 24.89 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.04 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.27 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 65.0% |
| Raw p btts yes | 54.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.29 |
| Reference draw odds | 6.00 |
| Reference away odds | 12.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.60 |
| Home probability edge | -8.1% |
| Draw probability edge | +2.4% |
| Away probability edge | +5.8% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.1626 |
| Raw ev home | -0.2070 |
| Raw edge prob draw | 0.0476 |
| Raw ev draw | 0.2725 |
| Raw edge prob away | 0.1150 |
| Raw ev away | 1.2926 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **41.1%**. Expected goals are 1.58 for RB Leipzig and 1.78 for PSV Eindhoven (3.36 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 64.7%; Under 4.5 goals: 75.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 41.1% | 2.43 |
| Draw | 23.3% | 4.29 |
| PSV Eindhoven win | 35.6% | 2.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.58 |
| PSV Eindhoven expected goals | 1.78 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 84.3% |
| Under 1.5 | 15.7% |
| Over 2.5 | 64.7% |
| Under 2.5 | 35.3% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.5% |
| Under 4.5 | 75.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.96% |
| 2 | 2-1 | 9.08% |
| 3 | 2-2 | 7.37% |
| 4 | 1-2 | 7.14% |
| 5 | 1-0 | 7.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 41.1% | 47.3% | 2.08 | -14.5% |
| Draw | 23.3% | 24.9% | 4.33 | +0.9% |
| PSV Eindhoven win | 35.6% | 27.8% | 3.65 | +30.0% |
| Over 2.5 | 64.7% | 70.8% | 1.39 | -10.1% |
| Under 2.5 | 35.3% | 29.2% | 3.03 | +7.0% |

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
| Market best home last update utc | 2026-10-09T14:38:53Z |
| Market best draw last update utc | 2026-10-09T14:38:10Z |
| Market best away last update utc | 2026-10-09T14:38:09Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.0% |
| P btts no | 34.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.18 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.36 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.83 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.09 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 34.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 43.4% |
| Raw p over 1 5 | 84.4% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.08 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -6.2% |
| Draw probability edge | -1.6% |
| Away probability edge | +7.8% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.1243 |
| Raw ev home | -0.2744 |
| Raw edge prob draw | -0.0319 |
| Raw ev draw | -0.0603 |
| Raw edge prob away | 0.1562 |
| Raw ev away | 0.5846 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **42.4%**. Expected goals are 1.25 for RC Lens and 1.66 for Sporting Lisbon (2.91 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 55.1%; Under 4.5 goals: 83.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 33.4% | 3.00 |
| Draw | 24.3% | 4.12 |
| Sporting Lisbon win | 42.4% | 2.36 |

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
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.33% |
| 2 | 0-1 | 8.55% |
| 3 | 1-2 | 8.36% |
| 4 | 1-0 | 8.35% |
| 5 | 2-1 | 8.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 33.4% | 37.2% | 2.63 | -12.3% |
| Draw | 24.3% | 25.6% | 3.90 | -5.3% |
| Sporting Lisbon win | 42.4% | 37.2% | 2.70 | +14.3% |
| Over 2.5 | 55.1% | 60.9% | 1.64 | -9.6% |
| Under 2.5 | 44.9% | 39.1% | 2.46 | +10.4% |

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
| Market best home last update utc | 2026-10-09T14:38:52Z |
| Market best draw last update utc | 2026-10-09T14:38:41Z |
| Market best away last update utc | 2026-10-09T14:38:26Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 11.00 |
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
| Fair Under 0.5 odds | 19.45 |
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
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.63 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.63 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | -3.9% |
| Draw probability edge | -1.3% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0773 |
| Raw ev home | -0.2244 |
| Raw edge prob draw | -0.0252 |
| Raw ev draw | -0.1018 |
| Raw edge prob away | 0.1025 |
| Raw ev away | 0.2819 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **54.3%**. Expected goals are 0.37 for Sabah FK and 1.26 for Slavia Praha (1.63 combined). The most likely exact score is 0-1 at 22.9%. Goal-market probabilities: at least one goal: 82.3%; Over 2.5 goals: 22.2%; Under 4.5 goals: 97.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 18.8% | 5.32 |
| Draw | 26.9% | 3.72 |
| Slavia Praha win | 54.3% | 1.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.37 |
| Slavia Praha expected goals | 1.26 |
| Expected total goals | 1.63 |
| Over 0.5 | 82.3% |
| Under 0.5 | 17.7% |
| Over 1.5 | 46.6% |
| Under 1.5 | 53.4% |
| Over 2.5 | 22.2% |
| Under 2.5 | 77.8% |
| Over 3.5 | 7.9% |
| Under 3.5 | 92.1% |
| Over 4.5 | 2.4% |
| Under 4.5 | 97.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.88% |
| 2 | 0-0 | 17.73% |
| 3 | 0-2 | 14.09% |
| 4 | 1-0 | 12.78% |
| 5 | 1-1 | 8.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 18.8% | 26.1% | 3.74 | -29.7% |
| Draw | 26.9% | 24.8% | 4.00 | +7.6% |
| Slavia Praha win | 54.3% | 49.1% | 2.06 | +11.9% |
| Over 2.5 | 22.2% | 58.1% | 1.71 | -62.1% |
| Under 2.5 | 77.8% | 41.9% | 2.32 | +80.6% |

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
| Market best home last update utc | 2026-10-09T14:38:09Z |
| Market best draw last update utc | 2026-10-09T14:38:26Z |
| Market best away last update utc | 2026-10-09T14:38:41Z |
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
| P btts yes | 21.6% |
| P btts no | 78.4% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.64 |
| Fair Over 1.5 odds | 2.15 |
| Fair Under 1.5 odds | 1.87 |
| Fair Over 2.5 odds | 4.51 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 12.68 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 40.91 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.5% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 59.5% |
| Raw p over 1 5 | 48.0% |
| Raw p under 3 5 | 91.7% |
| Raw p btts yes | 21.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.70 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -7.3% |
| Draw probability edge | +2.1% |
| Away probability edge | +5.2% |
| Over 2.5 probability edge | -35.9% |
| Under 2.5 probability edge | +35.9% |
| Raw edge prob home | -0.1465 |
| Raw ev home | -0.5708 |
| Raw edge prob draw | 0.0427 |
| Raw ev draw | 0.1611 |
| Raw edge prob away | 0.1038 |
| Raw ev away | 0.2256 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **91.7%**. Expected goals are 0.69 for Viking FK and 4.47 for Bayern Munich (5.16 combined). The most likely exact score is 0-4 at 9.4%. Goal-market probabilities: at least one goal: 99.3%; Over 2.5 goals: 87.9%; Under 4.5 goals: 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 2.7% | 36.70 |
| Draw | 5.6% | 17.91 |
| Bayern Munich win | 91.7% | 1.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.69 |
| Bayern Munich expected goals | 4.47 |
| Expected total goals | 5.16 |
| Over 0.5 | 99.3% |
| Under 0.5 | 0.7% |
| Over 1.5 | 96.0% |
| Under 1.5 | 4.0% |
| Over 2.5 | 87.9% |
| Under 2.5 | 12.1% |
| Over 3.5 | 74.7% |
| Under 3.5 | 25.3% |
| Over 4.5 | 57.4% |
| Under 4.5 | 42.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.39% |
| 2 | 0-3 | 8.41% |
| 3 | 0-5 | 8.39% |
| 4 | 1-4 | 6.47% |
| 5 | 0-6 | 6.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 2.7% | 3.5% | 27.00 | -26.4% |
| Draw | 5.6% | 7.0% | 15.50 | -13.4% |
| Bayern Munich win | 91.7% | 89.5% | 1.11 | +1.8% |
| Over 2.5 | 87.9% | 85.6% | 1.15 | +1.1% |
| Under 2.5 | 12.1% | 14.4% | 5.70 | -31.0% |

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
| Market best home last update utc | 2026-10-09T14:38:28Z |
| Market best draw last update utc | 2026-10-09T14:38:09Z |
| Market best away last update utc | 2026-10-09T14:38:52Z |
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
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 150.92 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 25.22 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.27 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.95 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.35 |
| Unadjusted home-win probability | 1.9% |
| Unadjusted draw probability | 4.1% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.3% |
| Raw p under 3 5 | 24.5% |
| Raw p btts yes | 49.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 23.00 |
| Reference draw odds | 12.00 |
| Reference away odds | 1.11 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.70 |
| Home probability edge | -0.8% |
| Draw probability edge | -1.5% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | -0.0157 |
| Raw ev home | -0.4769 |
| Raw edge prob draw | -0.0290 |
| Raw ev draw | -0.3593 |
| Raw edge prob away | 0.0448 |
| Raw ev away | 0.0426 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **40.3%**. Expected goals are 0.87 for Villarreal and 1.43 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 39.7%; Under 4.5 goals: 91.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 33.1% | 3.02 |
| Draw | 26.7% | 3.75 |
| Napoli win | 40.3% | 2.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.87 |
| Napoli expected goals | 1.43 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 39.7% |
| Under 2.5 | 60.3% |
| Over 3.5 | 19.5% |
| Under 3.5 | 80.5% |
| Over 4.5 | 8.1% |
| Under 4.5 | 91.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.08% |
| 2 | 1-1 | 12.30% |
| 3 | 0-1 | 11.82% |
| 4 | 0-0 | 9.69% |
| 5 | 0-2 | 8.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 33.1% | 42.5% | 2.33 | -23.0% |
| Draw | 26.7% | 27.6% | 3.95 | +5.3% |
| Napoli win | 40.3% | 29.8% | 3.25 | +30.9% |
| Over 2.5 | 39.7% | 56.2% | 1.77 | -29.8% |
| Under 2.5 | 60.3% | 43.8% | 2.22 | +34.0% |

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
| Market best home last update utc | 2026-10-09T14:38:27Z |
| Market best draw last update utc | 2026-10-09T14:38:44Z |
| Market best away last update utc | 2026-10-09T14:38:52Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.2% |
| P btts no | 55.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.32 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.13 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.34 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 23.6% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 50.7% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 79.8% |
| Raw p btts yes | 43.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | -9.5% |
| Draw probability edge | -1.0% |
| Away probability edge | +10.4% |
| Over 2.5 probability edge | -16.6% |
| Under 2.5 probability edge | +16.6% |
| Raw edge prob home | -0.1893 |
| Raw ev home | -0.4502 |
| Raw edge prob draw | -0.0196 |
| Raw ev draw | 0.0144 |
| Raw edge prob away | 0.2090 |
| Raw ev away | 0.6485 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **51.5%**. Expected goals are 1.26 for AS Roma and 1.83 for Real Madrid (3.09 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 59.6%; Under 4.5 goals: 80.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.0% | 3.84 |
| Draw | 22.5% | 4.45 |
| Real Madrid win | 51.5% | 1.94 |

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
| 1 | 1-1 | 10.24% |
| 2 | 1-2 | 9.63% |
| 3 | 0-1 | 8.85% |
| 4 | 0-2 | 7.63% |
| 5 | 2-1 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.0% | 25.2% | 4.10 | +6.8% |
| Draw | 22.5% | 23.1% | 4.30 | -3.4% |
| Real Madrid win | 51.5% | 51.6% | 1.95 | +0.4% |
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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:38:28Z |
| Market best draw last update utc | 2026-10-09T14:38:41Z |
| Market best away last update utc | 2026-10-09T14:38:26Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.9% |
| P btts no | 40.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.24 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.25 |
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
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.85 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.91 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | +0.8% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | 0.0160 |
| Raw ev home | 0.1008 |
| Raw edge prob draw | -0.0129 |
| Raw ev draw | -0.0620 |
| Raw edge prob away | -0.0031 |
| Raw ev away | 0.0011 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **65.6%**. Expected goals are 2.22 for Aston Villa and 0.60 for Fenerbahce (2.83 combined). The most likely exact score is 2-0 at 12.8%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 51.1%; Under 4.5 goals: 85.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 65.6% | 1.52 |
| Draw | 19.4% | 5.15 |
| Fenerbahce win | 14.9% | 6.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.22 |
| Fenerbahce expected goals | 0.60 |
| Expected total goals | 2.83 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 29.5% |
| Under 3.5 | 70.5% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.83% |
| 2 | 1-0 | 11.89% |
| 3 | 3-0 | 9.51% |
| 4 | 1-1 | 9.07% |
| 5 | 2-1 | 7.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 65.6% | 56.4% | 1.75 | +14.8% |
| Draw | 19.4% | 22.7% | 4.25 | -17.4% |
| Fenerbahce win | 14.9% | 20.9% | 5.40 | -19.3% |
| Over 2.5 | 51.1% | 59.2% | 1.74 | -11.0% |
| Under 2.5 | 48.9% | 40.8% | 2.28 | +11.4% |

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
| Market best home last update utc | 2026-10-09T14:38:10Z |
| Market best draw last update utc | 2026-10-09T14:38:10Z |
| Market best away last update utc | 2026-10-09T14:38:41Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Unibet (NL) |
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
| Fair Under 0.5 odds | 15.05 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.97 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.39 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.91 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.2% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 76.9% |
| Raw p under 3 5 | 68.6% |
| Raw p btts yes | 40.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.75 |
| Reference draw odds | 4.25 |
| Reference away odds | 4.60 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +9.3% |
| Draw probability edge | -3.3% |
| Away probability edge | -6.0% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | 0.1851 |
| Raw ev home | 0.3103 |
| Raw edge prob draw | -0.0654 |
| Raw ev draw | -0.3129 |
| Raw edge prob away | -0.1198 |
| Raw ev away | -0.5162 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **47.3%**. Expected goals are 1.67 for Bodø/Glimt and 2.04 for Borussia Dortmund (3.70 combined). The most likely exact score is 1-2 at 8.5%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 71.2%; Under 4.5 goals: 68.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 31.0% | 3.23 |
| Draw | 21.7% | 4.60 |
| Borussia Dortmund win | 47.3% | 2.11 |

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
| 1 | 1-2 | 8.55% |
| 2 | 1-1 | 8.45% |
| 3 | 2-2 | 7.55% |
| 4 | 2-1 | 6.65% |
| 5 | 1-3 | 5.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 31.0% | 29.5% | 3.35 | +3.8% |
| Draw | 21.7% | 23.0% | 4.30 | -6.6% |
| Borussia Dortmund win | 47.3% | 47.5% | 2.14 | +1.2% |
| Over 2.5 | 71.2% | 69.0% | 1.41 | +0.4% |
| Under 2.5 | 28.8% | 31.0% | 2.97 | -14.5% |

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
| Market best home last update utc | 2026-10-09T14:38:41Z |
| Market best draw last update utc | 2026-10-09T14:38:26Z |
| Market best away last update utc | 2026-10-09T14:38:09Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.4% |
| P btts no | 29.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.97 |
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
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.30 |
| Reference draw odds | 4.20 |
| Reference away odds | 2.07 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +1.5% |
| Draw probability edge | -1.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +2.2% |
| Under 2.5 probability edge | -2.2% |
| Raw edge prob home | 0.0302 |
| Raw ev home | 0.0885 |
| Raw edge prob draw | -0.0260 |
| Raw ev draw | -0.1217 |
| Raw edge prob away | -0.0042 |
| Raw ev away | 0.0075 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **63.6%**. Expected goals are 1.84 for Feyenoord and 3.93 for Como (5.77 combined). The most likely exact score is 2-2 at 6.0%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 91.6%; Under 4.5 goals: 33.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 19.2% | 5.21 |
| Draw | 17.2% | 5.80 |
| Como win | 63.6% | 1.57 |

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
| 1 | 2-2 | 6.01% |
| 2 | 1-3 | 4.96% |
| 3 | 1-4 | 4.87% |
| 4 | 3-3 | 4.82% |
| 5 | 2-3 | 4.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 19.2% | 24.8% | 3.90 | -25.2% |
| Draw | 17.2% | 22.7% | 4.33 | -25.4% |
| Como win | 63.6% | 52.4% | 1.95 | +24.0% |
| Over 2.5 | 91.6% | 68.5% | 1.43 | +31.0% |
| Under 2.5 | 8.4% | 31.5% | 2.87 | -75.9% |

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
| Market best home last update utc | 2026-10-09T14:38:53Z |
| Market best draw last update utc | 2026-10-09T14:38:10Z |
| Market best away last update utc | 2026-10-09T14:38:27Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 83.8% |
| P btts no | 16.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 340.13 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 41.43 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 11.93 |
| Fair Over 3.5 odds | 1.22 |
| Fair Under 3.5 odds | 5.47 |
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
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.90 |
| Reference draw odds | 4.25 |
| Reference away odds | 1.88 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -5.7% |
| Draw probability edge | -5.5% |
| Away probability edge | +11.2% |
| Over 2.5 probability edge | +23.1% |
| Under 2.5 probability edge | -23.1% |
| Raw edge prob home | -0.1132 |
| Raw ev home | -0.4727 |
| Raw edge prob draw | -0.1102 |
| Raw ev draw | -0.4924 |
| Raw edge prob away | 0.2234 |
| Raw ev away | 0.4578 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **72.9%**. Expected goals are 0.33 for LASK and 1.48 for Liverpool (1.80 combined). The most likely exact score is 0-1 at 26.9%. Goal-market probabilities: at least one goal: 87.5%; Over 2.5 goals: 28.9%; Under 4.5 goals: 96.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 8.0% | 12.58 |
| Draw | 19.2% | 5.21 |
| Liverpool win | 72.9% | 1.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.33 |
| Liverpool expected goals | 1.48 |
| Expected total goals | 1.80 |
| Over 0.5 | 87.5% |
| Under 0.5 | 12.5% |
| Over 1.5 | 55.1% |
| Under 1.5 | 44.9% |
| Over 2.5 | 28.9% |
| Under 2.5 | 71.1% |
| Over 3.5 | 11.5% |
| Under 3.5 | 88.5% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 26.86% |
| 2 | 0-2 | 19.52% |
| 3 | 0-0 | 12.53% |
| 4 | 0-3 | 9.61% |
| 5 | 1-2 | 6.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 8.0% | 7.6% | 13.00 | +3.4% |
| Draw | 19.2% | 13.8% | 7.25 | +39.2% |
| Liverpool win | 72.9% | 78.7% | 1.29 | -6.0% |
| Over 2.5 | 28.9% | 71.6% | 1.38 | -60.2% |
| Under 2.5 | 71.1% | 28.4% | 3.10 | +120.6% |

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
| Market best home last update utc | 2026-10-09T14:38:28Z |
| Market best draw last update utc | 2026-10-09T14:38:29Z |
| Market best away last update utc | 2026-10-09T14:38:09Z |
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
| P btts yes | 20.1% |
| P btts no | 79.9% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 7.98 |
| Fair Over 1.5 odds | 1.82 |
| Fair Under 1.5 odds | 2.23 |
| Fair Over 2.5 odds | 3.47 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.67 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 25.30 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 8.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 67.0% |
| Raw p over 1 5 | 53.4% |
| Raw p under 3 5 | 89.1% |
| Raw p btts yes | 21.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 12.00 |
| Reference draw odds | 6.75 |
| Reference away odds | 1.26 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | +0.4% |
| Draw probability edge | +5.4% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -42.8% |
| Under 2.5 probability edge | +42.8% |
| Raw edge prob home | 0.0076 |
| Raw ev home | 0.0827 |
| Raw edge prob draw | 0.1086 |
| Raw ev draw | 0.7856 |
| Raw edge prob away | -0.1162 |
| Raw ev away | -0.1352 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **46.7%**. Expected goals are 1.53 for Manchester City and 2.51 for Paris Saint Germain (4.04 combined). The most likely exact score is 2-2 at 7.5%. Goal-market probabilities: at least one goal: 98.4%; Over 2.5 goals: 75.5%; Under 4.5 goals: 63.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 32.6% | 3.07 |
| Draw | 20.7% | 4.82 |
| Paris Saint Germain win | 46.7% | 2.14 |

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
| Over 2.5 | 75.5% |
| Under 2.5 | 24.5% |
| Over 3.5 | 56.3% |
| Under 3.5 | 43.7% |
| Over 4.5 | 36.6% |
| Under 4.5 | 63.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.53% |
| 2 | 1-1 | 7.45% |
| 3 | 2-1 | 7.37% |
| 4 | 1-2 | 6.69% |
| 5 | 1-3 | 5.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 32.6% | 42.2% | 2.34 | -23.8% |
| Draw | 20.7% | 23.6% | 4.30 | -10.8% |
| Paris Saint Germain win | 46.7% | 34.2% | 2.97 | +38.7% |
| Over 2.5 | 75.5% | 67.0% | 1.44 | +8.8% |
| Under 2.5 | 24.5% | 33.0% | 2.87 | -29.7% |

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
| Market best home last update utc | 2026-10-09T14:38:09Z |
| Market best draw last update utc | 2026-10-09T14:38:41Z |
| Market best away last update utc | 2026-10-09T14:38:09Z |
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
| Fair Under 0.5 odds | 60.63 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.29 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.09 |
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
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.32 |
| Reference draw odds | 4.10 |
| Reference away odds | 2.85 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -9.7% |
| Draw probability edge | -2.8% |
| Away probability edge | +12.5% |
| Over 2.5 probability edge | +8.5% |
| Under 2.5 probability edge | -8.5% |
| Raw edge prob home | -0.1933 |
| Raw ev home | -0.4641 |
| Raw edge prob draw | -0.0566 |
| Raw ev draw | -0.2301 |
| Raw edge prob away | 0.2499 |
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
| Draw | 17.1% | 5.86 |
| Porto win | 18.1% | 5.52 |

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
| Over 3.5 | 81.7% |
| Under 3.5 | 18.3% |
| Over 4.5 | 66.1% |
| Under 4.5 | 33.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.14% |
| 2 | 4-1 | 4.88% |
| 3 | 3-3 | 4.54% |
| 4 | 5-1 | 4.40% |
| 5 | 3-1 | 4.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 64.8% | 44.1% | 2.27 | +47.1% |
| Draw | 17.1% | 26.3% | 3.80 | -35.2% |
| Porto win | 18.1% | 29.6% | 3.30 | -40.2% |
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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:38:09Z |
| Market best draw last update utc | 2026-10-09T14:38:44Z |
| Market best away last update utc | 2026-10-09T14:38:10Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 79.9% |
| P btts no | 20.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 269.38 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 39.21 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 11.40 |
| Fair Over 3.5 odds | 1.22 |
| Fair Under 3.5 odds | 5.45 |
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
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.23 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | +20.7% |
| Draw probability edge | -9.3% |
| Away probability edge | -11.4% |
| Over 2.5 probability edge | +35.0% |
| Under 2.5 probability edge | -35.0% |
| Raw edge prob home | 0.4141 |
| Raw ev home | 0.9415 |
| Raw edge prob draw | -0.1852 |
| Raw ev draw | -0.7037 |
| Raw edge prob away | -0.2290 |
| Raw ev away | -0.7797 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **38.6%**. Expected goals are 1.45 for Shakhtar Donetsk and 1.25 for AEK Athens (2.71 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 50.4%; Under 4.5 goals: 86.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 38.6% | 2.59 |
| Draw | 25.5% | 3.92 |
| AEK Athens win | 35.8% | 2.79 |

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
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.7% |
| Under 3.5 | 71.3% |
| Over 4.5 | 13.7% |
| Under 4.5 | 86.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.08% |
| 2 | 0-1 | 9.68% |
| 3 | 1-0 | 9.40% |
| 4 | 1-2 | 8.22% |
| 5 | 2-1 | 8.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 38.6% | 34.9% | 2.81 | +8.6% |
| Draw | 25.5% | 26.6% | 3.65 | -6.8% |
| AEK Athens win | 35.8% | 38.4% | 2.65 | -5.1% |
| Over 2.5 | 50.4% | 52.3% | 1.91 | -3.7% |
| Under 2.5 | 49.6% | 47.7% | 2.03 | +0.6% |

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
| Market best home last update utc | 2026-10-09T14:38:09Z |
| Market best draw last update utc | 2026-10-09T14:38:53Z |
| Market best away last update utc | 2026-10-09T14:38:29Z |
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
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.78 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.32 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 42.4% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 54.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.55 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +3.7% |
| Draw probability edge | -1.1% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.0743 |
| Raw ev home | 0.1903 |
| Raw edge prob draw | -0.0223 |
| Raw ev draw | -0.1089 |
| Raw edge prob away | -0.0520 |
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
| Draw | 17.3% | 5.78 |
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
| 1 | 1-2 | 10.83% |
| 2 | 1-3 | 7.94% |
| 3 | 0-2 | 7.75% |
| 4 | 0-1 | 7.55% |
| 5 | 1-1 | 7.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.1% | 9.8% | 9.90 | +69.3% |
| Draw | 17.3% | 15.1% | 6.25 | +8.1% |
| VfB Stuttgart win | 65.6% | 75.1% | 1.35 | -11.4% |
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
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:38:29Z |
| Market best draw last update utc | 2026-10-09T14:38:29Z |
| Market best away last update utc | 2026-10-09T14:38:09Z |
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
| P btts yes | 65.6% |
| P btts no | 34.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 48.51 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.94 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.41 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.97 |
| Fair Over 4.5 odds | 3.32 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 56.1% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 51.6% |
| Raw p btts yes | 66.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 9.50 |
| Reference draw odds | 6.25 |
| Reference away odds | 1.32 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +7.3% |
| Draw probability edge | +2.2% |
| Away probability edge | -9.5% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.1460 |
| Raw ev home | 1.4158 |
| Raw edge prob draw | 0.0440 |
| Raw ev draw | 0.2189 |
| Raw edge prob away | -0.1900 |
| Raw ev away | -0.2427 |

</details>


---
