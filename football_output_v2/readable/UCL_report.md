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
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 18.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 18.00 |
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

The model's most likely 1X2 outcome is **Arsenal win** at **75.3%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.6%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 49.8%; Under 3.5 goals: 73.0%; Double Chance 1X: 90.8%; Double Chance X2: 24.7%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 39.2%; BTTS No (at least one team does not score): 60.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 75.3% | 1.33 |
| Draw | 15.5% | 6.45 |
| Lille win | 9.2% | 10.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.93 |
| Lille expected goals | 0.65 |
| Expected total goals | 2.58 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 49.8% |
| Under 2.5 | 50.2% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.8% |
| Under 4.5 | 87.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.62% |
| 2 | 2-0 | 15.52% |
| 3 | 2-1 | 10.15% |
| 4 | 3-0 | 9.98% |
| 5 | 1-1 | 7.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 75.3% | 82.4% | 1.23 | -7.4% |
| Draw | 15.5% | 11.4% | 7.80 | +20.9% |
| Lille win | 9.2% | 6.2% | 16.00 | +47.8% |
| Over 2.5 | 49.8% | 64.9% | 1.50 | -25.3% |
| Under 2.5 | 50.2% | 35.1% | 2.63 | +32.0% |

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
| Market best home last update utc | 2026-10-13T11:02:18Z |
| Market best draw last update utc | 2026-10-13T11:02:57Z |
| Market best away last update utc | 2026-10-13T11:02:18Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (FR) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 39.2% |
| P btts no | 60.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.86 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.70 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.83 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 72.5% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 40.6% |
| P home draw | 90.8% |
| P draw away | 24.7% |
| Raw p home draw | 87.8% |
| Raw p draw away | 31.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.19 |
| Reference draw odds | 7.00 |
| Reference away odds | 12.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -7.1% |
| Draw probability edge | +4.1% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | -15.1% |
| Under 2.5 probability edge | +15.1% |
| Raw edge prob home | -0.1418 |
| Raw ev home | -0.1615 |
| Raw edge prob draw | 0.0819 |
| Raw ev draw | 0.5283 |
| Raw edge prob away | 0.0599 |
| Raw ev away | 0.9575 |
| Market p home draw | 93.9% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:03:24Z |
| Market reference home draw last update utc | 2026-10-13T11:03:32Z |
| Market home draw bookmakers | 4 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 20.6% |
| Market draw away odds | 4.86 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:03:24Z |
| Market reference draw away last update utc | 2026-10-13T11:03:32Z |
| Market draw away bookmakers | 4 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.02 |
| Market reference dc draw away odds | 4.65 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 58.8% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:02:24Z |
| Market reference under 3 5 odds | 1.64 |
| Market reference under 3 5 opposite odds | 2.28 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 44.7% |
| Market btts yes odds | 2.23 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:03:24Z |
| Market reference btts yes odds | 2.22 |
| Market reference btts yes opposite odds | 1.80 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **64.0%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.6%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.9%; Under 3.5 goals: 24.5%; Double Chance 1X: 81.7%; Double Chance X2: 36.0%; Under 4.5 goals: 42.3%; BTTS Yes (both teams score): 78.7%; BTTS No (at least one team does not score): 21.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 64.0% | 1.56 |
| Draw | 17.7% | 5.65 |
| Manchester United win | 18.3% | 5.47 |

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
| Over 3.5 | 75.5% |
| Under 3.5 | 24.5% |
| Over 4.5 | 57.7% |
| Under 4.5 | 42.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.61% |
| 2 | 3-1 | 5.70% |
| 3 | 4-1 | 5.31% |
| 4 | 2-1 | 4.59% |
| 5 | 3-2 | 4.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 64.0% | 50.9% | 1.99 | +27.4% |
| Draw | 17.7% | 24.0% | 3.95 | -30.0% |
| Manchester United win | 18.3% | 25.1% | 4.00 | -26.9% |
| Over 2.5 | 87.9% | 58.8% | 1.71 | +50.3% |
| Under 2.5 | 12.1% | 41.2% | 2.33 | -71.8% |

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
| Market best home last update utc | 2026-10-13T11:03:01Z |
| Market best draw last update utc | 2026-10-13T11:03:01Z |
| Market best away last update utc | 2026-10-13T11:03:01Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 78.7% |
| P btts no | 21.3% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 175.32 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.38 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.26 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.08 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 77.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 23.0% |
| Raw p btts yes | 76.6% |
| P home draw | 81.7% |
| P draw away | 36.0% |
| Raw p home draw | 88.5% |
| Raw p draw away | 22.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.65 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.17 |
| Home probability edge | +13.1% |
| Draw probability edge | -6.3% |
| Away probability edge | -6.8% |
| Over 2.5 probability edge | +29.1% |
| Under 2.5 probability edge | -29.1% |
| Raw edge prob home | 0.2616 |
| Raw ev home | 0.5341 |
| Raw edge prob draw | -0.1259 |
| Raw ev draw | -0.5492 |
| Raw edge prob away | -0.1356 |
| Raw ev away | -0.5400 |
| Market p home draw | 73.3% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:02:18Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.1% |
| Market draw away odds | 1.94 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:03:01Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 1.85 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 63.2% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T11:03:41Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.56 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.2% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.38 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **69.0%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 77.9%; Under 3.5 goals: 41.7%; Double Chance 1X: 31.0%; Double Chance X2: 84.0%; Under 4.5 goals: 60.9%; BTTS Yes (both teams score): 70.7%; BTTS No (at least one team does not score): 29.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 16.0% | 6.25 |
| Draw | 15.0% | 6.67 |
| Barcelona win | 69.0% | 1.45 |

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
| Over 2.5 | 77.9% |
| Under 2.5 | 22.1% |
| Over 3.5 | 58.3% |
| Under 3.5 | 41.7% |
| Over 4.5 | 39.1% |
| Under 4.5 | 60.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.87% |
| 2 | 1-3 | 8.26% |
| 3 | 0-2 | 6.43% |
| 4 | 2-3 | 6.34% |
| 5 | 0-1 | 5.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 16.0% | 9.1% | 10.00 | +59.9% |
| Draw | 15.0% | 12.1% | 7.50 | +12.4% |
| Barcelona win | 69.0% | 78.8% | 1.33 | -8.2% |
| Over 2.5 | 77.9% | 82.4% | 1.20 | -6.5% |
| Under 2.5 | 22.1% | 17.6% | 4.79 | +5.7% |

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
| Market best home last update utc | 2026-10-13T11:03:12Z |
| Market best draw last update utc | 2026-10-13T11:03:28Z |
| Market best away last update utc | 2026-10-13T11:02:18Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Matchbook |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.7% |
| P btts no | 29.3% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 84.37 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.34 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.53 |
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
| P home draw | 31.0% |
| P draw away | 84.0% |
| Raw p home draw | 40.8% |
| Raw p draw away | 77.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 8.75 |
| Reference draw odds | 6.75 |
| Reference away odds | 1.24 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.19 |
| Reference Under 2.5 odds | 4.75 |
| Home probability edge | +6.9% |
| Draw probability edge | +2.9% |
| Away probability edge | -9.8% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | 0.1382 |
| Raw ev home | 1.2898 |
| Raw edge prob draw | 0.0579 |
| Raw ev draw | 0.3416 |
| Raw edge prob away | -0.1961 |
| Raw ev away | -0.2125 |
| Market p home draw | 27.8% |
| Market home draw odds | 4.10 |
| Best home draw bookmaker | Codere (IT) |
| Market best home draw last update utc | 2026-10-13T11:03:29Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 87.6% |
| Market draw away odds | 1.09 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T11:02:18Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.40 |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 94.5% |
| Market over 1 5 odds | 1.05 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-13T11:03:42Z |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 12.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 36.2% |
| Market under 3 5 odds | 2.66 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference under 3 5 odds | 2.57 |
| Market reference under 3 5 opposite odds | 1.52 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.90 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **70.4%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 56.5%; Under 3.5 goals: 66.7%; Double Chance 1X: 87.3%; Double Chance X2: 29.6%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.4% | 1.42 |
| Draw | 16.9% | 5.93 |
| Club Brugge win | 12.7% | 7.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.92 |
| Club Brugge expected goals | 0.94 |
| Expected total goals | 2.86 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 56.5% |
| Under 2.5 | 43.5% |
| Over 3.5 | 33.3% |
| Under 3.5 | 66.7% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.30% |
| 2 | 2-0 | 12.19% |
| 3 | 2-1 | 11.51% |
| 4 | 1-1 | 7.98% |
| 5 | 3-0 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.4% | 80.1% | 1.28 | -9.9% |
| Draw | 16.9% | 13.0% | 7.00 | +18.1% |
| Club Brugge win | 12.7% | 6.9% | 12.75 | +62.2% |
| Over 2.5 | 56.5% | 72.7% | 1.34 | -24.3% |
| Under 2.5 | 43.5% | 27.3% | 3.32 | +44.4% |

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
| Market best home last update utc | 2026-10-13T11:03:01Z |
| Market best draw last update utc | 2026-10-13T11:03:01Z |
| Market best away last update utc | 2026-10-13T11:02:42Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.2% |
| P btts no | 49.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.72 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.64 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
| Fair Over 3.5 odds | 3.00 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.82 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 51.6% |
| P home draw | 87.3% |
| P draw away | 29.6% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.22 |
| Reference draw odds | 6.25 |
| Reference away odds | 11.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.30 |
| Home probability edge | -9.7% |
| Draw probability edge | +3.9% |
| Away probability edge | +5.8% |
| Over 2.5 probability edge | -16.2% |
| Under 2.5 probability edge | +16.2% |
| Raw edge prob home | -0.1942 |
| Raw ev home | -0.2230 |
| Raw edge prob draw | 0.0779 |
| Raw ev draw | 0.4531 |
| Raw edge prob away | 0.1163 |
| Raw ev away | 1.3640 |
| Market p home draw | 90.6% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:03:24Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 24.4% |
| Market draw away odds | 4.24 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:03:24Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 3.90 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 48.7% |
| Market under 3 5 odds | 1.99 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T11:03:41Z |
| Market reference under 3 5 odds | 1.99 |
| Market reference under 3 5 opposite odds | 1.89 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 55.8% |
| Market btts yes odds | 1.80 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **48.1%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 10.4%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 68.4%; Under 3.5 goals: 53.6%; Double Chance 1X: 68.0%; Double Chance X2: 51.9%; Under 4.5 goals: 72.2%; BTTS Yes (both teams score): 67.6%; BTTS No (at least one team does not score): 32.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 48.1% | 2.08 |
| Draw | 20.0% | 5.01 |
| PSV Eindhoven win | 32.0% | 3.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.65 |
| PSV Eindhoven expected goals | 1.87 |
| Expected total goals | 3.52 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 85.9% |
| Under 1.5 | 14.1% |
| Over 2.5 | 68.4% |
| Under 2.5 | 31.6% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.8% |
| Under 4.5 | 72.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.37% |
| 2 | 1-1 | 8.19% |
| 3 | 1-0 | 7.37% |
| 4 | 2-2 | 6.64% |
| 5 | 1-2 | 6.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 48.1% | 61.2% | 1.65 | -20.7% |
| Draw | 20.0% | 18.7% | 5.10 | +1.8% |
| PSV Eindhoven win | 32.0% | 20.1% | 4.90 | +56.6% |
| Over 2.5 | 68.4% | 77.6% | 1.29 | -11.8% |
| Under 2.5 | 31.6% | 22.4% | 3.91 | +23.7% |

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
| Market best home last update utc | 2026-10-13T11:02:18Z |
| Market best draw last update utc | 2026-10-13T11:03:01Z |
| Market best away last update utc | 2026-10-13T11:03:01Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.6% |
| P btts no | 32.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.20 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.08 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.16 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.60 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 35.0% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 67.8% |
| P home draw | 68.0% |
| P draw away | 51.9% |
| Raw p home draw | 56.2% |
| Raw p draw away | 65.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.75 |
| Reference away odds | 4.45 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.90 |
| Home probability edge | -13.1% |
| Draw probability edge | +1.2% |
| Away probability edge | +11.9% |
| Over 2.5 probability edge | -9.2% |
| Under 2.5 probability edge | +9.2% |
| Raw edge prob home | -0.2619 |
| Raw ev home | -0.4229 |
| Raw edge prob draw | 0.0245 |
| Raw ev draw | 0.0804 |
| Raw edge prob away | 0.2374 |
| Raw ev away | 1.1481 |
| Market p home draw | 78.9% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:02:18Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.1% |
| Market draw away odds | 2.44 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:03:01Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.25 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 91.5% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-13T11:03:42Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 8.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 42.7% |
| Market under 3 5 odds | 2.25 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T11:03:41Z |
| Market reference under 3 5 odds | 2.25 |
| Market reference under 3 5 opposite odds | 1.70 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 72.0% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.35 |
| Market reference btts yes opposite odds | 3.20 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **41.2%**. Expected goals are 1.28 for RC Lens and 1.60 for Sporting Lisbon (2.89 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.7%; Under 3.5 goals: 67.4%; Double Chance 1X: 58.8%; Double Chance X2: 65.5%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 34.5% | 2.90 |
| Draw | 24.3% | 4.12 |
| Sporting Lisbon win | 41.2% | 2.43 |

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
| 2 | 0-1 | 8.62% |
| 3 | 1-0 | 8.54% |
| 4 | 1-2 | 8.34% |
| 5 | 2-1 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 34.5% | 37.8% | 2.62 | -9.6% |
| Draw | 24.3% | 25.3% | 3.85 | -6.4% |
| Sporting Lisbon win | 41.2% | 37.0% | 2.76 | +13.7% |
| Over 2.5 | 54.7% | 60.8% | 1.64 | -10.3% |
| Under 2.5 | 45.3% | 39.2% | 2.46 | +11.4% |

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
| Market best home last update utc | 2026-10-13T11:03:01Z |
| Market best draw last update utc | 2026-10-13T11:03:01Z |
| Market best away last update utc | 2026-10-13T11:03:01Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
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
| P home draw | 58.8% |
| P draw away | 65.5% |
| Raw p home draw | 54.6% |
| Raw p draw away | 68.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.50 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.55 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Home probability edge | -3.3% |
| Draw probability edge | -1.0% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.0655 |
| Raw ev home | -0.1822 |
| Raw edge prob draw | -0.0192 |
| Raw ev draw | -0.1014 |
| Raw edge prob away | 0.0847 |
| Raw ev away | 0.2543 |
| Market p home draw | 63.2% |
| Market home draw odds | 1.53 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:02:18Z |
| Market reference home draw last update utc | 2026-10-13T11:03:32Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.4% |
| Market draw away odds | 1.56 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:03:01Z |
| Market reference draw away last update utc | 2026-10-13T11:03:32Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.52 |
| Market reference dc draw away odds | 1.54 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 61.4% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T11:03:12Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 64.2% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:12Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.76 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **55.5%**. Expected goals are 0.38 for Sabah FK and 1.28 for Slavia Praha (1.66 combined). The most likely exact score is 0-1 at 22.9%. Goal-market probabilities: at least one goal: 82.9%; Over 2.5 goals: 23.1%; Under 3.5 goals: 91.6%; Double Chance 1X: 44.5%; Double Chance X2: 81.8%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 22.1%; BTTS No (at least one team does not score): 77.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 18.2% | 5.48 |
| Draw | 26.3% | 3.81 |
| Slavia Praha win | 55.5% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.38 |
| Slavia Praha expected goals | 1.28 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.9% |
| Under 0.5 | 17.1% |
| Over 1.5 | 47.8% |
| Under 1.5 | 52.2% |
| Over 2.5 | 23.1% |
| Under 2.5 | 76.9% |
| Over 3.5 | 8.4% |
| Under 3.5 | 91.6% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.90% |
| 2 | 0-0 | 17.07% |
| 3 | 0-2 | 14.39% |
| 4 | 1-0 | 12.28% |
| 5 | 1-1 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 18.2% | 25.1% | 4.00 | -27.0% |
| Draw | 26.3% | 24.0% | 3.95 | +3.7% |
| Slavia Praha win | 55.5% | 50.9% | 2.02 | +12.1% |
| Over 2.5 | 23.1% | 60.5% | 1.65 | -61.9% |
| Under 2.5 | 76.9% | 39.5% | 2.45 | +88.5% |

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
| Market best home last update utc | 2026-10-13T11:03:01Z |
| Market best draw last update utc | 2026-10-13T11:03:01Z |
| Market best away last update utc | 2026-10-13T11:02:18Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 22.1% |
| P btts no | 77.9% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.86 |
| Fair Over 1.5 odds | 2.09 |
| Fair Under 1.5 odds | 1.91 |
| Fair Over 2.5 odds | 4.33 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.96 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.88 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.4% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 60.1% |
| Raw p over 1 5 | 49.0% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 22.4% |
| P home draw | 44.5% |
| P draw away | 81.8% |
| Raw p home draw | 39.9% |
| Raw p draw away | 88.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.65 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.88 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -6.8% |
| Draw probability edge | +2.3% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -37.4% |
| Under 2.5 probability edge | +37.4% |
| Raw edge prob home | -0.1364 |
| Raw ev home | -0.5432 |
| Raw edge prob draw | 0.0450 |
| Raw ev draw | 0.1261 |
| Raw edge prob away | 0.0914 |
| Raw ev away | 0.2134 |
| Market p home draw | 51.4% |
| Market home draw odds | 1.96 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:03:23Z |
| Market reference home draw last update utc | 2026-10-13T11:03:32Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.7% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | Marathon Bet |
| Market best draw away last update utc | 2026-10-13T11:03:32Z |
| Market reference draw away last update utc | 2026-10-13T11:03:32Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.88 |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 61.3% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T11:03:12Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.28 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.59 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:12Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.57 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **92.2%**. Expected goals are 0.70 for Viking FK and 4.47 for Bayern Munich (5.17 combined). The most likely exact score is 0-4 at 9.4%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.2%; Under 3.5 goals: 25.0%; Double Chance 1X: 7.8%; Double Chance X2: 97.3%; Under 4.5 goals: 42.2%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 2.7% | 36.94 |
| Draw | 5.1% | 19.45 |
| Bayern Munich win | 92.2% | 1.09 |

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
| Over 2.5 | 88.2% |
| Under 2.5 | 11.8% |
| Over 3.5 | 75.0% |
| Under 3.5 | 25.0% |
| Over 4.5 | 57.8% |
| Under 4.5 | 42.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.37% |
| 2 | 0-3 | 8.39% |
| 3 | 0-5 | 8.37% |
| 4 | 1-4 | 6.53% |
| 5 | 0-6 | 6.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 2.7% | 3.4% | 25.00 | -32.3% |
| Draw | 5.1% | 6.1% | 15.50 | -20.3% |
| Bayern Munich win | 92.2% | 90.4% | 1.13 | +4.1% |
| Over 2.5 | 88.2% | 85.4% | 1.15 | +1.4% |
| Under 2.5 | 11.8% | 14.6% | 5.54 | -34.6% |

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
| Market best home last update utc | 2026-10-13T11:02:57Z |
| Market best draw last update utc | 2026-10-13T11:02:18Z |
| Market best away last update utc | 2026-10-13T11:03:01Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 167.12 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 25.76 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.47 |
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
| P home draw | 7.8% |
| P draw away | 97.3% |
| Raw p home draw | 6.1% |
| Raw p draw away | 98.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 18.00 |
| Reference draw odds | 11.00 |
| Reference away odds | 1.09 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.50 |
| Home probability edge | -0.7% |
| Draw probability edge | -1.0% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | +2.8% |
| Under 2.5 probability edge | -2.8% |
| Raw edge prob home | -0.0147 |
| Raw ev home | -0.5073 |
| Raw edge prob draw | -0.0194 |
| Raw ev draw | -0.3536 |
| Raw edge prob away | 0.0342 |
| Raw ev away | 0.0606 |
| Market p home draw | 12.1% |
| Market home draw odds | 8.60 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:02:18Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 4 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 94.9% |
| Market draw away odds | 1.03 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:03:01Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 4 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 8.00 |
| Market reference dc draw away odds | 1.02 |
| Market reference dc home away odds | 1.04 |
| Market p over 1 5 | 96.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 15.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 32.3% |
| Market under 3 5 odds | 2.95 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference under 3 5 odds | 2.65 |
| Market reference under 3 5 opposite odds | 1.40 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 55.2% |
| Market btts yes odds | 1.74 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **38.4%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 14.0%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.4%; Double Chance 1X: 61.6%; Double Chance X2: 63.9%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 44.4%; BTTS No (at least one team does not score): 55.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 36.1% | 2.77 |
| Draw | 25.5% | 3.92 |
| Napoli win | 38.4% | 2.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.90 |
| Napoli expected goals | 1.42 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 65.5% |
| Under 1.5 | 34.5% |
| Over 2.5 | 40.2% |
| Under 2.5 | 59.8% |
| Over 3.5 | 19.6% |
| Under 3.5 | 80.4% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.01% |
| 2 | 1-1 | 11.81% |
| 3 | 0-1 | 11.29% |
| 4 | 0-0 | 9.15% |
| 5 | 2-1 | 8.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 36.1% | 47.7% | 2.16 | -22.1% |
| Draw | 25.5% | 25.2% | 3.80 | -3.0% |
| Napoli win | 38.4% | 27.1% | 3.65 | +40.2% |
| Over 2.5 | 40.2% | 57.7% | 1.72 | -30.8% |
| Under 2.5 | 59.8% | 42.3% | 2.30 | +37.5% |

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
| Market best home last update utc | 2026-10-13T11:03:01Z |
| Market best draw last update utc | 2026-10-13T11:03:01Z |
| Market best away last update utc | 2026-10-13T11:03:01Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.4% |
| P btts no | 55.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.93 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.90 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.09 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.08 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 44.3% |
| P home draw | 61.6% |
| P draw away | 63.9% |
| Raw p home draw | 50.2% |
| Raw p draw away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.63 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -11.6% |
| Draw probability edge | +0.3% |
| Away probability edge | +11.3% |
| Over 2.5 probability edge | -17.5% |
| Under 2.5 probability edge | +17.5% |
| Raw edge prob home | -0.2325 |
| Raw ev home | -0.4719 |
| Raw edge prob draw | 0.0056 |
| Raw ev draw | -0.0198 |
| Raw edge prob away | 0.2269 |
| Raw ev away | 0.8160 |
| Market p home draw | 70.4% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:02:18Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.9% |
| Market draw away odds | 1.80 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:03:24Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.35 |
| Market reference dc draw away odds | 1.70 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 65.9% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.3% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.40 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **50.6%**. Expected goals are 1.18 for AS Roma and 1.67 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 54.5%; Under 3.5 goals: 67.9%; Double Chance 1X: 49.4%; Double Chance X2: 73.4%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.6% | 3.76 |
| Draw | 22.8% | 4.39 |
| Real Madrid win | 50.6% | 1.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.18 |
| Real Madrid expected goals | 1.67 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
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
| 1 | 1-1 | 10.71% |
| 2 | 0-1 | 10.43% |
| 3 | 1-2 | 9.74% |
| 4 | 0-2 | 8.24% |
| 5 | 1-0 | 7.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.6% | 25.7% | 3.90 | +3.9% |
| Draw | 22.8% | 22.6% | 4.16 | -5.1% |
| Real Madrid win | 50.6% | 51.7% | 2.00 | +1.1% |
| Over 2.5 | 54.5% | 67.7% | 1.44 | -21.6% |
| Under 2.5 | 45.5% | 32.3% | 2.88 | +31.1% |

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
| Market best home last update utc | 2026-10-13T11:02:57Z |
| Market best draw last update utc | 2026-10-13T11:02:18Z |
| Market best away last update utc | 2026-10-13T11:03:01Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | 1xBet |
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
| Fair Under 0.5 odds | 19.47 |
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
| P home draw | 49.4% |
| P draw away | 73.4% |
| Raw p home draw | 50.5% |
| Raw p draw away | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.84 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.82 |
| Home probability edge | +0.9% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -13.2% |
| Under 2.5 probability edge | +13.2% |
| Raw edge prob home | 0.0176 |
| Raw ev home | 0.0729 |
| Raw edge prob draw | 0.0043 |
| Raw ev draw | -0.0424 |
| Raw edge prob away | -0.0219 |
| Raw ev away | -0.0106 |
| Market p home draw | 50.5% |
| Market home draw odds | 1.96 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:02:18Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.7% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:03:01Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.85 |
| Market reference dc draw away odds | 1.25 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 54.4% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T10:53:13Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.46 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.90 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **67.5%**. Expected goals are 2.23 for Aston Villa and 0.61 for Fenerbahce (2.84 combined). The most likely exact score is 2-0 at 13.1%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 51.9%; Under 3.5 goals: 69.8%; Double Chance 1X: 86.5%; Double Chance X2: 32.5%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 41.5%; BTTS No (at least one team does not score): 58.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 67.5% | 1.48 |
| Draw | 19.0% | 5.26 |
| Fenerbahce win | 13.5% | 7.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.23 |
| Fenerbahce expected goals | 0.61 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.11% |
| 2 | 1-0 | 12.10% |
| 3 | 3-0 | 9.75% |
| 4 | 1-1 | 8.89% |
| 5 | 2-1 | 7.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 67.5% | 60.1% | 1.69 | +14.0% |
| Draw | 19.0% | 21.9% | 4.40 | -16.3% |
| Fenerbahce win | 13.5% | 18.0% | 5.70 | -23.0% |
| Over 2.5 | 51.9% | 58.9% | 1.69 | -12.3% |
| Under 2.5 | 48.1% | 41.1% | 2.36 | +13.5% |

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
| Market best home last update utc | 2026-10-13T11:02:18Z |
| Market best draw last update utc | 2026-10-13T11:03:02Z |
| Market best away last update utc | 2026-10-13T11:03:02Z |
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
| P btts yes | 41.5% |
| P btts no | 58.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.56 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.09 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.71 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.1% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 40.3% |
| P home draw | 86.5% |
| P draw away | 32.5% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.60 |
| Reference draw odds | 4.05 |
| Reference away odds | 4.85 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.29 |
| Home probability edge | +7.4% |
| Draw probability edge | -2.9% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | 0.1486 |
| Raw ev home | 0.2660 |
| Raw edge prob draw | -0.0581 |
| Raw ev draw | -0.2912 |
| Raw edge prob away | -0.0905 |
| Raw ev away | -0.4881 |
| Market p home draw | 80.2% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:02:18Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.0% |
| Market draw away odds | 2.35 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:03:24Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.18 |
| Market reference dc draw away odds | 2.15 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.9% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 63.1% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 57.4% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T11:03:24Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.20 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **45.8%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-2 at 8.7%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.0%; Double Chance 1X: 54.2%; Double Chance X2: 67.5%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 70.2%; BTTS No (at least one team does not score): 29.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 32.5% | 3.08 |
| Draw | 21.7% | 4.60 |
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
| 2 | 1-1 | 8.52% |
| 3 | 2-2 | 7.51% |
| 4 | 2-1 | 6.78% |
| 5 | 0-1 | 5.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 32.5% | 29.5% | 3.30 | +7.2% |
| Draw | 21.7% | 22.7% | 4.22 | -8.3% |
| Borussia Dortmund win | 45.8% | 47.8% | 2.16 | -1.1% |
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
| Market best home last update utc | 2026-10-13T11:03:02Z |
| Market best draw last update utc | 2026-10-13T11:02:56Z |
| Market best away last update utc | 2026-10-13T11:03:02Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Betfair |
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
| P home draw | 54.2% |
| P draw away | 67.5% |
| Raw p home draw | 56.2% |
| Raw p draw away | 64.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.98 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +3.0% |
| Draw probability edge | -1.0% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.0602 |
| Raw ev home | 0.1715 |
| Raw edge prob draw | -0.0194 |
| Raw ev draw | -0.1244 |
| Raw edge prob away | -0.0408 |
| Raw ev away | -0.0550 |
| Market p home draw | 53.8% |
| Market home draw odds | 1.81 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:03:24Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.8% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T11:02:18Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.75 |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T10:57:36Z |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 1.98 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 70.8% |
| Market btts yes odds | 1.42 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.36 |
| Market reference btts yes opposite odds | 3.00 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **62.4%**. Expected goals are 1.82 for Feyenoord and 3.81 for Como (5.63 combined). The most likely exact score is 2-2 at 6.1%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.9%; Under 3.5 goals: 19.7%; Double Chance 1X: 37.6%; Double Chance X2: 79.7%; Under 4.5 goals: 35.8%; BTTS Yes (both teams score): 83.3%; BTTS No (at least one team does not score): 16.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 20.3% | 4.93 |
| Draw | 17.3% | 5.77 |
| Como win | 62.4% | 1.60 |

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
| Over 3.5 | 80.3% |
| Under 3.5 | 19.7% |
| Over 4.5 | 64.2% |
| Under 4.5 | 35.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.14% |
| 2 | 1-3 | 5.11% |
| 3 | 1-4 | 4.87% |
| 4 | 3-3 | 4.73% |
| 5 | 2-3 | 4.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 20.3% | 26.4% | 3.75 | -24.0% |
| Draw | 17.3% | 22.5% | 4.40 | -23.8% |
| Como win | 62.4% | 51.1% | 1.98 | +23.6% |
| Over 2.5 | 90.9% | 67.9% | 1.43 | +29.9% |
| Under 2.5 | 9.1% | 32.1% | 2.87 | -73.8% |

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
| Market best home last update utc | 2026-10-13T11:03:02Z |
| Market best draw last update utc | 2026-10-13T11:03:02Z |
| Market best away last update utc | 2026-10-13T11:02:18Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 83.3% |
| P btts no | 16.7% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 299.67 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 36.90 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.95 |
| Fair Over 3.5 odds | 1.25 |
| Fair Under 3.5 odds | 5.07 |
| Fair Over 4.5 odds | 1.56 |
| Fair Under 4.5 odds | 2.79 |
| Unadjusted home-win probability | 14.2% |
| Unadjusted draw probability | 12.2% |
| Unadjusted away-win probability | 73.7% |
| Raw p over 1 5 | 97.5% |
| Raw p under 3 5 | 18.8% |
| Raw p btts yes | 81.8% |
| P home draw | 37.6% |
| P draw away | 79.7% |
| Raw p home draw | 26.3% |
| Raw p draw away | 85.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.43 |
| Reference draw odds | 3.98 |
| Reference away odds | 1.86 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.85 |
| Home probability edge | -6.1% |
| Draw probability edge | -5.2% |
| Away probability edge | +11.3% |
| Over 2.5 probability edge | +23.0% |
| Under 2.5 probability edge | -23.0% |
| Raw edge prob home | -0.1222 |
| Raw ev home | -0.4687 |
| Raw edge prob draw | -0.1031 |
| Raw ev draw | -0.4648 |
| Raw edge prob away | 0.2253 |
| Raw ev away | 0.4586 |
| Market p home draw | 49.6% |
| Market home draw odds | 1.93 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:03:24Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.8% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T11:02:18Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.91 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 54.4% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:00:53Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 68.9% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.88 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **73.2%**. Expected goals are 0.28 for LASK and 1.45 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 28.1%. Goal-market probabilities: at least one goal: 86.9%; Over 2.5 goals: 27.0%; Under 3.5 goals: 89.6%; Double Chance 1X: 26.8%; Double Chance X2: 92.1%; Under 4.5 goals: 96.6%; BTTS Yes (both teams score): 17.5%; BTTS No (at least one team does not score): 82.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 7.9% | 12.63 |
| Draw | 18.9% | 5.30 |
| Liverpool win | 73.2% | 1.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.45 |
| Expected total goals | 1.74 |
| Over 0.5 | 86.9% |
| Under 0.5 | 13.1% |
| Over 1.5 | 53.1% |
| Under 1.5 | 46.9% |
| Over 2.5 | 27.0% |
| Under 2.5 | 73.0% |
| Over 3.5 | 10.4% |
| Under 3.5 | 89.6% |
| Over 4.5 | 3.4% |
| Under 4.5 | 96.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 28.05% |
| 2 | 0-2 | 20.12% |
| 3 | 0-0 | 13.08% |
| 4 | 0-3 | 9.76% |
| 5 | 1-0 | 5.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 7.9% | 8.5% | 10.50 | -16.9% |
| Draw | 18.9% | 12.9% | 6.75 | +27.4% |
| Liverpool win | 73.2% | 78.6% | 1.32 | -3.4% |
| Over 2.5 | 27.0% | 71.5% | 1.36 | -63.3% |
| Under 2.5 | 73.0% | 28.5% | 3.18 | +132.1% |

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
| Market best home last update utc | 2026-10-13T11:03:02Z |
| Market best draw last update utc | 2026-10-13T11:03:28Z |
| Market best away last update utc | 2026-10-13T11:02:18Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
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
| Fair Under 0.5 odds | 7.64 |
| Fair Over 1.5 odds | 1.88 |
| Fair Under 1.5 odds | 2.13 |
| Fair Over 2.5 odds | 3.70 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.61 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 29.06 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 67.8% |
| Raw p over 1 5 | 51.4% |
| Raw p under 3 5 | 90.1% |
| Raw p btts yes | 18.5% |
| P home draw | 26.8% |
| P draw away | 92.1% |
| Raw p home draw | 32.2% |
| Raw p draw away | 92.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 9.00 |
| Reference draw odds | 6.25 |
| Reference away odds | 1.24 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.15 |
| Home probability edge | -0.6% |
| Draw probability edge | +6.0% |
| Away probability edge | -5.4% |
| Over 2.5 probability edge | -44.5% |
| Under 2.5 probability edge | +44.5% |
| Raw edge prob home | -0.0126 |
| Raw ev home | -0.2348 |
| Raw edge prob draw | 0.1203 |
| Raw ev draw | 0.6798 |
| Raw edge prob away | -0.1077 |
| Raw ev away | -0.1047 |
| Market p home draw | 27.0% |
| Market home draw odds | 3.97 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:02:18Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 88.5% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:02:18Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.50 |
| Market reference dc draw away odds | 1.07 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 51.0% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:03:33Z |
| Market reference under 3 5 odds | 1.90 |
| Market reference under 3 5 opposite odds | 1.97 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.77 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.15 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **44.8%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.5%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 69.3%; Under 3.5 goals: 51.9%; Double Chance 1X: 55.2%; Double Chance X2: 65.7%; Under 4.5 goals: 70.9%; BTTS Yes (both teams score): 67.7%; BTTS No (at least one team does not score): 32.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 34.3% | 2.92 |
| Draw | 20.9% | 4.79 |
| Paris Saint Germain win | 44.8% | 2.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.40 |
| Paris Saint Germain expected goals | 2.23 |
| Expected total goals | 3.63 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 69.3% |
| Under 2.5 | 30.7% |
| Over 3.5 | 48.1% |
| Under 3.5 | 51.9% |
| Over 4.5 | 29.1% |
| Under 4.5 | 70.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.50% |
| 2 | 2-1 | 8.27% |
| 3 | 1-2 | 7.30% |
| 4 | 2-2 | 7.00% |
| 5 | 1-0 | 5.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 34.3% | 44.5% | 2.23 | -23.6% |
| Draw | 20.9% | 22.5% | 4.20 | -12.3% |
| Paris Saint Germain win | 44.8% | 33.0% | 3.15 | +41.2% |
| Over 2.5 | 69.3% | 67.2% | 1.45 | +0.5% |
| Under 2.5 | 30.7% | 32.8% | 2.80 | -14.0% |

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
| Market best home last update utc | 2026-10-13T11:02:18Z |
| Market best draw last update utc | 2026-10-13T11:03:02Z |
| Market best away last update utc | 2026-10-13T11:03:02Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.7% |
| P btts no | 32.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.42 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.53 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.26 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.44 |
| Fair Under 4.5 odds | 1.41 |
| Unadjusted home-win probability | 24.0% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 56.7% |
| Raw p over 1 5 | 87.3% |
| Raw p under 3 5 | 50.8% |
| Raw p btts yes | 66.9% |
| P home draw | 55.2% |
| P draw away | 65.7% |
| Raw p home draw | 43.3% |
| Raw p draw away | 76.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.12 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.80 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.78 |
| Home probability edge | -10.3% |
| Draw probability edge | -1.6% |
| Away probability edge | +11.8% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | -0.2050 |
| Raw ev home | -0.4643 |
| Raw edge prob draw | -0.0318 |
| Raw ev draw | -0.1895 |
| Raw edge prob away | 0.2368 |
| Raw ev away | 0.7854 |
| Market p home draw | 67.6% |
| Market home draw odds | 1.43 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:02:18Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.7% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T11:02:18Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.40 |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 55.3% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:03:33Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.14 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.47 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.90 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **61.5%**. Expected goals are 3.29 for Real Betis and 1.29 for Porto (4.58 combined). The most likely exact score is 2-2 at 7.0%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 81.0%; Under 3.5 goals: 35.1%; Double Chance 1X: 80.3%; Double Chance X2: 38.5%; Under 4.5 goals: 54.8%; BTTS Yes (both teams score): 72.2%; BTTS No (at least one team does not score): 27.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 61.5% | 1.63 |
| Draw | 18.8% | 5.33 |
| Porto win | 19.7% | 5.06 |

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
| Over 2.5 | 81.0% |
| Under 2.5 | 19.0% |
| Over 3.5 | 64.9% |
| Under 3.5 | 35.1% |
| Over 4.5 | 45.2% |
| Under 4.5 | 54.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.98% |
| 2 | 3-1 | 6.34% |
| 3 | 1-1 | 6.24% |
| 4 | 2-1 | 5.78% |
| 5 | 4-1 | 5.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 61.5% | 46.8% | 2.16 | +32.8% |
| Draw | 18.8% | 25.1% | 3.90 | -26.8% |
| Porto win | 19.7% | 28.0% | 3.70 | -26.9% |
| Over 2.5 | 81.0% | 55.3% | 1.79 | +45.1% |
| Under 2.5 | 19.0% | 44.7% | 2.19 | -58.5% |

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
| Market best home last update utc | 2026-10-13T11:02:18Z |
| Market best draw last update utc | 2026-10-13T11:03:01Z |
| Market best away last update utc | 2026-10-13T11:03:01Z |
| Odds bookmakers 1x2 | 22.00 |
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
| P btts yes | 72.2% |
| P btts no | 27.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 82.16 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.77 |
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
| P home draw | 80.3% |
| P draw away | 38.5% |
| Raw p home draw | 88.6% |
| Raw p draw away | 23.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.02 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | +14.6% |
| Draw probability edge | -6.3% |
| Away probability edge | -8.3% |
| Over 2.5 probability edge | +25.8% |
| Under 2.5 probability edge | -25.8% |
| Raw edge prob home | 0.2927 |
| Raw ev home | 0.6441 |
| Raw edge prob draw | -0.1268 |
| Raw ev draw | -0.5150 |
| Raw edge prob away | -0.1660 |
| Raw ev away | -0.5764 |
| Market p home draw | 72.2% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T11:02:18Z |
| Market reference home draw last update utc | 2026-10-13T11:03:48Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.9% |
| Market draw away odds | 1.83 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:03:48Z |
| Market reference draw away last update utc | 2026-10-13T11:03:48Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.2% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 66.1% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.74 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 59.6% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.35 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **40.1%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 51.2%; Under 3.5 goals: 70.6%; Double Chance 1X: 65.6%; Double Chance X2: 59.9%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 40.1% | 2.49 |
| Draw | 25.5% | 3.92 |
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
| Over 2.5 | 51.2% |
| Under 2.5 | 48.8% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.04% |
| 2 | 1-0 | 9.47% |
| 3 | 0-1 | 9.18% |
| 4 | 2-1 | 8.30% |
| 5 | 1-2 | 7.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 40.1% | 37.0% | 2.78 | +11.5% |
| Draw | 25.5% | 26.8% | 3.55 | -9.5% |
| AEK Athens win | 34.4% | 36.2% | 2.77 | -4.7% |
| Over 2.5 | 51.2% | 50.6% | 1.95 | -0.2% |
| Under 2.5 | 48.8% | 49.4% | 2.02 | -1.3% |

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
| Market best home last update utc | 2026-10-13T11:03:12Z |
| Market best draw last update utc | 2026-10-13T11:03:01Z |
| Market best away last update utc | 2026-10-13T11:02:18Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Matchbook |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 67/100 |
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.20 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.08 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 75.2% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 54.7% |
| P home draw | 65.6% |
| P draw away | 59.9% |
| Raw p home draw | 67.4% |
| Raw p draw away | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.52 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.57 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.93 |
| Home probability edge | +3.1% |
| Draw probability edge | -1.3% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | 0.0625 |
| Raw ev home | 0.2020 |
| Raw edge prob draw | -0.0260 |
| Raw ev draw | -0.1410 |
| Raw edge prob away | -0.0365 |
| Raw ev away | -0.0979 |
| Market p home draw | 63.0% |
| Market home draw odds | 1.53 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:03:48Z |
| Market reference home draw last update utc | 2026-10-13T11:03:48Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.9% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T11:02:18Z |
| Market reference draw away last update utc | 2026-10-13T11:03:48Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.53 |
| Market reference dc draw away odds | 1.51 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 77.3% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.60 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 71.3% |
| Market under 3 5 odds | 1.37 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T11:03:41Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.20 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 57.0% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.22 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.9%**. Expected goals are 1.46 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 72.8%; Under 3.5 goals: 48.5%; Double Chance 1X: 33.1%; Double Chance X2: 83.1%; Under 4.5 goals: 67.5%; BTTS Yes (both teams score): 67.0%; BTTS No (at least one team does not score): 33.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 16.9% | 5.91 |
| Draw | 16.2% | 6.18 |
| VfB Stuttgart win | 66.9% | 1.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.46 |
| VfB Stuttgart expected goals | 2.25 |
| Expected total goals | 3.71 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 88.5% |
| Under 1.5 | 11.5% |
| Over 2.5 | 72.8% |
| Under 2.5 | 27.2% |
| Over 3.5 | 51.5% |
| Under 3.5 | 48.5% |
| Over 4.5 | 32.5% |
| Under 4.5 | 67.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.83% |
| 2 | 1-3 | 8.13% |
| 3 | 0-2 | 7.44% |
| 4 | 0-1 | 7.10% |
| 5 | 1-1 | 6.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 16.9% | 9.0% | 11.00 | +86.2% |
| Draw | 16.2% | 13.1% | 6.60 | +6.9% |
| VfB Stuttgart win | 66.9% | 77.8% | 1.32 | -11.7% |
| Over 2.5 | 72.8% | 72.7% | 1.34 | -2.4% |
| Under 2.5 | 27.2% | 27.3% | 3.32 | -9.7% |

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
| Market best home last update utc | 2026-10-13T11:02:42Z |
| Market best draw last update utc | 2026-10-13T11:03:02Z |
| Market best away last update utc | 2026-10-13T11:03:02Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.0% |
| P btts no | 33.0% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 57.86 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.67 |
| Fair Over 2.5 odds | 1.37 |
| Fair Under 2.5 odds | 3.68 |
| Fair Over 3.5 odds | 1.94 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.08 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 24.8% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 55.9% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 68.2% |
| P home draw | 33.1% |
| P draw away | 83.1% |
| Raw p home draw | 44.1% |
| Raw p draw away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 8.50 |
| Reference draw odds | 6.10 |
| Reference away odds | 1.25 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.30 |
| Home probability edge | +7.9% |
| Draw probability edge | +3.1% |
| Away probability edge | -11.0% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.1577 |
| Raw ev home | 1.7297 |
| Raw edge prob draw | 0.0613 |
| Raw ev draw | 0.2708 |
| Raw edge prob away | -0.2190 |
| Raw ev away | -0.2617 |
| Market p home draw | 27.2% |
| Market home draw odds | 3.82 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T11:03:24Z |
| Market reference home draw last update utc | 2026-10-13T11:03:42Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.1% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T11:03:24Z |
| Market reference draw away last update utc | 2026-10-13T11:03:42Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.50 |
| Market reference dc draw away odds | 1.07 |
| Market reference dc home away odds | 1.14 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T11:02:42Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 49.9% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T11:03:07Z |
| Market reference under 3 5 odds | 1.94 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 58.9% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T11:03:41Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.25 |
| Market btts yes bookmakers | 4 |

</details>


---
