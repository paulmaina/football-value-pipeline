# Premier League — football model report

Fixtures in this report: **19**.

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
| Training sha256 | 55d1951271ab7b6fe97dac4b7c997367d53f528828c576b121d9c0b42d15be3a |
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
| Live odds matched | 19.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
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

The model's most likely 1X2 outcome is **Brentford win** at **39.2%**. Expected goals are 1.58 for Brentford and 1.48 for Liverpool (3.06 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 59.1%; Under 3.5 goals: 63.4%; Double Chance 1X: 65.5%; Double Chance X2: 60.8%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 80.5%; BTTS Yes (both teams score): 62.5%; BTTS No (at least one team does not score): 37.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 39.2% | 2.55 |
| Draw | 26.3% | 3.80 |
| Liverpool win | 34.5% | 2.90 |

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
| 2 | 2-1 | 8.73% |
| 3 | 1-2 | 8.09% |
| 4 | 2-2 | 6.35% |
| 5 | 1-0 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 39.2% | 39.5% | 2.51 | -1.5% |
| Draw | 26.3% | 26.1% | 3.74 | -1.6% |
| Liverpool win | 34.5% | 34.4% | 2.87 | -1.1% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
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
| P home draw | 65.5% |
| P draw away | 60.8% |
| P home away | 73.7% |
| Raw p home draw | 65.5% |
| Raw p draw away | 61.0% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.44 |
| Reference draw odds | 3.64 |
| Reference away odds | 2.79 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:44Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:44Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0058 |
| Raw ev home | -0.0222 |
| Raw edge prob draw | 0.0045 |
| Raw ev draw | -0.0078 |
| Raw edge prob away | 0.0012 |
| Raw ev away | -0.0095 |
| Market p home draw | 65.6% |
| Market home draw odds | 1.48 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:08Z |
| Market reference home draw last update utc | 2026-10-15T15:32:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.7% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:08Z |
| Market reference draw away last update utc | 2026-10-15T15:32:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.7% |
| Market home away odds | 1.32 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:08Z |
| Market reference home away last update utc | 2026-10-15T15:32:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.59 |
| Market reference dc home draw odds | 1.47 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:24Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.6% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:24Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.47 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:00Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.4% |
| Market btts yes odds | 1.46 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:08Z |
| Market reference btts yes odds | 1.54 |
| Market reference btts yes opposite odds | 2.76 |
| Market reference btts yes last update utc | 2026-10-15T15:32:00Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **39.9%**. Expected goals are 1.40 for Everton and 1.37 for Chelsea (2.76 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 52.8%; Under 3.5 goals: 69.9%; Double Chance 1X: 60.1%; Double Chance X2: 66.6%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 33.4% | 2.99 |
| Draw | 26.7% | 3.75 |
| Chelsea win | 39.9% | 2.51 |

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
| Over 2.5 | 52.8% |
| Under 2.5 | 47.2% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.67% |
| 2 | 1-2 | 9.33% |
| 3 | 0-1 | 8.20% |
| 4 | 2-1 | 7.69% |
| 5 | 0-0 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 33.4% | 30.3% | 3.23 | +8.0% |
| Draw | 26.7% | 25.1% | 3.88 | +3.4% |
| Chelsea win | 39.9% | 44.6% | 2.23 | -11.0% |
| Over 2.5 | 52.8% | 57.3% | 1.73 | -8.7% |
| Under 2.5 | 47.2% | 42.7% | 2.28 | +7.7% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.76 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.32 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.72 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 36.6% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 70.0% |
| Raw p btts yes | 57.5% |
| P home draw | 60.1% |
| P draw away | 66.6% |
| P home away | 73.3% |
| Raw p home draw | 64.8% |
| Raw p draw away | 63.4% |
| Raw p home away | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.15 |
| Reference draw odds | 3.78 |
| Reference away odds | 2.17 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | +3.1% |
| Draw probability edge | +1.6% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | 0.0626 |
| Raw ev home | 0.1808 |
| Raw edge prob draw | 0.0319 |
| Raw ev draw | 0.0962 |
| Raw edge prob away | -0.0946 |
| Raw ev away | -0.2153 |
| Market p home draw | 55.9% |
| Market home draw odds | 1.73 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:08Z |
| Market reference home draw last update utc | 2026-10-15T15:32:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.6% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:08Z |
| Market reference draw away last update utc | 2026-10-15T15:32:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.5% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:08Z |
| Market reference home away last update utc | 2026-10-15T15:32:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home draw odds | 1.72 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:19Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.2% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:19Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.76 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:00Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.2% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:08Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.54 |
| Market reference btts yes last update utc | 2026-10-15T15:32:00Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **41.8%**. Expected goals are 0.94 for Fulham and 1.22 for Hull City (2.16 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 88.6%; Over 2.5 goals: 37.8%; Under 3.5 goals: 82.9%; Double Chance 1X: 69.8%; Double Chance X2: 58.2%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 93.0%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 41.8% | 2.39 |
| Draw | 28.0% | 3.57 |
| Hull City win | 30.2% | 3.31 |

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
| 1 | 1-0 | 14.49% |
| 2 | 1-1 | 12.86% |
| 3 | 0-0 | 11.37% |
| 4 | 2-1 | 9.68% |
| 5 | 0-1 | 9.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 41.8% | 56.7% | 1.77 | -25.9% |
| Draw | 28.0% | 23.9% | 4.05 | +13.4% |
| Hull City win | 30.2% | 19.4% | 4.93 | +48.7% |
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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| Fair Under 0.5 odds | 8.79 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.85 |
| Fair Over 2.5 odds | 2.64 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.84 |
| Fair Under 3.5 odds | 1.21 |
| Fair Over 4.5 odds | 14.27 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 32.1% |
| Unadjusted away-win probability | 40.9% |
| Raw p over 1 5 | 65.1% |
| Raw p under 3 5 | 82.7% |
| Raw p btts yes | 44.5% |
| P home draw | 69.8% |
| P draw away | 58.2% |
| P home away | 72.0% |
| Raw p home draw | 59.1% |
| Raw p draw away | 73.1% |
| Raw p home away | 67.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.72 |
| Reference draw odds | 3.94 |
| Reference away odds | 4.80 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | -14.9% |
| Draw probability edge | +4.1% |
| Away probability edge | +10.8% |
| Over 2.5 probability edge | -17.1% |
| Under 2.5 probability edge | +17.1% |
| Raw edge prob home | -0.2979 |
| Raw ev home | -0.5231 |
| Raw edge prob draw | 0.0827 |
| Raw ev draw | 0.3011 |
| Raw edge prob away | 0.2152 |
| Raw ev away | 1.0179 |
| Market p home draw | 76.1% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:08Z |
| Market reference home draw last update utc | 2026-10-15T15:32:09Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.7% |
| Market draw away odds | 2.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:08Z |
| Market reference draw away last update utc | 2026-10-15T15:32:09Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.2% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:08Z |
| Market reference home away last update utc | 2026-10-15T15:32:09Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.79 |
| Market reference dc home draw odds | 1.17 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 79.6% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:41Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 68.3% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:41Z |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 2.94 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:00Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.2% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:08Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 2.09 |
| Market reference btts yes last update utc | 2026-10-15T15:32:13Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **83.2%**. Expected goals are 3.47 for Manchester City and 0.73 for Ipswich Town (4.20 combined). The most likely exact score is 3-0 at 10.0%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 77.8%; Under 3.5 goals: 40.7%; Double Chance 1X: 94.2%; Double Chance X2: 16.8%; Double Chance 12 (either team wins): 88.9%; Under 4.5 goals: 60.1%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 83.2% | 1.20 |
| Draw | 11.1% | 9.05 |
| Ipswich Town win | 5.8% | 17.29 |

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
| 1 | 3-0 | 10.04% |
| 2 | 4-0 | 8.70% |
| 3 | 2-0 | 8.68% |
| 4 | 3-1 | 7.29% |
| 5 | 4-1 | 6.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 83.2% | 79.5% | 1.26 | +4.8% |
| Draw | 11.1% | 12.7% | 7.26 | -19.8% |
| Ipswich Town win | 5.8% | 7.8% | 11.50 | -33.5% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.55 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.70 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.51 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.45 |
| Fair Over 4.5 odds | 2.51 |
| Fair Under 4.5 odds | 1.66 |
| Unadjusted home-win probability | 86.8% |
| Unadjusted draw probability | 9.4% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 92.6% |
| Raw p under 3 5 | 39.6% |
| Raw p btts yes | 50.5% |
| P home draw | 94.2% |
| P draw away | 16.8% |
| P home away | 88.9% |
| Raw p home draw | 96.2% |
| Raw p draw away | 13.2% |
| Raw p home away | 90.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.24 |
| Reference draw odds | 6.90 |
| Reference away odds | 11.00 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:43Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:43Z |
| Home probability edge | +3.7% |
| Draw probability edge | -1.7% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +6.7% |
| Under 2.5 probability edge | -6.7% |
| Raw edge prob home | 0.0732 |
| Raw ev home | 0.0940 |
| Raw edge prob draw | -0.0339 |
| Raw ev draw | -0.3206 |
| Raw edge prob away | -0.0393 |
| Raw ev away | -0.5610 |
| Market p home draw | 91.2% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:08Z |
| Market reference home draw last update utc | 2026-10-15T15:32:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.5% |
| Market draw away odds | 4.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:08Z |
| Market reference draw away last update utc | 2026-10-15T15:32:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.3% |
| Market home away odds | 1.13 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:08Z |
| Market reference home away last update utc | 2026-10-15T15:32:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.25 |
| Market reference dc home draw odds | 1.05 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:40Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.95 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:40Z |
| Market reference under 3 5 odds | 1.88 |
| Market reference under 3 5 opposite odds | 1.99 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:00Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.2% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:08Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-15T15:32:00Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **43.1%**. Expected goals are 1.76 for Newcastle United and 1.52 for Aston Villa (3.28 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 63.7%; Under 3.5 goals: 58.4%; Double Chance 1X: 68.4%; Double Chance X2: 56.9%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 65.9%; BTTS No (at least one team does not score): 34.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 43.1% | 2.32 |
| Draw | 25.2% | 3.96 |
| Aston Villa win | 31.6% | 3.16 |

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
| 1 | 1-1 | 11.21% |
| 2 | 2-1 | 9.02% |
| 3 | 1-2 | 7.47% |
| 4 | 2-2 | 6.74% |
| 5 | 2-0 | 5.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 43.1% | 44.0% | 2.26 | -2.5% |
| Draw | 25.2% | 25.2% | 3.85 | -2.8% |
| Aston Villa win | 31.6% | 30.8% | 3.19 | +0.9% |
| Over 2.5 | 63.7% | 59.6% | 1.67 | +6.4% |
| Under 2.5 | 36.3% | 40.4% | 2.40 | -12.9% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| P btts yes | 65.9% |
| P btts no | 34.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.36 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.71 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.76 |
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
| P home draw | 68.4% |
| P draw away | 56.9% |
| P home away | 74.8% |
| Raw p home draw | 67.5% |
| Raw p draw away | 57.7% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.20 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | -0.9% |
| Draw probability edge | +0.0% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +4.1% |
| Under 2.5 probability edge | -4.1% |
| Raw edge prob home | -0.0170 |
| Raw ev home | -0.0444 |
| Raw edge prob draw | 0.0002 |
| Raw ev draw | -0.0277 |
| Raw edge prob away | 0.0169 |
| Raw ev away | 0.0355 |
| Market p home draw | 67.8% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:08Z |
| Market reference home draw last update utc | 2026-10-15T15:32:08Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.0% |
| Market draw away odds | 1.71 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:08Z |
| Market reference draw away last update utc | 2026-10-15T15:32:08Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.2% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:08Z |
| Market reference home away last update utc | 2026-10-15T15:32:08Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.48 |
| Market reference dc home draw odds | 1.31 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 82.7% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:41Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.4% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:41Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.52 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:00Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.3% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:08Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.43 |
| Market reference btts yes last update utc | 2026-10-15T15:32:08Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.8%**. Expected goals are 1.59 for Bournemouth and 1.06 for Sunderland (2.65 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 49.6%; Under 3.5 goals: 72.5%; Double Chance 1X: 74.9%; Double Chance X2: 52.2%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 53.2%; BTTS No (at least one team does not score): 46.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.8% | 2.09 |
| Draw | 27.1% | 3.70 |
| Sunderland win | 25.1% | 3.98 |

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
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 27.5% |
| Under 3.5 | 72.5% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.93% |
| 2 | 1-0 | 9.78% |
| 3 | 2-1 | 9.37% |
| 4 | 2-0 | 8.86% |
| 5 | 0-0 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.8% | 47.3% | 2.11 | +0.9% |
| Draw | 27.1% | 26.3% | 3.70 | +0.1% |
| Sunderland win | 25.1% | 26.3% | 3.70 | -7.1% |
| Over 2.5 | 49.6% | 52.2% | 1.89 | -6.2% |
| Under 2.5 | 50.4% | 47.8% | 2.05 | +3.3% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| P btts yes | 53.2% |
| P btts no | 46.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.15 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.09 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.68 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 53.4% |
| P home draw | 74.9% |
| P draw away | 52.2% |
| P home away | 72.9% |
| Raw p home draw | 76.1% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.05 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.99 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | +0.5% |
| Draw probability edge | +0.7% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -2.6% |
| Under 2.5 probability edge | +2.6% |
| Raw edge prob home | 0.0099 |
| Raw ev home | 0.0197 |
| Raw edge prob draw | 0.0146 |
| Raw ev draw | 0.0281 |
| Raw edge prob away | -0.0244 |
| Raw ev away | -0.1161 |
| Market p home draw | 73.3% |
| Market home draw odds | 1.32 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.4% |
| Market draw away odds | 1.81 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.3% |
| Market home away odds | 1.32 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.81 |
| Market reference dc home draw odds | 1.32 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 77.3% |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.94 |
| Market reference over 1 5 last update utc | 2026-10-15T15:32:00Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 70.3% |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.10 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:00Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 56.8% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-15T15:32:16Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **60.3%**. Expected goals are 2.00 for Brighton and Hove Albion and 1.02 for Crystal Palace (3.02 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 58.7%; Under 3.5 goals: 64.1%; Double Chance 1X: 82.5%; Double Chance X2: 39.7%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 60.3% | 1.66 |
| Draw | 22.2% | 4.50 |
| Crystal Palace win | 17.5% | 5.72 |

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
| Over 3.5 | 35.9% |
| Under 3.5 | 64.1% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.50% |
| 2 | 2-1 | 10.17% |
| 3 | 2-0 | 9.97% |
| 4 | 1-0 | 8.79% |
| 5 | 3-1 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 60.3% | 61.6% | 1.63 | -1.8% |
| Draw | 22.2% | 21.0% | 4.57 | +1.6% |
| Crystal Palace win | 17.5% | 17.5% | 5.44 | -4.8% |
| Over 2.5 | 58.7% | 61.2% | 1.63 | -4.3% |
| Under 2.5 | 41.3% | 38.8% | 2.49 | +2.8% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
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
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.56 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.46 |
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
| P home draw | 82.5% |
| P draw away | 39.7% |
| P home away | 77.8% |
| Raw p home draw | 82.5% |
| Raw p draw away | 41.0% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.59 |
| Reference draw odds | 4.45 |
| Reference away odds | 5.30 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.41 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | -1.3% |
| Draw probability edge | +1.3% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0258 |
| Raw ev home | -0.0386 |
| Raw edge prob draw | 0.0253 |
| Raw ev draw | 0.0742 |
| Raw edge prob away | 0.0005 |
| Raw ev away | -0.0472 |
| Market p home draw | 81.6% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.1% |
| Market draw away odds | 2.42 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.3% |
| Market home away odds | 1.24 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.42 |
| Market reference dc home draw odds | 1.19 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:43Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.0% |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.49 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:00Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.7% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-15T15:32:16Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **39.8%**. Expected goals are 1.42 for Leeds United and 1.28 for Manchester United (2.70 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.4%; Double Chance 1X: 67.3%; Double Chance X2: 60.2%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 39.8% | 2.51 |
| Draw | 27.5% | 3.64 |
| Manchester United win | 32.7% | 3.06 |

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
| 1 | 1-1 | 13.11% |
| 2 | 2-1 | 8.89% |
| 3 | 1-0 | 8.35% |
| 4 | 1-2 | 7.84% |
| 5 | 0-0 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 39.8% | 40.9% | 2.42 | -3.6% |
| Draw | 27.5% | 26.4% | 3.69 | +1.4% |
| Manchester United win | 32.7% | 32.7% | 3.01 | -1.7% |
| Over 2.5 | 51.0% | 58.1% | 1.71 | -12.8% |
| Under 2.5 | 49.0% | 41.9% | 2.32 | +13.7% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.76 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.27 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.24 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 76.5% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 56.1% |
| P home draw | 67.3% |
| P draw away | 60.2% |
| P home away | 72.5% |
| Raw p home draw | 67.4% |
| Raw p draw away | 61.2% |
| Raw p home away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.36 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.93 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | -1.1% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | -0.0217 |
| Raw ev home | -0.0619 |
| Raw edge prob draw | 0.0221 |
| Raw ev draw | 0.0550 |
| Raw edge prob away | -0.0004 |
| Raw ev away | -0.0173 |
| Market p home draw | 67.2% |
| Market home draw odds | 1.44 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.4% |
| Market draw away odds | 1.63 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.4% |
| Market home away odds | 1.32 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.63 |
| Market reference dc home draw odds | 1.44 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 82.5% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:30:30Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.8% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:30:30Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:00Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.5% |
| Market btts yes odds | 1.52 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-15T15:32:16Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **57.3%**. Expected goals are 0.76 for Nottingham Forest and 1.53 for Arsenal (2.29 combined). The most likely exact score is 0-1 at 14.9%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 41.1%; Under 3.5 goals: 79.8%; Double Chance 1X: 42.7%; Double Chance X2: 83.6%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 42.6%; BTTS No (at least one team does not score): 57.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.4% | 6.11 |
| Draw | 26.4% | 3.79 |
| Arsenal win | 57.3% | 1.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.76 |
| Arsenal expected goals | 1.53 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 68.5% |
| Under 1.5 | 31.5% |
| Over 2.5 | 41.1% |
| Under 2.5 | 58.9% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.89% |
| 2 | 0-2 | 12.48% |
| 3 | 1-1 | 12.15% |
| 4 | 0-0 | 10.59% |
| 5 | 1-2 | 9.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.4% | 15.5% | 6.11 | +0.1% |
| Draw | 26.4% | 24.2% | 3.98 | +4.9% |
| Arsenal win | 57.3% | 60.4% | 1.66 | -5.0% |
| Over 2.5 | 41.1% | 50.0% | 1.97 | -19.1% |
| Under 2.5 | 58.9% | 50.0% | 1.97 | +16.1% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| P btts yes | 42.6% |
| P btts no | 57.4% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.44 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.95 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.72 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 54.2% |
| Raw p over 1 5 | 68.1% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 43.2% |
| P home draw | 42.7% |
| P draw away | 83.6% |
| P home away | 73.6% |
| Raw p home draw | 45.8% |
| Raw p draw away | 82.7% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 5.95 |
| Reference draw odds | 3.88 |
| Reference away odds | 1.62 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | +0.9% |
| Draw probability edge | +2.2% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | 0.0183 |
| Raw ev home | 0.0567 |
| Raw edge prob draw | 0.0435 |
| Raw ev draw | 0.1360 |
| Raw edge prob away | -0.0619 |
| Raw ev away | -0.1009 |
| Market p home draw | 41.3% |
| Market home draw odds | 2.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:16Z |
| Market reference home draw last update utc | 2026-10-15T15:32:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.6% |
| Market draw away odds | 1.16 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:16Z |
| Market reference draw away last update utc | 2026-10-15T15:32:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:16Z |
| Market reference home away last update utc | 2026-10-15T15:32:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home draw odds | 2.35 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 75.5% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:15Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market reference over 1 5 last update utc | 2026-10-15T15:32:00Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.0% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:15Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.28 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:00Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 49.4% |
| Market btts yes odds | 1.88 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:16Z |
| Market reference btts yes odds | 1.88 |
| Market reference btts yes opposite odds | 1.84 |
| Market reference btts yes last update utc | 2026-10-15T15:32:16Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **54.7%**. Expected goals are 1.43 for Tottenham Hotspur and 1.06 for Coventry City (2.49 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 47.2%; Under 3.5 goals: 75.4%; Double Chance 1X: 79.5%; Double Chance X2: 45.3%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 49.8%; BTTS No (at least one team does not score): 50.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 54.7% | 1.83 |
| Draw | 24.8% | 4.03 |
| Coventry City win | 20.5% | 4.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.43 |
| Coventry City expected goals | 1.06 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 73.1% |
| Under 1.5 | 26.9% |
| Over 2.5 | 47.2% |
| Under 2.5 | 52.8% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 11.3% |
| Under 4.5 | 88.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.96% |
| 2 | 1-1 | 11.82% |
| 3 | 2-1 | 11.15% |
| 4 | 2-0 | 10.54% |
| 5 | 0-0 | 8.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 54.7% | 65.3% | 1.54 | -15.7% |
| Draw | 24.8% | 20.2% | 4.72 | +17.0% |
| Coventry City win | 20.5% | 14.5% | 6.47 | +32.5% |
| Over 2.5 | 47.2% | 60.8% | 1.64 | -22.7% |
| Under 2.5 | 52.8% | 39.2% | 2.46 | +30.0% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
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
| P btts yes | 49.8% |
| P btts no | 50.2% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.14 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.72 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 4.07 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.83 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 44.1% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 26.5% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 76.1% |
| Raw p btts yes | 51.1% |
| P home draw | 79.5% |
| P draw away | 45.3% |
| P home away | 75.2% |
| Raw p home draw | 73.5% |
| Raw p draw away | 55.9% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.50 |
| Reference draw odds | 4.60 |
| Reference away odds | 6.30 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | -10.6% |
| Draw probability edge | +4.6% |
| Away probability edge | +6.0% |
| Over 2.5 probability edge | -13.6% |
| Under 2.5 probability edge | +13.6% |
| Raw edge prob home | -0.2125 |
| Raw ev home | -0.3210 |
| Raw edge prob draw | 0.0927 |
| Raw ev draw | 0.3891 |
| Raw edge prob away | 0.1198 |
| Raw ev away | 0.7131 |

</details>


---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **45.2%**. Expected goals are 1.22 for Ipswich Town and 1.76 for Nottingham Forest (2.98 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 57.0%; Under 3.5 goals: 65.4%; Double Chance 1X: 54.8%; Double Chance X2: 71.6%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 28.4% | 3.52 |
| Draw | 26.4% | 3.79 |
| Nottingham Forest win | 45.2% | 2.21 |

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
| 1 | 1-1 | 12.37% |
| 2 | 1-2 | 8.87% |
| 3 | 2-1 | 7.49% |
| 4 | 0-2 | 7.29% |
| 5 | 0-1 | 7.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 28.4% | 31.7% | 3.10 | -12.0% |
| Draw | 26.4% | 26.8% | 3.63 | -4.2% |
| Nottingham Forest win | 45.2% | 41.5% | 2.39 | +8.1% |
| Over 2.5 | 57.0% | 53.9% | 1.84 | +4.8% |
| Under 2.5 | 43.0% | 46.1% | 2.12 | -8.8% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.52 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.23 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.32 |
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
| P home draw | 54.8% |
| P draw away | 71.6% |
| P home away | 73.6% |
| Raw p home draw | 51.0% |
| Raw p draw away | 74.9% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.02 |
| Reference draw odds | 3.54 |
| Reference away odds | 2.33 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | -3.3% |
| Draw probability edge | -0.5% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | +3.1% |
| Under 2.5 probability edge | -3.1% |
| Raw edge prob home | -0.0656 |
| Raw ev home | -0.2216 |
| Raw edge prob draw | -0.0092 |
| Raw ev draw | -0.0588 |
| Raw edge prob away | 0.0748 |
| Raw ev away | 0.1702 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **66.4%**. Expected goals are 1.67 for Arsenal and 0.61 for Everton (2.28 combined). The most likely exact score is 1-0 at 17.0%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.8%; Double Chance 1X: 88.9%; Double Chance X2: 33.6%; Double Chance 12 (either team wins): 77.5%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 37.2%; BTTS No (at least one team does not score): 62.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 66.4% | 1.51 |
| Draw | 22.5% | 4.43 |
| Everton win | 11.1% | 9.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.67 |
| Everton expected goals | 0.61 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 68.4% |
| Under 1.5 | 31.6% |
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.03% |
| 2 | 2-0 | 15.31% |
| 3 | 1-1 | 10.05% |
| 4 | 0-0 | 9.94% |
| 5 | 2-1 | 9.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 66.4% | 70.7% | 1.43 | -5.1% |
| Draw | 22.5% | 19.1% | 4.93 | +11.2% |
| Everton win | 11.1% | 10.2% | 8.90 | -1.6% |
| Over 2.5 | 41.3% | 54.2% | 1.83 | -24.5% |
| Under 2.5 | 58.7% | 45.8% | 2.14 | +25.7% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| Fair Under 0.5 odds | 10.06 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.16 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.96 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.76 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 62.1% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 11.9% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 38.1% |
| P home draw | 88.9% |
| P draw away | 33.6% |
| P home away | 77.5% |
| Raw p home draw | 88.1% |
| Raw p draw away | 37.9% |
| Raw p home away | 74.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.39 |
| Reference draw odds | 4.80 |
| Reference away odds | 8.70 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | -4.3% |
| Draw probability edge | +3.4% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -12.9% |
| Under 2.5 probability edge | +12.9% |
| Raw edge prob home | -0.0854 |
| Raw ev home | -0.1116 |
| Raw edge prob draw | 0.0685 |
| Raw ev draw | 0.2805 |
| Raw edge prob away | 0.0169 |
| Raw ev away | 0.0594 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **56.3%**. Expected goals are 1.09 for Aston Villa and 1.92 for Manchester City (3.00 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 58.2%; Under 3.5 goals: 64.5%; Double Chance 1X: 43.7%; Double Chance X2: 79.8%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 81.3%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 20.2% | 4.96 |
| Draw | 23.6% | 4.25 |
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
| 1 | 1-1 | 11.09% |
| 2 | 1-2 | 10.05% |
| 3 | 0-2 | 9.23% |
| 4 | 0-1 | 8.43% |
| 5 | 1-3 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 20.2% | 20.3% | 4.72 | -4.8% |
| Draw | 23.6% | 22.6% | 4.26 | +0.3% |
| Manchester City win | 56.3% | 57.1% | 1.76 | -1.0% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| Fair Under 0.5 odds | 16.91 |
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
| P home away | 76.4% |
| Raw p home draw | 44.5% |
| Raw p draw away | 80.0% |
| Raw p home away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.60 |
| Reference draw odds | 4.15 |
| Reference away odds | 1.71 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:43Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:43Z |
| Home probability edge | -0.1% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | -0.0026 |
| Raw ev home | -0.0540 |
| Raw edge prob draw | 0.0189 |
| Raw ev draw | 0.0435 |
| Raw edge prob away | -0.0163 |
| Raw ev away | -0.0239 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **55.2%**. Expected goals are 2.11 for Chelsea and 1.17 for Tottenham Hotspur (3.28 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 63.4%; Under 3.5 goals: 58.8%; Double Chance 1X: 78.4%; Double Chance X2: 44.8%; Double Chance 12 (either team wins): 76.8%; Under 4.5 goals: 76.9%; BTTS Yes (both teams score): 61.9%; BTTS No (at least one team does not score): 38.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 55.2% | 1.81 |
| Draw | 23.2% | 4.32 |
| Tottenham Hotspur win | 21.6% | 4.62 |

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
| Over 4.5 | 23.1% |
| Under 4.5 | 76.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.54% |
| 2 | 2-1 | 9.36% |
| 3 | 2-0 | 8.00% |
| 4 | 3-1 | 6.58% |
| 5 | 1-0 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 55.2% | 52.6% | 1.90 | +4.9% |
| Draw | 23.2% | 23.5% | 4.11 | -4.8% |
| Tottenham Hotspur win | 21.6% | 23.8% | 4.06 | -12.2% |
| Over 2.5 | 63.4% | 60.0% | 1.66 | +5.2% |
| Under 2.5 | 36.6% | 40.0% | 2.42 | -11.4% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| Fair Over 3.5 odds | 2.43 |
| Fair Under 3.5 odds | 1.70 |
| Fair Over 4.5 odds | 4.32 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 57.8% |
| Unadjusted draw probability | 22.8% |
| Unadjusted away-win probability | 19.4% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 61.7% |
| P home draw | 78.4% |
| P draw away | 44.8% |
| P home away | 76.8% |
| Raw p home draw | 80.6% |
| Raw p draw away | 42.2% |
| Raw p home away | 77.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.85 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.95 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | +2.6% |
| Draw probability edge | -0.4% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +3.4% |
| Under 2.5 probability edge | -3.4% |
| Raw edge prob home | 0.0516 |
| Raw ev home | 0.0978 |
| Raw edge prob draw | -0.0074 |
| Raw ev draw | -0.0632 |
| Raw edge prob away | -0.0442 |
| Raw ev away | -0.2113 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **38.5%**. Expected goals are 1.13 for Coventry City and 1.17 for Fulham (2.30 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.7%; Double Chance 1X: 61.5%; Double Chance X2: 67.7%; Double Chance 12 (either team wins): 70.8%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 32.3% | 3.09 |
| Draw | 29.2% | 3.42 |
| Fulham win | 38.5% | 2.60 |

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
| 1 | 1-1 | 13.75% |
| 2 | 0-1 | 11.08% |
| 3 | 0-0 | 10.72% |
| 4 | 1-0 | 9.50% |
| 5 | 1-2 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 32.3% | 31.5% | 3.12 | +0.9% |
| Draw | 29.2% | 27.0% | 3.61 | +5.5% |
| Fulham win | 38.5% | 41.5% | 2.39 | -8.1% |
| Over 2.5 | 41.3% | 54.6% | 1.81 | -25.3% |
| Under 2.5 | 58.7% | 45.4% | 2.15 | +26.3% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| Fair Under 0.5 odds | 9.33 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.94 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.61 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 31.4% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.9% |
| Raw p btts yes | 48.3% |
| P home draw | 61.5% |
| P draw away | 67.7% |
| P home away | 70.8% |
| Raw p home draw | 64.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 68.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.04 |
| Reference draw odds | 3.52 |
| Reference away odds | 2.33 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | +0.9% |
| Draw probability edge | +2.2% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -13.3% |
| Under 2.5 probability edge | +13.3% |
| Raw edge prob home | 0.0172 |
| Raw ev home | 0.0356 |
| Raw edge prob draw | 0.0437 |
| Raw ev draw | 0.1335 |
| Raw edge prob away | -0.0609 |
| Raw ev away | -0.1537 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **37.5%**. Expected goals are 1.56 for Crystal Palace and 1.57 for Newcastle United (3.12 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 60.4%; Under 3.5 goals: 61.9%; Double Chance 1X: 62.5%; Double Chance X2: 63.8%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 63.7%; BTTS No (at least one team does not score): 36.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 36.2% | 2.76 |
| Draw | 26.3% | 3.80 |
| Newcastle United win | 37.5% | 2.67 |

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
| Over 2.5 | 60.4% |
| Under 2.5 | 39.6% |
| Over 3.5 | 38.1% |
| Under 3.5 | 61.9% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.00% |
| 2 | 1-2 | 8.50% |
| 3 | 2-1 | 8.24% |
| 4 | 2-2 | 6.57% |
| 5 | 0-1 | 5.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 36.2% | 35.7% | 2.76 | -0.1% |
| Draw | 26.3% | 26.4% | 3.69 | -3.0% |
| Newcastle United win | 37.5% | 37.9% | 2.61 | -2.1% |
| Over 2.5 | 60.4% | 58.9% | 1.69 | +2.1% |
| Under 2.5 | 39.6% | 41.1% | 2.36 | -6.5% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| P btts yes | 63.7% |
| P btts no | 36.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.70 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.92 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 36.7% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 37.1% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 61.9% |
| Raw p btts yes | 63.7% |
| P home draw | 62.5% |
| P draw away | 63.8% |
| P home away | 73.7% |
| Raw p home draw | 62.9% |
| Raw p draw away | 63.3% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.69 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.54 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.29 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | +0.5% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +1.5% |
| Under 2.5 probability edge | -1.5% |
| Raw edge prob home | 0.0097 |
| Raw ev home | 0.0124 |
| Raw edge prob draw | -0.0015 |
| Raw ev draw | -0.0324 |
| Raw edge prob away | -0.0082 |
| Raw ev away | -0.0318 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **41.4%**. Expected goals are 1.40 for Hull City and 1.05 for Brentford (2.46 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 45.3%; Under 3.5 goals: 77.0%; Double Chance 1X: 58.6%; Double Chance X2: 68.0%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 32.0% | 3.13 |
| Draw | 26.7% | 3.75 |
| Brentford win | 41.4% | 2.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.40 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 71.5% |
| Under 1.5 | 28.5% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 23.0% |
| Under 3.5 | 77.0% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.69% |
| 2 | 0-1 | 11.70% |
| 3 | 1-2 | 10.32% |
| 4 | 0-0 | 9.01% |
| 5 | 1-0 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 32.0% | 20.3% | 4.72 | +50.8% |
| Draw | 26.7% | 23.6% | 4.09 | +9.0% |
| Brentford win | 41.4% | 56.1% | 1.79 | -25.9% |
| Over 2.5 | 45.3% | 57.3% | 1.73 | -21.6% |
| Under 2.5 | 54.7% | 42.7% | 2.28 | +24.7% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| Fair Under 0.5 odds | 11.10 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.51 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.35 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.60 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 43.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 50.6% |
| P home draw | 58.6% |
| P draw away | 68.0% |
| P home away | 73.3% |
| Raw p home draw | 73.3% |
| Raw p draw away | 56.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.60 |
| Reference draw odds | 3.98 |
| Reference away odds | 1.74 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:08Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:08Z |
| Home probability edge | +11.6% |
| Draw probability edge | +3.0% |
| Away probability edge | -14.7% |
| Over 2.5 probability edge | -12.0% |
| Under 2.5 probability edge | +12.0% |
| Raw edge prob home | 0.2329 |
| Raw ev home | 1.0578 |
| Raw edge prob draw | 0.0606 |
| Raw ev draw | 0.2142 |
| Raw edge prob away | -0.2935 |
| Raw ev away | -0.5218 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **44.3%**. Expected goals are 1.63 for Liverpool and 1.43 for Brighton and Hove Albion (3.06 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 59.4%; Under 3.5 goals: 63.3%; Double Chance 1X: 69.6%; Double Chance X2: 55.7%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 62.1%; BTTS No (at least one team does not score): 37.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 44.3% | 2.26 |
| Draw | 25.3% | 3.95 |
| Brighton and Hove Albion win | 30.4% | 3.29 |

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
| 1 | 1-1 | 11.68% |
| 2 | 2-1 | 9.58% |
| 3 | 1-2 | 7.33% |
| 4 | 1-0 | 6.87% |
| 5 | 2-0 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 44.3% | 47.3% | 2.11 | -6.6% |
| Draw | 25.3% | 24.2% | 4.00 | +1.3% |
| Brighton and Hove Albion win | 30.4% | 28.5% | 3.43 | +4.3% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| Fair Under 1.5 odds | 5.65 |
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
| P home draw | 69.6% |
| P draw away | 55.7% |
| P home away | 74.7% |
| Raw p home draw | 67.6% |
| Raw p draw away | 58.8% |
| Raw p home away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.05 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.34 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:43Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:43Z |
| Home probability edge | -3.1% |
| Draw probability edge | +1.1% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | -0.0612 |
| Raw ev home | -0.1305 |
| Raw edge prob draw | 0.0221 |
| Raw ev draw | 0.0570 |
| Raw edge prob away | 0.0391 |
| Raw ev away | 0.1102 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **51.0%**. Expected goals are 1.79 for Manchester United and 1.28 for Bournemouth (3.08 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 60.0%; Under 3.5 goals: 62.8%; Double Chance 1X: 75.1%; Double Chance X2: 49.0%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 79.9%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 51.0% | 1.96 |
| Draw | 24.1% | 4.15 |
| Bournemouth win | 24.9% | 4.02 |

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
| Over 2.5 | 60.0% |
| Under 2.5 | 40.0% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 20.1% |
| Under 4.5 | 79.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.15% |
| 2 | 2-1 | 10.07% |
| 3 | 2-0 | 7.85% |
| 4 | 1-0 | 7.45% |
| 5 | 1-2 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 51.0% | 53.8% | 1.86 | -5.1% |
| Draw | 24.1% | 22.6% | 4.26 | +2.7% |
| Bournemouth win | 24.9% | 23.5% | 4.11 | +2.2% |

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
| Market best home last update utc | 2026-10-15T15:31:08Z |
| Market best draw last update utc | 2026-10-15T15:31:08Z |
| Market best away last update utc | 2026-10-15T15:31:08Z |
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
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.19 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.75 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 4.98 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 48.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 26.2% |
| Raw p over 1 5 | 82.4% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 61.5% |
| P home draw | 75.1% |
| P draw away | 49.0% |
| P home away | 75.9% |
| Raw p home draw | 73.8% |
| Raw p draw away | 51.8% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.81 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:05Z |
| Market reference home last update utc | 2026-10-15T15:32:05Z |
| Market reference draw last update utc | 2026-10-15T15:32:05Z |
| Market reference away last update utc | 2026-10-15T15:32:05Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-15T15:31:43Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:31:43Z |
| Home probability edge | -2.8% |
| Draw probability edge | +1.5% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.0563 |
| Raw ev home | -0.1035 |
| Raw edge prob draw | 0.0294 |
| Raw ev draw | 0.0898 |
| Raw edge prob away | 0.0269 |
| Raw ev away | 0.0775 |

</details>


---
