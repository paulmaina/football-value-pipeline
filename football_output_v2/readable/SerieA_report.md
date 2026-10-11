# Serie A — football model report

Fixtures in this report: **17**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,190 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 879.078 |
| Base scoring parameter | 0.134 |
| Home-advantage parameter | 0.091 |
| Dixon-Coles low-score adjustment | 0.005 |
| Xi per day | 0.0029 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 17.00 |
| Additional event odds calls used before this league | 12.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-11 — Cagliari vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **57.9%**. Expected goals are 0.80 for Cagliari and 1.48 for Juventus (2.28 combined). The most likely exact score is 0-1 at 16.5%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 40.6%; Under 3.5 goals: 80.0%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 41.9%; BTTS No (at least one team does not score): 58.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 17.2% | 5.80 |
| Draw | 24.8% | 4.03 |
| Juventus win | 57.9% | 1.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 0.80 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.6% |
| Under 2.5 | 59.4% |
| Over 3.5 | 20.0% |
| Under 3.5 | 80.0% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.49% |
| 2 | 0-2 | 12.18% |
| 3 | 1-1 | 11.36% |
| 4 | 1-2 | 9.70% |
| 5 | 0-0 | 9.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 17.2% | 14.3% | 7.20 | +24.1% |
| Draw | 24.8% | 23.4% | 4.17 | +3.5% |
| Juventus win | 57.9% | 62.3% | 1.61 | -6.7% |
| Over 2.5 | 40.6% | 47.4% | 2.10 | -14.8% |
| Under 2.5 | 59.4% | 52.6% | 1.88 | +11.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T18:45:00+00:00 |
| Fixture id | 407f7d03157d1dfad384876e6a6bc910 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:59Z |
| Market best draw last update utc | 2026-10-11T08:22:54Z |
| Market best away last update utc | 2026-10-11T08:22:54Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.9% |
| P btts no | 58.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.41 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.46 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 4.99 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.94 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 53.6% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.3% |
| Raw p btts yes | 42.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 6.40 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.57 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +2.9% |
| Draw probability edge | +1.4% |
| Away probability edge | -4.4% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
| Raw edge prob home | 0.0589 |
| Raw ev home | 0.4531 |
| Raw edge prob draw | 0.0286 |
| Raw ev draw | 0.0946 |
| Raw edge prob away | -0.0876 |
| Raw ev away | -0.1375 |

</details>


---

## 2026-10-11 — Como vs AS Roma

The model's most likely 1X2 outcome is **Como win** at **36.7%**. Expected goals are 1.17 for Como and 1.30 for AS Roma (2.47 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 44.9%; Under 3.5 goals: 76.4%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 36.7% | 2.73 |
| Draw | 26.9% | 3.72 |
| AS Roma win | 36.4% | 2.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 1.17 |
| AS Roma expected goals | 1.30 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 70.6% |
| Under 1.5 | 29.4% |
| Over 2.5 | 44.9% |
| Under 2.5 | 55.1% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.76% |
| 2 | 1-0 | 10.90% |
| 3 | 0-1 | 10.16% |
| 4 | 0-0 | 8.34% |
| 5 | 2-1 | 8.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 36.7% | 39.8% | 2.52 | -7.6% |
| Draw | 26.9% | 26.8% | 3.65 | -1.8% |
| AS Roma win | 36.4% | 33.4% | 3.10 | +12.9% |
| Over 2.5 | 44.9% | 58.7% | 1.71 | -23.2% |
| Under 2.5 | 55.1% | 41.3% | 2.35 | +29.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T10:30:00+00:00 |
| Fixture id | 2547c0dbddd26d23fa532228e36348cb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:54Z |
| Market best draw last update utc | 2026-10-11T08:22:54Z |
| Market best away last update utc | 2026-10-11T08:23:11Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Tipico |
| Matched home-team name | Como |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.2% |
| P btts no | 49.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.99 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.40 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.23 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.51 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 33.6% |
| Unadjusted draw probability | 27.0% |
| Unadjusted away-win probability | 39.5% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.3% |
| Raw p btts yes | 50.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.43 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.88 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -3.1% |
| Draw probability edge | +0.1% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -13.8% |
| Under 2.5 probability edge | +13.8% |
| Raw edge prob home | -0.0624 |
| Raw ev home | -0.1545 |
| Raw edge prob draw | 0.0012 |
| Raw ev draw | -0.0155 |
| Raw edge prob away | 0.0612 |
| Raw ev away | 0.2238 |

</details>


---

## 2026-10-11 — Lazio vs Monza

