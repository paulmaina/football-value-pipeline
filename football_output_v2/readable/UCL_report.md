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
| Optimizer objective | 1537.063 |
| Base scoring parameter | 0.141 |
| Home-advantage parameter | 0.278 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0 |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 2.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-13 — Arsenal vs Lille

The model's most likely 1X2 outcome is **Arsenal win** at **74.4%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.4%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 49.4%; Under 3.5 goals: 73.0%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 39.5%; BTTS No (at least one team does not score): 60.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 74.4% | 1.34 |
| Draw | 16.7% | 6.00 |
| Lille win | 8.9% | 11.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.93 |
| Lille expected goals | 0.65 |
| Expected total goals | 2.58 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 49.4% |
| Under 2.5 | 50.6% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.43% |
| 2 | 2-0 | 15.34% |
| 3 | 2-1 | 10.03% |
| 4 | 3-0 | 9.87% |
| 5 | 1-1 | 7.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 74.4% | 80.6% | 1.28 | -4.8% |
| Draw | 16.7% | 13.7% | 7.20 | +20.0% |
| Lille win | 8.9% | 5.6% | 16.00 | +42.7% |
| Over 2.5 | 49.4% | 61.9% | 1.64 | -19.0% |
| Under 2.5 | 50.6% | 38.1% | 2.46 | +24.5% |

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
| Market best home last update utc | 2026-10-12T16:30:40Z |
| Market best draw last update utc | 2026-10-12T16:31:23Z |
| Market best away last update utc | 2026-10-12T16:31:39Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 39.5% |
| P btts no | 60.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.61 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.71 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.91 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 72.5% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 40.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.23 |
| Reference draw odds | 6.75 |
| Reference away odds | 16.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | -6.2% |
| Draw probability edge | +2.9% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | -0.1247 |
| Raw ev home | -0.1274 |
| Raw edge prob draw | 0.0585 |
| Raw ev draw | 0.4107 |
| Raw edge prob away | 0.0663 |
| Raw ev away | 0.9575 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **63.1%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.7%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.8%; Under 3.5 goals: 24.7%; Under 4.5 goals: 42.5%; BTTS Yes (both teams score): 78.8%; BTTS No (at least one team does not score): 21.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 63.1% | 1.58 |
| Draw | 17.8% | 5.61 |
| Manchester United win | 19.0% | 5.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 3.73 |
| Manchester United expected goals | 1.54 |
| Expected total goals | 5.27 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 87.8% |
| Under 2.5 | 12.2% |
| Over 3.5 | 75.3% |
| Under 3.5 | 24.7% |
| Over 4.5 | 57.5% |
| Under 4.5 | 42.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.65% |
| 2 | 3-1 | 5.62% |
| 3 | 4-1 | 5.23% |
| 4 | 2-1 | 4.53% |
| 5 | 1-1 | 4.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 63.1% | 49.2% | 2.00 | +26.3% |
| Draw | 17.8% | 24.2% | 4.11 | -26.8% |
| Manchester United win | 19.0% | 26.6% | 3.90 | -25.7% |
| Over 2.5 | 87.8% | 64.3% | 1.51 | +32.6% |
| Under 2.5 | 12.2% | 35.7% | 2.60 | -68.3% |

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
| Market best home last update utc | 2026-10-12T16:31:09Z |
| Market best draw last update utc | 2026-10-12T16:31:09Z |
| Market best away last update utc | 2026-10-12T16:31:23Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 78.8% |
| P btts no | 21.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 174.33 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.09 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.21 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.06 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.35 |
| Unadjusted home-win probability | 77.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 23.0% |
| Raw p btts yes | 76.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.00 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.65 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.58 |
| Home probability edge | +13.9% |
| Draw probability edge | -6.4% |
| Away probability edge | -7.5% |
| Over 2.5 probability edge | +23.5% |
| Under 2.5 probability edge | -23.5% |
| Raw edge prob home | 0.2788 |
| Raw ev home | 0.5418 |
| Raw edge prob draw | -0.1280 |
| Raw ev draw | -0.5309 |
| Raw edge prob away | -0.1509 |
| Raw ev away | -0.5515 |
| Market p over 1 5 | 85.2% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-12T16:31:12Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 58.4% |
| Market under 3 5 odds | 1.74 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-12T16:29:56Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.15 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 66.5% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-12T16:31:23Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.81 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **68.3%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 98.7%; Over 2.5 goals: 77.7%; Under 3.5 goals: 41.7%; Under 4.5 goals: 61.1%; BTTS Yes (both teams score): 70.9%; BTTS No (at least one team does not score): 29.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 15.8% | 6.32 |
| Draw | 15.9% | 6.31 |
| Barcelona win | 68.3% | 1.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.53 |
| Barcelona expected goals | 2.51 |
| Expected total goals | 4.04 |
| Over 0.5 | 98.7% |
| Under 0.5 | 1.3% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 77.7% |
| Under 2.5 | 22.3% |
| Over 3.5 | 58.3% |
| Under 3.5 | 41.7% |
| Over 4.5 | 38.9% |
| Under 4.5 | 61.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.77% |
| 2 | 1-3 | 8.17% |
| 3 | 0-2 | 6.37% |
| 4 | 2-3 | 6.27% |
| 5 | 2-2 | 5.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 15.8% | 8.7% | 10.50 | +66.1% |
| Draw | 15.9% | 13.8% | 7.40 | +17.3% |
| Barcelona win | 68.3% | 77.4% | 1.33 | -9.1% |
| Over 2.5 | 77.7% | 81.6% | 1.20 | -6.7% |
| Under 2.5 | 22.3% | 18.4% | 4.61 | +2.7% |

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
| Market best home last update utc | 2026-10-12T16:31:24Z |
| Market best draw last update utc | 2026-10-12T16:31:23Z |
| Market best away last update utc | 2026-10-12T16:30:40Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.9% |
| P btts no | 29.1% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 79.78 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.36 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.49 |
| Fair Over 3.5 odds | 1.71 |
| Fair Under 3.5 odds | 2.40 |
| Fair Over 4.5 odds | 2.57 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.5% |
| Raw p btts yes | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 10.50 |
| Reference draw odds | 6.75 |
| Reference away odds | 1.28 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.55 |
| Home probability edge | +7.1% |
| Draw probability edge | +2.0% |
| Away probability edge | -9.1% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | 0.1415 |
| Raw ev home | 1.4043 |
| Raw edge prob draw | 0.0406 |
| Raw ev draw | 0.3237 |
| Raw edge prob away | -0.1822 |
| Raw ev away | -0.2125 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **69.4%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 56.2%; Under 3.5 goals: 66.8%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 50.4%; BTTS No (at least one team does not score): 49.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 69.4% | 1.44 |
| Draw | 17.7% | 5.65 |
| Club Brugge win | 12.9% | 7.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.92 |
| Club Brugge expected goals | 0.94 |
| Expected total goals | 2.86 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 56.2% |
| Under 2.5 | 43.8% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.11% |
| 2 | 2-0 | 12.02% |
| 3 | 2-1 | 11.34% |
| 4 | 1-1 | 8.37% |
| 5 | 3-0 | 7.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 69.4% | 78.1% | 1.31 | -9.1% |
| Draw | 17.7% | 14.6% | 7.00 | +23.8% |
| Club Brugge win | 12.9% | 7.3% | 12.50 | +61.6% |
| Over 2.5 | 56.2% | 68.2% | 1.43 | -19.6% |
| Under 2.5 | 43.8% | 31.8% | 2.90 | +27.0% |

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
| Market best home last update utc | 2026-10-12T16:30:40Z |
| Market best draw last update utc | 2026-10-12T16:31:23Z |
| Market best away last update utc | 2026-10-12T16:31:39Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.4% |
| P btts no | 49.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.61 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.62 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 51.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.27 |
| Reference draw odds | 6.40 |
| Reference away odds | 12.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.85 |
| Home probability edge | -8.7% |
| Draw probability edge | +3.1% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -12.0% |
| Under 2.5 probability edge | +12.0% |
| Raw edge prob home | -0.1737 |
| Raw ev home | -0.2048 |
| Raw edge prob draw | 0.0614 |
| Raw ev draw | 0.4531 |
| Raw edge prob away | 0.1123 |
| Raw ev away | 1.3177 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **45.3%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 68.1%; Under 3.5 goals: 53.6%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 45.3% | 2.21 |
| Draw | 21.1% | 4.73 |
| PSV Eindhoven win | 33.5% | 2.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.65 |
| PSV Eindhoven expected goals | 1.87 |
| Expected total goals | 3.52 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 86.0% |
| Under 1.5 | 14.0% |
| Over 2.5 | 68.1% |
| Under 2.5 | 31.9% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.78% |
| 2 | 1-1 | 8.67% |
| 3 | 2-2 | 7.03% |
| 4 | 1-0 | 6.95% |
| 5 | 1-2 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 45.3% | 55.7% | 1.81 | -17.9% |
| Draw | 21.1% | 21.1% | 4.90 | +3.6% |
| PSV Eindhoven win | 33.5% | 23.2% | 4.25 | +42.5% |
| Over 2.5 | 68.1% | 73.3% | 1.33 | -9.5% |
| Under 2.5 | 31.9% | 26.7% | 3.37 | +7.6% |

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
| Market best home last update utc | 2026-10-12T16:31:09Z |
| Market best draw last update utc | 2026-10-12T16:31:23Z |
| Market best away last update utc | 2026-10-12T16:31:24Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.9% |
| P btts no | 32.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.86 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.12 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.13 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.62 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 35.0% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 67.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.76 |
| Reference draw odds | 4.50 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.35 |
| Home probability edge | -10.4% |
| Draw probability edge | +0.1% |
| Away probability edge | +10.3% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.2073 |
| Raw ev home | -0.3669 |
| Raw edge prob draw | 0.0010 |
| Raw ev draw | 0.0380 |
| Raw edge prob away | 0.2062 |
| Raw ev away | 0.8631 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **40.6%**. Expected goals are 1.28 for RC Lens and 1.60 for Sporting Lisbon (2.89 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.7%; Under 3.5 goals: 67.4%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 35.0% | 2.86 |
| Draw | 24.4% | 4.10 |
| Sporting Lisbon win | 40.6% | 2.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.28 |
| Sporting Lisbon expected goals | 1.60 |
| Expected total goals | 2.89 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 54.7% |
| Under 2.5 | 45.3% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.40% |
| 2 | 1-0 | 8.66% |
| 3 | 0-1 | 8.50% |
| 4 | 2-1 | 8.25% |
| 5 | 1-2 | 8.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 35.0% | 38.7% | 2.64 | -7.7% |
| Draw | 24.4% | 25.5% | 3.90 | -4.8% |
| Sporting Lisbon win | 40.6% | 35.8% | 2.74 | +11.3% |
| Over 2.5 | 54.7% | 60.8% | 1.64 | -10.3% |
| Under 2.5 | 45.3% | 39.2% | 2.46 | +11.5% |

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
| Market best home last update utc | 2026-10-12T16:31:23Z |
| Market best draw last update utc | 2026-10-12T16:30:45Z |
| Market best away last update utc | 2026-10-12T16:31:23Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 6.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Sporting Clube de Portugal |
| Home-name matching confidence | 86/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.13 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.10 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.50 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Home probability edge | -3.8% |
| Draw probability edge | -1.1% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.0753 |
| Raw ev home | -0.1760 |
| Raw edge prob draw | -0.0213 |
| Raw ev draw | -0.0897 |
| Raw edge prob away | 0.0966 |
| Raw ev away | 0.2452 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **52.9%**. Expected goals are 0.38 for Sabah FK and 1.28 for Slavia Praha (1.66 combined). The most likely exact score is 0-1 at 21.8%. Goal-market probabilities: at least one goal: 82.3%; Over 2.5 goals: 22.6%; Under 3.5 goals: 91.8%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 22.3%; BTTS No (at least one team does not score): 77.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 20.0% | 5.00 |
| Draw | 27.2% | 3.68 |
| Slavia Praha win | 52.9% | 1.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.38 |
| Slavia Praha expected goals | 1.28 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.3% |
| Under 0.5 | 17.7% |
| Over 1.5 | 47.1% |
| Under 1.5 | 52.9% |
| Over 2.5 | 22.6% |
| Under 2.5 | 77.4% |
| Over 3.5 | 8.2% |
| Under 3.5 | 91.8% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 21.81% |
| 2 | 0-0 | 17.66% |
| 3 | 0-2 | 13.71% |
| 4 | 1-0 | 13.45% |
| 5 | 1-1 | 8.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 20.0% | 28.5% | 3.74 | -25.3% |
| Draw | 27.2% | 25.8% | 3.86 | +4.8% |
| Slavia Praha win | 52.9% | 45.6% | 2.15 | +13.6% |
| Over 2.5 | 22.6% | 58.1% | 1.71 | -61.4% |
| Under 2.5 | 77.4% | 41.9% | 2.32 | +79.6% |

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
| Market best home last update utc | 2026-10-12T16:31:09Z |
| Market best draw last update utc | 2026-10-12T16:31:09Z |
| Market best away last update utc | 2026-10-12T16:31:39Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 22.3% |
| P btts no | 77.7% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.66 |
| Fair Over 1.5 odds | 2.12 |
| Fair Under 1.5 odds | 1.89 |
| Fair Over 2.5 odds | 4.42 |
| Fair Under 2.5 odds | 1.29 |
| Fair Over 3.5 odds | 12.26 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 39.03 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.4% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 60.1% |
| Raw p over 1 5 | 49.0% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 22.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.40 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -8.6% |
| Draw probability edge | +1.3% |
| Away probability edge | +7.2% |
| Over 2.5 probability edge | -35.5% |
| Under 2.5 probability edge | +35.5% |
| Raw edge prob home | -0.1712 |
| Raw ev home | -0.5729 |
| Raw edge prob draw | 0.0269 |
| Raw ev draw | 0.1004 |
| Raw edge prob away | 0.1443 |
| Raw ev away | 0.2915 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **92.1%**. Expected goals are 0.70 for Viking FK and 4.47 for Bayern Munich (5.17 combined). The most likely exact score is 0-4 at 9.4%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.1%; Under 3.5 goals: 25.0%; Under 4.5 goals: 42.2%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 2.6% | 38.57 |
| Draw | 5.3% | 18.81 |
| Bayern Munich win | 92.1% | 1.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.70 |
| Bayern Munich expected goals | 4.47 |
| Expected total goals | 5.17 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.1% |
| Under 1.5 | 3.9% |
| Over 2.5 | 88.1% |
| Under 2.5 | 11.9% |
| Over 3.5 | 75.0% |
| Under 3.5 | 25.0% |
| Over 4.5 | 57.8% |
| Under 4.5 | 42.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.37% |
| 2 | 0-3 | 8.38% |
| 3 | 0-5 | 8.37% |
| 4 | 1-4 | 6.53% |
| 5 | 0-6 | 6.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 2.6% | 3.2% | 26.00 | -32.6% |
| Draw | 5.3% | 6.5% | 15.50 | -17.6% |
| Bayern Munich win | 92.1% | 90.3% | 1.12 | +3.1% |
| Over 2.5 | 88.1% | 86.8% | 1.15 | +1.4% |
| Under 2.5 | 11.9% | 13.2% | 5.90 | -30.1% |

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
| Market best home last update utc | 2026-10-12T16:31:24Z |
| Market best draw last update utc | 2026-10-12T16:31:09Z |
| Market best away last update utc | 2026-10-12T16:31:23Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 161.62 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 25.83 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.44 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.00 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.37 |
| Unadjusted home-win probability | 2.0% |
| Unadjusted draw probability | 4.2% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.4% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 25.00 |
| Reference draw odds | 13.00 |
| Reference away odds | 1.10 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.13 |
| Reference Under 2.5 odds | 5.80 |
| Home probability edge | -0.6% |
| Draw probability edge | -1.1% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | -0.0124 |
| Raw ev home | -0.4876 |
| Raw edge prob draw | -0.0229 |
| Raw ev draw | -0.3536 |
| Raw edge prob away | 0.0354 |
| Raw ev away | 0.0512 |
| Market p over 1 5 | 95.8% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-12T16:31:12Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 8.60 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 31.1% |
| Market under 3 5 odds | 2.95 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-12T16:31:12Z |
| Market reference under 3 5 odds | 2.75 |
| Market reference under 3 5 opposite odds | 1.38 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 55.2% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-12T16:31:23Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.11 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **39.1%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.5%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 40.1%; Under 3.5 goals: 80.3%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 44.6%; BTTS No (at least one team does not score): 55.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 34.7% | 2.88 |
| Draw | 26.2% | 3.82 |
| Napoli win | 39.1% | 2.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.90 |
| Napoli expected goals | 1.42 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 65.6% |
| Under 1.5 | 34.4% |
| Over 2.5 | 40.1% |
| Under 2.5 | 59.9% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.48% |
| 2 | 1-1 | 12.10% |
| 3 | 0-1 | 11.51% |
| 4 | 0-0 | 9.38% |
| 5 | 2-1 | 8.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 34.7% | 45.0% | 2.29 | -20.5% |
| Draw | 26.2% | 26.5% | 3.86 | +1.0% |
| Napoli win | 39.1% | 28.5% | 3.40 | +33.1% |
| Over 2.5 | 40.1% | 59.0% | 1.71 | -31.5% |
| Under 2.5 | 59.9% | 41.0% | 2.32 | +39.0% |

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
| Market best home last update utc | 2026-10-12T16:31:09Z |
| Market best draw last update utc | 2026-10-12T16:30:46Z |
| Market best away last update utc | 2026-10-12T16:31:23Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.6% |
| P btts no | 55.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.66 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.11 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 44.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.18 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | -10.3% |
| Draw probability edge | -0.4% |
| Away probability edge | +10.6% |
| Over 2.5 probability edge | -18.9% |
| Under 2.5 probability edge | +18.9% |
| Raw edge prob home | -0.2052 |
| Raw ev home | -0.4401 |
| Raw edge prob draw | -0.0072 |
| Raw ev draw | -0.0043 |
| Raw edge prob away | 0.2124 |
| Raw ev away | 0.6916 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **50.2%**. Expected goals are 1.18 for AS Roma and 1.67 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.4%; Under 3.5 goals: 67.9%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.8% | 3.73 |
| Draw | 23.0% | 4.35 |
| Real Madrid win | 50.2% | 1.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.18 |
| Real Madrid expected goals | 1.67 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 54.4% |
| Under 2.5 | 45.6% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.79% |
| 2 | 0-1 | 10.35% |
| 3 | 1-2 | 9.67% |
| 4 | 0-2 | 8.18% |
| 5 | 1-0 | 7.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.8% | 26.1% | 3.88 | +4.1% |
| Draw | 23.0% | 22.9% | 4.20 | -3.5% |
| Real Madrid win | 50.2% | 50.9% | 1.97 | -1.1% |
| Over 2.5 | 54.4% | 67.9% | 1.43 | -22.2% |
| Under 2.5 | 45.6% | 32.1% | 2.88 | +31.3% |

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
| Market best home last update utc | 2026-10-12T16:31:09Z |
| Market best draw last update utc | 2026-10-12T16:31:23Z |
| Market best away last update utc | 2026-10-12T16:31:23Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.32 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.40 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.12 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.20 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 27.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 49.5% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.0% |
| Raw p btts yes | 55.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.70 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.93 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.85 |
| Home probability edge | +0.7% |
| Draw probability edge | +0.0% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -13.5% |
| Under 2.5 probability edge | +13.5% |
| Raw edge prob home | 0.0139 |
| Raw ev home | 0.0674 |
| Raw edge prob draw | 0.0008 |
| Raw ev draw | -0.0332 |
| Raw edge prob away | -0.0147 |
| Raw ev away | -0.0254 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **66.4%**. Expected goals are 2.23 for Aston Villa and 0.61 for Fenerbahce (2.84 combined). The most likely exact score is 2-0 at 12.9%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 51.5%; Under 3.5 goals: 70.0%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 41.8%; BTTS No (at least one team does not score): 58.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 66.4% | 1.51 |
| Draw | 19.9% | 5.03 |
| Fenerbahce win | 13.8% | 7.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.23 |
| Fenerbahce expected goals | 0.61 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 30.0% |
| Under 3.5 | 70.0% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.89% |
| 2 | 1-0 | 11.90% |
| 3 | 3-0 | 9.59% |
| 4 | 1-1 | 9.29% |
| 5 | 2-1 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 66.4% | 57.8% | 1.74 | +15.5% |
| Draw | 19.9% | 23.7% | 4.30 | -14.5% |
| Fenerbahce win | 13.8% | 18.6% | 5.50 | -24.3% |
| Over 2.5 | 51.5% | 56.2% | 1.74 | -10.4% |
| Under 2.5 | 48.5% | 43.8% | 2.29 | +11.1% |

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
| Market best home last update utc | 2026-10-12T16:31:09Z |
| Market best draw last update utc | 2026-10-12T16:31:23Z |
| Market best away last update utc | 2026-10-12T16:31:23Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 41.8% |
| P btts no | 58.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.88 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.05 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.79 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.1% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 40.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.71 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.20 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | +8.6% |
| Draw probability edge | -3.8% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | 0.1711 |
| Raw ev home | 0.3034 |
| Raw edge prob draw | -0.0754 |
| Raw ev draw | -0.3073 |
| Raw edge prob away | -0.0957 |
| Raw ev away | -0.5060 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **45.6%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-2 at 8.6%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.0%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 70.2%; BTTS No (at least one team does not score): 29.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 32.7% | 3.06 |
| Draw | 21.7% | 4.60 |
| Borussia Dortmund win | 45.6% | 2.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 1.73 |
| Borussia Dortmund expected goals | 1.94 |
| Expected total goals | 3.67 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 50.0% |
| Under 3.5 | 50.0% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.64% |
| 2 | 1-1 | 8.51% |
| 3 | 2-2 | 7.51% |
| 4 | 2-1 | 6.82% |
| 5 | 0-1 | 5.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 32.7% | 29.9% | 3.35 | +9.5% |
| Draw | 21.7% | 22.7% | 4.25 | -7.7% |
| Borussia Dortmund win | 45.6% | 47.4% | 2.14 | -2.4% |
| Over 2.5 | 70.7% | 69.8% | 1.40 | -1.1% |
| Under 2.5 | 29.3% | 30.2% | 3.03 | -11.2% |

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
| Market best home last update utc | 2026-10-12T16:31:23Z |
| Market best draw last update utc | 2026-10-12T16:31:39Z |
| Market best away last update utc | 2026-10-12T16:31:09Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.2% |
| P btts no | 29.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.92 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.13 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.41 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.28 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 35.5% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 50.1% |
| Raw p btts yes | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.25 |
| Reference draw odds | 4.25 |
| Reference away odds | 2.07 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +2.8% |
| Draw probability edge | -1.0% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.0563 |
| Raw ev home | 0.1893 |
| Raw edge prob draw | -0.0194 |
| Raw ev draw | -0.1182 |
| Raw edge prob away | -0.0369 |
| Raw ev away | -0.0637 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **62.5%**. Expected goals are 1.82 for Feyenoord and 3.81 for Como (5.63 combined). The most likely exact score is 2-2 at 6.2%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.8%; Under 3.5 goals: 19.7%; Under 4.5 goals: 35.9%; BTTS Yes (both teams score): 83.3%; BTTS No (at least one team does not score): 16.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 20.0% | 5.00 |
| Draw | 17.6% | 5.69 |
| Como win | 62.5% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 1.82 |
| Como expected goals | 3.81 |
| Expected total goals | 5.63 |
| Over 0.5 | 99.7% |
| Under 0.5 | 0.3% |
| Over 1.5 | 97.3% |
| Under 1.5 | 2.7% |
| Over 2.5 | 90.8% |
| Under 2.5 | 9.2% |
| Over 3.5 | 80.3% |
| Under 3.5 | 19.7% |
| Over 4.5 | 64.1% |
| Under 4.5 | 35.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.23% |
| 2 | 1-3 | 5.11% |
| 3 | 1-4 | 4.88% |
| 4 | 3-3 | 4.80% |
| 5 | 2-3 | 4.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 20.0% | 25.8% | 3.75 | -25.1% |
| Draw | 17.6% | 23.0% | 4.37 | -23.2% |
| Como win | 62.5% | 51.2% | 2.00 | +24.9% |
| Over 2.5 | 90.8% | 67.9% | 1.43 | +29.9% |
| Under 2.5 | 9.2% | 32.1% | 2.87 | -73.7% |

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
| Market best home last update utc | 2026-10-12T16:31:39Z |
| Market best draw last update utc | 2026-10-12T16:30:46Z |
| Market best away last update utc | 2026-10-12T16:31:23Z |
| Odds bookmakers 1x2 | 22.00 |
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
| P btts yes | 83.3% |
| P btts no | 16.7% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 295.46 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 37.04 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.92 |
| Fair Over 3.5 odds | 1.25 |
| Fair Under 3.5 odds | 5.08 |
| Fair Over 4.5 odds | 1.56 |
| Fair Under 4.5 odds | 2.79 |
| Unadjusted home-win probability | 14.2% |
| Unadjusted draw probability | 12.2% |
| Unadjusted away-win probability | 73.7% |
| Raw p over 1 5 | 97.5% |
| Raw p under 3 5 | 18.8% |
| Raw p btts yes | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.75 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.92 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.85 |
| Home probability edge | -5.8% |
| Draw probability edge | -5.4% |
| Away probability edge | +11.2% |
| Over 2.5 probability edge | +23.0% |
| Under 2.5 probability edge | -23.0% |
| Raw edge prob home | -0.1163 |
| Raw ev home | -0.4687 |
| Raw edge prob draw | -0.1080 |
| Raw ev draw | -0.4684 |
| Raw edge prob away | 0.2243 |
| Raw ev away | 0.4734 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-12T16:31:12Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 54.6% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-12T16:24:26Z |
| Market reference under 3 5 odds | 1.70 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 67.9% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-12T16:31:23Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.91 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **72.0%**. Expected goals are 0.28 for LASK and 1.45 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 27.6%. Goal-market probabilities: at least one goal: 86.2%; Over 2.5 goals: 26.7%; Under 3.5 goals: 89.7%; Under 4.5 goals: 96.6%; BTTS Yes (both teams score): 17.7%; BTTS No (at least one team does not score): 82.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 8.0% | 12.45 |
| Draw | 19.9% | 5.01 |
| Liverpool win | 72.0% | 1.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.45 |
| Expected total goals | 1.74 |
| Over 0.5 | 86.2% |
| Under 0.5 | 13.8% |
| Over 1.5 | 52.7% |
| Under 1.5 | 47.3% |
| Over 2.5 | 26.7% |
| Under 2.5 | 73.3% |
| Over 3.5 | 10.3% |
| Under 3.5 | 89.7% |
| Over 4.5 | 3.4% |
| Under 4.5 | 96.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 27.60% |
| 2 | 0-2 | 19.79% |
| 3 | 0-0 | 13.83% |
| 4 | 0-3 | 9.60% |
| 5 | 1-0 | 5.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 8.0% | 8.8% | 11.00 | -11.7% |
| Draw | 19.9% | 15.0% | 6.75 | +34.6% |
| Liverpool win | 72.0% | 76.2% | 1.32 | -4.9% |
| Over 2.5 | 26.7% | 69.8% | 1.39 | -63.0% |
| Under 2.5 | 73.3% | 30.2% | 3.10 | +127.4% |

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
| Market best home last update utc | 2026-10-12T16:31:24Z |
| Market best draw last update utc | 2026-10-12T16:31:11Z |
| Market best away last update utc | 2026-10-12T16:31:23Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 17.7% |
| P btts no | 82.3% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.23 |
| Fair Over 1.5 odds | 1.90 |
| Fair Under 1.5 odds | 2.11 |
| Fair Over 2.5 odds | 3.75 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 9.72 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 29.49 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 67.8% |
| Raw p over 1 5 | 51.4% |
| Raw p under 3 5 | 90.1% |
| Raw p btts yes | 18.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 10.50 |
| Reference draw odds | 6.25 |
| Reference away odds | 1.30 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -0.7% |
| Draw probability edge | +4.9% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -43.2% |
| Under 2.5 probability edge | +43.2% |
| Raw edge prob home | -0.0148 |
| Raw ev home | -0.1983 |
| Raw edge prob draw | 0.0988 |
| Raw ev draw | 0.6798 |
| Raw edge prob away | -0.0840 |
| Raw ev away | -0.1047 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **44.3%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 69.1%; Under 3.5 goals: 51.9%; Under 4.5 goals: 71.0%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 34.3% | 2.92 |
| Draw | 21.4% | 4.67 |
| Paris Saint Germain win | 44.3% | 2.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.40 |
| Paris Saint Germain expected goals | 2.23 |
| Expected total goals | 3.63 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 69.1% |
| Under 2.5 | 30.9% |
| Over 3.5 | 48.1% |
| Under 3.5 | 51.9% |
| Over 4.5 | 29.0% |
| Under 4.5 | 71.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.72% |
| 2 | 2-1 | 8.28% |
| 3 | 1-2 | 7.21% |
| 4 | 2-2 | 7.18% |
| 5 | 1-0 | 5.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 34.3% | 44.6% | 2.28 | -21.8% |
| Draw | 21.4% | 23.5% | 4.20 | -10.0% |
| Paris Saint Germain win | 44.3% | 31.9% | 3.10 | +37.3% |
| Over 2.5 | 69.1% | 67.2% | 1.45 | +0.3% |
| Under 2.5 | 30.9% | 32.8% | 2.80 | -13.6% |

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
| Market best home last update utc | 2026-10-12T16:30:41Z |
| Market best draw last update utc | 2026-10-12T16:31:23Z |
| Market best away last update utc | 2026-10-12T16:31:23Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.9% |
| P btts no | 32.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.39 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.52 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.24 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.45 |
| Fair Under 4.5 odds | 1.41 |
| Unadjusted home-win probability | 24.0% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 56.7% |
| Raw p over 1 5 | 87.3% |
| Raw p under 3 5 | 50.8% |
| Raw p btts yes | 66.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.20 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.78 |
| Home probability edge | -10.3% |
| Draw probability edge | -2.1% |
| Away probability edge | +12.4% |
| Over 2.5 probability edge | +1.9% |
| Under 2.5 probability edge | -1.9% |
| Raw edge prob home | -0.2055 |
| Raw ev home | -0.4523 |
| Raw edge prob draw | -0.0425 |
| Raw ev draw | -0.1895 |
| Raw edge prob away | 0.2479 |
| Raw ev away | 0.7571 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **60.8%**. Expected goals are 3.29 for Real Betis and 1.29 for Porto (4.58 combined). The most likely exact score is 2-2 at 7.1%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 80.9%; Under 3.5 goals: 35.2%; Under 4.5 goals: 54.9%; BTTS Yes (both teams score): 72.3%; BTTS No (at least one team does not score): 27.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 60.8% | 1.64 |
| Draw | 19.2% | 5.22 |
| Porto win | 20.0% | 4.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 3.29 |
| Porto expected goals | 1.29 |
| Expected total goals | 4.58 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 93.2% |
| Under 1.5 | 6.8% |
| Over 2.5 | 80.9% |
| Under 2.5 | 19.1% |
| Over 3.5 | 64.8% |
| Under 3.5 | 35.2% |
| Over 4.5 | 45.1% |
| Under 4.5 | 54.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.12% |
| 2 | 1-1 | 6.37% |
| 3 | 3-1 | 6.27% |
| 4 | 2-1 | 5.72% |
| 5 | 4-1 | 5.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 60.8% | 45.5% | 2.16 | +31.3% |
| Draw | 19.2% | 25.9% | 3.90 | -25.3% |
| Porto win | 20.0% | 28.6% | 3.55 | -28.9% |
| Over 2.5 | 80.9% | 56.8% | 1.79 | +44.8% |
| Under 2.5 | 19.1% | 43.2% | 2.28 | -56.5% |

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
| Market best home last update utc | 2026-10-12T16:31:09Z |
| Market best draw last update utc | 2026-10-12T16:31:23Z |
| Market best away last update utc | 2026-10-12T16:31:23Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 72.3% |
| P btts no | 27.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 80.51 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.70 |
| Fair Over 2.5 odds | 1.24 |
| Fair Under 2.5 odds | 5.24 |
| Fair Over 3.5 odds | 1.54 |
| Fair Under 3.5 odds | 2.84 |
| Fair Over 4.5 odds | 2.22 |
| Fair Under 4.5 odds | 1.82 |
| Unadjusted home-win probability | 76.1% |
| Unadjusted draw probability | 12.4% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 94.1% |
| Raw p under 3 5 | 32.9% |
| Raw p btts yes | 69.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.16 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | +15.3% |
| Draw probability edge | -6.7% |
| Away probability edge | -8.6% |
| Over 2.5 probability edge | +24.1% |
| Under 2.5 probability edge | -24.1% |
| Raw edge prob home | 0.3061 |
| Raw ev home | 0.6441 |
| Raw edge prob draw | -0.1345 |
| Raw ev draw | -0.5150 |
| Raw edge prob away | -0.1716 |
| Raw ev away | -0.5936 |
| Market p over 1 5 | 80.3% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-12T16:31:12Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 66.8% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-12T16:31:12Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 59.6% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-12T16:31:23Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.35 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.8%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 51.1%; Under 3.5 goals: 70.6%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.8% | 2.52 |
| Draw | 25.8% | 3.87 |
| AEK Athens win | 34.4% | 2.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.49 |
| AEK Athens expected goals | 1.25 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.20% |
| 2 | 1-0 | 9.38% |
| 3 | 0-1 | 9.19% |
| 4 | 2-1 | 8.22% |
| 5 | 1-2 | 7.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.8% | 36.3% | 2.81 | +11.7% |
| Draw | 25.8% | 27.4% | 3.58 | -7.6% |
| AEK Athens win | 34.4% | 36.3% | 2.80 | -3.6% |
| Over 2.5 | 51.1% | 52.0% | 1.93 | -1.5% |
| Under 2.5 | 48.9% | 48.0% | 2.03 | -0.6% |

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
| Market best home last update utc | 2026-10-12T16:31:09Z |
| Market best draw last update utc | 2026-10-12T16:31:09Z |
| Market best away last update utc | 2026-10-12T16:31:23Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 67/100 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.00 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.10 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 54.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | +3.5% |
| Draw probability edge | -1.6% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | 0.0696 |
| Raw ev home | 0.2150 |
| Raw edge prob draw | -0.0324 |
| Raw ev draw | -0.1338 |
| Raw edge prob away | -0.0372 |
| Raw ev away | -0.0882 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.1%**. Expected goals are 1.46 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 72.6%; Under 3.5 goals: 48.5%; Under 4.5 goals: 67.7%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.0% | 5.87 |
| Draw | 16.9% | 5.93 |
| VfB Stuttgart win | 66.1% | 1.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.46 |
| VfB Stuttgart expected goals | 2.25 |
| Expected total goals | 3.71 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 88.5% |
| Under 1.5 | 11.5% |
| Over 2.5 | 72.6% |
| Under 2.5 | 27.4% |
| Over 3.5 | 51.5% |
| Under 3.5 | 48.5% |
| Over 4.5 | 32.3% |
| Under 4.5 | 67.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.71% |
| 2 | 1-3 | 8.03% |
| 3 | 0-2 | 7.36% |
| 4 | 0-1 | 7.01% |
| 5 | 1-1 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.0% | 9.3% | 11.00 | +87.5% |
| Draw | 16.9% | 14.5% | 6.80 | +14.7% |
| VfB Stuttgart win | 66.1% | 76.3% | 1.31 | -13.4% |
| Over 2.5 | 72.6% | 72.5% | 1.35 | -2.0% |
| Under 2.5 | 27.4% | 27.5% | 3.26 | -10.7% |

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
| Market best home last update utc | 2026-10-12T16:31:24Z |
| Market best draw last update utc | 2026-10-12T16:31:23Z |
| Market best away last update utc | 2026-10-12T16:31:09Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.2% |
| P btts no | 32.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.56 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.66 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.65 |
| Fair Over 3.5 odds | 1.94 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.09 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 24.8% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 55.9% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 68.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 10.00 |
| Reference draw odds | 6.50 |
| Reference away odds | 1.30 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.25 |
| Home probability edge | +7.8% |
| Draw probability edge | +2.4% |
| Away probability edge | -10.2% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.1554 |
| Raw ev home | 1.7297 |
| Raw edge prob draw | 0.0479 |
| Raw ev draw | 0.3093 |
| Raw edge prob away | -0.2033 |
| Raw ev away | -0.2673 |

</details>


---
