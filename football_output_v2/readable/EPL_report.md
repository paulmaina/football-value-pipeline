# Premier League — football model report

Fixtures in this report: **15**.

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
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 15.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
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

The model's most likely 1X2 outcome is **Brentford win** at **39.8%**. Expected goals are 1.58 for Brentford and 1.48 for Liverpool (3.06 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 59.2%; Under 3.5 goals: 63.3%; Double Chance 1X: 65.8%; Double Chance X2: 60.2%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 80.4%; BTTS Yes (both teams score): 62.5%; BTTS No (at least one team does not score): 37.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 39.8% | 2.51 |
| Draw | 25.9% | 3.85 |
| Liverpool win | 34.2% | 2.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.58 |
| Liverpool expected goals | 1.48 |
| Expected total goals | 3.06 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 82.3% |
| Under 1.5 | 17.7% |
| Over 2.5 | 59.2% |
| Under 2.5 | 40.8% |
| Over 3.5 | 36.7% |
| Under 3.5 | 63.3% |
| Over 4.5 | 19.6% |
| Under 4.5 | 80.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.96% |
| 2 | 2-1 | 8.86% |
| 3 | 1-2 | 8.05% |
| 4 | 1-0 | 6.28% |
| 5 | 2-2 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 39.8% | 40.6% | 2.51 | -0.1% |
| Draw | 25.9% | 25.4% | 3.74 | -2.9% |
| Liverpool win | 34.2% | 34.0% | 2.87 | -1.7% |

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
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
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
| Fair Under 0.5 odds | 17.16 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.64 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.11 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 34.5% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 62.6% |
| P home draw | 65.8% |
| P draw away | 60.2% |
| P home away | 74.1% |
| Raw p home draw | 65.5% |
| Raw p draw away | 61.0% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.36 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.80 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.52 |
| Home probability edge | -0.8% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | -0.0169 |
| Raw ev home | -0.0222 |
| Raw edge prob draw | 0.0116 |
| Raw ev draw | -0.0078 |
| Raw edge prob away | 0.0053 |
| Raw ev away | -0.0095 |
| Market p home draw | 66.0% |
| Market home draw odds | 1.48 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:31Z |
| Market reference home draw last update utc | 2026-10-15T06:53:36Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.8% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:31Z |
| Market reference draw away last update utc | 2026-10-15T06:53:36Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.2% |
| Market home away odds | 1.32 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:31Z |
| Market reference home away last update utc | 2026-10-15T06:53:36Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.59 |
| Market reference dc home draw odds | 1.44 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:52:43Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.0% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:52:43Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.28 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.3% |
| Market btts yes odds | 1.46 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:31Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 2.56 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **39.8%**. Expected goals are 1.40 for Everton and 1.37 for Chelsea (2.76 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 52.7%; Under 3.5 goals: 69.9%; Double Chance 1X: 60.2%; Double Chance X2: 66.7%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 33.3% | 3.00 |
| Draw | 26.8% | 3.73 |
| Chelsea win | 39.8% | 2.51 |

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
| 1 | 1-1 | 12.76% |
| 2 | 1-2 | 9.31% |
| 3 | 0-1 | 8.19% |
| 4 | 2-1 | 7.67% |
| 5 | 0-0 | 7.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 33.3% | 30.1% | 3.23 | +7.7% |
| Draw | 26.8% | 25.4% | 3.88 | +4.2% |
| Chelsea win | 39.8% | 44.5% | 2.23 | -11.2% |
| Over 2.5 | 52.7% | 57.5% | 1.73 | -8.8% |
| Under 2.5 | 47.3% | 42.5% | 2.28 | +7.9% |

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
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
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
| Fair Under 0.5 odds | 13.67 |
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
| P home draw | 60.2% |
| P draw away | 66.7% |
| P home away | 73.2% |
| Raw p home draw | 64.8% |
| Raw p draw away | 63.4% |
| Raw p home away | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.15 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.17 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.11 |
| Home probability edge | +3.2% |
| Draw probability edge | +1.4% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | 0.0645 |
| Raw ev home | 0.1808 |
| Raw edge prob draw | 0.0281 |
| Raw ev draw | 0.0962 |
| Raw edge prob away | -0.0927 |
| Raw ev away | -0.2153 |
| Market p home draw | 56.0% |
| Market home draw odds | 1.73 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:31Z |
| Market reference home draw last update utc | 2026-10-15T06:53:36Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.5% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:31Z |
| Market reference draw away last update utc | 2026-10-15T06:53:36Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.4% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:31Z |
| Market reference home away last update utc | 2026-10-15T06:53:36Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.37 |
| Market reference dc home draw odds | 1.70 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 81.1% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:29Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.2% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:29Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.1% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:31Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.32 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **41.4%**. Expected goals are 0.94 for Fulham and 1.22 for Hull City (2.16 combined). The most likely exact score is 1-0 at 14.3%. Goal-market probabilities: at least one goal: 88.6%; Over 2.5 goals: 37.8%; Under 3.5 goals: 82.9%; Double Chance 1X: 69.5%; Double Chance X2: 58.6%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 93.0%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 41.4% | 2.41 |
| Draw | 28.0% | 3.57 |
| Hull City win | 30.5% | 3.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.94 |
| Hull City expected goals | 1.22 |
| Expected total goals | 2.16 |
| Over 0.5 | 88.6% |
| Under 0.5 | 11.4% |
| Over 1.5 | 64.9% |
| Under 1.5 | 35.1% |
| Over 2.5 | 37.8% |
| Under 2.5 | 62.2% |
| Over 3.5 | 17.1% |
| Under 3.5 | 82.9% |
| Over 4.5 | 7.0% |
| Under 4.5 | 93.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.34% |
| 2 | 1-1 | 12.88% |
| 3 | 0-0 | 11.39% |
| 4 | 2-1 | 9.58% |
| 5 | 0-1 | 9.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 41.4% | 55.9% | 1.77 | -26.7% |
| Draw | 28.0% | 24.0% | 4.05 | +13.6% |
| Hull City win | 30.5% | 20.1% | 4.93 | +50.5% |
| Over 2.5 | 37.8% | 54.9% | 1.81 | -31.6% |
| Under 2.5 | 62.2% | 45.1% | 2.17 | +35.0% |

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
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
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
| P btts yes | 43.9% |
| P btts no | 56.1% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.78 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.85 |
| Fair Over 2.5 odds | 2.65 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.83 |
| Fair Under 3.5 odds | 1.21 |
| Fair Over 4.5 odds | 14.27 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 32.1% |
| Unadjusted away-win probability | 40.9% |
| Raw p over 1 5 | 65.1% |
| Raw p under 3 5 | 82.7% |
| Raw p btts yes | 44.5% |
| P home draw | 69.5% |
| P draw away | 58.6% |
| P home away | 72.0% |
| Raw p home draw | 59.1% |
| Raw p draw away | 73.1% |
| Raw p home away | 67.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.74 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.60 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.01 |
| Home probability edge | -14.5% |
| Draw probability edge | +4.1% |
| Away probability edge | +10.4% |
| Over 2.5 probability edge | -17.1% |
| Under 2.5 probability edge | +17.1% |
| Raw edge prob home | -0.2896 |
| Raw ev home | -0.5231 |
| Raw edge prob draw | 0.0817 |
| Raw ev draw | 0.3011 |
| Raw edge prob away | 0.2079 |
| Raw ev away | 1.0179 |
| Market p home draw | 79.3% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:31Z |
| Market reference home draw last update utc | 2026-10-15T06:53:36Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 45.1% |
| Market draw away odds | 2.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:31Z |
| Market reference draw away last update utc | 2026-10-15T06:53:36Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.6% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:31Z |
| Market reference home away last update utc | 2026-10-15T06:53:36Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.11 |
| Market reference dc home draw odds | 1.20 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 79.5% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:29Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.7% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:29Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 2.65 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.2% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:31Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 2.09 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **83.4%**. Expected goals are 3.47 for Manchester City and 0.73 for Ipswich Town (4.20 combined). The most likely exact score is 3-0 at 10.1%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 77.9%; Under 3.5 goals: 40.7%; Double Chance 1X: 94.4%; Double Chance X2: 16.6%; Double Chance 12 (either team wins): 89.0%; Under 4.5 goals: 60.1%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 83.4% | 1.20 |
| Draw | 11.0% | 9.11 |
| Ipswich Town win | 5.6% | 17.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.47 |
| Ipswich Town expected goals | 0.73 |
| Expected total goals | 4.20 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 92.1% |
| Under 1.5 | 7.9% |
| Over 2.5 | 77.9% |
| Under 2.5 | 22.1% |
| Over 3.5 | 59.3% |
| Under 3.5 | 40.7% |
| Over 4.5 | 39.9% |
| Under 4.5 | 60.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.07% |
| 2 | 4-0 | 8.74% |
| 3 | 2-0 | 8.71% |
| 4 | 3-1 | 7.32% |
| 5 | 4-1 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 83.4% | 79.9% | 1.26 | +5.1% |
| Draw | 11.0% | 12.6% | 7.26 | -20.3% |
| Ipswich Town win | 5.6% | 7.5% | 11.50 | -35.0% |

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
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man City |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.86 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.74 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.52 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.46 |
| Fair Over 4.5 odds | 2.51 |
| Fair Under 4.5 odds | 1.66 |
| Unadjusted home-win probability | 86.8% |
| Unadjusted draw probability | 9.4% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 92.6% |
| Raw p under 3 5 | 39.7% |
| Raw p btts yes | 50.5% |
| P home draw | 94.4% |
| P draw away | 16.6% |
| P home away | 89.0% |
| Raw p home draw | 96.2% |
| Raw p draw away | 13.2% |
| Raw p home away | 90.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.23 |
| Reference draw odds | 6.80 |
| Reference away odds | 11.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.21 |
| Home probability edge | +3.4% |
| Draw probability edge | -1.6% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +6.2% |
| Under 2.5 probability edge | -6.2% |
| Raw edge prob home | 0.0687 |
| Raw ev home | 0.0938 |
| Raw edge prob draw | -0.0321 |
| Raw ev draw | -0.3199 |
| Raw edge prob away | -0.0366 |
| Raw ev away | -0.5606 |
| Market p home draw | 91.9% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:31Z |
| Market reference home draw last update utc | 2026-10-15T06:53:31Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.7% |
| Market draw away odds | 4.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:31Z |
| Market reference draw away last update utc | 2026-10-15T06:53:31Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 85.4% |
| Market home away odds | 1.13 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:31Z |
| Market reference home away last update utc | 2026-10-15T06:53:31Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.26 |
| Market reference dc home draw odds | 1.05 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 88.7% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:04Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.1% |
| Market under 3 5 odds | 1.95 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:04Z |
| Market reference under 3 5 odds | 1.80 |
| Market reference under 3 5 opposite odds | 1.87 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.5% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:31Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 1.98 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **42.3%**. Expected goals are 1.76 for Newcastle United and 1.52 for Aston Villa (3.28 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.4%; Double Chance 1X: 67.7%; Double Chance X2: 57.7%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 66.0%; BTTS No (at least one team does not score): 34.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 42.3% | 2.37 |
| Draw | 25.5% | 3.93 |
| Aston Villa win | 32.3% | 3.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.76 |
| Aston Villa expected goals | 1.52 |
| Expected total goals | 3.28 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 63.6% |
| Under 2.5 | 36.4% |
| Over 3.5 | 41.6% |
| Under 3.5 | 58.4% |
| Over 4.5 | 23.4% |
| Under 4.5 | 76.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.31% |
| 2 | 2-1 | 8.84% |
| 3 | 1-2 | 7.62% |
| 4 | 2-2 | 6.79% |
| 5 | 2-0 | 5.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 42.3% | 42.3% | 2.26 | -4.5% |
| Draw | 25.5% | 25.7% | 3.85 | -2.0% |
| Aston Villa win | 32.3% | 32.1% | 3.19 | +3.0% |
| Over 2.5 | 63.6% | 60.4% | 1.67 | +6.3% |
| Under 2.5 | 36.4% | 39.6% | 2.40 | -12.7% |

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
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Newcastle |
| Matched away-team name | Aston Villa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.0% |
| P btts no | 34.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.20 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.70 |
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
| P home draw | 67.7% |
| P draw away | 57.7% |
| P home away | 74.5% |
| Raw p home draw | 67.5% |
| Raw p draw away | 57.7% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.27 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.95 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.24 |
| Home probability edge | +0.0% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | +3.2% |
| Under 2.5 probability edge | -3.2% |
| Raw edge prob home | 0.0003 |
| Raw ev home | -0.0444 |
| Raw edge prob draw | -0.0040 |
| Raw ev draw | -0.0277 |
| Raw edge prob away | 0.0037 |
| Raw ev away | 0.0355 |
| Market p home draw | 67.7% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:31Z |
| Market reference home draw last update utc | 2026-10-15T06:53:36Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.2% |
| Market draw away odds | 1.71 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:31Z |
| Market reference draw away last update utc | 2026-10-15T06:53:36Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:31Z |
| Market reference home away last update utc | 2026-10-15T06:53:36Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.63 |
| Market reference dc home draw odds | 1.40 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 83.3% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:05Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.2% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:05Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.33 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.9% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:31Z |
| Market reference btts yes odds | 1.51 |
| Market reference btts yes opposite odds | 2.42 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.1%**. Expected goals are 1.59 for Bournemouth and 1.06 for Sunderland (2.65 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 49.5%; Under 3.5 goals: 72.6%; Double Chance 1X: 74.4%; Double Chance X2: 52.9%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 53.3%; BTTS No (at least one team does not score): 46.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.1% | 2.12 |
| Draw | 27.3% | 3.66 |
| Sunderland win | 25.6% | 3.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.59 |
| Sunderland expected goals | 1.06 |
| Expected total goals | 2.65 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 27.4% |
| Under 3.5 | 72.6% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.06% |
| 2 | 1-0 | 9.63% |
| 3 | 2-1 | 9.23% |
| 4 | 2-0 | 8.72% |
| 5 | 0-0 | 8.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.1% | 45.9% | 2.04 | -3.9% |
| Draw | 27.3% | 26.8% | 3.75 | +2.4% |
| Sunderland win | 25.6% | 27.3% | 3.85 | -1.5% |
| Over 2.5 | 49.5% | 53.1% | 1.88 | -7.0% |
| Under 2.5 | 50.5% | 46.9% | 2.07 | +4.5% |

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
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
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
| P btts yes | 53.3% |
| P btts no | 46.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.04 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.65 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.71 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 53.4% |
| P home draw | 74.4% |
| P draw away | 52.9% |
| P home away | 72.7% |
| Raw p home draw | 76.1% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.45 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 1.94 |
| Home probability edge | +1.2% |
| Draw probability edge | +0.5% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | 0.0243 |
| Raw ev home | -0.0142 |
| Raw edge prob draw | 0.0094 |
| Raw ev draw | 0.0420 |
| Raw edge prob away | -0.0337 |
| Raw ev away | -0.0803 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **60.9%**. Expected goals are 2.00 for Brighton and Hove Albion and 1.02 for Crystal Palace (3.02 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 58.8%; Under 3.5 goals: 64.0%; Double Chance 1X: 82.9%; Double Chance X2: 39.1%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 56.0%; BTTS No (at least one team does not score): 44.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 60.9% | 1.64 |
| Draw | 21.9% | 4.56 |
| Crystal Palace win | 17.1% | 5.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 2.00 |
| Crystal Palace expected goals | 1.02 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.35% |
| 2 | 2-1 | 10.28% |
| 3 | 2-0 | 10.08% |
| 4 | 1-0 | 8.89% |
| 5 | 3-1 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 60.9% | 62.9% | 1.63 | -0.7% |
| Draw | 21.9% | 20.3% | 4.57 | +0.2% |
| Crystal Palace win | 17.1% | 16.8% | 5.44 | -6.7% |
| Over 2.5 | 58.8% | 60.7% | 1.63 | -4.1% |
| Under 2.5 | 41.2% | 39.3% | 2.49 | +2.5% |

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
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.0% |
| P btts no | 44.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.81 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.48 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.22 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 59.0% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 17.5% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 56.5% |
| P home draw | 82.9% |
| P draw away | 39.1% |
| P home away | 78.1% |
| Raw p home draw | 82.5% |
| Raw p draw away | 41.0% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.55 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.40 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.49 |
| Home probability edge | -1.9% |
| Draw probability edge | +1.6% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | -0.0390 |
| Raw ev home | -0.0386 |
| Raw edge prob draw | 0.0316 |
| Raw ev draw | 0.0742 |
| Raw edge prob away | 0.0074 |
| Raw ev away | -0.0472 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **39.7%**. Expected goals are 1.42 for Leeds United and 1.28 for Manchester United (2.70 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.4%; Double Chance 1X: 67.0%; Double Chance X2: 60.3%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 55.8%; BTTS No (at least one team does not score): 44.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 39.7% | 2.52 |
| Draw | 27.3% | 3.66 |
| Manchester United win | 33.0% | 3.03 |

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
| 1 | 1-1 | 13.04% |
| 2 | 2-1 | 8.86% |
| 3 | 1-0 | 8.32% |
| 4 | 1-2 | 7.92% |
| 5 | 0-0 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 39.7% | 40.6% | 2.51 | -0.4% |
| Draw | 27.3% | 26.1% | 3.75 | +2.5% |
| Manchester United win | 33.0% | 33.3% | 2.86 | -5.7% |
| Over 2.5 | 51.0% | 58.5% | 1.70 | -13.2% |
| Under 2.5 | 49.0% | 41.5% | 2.34 | +14.6% |

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
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
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
| P btts yes | 55.8% |
| P btts no | 44.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.84 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.27 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.23 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 76.5% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 56.1% |
| P home draw | 67.0% |
| P draw away | 60.3% |
| P home away | 72.7% |
| Raw p home draw | 67.4% |
| Raw p draw away | 61.2% |
| Raw p home away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.36 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.85 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | -0.9% |
| Draw probability edge | +1.3% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.0185 |
| Raw ev home | -0.0270 |
| Raw edge prob draw | 0.0252 |
| Raw ev draw | 0.0721 |
| Raw edge prob away | -0.0067 |
| Raw ev away | -0.0663 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **57.5%**. Expected goals are 0.76 for Nottingham Forest and 1.53 for Arsenal (2.29 combined). The most likely exact score is 0-1 at 15.0%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.8%; Double Chance 1X: 42.5%; Double Chance X2: 83.5%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 42.5%; BTTS No (at least one team does not score): 57.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.5% | 6.07 |
| Draw | 26.0% | 3.85 |
| Arsenal win | 57.5% | 1.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.76 |
| Arsenal expected goals | 1.53 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 68.5% |
| Under 1.5 | 31.5% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.96% |
| 2 | 0-2 | 12.54% |
| 3 | 1-1 | 11.98% |
| 4 | 0-0 | 10.45% |
| 5 | 1-2 | 9.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.5% | 15.6% | 6.11 | +0.6% |
| Draw | 26.0% | 23.5% | 3.98 | +3.5% |
| Arsenal win | 57.5% | 60.9% | 1.66 | -4.5% |
| Over 2.5 | 41.2% | 49.5% | 1.97 | -18.8% |
| Under 2.5 | 58.8% | 50.5% | 1.97 | +15.8% |

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
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
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
| Fair Over 3.5 odds | 4.94 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.68 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 54.2% |
| Raw p over 1 5 | 68.1% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 43.2% |
| P home draw | 42.5% |
| P draw away | 83.5% |
| P home away | 74.0% |
| Raw p home draw | 45.8% |
| Raw p draw away | 82.7% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 5.80 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +0.8% |
| Draw probability edge | +2.5% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -8.3% |
| Under 2.5 probability edge | +8.3% |
| Raw edge prob home | 0.0165 |
| Raw ev home | 0.0567 |
| Raw edge prob draw | 0.0508 |
| Raw ev draw | 0.1360 |
| Raw edge prob away | -0.0673 |
| Raw ev away | -0.1009 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **55.3%**. Expected goals are 1.43 for Tottenham Hotspur and 1.06 for Coventry City (2.49 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 47.4%; Under 3.5 goals: 75.4%; Double Chance 1X: 79.5%; Double Chance X2: 44.7%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 88.6%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 55.3% | 1.81 |
| Draw | 24.2% | 4.13 |
| Coventry City win | 20.5% | 4.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.43 |
| Coventry City expected goals | 1.06 |
| Expected total goals | 2.49 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 73.2% |
| Under 1.5 | 26.8% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 11.4% |
| Under 4.5 | 88.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.09% |
| 2 | 1-1 | 11.54% |
| 3 | 2-1 | 11.26% |
| 4 | 2-0 | 10.65% |
| 5 | 0-0 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 55.3% | 66.5% | 1.54 | -14.8% |
| Draw | 24.2% | 19.0% | 4.72 | +14.3% |
| Coventry City win | 20.5% | 14.5% | 6.47 | +32.5% |
| Over 2.5 | 47.4% | 60.9% | 1.64 | -22.3% |
| Under 2.5 | 52.6% | 39.1% | 2.46 | +29.5% |

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
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
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
| Fair Under 0.5 odds | 12.43 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.73 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 4.06 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.77 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 44.1% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 26.5% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 76.1% |
| Raw p btts yes | 51.1% |
| P home draw | 79.5% |
| P draw away | 44.7% |
| P home away | 75.8% |
| Raw p home draw | 73.5% |
| Raw p draw away | 55.9% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.47 |
| Reference draw odds | 4.80 |
| Reference away odds | 6.20 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | -11.2% |
| Draw probability edge | +5.2% |
| Away probability edge | +6.0% |
| Over 2.5 probability edge | -13.6% |
| Under 2.5 probability edge | +13.6% |
| Raw edge prob home | -0.2241 |
| Raw ev home | -0.3210 |
| Raw edge prob draw | 0.1043 |
| Raw ev draw | 0.3891 |
| Raw edge prob away | 0.1199 |
| Raw ev away | 0.7131 |

</details>


---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **46.0%**. Expected goals are 1.22 for Ipswich Town and 1.76 for Nottingham Forest (2.98 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 57.0%; Under 3.5 goals: 65.3%; Double Chance 1X: 54.0%; Double Chance X2: 72.3%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 27.7% | 3.60 |
| Draw | 26.3% | 3.81 |
| Nottingham Forest win | 46.0% | 2.17 |

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
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.31% |
| 2 | 1-2 | 9.02% |
| 3 | 0-2 | 7.41% |
| 4 | 2-1 | 7.32% |
| 5 | 0-1 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 27.7% | 30.4% | 3.10 | -14.0% |
| Draw | 26.3% | 26.6% | 3.63 | -4.6% |
| Nottingham Forest win | 46.0% | 43.0% | 2.39 | +9.9% |
| Over 2.5 | 57.0% | 53.6% | 1.84 | +5.0% |
| Under 2.5 | 43.0% | 46.4% | 2.12 | -8.9% |

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
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
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
| Fair Under 0.5 odds | 15.58 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.55 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 25.1% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 49.0% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 59.6% |
| P home draw | 54.0% |
| P draw away | 72.3% |
| P home away | 73.7% |
| Raw p home draw | 51.0% |
| Raw p draw away | 74.9% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -2.6% |
| Draw probability edge | -0.3% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | +3.4% |
| Under 2.5 probability edge | -3.4% |
| Raw edge prob home | -0.0527 |
| Raw ev home | -0.2216 |
| Raw edge prob draw | -0.0070 |
| Raw ev draw | -0.0588 |
| Raw edge prob away | 0.0597 |
| Raw ev away | 0.1702 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **67.5%**. Expected goals are 1.67 for Arsenal and 0.61 for Everton (2.28 combined). The most likely exact score is 1-0 at 17.3%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 41.6%; Under 3.5 goals: 79.7%; Double Chance 1X: 89.2%; Double Chance X2: 32.5%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 37.0%; BTTS No (at least one team does not score): 63.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 67.5% | 1.48 |
| Draw | 21.8% | 4.60 |
| Everton win | 10.8% | 9.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.67 |
| Everton expected goals | 0.61 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 68.6% |
| Under 1.5 | 31.4% |
| Over 2.5 | 41.6% |
| Under 2.5 | 58.4% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.31% |
| 2 | 2-0 | 15.56% |
| 3 | 1-1 | 9.70% |
| 4 | 0-0 | 9.58% |
| 5 | 2-1 | 9.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 67.5% | 72.8% | 1.43 | -3.5% |
| Draw | 21.8% | 17.5% | 4.93 | +7.2% |
| Everton win | 10.8% | 9.7% | 8.90 | -4.0% |
| Over 2.5 | 41.6% | 54.0% | 1.83 | -23.9% |
| Under 2.5 | 58.4% | 46.0% | 2.14 | +25.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:00:00+00:00 |
| Fixture id | f66e4f29c1b7bcfc5ab58c0b88c8850b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 37.0% |
| P btts no | 63.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.43 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.18 |
| Fair Over 2.5 odds | 2.40 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.92 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.63 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 62.1% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 11.9% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 38.1% |
| P home draw | 89.2% |
| P draw away | 32.5% |
| P home away | 78.2% |
| Raw p home draw | 88.1% |
| Raw p draw away | 37.9% |
| Raw p home away | 74.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.31 |
| Reference draw odds | 4.40 |
| Reference away odds | 7.30 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | -5.3% |
| Draw probability edge | +4.2% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -12.4% |
| Under 2.5 probability edge | +12.4% |
| Raw edge prob home | -0.1068 |
| Raw ev home | -0.1116 |
| Raw edge prob draw | 0.0845 |
| Raw ev draw | 0.2805 |
| Raw edge prob away | 0.0224 |
| Raw ev away | 0.0594 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **56.3%**. Expected goals are 1.09 for Aston Villa and 1.92 for Manchester City (3.00 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 58.2%; Under 3.5 goals: 64.5%; Double Chance 1X: 43.7%; Double Chance X2: 79.7%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 81.3%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 20.3% | 4.94 |
| Draw | 23.4% | 4.27 |
| Manchester City win | 56.3% | 1.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.09 |
| Manchester City expected goals | 1.92 |
| Expected total goals | 3.00 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 58.2% |
| Under 2.5 | 41.8% |
| Over 3.5 | 35.5% |
| Under 3.5 | 64.5% |
| Over 4.5 | 18.7% |
| Under 4.5 | 81.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.03% |
| 2 | 1-2 | 10.06% |
| 3 | 0-2 | 9.24% |
| 4 | 0-1 | 8.43% |
| 5 | 1-3 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 20.3% | 20.5% | 4.72 | -4.4% |
| Draw | 23.4% | 22.4% | 4.26 | -0.2% |
| Manchester City win | 56.3% | 57.2% | 1.76 | -0.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T11:30:00+00:00 |
| Fixture id | aca5dd297dbee71f576f7641569fe578 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.00 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.39 |
| Fair Over 2.5 odds | 1.72 |
| Fair Under 2.5 odds | 2.39 |
| Fair Over 3.5 odds | 2.82 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.34 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 20.0% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 55.5% |
| Raw p over 1 5 | 81.3% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 57.8% |
| P home draw | 43.7% |
| P draw away | 79.7% |
| P home away | 76.6% |
| Raw p home draw | 44.5% |
| Raw p draw away | 80.0% |
| Raw p home away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 4.00 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.63 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -0.2% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | -0.0042 |
| Raw ev home | -0.0540 |
| Raw edge prob draw | 0.0213 |
| Raw ev draw | 0.0435 |
| Raw edge prob away | -0.0171 |
| Raw ev away | -0.0239 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **55.8%**. Expected goals are 2.11 for Chelsea and 1.17 for Tottenham Hotspur (3.28 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 63.5%; Under 3.5 goals: 58.7%; Double Chance 1X: 78.6%; Double Chance X2: 44.2%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 76.8%; BTTS Yes (both teams score): 61.8%; BTTS No (at least one team does not score): 38.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 55.8% | 1.79 |
| Draw | 22.8% | 4.39 |
| Tottenham Hotspur win | 21.4% | 4.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.11 |
| Tottenham Hotspur expected goals | 1.17 |
| Expected total goals | 3.28 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 63.5% |
| Under 2.5 | 36.5% |
| Over 3.5 | 41.3% |
| Under 3.5 | 58.7% |
| Over 4.5 | 23.2% |
| Under 4.5 | 76.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.36% |
| 2 | 2-1 | 9.46% |
| 3 | 2-0 | 8.08% |
| 4 | 3-1 | 6.65% |
| 5 | 1-0 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 55.8% | 53.8% | 1.90 | +6.0% |
| Draw | 22.8% | 22.8% | 4.11 | -6.4% |
| Tottenham Hotspur win | 21.4% | 23.5% | 4.06 | -12.9% |
| Over 2.5 | 63.5% | 59.5% | 1.66 | +5.5% |
| Under 2.5 | 36.5% | 40.5% | 2.42 | -11.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0382a9faef0bb8df1bcc436536cffb05 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 6.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.8% |
| P btts no | 38.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.66 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.60 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.74 |
| Fair Over 3.5 odds | 2.42 |
| Fair Under 3.5 odds | 1.70 |
| Fair Over 4.5 odds | 4.30 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 57.8% |
| Unadjusted draw probability | 22.8% |
| Unadjusted away-win probability | 19.4% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 61.7% |
| P home draw | 78.6% |
| P draw away | 44.2% |
| P home away | 77.2% |
| Raw p home draw | 80.6% |
| Raw p draw away | 42.2% |
| Raw p home away | 77.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.73 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | +2.0% |
| Draw probability edge | +0.0% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +4.0% |
| Under 2.5 probability edge | -4.0% |
| Raw edge prob home | 0.0400 |
| Raw ev home | 0.0978 |
| Raw edge prob draw | 0.0004 |
| Raw ev draw | -0.0632 |
| Raw edge prob away | -0.0404 |
| Raw ev away | -0.2113 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **38.3%**. Expected goals are 1.13 for Coventry City and 1.17 for Fulham (2.30 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 41.4%; Under 3.5 goals: 79.7%; Double Chance 1X: 61.7%; Double Chance X2: 67.0%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 47.7%; BTTS No (at least one team does not score): 52.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 33.0% | 3.03 |
| Draw | 28.7% | 3.48 |
| Fulham win | 38.3% | 2.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.13 |
| Fulham expected goals | 1.17 |
| Expected total goals | 2.30 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 68.7% |
| Under 1.5 | 31.3% |
| Over 2.5 | 41.4% |
| Under 2.5 | 58.6% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.53% |
| 2 | 0-1 | 11.04% |
| 3 | 0-0 | 10.55% |
| 4 | 1-0 | 9.69% |
| 5 | 1-2 | 8.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 33.0% | 32.7% | 3.12 | +2.8% |
| Draw | 28.7% | 26.1% | 3.61 | +3.8% |
| Fulham win | 38.3% | 41.2% | 2.39 | -8.5% |
| Over 2.5 | 41.4% | 55.8% | 1.81 | -25.0% |
| Under 2.5 | 58.6% | 44.2% | 2.15 | +26.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:00:00+00:00 |
| Fixture id | 0fbb2626ed9534b9dcf21d16925f9bd7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T06:53:31Z |
| Market best draw last update utc | 2026-10-15T06:53:31Z |
| Market best away last update utc | 2026-10-15T06:53:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Fulham |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 47.7% |
| P btts no | 52.3% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.48 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.20 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.93 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.56 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 31.4% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.9% |
| Raw p btts yes | 48.3% |
| P home draw | 61.7% |
| P draw away | 67.0% |
| P home away | 71.3% |
| Raw p home draw | 64.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 68.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | +0.2% |
| Draw probability edge | +2.6% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -14.4% |
| Under 2.5 probability edge | +14.4% |
| Raw edge prob home | 0.0048 |
| Raw ev home | 0.0356 |
| Raw edge prob draw | 0.0530 |
| Raw ev draw | 0.1335 |
| Raw edge prob away | -0.0578 |
| Raw ev away | -0.1537 |

</details>


---
