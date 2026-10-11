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
| Additional event odds calls used before this league | 15.00 |
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

The model's most likely 1X2 outcome is **Arsenal win** at **74.1%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.4%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 49.3%; Under 3.5 goals: 73.1%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 39.6%; BTTS No (at least one team does not score): 60.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 74.1% | 1.35 |
| Draw | 16.8% | 5.94 |
| Lille win | 9.0% | 11.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.93 |
| Lille expected goals | 0.65 |
| Expected total goals | 2.58 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.37% |
| 2 | 2-0 | 15.29% |
| 3 | 2-1 | 10.00% |
| 4 | 3-0 | 9.83% |
| 5 | 1-1 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 74.1% | 80.1% | 1.29 | -4.4% |
| Draw | 16.8% | 14.1% | 7.00 | +17.8% |
| Lille win | 9.0% | 5.8% | 14.00 | +26.5% |
| Over 2.5 | 49.3% | 62.4% | 1.67 | -17.7% |
| Under 2.5 | 50.7% | 37.6% | 2.48 | +25.7% |

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
| Market best home last update utc | 2026-10-11T11:23:12Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
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
| P btts yes | 39.6% |
| P btts no | 60.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.45 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.78 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.93 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 72.5% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 40.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.21 |
| Reference draw odds | 5.40 |
| Reference away odds | 11.50 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -6.0% |
| Draw probability edge | +2.8% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -13.1% |
| Under 2.5 probability edge | +13.1% |
| Raw edge prob home | -0.1194 |
| Raw ev home | -0.1206 |
| Raw edge prob draw | 0.0554 |
| Raw ev draw | 0.3715 |
| Raw edge prob away | 0.0640 |
| Raw ev away | 0.7128 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **63.4%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.5%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.9%; Under 3.5 goals: 24.7%; Under 4.5 goals: 42.3%; BTTS Yes (both teams score): 78.7%; BTTS No (at least one team does not score): 21.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 63.4% | 1.58 |
| Draw | 17.3% | 5.79 |
| Manchester United win | 19.3% | 5.18 |

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
| Over 2.5 | 87.9% |
| Under 2.5 | 12.1% |
| Over 3.5 | 75.3% |
| Under 3.5 | 24.7% |
| Over 4.5 | 57.7% |
| Under 4.5 | 42.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.45% |
| 2 | 3-1 | 5.64% |
| 3 | 4-1 | 5.26% |
| 4 | 2-1 | 4.54% |
| 5 | 3-2 | 4.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 63.4% | 49.7% | 2.07 | +31.2% |
| Draw | 17.3% | 23.2% | 4.10 | -29.1% |
| Manchester United win | 19.3% | 27.1% | 3.80 | -26.6% |
| Over 2.5 | 87.9% | 65.5% | 1.50 | +31.9% |
| Under 2.5 | 12.1% | 34.5% | 2.68 | -67.6% |

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
| Market best home last update utc | 2026-10-11T11:23:12Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 78.7% |
| P btts no | 21.3% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 179.66 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.01 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.27 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.05 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 77.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 23.0% |
| Raw p btts yes | 76.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.68 |
| Home probability edge | +13.7% |
| Draw probability edge | -5.9% |
| Away probability edge | -7.8% |
| Over 2.5 probability edge | +22.4% |
| Under 2.5 probability edge | -22.4% |
| Raw edge prob home | 0.2737 |
| Raw ev home | 0.5957 |
| Raw edge prob draw | -0.1174 |
| Raw ev draw | -0.5321 |
| Raw edge prob away | -0.1563 |
| Raw ev away | -0.5630 |
| Market p over 1 5 | 85.9% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T11:26:24Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 57.3% |
| Market under 3 5 odds | 1.73 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T11:16:20Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.23 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 65.8% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:26:41Z |
| Market reference btts yes odds | 1.51 |
| Market reference btts yes opposite odds | 2.88 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **68.3%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 77.8%; Under 3.5 goals: 41.7%; Under 4.5 goals: 61.0%; BTTS Yes (both teams score): 70.8%; BTTS No (at least one team does not score): 29.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 16.0% | 6.23 |
| Draw | 15.7% | 6.39 |
| Barcelona win | 68.3% | 1.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.53 |
| Barcelona expected goals | 2.51 |
| Expected total goals | 4.04 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 77.8% |
| Under 2.5 | 22.2% |
| Over 3.5 | 58.3% |
| Under 3.5 | 41.7% |
| Over 4.5 | 39.0% |
| Under 4.5 | 61.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.77% |
| 2 | 1-3 | 8.17% |
| 3 | 0-2 | 6.36% |
| 4 | 2-3 | 6.27% |
| 5 | 2-2 | 5.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 16.0% | 9.2% | 10.00 | +60.4% |
| Draw | 15.7% | 13.4% | 7.40 | +15.8% |
| Barcelona win | 68.3% | 77.4% | 1.34 | -8.5% |
| Over 2.5 | 77.8% | 80.9% | 1.21 | -5.9% |
| Under 2.5 | 22.2% | 19.1% | 4.50 | +0.1% |

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
| Market best home last update utc | 2026-10-11T11:25:38Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:23:12Z |
| Odds bookmakers 1x2 | 21.00 |
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
| P btts yes | 70.8% |
| P btts no | 29.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 80.81 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.34 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.50 |
| Fair Over 3.5 odds | 1.72 |
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
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 8.00 |
| Reference draw odds | 5.75 |
| Reference away odds | 1.25 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.21 |
| Reference Under 2.5 odds | 4.45 |
| Home probability edge | +6.9% |
| Draw probability edge | +2.2% |
| Away probability edge | -9.1% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | 0.1371 |
| Raw ev home | 1.2898 |
| Raw edge prob draw | 0.0447 |
| Raw ev draw | 0.3237 |
| Raw edge prob away | -0.1818 |
| Raw ev away | -0.2065 |
| Market p over 1 5 | 98.2% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T11:26:24Z |
| Market reference over 1 5 odds | 1.01 |
| Market reference over 1 5 opposite odds | 8.60 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 37.2% |
| Market under 3 5 odds | 2.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T11:26:41Z |
| Market reference under 3 5 odds | 2.51 |
| Market reference under 3 5 opposite odds | 1.54 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 66.6% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:26:41Z |
| Market reference btts yes odds | 1.49 |
| Market reference btts yes opposite odds | 2.94 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **69.4%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 56.2%; Under 3.5 goals: 66.8%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 50.4%; BTTS No (at least one team does not score): 49.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 69.4% | 1.44 |
| Draw | 17.7% | 5.66 |
| Club Brugge win | 13.0% | 7.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.92 |
| Club Brugge expected goals | 0.94 |
| Expected total goals | 2.86 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 78.3% |
| Under 1.5 | 21.7% |
| Over 2.5 | 56.2% |
| Under 2.5 | 43.8% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.10% |
| 2 | 2-0 | 12.01% |
| 3 | 2-1 | 11.34% |
| 4 | 1-1 | 8.36% |
| 5 | 3-0 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 69.4% | 78.0% | 1.31 | -9.2% |
| Draw | 17.7% | 14.6% | 6.50 | +14.8% |
| Club Brugge win | 13.0% | 7.4% | 12.00 | +55.8% |
| Over 2.5 | 56.2% | 67.4% | 1.44 | -19.1% |
| Under 2.5 | 43.8% | 32.6% | 2.83 | +24.0% |

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
| Market best home last update utc | 2026-10-11T11:23:12Z |
| Market best draw last update utc | 2026-10-11T11:25:54Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.4% |
| P btts no | 49.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.64 |
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
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.24 |
| Reference draw odds | 5.30 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.82 |
| Home probability edge | -8.7% |
| Draw probability edge | +3.1% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | -0.1730 |
| Raw ev home | -0.2048 |
| Raw edge prob draw | 0.0619 |
| Raw ev draw | 0.3493 |
| Raw edge prob away | 0.1111 |
| Raw ev away | 1.2250 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **44.7%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 68.1%; Under 3.5 goals: 53.6%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 44.7% | 2.24 |
| Draw | 21.1% | 4.75 |
| PSV Eindhoven win | 34.2% | 2.92 |

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
| 1 | 2-1 | 9.65% |
| 2 | 1-1 | 8.64% |
| 3 | 2-2 | 7.00% |
| 4 | 1-0 | 6.86% |
| 5 | 1-2 | 6.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 44.7% | 54.5% | 1.90 | -15.0% |
| Draw | 21.1% | 20.9% | 4.80 | +1.1% |
| PSV Eindhoven win | 34.2% | 24.6% | 3.95 | +35.1% |
| Over 2.5 | 68.1% | 72.5% | 1.35 | -8.1% |
| Under 2.5 | 31.9% | 27.5% | 3.26 | +4.0% |

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
| Market best home last update utc | 2026-10-11T11:23:12Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
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
| P btts yes | 67.9% |
| P btts no | 32.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.99 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.12 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.14 |
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
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.73 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.55 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.25 |
| Home probability edge | -9.8% |
| Draw probability edge | +0.1% |
| Away probability edge | +9.6% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | -0.1951 |
| Raw ev home | -0.3354 |
| Raw edge prob draw | 0.0024 |
| Raw ev draw | 0.0169 |
| Raw edge prob away | 0.1927 |
| Raw ev away | 0.7316 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **40.2%**. Expected goals are 1.28 for RC Lens and 1.60 for Sporting Lisbon (2.89 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 54.6%; Under 3.5 goals: 67.4%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 57.6%; BTTS No (at least one team does not score): 42.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 35.1% | 2.85 |
| Draw | 24.7% | 4.05 |
| Sporting Lisbon win | 40.2% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.28 |
| Sporting Lisbon expected goals | 1.60 |
| Expected total goals | 2.89 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 54.6% |
| Under 2.5 | 45.4% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.52% |
| 2 | 1-0 | 8.70% |
| 3 | 0-1 | 8.41% |
| 4 | 2-1 | 8.29% |
| 5 | 1-2 | 8.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 35.1% | 39.1% | 2.62 | -8.0% |
| Draw | 24.7% | 26.0% | 3.91 | -3.5% |
| Sporting Lisbon win | 40.2% | 34.9% | 2.78 | +11.7% |
| Over 2.5 | 54.6% | 61.6% | 1.64 | -10.5% |
| Under 2.5 | 45.4% | 38.4% | 2.46 | +11.7% |

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
| Market best home last update utc | 2026-10-11T11:23:12Z |
| Market best draw last update utc | 2026-10-11T11:26:11Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Sporting Clube de Portugal |
| Home-name matching confidence | 86/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.6% |
| P btts no | 42.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.92 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.11 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.35 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.60 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | -3.9% |
| Draw probability edge | -1.3% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | -0.0784 |
| Raw ev home | -0.1822 |
| Raw edge prob draw | -0.0267 |
| Raw ev draw | -0.0874 |
| Raw edge prob away | 0.1051 |
| Raw ev away | 0.2634 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **54.9%**. Expected goals are 0.38 for Sabah FK and 1.28 for Slavia Praha (1.66 combined). The most likely exact score is 0-1 at 22.6%. Goal-market probabilities: at least one goal: 82.8%; Over 2.5 goals: 22.9%; Under 3.5 goals: 91.7%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 22.2%; BTTS No (at least one team does not score): 77.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 18.6% | 5.38 |
| Draw | 26.5% | 3.77 |
| Slavia Praha win | 54.9% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.38 |
| Slavia Praha expected goals | 1.28 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.8% |
| Under 0.5 | 17.2% |
| Over 1.5 | 47.6% |
| Under 1.5 | 52.4% |
| Over 2.5 | 22.9% |
| Under 2.5 | 77.1% |
| Over 3.5 | 8.3% |
| Under 3.5 | 91.7% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.64% |
| 2 | 0-0 | 17.25% |
| 3 | 0-2 | 14.23% |
| 4 | 1-0 | 12.51% |
| 5 | 1-1 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 18.6% | 25.8% | 3.74 | -30.5% |
| Draw | 26.5% | 24.6% | 4.00 | +6.1% |
| Slavia Praha win | 54.9% | 49.7% | 2.12 | +16.3% |
| Over 2.5 | 22.9% | 58.8% | 1.71 | -60.8% |
| Under 2.5 | 77.1% | 41.2% | 2.34 | +80.3% |

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
| Market best home last update utc | 2026-10-11T11:23:12Z |
| Market best draw last update utc | 2026-10-11T11:26:24Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Sabah FK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 22.2% |
| P btts no | 77.8% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.80 |
| Fair Over 1.5 odds | 2.10 |
| Fair Under 1.5 odds | 1.91 |
| Fair Over 2.5 odds | 4.36 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 12.03 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 38.16 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.4% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 60.1% |
| Raw p over 1 5 | 49.0% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 22.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 3.40 |
| Reference draw odds | 3.55 |
| Reference away odds | 1.88 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | -7.2% |
| Draw probability edge | +2.0% |
| Away probability edge | +5.2% |
| Over 2.5 probability edge | -35.9% |
| Under 2.5 probability edge | +35.9% |
| Raw edge prob home | -0.1434 |
| Raw ev home | -0.5729 |
| Raw edge prob draw | 0.0395 |
| Raw ev draw | 0.1404 |
| Raw edge prob away | 0.1039 |
| Raw ev away | 0.2735 |
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T11:26:24Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 64.5% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T11:26:41Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.64 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.0% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T11:26:41Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **92.8%**. Expected goals are 0.70 for Viking FK and 4.47 for Bayern Munich (5.17 combined). The most likely exact score is 0-4 at 9.4%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.4%; Under 3.5 goals: 24.8%; Under 4.5 goals: 41.9%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 2.4% | 42.15 |
| Draw | 4.8% | 20.83 |
| Bayern Munich win | 92.8% | 1.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.70 |
| Bayern Munich expected goals | 4.47 |
| Expected total goals | 5.17 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 88.4% |
| Under 2.5 | 11.6% |
| Over 3.5 | 75.2% |
| Under 3.5 | 24.8% |
| Over 4.5 | 58.1% |
| Under 4.5 | 41.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.44% |
| 2 | 0-3 | 8.45% |
| 3 | 0-5 | 8.44% |
| 4 | 1-4 | 6.58% |
| 5 | 0-6 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 2.4% | 2.8% | 27.00 | -35.9% |
| Draw | 4.8% | 5.4% | 15.50 | -25.6% |
| Bayern Munich win | 92.8% | 91.8% | 1.11 | +3.0% |
| Over 2.5 | 88.4% | 86.8% | 1.15 | +1.7% |
| Under 2.5 | 11.6% | 13.2% | 5.90 | -31.7% |

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
| Market best home last update utc | 2026-10-11T11:26:25Z |
| Market best draw last update utc | 2026-10-11T11:23:12Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
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
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 179.01 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.47 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.64 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.04 |
| Fair Over 4.5 odds | 1.72 |
| Fair Under 4.5 odds | 2.39 |
| Unadjusted home-win probability | 2.0% |
| Unadjusted draw probability | 4.2% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.4% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 17.00 |
| Reference draw odds | 10.00 |
| Reference away odds | 1.07 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.13 |
| Reference Under 2.5 odds | 5.80 |
| Home probability edge | -0.4% |
| Draw probability edge | -0.6% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | -0.0080 |
| Raw ev home | -0.4679 |
| Raw edge prob draw | -0.0126 |
| Raw ev draw | -0.3536 |
| Raw edge prob away | 0.0206 |
| Raw ev away | 0.0418 |
| Market p over 1 5 | 95.7% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-11T11:25:43Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 8.40 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 31.7% |
| Market under 3 5 odds | 2.93 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T11:26:24Z |
| Market reference under 3 5 odds | 2.70 |
| Market reference under 3 5 opposite odds | 1.39 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 55.2% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-11T11:26:03Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **39.5%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 40.1%; Under 3.5 goals: 80.3%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 44.6%; BTTS No (at least one team does not score): 55.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 34.1% | 2.93 |
| Draw | 26.3% | 3.80 |
| Napoli win | 39.5% | 2.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.90 |
| Napoli expected goals | 1.42 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 65.7% |
| Under 1.5 | 34.3% |
| Over 2.5 | 40.1% |
| Under 2.5 | 59.9% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.24% |
| 2 | 1-1 | 12.19% |
| 3 | 0-1 | 11.63% |
| 4 | 0-0 | 9.45% |
| 5 | 0-2 | 7.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 34.1% | 43.8% | 2.33 | -20.5% |
| Draw | 26.3% | 26.9% | 3.90 | +2.8% |
| Napoli win | 39.5% | 29.3% | 3.35 | +32.5% |
| Over 2.5 | 40.1% | 58.6% | 1.71 | -31.5% |
| Under 2.5 | 59.9% | 41.4% | 2.46 | +47.5% |

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
| Market best home last update utc | 2026-10-11T11:26:11Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.6% |
| P btts no | 55.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.58 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.07 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.12 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 44.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.12 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | -9.7% |
| Draw probability edge | -0.6% |
| Away probability edge | +10.2% |
| Over 2.5 probability edge | -18.5% |
| Under 2.5 probability edge | +18.5% |
| Raw edge prob home | -0.1931 |
| Raw ev home | -0.4303 |
| Raw edge prob draw | -0.0111 |
| Raw ev draw | 0.0060 |
| Raw edge prob away | 0.2042 |
| Raw ev away | 0.6668 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **50.8%**. Expected goals are 1.18 for AS Roma and 1.67 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.5%; Under 3.5 goals: 67.9%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.3% | 3.81 |
| Draw | 22.9% | 4.36 |
| Real Madrid win | 50.8% | 1.97 |

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
| Over 2.5 | 54.5% |
| Under 2.5 | 45.5% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.76% |
| 2 | 0-1 | 10.48% |
| 3 | 1-2 | 9.79% |
| 4 | 0-2 | 8.29% |
| 5 | 1-0 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.3% | 25.0% | 4.10 | +7.6% |
| Draw | 22.9% | 22.8% | 4.30 | -1.4% |
| Real Madrid win | 50.8% | 52.2% | 1.95 | -0.9% |
| Over 2.5 | 54.5% | 68.7% | 1.42 | -22.7% |
| Under 2.5 | 45.5% | 31.3% | 2.91 | +32.5% |

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
| Market best home last update utc | 2026-10-11T11:26:25Z |
| Market best draw last update utc | 2026-10-11T11:26:24Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.37 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.19 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 27.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 49.5% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.0% |
| Raw p btts yes | 55.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +1.3% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -14.3% |
| Under 2.5 probability edge | +14.3% |
| Raw edge prob home | 0.0251 |
| Raw ev home | 0.1279 |
| Raw edge prob draw | 0.0020 |
| Raw ev draw | -0.0102 |
| Raw edge prob away | -0.0271 |
| Raw ev away | -0.0353 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **66.8%**. Expected goals are 2.23 for Aston Villa and 0.61 for Fenerbahce (2.84 combined). The most likely exact score is 2-0 at 13.0%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 51.8%; Under 3.5 goals: 69.9%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 41.5%; BTTS No (at least one team does not score): 58.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 66.8% | 1.50 |
| Draw | 19.0% | 5.26 |
| Fenerbahce win | 14.2% | 7.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.23 |
| Fenerbahce expected goals | 0.61 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 51.8% |
| Under 2.5 | 48.2% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.98% |
| 2 | 1-0 | 11.99% |
| 3 | 3-0 | 9.66% |
| 4 | 1-1 | 8.88% |
| 5 | 2-1 | 7.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 66.8% | 58.8% | 1.74 | +16.3% |
| Draw | 19.0% | 21.9% | 4.35 | -17.4% |
| Fenerbahce win | 14.2% | 19.4% | 5.40 | -23.5% |
| Over 2.5 | 51.8% | 60.7% | 1.74 | -9.9% |
| Under 2.5 | 48.2% | 39.3% | 2.32 | +11.8% |

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
| Market best home last update utc | 2026-10-11T11:23:12Z |
| Market best draw last update utc | 2026-10-11T11:25:39Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 41.5% |
| P btts no | 58.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.57 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.32 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.74 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.1% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 40.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.61 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.35 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | +8.1% |
| Draw probability edge | -2.9% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | 0.1615 |
| Raw ev home | 0.3034 |
| Raw edge prob draw | -0.0577 |
| Raw ev draw | -0.2992 |
| Raw edge prob away | -0.1038 |
| Raw ev away | -0.5150 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **45.8%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-2 at 8.7%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.0%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 70.2%; BTTS No (at least one team does not score): 29.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 32.5% | 3.08 |
| Draw | 21.7% | 4.61 |
| Borussia Dortmund win | 45.8% | 2.18 |

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
| 1 | 1-2 | 8.68% |
| 2 | 1-1 | 8.51% |
| 3 | 2-2 | 7.51% |
| 4 | 2-1 | 6.78% |
| 5 | 0-1 | 5.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 32.5% | 29.5% | 3.30 | +7.2% |
| Draw | 21.7% | 22.7% | 4.30 | -6.7% |
| Borussia Dortmund win | 45.8% | 47.9% | 2.14 | -2.0% |
| Over 2.5 | 70.7% | 69.8% | 1.40 | -1.0% |
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
| Market best home last update utc | 2026-10-11T11:26:25Z |
| Market best draw last update utc | 2026-10-11T11:26:24Z |
| Market best away last update utc | 2026-10-11T11:23:12Z |
| Odds bookmakers 1x2 | 21.00 |
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
| P btts yes | 70.2% |
| P btts no | 29.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.95 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
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
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.94 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +3.0% |
| Draw probability edge | -1.0% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.0602 |
| Raw ev home | 0.1715 |
| Raw edge prob draw | -0.0191 |
| Raw ev draw | -0.1078 |
| Raw edge prob away | -0.0411 |
| Raw ev away | -0.0637 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **63.1%**. Expected goals are 1.82 for Feyenoord and 3.81 for Como (5.63 combined). The most likely exact score is 2-2 at 6.1%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.9%; Under 3.5 goals: 19.6%; Under 4.5 goals: 35.8%; BTTS Yes (both teams score): 83.2%; BTTS No (at least one team does not score): 16.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 19.6% | 5.11 |
| Draw | 17.3% | 5.77 |
| Como win | 63.1% | 1.59 |

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
| Over 2.5 | 90.9% |
| Under 2.5 | 9.1% |
| Over 3.5 | 80.4% |
| Under 3.5 | 19.6% |
| Over 4.5 | 64.2% |
| Under 4.5 | 35.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.15% |
| 2 | 1-3 | 5.17% |
| 3 | 1-4 | 4.93% |
| 4 | 3-3 | 4.74% |
| 5 | 2-3 | 4.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 19.6% | 25.0% | 3.85 | -24.6% |
| Draw | 17.3% | 22.5% | 4.40 | -23.7% |
| Como win | 63.1% | 52.5% | 1.98 | +24.9% |
| Over 2.5 | 90.9% | 67.9% | 1.43 | +30.0% |
| Under 2.5 | 9.1% | 32.1% | 2.86 | -74.0% |

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
| Market best home last update utc | 2026-10-11T11:26:25Z |
| Market best draw last update utc | 2026-10-11T11:26:08Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 83.2% |
| P btts no | 16.8% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 299.47 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 37.23 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.98 |
| Fair Over 3.5 odds | 1.24 |
| Fair Under 3.5 odds | 5.09 |
| Fair Over 4.5 odds | 1.56 |
| Fair Under 4.5 odds | 2.80 |
| Unadjusted home-win probability | 14.2% |
| Unadjusted draw probability | 12.2% |
| Unadjusted away-win probability | 73.7% |
| Raw p over 1 5 | 97.5% |
| Raw p under 3 5 | 18.8% |
| Raw p btts yes | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.85 |
| Reference away odds | 1.79 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.85 |
| Home probability edge | -5.4% |
| Draw probability edge | -5.2% |
| Away probability edge | +10.6% |
| Over 2.5 probability edge | +23.0% |
| Under 2.5 probability edge | -23.0% |
| Raw edge prob home | -0.1083 |
| Raw ev home | -0.4545 |
| Raw edge prob draw | -0.1033 |
| Raw ev draw | -0.4648 |
| Raw edge prob away | 0.2116 |
| Raw ev away | 0.4586 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **73.6%**. Expected goals are 0.28 for LASK and 1.45 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 28.2%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 27.1%; Under 3.5 goals: 89.5%; Under 4.5 goals: 96.5%; BTTS Yes (both teams score): 17.5%; BTTS No (at least one team does not score): 82.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 7.4% | 13.60 |
| Draw | 19.0% | 5.26 |
| Liverpool win | 73.6% | 1.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.45 |
| Expected total goals | 1.74 |
| Over 0.5 | 86.8% |
| Under 0.5 | 13.2% |
| Over 1.5 | 53.2% |
| Under 1.5 | 46.8% |
| Over 2.5 | 27.1% |
| Under 2.5 | 72.9% |
| Over 3.5 | 10.5% |
| Under 3.5 | 89.5% |
| Over 4.5 | 3.5% |
| Under 4.5 | 96.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 28.22% |
| 2 | 0-2 | 20.24% |
| 3 | 0-0 | 13.17% |
| 4 | 0-3 | 9.81% |
| 5 | 1-2 | 5.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 7.4% | 7.4% | 12.00 | -11.8% |
| Draw | 19.0% | 13.1% | 7.11 | +35.1% |
| Liverpool win | 73.6% | 79.5% | 1.29 | -5.0% |
| Over 2.5 | 27.1% | 70.9% | 1.37 | -62.9% |
| Under 2.5 | 72.9% | 29.1% | 3.13 | +128.3% |

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
| Market best home last update utc | 2026-10-11T11:26:25Z |
| Market best draw last update utc | 2026-10-11T11:26:11Z |
| Market best away last update utc | 2026-10-11T11:23:12Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 17.5% |
| P btts no | 82.5% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.59 |
| Fair Over 1.5 odds | 1.88 |
| Fair Under 1.5 odds | 2.14 |
| Fair Over 2.5 odds | 3.70 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.57 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 28.94 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 67.8% |
| Raw p over 1 5 | 51.4% |
| Raw p under 3 5 | 90.1% |
| Raw p btts yes | 18.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 9.50 |
| Reference draw odds | 5.80 |
| Reference away odds | 1.22 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -0.1% |
| Draw probability edge | +5.9% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -43.9% |
| Under 2.5 probability edge | +43.9% |
| Raw edge prob home | -0.0013 |
| Raw ev home | -0.1254 |
| Raw edge prob draw | 0.1177 |
| Raw ev draw | 0.7694 |
| Raw edge prob away | -0.1164 |
| Raw ev away | -0.1251 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **45.1%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.8%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 69.2%; Under 3.5 goals: 51.8%; Under 4.5 goals: 71.0%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 33.4% | 3.00 |
| Draw | 21.5% | 4.65 |
| Paris Saint Germain win | 45.1% | 2.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.40 |
| Paris Saint Germain expected goals | 2.23 |
| Expected total goals | 3.63 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 86.8% |
| Under 1.5 | 13.2% |
| Over 2.5 | 69.2% |
| Under 2.5 | 30.8% |
| Over 3.5 | 48.2% |
| Under 3.5 | 51.8% |
| Over 4.5 | 29.0% |
| Under 4.5 | 71.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.76% |
| 2 | 2-1 | 8.05% |
| 3 | 1-2 | 7.34% |
| 4 | 2-2 | 7.21% |
| 5 | 1-0 | 5.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 33.4% | 42.7% | 2.35 | -21.6% |
| Draw | 21.5% | 23.7% | 4.30 | -7.5% |
| Paris Saint Germain win | 45.1% | 33.6% | 2.94 | +32.7% |
| Over 2.5 | 69.2% | 67.9% | 1.44 | -0.4% |
| Under 2.5 | 30.8% | 32.1% | 2.87 | -11.5% |

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
| Market best home last update utc | 2026-10-11T11:26:24Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:23:12Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.9% |
| P btts no | 32.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.20 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.56 |
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
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.17 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.85 |
| Home probability edge | -9.3% |
| Draw probability edge | -2.2% |
| Away probability edge | +11.6% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | -0.1866 |
| Raw ev home | -0.4355 |
| Raw edge prob draw | -0.0445 |
| Raw ev draw | -0.1702 |
| Raw edge prob away | 0.2311 |
| Raw ev away | 0.6664 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **60.4%**. Expected goals are 3.29 for Real Betis and 1.29 for Porto (4.58 combined). The most likely exact score is 2-2 at 7.1%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 80.9%; Under 3.5 goals: 35.3%; Under 4.5 goals: 55.0%; BTTS Yes (both teams score): 72.4%; BTTS No (at least one team does not score): 27.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 60.4% | 1.66 |
| Draw | 19.2% | 5.20 |
| Porto win | 20.4% | 4.91 |

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
| Over 3.5 | 64.7% |
| Under 3.5 | 35.3% |
| Over 4.5 | 45.0% |
| Under 4.5 | 55.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.15% |
| 2 | 1-1 | 6.39% |
| 3 | 3-1 | 6.23% |
| 4 | 2-1 | 5.68% |
| 5 | 4-1 | 5.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 60.4% | 44.7% | 2.27 | +37.1% |
| Draw | 19.2% | 26.0% | 3.75 | -27.9% |
| Porto win | 20.4% | 29.3% | 3.35 | -31.7% |
| Over 2.5 | 80.9% | 56.9% | 1.78 | +43.9% |
| Under 2.5 | 19.1% | 43.1% | 2.21 | -57.7% |

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
| Market best home last update utc | 2026-10-11T11:23:12Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 72.4% |
| P btts no | 27.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 80.24 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.64 |
| Fair Over 2.5 odds | 1.24 |
| Fair Under 2.5 odds | 5.22 |
| Fair Over 3.5 odds | 1.55 |
| Fair Under 3.5 odds | 2.83 |
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
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.08 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.02 |
| Home probability edge | +15.7% |
| Draw probability edge | -6.8% |
| Away probability edge | -8.9% |
| Over 2.5 probability edge | +23.9% |
| Under 2.5 probability edge | -23.9% |
| Raw edge prob home | 0.3144 |
| Raw ev home | 0.7278 |
| Raw edge prob draw | -0.1358 |
| Raw ev draw | -0.5336 |
| Raw edge prob away | -0.1787 |
| Raw ev away | -0.6165 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.1%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 51.1%; Under 3.5 goals: 70.6%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.1% | 2.56 |
| Draw | 25.5% | 3.92 |
| AEK Athens win | 35.4% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.49 |
| AEK Athens expected goals | 1.25 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.07% |
| 2 | 0-1 | 9.44% |
| 3 | 1-0 | 9.23% |
| 4 | 1-2 | 8.19% |
| 5 | 2-1 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.1% | 34.9% | 2.81 | +9.9% |
| Draw | 25.5% | 26.9% | 3.65 | -6.8% |
| AEK Athens win | 35.4% | 38.2% | 2.69 | -4.9% |
| Over 2.5 | 51.1% | 52.9% | 1.92 | -1.8% |
| Under 2.5 | 48.9% | 47.1% | 2.03 | -0.8% |

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
| Market best home last update utc | 2026-10-11T11:23:12Z |
| Market best draw last update utc | 2026-10-11T11:26:25Z |
| Market best away last update utc | 2026-10-11T11:26:11Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 67/100 |
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.17 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.02 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.41 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.09 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 54.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 1.87 |
| Home probability edge | +4.1% |
| Draw probability edge | -1.3% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | 0.0829 |
| Raw ev home | 0.2150 |
| Raw edge prob draw | -0.0269 |
| Raw ev draw | -0.1168 |
| Raw edge prob away | -0.0560 |
| Raw ev away | -0.1240 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.3%**. Expected goals are 1.46 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 72.7%; Under 3.5 goals: 48.5%; Under 4.5 goals: 67.6%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.0% | 5.88 |
| Draw | 16.7% | 5.99 |
| VfB Stuttgart win | 66.3% | 1.51 |

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
| Over 2.5 | 72.7% |
| Under 2.5 | 27.3% |
| Over 3.5 | 51.5% |
| Under 3.5 | 48.5% |
| Over 4.5 | 32.4% |
| Under 4.5 | 67.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.74% |
| 2 | 1-3 | 8.06% |
| 3 | 0-2 | 7.38% |
| 4 | 0-1 | 7.04% |
| 5 | 1-1 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.0% | 9.2% | 10.00 | +70.0% |
| Draw | 16.7% | 14.1% | 6.48 | +8.1% |
| VfB Stuttgart win | 66.3% | 76.7% | 1.35 | -10.5% |
| Over 2.5 | 72.7% | 70.9% | 1.37 | -0.4% |
| Under 2.5 | 27.3% | 29.1% | 3.13 | -14.4% |

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
| Market best home last update utc | 2026-10-11T11:23:12Z |
| Market best draw last update utc | 2026-10-11T11:23:12Z |
| Market best away last update utc | 2026-10-11T11:26:25Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.2% |
| P btts no | 32.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 56.13 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.66 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.66 |
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
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 8.00 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.26 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | +7.8% |
| Draw probability edge | +2.6% |
| Away probability edge | -10.4% |
| Over 2.5 probability edge | +1.7% |
| Under 2.5 probability edge | -1.7% |
| Raw edge prob home | 0.1563 |
| Raw ev home | 1.4815 |
| Raw edge prob draw | 0.0513 |
| Raw ev draw | 0.2477 |
| Raw edge prob away | -0.2076 |
| Raw ev away | -0.2449 |

</details>


---
