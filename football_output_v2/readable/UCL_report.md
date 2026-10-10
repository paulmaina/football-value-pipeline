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

The model's most likely 1X2 outcome is **Arsenal win** at **72.4%**. Expected goals are 2.01 for Arsenal and 0.77 for Lille (2.78 combined). The most likely exact score is 1-0 at 14.0%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 54.0%; Under 3.5 goals: 68.8%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 45.2%; BTTS No (at least one team does not score): 54.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 72.4% | 1.38 |
| Draw | 16.9% | 5.93 |
| Lille win | 10.7% | 9.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 2.01 |
| Lille expected goals | 0.77 |
| Expected total goals | 2.78 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 77.0% |
| Under 1.5 | 23.0% |
| Over 2.5 | 54.0% |
| Under 2.5 | 46.0% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.99% |
| 2 | 2-0 | 13.55% |
| 3 | 2-1 | 10.45% |
| 4 | 3-0 | 9.09% |
| 5 | 1-1 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 72.4% | 78.0% | 1.30 | -5.9% |
| Draw | 16.9% | 14.5% | 7.00 | +18.1% |
| Lille win | 10.7% | 7.5% | 14.00 | +49.9% |
| Over 2.5 | 54.0% | 60.9% | 1.67 | -9.8% |
| Under 2.5 | 46.0% | 39.1% | 2.44 | +12.2% |

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
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:46:49Z |
| Market best away last update utc | 2026-10-10T15:46:49Z |
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
| Fair Under 0.5 odds | 20.01 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.34 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.42 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 19.2% |
| Unadjusted away-win probability | 13.9% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.26 |
| Reference draw odds | 6.00 |
| Reference away odds | 11.00 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | -5.5% |
| Draw probability edge | +2.4% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | -0.1107 |
| Raw ev home | -0.1305 |
| Raw edge prob draw | 0.0475 |
| Raw ev draw | 0.3474 |
| Raw edge prob away | 0.0632 |
| Raw ev away | 0.9416 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **60.8%**. Expected goals are 3.87 for Atlético Madrid and 1.70 for Manchester United (5.57 combined). The most likely exact score is 2-2 at 6.5%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 90.0%; Under 3.5 goals: 21.0%; Under 4.5 goals: 37.7%; BTTS Yes (both teams score): 82.1%; BTTS No (at least one team does not score): 17.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 60.8% | 1.65 |
| Draw | 18.0% | 5.55 |
| Manchester United win | 21.2% | 4.72 |

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
| 1 | 2-2 | 6.51% |
| 2 | 3-1 | 5.00% |
| 3 | 4-1 | 4.84% |
| 4 | 3-3 | 4.77% |
| 5 | 3-2 | 4.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 60.8% | 45.4% | 2.18 | +32.5% |
| Draw | 18.0% | 24.6% | 4.00 | -27.9% |
| Manchester United win | 21.2% | 30.0% | 3.50 | -25.9% |
| Over 2.5 | 90.0% | 63.8% | 1.50 | +35.0% |
| Under 2.5 | 10.0% | 36.2% | 2.66 | -73.4% |

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
| Market best home last update utc | 2026-10-10T15:46:49Z |
| Market best draw last update utc | 2026-10-10T15:46:49Z |
| Market best away last update utc | 2026-10-10T15:46:49Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 82.1% |
| P btts no | 17.9% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 248.35 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 33.26 |
| Fair Over 2.5 odds | 1.11 |
| Fair Under 2.5 odds | 10.01 |
| Fair Over 3.5 odds | 1.27 |
| Fair Under 3.5 odds | 4.76 |
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
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.12 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | +15.4% |
| Draw probability edge | -6.6% |
| Away probability edge | -8.8% |
| Over 2.5 probability edge | +26.2% |
| Under 2.5 probability edge | -26.2% |
| Raw edge prob home | 0.3073 |
| Raw ev home | 0.6601 |
| Raw edge prob draw | -0.1315 |
| Raw ev draw | -0.5417 |
| Raw edge prob away | -0.1758 |
| Raw ev away | -0.5663 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **66.5%**. Expected goals are 1.61 for Galatasaray and 2.47 for Barcelona (4.09 combined). The most likely exact score is 1-2 at 9.7%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 78.4%; Under 3.5 goals: 40.9%; Under 4.5 goals: 60.1%; BTTS Yes (both teams score): 72.1%; BTTS No (at least one team does not score): 27.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 17.9% | 5.59 |
| Draw | 15.7% | 6.39 |
| Barcelona win | 66.5% | 1.50 |

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
| Over 2.5 | 78.4% |
| Under 2.5 | 21.6% |
| Over 3.5 | 59.1% |
| Under 3.5 | 40.9% |
| Over 4.5 | 39.9% |
| Under 4.5 | 60.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.67% |
| 2 | 1-3 | 7.98% |
| 3 | 2-3 | 6.44% |
| 4 | 0-2 | 5.99% |
| 5 | 2-2 | 5.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 17.9% | 10.9% | 10.00 | +78.9% |
| Draw | 15.7% | 13.1% | 7.20 | +12.7% |
| Barcelona win | 66.5% | 76.0% | 1.34 | -10.9% |
| Over 2.5 | 78.4% | 81.3% | 1.21 | -5.1% |
| Under 2.5 | 21.6% | 18.7% | 4.50 | -2.8% |

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
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:46:49Z |
| Market best away last update utc | 2026-10-10T15:46:16Z |
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
| P btts yes | 72.1% |
| P btts no | 27.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 86.86 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.67 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.63 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.44 |
| Fair Over 4.5 odds | 2.51 |
| Fair Under 4.5 odds | 1.66 |
| Unadjusted home-win probability | 24.9% |
| Unadjusted draw probability | 18.2% |
| Unadjusted away-win probability | 56.9% |
| Raw p over 1 5 | 91.1% |
| Raw p under 3 5 | 41.6% |
| Raw p btts yes | 73.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 7.80 |
| Reference draw odds | 6.60 |
| Reference away odds | 1.29 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.40 |
| Home probability edge | +7.0% |
| Draw probability edge | +2.6% |
| Away probability edge | -9.5% |
| Over 2.5 probability edge | -2.9% |
| Under 2.5 probability edge | +2.9% |
| Raw edge prob home | 0.1393 |
| Raw ev home | 1.4854 |
| Raw edge prob draw | 0.0515 |
| Raw ev draw | 0.3126 |
| Raw edge prob away | -0.1908 |
| Raw ev away | -0.2373 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **68.4%**. Expected goals are 1.98 for Inter Milan and 1.01 for Club Brugge (2.99 combined). The most likely exact score is 1-0 at 11.9%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 58.8%; Under 3.5 goals: 64.2%; Under 4.5 goals: 81.0%; BTTS Yes (both teams score): 53.1%; BTTS No (at least one team does not score): 46.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 68.4% | 1.46 |
| Draw | 17.6% | 5.69 |
| Club Brugge win | 14.0% | 7.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.98 |
| Club Brugge expected goals | 1.01 |
| Expected total goals | 2.99 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 35.8% |
| Under 3.5 | 64.2% |
| Over 4.5 | 19.0% |
| Under 4.5 | 81.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.87% |
| 2 | 2-1 | 11.25% |
| 3 | 2-0 | 11.19% |
| 4 | 1-1 | 8.25% |
| 5 | 3-1 | 7.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 68.4% | 76.2% | 1.31 | -10.4% |
| Draw | 17.6% | 14.8% | 6.40 | +12.5% |
| Club Brugge win | 14.0% | 9.0% | 11.50 | +61.4% |
| Over 2.5 | 58.8% | 64.5% | 1.50 | -11.8% |
| Under 2.5 | 41.2% | 35.5% | 2.72 | +12.1% |

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
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:46:33Z |
| Market best away last update utc | 2026-10-10T15:46:49Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 53.1% |
| P btts no | 46.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.46 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.03 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.26 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 65.0% |
| Raw p btts yes | 54.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.29 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.60 |
| Home probability edge | -7.8% |
| Draw probability edge | +2.8% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | -0.1569 |
| Raw ev home | -0.2070 |
| Raw edge prob draw | 0.0556 |
| Raw ev draw | 0.3030 |
| Raw edge prob away | 0.1013 |
| Raw ev away | 1.1970 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **42.7%**. Expected goals are 1.58 for RB Leipzig and 1.78 for PSV Eindhoven (3.36 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 65.1%; Under 3.5 goals: 56.9%; Under 4.5 goals: 75.3%; BTTS Yes (both teams score): 65.7%; BTTS No (at least one team does not score): 34.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 42.7% | 2.34 |
| Draw | 22.0% | 4.55 |
| PSV Eindhoven win | 35.4% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.58 |
| PSV Eindhoven expected goals | 1.78 |
| Expected total goals | 3.36 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 84.2% |
| Under 1.5 | 15.8% |
| Over 2.5 | 65.1% |
| Under 2.5 | 34.9% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.43% |
| 2 | 1-1 | 9.39% |
| 3 | 1-0 | 7.31% |
| 4 | 1-2 | 7.09% |
| 5 | 2-2 | 6.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 42.7% | 50.5% | 1.96 | -16.4% |
| Draw | 22.0% | 22.2% | 4.40 | -3.4% |
| PSV Eindhoven win | 35.4% | 27.3% | 3.80 | +34.4% |
| Over 2.5 | 65.1% | 70.8% | 1.39 | -9.6% |
| Under 2.5 | 34.9% | 29.2% | 3.03 | +5.9% |

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
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:46:49Z |
| Market best away last update utc | 2026-10-10T15:46:49Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.7% |
| P btts no | 34.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.08 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.34 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.05 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 34.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 43.4% |
| Raw p over 1 5 | 84.4% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.92 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.45 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -7.8% |
| Draw probability edge | -0.3% |
| Away probability edge | +8.1% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.1559 |
| Raw ev home | -0.3163 |
| Raw edge prob draw | -0.0052 |
| Raw ev draw | -0.0452 |
| Raw edge prob away | 0.1611 |
| Raw ev away | 0.6498 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **41.8%**. Expected goals are 1.25 for RC Lens and 1.66 for Sporting Lisbon (2.91 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 55.2%; Under 3.5 goals: 67.0%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 34.1% | 2.94 |
| Draw | 24.1% | 4.15 |
| Sporting Lisbon win | 41.8% | 2.39 |

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
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 33.0% |
| Under 3.5 | 67.0% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.24% |
| 2 | 1-0 | 8.52% |
| 3 | 0-1 | 8.45% |
| 4 | 1-2 | 8.26% |
| 5 | 2-1 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 34.1% | 38.6% | 2.63 | -10.4% |
| Draw | 24.1% | 25.2% | 3.95 | -4.8% |
| Sporting Lisbon win | 41.8% | 36.2% | 2.72 | +13.8% |
| Over 2.5 | 55.2% | 61.0% | 1.64 | -9.5% |
| Under 2.5 | 44.8% | 39.0% | 2.46 | +10.3% |

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
| Market best home last update utc | 2026-10-10T15:46:49Z |
| Market best draw last update utc | 2026-10-10T15:46:33Z |
| Market best away last update utc | 2026-10-10T15:46:49Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Sporting Clube de Portugal |
| Home-name matching confidence | 86/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.59 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.53 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.03 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.97 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 47.5% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 66.7% |
| Raw p btts yes | 57.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.49 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | -4.6% |
| Draw probability edge | -1.1% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0913 |
| Raw ev home | -0.2244 |
| Raw edge prob draw | -0.0216 |
| Raw ev draw | -0.0903 |
| Raw edge prob away | 0.1129 |
| Raw ev away | 0.2914 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **53.7%**. Expected goals are 0.37 for Sabah FK and 1.26 for Slavia Praha (1.63 combined). The most likely exact score is 0-1 at 22.6%. Goal-market probabilities: at least one goal: 82.2%; Over 2.5 goals: 22.1%; Under 3.5 goals: 92.2%; Under 4.5 goals: 97.6%; BTTS Yes (both teams score): 21.7%; BTTS No (at least one team does not score): 78.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 19.2% | 5.20 |
| Draw | 27.1% | 3.70 |
| Slavia Praha win | 53.7% | 1.86 |

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
| Over 3.5 | 7.8% |
| Under 3.5 | 92.2% |
| Over 4.5 | 2.4% |
| Under 4.5 | 97.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.63% |
| 2 | 0-0 | 17.84% |
| 3 | 0-2 | 13.94% |
| 4 | 1-0 | 13.06% |
| 5 | 1-1 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 19.2% | 27.0% | 3.74 | -28.1% |
| Draw | 27.1% | 25.1% | 4.00 | +8.2% |
| Slavia Praha win | 53.7% | 47.9% | 2.08 | +11.7% |
| Over 2.5 | 22.1% | 57.9% | 1.71 | -62.3% |
| Under 2.5 | 77.9% | 42.1% | 2.32 | +80.8% |

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
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:46:17Z |
| Market best away last update utc | 2026-10-10T15:46:49Z |
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
| Fair Under 0.5 odds | 5.61 |
| Fair Over 1.5 odds | 2.15 |
| Fair Under 1.5 odds | 1.87 |
| Fair Over 2.5 odds | 4.53 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 12.76 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 41.18 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 11.5% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 59.5% |
| Raw p over 1 5 | 48.0% |
| Raw p under 3 5 | 91.7% |
| Raw p btts yes | 21.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.02 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.13 |
| Home probability edge | -7.7% |
| Draw probability edge | +2.0% |
| Away probability edge | +5.8% |
| Over 2.5 probability edge | -35.9% |
| Under 2.5 probability edge | +35.9% |
| Raw edge prob home | -0.1550 |
| Raw ev home | -0.5708 |
| Raw edge prob draw | 0.0393 |
| Raw ev draw | 0.1611 |
| Raw edge prob away | 0.1156 |
| Raw ev away | 0.2375 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **91.8%**. Expected goals are 0.69 for Viking FK and 4.47 for Bayern Munich (5.16 combined). The most likely exact score is 0-4 at 9.4%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.0%; Under 3.5 goals: 25.3%; Under 4.5 goals: 42.5%; BTTS Yes (both teams score): 49.8%; BTTS No (at least one team does not score): 50.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 2.8% | 35.26 |
| Draw | 5.3% | 18.74 |
| Bayern Munich win | 91.8% | 1.09 |

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
| Over 2.5 | 88.0% |
| Under 2.5 | 12.0% |
| Over 3.5 | 74.7% |
| Under 3.5 | 25.3% |
| Over 4.5 | 57.5% |
| Under 4.5 | 42.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.41% |
| 2 | 0-3 | 8.42% |
| 3 | 0-5 | 8.40% |
| 4 | 1-4 | 6.48% |
| 5 | 0-6 | 6.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 2.8% | 3.7% | 27.00 | -23.4% |
| Draw | 5.3% | 6.5% | 15.50 | -17.3% |
| Bayern Munich win | 91.8% | 89.7% | 1.11 | +1.9% |
| Over 2.5 | 88.0% | 84.9% | 1.15 | +1.2% |
| Under 2.5 | 12.0% | 15.1% | 5.90 | -29.1% |

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
| Market best home last update utc | 2026-10-10T15:46:04Z |
| Market best draw last update utc | 2026-10-10T15:46:16Z |
| Market best away last update utc | 2026-10-10T15:46:49Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 49.8% |
| P btts no | 50.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 157.94 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 25.20 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.32 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.96 |
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
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 18.00 |
| Reference draw odds | 11.00 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.00 |
| Home probability edge | -0.9% |
| Draw probability edge | -1.2% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +3.1% |
| Under 2.5 probability edge | -3.1% |
| Raw edge prob home | -0.0180 |
| Raw ev home | -0.4769 |
| Raw edge prob draw | -0.0241 |
| Raw ev draw | -0.3593 |
| Raw edge prob away | 0.0420 |
| Raw ev away | 0.0426 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **40.9%**. Expected goals are 0.87 for Villarreal and 1.43 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 40.0%; Under 3.5 goals: 80.5%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 44.0%; BTTS No (at least one team does not score): 56.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 33.4% | 2.99 |
| Draw | 25.7% | 3.89 |
| Napoli win | 40.9% | 2.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.87 |
| Napoli expected goals | 1.43 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 40.0% |
| Under 2.5 | 60.0% |
| Over 3.5 | 19.5% |
| Under 3.5 | 80.5% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.23% |
| 2 | 0-1 | 12.00% |
| 3 | 1-1 | 11.85% |
| 4 | 0-0 | 9.34% |
| 5 | 0-2 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 33.4% | 43.3% | 2.33 | -22.1% |
| Draw | 25.7% | 25.7% | 3.85 | -1.1% |
| Napoli win | 40.9% | 31.0% | 3.40 | +39.0% |
| Over 2.5 | 40.0% | 59.2% | 1.71 | -31.7% |
| Under 2.5 | 60.0% | 40.8% | 2.44 | +46.5% |

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
| Market best home last update utc | 2026-10-10T15:46:50Z |
| Market best draw last update utc | 2026-10-10T15:46:49Z |
| Market best away last update utc | 2026-10-10T15:46:49Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.0% |
| P btts no | 56.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.71 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.12 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.22 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 23.6% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 50.7% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 79.8% |
| Raw p btts yes | 43.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.22 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.19 |
| Home probability edge | -9.8% |
| Draw probability edge | -0.0% |
| Away probability edge | +9.9% |
| Over 2.5 probability edge | -19.3% |
| Under 2.5 probability edge | +19.3% |
| Raw edge prob home | -0.1970 |
| Raw ev home | -0.4502 |
| Raw edge prob draw | -0.0001 |
| Raw ev draw | -0.0113 |
| Raw edge prob away | 0.1970 |
| Raw ev away | 0.7246 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **51.3%**. Expected goals are 1.26 for AS Roma and 1.83 for Real Madrid (3.09 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 59.5%; Under 3.5 goals: 62.6%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 59.9%; BTTS No (at least one team does not score): 40.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.1% | 3.83 |
| Draw | 22.6% | 4.43 |
| Real Madrid win | 51.3% | 1.95 |

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
| Over 2.5 | 59.5% |
| Under 2.5 | 40.5% |
| Over 3.5 | 37.4% |
| Under 3.5 | 62.6% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.30% |
| 2 | 1-2 | 9.60% |
| 3 | 0-1 | 8.82% |
| 4 | 0-2 | 7.61% |
| 5 | 2-1 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.1% | 25.4% | 4.10 | +7.0% |
| Draw | 22.6% | 23.4% | 4.30 | -2.9% |
| Real Madrid win | 51.3% | 51.3% | 1.95 | +0.1% |
| Over 2.5 | 59.5% | 67.0% | 1.44 | -14.2% |
| Under 2.5 | 40.5% | 33.0% | 2.95 | +19.3% |

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
| Market best home last update utc | 2026-10-10T15:46:04Z |
| Market best draw last update utc | 2026-10-10T15:46:49Z |
| Market best away last update utc | 2026-10-10T15:46:17Z |
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
| Fair Under 0.5 odds | 24.10 |
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
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.70 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.89 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | +0.7% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | 0.0150 |
| Raw ev home | 0.1008 |
| Raw edge prob draw | -0.0155 |
| Raw ev draw | -0.0620 |
| Raw edge prob away | 0.0005 |
| Raw ev away | 0.0011 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **66.4%**. Expected goals are 2.22 for Aston Villa and 0.60 for Fenerbahce (2.83 combined). The most likely exact score is 2-0 at 13.0%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 51.2%; Under 3.5 goals: 70.3%; Under 4.5 goals: 85.5%; BTTS Yes (both teams score): 41.4%; BTTS No (at least one team does not score): 58.6%.

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
| Aston Villa win | 66.4% | 57.9% | 1.75 | +16.2% |
| Draw | 19.7% | 23.3% | 4.25 | -16.2% |
| Fenerbahce win | 13.9% | 18.8% | 5.40 | -25.1% |
| Over 2.5 | 51.2% | 58.3% | 1.74 | -10.9% |
| Under 2.5 | 48.8% | 41.7% | 2.28 | +11.2% |

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
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:46:16Z |
| Market best away last update utc | 2026-10-10T15:46:49Z |
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
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.68 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.90 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | +8.5% |
| Draw probability edge | -3.5% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | 0.1693 |
| Raw ev home | 0.3103 |
| Raw edge prob draw | -0.0710 |
| Raw ev draw | -0.3129 |
| Raw edge prob away | -0.0983 |
| Raw ev away | -0.5162 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **46.8%**. Expected goals are 1.67 for Bodø/Glimt and 2.04 for Borussia Dortmund (3.70 combined). The most likely exact score is 1-1 at 8.5%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 71.1%; Under 3.5 goals: 49.3%; Under 4.5 goals: 68.9%; BTTS Yes (both teams score): 70.5%; BTTS No (at least one team does not score): 29.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 31.3% | 3.20 |
| Draw | 21.9% | 4.56 |
| Borussia Dortmund win | 46.8% | 2.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 1.67 |
| Borussia Dortmund expected goals | 2.04 |
| Expected total goals | 3.70 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 88.0% |
| Under 1.5 | 12.0% |
| Over 2.5 | 71.1% |
| Under 2.5 | 28.9% |
| Over 3.5 | 50.7% |
| Under 3.5 | 49.3% |
| Over 4.5 | 31.1% |
| Under 4.5 | 68.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.53% |
| 2 | 1-2 | 8.46% |
| 3 | 2-2 | 7.62% |
| 4 | 2-1 | 6.72% |
| 5 | 1-3 | 5.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 31.3% | 30.1% | 3.30 | +3.3% |
| Draw | 21.9% | 23.4% | 4.30 | -5.7% |
| Borussia Dortmund win | 46.8% | 46.5% | 2.14 | +0.1% |
| Over 2.5 | 71.1% | 69.0% | 1.40 | -0.4% |
| Under 2.5 | 28.9% | 31.0% | 3.03 | -12.6% |

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
| Market best home last update utc | 2026-10-10T15:46:49Z |
| Market best draw last update utc | 2026-10-10T15:46:17Z |
| Market best away last update utc | 2026-10-10T15:46:16Z |
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
| P btts yes | 70.5% |
| P btts no | 29.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.54 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.37 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.47 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.22 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 32.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 47.1% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 70.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.15 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.08 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +1.2% |
| Draw probability edge | -1.5% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | 0.0240 |
| Raw ev home | 0.0723 |
| Raw edge prob draw | -0.0301 |
| Raw ev draw | -0.1217 |
| Raw edge prob away | 0.0062 |
| Raw ev away | 0.0075 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **63.0%**. Expected goals are 1.84 for Feyenoord and 3.93 for Como (5.77 combined). The most likely exact score is 2-2 at 6.0%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 91.6%; Under 3.5 goals: 18.3%; Under 4.5 goals: 34.0%; BTTS Yes (both teams score): 83.9%; BTTS No (at least one team does not score): 16.1%.

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
| Over 4.5 | 66.0% |
| Under 4.5 | 34.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.00% |
| 2 | 1-3 | 4.91% |
| 3 | 1-4 | 4.82% |
| 4 | 3-3 | 4.82% |
| 5 | 2-3 | 4.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 19.8% | 26.0% | 3.85 | -23.8% |
| Draw | 17.2% | 22.7% | 4.33 | -25.4% |
| Como win | 63.0% | 51.2% | 1.95 | +22.8% |
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
| Market best home last update utc | 2026-10-10T15:46:49Z |
| Market best draw last update utc | 2026-10-10T15:45:57Z |
| Market best away last update utc | 2026-10-10T15:46:49Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 83.9% |
| P btts no | 16.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 340.44 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 41.09 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 11.90 |
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
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.60 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.89 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -6.3% |
| Draw probability edge | -5.5% |
| Away probability edge | +11.8% |
| Over 2.5 probability edge | +23.1% |
| Under 2.5 probability edge | -23.1% |
| Raw edge prob home | -0.1252 |
| Raw ev home | -0.4795 |
| Raw edge prob draw | -0.1099 |
| Raw ev draw | -0.4924 |
| Raw edge prob away | 0.2352 |
| Raw ev away | 0.4578 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **72.3%**. Expected goals are 0.33 for LASK and 1.48 for Liverpool (1.80 combined). The most likely exact score is 0-1 at 26.6%. Goal-market probabilities: at least one goal: 87.5%; Over 2.5 goals: 28.8%; Under 3.5 goals: 88.5%; Under 4.5 goals: 96.1%; BTTS Yes (both teams score): 20.1%; BTTS No (at least one team does not score): 79.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 8.5% | 11.72 |
| Draw | 19.2% | 5.21 |
| Liverpool win | 72.3% | 1.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.33 |
| Liverpool expected goals | 1.48 |
| Expected total goals | 1.80 |
| Over 0.5 | 87.5% |
| Under 0.5 | 12.5% |
| Over 1.5 | 54.9% |
| Under 1.5 | 45.1% |
| Over 2.5 | 28.8% |
| Under 2.5 | 71.2% |
| Over 3.5 | 11.5% |
| Under 3.5 | 88.5% |
| Over 4.5 | 3.9% |
| Under 4.5 | 96.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 26.65% |
| 2 | 0-2 | 19.36% |
| 3 | 0-0 | 12.53% |
| 4 | 0-3 | 9.53% |
| 5 | 1-2 | 6.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 8.5% | 8.7% | 12.00 | +2.4% |
| Draw | 19.2% | 13.8% | 7.10 | +36.4% |
| Liverpool win | 72.3% | 77.5% | 1.29 | -6.8% |
| Over 2.5 | 28.8% | 71.6% | 1.37 | -60.6% |
| Under 2.5 | 71.2% | 28.4% | 3.13 | +123.0% |

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
| Market best home last update utc | 2026-10-10T15:46:04Z |
| Market best draw last update utc | 2026-10-10T15:45:57Z |
| Market best away last update utc | 2026-10-10T15:46:16Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 20.1% |
| P btts no | 79.9% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 7.98 |
| Fair Over 1.5 odds | 1.82 |
| Fair Under 1.5 odds | 2.22 |
| Fair Over 2.5 odds | 3.48 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.72 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 25.44 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 8.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 67.0% |
| Raw p over 1 5 | 53.4% |
| Raw p under 3 5 | 89.1% |
| Raw p btts yes | 21.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 9.80 |
| Reference draw odds | 6.40 |
| Reference away odds | 1.27 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -0.2% |
| Draw probability edge | +5.4% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | -42.9% |
| Under 2.5 probability edge | +42.9% |
| Raw edge prob home | -0.0042 |
| Raw ev home | -0.0006 |
| Raw edge prob draw | 0.1085 |
| Raw ev draw | 0.7487 |
| Raw edge prob away | -0.1043 |
| Raw ev away | -0.1352 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **46.9%**. Expected goals are 1.53 for Manchester City and 2.51 for Paris Saint Germain (4.04 combined). The most likely exact score is 2-2 at 7.6%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 75.5%; Under 3.5 goals: 43.7%; Under 4.5 goals: 63.5%; BTTS Yes (both teams score): 72.9%; BTTS No (at least one team does not score): 27.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 32.1% | 3.12 |
| Draw | 21.0% | 4.77 |
| Paris Saint Germain win | 46.9% | 2.13 |

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
| 1 | 2-2 | 7.62% |
| 2 | 1-1 | 7.54% |
| 3 | 2-1 | 7.26% |
| 4 | 1-2 | 6.73% |
| 5 | 1-3 | 5.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 32.1% | 41.3% | 2.43 | -22.0% |
| Draw | 21.0% | 24.1% | 4.30 | -9.8% |
| Paris Saint Germain win | 46.9% | 34.7% | 2.88 | +35.2% |
| Over 2.5 | 75.5% | 67.0% | 1.45 | +9.4% |
| Under 2.5 | 24.5% | 33.0% | 2.80 | -31.3% |

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
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:46:49Z |
| Market best away last update utc | 2026-10-10T15:46:49Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 72.9% |
| P btts no | 27.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 59.92 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.31 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.08 |
| Fair Over 3.5 odds | 1.77 |
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
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.33 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.75 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -9.2% |
| Draw probability edge | -3.1% |
| Away probability edge | +12.3% |
| Over 2.5 probability edge | +8.4% |
| Under 2.5 probability edge | -8.4% |
| Raw edge prob home | -0.1835 |
| Raw ev home | -0.4434 |
| Raw edge prob draw | -0.0616 |
| Raw ev draw | -0.2301 |
| Raw edge prob away | 0.2451 |
| Raw ev away | 0.7047 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **64.7%**. Expected goals are 4.51 for Real Betis and 1.48 for Porto (5.98 combined). The most likely exact score is 2-2 at 6.1%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 91.2%; Under 3.5 goals: 18.4%; Under 4.5 goals: 33.9%; BTTS Yes (both teams score): 79.9%; BTTS No (at least one team does not score): 20.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 64.7% | 1.55 |
| Draw | 17.0% | 5.89 |
| Porto win | 18.4% | 5.44 |

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
| 2 | 4-1 | 4.87% |
| 3 | 3-3 | 4.51% |
| 4 | 5-1 | 4.39% |
| 5 | 3-1 | 4.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 64.7% | 43.8% | 2.27 | +46.8% |
| Draw | 17.0% | 26.1% | 3.80 | -35.5% |
| Porto win | 18.4% | 30.1% | 3.30 | -39.4% |
| Over 2.5 | 91.2% | 56.0% | 1.78 | +62.4% |
| Under 2.5 | 8.8% | 44.0% | 2.21 | -80.6% |

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
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:46:33Z |
| Market best away last update utc | 2026-10-10T15:46:16Z |
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
| Fair Under 0.5 odds | 270.73 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 39.01 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 11.40 |
| Fair Over 3.5 odds | 1.23 |
| Fair Under 3.5 odds | 5.44 |
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
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | +20.9% |
| Draw probability edge | -9.2% |
| Away probability edge | -11.7% |
| Over 2.5 probability edge | +35.2% |
| Under 2.5 probability edge | -35.2% |
| Raw edge prob home | 0.4174 |
| Raw ev home | 0.9415 |
| Raw edge prob draw | -0.1835 |
| Raw ev draw | -0.7037 |
| Raw edge prob away | -0.2339 |
| Raw ev away | -0.7797 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.2%**. Expected goals are 1.45 for Shakhtar Donetsk and 1.25 for AEK Athens (2.71 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 50.3%; Under 3.5 goals: 71.3%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 54.6%; BTTS No (at least one team does not score): 45.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.2% | 2.55 |
| Draw | 25.9% | 3.87 |
| AEK Athens win | 35.0% | 2.86 |

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
| Over 2.5 | 50.3% |
| Under 2.5 | 49.7% |
| Over 3.5 | 28.7% |
| Under 3.5 | 71.3% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.23% |
| 2 | 1-0 | 9.53% |
| 3 | 0-1 | 9.45% |
| 4 | 2-1 | 8.17% |
| 5 | 1-2 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.2% | 36.0% | 2.81 | +10.1% |
| Draw | 25.9% | 27.3% | 3.65 | -5.6% |
| AEK Athens win | 35.0% | 36.7% | 2.65 | -7.3% |
| Over 2.5 | 50.3% | 52.5% | 1.91 | -3.8% |
| Under 2.5 | 49.7% | 47.5% | 2.03 | +0.8% |

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
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:46:49Z |
| Market best away last update utc | 2026-10-10T15:46:48Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 67/100 |
| P btts yes | 54.6% |
| P btts no | 45.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.58 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.34 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 42.4% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 54.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.60 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 1.92 |
| Home probability edge | +3.2% |
| Draw probability edge | -1.4% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | 0.0637 |
| Raw ev home | 0.1903 |
| Raw edge prob draw | -0.0288 |
| Raw ev draw | -0.1089 |
| Raw edge prob away | -0.0349 |
| Raw ev away | -0.1195 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **65.5%**. Expected goals are 1.40 for ŠK Slovan Bratislava and 2.20 for VfB Stuttgart (3.60 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.9%; Under 4.5 goals: 69.9%; BTTS Yes (both teams score): 65.6%; BTTS No (at least one team does not score): 34.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.4% | 5.76 |
| Draw | 17.1% | 5.84 |
| VfB Stuttgart win | 65.5% | 1.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.40 |
| VfB Stuttgart expected goals | 2.20 |
| Expected total goals | 3.60 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 49.1% |
| Under 3.5 | 50.9% |
| Over 4.5 | 30.1% |
| Under 4.5 | 69.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.82% |
| 2 | 1-3 | 7.93% |
| 3 | 0-2 | 7.74% |
| 4 | 0-1 | 7.54% |
| 5 | 1-1 | 7.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.4% | 10.3% | 10.00 | +73.5% |
| Draw | 17.1% | 14.8% | 6.48 | +11.0% |
| VfB Stuttgart win | 65.5% | 74.9% | 1.35 | -11.5% |
| Over 2.5 | 70.7% | 70.8% | 1.36 | -3.8% |
| Under 2.5 | 29.3% | 29.2% | 3.18 | -6.9% |

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
| Market best home last update utc | 2026-10-10T15:46:16Z |
| Market best draw last update utc | 2026-10-10T15:46:16Z |
| Market best away last update utc | 2026-10-10T15:46:50Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.6% |
| P btts no | 34.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 49.00 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.93 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.41 |
| Fair Over 3.5 odds | 2.04 |
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
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 8.40 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.31 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +7.1% |
| Draw probability edge | +2.4% |
| Away probability edge | -9.4% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.1410 |
| Raw ev home | 1.4402 |
| Raw edge prob draw | 0.0475 |
| Raw ev draw | 0.2637 |
| Raw edge prob away | -0.1885 |
| Raw ev away | -0.2427 |

</details>


---