The model's most likely 1X2 outcome is **Lazio win** at **61.4%**. Expected goals are 2.01 for Lazio and 0.87 for Monza (2.88 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 54.2%; Under 3.5 goals: 67.8%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 61.4% | 1.63 |
| Draw | 22.1% | 4.53 |
| Monza win | 16.6% | 6.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 2.01 |
| Monza expected goals | 0.87 |
| Expected total goals | 2.88 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 54.2% |
| Under 2.5 | 45.8% |
| Over 3.5 | 32.2% |
| Under 3.5 | 67.8% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.90% |
| 2 | 1-0 | 10.88% |
| 3 | 1-1 | 10.48% |
| 4 | 2-1 | 9.44% |
| 5 | 3-0 | 7.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 61.4% | 58.6% | 1.75 | +7.4% |
| Draw | 22.1% | 23.6% | 4.05 | -10.7% |
| Monza win | 16.6% | 17.8% | 5.50 | -8.9% |
| Over 2.5 | 54.2% | 52.3% | 1.86 | +0.7% |
| Under 2.5 | 45.8% | 47.7% | 2.16 | -1.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | c0f72699f32ec193b64fd54092fe268d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:58Z |
| Market best draw last update utc | 2026-10-11T08:22:54Z |
| Market best away last update utc | 2026-10-11T08:22:58Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Lazio |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.69 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.51 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.20 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 64.1% |
| Unadjusted draw probability | 20.5% |
| Unadjusted away-win probability | 15.4% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 67.5% |
| Raw p btts yes | 50.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.67 |
| Reference draw odds | 4.00 |
| Reference away odds | 5.25 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | +2.8% |
| Draw probability edge | -1.5% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | 0.0551 |
| Raw ev home | 0.1222 |
| Raw edge prob draw | -0.0309 |
| Raw ev draw | -0.1694 |
| Raw edge prob away | -0.0242 |
| Raw ev away | -0.1549 |

</details>


---

