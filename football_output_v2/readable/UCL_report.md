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
| Additional event odds calls used before this league | 0.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-13 — Arsenal vs Lille

The model's most likely 1X2 outcome is **Arsenal win** at **74.6%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.5%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 49.4%; Under 3.5 goals: 73.0%; Double Chance 1X: 91.2%; Double Chance X2: 25.4%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 39.5%; BTTS No (at least one team does not score): 60.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 74.6% | 1.34 |
| Draw | 16.6% | 6.01 |
| Lille win | 8.8% | 11.37 |

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
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.46% |
| 2 | 2-0 | 15.37% |
| 3 | 2-1 | 10.05% |
| 4 | 3-0 | 9.89% |
| 5 | 1-1 | 7.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 74.6% | 80.9% | 1.28 | -4.6% |
| Draw | 16.6% | 13.7% | 7.00 | +16.5% |
| Lille win | 8.8% | 5.4% | 16.50 | +45.1% |
| Over 2.5 | 49.4% | 61.6% | 1.64 | -19.0% |
| Under 2.5 | 50.6% | 38.4% | 2.46 | +24.5% |

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
| Market best home last update utc | 2026-10-12T21:07:53Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 39.5% |
| P btts no | 60.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.63 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.71 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.90 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 72.5% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 40.6% |
| P home draw | 91.2% |
| P draw away | 25.4% |
| Raw p home draw | 87.8% |
| Raw p draw away | 31.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.21 |
| Reference draw odds | 6.00 |
| Reference away odds | 14.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.44 |
| Home probability edge | -6.4% |
| Draw probability edge | +2.9% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -12.2% |
| Under 2.5 probability edge | +12.2% |
| Raw edge prob home | -0.1277 |
| Raw ev home | -0.1274 |
| Raw edge prob draw | 0.0589 |
| Raw ev draw | 0.3715 |
| Raw edge prob away | 0.0688 |
| Raw ev away | 1.0186 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **64.7%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.5%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.0%; Under 3.5 goals: 24.5%; Double Chance 1X: 82.0%; Double Chance X2: 35.3%; Under 4.5 goals: 42.2%; BTTS Yes (both teams score): 78.6%; BTTS No (at least one team does not score): 21.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 64.7% | 1.55 |
| Draw | 17.3% | 5.78 |
| Manchester United win | 18.0% | 5.55 |

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
| Over 2.5 | 88.0% |
| Under 2.5 | 12.0% |
| Over 3.5 | 75.5% |
| Under 3.5 | 24.5% |
| Over 4.5 | 57.8% |
| Under 4.5 | 42.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.46% |
| 2 | 3-1 | 5.76% |
| 3 | 4-1 | 5.36% |
| 4 | 2-1 | 4.63% |
| 5 | 3-2 | 4.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 64.7% | 52.3% | 2.00 | +29.4% |
| Draw | 17.3% | 23.2% | 4.11 | -28.9% |
| Manchester United win | 18.0% | 24.5% | 4.00 | -27.9% |
| Over 2.5 | 88.0% | 64.2% | 1.51 | +32.9% |
| Under 2.5 | 12.0% | 35.8% | 2.60 | -68.8% |

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
| Market best home last update utc | 2026-10-12T21:07:37Z |
| Market best draw last update utc | 2026-10-12T21:07:37Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
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
| P btts yes | 78.6% |
| P btts no | 21.4% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 179.44 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.50 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.33 |
| Fair Over 3.5 odds | 1.32 |
| Fair Under 3.5 odds | 4.09 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.37 |
| Unadjusted home-win probability | 77.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 23.0% |
| Raw p btts yes | 76.6% |
| P home draw | 82.0% |
| P draw away | 35.3% |
| Raw p home draw | 88.5% |
| Raw p draw away | 22.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.83 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.60 |
| Home probability edge | +12.4% |
| Draw probability edge | -5.9% |
| Away probability edge | -6.5% |
| Over 2.5 probability edge | +23.8% |
| Under 2.5 probability edge | -23.8% |
| Raw edge prob home | 0.2482 |
| Raw ev home | 0.5418 |
| Raw edge prob draw | -0.1178 |
| Raw ev draw | -0.5309 |
| Raw edge prob away | -0.1304 |
| Raw ev away | -0.5400 |
| Market p home draw | 74.3% |
| Market home draw odds | 1.32 |
| Best home draw bookmaker | Marathon Bet |
| Market best home draw last update utc | 2026-10-12T21:08:26Z |
| Market reference home draw last update utc | 2026-10-12T21:08:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.6% |
| Market draw away odds | 1.95 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-12T21:08:42Z |
| Market reference draw away last update utc | 2026-10-12T21:08:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.30 |
| Market reference dc draw away odds | 1.95 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-12T21:08:52Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 58.4% |
| Market under 3 5 odds | 1.74 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-12T21:06:54Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 64.3% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-12T21:08:54Z |
| Market reference btts yes odds | 1.54 |
| Market reference btts yes opposite odds | 2.74 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **68.7%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 77.8%; Under 3.5 goals: 41.7%; Double Chance 1X: 31.3%; Double Chance X2: 84.3%; Under 4.5 goals: 61.0%; BTTS Yes (both teams score): 70.8%; BTTS No (at least one team does not score): 29.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 15.7% | 6.39 |
| Draw | 15.6% | 6.41 |
| Barcelona win | 68.7% | 1.45 |

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
| 1 | 1-2 | 9.83% |
| 2 | 1-3 | 8.22% |
| 3 | 0-2 | 6.40% |
| 4 | 2-3 | 6.31% |
| 5 | 2-2 | 5.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 15.7% | 8.4% | 10.50 | +64.4% |
| Draw | 15.6% | 13.3% | 7.40 | +15.5% |
| Barcelona win | 68.7% | 78.2% | 1.33 | -8.6% |
| Over 2.5 | 77.8% | 81.7% | 1.20 | -6.6% |
| Under 2.5 | 22.2% | 18.3% | 4.61 | +2.4% |

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
| Market best home last update utc | 2026-10-12T21:08:21Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:07:53Z |
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
| P btts yes | 70.8% |
| P btts no | 29.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 81.02 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.37 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.50 |
| Fair Over 3.5 odds | 1.71 |
| Fair Under 3.5 odds | 2.40 |
| Fair Over 4.5 odds | 2.56 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.5% |
| Raw p btts yes | 71.7% |
| P home draw | 31.3% |
| P draw away | 84.3% |
| Raw p home draw | 40.8% |
| Raw p draw away | 77.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 9.50 |
| Reference draw odds | 6.25 |
| Reference away odds | 1.25 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.61 |
| Home probability edge | +7.2% |
| Draw probability edge | +2.3% |
| Away probability edge | -9.5% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | 0.1448 |
| Raw ev home | 1.4043 |
| Raw edge prob draw | 0.0455 |
| Raw ev draw | 0.3237 |
| Raw edge prob away | -0.1903 |
| Raw ev away | -0.2125 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **69.8%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 56.3%; Under 3.5 goals: 66.8%; Double Chance 1X: 87.2%; Double Chance X2: 30.2%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 69.8% | 1.43 |
| Draw | 17.3% | 5.77 |
| Club Brugge win | 12.8% | 7.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.92 |
| Club Brugge expected goals | 0.94 |
| Expected total goals | 2.86 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 56.3% |
| Under 2.5 | 43.7% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.19% |
| 2 | 2-0 | 12.09% |
| 3 | 2-1 | 11.41% |
| 4 | 1-1 | 8.21% |
| 5 | 3-0 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 69.8% | 78.9% | 1.31 | -8.5% |
| Draw | 17.3% | 13.9% | 6.80 | +17.9% |
| Club Brugge win | 12.8% | 7.1% | 12.50 | +60.6% |
| Over 2.5 | 56.3% | 69.0% | 1.41 | -20.6% |
| Under 2.5 | 43.7% | 31.0% | 2.95 | +28.8% |

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
| Market best home last update utc | 2026-10-12T21:07:53Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.07 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.63 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.84 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 51.6% |
| P home draw | 87.2% |
| P draw away | 30.2% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.24 |
| Reference draw odds | 6.00 |
| Reference away odds | 11.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | -9.1% |
| Draw probability edge | +3.4% |
| Away probability edge | +5.7% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | -0.1822 |
| Raw ev home | -0.2048 |
| Raw edge prob draw | 0.0683 |
| Raw ev draw | 0.4115 |
| Raw edge prob away | 0.1139 |
| Raw ev away | 1.3177 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **45.6%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 68.1%; Under 3.5 goals: 53.6%; Double Chance 1X: 66.7%; Double Chance X2: 54.4%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 45.6% | 2.19 |
| Draw | 21.1% | 4.74 |
| PSV Eindhoven win | 33.3% | 3.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.65 |
| PSV Eindhoven expected goals | 1.87 |
| Expected total goals | 3.52 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 85.9% |
| Under 1.5 | 14.1% |
| Over 2.5 | 68.1% |
| Under 2.5 | 31.9% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.85% |
| 2 | 1-1 | 8.65% |
| 3 | 2-2 | 7.01% |
| 4 | 1-0 | 7.00% |
| 5 | 1-2 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 45.6% | 56.3% | 1.81 | -17.4% |
| Draw | 21.1% | 21.0% | 4.90 | +3.3% |
| PSV Eindhoven win | 33.3% | 22.7% | 4.25 | +41.4% |
| Over 2.5 | 68.1% | 73.3% | 1.33 | -9.4% |
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
| Market best home last update utc | 2026-10-12T21:07:37Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:22Z |
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
| Fair Under 0.5 odds | 39.94 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.11 |
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
| P home draw | 66.7% |
| P draw away | 54.4% |
| Raw p home draw | 56.2% |
| Raw p draw away | 65.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.71 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Home probability edge | -10.7% |
| Draw probability edge | +0.1% |
| Away probability edge | +10.6% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.2134 |
| Raw ev home | -0.3669 |
| Raw edge prob draw | 0.0019 |
| Raw ev draw | 0.0380 |
| Raw edge prob away | 0.2115 |
| Raw ev away | 0.8631 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **41.6%**. Expected goals are 1.28 for RC Lens and 1.60 for Sporting Lisbon (2.89 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.7%; Under 3.5 goals: 67.4%; Double Chance 1X: 58.4%; Double Chance X2: 65.9%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 34.1% | 2.93 |
| Draw | 24.3% | 4.12 |
| Sporting Lisbon win | 41.6% | 2.40 |

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
| 1 | 1-1 | 11.35% |
| 2 | 0-1 | 8.71% |
| 3 | 1-0 | 8.44% |
| 4 | 1-2 | 8.42% |
| 5 | 2-1 | 8.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 34.1% | 37.0% | 2.64 | -10.0% |
| Draw | 24.3% | 25.3% | 3.90 | -5.2% |
| Sporting Lisbon win | 41.6% | 37.8% | 2.70 | +12.3% |
| Over 2.5 | 54.7% | 62.0% | 1.64 | -10.2% |
| Under 2.5 | 45.3% | 38.0% | 2.46 | +11.4% |

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
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Sporting Clube de Portugal |
| Home-name matching confidence | 86/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.21 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.09 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.2% |
| P home draw | 58.4% |
| P draw away | 65.9% |
| Raw p home draw | 54.6% |
| Raw p draw away | 68.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.55 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.43 |
| Home probability edge | -2.9% |
| Draw probability edge | -1.0% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.0576 |
| Raw ev home | -0.1760 |
| Raw edge prob draw | -0.0192 |
| Raw ev draw | -0.0897 |
| Raw edge prob away | 0.0768 |
| Raw ev away | 0.2270 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **53.9%**. Expected goals are 0.38 for Sabah FK and 1.28 for Slavia Praha (1.66 combined). The most likely exact score is 0-1 at 22.2%. Goal-market probabilities: at least one goal: 82.6%; Over 2.5 goals: 22.8%; Under 3.5 goals: 91.8%; Double Chance 1X: 46.1%; Double Chance X2: 80.7%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 22.2%; BTTS No (at least one team does not score): 77.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 19.3% | 5.19 |
| Draw | 26.8% | 3.73 |
| Slavia Praha win | 53.9% | 1.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.38 |
| Slavia Praha expected goals | 1.28 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.6% |
| Under 0.5 | 17.4% |
| Over 1.5 | 47.4% |
| Under 1.5 | 52.6% |
| Over 2.5 | 22.8% |
| Under 2.5 | 77.2% |
| Over 3.5 | 8.2% |
| Under 3.5 | 91.8% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.25% |
| 2 | 0-0 | 17.44% |
| 3 | 0-2 | 13.98% |
| 4 | 1-0 | 12.97% |
| 5 | 1-1 | 8.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 19.3% | 27.1% | 3.74 | -27.9% |
| Draw | 26.8% | 25.1% | 3.86 | +3.5% |
| Slavia Praha win | 53.9% | 47.7% | 2.12 | +14.3% |
| Over 2.5 | 22.8% | 58.5% | 1.71 | -61.0% |
| Under 2.5 | 77.2% | 41.5% | 2.32 | +79.1% |

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
| Market best home last update utc | 2026-10-12T21:07:37Z |
| Market best draw last update utc | 2026-10-12T21:07:37Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 22.2% |
| P btts no | 77.8% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.74 |
| Fair Over 1.5 odds | 2.11 |
| Fair Under 1.5 odds | 1.90 |
| Fair Over 2.5 odds | 4.39 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 12.14 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 38.57 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.4% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 60.1% |
| Raw p over 1 5 | 49.0% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 22.4% |
| P home draw | 46.1% |
| P draw away | 80.7% |
| Raw p home draw | 39.9% |
| Raw p draw away | 88.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.40 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -7.8% |
| Draw probability edge | +1.7% |
| Away probability edge | +6.2% |
| Over 2.5 probability edge | -35.7% |
| Under 2.5 probability edge | +35.7% |
| Raw edge prob home | -0.1569 |
| Raw ev home | -0.5729 |
| Raw edge prob draw | 0.0337 |
| Raw ev draw | 0.1004 |
| Raw edge prob away | 0.1232 |
| Raw ev away | 0.2735 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **92.7%**. Expected goals are 0.70 for Viking FK and 4.47 for Bayern Munich (5.17 combined). The most likely exact score is 0-4 at 9.4%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.4%; Under 3.5 goals: 24.8%; Double Chance 1X: 7.3%; Double Chance X2: 97.5%; Under 4.5 goals: 42.0%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 2.5% | 40.81 |
| Draw | 4.9% | 20.46 |
| Bayern Munich win | 92.7% | 1.08 |

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
| Over 4.5 | 58.0% |
| Under 4.5 | 42.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.42% |
| 2 | 0-3 | 8.44% |
| 3 | 0-5 | 8.42% |
| 4 | 1-4 | 6.57% |
| 5 | 0-6 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 2.5% | 2.9% | 26.00 | -36.3% |
| Draw | 4.9% | 5.6% | 15.50 | -24.2% |
| Bayern Munich win | 92.7% | 91.5% | 1.12 | +3.8% |
| Over 2.5 | 88.4% | 86.3% | 1.15 | +1.6% |
| Under 2.5 | 11.6% | 13.7% | 5.90 | -31.4% |

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
| Market best home last update utc | 2026-10-12T21:08:51Z |
| Market best draw last update utc | 2026-10-12T21:07:37Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
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
| Fair Under 0.5 odds | 175.77 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.30 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.59 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.03 |
| Fair Over 4.5 odds | 1.72 |
| Fair Under 4.5 odds | 2.38 |
| Unadjusted home-win probability | 2.0% |
| Unadjusted draw probability | 4.2% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.4% |
| Raw p btts yes | 49.5% |
| P home draw | 7.3% |
| P draw away | 97.5% |
| Raw p home draw | 6.1% |
| Raw p draw away | 98.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 21.00 |
| Reference draw odds | 12.00 |
| Reference away odds | 1.08 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.90 |
| Home probability edge | -0.5% |
| Draw probability edge | -0.7% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | -0.0096 |
| Raw ev home | -0.4876 |
| Raw edge prob draw | -0.0144 |
| Raw ev draw | -0.3536 |
| Raw edge prob away | 0.0240 |
| Raw ev away | 0.0512 |
| Market p home draw | 12.1% |
| Market home draw odds | 8.70 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-12T21:07:37Z |
| Market reference home draw last update utc | 2026-10-12T21:08:22Z |
| Market home draw bookmakers | 3 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 94.9% |
| Market draw away odds | 1.03 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-12T21:08:21Z |
| Market reference draw away last update utc | 2026-10-12T21:08:22Z |
| Market draw away bookmakers | 3 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 8.00 |
| Market reference dc draw away odds | 1.02 |
| Market reference dc home away odds | 1.04 |
| Market p over 1 5 | 95.5% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-12T21:08:52Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 14.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 31.9% |
| Market under 3 5 odds | 2.95 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-12T21:08:52Z |
| Market reference under 3 5 odds | 2.95 |
| Market reference under 3 5 opposite odds | 1.44 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 56.5% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-12T21:08:54Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.28 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **39.2%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.5%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 40.1%; Under 3.5 goals: 80.3%; Double Chance 1X: 60.8%; Double Chance X2: 65.3%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 44.5%; BTTS No (at least one team does not score): 55.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 34.7% | 2.88 |
| Draw | 26.1% | 3.83 |
| Napoli win | 39.2% | 2.55 |

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
| 2 | 1-1 | 12.08% |
| 3 | 0-1 | 11.52% |
| 4 | 0-0 | 9.36% |
| 5 | 2-1 | 8.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 34.7% | 45.0% | 2.20 | -23.6% |
| Draw | 26.1% | 26.4% | 3.90 | +1.8% |
| Napoli win | 39.2% | 28.6% | 3.45 | +35.1% |
| Over 2.5 | 40.1% | 59.2% | 1.68 | -32.6% |
| Under 2.5 | 59.9% | 40.8% | 2.38 | +42.6% |

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
| Market best home last update utc | 2026-10-12T21:08:52Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:54Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.5% |
| P btts no | 55.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.68 |
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
| P home draw | 60.8% |
| P draw away | 65.3% |
| Raw p home draw | 50.2% |
| Raw p draw away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.12 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | -10.3% |
| Draw probability edge | -0.3% |
| Away probability edge | +10.6% |
| Over 2.5 probability edge | -19.1% |
| Under 2.5 probability edge | +19.1% |
| Raw edge prob home | -0.2055 |
| Raw ev home | -0.4621 |
| Raw edge prob draw | -0.0062 |
| Raw ev draw | 0.0060 |
| Raw edge prob away | 0.2117 |
| Raw ev away | 0.7165 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **50.2%**. Expected goals are 1.18 for AS Roma and 1.67 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.4%; Under 3.5 goals: 67.9%; Double Chance 1X: 49.8%; Double Chance X2: 73.3%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.7% | 3.75 |
| Draw | 23.1% | 4.34 |
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
| 1 | 1-1 | 10.83% |
| 2 | 0-1 | 10.36% |
| 3 | 1-2 | 9.67% |
| 4 | 0-2 | 8.19% |
| 5 | 1-0 | 7.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.7% | 25.9% | 3.88 | +3.6% |
| Draw | 23.1% | 23.1% | 4.20 | -3.1% |
| Real Madrid win | 50.2% | 51.0% | 1.99 | -0.0% |
| Over 2.5 | 54.4% | 67.5% | 1.44 | -21.7% |
| Under 2.5 | 45.6% | 32.5% | 2.88 | +31.4% |

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
| Market best home last update utc | 2026-10-12T21:07:37Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
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
| Fair Under 0.5 odds | 19.25 |
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
| P home draw | 49.8% |
| P draw away | 73.3% |
| Raw p home draw | 50.5% |
| Raw p draw away | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.55 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.88 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.84 |
| Home probability edge | +0.8% |
| Draw probability edge | -0.0% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -13.1% |
| Under 2.5 probability edge | +13.1% |
| Raw edge prob home | 0.0162 |
| Raw ev home | 0.0674 |
| Raw edge prob draw | -0.0009 |
| Raw ev draw | -0.0332 |
| Raw edge prob away | -0.0153 |
| Raw ev away | -0.0155 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **67.3%**. Expected goals are 2.23 for Aston Villa and 0.61 for Fenerbahce (2.84 combined). The most likely exact score is 2-0 at 13.1%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 51.7%; Under 3.5 goals: 69.8%; Double Chance 1X: 86.8%; Double Chance X2: 32.7%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 41.6%; BTTS No (at least one team does not score): 58.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 67.3% | 1.49 |
| Draw | 19.5% | 5.12 |
| Fenerbahce win | 13.2% | 7.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.23 |
| Fenerbahce expected goals | 0.61 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 51.7% |
| Under 2.5 | 48.3% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.07% |
| 2 | 1-0 | 12.07% |
| 3 | 3-0 | 9.72% |
| 4 | 1-1 | 9.13% |
| 5 | 2-1 | 7.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 67.3% | 59.6% | 1.69 | +13.7% |
| Draw | 19.5% | 22.9% | 4.30 | -16.1% |
| Fenerbahce win | 13.2% | 17.4% | 5.60 | -26.0% |
| Over 2.5 | 51.7% | 56.9% | 1.69 | -12.6% |
| Under 2.5 | 48.3% | 43.1% | 2.36 | +13.9% |

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
| Market best home last update utc | 2026-10-12T21:07:37Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 41.6% |
| P btts no | 58.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.15 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.09 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.74 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.1% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 40.3% |
| P home draw | 86.8% |
| P draw away | 32.7% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.62 |
| Reference draw odds | 3.95 |
| Reference away odds | 5.10 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.17 |
| Home probability edge | +7.6% |
| Draw probability edge | -3.4% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | 0.1529 |
| Raw ev home | 0.2660 |
| Raw edge prob draw | -0.0683 |
| Raw ev draw | -0.3073 |
| Raw edge prob away | -0.0846 |
| Raw ev away | -0.4970 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **45.8%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-2 at 8.7%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.0%; Double Chance 1X: 54.2%; Double Chance X2: 67.5%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 70.2%; BTTS No (at least one team does not score): 29.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 32.5% | 3.08 |
| Draw | 21.8% | 4.59 |
| Borussia Dortmund win | 45.8% | 2.19 |

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
| 1 | 1-2 | 8.67% |
| 2 | 1-1 | 8.54% |
| 3 | 2-2 | 7.53% |
| 4 | 2-1 | 6.78% |
| 5 | 0-1 | 5.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 32.5% | 29.4% | 3.35 | +8.8% |
| Draw | 21.8% | 22.8% | 4.25 | -7.4% |
| Borussia Dortmund win | 45.8% | 47.8% | 2.14 | -2.1% |
| Over 2.5 | 70.7% | 70.0% | 1.40 | -1.1% |
| Under 2.5 | 29.3% | 30.0% | 3.03 | -11.1% |

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
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:51Z |
| Market best away last update utc | 2026-10-12T21:07:37Z |
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
| Fair Under 0.5 odds | 44.80 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
| Fair Over 2.5 odds | 1.42 |
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
| P home draw | 54.2% |
| P draw away | 67.5% |
| Raw p home draw | 56.2% |
| Raw p draw away | 64.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.15 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.03 |
| Home probability edge | +3.0% |
| Draw probability edge | -1.0% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0607 |
| Raw ev home | 0.1893 |
| Raw edge prob draw | -0.0206 |
| Raw ev draw | -0.1182 |
| Raw edge prob away | -0.0401 |
| Raw ev away | -0.0637 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **62.5%**. Expected goals are 1.82 for Feyenoord and 3.81 for Como (5.63 combined). The most likely exact score is 2-2 at 6.2%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.8%; Under 3.5 goals: 19.7%; Double Chance 1X: 37.5%; Double Chance X2: 80.1%; Under 4.5 goals: 35.9%; BTTS Yes (both teams score): 83.3%; BTTS No (at least one team does not score): 16.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 19.9% | 5.02 |
| Draw | 17.5% | 5.70 |
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
| 1 | 2-2 | 6.22% |
| 2 | 1-3 | 5.12% |
| 3 | 1-4 | 4.88% |
| 4 | 3-3 | 4.79% |
| 5 | 2-3 | 4.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 19.9% | 25.6% | 3.75 | -25.4% |
| Draw | 17.5% | 22.9% | 4.37 | -23.3% |
| Como win | 62.5% | 51.4% | 2.00 | +25.1% |
| Over 2.5 | 90.8% | 68.0% | 1.43 | +29.9% |
| Under 2.5 | 9.2% | 32.0% | 2.87 | -73.7% |

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
| Market best home last update utc | 2026-10-12T21:08:51Z |
| Market best draw last update utc | 2026-10-12T21:08:51Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
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
| Fair Under 0.5 odds | 295.79 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 37.08 |
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
| P home draw | 37.5% |
| P draw away | 80.1% |
| Raw p home draw | 26.3% |
| Raw p draw away | 85.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.60 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.87 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.87 |
| Home probability edge | -5.7% |
| Draw probability edge | -5.4% |
| Away probability edge | +11.1% |
| Over 2.5 probability edge | +22.9% |
| Under 2.5 probability edge | -22.9% |
| Raw edge prob home | -0.1148 |
| Raw ev home | -0.4687 |
| Raw edge prob draw | -0.1076 |
| Raw ev draw | -0.4684 |
| Raw edge prob away | 0.2224 |
| Raw ev away | 0.4734 |
| Market p home draw | 50.4% |
| Market home draw odds | 1.92 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-12T21:07:37Z |
| Market reference home draw last update utc | 2026-10-12T21:09:04Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.2% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-12T21:07:37Z |
| Market reference draw away last update utc | 2026-10-12T21:09:04Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.92 |
| Market reference dc draw away odds | 1.34 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 86.7% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-12T21:08:52Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.40 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 54.6% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-12T21:04:22Z |
| Market reference under 3 5 odds | 1.77 |
| Market reference under 3 5 opposite odds | 2.11 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 67.9% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-12T21:08:54Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.91 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **72.4%**. Expected goals are 0.28 for LASK and 1.45 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 27.7%. Goal-market probabilities: at least one goal: 86.3%; Over 2.5 goals: 26.7%; Under 3.5 goals: 89.7%; Double Chance 1X: 27.6%; Double Chance X2: 92.1%; Under 4.5 goals: 96.6%; BTTS Yes (both teams score): 17.6%; BTTS No (at least one team does not score): 82.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 7.9% | 12.72 |
| Draw | 19.8% | 5.06 |
| Liverpool win | 72.4% | 1.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.45 |
| Expected total goals | 1.74 |
| Over 0.5 | 86.3% |
| Under 0.5 | 13.7% |
| Over 1.5 | 52.8% |
| Under 1.5 | 47.2% |
| Over 2.5 | 26.7% |
| Under 2.5 | 73.3% |
| Over 3.5 | 10.3% |
| Under 3.5 | 89.7% |
| Over 4.5 | 3.4% |
| Under 4.5 | 96.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 27.73% |
| 2 | 0-2 | 19.89% |
| 3 | 0-0 | 13.71% |
| 4 | 0-3 | 9.64% |
| 5 | 1-0 | 5.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 7.9% | 8.4% | 11.00 | -13.5% |
| Draw | 19.8% | 14.6% | 6.75 | +33.4% |
| Liverpool win | 72.4% | 76.9% | 1.32 | -4.5% |
| Over 2.5 | 26.7% | 70.5% | 1.38 | -63.1% |
| Under 2.5 | 73.3% | 29.5% | 3.10 | +127.1% |

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
| Market best home last update utc | 2026-10-12T21:08:22Z |
| Market best draw last update utc | 2026-10-12T21:08:09Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
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
| P btts yes | 17.6% |
| P btts no | 82.4% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.30 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.12 |
| Fair Over 2.5 odds | 3.74 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 9.69 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 29.38 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 67.8% |
| Raw p over 1 5 | 51.4% |
| Raw p under 3 5 | 90.1% |
| Raw p btts yes | 18.5% |
| P home draw | 27.6% |
| P draw away | 92.1% |
| Raw p home draw | 32.2% |
| Raw p draw away | 92.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 9.50 |
| Reference draw odds | 5.75 |
| Reference away odds | 1.27 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.08 |
| Home probability edge | -0.6% |
| Draw probability edge | +5.1% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -43.8% |
| Under 2.5 probability edge | +43.8% |
| Raw edge prob home | -0.0115 |
| Raw ev home | -0.1983 |
| Raw edge prob draw | 0.1024 |
| Raw ev draw | 0.6798 |
| Raw edge prob away | -0.0909 |
| Raw ev away | -0.1047 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **44.2%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.7%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 69.1%; Under 3.5 goals: 51.9%; Double Chance 1X: 55.8%; Double Chance X2: 65.7%; Under 4.5 goals: 71.1%; BTTS Yes (both teams score): 67.9%; BTTS No (at least one team does not score): 32.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 34.3% | 2.91 |
| Draw | 21.5% | 4.66 |
| Paris Saint Germain win | 44.2% | 2.26 |

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
| Over 4.5 | 28.9% |
| Under 4.5 | 71.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.73% |
| 2 | 2-1 | 8.28% |
| 3 | 1-2 | 7.20% |
| 4 | 2-2 | 7.19% |
| 5 | 1-0 | 5.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 34.3% | 44.6% | 2.28 | -21.7% |
| Draw | 21.5% | 23.6% | 4.20 | -9.9% |
| Paris Saint Germain win | 44.2% | 31.8% | 3.10 | +37.1% |
| Over 2.5 | 69.1% | 67.0% | 1.45 | +0.2% |
| Under 2.5 | 30.9% | 33.0% | 2.80 | -13.6% |

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
| Market best home last update utc | 2026-10-12T21:07:53Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
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
| Fair Under 0.5 odds | 40.32 |
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
| P home draw | 55.8% |
| P draw away | 65.7% |
| Raw p home draw | 43.3% |
| Raw p draw away | 76.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.14 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.95 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -10.3% |
| Draw probability edge | -2.2% |
| Away probability edge | +12.5% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | -0.2061 |
| Raw ev home | -0.4523 |
| Raw edge prob draw | -0.0432 |
| Raw ev draw | -0.1895 |
| Raw edge prob away | 0.2493 |
| Raw ev away | 0.7571 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **61.7%**. Expected goals are 3.29 for Real Betis and 1.29 for Porto (4.58 combined). The most likely exact score is 2-2 at 7.1%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 81.0%; Under 3.5 goals: 35.1%; Double Chance 1X: 80.7%; Double Chance X2: 38.3%; Under 4.5 goals: 54.8%; BTTS Yes (both teams score): 72.2%; BTTS No (at least one team does not score): 27.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 61.7% | 1.62 |
| Draw | 19.0% | 5.26 |
| Porto win | 19.3% | 5.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 3.29 |
| Porto expected goals | 1.29 |
| Expected total goals | 4.58 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 93.3% |
| Under 1.5 | 6.7% |
| Over 2.5 | 81.0% |
| Under 2.5 | 19.0% |
| Over 3.5 | 64.9% |
| Under 3.5 | 35.1% |
| Over 4.5 | 45.2% |
| Under 4.5 | 54.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.06% |
| 2 | 3-1 | 6.37% |
| 3 | 1-1 | 6.31% |
| 4 | 2-1 | 5.80% |
| 5 | 4-1 | 5.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 61.7% | 47.3% | 2.16 | +33.3% |
| Draw | 19.0% | 25.6% | 3.90 | -25.9% |
| Porto win | 19.3% | 27.2% | 3.60 | -30.5% |
| Over 2.5 | 81.0% | 57.2% | 1.79 | +45.0% |
| Under 2.5 | 19.0% | 42.8% | 2.22 | -57.9% |

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
| Market best home last update utc | 2026-10-12T21:07:37Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | BetAnything |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 72.2% |
| P btts no | 27.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 81.21 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.85 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.27 |
| Fair Over 3.5 odds | 1.54 |
| Fair Under 3.5 odds | 2.85 |
| Fair Over 4.5 odds | 2.21 |
| Fair Under 4.5 odds | 1.83 |
| Unadjusted home-win probability | 76.1% |
| Unadjusted draw probability | 12.4% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 94.1% |
| Raw p under 3 5 | 32.9% |
| Raw p btts yes | 69.6% |
| P home draw | 80.7% |
| P draw away | 38.3% |
| Raw p home draw | 88.6% |
| Raw p draw away | 23.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.02 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | +14.4% |
| Draw probability edge | -6.6% |
| Away probability edge | -7.9% |
| Over 2.5 probability edge | +23.8% |
| Under 2.5 probability edge | -23.8% |
| Raw edge prob home | 0.2883 |
| Raw ev home | 0.6441 |
| Raw edge prob draw | -0.1312 |
| Raw ev draw | -0.5150 |
| Raw edge prob away | -0.1571 |
| Raw ev away | -0.5878 |
| Market p home draw | 72.2% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-12T21:07:37Z |
| Market reference home draw last update utc | 2026-10-12T21:09:06Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.9% |
| Market draw away odds | 1.83 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-12T21:09:06Z |
| Market reference draw away last update utc | 2026-10-12T21:09:06Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 80.1% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-12T21:08:52Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 66.1% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-12T21:08:52Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.74 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 59.6% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-12T21:08:54Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.35 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.4%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 51.0%; Under 3.5 goals: 70.6%; Double Chance 1X: 65.3%; Double Chance X2: 60.6%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.4% | 2.54 |
| Draw | 25.9% | 3.87 |
| AEK Athens win | 34.7% | 2.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.49 |
| AEK Athens expected goals | 1.25 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.22% |
| 2 | 1-0 | 9.31% |
| 3 | 0-1 | 9.26% |
| 4 | 2-1 | 8.16% |
| 5 | 1-2 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.4% | 35.6% | 2.73 | +7.7% |
| Draw | 25.9% | 27.5% | 3.55 | -8.2% |
| AEK Athens win | 34.7% | 36.8% | 2.80 | -2.8% |
| Over 2.5 | 51.0% | 51.2% | 1.95 | -0.5% |
| Under 2.5 | 49.0% | 48.8% | 2.00 | -2.1% |

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
| Market best home last update utc | 2026-10-12T21:07:37Z |
| Market best draw last update utc | 2026-10-12T21:08:51Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 67/100 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.97 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.41 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.11 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 54.7% |
| P home draw | 65.3% |
| P draw away | 60.6% |
| Raw p home draw | 67.4% |
| Raw p draw away | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.63 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.55 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.93 |
| Home probability edge | +3.8% |
| Draw probability edge | -1.7% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0760 |
| Raw ev home | 0.1804 |
| Raw edge prob draw | -0.0333 |
| Raw ev draw | -0.1410 |
| Raw edge prob away | -0.0427 |
| Raw ev away | -0.0882 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.4%**. Expected goals are 1.46 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 72.7%; Under 3.5 goals: 48.5%; Double Chance 1X: 33.6%; Double Chance X2: 83.1%; Under 4.5 goals: 67.6%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 16.9% | 5.91 |
| Draw | 16.6% | 6.01 |
| VfB Stuttgart win | 66.4% | 1.51 |

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
| 1 | 1-2 | 10.76% |
| 2 | 1-3 | 8.07% |
| 3 | 0-2 | 7.40% |
| 4 | 0-1 | 7.05% |
| 5 | 1-1 | 6.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 16.9% | 9.0% | 11.00 | +86.0% |
| Draw | 16.6% | 14.0% | 6.60 | +9.9% |
| VfB Stuttgart win | 66.4% | 77.0% | 1.31 | -13.0% |
| Over 2.5 | 72.7% | 72.2% | 1.35 | -1.9% |
| Under 2.5 | 27.3% | 27.8% | 3.26 | -10.9% |

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
| Market best home last update utc | 2026-10-12T21:08:22Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:07:37Z |
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
| Fair Under 0.5 odds | 56.27 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.67 |
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
| P home draw | 33.6% |
| P draw away | 83.1% |
| Raw p home draw | 44.1% |
| Raw p draw away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 9.00 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.27 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.26 |
| Home probability edge | +7.9% |
| Draw probability edge | +2.6% |
| Away probability edge | -10.5% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.1581 |
| Raw ev home | 1.7297 |
| Raw edge prob draw | 0.0522 |
| Raw ev draw | 0.2708 |
| Raw edge prob away | -0.2103 |
| Raw ev away | -0.2673 |

</details>


---
