# Premier League — football model report

Fixtures in this report: **11**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,200 |
| Training data through | 2026-10-12 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 897.623 |
| Base scoring parameter | 0.217 |
| Home-advantage parameter | 0.179 |
| Dixon-Coles low-score adjustment | -0.115 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 11.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Brentford win** at **39.5%**. Expected goals are 1.58 for Brentford and 1.48 for Liverpool (3.06 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 59.1%; Under 3.5 goals: 63.4%; Double Chance 1X: 65.8%; Double Chance X2: 60.5%; Under 4.5 goals: 80.5%; BTTS Yes (both teams score): 62.5%; BTTS No (at least one team does not score): 37.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 39.5% | 2.53 |
| Draw | 26.3% | 3.81 |
| Liverpool win | 34.2% | 2.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.58 |
| Liverpool expected goals | 1.48 |
| Expected total goals | 3.06 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 82.2% |
| Under 1.5 | 17.8% |
| Over 2.5 | 59.1% |
| Under 2.5 | 40.9% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.5% |
| Under 4.5 | 80.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.11% |
| 2 | 2-1 | 8.80% |
| 3 | 1-2 | 8.03% |
| 4 | 2-2 | 6.34% |
| 5 | 1-0 | 6.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 39.5% | 40.1% | 2.51 | -0.7% |
| Draw | 26.3% | 26.0% | 3.74 | -1.8% |
| Liverpool win | 34.2% | 33.9% | 2.87 | -1.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | 8f1945e7272bc7e89016439f5ab321c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:14Z |
| Market best draw last update utc | 2026-10-14T11:22:14Z |
| Market best away last update utc | 2026-10-14T11:22:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Brentford |
| Matched away-team name | Liverpool |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 62.5% |
| P btts no | 37.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.96 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.63 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.12 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 34.5% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 62.6% |
| P home draw | 65.8% |
| P draw away | 60.5% |
| Raw p home draw | 65.5% |
| Raw p draw away | 61.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.39 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.81 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -0.6% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | -0.0118 |
| Raw ev home | -0.0222 |
| Raw edge prob draw | 0.0055 |
| Raw ev draw | -0.0078 |
| Raw edge prob away | 0.0064 |
| Raw ev away | -0.0095 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **40.0%**. Expected goals are 1.40 for Everton and 1.37 for Chelsea (2.76 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 52.7%; Under 3.5 goals: 69.9%; Double Chance 1X: 60.0%; Double Chance X2: 66.9%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 33.1% | 3.02 |
| Draw | 26.9% | 3.71 |
| Chelsea win | 40.0% | 2.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.40 |
| Chelsea expected goals | 1.37 |
| Expected total goals | 2.76 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.81% |
| 2 | 1-2 | 9.35% |
| 3 | 0-1 | 8.22% |
| 4 | 2-1 | 7.61% |
| 5 | 0-0 | 7.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 33.1% | 29.6% | 3.23 | +6.8% |
| Draw | 26.9% | 25.6% | 3.88 | +4.5% |
| Chelsea win | 40.0% | 44.8% | 2.23 | -10.8% |
| Over 2.5 | 52.7% | 57.7% | 1.73 | -8.9% |
| Under 2.5 | 47.3% | 42.3% | 2.28 | +7.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T11:30:00+00:00 |
| Fixture id | 764e6513cb3f348881503df70ccb90e0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:14Z |
| Market best draw last update utc | 2026-10-14T11:22:14Z |
| Market best away last update utc | 2026-10-14T11:22:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Everton |
| Matched away-team name | Chelsea |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.62 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.74 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 36.6% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 70.0% |
| Raw p btts yes | 57.5% |
| P home draw | 60.0% |
| P draw away | 66.9% |
| Raw p home draw | 64.8% |
| Raw p draw away | 63.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 3.19 |
| Reference draw odds | 3.66 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | +3.5% |
| Draw probability edge | +1.3% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | 0.0696 |
| Raw ev home | 0.1808 |
| Raw edge prob draw | 0.0263 |
| Raw ev draw | 0.0962 |
| Raw edge prob away | -0.0959 |
| Raw ev away | -0.2153 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.1%**. Expected goals are 0.94 for Fulham and 1.22 for Hull City (2.16 combined). The most likely exact score is 1-0 at 14.6%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 37.9%; Under 3.5 goals: 82.9%; Double Chance 1X: 69.7%; Double Chance X2: 57.9%; Under 4.5 goals: 93.0%; BTTS Yes (both teams score): 43.8%; BTTS No (at least one team does not score): 56.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.1% | 2.38 |
| Draw | 27.7% | 3.61 |
| Hull City win | 30.3% | 3.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.94 |
| Hull City expected goals | 1.22 |
| Expected total goals | 2.16 |
| Over 0.5 | 88.7% |
| Under 0.5 | 11.3% |
| Over 1.5 | 64.9% |
| Under 1.5 | 35.1% |
| Over 2.5 | 37.9% |
| Under 2.5 | 62.1% |
| Over 3.5 | 17.1% |
| Under 3.5 | 82.9% |
| Over 4.5 | 7.0% |
| Under 4.5 | 93.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.56% |
| 2 | 1-1 | 12.72% |
| 3 | 0-0 | 11.25% |
| 4 | 2-1 | 9.73% |
| 5 | 0-1 | 9.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 42.1% | 57.2% | 1.77 | -25.6% |
| Draw | 27.7% | 23.3% | 4.05 | +12.2% |
| Hull City win | 30.3% | 19.6% | 4.93 | +49.1% |
| Over 2.5 | 37.9% | 55.6% | 1.81 | -31.4% |
| Under 2.5 | 62.1% | 44.4% | 2.17 | +34.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | 7895f97f2f9577f3b13287a3d086859d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:14Z |
| Market best draw last update utc | 2026-10-14T11:22:14Z |
| Market best away last update utc | 2026-10-14T11:22:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fulham |
| Matched away-team name | Hull |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 43.8% |
| P btts no | 56.2% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.89 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.85 |
| Fair Over 2.5 odds | 2.64 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.83 |
| Fair Under 3.5 odds | 1.21 |
| Fair Over 4.5 odds | 14.23 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 32.1% |
| Unadjusted away-win probability | 40.9% |
| Raw p over 1 5 | 65.1% |
| Raw p under 3 5 | 82.7% |
| Raw p btts yes | 44.5% |
| P home draw | 69.7% |
| P draw away | 57.9% |
| Raw p home draw | 59.1% |
| Raw p draw away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.70 |
| Reference draw odds | 3.99 |
| Reference away odds | 4.70 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Home probability edge | -15.1% |
| Draw probability edge | +4.4% |
| Away probability edge | +10.7% |
| Over 2.5 probability edge | -17.6% |
| Under 2.5 probability edge | +17.6% |
| Raw edge prob home | -0.3022 |
| Raw ev home | -0.5231 |
| Raw edge prob draw | 0.0887 |
| Raw ev draw | 0.3011 |
| Raw edge prob away | 0.2136 |
| Raw ev away | 1.0179 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **84.4%**. Expected goals are 3.47 for Manchester City and 0.73 for Ipswich Town (4.20 combined). The most likely exact score is 3-0 at 10.2%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 78.2%; Under 3.5 goals: 40.4%; Double Chance 1X: 95.0%; Double Chance X2: 15.6%; Under 4.5 goals: 59.8%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 84.4% | 1.18 |
| Draw | 10.5% | 9.48 |
| Ipswich Town win | 5.0% | 19.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.47 |
| Ipswich Town expected goals | 0.73 |
| Expected total goals | 4.20 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 92.3% |
| Under 1.5 | 7.7% |
| Over 2.5 | 78.2% |
| Under 2.5 | 21.8% |
| Over 3.5 | 59.6% |
| Under 3.5 | 40.4% |
| Over 4.5 | 40.2% |
| Under 4.5 | 59.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.20% |
| 2 | 4-0 | 8.85% |
| 3 | 2-0 | 8.82% |
| 4 | 3-1 | 7.41% |
| 5 | 4-1 | 6.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 84.4% | 82.1% | 1.26 | +6.4% |
| Draw | 10.5% | 11.7% | 7.26 | -23.4% |
| Ipswich Town win | 5.0% | 6.2% | 11.50 | -42.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | bf2142d1ca76ba2fc9e61afce80f86c0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:14Z |
| Market best draw last update utc | 2026-10-14T11:22:14Z |
| Market best away last update utc | 2026-10-14T11:22:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man City |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.65 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 12.96 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.58 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.48 |
| Fair Over 4.5 odds | 2.49 |
| Fair Under 4.5 odds | 1.67 |
| Unadjusted home-win probability | 86.8% |
| Unadjusted draw probability | 9.4% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 92.6% |
| Raw p under 3 5 | 39.7% |
| Raw p btts yes | 50.5% |
| P home draw | 95.0% |
| P draw away | 15.6% |
| Raw p home draw | 96.2% |
| Raw p draw away | 13.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.20 |
| Reference draw odds | 7.21 |
| Reference away odds | 12.92 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.21 |
| Home probability edge | +2.4% |
| Draw probability edge | -1.2% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +6.5% |
| Under 2.5 probability edge | -6.5% |
| Raw edge prob home | 0.0476 |
| Raw ev home | 0.0938 |
| Raw edge prob draw | -0.0236 |
| Raw ev draw | -0.3199 |
| Raw edge prob away | -0.0240 |
| Raw ev away | -0.5606 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **43.1%**. Expected goals are 1.76 for Newcastle United and 1.52 for Aston Villa (3.28 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 63.7%; Under 3.5 goals: 58.4%; Double Chance 1X: 68.5%; Double Chance X2: 56.9%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 65.9%; BTTS No (at least one team does not score): 34.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 43.1% | 2.32 |
| Draw | 25.4% | 3.93 |
| Aston Villa win | 31.5% | 3.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.76 |
| Aston Villa expected goals | 1.52 |
| Expected total goals | 3.28 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 63.7% |
| Under 2.5 | 36.3% |
| Over 3.5 | 41.6% |
| Under 3.5 | 58.4% |
| Over 4.5 | 23.4% |
| Under 4.5 | 76.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.30% |
| 2 | 2-1 | 9.01% |
| 3 | 1-2 | 7.44% |
| 4 | 2-2 | 6.79% |
| 5 | 2-0 | 5.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 43.1% | 43.9% | 2.26 | -2.6% |
| Draw | 25.4% | 25.6% | 3.85 | -2.1% |
| Aston Villa win | 31.5% | 30.5% | 3.19 | +0.4% |
| Over 2.5 | 63.7% | 60.1% | 1.67 | +6.3% |
| Under 2.5 | 36.3% | 39.9% | 2.40 | -12.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | d1bbbdcd3d430e70091b518369b559cf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:14Z |
| Market best draw last update utc | 2026-10-14T11:22:14Z |
| Market best away last update utc | 2026-10-14T11:22:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Newcastle |
| Matched away-team name | Aston Villa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.9% |
| P btts no | 34.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.22 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.71 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.40 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.27 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 32.5% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 58.4% |
| Raw p btts yes | 65.9% |
| P home draw | 68.5% |
| P draw away | 56.9% |
| Raw p home draw | 67.5% |
| Raw p draw away | 57.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.19 |
| Reference draw odds | 3.66 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.36 |
| Home probability edge | -0.8% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Raw edge prob home | -0.0162 |
| Raw ev home | -0.0444 |
| Raw edge prob draw | -0.0035 |
| Raw ev draw | -0.0277 |
| Raw edge prob away | 0.0197 |
| Raw ev away | 0.0355 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **48.1%**. Expected goals are 1.59 for Bournemouth and 1.06 for Sunderland (2.65 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 49.7%; Under 3.5 goals: 72.5%; Double Chance 1X: 74.9%; Double Chance X2: 51.9%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 53.2%; BTTS No (at least one team does not score): 46.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 48.1% | 2.08 |
| Draw | 26.9% | 3.72 |
| Sunderland win | 25.1% | 3.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.59 |
| Sunderland expected goals | 1.06 |
| Expected total goals | 2.65 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 75.6% |
| Under 1.5 | 24.4% |
| Over 2.5 | 49.7% |
| Under 2.5 | 50.3% |
| Over 3.5 | 27.5% |
| Under 3.5 | 72.5% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.85% |
| 2 | 1-0 | 9.83% |
| 3 | 2-1 | 9.42% |
| 4 | 2-0 | 8.90% |
| 5 | 0-0 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 48.1% | 47.8% | 2.04 | -2.0% |
| Draw | 26.9% | 26.0% | 3.75 | +0.8% |
| Sunderland win | 25.1% | 26.2% | 3.85 | -3.6% |
| Over 2.5 | 49.7% | 53.2% | 1.88 | -6.6% |
| Under 2.5 | 50.3% | 46.8% | 2.07 | +4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | dfd5d6648be46426e418801584d46a68 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:14Z |
| Market best draw last update utc | 2026-10-14T11:22:14Z |
| Market best away last update utc | 2026-10-14T11:22:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bournemouth |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 53.2% |
| P btts no | 46.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.23 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.10 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.67 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 53.4% |
| P home draw | 74.9% |
| P draw away | 51.9% |
| Raw p home draw | 76.1% |
| Raw p draw away | 51.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.02 |
| Reference draw odds | 3.61 |
| Reference away odds | 3.58 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.03 |
| Home probability edge | +0.3% |
| Draw probability edge | +0.9% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | 0.0052 |
| Raw ev home | -0.0142 |
| Raw edge prob draw | 0.0180 |
| Raw ev draw | 0.0420 |
| Raw edge prob away | -0.0232 |
| Raw ev away | -0.0803 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **60.7%**. Expected goals are 2.00 for Brighton and Hove Albion and 1.02 for Crystal Palace (3.02 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 58.7%; Under 3.5 goals: 64.0%; Double Chance 1X: 83.0%; Double Chance X2: 39.3%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 60.7% | 1.65 |
| Draw | 22.3% | 4.49 |
| Crystal Palace win | 17.0% | 5.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 2.00 |
| Crystal Palace expected goals | 1.02 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 58.7% |
| Under 2.5 | 41.3% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.52% |
| 2 | 2-1 | 10.25% |
| 3 | 2-0 | 10.05% |
| 4 | 1-0 | 8.86% |
| 5 | 3-1 | 6.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 60.7% | 62.5% | 1.63 | -1.0% |
| Draw | 22.3% | 21.1% | 4.57 | +1.9% |
| Crystal Palace win | 17.0% | 16.4% | 5.44 | -7.6% |
| Over 2.5 | 58.7% | 60.9% | 1.63 | -4.3% |
| Under 2.5 | 41.3% | 39.1% | 2.49 | +2.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 9fc08b390a49c4434f7cf631a0bb88fb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:14Z |
| Market best draw last update utc | 2026-10-14T11:22:14Z |
| Market best away last update utc | 2026-10-14T11:22:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.52 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.47 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.24 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 59.0% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 17.5% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 56.5% |
| P home draw | 83.0% |
| P draw away | 39.3% |
| Raw p home draw | 82.5% |
| Raw p draw away | 41.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.56 |
| Reference draw odds | 4.36 |
| Reference away odds | 5.51 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -1.8% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.0350 |
| Raw ev home | -0.0386 |
| Raw edge prob draw | 0.0243 |
| Raw ev draw | 0.0742 |
| Raw edge prob away | 0.0107 |
| Raw ev away | -0.0472 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **39.0%**. Expected goals are 1.42 for Leeds United and 1.28 for Manchester United (2.70 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.4%; Double Chance 1X: 66.5%; Double Chance X2: 61.0%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 39.0% | 2.56 |
| Draw | 27.5% | 3.64 |
| Manchester United win | 33.5% | 2.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.28 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 76.6% |
| Under 1.5 | 23.4% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 28.6% |
| Under 3.5 | 71.4% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.12% |
| 2 | 2-1 | 8.70% |
| 3 | 1-0 | 8.17% |
| 4 | 1-2 | 8.04% |
| 5 | 0-0 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 39.0% | 39.2% | 2.51 | -2.1% |
| Draw | 27.5% | 26.4% | 3.75 | +3.1% |
| Manchester United win | 33.5% | 34.4% | 2.86 | -4.2% |
| Over 2.5 | 51.0% | 58.9% | 1.70 | -13.3% |
| Under 2.5 | 49.0% | 41.1% | 2.34 | +14.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 676b3b0b609e9cf565da450786618d26 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:14Z |
| Market best draw last update utc | 2026-10-14T11:22:14Z |
| Market best away last update utc | 2026-10-14T11:22:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.76 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.27 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.24 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 76.5% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 56.1% |
| P home draw | 66.5% |
| P draw away | 61.0% |
| Raw p home draw | 67.4% |
| Raw p draw away | 61.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.44 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.77 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.29 |
| Home probability edge | -0.2% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -7.9% |
| Under 2.5 probability edge | +7.9% |
| Raw edge prob home | -0.0048 |
| Raw ev home | -0.0270 |
| Raw edge prob draw | 0.0218 |
| Raw ev draw | 0.0721 |
| Raw edge prob away | -0.0171 |
| Raw ev away | -0.0663 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **57.9%**. Expected goals are 0.76 for Nottingham Forest and 1.53 for Arsenal (2.29 combined). The most likely exact score is 0-1 at 15.1%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.7%; Double Chance 1X: 42.1%; Double Chance X2: 83.9%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 42.5%; BTTS No (at least one team does not score): 57.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.1% | 6.21 |
| Draw | 26.0% | 3.85 |
| Arsenal win | 57.9% | 1.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.76 |
| Arsenal expected goals | 1.53 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 68.6% |
| Under 1.5 | 31.4% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.06% |
| 2 | 0-2 | 12.62% |
| 3 | 1-1 | 11.98% |
| 4 | 0-0 | 10.45% |
| 5 | 1-2 | 9.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.1% | 14.9% | 6.11 | -1.6% |
| Draw | 26.0% | 23.5% | 3.98 | +3.5% |
| Arsenal win | 57.9% | 61.6% | 1.66 | -3.9% |
| Over 2.5 | 41.2% | 50.0% | 1.97 | -18.8% |
| Under 2.5 | 58.8% | 50.0% | 1.97 | +15.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | f696a248965373d9071dc0662e5c58a8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:15Z |
| Market best draw last update utc | 2026-10-14T11:22:15Z |
| Market best away last update utc | 2026-10-14T11:22:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.5% |
| P btts no | 57.5% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.57 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.18 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.93 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.66 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 54.2% |
| Raw p over 1 5 | 68.1% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 43.2% |
| P home draw | 42.1% |
| P draw away | 83.9% |
| Raw p home draw | 45.8% |
| Raw p draw away | 82.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 6.05 |
| Reference draw odds | 3.94 |
| Reference away odds | 1.58 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.91 |
| Home probability edge | +1.2% |
| Draw probability edge | +2.5% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | 0.0239 |
| Raw ev home | 0.0567 |
| Raw edge prob draw | 0.0509 |
| Raw ev draw | 0.1360 |
| Raw edge prob away | -0.0748 |
| Raw ev away | -0.1009 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **55.3%**. Expected goals are 1.43 for Tottenham Hotspur and 1.06 for Coventry City (2.49 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 47.3%; Under 3.5 goals: 75.4%; Double Chance 1X: 79.8%; Double Chance X2: 44.7%; Under 4.5 goals: 88.6%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 55.3% | 1.81 |
| Draw | 24.5% | 4.07 |
| Coventry City win | 20.2% | 4.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.43 |
| Coventry City expected goals | 1.06 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 73.2% |
| Under 1.5 | 26.8% |
| Over 2.5 | 47.3% |
| Under 2.5 | 52.7% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 11.4% |
| Under 4.5 | 88.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.09% |
| 2 | 1-1 | 11.70% |
| 3 | 2-1 | 11.26% |
| 4 | 2-0 | 10.65% |
| 5 | 0-0 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 55.3% | 66.4% | 1.54 | -14.9% |
| Draw | 24.5% | 19.7% | 4.72 | +15.9% |
| Coventry City win | 20.2% | 13.9% | 6.47 | +30.6% |
| Over 2.5 | 47.3% | 60.9% | 1.64 | -22.5% |
| Under 2.5 | 52.7% | 39.1% | 2.46 | +29.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T19:00:00+00:00 |
| Fixture id | 9baaf4e48b041cfef04e70e42532502e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:15Z |
| Market best draw last update utc | 2026-10-14T11:22:15Z |
| Market best away last update utc | 2026-10-14T11:22:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 49.7% |
| P btts no | 50.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.26 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.72 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 4.06 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.80 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 44.1% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 26.5% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 76.1% |
| Raw p btts yes | 51.1% |
| P home draw | 79.8% |
| P draw away | 44.7% |
| Raw p home draw | 73.5% |
| Raw p draw away | 55.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.47 |
| Reference draw odds | 4.63 |
| Reference away odds | 6.42 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -11.2% |
| Draw probability edge | +4.9% |
| Away probability edge | +6.3% |
| Over 2.5 probability edge | -13.6% |
| Under 2.5 probability edge | +13.6% |
| Raw edge prob home | -0.2235 |
| Raw ev home | -0.3210 |
| Raw edge prob draw | 0.0977 |
| Raw ev draw | 0.3891 |
| Raw edge prob away | 0.1258 |
| Raw ev away | 0.7131 |

</details>


---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **45.5%**. Expected goals are 1.22 for Ipswich Town and 1.76 for Nottingham Forest (2.98 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 57.0%; Under 3.5 goals: 65.4%; Double Chance 1X: 54.5%; Double Chance X2: 71.9%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 28.1% | 3.56 |
| Draw | 26.3% | 3.80 |
| Nottingham Forest win | 45.5% | 2.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.22 |
| Nottingham Forest expected goals | 1.76 |
| Expected total goals | 2.98 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 57.0% |
| Under 2.5 | 43.0% |
| Over 3.5 | 34.6% |
| Under 3.5 | 65.4% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.35% |
| 2 | 1-2 | 8.94% |
| 3 | 2-1 | 7.42% |
| 4 | 0-2 | 7.34% |
| 5 | 0-1 | 7.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 28.1% | 31.1% | 3.10 | -12.8% |
| Draw | 26.3% | 26.8% | 3.63 | -4.4% |
| Nottingham Forest win | 45.5% | 42.1% | 2.39 | +8.8% |
| Over 2.5 | 57.0% | 53.5% | 1.84 | +4.9% |
| Under 2.5 | 43.0% | 46.5% | 2.12 | -8.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T19:00:00+00:00 |
| Fixture id | d0202960708a442401d7fc7bd74a0183 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T11:22:15Z |
| Market best draw last update utc | 2026-10-14T11:22:15Z |
| Market best away last update utc | 2026-10-14T11:22:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.54 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.56 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 25.1% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 49.0% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 59.6% |
| P home draw | 54.5% |
| P draw away | 71.9% |
| Raw p home draw | 51.0% |
| Raw p draw away | 74.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 3.04 |
| Reference draw odds | 3.51 |
| Reference away odds | 2.28 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.04 |
| Home probability edge | -3.0% |
| Draw probability edge | -0.4% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | +3.5% |
| Under 2.5 probability edge | -3.5% |
| Raw edge prob home | -0.0602 |
| Raw ev home | -0.2216 |
| Raw edge prob draw | -0.0084 |
| Raw ev draw | -0.0588 |
| Raw edge prob away | 0.0686 |
| Raw ev away | 0.1702 |

</details>


---