## 2026-10-11 — Lecce vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **50.5%**. Expected goals are 0.78 for Lecce and 1.33 for Bologna (2.11 combined). The most likely exact score is 0-1 at 16.4%. Goal-market probabilities: at least one goal: 88.1%; Over 2.5 goals: 35.5%; Under 3.5 goals: 83.6%; Under 4.5 goals: 93.6%; BTTS Yes (both teams score): 39.8%; BTTS No (at least one team does not score): 60.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 21.5% | 4.64 |
| Draw | 28.0% | 3.57 |
| Bologna win | 50.5% | 1.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.78 |
| Bologna expected goals | 1.33 |
| Expected total goals | 2.11 |
| Over 0.5 | 88.1% |
| Under 0.5 | 11.9% |
| Over 1.5 | 62.4% |
| Under 1.5 | 37.6% |
| Over 2.5 | 35.5% |
| Under 2.5 | 64.5% |
| Over 3.5 | 16.4% |
| Under 3.5 | 83.6% |
| Over 4.5 | 6.4% |
| Under 4.5 | 93.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.39% |
| 2 | 1-1 | 12.41% |
| 3 | 0-0 | 11.93% |
| 4 | 0-2 | 10.87% |
| 5 | 1-0 | 9.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 21.5% | 21.1% | 4.50 | -3.1% |
| Draw | 28.0% | 27.7% | 3.45 | -3.5% |
| Bologna win | 50.5% | 51.2% | 2.08 | +5.0% |
| Over 2.5 | 35.5% | 44.4% | 2.28 | -19.1% |
| Under 2.5 | 64.5% | 55.6% | 1.76 | +13.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | 946716d7e5e52822f08be8cb95193d9d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:38Z |
| Market best draw last update utc | 2026-10-11T08:22:38Z |
| Market best away last update utc | 2026-10-11T08:22:54Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 39.8% |
| P btts no | 60.2% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.38 |
| Fair Over 1.5 odds | 1.60 |
| Fair Under 1.5 odds | 2.66 |
| Fair Over 2.5 odds | 2.82 |
| Fair Under 2.5 odds | 1.55 |
| Fair Over 3.5 odds | 6.09 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.71 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 22.0% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 49.8% |
| Raw p over 1 5 | 62.3% |
| Raw p under 3 5 | 83.6% |
| Raw p btts yes | 39.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 4.50 |
| Reference draw odds | 3.45 |
| Reference away odds | 1.91 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.71 |
| Home probability edge | +0.5% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | 0.0094 |
| Raw ev home | -0.0094 |
| Raw edge prob draw | 0.0046 |
| Raw ev draw | -0.0268 |
| Raw edge prob away | -0.0140 |
| Raw ev away | 0.0354 |
| Market p over 1 5 | 70.5% |
| Market over 1 5 odds | 1.42 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:22:56Z |
| Market reference over 1 5 odds | 1.39 |
| Market reference over 1 5 opposite odds | 3.17 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 78.3% |
| Market under 3 5 odds | 1.26 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T08:22:56Z |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 4.25 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 49.0% |
| Market btts yes odds | 1.98 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:23:11Z |
| Market reference btts yes odds | 1.97 |
| Market reference btts yes opposite odds | 1.90 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-11 — Sassuolo vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **51.9%**. Expected goals are 1.13 for Sassuolo and 1.68 for AC Milan (2.81 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 53.3%; Under 3.5 goals: 68.8%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 23.6% | 4.24 |
| Draw | 24.5% | 4.08 |
| AC Milan win | 51.9% | 1.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.13 |
| AC Milan expected goals | 1.68 |
| Expected total goals | 2.81 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 53.3% |
| Under 2.5 | 46.7% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.60% |
| 2 | 0-1 | 10.47% |
| 3 | 1-2 | 9.90% |
| 4 | 0-2 | 8.76% |
| 5 | 1-0 | 6.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 23.6% | 21.5% | 4.50 | +6.0% |
| Draw | 24.5% | 25.0% | 3.90 | -4.3% |
| AC Milan win | 51.9% | 53.4% | 1.91 | -0.8% |
| Over 2.5 | 53.3% | 54.5% | 1.81 | -3.5% |
| Under 2.5 | 46.7% | 45.5% | 2.25 | +5.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T16:00:00+00:00 |
| Fixture id | 1cf64166dda1e0da8b325161deb39662 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:59Z |
| Market best draw last update utc | 2026-10-11T08:22:54Z |
| Market best away last update utc | 2026-10-11T08:22:54Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | BetAnything |
| Matched home-team name | Sassuolo |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.49 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.48 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 25.6% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 50.4% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 68.9% |
| Raw p btts yes | 55.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 4.40 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.83 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.05 |
| Home probability edge | +2.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -1.2% |
| Under 2.5 probability edge | +1.2% |
| Raw edge prob home | 0.0409 |
| Raw ev home | 0.1522 |
| Raw edge prob draw | -0.0104 |
| Raw ev draw | -0.0637 |
| Raw edge prob away | -0.0305 |
| Raw ev away | -0.0376 |

</details>


---

## 2026-10-12 — Atalanta BC vs Venezia

The model's most likely 1X2 outcome is **Atalanta BC win** at **68.8%**. Expected goals are 2.35 for Atalanta BC and 0.66 for Venezia (3.02 combined). The most likely exact score is 2-0 at 12.4%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.2%; Under 3.5 goals: 65.7%; Under 4.5 goals: 82.2%; BTTS Yes (both teams score): 44.9%; BTTS No (at least one team does not score): 55.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 68.8% | 1.45 |
| Draw | 18.5% | 5.40 |
| Venezia win | 12.7% | 7.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.35 |
| Venezia expected goals | 0.66 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 79.0% |
| Under 1.5 | 21.0% |
| Over 2.5 | 56.2% |
| Under 2.5 | 43.8% |
| Over 3.5 | 34.3% |
| Under 3.5 | 65.7% |
| Over 4.5 | 17.8% |
| Under 4.5 | 82.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.42% |
| 2 | 1-0 | 10.58% |
| 3 | 3-0 | 9.75% |
| 4 | 1-1 | 8.79% |
| 5 | 2-1 | 8.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 68.8% | 62.2% | 1.63 | +12.1% |
| Draw | 18.5% | 21.1% | 4.40 | -18.5% |
| Venezia win | 12.7% | 16.7% | 6.20 | -21.4% |
| Over 2.5 | 56.2% | 62.2% | 1.55 | -12.9% |
| Under 2.5 | 43.8% | 37.8% | 2.48 | +8.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-12T16:30:00+00:00 |
| Fixture id | 0f2e7ff90b994f31d5cd48a9680943e1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:54Z |
| Market best draw last update utc | 2026-10-11T08:22:38Z |
| Market best away last update utc | 2026-10-11T08:22:59Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Atalanta |
| Matched away-team name | Venezia |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 44.9% |
| P btts no | 55.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.73 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.76 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.62 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 75.3% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 8.7% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 64.4% |
| Raw p btts yes | 43.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.57 |
| Reference draw odds | 4.40 |
| Reference away odds | 5.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | +6.5% |
| Draw probability edge | -2.6% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | 0.1309 |
| Raw ev home | 0.2280 |
| Raw edge prob draw | -0.0510 |
| Raw ev draw | -0.2971 |
| Raw edge prob away | -0.0799 |
| Raw ev away | -0.4615 |

</details>


---

## 2026-10-12 — Torino vs Udinese

The model's most likely 1X2 outcome is **Torino win** at **38.0%**. Expected goals are 1.29 for Torino and 1.35 for Udinese (2.64 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.6%; Under 3.5 goals: 72.8%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 54.0%; BTTS No (at least one team does not score): 46.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 38.0% | 2.63 |
| Draw | 27.5% | 3.63 |
| Udinese win | 34.4% | 2.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.29 |
| Udinese expected goals | 1.35 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.6% |
| Under 2.5 | 51.4% |
| Over 3.5 | 27.2% |
| Under 3.5 | 72.8% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.09% |
| 2 | 1-0 | 9.91% |
| 3 | 0-1 | 8.71% |
| 4 | 2-1 | 8.56% |
| 5 | 1-2 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 38.0% | 40.4% | 2.46 | -6.4% |
| Draw | 27.5% | 29.1% | 3.35 | -7.7% |
| Udinese win | 34.4% | 30.5% | 3.40 | +17.0% |
| Over 2.5 | 48.6% | 44.6% | 2.24 | +8.9% |
| Under 2.5 | 51.4% | 55.4% | 1.79 | -8.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-12T18:45:00+00:00 |
| Fixture id | f4a28510bb0c835280a2aca709c19d50 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:59Z |
| Market best draw last update utc | 2026-10-11T08:22:54Z |
| Market best away last update utc | 2026-10-11T08:22:59Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Torino |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.0% |
| P btts no | 46.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.35 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.68 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.92 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 38.3% |
| Raw p over 1 5 | 73.9% |
| Raw p under 3 5 | 72.7% |
| Raw p btts yes | 53.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.40 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.71 |
| Home probability edge | -2.4% |
| Draw probability edge | -1.5% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | +4.0% |
| Under 2.5 probability edge | -4.0% |
| Raw edge prob home | -0.0476 |
| Raw ev home | -0.1228 |
| Raw edge prob draw | -0.0306 |
| Raw ev draw | -0.1285 |
| Raw edge prob away | 0.0782 |
| Raw ev away | 0.3031 |

</details>


---

## 2026-10-16 — Frosinone vs Sassuolo

The model's most likely 1X2 outcome is **Frosinone win** at **46.5%**. Expected goals are 1.84 for Frosinone and 1.12 for Sassuolo (2.95 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 55.5%; Under 3.5 goals: 66.5%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 46.5% | 2.15 |
| Draw | 24.8% | 4.03 |
| Sassuolo win | 28.7% | 3.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.84 |
| Sassuolo expected goals | 1.12 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 78.8% |
| Under 1.5 | 21.2% |
| Over 2.5 | 55.5% |
| Under 2.5 | 44.5% |
| Over 3.5 | 33.5% |
| Under 3.5 | 66.5% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.63% |
| 2 | 2-1 | 8.42% |
| 3 | 1-0 | 8.26% |
| 4 | 2-0 | 7.54% |
| 5 | 1-2 | 7.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 46.5% | 38.7% | 2.53 | +17.6% |
| Draw | 24.8% | 26.9% | 3.80 | -5.7% |
| Sassuolo win | 28.7% | 34.4% | 2.96 | -15.0% |
| Over 2.5 | 55.5% | 59.6% | 1.62 | -10.0% |
| Under 2.5 | 44.5% | 40.4% | 2.61 | +16.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-16T18:45:00+00:00 |
| Fixture id | 7d3160040958fe21778fd5ee485666c3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:54Z |
| Market best draw last update utc | 2026-10-11T08:22:59Z |
| Market best away last update utc | 2026-10-11T08:22:54Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Unibet (SE) |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.73 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.71 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 2.98 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.85 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.3% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 79.3% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.50 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.80 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +7.8% |
| Draw probability edge | -2.1% |
| Away probability edge | -5.7% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | 0.1556 |
| Raw ev home | 0.3726 |
| Raw edge prob draw | -0.0419 |
| Raw ev draw | -0.1367 |
| Raw edge prob away | -0.1138 |
| Raw ev away | -0.3183 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **71.9%**. Expected goals are 2.01 for AS Roma and 0.66 for Genoa (2.67 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 50.6%; Under 3.5 goals: 71.7%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 41.3%; BTTS No (at least one team does not score): 58.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 71.9% | 1.39 |
| Draw | 18.2% | 5.50 |
| Genoa win | 9.9% | 10.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 2.01 |
| Genoa expected goals | 0.66 |
| Expected total goals | 2.67 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 75.0% |
| Under 1.5 | 25.0% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 28.3% |
| Under 3.5 | 71.7% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.54% |
| 2 | 2-0 | 14.54% |
| 3 | 3-0 | 9.72% |
| 4 | 2-1 | 9.62% |
| 5 | 1-1 | 8.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 71.9% | 74.8% | 1.36 | -2.2% |
| Draw | 18.2% | 16.7% | 5.70 | +3.6% |
| Genoa win | 9.9% | 8.5% | 10.50 | +4.0% |
| Over 2.5 | 50.6% | 58.7% | 1.72 | -12.9% |
| Under 2.5 | 49.4% | 41.3% | 2.31 | +14.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | 18d478f469da3bcc654dd4555b85c7e3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:54Z |
| Market best draw last update utc | 2026-10-11T08:22:37Z |
| Market best away last update utc | 2026-10-11T08:23:12Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.3% |
| P btts no | 58.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.65 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.00 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.53 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.38 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 11.3% |
| Raw p over 1 5 | 74.5% |
| Raw p under 3 5 | 72.1% |
| Raw p btts yes | 41.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.32 |
| Reference draw odds | 5.50 |
| Reference away odds | 10.50 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -2.8% |
| Draw probability edge | +1.4% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | -0.0565 |
| Raw ev home | -0.0603 |
| Raw edge prob draw | 0.0285 |
| Raw ev draw | 0.1172 |
| Raw edge prob away | 0.0280 |
| Raw ev away | 0.1866 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **60.8%**. Expected goals are 1.07 for Bologna and 2.13 for Inter Milan (3.21 combined). The most likely exact score is 1-1 at 9.8%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.2%; Under 4.5 goals: 78.2%; BTTS Yes (both teams score): 58.3%; BTTS No (at least one team does not score): 41.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.8% | 5.60 |
| Draw | 21.4% | 4.68 |
| Inter Milan win | 60.8% | 1.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.07 |
| Inter Milan expected goals | 2.13 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 61.7% |
| Under 2.5 | 38.3% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.8% |
| Under 4.5 | 78.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.81% |
| 2 | 1-2 | 9.75% |
| 3 | 0-2 | 9.09% |
| 4 | 0-1 | 8.57% |
| 5 | 1-3 | 6.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.8% | 17.4% | 5.70 | +1.7% |
| Draw | 21.4% | 22.6% | 4.20 | -10.3% |
| Inter Milan win | 60.8% | 59.9% | 1.69 | +2.7% |
| Over 2.5 | 61.7% | 56.4% | 1.72 | +6.1% |
| Under 2.5 | 38.3% | 43.6% | 2.30 | -11.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:00:00+00:00 |
| Fixture id | bfefc309177723410230fee52f650315 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:37Z |
| Market best draw last update utc | 2026-10-11T08:23:12Z |
| Market best away last update utc | 2026-10-11T08:22:54Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bologna |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.3% |
| P btts no | 41.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.49 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.84 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.58 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 61.7% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 57.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 5.40 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.64 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | +0.4% |
| Draw probability edge | -1.3% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | +5.3% |
| Under 2.5 probability edge | -5.3% |
| Raw edge prob home | 0.0080 |
| Raw ev home | 0.0399 |
| Raw edge prob draw | -0.0254 |
| Raw ev draw | -0.1562 |
| Raw edge prob away | 0.0174 |
| Raw ev away | 0.0421 |
| Market p over 1 5 | 83.4% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:21:21Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 64.4% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:23:10Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.59 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:23:11Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.22 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **63.8%**. Expected goals are 0.67 for Venezia and 2.18 for Napoli (2.85 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 52.0%; Under 3.5 goals: 69.7%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 44.6%; BTTS No (at least one team does not score): 55.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 15.1% | 6.63 |
| Draw | 21.1% | 4.74 |
| Napoli win | 63.8% | 1.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.18 |
| Expected total goals | 2.85 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 76.1% |
| Under 1.5 | 23.9% |
| Over 2.5 | 52.0% |
| Under 2.5 | 48.0% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.18% |
| 2 | 0-1 | 11.24% |
| 3 | 1-1 | 9.97% |
| 4 | 0-3 | 8.83% |
| 5 | 1-2 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 15.1% | 20.1% | 4.90 | -26.1% |
| Draw | 21.1% | 24.3% | 4.22 | -11.0% |
| Napoli win | 63.8% | 55.6% | 1.76 | +12.3% |
| Over 2.5 | 52.0% | 56.4% | 1.75 | -9.0% |
| Under 2.5 | 48.0% | 43.6% | 2.25 | +8.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:00:00+00:00 |
| Fixture id | 907639dade64cca45d1ab639195d201e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:38Z |
| Market best draw last update utc | 2026-10-11T08:22:54Z |
| Market best away last update utc | 2026-10-11T08:22:54Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betsson |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 44.6% |
| P btts no | 55.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.67 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.18 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.70 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 72.1% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 43.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 4.70 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.76 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -5.0% |
| Draw probability edge | -3.3% |
| Away probability edge | +8.2% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | -0.0994 |
| Raw ev home | -0.5043 |
| Raw edge prob draw | -0.0651 |
| Raw ev draw | -0.2477 |
| Raw edge prob away | 0.1645 |
| Raw ev away | 0.2682 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **46.4%**. Expected goals are 1.28 for AC Milan and 1.16 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 44.5%; Under 3.5 goals: 76.9%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 49.1%; BTTS No (at least one team does not score): 50.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 46.4% | 2.15 |
| Draw | 25.9% | 3.86 |
| Atalanta BC win | 27.7% | 3.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.28 |
| Atalanta BC expected goals | 1.16 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.5% |
| Under 2.5 | 55.5% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.24% |
| 2 | 1-1 | 12.27% |
| 3 | 2-1 | 9.77% |
| 4 | 2-0 | 8.45% |
| 5 | 0-1 | 8.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 46.4% | 53.4% | 1.93 | -10.4% |
| Draw | 25.9% | 24.6% | 3.86 | +0.0% |
| Atalanta BC win | 27.7% | 22.0% | 4.30 | +18.9% |
| Over 2.5 | 44.5% | 55.8% | 1.83 | -18.5% |
| Under 2.5 | 55.5% | 44.2% | 2.13 | +18.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T16:00:00+00:00 |
| Fixture id | f9403dd597edbfaa73abdc974e55344c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:54Z |
| Market best draw last update utc | 2026-10-11T08:22:54Z |
| Market best away last update utc | 2026-10-11T08:23:12Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 49.1% |
| P btts no | 50.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.13 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.75 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 33.3% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.83 |
| Reference draw odds | 3.85 |
| Reference away odds | 4.30 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -6.9% |
| Draw probability edge | +1.3% |
| Away probability edge | +5.7% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | -0.1389 |
| Raw ev home | -0.2379 |
| Raw edge prob draw | 0.0254 |
| Raw ev draw | 0.0493 |
| Raw edge prob away | 0.1135 |
| Raw ev away | 0.4332 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **51.4%**. Expected goals are 1.00 for Fiorentina and 1.73 for Como (2.73 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.0%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 52.3%; BTTS No (at least one team does not score): 47.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 23.9% | 4.18 |
| Draw | 24.7% | 4.06 |
| Como win | 51.4% | 1.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.00 |
| Como expected goals | 1.73 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 29.0% |
| Under 3.5 | 71.0% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.72% |
| 2 | 0-1 | 10.68% |
| 3 | 0-2 | 9.20% |
| 4 | 1-2 | 9.19% |
| 5 | 1-0 | 7.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 23.9% | 26.1% | 3.65 | -12.7% |
| Draw | 24.7% | 25.7% | 3.85 | -5.1% |
| Como win | 51.4% | 48.2% | 2.13 | +9.5% |
| Over 2.5 | 50.9% | 56.8% | 1.73 | -12.0% |
| Under 2.5 | 49.1% | 43.2% | 2.29 | +12.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 3ea32a0aa44a5f0ef7fd088155430087 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:23:12Z |
| Market best draw last update utc | 2026-10-11T08:22:59Z |
| Market best away last update utc | 2026-10-11T08:22:54Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 52.3% |
| P btts no | 47.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.82 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.45 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.18 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 21.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 51.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 3.65 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.02 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | -2.2% |
| Draw probability edge | -1.1% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0433 |
| Raw ev home | -0.2061 |
| Raw edge prob draw | -0.0213 |
| Raw ev draw | -0.0919 |
| Raw edge prob away | 0.0646 |
| Raw ev away | 0.1643 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **53.6%**. Expected goals are 1.37 for Juventus and 0.85 for Lazio (2.22 combined). The most likely exact score is 1-0 at 16.4%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 38.9%; Under 3.5 goals: 81.3%; Under 4.5 goals: 92.3%; BTTS Yes (both teams score): 42.1%; BTTS No (at least one team does not score): 57.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 53.6% | 1.86 |
| Draw | 26.1% | 3.84 |
| Lazio win | 20.3% | 4.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.85 |
| Expected total goals | 2.22 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 65.3% |
| Under 1.5 | 34.7% |
| Over 2.5 | 38.9% |
| Under 2.5 | 61.1% |
| Over 3.5 | 18.7% |
| Under 3.5 | 81.3% |
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.35% |
| 2 | 1-1 | 11.89% |
| 3 | 2-0 | 11.14% |
| 4 | 0-0 | 10.21% |
| 5 | 2-1 | 9.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 53.6% | 58.2% | 1.69 | -9.3% |
| Draw | 26.1% | 24.5% | 4.04 | +5.3% |
| Lazio win | 20.3% | 17.2% | 5.80 | +17.7% |
| Over 2.5 | 38.9% | 48.5% | 2.03 | -21.0% |
| Under 2.5 | 61.1% | 51.5% | 1.92 | +17.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T18:45:00+00:00 |
| Fixture id | 4c4026e2782f09d6f0ff2bde2a390513 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:54Z |
| Market best draw last update utc | 2026-10-11T08:22:54Z |
| Market best away last update utc | 2026-10-11T08:22:59Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Juventus |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.1% |
| P btts no | 57.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.79 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.34 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.07 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 23.4% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 42.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.68 |
| Reference draw odds | 3.85 |
| Reference away odds | 5.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | -4.6% |
| Draw probability edge | +1.5% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | -0.0917 |
| Raw ev home | -0.1710 |
| Raw edge prob draw | 0.0305 |
| Raw ev draw | 0.1144 |
| Raw edge prob away | 0.0612 |
| Raw ev away | 0.3549 |
| Market p over 1 5 | 74.3% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T08:23:10Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.44 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 74.2% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:23:10Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 48.2% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T08:22:54Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 1.80 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.9%**. Expected goals are 1.44 for Udinese and 0.82 for Lecce (2.26 combined). The most likely exact score is 1-0 at 15.2%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 39.5%; Under 3.5 goals: 80.7%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.6%; BTTS No (at least one team does not score): 57.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.9% | 1.93 |
| Draw | 26.5% | 3.78 |
| Lecce win | 21.6% | 4.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.44 |
| Lecce expected goals | 0.82 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 66.0% |
| Under 1.5 | 34.0% |
| Over 2.5 | 39.5% |
| Under 2.5 | 60.5% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.15% |
| 2 | 1-1 | 12.13% |
| 3 | 2-0 | 10.84% |
| 4 | 0-0 | 10.24% |
| 5 | 2-1 | 8.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.9% | 52.3% | 1.95 | +1.3% |
| Draw | 26.5% | 26.2% | 3.71 | -1.8% |
| Lecce win | 21.6% | 21.6% | 4.40 | -5.1% |
| Over 2.5 | 39.5% | 48.5% | 2.00 | -21.1% |
| Under 2.5 | 60.5% | 51.5% | 1.94 | +17.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T10:30:00+00:00 |
| Fixture id | 367da93aa21a1e13eeafb94fd2263c75 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:54Z |
| Market best draw last update utc | 2026-10-11T08:22:54Z |
| Market best away last update utc | 2026-10-11T08:22:37Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Tipico |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.6% |
| P btts no | 57.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.77 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.58 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 21.6% |
| Raw p over 1 5 | 65.9% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 42.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.87 |
| Reference draw odds | 3.65 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | -0.3% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -9.1% |
| Under 2.5 probability edge | +9.1% |
| Raw edge prob home | -0.0070 |
| Raw ev home | 0.0061 |
| Raw edge prob draw | 0.0065 |
| Raw ev draw | -0.0054 |
| Raw edge prob away | 0.0004 |
| Raw ev away | -0.0498 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **36.9%**. Expected goals are 1.13 for Monza and 1.57 for Cagliari (2.70 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 49.4%; Under 3.5 goals: 72.1%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 54.3%; BTTS No (at least one team does not score): 45.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 35.7% | 2.80 |
| Draw | 27.4% | 3.65 |
| Cagliari win | 36.9% | 2.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.13 |
| Cagliari expected goals | 1.57 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 74.4% |
| Under 1.5 | 25.6% |
| Over 2.5 | 49.4% |
| Under 2.5 | 50.6% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.02% |
| 2 | 1-0 | 10.00% |
| 3 | 2-1 | 8.77% |
| 4 | 0-1 | 8.23% |
| 5 | 0-0 | 7.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 35.7% | 44.1% | 2.40 | -14.3% |
| Draw | 27.4% | 29.9% | 3.30 | -9.5% |
| Cagliari win | 36.9% | 26.1% | 3.65 | +34.5% |
| Over 2.5 | 49.4% | 44.2% | 2.13 | +5.2% |
| Under 2.5 | 50.6% | 55.8% | 1.83 | -7.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T16:30:00+00:00 |
| Fixture id | ce94aca384a20f6af459366da6e1dd21 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:59Z |
| Market best draw last update utc | 2026-10-11T08:22:37Z |
| Market best away last update utc | 2026-10-11T08:23:13Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Tipico |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.3% |
| P btts no | 45.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.65 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.91 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.61 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 27.4% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 47.7% |
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 53.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.65 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.70 |
| Home probability edge | -8.4% |
| Draw probability edge | -2.4% |
| Away probability edge | +10.8% |
| Over 2.5 probability edge | +5.2% |
| Under 2.5 probability edge | -5.2% |
| Raw edge prob home | -0.1671 |
| Raw ev home | -0.3430 |
| Raw edge prob draw | -0.0490 |
| Raw ev draw | -0.1759 |
| Raw edge prob away | 0.2160 |
| Raw ev away | 0.7393 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.5%**. Expected goals are 1.02 for Parma and 1.08 for Torino (2.10 combined). The most likely exact score is 0-1 at 14.0%. Goal-market probabilities: at least one goal: 87.9%; Over 2.5 goals: 35.1%; Under 3.5 goals: 83.8%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 42.1%; BTTS No (at least one team does not score): 57.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.9% | 3.14 |
| Draw | 29.7% | 3.37 |
| Torino win | 38.5% | 2.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.02 |
| Torino expected goals | 1.08 |
| Expected total goals | 2.10 |
| Over 0.5 | 87.9% |
| Under 0.5 | 12.1% |
| Over 1.5 | 62.0% |
| Under 1.5 | 38.0% |
| Over 2.5 | 35.1% |
| Under 2.5 | 64.9% |
| Over 3.5 | 16.2% |
| Under 3.5 | 83.8% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.98% |
| 2 | 1-1 | 13.36% |
| 3 | 0-0 | 12.12% |
| 4 | 1-0 | 11.91% |
| 5 | 1-2 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.9% | 30.0% | 3.25 | +3.6% |
| Draw | 29.7% | 29.5% | 3.25 | -3.6% |
| Torino win | 38.5% | 40.4% | 2.54 | -2.3% |
| Over 2.5 | 35.1% | 41.3% | 2.48 | -13.0% |
| Under 2.5 | 64.9% | 58.7% | 1.64 | +6.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T18:45:00+00:00 |
| Fixture id | 07014d9adc65ca39710bd9f0c7c0d3f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-11T08:22:54Z |
| Market best draw last update utc | 2026-10-11T08:23:13Z |
| Market best away last update utc | 2026-10-11T08:22:54Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | LeoVegas (SE) |
| Matched home-team name | Parma |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.1% |
| P btts no | 57.9% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.25 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.63 |
| Fair Over 2.5 odds | 2.85 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.19 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.06 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 36.5% |
| Raw p over 1 5 | 62.0% |
| Raw p under 3 5 | 83.9% |
| Raw p btts yes | 42.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 3.20 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 2.23 |
| Reference Under 2.5 odds | 1.62 |
| Home probability edge | +1.9% |
| Draw probability edge | +0.1% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | 0.0371 |
| Raw ev home | 0.0964 |
| Raw edge prob draw | 0.0025 |
| Raw ev draw | -0.0317 |
| Raw edge prob away | -0.0396 |
| Raw ev away | -0.0736 |
| Market p over 1 5 | 67.4% |
| Market over 1 5 odds | 1.44 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-11T08:23:10Z |
| Market reference over 1 5 odds | 1.44 |
| Market reference over 1 5 opposite odds | 2.81 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 80.5% |
| Market under 3 5 odds | 1.20 |
| Best under 3 5 bookmaker | Codere (IT) |
| Market best under 3 5 last update utc | 2026-10-11T08:22:38Z |
| Market reference under 3 5 odds | 1.20 |
| Market reference under 3 5 opposite odds | 3.95 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 47.2% |
| Market btts yes odds | 1.96 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T08:22:54Z |
| Market reference btts yes odds | 1.96 |
| Market reference btts yes opposite odds | 1.77 |
| Market btts yes bookmakers | 2 |

</details>


---
