# Premier League — football model report

Fixtures in this report: **20**.

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
| Training sha256 | 5e47fcac22b19c93fdbf5582097b19308a37c09cba726b46511adb6796b7a5ac |
| Optimizer objective | 897.623 |
| Base scoring parameter | 0.217 |
| Home-advantage parameter | 0.179 |
| Dixon-Coles low-score adjustment | -0.115 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 10.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 10.00 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Brentford win** at **39.6%**. Expected goals are 1.58 for Brentford and 1.48 for Liverpool (3.06 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 59.1%; Under 3.5 goals: 63.4%; Double Chance 1X: 65.9%; Double Chance X2: 60.4%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 80.5%; BTTS Yes (both teams score): 62.5%; BTTS No (at least one team does not score): 37.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 39.6% | 2.53 |
| Draw | 26.3% | 3.80 |
| Liverpool win | 34.1% | 2.93 |

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
| 1 | 1-1 | 12.13% |
| 2 | 2-1 | 8.81% |
| 3 | 1-2 | 8.01% |
| 4 | 2-2 | 6.35% |
| 5 | 1-0 | 6.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 39.6% | 40.2% | 2.51 | -0.6% |
| Draw | 26.3% | 26.1% | 3.73 | -1.9% |
| Liverpool win | 34.1% | 33.7% | 2.86 | -2.5% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Brentford |
| Matched away-team name | Liverpool |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.5% |
| P btts no | 37.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.93 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.63 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
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
| P home draw | 65.9% |
| P draw away | 60.4% |
| P home away | 73.7% |
| Raw p home draw | 65.5% |
| Raw p draw away | 61.0% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.38 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.82 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Home probability edge | -0.6% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | -0.0129 |
| Raw ev home | -0.0222 |
| Raw edge prob draw | 0.0046 |
| Raw ev draw | -0.0105 |
| Raw edge prob away | 0.0083 |
| Raw ev away | -0.0129 |
| Market p home draw | 65.5% |
| Market home draw odds | 1.48 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:14:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.0% |
| Market draw away odds | 1.59 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:14:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.5% |
| Market home away odds | 1.32 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:14:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.59 |
| Market reference dc home draw odds | 1.48 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 85.7% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:15:02Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:02Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.2% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:15:02Z |
| Market reference under 3 5 odds | 1.64 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:02Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.3% |
| Market btts yes odds | 1.46 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.82 |
| Market reference btts yes last update utc | 2026-10-16T22:14:53Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **39.6%**. Expected goals are 1.40 for Everton and 1.37 for Chelsea (2.76 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 52.6%; Under 3.5 goals: 70.0%; Double Chance 1X: 60.4%; Double Chance X2: 66.8%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 33.2% | 3.01 |
| Draw | 27.1% | 3.69 |
| Chelsea win | 39.6% | 2.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.40 |
| Chelsea expected goals | 1.37 |
| Expected total goals | 2.76 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.0% |
| Under 3.5 | 70.0% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.90% |
| 2 | 1-2 | 9.27% |
| 3 | 0-1 | 8.14% |
| 4 | 2-1 | 7.65% |
| 5 | 0-0 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 33.2% | 29.9% | 3.23 | +7.4% |
| Draw | 27.1% | 26.0% | 3.86 | +4.7% |
| Chelsea win | 39.6% | 44.1% | 2.24 | -11.2% |
| Over 2.5 | 52.6% | 59.2% | 1.73 | -9.0% |
| Under 2.5 | 47.4% | 40.8% | 2.28 | +8.1% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Everton |
| Matched away-team name | Chelsea |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.52 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.75 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 36.6% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 70.0% |
| Raw p btts yes | 57.5% |
| P home draw | 60.4% |
| P draw away | 66.8% |
| P home away | 72.9% |
| Raw p home draw | 64.8% |
| Raw p draw away | 63.4% |
| Raw p home away | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 3.15 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.18 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | +3.3% |
| Draw probability edge | +1.1% |
| Away probability edge | -4.4% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | 0.0663 |
| Raw ev home | 0.1808 |
| Raw edge prob draw | 0.0225 |
| Raw ev draw | 0.0905 |
| Raw edge prob away | -0.0888 |
| Raw ev away | -0.2117 |
| Market p home draw | 56.1% |
| Market home draw odds | 1.73 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:14:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.3% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:14:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.6% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:14:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home draw odds | 1.73 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 80.2% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:14:36Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.55 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.0% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:14:36Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.68 |
| Market reference under 3 5 last update utc | 2026-10-16T22:14:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.7% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.59 |
| Market reference btts yes opposite odds | 2.66 |
| Market reference btts yes last update utc | 2026-10-16T22:14:53Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.1%**. Expected goals are 0.94 for Fulham and 1.22 for Hull City (2.16 combined). The most likely exact score is 1-0 at 14.6%. Goal-market probabilities: at least one goal: 88.6%; Over 2.5 goals: 37.7%; Under 3.5 goals: 82.9%; Double Chance 1X: 70.2%; Double Chance X2: 57.9%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 93.0%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.1% | 2.38 |
| Draw | 28.2% | 3.55 |
| Hull City win | 29.8% | 3.36 |

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
| Over 2.5 | 37.7% |
| Under 2.5 | 62.3% |
| Over 3.5 | 17.1% |
| Under 3.5 | 82.9% |
| Over 4.5 | 7.0% |
| Under 4.5 | 93.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.57% |
| 2 | 1-1 | 12.94% |
| 3 | 0-0 | 11.44% |
| 4 | 2-1 | 9.73% |
| 5 | 0-1 | 9.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 42.1% | 57.2% | 1.77 | -25.5% |
| Draw | 28.2% | 24.2% | 4.05 | +14.1% |
| Hull City win | 29.8% | 18.6% | 4.93 | +46.7% |
| Over 2.5 | 37.7% | 54.6% | 1.81 | -31.7% |
| Under 2.5 | 62.3% | 45.4% | 2.17 | +35.1% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.9% |
| P btts no | 56.1% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.74 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.85 |
| Fair Over 2.5 odds | 2.65 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.84 |
| Fair Under 3.5 odds | 1.21 |
| Fair Over 4.5 odds | 14.31 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 32.1% |
| Unadjusted away-win probability | 40.9% |
| Raw p over 1 5 | 65.1% |
| Raw p under 3 5 | 82.7% |
| Raw p btts yes | 44.5% |
| P home draw | 70.2% |
| P draw away | 57.9% |
| P home away | 71.8% |
| Raw p home draw | 59.1% |
| Raw p draw away | 73.1% |
| Raw p home away | 67.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.70 |
| Reference draw odds | 3.85 |
| Reference away odds | 4.95 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | -15.1% |
| Draw probability edge | +4.0% |
| Away probability edge | +11.2% |
| Over 2.5 probability edge | -16.9% |
| Under 2.5 probability edge | +16.9% |
| Raw edge prob home | -0.3027 |
| Raw ev home | -0.5231 |
| Raw edge prob draw | 0.0792 |
| Raw ev draw | 0.3011 |
| Raw edge prob away | 0.2235 |
| Raw ev away | 1.0179 |
| Market p home draw | 79.5% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:14:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.7% |
| Market draw away odds | 2.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:14:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:14:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.17 |
| Market reference dc home draw odds | 1.22 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 80.5% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:15:04Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.96 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 68.4% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:15:04Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 2.72 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.1% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-16T22:14:53Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **83.3%**. Expected goals are 3.47 for Manchester City and 0.73 for Ipswich Town (4.20 combined). The most likely exact score is 3-0 at 10.1%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 77.8%; Under 3.5 goals: 40.7%; Double Chance 1X: 94.4%; Double Chance X2: 16.7%; Double Chance 12 (either team wins): 88.9%; Under 4.5 goals: 60.1%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 83.3% | 1.20 |
| Draw | 11.1% | 9.02 |
| Ipswich Town win | 5.6% | 17.90 |

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
| Over 2.5 | 77.8% |
| Under 2.5 | 22.2% |
| Over 3.5 | 59.3% |
| Under 3.5 | 40.7% |
| Over 4.5 | 39.9% |
| Under 4.5 | 60.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.06% |
| 2 | 4-0 | 8.72% |
| 3 | 2-0 | 8.70% |
| 4 | 3-1 | 7.31% |
| 5 | 4-1 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 83.3% | 79.8% | 1.29 | +7.5% |
| Draw | 11.1% | 12.8% | 6.85 | -24.0% |
| Ipswich Town win | 5.6% | 7.4% | 10.60 | -40.8% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man City |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.41 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.73 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.51 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.46 |
| Fair Over 4.5 odds | 2.50 |
| Fair Under 4.5 odds | 1.66 |
| Unadjusted home-win probability | 86.8% |
| Unadjusted draw probability | 9.4% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 92.6% |
| Raw p under 3 5 | 39.6% |
| Raw p btts yes | 50.5% |
| P home draw | 94.4% |
| P draw away | 16.7% |
| P home away | 88.9% |
| Raw p home draw | 96.2% |
| Raw p draw away | 13.2% |
| Raw p home away | 90.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.23 |
| Reference draw odds | 6.60 |
| Reference away odds | 11.00 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.05 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Home probability edge | +3.5% |
| Draw probability edge | -1.7% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +7.5% |
| Under 2.5 probability edge | -7.5% |
| Raw edge prob home | 0.0700 |
| Raw ev home | 0.1200 |
| Raw edge prob draw | -0.0346 |
| Raw ev draw | -0.3590 |
| Raw edge prob away | -0.0354 |
| Raw ev away | -0.5954 |
| Market p home draw | 91.1% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:14:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 24.3% |
| Market draw away odds | 3.98 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:14:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.7% |
| Market home away odds | 1.14 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:14:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.98 |
| Market reference dc home draw odds | 1.06 |
| Market reference dc home away odds | 1.14 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:14:13Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.80 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.2% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:14:13Z |
| Market reference under 3 5 odds | 1.86 |
| Market reference under 3 5 opposite odds | 2.02 |
| Market reference under 3 5 last update utc | 2026-10-16T22:14:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.4% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 2.18 |
| Market reference btts yes last update utc | 2026-10-16T22:14:53Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **42.5%**. Expected goals are 1.76 for Newcastle United and 1.53 for Aston Villa (3.28 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.4%; Double Chance 1X: 68.2%; Double Chance X2: 57.5%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 66.0%; BTTS No (at least one team does not score): 34.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 42.5% | 2.35 |
| Draw | 25.7% | 3.89 |
| Aston Villa win | 31.8% | 3.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.76 |
| Aston Villa expected goals | 1.53 |
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
| 1 | 1-1 | 11.41% |
| 2 | 2-1 | 8.89% |
| 3 | 1-2 | 7.51% |
| 4 | 2-2 | 6.86% |
| 5 | 2-0 | 5.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 42.5% | 42.8% | 2.26 | -3.9% |
| Draw | 25.7% | 26.1% | 3.85 | -1.1% |
| Aston Villa win | 31.8% | 31.1% | 3.19 | +1.4% |
| Over 2.5 | 63.6% | 60.2% | 1.67 | +6.1% |
| Under 2.5 | 36.4% | 39.8% | 2.40 | -12.5% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 66.0% |
| P btts no | 34.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.01 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.70 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.74 |
| Fair Over 3.5 odds | 2.41 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.28 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 32.5% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 58.4% |
| Raw p btts yes | 65.9% |
| P home draw | 68.2% |
| P draw away | 57.5% |
| P home away | 74.3% |
| Raw p home draw | 67.5% |
| Raw p draw away | 57.7% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.25 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | -0.2% |
| Draw probability edge | -0.4% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | +3.3% |
| Under 2.5 probability edge | -3.3% |
| Raw edge prob home | -0.0048 |
| Raw ev home | -0.0443 |
| Raw edge prob draw | -0.0088 |
| Raw ev draw | -0.0277 |
| Raw edge prob away | 0.0136 |
| Raw ev away | 0.0355 |
| Market p home draw | 68.4% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.4% |
| Market draw away odds | 1.71 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.2% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.68 |
| Market reference dc home draw odds | 1.41 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 82.1% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:14:38Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.9% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:14:38Z |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market reference under 3 5 last update utc | 2026-10-16T22:14:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.3% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.54 |
| Market reference btts yes opposite odds | 2.57 |
| Market reference btts yes last update utc | 2026-10-16T22:15:16Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **46.9%**. Expected goals are 1.59 for Bournemouth and 1.06 for Sunderland (2.65 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 49.4%; Under 3.5 goals: 72.6%; Double Chance 1X: 74.4%; Double Chance X2: 53.1%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 53.4%; BTTS No (at least one team does not score): 46.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 46.9% | 2.13 |
| Draw | 27.5% | 3.63 |
| Sunderland win | 25.6% | 3.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.59 |
| Sunderland expected goals | 1.06 |
| Expected total goals | 2.65 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 49.4% |
| Under 2.5 | 50.6% |
| Over 3.5 | 27.4% |
| Under 3.5 | 72.6% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.16% |
| 2 | 1-0 | 9.59% |
| 3 | 2-1 | 9.19% |
| 4 | 2-0 | 8.68% |
| 5 | 0-0 | 8.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 46.9% | 45.5% | 2.15 | +0.8% |
| Draw | 27.5% | 27.3% | 3.63 | -0.1% |
| Sunderland win | 25.6% | 27.3% | 3.63 | -7.1% |
| Over 2.5 | 49.4% | 52.3% | 1.96 | -3.2% |
| Under 2.5 | 50.6% | 47.7% | 1.98 | +0.2% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.4% |
| P btts no | 46.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.94 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.65 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.73 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 53.4% |
| P home draw | 74.4% |
| P draw away | 53.1% |
| P home away | 72.5% |
| Raw p home draw | 76.1% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.12 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | +1.4% |
| Draw probability edge | +0.3% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -2.9% |
| Under 2.5 probability edge | +2.9% |
| Raw edge prob home | 0.0287 |
| Raw ev home | 0.0390 |
| Raw edge prob draw | 0.0051 |
| Raw ev draw | 0.0086 |
| Raw edge prob away | -0.0338 |
| Raw ev away | -0.1328 |
| Market p home draw | 72.6% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:17Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.8% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:17Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:17Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.76 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 76.0% |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.77 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 71.5% |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.24 |
| Market reference under 3 5 last update utc | 2026-10-16T22:14:52Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 55.2% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.13 |
| Market reference btts yes last update utc | 2026-10-16T22:15:17Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **62.0%**. Expected goals are 2.00 for Brighton and Hove Albion and 1.02 for Crystal Palace (3.02 combined). The most likely exact score is 2-1 at 10.5%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.0%; Under 3.5 goals: 63.9%; Double Chance 1X: 83.8%; Double Chance X2: 38.0%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 62.0% | 1.61 |
| Draw | 21.8% | 4.59 |
| Crystal Palace win | 16.2% | 6.16 |

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
| Over 2.5 | 59.0% |
| Under 2.5 | 41.0% |
| Over 3.5 | 36.1% |
| Under 3.5 | 63.9% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.47% |
| 2 | 1-1 | 10.28% |
| 3 | 2-0 | 10.26% |
| 4 | 1-0 | 9.04% |
| 5 | 3-1 | 6.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 62.0% | 65.0% | 1.58 | -2.0% |
| Draw | 21.8% | 20.0% | 4.72 | +2.7% |
| Crystal Palace win | 16.2% | 14.9% | 5.80 | -5.9% |
| Over 2.5 | 59.0% | 62.5% | 1.63 | -3.9% |
| Under 2.5 | 41.0% | 37.5% | 2.49 | +2.2% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.94 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.51 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.20 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 59.0% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 17.5% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 56.5% |
| P home draw | 83.8% |
| P draw away | 38.0% |
| P home away | 78.2% |
| Raw p home draw | 82.5% |
| Raw p draw away | 41.0% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.50 |
| Reference draw odds | 4.55 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | -3.0% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | -0.0605 |
| Raw ev home | -0.0681 |
| Raw edge prob draw | 0.0347 |
| Raw ev draw | 0.1094 |
| Raw edge prob away | 0.0258 |
| Raw ev away | 0.0159 |
| Market p home draw | 83.7% |
| Market home draw odds | 1.17 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:17Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.8% |
| Market draw away odds | 2.54 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:17Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.6% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:17Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.64 |
| Market reference dc home draw odds | 1.16 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 83.6% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:43Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.5% |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.41 |
| Market reference under 3 5 last update utc | 2026-10-16T22:14:52Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.26 |
| Market reference btts yes last update utc | 2026-10-16T22:15:17Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **39.7%**. Expected goals are 1.42 for Leeds United and 1.28 for Manchester United (2.70 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 50.8%; Under 3.5 goals: 71.4%; Double Chance 1X: 67.6%; Double Chance X2: 60.3%; Double Chance 12 (either team wins): 72.1%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 56.0%; BTTS No (at least one team does not score): 44.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 39.7% | 2.52 |
| Draw | 27.9% | 3.58 |
| Manchester United win | 32.4% | 3.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.28 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 76.6% |
| Under 1.5 | 23.4% |
| Over 2.5 | 50.8% |
| Under 2.5 | 49.2% |
| Over 3.5 | 28.6% |
| Under 3.5 | 71.4% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.31% |
| 2 | 2-1 | 8.87% |
| 3 | 1-0 | 8.33% |
| 4 | 0-0 | 7.95% |
| 5 | 1-2 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 39.7% | 40.7% | 2.42 | -3.8% |
| Draw | 27.9% | 27.2% | 3.69 | +2.9% |
| Manchester United win | 32.4% | 32.1% | 3.01 | -2.6% |
| Over 2.5 | 50.8% | 58.0% | 1.71 | -13.1% |
| Under 2.5 | 49.2% | 42.0% | 2.32 | +14.1% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 56.0% |
| P btts no | 44.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.58 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.27 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.27 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 76.5% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 56.1% |
| P home draw | 67.6% |
| P draw away | 60.3% |
| P home away | 72.1% |
| Raw p home draw | 67.4% |
| Raw p draw away | 61.2% |
| Raw p home away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.35 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | -1.0% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -7.2% |
| Under 2.5 probability edge | +7.2% |
| Raw edge prob home | -0.0196 |
| Raw ev home | -0.0619 |
| Raw edge prob draw | 0.0139 |
| Raw ev draw | 0.0549 |
| Raw edge prob away | 0.0058 |
| Raw ev away | -0.0173 |
| Market p home draw | 66.9% |
| Market home draw odds | 1.44 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.4% |
| Market draw away odds | 1.63 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.7% |
| Market home away odds | 1.32 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.45 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 80.2% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:14:35Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.55 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.5% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:14:35Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.72 |
| Market reference under 3 5 last update utc | 2026-10-16T22:14:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.8% |
| Market btts yes odds | 1.52 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.34 |
| Market reference btts yes last update utc | 2026-10-16T22:15:07Z |
| Market btts yes bookmakers | 1 |

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
| Nottingham Forest win | 16.5% | 15.6% | 5.80 | -4.5% |
| Draw | 26.0% | 23.5% | 3.90 | +1.4% |
| Arsenal win | 57.5% | 60.9% | 1.71 | -1.6% |
| Over 2.5 | 41.2% | 49.4% | 1.99 | -18.0% |
| Under 2.5 | 58.8% | 50.6% | 1.95 | +14.6% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
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
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 5.80 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.60 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | +0.8% |
| Draw probability edge | +2.5% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -8.2% |
| Under 2.5 probability edge | +8.2% |
| Raw edge prob home | 0.0165 |
| Raw ev home | 0.0031 |
| Raw edge prob draw | 0.0508 |
| Raw ev draw | 0.1132 |
| Raw edge prob away | -0.0673 |
| Raw ev away | -0.0738 |
| Market p home draw | 42.5% |
| Market home draw odds | 2.28 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:14:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 82.9% |
| Market draw away odds | 1.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:14:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.6% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:14:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.17 |
| Market reference dc home draw odds | 2.28 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 75.6% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:15:08Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.34 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.7% |
| Market under 3 5 odds | 1.30 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:15:08Z |
| Market reference under 3 5 odds | 1.30 |
| Market reference under 3 5 opposite odds | 3.14 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:08Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 49.5% |
| Market btts yes odds | 1.87 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 2.00 |
| Market reference btts yes opposite odds | 1.96 |
| Market reference btts yes last update utc | 2026-10-16T22:14:53Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **55.1%**. Expected goals are 1.43 for Tottenham Hotspur and 1.06 for Coventry City (2.49 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 47.3%; Under 3.5 goals: 75.4%; Double Chance 1X: 79.5%; Double Chance X2: 44.9%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 88.6%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 55.1% | 1.82 |
| Draw | 24.5% | 4.09 |
| Coventry City win | 20.5% | 4.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.43 |
| Coventry City expected goals | 1.06 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 73.1% |
| Under 1.5 | 26.9% |
| Over 2.5 | 47.3% |
| Under 2.5 | 52.7% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 11.4% |
| Under 4.5 | 88.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.04% |
| 2 | 1-1 | 11.67% |
| 3 | 2-1 | 11.21% |
| 4 | 2-0 | 10.60% |
| 5 | 0-0 | 8.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 55.1% | 66.0% | 1.54 | -15.2% |
| Draw | 24.5% | 19.5% | 4.72 | +15.5% |
| Coventry City win | 20.5% | 14.5% | 6.47 | +32.5% |
| Over 2.5 | 47.3% | 61.9% | 1.64 | -22.5% |
| Under 2.5 | 52.7% | 38.1% | 2.46 | +29.7% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.7% |
| P btts no | 50.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.30 |
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
| P home draw | 79.5% |
| P draw away | 44.9% |
| P home away | 75.5% |
| Raw p home draw | 73.5% |
| Raw p draw away | 55.9% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.49 |
| Reference draw odds | 4.80 |
| Reference away odds | 6.40 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:07Z |
| Market reference home last update utc | 2026-10-16T22:15:07Z |
| Market reference draw last update utc | 2026-10-16T22:15:07Z |
| Market reference away last update utc | 2026-10-16T22:15:07Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | -11.0% |
| Draw probability edge | +5.0% |
| Away probability edge | +6.0% |
| Over 2.5 probability edge | -14.7% |
| Under 2.5 probability edge | +14.7% |
| Raw edge prob home | -0.2192 |
| Raw ev home | -0.3210 |
| Raw edge prob draw | 0.0991 |
| Raw ev draw | 0.3891 |
| Raw edge prob away | 0.1201 |
| Raw ev away | 0.7131 |
| Market p home draw | 80.6% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 41.6% |
| Market draw away odds | 2.65 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.8% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.13 |
| Market reference dc home draw odds | 1.10 |
| Market reference dc home away odds | 1.14 |
| Market p over 1 5 | 82.8% |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 5.10 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:43Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.6% |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.47 |
| Market reference under 3 5 last update utc | 2026-10-16T22:14:52Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 55.0% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.03 |
| Market reference btts yes last update utc | 2026-10-16T22:15:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **45.8%**. Expected goals are 1.22 for Ipswich Town and 1.76 for Nottingham Forest (2.98 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 57.1%; Under 3.5 goals: 65.4%; Double Chance 1X: 54.2%; Double Chance X2: 71.9%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 28.1% | 3.56 |
| Draw | 26.1% | 3.83 |
| Nottingham Forest win | 45.8% | 2.18 |

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
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.6% |
| Under 3.5 | 65.4% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.24% |
| 2 | 1-2 | 8.99% |
| 3 | 2-1 | 7.41% |
| 4 | 0-2 | 7.39% |
| 5 | 0-1 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 28.1% | 31.0% | 3.10 | -13.0% |
| Draw | 26.1% | 26.3% | 3.63 | -5.2% |
| Nottingham Forest win | 45.8% | 42.7% | 2.39 | +9.5% |
| Over 2.5 | 57.1% | 55.2% | 1.84 | +5.1% |
| Under 2.5 | 42.9% | 44.8% | 2.12 | -9.0% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.68 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.54 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 25.1% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 49.0% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 59.6% |
| P home draw | 54.2% |
| P draw away | 71.9% |
| P home away | 73.9% |
| Raw p home draw | 51.0% |
| Raw p draw away | 74.9% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 3.05 |
| Reference draw odds | 3.57 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.11 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | -3.0% |
| Draw probability edge | -0.2% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | +1.9% |
| Under 2.5 probability edge | -1.9% |
| Raw edge prob home | -0.0591 |
| Raw ev home | -0.2216 |
| Raw edge prob draw | -0.0037 |
| Raw ev draw | -0.0588 |
| Raw edge prob away | 0.0627 |
| Raw ev away | 0.1702 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **66.2%**. Expected goals are 1.67 for Arsenal and 0.61 for Everton (2.28 combined). The most likely exact score is 1-0 at 17.0%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.8%; Double Chance 1X: 89.0%; Double Chance X2: 33.8%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 37.2%; BTTS No (at least one team does not score): 62.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 66.2% | 1.51 |
| Draw | 22.8% | 4.39 |
| Everton win | 11.0% | 9.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.67 |
| Everton expected goals | 0.61 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 68.3% |
| Under 1.5 | 31.7% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.99% |
| 2 | 2-0 | 15.27% |
| 3 | 1-1 | 10.17% |
| 4 | 0-0 | 10.05% |
| 5 | 2-1 | 9.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 66.2% | 70.3% | 1.43 | -5.3% |
| Draw | 22.8% | 19.6% | 4.93 | +12.4% |
| Everton win | 11.0% | 10.0% | 8.90 | -2.4% |
| Over 2.5 | 41.2% | 53.2% | 1.83 | -24.7% |
| Under 2.5 | 58.8% | 46.8% | 2.14 | +25.9% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 37.2% |
| P btts no | 62.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.95 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.16 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.96 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.78 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 62.1% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 11.9% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 38.1% |
| P home draw | 89.0% |
| P draw away | 33.8% |
| P home away | 77.2% |
| Raw p home draw | 88.1% |
| Raw p draw away | 37.9% |
| Raw p home away | 74.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.39 |
| Reference draw odds | 4.59 |
| Reference away odds | 8.61 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.03 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | -4.1% |
| Draw probability edge | +3.2% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -12.0% |
| Under 2.5 probability edge | +12.0% |
| Raw edge prob home | -0.0822 |
| Raw ev home | -0.1116 |
| Raw edge prob draw | 0.0634 |
| Raw ev draw | 0.2805 |
| Raw edge prob away | 0.0188 |
| Raw ev away | 0.0594 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **56.3%**. Expected goals are 1.09 for Aston Villa and 1.92 for Manchester City (3.00 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 58.2%; Under 3.5 goals: 64.5%; Double Chance 1X: 43.7%; Double Chance X2: 79.8%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 81.3%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 20.2% | 4.96 |
| Draw | 23.5% | 4.25 |
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
| 1 | 1-1 | 11.08% |
| 2 | 1-2 | 10.05% |
| 3 | 0-2 | 9.23% |
| 4 | 0-1 | 8.43% |
| 5 | 1-3 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 20.2% | 20.3% | 4.72 | -4.8% |
| Draw | 23.5% | 22.6% | 4.26 | +0.2% |
| Manchester City win | 56.3% | 57.1% | 1.76 | -0.9% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.93 |
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
| P draw away | 79.8% |
| P home away | 76.5% |
| Raw p home draw | 44.5% |
| Raw p draw away | 80.0% |
| Raw p home away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 4.53 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Home probability edge | -0.1% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | -0.0027 |
| Raw ev home | -0.0540 |
| Raw edge prob draw | 0.0193 |
| Raw ev draw | 0.0435 |
| Raw edge prob away | -0.0167 |
| Raw ev away | -0.0239 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **55.5%**. Expected goals are 2.11 for Chelsea and 1.17 for Tottenham Hotspur (3.28 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 63.4%; Under 3.5 goals: 58.8%; Double Chance 1X: 78.7%; Double Chance X2: 44.5%; Double Chance 12 (either team wins): 76.8%; Under 4.5 goals: 76.8%; BTTS Yes (both teams score): 61.9%; BTTS No (at least one team does not score): 38.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 55.5% | 1.80 |
| Draw | 23.2% | 4.32 |
| Tottenham Hotspur win | 21.3% | 4.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.11 |
| Tottenham Hotspur expected goals | 1.17 |
| Expected total goals | 3.28 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 63.4% |
| Under 2.5 | 36.6% |
| Over 3.5 | 41.2% |
| Under 3.5 | 58.8% |
| Over 4.5 | 23.2% |
| Under 4.5 | 76.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.54% |
| 2 | 2-1 | 9.41% |
| 3 | 2-0 | 8.04% |
| 4 | 3-1 | 6.61% |
| 5 | 1-0 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 55.5% | 53.2% | 1.90 | +5.5% |
| Draw | 23.2% | 23.5% | 4.11 | -4.8% |
| Tottenham Hotspur win | 21.3% | 23.2% | 4.06 | -13.4% |
| Over 2.5 | 63.4% | 62.2% | 1.66 | +5.2% |
| Under 2.5 | 36.6% | 37.8% | 2.42 | -11.4% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.9% |
| P btts no | 38.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.31 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.58 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.73 |
| Fair Over 3.5 odds | 2.42 |
| Fair Under 3.5 odds | 1.70 |
| Fair Over 4.5 odds | 4.32 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 57.8% |
| Unadjusted draw probability | 22.8% |
| Unadjusted away-win probability | 19.4% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 61.7% |
| P home draw | 78.7% |
| P draw away | 44.5% |
| P home away | 76.8% |
| Raw p home draw | 80.6% |
| Raw p draw away | 42.2% |
| Raw p home away | 77.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.82 |
| Reference draw odds | 3.95 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | +2.3% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | 0.0455 |
| Raw ev home | 0.0979 |
| Raw edge prob draw | -0.0075 |
| Raw ev draw | -0.0632 |
| Raw edge prob away | -0.0381 |
| Raw ev away | -0.2113 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **38.2%**. Expected goals are 1.13 for Coventry City and 1.17 for Fulham (2.30 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.7%; Double Chance 1X: 61.8%; Double Chance X2: 67.2%; Double Chance 12 (either team wins): 71.0%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 32.8% | 3.05 |
| Draw | 29.0% | 3.44 |
| Fulham win | 38.2% | 2.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.13 |
| Fulham expected goals | 1.17 |
| Expected total goals | 2.30 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 68.7% |
| Under 1.5 | 31.3% |
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.67% |
| 2 | 0-1 | 11.01% |
| 3 | 0-0 | 10.66% |
| 4 | 1-0 | 9.63% |
| 5 | 1-2 | 8.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 32.8% | 32.4% | 3.12 | +2.2% |
| Draw | 29.0% | 26.7% | 3.61 | +4.8% |
| Fulham win | 38.2% | 41.0% | 2.39 | -8.7% |
| Over 2.5 | 41.3% | 55.6% | 1.81 | -25.2% |
| Under 2.5 | 58.7% | 44.4% | 2.15 | +26.2% |

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
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.38 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.93 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.59 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 31.4% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.9% |
| Raw p btts yes | 48.3% |
| P home draw | 61.8% |
| P draw away | 67.2% |
| P home away | 71.0% |
| Raw p home draw | 64.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 68.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.93 |
| Reference draw odds | 3.52 |
| Reference away odds | 2.34 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | +0.4% |
| Draw probability edge | +2.4% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -14.2% |
| Under 2.5 probability edge | +14.2% |
| Raw edge prob home | 0.0084 |
| Raw ev home | 0.0356 |
| Raw edge prob draw | 0.0471 |
| Raw ev draw | 0.1334 |
| Raw edge prob away | -0.0555 |
| Raw ev away | -0.1537 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **37.2%**. Expected goals are 1.56 for Crystal Palace and 1.57 for Newcastle United (3.12 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 60.2%; Under 3.5 goals: 62.0%; Double Chance 1X: 62.8%; Double Chance X2: 63.9%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 63.8%; BTTS No (at least one team does not score): 36.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 36.1% | 2.77 |
| Draw | 26.7% | 3.75 |
| Newcastle United win | 37.2% | 2.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.56 |
| Newcastle United expected goals | 1.57 |
| Expected total goals | 3.12 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 60.2% |
| Under 2.5 | 39.8% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.17% |
| 2 | 1-2 | 8.43% |
| 3 | 2-1 | 8.23% |
| 4 | 2-2 | 6.66% |
| 5 | 0-0 | 5.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 36.1% | 35.6% | 2.76 | -0.3% |
| Draw | 26.7% | 27.1% | 3.69 | -1.6% |
| Newcastle United win | 37.2% | 37.3% | 2.61 | -2.9% |
| Over 2.5 | 60.2% | 60.1% | 1.69 | +1.8% |
| Under 2.5 | 39.8% | 39.9% | 2.36 | -6.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | fe235b26408c477368c40672a4488694 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 63.8% |
| P btts no | 36.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.45 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.91 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.87 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 36.7% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 37.1% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 61.9% |
| Raw p btts yes | 63.7% |
| P home draw | 62.8% |
| P draw away | 63.9% |
| P home away | 73.3% |
| Raw p home draw | 62.9% |
| Raw p draw away | 63.3% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.68 |
| Reference draw odds | 3.47 |
| Reference away odds | 2.56 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | +0.6% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0112 |
| Raw ev home | 0.0124 |
| Raw edge prob draw | -0.0090 |
| Raw ev draw | -0.0324 |
| Raw edge prob away | -0.0022 |
| Raw ev away | -0.0318 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **41.6%**. Expected goals are 1.40 for Hull City and 1.05 for Brentford (2.46 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 45.2%; Under 3.5 goals: 77.0%; Double Chance 1X: 58.4%; Double Chance X2: 68.5%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 31.5% | 3.18 |
| Draw | 26.9% | 3.71 |
| Brentford win | 41.6% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.40 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.46 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 71.5% |
| Under 1.5 | 28.5% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.0% |
| Under 3.5 | 77.0% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.81% |
| 2 | 0-1 | 11.76% |
| 3 | 1-2 | 10.37% |
| 4 | 0-0 | 9.10% |
| 5 | 1-0 | 7.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 31.5% | 19.4% | 4.72 | +48.6% |
| Draw | 26.9% | 24.2% | 4.09 | +10.1% |
| Brentford win | 41.6% | 56.5% | 1.79 | -25.5% |
| Over 2.5 | 45.2% | 55.4% | 1.73 | -21.8% |
| Under 2.5 | 54.8% | 44.6% | 2.28 | +25.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 69493b5ebb84f24ab1d6023a30ee89f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.99 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.51 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.36 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.63 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 43.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 50.6% |
| P home draw | 58.4% |
| P draw away | 68.5% |
| P home away | 73.1% |
| Raw p home draw | 73.3% |
| Raw p draw away | 56.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 4.75 |
| Reference draw odds | 3.85 |
| Reference away odds | 1.72 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | +12.1% |
| Draw probability edge | +2.8% |
| Away probability edge | -14.9% |
| Over 2.5 probability edge | -10.2% |
| Under 2.5 probability edge | +10.2% |
| Raw edge prob home | 0.2423 |
| Raw ev home | 1.0578 |
| Raw edge prob draw | 0.0552 |
| Raw ev draw | 0.2142 |
| Raw edge prob away | -0.2976 |
| Raw ev away | -0.5218 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **44.5%**. Expected goals are 1.63 for Liverpool and 1.43 for Brighton and Hove Albion (3.06 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 59.4%; Under 3.5 goals: 63.3%; Double Chance 1X: 69.8%; Double Chance X2: 55.5%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 62.1%; BTTS No (at least one team does not score): 37.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 44.5% | 2.25 |
| Draw | 25.3% | 3.95 |
| Brighton and Hove Albion win | 30.2% | 3.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.63 |
| Brighton and Hove Albion expected goals | 1.43 |
| Expected total goals | 3.06 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 82.3% |
| Under 1.5 | 17.7% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 36.7% |
| Under 3.5 | 63.3% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.69% |
| 2 | 2-1 | 9.62% |
| 3 | 1-2 | 7.28% |
| 4 | 1-0 | 6.90% |
| 5 | 2-0 | 6.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 44.5% | 47.7% | 2.11 | -6.2% |
| Draw | 25.3% | 24.2% | 4.00 | +1.3% |
| Brighton and Hove Albion win | 30.2% | 28.0% | 3.43 | +3.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 290ba8cd3f3a2e9252effca673bf5549 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.1% |
| P btts no | 37.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.52 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.66 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.72 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.08 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 41.2% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 62.4% |
| P home draw | 69.8% |
| P draw away | 55.5% |
| P home away | 74.7% |
| Raw p home draw | 67.6% |
| Raw p draw away | 58.8% |
| Raw p home away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.02 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.35 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Home probability edge | -3.3% |
| Draw probability edge | +1.1% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0653 |
| Raw ev home | -0.1305 |
| Raw edge prob draw | 0.0220 |
| Raw ev draw | 0.0570 |
| Raw edge prob away | 0.0433 |
| Raw ev away | 0.1102 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **50.7%**. Expected goals are 1.79 for Manchester United and 1.28 for Bournemouth (3.08 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 59.9%; Under 3.5 goals: 62.8%; Double Chance 1X: 75.0%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 79.9%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 50.7% | 1.97 |
| Draw | 24.3% | 4.11 |
| Bournemouth win | 25.0% | 4.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.79 |
| Bournemouth expected goals | 1.28 |
| Expected total goals | 3.08 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 82.6% |
| Under 1.5 | 17.4% |
| Over 2.5 | 59.9% |
| Under 2.5 | 40.1% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 20.1% |
| Under 4.5 | 79.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.25% |
| 2 | 2-1 | 10.01% |
| 3 | 2-0 | 7.80% |
| 4 | 1-0 | 7.41% |
| 5 | 1-2 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 50.7% | 53.2% | 1.86 | -5.7% |
| Draw | 24.3% | 23.0% | 4.26 | +3.6% |
| Bournemouth win | 25.0% | 23.7% | 4.11 | +2.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 33fb7467b23c91d57dc976d9ab05ea97 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.04 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.74 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 4.99 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 48.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 26.2% |
| Raw p over 1 5 | 82.4% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 61.5% |
| P home draw | 75.0% |
| P draw away | 49.3% |
| P home away | 75.7% |
| Raw p home draw | 73.8% |
| Raw p draw away | 51.8% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.82 |
| Reference draw odds | 4.03 |
| Reference away odds | 3.92 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.73 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.0503 |
| Raw ev home | -0.1035 |
| Raw edge prob draw | 0.0254 |
| Raw ev draw | 0.0898 |
| Raw edge prob away | 0.0249 |
| Raw ev away | 0.0775 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **37.5%**. Expected goals are 1.08 for Sunderland and 1.23 for Leeds United (2.31 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 41.0%; Under 3.5 goals: 79.7%; Double Chance 1X: 62.5%; Double Chance X2: 67.5%; Double Chance 12 (either team wins): 70.0%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 32.5% | 3.07 |
| Draw | 30.0% | 3.33 |
| Leeds United win | 37.5% | 2.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.08 |
| Leeds United expected goals | 1.23 |
| Expected total goals | 2.31 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 68.7% |
| Under 1.5 | 31.3% |
| Over 2.5 | 41.0% |
| Under 2.5 | 59.0% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.12% |
| 2 | 0-0 | 11.00% |
| 3 | 0-1 | 10.55% |
| 4 | 1-0 | 9.75% |
| 5 | 1-2 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 32.5% | 34.3% | 2.90 | -5.7% |
| Draw | 30.0% | 28.7% | 3.44 | +3.2% |
| Leeds United win | 37.5% | 37.0% | 2.63 | -1.4% |
| Over 2.5 | 41.0% | 46.8% | 2.14 | -12.2% |
| Under 2.5 | 59.0% | 53.2% | 1.83 | +7.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | e82f6b60fa41b82c8510f5b67ce61849 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.09 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.93 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.66 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 30.8% |
| Unadjusted draw probability | 31.3% |
| Unadjusted away-win probability | 37.9% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.8% |
| Raw p btts yes | 48.2% |
| P home draw | 62.5% |
| P draw away | 67.5% |
| P home away | 70.0% |
| Raw p home draw | 62.1% |
| Raw p draw away | 69.2% |
| Raw p home away | 68.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.78 |
| Reference draw odds | 3.29 |
| Reference away odds | 2.58 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:06Z |
| Market reference home last update utc | 2026-10-16T22:15:06Z |
| Market reference draw last update utc | 2026-10-16T22:15:06Z |
| Market reference away last update utc | 2026-10-16T22:15:06Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.80 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:06Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | -1.7% |
| Draw probability edge | +1.3% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | -0.0345 |
| Raw ev home | -0.1068 |
| Raw edge prob draw | 0.0255 |
| Raw ev draw | 0.0755 |
| Raw edge prob away | 0.0090 |
| Raw ev away | -0.0023 |

</details>


---
