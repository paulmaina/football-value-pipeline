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

The model's most likely 1X2 outcome is **Arsenal win** at **75.3%**. Expected goals are 1.93 for Arsenal and 0.65 for Lille (2.58 combined). The most likely exact score is 1-0 at 16.6%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 49.8%; Under 3.5 goals: 73.0%; Double Chance 1X: 90.6%; Double Chance X2: 24.7%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 39.1%; BTTS No (at least one team does not score): 60.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 75.3% | 1.33 |
| Draw | 15.3% | 6.53 |
| Lille win | 9.4% | 10.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.93 |
| Lille expected goals | 0.65 |
| Expected total goals | 2.58 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
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
| 5 | 1-1 | 7.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 75.3% | 82.4% | 1.23 | -7.4% |
| Draw | 15.3% | 11.0% | 7.60 | +16.3% |
| Lille win | 9.4% | 6.6% | 17.00 | +60.0% |
| Over 2.5 | 49.8% | 63.6% | 1.52 | -24.2% |
| Under 2.5 | 50.2% | 36.4% | 2.57 | +28.9% |

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
| Market best home last update utc | 2026-10-13T07:41:45Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 39.1% |
| P btts no | 60.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.09 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.70 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.82 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 72.5% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 40.6% |
| P home draw | 90.6% |
| P draw away | 24.7% |
| Raw p home draw | 87.8% |
| Raw p draw away | 31.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.19 |
| Reference draw odds | 7.25 |
| Reference away odds | 11.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.55 |
| Home probability edge | -7.1% |
| Draw probability edge | +4.3% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -13.8% |
| Under 2.5 probability edge | +13.8% |
| Raw edge prob home | -0.1422 |
| Raw ev home | -0.1615 |
| Raw edge prob draw | 0.0858 |
| Raw ev draw | 0.4891 |
| Raw edge prob away | 0.0564 |
| Raw ev away | 1.0798 |
| Market p home draw | 93.6% |
| Market home draw odds | 1.04 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T07:42:53Z |
| Market reference home draw last update utc | 2026-10-13T07:42:53Z |
| Market home draw bookmakers | 4 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 20.2% |
| Market draw away odds | 4.82 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:42:53Z |
| Market reference draw away last update utc | 2026-10-13T07:42:53Z |
| Market draw away bookmakers | 4 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.04 |
| Market reference dc draw away odds | 4.82 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 83.6% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 60.5% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T07:42:15Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.41 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 43.7% |
| Market btts yes odds | 2.26 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 2.26 |
| Market reference btts yes opposite odds | 1.76 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **64.0%**. Expected goals are 3.73 for Atlético Madrid and 1.54 for Manchester United (5.27 combined). The most likely exact score is 2-2 at 6.4%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.0%; Under 3.5 goals: 24.6%; Double Chance 1X: 81.3%; Double Chance X2: 36.0%; Under 4.5 goals: 42.3%; BTTS Yes (both teams score): 78.7%; BTTS No (at least one team does not score): 21.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 64.0% | 1.56 |
| Draw | 17.3% | 5.79 |
| Manchester United win | 18.7% | 5.35 |

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
| Over 3.5 | 75.4% |
| Under 3.5 | 24.6% |
| Over 4.5 | 57.7% |
| Under 4.5 | 42.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.45% |
| 2 | 3-1 | 5.70% |
| 3 | 4-1 | 5.31% |
| 4 | 2-1 | 4.59% |
| 5 | 3-2 | 4.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 64.0% | 51.0% | 2.00 | +28.1% |
| Draw | 17.3% | 23.1% | 3.95 | -31.8% |
| Manchester United win | 18.7% | 25.9% | 3.95 | -26.2% |
| Over 2.5 | 88.0% | 59.4% | 1.66 | +46.0% |
| Under 2.5 | 12.0% | 40.6% | 2.43 | -70.7% |

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
| Market best home last update utc | 2026-10-13T07:42:58Z |
| Market best draw last update utc | 2026-10-13T07:43:00Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
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
| Fair Under 0.5 odds | 179.90 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.24 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.30 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.07 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.37 |
| Unadjusted home-win probability | 77.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 96.6% |
| Raw p under 3 5 | 23.0% |
| Raw p btts yes | 76.6% |
| P home draw | 81.3% |
| P draw away | 36.0% |
| Raw p home draw | 88.5% |
| Raw p draw away | 22.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.55 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +13.0% |
| Draw probability edge | -5.8% |
| Away probability edge | -7.2% |
| Over 2.5 probability edge | +28.6% |
| Under 2.5 probability edge | -28.6% |
| Raw edge prob home | 0.2608 |
| Raw ev home | 0.5418 |
| Raw edge prob draw | -0.1169 |
| Raw ev draw | -0.5492 |
| Raw edge prob away | -0.1439 |
| Raw ev away | -0.5458 |
| Market p home draw | 74.1% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T07:41:45Z |
| Market reference home draw last update utc | 2026-10-13T07:42:58Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.1% |
| Market draw away odds | 1.92 |
| Best draw away bookmaker | Marathon Bet |
| Market best draw away last update utc | 2026-10-13T07:42:21Z |
| Market reference draw away last update utc | 2026-10-13T07:42:58Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 1.87 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 5.10 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 61.3% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 61.0% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.54 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **68.4%**. Expected goals are 1.53 for Galatasaray and 2.51 for Barcelona (4.04 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 77.9%; Under 3.5 goals: 41.7%; Double Chance 1X: 31.6%; Double Chance X2: 83.3%; Under 4.5 goals: 60.9%; BTTS Yes (both teams score): 70.7%; BTTS No (at least one team does not score): 29.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 16.7% | 5.98 |
| Draw | 14.9% | 6.73 |
| Barcelona win | 68.4% | 1.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.53 |
| Barcelona expected goals | 2.51 |
| Expected total goals | 4.04 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 91.1% |
| Under 1.5 | 8.9% |
| Over 2.5 | 77.9% |
| Under 2.5 | 22.1% |
| Over 3.5 | 58.3% |
| Under 3.5 | 41.7% |
| Over 4.5 | 39.1% |
| Under 4.5 | 60.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.78% |
| 2 | 1-3 | 8.18% |
| 3 | 0-2 | 6.37% |
| 4 | 2-3 | 6.28% |
| 5 | 0-1 | 5.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 16.7% | 10.6% | 9.40 | +57.3% |
| Draw | 14.9% | 11.8% | 7.00 | +4.0% |
| Barcelona win | 68.4% | 77.6% | 1.33 | -9.0% |
| Over 2.5 | 77.9% | 83.0% | 1.20 | -6.5% |
| Under 2.5 | 22.1% | 17.0% | 4.91 | +8.3% |

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
| Market best home last update utc | 2026-10-13T07:42:59Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:41:45Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Matchbook |
| Best draw bookmaker | Betfair |
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
| Fair Under 0.5 odds | 85.15 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.29 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.53 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.40 |
| Fair Over 4.5 odds | 2.56 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.5% |
| Raw p btts yes | 71.7% |
| P home draw | 31.6% |
| P draw away | 83.3% |
| Raw p home draw | 40.8% |
| Raw p draw away | 77.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 7.75 |
| Reference draw odds | 7.00 |
| Reference away odds | 1.26 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.18 |
| Reference Under 2.5 odds | 4.85 |
| Home probability edge | +6.2% |
| Draw probability edge | +3.0% |
| Away probability edge | -9.2% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | 0.1232 |
| Raw ev home | 1.1524 |
| Raw edge prob draw | 0.0606 |
| Raw ev draw | 0.2522 |
| Raw edge prob away | -0.1839 |
| Raw ev away | -0.2125 |
| Market p home draw | 25.9% |
| Market home draw odds | 3.73 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T07:42:53Z |
| Market reference home draw last update utc | 2026-10-13T07:42:58Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 88.2% |
| Market draw away odds | 1.10 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:42:53Z |
| Market reference draw away last update utc | 2026-10-13T07:42:58Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.68 |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 93.6% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 11.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 36.6% |
| Market under 3 5 odds | 2.68 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T07:42:43Z |
| Market reference under 3 5 odds | 2.59 |
| Market reference under 3 5 opposite odds | 1.54 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 68.7% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 3.15 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **70.5%**. Expected goals are 1.92 for Inter Milan and 0.94 for Club Brugge (2.86 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 56.6%; Under 3.5 goals: 66.7%; Double Chance 1X: 86.8%; Double Chance X2: 29.5%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.5% | 1.42 |
| Draw | 16.4% | 6.10 |
| Club Brugge win | 13.2% | 7.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.92 |
| Club Brugge expected goals | 0.94 |
| Expected total goals | 2.86 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 56.6% |
| Under 2.5 | 43.4% |
| Over 3.5 | 33.3% |
| Under 3.5 | 66.7% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.31% |
| 2 | 2-0 | 12.20% |
| 3 | 2-1 | 11.52% |
| 4 | 3-0 | 7.81% |
| 5 | 1-1 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.5% | 80.2% | 1.28 | -9.8% |
| Draw | 16.4% | 12.0% | 6.80 | +11.5% |
| Club Brugge win | 13.2% | 7.8% | 13.00 | +71.0% |
| Over 2.5 | 56.6% | 70.9% | 1.37 | -22.4% |
| Under 2.5 | 43.4% | 29.1% | 3.13 | +35.7% |

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
| Market best home last update utc | 2026-10-13T07:42:58Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.41 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.63 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 3.00 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.80 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 51.6% |
| P home draw | 86.8% |
| P draw away | 29.5% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.22 |
| Reference draw odds | 6.75 |
| Reference away odds | 10.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -9.8% |
| Draw probability edge | +4.4% |
| Away probability edge | +5.4% |
| Over 2.5 probability edge | -14.3% |
| Under 2.5 probability edge | +14.3% |
| Raw edge prob home | -0.1950 |
| Raw ev home | -0.2230 |
| Raw edge prob draw | 0.0874 |
| Raw ev draw | 0.4115 |
| Raw edge prob away | 0.1077 |
| Raw ev away | 1.4104 |
| Market p home draw | 91.1% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T07:42:53Z |
| Market reference home draw last update utc | 2026-10-13T07:42:58Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.8% |
| Market draw away odds | 4.27 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:42:53Z |
| Market reference draw away last update utc | 2026-10-13T07:42:58Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 4.20 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.80 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 51.0% |
| Market under 3 5 odds | 1.89 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T07:35:23Z |
| Market reference under 3 5 odds | 1.88 |
| Market reference under 3 5 opposite odds | 1.95 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 53.3% |
| Market btts yes odds | 1.86 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 1.86 |
| Market reference btts yes opposite odds | 2.12 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **47.8%**. Expected goals are 1.65 for RB Leipzig and 1.87 for PSV Eindhoven (3.52 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 68.4%; Under 3.5 goals: 53.6%; Double Chance 1X: 67.6%; Double Chance X2: 52.2%; Under 4.5 goals: 72.2%; BTTS Yes (both teams score): 67.6%; BTTS No (at least one team does not score): 32.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 47.8% | 2.09 |
| Draw | 19.8% | 5.05 |
| PSV Eindhoven win | 32.4% | 3.09 |

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
| 1 | 2-1 | 10.32% |
| 2 | 1-1 | 8.13% |
| 3 | 1-0 | 7.33% |
| 4 | 2-2 | 6.59% |
| 5 | 1-2 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 47.8% | 60.7% | 1.67 | -20.1% |
| Draw | 19.8% | 18.5% | 5.00 | -0.9% |
| PSV Eindhoven win | 32.4% | 20.9% | 4.85 | +56.9% |
| Over 2.5 | 68.4% | 77.6% | 1.29 | -11.8% |
| Under 2.5 | 31.6% | 22.4% | 3.91 | +23.5% |

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
| Market best home last update utc | 2026-10-13T07:42:58Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:42:59Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.6% |
| P btts no | 32.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.51 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.09 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.16 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.59 |
| Fair Under 4.5 odds | 1.39 |
| Unadjusted home-win probability | 35.0% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 67.8% |
| P home draw | 67.6% |
| P draw away | 52.2% |
| Raw p home draw | 56.2% |
| Raw p draw away | 65.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.70 |
| Reference away odds | 4.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.90 |
| Home probability edge | -12.9% |
| Draw probability edge | +1.4% |
| Away probability edge | +11.5% |
| Over 2.5 probability edge | -9.2% |
| Under 2.5 probability edge | +9.2% |
| Raw edge prob home | -0.2571 |
| Raw ev home | -0.4159 |
| Raw edge prob draw | 0.0273 |
| Raw ev draw | 0.0592 |
| Raw edge prob away | 0.2297 |
| Raw ev away | 1.1261 |
| Market p home draw | 79.7% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T07:41:45Z |
| Market reference home draw last update utc | 2026-10-13T07:43:14Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.0% |
| Market draw away odds | 2.43 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:43:14Z |
| Market reference draw away last update utc | 2026-10-13T07:43:14Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.43 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 91.5% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-13T07:43:14Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 8.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 42.6% |
| Market under 3 5 odds | 2.24 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T07:43:12Z |
| Market reference under 3 5 odds | 2.24 |
| Market reference under 3 5 opposite odds | 1.69 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 72.6% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 1.35 |
| Market reference btts yes opposite odds | 3.37 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **41.5%**. Expected goals are 1.28 for RC Lens and 1.60 for Sporting Lisbon (2.89 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 54.9%; Under 3.5 goals: 67.4%; Double Chance 1X: 58.5%; Double Chance X2: 65.2%; Under 4.5 goals: 83.5%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 34.8% | 2.87 |
| Draw | 23.7% | 4.22 |
| Sporting Lisbon win | 41.5% | 2.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.28 |
| Sporting Lisbon expected goals | 1.60 |
| Expected total goals | 2.89 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 54.9% |
| Under 2.5 | 45.1% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.5% |
| Under 4.5 | 83.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.06% |
| 2 | 0-1 | 8.69% |
| 3 | 1-0 | 8.62% |
| 4 | 1-2 | 8.40% |
| 5 | 2-1 | 8.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 34.8% | 38.4% | 2.64 | -8.1% |
| Draw | 23.7% | 24.0% | 3.85 | -8.8% |
| Sporting Lisbon win | 41.5% | 37.6% | 2.72 | +12.9% |
| Over 2.5 | 54.9% | 61.1% | 1.64 | -10.0% |
| Under 2.5 | 45.1% | 38.9% | 2.46 | +10.9% |

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
| Market best home last update utc | 2026-10-13T07:42:58Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
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
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.71 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.06 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.2% |
| P home draw | 58.5% |
| P draw away | 65.2% |
| Raw p home draw | 54.6% |
| Raw p draw away | 68.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.45 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -3.6% |
| Draw probability edge | -0.3% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | -0.0718 |
| Raw ev home | -0.1760 |
| Raw edge prob draw | -0.0068 |
| Raw ev draw | -0.1014 |
| Raw edge prob away | 0.0787 |
| Raw ev away | 0.2361 |
| Market p home draw | 63.3% |
| Market home draw odds | 1.53 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T07:41:45Z |
| Market reference home draw last update utc | 2026-10-13T07:42:58Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.5% |
| Market draw away odds | 1.55 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T07:41:45Z |
| Market reference draw away last update utc | 2026-10-13T07:42:58Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.51 |
| Market reference dc draw away odds | 1.53 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 5.10 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 61.7% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.48 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 63.5% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.72 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **53.9%**. Expected goals are 0.38 for Sabah FK and 1.28 for Slavia Praha (1.66 combined). The most likely exact score is 0-1 at 22.2%. Goal-market probabilities: at least one goal: 82.8%; Over 2.5 goals: 22.8%; Under 3.5 goals: 91.8%; Double Chance 1X: 46.1%; Double Chance X2: 80.3%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 22.2%; BTTS No (at least one team does not score): 77.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 19.7% | 5.08 |
| Draw | 26.4% | 3.78 |
| Slavia Praha win | 53.9% | 1.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.38 |
| Slavia Praha expected goals | 1.28 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.8% |
| Under 0.5 | 17.2% |
| Over 1.5 | 47.3% |
| Under 1.5 | 52.7% |
| Over 2.5 | 22.8% |
| Under 2.5 | 77.2% |
| Over 3.5 | 8.2% |
| Under 3.5 | 91.8% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 22.24% |
| 2 | 0-0 | 17.19% |
| 3 | 0-2 | 13.97% |
| 4 | 1-0 | 13.24% |
| 5 | 1-1 | 8.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 19.7% | 27.9% | 3.75 | -26.2% |
| Draw | 26.4% | 24.4% | 3.90 | +3.1% |
| Slavia Praha win | 53.9% | 47.7% | 2.10 | +13.2% |
| Over 2.5 | 22.8% | 59.4% | 1.71 | -60.9% |
| Under 2.5 | 77.2% | 40.6% | 2.32 | +79.0% |

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
| Market best home last update utc | 2026-10-13T07:42:58Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Betfair |
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
| Fair Under 0.5 odds | 5.82 |
| Fair Over 1.5 odds | 2.11 |
| Fair Under 1.5 odds | 1.90 |
| Fair Over 2.5 odds | 4.38 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 12.15 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 38.50 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.4% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 60.1% |
| Raw p over 1 5 | 49.0% |
| Raw p under 3 5 | 91.3% |
| Raw p btts yes | 22.4% |
| P home draw | 46.1% |
| P draw away | 80.3% |
| Raw p home draw | 39.9% |
| Raw p draw away | 88.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -8.3% |
| Draw probability edge | +2.1% |
| Away probability edge | +6.2% |
| Over 2.5 probability edge | -36.5% |
| Under 2.5 probability edge | +36.5% |
| Raw edge prob home | -0.1652 |
| Raw ev home | -0.5718 |
| Raw edge prob draw | 0.0414 |
| Raw ev draw | 0.1119 |
| Raw edge prob away | 0.1238 |
| Raw ev away | 0.2615 |
| Market p home draw | 53.9% |
| Market home draw odds | 1.86 |
| Best home draw bookmaker | Marathon Bet |
| Market best home draw last update utc | 2026-10-13T07:42:21Z |
| Market reference home draw last update utc | 2026-10-13T07:42:58Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.9% |
| Market draw away odds | 1.33 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:42:53Z |
| Market reference draw away last update utc | 2026-10-13T07:42:58Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.76 |
| Market reference dc draw away odds | 1.32 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 80.8% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.65 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T07:42:43Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.67 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.4% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.56 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **92.6%**. Expected goals are 0.70 for Viking FK and 4.47 for Bayern Munich (5.17 combined). The most likely exact score is 0-4 at 9.4%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 88.4%; Under 3.5 goals: 24.9%; Double Chance 1X: 7.4%; Double Chance X2: 97.0%; Under 4.5 goals: 41.9%; BTTS Yes (both teams score): 49.8%; BTTS No (at least one team does not score): 50.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 3.0% | 33.07 |
| Draw | 4.4% | 22.76 |
| Bayern Munich win | 92.6% | 1.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.70 |
| Bayern Munich expected goals | 4.47 |
| Expected total goals | 5.17 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 96.1% |
| Under 1.5 | 3.9% |
| Over 2.5 | 88.4% |
| Under 2.5 | 11.6% |
| Over 3.5 | 75.1% |
| Under 3.5 | 24.9% |
| Over 4.5 | 58.1% |
| Under 4.5 | 41.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.42% |
| 2 | 0-3 | 8.43% |
| 3 | 0-5 | 8.41% |
| 4 | 1-4 | 6.56% |
| 5 | 0-6 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 3.0% | 4.1% | 26.00 | -21.4% |
| Draw | 4.4% | 4.6% | 15.50 | -31.9% |
| Bayern Munich win | 92.6% | 91.3% | 1.12 | +3.7% |
| Over 2.5 | 88.4% | 87.0% | 1.15 | +1.7% |
| Under 2.5 | 11.6% | 13.0% | 6.10 | -29.5% |

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
| Market best home last update utc | 2026-10-13T07:42:13Z |
| Market best draw last update utc | 2026-10-13T07:41:45Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 49.8% |
| P btts no | 50.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 195.57 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 25.74 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.66 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.01 |
| Fair Over 4.5 odds | 1.72 |
| Fair Under 4.5 odds | 2.39 |
| Unadjusted home-win probability | 2.0% |
| Unadjusted draw probability | 4.2% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.4% |
| Raw p btts yes | 49.5% |
| P home draw | 7.4% |
| P draw away | 97.0% |
| Raw p home draw | 6.1% |
| Raw p draw away | 98.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 15.00 |
| Reference draw odds | 13.50 |
| Reference away odds | 1.08 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.13 |
| Reference Under 2.5 odds | 6.00 |
| Home probability edge | -1.1% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | +1.4% |
| Under 2.5 probability edge | -1.4% |
| Raw edge prob home | -0.0211 |
| Raw ev home | -0.4876 |
| Raw edge prob draw | -0.0045 |
| Raw ev draw | -0.3536 |
| Raw edge prob away | 0.0255 |
| Raw ev away | 0.0512 |
| Market p home draw | 12.2% |
| Market home draw odds | 8.60 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T07:41:45Z |
| Market reference home draw last update utc | 2026-10-13T07:43:14Z |
| Market home draw bookmakers | 4 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 94.8% |
| Market draw away odds | 1.03 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:43:14Z |
| Market reference draw away last update utc | 2026-10-13T07:43:14Z |
| Market draw away bookmakers | 4 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 7.98 |
| Market reference dc draw away odds | 1.03 |
| Market reference dc home away odds | 1.05 |
| Market p over 1 5 | 96.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 15.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 31.9% |
| Market under 3 5 odds | 2.95 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference under 3 5 odds | 2.95 |
| Market reference under 3 5 opposite odds | 1.44 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 56.1% |
| Market btts yes odds | 1.84 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.15 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **39.9%**. Expected goals are 0.90 for Villarreal and 1.42 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.6%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 40.4%; Under 3.5 goals: 80.3%; Double Chance 1X: 60.1%; Double Chance X2: 65.1%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 44.3%; BTTS No (at least one team does not score): 55.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 34.9% | 2.86 |
| Draw | 25.2% | 3.97 |
| Napoli win | 39.9% | 2.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.90 |
| Napoli expected goals | 1.42 |
| Expected total goals | 2.31 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 65.7% |
| Under 1.5 | 34.3% |
| Over 2.5 | 40.4% |
| Under 2.5 | 59.6% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.57% |
| 2 | 0-1 | 11.73% |
| 3 | 1-1 | 11.64% |
| 4 | 0-0 | 9.02% |
| 5 | 2-1 | 8.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 34.9% | 45.4% | 2.26 | -21.0% |
| Draw | 25.2% | 24.5% | 3.80 | -4.4% |
| Napoli win | 39.9% | 30.0% | 3.40 | +35.6% |
| Over 2.5 | 40.4% | 60.2% | 1.68 | -32.1% |
| Under 2.5 | 59.6% | 39.8% | 2.38 | +41.9% |

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
| Market best home last update utc | 2026-10-13T07:42:58Z |
| Market best draw last update utc | 2026-10-13T07:41:45Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.3% |
| P btts no | 55.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.08 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.07 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.99 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 44.3% |
| P home draw | 60.1% |
| P draw away | 65.1% |
| Raw p home draw | 50.2% |
| Raw p draw away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | -10.5% |
| Draw probability edge | +0.6% |
| Away probability edge | +9.9% |
| Over 2.5 probability edge | -19.8% |
| Under 2.5 probability edge | +19.8% |
| Raw edge prob home | -0.2099 |
| Raw ev home | -0.4474 |
| Raw edge prob draw | 0.0127 |
| Raw ev draw | -0.0198 |
| Raw edge prob away | 0.1972 |
| Raw ev away | 0.6916 |
| Market p home draw | 70.4% |
| Market home draw odds | 1.37 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T07:41:45Z |
| Market reference home draw last update utc | 2026-10-13T07:43:14Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.9% |
| Market draw away odds | 1.77 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:42:53Z |
| Market reference draw away last update utc | 2026-10-13T07:43:14Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.35 |
| Market reference dc draw away odds | 1.70 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 82.9% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 62.5% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T07:43:12Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.53 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.2% |
| Market btts yes odds | 1.59 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.38 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **50.3%**. Expected goals are 1.18 for AS Roma and 1.67 for Real Madrid (2.86 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 54.5%; Under 3.5 goals: 67.9%; Double Chance 1X: 49.7%; Double Chance X2: 72.9%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 55.6%; BTTS No (at least one team does not score): 44.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 27.1% | 3.69 |
| Draw | 22.6% | 4.42 |
| Real Madrid win | 50.3% | 1.99 |

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
| 1 | 1-1 | 10.62% |
| 2 | 0-1 | 10.36% |
| 3 | 1-2 | 9.68% |
| 4 | 0-2 | 8.19% |
| 5 | 1-0 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 27.1% | 26.7% | 3.88 | +5.2% |
| Draw | 22.6% | 22.2% | 4.20 | -5.0% |
| Real Madrid win | 50.3% | 51.0% | 2.00 | +0.5% |
| Over 2.5 | 54.5% | 67.7% | 1.44 | -21.5% |
| Under 2.5 | 45.5% | 32.3% | 2.88 | +31.0% |

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
| Market best home last update utc | 2026-10-13T07:41:45Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.6% |
| P btts no | 44.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.62 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.40 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.12 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.18 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 27.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 49.5% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.0% |
| Raw p btts yes | 55.7% |
| P home draw | 49.7% |
| P draw away | 72.9% |
| Raw p home draw | 50.5% |
| Raw p draw away | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.45 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.88 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.82 |
| Home probability edge | +0.4% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -13.2% |
| Under 2.5 probability edge | +13.2% |
| Raw edge prob home | 0.0078 |
| Raw ev home | 0.0674 |
| Raw edge prob draw | 0.0078 |
| Raw ev draw | -0.0332 |
| Raw edge prob away | -0.0156 |
| Raw ev away | -0.0106 |
| Market p home draw | 50.1% |
| Market home draw odds | 1.96 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T07:41:45Z |
| Market reference home draw last update utc | 2026-10-13T07:43:15Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.8% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:43:15Z |
| Market reference draw away last update utc | 2026-10-13T07:43:15Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.93 |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 54.4% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T07:38:02Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 67.9% |
| Market btts yes odds | 1.46 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.92 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **67.2%**. Expected goals are 2.23 for Aston Villa and 0.61 for Fenerbahce (2.84 combined). The most likely exact score is 2-0 at 13.1%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 51.9%; Under 3.5 goals: 69.8%; Double Chance 1X: 86.0%; Double Chance X2: 32.8%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 41.4%; BTTS No (at least one team does not score): 58.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 67.2% | 1.49 |
| Draw | 18.8% | 5.33 |
| Fenerbahce win | 14.0% | 7.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.23 |
| Fenerbahce expected goals | 0.61 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.06% |
| 2 | 1-0 | 12.06% |
| 3 | 3-0 | 9.72% |
| 4 | 1-1 | 8.78% |
| 5 | 2-1 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 67.2% | 59.6% | 1.69 | +13.6% |
| Draw | 18.8% | 21.4% | 4.40 | -17.4% |
| Fenerbahce win | 14.0% | 19.0% | 5.50 | -23.1% |
| Over 2.5 | 51.9% | 59.5% | 1.69 | -12.2% |
| Under 2.5 | 48.1% | 40.5% | 2.36 | +13.5% |

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
| Market best home last update utc | 2026-10-13T07:41:45Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
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
| P btts yes | 41.4% |
| P btts no | 58.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.76 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.32 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.72 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.1% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 40.3% |
| P home draw | 86.0% |
| P draw away | 32.8% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.62 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.70 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | +7.7% |
| Draw probability edge | -2.7% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | 0.1533 |
| Raw ev home | 0.2660 |
| Raw edge prob draw | -0.0532 |
| Raw ev draw | -0.2912 |
| Raw edge prob away | -0.1001 |
| Raw ev away | -0.5060 |
| Market p home draw | 80.2% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T07:41:45Z |
| Market reference home draw last update utc | 2026-10-13T07:43:14Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.0% |
| Market draw away odds | 2.35 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:42:53Z |
| Market reference draw away last update utc | 2026-10-13T07:43:14Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.18 |
| Market reference dc draw away odds | 2.15 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.9% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 63.1% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T07:43:12Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 57.4% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-13T07:42:53Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.20 |
| Market btts yes bookmakers | 3 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **45.8%**. Expected goals are 1.73 for Bodø/Glimt and 1.94 for Borussia Dortmund (3.67 combined). The most likely exact score is 1-2 at 8.7%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.0%; Double Chance 1X: 54.2%; Double Chance X2: 67.3%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 70.2%; BTTS No (at least one team does not score): 29.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 32.7% | 3.06 |
| Draw | 21.5% | 4.65 |
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
| 1 | 1-2 | 8.67% |
| 2 | 1-1 | 8.43% |
| 3 | 2-2 | 7.43% |
| 4 | 2-1 | 6.83% |
| 5 | 0-1 | 5.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 32.7% | 30.0% | 3.30 | +8.0% |
| Draw | 21.5% | 22.2% | 4.25 | -8.6% |
| Borussia Dortmund win | 45.8% | 47.8% | 2.16 | -1.1% |
| Over 2.5 | 70.7% | 69.8% | 1.40 | -1.0% |
| Under 2.5 | 29.3% | 30.2% | 3.03 | -11.3% |

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
| Market best home last update utc | 2026-10-13T07:42:58Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
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
| Fair Under 0.5 odds | 45.39 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.13 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.42 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.27 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 35.5% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 43.8% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 50.1% |
| Raw p btts yes | 70.0% |
| P home draw | 54.2% |
| P draw away | 67.3% |
| Raw p home draw | 56.2% |
| Raw p draw away | 64.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.10 |
| Reference draw odds | 4.10 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +2.8% |
| Draw probability edge | -0.7% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.0554 |
| Raw ev home | 0.1715 |
| Raw edge prob draw | -0.0150 |
| Raw ev draw | -0.1182 |
| Raw edge prob away | -0.0404 |
| Raw ev away | -0.0550 |
| Market p home draw | 53.8% |
| Market home draw odds | 1.81 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T07:42:53Z |
| Market reference home draw last update utc | 2026-10-13T07:43:14Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.8% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T07:41:45Z |
| Market reference draw away last update utc | 2026-10-13T07:43:14Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.75 |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T07:40:16Z |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 1.98 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 69.7% |
| Market btts yes odds | 1.42 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:43:27Z |
| Market reference btts yes odds | 1.42 |
| Market reference btts yes opposite odds | 3.20 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **62.0%**. Expected goals are 1.82 for Feyenoord and 3.81 for Como (5.63 combined). The most likely exact score is 2-2 at 6.0%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 90.9%; Under 3.5 goals: 19.8%; Double Chance 1X: 38.0%; Double Chance X2: 78.9%; Under 4.5 goals: 35.8%; BTTS Yes (both teams score): 83.3%; BTTS No (at least one team does not score): 16.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 21.1% | 4.75 |
| Draw | 16.9% | 5.92 |
| Como win | 62.0% | 1.61 |

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
| Over 3.5 | 80.2% |
| Under 3.5 | 19.8% |
| Over 4.5 | 64.2% |
| Under 4.5 | 35.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 5.99% |
| 2 | 1-3 | 5.08% |
| 3 | 1-4 | 4.84% |
| 4 | 2-3 | 4.62% |
| 5 | 3-3 | 4.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 21.1% | 28.0% | 3.75 | -21.0% |
| Draw | 16.9% | 21.6% | 4.40 | -25.7% |
| Como win | 62.0% | 50.4% | 1.98 | +22.8% |
| Over 2.5 | 90.9% | 67.9% | 1.43 | +30.0% |
| Under 2.5 | 9.1% | 32.1% | 2.87 | -73.9% |

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
| Market best home last update utc | 2026-10-13T07:42:58Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:41:45Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
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
| Fair Under 0.5 odds | 307.23 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 36.53 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.99 |
| Fair Over 3.5 odds | 1.25 |
| Fair Under 3.5 odds | 5.05 |
| Fair Over 4.5 odds | 1.56 |
| Fair Under 4.5 odds | 2.79 |
| Unadjusted home-win probability | 14.2% |
| Unadjusted draw probability | 12.2% |
| Unadjusted away-win probability | 73.7% |
| Raw p over 1 5 | 97.5% |
| Raw p under 3 5 | 18.8% |
| Raw p btts yes | 81.8% |
| P home draw | 38.0% |
| P draw away | 78.9% |
| Raw p home draw | 26.3% |
| Raw p draw away | 85.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.30 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.90 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.85 |
| Home probability edge | -6.9% |
| Draw probability edge | -4.7% |
| Away probability edge | +11.6% |
| Over 2.5 probability edge | +23.0% |
| Under 2.5 probability edge | -23.0% |
| Raw edge prob home | -0.1380 |
| Raw ev home | -0.4687 |
| Raw edge prob draw | -0.0946 |
| Raw ev draw | -0.4648 |
| Raw edge prob away | 0.2326 |
| Raw ev away | 0.4586 |
| Market p home draw | 49.6% |
| Market home draw odds | 1.92 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T07:41:45Z |
| Market reference home draw last update utc | 2026-10-13T07:43:14Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.8% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T07:41:45Z |
| Market reference draw away last update utc | 2026-10-13T07:43:14Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.91 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 54.5% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T07:41:49Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.11 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 68.9% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.88 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **73.0%**. Expected goals are 0.28 for LASK and 1.45 for Liverpool (1.74 combined). The most likely exact score is 0-1 at 28.0%. Goal-market probabilities: at least one goal: 87.1%; Over 2.5 goals: 27.0%; Under 3.5 goals: 89.6%; Double Chance 1X: 27.0%; Double Chance X2: 91.6%; Under 4.5 goals: 96.6%; BTTS Yes (both teams score): 17.4%; BTTS No (at least one team does not score): 82.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 8.4% | 11.91 |
| Draw | 18.6% | 5.39 |
| Liverpool win | 73.0% | 1.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.28 |
| Liverpool expected goals | 1.45 |
| Expected total goals | 1.74 |
| Over 0.5 | 87.1% |
| Under 0.5 | 12.9% |
| Over 1.5 | 53.0% |
| Under 1.5 | 47.0% |
| Over 2.5 | 27.0% |
| Under 2.5 | 73.0% |
| Over 3.5 | 10.4% |
| Under 3.5 | 89.6% |
| Over 4.5 | 3.4% |
| Under 4.5 | 96.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 27.98% |
| 2 | 0-2 | 20.07% |
| 3 | 0-0 | 12.87% |
| 4 | 0-3 | 9.73% |
| 5 | 1-0 | 6.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 8.4% | 9.5% | 10.50 | -11.8% |
| Draw | 18.6% | 12.3% | 6.75 | +25.3% |
| Liverpool win | 73.0% | 78.2% | 1.31 | -4.3% |
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
| Market best home last update utc | 2026-10-13T07:42:58Z |
| Market best draw last update utc | 2026-10-13T07:43:00Z |
| Market best away last update utc | 2026-10-13T07:41:45Z |
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
| P btts yes | 17.4% |
| P btts no | 82.6% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.77 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.13 |
| Fair Over 2.5 odds | 3.70 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.63 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 29.08 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 7.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 67.8% |
| Raw p over 1 5 | 51.4% |
| Raw p under 3 5 | 90.1% |
| Raw p btts yes | 18.5% |
| P home draw | 27.0% |
| P draw away | 91.6% |
| Raw p home draw | 32.2% |
| Raw p draw away | 92.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 8.50 |
| Reference draw odds | 6.75 |
| Reference away odds | 1.25 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.15 |
| Home probability edge | -1.1% |
| Draw probability edge | +6.3% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | -44.4% |
| Under 2.5 probability edge | +44.4% |
| Raw edge prob home | -0.0222 |
| Raw ev home | -0.2348 |
| Raw edge prob draw | 0.1264 |
| Raw ev draw | 0.6798 |
| Raw edge prob away | -0.1042 |
| Raw ev away | -0.1115 |
| Market p home draw | 24.5% |
| Market home draw odds | 3.97 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T07:43:14Z |
| Market reference home draw last update utc | 2026-10-13T07:43:14Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.1% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:43:14Z |
| Market reference draw away last update utc | 2026-10-13T07:43:14Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.97 |
| Market reference dc draw away odds | 1.08 |
| Market reference dc home away odds | 1.14 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 51.0% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T07:38:46Z |
| Market reference under 3 5 odds | 1.90 |
| Market reference under 3 5 opposite odds | 1.97 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 55.5% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:42:59Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.14 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **44.7%**. Expected goals are 1.40 for Manchester City and 2.23 for Paris Saint Germain (3.63 combined). The most likely exact score is 1-1 at 8.4%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 69.3%; Under 3.5 goals: 51.9%; Double Chance 1X: 55.3%; Double Chance X2: 65.4%; Under 4.5 goals: 70.9%; BTTS Yes (both teams score): 67.7%; BTTS No (at least one team does not score): 32.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 34.6% | 2.89 |
| Draw | 20.7% | 4.83 |
| Paris Saint Germain win | 44.7% | 2.24 |

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
| 1 | 1-1 | 8.43% |
| 2 | 2-1 | 8.36% |
| 3 | 1-2 | 7.27% |
| 4 | 2-2 | 6.94% |
| 5 | 1-0 | 5.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 34.6% | 45.2% | 2.24 | -22.4% |
| Draw | 20.7% | 22.1% | 4.20 | -13.0% |
| Paris Saint Germain win | 44.7% | 32.6% | 3.15 | +40.7% |
| Over 2.5 | 69.3% | 67.2% | 1.45 | +0.5% |
| Under 2.5 | 30.7% | 32.8% | 2.80 | -14.1% |

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
| Market best home last update utc | 2026-10-13T07:41:45Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
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
| Fair Under 0.5 odds | 41.78 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.51 |
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
| P home draw | 55.3% |
| P draw away | 65.4% |
| Raw p home draw | 43.3% |
| Raw p draw away | 76.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.10 |
| Reference draw odds | 4.10 |
| Reference away odds | 2.85 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.78 |
| Home probability edge | -10.6% |
| Draw probability edge | -1.4% |
| Away probability edge | +12.0% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | -0.2122 |
| Raw ev home | -0.4619 |
| Raw edge prob draw | -0.0283 |
| Raw ev draw | -0.1895 |
| Raw edge prob away | 0.2404 |
| Raw ev away | 0.7854 |
| Market p home draw | 67.6% |
| Market home draw odds | 1.43 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T07:41:45Z |
| Market reference home draw last update utc | 2026-10-13T07:43:14Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.7% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T07:41:45Z |
| Market reference draw away last update utc | 2026-10-13T07:43:14Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.40 |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 55.3% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T07:42:35Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.14 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 66.8% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:43:27Z |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.92 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **61.4%**. Expected goals are 3.29 for Real Betis and 1.29 for Porto (4.58 combined). The most likely exact score is 2-2 at 6.8%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 81.1%; Under 3.5 goals: 35.2%; Double Chance 1X: 79.7%; Double Chance X2: 38.6%; Under 4.5 goals: 54.7%; BTTS Yes (both teams score): 72.1%; BTTS No (at least one team does not score): 27.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 61.4% | 1.63 |
| Draw | 18.3% | 5.45 |
| Porto win | 20.3% | 4.93 |

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
| Over 2.5 | 81.1% |
| Under 2.5 | 18.9% |
| Over 3.5 | 64.8% |
| Under 3.5 | 35.2% |
| Over 4.5 | 45.3% |
| Under 4.5 | 54.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.82% |
| 2 | 3-1 | 6.33% |
| 3 | 1-1 | 6.09% |
| 4 | 2-1 | 5.77% |
| 5 | 4-1 | 5.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 61.4% | 46.7% | 2.16 | +32.6% |
| Draw | 18.3% | 24.2% | 3.90 | -28.5% |
| Porto win | 20.3% | 29.1% | 3.70 | -25.0% |
| Over 2.5 | 81.1% | 57.0% | 1.79 | +45.2% |
| Under 2.5 | 18.9% | 43.0% | 2.19 | -58.6% |

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
| Market best home last update utc | 2026-10-13T07:41:45Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:42:58Z |
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
| P btts yes | 72.1% |
| P btts no | 27.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 84.13 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.69 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.30 |
| Fair Over 3.5 odds | 1.54 |
| Fair Under 3.5 odds | 2.84 |
| Fair Over 4.5 odds | 2.21 |
| Fair Under 4.5 odds | 1.83 |
| Unadjusted home-win probability | 76.1% |
| Unadjusted draw probability | 12.4% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 94.1% |
| Raw p under 3 5 | 32.9% |
| Raw p btts yes | 69.6% |
| P home draw | 79.7% |
| P draw away | 38.6% |
| Raw p home draw | 88.6% |
| Raw p draw away | 23.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | +14.7% |
| Draw probability edge | -5.9% |
| Away probability edge | -8.8% |
| Over 2.5 probability edge | +24.1% |
| Under 2.5 probability edge | -24.1% |
| Raw edge prob home | 0.2944 |
| Raw ev home | 0.6441 |
| Raw edge prob draw | -0.1180 |
| Raw ev draw | -0.5150 |
| Raw edge prob away | -0.1764 |
| Raw ev away | -0.5764 |
| Market p home draw | 72.2% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T07:41:45Z |
| Market reference home draw last update utc | 2026-10-13T07:43:16Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.9% |
| Market draw away odds | 1.83 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:43:16Z |
| Market reference draw away last update utc | 2026-10-13T07:43:16Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.2% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 66.1% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.74 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 59.3% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:43:27Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.42 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **40.1%**. Expected goals are 1.49 for Shakhtar Donetsk and 1.25 for AEK Athens (2.74 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 51.0%; Under 3.5 goals: 70.6%; Double Chance 1X: 66.0%; Double Chance X2: 59.9%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 40.1% | 2.49 |
| Draw | 25.9% | 3.86 |
| AEK Athens win | 34.0% | 2.94 |

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
| 1 | 1-1 | 12.24% |
| 2 | 1-0 | 9.46% |
| 3 | 0-1 | 9.08% |
| 4 | 2-1 | 8.29% |
| 5 | 1-2 | 7.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 40.1% | 36.9% | 2.76 | +10.6% |
| Draw | 25.9% | 27.6% | 3.55 | -8.0% |
| AEK Athens win | 34.0% | 35.4% | 2.77 | -5.8% |
| Over 2.5 | 51.0% | 51.8% | 1.95 | -0.5% |
| Under 2.5 | 49.0% | 48.2% | 2.02 | -1.1% |

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
| Market best home last update utc | 2026-10-13T07:42:58Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:41:45Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 67/100 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.94 |
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
| P home draw | 66.0% |
| P draw away | 59.9% |
| Raw p home draw | 67.4% |
| Raw p draw away | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.55 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.98 |
| Home probability edge | +3.2% |
| Draw probability edge | -1.7% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | 0.0631 |
| Raw ev home | 0.1934 |
| Raw edge prob draw | -0.0343 |
| Raw ev draw | -0.1410 |
| Raw edge prob away | -0.0288 |
| Raw ev away | -0.0979 |
| Market p home draw | 64.1% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-13T07:41:45Z |
| Market reference home draw last update utc | 2026-10-13T07:43:32Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.1% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-13T07:41:45Z |
| Market reference draw away last update utc | 2026-10-13T07:43:32Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.50 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 77.6% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 3.56 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 73.0% |
| Market under 3 5 odds | 1.37 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-13T07:43:12Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.08 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 56.3% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:43:27Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.26 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **66.4%**. Expected goals are 1.46 for ŠK Slovan Bratislava and 2.25 for VfB Stuttgart (3.71 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 72.8%; Under 3.5 goals: 48.5%; Double Chance 1X: 33.6%; Double Chance X2: 82.8%; Under 4.5 goals: 67.6%; BTTS Yes (both teams score): 67.1%; BTTS No (at least one team does not score): 32.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.2% | 5.81 |
| Draw | 16.3% | 6.12 |
| VfB Stuttgart win | 66.4% | 1.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.46 |
| VfB Stuttgart expected goals | 2.25 |
| Expected total goals | 3.71 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 72.8% |
| Under 2.5 | 27.2% |
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
| 5 | 1-1 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.2% | 9.6% | 11.00 | +89.3% |
| Draw | 16.3% | 13.4% | 6.60 | +7.9% |
| VfB Stuttgart win | 66.4% | 77.0% | 1.31 | -13.0% |
| Over 2.5 | 72.8% | 72.5% | 1.35 | -1.8% |
| Under 2.5 | 27.2% | 27.5% | 3.26 | -11.2% |

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
| Market best home last update utc | 2026-10-13T07:42:59Z |
| Market best draw last update utc | 2026-10-13T07:42:58Z |
| Market best away last update utc | 2026-10-13T07:41:45Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.1% |
| P btts no | 32.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 57.31 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.65 |
| Fair Over 2.5 odds | 1.37 |
| Fair Under 2.5 odds | 3.67 |
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
| P home draw | 33.6% |
| P draw away | 82.8% |
| Raw p home draw | 44.1% |
| Raw p draw away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 8.50 |
| Reference draw odds | 6.25 |
| Reference away odds | 1.27 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.25 |
| Home probability edge | +7.6% |
| Draw probability edge | +2.9% |
| Away probability edge | -10.5% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.1522 |
| Raw ev home | 1.7297 |
| Raw edge prob draw | 0.0582 |
| Raw ev draw | 0.2708 |
| Raw edge prob away | -0.2104 |
| Raw ev away | -0.2673 |
| Market p home draw | 25.4% |
| Market home draw odds | 3.82 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-13T07:42:53Z |
| Market reference home draw last update utc | 2026-10-13T07:43:32Z |
| Market home draw bookmakers | 5 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.1% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-13T07:42:53Z |
| Market reference draw away last update utc | 2026-10-13T07:43:32Z |
| Market draw away bookmakers | 5 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.80 |
| Market reference dc draw away odds | 1.07 |
| Market reference dc home away odds | 1.14 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-13T07:42:59Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 49.9% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-13T07:41:27Z |
| Market reference under 3 5 odds | 1.94 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 57.6% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-13T07:43:27Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.32 |
| Market btts yes bookmakers | 4 |

</details>


---
